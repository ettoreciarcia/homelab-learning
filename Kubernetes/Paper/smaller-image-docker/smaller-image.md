# Smaller docker images

In questo articolo andremo a creare delle immagini Docker via via sempre più piccole di un'applicazione di prova.
L'applicazione che stiamo containerizzando è scritta in Go e si limita a rispondere a richieste HTTP ad un certo path.

Ecco il codice della nostra semplice applicazione

```Go
package main
import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", HelloServer)
	http.ListenAndServe(":8080", nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}
```

Ma prima di buttarci a capofitto nella build della del nostro container, proviamo a dare qualche definizione che ci tornerà utile più avanti!