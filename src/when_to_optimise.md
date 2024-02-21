# ❓ When to Optimise your Code

In most organisations, programmers live under the paradigm: `overall team velocity > individual code optimisation`

Some of the tips in this book are general best practice (e.g. avoid pointless iterations in your loops); others require more of a time investment. So before considering any implementation of the latter, ask yourself the following three questions;

1. **Does the code achieve its objectives?**

Can you build a prototype to demonstrate proof-of-concept? Is the code useful? Does it do what it's meant to do? If not, figure this bit out first!

2. **Is the code robust?**

Have you documented what you're doing? Does your code conform to organisational standards? Can other developers easily build on top of it?

3. **Is it worth further development?**

Is this a mission-critical piece of code? Or is it only being run occasionally? Remember the famous quote from Tony Hoare/Donald Knuth: `Premature optimisation is the root of all evil`

We code to make the world more efficient. But consult this xkcd graphic if in doubt:

![A matrix about time saved vs time invested](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

Some problems just aren't worth worrying about!