zk-find
=======

FIND utility for Zookeeper

*Written in Python*

Usage
-----

``python zk-find [hosts] [root]``

Example
-------

``python zk-find.py 192.168.56.110:2181 ''``

```
/zookeeper
/zookeeper/quota
/mydata
/mydata/bucket
```

Dependencies
------------

* [Kazoo](https://github.com/python-zk/kazoo)
