# ambari-cassandra-service
Ambari service for installing and managing Cassandra on HDP clusters. Apache Cassandra is an open source distributed database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.

Author: [Amey Jain](https://github.com/ajak6)


....

- Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check Cassandra -> Next -> check nodes to be present in the cluster and act as client-> Next -> Change any config you like (e.g. install dir, memory sizes, num containers or values in cassandra.yaml) -> Next -> Deploy


- On successful deployment you will see the Flink service as part of Ambari stack and will be able to start/stop the service from here:
 ![Image](../master/screenshots/Installed-service-stop.png?raw=true)

- You can see the parameters you configured under 'Configs' tab
![Image](../master/screenshots/Installed-service-config.png?raw=true)


#### Remove service

- To remove the Cassandra service: 
  - Stop the service via Ambari
  - Unregister the service
  -     ```
export SERVICE=Cassandra
export PASSWORD=admin
export AMBARI_HOST=localhost
#detect name of cluster
output=`curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari'  http://$AMBARI_HOST:8080/api/v1/clusters`
CLUSTER=`echo $output | sed -n 's/.*"cluster_name" : "\([^\"]*\)".*/\1/p'`

curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X DELETE http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#if above errors out, run below first to fully stop the service
#curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

 - Remove artifacts
    ```
    rm -rf /opt/flink*
    rm /tmp/flink.tgz
    ```   
