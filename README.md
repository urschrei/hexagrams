[![Tui](http://cleromancer.herokuapp.com/hexagram/100100.png)](Tui_hex.png)

# Description
Procedural generation of I Ching hexagrams using PIL and NumPy.

# Usage
First, install [`requirements`](requirements.txt) (PIL and NumPy).  

A Hexagram is composed from two of the eight trigrams. Its bars are encoded as binary numbers, **from bottom to top**.  
`1` encodes a solid bar, `0` encodes a broken bar.  
Pass a 6-digit iterable of `1`/`0` or `True`/`False` to generate the hexagram.  

Call `dump()` to dump it to `hexagram_output\hexagram.png`. Pass an optional string to `dump()` to control the output filename.  
Call `dump_json()` to dump it to `hexagram.json`. Pass an optional string to `dump_json()` to control the output filename. 

Trigrams can be constructed and dumped in the same way; pass a 3-digit iterable.

``` python
from hexagram import Hexagram, Trigram
from hexagrams import hexagrams, trigrams

for k, v in hexagrams.items():
    h = Hexagram(v)
    h.dump(k)

for k, v in trigrams.items():
    t = Trigram(v)
    t.dump(k)
```

# The Trigrams and Hexagrams
Can be found [here](hexagrams.py).

# License
[MIT](LICENSE)

# Why
[The Lottery in Babylon](https://en.wikipedia.org/wiki/The_Lottery_in_Babylon) is a very good story. You should [read](http://web.itu.edu.tr/~inceogl4/modernism/lotteryofbabylon.pdf) it.
