---
title: Qu'est-ce que Node.js ? Les bases du développement JavaScript côté serveur
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-25T18:24:42.000Z'
originalURL: https://freecodecamp.org/news/node-js-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-tomasz-filipek-1630035.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Qu'est-ce que Node.js ? Les bases du développement JavaScript côté serveur
seo_desc: 'Node.js is a powerful runtime environment for executing JavaScript code
  outside of a web browser. It brings the JavaScript language to the server-side,
  enabling developers to build scalable, high-performance, and event-driven applications.

  Let''s disc...'
---

Node.js est un environnement d'exécution puissant pour exécuter du code JavaScript _en dehors_ d'un navigateur web. Il amène le langage JavaScript côté serveur, permettant aux développeurs de créer des applications scalables, haute performance et pilotées par événements.

Découvrons comment fonctionne le code Node.js, et comment ce code peut être intégré dans votre JavaScript puis exécuté.

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/pSvvqaXCL30]

Node.js permet aux développeurs d'utiliser JavaScript à la fois côté client et côté serveur, offrant un langage et un écosystème unifiés. Cela élimine le besoin de changer de contexte et permet la réutilisation de code entre le front-end et le back-end. Cela se traduit par une productivité améliorée et un temps de développement réduit.

Node.js dispose d'un vaste et actif écosystème de modules et de bibliothèques disponibles via le Node Package Manager (npm). Cet écosystème riche offre des outils et des packages prêts à l'emploi pour diverses fonctionnalités, telles que des frameworks web, des connecteurs de base de données, l'authentification et des frameworks de test. 

Les développeurs peuvent exploiter ces modules pour accélérer le développement et améliorer les fonctionnalités des applications.

Étant donné tout cela, Node.js est particulièrement bien adapté pour construire :

* Des applications web
* Des API scalables
* Des applications en temps réel nécessitant des mises à jour de données instantanées et une communication bidirectionnelle comme les applications de chat et les jeux multijoueurs
* Des applications de streaming comme le traitement audio ou vidéo ou l'analyse en temps réel
* Des applications monopages
* Des déploiements pour l'Internet des objets

Tout cela semble correspondre à des applications web utiles ? Je le pensais aussi. Alors voyons comment tout cela fonctionne. 

## Comment construire un environnement serveur Node.js

Tout d'abord, vous n'aurez pas besoin de configurer et d'exécuter un serveur web tiers comme Apache HTTPD ou NGINX, ni de placer votre contenu dans la hiérarchie du répertoire `/var/www/html`. C'est parce que Node.js est, entre autres, un framework de serveur web. 

Permettez-moi de vous montrer ce que cela signifie. Vous devrez vous assurer d'avoir Node.js installé ainsi que les dépendances nécessaires. Dans l'ensemble, vous utiliserez le gestionnaire de packages NPM pour cela. Il existe une excellente documentation pour installer Node sur votre système d'exploitation [sur le site officiel](https://nodejs.org/en/download). 

Vous pouvez confirmer que Node et NPM sont actifs et prêts à l'action en exécutant ces commandes :

```
$ node -v
v18.16.0
$ npm -v
9.5.1
```

Pour avoir un peu de HTML avec lequel travailler, vous devriez trouver ou créer un simple fichier `index.html` et l'enregistrer dans un répertoire local sur votre machine. Cette commande téléchargera le `html` d'une page LPI depuis mon propre site web si vous avez besoin de quelque chose de rapide et de petit :

```
wget https://bootstrap-it.com/lpi/
```

Examinons le code `server.js` que nous avons utilisé pour notre serveur Node. 

```javascript
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  // Lire le fichier HTML
  fs.readFile('index.html', 'utf8', (err, data) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Erreur de chargement du fichier HTML');
      return;
    }

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(data);
  });
});

const port = 3000;
server.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur http://localhost:${port}`);
});
```

Maintenant, analysons ce code, section par section. Nous commençons par charger deux modules nécessaires : `http` pour gérer l'hébergement du site web, et `fs` pour lire les fichiers HTML. 

```javascript
const http = require('http');
const fs = require('fs');
```

Nous créons ensuite une fonction serveur – appelée `server`. Lorsqu'elle est appelée, elle lira et servira notre fichier `index.html` (générant un code de succès 200) ou, s'il y a un problème de lecture du fichier, elle générera un message d'erreur 500.

```javascript
  fs.readFile('index.html', 'utf8', (err, data) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Erreur de chargement du fichier HTML');
      return;
    }
