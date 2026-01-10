---
title: Comment protéger votre application contre une attaque par déni de service
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-20T23:54:53.000Z'
originalURL: https://freecodecamp.org/news/how-we-handled-a-denial-of-service-attack-a-simple-security-lesson-8cdd542d4def
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YOOMRpyJbALLB9XH1G_E1Q.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: mobile app development
  slug: mobile-app-development
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment protéger votre application contre une attaque par déni de service
seo_desc: 'By Akash Sant

  I wrote this post not to describe how to use certain technologies, but rather to
  provide insights into the lessons we learned while mitigating a Denial of Service
  (DoS) attack on a web based service we built.

  We’ll start with a bit of a...'
---

Par Akash Sant

J'ai écrit cet article non pas pour décrire comment utiliser certaines technologies, mais plutôt pour fournir des informations sur les leçons que nous avons apprises en atténuant une attaque par déni de service (DoS) sur un service web que nous avons construit.

Nous commencerons par un peu de contexte.

Depuis l'année dernière, mes amis et moi pensions que les transports interurbains avaient besoin d'une sérieuse mise à niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/7Kxbdk5QNFk7sR2BoD7Vb4pxZyOcUTHKEkbI)
_Facebook - Groupe de covoiturage de l'Université de Waterloo_

![Image](https://cdn-media-1.freecodecamp.org/images/Sj2NsUg435Ew6fMH78Nr8XsFEJ1siOk1IngG)
_Université de Waterloo - Centre Davis_

Nous avons commencé à remarquer que quelque chose ne semblait pas correct ici. Nous sommes tous des étudiants occupés, et attendre dans des files d'attente aussi longues pour les transports en commun n'en vaut tout simplement pas la peine. Les transports interurbains manquaient d'éléments de fiabilité, d'efficacité et de simplicité. Nous avons décidé que, à l'avenir, cela devait changer.

### **Présentation de [POOL](http://coming-soon.poolapp.io) - #MadeWithLove**

Depuis quelques mois, une équipe de quatre ingénieurs logiciels et moi avons travaillé sur une application de covoiturage simple, rapide et facile à utiliser pour Android et iOS.

Je me souviens du jour où nous nous sommes rencontrés pour la première fois pour brainstormer l'idée du projet. Nos notes étaient remplies des défis que nous allions rencontrer en exécutant une idée d'une telle envergure. Des défis liés à la fiabilité des utilisateurs, à la confiance entre les conducteurs et les passagers, et aux problèmes de planification des trajets.

Le nombre actuel de membres dans les groupes de covoiturage et de partage de trajets de Waterloo sur Facebook est d'environ 40 000. Nous savions que nous devrions construire des services rapides et évolutifs. Nous avons commencé notre premier prototype en tant qu'application Android, ce qui a conduit à un portage vers React Native pour la rendre multiplateforme.

Le 7 mars 2018, nous avons annoncé la sortie officielle de la version 1.0.

En deux heures, plus de 40 utilisateurs s'étaient inscrits et plus de 14 conducteurs avaient proposé leurs services. Tout se passait comme prévu. Cependant, ce ne serait pas vraiment une fête sans un trouble-fête, n'est-ce pas ?

#### **L'attaque par déni de service**

Les attaques par déni de service (DoS) visent à inonder les serveurs victimes avec de fausses requêtes, les empêchant ainsi de servir les utilisateurs légitimes.

Trois heures après le lancement, nous avons reçu un e-mail de support d'un utilisateur avec le message suivant : « Les trajets à proximité continuent d'afficher le symbole de chargement ». J'étais légèrement excité de savoir que quelqu'un se souciait assez de nous envoyer un e-mail de support, mais mon excitation fut de courte durée après avoir décidé de jeter un coup d'œil aux journaux du serveur. Je ne pouvais pas croire ce que je voyais.

Les serveurs étaient submergés par un déluge de **~600 requêtes par seconde**. Nous étions sous attaque, et nous avons immédiatement su que ce n'était pas un trafic légitime.

Mon premier instinct fut de mettre les serveurs en mode maintenance et d'espérer que l'attaquant s'en irait. Mais dès que nous avons restauré le serveur depuis le mode maintenance, les attaques ont repris. À ce stade, nous avons réalisé que notre application recevait plus d'attention que nous ne l'avions supposé et j'étais complètement confus quant à la manière de commencer à mettre en place une solution.

### **Projet S.O.S - Sécurisation de nos services**

Tous les membres de l'équipe principale ont été alertés, et nous nous sommes réunis pour mettre nos cerveaux en commun afin d'atténuer l'attaque. Nous avons utilisé plusieurs méthodes différentes, que je vais décrire ci-dessous.

#### **Limitation de débit**

Lorsque les attaques ont continué, j'ai su que nous devions les ralentir en mettant en place une sorte de limitation de débit sur nos API.

La limitation de débit consiste essentiellement à limiter le nombre de requêtes (par minute) à une adresse IP donnée à partir d'une source spécifique (qui, dans notre cas, était Internet). Après avoir appliqué la limite de débit, seul un nombre spécifique de requêtes serait accepté par le serveur.

L'algorithme de limitation de débit doit être rapide afin qu'il ne met pas simplement en file d'attente toutes les requêtes entrantes, mais rejette plutôt toutes les requêtes de l'attaquant aussi rapidement que possible.

C'était un début, mais cela n'était définitivement pas suffisant pour arrêter l'attaquant pour de bon.

#### **Limitation de débit spécifique aux endpoints**

Ensuite, en raison de la limitation de débit, l'inondation des serveurs et la mise en file d'attente des requêtes n'étaient plus réalisables pour l'attaquant. L'attaquant a donc légèrement changé de stratégie. Au lieu de cela, ils ont ciblé les endpoints POST sur le serveur afin de poster de fausses données sur le serveur. Cela signifiait qu'ils pouvaient créer N trajets chaque minute (en fonction de l'étape précédente de limitation de débit).

En quelques heures, le serveur avait des centaines de trajets factices créés par l'attaquant. Cela nécessitait une limitation de débit des endpoints POST avec une limite plus stricte. La limitation de débit de nos endpoints POST à environ deux requêtes par heure a fait l'affaire. Même si l'attaquant créait maintenant des trajets factices, nous aurions assez de temps pour les détecter et nettoyer notre datastore.

#### **Meilleure chance la prochaine fois !**

Au cours des prochaines heures de surveillance, l'attaquant a réessayé. Cependant, aucun dommage n'a été causé et l'application est restée en ligne tout au long de l'attaque. Les stratégies de limitation de débit avaient donc fait l'affaire ! Il était maintenant temps de se concentrer sur la recherche de l'attaquant.

La surveillance et le suivi de nos journaux de serveur nous ont permis de récupérer l'adresse IP à l'origine des attaques.

![Image](https://cdn-media-1.freecodecamp.org/images/TiW4P0rOFHPqnq8wGpxgkr2pnNWhj2UowkD8)
_Journaux du serveur pendant les attaques_

Le chemin de la requête et l'adresse IP de l'attaquant ont été masqués pour des raisons de confidentialité. Les journaux ont été enregistrés en mode maintenance. Si vous inspectez les journaux de plus près, vous remarquerez le champ `id` dans la requête. Cela représente le faux compte que l'utilisateur avait créé sur nos services pour pouvoir accéder à l'application.

Pool utilise l'authentification Facebook, ce qui signifie que l'attaquant avait créé un faux compte Facebook pour s'inscrire avec Pool. En utilisant l'`id` local (enregistré dans les journaux), nous avons pu trouver l'`id` Facebook de l'utilisateur et émettre une interdiction de compte.

Notre équipe a ensuite utilisé [https://www.whois.com/whois/](https://www.whois.com/whois/) pour effectuer une recherche de domaine sur cette adresse IP.

En creusant davantage, nous avons remarqué que les requêtes provenaient d'une instance `EC2` sur Amazon Web Services. À ce stade, nous avons réalisé que nous aurions pu simplement signaler l'adresse IP à AWS, mais quel est l'intérêt de prendre la voie facile ?

#### **Ce n'est pas encore fini...**

Suite à ces mesures, avant que l'interdiction de compte ne puisse prendre effet, l'attaquant a décidé d'utiliser les clés API de la plateforme Google Cloud (anciennement exposées côté client) pour utiliser tout le quota de l'API Google. Environ 4 millions de requêtes avaient frappé les serveurs en moins d'une heure.

Mais cela nécessitait une solution simple.

1. Nous avons d'abord empêché la tentative de l'attaquant de voler le quota de l'API Google en ajoutant des restrictions au niveau de l'application aux clés API. Cela signifie que seules les requêtes faites à partir de l'application seraient acceptées.
2. Nous avons ajouté une solution plus permanente en déplaçant les appels à l'API Google côté serveur, masquant ainsi les clés API sur le serveur. Il est généralement considéré comme une pratique sécurisée de masquer la clé derrière une variable d'environnement sur le serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/NI6Hhbw5iNboM-KPuzIo9HqUqS641YAA6VZS)
_Pool - Requêtes Google Cloud Platform (8-9 mars)_

#### **Si vous avez l'intention de vaincre un hacker, vous devez penser comme un hacker !**

Si j'étais l'attaquant utilisant l'instance `EC2` pour inonder les serveurs de requêtes, je voudrais vérifier un code d'erreur de requête HTTP pour savoir quand les services sont tombés afin d'économiser des ressources. La limitation de débit renvoie un code d'erreur 429 - Trop de requêtes, tandis qu'une requête de connexion réussie renverrait un 200 - OK.

J'ai pu configurer cela côté serveur pour renvoyer 200 - OK au lieu du code d'erreur de limitation de débit « trop de requêtes ». Cela a empêché les scripts de l'attaquant de savoir quand ils étaient limités en débit et a constamment utilisé leurs ressources.

En surveillant les journaux du serveur, nous avons remarqué que les requêtes de l'attaquant arrivaient et étaient rejetées par le serveur via la limitation de débit.

### **Conclusion**

Après avoir combattu les attaques pendant 30 heures, nos services étaient enfin impénétrables à une attaque DOS de cet attaquant. Ils ont fait de nombreuses tentatives avant d'abandonner enfin. À chaque étape de l'attaque, une mesure petite et simple a été prise pour atténuer le DOS. Ensemble, ces tactiques simples se sont avérées hautement efficaces.

À la fin de la journée, la simplicité et la persévérance mènent loin, et les échecs ne sont que les pierres de gué vers le succès.