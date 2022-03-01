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

## What do I have available

### - Computing Power

#### RaspberryPi 4

I recently bought a second-hand Raspberry Pi (The prices of these toys have skyrocketed lately due to supply chain problems).
It's a 4 GB RAM And it comes with a 32 SD card.
OS: Raspbian for ARM 64

<img src="img/Raspberry.jpg " alt="Raspberry" width="200"/>

Isn't it very tender?

### Asus P550C

To get a little more computing power, I also used an old computer, a veteran.
He accompanied me throughout my university career and now we will do another piece of travel together.
This is an Asus P550C, third generation i5 and 4GB of RAM, 256 GB SSD.
It will be useful for doing things that you can't **yet** do on an ARM architecture.
OS: Ubuntu Desktop 21.10

<img src="img/PC.jpg " alt="Asus P550C" width="300"/>

After 7 years it's still on track

### Storage

#### Old HDD

An old 500 GB HDD, I'll use it to extend the raspberry storage.
Maybe in the future I will buy a NAS :)

<img src="img/HDD.jpg " alt="HDD" width="200"/>

## Monitoring

Here you can find an architecture overview of my monitoring tool.

<img src="img/monitoring.jpg " alt="HDD" width="500"/>

What i use:
- **Telegraf** to push logs and metrics to InfluxDB. This It is the agent that I have installed on the servers to be monitored.
- **InfluxDB** to store logs and metrics. I installed it in a docker container. I mapped port 8086 on my Ubuntu Server tith port 8086 on docker container.
I mapped volumes too.
- **Grafana** to view metrics and logs in dashboard. Also for Grafana I preferred to use a docker container, this time mapping port 300 on Ubuntu Server with port 3000 on Docker Container

Final Result:

<img src="img/MonitoringDash2.jpg " alt="HDD" width="500"/>

<img src="img/MonitoringDash1.jpg " alt="HDD" width="500"/>


## External Access

