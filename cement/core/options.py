"""Cement methods and classes to handle cli option/arg parsing."""

from optparse import OptionParser, IndentedHelpFormatter
import sys, os

            
class Options(object):
    """
    This class is used to setup the OptParse object for later use, and is
    the object that is passed around thoughout the application.
    """
    def __init__(self):
        self.parser = None
        self.init_parser()
        
    def add_default_options(self):
        """
        Sets up default options for applications using Cement.
        """
        pass  
         
    def init_parser(self, version_banner=None):
        """
        Sets up the Options object and returns it for use throughout the 
        application.
    
        Arguments
    
        version_banner => option txt to be display for --version.
        """
        fmt = IndentedHelpFormatter(
            indent_increment=4, max_help_position=32, width=77, short_first=1
            )
        self.parser = OptionParser(formatter=fmt, version=version_banner)
    
def get_options():
    o = Options()
    return o
    

def init_parser(version_banner=None):
    fmt = IndentedHelpFormatter(
            indent_increment=4, max_help_position=32, width=77, short_first=1
            )
    parser = OptionParser(formatter=fmt, version=version_banner)
    return parser

    
