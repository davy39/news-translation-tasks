---
title: Comment configurer l'authentification par lien magique avec React, Flask et
  Authsignal
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2024-01-11T18:40:41.000Z'
originalURL: https://freecodecamp.org/news/set-up-magic-link-authentication-with-react-flask-and-authsignal
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/magic-link-authsignal.png
tags:
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
- name: React
  slug: react
seo_title: Comment configurer l'authentification par lien magique avec React, Flask
  et Authsignal
seo_desc: 'Authentication is the process of verifying the identity of a user or system.
  It ensures that only authorized individuals or systems can access certain resources
  or perform specific actions.

  Magic Link Authentication offers a simple yet secure way for...'
---

L'authentification est le processus de vérification de l'identité d'un utilisateur ou d'un système. Elle garantit que seuls les individus ou systèmes autorisés peuvent accéder à certaines ressources ou effectuer des actions spécifiques.

L'authentification par lien magique offre une méthode simple mais sécurisée pour permettre aux utilisateurs de se connecter sans mot de passe. Ce tutoriel vous guidera à travers la mise en œuvre de l'authentification par lien magique en utilisant React pour le front-end, Flask pour le back-end et le service d'authentification fourni par [Authsignal](https://www.authsignal.com/).

### Table des matières :

1. [Comprendre l'authentification par lien magique](#heading-comprendre-lauthentification-par-lien-magique)
2. [Comment configurer Authsignal](https://www.freecodecamp.org/news/set-up-magic-link-authentication-with-react-flask-and-authsignal/how-to-configure-authsignal)
3. [Flux de l'application](#heading-flux-de-lapplication)
4. [Comment configurer votre serveur back-end](#heading-comment-configurer-votre-serveur-backend)
5. [Comment configurer les variables d'environnement](#heading-comment-configurer-les-variables-denvironnement)
6. [Comment initialiser le client Authsignal](#heading-comment-initialiser-le-client-authsignal)
7. [Actions Authsignal](#heading-actions-authsignal)
8. [Comment créer les routes requises](#heading-comment-creer-les-routes-requises)
9. [Comment configurer un nouveau projet React en front-end](#heading-comment-configurer-un-nouveau-projet-react-en-frontend)
10. [Comment configurer les composants](#heading-comment-configurer-les-composants)
11. [Comment exécuter l'application](#heading-comment-executer-lapplication)
12. [Conclusion](#heading-conclusion)

## Comprendre l'authentification par lien magique

L'authentification par lien magique est une méthode d'authentification pratique et sécurisée qui simplifie le processus de connexion des utilisateurs. Au lieu de saisir un nom d'utilisateur et un mot de passe, les utilisateurs reçoivent un lien unique par e-mail. Ce lien, connu sous le nom de lien magique, leur donne accès à leur compte sans identifiants traditionnels.

Une différence clé entre l'authentification par lien magique et l'authentification avec vérification par e-mail est l'expérience utilisateur. Avec l'authentification par lien magique, les utilisateurs peuvent s'authentifier avec un seul clic. Ils n'ont pas besoin de se souvenir ou de saisir un mot de passe, ce qui peut être particulièrement bénéfique pour les utilisateurs qui ont du mal à gérer les mots de passe ou qui trouvent inconvénient de saisir leurs identifiants à plusieurs reprises.

Bien que la vérification par e-mail ajoute une couche de sécurité supplémentaire, elle peut nécessiter que l'utilisateur se souvienne de ses identifiants ou passe par plusieurs étapes avant d'accéder à son compte. Si vous souhaitez en savoir plus sur la vérification par e-mail, vous pouvez consulter mon article [ici](https://blog.ashutoshkrris.in/how-to-set-up-email-verification-in-a-flask-app) pour approfondir le sujet.

## Comment configurer Authsignal

[Authsignal](https://www.authsignal.com/) est un service qui facilite la mise en œuvre de méthodes d'authentification modernes (comme les liens magiques et les clés d'authentification). Il fournit des outils simples pour intégrer des méthodes de connexion sécurisées dans vos applications web sans tracas.

Avant de poursuivre le tutoriel, vous devez créer un compte Authsignal. Pour ce faire, vous pouvez suivre ces étapes :

Tout d'abord, allez sur [authsignal.com](https://portal.authsignal.com/users/sign_up) et cliquez sur "Créer un compte gratuit".

À l'étape suivante, créez votre premier locataire. Choisissez un nom pour votre locataire et sélectionnez la région de stockage des données.

![Image](https://lh7-us.googleusercontent.com/PoQ1Jl8b1fNXmzruv750erSeyi4jxnVlI_QAvoHDH6-O6GVHmDQ07yd2U7WxHrYTUMCyKowll7W-Bs0dBuet9KqiF-mZuV_w8IbFO5tpYziI5M5kaO1ipWEaJPJ7dkPWTNtXyib-BE-8S5VcVtanNNc)
_Création d'un locataire sur Authsignal_

Ensuite, vous devez configurer les authentificateurs que vous souhaitez utiliser pour votre application. Par exemple, j'ai activé le lien magique par e-mail et l'application d'authentification (TOTP).

![Image](https://lh7-us.googleusercontent.com/AagTYGVbXToDeHqe4S-lFUx2qgIerUbzlUnGTv3sxZ2EyPBzfDeXNcvT-_oeQksckyhGFHX2YY6g8heKHdIz18qf2N_ejed9fJDFA_pSMzfKX3d5Tid4eDnrn7PUbEX_zVh10urhFa49Ek-eSYZJdAA)
_Configuration des authentificateurs_

Une fois que vous avez configuré l'authentificateur, accédez à l'option Clés API. Ici, vous trouverez votre clé secrète, qui sera nécessaire pour la mise en œuvre de l'authentification.

![Image](https://lh7-us.googleusercontent.com/UJgdqGLl6IRK8sr3NOsf1BXVp7EJpSFMkxTzdRw0QNhz7DqL5fyGMn7KBotMvrp3ivZnYtw8M-fdVX-aJgNrdszRyAziVCxIAXAxb-g8r42F9ZgQFlpm9D1FYicnhuS4DcS5V7hZ430FM5ruEUioiSw)
_Trouver votre clé secrète_

## Flux de l'application

Comprenons le flux de l'application :

### Première visite

* L'utilisateur visite l'interface utilisateur de l'application. Sur l'interface utilisateur, il voit une boîte de connexion et une option d'inscription. Comme l'utilisateur est nouveau, il choisit de s'inscrire.

### Flux d'inscription

* En cliquant sur le lien d'inscription, l'utilisateur est dirigé vers une page pour entrer son nom d'utilisateur choisi.
* Après avoir entré le nom d'utilisateur et cliqué sur le bouton d'inscription, le front-end déclenche un appel API POST à /api/signup, envoyant le nom d'utilisateur dans le corps de la requête.
* Le back-end reçoit la requête et communique avec le serveur Authsignal pour l'authentification de l'utilisateur.
* Authsignal invite l'utilisateur à configurer l'authentification par lien magique en entrant son adresse e-mail.
* Authsignal envoie un lien magique à l'adresse e-mail fournie.
* Après avoir cliqué sur le lien magique, l'utilisateur est authentifié et redirigé vers la page d'accueil, où il reçoit un message de bienvenue affichant son adresse e-mail. La page comprend également un bouton de déconnexion.

### Flux de connexion

* L'utilisateur se déconnecte et retourne à la page de connexion.
* Ici, l'utilisateur entre son nom d'utilisateur enregistré et clique sur le bouton de connexion.
* En cliquant sur Connexion, le front-end déclenche un appel API POST à /api/login, passant le nom d'utilisateur dans le corps de la requête.
* Le back-end communique à nouveau avec Authsignal pour l'authentification de l'utilisateur, demandant la configuration de l'authentification par lien magique.
* L'utilisateur est dirigé vers une page pour entrer son adresse e-mail.
* Authsignal envoie un lien magique à l'adresse e-mail fournie.
* Après avoir cliqué sur le lien magique, l'utilisateur est authentifié et redirigé vers la page d'accueil, accueilli avec un message de bienvenue affichant son adresse e-mail.

Ce flux permet aux utilisateurs de s'inscrire en utilisant un nom d'utilisateur choisi et de configurer l'authentification par lien magique via e-mail pour l'inscription et la connexion. Voici un tutoriel vidéo pour vous aider visuellement à comprendre le flux :

%[https://youtu.be/kr8frW5Wwcg]

## Comment configurer votre serveur back-end

Dans cette section, je vais vous guider à travers la configuration de votre serveur Flask pour la mise en œuvre de l'authentification par lien magique. Avant de commencer, il est recommandé de configurer un environnement virtuel pour isoler les dépendances de votre projet. Voici comment procéder :

1. Ouvrez votre terminal ou invite de commande.
2. Accédez au répertoire de votre projet.
3. Exécutez la commande suivante pour créer un nouvel environnement virtuel :

```bash
python -m venv myenv
```

Note : Remplacez `myenv` par le nom souhaité pour votre environnement virtuel.

4. Activez l'environnement virtuel en utilisant la commande appropriée pour votre système d'exploitation :

* Pour Windows :

```bash
source myenv/Scripts/activate
```

* Pour macOS/Linux :

```bash
source myenv/bin/activate
```

Maintenant que vous avez configuré votre environnement virtuel, installons les dépendances nécessaires.

Pour commencer, assurez-vous d'avoir Flask installé, qui est un micro framework web pour Python. Vous pouvez l'installer en utilisant la commande suivante :

```bash
pip install Flask
```

Ensuite, nous avons besoin de `python-decouple`, une bibliothèque qui aide à gérer les paramètres de configuration dans des fichiers séparés. Installez-la avec la commande suivante :

```bash
pip install python-decouple
```

La bibliothèque `flask-cors` est une extension Flask qui permet la prise en charge du partage de ressources cross-origin (CORS) dans votre application Flask.

```bash
pip install flask-cors
```

Enfin, nous devons installer le SDK Python pour Authsignal. Vous pouvez l'installer avec la commande suivante :

```bash
pip install authsignal
```

Maintenant que nous avons toutes les dépendances nécessaires installées, créons un serveur Flask de base pour commencer avec l'authentification par lien magique. Voici une configuration de base pour vous aider à démarrer :

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)
```

Dans les étapes suivantes, nous allons intégrer AuthSignal et implémenter la fonctionnalité d'authentification par lien magique dans ce serveur.

## Comment configurer les variables d'environnement

Pour configurer et intégrer AuthSignal dans votre serveur Flask, vous devez configurer les variables d'environnement suivantes :

* `AUTHSIGNAL_BASE_URL` : Cette variable contient l'URL de base du serveur Authsignal. Elle permet à votre serveur de communiquer avec le service d'authentification d'Authsignal.
* `AUTHSIGNAL_SECRET_KEY` : Cette variable contient la clé secrète associée à votre projet Authsignal. Elle est utilisée pour la communication sécurisée entre votre serveur et AuthSignal.
* `SECRET_KEY` : Cette variable est une clé aléatoire utilisée pour chiffrer les cookies et les envoyer au navigateur.

La configuration des variables d'environnement au lieu de les coder en dur dans le code offre une sécurité améliorée en gardant les informations sensibles, telles que les clés API et les clés secrètes, séparées du code. Cela réduit le risque d'exposition accidentelle ou d'accès non autorisé à ces identifiants.

Pour configurer ces variables d'environnement, vous pouvez suivre ces étapes :

1. Ouvrez un terminal ou une invite de commande.
2. Accédez au répertoire où se trouve votre serveur Flask.
3. Créez un fichier `.env` et exportez les variables d'environnement en utilisant les commandes suivantes :

```bash
export AUTHSIGNAL_BASE_URL=<base_url>
export AUTHSIGNAL_SECRET_KEY=<secret_key>
export SECRET_KEY=<random-secret-key>
```

Assurez-vous de remplacer `<base_url>`, `<secret_key>`, et `<random-secret-key>` par les valeurs appropriées pour votre projet Authsignal. Vous pouvez trouver les valeurs de ces variables d'environnement dans la section Clés API du tableau de bord Authsignal comme expliqué précédemment.

Note : La méthode de configuration des variables d'environnement peut varier en fonction de votre système d'exploitation. Les commandes ci-dessus sont applicables pour les systèmes basés sur Unix. Pour Windows, vous pouvez utiliser la commande `set` au lieu de `export`.

Pour exporter les variables ajoutées dans le fichier .env, vous pouvez utiliser la commande suivante dans le terminal :

```bash
source .env
```

En configurant correctement ces variables d'environnement, votre serveur Flask peut communiquer de manière sécurisée avec Authsignal et implémenter la fonctionnalité d'authentification par lien magique.

## Comment initialiser le client Authsignal

Pour intégrer Authsignal dans votre serveur Flask et implémenter l'authentification par lien magique, vous devez initialiser le client Authsignal. Voici un exemple de la manière dont vous pouvez procéder :

```python
from flask import Flask
from flask_cors import CORS
import authsignal.client
from decouple import config

app = Flask(__name__)
CORS(app)

AUTHSIGNAL_BASE_URL = config("AUTHSIGNAL_BASE_URL")
AUTHSIGNAL_SECRET_KEY = config("AUTHSIGNAL_SECRET_KEY")
SECRET_KEY = config("SECRET_KEY")

authsignal_client = authsignal.Client(
    api_key=AUTHSIGNAL_SECRET_KEY,
    api_url=AUTHSIGNAL_BASE_URL
)
```

Dans cet extrait de code, nous importons d'abord `authsignal.client`, le SDK Python pour Authsignal. Nous importons également config de python-decouple pour récupérer les variables d'environnement.

Nous récupérons les variables d'environnement `AUTHSIGNAL_BASE_URL`, `AUTHSIGNAL_SECRET_KEY` et `SECRET_KEY` en utilisant config de python-decouple.

Enfin, nous initialisons le `authsignal.Client` en passant la clé API `AUTHSIGNAL_SECRET_KEY` et l'URL de base du serveur Authsignal `AUTHSIGNAL_BASE_URL`.

En initialisant le client Authsignal, nous sommes prêts à implémenter la fonctionnalité d'authentification par lien magique dans notre serveur Flask.

## Actions Authsignal

Authsignal vous permet de créer des actions pour suivre et gérer les interactions des utilisateurs dans votre application. Les actions sont des événements qui peuvent être déclenchés par les utilisateurs, tels que l'inscription ou la connexion. En créant des actions personnalisées, vous pouvez avoir plus de contrôle sur le processus d'authentification et implémenter des méthodes d'authentification spécifiques comme l'authentification par lien magique.

Pour créer une action sur votre tableau de bord Authsignal, suivez ces étapes :

1. Cliquez sur "**Actions**" dans votre tableau de bord Authsignal.
2. Cliquez sur "**Configurer une nouvelle action**" pour créer une nouvelle action.
3. Entrez un nom pour l'action qui décrit son but ou l'interaction utilisateur qu'elle représente.
4. Ensuite, vous pouvez configurer la règle pour l'action. Dans notre cas, comme nous voulons implémenter l'authentification par lien magique, nous allons ajouter une règle pour défier les utilisateurs avec un lien magique par e-mail. Cela enverra un lien magique à l'adresse e-mail de l'utilisateur pour l'authentification.
5. Enregistrez l'action pour appliquer la règle et la rendre active.

Voici une vidéo démontrant le processus de création d'une action Authsignal et de sa configuration pour l'authentification par lien magique :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/action.gif)
_Création d'une action sur Authsignal_

Vous pouvez créer deux actions - "**signUp**" et "**signIn**". Dans les étapes suivantes, nous utiliserons ces actions.

## Comment créer les routes requises

Enfin, pour implémenter l'authentification par lien magique, nous devons créer trois routes : `/api/signup`, `/api/login`, `/api/callback`, et `/api/user`.

### Route `/api/signup`

La route `/api/signup` est responsable de permettre aux utilisateurs de s'inscrire dans notre application. Voici comment nous l'implémentons :

```python
@app.route('/api/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Missing username parameter'}), 400

    response = authsignal_client.track(
        user_id=username,
        action="signUp",
        payload={
            "user_id": username,
            "redirectUrl": "http://localhost:5000/api/callback"
        }
    )
    return jsonify(response), 200
```

Dans cette implémentation, la route attend une charge utile JSON contenant le paramètre `username`. Elle utilise ensuite le `authsignal_client` pour suivre l'action **signUp** de l'utilisateur et générer un lien magique. La méthode `track` vous permet d'enregistrer les actions effectuées par les utilisateurs et d'initier des défis. Le `redirectUrl` spécifie l'URL où l'utilisateur sera redirigé après avoir été authentifié. Nous allons créer cette API ensuite.

### Route `/api/callback`

La route `/api/callback` gère l'URL de rappel où l'utilisateur est redirigé après s'être vérifié. Voici l'implémentation de cette route :

```python
@app.route('/api/callback', methods=['GET'])
def callback():
    token = request.args.get('token')
    challenge_response = authsignal_client.validate_challenge(token)

    if challenge_response["state"] == 'CHALLENGE_SUCCEEDED':
        encoded_token = jwt.encode(
            payload={"username": challenge_response["user_id"]},
            key=SECRET_KEY,
            algorithm="HS256"
        )
        response = redirect('http://localhost:3000/')
        response.set_cookie(
            key='auth-session',
            value=encoded_token,
            secure=False,
            path='/'
        )
        return response

    return redirect("/")
```

Lorsque les utilisateurs sont redirigés, Authsignal ajoute le jeton JWT dans l'URL en tant que paramètre de requête de jeton.

Dans cette implémentation, la route récupère le paramètre de jeton de la chaîne de requête. Elle utilise ensuite le `authsignal_client` pour valider le défi et vérifier si l'authentification a réussi.

Si l'authentification réussit, nous encodons un jeton Web JSON (JWT). La charge utile du jeton inclut le `username` obtenu à partir de la réponse au défi. Elle utilise la `SECRET_KEY` et l'algorithme _HS256_ pour le chiffrement.

Ensuite, l'utilisateur est redirigé vers la page d'accueil (http://localhost:3000/), et un cookie `auth-session` est défini avec le jeton encodé pour une identification ultérieure de l'utilisateur.

Notez que le jeton retourné par Authsignal dans la redirection n'est pas destiné à être utilisé comme jeton de session. Il contient simplement des informations sur le défi afin que nous puissions déterminer si le défi a réussi.

### Route `/api/login`

La route `/api/login` est responsable de permettre aux utilisateurs de se connecter à l'application. Voici l'implémentation de la route :

```python
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Missing username parameter'}), 400

    response = authsignal_client.track(
        user_id=username,
        action="signIn",
        payload={
            "user_id": username,
            "redirectUrl": "http://localhost:5000/api/callback"
        }
    )
    return jsonify(response), 200 
```

La route est configurée pour gérer les requêtes POST sur le point de terminaison `/api/login`. Lors de la réception d'une requête POST, la route extrait d'abord le `username` fourni de la charge utile JSON envoyée avec la requête. Elle s'assure que le nom d'utilisateur est présent. Si ce n'est pas le cas, elle retourne rapidement une réponse d'erreur 400 indiquant un paramètre de nom d'utilisateur manquant.

De manière similaire au flux d'inscription, elle utilise ensuite le `authsignal_client` pour suivre l'action **signIn** de l'utilisateur et générer un lien magique. Le `redirectUrl` spécifie l'URL où l'utilisateur sera redirigé après avoir été authentifié.

### Route `/api/user`

La route `/api/user` est responsable de la récupération des informations utilisateur. Voici l'implémentation de cette route :

```python
@app.route("/api/user", methods=['GET'])
def user():
    token = request.cookies.get('auth-session')
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    username = decoded_token.get('username')
    response = authsignal_client.get_user(user_id=username)
    return jsonify({"username": username, "email": response["email"]}), 200
```

Dans cette implémentation, le point de terminaison GET commence par extraire le cookie auth-session de la requête entrante. Ensuite, il décode le JWT en utilisant la méthode jwt.decode, en utilisant la `SECRET_KEY` comme clé secrète pour le décodage.

Le jeton décodé fournit le nom d'utilisateur de l'utilisateur. Il utilise ensuite le `authsignal_client` pour récupérer les informations utilisateur en fonction de l'`userId` fourni. Il retourne ensuite une réponse JSON avec les informations de nom d'utilisateur et d'e-mail.

En implémentant ces routes, nous pourrons gérer le processus d'authentification de base et récupérer les informations utilisateur dans notre serveur Flask.

## Comment configurer un nouveau projet React en front-end

Configurons notre projet front-end dans cette section. Cela inclura également la configuration du routage dans l'application.

Commencez par initialiser un nouveau projet React en utilisant `create-react-app` ou toute méthode préférée ([comme Vite](https://www.freecodecamp.org/news/complete-vite-course-for-beginners/), par exemple, qui est une manière plus moderne de configurer une application React). Cette commande configure la structure de base de votre application React.

```bash
npx create-react-app magic-link-auth
cd magic-link-auth
```

Une fois le projet créé et que vous êtes dans le répertoire du projet, installez les dépendances requises. Ici, nous avons besoin de `react-router-dom` pour gérer le routage et de `bootstrap` pour un style facile.

```bash
npm install react-router-dom bootstrap
```

### Importer le CSS de Bootstrap

Bootstrap fournit des composants et des utilitaires pré-stylisés pour un style plus facile et plus rapide de votre application.

Dans le fichier `index.js`, importez Bootstrap :

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import "bootstrap/dist/css/bootstrap.min.css"; // Importer le CSS de Bootstrap

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Si vous voulez commencer à mesurer les performances dans votre application, passez une fonction
// pour enregistrer les résultats (par exemple : reportWebVitals(console.log))
// ou envoyez à un point de terminaison d'analyse. En savoir plus : https://bit.ly/CRA-vitals
reportWebVitals();
```

De plus, nous allons écrire un peu de CSS personnalisé. Remplacez le code dans le fichier `index.css` par le code suivant :

```css
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

* {
  box-sizing: border-box;
}

main {
  padding: 5rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

code {
  background: #fafafa;
  border-radius: 5px;
  padding: 0.75rem;
  font-family: Menlo, Monaco, Lucida Console, Courier New, monospace;
}

input[type="button"] {
  border: none;
  background: cornflowerblue;
  color: white;
  padding: 12px 24px;
  margin: 8px;
  font-size: 18px;
  border-radius: 8px;
  cursor: pointer;
}
```

De même, remplacez le code dans `App.css` par le code suivant :

```css
.mainContainer {
  flex-direction: column;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.titleContainer {
  display: flex;
  flex-direction: column;
  font-size: 48px;
  font-weight: bolder;
  align-items: center;
  justify-content: center;
}

.resultContainer,
.historyItem {
  flex-direction: row;
  display: flex;
  width: 400px;
  align-items: center;
  justify-content: space-between;
}

.historyContainer {
  flex-direction: column;
  display: flex;
  height: 200px;
  align-items: center;
  flex-grow: 5;
  justify-content: flex-start;
}

.buttonContainer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 260px;
}

.inputContainer {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.inputContainer>.errorLabel {
  color: red;
  font-size: 16px;
  text-align: center;
}

.inputBox {
  height: 48px;
  width: 400px;
  font-size: medium;
  border-radius: 8px;
  border: 1px solid grey;
  padding-left: 8px;
}

.inputButton {
  height: 48px;
  width: 400px;
}
```

### Configurer le routage

Le routage dans les applications React aide à naviguer entre différentes vues ou pages. `react-router-dom` simplifie ce processus.

Dans votre fichier `App.js`, configurez le routage :

```javascript
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Register from "./pages/Register";
import Login from "./pages/Login";
import "./App.css";
import "./index.css";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
```

Il définit un composant App qui encapsule toute la structure de l'application dans un composant `<BrowserRouter>`. À l'intérieur de `<Routes>`, nous définissons trois composants <Route> : un pour le chemin racine `/` rendant le composant `Dashboard`, et deux pour les chemins `/login` et `/signup`, rendant respectivement les composants `Login` et `Register`.

Cette configuration permet la navigation entre différentes vues en fonction des chemins d'URL, permettant aux utilisateurs d'accéder à des composants spécifiques lorsqu'ils visitent des routes correspondantes au sein de l'application.

Dans les sections à venir, nous allons configurer les trois composants mentionnés ci-dessus.

## Comment configurer les composants

Dans la section précédente, nous avons importé deux composants du dossier `src/pages`. Créons un dossier `pages` à l'intérieur du dossier `src`, puis nous pourrons commencer à créer les composants.

### Composant Register

Créons un fichier `Register.jsx` à l'intérieur du dossier pages. Le composant **Register** permet aux utilisateurs de s'inscrire dans notre application.

```javascript
import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

const Register = () => {
  const [username, setUsername] = useState("");
  const [usernameError, setUsernameError] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    const isAuthenticated = checkCookies();
    if (isAuthenticated) {
      navigate("/");
    }
  }, [navigate]);

  const checkCookies = () => {
    const authSessionCookie = document.cookie.match("auth-session=([^;]+)");

    return !!authSessionCookie;
  };

  const onButtonClick = () => {
    setUsernameError("");

    if ("" === username) {
      setUsernameError("Username is mandatory!");
      return;
    }

    signup();
  };

  const signup = async () => {
    const response = await fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
      }),
      credentials: "include",
    });

    const { url } = await response.json();

    // Rediriger vers l'URL de vérification
    window.location.href = url;
  };

  return (
    <div className={"mainContainer"}>
      <div className={"titleContainer"}>
        <div>Sign Up</div>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          value={username}
          placeholder="Enter your username"
          onChange={(e) => setUsername(e.target.value)}
          className={"inputBox"}
        />
        <label className="errorLabel text-center">{usernameError}</label>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          className={"inputButton"}
          type="button"
          onClick={onButtonClick}
          value={"Sign Up"}
        />
      </div>
      <div>
        Existing User? <Link to="/login">Login here</Link>
      </div>
    </div>
  );
};

export default Register;
```

Le composant initialise les variables d'état en utilisant `useState` pour gérer la visibilité de `usernameError` et stocker la saisie du nom d'utilisateur dans `userName`. Il initialise également la fonction `navigate` de `useNavigate` pour gérer la navigation au sein de l'application.

Nous utilisons le hook `useEffect` pour vérifier les cookies d'authentification lorsque le composant est monté. Il appelle la fonction `checkCookies`, qui vérifie l'existence des cookies que nous avions définis à partir du serveur back-end. Si le cookie `auth-session` est trouvé, l'utilisateur est automatiquement redirigé vers l'URL racine en utilisant navigate("/").

En cliquant sur le bouton "Sign Up", la fonction `onButtonClick` est déclenchée. Elle vérifie d'abord si l'utilisateur a saisi le nom d'utilisateur. Si ce n'est pas le cas, elle affiche un message d'erreur en utilisant `usernameError`. Si l'utilisateur a saisi le nom d'utilisateur, elle appelle la fonction `signup`.

La fonction `signup` effectue une requête POST asynchrone vers le point de terminaison `/api/signup` avec le nom d'utilisateur fourni. En cas de réponse réussie, elle redirige l'utilisateur vers l'URL de vérification reçue en modifiant window.location.href.

Le JSX retourné par le composant définit la disposition de l'interface utilisateur qui ressemble à ce qui suit :

![Image](https://lh7-us.googleusercontent.com/gncsDRe9QVK20DWMkiWwdGOt_ZymbSVXTv-8UGvyKIpp5-TZ64-DwLGLbMtDM0B-wgXh8jNOCdkA0kia3-gJftMxFaH-za_4O0cqCSvK9GLMHSbO_nH_UfgGIf5QhHaOZg559_N0c4P9Oof4O5JmkPE)
_Composant UI Register_

Il comprend un champ de saisie pour que les utilisateurs entrent leur nom d'utilisateur et un bouton "Sign Up". Sous le bouton, nous avons un lien vers la page de connexion pour que les utilisateurs existants puissent se connecter.

### Composant Login

Nous avons gardé la page de connexion similaire à la page d'inscription pour simplifier. Par conséquent, le composant Login est pratiquement le même que le composant Register.

```javascript
import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [usernameError, setUsernameError] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    const isAuthenticated = checkCookies();
    if (isAuthenticated) {
      navigate("/");
    }
  }, [navigate]);

  const checkCookies = () => {
    const authSessionCookie = document.cookie.match("auth-session=([^;]+)");

    return !!authSessionCookie;
  };

  const onButtonClick = () => {
    setUsernameError("");

    if ("" === username) {
      setUsernameError("Username is mandatory!");
      return;
    }

    login();
  };

  const login = async () => {
    const response = await fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
      }),
      credentials: "include",
    });

    const { url } = await response.json();

    // Rediriger vers l'URL de vérification
    window.location.href = url;
  };

  return (
    <div className={"mainContainer"}>
      <div className={"titleContainer"}>
        <div>Login</div>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          value={username}
          placeholder="Enter your username"
          onChange={(ev) => setUsername(ev.target.value)}
          className={"inputBox"}
        />
        <label className="errorLabel text-center">{usernameError}</label>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          className={"inputButton"}
          type="button"
          onClick={onButtonClick}
          value={"Log in"}
        />
      </div>
      <div>
        New User? <Link to="/signup">Sign up here</Link>
      </div>
    </div>
  );
};

export default Login;
```

La seule différence significative, autre que le texte et le bouton dans l'interface utilisateur ici, est que nous allons faire l'appel API à la route `/api/login` lorsque les utilisateurs cliquent sur le bouton de connexion.

L'interface utilisateur ressemble à ce qui suit :

![Image](https://lh7-us.googleusercontent.com/F4EDOhuMbTRtXt3UxhpLYdZPT8XtCuYWjEX3H95bEXEZatLDsuRxaut3KZ3ZtyHSWIQ1WkuA5WWUxZcXrCBHyCMfMG-LQTKjnQHXyY8Y2Ha93YstE0Kycd9ji9lj33wMc1D8Km7pFNu5EGyQh14D9m8)
_Composant UI Login_

### Composant Dashboard

Le composant Dashboard dans notre application sert d'interface pour les utilisateurs authentifiés, affichant un message de bienvenue avec l'e-mail de l'utilisateur et permettant la fonctionnalité de déconnexion de l'utilisateur.

Créons un fichier `Dashboard.jsx` à l'intérieur du dossier `pages`.

```javascript
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const [userEmail, setUserEmail] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const checkCookies = async () => {
      const authSessionCookie = document.cookie.match("auth-session=([^;]+)");

      if (!authSessionCookie) {
        navigate("/auth");
        return false;
      }

      return true;
    };

    const fetchData = async () => {
      const cookiesValid = await checkCookies();
      if (!cookiesValid) return;

      try {
        const response = await fetch("http://localhost:5000/api/user", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include"
        });

        if (!response.ok) {
          throw new Error("Failed to fetch user data");
        }

        const data = await response.json();
        setUserEmail(data.email);
      } catch (error) {
        navigate("/auth");
      }
    };

    fetchData();
  }, [navigate]);

  const handleLogout = () => {
    document.cookie = `auth-session=; max-age=0`;
    navigate("/auth");
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <main className="px-3 text-center">
        <h1>Welcome Home!</h1>
        <p className="lead">You're logged in as {userEmail}!</p>
        <div className="d-flex justify-content-center">
          <button
            className="btn btn-lg btn-dark fw-bold border-white bg-dark"
            onClick={handleLogout}
          >
            Log Out
          </button>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
```

Lors du montage du composant ou lorsque `navigate` change (une dépendance de `useEffect`), l'effet s'exécute. Il commence par définir deux fonctions asynchrones. La première, `checkCookies`, vérifie la présence des cookies `auth-session`. Si celui-ci est manquant, il redirige l'utilisateur vers la route d'authentification.

La deuxième fonction, `fetchData`, est responsable de la récupération des données utilisateur. Elle vérifie la validité des cookies en utilisant `checkCookies`. Après vérification, elle envoie une requête GET à notre point de terminaison API back-end. En cas de réponse réussie, elle met à jour l'état `userEmail` avec l'e-mail de l'utilisateur récupéré depuis les données de l'API.

Si une erreur se produit pendant ce processus, comme l'échec de la récupération des données utilisateur, elle redirige l'utilisateur vers la route d'authentification.

Le JSX retourné par le composant rend une disposition de tableau de bord simple.

![Image](https://lh7-us.googleusercontent.com/ca-epjkteyLzE_dVbbWN6bC5fMVogCJLRvR8Milfjl7UzoHRK7462_YJZhkJvhoTpBtD0sNFwpGbNaLTKNEuBg6wKSxv6j5-ApmjpOtPgx-UkeM8i39A0KwAuU3L2TeRc8R_3aXugnAMcH4iGrlBP0M)
_Composant UI Dashboard_

Le contenu affiché comprend un message de bienvenue et l'e-mail de l'utilisateur actuellement connecté. Il y a également un bouton "Log Out" qui, lorsqu'on clique dessus, initie le processus de déconnexion en déclenchant la fonction `handleLogout`. Il supprime les cookies `auth-session` en définissant leur max-age à 0, les expirant ainsi. Ensuite, il redirige l'utilisateur vers la route d'authentification.

## Comment exécuter l'application

Vous pouvez trouver le code de l'application finale dans ce [dépôt GitHub](https://github.com/ashutoshkrris/authsignal-magic-link-demo). Pour exécuter votre application back-end, exécutez `python app.py` depuis votre dossier back-end dans votre terminal. Cela démarrera votre serveur back-end sur le port 5000. Ensuite, exécutez l'application front-end en utilisant la commande `npm start`. Cela démarrera votre application front-end sur le port 3000.

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser Authsignal pour implémenter une authentification utilisateur de base avec vérification par e-mail via des liens magiques.

Authsignal facilite la gestion des utilisateurs et maintient la sécurité, permettant aux développeurs de se concentrer sur l'amélioration des applications. Il supprime également la surcharge de se souvenir d'un autre mot de passe pour les utilisateurs de l'application.

Pour en savoir plus sur Authsignal, [consultez la documentation Authsignal](https://docs.authsignal.com/).

Si vous avez des problèmes ou des questions liés au tutoriel, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/ashutoshkrris).