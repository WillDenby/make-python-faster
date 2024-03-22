# Data Structures and Types

Python comes with several ways of creating, storing, moving, and transforming data:

- Lists
- Tuples
- Sets
- Dictionaries

In addition, people have created libraries with their own data structures, typically for tackling maths/stats/physics data problems, e.g.

- Numpy
- Pandas
- Dask
- Polars
- GPU Accelerated Pandas

In this section, we'll look at all their various advantages and disadvantages. Picking appropriate data structures for what you are trying to do is a major factor in writing high-performance code. A rule of thumb to remember throughout is that "generic" structures containing multiple data types will tend to incur greater overhead when being manipulated than those of a single type. 

We'll also consider how data structures interact with algorithm selection.
