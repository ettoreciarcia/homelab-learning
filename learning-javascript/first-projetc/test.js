const axios = require('axios').default;

axios.post('http://hecha.homepc.it:8008/form', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
