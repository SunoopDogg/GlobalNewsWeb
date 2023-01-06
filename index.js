const express = require('express');
const mysql = require('mysql');
const db = require('./db.js');
const myDB = mysql.createConnection(db);

const app = express();

app.set('port', process.env.PORT || 3000);

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(app.get('port'), () => {
    console.log('Server is running on port', app.get('port'));
});