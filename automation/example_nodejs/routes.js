const sqlite3 = require('sqlite3').verbose();

// Open a SQLite database file
const db = new sqlite3.Database('mydatabase.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the database.');
});

module.exports = db;
