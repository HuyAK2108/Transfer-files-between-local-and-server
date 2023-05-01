# Transfer-files-between-local-and-server
This tools is used to transfer files from local to server and reverse.

*************** loc2ser.py ***************
usage: loc2ser.py [-h] [-r] src dst

positional arguments:
  src              Source location
  dst              Destination location

options:
  -h, --help       show this help message and exit
  -r, --recursive  folder


*************** ser2loc.py ***************
usage: ser2loc.py [-h] [-r] src dst

Secure copy files from server to local, src is the path to file on SERVER, des is the path on LOCAL

positional arguments:
  src              Source location
  dst              Destination location

options:
  -h, --help       show this help message and exit
  -r, --recursive  folder
