import unittest

'''Make a test case class that inherits from unittest.TestCase.
   They call this a 'fixture'.
'''
class SimpleWidgetTestCase(unittest.TestCase):
    '''Now you can override setUp, to prep your class for testing.'''
    def setUp(self):
        '''setUp instantiates the widget'''
        self.widget = Widget("The Widget")
    def tearDown(self):
        self.widget.dispose()
        self.widget = None

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        assert self.widget.size() == (50,50), 'incorrect default size'

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        assert self.widget.size() == (100,150), \
            'wrong size after resize'

