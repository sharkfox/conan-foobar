
from conans import ConanFile, CMake

class ConanFoobar(ConanFile):
    name        = "foobar"
    version     = "1.1.0"
    description = "This is the foobar application."
    url         = "https://github.com/sharkfox/conan-foobar"
    license     = "proprietary"
    generators  = "cmake"
    settings    = "os", "compiler", "build_type", "arch"
    requires    = "foo/4.0.1@emy/beta"

    def source(self):
        self.run("git clone -b v%s %s.git ." % (self.version, self.url))

    def imports(self):
        self.copy(pattern = "*.xml")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern = "foobar", keep_path = False)

