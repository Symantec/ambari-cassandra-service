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

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import commands

# server configurations
config = Script.get_config()

cassandra_home = '/etc/cassandra/'
cassandra_bin = '/usr/sbin/cassandra'
cassandra_pid_dir = config['configurations']['cassandra-env']['cassandra_pid_dir']
cassandra_pid_file = format("{cassandra_pid_dir}/cassandra.pid")

conf_dir = "/etc/cassandra/conf"
cassandra_user = config['configurations']['cassandra-env']['cassandra_user']
log_dir = config['configurations']['cassandra-env']['cassandra_log_dir']
pid_dir = '/var/run/cassandra'
pid_file = '/var/run/cassandra/cassandra.pid'

hostname = config['hostname']
user_group = config['configurations']['cluster-env']['user_group']
java64_home = config['hostLevelParams']['java_home']

template = config['configurations']['cassandra-site']['template']
defaultName = config['configurations']['cassandra-site']['defaultName']

cluster_name_py = config['configurations']['cassandra-site']['cluster_name']
seed_provider_parameters_seeds = config['configurations']['cassandra-site']['seed_provider_parameters_seeds']
hinted_handoff_throttle_in_kb=config['configurations']['cassandra-site']['hinted_handoff_throttle_in_kb']
max_hints_delivery_threads=config['configurations']['cassandra-site']['max_hints_delivery_threads']
num_tokens=config['configurations']['cassandra-site']['num_tokens']
hinted_handoff_enabled=config['configurations']['cassandra-site']['hinted_handoff_enabled']
batchlog_replay_throttle_in_kb=config['configurations']['cassandra-site']['batchlog_replay_throttle_in_kb']
authenticator=config['configurations']['cassandra-site']['authenticator']
authorizer=config['configurations']['cassandra-site']['authorizer']
permissions_validity_in_ms=config['configurations']['cassandra-site']['permissions_validity_in_ms']
partitioner=config['configurations']['cassandra-site']['partitioner']
data_file_directories=config['configurations']['cassandra-site']['data_file_directories']
commitlog_directory=config['configurations']['cassandra-site']['commitlog_directory']
disk_failure_policy=config['configurations']['cassandra-site']['disk_failure_policy']
commit_failure_policy=config['configurations']['cassandra-site']['commit_failure_policy']
key_cache_save_period=config['configurations']['cassandra-site']['key_cache_save_period']
row_cache_size_in_mb=config['configurations']['cassandra-site']['row_cache_size_in_mb']
row_cache_save_period=config['configurations']['cassandra-site']['row_cache_save_period']
saved_caches_directory=config['configurations']['cassandra-site']['saved_caches_directory']
counter_cache_save_period=config['configurations']['cassandra-site']['counter_cache_save_period']
commitlog_sync=config['configurations']['cassandra-site']['commitlog_sync']
commitlog_sync_period_in_ms=config['configurations']['cassandra-site']['commitlog_sync_period_in_ms']
commitlog_segment_size_in_mb=config['configurations']['cassandra-site']['commitlog_segment_size_in_mb']
concurrent_reads=config['configurations']['cassandra-site']['concurrent_reads']
concurrent_writes=config['configurations']['cassandra-site']['concurrent_writes']
concurrent_counter_writes=config['configurations']['cassandra-site']['concurrent_counter_writes']

memtable_allocation_type=config['configurations']['cassandra-site']['memtable_allocation_type']

index_summary_resize_interval_in_minutes=config['configurations']['cassandra-site']['index_summary_resize_interval_in_minutes']
trickle_fsync=config['configurations']['cassandra-site']['trickle_fsync']
trickle_fsync_interval_in_kb=config['configurations']['cassandra-site']['trickle_fsync_interval_in_kb']
storage_port=config['configurations']['cassandra-site']['storage_port']
ssl_storage_port=config['configurations']['cassandra-site']['ssl_storage_port']

# a,listen_address1=commands.getstatusoutput('hostname -i')
# listen_address=listen_address1.split()[0]
a,listen_address=commands.getstatusoutput("hostname -i | awk '{print $NF}'")
start_native_transport=config['configurations']['cassandra-site']['start_native_transport']
native_transport_port=config['configurations']['cassandra-site']['native_transport_port']
start_rpc=config['configurations']['cassandra-site']['start_rpc']

