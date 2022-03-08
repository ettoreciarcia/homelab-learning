const express = require('express')
const app = express()
const port = 3000
const fs = require('fs');
var logger = require('morgan')

//logging
app.use(logger('combined', {
  stream: fs.createWriteStream('./access.log', {flags: 'a'})
}));
app.use(logger('dev'));
//end logging

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/random', (req, res) => {
  res.send('You are in random path and you are using GET method')
})

app.post('/random', (req, res) => {
  res.send('You are in random path and you are using POST method')
})

app.put('/random', (req, res) => {
  res.send('You are in random path and you are using PUT method')
})

app.delete('/random', (req, res) => {
  res.send('You are in random path and you are using delete method')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

//Serve a file in public directory
app.use(express.static('public'))



app.get('/index', (req,res) =>{
  let index = Math.floor(Math.random() * 11);
  res.send('Your index value is equal to' + index)
  console.log('Value generate for user is equal to ' + index)
})
