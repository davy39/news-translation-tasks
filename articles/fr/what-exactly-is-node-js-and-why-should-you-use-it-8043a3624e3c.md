---
title: Qu'est-ce que Node.js exactement et pourquoi devriez-vous l'utiliser ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-02T10:34:12.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-node-js-and-why-should-you-use-it-8043a3624e3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PD8tLMlOrnH814-GUDDKjQ.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: platform
  slug: platform
- name: 'tech '
  slug: tech
seo_title: Qu'est-ce que Node.js exactement et pourquoi devriez-vous l'utiliser ?
seo_desc: 'By Dariya Kursova

  JavaScript as programming language and data format (JSON) has changed web development
  drastically. Integrating Node.js with it to do things on the server as well as in
  browser is a trend lately. These two sentences, we feel, have to...'
---

Par Dariya Kursova

JavaScript, en tant que langage de programmation et format de données (JSON), a radicalement changé le [développement web](https://thinkmobiles.com/full-stack-development/). L'intégration de Node.js pour effectuer des tâches sur le serveur ainsi que dans le navigateur est une tendance récente. Ces deux phrases, nous le pensons, doivent être éclaircies et expliquées pour que chacun puisse les comprendre. Ainsi, dans cet article, nous allons parler **pourquoi** utiliser Node.js, **à quoi** sert Node.js et des **meilleurs exemples** d'utilisation de Node.js.

Bien sûr, cela concerne principalement les programmeurs/développeurs, et certains pourraient trouver le langage pas tout à fait compréhensible. Dans cette optique, nous allons essayer de rendre cela aussi simple que possible et de parler en termes plus humains. Nous voulons simplement expliquer **ce qui rend Node.js génial** et pourquoi il suscite autant d'engouement.

Tout d'abord, les éloges sont bien mérités, car Node a grandement facilité le travail de quiconque construit des applications web. Après des décennies de paradigme de requête/réponse web, avoir une **communication bidirectionnelle en temps réel** est un bonheur. Il s'agit d'une communication entre le serveur et le client. Et cela, à son tour, est un modèle pour répartir les charges de travail entre les fournisseurs de services (serveur) et les demandes de services (clients).

Vous êtes toujours à bord ? Super, voici quelques informations statistiques sur la demande pour Node.js. C'est de loin le langage à la croissance la plus rapide en usage, et il figure dans le Top-10 des compétences de développeurs les plus recherchées. L'utilisation de Node.js est principalement pour le full stack, le front-end et le back-end.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ENOWYhQ_peWrfFRmeHj_Qg.jpeg)

### Qu'est-ce que Node.js ?

Comme nous l'avons précédemment abordé dans [Meilleurs exemples de Node.js](https://thinkmobiles.com/blog/node-js-app-examples/), **Node.js est un environnement d'exécution JavaScript**. Mais qu'est-ce que cela signifie, pourrait-on demander. Par environnement d'exécution, on entend l'infrastructure pour construire et exécuter des applications logicielles. Pour construire des applications en JavaScript, dans ce cas. Voyons quelles sont les versions de la définition de Node.js.

L'entreprise elle-même décrit Node.js comme un "environnement d'exécution JavaScript basé sur le moteur Chrome V8". Wikipedia indique que "Node.js est un environnement open-source et multiplateforme pour exécuter du code". Selon TechTarget, c'est
"une plateforme de développement visant à construire des applications côté serveur". Et PCMag nous dit que Node.js est "une plateforme avec son propre serveur web pour un meilleur contrôle". Cela est certainement suffisant pour saisir l'idée principale.

Un bref résumé serait le suivant :

* Node.js est un framework serveur et est gratuit
* Il fonctionne sur Windows, Linux, Mac OS, etc.
* Node.js utilise JavaScript sur le serveur

Comment fonctionne Node.js ? Prenons une tâche simple comme l'ouverture d'un fichier sur un serveur, la séquence serait :

* Une tâche est envoyée au système de fichiers
* Le système est prêt pour les prochaines requêtes
* Lorsque le fichier est ouvert et lu, le système envoie le contenu au client

