Introduction
============
collective.piwik.flowplayer was created to display the hits of a video, for Plone systems that use piwik. 

Piwik (http://piwik.org/) is a great Open Source web analytics platform. 

How to get it working
============
1)Needs collective.flowplayer (http://pypi.python.org/pypi/collective.flowplayer) or collective.transcode.star 
(pypi.python.org/pypi/collective.transcode.star) in order to work, and of course a Piwik account!

2)A little change is necessary to be done on the Piwik code, that is pasted on your Plone site. 
From the control panel, choose Site, and add on the first line of the Piwik code the snippet "var site_id = X;" , 
where X is the site id that Piwik assigns to your site. 

<script type="text/javascript">
var site_id=X;
...
<!-- End Piwik Tag -->

3)Also, make sure the anonymous user has view access to this Piwik website. On Piwik, go to settings, then 
on the users tab, pick up your website, and grant the anonymous user with view access. 

Site id is a variable assigned for your website, by Piwik, because Piwik can have many websites on an installation. 
For example, if on the Piwik code you have

var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 6);
then site_id = 6 in your case!


So after this is done, a viewlet appears on videos handled by flowplayer, that shows the number of views of a video. 


Authors
============
Dimitris Moraitis (dimo@unweb.me)
Giorgos Logiotatidis (seadog@sealabs.net)
Markos Gogoulos (mgogoulos@unweb.me)
Mike Muzurakis (clopy@unweb.me)


Credits
============
The product was created during the Bristol 2010 Plone conference. 
Thanks to Engagemedia.org for sponsoring. 

