# 🌐 Performant Web Applications

Python enables you to rapidly built backend applications using frameworks like Django, Flask, and FastAPI, but these can struggle to scale to intensive loads and high numbers of requests. Fortunately, there are some useful optimisation tricks, to do with database queuing, caching, and async processing. 

Here's an overview of some strategies for each framework, along with relevant code examples.

## Django Optimisation

**Database queries and indexing**: Use `select_related()` for forward `ForeignKey` relationships to reduce the number of database queries. Use `prefetch_related()` for many-to-many and reverse `ForeignKey` relationships:

```python
# Without optimisation
books = Book.objects.all()
for book in books:
    print(book.author.name)  # Each iteration hits the database

# With select_related
books = Book.objects.select_related('author').all()
for book in books:
    print(book.author.name)  # No additional database queries
```

Also, consider adding indexes to your models for fields that are frequently queried:

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100, db_index=True)
```

**Caching**: Use Django’s cache framework to cache views, query sets, or template fragments:

```python
from django.core.cache import cache

def my_view(request):
    if cache.get('my_key'):
        return cache.get('my_key')
    else:
        result = expensive_query()
        cache.set('my_key', result, 60)  # Cache for 60 seconds
        return result
```

And consider template fragment caching to cache parts of templates that are expensive to render:

```python
{% load cache %}
{% cache 600 sidebar %}
    ... expensive calculations here ...
{% endcache %}
```

**Middleware, query, and static file optimisation**: Reduce middleware classes that are not necessary for your project and consider using Django Debug Toolbar to identify and optimise slow queries. GZipMiddleware can compresses responses (for browsers that support `gzip`), while WhiteNoise or a similar tool can serve static files directly from WSGI and apply cache control headers.

## Flask Optimisation

**Database queries**: You can use SQLAlchemy or another ORM and apply similar strategies to those seen in the Django section above. Optimise queries by joining tables only when necessary and filtering queries as much as possible:

```python
from myapp import db
from myapp.models import User, Post

posts = Post.query.join(User).filter(Post.user_id == User.id).all()
```

**Caching**: Use `flask_caching` to cache views or data:

```python
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})
app = Flask(__name__)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=50)
def index():
    return expensive_function()
```

**Asynchronous views**: Try using Flask’s built-in support for async views to handle I/O-bound operations efficiently.

```python
@app.route('/async')
async def async_view():
    await asyncio.sleep(1)  # Simulate async I/O operation
    return 'This is an async view'
```

**Profiling and monitoring**: You can use Flask extensions like Flask-DebugToolbar to monitor performance bottlenecks.

**Use efficient WSGI servers**: Deploy Flask applications using efficient WSGI servers like Gunicorn or uWSGI instead of the built-in Flask server for production environments.

## FastAPI Optimisation

**Asynchronous and concurrent handling**: FastAPI is built to be asynchronous, so use async and await for I/O-bound operations, including database operations:

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/async")
async def read_async():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://example.com')
        return response.text
```

**Database queries**: Again, use packages like TortoiseORM or SQLAlchemy with async support to optimise database interactions. Implement strategies similar to those in Django and Flask for prefetching and selecting related data asynchronously.

**Dependency injection for caching**: Use FastAPI's dependency injection system for efficient caching mechanisms across your app. Implement background tasks for operations that can be processed asynchronously.

## Other Optimisation Tips

- Profile your application to identify bottlenecks using tools seen earlier.
- Serve static files efficiently using a CDN.
- Optimise front-end assets (e.g. minified CSS/JS, image compression) to reduce load times.
- Use something like Celery for background tasks, to prevent blocking web requests for operations like sending emails or processing data.
- Use persistent database connections and connection pooling.
