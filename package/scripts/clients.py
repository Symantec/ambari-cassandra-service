#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
