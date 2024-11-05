var mysql = require("mysql2");
var express = require("express");
var app = express();

// Set up EJS as the template engine
app.set('view engine', 'ejs');

// Serve the "views" folder
app.set('views', __dirname + '/views');

// Create MySQL connection (connect once)
var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'pfa_orange'
});

con.connect(function (err) {
    if (err) {
        console.error("Error connecting to MySQL:", err);
        return;
    }
    console.log("Connected to MySQL");
});

app.get('/schemes', (req, res) => {
    con.query('SELECT * FROM schemes', (err, result) => {
        if (err) {
            console.error("Error fetching data:", err);
            res.send("Error fetching data");
            return;
        }
        // Render the "schemes" view and pass the data
        res.render('schemes', { data: result });
    });
});

app.get('/transactions', (req, res) => {
    const userId = req.query.user_id; 
    if (!userId) {
        return res.status(400).send("User ID not provided");
    }

    con.query('SELECT * FROM transactions WHERE User_ID = ?', [userId], (error, results) => {
        if (error) throw error;
        res.render('transaction_history', { transactions: results });
    });
});

app.listen(3000,'0.0.0.0', () => {
    console.log("Server running on port 3000");
});
