var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  const userAgent = req.header('User-Agent')
  const header = req.header('Accept-Language')
  
  res.send('That s your user agent ' + header);
  
});

module.exports = router;