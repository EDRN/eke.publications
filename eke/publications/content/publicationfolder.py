# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Publication folder.'''

from eea.facetednavigation.interfaces import IPossibleFacetedNavigable
from eke.knowledge.content import knowledgefolder
from eke.publications import ProjectMessageFactory as _
from eke.publications.config import PROJECTNAME
from eke.publications.interfaces import IPublicationFolder
from eke.publications.utils import setFacetedNavigation
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.CMFCore.utils import getToolByName
from zope.interface import implements

PublicationFolderSchema = knowledgefolder.KnowledgeFolderSchema.copy() + atapi.Schema((
    atapi.LinesField(
        'additionalDataSources',
        required=False,
        storage=atapi.AnnotationStorage(),
        widget=atapi.LinesWidget(
            label=_(u'Additonal Data Sources'),
            description=_(u'URLs to additional sources of RDF that describe publications.'),
        ),
    ),
    atapi.StringField(
        'pubSumDataSource',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Publication Summary Statistics Data Source'),
            description=_(u'URL to a source of summary statistics json that describes publication data.'),
            size=60,
        ),
    ),
    atapi.StringField(
        'dataSummary',
        required=False,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Publication Summary Statistics Data'),            description=_(u'Summary statistics json that describes biomarker data.'),
            size=10000,
        ),
    ),
))

finalizeATCTSchema(PublicationFolderSchema, folderish=True, moveDiscussion=False)

class PublicationFolder(knowledgefolder.KnowledgeFolder):
    '''Publication folder which contains publications.'''
    implements(IPublicationFolder, IPossibleFacetedNavigable)
    portal_type               = 'Publication Folder'
    _at_rename_after_creation = True
    schema                    = PublicationFolderSchema
    additionalDataSources     = atapi.ATFieldProperty('additionalDataSources')
    pubSumDataSource          = atapi.ATFieldProperty('pubSumDataSource')
    dataSummary               = atapi.ATFieldProperty('dataSummary')

atapi.registerType(PublicationFolder, PROJECTNAME)

def addFacetedNavigation(obj, event):
    '''Set up faceted navigation on all newly created Publication Folders.'''
    if not IPublicationFolder.providedBy(obj): return
    factory = getToolByName(obj, 'portal_factory')
    if factory.isTemporary(obj): return
    request = obj.REQUEST
    setFacetedNavigation(obj, request)
