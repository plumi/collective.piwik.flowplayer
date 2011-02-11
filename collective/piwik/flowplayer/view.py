from Products.Five.browser  import BrowserView
import urllib2, simplejson
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.piwik.core.interfaces import IPiwikSettings
import logging

log = logging.getLogger('collective.piwik.flowplayer')

class PlayCountView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json')
        result = self.getPlayCount()
        return simplejson.dumps(result)

    def getPlayCount(self):
        """ Return video play count and unique visits from Piwik 
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPiwikSettings)

        self.plays = 0
        self.unique = 0
        
        #for urls with slash(es) on the end
        self.page_url = self.context.absolute_url().strip('/')        
        self.page_id = self.page_url.split('/')[-1]

        url = settings.piwik_server +'?module=API&method=Actions.getOutlinks&idSite=' + settings.piwik_siteid + '&period=year&date=last100&format=json&filter_column_recursive=label&filter_pattern_recursive=' +  self.page_id + '&expanded=1&token_auth=' + settings.piwik_key
        
        try: 
            piwik_data = simplejson.load(urllib2.urlopen(url))
        except Exception, e: # might be a URLError, timeout etc
            log.error("exception %s !"  % e)
            piwik_data = {}

        if piwik_data.get('result') == 'error':
            log.error("error loading piwik data: %s" % piwik_data)
            piwik_data = {} # error on the communication.maybe wrong token?

        for year in piwik_data:
            if piwik_data[year]:
                self.check_url(piwik_data[year])

        return(self.plays, self.unique)

    def check_url(self, entry):
        for level in entry:
            if level.get('url'):            
                if level['url'] == self.page_url or level['url'] == (self.page_url + '/'):
                    self.plays += int(level['nb_hits'])
                    self.unique += int(level['nb_visits'])
            elif level.get('subtable'):
                self.check_url(level['subtable'])

class DownCountView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json')
        result = self.getDownloads()
        return simplejson.dumps(result)

    def getDownloads(self):
        """ Return the number of downloads from Piwik 
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPiwikSettings)

        self.downloads = 0
        self.unique = 0
        
        #for urls with slash(es) on the end
        self.page_url = self.context.absolute_url().strip('/')        
        self.page_id = self.page_url.split('/')[-1]
        url = settings.piwik_server +'?module=API&method=Actions.getDownloads&idSite=' + settings.piwik_siteid + '&period=year&date=last100&format=json&filter_column_recursive=label&filter_pattern_recursive=' +  self.page_id + '&expanded=1&token_auth=' + settings.piwik_key

        try: 
            piwik_data = simplejson.load(urllib2.urlopen(url))
        except Exception, e: # might be a URLError, timeout etc
            piwik_data = {}

        if piwik_data.get('result') == 'error':
            piwik_data = {} # error on the communication.maybe wrong token?

        for year in piwik_data:
            if piwik_data[year]:
                self.check_url(piwik_data[year])

        return(self.downloads, self.unique)

    def check_url(self, entry):
        for level in entry:
            if level.get('url'):            
                if level['url'] == self.page_url or level['url'] == (self.page_url + '/'):
                    self.downloads += int(level['nb_hits'])
                    self.unique += int(level['nb_visits'])
            elif level.get('subtable'):
                self.check_url(level['subtable'])
