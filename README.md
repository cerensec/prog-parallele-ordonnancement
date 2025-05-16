# prog-parallele-ordonnancement

## Configuration de l'environnement

### Prérequis

- Python 3.x
- Node.js
- MySQL

### Installation

1. Créer l'environnement virtuel Python :

```bash
python -m venv venv
```

2. Activer l'environnement virtuel :

- Sur Windows :

```bash
.\venv\Scripts\activate
```

- Sur Linux/Mac :

```bash
source venv/bin/activate
```

3. Installer les dépendances Python :

```bash
pip install -r requirements.txt
```

4. Installer les dépendances Node.js :

```bash
npm install
```

## Démarrage des serveurs

1. Démarrer l'API Node.js (port 3000) :

```bash
node api.js
```

2. Démarrer le serveur Python (port 8080) :

```bash
python server.py
```

## Tests des APIs

### Test de l'API Node.js (port 3000)

1. Test avec un utilisateur existant :

```bash
curl "http://localhost:3000/api/users?email=bob@example.com"
```

2. Test avec un autre utilisateur existant :

```bash
curl "http://localhost:3000/api/users?email=alice@example.com"
```

3. Test avec un utilisateur inexistant :

```bash
curl "http://localhost:3000/api/users?email=inconnu@example.com"
```

### Test du serveur Python (port 8080)

1. Test avec un ID utilisateur (remplacer {id} par un ID valide) :

```bash
curl "http://localhost:8080/user/{id}"
```

## Structure du projet

- `api.js` : Serveur Node.js (port 3000)
- `server.py` : Serveur Python (port 8080)
- `requirements.txt` : Dépendances Python
