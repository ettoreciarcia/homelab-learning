# Kubernetes Networking

Nell'articolo precedente abbiamo visto quali sono i comoponenti base di un cluster Kubernetes e in che modo si susseguono gli eventi quando creiamo un Deployment mediante Kubectl.
In questo articolo proverermo a scendere un po' più nel dettaglio del Networking in Kubernetes.

Chiariamo subito un punto fondamentale. Qualunque sia la distro che utilizzate e la CNI che meglio si adatta al vostro caso d'uso, le seguenti regole saranno universali:

- Tutti i Pod possono comunicare tra loro senza NAT
- Tutti i nodi possono comunicare con tutti i Pod senza NAT. È vero anche il contrario, tutti i Pod possono comunicare con tutti i nodi senza NAT.
- L'IP con cui un Pod si "vede" nella rete sarà lo stesso indirizzo IP con cui gli altri Pod all'interno del cluster lo vedranno.

Ragioneremo per gradi andando a vedere come i Pod comunicano a diversi livelli:

- Livello 0: I due pod si trovano all'interno dello stesso namespace sullo stesso nodo.
- Livello 1: I due pod si trovano in due namespace differenti sullo stesso nodo
- Livello 2: I due pod si trovano su due nodi diversi, ma quei due nodi sono all'interno della stessa Subnet
- Livello 3: I due pod si trovano su due nodi diversi e i due nodi non si trovano nella stessa subnet

1. [Setup del laboratorio](#setuplaboratorio)
2. [Premesse](#networknamespace)
3. [Livello 0](#third-example)
4. [Livello 1](#livello1)
5. [Livello 2](#livello2)
6. [Livello 3](#Livello3)
7. [Livello 4](#Livello4)


### Setup del nostro laboratorio

#### 1. Installazione Vagrant

Utilizzeremo Vagrant per il setup delle macchine virtuali su cui andremo a testare il nostro codice.

##### OSX

```
brew cask install virtualbox
brew cask install vagrant
vagrant plugin install vagrant-vbguest
```

##### Linux

```
sudo apt-get install virtualbox
sudo apt-get install vagrant
vagrant plugin install vagrant-vbguest
```

##### Windows
```
Corri a comprare un supporto USB
Prepara il supporto USB appena comprato come avviabile della tua distro Linux preferita
Rimuovi Windows e installa Linux :)
```

Visto che andremo a sporcarci le mani con il networking, ho scelto un' immagine Docker che ha tutto il necessario per fare i test di cui abbiamo bisogno
Potete trovare l'immagine a questo repository: [wbitt/network-multitool:alpine-extra](https://hub.docker.com/r/praqma/network-multitool) 
Al posto vostro la salverei e ne valuterei l'utilizzo per aiutarvi a fare troubleshooting all'interno dei vostri cluster Kubernetes :)


#### 2. Setup delle macchine virtuali
All'interno di questa repo troverete i [Vagrantfile](https://github.com/ettoreciarcia) per il provisioning delle macchine virtuali.
Spostatevi nella directory che contiene questo file e lanciate iul comando
```
sudo vagrant up
```

State creando 3 macchine virtuali:
1. Una prima istanza con 4 GB di RAM e 2 CPU che sarà il control plane del nostro cluster
2. Una seconda istanza con 2 GB di RAM e 1 CPU che sarà un worker
3. Una terza istanza con 2 GB di RAM e 1 CPU che sarà il secondo worker

Queste 3 macchine virtuali saranno in modalità bridge con la vostra scheda di rete, avranno quindi un indirizzo IP privato della subnet del vostro host.

#### 3. SSH nelle macchine virtuali

Se avete utilizzato il Vagrantfile del punto precedente, potete raggiungere la macchina virtuale appena creata lanciando il comando 
```
ssh vagant epsilon-lab
```

Ti sarà chiesta una password, utilizza ```vagrant``` e ricorda di cambiarla se non distruggi la macchina virtuale alla fine del laboratorio.

### 2. Premesse
Prima di immergerci nel netowking abbiamo bisogno di definire in maniera chiara quali sono gli "strumentopoli" che ci serviranno tra poco:

####  Network Namespaces
Un Network namesapce è una copia dello stack di rete con i propri percorsi e regole firewall.
I sistemi Linux hanno un insieme di interfacce di rete e di tabelle di routing condivise all'interno dell'intero sistema operativo. I Network Namespace permettono di avere differenti e separati gruppi di interfacce di rete e tabelle di routing che operano in maniera indipennte l'una dall'altra.
In Linux **ogni processo comunica con un Network Namespace Stack** che fornisce uno stack di rete logico con le sue rotte, i suoi network device e le sue regole firewall. In sostanza un network namesapce stack fornisce uno stack di rete nuovo di zecca per tutti i processi all'intenro di quel namespace.
Di default, Linux assegna ogni processo al **root network namespace** che fornisce l'accesso al mondo esterno.
Per esempio, lanciando il comando ``` sudo ip netns list``` otteremo la lista di tutti i Network Namespace attualemte presenti sulla nostra instanza:
```
[root@oke-calg6knlq2q-npcn276q7rq-shu2qwemztq-3 opc]# ip netns list
56014e26-cf06-471d-a2d7-abca84ecead3 (id: 15)
f7c227ab-a2a2-4d96-8ebc-73c2d558623b (id: 14)
79fbc4d0-b4ae-4a75-b8e5-7f76d6d0a5ec (id: 12)
660c4236-e76c-4351-930d-effa1f3a26f7 (id: 10)
f5bc79c5-844e-49e5-9584-493cef20b795 (id: 2)
7ebc27cf-817d-455a-986c-0b4140d1124d (id: 8)
b1eca307-2139-44d2-bfe9-c2266495f72c (id: 13)
7a71390e-f889-46c6-8936-95f50f8dab0c (id: 11)
92e6fe9f-9dca-46be-a906-a6c6506c9354
acf85962-ca6f-420d-b716-4dc4fa521163 (id: 9)
948cb888-bff8-4e6d-a1fe-c1485d2f2b27 (id: 7)
b78f633f-efec-44d8-9601-b0654ef7a285 (id: 6)
db1318e5-7183-4e91-96b7-dd1843fd87e5 (id: 5)
a4d3f8d5-ae06-4e2a-91fb-148b1e81ca3e (id: 4)
be5d0fb9-87d2-46e2-a35d-40686c56b1ab (id: 3)
9d32d1c4-2f49-4433-a0fe-d3f364c5bfdd (id: 0)
e3694537-7617-43b9-ab78-caa0356d9d28
7b01bcc2-8e33-48a7-a95a-9d1108be48aa
f081f3de-514e-4c64-a591-362c205559a1
f6ce6e5b-1842-4bb3-a3ef-117fb369faf
```
[netns-list](img/netns-list.jpg)

A questi network namespace possiamo associare delle interfacce, quelle di cui faremo largamente uso sono le interfacce di tipo VETH (Virtual Ethernet Device)

#### VETH (Virtual Ethernet Device)
Ma cos'è una Veth? 
Dal man di Linux otteniamo questa definizione:
```
The veth devices are virtual Ethernet devices.  They can act as
       tunnels between network namespaces to create a bridge to a
       physical network device in another namespace, but can also be
       used as standalone network devices.

       veth devices are always created in interconnes
```



## Livello 0

Ci troviamo in questa situazione:

## Livello 1

## Livello 2

## Livello 3

## Livello 4
___
- Bibliografia: [Network Namespace](https://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/)