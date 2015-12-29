#!/usr/bin/env python
"""
Cassandra service params.

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def cassandra():
    import params

    Directory([params.log_dir, params.pid_dir, params.conf_dir],
              owner=params.cassandra_user,
              group=params.user_group,
              recursive=True
          )
    configurations = params.config['configurations']['cassandra-site']

    File(format("{conf_dir}/cassandra.yaml"),
       content=Template(
                        "cassandra.master.yaml.j2", 
                        configurations = configurations),
       owner=params.cassandra_user,
       group=params.user_group 
    )
