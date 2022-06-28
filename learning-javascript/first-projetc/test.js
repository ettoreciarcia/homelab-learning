const axios = require('axios').default;
const winston = require('winston');
//Testing JSON object javascript
//Creiamo la stringa e alla fine la convertiamo in un oggetto JSON usando : const obj = JSON.parse(text);

async function httpPost(request){
  await axios.post('http://hecha.homepc.it:8008/form', 
    request)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
}

tagbim = {"key1":"value1","key2":"value2"}

var request = {
  "name" : "test_name",
  "code" : "test_code",
  "subject" : "test_subject",
  "state" : "test_state",
  "start_date" : "test_startdate",
  "end_date" : "test_end_date",
  "external_data": "test_external_data",
  "extension":  "test_extension",
  "image" :  "test_image",
  // "tagbim" :  tagbim
}

request.tagbim = tagbim

console.log(request);

httpPost(request);

// await axios.post('http://hecha.homepc.it:8008/form', 
//   request)
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   });


const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'user-service' },
  transports: [
    //
    // - Write all logs with importance level of `error` or less to `error.log`
    // - Write all logs with importance level of `info` or less to `combined.log`
    //
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

//
// If we're not in production then log to the `console` with the format:
// `${info.level}: ${info.message} JSON.stringify({ ...rest }) `
//
if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple(),
  }));
}
   