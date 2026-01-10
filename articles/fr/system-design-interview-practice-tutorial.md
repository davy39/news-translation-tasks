---
title: Tutoriel d'entretien sur la conception de systèmes – Le guide du débutant pour
  la conception de systèmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T22:46:31.000Z'
originalURL: https://freecodecamp.org/news/system-design-interview-practice-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/youtube-system-design-thumbnail.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: distributed systems
  slug: distributed-systems
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: Microservices
  slug: microservices
- name: System Architecture
  slug: system-architecture
- name: System Design
  slug: system-design
seo_title: Tutoriel d'entretien sur la conception de systèmes – Le guide du débutant
  pour la conception de systèmes
seo_desc: 'By Charles M.

  System Design is an important topic to understand if you want to advance further
  in your career as a software engineer. Even if you are just beginning your coding
  journey, it''s a good idea to get a head start on learning about system de...'
---

Par Charles M.

La conception de systèmes est un sujet important à comprendre si vous souhaitez avancer dans votre carrière en tant qu'ingénieur logiciel. Même si vous débutez votre parcours en codage, il est bon de prendre de l'avance sur l'apprentissage de la conception de systèmes.

Au début de votre carrière, vous serez principalement testé sur votre capacité à coder. Cependant, lors d'entretiens de niveau supérieur, il y aura souvent un accent plus marqué sur la vérification de votre capacité et de votre expérience en matière de conception d'applications.

Le plus grand défi des ingénieurs lors des entretiens sur la conception de systèmes est qu'ils sont plus ouverts et qu'il n'existe pas de réponse unique et correcte. Ce manque de structure peut être intimidant, donc mon objectif avec cet article est de vous donner une feuille de route pour aborder ces types d'entretiens avec confiance.

Ce que cet article couvrira :

* Qu'est-ce qu'un entretien sur la conception de systèmes et pourquoi ils sont utilisés
* Les principales étapes d'un entretien sur la conception de systèmes
* Exemple de problème d'entretien – Concevoir YouTube

## Tutoriel Vidéo

Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/YEwKnGARDZI]

Et j'ai créé une playlist de vidéos sur des sujets spécifiques liés à la conception de systèmes et à l'architecture web :

%[https://www.youtube.com/playlist?list=PL_esswHjNwIeiFfVFer8uYly3Zk6YqXd0]

## Aperçu de l'entretien sur la conception de systèmes

À première vue, il semble ridicule de demander à quelqu'un de concevoir une énorme application comme Twitter ou YouTube en 45-60 minutes. Ces applications ont été conçues sur une période de plusieurs années par des centaines d'ingénieurs travaillant ensemble, donc c'est clairement une tâche impossible à réaliser lors d'un court entretien.

Il y a deux raisons principales pour lesquelles les entreprises utilisent ces types d'entretiens. La première est, bien sûr, de tester vos connaissances sur les technologies discutées. Ils veulent que vous alliez assez loin pour vous assurer que vous ne lancez pas simplement des mots à la mode sans comprendre comment les choses fonctionnent réellement.

La deuxième raison pourrait être plus importante, cependant. L'entretien sur la conception de systèmes est un moyen de simuler un scénario réaliste où vous travaillez ensemble avec l'intervieweur pour déterminer la meilleure décision de conception.

Obtenir la réponse parfaite n'est pas nécessairement la chose la plus importante ici – c'est certaines des autres choses que vous pouvez montrer, comme :

* Comment gérez-vous le fait d'être mis au défi ? Devenez-vous défensif ou prenez-vous les commentaires avec une attitude positive ? Êtes-vous obstiné ou étriqué ?
* Montrez-vous une connaissance des divers compromis que certaines décisions de conception impliquent ? Il y a une grande différence entre prendre une décision à l'aveugle et ne pas réaliser les conséquences, et connaître les avantages/inconvénients et accepter les compromis.
* Êtes-vous capable de communiquer efficacement et, si nécessaire, d'expliquer des concepts techniques complexes de manière facile à comprendre ?
* Êtes-vous un candidat avec qui l'intervieweur aimerait travailler à long terme ? Même si quelqu'un est un génie, s'il est désagréable de travailler avec lui, il pourrait ne pas être un bon recrutement.

## Étapes d'un entretien sur la conception de systèmes

Dans cette section, vous apprendrez un cadre général pour structurer la manière d'aborder un problème lors d'un entretien sur la conception de systèmes.

### Clarifier le problème et établir la portée de la conception

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-106.png)

