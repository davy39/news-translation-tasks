---
title: Comment j'ai conçu, développé et déployé un chatbot entièrement dans le cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-07T04:18:13.000Z'
originalURL: https://freecodecamp.org/news/how-i-designed-developed-and-deployed-a-chatbot-entirely-in-the-cloud-a60614eb94f2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bu2w7ew1YC6gWzVhwksGEQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai conçu, développé et déployé un chatbot entièrement dans le
  cloud
seo_desc: 'By Rajat Saxena

  It all started with a YouTube video I recorded few months back. In it, I talked
  about the importance of deliberate revision. This helps you retain things in your
  mind for a longer period of time, and gives you techniques to revise imp...'
---

Par Rajat Saxena

Tout a commencé avec une vidéo YouTube que j'ai enregistrée il y a quelques mois. Dans cette vidéo, je parlais de **l'importance de la révision délibérée**. Cela vous aide à retenir les choses dans votre esprit pendant une période plus longue et vous donne des techniques pour réviser des projets importants. Si vous ne l'avez pas encore fait, veuillez [la regarder ici](https://youtu.be/SvOzfgptqhM).

Dans la vidéo, j'ai parlé de la fréquence à laquelle vous devriez réviser, de ce qu'est [la courbe de l'oubli](https://en.wikipedia.org/wiki/Forgetting_curve), et pourquoi vous devriez vous en soucier.

Je voulais vous donner un outil approprié, en plus de la vidéo, afin que vous puissiez réviser mieux. Étant développeur, ma réponse naturelle a été « Écrivons une appli ! »

Mais si vous avez lu mon autre article sur [pourquoi les applications natives sont condamnées](https://hackernoon.com/mobile-apps-are-doomed-i-repeat-mobile-apps-are-doomed-3cf80193819f), vous savez que j'étais un peu réticent à écrire une application autonome pour cela. J'ai fait un pas en arrière et analysé la situation. J'avais besoin d'un back-end pour stocker les données des utilisateurs et d'un front-end pour collecter et afficher ces données.

Je voulais que l'intégration des utilisateurs soit aussi fluide que possible. Forcer les utilisateurs à télécharger une nouvelle application est difficile. Si je construisais un chatbot, cela servirait ce but et je n'aurais pas à convaincre qui que ce soit de télécharger quoi que ce soit. Je gagnerais aussi du temps puisque je n'aurais pas à construire une application cliente autonome et à passer par les processus des magasins d'applications.

Vous pouvez essayer le bot que j'ai construit [ici](https://blooming-escarpment-58368.herokuapp.com/).

Passons directement au processus. Lisez la suite pour voir comment mon chatbot est passé d'une idée à un produit entièrement fonctionnel — entièrement en utilisant des outils basés sur le cloud.

### Quête #1 : IA et NLP

Le traitement du langage naturel (NLP) et l'IA sont des parties intégrantes de tout chatbot intelligent. Donc, dès le début, je savais que j'aurais besoin d'IA et de NLP pour rendre mon bot « intelligent » et quelque chose avec lequel vous pourriez parler. Il devrait également comprendre ce que vous lui demandez de faire. Je viens d'un milieu de développement full stack et je n'ai aucune expérience avec le Machine Learning, l'IA ou le NLP. Mais pour ce bot, toutes ces choses étaient des nécessités.

En tant qu'enthousiaste de la technologie, je garde toujours un œil sur les outils et bibliothèques que les grands lancent. J'étais au courant de [Wit.ai](https://wit.ai/), une API en ligne, publiée par Facebook pour permettre le NLP dans vos applications et bots. J'ai joué avec pendant un certain temps mais je l'ai trouvé particulièrement difficile.

J'ai rapidement recherché d'autres alternatives et trouvé [Api.ai](https://api.ai/). J'ai joué avec et je l'ai trouvé plus convivial pour les développeurs, alors je l'ai choisi.

Voici exactement ce que vous faites avec ces API d'IA :

1. Tout d'abord, vous écrivez une conversation probable qui peut avoir lieu entre votre bot et une personne.
2. Sur la base de cette conversation, vous créez un diagramme de flux exclusif (ou quelque chose de similaire) qui gère tous les résultats de la conversation.
3. Vous programmez l'agent Api.ai pour gérer tous les résultats prédéfinis en utilisant son tableau de bord. C'est assez simple — une fois que vous l'avez appris.

**Note :** Vous pouvez appeler une logique personnalisée, qui réside dans votre back-end sécurisé, si les gestionnaires intégrés d'API.ai ne peuvent pas gérer votre cas d'utilisation. Dans le cas de Revisebot, je stockais l'historique d'apprentissage de chaque utilisateur et calculais les sujets que l'utilisateur devait réviser ensuite. Cela nécessitait des calculs personnalisés et des mécanismes de persistance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3LjbN07y5RZBvo1JYIBt9w.png)
_NLP de Revisebot utilisant Api.ai_

Api.ai propose également certains agents pré-construits, tels que des agents de conversation et de météo, qui peuvent répondre aux requêtes des utilisateurs sur la météo et d'autres sujets. Ce sont des choses plug-n-play que vous pouvez utiliser directement dans vos chatbots.

Puisque Revisebot devait gérer des cas d'utilisation personnalisés, j'ai dû écrire du code. Il est temps de produire du code JavaScript/Node.js. Hourra !

### Quête #2 : Hébergement Cloud

Je suis un utilisateur de longue date de [Digital Ocean](https://www.digitalocean.com), mais cela coûte environ 6 $/mois au minimum. Comme je n'espérais pas gagner de l'argent avec Revisebot, l'héberger sur Digital Ocean n'avait pas de sens. Je perdrais de l'argent sur une base mensuelle.

**J'avais besoin d'un hébergement cloud gratuit pour ce projet**. Je savais que Firebase offrait un hébergement gratuit (comme je l'ai utilisé par le passé). J'ai également utilisé [Open Shift](https://www.openshift.com) pour d'autres projets (principalement [Laravel](https://laravel.com/)). Mais j'ai pensé qu'il serait bon de chercher d'autres alternatives sur Google, au moins pour le bien de Node.js.

C'est alors que j'ai découvert [Heroku](https://www.heroku.com/) et son plan gratuit.

En peu de temps, j'ai appris que l'intégration de Node.js de Heroku est géniale. J'ai donc lu leur documentation et rapidement lancé une application Node.js sur leur dynamo gratuit. C'était suffisant pour mes besoins. Sa seule limitation était qu'il s'endormait après un certain temps, donc le premier appel API pouvait échouer pendant que le dynamo se réveillait. Mais j'ai adapté mon chatbot pour répondre à de tels scénarios.

### Quête #3 : MongoDB dans le cloud

J'avais envisagé d'apprendre MongoDB. J'ai donc décidé d'utiliser MongoDB comme base de données pour mon chatbot. Une application de chat est un bon cas d'utilisation pour le système de stockage basé sur des documents de MongoDB.

Mon plan a rencontré un petit obstacle lorsque j'ai découvert que Heroku n'offrait pas d'intégration MongoDB gratuitement. Pas de souci — je suis retourné voir mon ami Google et j'ai recherché un « MongoDB cloud gratuit ».

C'est ainsi que j'ai découvert [mLabs](https://mlab.com/), qui offre des instances MongoDB gratuites dans le cloud.

Leur plan gratuit n'est pas recommandé pour les applications prêtes pour la production, mais ce n'est pas grave. Je vais faire fonctionner mon chatbot sur le plan gratuit de toute façon.

### Quête #4 : IDE Cloud

Mon plan était de coder tout cela dans le peu de temps libre que j'avais après mon travail à temps plein. À cause de cela, j'avais besoin de la flexibilité de coder de n'importe où. Mon espace de travail de développeur devait donc résider dans le cloud, que je pouvais charger de n'importe où j'avais internet.

J'utilise des IDE basés sur le cloud depuis un certain temps et l'expérience est mitigée. [Nitrous.io était génial mais ils l'ont fermé](https://www.nitrous.io/). :( Après avoir essayé quelques IDE en ligne comme [cloud9](https://c9.io/) et [codeanywhere](https://codeanywhere.com/), celui que j'ai trouvé le plus stable et convivial pour les développeurs était [Codenvy](https://codenvy.io). Il offre des espaces de travail que vous pouvez créer ou détruire à votre guise.

J'ai donc créé un nouvel espace de travail basé sur Ubuntu dans Codenvy et installé node, npm, git et curl immédiatement. Codenvy offre également un terminal, donc les utilisateurs de Linux se sentent chez eux. Mon espace de travail de développeur dans le cloud était prêt.

Ensuite, j'ai **git-cloné** le dépôt de mon projet depuis Heroku, et configuré l'intégration de la base de données avec l'instance MongoDB de mLab en utilisant des fichiers ._env_. Comme vous pouvez le voir dans la capture d'écran ci-dessous, _blooming-escarpment-58368_ était mon projet Node.js Heroku.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hpg2Wdi9l1fLt3oX5LaoYQ.png)
_Codage de revisebot dans Codenvy.io_

### Quête #5 : Intégration du chatbot avec les API des réseaux sociaux

Le chatbot devait fonctionner avec Facebook Messenger et Slack. J'aurais dû apprendre les API de développeur pour les deux plateformes et configurer ma machine de développement pour tester les appels API. Heureusement, [Api.ai](https://api.ai) offre également une intégration facile en un clic avec la plupart des plateformes de réseaux sociaux. Vous devez simplement suivre leur documentation pour amener votre chatbot sur la plateforme spécifiée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*blosw16HhjUGCvC6Bz98ZA.png)
_Intégration des réseaux sociaux pour Revisebot_

Comme vous pouvez le voir dans la capture d'écran ci-dessus, j'ai intégré Revisebot avec Facebook Messenger et Slack, pour l'instant. Cette étape ne prendra pas longtemps, croyez-moi.

En utilisant ces outils, j'ai pu écrire, tester et déployer l'ensemble de l'écosystème de mon chatbot (la base de données, la couche application, le front-end et l'agent IA) pour réagir aux requêtes des utilisateurs.

Mais il restait encore quelques éléments à mettre en place pour faire de Revisebot un produit complet et fini.

### Quête #6 : Gestion du code source

Bien que j'étais le seul développeur travaillant sur ce chatbot, je devais stocker le code quelque part en sécurité. Git était un choix évident pour le code source et la gestion de version, mais [GitHub](https://github.com/) n'offre pas de dépôt privé gratuit. Revisebot n'était pas censé être une aventure open-source, donc je ne pouvais pas héberger le code source là-bas. De plus, comme je n'utilisais pas de machine de développement locale, je ne pouvais pas utiliser de dépôt git local pour stocker mon code.

À l'époque, j'ai joué avec [bitbucket.org](https://bitbucket.org/product). J'avais une certaine idée qu'ils offraient un **dépôt privé gratuit**, mais je n'étais pas sûr s'ils offraient encore de tels plans. Je suis allé sur leur site et j'ai trouvé qu'ils le faisaient. Le reste est assez explicite.

### Quête #7 : Éléments graphiques

Le design et les graphiques sont au cœur de tout produit numérique. J'avais besoin d'un logo, d'images de fond et d'images de couverture pour la page Facebook de mon chatbot, la liste de l'application Slack et la page d'accueil.

Je ne suis pas un designer, donc j'avais besoin d'aide. J'ai dû choisir la palette de couleurs et les icônes, mélanger des formes pour créer un logo, et plus encore.

Heureusement, il existe un outil utile pour cela appelé [Canva](https://www.canva.com/).

Il offre des modèles de design prêts à l'emploi pour les réseaux sociaux, YouTube et les logos que vous pouvez personnaliser selon vos besoins. J'ai créé le logo de Revisebot entièrement dans Canva, en utilisant des formes gratuites et un peu de créativité. Je pense que je m'en suis bien sorti.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bu2w7ew1YC6gWzVhwksGEQ.png)
_Logo de Revisebot, construit en utilisant Canva.com_

J'ai également utilisé certains de leurs modèles gratuits pour créer d'autres éléments visuels pour Revisebot comme une image de couverture Facebook.

C'est ainsi que j'ai codé et déployé un chatbot entièrement fonctionnel, qui peut vous aider à planifier vos révisions, entièrement dans le cloud.

Cela me coûte exactement 0 $ pour exécuter ce service.

Faites-moi savoir si vous avez des questions concernant mon projet.

*Aucune machine locale n'a été utilisée dans la création de ce chatbot.*

Si vous avez aimé cet article, donnez-moi quelques applaudissements et suivez-moi pour plus d'articles comme celui-ci. Vous devriez également vous abonner à ma chaîne YouTube, si vous aimez développer des choses numériques.

#### [Twitter](https://twitter.com/rajat1saxena)|[YouTube](https://www.youtube.com/channel/UCUmQhjjF9bsIaVDJUHSIIKw)|[Rayn Studios](https://medium.com/rayn-studios)

Jusqu'à la prochaine fois…