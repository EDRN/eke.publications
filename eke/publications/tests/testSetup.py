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
import unittest

class SetupTest(BaseTestCase):
    '''Unit tests the setup of this package.'''
    def testCatalogIndexes(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        indexes = catalog.indexes()
        for i in ('journal', 'authors', 'year'):
            self.failUnless(i in indexes, '%s not found in catalog indexes' % i)
    def testCatalogMetadata(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        metadata = catalog.schema()
        for i in ('journal', 'authors', 'year'):
            self.failUnless(i in metadata, '%s not found in catalog metadata' % i)
    def testVocabularies(self):
        '''Ensure we have our expected vocabularies'''
        vocabs = (
            u'eke.publications.attributes.year',
            u'eke.publications.attributes.journal',
            u'eke.publications.attributes.author',
        )
        for v in vocabs:
            vocab = queryUtility(IVocabularyFactory, name=v)
            self.failIf(v is None, u'Vocabulary %s not available' % v)
    # TBD:
    # def testMonkeyPatching(self):
    #     '''Check that the Plone portal has a "macros" attribute to work around the eea.facetedvocabularies problem'''
        

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetupTest))
    return suite
    