La première chose que vous voudrez faire après que votre intervieweur vous ait donné le problème est de prendre quelques minutes pour poser des questions de clarification et comprendre exactement ce qu'ils recherchent.

La pire chose que vous pourriez faire ici est de commencer dans la mauvaise direction simplement parce que vous n'avez pas pris le temps de poser quelques questions. Vous avez un temps limité pendant l'entretien, donc vous voulez vous assurer de vous concentrer sur ce qui est important.

Voici quelques exemples de questions que vous pourriez poser :

#### Quels sont les cas d'utilisation / fonctionnalités de l'application ?

Dans cet article, nous utiliserons YouTube comme exemple. Il y a des centaines de fonctionnalités différentes que vous pourriez concevoir comme la diffusion de publicités, l'authentification, les algorithmes de recommandation, les commentaires, le téléchargement de vidéos, le traitement vidéo, et bien d'autres.

Lors d'un entretien, vous n'avez le temps de couvrir que quelques-unes de celles-ci, donc assurez-vous de poser des questions à l'intervieweur pour comprendre sur quoi ils veulent que vous vous concentriez pour la conception.

#### Combien d'utilisateurs sont attendus / quel est le volume de trafic probable ?

La complexité du système dépendra de la quantité de trafic qu'il doit gérer, donc assurez-vous de recueillir ces informations.

Vous ne voulez pas sur-ingénier les choses si le trafic est relativement faible et vous ne voulez pas non plus vous retrouver avec une application qui ne peut pas évoluer parce que vous ne l'avez pas conçue correctement.

Posez des questions comme combien d'utilisateurs l'application aura, la quantité moyenne de données par requête, combien de temps les données doivent être stockées, et à quel point le système doit être fiable et disponible ?

Cette étape va vous aider au-delà de la simple obtention de plus d'informations à travailler. Vous montrez également à l'intervieweur que vous comprenez comment recueillir des informations sur un problème vague.

### Déterminer des estimations de capacité approximatives

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-107.png)

En utilisant les informations que vous avez recueillies lors de la première étape, vous pouvez commencer à faire quelques estimations et généralisations approximatives pour des choses comme les exigences de stockage et de bande passante.

Ce processus impliquera quelques calculs de base comme multiplier le nombre d'utilisateurs par la taille moyenne des requêtes et la quantité de requêtes que chaque utilisateur est susceptible de faire quotidiennement.

### Créer une conception de haut niveau

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-108.png)

Ici, vous voulez créer une architecture approximative pour le système. Dessinez des éléments comme les équilibreurs de charge, les serveurs web, les serveurs d'applications, les files d'attente de tâches, la base de données, la mise en cache, le stockage de fichiers, et ainsi de suite. Vous devez inclure tous les composants principaux dont vous avez besoin pour créer le système.

Assurez-vous de communiquer avec l'intervieweur pendant cette étape et vérifiez pour vous assurer que vous n'avez rien oublié. Bien qu'ils ne vous le diront probablement pas directement, ils vous donneront un coup de pouce dans la bonne direction si vous avez oublié une fonctionnalité cruciale.

### Conception de l'API

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-114.png)

Cette partie est presque de la triche car vous utilisez la structure de l'entretien à votre avantage pour confirmer que vous êtes sur la bonne voie.

