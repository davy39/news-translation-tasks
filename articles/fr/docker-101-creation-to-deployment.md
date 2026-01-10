---
title: Docker 101 - comment passer de la création au déploiement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-31T07:31:53.000Z'
originalURL: https://freecodecamp.org/news/docker-101-creation-to-deployment
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca090740569d1a4ca496f.jpg
tags:
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: Tutorial
  slug: tutorial
- name: Web Applications
  slug: web-applications
seo_title: Docker 101 - comment passer de la création au déploiement
seo_desc: 'By Usheninte Dangana

  Docker is a game-changer, and has very much altered the world of application development.
  Learn the vital skills needed to work with this container technology today.

  What is Docker?

  In simple terms, Docker is a tool that lets dev...'
---

Par Usheninte Dangana

Docker est un changement de jeu et a grandement modifié le monde du développement d'applications. Apprenez les compétences vitales nécessaires pour travailler avec cette technologie de conteneurs aujourd'hui.

## Qu'est-ce que Docker ?

En termes simples, **Docker** est un outil qui permet aux développeurs de créer, déployer et exécuter des applications dans des conteneurs. **_La conteneurisation_** est l'utilisation de conteneurs Linux pour déployer des applications.

Alors, pourquoi Docker est-il si génial, et pourquoi devrions-nous, en tant que développeurs, nous donner la peine de l'apprendre ?

| Raison | Explication |
|:---:|---|
| Flexible | Même les applications les plus complexes peuvent être conteneurisées. |
| Léger | Les conteneurs utilisent et partagent le noyau de l'hôte. |
| Interchangeable | Vous pouvez déployer des mises à jour et des mises à niveau à la volée. |
| Portable | Vous pouvez construire localement, déployer dans le cloud et exécuter n'importe où. |
| Évolutif | Vous pouvez augmenter et distribuer automatiquement les répliques de conteneurs. |
| Empilable | Vous pouvez empiler des services verticalement et à la volée. |

Maintenant que nous savons pourquoi Docker est si important, installons-le sur notre machine locale.

