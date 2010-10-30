Introduction
============
collective.piwik.flowplayer was created to display the hits of a video, for Plone systems that use piwik. Piwik (http://piwik.org/) is an Open Source web analytics platform. 

How to get it working
============
Needs collective.flowplayer or collective.transcode.star in order to work, and of course a Piwik account!

The only change you'll have to do is on the Piwik code, that is pasted on your Plone site. From the control panel, choose Site add on the first line the snippet "var site_id = X" , where X is the site id that Piwik assigns to your site! 

<script type="text/javascript">
var site_id=X;
...
<!-- End Piwik Tag -->


viewlet


