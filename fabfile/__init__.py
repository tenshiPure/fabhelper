from fabric.api import env

env.hosts = ['192.168.100.10']
env.user = 'vagrant'
env.password = 'vagrant'

# import samples

import result
import yum
import service
