#!/usr/bin/env python

import sys
import unittest
import os.path

sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../src")
from doctorj import parse_orderly_blocks

def read_file(path):
    dirname = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(dirname, path)
    f = open(fname)
    d = f.read()
    f.close()
    return d

class ParserTest(unittest.TestCase):

    def test_parse_orderly_block(self):
        t = read_file("data/mail.md")
        blocks = parse_orderly_blocks(t)
        self.assertEquals(2, len(blocks))
        self.assertEquals("foo_request", blocks[0][0])
        self.assertEquals("foo_response", blocks[1][0])
        
##############################

if __name__ == '__main__':
    unittest.main()
