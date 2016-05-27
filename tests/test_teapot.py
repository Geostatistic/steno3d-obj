import unittest, numpy as np, os
import steno3d, steno3d_obj

class TestBasic(unittest.TestCase):

    def test_teapot(self):

        p = steno3d.parsers.obj('../examples/teapot.obj')
        S = p.parse()
        s, = S
        assert len(S) == 1
        assert s.mesh.nN == 3644
        assert s.mesh.nC == 6320


if __name__ == '__main__':
    unittest.main()


