var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;


function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function httpPost(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function httpPostJSON(theUrl,data)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", theUrl, false ); // false for synchronous request
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify(data));
    return xmlHttp.responseText;
}

console.log("Testing HTTP GET request ... ");
let URL_GET= "http://raspberry:8080/"
let response = httpGet(URL_GET);
console.log(response);

console.log("Testing HTTP POST request ...");
let URL_POST = ("http://raspberry:8080/helloPerson?firstname=Ettore");
let response_post = httpPost(URL_POST);
console.log(response_post);

console.log("Testing HTTP POST with json request ...");
let URL_LOCAL = "http://localhost:8008/form"
let test = {
    "employees":[
      {"firstName":"Ettore", "lastName":"Doe"},
      {"firstName":"Anna", "lastName":"Smith"},
      {"firstName":"Peter", "lastName":"Jones"}
    ]
    }
let response_post_json = httpPostJSON(URL_LOCAL, test);





