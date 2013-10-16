bligress
========

Kanban based process system.

Bligress is a Kanban tool for following process and marking hours.
Target is in to get easy progress control, great data and visualizations.
One major target is to use for hour tracking.
Developed for needs of Blistud:io.

Dependencies
------------

To install basic dependencies:

> pip install Django==1.5.1
> 
> pip install South


Distribution already contains jQuery and jQuery UI code.

After changing settings.py the minimal WSGI server can be run with:

> ./manage.py runserver


Static files
-------------

To install static files:

> ./manage.py collectstatic

Target location is defined in settings.

Copyright
---------

Copyright (c)2013 Blistud:io
http://blistud.io

Licenced under 3-Clause BSD licence.
