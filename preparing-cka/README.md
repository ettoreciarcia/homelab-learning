# Useful commands

Create an nginx pod

```kubectl run nginx --image=nginx```

Generate POD Manifest YAML file (-o yaml). Don’t create it(–dry-run)

```kubectl run nginx --image=nginx --dry-run=client -o yaml   > pod.yaml```

Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run)

```kubectl create deployment --image=nginx nginx --dry-run=client -o yaml```

Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file.

```kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml```

Create a service file 

```kubectl create service nodeport ns-service --tcp=80:80 --dry-run=client -o yaml```

Interact with etcd
```export ETCDCTL_API=3 ```

```etcdctl --cacert="/etc/kubernetes/pki/etcd/ca.crt" --cert="/etc/kubernetes/pki/etcd/server.crt" --key="/etc/kubernetes/pki/etcd/server.key" --endpoints=https://127.0.0.1:2379 snapshot save /opt/snapshot-pre-boot.db```