# ambari-cassandra-service
Ambari service for installing and managing Cassandra on HDP clusters. Apache Cassandra is an open source distributed database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.

Author: [Amey Jain](https://github.com/ajak6)

#### Setup
- Download HDP 2.3 sandbox VM image (Sandbox_HDP_2.3_1_VMware.ova) from [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- Import Sandbox_HDP_2.3_1_VMware.ova into VMWare and set the VM memory size to 8GB
- Now start the VM
- After it boots up, find the IP address of the VM and add an entry into your machines hosts file. For example:
```
xx.xx.xx.xx sandbox.hortonworks.com sandbox    
```
  - Note that you will need to replace the above xx.xx.xx.xx with the IP for your own VM
  
- Connect to the VM via SSH (password hadoop)
```
ssh root@sandbox.hortonworks.com
```

- To download the Cassandra service folder, run below
```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/ajak6/ambari-cassandra-service.git   /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/CASSANDRA   
```
- Restart Ambari
```
#sandbox
service ambari restart

#non sandbox
sudo service ambari-server restart
```

- Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check Cassandra -> Next -> check nodes to be present in the cluster and act as client-> Next -> Change any config you like (e.g. install dir, memory sizes, num containers or values in cassandra.yaml) -> Next -> Deploy
Add the Ip address of all the seed nodes in the ring. It can be 1 to many. Add comma separated IP/Hostname value in quotes

 ![Image](../master/screenshots/Initial-config.png?raw=true)

- On successful deployment you will see the Cassaandra service as part of Ambari stack and will be able to start/stop the service from here:
 ![Image](../master/screenshots/Installed-service-stop.png?raw=true)

- You can see the parameters you configured under 'Configs' tab
![Image](../master/screenshots/Installed-service-config.png?raw=true)


#### Remove service

- To remove the Cassandra service: 
  - Stop the service via Ambari
  - Unregister the service

  ```
export SERVICE=Cassandra
export PASSWORD=admin
export AMBARI_HOST=localhost
#detect name of cluster
output=`curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari'  http://$AMBARI_HOST:8080/api/v1/clusters`
CLUSTER=`echo $output | sed -n 's/.*"cluster_name" : "\([^\"]*\)".*/\1/p'`

curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X DELETE http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#if above errors out, run below first to fully stop the service
#curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE
  ```
  - Remove artifacts
  ```
  rm -rf /var/lib/cassandra/*
  
  ```   
  
# Contributions
Prior to receiving information from any contributor, Symantec requires that all contributors complete, sign, and submit Symantec Personal Contributor Agreement (SPCA). The purpose of the SPCA is to clearly define the terms under which intellectual property has been contributed to the project and thereby allow Symantec to defend the project should there be a legal dispute regarding the software at some future time. A signed SPCA is required to be on file before an individual is given commit privileges to the Symantec open source project. Please note that the privilege to commit to the project is conditional and may be revoked by Symantec.

If you are employed by a corporation, a Symantec Corporate Contributor Agreement (SCCA) is also required before you may contribute to the project. If you are employed by a company, you may have signed an employment agreement that assigns intellectual property ownership in certain of your ideas or code to your company. We require a SCCA to make sure that the intellectual property in your contribution is clearly contributed to the Symantec open source project, even if that intellectual property had previously been assigned by you.

Please complete the SPCA and, if required, the SCCA and return to Symantec at:

Symantec Corporation Legal Department Attention: Product Legal Support Team 350 Ellis Street Mountain View, CA 94043

Please be sure to keep a signed copy for your records.

# License
Copyright 2016 Symantec Corporation.

Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License.

You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
