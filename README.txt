Introduction
============
collective.piwik.flowplayer was created to display a video play counter for Plone sites that use flowplayer. 

The Piwik open source analytics system (http://piwik.org/) is used to store the play counter.

Works with and without collective.transcode.star

How to get it working
============
 - You need to have access to a working Piwik installation. Anonymous users should have view permission for your site's stats.

 - Add the Piwik Tracking Tag to Javascript web stats support field at <SITEURL>/@@site-controlpanel

 - You need to make a small change adding the link "var site_id = X;", replacing X with your Piwik site_id
   For example, if on the Piwik code you have:
   var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 6);
   then site_id = 6 in your case


If you do the above steps a viewlet should appear on top of flowplayer displaying the number of views of a video. 

Tweaks
============
The number of a video views shown is increased when a user presses play on a video. If you want to change this 
behavior, edit collective/piwik/flowplayer/viewlet.pt (change onStart for example).

Credits
============
The product was created by Unweb.me and Giorgos Logiotatidis  during the Bristol 2010 Plone conference. 
Thanks to Engagemedia.org for sponsoring our tickets and registrations.

