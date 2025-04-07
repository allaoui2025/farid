const express = require('express');
const app = express();
const port = 3000;

// Servir les fichiers statiques (HTML, CSS)
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
    console.log(`Serveur en cours d'exécution sur http://127.0.0.1:${port}`);
});