```

Le code continue en définissant le port 3000 comme port d'écoute pour notre application – bien que, techniquement, vous puissiez le changer pour n'importe quelle valeur entre 1 et 65535. 

```javascript
const port = 3000;
```

Enfin, nous appelons la fonction `server` en utilisant la méthode `listen` et en spécifiant le numéro de port, puis en écrivant une entrée dans `console.log`.

```javascript
server.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur http://localhost:${port}`);
```

## Comment exécuter votre serveur Node.js

L'exécution de la commande `npm init` dans le même répertoire où vos fichiers de programme résideront est utilisée pour initialiser un nouveau projet Node.js et créer un fichier `package.json`. 

Le fichier `package.json` sert de manifeste pour le projet, contenant des métadonnées et des informations de configuration sur le projet, ses dépendances, ses scripts et autres détails.

Vous pouvez ajouter manuellement des dépendances au fichier ou utiliser :

```js
npm install <nom-du-package> 
```

...pour ajouter des packages et leurs versions à la section des dépendances du `package.json`.

Lorsque vous exécutez réellement `npm init` pour initialiser un répertoire pour un nouveau projet, un script vous posera quelques questions. Les valeurs par défaut que npm vous suggère incluront `1.0.0` comme numéro de version et un point d'entrée `index.js`. 

Vous aurez également la possibilité de définir un dépôt git, des mots-clés et un choix de modèles de licence utilisateur. Toutes les valeurs par défaut devraient fonctionner parfaitement.

Lorsque cela est terminé, le script vous montrera la version proposée au format JSON de vos paramètres et demandera votre approbation. Le fichier `package.json` qui a été créé reflétera ces paramètres.

Pour notre projet, installez le module de connecteur de base de données MySQL ainsi qu'express.js :

```javascript
$ npm install mysql
$ npm install express.js
```

Aucun des deux ne prend plus de quelques secondes. Lorsque tout cela est terminé, je verrai qu'il y a maintenant un nouveau fichier en ville : `package-lock.json`. 

En jetant un coup d'œil à l'intérieur de ce fichier, vous verrez beaucoup de bonnes choses en JSON. De quoi s'agit-il ? Le fichier package-lock.json est généré automatiquement par npm lorsque vous installez des dépendances pour votre projet. Il sert de fichier de verrouillage qui garantit des builds déterministes et reproductibles de votre projet dans différents environnements. 

Il est important d'inclure le fichier package-lock.json dans les systèmes de contrôle de version comme Git afin que d'autres développeurs ou environnements de déploiement puissent reproduire l'arborescence exacte des dépendances et les versions utilisées dans le projet. Cela garantit la cohérence et évite les conflits ou surprises potentiels lors de l'utilisation des dépendances.

Il y aura également un nouveau répertoire `node_modules` qui a été créé et peuplé automatiquement par cette opération d'initialisation. Ce répertoire est un emplacement de stockage pour tous les packages et modules dont notre projet dépend. Lorsque vous installez des packages à l'aide de `npm install`, les packages téléchargés sont placés ici. 

npm résout et installe automatiquement les dépendances requises de chaque package. Il crée une structure hiérarchique dans le répertoire node_modules qui reflète l'arborescence des dépendances de votre projet.

Lancer votre serveur est simple :

```javascript
$ node server.js
```

Pour afficher le service, ouvrez votre navigateur et dirigez-le vers l'URL de l'application, en utilisant le port `3000`. Lorsque votre navigateur est sur la même machine que le serveur Node, voici à quoi cela ressemblera :

```javascript
localhost:3000
```

Bien sûr, vous n'avez pas vraiment besoin de Node.js juste pour cela. La valeur de Node.js vient de la construction de l'interactivité utilisateur en l'intégrant avec une base de données backend. Cela peut se faire en utilisant Express.js, mais cela devra attendre une autre fois.

## Conclusion

Ce que nous _avons_ vu ici, c'est comment la magie derrière la construction d'un environnement Node.js peut fournir toute l'infrastructure et les fonctionnalités backend dont vous avez besoin pour lancer et maintenir un serveur interactif et dynamique.

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_