var app = require('express')();
var request = require('request-promise');

var REQ_URL = 'http://127.0.0.1:80';
REQ_URL = (process.argv[2]) ? process.argv[2] : REQ_URL;
console.log(process.argv);

app.get('*', function(req, res) {
	request({
		method: 'GET',
		uri: REQ_URL + req.url
	}).then(rp => {
		res.set('Access-Control-Allow-Origin', '*');
		res.json(JSON.parse(rp));
	}).catch(err => {
		console.log(err);
		res.json({});
	});
});

var PORT = 8080;
app.listen(PORT, _ => console.log('reflecting ' + REQ_URL + ' on ' + PORT));
