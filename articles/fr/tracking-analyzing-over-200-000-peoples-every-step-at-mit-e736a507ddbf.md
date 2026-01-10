---
title: Comment nous avons suivi et analysé les pas de plus de 200 000 personnes au
  MIT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-09T19:42:24.000Z'
originalURL: https://freecodecamp.org/news/tracking-analyzing-over-200-000-peoples-every-step-at-mit-e736a507ddbf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fnjGWp8sH0PxekvaqSES5w.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment nous avons suivi et analysé les pas de plus de 200 000 personnes
  au MIT
seo_desc: 'By Moin Nadeem

  My freshman spring, I had the pleasure to take 6.S08 (Interconnected Embedded Systems),
  which teaches basic EECS concepts such as breadboarding, cryptography, and algorithmic
  design.

  While the class was incredibly time-consuming and ch...'
---

Par Moin Nadeem

Mon premier printemps à l'université, j'ai eu le plaisir de suivre [6.S08](https://iesc-s2.mit.edu/6S08/S17) (Systèmes embarqués interconnectés), qui enseigne les concepts de base en EECS tels que le prototypage sur plaque d'essai, la cryptographie et la conception algorithmique.

Bien que ce cours soit incroyablement chronophage et difficile, je dois dire qu'il s'agit de l'un des cours les plus enrichissants que j'ai suivis jusqu'à présent. Je suis fier d'avoir travaillé avec des personnes incroyables (Un grand merci à Avery Lamp, Daniel Gonzalez et Ethan Weber pour les souvenirs inoubliables), et ensemble, nous avons construit un projet final que nous n'oublierons pas.

Pour notre projet final, notre équipe savait que nous voulions être aventureux. En allant chercher une glace un jour, Avery a suggéré un dispositif pour surveiller les requêtes de sondage WiFi, similaire à ce que font certains centres commerciaux. Après quelques recherches initiales et une persuasion envers nos instructeurs, nous avons décidé de nous engager et avons commencé à étudier l'idée.

### Qu'est-ce que les requêtes de sondage WiFi ?

La plupart des gens considèrent leur téléphone comme un récepteur ; il se connecte aux réseaux cellulaires / WiFi, et pour tous les usages pratiques, il n'est fonctionnel que lorsqu'il est connecté. Cependant, lorsque les téléphones recherchent des réseaux WiFi, ils envoient également des petits paquets d'informations appelés _requêtes de sondage_.

Ces _requêtes de sondage_ envoient des extraits d'informations tels qu'une adresse MAC unique (similaire à une empreinte digitale), un signal [RSSI](http://www.metageek.com/training/resources/understanding-rssi.html) (force du signal logarithmique), et une liste des SSID précédents rencontrés. Comme chaque téléphone envoie une adresse MAC (à l'exclusion des tentatives récentes d'anonymisation), nous pouvons facilement exploiter celles-ci pour suivre les étudiants qui se déplacent sur le campus.

### Collecte des requêtes de sondage

Les exigences pour notre projet final incluaient l'utilisation des composants standard 6.S08 que nous avons utilisés pendant le semestre : un microcontrôleur [Teensy](https://www.pjrc.com/teensy/), un [ESP8266](https://www.sparkfun.com/products/13678), et un module GPS. Cependant, étant donné la faible consommation d'énergie de l'ESP8266 (120 mA) et le manque de besoin d'un CPU puissant, nous avons décidé de contourner complètement le Teensy. Cette décision de conception nous a obligés à apprendre à utiliser les [programmeurs FTDI](https://www.sparkfun.com/products/9716) afin de flasher une [implémentation d'Arduino](https://github.com/esp8266/Arduino) pour nos ESP, mais cela nous a permis de continuer avec un environnement qui offrait une forte familiarité et une multitude de bibliothèques par rapport au firmware AT-command intégré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fnjGWp8sH0PxekvaqSES5w.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UahEImt5pp9QCQTRsnXdNA.jpeg)
_Flashage de l'ESP8266 et affichage des requêtes de sondage_

Dans les jours qui ont suivi, nous avions une preuve de concept qui suivait les requêtes de sondage faites autour du campus ; cela était suffisant pour atténuer les doutes de nos professeurs, et le jeu était lancé.

### Développement d'une preuve de concept

Maintenant que nous en savions assez sur les requêtes de sondage pour continuer, notre équipe a passé les jours suivants à écrire l'infrastructure qui nous permettrait de collecter ces requêtes en masse. J'ai écrit un backend Flask + MySQL pour gérer l'infrastructure des appareils et les informations, Avery a travaillé sur une application iOS pour faciliter le déploiement des appareils, Daniel Gonzalez a créé une belle interface pour notre site web, et Ethan a créé une plateforme d'analyse qui transformait la richesse des données entrantes en données intelligibles avec des informations précieuses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-wLnySlvmraFUsei8CkYHg.jpeg)
_AREALYTICS prenant ses premiers souffles de vie_

Côté matériel, Daniel et Ethan ont soudé nos ESP8266 sur des cartes prototypes, ainsi que des modules d'alimentation. Nous avons réutilisé les [PowerBoost 1000C](https://www.adafruit.com/product/2465) donnés par le cours pour rendre ces appareils entièrement portables, ce qui avait l'effet secondaire agréable de nous permettre d'effectuer un suivi dans certains endroits _étroits_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gTzncpBgMCHNbzWYT-AWHw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gc9ZeiZqp9OaaRow6UbKVw.jpeg)
_Soudure terminée des cartes et emballées dans de petites boîtes !_

Notamment, la dynamique de l'équipe était absolument merveilleuse : nous avons ri ensemble, appris ensemble et vraiment apprécié la compagnie les uns des autres. Les déploiements à 4h du matin n'étaient pas si mauvais lorsqu'ils étaient faits avec certains de vos meilleurs amis.

### Déploiement

Étant donné qu'Ethan a écrit un code astucieux pour connecter automatiquement les appareils au point d'accès WiFi non sécurisé le plus proche au démarrage, et qu'Avery a écrit une application pour mettre à jour l'emplacement et les champs de dernier déplacement (utile pour savoir quelles adresses MAC associer à chaque emplacement), le déploiement était aussi simple que de brancher les appareils à une prise à proximité et de s'assurer qu'ils pouvaient pinguer à la maison. Le déploiement était assez agréable si vous étiez créatif avec cela.

### Analyse des données

Après avoir laissé le projet fonctionner pendant une semaine, nous avons collecté environ **3,5 millions de requêtes de sondage** (!). J'aimerais également noter que les données sont toutes anonymisées ; en aucun cas ces données ne sont suffisamment fines pour déterminer une correspondance entre les adresses MAC et les individus, atténuant ainsi la plupart des préoccupations de confidentialité de nos instructeurs.

Nous avons commencé par appliquer le travail d'Ethan à tous les emplacements, ce qui a suscité un enthousiasme immédiat. Nos données **montront clairement le comportement périodique** derrière chaque emplacement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PRCcKh9MtmwornHRleingw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1cheoiD1N5eMwWX3ZkIHhw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-VKQ9i4Q3K2D2AzMm2nsXg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AmLqCmCnPMXrzEx7S0sDjw.png)

De plus, cela était clairement indicatif de certaines tendances plus larges à travers le campus : les artères principales (Lobby 10, 26-100) atteignaient un pic de trafic vers 17h, tandis que les bâtiments en bordure du campus (comme Stata, qui dispose d'un café) atteignaient un pic de trafic à midi. Inutile de dire qu'avec l'infrastructure en place, les données deviennent beaucoup plus excitantes.

Une fois que nous avons compris que les données pour ces tendances existaient, nous avons commencé à nous poser des questions plus intéressantes :

* Que pourrions-nous conclure sur la fabrication et la distribution des appareils au MIT ?
* Et si nous modélisions notre campus comme un graphe de réseau ?
* Existe-t-il une promenade la plus courante ?
* Plus intéressant encore, pourrions-nous prédire où les gens iront ensuite étant donné leur historique de localisation ?

Nous avons procédé à l'attaque de ces questions une par une.

### Analyse du jeu de données

Les adresses MAC fournissent en réalité une multitude d'informations en 6 octets ; nous pouvons exploiter ces informations pour déterminer davantage sur les personnes qui se déplacent autour de nous. Par exemple, chaque fabricant achète un préfixe de fournisseur pour chaque appareil qu'il fabrique, et nous pouvons utiliser cela pour déterminer les appareils les plus populaires autour du MIT.

Mais il y a aussi un piège — les tentatives récentes d'utiliser cette technologie pour suivre les individus par la NSA ont conduit de nombreux fabricants à anonymiser les requêtes de sondage. Par conséquent, nous ne pourrons pas déterminer complètement la distribution des appareils, mais nous pouvons enquêter sur la prévalence de l'anonymisation des requêtes de sondage.

Il est assez ironique que tout appareil qui anonymise les requêtes de sondage vous **informe en réalité qu'ils le font** — dans les appareils anonymisés, le [bit d'adresse locale](https://en.wikipedia.org/wiki/MAC_address) (deuxième bit le moins significatif) de l'adresse est défini sur 1. Par conséquent, l'exécution d'une simple requête SQL nous permet de savoir que près de **25 % des appareils anonymisent les adresses MAC** (891 131 / 3 570 048 requêtes de sondage collectées).

En exécutant la liste des préfixes de fournisseurs (trois premiers octets d'une adresse MAC), nous voyons que les deux premiers des huit principaux sont anonymisés.

* Adresse locale « 02:18:6a », 162 589 occurrences
* Adresse locale « da:a1:19 », 145 707 occurrences
* 74:da:ea de Texas Instruments, 116 133 occurrences
* 68:c4:4d de Motorola Mobility, 66 829 occurrences
* fc:f1:36 de Samsung, 66 573 occurrences
* 64:bc:0c de LG, 63 200 occurrences
* ac:37:43 de HTC, 60 420 occurrences
* ac:bc:32 d'Apple, 55 643 occurrences

Il est intéressant de noter qu'Apple est de loin le plus grand acteur dans l'anonymisation des requêtes de sondage, mais qu'ils semblent envoyer aléatoirement l'adresse réelle de temps en temps. Pour quelqu'un qui suit à une fréquence aussi élevée que la nôtre (presque toutes les secondes), cela pose problème ; nous avons vérifié avec des amis possédant des iPhones et avons pu suivre leur localisation avec une précision effrayante.

### Prédire les emplacements futurs

Après avoir modélisé les promenades des étudiants sous forme de graphe de réseau, nous avons réalisé que nous pouvions facilement calculer la probabilité d'aller à un autre nœud étant donné le nœud où ils se trouvaient précédemment. De plus, nous avons réalisé que ce graphe pouvait être facilement modélisé comme une chaîne de Markov. Étant donné un ensemble initial de sommets, où iront-ils ensuite ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*zSWMJG2uzQRbS_RHAYwJIg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gBCK_Pi0mpFO8XYp19N1Kg.jpeg)
_Modélisation des promenades sous forme de graphes avec networkx. Une ligne noire représente une flèche vers ce sommet._

![Image](https://cdn-media-1.freecodecamp.org/images/1*OlG47BYTViFUZm12QGIbCQ.jpeg)
_Adresses MAC floutées afin de préserver l'anonymat des utilisateurs._

Cependant, cela posait un défi significatif : notre base de données avait peu de compréhension de quand une promenade commençait et quand elle se terminait. **Ce n'était guère plus qu'un dump de coordonnées avec des emplacements et des horodatages**. Si vous examiniez les promenades manuellement, il était clair quand certaines commençaient et d'autres se terminaient, car les horaires seraient assez éloignés les uns des autres.

Cela peut être compris en examinant l'image ci-dessus. Par exemple, cet individu n'a clairement pas marché de Stata au bâtiment Whitaker, puisque ceux-ci sont sur des jours différents. Cependant, notre base de données n'en a aucune idée, et toute tentative ultérieure **d'utiliser ces données produirait des résultats erronés**.

Il est intéressant de noter que si nous restructurions cela comme un problème de clustering de _données de séries temporelles_, cela devient très intrigant. Et si nous pouvions regrouper les horodatages de manière à identifier les diverses « promenades » qu'un étudiant a faites ? Considérant le récent buzz autour du clustering des données de séries temporelles, j'ai pensé que ce serait un projet amusant pour commencer mon été.

### Analyse de la base de données en promenades

Afin de mieux comprendre comment potentiellement regrouper les données, j'avais besoin de mieux comprendre les horodatages. J'ai commencé par tracer les horodatages sur un histogramme pour mieux comprendre la distribution des données. Heureusement, cette étape simple m'a aidé à trouver ce que je cherchais : il s'avère que la fréquence des requêtes de sondage par rapport à la distance d'un ESP8266 suit approximativement une distribution gaussienne, nous permettant d'utiliser un [modèle de mélange gaussien](http://scikit-learn.org/stable/modules/mixture.html). Plus simplement, nous pourrions simplement exploiter le fait que les horodatages suivraient cette distribution pour extraire les clusters individuels.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mjt7LiE5lfCRslIRlj8mkQ.jpeg)
_Par exemple, ce modèle a un nombre optimal de dix clusters, visible par le « coude »._

Le problème suivant était qu'**un GMM doit être informé du nombre de clusters à utiliser**, il ne l'identifie pas de lui-même. Cela posait un problème majeur, surtout en considérant que le nombre de promenades que chaque individu a faites était très variable. Heureusement, j'ai pu utiliser le [critère d'information bayésien](https://en.wikipedia.org/wiki/Bayesian_information_criterion), qui évalue quantitativement les modèles en fonction de leur complexité. Si j'optimisais pour minimiser le BIC par rapport à la taille du modèle, je pourrais déterminer un nombre optimal de clusters sans surajustement ; cela est communément appelé la _technique du coude_.

Le BIC a bien fonctionné au début, mais il pénaliserait excessivement les individus qui ont fait de nombreuses promenades en **sous-calculant le nombre de clusters possibles**. J'ai comparé cela avec le [score de silhouette](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html), qui évalue un cluster en comparant la distance intra-cluster avec la distance au cluster le plus proche. Étonnamment, cela a fourni une approche beaucoup plus raisonnable pour le clustering des données de séries temporelles et a évité de nombreux pièges rencontrés par le BIC.

J'ai mis à l'échelle ma droplet DO pour laisser cela fonctionner pendant quelques jours et j'ai développé un rapide [bot Facebook](http://github.com/moinnadeem/ml_notification_system) pour me notifier à la fin. Avec cela hors du chemin, je pouvais retourner au travail pour prédire les prochaines étapes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*na9U9vmxzpfvGSWuiydHgg.jpeg)
_Résultats du clustering avec le score de silhouette ! Les adresses MAC sont floutées pour préserver l'anonymat._

### Développement d'une chaîne de Markov

Maintenant que nous avons segmenté une énorme chaîne de requêtes de sondage en promenades séparées, nous pouvons développer une chaîne de Markov. Cela nous a permis de prédire l'état suivant des événements étant donné les précédents.

J'ai utilisé la bibliothèque Python [Markovify](https://github.com/jsvine/markovify) pour générer un modèle de Markov étant donné un corpus de notre étape précédente, ce qui a considérablement raccourci le temps de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*D9VyxKl8PkOKffC9ukKEBg.jpeg)
_Une promenade auto-générée à partir de notre chaîne de Markov. Comme chaque événement représente une observation, des événements accrus signifient qu'une personne était à un emplacement pendant une période prolongée._

J'ai inclus un échantillon de chaîne de Markov généré ci-dessus ; cela représente en réalité la promenade d'un étudiant quittant une conférence (26-100 est une salle de conférence) et se rendant à son dortoir ! C'est vraiment excitant qu'un ordinateur ait pu capter cela et générer une promenade similaire. Certains emplacements sont répétés, cela est dû au fait que chaque emplacement enregistré représente en réalité une observation. Par conséquent, si un emplacement apparaît plus que d'autres, cela signifie simplement que l'individu a passé plus de temps là-bas.

Bien que cela soit primitif, **les possibilités sont assez excitantes**. Et si nous pouvions exploiter cette technologie pour créer des villes plus intelligentes, lutter contre la congestion et fournir de meilleures informations sur la manière dont nous pourrions réduire les temps de marche moyens ? Les possibilités de science des données dans ce projet sont _illimitées_, et je suis incroyablement enthousiaste à l'idée de les poursuivre.

### Conclusion

Ce projet a été l'un des moments les plus excitants de ma première année, et je suis incroyablement heureux de l'avoir fait ! J'aimerais remercier mes incroyables pairs de 6.S08, notre mentor Joe Steinmeyer, et tout le personnel de 6.S08 qui a rendu cela possible.

J'ai appris beaucoup en poursuivant ce projet, de la manière de regrouper les données de séries temporelles à l'infrastructure nécessaire pour suivre les requêtes de sondage autour du campus. J'ai joint quelques autres bonnes choses ci-dessous des aventures de notre équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kCGh82wAJcEaJdbCUx5zbA.jpeg)
_L'équipe Arealytics !_