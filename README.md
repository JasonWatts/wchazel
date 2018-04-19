
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



|                         | Prefix Verb |  URI Pattern                         |   Controller#Action
|-------------------------|-------------|--------------------------------------|--------------------------------------|
|   request_attachments   | GET         | /request_attachments(.:format)       |   request_attachments#index
|                         | POST        | /request_attachments(.:format)       |   request_attachments#create
|   new_request_attachment| GET         | /request_attachments/new(.:format)   |   request_attachments#new
|  edit_request_attachment| GET         | /request_attachments/:id/edit(.:f    |   request_attachments#edit
|       request_attachment| GET         | /request_attachments/:id(.:format)   |   request_attachments#show
|                         | PATCH       | /request_attachments/:id(.:format)   |   request_attachments#update
|                         | PUT         | /request_attachments/:id(.:format)   |   request_attachments#update
|                         | DELETE      | /request_attachments/:id(.:format)   |   request_attachments#destroy
|         file_attachments| GET         | /file_attachments(.:format)          |   file_attachments#index
|                         | POST        | /file_attachments(.:format)          |   file_attachments#create
|      new_file_attachment| GET         | /file_attachments/new(.:format)      |   file_attachments#new
|     edit_file_attachment| GET         | /file_attachments/:id/edit(.:format) |   file_attachments#edit
|          file_attachment| GET         | /file_attachments/:id(.:format)      |   file_attachments#show
|                         | PATCH       | /file_attachments/:id(.:format)      |   file_attachments#update
|                         | PUT         | /file_attachments/:id(.:format)      |   file_attachments#update
|                         | DELETE      | /file_attachments/:id(.:format)      |   file_attachments#destroy
|   costs_populate_options| GET         | /costs/populate_options(.:format)    |   costs#populate_options
|      costs_get_estimate | GET         | /costs/get_estimate(.:format)        |   costs#get_estimate
|        new_dependency   | GET         | /costs/new_dependency(.:format)      |   costs#new_dependency

