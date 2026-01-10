---
title: Comment configurer HTTPS localement avec create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T16:12:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-https-locally-with-create-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/react-https.png
tags:
- name: create-react-app
  slug: create-react-app
- name: how-to
  slug: how-to
- name: http
  slug: http
- name: https
  slug: https
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment configurer HTTPS localement avec create-react-app
seo_desc: "By Braedon Gough\nRunning HTTPS in development is helpful when you need\
  \ to consume an API that is also serving requests via HTTPS. \nIn this article,\
  \ we will be setting up HTTPS in development for our create-react-app with our own\
  \ SSL certificate. \nThi..."
---

Par Braedon Gough

Exécuter HTTPS en développement est utile lorsque vous devez consommer une API qui sert également des requêtes via HTTPS. 

Dans cet article, nous allons configurer HTTPS en développement pour notre create-react-app avec notre propre certificat SSL. 

Ce guide est destiné aux utilisateurs de macOS et nécessite que vous ayez `[brew](https://brew.sh/)` installé. 

## Ajout de HTTPS

Dans votre `package.json`, mettez à jour le script **start** pour inclure https :

```json
"scripts": {
    "start": "HTTPS=true react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

L'exécution de `yarn start` après cette étape affichera cet écran dans votre navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/privacy-error.png)

À ce stade, vous êtes déjà prêt à utiliser `https`. Mais vous n'avez pas de certificat valide, donc votre connexion est considérée comme non sécurisée. 

## Création d'un certificat SSL

Le moyen le plus simple d'obtenir un certificat est via `[mkcert](https://github.com/FiloSottile/mkcert)`.

```bash
# Installer l'outil mkcert
brew install mkcert

# Installer nss (nécessaire uniquement si vous utilisez Firefox)
brew install nss

# Configurer mkcert sur votre machine (crée une CA)
mkcert -install
```

Après avoir exécuté les commandes ci-dessus, vous aurez créé une **[autorité de certification](https://en.wikipedia.org/wiki/Certificate_authority)** sur votre machine, ce qui vous permettra de générer des certificats pour tous vos futurs projets. 

À partir de la racine de votre projet `create-react-app`, vous devez maintenant exécuter :

```bash
# Créer le répertoire .cert s'il n'existe pas
mkdir -p .cert

# Générer le certificat (exécuté depuis la racine de ce projet)
mkcert -key-file ./.cert/key.pem -cert-file ./.cert/cert.pem "localhost"
```

Nous allons stocker nos certificats générés dans le répertoire `.cert`. Ceux-ci ne doivent pas être commités dans le contrôle de version, vous devez donc mettre à jour votre `.gitignore` pour inclure le répertoire `.cert`. 

Ensuite, nous devons mettre à jour le script `start` à nouveau pour inclure notre nouveau certificat :

```json
  "scripts": {
    "start": "HTTPS=true SSL_CRT_FILE=./.cert/cert.pem SSL_KEY_FILE=./.cert/key.pem react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

Lorsque vous exécutez `yarn start` à nouveau, vous devriez maintenant voir que votre connexion est sécurisée. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/secure.png)

N'hésitez pas à écrire si vous avez des questions - [connectez-vous avec moi sur LinkedIn](https://www.linkedin.com/in/braedon-gough-ba92a048/) ou [suivez-moi sur Twitter](https://twitter.com/bbbraedddon).