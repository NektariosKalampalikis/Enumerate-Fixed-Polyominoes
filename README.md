# Enumerate Fixed Polyominoes
Python implementation based on [1] to count the number of fixed polyominoes [2] for every possible number of tiles. According to [1], "a polyomino is a geometrical shape consisting of a number of square tiles, with each two of them sharing a side". If rotations and reflections are allowed, then the set of polyominoes is called free. Otherwise, it is called fixed. For instance, with 5 tiles we get the following [1] :

![pentominoes](https://louridas.github.io/rwa/assignments/polyominoes/pentominoes_fixed.png)

Since the algorithm implemented in this repository has exponential complexity, it is recommended for sizes up to 15. For higher number of tiles a faster algorithm such as the one found in [3] should be used. A great introductory source with examples is [1].

The code has been developed and tested on Python 3.9.4. Apart from the optional pprint module, which is used to "pretty print" a dictionary, only Python3 built-in modules have been used.

# Values for different sizes
In the following table the number of different fixed polyominoes of size up to and including 46 according to [3], is presented: 
| Polyomino Size   | Number of Fixed Polyominoes  |   
|---|---|
|  1 |  1 | 
|  2 |  2 | 
|  3 |  6 |
|  4 |  19 | 
|  5 |  63 | 
|  6 |  216 |
|  7 |  760 | 
|  8 |  2725 | 
|  9 |  9910 |
|  10 |  36446 | 
|  11 |  135268 | 
|  12 |  505861 |
|  13 |  1903890 | 
|  14 |  7204874 | 
|  15 |  27394666 |
|  16 |  104592937 | 
|  17 |  400795844 |
|  18 |  1540820542 | 
|  19 |  5940738676 |
|  20 |  22964779660 | 
|  21 |  88983512783 |
|  22 |  345532572678 | 
|  23 |  1344372335524 |
|  24 |  5239988770268 | 
|  25 |  20457802016011 | 
|  26 |  79992676367108 | 
|  27 |  313224032098244 |
|  28 |  1228088671826973 | 
|  29 |  4820975409710116 | 
|  30 |  18946775782611174 |
|  31 |  74541651404935148 | 
|  32 |  293560133910477776 | 
|  33 |  1157186142148293638 |
|  34 |  4565553929115769162 | 
|  35 |  18027932215016128134 | 
|  36 |  71242712815411950635 |
|  37 |  281746550485032531911 | 
|  38 |  1115021869572604692100 | 
|  39 |  4415695134978868448596 |
|  40 |  17498111172838312982542 | 
|  41 |  69381900728932743048483 |
|  42 |  275265412856343074274146 | 
|  43 |  1092687308874612006972082 |
|  44 |  4339784013643393384603906 | 
|  45 |  17244800728846724289191074 |
|  46 |  68557762666345165410168738 |


# References
[1] [Github of the book: Louridas, Panos. Real-world Algorithms: A Beginner's Guide. MIT Press, 2017](https://louridas.github.io/rwa/assignments/polyominoes/) 

[2] Redelmeier, D. Hugh. "Counting polyominoes: yet another attack." Discrete Mathematics 36.2 (1981): 191-203.

[3] Jensen, Iwan. "Enumerations of lattice animals and trees.", Journal of statistical physics 102.3 (2001): 865-881.
