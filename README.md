# homelab
Here you can find script, architecture overview and test which i did in my home lab



3003 grafana -> hecha, solita
Abbiamo installato influxdb sulla 8086, telegraf e grafana. Andrebbe risolto il problema che nelle dashboard di grafana non vediamo temperatura di CPU, GPU e tutte le informazioni relative al networking.
Tutti i volumi sono mappati in docker volume

https://hub.docker.com/r/pluim003/influxdb-grafana-telegraf dove abbiamo preso l'immagine

Comando lanciato per l'installazione 

docker run -d   --name influxdb-grafana   --restart unless-stopped   -p 3003:3003   -p 8086:8086   -v /home/pi/docker-volume/influxdb:/var/lib/influxdb   -v /home/pi/docker-volume/influxdb:/var/log/influxdb   -v /home/pi/docker-volume/grafana:/var/lib/grafana   -v /home/pi/docker-volume/grafana:/var/log/grafana   -v /home/pi/docker-volume/telegraf:/var/log/telegraf   -e "GF_SECURITY_ADMIN_USER=hecha"   -e "GF_SECURITY_ADMIN_PASSWORD=AnalisiI23"   -e “TZ=Europe/Amsterdam”  pluim003/influxdb-grafana-telegraf:latest
