
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

    | Function name  | Description                                                            |
    | -------------- |------------------------------------------------------------------------|
    |  GET/          | Display the help window.                                               |
    |  FIND/         | Lists all users                                                        |
    |  CALL/TARGET   | Defines which user to call                                             |
    |  DROP/         | Drops connection to other user but still allows for other connections  |
    |  GOODBYE/      | Disconnects from the server.  Does not allow new connections           |
    |  /HELLO/BOB    | Pushes string "Hello NAME" to client                                   |

| Server API          |    Client API                        |   Action                             |  Return                                      |
|---------------------|--------------------------------------|--------------------------------------|----------------------------------------------|
|  GET /hello/name    |                                      |                                      | {connected True, users:{"jason","john"}}     |
|  /hello/name        |                                      | userappend(user)                     |                                              |
|  /find              |                                      | lists all users                      |                                              |
|  /call/target       | target/ring/user                     |                                      |                                              |
|                     | {accept:True/False, port:Port}       |                                      |                                              |
|  /drop              |                                      |                                      |                                              |
|  /goodbye           |                                      |                                      |                                              |


