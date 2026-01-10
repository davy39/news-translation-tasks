---
title: Comment utiliser les JSON Web Tokens pour une authentification sécurisée dans
  les applications Flask
subtitle: ''
author: Yemi Ojedapo
co_authors: []
series: null
date: '2024-04-17T16:29:02.000Z'
originalURL: https://freecodecamp.org/news/jwt-authentication-in-flask
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/pexels-soumil-kumar-735911--1-.jpg
tags:
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
- name: JSON Web Tokens
  slug: json-web-tokens
- name: JWT
  slug: jwt
- name: Python
  slug: python
- name: Security
  slug: security
seo_title: Comment utiliser les JSON Web Tokens pour une authentification sécurisée
  dans les applications Flask
seo_desc: 'Passwords, credit card information, personal identification numbers (PINs)
  – these are all critical assets used for authorization and authentication. This
  means they need to be protected from unauthorized users.

  As developers, we are tasked with safe...'
---

Mots de passe, informations de carte de crédit, numéros d'identification personnelle (PIN) – ce sont tous des éléments critiques utilisés pour l'autorisation et l'authentification. Cela signifie qu'ils doivent être protégés des utilisateurs non autorisés.

En tant que développeurs, nous sommes chargés de protéger ces informations sensibles, et il est important de mettre en œuvre des mesures de sécurité solides dans nos applications.

Il existe de nombreux mécanismes d'authentification disponibles pour sécuriser les données, comme OAuth, OpenID Connect et les JSON Web Tokens (JWT).

Dans cet article, je vais vous montrer comment utiliser les JWT pour sécuriser les informations dans les API en intégrant l'authentification basée sur les JWT dans une application Flask.

Voici ce que cet article couvrira :

