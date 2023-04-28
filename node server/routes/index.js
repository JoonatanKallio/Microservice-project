var express = require('express');
var router = express.Router();
const axios = require('axios').default;


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

//activity microservice recreational activity
router.get('/get/activity/random/recreational', function(req, res, next) {
  try{
    axios.get("http://127.0.0.1:5000/activity/recreational")
    .then(function(response) {
      res.send(response.data)
    })
  } catch (error) {
    console.log(error)
  }
});

//activity microservice relaxation activity
router.get('/get/activity/random/relaxation', function(req, res, next) {
  try {
    axios.get("http://127.0.0.1:5000/activity/relaxation")
    .then(function(response) {
      res.send(response.data)
    })
  } catch (error) {
    console.log(error)
  }
});

//Wikipedia microservice
router.get('/get/wikipedia', function(req, res, next) {
  try {
    axios.get("http://127.0.0.1:5001/wikipedia/information?input="+req.body.input)
    .then(function(response) {
      res.send(response.data)
    })
  } catch (error) {
    console.log(error)
  }
});

//Weather microservice
router.get('/get/weather', function(req, res, next) {
  try {
    axios.get("http://127.0.0.1:5002/weather/current?location="+req.body.location)
    .then(function(response) {
      res.send(response.data)
    })
  } catch (error) {
    console.log(error)
  }
});


module.exports = router;
