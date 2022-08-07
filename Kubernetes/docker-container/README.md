# Introduzione

Un contenitore docker (container) non è altro che l'insieme dei dati di cui necessita un'applicazione per essere eseguita: librerie, altri eseguibili, rami del file system, file di configurazione, script, ecc.

Possiamo vedere un container come un processo isolato.

Per distribuire un'applicazione basterà quindi creare una semplice **immagine docker**. Quest'immagine sarà utilizzata successivamente da docker per creare un container.

Un container è un'entità autosufficiente e leggera e soprattuto **portabile** in quanto distribuito in un formato standard che può essere letto ed eseguito da qualsiasi server docker.

I container sono un'alternativa alla classica virtualizzazione ma offrono una maggiore flessibilità nella gestione delle risorse e una maggiore sicurezza
Sono il classico esempio di virtualizzazione leggera e si basano sulle caratteristiche proprie del Kernel Linux, in particolare **cgroups** e **namespaces**

- *control groups*: sono lo strumento utilizzato dal kernel Linux per gestire l’utilizzo delle risorse di calcolo da parte di un gruppo specifico di processi. Grazie ai cgroups è possibile limitare la quantità di risorse utilizzate da uno o più processi. Ad esempio, è possibile limitare il quantitativo massimo di memoria RAM che un gruppo di processi può utilizzare.

- *namespaces* : sono essenzialmente dei “contenitori” che astraggono le risorse offerte dal kernel. Quando un processo fa parte di un certo namespace esso potrà accedere soltanto alle risorse presenti nel namespace.

L'incremento prestazionale dovuto all'utilizzo dei container si deve all'eliminazione di uno strato: a differenza di una macchina virtuale, i processi eseguiti da un container sono di fatto eseguiti dal sistema ospitante(Linux), usufruendo dei servizi eseguiti dal sistema che quest'ultimo esegue. Non andremo quindi a sovraccaricare il sistema caricando un altro kernel per intero per ogni VM. Possiamo vederlo come una sorta di kernel condiviso.

In un ambiente basato su container, dove quindi non è presente un Hypervisor, queste funzionalità sono assolte dal kernel del sistema operativo ospitante. Linux dispone di due caratteristiche progettate proprio per questo scopo: **Control Groups (o cgroups)** e **Namespaces**.

Osservazione: Tuttavia, ricordiamo che non è possibile eseguire container Linux direttamente sul kernel Windows (dato che, per l’appunto, non si virtualizza il sistema operativo ospite). In questi casi (host Windows ed immagini Linux), Docker ricorre comunque ad una macchina virtuale Linux, in esecuzione su HyperV.
___

## Installazione di Docker su Ubuntu

Cominciamo con l'aggiornare il nostro sistema operativo

```unix
sudo apt-get update
```

Disinstalliamo eventuali versioni di Docker

```unix
sudo apt-get remove docker docker-engine docker.io
```

Installiamo Docker

```unix
sudo apt-get install docker.io
```

A questo punto Docker dovrebbe essere già avviato e abilitato per l'avvio automatico. Nel caso in cui non dovesse esserlo lanciamo i seguenti comandi:

```unix
sudo systemctl start docker
```

```unix
sudo systemctl enable docker
```

Per controllare la versione di Docker appena installata

```unix
docker --version
```

ATTENZIONE: Per poter utilzzare Docker come utenti non sudo dobbiamo aggiungere il nostro utente al gruppo di utenti Docker. Per farlo controlliamo il nome del nostro utente lanciando il comando

```unix
whoami
```

o equivalentemente

```unix
echo $USER
```

Trovato il nome utente lo aggiungiamo al gruppo:

```unix
sudo gpasswd -a <nomeutente> docker
```

Per l'installazione di Docker su sistemi operativi diversi da Ubuntu: [Installazione di Docker su Windows](https://docs.docker.com/desktop/windows/install/)