* [Qu'est-ce qu'un JSON Web Token ?](#heading-quest-ce-quun-json-web-token)
* [Comment fonctionnent les JWT ?](#heading-comment-fonctionnent-les-jwt)
* [Comment utiliser les JSON Web Tokens pour authentifier les applications Flask](#heading-comment-utiliser-les-json-web-tokens-pour-authentifier-les-applications-flask)
  1. [Installer les dépendances](#heading-1-installer-les-dependances)
  2. [Créer une base de données et un modèle d'utilisateur](#heading-2-creer-une-base-de-donnees-et-un-modele-dutilisateur)
  3. [Configurer l'application pour l'authentification JWT](#heading-3-configurer-lapplication-pour-lauthentification-jwt)
  4. [Créer des routes protégées](#heading-4-creer-des-routes-protegees)
  5. [Créer une fonction de connexion](#heading-5-creer-une-page-de-connexion)
* [Conclusion](#heading-conclusion)

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* Une compréhension des méthodes HTTP
* Une compréhension de la création d'API dans Flask
* Un éditeur VS Code (ou similaire)
* Un terminal

## Qu'est-ce qu'un JSON Web Token ?

Les JSON Web Tokens, ou JWT, sont un mécanisme d'authentification utilisé pour transmettre de manière sécurisée des informations entre un client et un serveur au format JSON.

Ces informations peuvent être vérifiées et considérées comme fiables car elles sont signées numériquement avec l'algorithme [HMAC](https://xilinx.github.io/Vitis_Libraries/security/2020.1/guide_L1/internals/hmac.html) ou une paire de clés publique/privée utilisant [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) ou [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm).

Les tokens sont encodés en trois parties, chacune séparée par un point, comme ceci :

```
Header.Payload.Signature

```

* **Header** : Cela définit le type de token (JWT) et l'algorithme de signature utilisé.
* **Payload** : Cela transporte des données spécifiques à l'utilisateur comme l'ID de l'utilisateur, le nom d'utilisateur, les rôles et toute autre revendication que vous souhaitez inclure. Ce payload est encodé en Base64 pour une sécurité maximale.
* **Signature** : Il s'agit d'une combinaison hachée de l'en-tête, du payload et de la clé secrète du serveur. Elle garantit l'intégrité du token et que toute modification du token sera détectée.

## Comment fonctionnent les JWT ?

Pour comprendre comment fonctionnent les JWT, vous devez savoir ce que les tokens sont censés faire. Les JWT ne sont pas créés pour cacher des données mais pour s'assurer que les données envoyées sont authentifiées. C'est pourquoi le JWT est signé et encodé, mais pas chiffré.

Un JWT agit comme un moyen sans état de transmettre des données d'un client à un serveur. Cela signifie qu'il ne stocke aucun objet de session dans le navigateur, donc le navigateur ne maintient pas d'état de session entre les requêtes.

Au lieu de cela, les JWT utilisent un token qui est envoyé dans un en-tête de requête chaque fois qu'une requête est faite. Ce token confirme que le token envoyé est authentifié et est autorisé à accéder à cette requête.

Voyons comment cela se passe :

1. Un utilisateur tente de se connecter et envoie un nom d'utilisateur et un mot de passe à vérifier par le serveur.
2. La fonction de vérification effectue une vérification pour voir s'il y a une correspondance dans la base de données.
3. Un JWT est ensuite généré par le serveur une fois que l'utilisateur est authentifié avec succès (connecté) en utilisant ses informations (payload), telles que l'ID de l'utilisateur ou le nom d'utilisateur, et le signe en utilisant une clé secrète.
4. Le JWT généré est envoyé comme un token porteur avec chaque en-tête de requête pour vérifier si l'utilisateur est authentifié pour faire cette requête.

## Comment utiliser les JSON Web Tokens pour authentifier les applications Flask

Pour démontrer comment vous pouvez implémenter l'authentification JWT dans Flask, nous allons créer une application simple qui utilise JWT pour gérer les fonctions de connexion et accéder aux routes protégées.

### 1. Installer les dépendances

Exécutez cette commande pour installer les dépendances dont nous aurons besoin

```
pip install flask flask-bcrypt Flask-JWT-Extended

```

Ensuite, assurez-vous d'importer les dépendances et d'initialiser votre application Flask avec ce code :

```python
from flask import Flask, jsonify, session, request, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt


app = Flask(__name__)

////ÉCRIRE LE CODE PRINCIPAL ICI


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

```

### 2. Créer une base de données et un modèle d'utilisateur

Pour cela, nous utiliserons SQL-Alchemy, qui est un outil SQL pour Python qui simplifie l'utilisation de SQL dans les scripts Python.

Pour configurer SQL Alchemy dans votre application, suivez ces étapes :

Tout d'abord, ouvrez votre terminal ou invite de commande et entrez la commande suivante :

```
pip install sqlalchemy

```

Cette commande installe SQLAlchemy dans votre environnement Python, le rendant disponible dans votre répertoire de projet.

Ensuite, configurez votre application pour utiliser votre système de gestion de base de données (DBMS) préféré. Ce tutoriel utilisera le DBMS SQlite3 car il ne nécessite pas de serveur séparé :

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

```

Ce snippet de code indique à Flask-SQLAlchemy de créer et d'utiliser le fichier `site.db` dans votre répertoire de projet comme base de données SQLite pour l'application.

Ensuite, initialisez la base de données dans votre application :

```
db = SQLAlchemy(app)

```

Cette instance de la base de données agit comme un pont entre l'application et la base de données.

Maintenant, créez le modèle d'utilisateur où nous stockerons les détails de l'utilisateur dans ce tutoriel :

```
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    cart = db.Column(JSON, nullable=True, default=list)  # Rendre le panier nullable

    # Définir la relation entre User et CartProducts
    cart_products = relationship('CartProducts', backref="user", lazy="dynamic")
    # Définir la relation entre User et Wishlists
    wishlists = db.relationship('Wishlists', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

```

 **Note :** Vous pouvez créer d'autres modèles en utilisant la même syntaxe pour représenter différentes entités de données dans votre application.

### 3. Configurer l'application pour l'authentification JWT

Pour implémenter l'authentification JWT dans votre application Flask, importez les bibliothèques nécessaires et configurez les paramètres appropriés avec ce code :

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'votre_cle_secrete_fort'
app.config["JWT_SECRET_KEY"] = 'votre_cle_secrete_jwt'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

# Initialisation de la base de données
db = SQLAlchemy(app)

# Initialisation JWT
jwt = JWTManager(app)

# Reste du code de l'application (routes, etc.)

```

Ce snippet de code importe les composants suivants nécessaires pour notre application :

* **app.config['SECRET_KEY']** définit la clé secrète de l'application Flask qui est utilisée pour signer de manière sécurisée les cookies de session et d'autres besoins liés à la sécurité.
* **app.config['JWT_SECRET_KEY']** définit la clé secrète utilisée pour encoder et décoder les JWT pour les opérations Flask-JWT.
* **app.config['JWT_TOKEN_LOCATION']** spécifie où l'application doit chercher le JWT. Ici, il est défini pour chercher dans les en-têtes HTTP.

Une fois que nous avons configuré cela, nous pouvons créer les endpoints et les routes que nous avons l'intention de protéger.

### 4. Créer des routes protégées

Les routes protégées sont les pages que nous avons l'intention de garder cachées des utilisateurs non autorisés.

Par exemple, supposons que nous essayons d'entrer dans un lieu exclusif aux membres d'une société. Mais un garde protège le lieu des "utilisateurs non autorisés" comme nous. Dans cette situation, nous sommes les utilisateurs de l'application, le lieu est l'URL que nous protégeons, et le garde qui protège le lieu est un décorateur **`@jwt_required`**.

Le décorateur **`@jwt_required`** est utilisé pour protéger des routes spécifiques qui nécessitent une authentification. Ce décorateur confirmera qu'il y a un token d'accès JWT dans les en-têtes de requête avant d'autoriser l'accès à la page :

```python
@app.route('/get_name', methods=['GET'])
@jwt_required()
def get_name():
    # Extraire l'ID de l'utilisateur du JWT
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    # Vérifier si l'utilisateur existe
    if user:
        return jsonify({'message': 'Utilisateur trouvé', 'name': user.name})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'}), 404

```

Dans ce snippet de code, nous avons créé une fonction qui retourne le nom de l'utilisateur après authentification. Si le token est manquant, invalide ou expiré, la requête sera refusée, et généralement, le serveur retournera un statut HTTP **401** Non autorisé.

### 5. Créer une page de connexion

Dans cet endpoint, nous allons créer une fonction qui accepte les identifiants de nom d'utilisateur et de mot de passe de la requête client (par exemple, les données de formulaire) et compare les identifiants obtenus de l'utilisateur avec les données de l'utilisateur dans la base de données. S'il y a une correspondance, un token d'accès JWT sera généré contenant les informations de l'utilisateur.

```python
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Données reçues :', username , password)

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Connexion réussie', 'access_token': access_token})
    else:
        return jsonify({'message': 'Échec de la connexion'}), 401

```

Dans cet exemple, la fonction vérifie les identifiants de l'utilisateur par rapport à la base de données en utilisant bcrypt pour une vérification sécurisée du mot de passe lorsqu'une requête POST est reçue. Si les identifiants sont valides, le serveur génère un JWT pour l'utilisateur, lui permettant d'accéder aux routes protégées.

Voici un exemple de formulaire React envoyant une requête POST à l'endpoint de connexion :

```jsx
import React from "react";
import axios from "axios";
import { useState } from "react";
import Footer from "./Footer";
// import "./Login.css";

function Login() {
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();
    const data = {
      username: username,
      Password: password,
    };

    try {
      const response = await axios.post("http://localhost:5000/login", {
        username,
        password,
      });
      localStorage.setItem("access_token", response.data.access_token);
      // Rediriger vers la route protégée
      alert("Connexion réussie");
    } catch (error) {
      console.error(error);
      // Afficher un message d'erreur à l'utilisateur
    }
  };

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  return (
    <div >
      
          <form method="post" >
              <input
                type="text"
                id=""
                placeholder="Nom d'utilisateur"
                name="username"
                required
                value={username}
                onChange={handleUsernameChange}
              />
              <input
                type="text"
                id=""
                placeholder="Votre email"
              />
              <input
                type="password"
                required
                placeholder="Votre mot de passe"
                name="password"
                value={password}
                onChange={handlePasswordChange}
              />
          </form>
          <button type="submit" onClick={handleLogin}>
            Se connecter
          </button>
       
    </div>
  );

}

export default Login;

```

Dans ce composant React, nous avons fourni un formulaire de connexion qui utilise Axios pour envoyer une requête POST à l'endpoint de connexion. Il gère les entrées de nom d'utilisateur et de mot de passe en utilisant le hook `useState` de React et soumet ces valeurs une fois le formulaire soumis.

Si la connexion est réussie, il stocke un JWT dans le stockage local. Cela permet à l'application côté client de récupérer facilement le token lors de l'envoi de requêtes authentifiées au serveur.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/jwtDemo-1.gif)

## Conclusion

Dans cet article, nous avons appris comment sécuriser les API avec les JSON Web Tokens dans Flask. Nous avons couvert les bases des JWT, leur fonctionnement, et fourni un processus étape par étape pour implémenter cette méthode d'authentification. Cela incluait tout, de l'installation des dépendances nécessaires à la création de modèles d'utilisateurs et à la protection des routes.

Vous pouvez construire sur cette base, par exemple en ajoutant des tokens de rafraîchissement, en intégrant avec des fournisseurs OAuth tiers, ou en gérant des permissions utilisateur plus complexes.