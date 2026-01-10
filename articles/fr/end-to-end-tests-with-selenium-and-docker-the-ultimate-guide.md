---
title: Le guide ultime des tests de bout en bout avec Selenium et Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-16T22:46:40.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-tests-with-selenium-and-docker-the-ultimate-guide
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/end-to-end-testing-selenium-docker.jpg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: selenium
  slug: selenium
- name: Software Testing
  slug: software-testing
seo_title: Le guide ultime des tests de bout en bout avec Selenium et Docker
seo_desc: 'By Jean-Paul Delimat

  Automated end to end testing is the most effective way to test your app. It also
  requires the least effort to get the benefit of tests if you currently have no tests
  at all. And you don’t need a ton of infrastructure or cloud ser...'
---

Par Jean-Paul Delimat

Les tests automatisés de bout en bout sont le moyen le plus efficace de tester votre application. Ils nécessitent également le moins d'efforts pour bénéficier des tests si vous n'avez actuellement aucun test. Et vous n'avez pas besoin d'une tonne d'infrastructure ou de serveurs cloud pour y parvenir. Dans ce guide, nous verrons comment surmonter facilement les deux principaux obstacles des tests de bout en bout.

Le premier obstacle est Selenium. L'API que vous utilisez pour écrire des tests est peu intuitive et peu pratique. Mais elle n'est pas si difficile à utiliser, et avec quelques fonctions pratiques, elle peut devenir un jeu d'enfant pour écrire des tests Selenium. L'effort est bien récompensé car vous pouvez tester automatiquement les flux de vos utilisateurs finaux de bout en bout.

Le second obstacle est de rassembler les composants dans un environnement isolé. Nous voulons le frontend, le backend, la base de données et tout ce que votre application utilise. Nous utiliserons Docker Compose pour rassembler les choses et automatiser les tests. C'est facile même si vos composants sont dans différents dépôts Git.

## Écrire des tests de bout en bout avec Selenium

Même si vous êtes une entreprise uniquement API, vous avez un frontend, et un frontend d'administration ou de back office. Donc, les tests de bout en bout finissent par parler à une application frontend.

L'outil standard de l'industrie est Selenium. Selenium fournit une API pour communiquer avec le navigateur web et interagir avec le DOM. Vous pouvez vérifier quels éléments sont affichés, remplir des champs et cliquer. Tout ce qu'un utilisateur réel ferait avec votre application, vous pouvez l'automatiser.

Selenium utilise quelque chose appelé l'API WebDriver. Elle n'est pas très pratique à utiliser au premier abord. Mais la courbe d'apprentissage n'est pas raide. Créer quelques fonctions de commodité vous rendra productif en un rien de temps. Je ne vais pas entrer dans les détails de l'API WebDriver ici. Vous pouvez consulter [cet excellent article](https://marmelab.com/blog/2016/04/19/e2e-testing-with-node-and-es6.html) pour approfondir.

