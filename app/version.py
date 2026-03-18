#im sorry man the java brainrot got to me
class Version:
    def __init__(self, version):
        self.version = version
        self.parts = tuple(int(num) for num in version.split('.'))

    def __lt__(self, other):
        return self.parts < other.parts

    def __le__(self, other):
        return self.parts <= other.parts

    def __gt__(self, other):
        return self.parts > other.parts

    def __ge__(self, other):
        return self.parts >= other.parts

    def __eq__(self, other):
        return self.parts == other.parts

    def __str__(self):
        return self.version

VERSION = Version("1.2.1")