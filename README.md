zk-find
=======

FIND utility for Zookeeper

*Written in Python*

Usage
-----

```
usage: zk-find.py [-h] [--hosts HOST:PORT[,HOST:PORT]] [--name REGEXP] [root]

positional arguments:
  root                  root of the search

optional arguments:
  -h, --help            show this help message and exit
  --hosts HOST:PORT[,HOST:PORT]
                        comma-separated list of hosts to connect to (default: 127.0.0.1:2181)
  --name REGEXP         regexp for matching node names
```

Example
-------

``python zk-find.py --hosts 192.168.56.110:2181``

```
/zookeeper
/zookeeper/quota
/mydata
/mydata/bucket
```

Dependencies
------------

* [Kazoo](https://github.com/python-zk/kazoo)
