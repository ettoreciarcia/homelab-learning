const os = require("os")

/*
ARROW FUNCTIONS
*/
let add = function (x, y) {
	return x + y;
};

console.log(add(1,3));

let test = (x , y) => {return x + y; };
console.log(test(1,4));

let hello = () => {return "Hello World!"; };
console.log(hello());


/*
Call back: funzione passata come argomento ad un'altra funzione. Questa tecnica consente ad una funzione di chiamare un'altra funzione.
IMPORTANTE: le funzioni in js vengono eseguite nell'ordine in cui sono chiamate, non in quello in cui sono definite

Nei flussi sincroni potremmo dover aspettare molto per fare alcune operazioni. NodeJS, essendo asicrono, non aspetta che le funzioni eseguano i loro calcoli
ma usa le callbacks. Quando una determinata funzione termina viene chiamata una funzione di callback, in questo modo il flusso non si ferma
*/

console.log(os.uptime());
console.log(os.userInfo());