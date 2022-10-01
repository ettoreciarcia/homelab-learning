# Il tuo cluster personale

Kubernetes è un progetto ormai sulla bocca di tutti. 
Nato nel 2014 in Google sotto il nome di Borg, è attualmente mantenuto dalla Cloud Native Computing Foundation.
Dopo l'avvento dei container serviva una tecnologia che permettesse di gestire i moltissimi "contenitori" in cui le applicazioni monolitiche erano state "divise".
Kubernetes risolve questo problema e ad oggi rappresenta lo standard de facto dell'orchestrazione di container.

È attualmente usato per gestire i carichi di lavoro di aziende Enterprise che fanno giarare centinaia o migliaia di container.

Ma come possiamo avvicinarci a Kubernetes? 

In quanto progetto open source la community è molto attiva e nel corso degli anni sono nate diverse soluzioni che permettono di avere un cluster Kubernetes nel proprio homelab in pochi minuti.

- **Minikube**: Crea una macchina virtuale come nodo singolo di K8S. Necessita quindi di un Hypervisor. Per chi comincia, questo tool è un must. In pochi minuti si ha il cluster up e si è pronti a lavorare utilizzando kubectl

- **Kind**: anche questo è un progetto Kubernetes ma a differenza di Minikube sposta il nodo all'interno di un container Docker. Questo significa che è sensibilmente più veloce rispetto a Minikube. Kind prevede anche un flag per creare più istanze Docker con Kubernetes in parallelo.
Permette anche di caricare le immagini direttamente nel cluster from local

- **K3s**: è una versione più leggera di Kubernetes sviluppata da Rancher Labs. Si divide in K3s Server e Agent.È particolarmente performante su dispositivi ARM

### Minkube VS Kind VS K3S 1
|   | Minikube  | Kind   | K3s  |
|---|---|---|---|
| runtime  | VM  | container   |  native |
|  supported architectures |  AMD64 |  AMD64 | AMD64, ARMv7, ARM64  |
| supported container runtime  | Docker,CRI-O,containerd,gvisor  |  Docker |  Docker, containerd |
|  start up time |  5:19 / 3:15 |  2:48 / 1:06 |   	0:15 / 0:15 |
| memory Requirements  |  2GB | 8GB (Windows, MacOS)  |  512 MB |
| Requires root?  |  no  | no  |  yes |
| Multi Cluster Support | yes  | yes  | no  |
| Multi Node support  | no  | no  | yes  |

