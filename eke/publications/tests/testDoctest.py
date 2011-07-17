# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE Publications: functional and documentation tests.
'''

import unittest, doctest, base
from zope.component import testing, eventtesting
from Testing import ZopeTestCase as ztc

def test_suite():
	return unittest.TestSuite([
		ztc.ZopeDocFileSuite('README.txt', package='eke.publications',
			test_class=base.FunctionalBaseTestCase,
			optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
	])
	

if __name__ == '__main__':
	unittest.main(defaultTest='test_suite')
	