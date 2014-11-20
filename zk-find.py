#
# This is a FIND utility for Zookeeper
#
# Author: Aleksandr Vinokurov <aleksandr.vin@gmail.com>
# Url:    https://github.com/aleksandr-vin/zk-find
#

import logging
import logging.config

try:
    logging.config.fileConfig('logging.conf')
except:
    logging.basicConfig()

logger = logging.getLogger('zk-find')

from kazoo.client     import KazooClient
from kazoo.client     import KazooState
from kazoo.exceptions import NoNodeError

def list_children(parent):
    try:
        for node in zk.get_children(parent):
            path = parent + "/" + node
            print path
            list_children(path)
    except NoNodeError:
        pass

from sys import argv

path = ''
hosts = '127.0.0.1:2181'
if len(argv) > 2:
    hosts = argv[1]
    path  = argv[2]
elif len(argv) > 1:
    path  = argv[1]

def my_listener(state):
    if state == KazooState.LOST:
        logger.debug('Session lost')
    elif state == KazooState.SUSPENDED:
        logger.debug('Session suspended')
    else:
        logger.info('Session connected')

zk = KazooClient(hosts=hosts)
zk.add_listener(my_listener)
zk.start()
list_children(path)
zk.stop()