Il existe également des bibliothèques pour faciliter votre vie. [Nightwatch](https://nightwatchjs.org/) est le plus populaire.

Si vous avez une application Angular, [Protractor](https://www.protractortest.org/) est votre meilleur ami. Il s'intègre avec la boucle d'événements Angular et vous permet d'utiliser des sélecteurs basés sur votre modèle. C'est de l'or.

Écrire un test pour la fonctionnalité la plus critique de votre utilisateur ou de votre application ne devrait prendre que quelques heures, alors allez-y. Il s'exécutera automatiquement par la suite. Voyons comment.

## Exécuter vos tests dans Docker

Nous devons exécuter nos tests dans un environnement isolé pour que le résultat soit prévisible. Et ainsi nous pouvons activer facilement l'[Intégration Continue](https://fire.ci/blog/how-to-get-started-with-continuous-integration/). Nous utiliserons Docker Compose.

Selenium fournit des images Docker prêtes à l'emploi pour tester avec un ou plusieurs navigateurs. Les images lancent un serveur Selenium et un navigateur en dessous. Il peut fonctionner avec différents navigateurs.

Commençons par un navigateur pour l'instant : headless-chrome. Vous pouvez voir le fichier _docker-compose.yml_ ci-dessous (les commandes proviennent d'un exemple Angular).

Note : Si vous n'avez jamais utilisé Docker, vous pouvez facilement l'installer sur votre ordinateur. Docker a la fâcheuse tendance de vous forcer à créer un compte juste pour télécharger l'outil. Mais vous n'avez pas à le faire. Allez aux notes de version ([lien pour Windows](https://docs.docker.com/docker-for-windows/release-notes/) et [lien pour Mac](https://docs.docker.com/docker-for-mac/release-notes/)) et téléchargez non pas la dernière version mais celle juste avant. C'est un lien de téléchargement direct.

```
version: '3.1'

services:
 app-serve:
   build: .
   image: myapp
   command: npm run serve:production
   expose:
    - 4200

 app-e2e-tests:
   image: myapp
   command: dockerize -wait tcp://app-serve:4200 
             -wait tcp://selenium-chrome-standalone:4444 
             -timeout 10s -wait-retry-interval 1s bash -c "npm run e2e"
   depends_on:
     - app-serve
     - selenium-chrome-standalone

 selenium-chrome-standalone:
   image: selenium/standalone-chrome
   expose:
    - 44444
```

Le fichier ci-dessus indique à Docker de lancer un environnement avec 3 conteneurs :

* Notre application à tester : le conteneur utilise l'image myapp que nous allons construire juste en dessous
* Un conteneur exécutant les tests : le conteneur utilise la même image myapp. Il utilise [dockerize](https://github.com/jwilder/dockerize) pour attendre que les serveurs soient opérationnels avant d'exécuter les tests
* Le serveur Selenium : le conteneur utilise l'image officielle Selenium. Rien à faire ici. Nous pourrions exécuter les tests à partir du même conteneur que l'application. Le fait de le séparer rend les choses plus claires. Cela vous permet également de séparer les sorties des 2 conteneurs dans les journaux de résultats.

Les conteneurs vivront dans un réseau virtuel privé et se verront les uns les autres comme http://the-container-name (plus [ici](https://docs.docker.com/compose/networking/) sur la mise en réseau dans Docker).

Nous avons besoin d'un _Dockerfile_ pour construire l'image _myapp_ utilisée pour les conteneurs. Il doit transformer votre code frontend en un bundle aussi proche que possible de la production. Exécuter des tests unitaires et du linting est une bonne idée à ce stade. Après tout, il n'est pas nécessaire d'exécuter des tests de bout en bout si les bases ne fonctionnent pas.

Dans le _Dockerfile_ ci-dessous, nous utilisons une image node comme base, installons dockerize et bundlons l'application. Il est important de construire pour la production. Vous ne voulez pas tester une build de développement qui est pré-optimisée. Beaucoup de choses peuvent mal tourner là.

```
FROM node:12.13.0 AS base

ENV DOCKERIZE_VERSION v0.6.0

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
   && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
   && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p ~/app
WORKDIR ~/app

COPY package.json .
COPY package-lock.json .

FROM base AS dependencies

RUN npm install

FROM dependencies AS runtime

COPY . .
RUN npm run lint
RUN npm run test:ci
RUN npm run build --production
```

Maintenant que nous avons toutes les pièces ensemble, lançons les tests en utilisant cette commande :

```
docker-compose up --build --abort-on-container-exit
```

C'est un peu long, alors scriptz-le dans votre projet d'une manière ou d'une autre. Il construira l'image myapp basée sur le _Dockerfile_ fourni puis démarrera tous les conteneurs. Dockerize s'assure que votre application et Selenium sont opérationnels avant d'exécuter les tests.

L'option _--abort-on-container-exit_ tuera l'environnement lorsqu'un conteneur sortira. Puisque seul notre conteneur de test est censé sortir (les autres sont des serveurs), c'est ce que nous voulons.

La commande docker-compose aura le même code de sortie que le conteneur sortant. Cela signifie que vous pouvez facilement détecter à partir de la ligne de commande si les tests ont réussi ou non.

Vous êtes maintenant prêt à exécuter des tests de bout en bout localement et sur n'importe quel serveur supportant Docker. C'est plutôt bien !

Les tests s'exécutent avec un seul navigateur pour l'instant. Ajoutons-en d'autres.

## Tester sur différents navigateurs

L'image autonome Selenium lance un serveur Selenium avec le navigateur que vous souhaitez. Pour exécuter les tests sur différents navigateurs, vous devez mettre à jour la configuration de vos tests et utiliser l'image Docker selenium/hub.

L'image crée un hub entre votre application et les images Selenium autonomes. Remplacez la section du conteneur selenium dans votre docker-compose.yml comme suit :

```
  selenium-hub:
    image: selenium/hub
    container_name: selenium-hub
    expose:
      - 4444
  chrome:
    image: selenium/node-chrome
    volumes:
      - /dev/shm:/dev/shm
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
      - HUB_PORT=4444
  firefox:
    image: selenium/node-firefox
    volumes:
      - /dev/shm:/dev/shm
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
      - HUB_PORT=4444
```

Nous avons maintenant 3 conteneurs : Chrome, Firefox et le hub Selenium.

Toutes les images Docker fournies par Selenium sont [dans ce dépôt](https://github.com/SeleniumHQ/docker-selenium).

Attention ! Il y a un effet de timing délicat à considérer. Nous utilisons dockerize pour que notre conteneur de test attende que le hub Selenium soit opérationnel. Ce n'est pas suffisant car nous devons attendre que les images autonomes soient prêtes, en fait, qu'elles s'enregistrent auprès du hub.

Nous pouvons faire cela en attendant que les images autonomes exposent un port, mais ce n'est pas une garantie. Il est plus facile d'attendre quelques secondes avant de démarrer les tests. Mettez à jour votre script de test pour attendre 5 secondes avant que les tests ne commencent (vous pouvez ajouter une commande sleep après l'appel dockerize).

Maintenant, vous pouvez être sûr que vos tests ne démarreront pas tant que tous les navigateurs ne seront pas prêts. Attendre n'est pas idéal, mais quelques secondes en valent la peine. Il n'y a rien de plus ennuyeux que des tests qui échouent à cause d'automatisations instables.

Bien. Nous avons maintenant couvert la partie frontend. Ajoutons le backend.

## Ajouter le backend en tant que conteneurs ou modules git

Ce qui précède peut sembler excessif pour tester uniquement la partie frontend de votre application. Mais nous visons beaucoup plus. Nous voulons tester l'ensemble du système.

Ajoutons une base de données et un backend à notre environnement Docker Compose.

Si vous êtes un développeur frontend, vous pourriez penser "nous sommes l'équipe frontend, nous ne nous soucions pas de tester le backend." En êtes-vous sûr ?

> Le frontend est toujours la dernière partie à intégrer toutes les autres pièces. Cela signifie des périodes de rush. Des périodes de rush qui n'existeraient plus si vous pouviez tester le frontend avec le backend en continu et détecter les erreurs plus tôt.

La technique que je décris ici est très facile à appliquer même si votre backend est dans un dépôt différent.

Voici à quoi ressemble le fichier _docker-compose.yml_ :

```
version: '3.1'

services:
 db:
   image: postgres
   environment:
     POSTGRES_USER: john
     POSTGRES_PASSWORD: mysecretpassword
   expose:
     - 5432
 backend:
   context: ./backend
   dockerfile: ./backend/Dockerfile
   image:mybackend
   command: dockerize
       -wait tcp://db:5432 -timeout 10s
       bash -c "./seed_db.sh && ./start_server.sh"
   environment:
     APP_DB_HOST: db
     APP_DB_USER: john
     APP_DB_PASSWORD: mysecretpassword
   expose:
     - 8000
   depends_on:
     - db
 app-serve:
   build: .
   image: myapp
   command: npm run serve:sw
   expose:
    - 4200
 app-e2e-tests:
   image: myapp
   command: dockerize -wait tcp://app-serve:4200 
        -wait tcp://backend:8000 
        -wait tcp://selenium-chrome-standalone:4444 -timeout 10s 
        -wait-retry-interval 1s bash -c "npm run e2e:docker"
   depends_on:
     - app-serve
     - selenium-chrome-standalone
 selenium-chrome-standalone:
   image: selenium/standalone-chrome
   expose:
    - 44444
```

Dans cet exemple, nous avons ajouté une base de données postgres et un conteneur pour exécuter le backend. Dockerize synchronise les commandes des conteneurs.

Si votre système a plus d'un composant backend, ajoutez autant de conteneurs que nécessaire. Vous devez connecter correctement les dépendances des conteneurs. Cela signifie des noms d'hôtes appropriés en tant que variables d'environnement sur vos composants. Et l'ordre de démarrage si certains composants dépendent d'autres.

Les tests Selenium que vous avez écrits ne devraient pas nécessiter de modifications. Vous devrez peut-être mettre des données de test dans la base de données. Pour garder cette étape dans la zone de test, nous avons ajouté le script de seeding avant le script de démarrage du backend. De cette façon, nous sommes sûrs que les choses se passent dans le bon ordre :

* La base de données démarre et est prête à accepter les connexions
* Un script remplit les données de la base de données
* Le backend et le frontend démarrent, donc les tests peuvent commencer

### Monorepository

Si vous regardez le conteneur backend, vous pouvez voir qu'il y a un piège. Il utilise une image appelée _mybackend_ construite à partir d'un fichier situé à _backend/Dockerfile_. Cela implique que votre backend est dans le même dépôt git dans un dossier appelé _backend_. Le nom n'est qu'un exemple bien sûr.

Si votre backend et votre frontend sont dans le même dépôt, vous êtes bon. Définissez le Dockerfile pour construire votre backend et ajustez la commande de démarrage à ce dont vous avez besoin.

C'est bien, mais généralement le backend n'est pas dans le même dépôt. Ou vous pouvez avoir de nombreux composants backend dans différents dépôts. Que faites-vous alors ?

### Multiple repositories

La solution super propre est d'avoir un processus CI sur chaque dépôt de composant backend.

Si vous n'en avez aucun, vous pouvez consulter le guide [API end to end testing with Docker](https://fire.ci/blog/api-end-to-end-testing-with-docker/) pour commencer. Il utilise les mêmes techniques que cet article afin que vous ayez une configuration cohérente dans l'ensemble de votre projet.

Le processus CI pour chaque composant exécute des tests automatisés. En cas de succès, il pousse une image docker avec le composant vers un registre Docker privé. Le conteneur backend dans notre fichier _docker-compose.yml_ ci-dessus utiliserait cette image.

Cette solution nécessite un registre Docker privé pour stocker vos images. Vous pouvez utiliser [Docker Hub](https://hub.docker.com/) mais il devient alors public. Si vous n'en avez pas déjà un et ne prévoyez pas d'en avoir un, cela ne vaut pas l'effort.

L'autre solution est d'utiliser la fonctionnalité de sous-modules dans git. Votre dépôt backend devient un enfant virtuel de votre dépôt frontend. Vous devez simplement ajouter le fichier _.gitmodules_ comme ceci à votre dépôt frontend :

```
[submodule "backend"]
  path = backend
  url = git@your:backend/repository.git
  branch = develop
```

Exécutez la commande _git submodule update --remote_ qui tirera la branche spécifiée du dépôt backend dans un dossier appelé "backend". Ajoutez autant de sous-modules que nécessaire si vous avez plus d'un composant backend.

C'est tout. Faites en sorte que votre CI exécute la commande de sous-module et, d'un point de vue système de fichiers, c'est comme si vous étiez dans un monorepository.

Si vous ne voulez pas le code backend localement lors du développement du frontend, ne lancez pas la commande. Vous aurez un dossier backend vide.

### Versioning and back end/front end incompatibilities

Les 2 techniques ci-dessus testent le frontend avec la dernière version "CI tests passed" de votre backend. Cela peut entraîner des builds cassés si vos composants ne sont pas compatibles à certains moments.

Si ils sont compatibles plus souvent qu'autrement, restez avec l'approche "always test with the latest versions". Vous corrigez les incompatibilités occasionnelles à la volée.

Cela ne fonctionnera pas, cependant, si les incompatibilités sont la norme. Dans ce cas, vous devez contrôler manuellement les mises à jour de version. C'est très facile à faire.

Vous pouvez verrouiller la version d'un composant dans le fichier _docker-compose.yml_ ou dans le fichier _.gitmodules_. Lors de l'envoi vers le registre Docker, vous étiquetteriez l'image du composant avec le numéro de commit du code correspondant. La section pertinente du fichier docker-compose.yml devient :

```
backend:
  image: backendapp:34028fc
```

De même, le fichier _.gitmodules_ ne ciblerait pas une tête de branche mais un commit donné :

```
[submodule "backend"]
  path = backend
  url = git@your:backend/repository.git
  branch = 34028fc
```

Bonus : les mises à jour de version sont versionnées avec votre code. Vous pouvez suivre quelle version a été utilisée pour chaque build. Cela est utile lors de la correction de builds échoués ou de la tentative de reproduction d'anciens bugs.

Nous pourrions pousser l'approche au niveau suivant. Vous pourriez avoir un dépôt dédié qui connecterait tous vos composants en tant que modules git. Les mises à jour de version pourraient être une forme de livraison et de transfert à l'équipe de test/QA.

En théorie, il est préférable de garder les dernières versions des composants fonctionnant ensemble plus souvent qu'autrement. Et de supprimer le besoin de versioning manuel. Si ce n'est pas le cas, ce n'est pas grave. Ignorez les puristes qui vous diront que vous ne suivez pas les meilleures pratiques, etc.

> Si vous commencez tout juste, ne visez pas les étoiles au début. Choisissez ce qui fonctionne le mieux pour vous afin de profiter des avantages des tests automatisés dès maintenant. Ensuite, continuez à améliorer votre processus en cours de route.

## Bonus sur l'écriture de tests Selenium maintenables

Revenons à Selenium et trois conseils importants pour vous aider à écrire de bons tests UI.

Premièrement, évitez les sélecteurs CSS si possible. Selenium fonctionne sur le DOM et peut identifier les éléments par ID, CSS ou XPath. Utilisez les ID autant que possible, même si vous devez les ajouter à votre code d'application uniquement à cette fin. Les sélecteurs CSS et XPath sont instables. Dès que la structure de votre application change, ils seront cassés.

Deuxièmement, utilisez l'approche Page Objects. Il s'agit d'encapsuler votre application afin que les sélecteurs ne soient pas utilisés directement dans les tests. Si votre page HTML/CSS change, vos tests devront être réécrits pour utiliser de nouveaux sélecteurs. Les Page Objects abstraient les sélecteurs et les transforment en actions utilisateur. Voici un excellent article sur [comment utiliser correctement les Page Objects](https://johnfergusonsmart.com/page-objects-that-suck-less-tips-for-writing-more-maintainable-page-objects/).

Troisièmement, ne construisez pas de longs parcours utilisateur dans vos tests. Si vos tests échouent à la 50ème action, il sera difficile de reproduire et de corriger. Créez des suites de tests qui jouent une partie des scénarios à partir de la page de connexion. De cette façon, vous êtes toujours à quelques clics du bug que vos tests attraperont.

Également, ne risquez pas d'écrire des tests qui dépendent de l'état des actions précédentes. Le couplage des suites de tests est quelque chose que vous voulez éviter.

Prenons un exemple pratique. Supposons que vous testez une application SaaS pour les écoles. Les cas d'utilisation pourraient être :

* Créer une classe
* Enregistrer les données des enfants et des parents
* Configurer le plan hebdomadaire pour la classe
* Vérifier les absences
* Saisir les notes

En cours de route, vous aurez le processus de connexion et quelques vérifications de navigation.

Vous pourriez écrire un test qui passe par toute la chaîne comme décrit ci-dessus. Et ce serait pratique car pour déclarer des enfants, vous avez besoin qu'une classe existe. Pour vérifier les absences, vous avez besoin d'un plan hebdomadaire en place. Et vous avez besoin d'enfants pour saisir les notes. C'est une victoire rapide de construire une suite de tests qui fait toutes ces choses au début.

Si vous n'avez rien pour le moment et que vous voulez atteindre une bonne couverture de test rapidement : allez-y ! Fait est mieux que parfait si cela vous permet de détecter des erreurs dans votre application maintenant.

La solution plus propre serait d'utiliser un scénario de base pour démarrer des suites de tests plus petites. Dans l'exemple ci-dessus, le scénario de base devrait être de créer une classe et d'enregistrer les données des enfants.

Créez une suite de tests qui fait exactement cela : créer une classe et enregistrer les données des enfants et des parents. Exécutez-la toujours en premier. Si cela cesse de fonctionner, alors vous n'avez pas besoin d'aller plus loin. Cette version du code n'atteindra jamais les utilisateurs finaux de toute façon.

Ensuite, créez une fonction qui encapsule le scénario de base. Ce sera du code dupliqué dans une certaine mesure avec la suite de tests précédente. Mais cela vous permettra d'avoir une fonction d'une ligne à utiliser comme crochet de configuration pour toutes les autres suites de tests. C'est le meilleur des deux mondes : des scénarios de test commençant à partir d'un état frais dans l'application avec un effort minimal.

## Conclusion

J'espère que cet article vous a donné un bon aperçu de la manière dont vous pouvez rapidement configurer des tests de bout en bout pour un système complexe. Plusieurs composants dans plusieurs dépôts ne devraient pas être un obstacle. Docker Compose facilite la mise en place des choses.

Les tests de bout en bout sont le meilleur moyen d'éviter les périodes de rush. Dans les systèmes complexes, la livraison tardive de certains composants met une charge sur les autres équipes. Les intégrations sont faites à la hâte. La qualité du code baisse. C'est un cercle vicieux. Tester souvent et détecter les erreurs inter-composants tôt est la solution.

Les tests Selenium peuvent être faits rapidement et de manière approximative pour avancer vite. C'est parfaitement acceptable. Automatisez les choses. Ensuite, améliorez. Souvenez-vous :

> Fait est mieux que parfait n'importe quel jour de l'année.

Merci d'avoir lu !

_Si vous voulez plus de mes articles comme celui-ci, vous pouvez les trouver sur [The Fire CI Blog](https://fire.ci/blog)._