---
title: Comment développer et déployer des micro-frontends avec Single-SPA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-03T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/developing-and-deploying-micro-frontends-with-single-spa
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/single-spa-3.jpg
tags:
- name: architecture
  slug: architecture
- name: AWS
  slug: aws
- name: Front-end Development
  slug: front-end-development
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Travis CI
  slug: travis-ci
- name: Web Development
  slug: web-development
seo_title: Comment développer et déployer des micro-frontends avec Single-SPA
seo_desc: 'By Tyler Hawkins

  Micro-frontends are the future of front end web development.

  Inspired by microservices, which allow you to break up your backend into smaller
  pieces, micro-frontends allow you to build, test, and deploy pieces of your frontend
  app in...'
---

Par Tyler Hawkins

Les micro-frontends sont l'avenir du développement web frontal.

Inspirés par les microservices, qui permettent de diviser votre backend en plus petits morceaux, les micro-frontends permettent de construire, tester et déployer des parties de votre application frontend indépendamment les unes des autres. 

Selon le framework de micro-frontend que vous choisissez, vous pouvez même avoir plusieurs applications micro-frontend — écrites en React, Angular, Vue, ou autre — coexistant pacifiquement ensemble dans la même application plus large.

Dans cet article, nous allons développer une application composée de micro-frontends en utilisant [single-spa](https://single-spa.js.org/) et la déployer sur [Heroku](https://www.heroku.com/). 

Nous allons configurer l'intégration continue en utilisant [Travis CI](https://travis-ci.org/). Chaque pipeline CI va bundler le JavaScript pour une application micro-frontend puis télécharger les artefacts de build résultants sur [AWS S3](https://aws.amazon.com/s3/). 

Enfin, nous allons apporter une mise à jour à l'une des applications micro-frontend et voir comment elle peut être déployée en production indépendamment des autres applications micro-frontend.

# Aperçu de l'application de démonstration

![Application de démonstration — résultat final](https://www.freecodecamp.org/news/content/images/2020/07/mfe1.png)
_Application de démonstration — résultat final_

Avant de discuter des instructions étape par étape, obtenons un aperçu rapide de ce qui compose l'application de démonstration. Cette application est composée de quatre sous-applications :

1. Une [application conteneur](https://github.com/thawkin3/single-spa-demo-root-config) qui sert de conteneur principal de la page et coordonne le montage et le démontage des applications micro-frontend
2. Une [application de barre de navigation micro-frontend](https://github.com/thawkin3/single-spa-demo-nav) qui est toujours présente sur la page
3. Une [application micro-frontend "page 1"](https://github.com/thawkin3/single-spa-demo-page-1) qui ne s'affiche que lorsqu'elle est active
4. Une [application micro-frontend "page 2"](https://github.com/thawkin3/single-spa-demo-page-2) qui ne s'affiche également que lorsqu'elle est active

Ces quatre applications vivent toutes dans des dépôts séparés, disponibles sur GitHub, que j'ai liés ci-dessus.

Le résultat final est assez simple en termes d'interface utilisateur, mais, pour être clair, l'interface utilisateur n'est pas le point ici. 

Si vous suivez sur votre propre machine, à la fin de cet article, vous aurez également toute l'infrastructure sous-jacente nécessaire pour commencer avec votre propre application micro-frontend.

Très bien, prenez votre équipement de plongée, car il est temps de plonger !

# Création de l'application conteneur

Pour générer les applications pour cette démonstration, nous allons utiliser un outil d'interface de ligne de commande (CLI) appelé [create-single-spa](https://single-spa.js.org/docs/create-single-spa/). La version de create-single-spa au moment de l'écriture est 1.10.0, et la version de single-spa installée via la CLI est 4.4.2.

Nous allons suivre ces étapes pour créer l'application conteneur (parfois appelée la configuration racine) :

```bash
mkdir single-spa-demo

cd single-spa-demo

mkdir single-spa-demo-root-config

cd single-spa-demo-root-config

npx create-single-spa
```

Nous allons ensuite suivre les invites de la CLI :

1. Sélectionnez "single spa root config"
2. Sélectionnez "yarn" ou "npm" (j'ai choisi "yarn")
3. Entrez un nom d'organisation (j'ai utilisé "thawkin3", mais cela peut être ce que vous voulez)

Super ! Maintenant, si vous consultez le répertoire `single-spa-demo-root-config`, vous devriez voir une application squelette de configuration racine. Nous allons la personnaliser un peu, mais d'abord, utilisons également l'outil CLI pour créer nos trois autres applications micro-frontend.

# Création des applications micro-frontend

Pour générer notre première application micro-frontend, la barre de navigation, nous allons suivre ces étapes :

```bash
cd ..

mkdir single-spa-demo-nav

cd single-spa-demo-nav

npx create-single-spa
```

Nous allons ensuite suivre les invites de la CLI :

1. Sélectionnez "single-spa application / parcel"
2. Sélectionnez "react"
3. Sélectionnez "yarn" ou "npm" (j'ai choisi "yarn")
4. Entrez un nom d'organisation, le même que celui utilisé lors de la création de l'application de configuration racine ("thawkin3" dans mon cas)
5. Entrez un nom de projet (j'ai utilisé "single-spa-demo-nav")

Maintenant que nous avons créé l'application de barre de navigation, nous pouvons suivre ces mêmes étapes pour créer nos deux applications de page. Mais nous remplacerons chaque occurrence de "single-spa-demo-nav" par "single-spa-demo-page-1" la première fois et par "single-spa-demo-page-2" la deuxième fois.

À ce stade, nous avons généré les quatre applications dont nous avons besoin : une application conteneur et trois applications micro-frontend. Il est maintenant temps de relier nos applications ensemble.

# Enregistrement des applications micro-frontend avec l'application conteneur

Comme indiqué précédemment, l'une des principales responsabilités de l'application conteneur est de coordonner quand chaque application est "active" ou non. En d'autres termes, elle gère quand chaque application doit être affichée ou masquée. 

Pour aider l'application conteneur à comprendre quand chaque application doit être affichée, nous lui fournissons ce que l'on appelle des "fonctions d'activité". Chaque application a une fonction d'activité qui retourne simplement un booléen, vrai ou faux, indiquant si l'application est actuellement active ou non.

Dans le répertoire `single-spa-demo-root-config`, dans le fichier `activity-functions.js`, nous allons écrire les fonctions d'activité suivantes pour nos trois applications micro-frontend.

```javascript
export function prefix(location, ...prefixes) {
  return prefixes.some(
    prefix => location.href.indexOf(`${location.origin}/${prefix}`) !== -1
  );
}

export function nav() {
  // La barre de navigation est toujours active
  return true;
}

export function page1(location) {
  return prefix(location, 'page1');
}

export function page2(location) {
  return prefix(location, 'page2');
}
```

Ensuite, nous devons enregistrer nos trois applications micro-frontend avec single-spa. Pour cela, nous utilisons la fonction `registerApplication`. Cette fonction accepte un minimum de trois arguments : le nom de l'application, une méthode pour charger l'application et une fonction d'activité pour déterminer quand l'application est active.

Dans le répertoire `single-spa-demo-root-config`, dans le fichier `root-config.js`, nous allons ajouter le code suivant pour enregistrer nos applications :

```javascript
import { registerApplication, start } from "single-spa";
import * as isActive from "./activity-functions";

registerApplication(
  "@thawkin3/single-spa-demo-nav",
  () => System.import("@thawkin3/single-spa-demo-nav"),
  isActive.nav
);

registerApplication(
  "@thawkin3/single-spa-demo-page-1",
  () => System.import("@thawkin3/single-spa-demo-page-1"),
  isActive.page1
);

registerApplication(
  "@thawkin3/single-spa-demo-page-2",
  () => System.import("@thawkin3/single-spa-demo-page-2"),
  isActive.page2
);

start();
```

Maintenant que nous avons configuré les fonctions d'activité et enregistré nos applications, la dernière étape avant de pouvoir exécuter cela localement est de mettre à jour la carte d'importation locale à l'intérieur du fichier `index.ejs` dans le même répertoire. 

Nous allons ajouter le code suivant à l'intérieur de la balise `head` pour spécifier où chaque application peut être trouvée lors de l'exécution locale :

```javascript
<% if (isLocal) { %>
  <script type="systemjs-importmap">
    {
      "imports": {
        "@thawkin3/root-config": "http://localhost:9000/root-config.js",
        "@thawkin3/single-spa-demo-nav": "http://localhost:9001/thawkin3-single-spa-demo-nav.js",
        "@thawkin3/single-spa-demo-page-1": "http://localhost:9002/thawkin3-single-spa-demo-page-1.js",
        "@thawkin3/single-spa-demo-page-2": "http://localhost:9003/thawkin3-single-spa-demo-page-2.js"
      }
    }
  </script>
<% } %>  
```

Chaque application contient son propre script de démarrage, ce qui signifie que chaque application sera exécutée localement sur son propre serveur de développement pendant le développement local. Comme vous pouvez le voir, notre application de barre de navigation est sur le port 9001, notre application de page 1 est sur le port 9002, et notre application de page 2 est sur le port 9003.

Avec ces trois étapes prises en charge, essayons notre application.

# Test d'exécution pour l'exécution locale

Pour exécuter notre application localement, nous pouvons suivre ces étapes :

1. Ouvrir quatre onglets de terminal, un pour chaque application
2. Pour la configuration racine, dans le répertoire `single-spa-demo-root-config` : `yarn start` (s'exécute sur le port 9000 par défaut)
3. Pour l'application de navigation, dans le répertoire `single-spa-demo-nav` : `yarn start --port 9001`
4. Pour l'application de page 1, dans le répertoire `single-spa-demo-page-1` : `yarn start --port 9002`
5. Pour l'application de page 2, dans le répertoire `single-spa-demo-page-2` : `yarn start --port 9003`

Maintenant, nous allons naviguer dans le navigateur vers [http://localhost:9000](http://localhost:9000/) pour voir notre application.

Nous devrions voir... du texte ! Super excitant.

![Application de démonstration — page principale](https://www.freecodecamp.org/news/content/images/2020/07/mfe2.png)
_Application de démonstration — page principale_

Sur notre page principale, la barre de navigation s'affiche car l'application de barre de navigation est toujours active.

Maintenant, naviguons vers [http://localhost:9000/page1](http://localhost:9000/page1). Comme le montrent nos fonctions d'activité ci-dessus, nous avons spécifié que l'application de page 1 doit être active (affichée) lorsque le chemin de l'URL commence par "page1". Cela active donc l'application de page 1, et nous devrions maintenant voir le texte pour la barre de navigation et l'application de page 1.

![Application de démonstration — route de la page 1](https://www.freecodecamp.org/news/content/images/2020/07/mfe3.png)
_Application de démonstration — route de la page 1_

Une fois de plus, naviguons maintenant vers [http://localhost:9000/page2](http://localhost:9000/page2). Comme prévu, cela active l'application de page 2, donc nous devrions maintenant voir le texte pour la barre de navigation et l'application de page 2.

![Application de démonstration — route de la page 2](https://www.freecodecamp.org/news/content/images/2020/07/mfe4.png)
_Application de démonstration — route de la page 2_

# Apporter des ajustements mineurs aux applications

Jusqu'à présent, notre application n'est pas très excitante à regarder, mais nous avons une configuration de micro-frontend fonctionnelle qui s'exécute localement. Si vous n'êtes pas en train de crier de joie sur votre siège en ce moment, vous devriez l'être !

Apportons quelques améliorations mineures à nos applications pour qu'elles aient une meilleure apparence et un meilleur comportement.

### Spécification des conteneurs de montage

Tout d'abord, si vous actualisez votre page encore et encore lors de la visualisation de l'application, vous pouvez remarquer que parfois les applications se chargent dans le désordre, avec l'application de page apparaissant au-dessus de l'application de barre de navigation. 

Cela est dû au fait que nous n'avons pas réellement spécifié _où_ chaque application doit être montée. Les applications sont simplement chargées par [SystemJS](https://github.com/systemjs/systemjs), et ensuite l'application qui termine le chargement le plus rapidement est ajoutée à la page en premier.

Nous pouvons corriger cela en spécifiant un conteneur de montage pour chaque application lors de leur enregistrement.

Dans notre fichier `index.ejs` sur lequel nous avons travaillé précédemment, ajoutons un peu de HTML pour servir de conteneurs de contenu principaux pour la page :

```html
<div id="nav-container"></div>
<main>
  <div id="page-1-container"></div>
  <div id="page-2-container"></div>
</main>
```

Ensuite, dans notre fichier `root-config.js` où nous avons enregistré nos applications, fournissons un quatrième argument à chaque appel de fonction qui inclut l'élément DOM où nous souhaitons monter chaque application :

```javascript
import { registerApplication, start } from "single-spa";
import * as isActive from "./activity-functions";

registerApplication(
  "@thawkin3/single-spa-demo-nav",
  () => System.import("@thawkin3/single-spa-demo-nav"),
  isActive.nav,
  { domElement: document.getElementById('nav-container') }
);

registerApplication(
  "@thawkin3/single-spa-demo-page-1",
  () => System.import("@thawkin3/single-spa-demo-page-1"),
  isActive.page1,
  { domElement: document.getElementById('page-1-container') }
);

registerApplication(
  "@thawkin3/single-spa-demo-page-2",
  () => System.import("@thawkin3/single-spa-demo-page-2"),
  isActive.page2,
  { domElement: document.getElementById('page-2-container') }
);

start();
```

Maintenant, les applications seront toujours montées à un emplacement spécifique et prévisible. Bien !

### Stylisation de l'application

Ensuite, stylisons un peu notre application. Le texte noir simple sur fond blanc n'est pas très intéressant à regarder.

Dans le répertoire `single-spa-demo-root-config`, dans le fichier `index.ejs` à nouveau, nous pouvons ajouter quelques styles de base pour toute l'application en collant le CSS suivant en bas de la balise `head` :

```html
<style>
  body, html { margin: 0; padding: 0; font-size: 16px; font-family: Arial, Helvetica, sans-serif; height: 100%; }
  body { display: flex; flex-direction: column; }
  * { box-sizing: border-box; }
</style>
```

Ensuite, nous pouvons styliser notre application de barre de navigation en trouvant le répertoire `single-spa-demo-nav`, en créant un fichier `root.component.css` et en ajoutant le CSS suivant :

```css
.nav {
  display: flex;
  flex-direction: row;
  padding: 20px;
  background: #000;
  color: #fff;
}

.link {
  margin-right: 20px;
  color: #fff;
  text-decoration: none;
}

.link:hover,
.link:focus {
  color: #1098f7;
}
```

Nous pouvons ensuite mettre à jour le fichier `root.component.js` dans le même répertoire pour importer le fichier CSS et appliquer ces classes et styles à notre HTML. Nous allons également changer le contenu de la barre de navigation pour qu'il contienne réellement deux liens afin que nous puissions naviguer dans l'application en cliquant sur les liens au lieu d'entrer une nouvelle URL dans la barre d'adresse du navigateur.

```javascript
import React from "react";
import "./root.component.css";

export default function Root() {
  return (
    <nav className="nav">
      <a href="/page1" className="link">
        Page 1
      </a>
      <a href="/page2" className="link">
        Page 2
      </a>
    </nav>
  );
}
```

Nous allons suivre un processus similaire pour les applications de page 1 et de page 2 également. Nous allons créer un fichier `root.component.css` pour chaque application dans leurs répertoires de projet respectifs et mettre à jour les fichiers `root.component.js` pour les deux applications également.

Pour l'application de page 1, les modifications ressemblent à ceci :

```css
.container1 {
  background: #1098f7;
  color: white;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  font-size: 3rem;
}
```

```javascript
import React from "react";
import "./root.component.css";

export default function Root() {
  return (
    <div className="container1">
      <p>Page 1 App</p>
    </div>
  );
}
```

Et pour l'application de page 2, les modifications ressemblent à ceci :

```css
.container2 {
  background: #9e4770;
  color: white;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  font-size: 3rem;
}
```

```javascript
import React from "react";
import "./root.component.css";

export default function Root() {
  return (
    <div className="container2">
      <p>Page 2 App</p>
    </div>
  );
}
```

### Ajout de React Router

Le dernier petit changement que nous allons apporter est d'ajouter [React Router](https://reacttraining.com/react-router/) à notre application. Actuellement, les deux liens que nous avons placés dans la barre de navigation sont simplement des balises d'ancrage normales, donc la navigation d'une page à l'autre provoque un rafraîchissement de la page. Notre application sera beaucoup plus fluide si la navigation est gérée côté client avec React Router.

Pour utiliser React Router, nous devons d'abord l'installer. À partir du terminal, dans le répertoire `single-spa-demo-nav`, nous allons installer React Router en utilisant yarn en entrant `yarn add react-router-dom`. (Ou si vous utilisez npm, vous pouvez entrer `npm install react-router-dom`.)

Ensuite, dans le répertoire `single-spa-demo-nav` dans le fichier `root.component.js`, nous allons remplacer nos balises d'ancrage par les composants `Link` de React Router comme suit :

```javascript
import React from "react";
import { BrowserRouter, Link } from "react-router-dom";
import "./root.component.css";

export default function Root() {
  return (
    <BrowserRouter>
      <nav className="nav">
        <Link to="/page1" className="link">
          Page 1
        </Link>
        <Link to="/page2" className="link">
          Page 2
        </Link>
      </nav>
    </BrowserRouter>
  );
}
```

Cool. Cela a l'air et fonctionne beaucoup mieux !

![Application de démonstration — stylisée et utilisant React Router](https://www.freecodecamp.org/news/content/images/2020/07/mfe5.png)
_Application de démonstration — stylisée et utilisant React Router_

# Préparation pour la production

À ce stade, nous avons tout ce dont nous avons besoin pour continuer à travailler sur l'application tout en l'exécutant localement. Mais comment la rendre accessible au public ? 

Il existe plusieurs approches possibles que nous pouvons adopter en utilisant nos outils de choix, mais les principales tâches sont :

1. avoir un endroit où nous pouvons télécharger nos artefacts de build, comme un CDN, et
2. automatiser ce processus de téléchargement des artefacts chaque fois que nous fusionnons du nouveau code dans la branche principale.

Pour cet article, nous allons utiliser AWS S3 pour stocker nos actifs, et nous allons utiliser Travis CI pour exécuter un travail de build et un travail de téléchargement dans le cadre d'un pipeline d'intégration continue.

Commençons par configurer le bucket S3.

### Configuration du bucket AWS S3

Cela devrait aller de soi, mais vous aurez besoin d'un compte AWS si vous suivez ce guide. 

Si nous sommes l'utilisateur root sur notre compte AWS, nous pouvons créer un nouvel utilisateur IAM qui a un accès programmatique uniquement. Cela signifie que nous recevrons une clé d'accès ID et une clé d'accès secrète de la part d'AWS lorsque nous créerons le nouvel utilisateur. Nous devrons les stocker dans un endroit sûr car nous en aurons besoin plus tard. 

Enfin, cet utilisateur doit se voir accorder des autorisations pour travailler uniquement avec S3, afin que le niveau d'accès soit limité si nos clés tombent entre de mauvaises mains.

AWS dispose de ressources utiles pour les [meilleures pratiques avec les clés d'accès](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) et la [gestion des clés d'accès pour les utilisateurs IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) qui valent la peine d'être consultées si vous n'êtes pas familier avec la manière de procéder.

Ensuite, nous devons créer un bucket S3. S3 signifie Simple Storage Service et est essentiellement un endroit pour télécharger et stocker des fichiers hébergés sur les serveurs d'Amazon. Un bucket est simplement un répertoire. 

J'ai nommé mon bucket "single-spa-demo", mais vous pouvez nommer le vôtre comme vous le souhaitez. Vous pouvez suivre les guides AWS pour [comment créer un nouveau bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) pour plus d'informations.

![Bucket AWS S3](https://www.freecodecamp.org/news/content/images/2020/07/mfe6.png)
_Bucket AWS S3_

Une fois que nous avons créé notre bucket, il est également important de s'assurer que le bucket est public et que [CORS (cross-origin resource sharing) est activé pour notre bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html#how-do-i-enable-cors) afin que nous puissions accéder et utiliser nos actifs téléchargés dans notre application. 

Dans les autorisations de notre bucket, nous pouvons ajouter les règles de configuration CORS suivantes :

```xml
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>*</AllowedOrigin>
   <AllowedMethod>GET</AllowedMethod>
 </CORSRule>
</CORSConfiguration>
```

Dans la console AWS, cela ressemble à ceci après avoir cliqué sur Enregistrer :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/mfe7.png)
_Configuration CORS_

### Création d'un travail Travis CI pour télécharger les artefacts sur AWS S3

Maintenant que nous avons un endroit où télécharger des fichiers, configurons un processus automatisé qui se chargera de télécharger de nouveaux bundles JavaScript chaque fois que nous fusionnerons du nouveau code dans la branche principale pour l'un de nos dépôts.

Pour cela, nous allons utiliser [Travis CI](https://travis-ci.org/). Comme mentionné précédemment, chaque application vit dans son propre dépôt sur GitHub, donc nous avons quatre dépôts GitHub à gérer. Nous pouvons [intégrer Travis CI avec chacun de nos dépôts](https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github) et configurer des pipelines d'intégration continue pour chacun d'eux.

Pour configurer Travis CI pour un projet donné, nous créons un fichier `.travis.yml` dans le répertoire racine du projet. Créons ce fichier dans le répertoire `single-spa-demo-root-config` et insérons le code suivant :

```yaml
language: node_js
node_js:
  - node
script:
  - yarn build
  - echo "Commit sha - $TRAVIS_COMMIT"
  - mkdir -p dist/@thawkin3/root-config/$TRAVIS_COMMIT
  - mv dist/*.* dist/@thawkin3/root-config/$TRAVIS_COMMIT/
deploy:
  provider: s3
  access_key_id: "$AWS_ACCESS_KEY_ID"
  secret_access_key: "$AWS_SECRET_ACCESS_KEY"
  bucket: "single-spa-demo"
  region: "us-west-2"
  cache-control: "max-age=31536000"
  acl: "public_read"
  local_dir: dist
  skip_cleanup: true
  on:
    branch: master
```

Cette implémentation est ce que j'ai conçu après avoir examiné la [documentation Travis CI pour les téléchargements AWS S3](https://docs.travis-ci.com/user/deployment-v2/providers/s3/) et un [exemple de configuration Travis CI pour single-spa](https://github.com/single-spa/import-map-deployer/blob/master/examples/ci-for-javascript-repo/travis-digital-ocean-spaces/.travis.yml).

Parce que nous ne voulons pas que nos secrets AWS soient exposés dans notre dépôt GitHub, nous pouvons les stocker en tant que variables d'environnement. Vous pouvez placer des variables d'environnement et leurs valeurs secrètes dans la console web Travis CI pour tout ce que vous souhaitez garder privé, c'est donc là que le fichier `.travis.yml` obtient ces valeurs.

Maintenant, lorsque nous validons et poussons du nouveau code dans la branche principale, le travail Travis CI s'exécutera, ce qui construira le bundle JavaScript pour l'application puis téléchargera ces actifs sur S3. Pour vérifier, nous pouvons consulter la console AWS pour voir nos fichiers nouvellement téléchargés :

![Fichiers téléchargés à la suite d'un travail Travis CI](https://www.freecodecamp.org/news/content/images/2020/07/mfe8.png)
_Fichiers téléchargés à la suite d'un travail Travis CI_

Super ! Jusqu'à présent, tout va bien. Maintenant, nous devons implémenter la même configuration Travis CI pour nos trois autres applications micro-frontend, mais en remplaçant les noms de répertoires dans le fichier `.travis.yml` selon les besoins. Après avoir suivi les mêmes étapes et fusionné notre code, nous avons maintenant quatre répertoires créés dans notre bucket S3, un pour chaque dépôt.

![Quatre répertoires dans notre bucket S3](https://www.freecodecamp.org/news/content/images/2020/07/mfe9.png)
_Quatre répertoires dans notre bucket S3_

# Création d'une carte d'importation pour la production

Faisons un récapitulatif de ce que nous avons fait jusqu'à présent. Nous avons quatre applications, toutes vivant dans des dépôts GitHub séparés. Chaque dépôt est configuré avec Travis CI pour exécuter un travail lorsque du code est fusionné dans la branche principale, et ce travail gère le téléchargement des artefacts de build dans un bucket S3. 

Avec tout cela en un seul endroit, il manque encore une chose : Comment ces nouveaux artefacts de build sont-ils référencés dans notre application conteneur ? En d'autres termes, même si nous poussons de nouveaux bundles JavaScript pour nos micro-frontends avec chaque nouvelle mise à jour, le nouveau code n'est pas encore utilisé dans notre application conteneur !

Si nous réfléchissons à la manière dont nous avons fait fonctionner notre application localement, nous avons utilisé une carte d'importation. Cette carte d'importation est simplement du JSON qui indique à l'application conteneur où chaque bundle JavaScript peut être trouvé. 

Mais notre carte d'importation précédente était spécifiquement utilisée pour exécuter l'application localement. Maintenant, nous devons créer une carte d'importation qui sera utilisée dans l'environnement de production.

Si nous regardons dans le répertoire `single-spa-demo-root-config`, dans le fichier `index.ejs`, nous voyons cette ligne :

```html
<script type="systemjs-importmap" src="https://storage.googleapis.com/react.microfrontends.app/importmap.json"></script>

```

Ouvrir cette URL dans le navigateur révèle une carte d'importation qui ressemble à ceci :

```json
{
  "imports": {
    "react": "https://cdn.jsdelivr.net/npm/react@16.13.1/umd/react.production.min.js",
    "react-dom": "https://cdn.jsdelivr.net/npm/react-dom@16.13.1/umd/react-dom.production.min.js",
    "single-spa": "https://cdn.jsdelivr.net/npm/single-spa@5.5.3/lib/system/single-spa.min.js",
    "@react-mf/root-config": "https://react.microfrontends.app/root-config/e129469347bb89b7ff74bcbebb53cc0bb4f5e27f/react-mf-root-config.js",
    "@react-mf/navbar": "https://react.microfrontends.app/navbar/631442f229de2401a1e7c7835dc7a56f7db606ea/react-mf-navbar.js",
    "@react-mf/styleguide": "https://react.microfrontends.app/styleguide/f965d7d74e99f032c27ba464e55051ae519b05dd/react-mf-styleguide.js",
    "@react-mf/people": "https://react.microfrontends.app/people/dd205282fbd60b09bb3a937180291f56e300d9db/react-mf-people.js",
    "@react-mf/api": "https://react.microfrontends.app/api/2966a1ca7799753466b7f4834ed6b4f2283123c5/react-mf-api.js",
    "@react-mf/planets": "https://react.microfrontends.app/planets/5f7fc62b71baeb7a0724d4d214565faedffd8f61/react-mf-planets.js",
    "@react-mf/things": "https://react.microfrontends.app/things/7f209a1ed9ac9690835c57a3a8eb59c17114bb1d/react-mf-things.js",
    "rxjs": "https://cdn.jsdelivr.net/npm/@esm-bundle/rxjs@6.5.5/system/rxjs.min.js",
    "rxjs/operators": "https://cdn.jsdelivr.net/npm/@esm-bundle/rxjs@6.5.5/system/rxjs-operators.min.js"
  }
}
```

Cette carte d'importation était celle fournie par défaut en exemple lorsque nous avons utilisé la CLI pour générer notre application conteneur. Ce que nous devons faire maintenant est de remplacer cette carte d'importation d'exemple par une carte d'importation qui référence réellement les bundles que nous utilisons.

Ainsi, en utilisant la carte d'importation originale comme modèle, nous pouvons créer un nouveau fichier appelé `importmap.json`, le placer _en dehors de nos dépôts_ et ajouter du JSON qui ressemble à ceci :

```json
{
  "imports": {
    "react": "https://cdn.jsdelivr.net/npm/react@16.13.0/umd/react.production.min.js",
    "react-dom": "https://cdn.jsdelivr.net/npm/react-dom@16.13.0/umd/react-dom.production.min.js",
    "single-spa": "https://cdn.jsdelivr.net/npm/single-spa@5.5.1/lib/system/single-spa.min.js",
    "@thawkin3/root-config": "https://single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/root-config/179ba4f2ce4d517bf461bee986d1026c34967141/root-config.js",
    "@thawkin3/single-spa-demo-nav": "https://single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/single-spa-demo-nav/f0e9d35392ea0da8385f6cd490d6c06577809f16/thawkin3-single-spa-demo-nav.js",
    "@thawkin3/single-spa-demo-page-1": "https://single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/single-spa-demo-page-1/4fd417ee3faf575fcc29d17d874e52c15e6f0780/thawkin3-single-spa-demo-page-1.js",
    "@thawkin3/single-spa-demo-page-2": "https://single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/single-spa-demo-page-2/8c58a825c1552aab823bcbd5bdd13faf2bd4f9dc/thawkin3-single-spa-demo-page-2.js"
  }
}
```

Vous noterez que les trois premières importations concernent des dépendances partagées : react, react-dom et single-spa. Ainsi, nous n'avons pas quatre copies de React dans notre application, ce qui provoquerait du ballonnement et des temps de téléchargement plus longs. Ensuite, nous avons des importations pour chacune de nos quatre applications. L'URL est simplement l'URL de chaque fichier téléchargé dans S3 (appelé un "objet" dans la terminologie AWS).

Maintenant que nous avons créé ce fichier, nous pouvons le télécharger manuellement dans notre bucket dans S3 via la console AWS. 

**Remarque** : Il s'agit d'une mise en garde assez importante et intéressante lors de l'utilisation de single-spa : La carte d'importation ne vit pas réellement dans le contrôle de source ou dans l'un des dépôts git. Ainsi, la carte d'importation peut être mise à jour à la volée sans nécessiter de modifications validées dans un dépôt. Nous reviendrons sur ce concept dans un petit instant.

![Carte d'importation téléchargée manuellement dans le bucket S3](https://www.freecodecamp.org/news/content/images/2020/07/mfe10.png)
_Carte d'importation téléchargée manuellement dans le bucket S3_

Enfin, nous pouvons maintenant référencer ce nouveau fichier dans notre fichier `index.ejs` au lieu de référencer la carte d'importation originale.

```html
<script type="systemjs-importmap" src="//single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/importmap.json"></script>

```

# Création d'un serveur de production

Nous approchons de plus en plus d'avoir quelque chose en production ! Nous allons héberger cette démonstration sur Heroku, donc pour ce faire, nous devons créer un serveur Node.js et [Express](https://expressjs.com/) simple pour servir notre fichier.

Tout d'abord, dans le répertoire `single-spa-demo-root-config`, nous allons installer express en exécutant `yarn add express` (ou `npm install express`). Ensuite, nous allons ajouter un fichier appelé `server.js` qui contient une petite quantité de code pour démarrer un serveur express et servir notre fichier `index.html` principal.

```javascript
const express = require("express");
const path = require("path");
const PORT = process.env.PORT || 5000;

express()
  .use(express.static(path.join(__dirname, "dist")))
  .get("*", (req, res) => {
    res.sendFile("index.html", { root: "dist" });
  })
  .listen(PORT, () => console.log(`Listening on ${PORT}`));
```

Enfin, nous allons mettre à jour les scripts NPM dans notre fichier `package.json` pour différencier l'exécution du serveur en mode développement et l'exécution du serveur en mode production.

```json
"scripts": {
  "build": "webpack --mode=production",
  "lint": "eslint src",
  "prettier": "prettier --write './**'",
  "start:dev": "webpack-dev-server --mode=development --port 9000 --env.isLocal=true",
  "start": "node server.js",
  "test": "jest"
}
```

# Déploiement sur Heroku

Maintenant que nous avons un serveur de production prêt, déployons cette chose sur Heroku ! Pour ce faire, vous devrez avoir un [compte Heroku créé](https://signup.heroku.com/), l'[interface de ligne de commande Heroku](https://devcenter.heroku.com/articles/heroku-cli) installée et être connecté. Le déploiement sur Heroku est aussi simple que 1-2-3 :

1. Dans le répertoire `single-spa-demo-root-config` : `heroku create thawkin3-single-spa-demo` (en changeant ce dernier argument par un nom unique à utiliser pour votre application Heroku)
2. `git push heroku master`
3. `heroku open`

Et avec cela, nous sommes opérationnels en production. En exécutant la commande `heroku open`, vous devriez voir votre application s'ouvrir dans votre navigateur. Essayez de naviguer entre les pages en utilisant les liens de navigation pour voir les différentes applications micro-frontend se monter et se démonter.

![Application de démonstration — opérationnelle en production](https://www.freecodecamp.org/news/content/images/2020/07/mfe11.png)
_Application de démonstration — opérationnelle en production_

# Apporter des mises à jour

À ce stade, vous pourriez vous demander : "Tout ce travail pour cela ? Pourquoi ?" Et vous auriez raison. En quelque sorte. C'est beaucoup de travail, et nous n'avons pas grand-chose à montrer pour cela, du moins pas visuellement. Mais nous avons posé les bases pour toutes les améliorations d'application que nous souhaitons apporter. 

Le coût de configuration pour tout microservice ou micro-frontend est souvent beaucoup plus élevé que le coût de configuration pour un monolithe ; ce n'est que plus tard que vous commencez à récolter les récompenses.

Alors commençons à penser aux modifications futures. Supposons qu'il est maintenant cinq ou dix ans plus tard, et que votre application a grandi. Beaucoup. Et, pendant ce temps, un nouveau framework à la mode a été publié, et vous mourez d'envie de réécrire toute votre application en utilisant ce nouveau framework. 

En travaillant avec un monolithe, cela serait probablement un effort de plusieurs années et pourrait être presque impossible à accomplir. Mais avec les micro-frontends, vous pourriez remplacer les technologies pièce par pièce de l'application, vous permettant de transitionner lentement et en douceur vers une nouvelle stack technologique. Magique !

Ou, vous pourriez avoir une partie de votre application qui change fréquemment et une autre partie de votre application qui est rarement touchée. En apportant des mises à jour à l'application volatile, ne serait-il pas agréable de pouvoir simplement laisser le code hérité tranquille ? 

Avec un monolithe, il est possible que les modifications que vous apportez à un endroit de votre application affectent d'autres sections de votre application. Et si vous modifiiez des feuilles de style que plusieurs sections du monolithe utilisaient ? Ou si vous mettiez à jour une dépendance qui était utilisée à de nombreux endroits différents ? 

Avec une approche micro-frontend, vous pouvez laisser ces soucis derrière vous, en refactorant et en mettant à jour une application là où c'est nécessaire tout en laissant les applications héritées tranquilles.

Mais comment apporter ce type de mises à jour ? Ou des mises à jour de quelque sorte, vraiment ? 

Actuellement, nous avons notre carte d'importation de production dans notre fichier `index.ejs`, mais elle pointe simplement vers le fichier que nous avons téléchargé manuellement dans notre bucket S3. Si nous voulions publier quelques nouvelles modifications maintenant, nous devrions pousser un nouveau code pour l'un des micro-frontends, obtenir un nouvel artefact de build, puis mettre à jour manuellement la carte d'importation avec une référence au nouveau bundle JavaScript.

Y a-t-il un moyen d'automatiser cela ? Oui !

# Mise à jour de l'une des applications

Supposons que nous voulons mettre à jour notre application de page 1 pour qu'elle affiche un texte différent. Afin d'automatiser le déploiement de cette modification, nous pouvons mettre à jour notre pipeline CI pour non seulement construire un artefact et le télécharger dans notre bucket S3, mais aussi pour mettre à jour la carte d'importation afin de référencer la nouvelle URL pour le dernier bundle JavaScript.

Commençons par mettre à jour notre fichier `.travis.yml` comme suit :

```yaml
language: node_js
node_js:
  - node
env:
  global:
    # include $HOME/.local/bin for `aws`
    - PATH=$HOME/.local/bin:$PATH
before_install:
  - pyenv global 3.7.1
  - pip install -U pip
  - pip install awscli
script:
  - yarn build
  - echo "Commit sha - $TRAVIS_COMMIT"
  - mkdir -p dist/@thawkin3/root-config/$TRAVIS_COMMIT
  - mv dist/*.* dist/@thawkin3/root-config/$TRAVIS_COMMIT/
deploy:
  provider: s3
  access_key_id: "$AWS_ACCESS_KEY_ID"
  secret_access_key: "$AWS_SECRET_ACCESS_KEY"
  bucket: "single-spa-demo"
  region: "us-west-2"
  cache-control: "max-age=31536000"
  acl: "public_read"
  local_dir: dist
  skip_cleanup: true
  on:
    branch: master
after_deploy:
  - chmod +x after_deploy.sh
  - "./after_deploy.sh"
```

Les principaux changements ici sont l'ajout d'une variable d'environnement globale, l'installation de l'interface de ligne de commande AWS et l'ajout d'un script `after_deploy` dans le pipeline. Cela fait référence à un fichier `after_deploy.sh` que nous devons créer. Le contenu sera :

```sh
echo "Downloading import map from S3"
aws s3 cp s3://single-spa-demo/@thawkin3/importmap.json importmap.json
echo "Updating import map to point to new version of @thawkin3/root-config"
node update-importmap.mjs
echo "Uploading new import map to S3"
aws s3 cp importmap.json s3://single-spa-demo/@thawkin3/importmap.json --cache-control 'public, must-revalidate, max-age=0' --acl 'public-read'
echo "Deployment successful"
```

Ce fichier télécharge la carte d'importation existante depuis S3, la modifie pour référencer le nouvel artefact de build, puis retélécharge la carte d'importation mise à jour sur S3. Pour gérer la mise à jour réelle du contenu du fichier de carte d'importation, nous utilisons un script personnalisé que nous ajouterons dans un fichier appelé `update-importmap.mjs`.

```javascript
// Note that this file requires node@13.2.0 or higher (or the --experimental-modules flag)
import fs from "fs";
import path from "path";
import https from "https";

const importMapFilePath = path.resolve(process.cwd(), "importmap.json");
const importMap = JSON.parse(fs.readFileSync(importMapFilePath));
const url = `https://single-spa-demo.s3-us-west-2.amazonaws.com/%40thawkin3/root-config/${process.env.TRAVIS_COMMIT}/root-config.js`;

https
  .get(url, res => {
    // HTTP redirects (301, 302, etc) not currently supported, but could be added
    if (res.statusCode >= 200 && res.statusCode < 300) {
      if (
        res.headers["content-type"] &&
        res.headers["content-type"].toLowerCase().trim() ===
          "application/javascript"
      ) {
        const moduleName = `@thawkin3/root-config`;
        importMap.imports[moduleName] = url;
        fs.writeFileSync(importMapFilePath, JSON.stringify(importMap, null, 2));
        console.log(
          `Updated import map for module ${moduleName}. New url is ${url}.`
        );
      } else {
        urlNotDownloadable(
          url,
          Error(`Content-Type response header must be application/javascript`)
        );
      }
    } else {
      urlNotDownloadable(
        url,
        Error(`HTTP response status was ${res.statusCode}`)
      );
    }
  })
  .on("error", err => {
    urlNotDownloadable(url, err);
  });

function urlNotDownloadable(url, err) {
  throw Error(
    `Refusing to update import map - could not download javascript file at url ${url}. Error was '${err.message}'`
  );
}
```

Notez que nous devons apporter ces modifications à ces trois fichiers dans tous nos dépôts GitHub afin que chacun d'eux puisse mettre à jour la carte d'importation après avoir créé un nouvel artefact de build. 

Le contenu des fichiers sera presque identique pour chaque dépôt, mais nous devrons changer les noms des applications ou les chemins d'URL vers les valeurs appropriées pour chacun.

### Une note à propos de la carte d'importation

Plus tôt, j'ai mentionné que le fichier de carte d'importation que nous avons téléchargé manuellement sur S3 ne vit pas réellement dans l'un de nos dépôts GitHub ou dans l'un de nos codes validés. Si vous êtes comme moi, cela semble probablement très étrange ! Tout ne devrait-il pas être dans le contrôle de source ?

La raison pour laquelle il n'est pas dans le contrôle de source est que notre pipeline CI peut gérer la mise à jour de la carte d'importation avec chaque nouvelle version d'application micro-frontend. 

Si la carte d'importation était dans le contrôle de source, apporter une mise à jour à une application micro-frontend nécessiterait des modifications dans deux dépôts : le dépôt de l'application micro-frontend où la modification est apportée, et le dépôt de configuration racine où la carte d'importation serait validée. Ce type de configuration invaliderait l'un des principaux avantages de l'architecture micro-frontend, qui est que chaque application peut être déployée complètement indépendamment des autres applications. 

Afin d'atteindre un certain niveau de contrôle de source sur la carte d'importation, nous pouvons toujours utiliser la fonction de versionnage de S3 pour notre bucket.

# Moment de vérité

Avec ces modifications apportées à nos pipelines CI, il est temps pour le moment de vérité final : pouvons-nous mettre à jour l'une de nos applications micro-frontend, la déployer indépendamment, puis voir ces modifications prendre effet en production sans avoir à toucher aucune de nos autres applications ?

Dans le répertoire `single-spa-demo-page-1`, dans le fichier `root.component.js`, changeons le texte de "Page 1 App" à "Page 1 App - MIS À JOUR !" Ensuite, validons cette modification et poussons-la et fusionnons-la avec la branche principale. 

Cela déclenchera le pipeline Travis CI pour construire le nouvel artefact de l'application de page 1 puis mettre à jour la carte d'importation pour référencer cette nouvelle URL de fichier.

Si nous naviguons ensuite dans notre navigateur vers [https://thawkin3-single-spa-demo.herokuapp.com/page1](https://thawkin3-single-spa-demo.herokuapp.com/page1), nous verrons maintenant... roulement de tambour... notre application mise à jour !

![Application de démonstration — mise à jour réussie de l'une des applications micro-frontend](https://www.freecodecamp.org/news/content/images/2020/07/mfe12.png)
_Application de démonstration — mise à jour réussie de l'une des applications micro-frontend_

# Conclusion

Je l'ai dit avant, et je le répète : **Les micro-frontends sont l'avenir du développement web frontal.** 

Les avantages sont énormes, notamment les déploiements indépendants, les zones de responsabilité indépendantes, des temps de construction et de test plus rapides, et la capacité de mélanger et d'assortir divers frameworks si nécessaire. 

Il y a quelques inconvénients, comme le coût initial de configuration et la complexité de la maintenance d'une architecture distribuée, mais je crois fermement que les avantages l'emportent sur les coûts.

Single-spa rend l'architecture micro-frontend facile. Maintenant, vous aussi, vous pouvez aller briser le monolithe !