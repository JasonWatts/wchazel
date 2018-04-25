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

- Issue Tracker: submit an issue at this page: https://gitlab.com/wchazel/hazelproject-server/hazel-server
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

|Sent by | Sent to | Route | purpose | return values | side effect | comments |
|  ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|  jasper | client | hello i am alice | introduce the client to the server in response to spoken "Hazel, hello. I am Alice." |  | http://server:1007/hello/alice | We could have the actual words spoken to hazel be "Hazel I am Alice" with 'hello' implied. |
|  client | server | /hello/alice |  | { connected: True, users: { "alice", "bob" }} | Insert alice, ipnumber into users{} |  |
|  jasper | client | find | see who can be connected to |  | http://server:1007/find |  |
|  client | server | /find | see who can be connected to | { users: { "alice", "bob" }} | none |  |
|  jasper | client | /call/bob | Make a connection to Bob | { connect: { users[Bob].port }} | open up streaming port X, http://server:1007/call/bob/X  |  |
|  client | server | /call/bob/IP:PORT | Make a connection to Bob | { request_received: True } | Receives a request to connect with caller<br/>sets user[Alice].IP=X<br/>http://user[bob].IP/ring/alice |  |
|  server | client | /ring/alice | Ask client if OK to talk with Alice | { accept: True } or { accept: False } | Asks the person to "answer" the call, and start to conversation.<br/>if (accept) then http://user[alice].IP/accept/bob<br/>else http://user[alice].IP/drop/bob |  |
|  client | jasper | /ring/alice | convert request to spoken "OK to talk with Alice?" |  | Listen for Yes/No response |  |
|  jasper | client | accept alice | if user says 'Yes' | { connected: True} | http://server:1007/accept/alice |  |
|  client | server | /accept/alice | Accepts connection with Alice | { user[Alice].IP, user[Alice].port } | bob connects stream to user[alice].IP:user[alice].Port |  |
|  jasper | client | drop alice | If user says "no" | { connected: False} | http://server:1007/drop/alice |  |
|  client | server | /drop/alice | Disconnects Alice if already connected, declines to connect if not |  | Drops connection to Alice but still allows for other connections |  |
|  jasper | client | /goodbye | Leave the server in response to "Hazel, goodbye" | { connected: False, users.remove[X]} | Removes user from the user JSON array |  |
|  jasper | client | call kclu | connect to stream at kclu |  |  | the url is https://kclustream.callutheran.edu:8090/kclump3?id=jp_audio_0<br/>This can be done by adding a special user{} entry called kclu and attaching it to a port Z on the server, and passing the server's IP and port Z to the client... |
|  client | server | /call/kclu |  |  | http://client:1007/ring/kclu/kcluPort |  |
