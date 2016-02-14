[![Tui](Tui.png)]( "The Joyous, Lake")

# Description
Procedural generation of I Ching hexagrams using PIL and NumPy.

# Usage
First, install [`requirements`](requirements.txt) (PIL and NumPy).  

The bars are encoded as binary numbers, from top to bottom.  
`1` encodes a solid bar, `0` encodes a broken bar.  

Pass a 6-digit iterable to generate the hexagram. Call `dump()` to dump it to `hexagram_output\hexagram.png`. Pass an optional string to `dump()` to control the output filename.

``` python
from hexagram import Hexagram
from hexagrams import hexagrams

for k, v in hexagrams.items():
    h = Hexagram(v)
    h.dump(k)
```

# The Hexagrams
Can be found [here](hexagrams.py).

# License
[MIT](LICENSE)

# Why
[The Lottery in Babylon] is a very good story. You should [read](http://web.itu.edu.tr/~inceogl4/modernism/lotteryofbabylon.pdf) it.
