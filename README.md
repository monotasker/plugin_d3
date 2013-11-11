plugin\_d3
==========

A web2py plugin to provide easy integration of d3.js, dc.js, and crossfilter 
libraries for building interactive data-visualizations.

Plugin assembled by Ian W. Scott. I didn't have anything to do with creating 
the libraries included here, so see the copyright statements of each library 
included in its own README file.

About These Libraries
---------------------

D3.js is a powerful library for creating (primarily svg) data visualizations on 
the web. The term "visualization" can mean traditional bar charts, line charts, 
ring charts, pie graphs, scatter plot graphs, data tables, etc. In addition, 
d3.js can also produce less common visualizations such as data-driven maps and 
force diagrams.

Dc.js is a helper library that simplifies the implementation of d3.js. Dc.js is 
especially good at building interactive data-visualizations that respond to 
mouse actions. These visualizations can be linked so that interaction with one 
chart will produce changes in another.

[Crossfilter.js http://square.github.io/crossfilter/] is a library for 
efficient live manipulation of data sets. This is used heavily by dc.js but is 
not required by d3.js itself.

A helpful orientation is available in the free-access ebook [D3 Tips and Tricks 
https://leanpub.com/D3-Tips-and-Tricks/read#leanpub-auto-crossfilter-dcjs-and-d3js-for-data-discovery
]. If you find the book helpful, you can purchase the ebook on a 
pay-what-you-want basis. (I have no connection to the author.)

Implementation
--------------

-   Download or clone this repository under the "plugins"  folder of your 
    web2py application (web2py/applications/{appname}/plugins).

-   You probably won't want to load these libraries in every  one of your 
    views. Instead, place the appropriate snippet below either in the 
controller function or in the view itself for the view in which d3 will be 
used.

-   Write some beautiful d3.js data-visualizations!

Script Loading Snippets
-----------------------

You should only use one of these  snippets, since they do the same job from 
different locations.

These snippets also assume that you wish to use all three of the included 
libraries. If you don't, include only the line(s) for the libraries you need 
(d3.js, dc.js, or crossfilter.js).

### In A Controller Function

This snippet may be placed anywhere in the controller function for the view in 
which you will use d3.

    response.files.append(URL('plugins', 'plugin_d3/static/d3/d3.js'))
    response.files.append(URL('plugins', 'plugin_d3/static/dc/dc.js'))
    response.files.append(URL('plugins', 
'plugin_d3/static/crossfilter/crossfilter.js'))

### In A View File

Note: This snippet must be included **before** any {{extend layout.html}} or 
similar instruction. It should be the very first line in the view file.

    {{response.files.append(URL('plugins', 'plugin_d3/static/d3/d3.js'))}}
    {{response.files.append(URL('plugins', 'plugin_d3/static/dc/dc.js'))}}
    {{response.files.append(URL('plugins', 
'plugin_d3/static/crossfilter/crossfilter.js'))}}
