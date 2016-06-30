from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
import steno3d
import steno3d_obj

class TestBasic(unittest.TestCase):

    def test_teapot(self):

        p = steno3d.parsers.obj('../assets/teapot.obj')
        Projs = p.parse()
        assert len(Projs) == 1
        P, = Projs
        assert len(P.resources) == 1
        assert isinstance(P.resources[0], steno3d.Surface)
        assert P.resources[0].mesh.nN == 3644
        assert P.resources[0].mesh.nC == 6320

        p.parse(P)
        assert len(P.resources) == 2

        self.assertRaises(IOError, lambda: steno3d.parsers.obj('junk.obj'))
        self.assertRaises(IOError, lambda: steno3d.parsers.obj(5))

    def test_allparsers(self):

        p = steno3d.parsers.AllParsers('../assets/teapot.obj')
        Projs = p.parse()
        assert len(Projs) == 1
        P, = Projs
        assert len(P.resources) == 1
        assert isinstance(P.resources[0], steno3d.Surface)
        assert P.resources[0].mesh.nN == 3644
        assert P.resources[0].mesh.nC == 6320

    def test_allparsers_obj(self):

        p = steno3d.parsers.AllParsers_obj('../assets/teapot.obj')
        Projs = p.parse()
        assert len(Projs) == 1
        P, = Projs
        assert len(P.resources) == 1
        assert isinstance(P.resources[0], steno3d.Surface)
        assert P.resources[0].mesh.nN == 3644
        assert P.resources[0].mesh.nC == 6320


if __name__ == '__main__':
    unittest.main()


