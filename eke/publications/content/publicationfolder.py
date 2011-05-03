# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Publication folder.'''

from eke.knowledge.content import knowledgefolder
from eke.publications import ProjectMessageFactory as _
from eke.publications.config import PROJECTNAME
from eke.publications.interfaces import IPublicationFolder
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
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
))

finalizeATCTSchema(PublicationFolderSchema, folderish=True, moveDiscussion=False)

class PublicationFolder(knowledgefolder.KnowledgeFolder):
    '''Publication folder which contains publications.'''
    implements(IPublicationFolder)
    portal_type               = 'Publication Folder'
    _at_rename_after_creation = True
    schema                    = PublicationFolderSchema
    additionalDataSources     = atapi.ATFieldProperty('additionalDataSources')

atapi.registerType(PublicationFolder, PROJECTNAME)
