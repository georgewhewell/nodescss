Node.scss
========

CSS on the server!

What?
=========
Node.scss lets you unleash the awesome power of SCSS on the server-side! No more maintainig different frontend and backend CSS - you can write fully DRY code using Node.scss

How?
=========
Node.scss includes a python wrapper to forward requests to your SCSS scripts. This is a stop-gap measure until the necessary interfaces exist to build a pure SCSS server.

Dependencies
==========
You will need a working copy of Python and scss. 

Usage
==========

     $ python nodescss.py example.scss
     $ curl --raw http://localhost:12345
       <h1>Hello World!</h1><p>Your user agent is: curl/7.30.0</p><small>Powered by NodeSCSS</small>

URL Params
==========

You can use the split_string function to extract url parameters

    $ curl --raw http://localhost:12345/hello/Sassy
      <h1>Hello Sassy!</h1><p>Your user agent is: curl/7.30.0</p><small>Powered by NodeSCSS</small>
     
Writing your application
==========

To customize the example application, you need to redefine the handle_request function. It takes a single argument, a request map.
