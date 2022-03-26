3003 grafana -> hecha, solita

We have installed influxdb on 8086, telegraf and grafana. The problem that we do not see CPU, GPU temperature and all information relating to networking should be solved in the graphana dashboards.
All volumes are mapped to docker volume 

Where we download image : [Link](https://hub.docker.com/r/pluim003/influxdb-grafana-telegraf]) 

Installation command 

docker run -d   --name influxdb-grafana   --restart unless-stopped   -p 3003:3003   -p 8086:8086   -v /home/pi/docker-volume/influxdb:/var/lib/influxdb   -v /home/pi/docker-volume/influxdb:/var/log/influxdb   -v /home/pi/docker-volume/grafana:/var/lib/grafana   -v /home/pi/docker-volume/grafana:/var/log/grafana   -v /home/pi/docker-volume/telegraf:/var/log/telegraf   -e "GF_SECURITY_ADMIN_USER=hecha"   -e "GF_SECURITY_ADMIN_PASSWORD=AnalisiI23"   -e “TZ=Europe/Amsterdam”  pluim003/influxdb-grafana-telegraf:latest


Useful Medium resource to install it without docker [Link](https://medium.com/@dorian599/iot-raspberry-pi-container-and-system-monitoring-with-influxdb-telegraf-and-grafana-a1767c38c109)
