const express = require('express');
const app = express();
const port = 3000;

// Simulation de la BDD
const users = {
    "bob@example.com": { age: 30, city: "New York" },
    "alice@example.com": { age: 25, city: "London" }
};

// Requête de Test pour l'API
// curl "http://localhost:3000/api/users?email=john.doe@example.com"


app.use(express.json());

app.get('/api/users', (req, res) => {
    const email = req.query.email;

    if(!email) {
        return res.status(400).json({ error: "Email is required" });
    }

    const user = users[email];
    if(!user) {
        return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
});

app.listen(port, () => {
    console.log(`API listening at http://localhost:${port}`);
});