L'intervieweur ne vous mènera jamais délibérément dans la mauvaise direction, donc une fois que vous avez créé votre conception de haut niveau, vous pouvez commencer à esquisser quelques points de terminaison d'API approximatifs pour chaque composant.

Pour l'exemple YouTube, ils pourraient ressembler à ceci, selon les fonctionnalités que vous construisez :

* uploadVideo (userID, video, description, title)
* comment (userID, videoID, comment)
* viewVideo (videoID)
* videoSearch (query)

Dans certains cas, vous n'aurez peut-être pas besoin d'aller jusqu'à ce niveau de détail. Si la question de l'entretien est très générale comme "concevoir YouTube", vous pouvez probablement sauter cette partie. En revanche, si vous obtenez une question plus ciblée comme "concevoir le système de commentaires de YouTube", il serait judicieux d'aller plus en profondeur.

### Créer un schéma de données

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-113.png)

À ce stade, vous devriez avoir une bonne idée de toutes les exigences et des données nécessaires pour que l'application fonctionne, donc maintenant vous pouvez planifier comment vos données sont structurées.

Selon ce que vous construisez et les exigences, vous devrez peser les coûts et les avantages de choses comme l'utilisation d'une base de données relationnelle vs non relationnelle. Lors de la modélisation de vos données, vous voudrez également tenir compte de choses comme le partitionnement potentiel des données et la réplication.

### Examiner en détail les composants

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-112.png)

Ce qui se passe pendant cette section dépendra principalement des commentaires de l'intervieweur. Ils choisiront probablement quelques composants spécifiques sur lesquels se concentrer et vous demanderont pourquoi vous avez pris certaines décisions.

La partie la plus importante ici n'est pas nécessairement d'avoir 100% raison. Au lieu de cela, il s'agit de montrer que vous n'avez pas simplement pris des décisions à l'aveugle et que vous comprenez exactement quels compromis vous faisiez.

Vous devriez être capable de proposer des décisions de conception alternatives qui auraient pu être utilisées et expliquer pourquoi vous ne les avez pas utilisées.

## Comment concevoir YouTube

Maintenant que vous avez une idée générale de la manière dont fonctionne un entretien sur la conception de systèmes et un cadre pour gérer un problème de conception de systèmes, je vais vous montrer comment mettre tout cela en pratique en utilisant YouTube comme exemple.

### Étape 1 – Définir la portée du problème et les exigences

Ce sera un problème de haut niveau où nous implémenterons quelques-unes des principales fonctionnalités de YouTube sans trop approfondir chacune d'elles. Les fonctionnalités sur lesquelles se concentrer seront :

* Les utilisateurs peuvent télécharger des vidéos
* Les utilisateurs peuvent regarder des vidéos
* Les utilisateurs peuvent commenter les vidéos

### Étape 2 – Déterminer les estimations de capacité

Les deux principaux facteurs de capacité dans une application gérant de grandes quantités de vidéo comme YouTube seront le stockage de tout ce contenu et les exigences de bande passante pour livrer le contenu aux utilisateurs. Dans cette section, vous apprendrez à faire des estimations approximatives pour les exigences de capacité.

L'accent principal ici n'est pas sur la grande précision, mais sur la démonstration d'un processus de réflexion logique pour calculer ces nombres en fonction des informations disponibles.

Lors d'un entretien, on vous donnerait les données, mais dans ce cas, j'utilise deux éléments clés de données que YouTube a rendus publics :

* **Les créateurs YouTube téléchargent 500 heures de vidéo chaque minute**
* **Les utilisateurs de YouTube regardent 1 milliard d'heures de vidéo par jour**

Vous pouvez utiliser ces chiffres pour calculer les exigences de stockage et de bande passante avec quelques hypothèses.

#### Calcul de la bande passante

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-92.png)
_Calcul de la bande passante quotidienne_

