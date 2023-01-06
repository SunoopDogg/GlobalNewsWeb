const mysql = require('mysql');
const myDB = mysql.createConnection(  {  
  host: 'localhost',
  port: '3306',
  user: 'SunoopDogg',
  password: '0210',
  database: 'test'
}); 

module.exports = myDB;

// myDB.connect();
 
// testQuery = "SELECT * FROM globalnewsweb;";
 
// myDB.query(testQuery, function (err, results, fields) { 
//     if (err) {
//         console.log(err);
//     }
//     console.log(results);
// });
 
// myDB.end(); 