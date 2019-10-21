import unittest

'''NOTE: here, we override the runTest method to create a quick test.
assert method comes from Python. Takes an expression, and a message. 
On fail, returns an AssertionError object.
'''

class DefaultWidgetSizeTestCase(unittest.TestCase): 
    '''Test case for Default Widget Size.'''
    def runTest(self):
        widget = Widget("The Widget")
        assert widget.size == (50,50), 'incorrect default size'

# Now, call the test case's constructor without arguments...
testcase = DefaultWidgetSizeTestCase()


