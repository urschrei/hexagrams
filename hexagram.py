# -*- coding: utf-8 -*-

# Requires PIL (pillow) and NumPy
# Copyright (C) Stephan Hügel, 2016
# License: MIT

import os
from PIL import Image
import numpy as np



class Hexagram(object):
    """
    Generate and write a hexagram to PNG
    Input is an iterable of six binary digits; 1 is a solid line, 0 a broken line
    Write to hexagram.png by calling .dump()
    
    """   
    def __init__(self, pattern):
        if len(pattern) != 6:
            raise HexagramException("Pass an iterable of six digits or booleans")
        self.bar_height = 8
        self.bar_width = 100
        self.pattern = pattern
        self.generated = self.generate(pattern)
    
    def _black_row(self):
        """ an unbroken bar """
        return np.vstack([
            np.zeros((self.bar_height, self.bar_width)),
            np.ones((self.bar_height, self.bar_width))]
        )
    
    def _broken_row(self):
        """ a broken bar """
        return np.vstack([
            np.hstack([
                np.zeros((self.bar_height, (self.bar_width / 2) - self.bar_height)),
                np.ones((self.bar_height, self.bar_height * 2)),
                np.zeros((self.bar_height, (self.bar_width / 2) - self.bar_height))]),
            np.ones((self.bar_height, self.bar_width))]
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
        # rescale to 256 x 8-bit    
        return (255.0 / stacked.max() * (stacked - stacked.min())).astype(np.uint8)
    
    def dump(self, filename="hexagram"):
        """ write hexagram to PNG """
        im = Image.fromarray(self.generated)
        outdir = 'hexagram_output'
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        path = os.path.join(outdir, filename + ".png")
        im.save(path)



class HexagramException(Exception):
    """ tfw your hexagram can't be constructed bc it's too short """
    pass
