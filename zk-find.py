#
# This is a FIND utility for Zookeeper
#
# Author: Aleksandr Vinokurov <aleksandr.vin@gmail.com>
# Url:    https://github.com/aleksandr-vin/zk-find
#

import logging
import logging.config
import argparse

try:
    logging.config.fileConfig('logging.conf')
except:
    logging.basicConfig()

logger = logging.getLogger('zk-find')

from kazoo.client     import KazooClient
from kazoo.client     import KazooState
from kazoo.exceptions import NoNodeError
import re

def list_children(parent,prog):
    try:
        for node in zk.get_children(parent):
            path = parent + "/" + node
            if prog:
                if prog.search(node):
                    print path
                else:
                    pass
            else:
                print path
            list_children(path,prog)
    except NoNodeError:
        pass
    except ValueError as e:
        print 'ValueError: %s' % (e)

def my_listener(state):
    if state == KazooState.LOST:
        logger.debug('Session lost')
    elif state == KazooState.SUSPENDED:
        logger.debug('Session suspended')
    else:
        logger.info('Session connected')

# defaults
defaults = {
    'hosts' : '127.0.0.1:2181'
    ,'root' : ''
}

parser = argparse.ArgumentParser(epilog='''
Report (and track progress on fixing) bugs via the github issues
page at https://github.com/aleksandr-vin/zk-find/issues or,
if you have no web access, by sending email to <aleksandr.vin+bug-zk-find@gmail.com>.
''')
parser.add_argument('root', nargs='?', type=str,
                    help='root of the search', default='%s' % defaults['root'],);
parser.add_argument('--hosts', default='%s' % defaults['hosts'],
                    type=str, metavar='HOST:PORT[,HOST:PORT]', dest='hosts', required=False,
                    help='comma-separated list of hosts to connect to (default: %s)' % defaults['hosts'])
parser.add_argument('--name',
                    type=str, metavar='REGEXP', dest='name',
                    help='regexp for matching node names')

if __name__ == "__main__":
    # setting run-time args by the command-line parameters
    settings = parser.parse_args()
    zk = KazooClient(hosts=settings.hosts)
    zk.add_listener(my_listener)
    zk.start()
    global prog
    prog = None
    if (settings.name):
        prog = re.compile(settings.name)
    list_children(settings.root,prog)
    zk.stop()
