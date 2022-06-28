const axios = require('axios').default;

console.log("Hello World");


URL = 'https://api-dev-platform.usbim.com/BimPlatformRest/api/1.0/login'

// var header = {
//     'X-USBIM-PLATFORM-SERVICE-KEY': 'q3msTz701V1yrRHMoxH0WKoCCj6kSbszCpzQTiYySqQqiOOrSiWW5gvEeu15gCmz'
// };
44
var config = {
  headers:{
    'X-USBIM-PLATFORM-SERVICE-KEY': 'q3msTz701V1yrRHMoxH0WKoCCj6kSbszCpzQTiYySqQqiOOrSiWW5gvEeu15gCmz'
  }
};

var postData = {
    'username': 'syncposte@acca.it',
    'password': '3jJ8XiXshkbYRfM'
};





// console.log("That's my token");

//  function httpPost(URL, postData, config){
//      axios.post(URL, postData, config)
//     .then(function (response) {
//       console.log(response.data.token);
//       return response.data.token;
//     })
//     .catch(function (error) {
//       console.log(error);
//     });
// }

// token = httpPost(URL, postData, config);
// console.log(token);

// const p = Promise.resolve('Hello World');

// async function example() {
//   try {
//     const value = await p;
//     console.log(value); // 👉️ "Hello World"
//   } catch (err) {
//     console.log(err);
//   }
// }


// function httpPost(URL, postData, config){
//      axios.post(URL, postData, config)
//       .then(function (response) {
//         console.log(response.data.token);
//         return response.data.token;
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
// }

// async function Post(){
//   token = await httpPost(URL, postData, config);
//   return token;
// }

// token = Post();
// console.log(token);

// async function getToken(){
//   let token = await httpPost(URL,postData, config);
//   // console.log(token);
//   return token
// }

// token = getToken();
// console.log(token);


//------------------TEST--------------------
// function axiosTest() {
//   // create a promise for the axios request
//   const promise = axios.post(URL,postData,config)

//   // using .then, create a new promise which extracts the data
//   const dataPromise = promise.then((response) => response.data)

//   // return it
//   return dataPromise
// }

// // now we can use that data from the outside!
// // axiosTest()
// //   .then(data => {
// //       response.json({ message: 'Request received!', data })
// //   })
// //   .catch(err => console.log(err))

//   async function axiosTest() {
//     const response = await axios.post(URL,postData, config);
//     return response.data.token;
// }

// token = axiosTest();
// console.log(token);

//------------------END TEST--------------------


// httpPost(URL, postData, config);

// let token = httpPost(URL, postData, config);
// console.log(token);

// async function test() {
//   return "Hello world";
// }

// test().then(console.log());

//----------------NEW TEST--------------
// async function httpPost(URL, postData, config){
//   const value = await axios.post(URL, postData, config)
//    .then(function (response) {
//      console.log(response.data.token);
//      // return response.data.token;
//    })
//    .catch(function (error) {
//      console.log(error);
//    });

//    return value;
// }

// async function test(){
// test = httpPost(URL, postData, config);
// console.log(test);
// }

// test();
//---------END NEW TEST--------------------------

// async function httpPost(URL, postData, config){

//   try {
//       const response = await axios.post(URL, postData, config)
//       // console.log(response.data.token);
//       return response.data.token;
//   } catch(error) {
//       console.log(error);
//   }

//   console.log(response);

// }

// httpPost(URL, postData, config);

let jwtToken = null;
console.log(1);

async function myFunction() {

  async function getToken() {

    return new Promise((resolve, reject) => {

      if (jwtToken !== null) {
        console.log("reusing token")
        resolve(jwtToken)
      }

      else {
        axios.post(URL, postData, config)
        .then(response => {
          console.log("getting token");
          jwtToken = response.data.token;
          resolve(jwtToken);
          console.log("sono qui")
          //setTimeout(() => {resolve(response.data.token);}, 5000)
        })
        .catch(error => {
          reject(error);
        })
      }

    });
    
  }

  try {
    let token = await getToken();
    jwtToken = token;

    // console.log("dopo await");
    console.log(token);
  } catch (error) {
    console.log(error.response.data.message);
  }


  // let token2 = await getToken();
  // console.log(token2);

// promise.catch()
}

myFunction();
console.log(jwtToken);