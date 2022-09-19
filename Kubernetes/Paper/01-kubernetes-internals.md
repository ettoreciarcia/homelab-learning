# Kubernetes internals

Tutti abbiamo lanciato il comando 
```kubectl run nginx-pod --image=nginx:latest```

E abbiamo potuto ammirare soddisfatti il nostro pod in esecuzione all'interno del cluster Kubernetes.
Ma cosa c'è dietro? Quale "magia" si cela dietro K8s affinchè quel pod possa esser "preso in carico" e avviato all'interno del cluster?

In questo articolo daremo una panoramica di quelli che sono gli attori coinvolti, sorvolando per il momento ciò che riguarda il netowrking.

Saranno coinvolti i seguenti componenti:

1. **Api Server** che ci permette di interagire con il cluster tramite chiamate API. Possiamo vederlo come il front end del control plane di Kubernetes. È progettato per scalare orizzontalmente, cioè scala aumentando il numero di instanze. Possiamo eseguire multiple istanze di kube-apiserver e bilanciare il traffico tra queste istanze

2. **Scheduler** schedulerà ed allocherà i nostri pod sulle macchine worker. Controlla i pod appena creati che non hanno un nodo assegnato e, dopo averlo identificato, glielo assegna. I fattori presi in considerazioni nell'individuare un nodo a cui assegnare l'esecuzione di un Pod includono la richiesta di risorse del Pod stesso e degli altri workload presenti nel sistema, i vincoli delle hardware/software/policy, le indicazioni di affinity e di anti-affinity, requisiti relativi alla disponibilità di dati/volumi, le interferenze tra diversi workload e le scadenze

3. **Controller** sono diversi applicativi che vanno a verificare lo stato del cluster interagendo con l'API server e controllano lo stato del cluster confrontandolo con quello desiderato dall'utente. Nel caso in cui questi due stati non combacino, lo scheduler sarà responsabile di far convergere lo stato del cluster verso quello desiderato dall'utente

4. **etcd** è un archivio dati di tipo chiave valore distribuito e ridondato. Serve a mantenere lo stato del cluster.

5. **Kubelet** un agente che è eseguito su ogni nodo del cluster. Si assicura che i container siano eseguiti in un pod.

6. **kube-proxy** è un proxy eseguito su ogni nodo del cluster, responsabile della gestione dei kubernetes service. I kube proxy mantengono le regole di networking sui nodi, queste regole permettono la comunicazione verso altri nodi del cluster o l'esterno.


[ TODO: CREARE DISEGNO CON TUTTI I COMPONENTI ELENCATI SOPRA]

[TODO ENTRARE NEL DETTAGLIO DI QUESTI STEP]

1. Lanciamo il comando "kubectl run .. "
2. Kubectl genera il manifest che descirve il pod
- Aggiungere autenticazione sull'api Server (?) 
3. Il manifest viene mandato all'API Server
4. L'API server valida il manifest
5. L'API server aggiorna lo stato di etcd
6. Un controller viene attivato e si accorge che lo stato presente in etcd non "matcha" con lo stato desidrato dall'utente
7. Questo "missmatch" tra stato attuale e stato desiderato attiva lo scheduler che deve decidere su quale dei nodi lanciare il pod
8. Deciso il nodo, le operazioni vengano affidate alla kubelet
9. La kubelet lancia il pod che contiene il container desiderato e contatta il control plane