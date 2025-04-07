const express = require('express');
const app = express();
const port = 3000;

// Simulation de la BDD
const users = {
    "john.doe@example.com": { age: 30, city: "New York" },
    "jane.smith@example.com": { age: 25, city: "London" },
    "alice.wonderland@example.com": { age: 28, city: "Paris" }
};

app.use(express.json());

app.get('/api/users', (req, res) => {
    const email = req.query.email;

    if(!email) {
        return res.statuts(400).json({ error: "Email is required" });
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