
import pyblish.backend.lib
import pyblish.backend.plugin


@pyblish.backend.lib.log
class ExtractInstancesFail(pyblish.backend.plugin.Extractor):
    hosts = ['python']
    families = ['test.family']
    version = (0, 1, 0)

    def process_instance(self, instance):
        raise ValueError("Could not extract {0}".format(instance))
