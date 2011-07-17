# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from eea.facetednavigation.interfaces import ICriteria
from eea.facetednavigation.layout.interfaces import IFacetedLayout
from eke.publications.interfaces import IPublication
from Products.CMFPlone.Portal import PloneSite
from zope.component import getMultiAdapter

def view(self):
    return super(PloneSite, self).view()

def patchMacrosDict(scope, original, replacement):
    scope.view.__dict__['macros'] = {}

def setFacetedNavigation(folder, request):
    subtyper = getMultiAdapter((folder, request), name=u'faceted_subtyper')
    if subtyper.is_faceted or not subtyper.can_enable: return
    subtyper.enable()
    criteria = ICriteria(folder)
    for cid in criteria.keys():
        criteria.delete(cid)
    criteria.add('resultsperpage', 'bottom', 'default', title='Results per page', hidden=True, start=0, end=50, step=5, default=20)
    criteria.add('sorting', 'bottom', 'default', title='Sort on', hidden=True, default='sortable_title')
    criteria.add(
        'checkbox', 'bottom', 'default',
        title='Obj provides',
        hidden=True,
        index='object_provides',
        operator='or',
        vocabulary=u'eea.faceted.vocabularies.ObjectProvides',
        default=[IPublication.__identifier__],
        count=False,
        maxitems=0,
        sortreversed=False,
        hidezerocount=False
    )
    criteria.add(
        'checkbox', 'left', 'default',
        title='Journal',
        hidden=False,
        index='journal',
        operator='or',
        vocabulary=u'eke.publications.attributes.journal',
        count=True,
        maxitems=4,
        sortreversed=False,
        hidezerocount=False
    )
    criteria.add(
        'checkbox', 'left', 'default',
        title='Year',
        hidden=False,
        index='year',
        operator='or',
        vocabulary=u'eke.publications.attributes.year',
        count=True,
        maxitems=4,
        sortreversed=False,
        hidezerocount=False
    )
    criteria.add('debug', 'top', 'default', title='Debug Criteria', user='kelly')
    criteria.add('criteria', 'top', 'default', title='Current Search')
    IFacetedLayout(folder).update_layout('faceted_publications_view')