rpc_address=config['configurations']['cassandra-site']['rpc_address1']
rpc_port=config['configurations']['cassandra-site']['rpc_port']
broadcast_rpc_address=config['configurations']['cassandra-site']['broadcast_rpc_address']
rpc_keepalive=config['configurations']['cassandra-site']['rpc_keepalive']
rpc_server_type=config['configurations']['cassandra-site']['rpc_server_type']
thrift_framed_transport_size_in_mb=config['configurations']['cassandra-site']['thrift_framed_transport_size_in_mb']


incremental_backups = config['configurations']['cassandra-site']['incremental_backups']
snapshot_before_compaction = config['configurations']['cassandra-site']['snapshot_before_compaction']
auto_snapshot = config['configurations']['cassandra-site']['auto_snapshot']
tombstone_warn_threshold = config['configurations']['cassandra-site']['tombstone_warn_threshold']
tombstone_failure_threshold = config['configurations']['cassandra-site']['tombstone_failure_threshold']
column_index_size_in_kb = config['configurations']['cassandra-site']['column_index_size_in_kb']
batch_size_warn_threshold_in_kb = config['configurations']['cassandra-site']['batch_size_warn_threshold_in_kb']
compaction_throughput_mb_per_sec = config['configurations']['cassandra-site']['compaction_throughput_mb_per_sec']
compaction_large_partition_warning_threshold_mb = config['configurations']['cassandra-site']['compaction_large_partition_warning_threshold_mb']
sstable_preemptive_open_interval_in_mb = config['configurations']['cassandra-site']['sstable_preemptive_open_interval_in_mb']
read_request_timeout_in_ms = config['configurations']['cassandra-site']['read_request_timeout_in_ms']
range_request_timeout_in_ms = config['configurations']['cassandra-site']['range_request_timeout_in_ms']
write_request_timeout_in_ms = config['configurations']['cassandra-site']['write_request_timeout_in_ms']
counter_write_request_timeout_in_ms = config['configurations']['cassandra-site']['counter_write_request_timeout_in_ms']
cas_contention_timeout_in_ms = config['configurations']['cassandra-site']['cas_contention_timeout_in_ms']
truncate_request_timeout_in_ms = config['configurations']['cassandra-site']['truncate_request_timeout_in_ms']
request_timeout_in_ms = config['configurations']['cassandra-site']['request_timeout_in_ms']
cross_node_timeout = config['configurations']['cassandra-site']['cross_node_timeout']
endpoint_snitch = config['configurations']['cassandra-site']['endpoint_snitch']
dynamic_snitch_update_interval_in_ms = config['configurations']['cassandra-site']['dynamic_snitch_update_interval_in_ms']
dynamic_snitch_reset_interval_in_ms = config['configurations']['cassandra-site']['dynamic_snitch_reset_interval_in_ms']
dynamic_snitch_badness_threshold = config['configurations']['cassandra-site']['dynamic_snitch_badness_threshold']
request_scheduler = config['configurations']['cassandra-site']['request_scheduler']

server_encryption_options_internode_encryption = config['configurations']['cassandra-site']['server_encryption_options_internode_encryption']
server_encryption_options_keystore = config['configurations']['cassandra-site']['server_encryption_options_keystore']
server_encryption_options_keystore_password = config['configurations']['cassandra-site']['server_encryption_options_keystore_password']
server_encryption_options_truststore = config['configurations']['cassandra-site']['server_encryption_options_truststore']
server_encryption_options_truststore_password = config['configurations']['cassandra-site']['server_encryption_options_truststore_password']

client_encryption_options_enabled=config['configurations']['cassandra-site']['client_encryption_options_enabled']
client_encryption_options_keystore_password = config['configurations']['cassandra-site']['client_encryption_options_keystore_password']
client_encryption_options_keystore = config['configurations']['cassandra-site']['client_encryption_options_keystore']

internode_compression = config['configurations']['cassandra-site']['internode_compression']
inter_dc_tcp_nodelay = config['configurations']['cassandra-site']['inter_dc_tcp_nodelay']
key_cache_size_in_mb = config['configurations']['cassandra-site']['key_cache_size_in_mb']
counter_cache_size_in_mb = config['configurations']['cassandra-site']['counter_cache_size_in_mb']
seed_provider_class_name = config['configurations']['cassandra-site']['seed_provider_class_name']
seed_provider_parameters_seeds = config['configurations']['cassandra-site']['seed_provider_parameters_seeds']
index_summary_capacity_in_mb = config['configurations']['cassandra-site']['index_summary_capacity_in_mb']
