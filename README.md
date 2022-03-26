# Homelab & Learning

Hello everyone!

I will use this space to share with you what I do in my home lab.
I hope that someone with a higher seniority than mine can give me advice on what can be improved and things you can add and to create new connections with people who have the same passions as me.

## Index

- [What do i have available](#what-do-i-have-available)
- [Monitoring](#monitoring)
- [Architecture Overview](#test)
- [External Access](#external-access)
- [Learning Material](#learning)
- [Personal Project](#personal-project)
- [Kubernetes](#Kubernetes)

## What do I have available

### - Computing Power

#### RaspberryPi 4

I recently bought a second-hand Raspberry Pi (The prices of these toys have skyrocketed lately due to supply chain problems).
It's a 4 GB RAM And it comes with a 32 SD card.
OS: Raspbian for ARM 64

<center><img src="img/Raspberry.jpg " alt="Raspberry" width="500"/></center>

Isn't it very tender?

### Asus P550C

To get a little more computing power, I also used an old computer, a veteran.
He accompanied me throughout my university career and now we will do another piece of travel together.
This is an Asus P550C, third generation i5 and 4GB of RAM, 256 GB SSD.
It will be useful for doing things that you can't **yet** do on an ARM architecture.
OS: Ubuntu Desktop 21.10

<center><img src="img/PC.jpg " alt="Asus P550C" width="500"/></center>

After 7 years it's still on track

### Storage

#### Old HDD

An old 500 GB HDD, I'll use it to extend the raspberry storage.
Maybe in the future I will buy a NAS :)

<!-- <center><img src="img/HDD.jpg " alt="HDD" width="400"/></center> -->

## Monitoring

Here you can find an architecture overview of my monitoring tool.

<center><img src="img/Monitoring.jpg " alt="ArchitectureMonitoring" width="600"/></center>

What i use:
- **Telegraf** to push logs and metrics to InfluxDB. This It is the agent that I have installed on the servers to be monitored.
- **InfluxDB** to store logs and metrics. I installed it in a docker container. I mapped port 8086 on my Ubuntu Server tith port 8086 on docker container.
I mapped volumes too.
- **Grafana** to view metrics and logs in dashboard. Also for Grafana I preferred to use a docker container, this time mapping port 300 on Ubuntu Server with port 3000 on Docker Container

Final Result:

<center><img src="img/MonitoringDash2.jpg " alt="DashMonitoring1" width="700"/></center>

<center><img src="img/MonitoringDash1.jpg " alt="DashMonitoring2" width="700"/></center>

## External Access

To access my homelab from Internet i create a VPN using OpenVPN. Also in this case it is a dockerized solution.
This is a blue print of my architecture for external access:

<center><img src="img/ExternalAccess.jpg " alt="DashMonitoring2" width="600"/></center>

You know, public ip addresses (if you don't have an enterprise contract) are like Hoghwarts ladders, they like to change.
To solve the problem I have configured a dynamic DNS, So if my public IP address changed as well, I would still refer to the same DDNS.

I use this [docker image](https://hub.docker.com/r/kylemanna/openvpn/).

Remember to map the traffic on your modem / router properly, otherwise you will not be able to reach the server running this docker image on the right port!

## Kubernetes

Here you will find a collection of Kubernetes resources