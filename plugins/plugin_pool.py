__author__ = 'mkaplenko'


class PluginPool(object):
    plugins = {}

    def register_plugin(self, plugin_model):
        self.plugins[plugin_model.__mapper_args__['polymorphic_identity']] = plugin_model

    def get_plugin(self, plugin_type):
        if plugin_type not in [x for x in self.plugins]:
            return None
        else:
            return self.plugins[plugin_type]


plugin_pool = PluginPool()
