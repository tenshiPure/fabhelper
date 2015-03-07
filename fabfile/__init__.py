from fabric.api import local, run, env, put, get, cd, lcd

env.hosts = ['192.168.100.10']
env.user = 'vagrant'
env.password = 'vagrant'


def test():
  run("uname -a")
