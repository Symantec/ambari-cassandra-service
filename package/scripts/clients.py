from resource_management import *
import signal
import sys
import os
from os.path import isfile

class clients(Script):
    def configure(self,env):
        import params
        env.set_params(params)
        cassandra()

    def status(self, env):
        raise ClientComponentHasNoStatus()

    def install(self,env):
        import params
        env.set_params(params)
        print 'Install the client'
        self.install_packages(env)

if __name__ == "__main__":
  clients().execute()