Pour calculer une estimation de la bande passante, nous commençons par la quantité de vidéo regardée quotidiennement. L'hypothèse clé ici est la quantité de bande passante utilisée par heure regardée, car cela dépendrait de la qualité de vidéo que la plupart des utilisateurs choisissent de regarder.

L'estimation de 3 Gigaoctets est basée sur un pourcentage approximatif d'utilisateurs regardant en définition standard et d'autres choisissant HD ou 4K, qui consomment beaucoup plus de bande passante par heure regardée.

Les calculs ici sont assez simples : multipliez 1 milliard d'heures par la bande passante moyenne d'une heure de vidéo, puis divisez cela par 1000 pour convertir en téraoctets, puis divisez à nouveau par 1000 pour obtenir des Pétaoctets. L'estimation finale de la bande passante est de **3 000 Po** utilisés quotidiennement.

#### Calcul du stockage

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-91.png)
_Calculs étape par étape pour le stockage_

Sur la base de quelques hypothèses, nous pouvons calculer que YouTube devra stocker environ **2,16 Pétaoctets** de nouvelles vidéos chaque jour. Voici comment nous obtenons ce chiffre :

* Convertissez 500 heures en 30 000 minutes de vidéo téléchargées par minute
* Chaque minute de vidéo HD est d'environ 50 Mégaoctets en raison de la présence de copies de chaque vidéo dans plusieurs formats. Nous multiplions cela par 30 000 minutes puis divisons par 1000 pour convertir en Gigaoctets.
* Nous prenons ensuite les 1 500 Go téléchargés par minute et multiplions par 60 puis par 24 pour calculer la quantité quotidienne de vidéo téléchargée. Nous divisons à nouveau par 1000 pour convertir les Gigaoctets en Téraoctets
* Notre total final est de 2 160 Téraoctets téléchargés quotidiennement ou 2,16 Pétaoctets

### Étape 3 – Conception de la base de données

Pour notre base de données, nous utiliserons une base de données relationnelle standard comme MySQL. Le schéma ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-93.png)

Cette conception est très simple mais contient les éléments essentiels dont vous auriez besoin pour une implémentation de base. Il serait bon de faire quelques recherches sur les différences entre les bases de données relationnelles et non relationnelles afin de comprendre les types de situations où chacune excelle et quand les utiliser.

Pour certaines applications avec des exigences différentes, une base de données NoSQL pourrait avoir du sens. Souvent, les grands systèmes auront de nombreux services différents qui utilisent différents types de bases de données en fonction de leurs besoins.

### Étape 4 – Conception de haut niveau

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-95.png)

C'est un diagramme assez complexe, donc laissez-moi le décomposer :

* **Client** – Il pourrait s'agir d'un utilisateur sur une application mobile ou son ordinateur essayant de télécharger une vidéo, de faire un commentaire ou de regarder une vidéo
* **CDN** – Un réseau de distribution de contenu est utilisé pour réduire la latence et améliorer la fiabilité en matière de livraison de contenu statique comme des vidéos ou des images. Un CDN fonctionne en stockant du contenu dans des centres de données du monde entier afin que le contenu soit plus proche des utilisateurs. Cela entraîne une réduction de la latence car les requêtes parcourent une distance plus courte. Il y a également un avantage supplémentaire de stockage du contenu dans plusieurs emplacements afin que, même si un emplacement ne peut pas servir le trafic pour une raison quelconque, un autre emplacement peut le faire.
* **Équilibreurs de charge** – Un équilibreur de charge accepte les requêtes et les achemine vers les serveurs en fonction de plusieurs facteurs. À l'échelle de YouTube, un seul serveur ne peut pas gérer tout le trafic et vous voulez une réplication pour éviter un point de défaillance unique. L'équilibreur de charge peut vérifier l'état des serveurs et vérifier s'ils peuvent gérer le trafic ou choisir un autre serveur qui peut gérer la requête.
* **Services** – Vous pouvez considérer cela comme la couche applicative du système. Au lieu d'utiliser un seul monolithe pour gérer le trafic, nous utiliserons plusieurs microservices pour gérer des tâches spécifiques. La deuxième boîte pour chacun de ces services dans le diagramme représente plusieurs serveurs en cours d'exécution pour chacun d'eux afin d'augmenter la fiabilité. Si une réplique du service tombe en panne, il y en a toujours une autre pour prendre le relais et gérer le trafic.
* **Stores de données** – Lors de l'utilisation de microservices, il est généralement considéré comme une bonne pratique pour chaque microservice de posséder ses propres données. Si un service a besoin de données d'un autre, il peut y accéder via une API.
* **Processus de téléchargement de vidéo** – La gestion des téléchargements de vidéos impliquera plusieurs étapes, car essayer de la gérer de manière synchrone avec le serveur d'application serait fragile et réduirait les performances. Je couvrirai cela plus en profondeur dans la section suivante

