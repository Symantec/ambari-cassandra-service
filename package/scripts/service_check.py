#!/usr/bin/env python
"""
Cassandra service checks.

"""
from __future__ import print_function
from resource_management import *
import  sys,subprocess,os
import requests
import time

class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)
        cmdfile = format("/tmp/cmds")
        File(cmdfile,
               mode=0600,
               content=InlineTemplate("CREATE KEYSPACE IF NOT EXISTS smokedemotest WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };\n"
                                  "Use smokedemotest;\n"
                                  "CREATE TABLE IF NOT EXISTS smokeusers (firstname text,lastname text,age int,email text,city text,PRIMARY KEY (lastname));\n"
                                  "INSERT INTO smokeusers (firstname, lastname, age, email, city) VALUES ('John', 'Smith', 46, 'johnsmith@email.com', 'Sacramento');\n"
                                  "DROP TABLE smokedemotest.smokeusers;\n"
                                  "DROP KEYSPACE smokedemotest;\n\n")
        )
        Execute(format("cqlsh -f {cmdfile}"))


if __name__ == "__main__":
    ServiceCheck().execute()
