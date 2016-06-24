from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from os.path import isfile
import re
from warnings import warn

from steno3d.parsers import AllParsers
from steno3d.parsers import BaseParser
from steno3d import Project, Surface


class obj(BaseParser):
    """class obj

    Parser class for wavefront .obj object files
    """

    extensions = ('obj',)

    def _initialize(self):
        """function _initialize

        Raise an exception if the file_name doesn't exist and warn the
        user if the extension is incorrect
        """
        if not isfile(self.file_name):
            raise ValueError('{}: File not found.'.format(self.file_name))
        if self.file_name.split('.')[-1] not in self.extensions:
            warn('{name}: Unsupported extension - parse() may fail. '
                 'Supported extensions are {exts}'.format(
                    name=self.file_name,
                    exts='(' + ', '.join(self.extensions) + ')'
                 ))

    def parse(self, project=None, **kwargs):
        """function parse

        Optional input:
            project - Preexisting project to add .obj surface to. If not
                      provided, a new project will be created

        Output:
            tuple containing one project with one surface parsed from
            the .obj file
        """
        if project is None:
            proj = Project(
                description='Project imported from ' + self.file_name
            )
        elif isinstance(project, Project):
            proj = project
        else:
            raise ValueError('Only allowed input for parse is '
                             'optional Steno3D project')
        self.set(**kwargs)

        digit = "-?\d*\.\d+|-?\d+"
        comment = re.compile("\s*#")
        vertex = re.compile(
            "\s*v\s+(" + digit + ")\s+(" + digit + ")\s+(" + digit + ")"
        )
        vertices = []
        faces = []

        with open(self.file_name, 'r') as f:
            for line in f:
                line = line.strip()
                if comment.match(line) is not None or len(line) == 0:
                    continue
                value = vertex.match(line)
                if value is not None:
                    vertices.append([float(value.group(1)),
                                     float(value.group(2)),
                                     float(value.group(3))])
                    continue
                if line.startswith('f '):
                    face = [int(_.split('/')[0])-1 for
                            _ in line.strip('f ').split(' ') if len(_) > 0]
                    faces += [face[0:3]]

        Surface(
            project=proj,
            mesh={
                "vertices": vertices,
                "triangles": faces
            }
        )
        return (proj,)

    def export(self, proj):
        raise NotImplementedError()


class AllParsers_obj(AllParsers):
    extensions = {
        'obj': obj
    }
