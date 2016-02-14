[![Tui](Tui.png)]( "The Joyous, Lake")

# Description
Procedural generation of I Ching hexagrams using PIL and NumPy

# Usage
The bars are encoded as binary numbers, from top to bottom.  
`1` encodes a solid bar, `0` encodes a broken bar.  

Pass a 6-digit iterable to generate the hexagram. Call `dump()` to dump it to `hexagram_output\hexagram.png`

``` python
from hexagram import Hexagram
from hexagrams import hexagrams

for k, v in hexagrams.items():
    h = Hexagram(v)
    h.dump(k)
```

# License
[MIT](LICENSE)
