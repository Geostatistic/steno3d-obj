from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from os import path
import unittest

from steno3d.parsers import ParseError
import steno3d
import steno3d_obj

class TestObj(unittest.TestCase):

    def setUp(self):
        obj_dir = path.split(path.realpath(steno3d_obj.__file__))[0]
        self.assets = obj_dir.split(path.sep)[:-1] + ['assets']

    def test_teapot(self):
        teapot = path.sep.join(self.assets + ['teapot.obj'])
        parser = steno3d.parsers.obj(teapot)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nN == 3644
        assert proj.resources[0].mesh.nC == 6320

        parser.parse(proj)
        assert len(proj.resources) == 2

        self.assertRaises(ParseError, lambda: steno3d.parsers.obj('junk.obj'))
        self.assertRaises(ParseError, lambda: steno3d.parsers.obj(5))

    def test_allparsers(self):
        teapot = path.sep.join(self.assets + ['teapot.obj'])
        parser = steno3d.parsers.AllParsers(teapot)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nN == 3644
        assert proj.resources[0].mesh.nC == 6320

    def test_allparsers_obj(self):
        teapot = path.sep.join(self.assets + ['teapot.obj'])
        parser = steno3d.parsers.AllParsers_obj(teapot)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nN == 3644
        assert proj.resources[0].mesh.nC == 6320

    def test_unsupported(self):
        unsupported_files = [
            'approx_curve.obj',
            'approx_surf.obj',
            'b_spline.obj',
            'bezier_b_spline.obj',
            'bezier_curve.obj',
            'bezier_patch.obj',
            'cardinal_curve.obj',
            'cardinal_surf.obj',
            'connectivity.obj',
            'cubic_bezier.obj',
            'hermite_curve.obj',
            'merging.obj',
            'rational_b_spline.obj',
            'taylor_curve.obj',
            'trim_curve.obj',
            'trim_nurb.obj',
            'trim_pts.obj',
            'two_trim.obj'
        ]
        for f in unsupported_files:
            objfile = path.sep.join(self.assets + [f])
            self.assertRaises(ParseError,
                              lambda: steno3d.parsers.obj(objfile).parse())

    def test_square(self):
        square_files = [
            'rectangle.obj',
            'square.obj',
            'square_texture.obj',
            'square_texture_2.obj',
        ]
        for f in square_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Surface)
            assert len(proj.resources[0].mesh.vertices) == 4
            assert len(proj.resources[0].mesh.triangles) == 2

    def test_squares(self):
        squares_files = [
            'squares_smoothing.obj',
            'squares_vn.obj',
        ]
        for f in squares_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Surface)
            assert len(proj.resources[0].mesh.vertices) == 6
            assert len(proj.resources[0].mesh.triangles) == 4

    def test_triangle(self):
        triangle_files = [
            'triangle.obj',
        ]
        for f in triangle_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Surface)
            assert len(proj.resources[0].mesh.vertices) == 3
            assert len(proj.resources[0].mesh.triangles) == 1

    def test_cube(self):
        cube_files = [
            'cube.obj',
            'cube_groups.obj',
            'cube_materials.obj',
            'cube_neg_ref.obj',
            'cube_reflection.obj',
            'cube_shadow.obj',
            'cube_with_materials.obj'
        ]
        for f in cube_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Surface)
            assert len(proj.resources[0].mesh.vertices) in (8, 24)
            assert len(proj.resources[0].mesh.triangles) == 12

    def test_points(self):
        pt_files = [
            'points.obj'
        ]
        for f in pt_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Point)
            assert len(proj.resources[0].mesh.vertices) == 8

    def test_lines(self):
        line_files = [
            'lines.obj'
        ]
        for f in line_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 1
            assert isinstance(proj.resources[0], steno3d.Line)
            assert len(proj.resources[0].mesh.vertices) == 8
            assert len(proj.resources[0].mesh.segments) == 6

    def test_mixed(self):
        mixed_files = [
            'mixed.obj'
        ]
        for f in mixed_files:
            objfile = path.sep.join(self.assets + [f])
            (proj,) = steno3d.parsers.obj(objfile).parse()
            assert len(proj.resources) == 3


if __name__ == '__main__':
    unittest.main()
