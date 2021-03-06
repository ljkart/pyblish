
import pyblish.backend.lib
import pyblish.backend.plugin


@pyblish.backend.lib.log
class ValidateInstance(pyblish.backend.plugin.Validator):
    hosts = ['python']
    families = ['full']
    version = (0, 1, 0)

    def process_instance(self, instance):
        instance.set_data('validated', True)
