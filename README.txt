Introduction
============
collective.piwik.flowplayer displays a video play counter for Plone sites that use `collective.flowplayer <http://pypi.python.org/pypi/collective.flowplayer>`_.
A download counter is displayed when used in combination with `collective.transcode.star <http://pypi.python.org/pypi/collective.transcode.star>`_ or `Plumi <http://plumi.org>`_.

The `Piwik <http://piwik.org/>`_  open source analytics system is used to store and retrieve the usage data.

How to get it working
=====================

 - Install collective.piwik.core and collective.flowplayer from the Plone control panel.
 - You need to have access to a working Piwik installation. Create a new site in the Piwik admin UI and a new user who should have view access for that site.
 - Go to the Piwik Settings page in the Plone control panel and enter the URL of your Piwik instance, the siteId and the user's authentication token
 - Upload an flv/mp4 video that can be played by flowplayer and click play

If you do the above a viewlet should appear on top of flowplayer displaying the number of views of each video. 

Credits
=======

The product was created by `Unweb.me <https://unweb.me>`_ and `Giorgos Logiotatidis <http://www.sealabs.net/seadog/>`_ during the `Bristol 2010 Plone conference <http://www.ploneconf2010.org/>`_. 
Thanks to `EngageMedia <http://www.engagemedia.org/>`_ for sponsoring our tickets and registrations.

