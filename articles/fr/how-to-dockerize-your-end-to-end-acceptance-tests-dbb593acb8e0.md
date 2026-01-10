---
title: Comment Dockeriser vos tests d'acceptation End-to-End
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T01:13:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-your-end-to-end-acceptance-tests-dbb593acb8e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p0ALhZOLfRFYBvosshCmjQ.png
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Comment Dockeriser vos tests d'acceptation End-to-End
seo_desc: 'By Dominic Fraser


  _[Source](https://www.docker.com/what-docker" rel="noopener" target="blank" title=")

  This article serves as a “how-to” guide for using Selenium Docker images alongside
  CodeceptJS and an Express server.

  In it, we will cover:


  What i...'
---

Par Dominic Fraser

![Image](https://cdn-media-1.freecodecamp.org/images/VKuRIyPcfnVrGvjRB3oe6NrQ026qn9DzmXru)
_[Source](https://www.docker.com/what-docker" rel="noopener" target="_blank" title=")_

Cet article sert de guide "comment faire" pour utiliser les images Docker de Selenium avec CodeceptJS et un serveur Express.

Dans cet article, nous aborderons :

* Qu'est-ce que les tests d'acceptation E2E ?
* Pourquoi utiliser Docker ?
* Outils de test faiblement couplés
* Couches d'outils de test
* Création d'un projet de test

### Tests d'acceptation E2E

Les [tests d'acceptation](https://en.wikipedia.org/wiki/Acceptance_testing) sont une [phase](https://www.tutorialspoint.com/software_testing_dictionary/acceptance_testing.htm) dans un processus typique de développement logiciel. Ils couvrent les tests pour voir si le produit a répondu aux spécifications globales des exigences et s'il est "accepté" comme prêt pour la livraison. Il s'agit généralement de la dernière phase de test avant la mise en production du produit. Cela peut inclure des tests d'acceptation basés sur les utilisateurs, des tests d'acceptation basés sur les entreprises, ou même des tests alpha/bêta.

Les tests [End-to-End](http://toolsqa.com/software-testing/what-does-end-to-end-test-mean/) (E2E) sont une implémentation des tests d'acceptation. Il s'agit d'une _approche_ des tests d'acceptation, mais les termes ne sont pas synonymes. Il permet de tester le flux d'une application du début à la fin pour voir si elle fonctionne comme prévu. Dans le cas d'une application web, cela impliquerait de déterminer un scénario utilisateur et de tester chacune des étapes que l'utilisateur suivrait dans l'ordre. Le test échoue si le scénario n'est pas complété avec succès.

Différents outils existent pour automatiser ce processus, simulant l'interaction de l'utilisateur avec l'application.

### Pourquoi Docker ?

La création et l'exécution de tests E2E sont souvent considérées comme un processus instable et complexe. Cela nécessite beaucoup de configuration qui peut encore facilement échouer lorsqu'elle est exécutée sur différentes machines ou dans un environnement CI (intégration continue). L'installation et la maintenance de différents navigateurs et WebDrivers à la fois pour les tests locaux et les tests CI prennent du temps. Et même lorsque cela est fait, cela peut encore échouer en raison de problèmes simples tels que si la [résolution d'écran sur les machines locales des développeurs, ou dans CI, est différente](https://medium.com/@garrensmith/consistent-selenium-testing-with-docker-f2d5a24a1bc5).

Les avantages standards de Docker s'appliquent également : ne pas avoir à gérer la compatibilité du système d'exploitation ou avoir des dépendances installées. Pour exécuter le serveur Selenium, vous auriez besoin de Java installé ([ou au moins être démarré/arrêté explicitement](https://engineering.thetrainline.com/dockerize-your-webdriverio-environment-to-run-everywhere-4f98e7a1d80e)). Pour exécuter Express, vous auriez besoin de Node.js, et pour Chrome, vous auriez besoin de Chrome lui-même ainsi que de ChromeDriver.

Lorsque vous utilisez Docker, ces dépendances sont éliminées. Vous utilisez simplement différents conteneurs qui contiennent déjà ces éléments, qui fonctionneront précisément de la même manière, peu importe sur quelle machine ils sont exécutés. Lorsque vous pensez ensuite à la facilité avec laquelle vous pouvez intégrer Docker dans votre CI, la Dockerisation de votre processus de test devient un choix évident.

### Outils de test faiblement couplés

Il existe plusieurs frameworks disponibles lors de l'écriture de tests E2E, et pour un nouveau venu, il peut être difficile de savoir lequel choisir et dans lequel investir du temps. Si vous choisissez le mauvais, vous aurez perdu beaucoup de temps.

C'est là que [CodeceptJS](http://codecept.io/) entre en jeu. CodeceptJS est un framework de test qui adopte une approche basée sur les scénarios, [développement piloté par le comportement](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD), avec un langage d'API facile à comprendre et à utiliser pour les non-ingénieurs. Cependant, peut-être encore plus important, il est agnostique du backend. Il est écrit au-dessus de plusieurs bibliothèques de test populaires (WebDriverIO ou Puppeteer, par exemple) et son API de haut niveau unique communique avec celle que vous choisissez. Ses [créateurs croient](https://hackernoon.com/effective-end-2-end-testing-in-javascript-with-codeceptjs-37c8d7d6a928) que

> Vos tests ne doivent pas être liés à votre moteur d'exécution. Que vous choisissiez Selenium ou Puppeteer, vos tests doivent avoir presque la même apparence. Si vous (plus tard) ressentez les limitations d'un moteur, vous pouvez facilement basculer vos tests vers un autre.

### Couches d'outils de test

![Image](https://cdn-media-1.freecodecamp.org/images/CseVMJoB7kKBDdz-oWzad7JGicjB-7V80JBw)
_Quelques-uns des différents produits disponibles à chaque couche de simulation de l'interaction utilisateur avec un navigateur_

Prenons une approche ascendante pour voir comment chaque couche s'appuie sur la précédente.

Il est utile de référencer initialement [Selenium](https://www.seleniumhq.org/), un projet de longue date avec un ensemble d'outils activement utilisés, qui aujourd'hui est composé de Selenium WebDriver, Grid, Server et IDE. En créant ces outils, ils ont établi de nombreuses normes industrielles, souvent nommées de manière confuse d'après le produit Selenium dont elles proviennent. Cela peut être vu dans 'Selenium WebDriver', et le 'protocole WebDriver wire' qui a été établi dans son développement. Ceux qui sont applicables seront montrés plus en détail ci-dessous.

#### Navigateur

N'importe quel navigateur web : Chrome, Firefox, Internet Explorer, Safari, Opera, etc. Souvent appelé 'user agent' dans la documentation.

#### Protocole WebDriver wire du W3C

Le protocole WebDriver wire est un moyen neutre en termes de plateforme et de langage d'interagir avec les navigateurs web. Il définit un service web [RESTful](http://www.drdobbs.com/web-development/restful-web-services-a-tutorial/240169069) commun utilisant JSON sur HTTP dans des paires requête/réponse. Il permet de manipuler des éléments DOM à partir d'une source externe, tout en permettant la navigation vers des pages web, l'entrée utilisateur, l'exécution de JavaScript, et plus encore.

Initialement écrit par Selenium pour le Selenium WebDriver, ce protocole a maintenant atteint le stade de l'Éditeur dans le processus de devenir une norme officielle [W3C](https://w3c.github.io/webdriver/).

D'autres protocoles existent, mais ne seront pas couverts en détail ici. Toutes les explications supposeront un backend qui implémente le protocole WebDriver wire.

Un autre protocole notable est le [protocole Chrome DevTools](https://chromedevtools.github.io/devtools-protocol/) utilisé par [Puppeteer](https://github.com/GoogleChrome/puppeteer). Puppeteer n'utilise pas le serveur Selenium, et est livré avec une version récente de [Chromium](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/) destinée à un usage local. Si vous souhaitez exécuter Puppeteer dans Docker, vous pouvez soit utiliser l'[image CodeceptJS](https://codecept.io/docker/) (qui inclut Puppeteer et Nightmare) ou suivre le guide officiel pour créer une [image personnalisée](https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md#running-puppeteer-in-docker) qui peut le supporter.

#### WebDrivers de navigateur

Ce sont des implémentations spécifiques aux navigateurs du protocole WebDriver wire, par exemple [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home) pour Chrome ou [GeckoDriver](https://github.com/mozilla/geckodriver) pour Firefox. Chacun agit comme un serveur [autonome](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol#server) pour recevoir les requêtes du [client](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol#client) où l'API WebDriver est utilisée (généralement où les tests sont effectués). Afin de communiquer avec le navigateur prévu, la bonne implémentation WebDriver **doit** être installée.

#### Serveur Selenium

Si les tests sont exécutés sur la même machine où ils sont définis, alors l'implémentation de l'API WebDriver côté client utilisée (décrite ci-dessous) peut communiquer directement avec le WebDriver du navigateur et un [serveur Selenium n'est pas requis](https://www.seleniumhq.org/docs/03_webdriver.jsp).

Cependant, si les tests doivent être exécutés sur une machine différente, que ce soit en CI, dans une configuration [Selenium Grid](https://www.guru99.com/introduction-to-selenium-grid.html) sur plusieurs machines ou machines virtuelles (VM), sur une plateforme de test à distance telle que [BrowserStack](https://www.browserstack.com/start#os=Windows&os_version=7&browser=IE&browser_version=11.0&zoom_to_fit=true&full_screen=true&resolution=responsive-mode&url=https%3A%2F%2Fwww.skyscanner.net%2Ftransport%2Fflights%2Fedi%2Fde%3Fmigrate%3Dtrue&speed=1) ou [SauceLabs](https://saucelabs.com/), ou dans Docker, alors un serveur Selenium est utilisé. Il agit comme un proxy pour transmettre les requêtes de l'API WebDriver côté client au bon WebDriver du navigateur, et renvoie la réponse du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/AC97-bPidMqMbZ51NLXSPf3gwjBgGxw5b4Oi)
_Comme nous le verrons plus tard, 'machine' peut également être remplacé par 'conteneur'_

#### Implémentation côté client de WebDriver

Une variété d'outils implémentent le protocole WebDriver wire côté client. Ici, le protocole peut être vu comme une API pour envoyer des requêtes au navigateur via les couches décrites ci-dessus. De nombreux outils utilisant le protocole sont des frameworks complets, tels que [WebDriverIO](http://webdriver.io/guide/getstarted/modes.html), qui incluent leurs propres exécuteurs de tests.

D'autres implémentations incluent : le [WebDriver Selenium original](https://www.swtestacademy.com/selenium-testing-selenium-history/), Protractor, Appium, et plus encore.

Les bibliothèques de chacun visent à atteindre les mêmes résultats, mais avec des focales et des implémentations d'API légèrement différentes. Cela peut être aussi basique que `browser.get(url)` de [Protractor](http://www.protractortest.org/#/tutorial) versus `browser.url(url)` de [WebDriverIO](http://webdriver.io/api/protocol/url.html).

#### Une API pour les gouverner toutes

Comme décrit au début de cette section, c'est là que CodeceptJS entre en jeu. Il fait référence à d'autres implémentations du protocole WebDriver côté client (ou autres) en tant que "[helpers](https://codecept.io/helpers/WebDriverIO/)", et vous permet de spécifier le helper que vous préférez tout en utilisant un langage d'API. CodeceptJS ne se soucie pas du protocole utilisé par le helper choisi.

WebDriverIO, Puppeteer, Protractor, Nightmare et Appium sont tous des helpers actuels disponibles.

Dans CodeceptJS, la commande précédente serait `I.amOnPage(url)` quel que soit le helper choisi. Cela signifie que si vous souhaitiez changer votre backend pour l'un des autres helpers supportés, vos tests n'auraient pas besoin d'être réécrits. Il est possible de [surcharger ou d'ajouter](https://codecept.io/helpers/) les méthodes d'API par défaut via des classes personnalisées si vous le souhaitez.

### Création d'un projet de test

Avec autant de couches, cela commence à sembler complexe, mais entre le script d'initialisation de CodeceptJS et les images Docker, nous pouvons rapidement avoir un exemple fonctionnel.

#### Ce que nous allons produire

![Image](https://cdn-media-1.freecodecamp.org/images/mb81mFfkSipoaHtimDmOLqloRRpCOAlev4RS)
_Deux conteneurs seront utilisés pour l'instant, bien que cela puisse être étendu_

Nous allons écrire un test simple dans CodeceptJS, en spécifiant un helper backend WebDriverIO, qui communiquera avec un navigateur distant dans le conteneur Docker standalone-firefox. Nous utiliserons l'application Express "hello world", mais celle-ci pourrait être remplacée par n'importe quelle application que vous souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/2kWArT3EpzQgqymSONorN81cpb3rcF7WPd2L)
_Bientôt, seulement deux commandes seront nécessaires pour exécuter l'application Dockerisée et toutes les suites de test_

Une fois que nous avons tout configuré, nous pourrons exécuter seulement deux commandes pour exécuter les tests :

* `docker-compose up --build`
* `docker exec -it app npm run test:e2e`

En exécutant dans deux fenêtres de terminal côte à côte, nous pouvons voir les conteneurs en cours d'exécution et le test s'exécuter en temps réel.

#### _Prérequis_

* [Docker](https://store.docker.com/search?type=edition&offering=community), pour la machine sur laquelle vous développez.
* Vous pourriez également installer [Node.js, & npm](https://nodesource.com/blog/installing-nodejs-tutorial-mac-os-x/) pour le développement et le débogage local, mais ceux-ci peuvent également être entièrement exécutés dans Docker.

#### Structure des fichiers

Nous allons produire la structure de fichiers ci-dessous. Vous pouvez voir un [exemple fonctionnel sur Github](https://github.com/dominicfraser/CodeceptJSDockerExamples/tree/master/seleniumStandaloneFirefox).

```
|-- .gitignore 
|-- output/
|-- Dockerfile
|-- app.js
|-- docker-compose.yml
|-- package.json
|-- package-lock.json
|-- e2eTests/
    |-- common_test.js
    |-- docker.conf.js
```

#### Dépendances

Tout d'abord, nous allons créer notre [package.json](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/) avec Express comme dépendance et CodeceptJS et WebDriverIO comme dépendances de développement.

```js
{
  "name": "example-standalone-firefox",
  "version": "1.0.0",
  "description": "Exemple de Dockerisation des tests E2E",
  "scripts": {
    "start": "node app.js",
    "test:e2e": "codeceptjs run --steps --verbose --config=./e2eTests/docker.conf.js"
  },
  "dependencies": {
    "express": "^4.16.3"
  },
  "devDependencies": {
    "codeceptjs": "^1.2.0",
    "webdriverio": "^4.12.0"
  }
}
```

Nous avons également inclus deux scripts, un pour exécuter l'application Express que nous allons ajouter (`npm run start`), et un pour exécuter notre test CodeceptJS (`npm run test:e2e`).

```
codeceptjs run --steps --verbose --config=./e2eTests/docker.conf.js
```

`--steps` est idéal pour afficher la sortie dans le terminal pendant que les tests sont en cours d'exécution, tandis que `--verbose` étend le niveau de détail encore plus loin. `--verbose` n'est probablement pas nécessaire en standard, mais est bon pour voir comment l'exemple fonctionne. `--config` nous montre le chemin vers le fichier de configuration du backend, dans ce cas, conservé dans un répertoire `e2eTests` séparé.

#### Notre application

Ensuite, nous avons besoin d'une application à tester. Pour cela, nous allons exécuter l'application Express "[hello world](https://expressjs.com/en/starter/hello-world.html)" à partir de `app.js`.

```
const express = require('express');

const app = express();

app.get('/', (req, res) => res.send('Hello World!'));

const server = app.listen(3000, () => {
    const port = server.address().port
    console.log(`Example app listening on port ${port}`)
 })
```

Vous pouvez voir cela en utilisant `npm run start` puis en allant sur `localhost:3000` dans votre navigateur.

#### Configuration des tests

CodeceptJS nécessite deux fichiers, un fichier de configuration et un fichier de test. Le fichier de test est extrêmement simple : il teste que l'application peut être accessible, sauvegarde une capture d'écran et vérifie que le texte "Hello" peut être vu sur la page.

```
Feature('Test de base');

Scenario('naviguer vers la page d'accueil', I => {
  I.amOnPage('http://app:3000');
  I.saveScreenshot('frontpageScreenshot.png');
  I.see('Hello');
});
```

La première indication que nous allons utiliser plusieurs conteneurs Docker est montrée ici dans l'utilisation de `app:3000` plutôt que `localhost:3000`. `localhost` ne peut être compris que depuis un seul conteneur. Si une commande est exécutée depuis un autre conteneur (dans ce cas par Firefox dans notre deuxième conteneur Selenium), alors elle a besoin d'une référence plus définitive. Nous pourrions utiliser l'adresse IP du premier conteneur directement, mais utiliser le nom du conteneur est beaucoup plus facile à lire.

Dans ce cas, `app` sera le nom du conteneur qui exécute l'application, donc nous pouvons utiliser `app:3000`. Ne vous inquiétez pas si vous ne suivez pas cela pour l'instant, voir comment notre `docker-compose.yml` est structuré aidera.

Nous avons également besoin d'un fichier de [configuration](https://codecept.io/configuration/) principal. Celui-ci peut être écrit en JSON ou JS, mais ici nous utilisons JS. Regardons cela :

```
exports.config = {
  tests: './*_test.js',    // comment savoir quels fichiers sont des fichiers de test
  output: './output',      // où sauvegarder les captures d'écran
  helpers: {
   WebDriverIO: {               // quel helper backend utiliser
     url: 'http://app:3000',    // une URL de base pour démarrer
     host: 'firefox-container', // identifier où selenium s'exécute
     browser: 'firefox',        // une série d'options de configuration
     smartWait: 5000,              
     waitForTimeout: 10000,
     desiredCapabilities: {        // pour une application de démonstration, nous ne voulons pas
         acceptInsecureCerts: true,   nous soucier des certificats SSL
     }
   },
  },
  name: 'codeceptjs-docker',
};
```

#### Configuration de Docker

En nous référant au diagramme ci-dessus dans la section "Ce que nous allons produire", nous pouvons voir que nous allons utiliser deux conteneurs Docker. Ils doivent être conscients l'un de l'autre et pouvoir communiquer. L'un contiendra notre application et nos tests, et l'autre un serveur Selenium, GeckoDriver et Firefox, afin que nous n'ayons pas besoin d'installer Firefox sur notre machine locale.

[Docker Compose](https://docs.docker.com/compose/) est un outil pour "définir et exécuter des applications Docker multi-conteneurs". Il démarre les conteneurs Docker avec la [commande](https://docs.docker.com/compose/reference/overview/) `docker-compose up`, et les arrête avec `docker-compose down`. Si un Dockerfile défini par l'utilisateur est utilisé, `--build` est utilisé pour le construire, soit la première fois que `docker-compose up` est exécuté, soit si des modifications ont été apportées au Dockerfile ou aux étapes exécutées dans celui-ci. `docker-compose.yml` est le fichier qui définit ce que la commande `up` fera.

Notre prochaine étape est de créer ce `docker-compose.yml`. Il dépend fortement de l'indentation.

```
version: "2"        // quelle version de la syntaxe compose vous utilisez
services:
  app:
    container_name: app  // explicite afin que nous puissions utiliser ceci pour app:3000
    build: .             // un Dockerfile auto-défini, voir ci-dessous
    ports:               // expose le port 3000 (où express s'exécute)
      - "3000:3000"         aux autres conteneurs, et à notre navigateur local       
    depends_on:             
      - firefox-container
    volumes:             // mappages afin que les modifications de ceux-ci puissent être vues
      - ./e2eTests:/e2eTests
      - ./package.json:/package.json
      - ./package-lock.json:/package-lock.json
      - ./.gitignore:/.gitignore
      - ./app.js:/app.js

  firefox-container:      // nous allons voir cela ci-dessous
    container_name: firefox-container
    image: selenium/standalone-firefox:3.12.0-americium
    volumes:
      - /dev/shm:/dev/shm
    ports:
      - "4444:4444"
```

Pour notre serveur Selenium, nos drivers et notre navigateur, nous utilisons une image pré-définie disponible sur le [Docker Hub](https://hub.docker.com/) public appelée [selenium/standalone-firefox](https://hub.docker.com/r/selenium/standalone-firefox/). Nous spécifions la version que nous voulons, 3.12.0-americium. Si nous ne spécifions pas cela, la dernière image serait utilisée par défaut (ce qui n'est pas une mauvaise chose). Comme [conseillé](https://github.com/SeleniumHQ/docker-selenium#running-the-images), nous la configurons pour partager la mémoire de l'hôte afin d'éviter que le navigateur exécuté ne plante, et exposons le port 4444, le port Selenium par défaut. Nous mappons également cela au port 4444 sur notre machine locale, ce qui nous permet de visiter `localhost:4444/wd/hub/static/resource/hub.html` dans notre navigateur.

Pour notre conteneur `app`, nous n'utilisons pas seulement une image construite par quelqu'un d'autre, mais nous écrivons un Dockerfile pour spécifier comment notre application est construite. De la même manière que le conteneur `selenium-firefox`, nous exposons un port, 3000 dans ce cas, car c'est là que Express s'exécute par défaut. En le mappant en utilisant `3000:3000`, nous sommes en mesure de visiter `localhost:3000` pendant que l'application est exécutée dans Docker pour la voir dans notre navigateur local.

Notre Dockerfile utilise l'image publique `node:carbon` comme base, définit le répertoire de travail, copie certains fichiers de notre machine locale vers le conteneur, exécute `npm install` afin que le conteneur ait toutes les dépendances nécessaires, puis exécute la commande `npm start` que nous avons spécifiée.

```
FROM node:carbon 
WORKDIR ./ 
COPY ./package.json ./package-lock.json ./app.js ./ 
RUN npm install 
CMD [ "npm", "start" ]
```

Cela signifie que lorsque `docker-compose up --build` est exécuté, il suivra ces étapes, ce qui entraînera notre application prête et en cours d'exécution sur le port 3000.

**Note** : Le drapeau `--build` n'est nécessaire que la première fois que `docker-compose up` est exécuté, ou si des modifications ont été apportées à notre Dockerfile ou aux étapes exécutées dans celui-ci. Par exemple, si nous ajoutions une autre dépendance dans notre `package.json`, Docker ne le saurait pas si nous ne reconstruisions pas notre image, car `npm install` est exécuté dans le Dockerfile.

#### Exécution des tests

Nous avons maintenant une application simple, des tests écrits pour celle-ci, et une configuration Docker Compose qui exécutera à la fois notre application, un serveur Selenium et Firefox.

Nous pouvons démarrer tout cela en utilisant `docker-compose up --build`.

Pour exécuter des commandes _dans_ un conteneur Docker en cours d'exécution, `docker exec` peut être utilisé à partir d'une autre fenêtre de terminal. Le format est :

`docker exex <flags> <container_name&g`t; <command>

La commande que nous allons utiliser est :

`docker exec [-it](https://docs.docker.com/engine/reference/commandline/exec/#options) app npm run test:e2e`

Nous pouvons maintenant voir notre test en cours d'exécution, et voir chaque étape au fur et à mesure qu'elle est effectuée ! À partir de là, nous pouvons étendre ce que fait notre test, ajouter des tests supplémentaires (en terminant les noms de fichiers par `_test.js`), et utiliser les mêmes deux commandes pour les exécuter. Aucune autre configuration n'est nécessaire.

Vous avez maintenant une configuration de test E2E facilement extensible qui peut être utilisée pour fonctionner de la même manière, quelle que soit la machine sur laquelle elle est exécutée. Elle a été écrite avec des commandes API qui peuvent être facilement comprises à la fois par les développeurs et les non-développeurs. Il ne reste plus qu'à décider du comportement que votre application doit être capable de faire, et à le tester !

### Mots de la fin

SeleniumHQ produit également des images Docker pour les [tests Chrome](https://github.com/SeleniumHQ/docker-selenium#standalone-chrome-and-firefox), et des images pour utiliser Selenium Grid pour exécuter plusieurs instances de Chrome et Firefox en même temps.

CodeceptJS dispose également d'[instructions pour exécuter CodeceptJS dans Docker](https://codecept.io/docker/), afin qu'il n'ait pas besoin d'être spécifié comme une dépendance dans votre application.

Une description plus technique, mais toujours de niveau débutant, de comment Docker fonctionne peut être vue dans la première section de l'article que j'ai écrit intitulé [_Un guide du débutant pour le service de conteneurs élastiques d'Amazon_](https://medium.freecodecamp.org/amazon-ecs-terms-and-architecture-807d8c4960fd)_._

Merci d'avoir lu ?

_Mise à jour :_   
J'ai récemment écrit [Personnalisation des tests e2e de CodeceptJS](https://codeburst.io/customising-codeceptjs-e2e-tests-1a2bf5f32f51) pour ceux qui cherchent les prochaines étapes dans le test d'applications complexes.

#### Ressources

* [Github](https://github.com/dominicfraser/CodeceptJSDockerExamples) des exemples Docker de CodeceptJS
* [Guide de démarrage rapide de CodeceptJS](https://codecept.io/quickstart/)
* [Architecture de Selenium WebDriver](https://www.youtube.com/watch?v=cDwNfAEo0lA)
* [Flux de Selenium WebDriver](https://seleniumjava.com/2015/09/13/how-does-selenium-webdriver-work/)