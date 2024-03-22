# Numpy: the Solution to Lists

Python's native list structure has a problem for vector operations and matrix manipulations. Lists don't actually hold the data - instead, they hold **pointers** to the data location. The advantage of this is that the contents of a list can be heterogenous. However, it introduces a fetch/look-up overhead, and if you are doing lots of operations, this fragmentation adds up. 

What does this look like in hardware terms? Data needs to be moved from memory to the CPU. Modern computers can have tiered architectures, with DRAM, SRAM, external caches, and on-chip caches. CPUs can also do things like branch prediction, speculation, overlapped instruction fetching, pipelining, and superscalar execution. If you want to get into the weeds, you can use the Linux `perf` tool to do some profiling, looking for `cache-misses` (memory bound) and `page-faults` (disk/network bound). But we might as well be sensible with how we do things. 

Python offers an `array` module, that overcomes the memory fragementation issue by storing items sequentially. Iterating through an array therefore doesn't require multiple look-ups, as data can be cached (i.e. closer in terms of spatial and temporal locality to the CPU). But then we run into a different issue: Python, as a high-level interpreted language, isn't optimised for vector operations, and isn't good at dealing with the low-level implementation of `array`.

**Enter `NumPy`**