Inscrivez-vous pour un compte sur [Docker Hub](https://hub.docker.com/signup) et téléchargez l'application Docker Desktop gratuite.

## En quoi Docker est-il différent des machines virtuelles traditionnelles ?

Un conteneur s'exécute nativement sur Linux et partage le noyau de la machine hôte avec d'autres conteneurs. Il s'exécute comme un processus discret, prenant pas plus de mémoire qu'un autre exécutable, ce qui signifie qu'il est très léger.

En revanche, une machine virtuelle (VM) exécute un système d'exploitation "invité" complet avec un accès virtuel aux ressources de l'hôte via un hyperviseur. En général, les VM fournissent un environnement avec plus de ressources que la plupart des applications n'en ont besoin.

Lorsque vous travaillez avec Docker, un `Dockerfile` définit ce qui se passe dans l'environnement à l'intérieur de votre conteneur. L'accès aux ressources comme les interfaces réseau et les disques durs est virtualisé dans cet environnement, qui est isolé du reste de votre système. Cela signifie que vous devez mapper les ports vers le monde extérieur et être spécifique sur les fichiers que vous souhaitez "copier" dans cet environnement. Cependant, après avoir fait cela, vous pouvez vous attendre à ce que la construction de votre application définie dans ce `Dockerfile` se comporte exactement de la même manière où qu'elle s'exécute.

## Commandes Docker

Pour tester que vous avez une version en cours d'exécution de Docker, exécutez la commande suivante :

`docker --version`

Pour tester que votre installation fonctionne parfaitement, essayez d'exécuter l'image Docker simple **hello-world** :

`docker run hello-world`

Si tout est configuré correctement, vous devriez voir une sortie similaire à ce qui suit :

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

Pour voir l'image Docker **hello-world** qui a été téléchargée sur votre ordinateur, utilisez la commande de liste des images Docker :

`docker image ls`

Super ! Vous avez déjà commencé à développer des applications conteneurisées avec Docker. Voici quelques commandes Docker de base utiles :

```
## Liste des commandes CLI Docker
docker
docker container --help

## Afficher la version et les informations Docker
docker --version
docker version
docker info

## Exécuter une image Docker
docker run hello-world

## Lister les images Docker
docker image ls

## Lister les conteneurs Docker (en cours d'exécution, tous, tous en mode silencieux)
docker container ls
docker container ls --all
docker container ls -aq
```

<blockquote>
La conteneurisation rend le CI/CD transparent. Par exemple :

- les applications n'ont pas de dépendances système
- les mises à jour peuvent être poussées vers n'importe quelle partie d'une application distribuée
- la densité des ressources peut être optimisée.
- Avec Docker, la mise à l'échelle de votre application est une question de lancement de nouveaux exécutables, et non d'exécution de machines virtuelles lourdes.
</blockquote>

## Construisons une application web Node.js en utilisant Docker

La première chose que nous faisons est de créer un fichier `package.json`. Nous pouvons faire cela rapidement en exécutant simplement la commande suivante :

```
npm init -y
```

Cela crée le fichier ci-dessus avec certains champs essentiels déjà remplis ou laissés vides.

Votre fichier devrait ressembler à quelque chose comme ceci :

```json
{
  "name": "app-name",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Ensuite, nous installons `express.js`, qui, selon le [site officiel](http://expressjs.com/), est un "**Framework web rapide, minimaliste et non opinionné pour Node.js**".

Nous faisons cela en exécutant la commande suivante dans un terminal :

```
npm install express --save
```

La commande ci-dessus ajoute le framework `express.js` à notre application, le drapeau **--save** servant d'instruction à l'application pour utiliser `express.js` comme dépendance.

Maintenant, allez dans votre `package.json`, et changez la paire clé-valeur `"main": "index.js"` en ce qui suit :

```
"main": "app.js"
```

Ensuite, créez un fichier `.gitignore` en utilisant la commande suivante :

```
touch .gitignore
```

Puis ajoutez la ligne suivante :

```
node_modules/
```

> Cela empêche le dossier **node_modules**, essentiel au développement `node.js`, d'être suivi par `git`.

Maintenant, ajoutez le code suivant au fichier `app.js` :

```js
const express = require('express');

const app = express();

const PORT = 8080;
const HOST = '0.0.0.0';

app.get('/', (req, res) => {
  res.send(
    `
    <h1>Accueil</h1>
    <p>Docker est génial !</p>
    <a href="/plus" alt="Page suivante">Page suivante</a>
    `
  )
});

app.get('/plus', (req, res) => {
  res.send(
    `
    <h1>Page deux</h1>
    <p>Node.js est plutôt génial aussi !!</p>
    <a href="/" alt="Retour à l'accueil">Retour à l'accueil</a>
    `
  )
});

app.listen(PORT, HOST);
console.log(`Running on https://${HOST}:${PORT}`);
```

Pour exécuter cela sur votre machine locale, exécutez la commande suivante dans le dossier de l'application :

```
npm start
```

> Vous trouverez l'application en cours d'exécution à l'adresse `http://0.0.0.0:8080/`

### Super !

![Félicitations](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif)
_Félicitations pour être arrivé aussi loin_

---

## Dans l'univers Docker

Maintenant, créez un `Dockerfile` avec la commande suivante :

```
touch Dockerfile
```

Puis ajoutez le code suivant :

```
# Une image Docker officielle pour Node.js
FROM node:10-alpine

# Répertoire de travail pour l'application conteneurisée
WORKDIR /src/app

# Cela copie les fichiers package.json importants vers le répertoire courant
COPY package*.json ./
# Installe les dépendances Node.js essentielles
RUN npm install

COPY . .

# Ouvre ce port sur le conteneur Docker
EXPOSE 8080

# Cela démarre l'application Docker
CMD [ "npm", "start" ]
```

Les commentaires ci-dessus tentent d'expliquer ce que fait chaque commande `Dockerfile`.

De plus, ajoutez un fichier `dockerignore` pour empêcher la conteneurisation de certains composants de l'application.

Placez ceci à l'intérieur du fichier `dockerignore` :

```
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.dockerignore
.git
.gitignore
README.md
LICENSE
```

## Comment déployer

Le `<nom-de-l-image>` est le nom que vous attribuez à votre application Docker, et `<tag>` est essentiellement un indicateur de version pour votre image Docker.
* `docker build -t nom-de-l-image:tag .`

Exécutez ceci pour accéder à votre compte Docker depuis votre terminal.
* `docker login`

Créez un dépôt sur Docker Hub.

Tag `<image>` pour le téléchargement vers le registre.
* `docker tag <nom-de-l-image> username/repository:tag`

Téléchargez l'image taguée vers le registre.
* `docker push username/repository:tag`

Exécutez le conteneur Docker déployé sur votre machine locale en connectant ses PORTS. Ciblez le port 8080 exposé et attribuez-le au port 10203 sur votre machine.
* `docker run -p 10203:8080 username/repository:tag`

---

#### C'est tout ! Vous avez construit et déployé une application web Node.js conteneurisée.

Tout le code ci-dessus peut être trouvé dans [ce dépôt Github](https://github.com/Usheninte/docker-101).

> Originalement publié [ici](https://blog.ninte.dev/docker-101-creation-to-deployment-cjzylgqnc0019eus1s10lg39r) sur [**blog.ninte.dev**](https://blog.ninte.dev)