Je ne veux pas trop approfondir ces composants individuels car je pourrais écrire des articles entiers sur chacun d'eux si je voulais les expliquer pleinement.

Si vous êtes intéressé par une explication plus détaillée, vous pouvez consulter la playlist sur la conception de systèmes que j'ai liée ci-dessus, qui contient des vidéos couvrant la plupart de ces concepts.

### Étape 5 – Examiner des composants et détails spécifiques

À ce stade, vous avez une conception fonctionnelle. Examinons maintenant certains des composants spécifiques en détail.

#### Téléchargement de vidéo

Le contenu vidéo est le cœur de YouTube, et il n'existe pas sans lui. Cela signifie que rendre le téléchargement de vidéos rapide et facile pour les utilisateurs est probablement la fonctionnalité la plus importante.

Imaginez télécharger une vidéo de plusieurs gigaoctets sur YouTube et voir le téléchargement échouer après 30 minutes lorsqu'il est à 95%. Pour éviter cela, vous voudrez supporter la capacité de reprendre les téléchargements si la connexion du client est temporairement perdue. La vidéo téléchargée peut ensuite être stockée avec un système de fichiers distribué comme HDFS.

Une fois le téléchargement terminé, il reste encore beaucoup à faire avant que la vidéo soit prête pour que les utilisateurs y accèdent. La vidéo doit être encodée dans plusieurs formats de qualité différents, vous devez générer des miniatures et pousser des copies de la vidéo vers le CDN global.

Encore une fois, à n'importe quelle étape, l'un de ces processus pourrait échouer. Pour éviter cela, vous aurez une file d'attente de tâches pour gérer ce processus et réessayer le traitement si celui-ci échoue à n'importe quelle étape.

#### Mise à l'échelle de la base de données

La base de données est souvent le goulot d'étranglement d'une application. Vous serez probablement testé sur votre compréhension de certains des concepts fondamentaux autour de la mise à l'échelle de la base de données. Cela pourrait inclure la mise en cache pour gérer les requêtes de lecture, le partitionnement et la réplication.

## Conclusion

J'espère que cet article vous a donné une meilleure compréhension de ce à quoi vous attendre lors d'un entretien sur la conception de systèmes.

Cet article s'est principalement concentré sur la structure de l'entretien lui-même plutôt que sur les concepts que vous devez comprendre pour répondre aux questions posées lors de l'entretien.

Deux excellentes ressources pour commencer à apprendre cela sont :

Un excellent article publié ici sur Free Code Camp News : [https://www.freecodecamp.org/news/systems-design-for-interviews/](https://www.freecodecamp.org/news/systems-design-for-interviews/)

Le dépôt system-design-primer sur GitHub : [https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

Les deux couvrent à peu près tous les concepts majeurs que vous devez connaître pour votre entretien sur la conception de systèmes et devraient vous mettre dans une excellente position pour réussir.