[Installazione di Docker su Mac](https://docs.docker.com/desktop/mac/install/)

___

## Primi passi

### Creazione di un container

Possiamo cominciare a muovere i primi passi nel mondo di Docker.
Scarichiamo l'immagine del nostro primo container!

```unix
docker pull hello-world
```

A questo punto possiamo lanciarlo

```unix
docker run hello-world
```

Avremmo pututo anche lanciare direttamente il comando

```unix
docker run hello-world
```

Docker si sarebbe accorto che l'immagine non era presente in locale e la avrebbe scaricata da Docker Hub (Come Git ma per Docker!)

Ovviamente una volta scaricata l'immagine localmente non sarà necessario scaricarla ogni volta

A questo punto, lanciando il seguente comando potremo vedere una lista di tutti i container presenti

```unix
docker ps -a
```

e delle relative informazioni su di essi.
Un container Docker è caratterizzato da:

- **ID**: codice alfanumerico casuale che identifica univocamente il container
- **Image**: l'immagine da cui il container è stato generato
- **Command**: il comando che è stato lanciato all'atto della creazione del container
- **Created**: tempo trascorso dalla creazione del container
- **Status**: indica se il container è UP o, nel caso in cui sia down, indica quando è stato UP l'ultima volta
- **Portsa**: indica come sono state mappate le porte

Lanciando invece il comando

```unix
docker ps
```

riceveremo come output una lista dei container attivi.

Perchè il nostro container non è in quella lista?

Perchè il container Hello-World ha cessato di esistere un secondo dopo la sua creazione in quanto un container resta up finchè ha qualcosa da fare. Non appena ha espletato il suo compito, muore.

### Fermare e rimovere un container

Per stoppare un container utilizziamo

```unix
docker stop <id_container>
```

Per farlo ripartire:

```unix
docker restart <id_container>
```

Solo dopo averlo stoppato potremo rimuoverlo lanciando il comando

```unix
docker rm <id_container>
```

Non è necessario scrivere l'id del container per intero, bastano le prime cifre.

ATTENZIONE: Non è possibile rimuovere un container attualmente attivo

#### Immagini

Possiamo controllare le immagini dei container presenti in locale lanciando il comando:

```unix
docker images
```

e ovviamente possiamo anche rimuoverle con

```unix
docker rmi 
```

ATTENZIONE: Non è possibile rimuovere l'immagine di un docker attualmente in esecuzione o se è attualmente associata ad un Docker fermo. Se il Docker è attivo bisogna prima stopparlo, poi rimuoverlo e infine rimuovere l'immagine.

___

### Mappare porte e volumi

Con i comandi precedenti abbiamo creato un semplice container che si limitava a salutarci e, espletato questo compito, terminava.
Proviamo adesso a creare un container che fa qualcoa in più

In questo esempio utilizzeremo Docker per far girare un Web Server Apache

Di cosa abbiamo bisogno?
Sicuramente di un'immagine da cui creare il nostro container.
Quindi andiamo a fare una ricerca su [Docker Hub](https://hub.docker.com/)
L'[Immagine](https://hub.docker.com/_/httpd) fa proprio al caso nostro!
ATTENZIONE: Le immagini su Docker Hub sono sempre ben documentate!

Lanciamo il comando

```unix
docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4
```

Andiamo più nel dettaglio di questi flag

- `-d`Il serve ad avviare il container  nel nostro terminale ma in background. Non riceviamo quindi input o mostriamo output. Serve a non tenere il terminale impegnato
- `-it` serve a specificare che vogliamo un'istanza di Docker interattiva
- `--name` ci permette di associare un nome al nostro container
- `p` serve a specificare come mappare le porte. In questo caso 8080:80 significa che vogliamo raggiungere il nostro servizio sulla porta 8080 di localhost mappando la porta 80 del nostro container
- `-v` serve a mappare un volume del nostro container. Potremmo aver bisogno di volume per salvare dati in maniera persistente. Segue la forma /Directory/Locale:/volume/docker

 Una volta lanciato il comando sarà possibile visualizzare la pagina di benvenuto navigando nel nostro browser all'indirizzo
 <http://localhost:8080>
 O equivalentemente utilizzando il terminale e lanciado

 ```unix
curl http://localhost:8080
```

## Dockerfile

Proviamo ora ad avvicinarci un po' di più al mondo reale.
Iniziamo a vedere le immagini Docker che utilizziamo non come il prodotto finale, ma come un template da cui cominciare.

Per farlo abbiamo bisogno del Dockerfile: un semplice file di testo scritto in YAML che ci permette di esprimere le personalizzazioni che vogliamo apportare ai vari template.

Nell'esempio precedente abbiamo creato il nostro webserver ma il sito che vedevamo andando sulla porta 8080 era quello di default offerto da Apache. E se volessimo creare un'immagine docker pronta all'uso che ci faccia vedere il nostro sito?
E' qui che entrano in gioco i Dockerfile

### Sintassi di un Dockerfile

#### **FROM**

Tra le tante istruzioni disponibili, FROM è sicuramente quella più importante e che non può assolutamente mancare. Tramite questa istruzione specifichiamo un'immagine base da cui partire per derivare la nostra immagine personalizzata

#### **RUN**

Grazie a questa istruzione possiamo istruire Docker affinchè esegua dei comandi all'interno dell'immagine che andremo a generar. Possiamo utilizzare (suppendo di aver specificato come sistema operativo nella FROM una distro Debian) il comando RUN per installare un pacchetto con il classico comando `apt-get`

#### **COPY**

Permette di copiare un file dalla macchina locale su cui stiamo creando il Dockerfile e copiarla all'interno del File System dell'immagine creata. Ad esempio:

`COPY /PATH/LOCALE /PATH/IMMAGINE/DOCKER`

#### **ENTRYPOINT**

Questa istruzione ci permette di eseguire un comando all'interno del container non appena questo è avviato. A differenza di RUN gli effetti si avranno sul container stesso piuttosto che sull'immagine che lo ha generato

##### **CMD**

Quest'istruzione si comporta in modo diverso a seconda del fatto che l'entrypoint venga specificato o meno
