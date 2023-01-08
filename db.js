const mysql = require("mysql2/promise");
const myDB = mysql.createConnection({
  host: "localhost",
  port: "3306",
  user: "SunoopDogg",
  password: "0210",
  database: "test",
});

module.exports = myDB;
