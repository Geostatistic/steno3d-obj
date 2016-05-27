import steno3d, properties
import re

class obj(steno3d.parsers.BaseParser):

    extensions = ('obj',)

    fileName = properties.String("The main file to parse.")

    def __init__(self, fileName, **kwargs):
        self.fileName = fileName
        self.set(**kwargs)

    def parse(self, **kwargs):
        self.set(**kwargs)

        digit = "-?\d*\.\d+|-?\d+"
        integer = "\d+"
        comment = re.compile("\s*#");
        vertex = re.compile("\s*v\s+("+digit+")\s+("+digit+")\s+("+digit+")")

        vertices = []
        vertTextures = []
        faces = []

        with open(self.fileName, 'r') as f:

            for line in f:
                line = line.strip()
                if (comment.match(line) is not None or len(line) == 0):
                    continue
                value = vertex.match(line)
                if value is not None:
                    vertices.append([float(value.group(1)), float(value.group(2)), float(value.group(3))])
                    continue

                if line.startswith('f '):
                    face = [int(_.split('/')[0])-1 for _ in line.strip('f ').split(' ') if len(_) > 0]
                    # for ii in range(len(face)-2):
                    ii = 0
                    faces += [face[ii:ii+3]]

        S = steno3d.resources.Surface(mesh={"vertices": vertices, "triangles": faces})

        return (S,)

    def export(self, S):
        raise NotImplementedError()
