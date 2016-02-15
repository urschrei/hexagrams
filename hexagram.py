# -*- coding: utf-8 -*-

# Requires PIL (pillow) and NumPy
# Copyright (C) Stephan Hügel, 2016
# License: MIT

import os
import json
import codecs
from PIL import Image
import numpy as np



class Hexagram(object):
    """
    Generate and write a hexagram to PNG
    Input is an iterable of six binary digits or booleans;
    1 / True is a solid line,
    0 / False is a broken line
    Write to hexagram_output\hexagram.png by calling .dump(),
    with an optional filename string argument
    
    """   
    def __init__(self, pattern, plength=6):
        if len(pattern) != plength:
            raise HexagramException("Pass an iterable of %s digits or booleans" % plength)
        self.bar_height = 8
        self.wbar_height = 6
        # we always want to produce a square hexagram
        self.bar_width = (self.bar_height * 6) + (self.wbar_height * 5)
        self.pattern = pattern
        self.generated = self.generate(pattern)
        self.json = json.dumps(
            self.generated.tolist(),
            indent=4,
            separators=(',', ':'),
            sort_keys=True)
    
    def _black_row(self):
        """ an unbroken bar """
        return np.vstack([
            np.zeros((self.bar_height, self.bar_width)),
            np.ones((self.wbar_height, self.bar_width))]
        )
    
    def _broken_row(self):
        """ a broken bar """
        return np.vstack([
            np.hstack([
                np.zeros((self.bar_height, (self.bar_width / 2) - self.bar_height)),
                np.ones((self.bar_height, self.bar_height * 2)),
                np.zeros((self.bar_height, (self.bar_width / 2) - self.bar_height))]),
            np.ones((self.wbar_height, self.bar_width))]
        )
    
    def trim(self, raw_hexagram):
        """ remove trailing white bar from bottom of hexagram / trigram """
        raw_hexagram[-1] = raw_hexagram[-1][0:self.bar_height]
        return raw_hexagram

    def generate(self, pattern):
        """ generate a scaled b&w hexagram """
        container = []
        # hexagrams are grown bottom to top
        for row in self.pattern:
            if row:
                container.insert(0, self._black_row())
            else:
                container.insert(0, self._broken_row())
        container = self.trim(container)
        stacked = np.vstack(container)
        # rescale to 256 x 8-bit (0 = black, 255 = white)
        return (255.0 / stacked.max() * (stacked - stacked.min())).astype(np.uint8)
    
    def dump(self, fname=False):
        """ write hexagram to PNG """
        _fname = (fname or self.__class__.__name__.lower())
        im = Image.fromarray(self.generated)
        outdir = '%s%s' % (self.__class__.__name__.lower(), '_output')
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        path = os.path.join(outdir, "%s%s" % (_fname, ".png"))
        im.save(path)

    def dump_json(self, fname=False):
        """ tries to dump JSON representation to a file """
        _fname = (fname or self.__class__.__name__.lower())
        try:
            with codecs.open("%s%s" % (_fname, ".json"), 'w', encoding="utf-8") as f:
                f.write(self.json)
        except IOError:
            raise("Couldn't write file! You could also copy the .json property to your clipboard.")


class Trigram(Hexagram):
    """ Same as hexagram, but with three bars """
    def __init__(self, pattern):
        super(self.__class__, self).__init__(pattern, plength=3)


class HexagramException(Exception):
    """ tfw your hexagram can't be constructed bc it's too short """
    pass