En d'autres termes, avec Node.js, vous n'avez pas à attendre et pouvez continuer avec les tâches suivantes. C'est l'une des raisons pour lesquelles il est si efficace. Maintenant, qu'est-ce qu'un fichier Node.js :

* Il contient des tâches et les exécute lors d'événements définis
* Un événement est lorsqu'une personne tente d'accéder au serveur
* Un fichier doit être initié sur le serveur
* Les fichiers ont l'extension '.js'

Et enfin, mais non des moindres, que pouvez-vous faire avec Node.js ?

* Générer du contenu dynamique
* Créer, ouvrir et lire, ou supprimer des fichiers sur le serveur
* Collecter et modifier des données dans la base de données

![Image](https://cdn-media-1.freecodecamp.org/images/1*TXg08jWp-iSjNgkTutdSPw.jpeg)

### Pourquoi utiliser Node.js

Il est maintenant temps de jouer à un quiz sur le pourquoi, qui, quand et pour quoi. Alors, pourquoi utiliser Node.js ? Probablement, son créateur et fondateur **Ryan Dahl** peut éclairer cela. Le principal avantage, dit-il, est que ce langage JavaScript ne bloque pas les I/O — signifiant la méthode de communication d'entrée/sortie. Cependant, la communauté des développeurs a deux avis sur la question. Certains soutiennent que les applications avec de nombreux cycles CPU peuvent planter. D'autres disent que ce n'est pas un gros problème, car le code Node fonctionne en petits processus.

Un autre avantage est la **boucle d'événements à thread unique**, responsable de l'abstraction des I/O des requêtes externes. En termes simples, cela signifie que Node.js initie la boucle d'événements au démarrage, traite l'entrée et commence l'ordre des opérations. Les passionnés de développement intéressés à explorer cela peuvent lire [Node.js event loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/).

Jim Hirschauer de Crafter Software a fait **quelques réalisations sur pourquoi utiliser Node.js**. Nous pensons qu'elles mettent en lumière l'essence et ce pour quoi Node.js est bon :

1. Moteur JavaScript de Google
Traduction : applications web rapides et évolutives en résultat.
2. Pour les applications côté serveur
Cela signifie que Node.js est un modèle de programmation piloté par événements, où le flux est déterminé par certains événements (actions de l'utilisateur, messages, etc.).
3. Plus facile et évolutif
C'est-à-dire, pour créer des [applications comme Uber](https://thinkmobiles.com/how-make-taxi-app/) ou Trello et les déployer sur des serveurs multi-CPU.
4. Par processus et à travers les serveurs
Traduction : Node.js peut évoluer sur une base de processus individuel en répartissant la charge sur des serveurs multi-cœurs.

Tout cela semble un peu difficile, nous le réalisons. Alors voici un résumé des avantages cohérents à utiliser Node.js.

#### 10 principales raisons d'utiliser Node.js

* Bon pour les développeurs débutants, JavaScript est simple à apprendre, framework riche (Angular, Node, Backbone, Ember)
* Il est rapide, grâce aux technologies innovantes de Google et à la boucle d'événements
* Capacité à conserver les données au format JSON natif (notation d'objet) dans votre base de données
* Modules multiples (NPM, Grunt, etc.) et communauté supportive
* Bon pour créer des applications en temps réel, comme les chats et les jeux
* Base de code unique et gratuite
* Bon pour le streaming de données, donc pour les fichiers audio et vidéo, par exemple
* Sponsorisé par la Linux Foundation, ainsi que PayPal, Joylent, Microsoft, Walmart
* Large gamme d'options d'hébergement
* JavaScript est le langage le plus ancien, 99 % des développeurs en connaissent un peu

![Image](https://cdn-media-1.freecodecamp.org/images/1*S9uulM0K7uJFX3SX0hDq6A.jpeg)

Eh bien, cela devrait éclaircir un peu plus le tableau pour vous. Mais attendez, saviez-vous que la NASA utilise également Node.js ?

### Qui travaille avec : Cas d'utilisation de Node.js

Montrant un rythme incroyable (proche de 100 % de croissance d'utilisation chaque année), Node.js est devenu une plateforme universelle pour les applications web. Des entreprises comme PayPal, Walmart utilisent Node pour des applications d'entreprise également. Les tendances qui se construisent au sein de la communauté Node sont les micro-services, les applications en temps réel et l'Internet des Objets (IoT). Mais nous en parlerons plus tard.

Avec près de **4 millions d'utilisateurs** début 2017, Node.js ne manque certainement pas d'entreprises de haut niveau qui travaillent avec. Par exemple, à quoi faisait référence notre précédente mention de la NASA ? Eh bien, c'est la vérité. L'agence, en partenariat avec UTC Aerospace Systems, a conçu un système de bout en bout pour le traitement de données en direct. Il est utilisé dans les combinaisons spatiales des astronautes et a été construit avec Node.js.

Si vous avez lu notre précédent article sur les principales entreprises utilisant Node.js, vous connaissez déjà Netflix, Microsoft, Uber et d'autres. Bien que ce ne soit pas tout. [Capital One](https://www.facebook.com/capitalone), une énorme corporation financière, exécute de nombreux projets avec Node.js en raison de **courts cycles de [développement Node.js](https://thinkmobiles.com/nodejs-development/)**. Les agences de publicité, comme [Fusion Marketing](https://thisisfusion.com/), créent des expériences client interactives. Walmart dans la vente au détail, Uber dans le transport, Google, Twitter, GoDaddy, Skycatch... il faudrait des heures pour tous les couvrir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*45k4PEBkR579hbPMMbEmTg.jpeg)

Il y a aussi une série de conversations sur Node.js pour les entreprises, où chaque épisode est consacré à un cas d'utilisation séparé de Node.js. Comme celui-ci, où Adam Geitgey, directeur de l'ingénierie logicielle chez Groupon, parle de la manière dont la plateforme les a aidés à se développer.

L'un des résultats de l'utilisation de Node.js chez Groupon a été une **réduction de 50 % des temps de chargement des pages**. Pas mal, non ? Parlons un peu plus des cas de succès de Node.js.

### Histoires de succès de Node.js : Groupon, Skycatch & Lowe's

**Groupon** a reconstruit son propre site web avec Node.js, passant de Ruby on Rails. Bien que Ruby était correct, avec le temps, il est devenu plus difficile de maintenir le site web avec chaque nouvelle mise à jour. Node.js a été choisi pour plusieurs raisons : il supportait les projets d'échelle, offrait de meilleures performances et tolérait l'ancien code Ruby. À la fin du processus, l'équipe a même publié quelques bibliothèques JavaScript maison : [Gofer](https://github.com/groupon/gofer) et [Node cached](https://github.com/groupon/node-cached). En résumé, Groupon utilise Node.js de nombreuses manières maintenant :

* pour les services back-end
* pour la couche d'intégration des API
* pour les applications et sites web des clients
* pour environ 70 applications propres à Groupon

**Skycatch** est une entreprise de données travaillant avec les données de drones commerciaux. Et bien que la création de SQL brut soit difficile et longue, Skycatch permet de le faire de manière plus facile et simplifie l'extraction de données depuis les sites web. **Andre Deutmeyer** et l'équipe de 20 développeurs avaient pour tâche d'architecturer et de livrer des données aux clients rapidement. Ils ont choisi Node.js et ont profité de victoires, comme :

* Les options évolutives sont meilleures car un obstacle entre le front-end et le back-end est supprimé
* Les services back-end de Node.js sont tolérés par le langage front-end sur les serveurs
* Comme AWS Lambda utilise également Node.js, cela a permis de se concentrer sur le développement d'applications, et non sur l'infrastructure

Rick Adam, un chef d'équipe de 25 développeurs chez **Lowe's**, avait pour tâche de gérer les applications aux niveaux de présentation. Afin de reconstruire une application monolithique en 2007, l'entreprise a choisi Node.js car, à cette époque, même des changements mineurs dans le texte d'une application nécessitaient que l'ensemble de l'application soit corrigé, tandis que Node.js offrait de la flexibilité à cet égard. Ce choix a abouti aux résultats suivants :

* un courtage positif des requêtes web et des API (plus un grand potentiel de croissance)
* le modèle asynchrone de Node.js a offert une opportunité d'améliorer la fonctionnalité des applications et une meilleure UX
* une performance excellente
* Certaines des compétences front-end également utilisées dans la programmation back-end

### À quoi sert Node.js

Comme avec Node.js, on peut utiliser JavaScript sur le serveur, cela signifie qu'on peut écrire du JavaScript en dehors du navigateur. De plus, Node.js a la même force que JavaScript. Et il est basé sur des événements. Ce sont les 3 piliers sur lesquels Node.js repose fermement.

Nous pouvons construire des applications rapides en temps réel comme un chat, ou un système de téléchargement, ou toute application qui doit répondre à un grand nombre de requêtes. Et nous le savions déjà, n'est-ce pas ?

Alors, à quoi peut réellement servir Node.js ? Quand utiliser Node.js et à quoi est-il bon ? Eh bien, voici quelques utilisations que vous pouvez nommer aux clients, et des exemples de ce à quoi Node.js pourrait servir.

* **Streaming de données**
Comme le téléchargement de fichiers en temps réel, l'encodage de fichiers pendant le téléchargement, la construction de proxies entre les couches de données.
* **Applications monopage**
Applications web modernes, lourdes en traitement côté client. Les temps de réponse positifs et le partage de données entre le serveur et le client conviennent bien à de telles applications.
* **Applications web**
Applications web classiques côté serveur, utilisant Node.js pour transporter du HTML. L'un des principaux avantages à cet égard est un contenu plus convivial pour le référencement.
* **Chats / RTAs**
Applications légères en temps réel, comme les interfaces d'applications de messagerie, Twitter, les logiciels de chat. Un chat classique serait un excellent exemple d'utilisation de Node.js. Simple, intensif en données et sur plusieurs appareils.
* **APIs**
Interfaces de programmation REST / JSON et exposition de bases de données ou de services web à travers celles-ci. Pas de soucis concernant la conversion entre les systèmes.
* **Proxy**
Pour déployer Node.js en tant que proxy pour gérer les connexions de manière non bloquante. Idéal pour une application travaillant avec des services externes, exportant et important beaucoup de données.
* **Tableaux de bord**
Tableaux de bord de surveillance d'applications web ou de systèmes, permettant de suivre les actions des utilisateurs. Node.js peut également visualiser de telles interactions pour vous en temps réel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*t5y4f4XvGleJlO7eWK0seg.jpeg)

### 5 utilisations moins connues de Node.js

Pourtant, Node.js évolue rapidement et il n'est pas seulement possible de construire des applications web. Découvrez ces projets Node.js alternatifs qui sont encore en développement.

1. [NodeOS](http://node-os.com/) : un système d'exploitation basé sur Linux, avec JavaScript comme environnement d'exécution principal et NPM comme gestionnaire de paquets.
2. [Node-Webkit](https://github.com/nwjs/nw.js) : un environnement d'exécution pour les applications Node.js. Processus de packaging d'applications simple — zippez-le, ajoutez des informations et déployez-le multiplateforme.
3. [Log.io](http://logio.org/) : un outil de surveillance de logs, utilisant la bibliothèque Socket.io. Toutes les modifications que vous suivez, vous pouvez les suivre en temps réel et dans le navigateur.
4. [Nodecast](https://github.com/mauimauer/nodecast) : une application qui envoie des images et des vidéos de votre téléphone mobile à votre PC. Inspiré par Google Chromecast.
5. [Nexe](https://github.com/nexe/nexe) : un utilitaire pour la distribution d'applications Node.js en créant un seul exécutable. Bien qu'il ne fonctionne pour l'instant que sur Linux et MacOS X.

Et ce n'est pas tout, chers lecteurs stoïques qui lisez encore ceci. Les entreprises et projets à l'échelle de l'entreprise adoptent également Node.js.

### Node.js pour les entreprises

Nous avons déjà mentionné Walmart, Paypal et Netflix. **Livraison rapide et itérations** sont ce que Node.js permet et ce qui le distingue. Les meilleurs développeurs, aimant tout ce qui est nouveau, et qui peuvent tout faire en JavaScript, aiment la haute performance de Node.js. Un exemple célèbre a été le choix de Bill Scott, qui est maintenant VP chez PayPal, lorsqu'il a été confronté à un choix de carrière.

> Pourquoi aller chez Facebook et faire du PHP, quand on peut aller chez Paypal et faire du Node.js. — Bill Scott, VP de l'ingénierie chez PayPal

Alors, pourquoi des entreprises similaires choisissent-elles Node.js ? **Réduction des temps de chargement des pages, facilité de maintenance, réduction du nombre de serveurs** pourraient contenir certaines réponses. De plus, un nouveau type d'architecture de Node.js, appelé **micro-services**, aide à gérer de nombreuses modifications des logiciels d'entreprise. Sous cette approche, vous pouvez créer des applications à partir de plus petits morceaux, et développer ces morceaux séparément. Aucun dommage au fonctionnement global.

Il y a aussi des développeurs qui préfèrent les solutions unifiées full-stack. En pratique, les 4 principales technologies utilisées avec Node.js sont :

* Express
* Mongo
* jQuery
* Angular JS

Quels sont les domaines d'application potentiels de Node.js ?

* Médias
* Passerelles de paiement
* E-commerce
* Réseaux sociaux
* Applications web d'entreprise
* Backend/API pour applications mobiles

En gros, toute entreprise utilisant Node.js peut : employer moins de développeurs, utiliser moins de serveurs, diminuer les temps de chargement des pages. Pour plus de réflexions sur ce sujet, vous pouvez regarder la vidéo suivante, où le CTO et le responsable de l'architecture de [Nodesource](https://nodesource.com/) parlent de Node.js.

### Node.js en production, à faire et à ne pas faire

Une dernière chose dans notre voyage à Nodeland : quelques conseils pratiques sur l'exécution de cet ensemble d'outils. Nous devrions commencer par les gestionnaires de processus pour déployer des applications. Pour vous faciliter la vie, utilisez NPM, PM2, Adios, Strongloop ou tout autre gestionnaire de production Node.js.

**Ne faites pas d'applications lourdes en CPU** avec Node.js. Programmer des choses comme l'intelligence artificielle (IA), les logiciels d'encodage vidéo, et autres logiciels qui chargent le processeur, mieux vaut utiliser une autre solution. Node.js a une limite de mémoire de 1,5 Go, bien que vous puissiez appliquer le clustering pour diviser les processus en plus petits.

Les serveurs Node.js ne sont pas idéaux pour les tâches computationnelles et intensives en données. Ainsi, il est préférable de diviser de telles tâches en **micro-services** et de les déployer séparément.

**N'exécutez pas** une application Node.js **via le port 80**. Utilisez un proxy inverse devant l'application, comme Nginx par exemple. De cette manière, vous protégez les serveurs du trafic internet et répartissez l'équilibre de charge.

**Installez SSL** pour des raisons de sécurité. Utilisez toujours un proxy inverse, vérifiez les vulnérabilités dans SSL et corrigez les problèmes possibles. Effectuez des vérifications de sécurité de base de temps en temps. N'utilisez pas de versions obsolètes de Node.js et Express.

Pensez à l'infrastructure et à l'architecture avant le déploiement de l'application. Les experts recommandent de développer une application **au sein d'un réseau privé (VPN)**, afin de ne permettre que des connexions de confiance.

### Conclusion

Vous vous posez probablement une question rhétorique : pourquoi diable avons-nous versé notre âme sur Node.js ? La réponse est simple — nous aimons à la fois Node.js et JavaScript. Chez **ThinkMobiles**, nous aimons développer des applications web et mobiles en utilisant ce langage. Nous aimons Node.js pour sa facilité et sa rapidité, pour sa nature multiplateforme.

Merci d'avoir lu. Si vous aimez, laissez quelques ?.

Si vous voulez lire plus, consultez [ici](https://thinkmobiles.com/blog/).