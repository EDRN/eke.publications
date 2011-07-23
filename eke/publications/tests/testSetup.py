# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE Publications: test the setup of this package.
'''

from eke.publications.tests.base import BaseTestCase
from Products.CMFCore.utils import getToolByName
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from eea.facetednavigation.interfaces import IPossibleFacetedNavigable
from eke.publications.content.publicationfolder import PublicationFolder
import unittest

class SetupTest(BaseTestCase):
    '''Unit tests the setup of this package.'''
    def testCatalogIndexes(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        indexes = catalog.indexes()
        for i in ('authors',):
            self.failUnless(i in indexes, '%s not found in catalog indexes' % i)
    def testMonkeyPatching(self):
        '''Check that the Plone portal has a "macros" attribute to work around the eea.facetedvocabularies problem'''
        from Products.CMFPlone.Portal import PloneSite
        viewFunction = PloneSite.view
        self.failUnless(hasattr(viewFunction, 'macros'), 'PloneSite.view not monkeypatched with a "macros" attribute')
    def testFacetNavigability(self):
        '''Ensure the Publications Folder type can use faceted navigation.'''
        self.failUnless(IPossibleFacetedNavigable.implementedBy(PublicationFolder))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetupTest))
    return suite
    
