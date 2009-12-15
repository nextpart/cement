"""This is an example of how to write a Cement plugin."""

import os
from cement.core.log import get_logger
from cement.core.app_setup import CementCommand, CementPlugin
from cement.core.options import init_parser
from cement import helpers as _h

log = get_logger(__name__)
    
def register_plugin(global_config):
    """
    All plugins that are set as enabled will be imported, and this method
    will be called.  The instantiated plugin object gets returned.
    """
    return ExamplePlugin(global_config)


class ExamplePlugin(CementPlugin):
    def __init__(self, global_config):
        CementPlugin.__init__(self, global_config)
        self.version = '0.1'
        self.required_abi = '20091207'
        self.description = "Example Plugin for a Cement Application."
        self.config = {
            'config_source': ['defaults'],
            'myplugin_opton' : 'My plugin value'
            }
        self.commands = {
            'myplugin' : MyPluginCommand,
            }
        self.options = init_parser(global_config)
        
        # Cement allows you to expose command line options to the 
        # unified cli utility as well. 
        self.options.parser.add_option('--myplugin', action ='store', 
            dest='myplugin_option', default=None, 
            help='example option for myplugun plugin', metavar='VAR' 
            )
        

class MyClass(object):
    def __init__(self, config):
        pass

    def my_class_method(self):
        log.info('example of using logger')
        

class MyPluginCommand(CementCommand):     
    """
    This is an example method that is called when the following command is 
    run:
    
        <your_app_name> example
    

    All plugin commands receive the global config dict, as well as the 
    cli options that were passed at command line.

    Our plugin configuration comes back in the global config as:

        self.config['plugins']['myplugin'].config
    
    So, to access our 'example_config_option' we would reference:

        config['plugins']['myplugin'].config['myplugin_option']
    
    
    But to make things shorter we create self.plugin_config.  So configurations
    local to this plugin can be called as:
    
        self.plugin_config['myplugin_option']
    
    
    The CementCommand parent object sets up the following objects as well:
    
        self.config     (global config)
        self.cli_opts   (cli options)
        self.cli_args   (cli arguents)
        self.handlers   (objects created by other plugins for use)
        
    """
    def __init__(self, *args):
        CementCommand.__init__(self, *args)
        self.plugin_config = self.config['plugins']['myplugin'].config

    def run(self):        
        if self.cli_opts.myplugin_option:
            print '--myplugin option passed with value %s' % \
                self.cli_opts.myplugin_option
        
        myclass = MyClass(self.config)
        # do something with our object
        
        # Note that you can either print to the console:
        print 'This is the myplugin plugin...  run() method'
        
        # or log to both console, and a log_file if one was configured in
        # the apps configuration.
        log.debug('This is the myplugin plugin...  run() method')


    def help(self):
        """
        Help commands are hidden in the commands list, but can be called
        for any module command by adding it like this.
        """
        print 'help content for cement.plugins.example.example_method()' 
    