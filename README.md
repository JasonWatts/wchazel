Hazel
========

Hazel is a Raspberry Pi based voice-enabled wi-fi walkie-talkie.  It allows users to speak to other
users through a Raspberry Pi based contraption.

Look how easy it is to use!

    Download server.py and run it on whichever machine you want to be the host.

    Download client.py and run it on whichever machine you want to connect with
    the host.


Features
--------

- Walkie Talkie-esque communication!
- Speech commands!  "Hi Hazel!"  "Hazel, connect me to Kevin."
- Make cool things happen.
- Annoy people.

Installation
------------



Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project
- Made by Westmont's CS145 class.  Operating Systems Spring 2018.

Support
-------

If you are having issues, please let us know.
Make an issue on this page: https://gitlab.com/wchazel/hazelproject-server/hazel-server

License
-------

The project is licensed under the BSD license.


Functions
---------
| Server API          |    Client API                        |   Action                             |  Return                                      | Description                                                             |
|---------------------|--------------------------------------|--------------------------------------|----------------------------------------------|-------------------------------------------------------------------------|
|  GET /hello/name    |                                      |                                      | {connected True, users:{"jason","john"}}     | Display the help window                                                 |
|  /hello/name        |                                      | userappend(user)                     |                                              |                                                                         |
|  /find              |                                      | lists all users                      |                                              | Lists all users                                                         |
|  /call/target       | target/ring/user                     |                                      |                                              | Defines which user to call                                              |
|                     | {accept:True/False, port:Port}       |                                      |                                              |                                                                         |
|  /drop              |                                      |                                      |                                              | Drops connection to other user but still allows for other connections   |
|  /goodbye           |                                      |                                      |                                              | Disconnects from the server.  Does not allow new connections            |


