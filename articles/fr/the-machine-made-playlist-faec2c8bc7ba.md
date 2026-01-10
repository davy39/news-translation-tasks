---
title: Comment j'ai conçu un algorithme qui mélange les playlists de groupes venant
  dans votre ville
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-05T15:15:57.000Z'
originalURL: https://freecodecamp.org/news/the-machine-made-playlist-faec2c8bc7ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T_4UZtxr2sGPwDS6FuSO6w.jpeg
tags:
- name: Design
  slug: design
- name: music
  slug: music
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
seo_title: Comment j'ai conçu un algorithme qui mélange les playlists de groupes venant
  dans votre ville
seo_desc: 'By Sina Habibian

  This is a retrospective on funkavinci.com, a web project I worked on last summer.
  It was a series of weekly computer-generated playlists showcasing the best upcoming
  concerts in town.

  Inspired by Spotify’s Discover Weekly, Funkavinci...'
---

Par Sina Habibian

Il s'agit d'une rétrospective sur [funkavinci.com](http://www.funkavinci.com), un projet web sur lequel j'ai travaillé l'été dernier. Il s'agissait d'une série de playlists générées par ordinateur chaque semaine, mettant en avant les meilleurs concerts à venir en ville.

Inspiré par Discover Weekly de Spotify, Funkavinci utilisait un algorithme pour générer une playlist hebdomadaire avec 20 titres. Chaque titre correspondait à un artiste qui se produirait en live au cours de la semaine suivante. Si un auditeur aimait un titre, il savait que l'artiste serait en ville et pouvait acheter des billets pour le voir performer.

J'ai récemment mis fin au support de Funkavinci après quelques mois de fonctionnement en parallèle. J'écris cet article pour décrire mon processus de construction et partager quelques enseignements.

### Motivation

Je découvrais beaucoup de nouvelle musique l'été dernier. Il y avait de nombreux artistes que je voulais voir en live et que je savais se produiraient à San Francisco tôt ou tard. Je me demandais également si un outil de découverte musicale pouvait être construit en surveillant les artistes en tournée dans la ville.

Des services comme Bands in Town et Songkick abordaient partiellement ces idées mais avaient des lacunes. Ils envoyaient des notifications quotidiennes mentionnant les noms de groupes en ville, mais j'avais du mal à reconnaître [les noms](https://www.youtube.com/watch?v=W_IzYUJANfk). Je ratais des concerts auxquels je serais allé. En faisant quelques recherches, j'ai découvert que c'était un problème courant. Une approche plus efficace serait de déplacer l'attention du nom de l'artiste vers leurs chansons et de laisser la musique parler d'elle-même.

J'ai également appris que les concerts devenaient de plus en plus importants dans l'industrie musicale globale. Les musiciens aujourd'hui dépendent de la musique live, plutôt que de la musique enregistrée, pour la [majorité de leurs revenus](http://www.nytimes.com/2015/08/23/magazine/the-creative-apocalypse-that-wasnt.html). Pourtant, la plupart des concerts ne sont pas complets. Construire un service qui met en avant les meilleurs concerts en ville aiderait non seulement les fans à découvrir de la musique, mais aiderait également les musiciens à vendre des billets.

J'ai décidé de construire une application qui générerait une nouvelle playlist chaque semaine avec 20 titres représentant 20 concerts à venir et de la livrer à mon email.

### Prototypage d'une solution

Après avoir consulté quelques APIs, j'ai décidé d'utiliser [Seatgeek](http://platform.seatgeek.com/) comme source pour les listes de concerts à jour. Ils ont une base de données relativement complète d'événements, fournissent une API JSON et permettent une utilisation commerciale de leur API.

Pour générer une playlist avec les meilleurs concerts, j'ai conçu l'algorithme suivant :

1. Interroger l'[API Seatgeek](http://platform.seatgeek.com/) pour tous les concerts à venir à San Francisco pour la semaine suivante. Cela retournait généralement environ 100 événements.
2. Extraire l'artiste principal pour chaque événement et interroger l'[API de recherche Spotify](https://developer.spotify.com/web-api/search-item/) pour cet artiste.
3. Interroger l'[API des titres populaires Spotify](https://developer.spotify.com/web-api/get-artists-top-tracks/) pour le titre le plus populaire de chaque artiste.
4. Filtrer la liste résultante pour obtenir les 20 meilleurs titres classés par popularité et les ajouter à une playlist Spotify pour l'écoute. Il s'agissait d'une liste des 20 meilleurs artistes en ville la semaine suivante, du moins selon la popularité de leur titre le plus populaire sur Spotify.

J'ai été agréablement surpris par le résultat. Le format de la playlist avait mis la musique au premier plan. Plus intimidé par les noms de groupes excentriques, j'ai écouté et suis tombé amoureux de quelques artistes. Mieux encore, ils étaient tous en tournée à San Francisco, donc je les ai vus en live en moins d'une semaine. J'ai partagé la playlist avec quelques amis qui ont eu des résultats similaires.

![Image](https://cdn-media-1.freecodecamp.org/images/AiWI5s5I0IIjmcn2ZLWQP9-O26eREypSTUjU)
_La première playlist Funkavinci_

### Construction d'un produit

J'ai rapidement réalisé que l'ajout de 20 titres populaires à une playlist ne permettait pas une expérience d'écoute fluide. Il y avait des titres électroniques, hip hop et rock qui apparaissaient en séquence. De plus, les données de recherche Seatgeek et Spotify n'étaient pas toujours parfaites. Il y avait parfois des artistes qui ne se produisaient pas en ville mais avaient des noms similaires à ceux qui y étaient.

J'ai modifié l'algorithme pour ajouter les 50 meilleurs titres à une playlist privée. Je les écoutais personnellement et les élaguais pour garder les 20 meilleurs. Je m'assurais que les artistes se produisaient tous dans la ville et que la musique s'écoulait à travers la playlist dans son ensemble.

J'ai construit une application Rails pour gérer les différentes playlists, spectacles, artistes et titres. J'ai ajouté une interface d'administration qui me permettait de visualiser, ajouter ou supprimer ces différentes entités.

![Image](https://cdn-media-1.freecodecamp.org/images/TMQv6ptwL-nXYOEQl7q7lvGOhGVcR12NCxve)
_L'interface d'administration_

Il y avait une structure sous-jacente propre reliant les artistes aux playlists et les playlists à la ville. Cela signifiait que, à l'avenir, je pourrais ajouter une couche d'abstraction au backend pour générer des playlists pour d'autres villes également.

Je suis ensuite passé au site orienté utilisateur. J'ai utilisé une disposition basée sur des cartes pour mettre en avant les concerts et compléter la playlist. Cette disposition permettrait également une expérimentation et un réordonnancement faciles si je décidais un jour de personnaliser les playlists pour l'utilisateur connecté.

![Image](https://cdn-media-1.freecodecamp.org/images/LdTfHwBBIyDqhaMUPVjDTZIlslE8g6vWqx8Y)
_Utilisation de cartes pour afficher les informations sur les concerts_

### Dans la nature

J'ai mis le site en ligne en août. Un groupe d'amis s'est inscrit au début et la portée a augmenté organiquement au cours des semaines suivantes.

La playlist Funkavinci était livrée sous forme de newsletter hebdomadaire chaque dimanche matin à 10h. L'email fournissait une parcelle de valeur et créait un sentiment d'attente autour de son arrivée hebdomadaire. Les utilisateurs pouvaient simplement transférer l'email à des amis, créant un chemin de croissance organique.

Un autre hack de croissance consistait à utiliser le flux social Spotify pour diffuser la notoriété. Les playlists avaient des noms comme « [Funkavinci.com | 12/2901/05](http://www.funkavinci.com/playlists/24) ». Si quelqu'un trouvait un ami écoutant la playlist et voulait en savoir plus, il pouvait simplement visiter le site web.

![Image](https://cdn-media-1.freecodecamp.org/images/2WImqZje3O1n6w9qCWoK-gvPRe7bSHF78BbQ)
_Funkavinci.com sur le flux social Spotify_

Le processus de mise en place de la playlist hebdomadaire était automatisé et prenait une heure de temps par semaine. J'écoutais 50 titres et écrivais un petit texte conversationnel annonçant la nouvelle playlist. Cela était inclus sur le site et dans la newsletter.

![Image](https://cdn-media-1.freecodecamp.org/images/km2FkAos7--LQbyu3n3C4pL5wU09z90y-f8w)
_Je me suis amusé à écrire ces petits textes hebdomadaires._

### Mes enseignements

Alors que je ferme Funkavinci et passe à autre chose, quelques-unes de mes notes pour moi-même sont :

#### **Comprendre les avantages et les inconvénients de l'utilisation d'API externes**

À un moment donné, j'ai envisagé de faire de Funkavinci une entreprise. J'entendais régulièrement des amis acheter des billets et aller à des concerts grâce au service. Je me demandais si cela pouvait se transformer en quelque chose de plus grand.

J'ai finalement décidé de ne pas le faire pour plusieurs raisons, dont le fait que Funkavinci était dans une position de faible levier. Il ne possédait ni le contenu (c'est-à-dire la musique) ni les données (c'est-à-dire les métriques d'écoute sur Spotify ou les métriques d'achat sur les sites de billetterie).

La construction d'une application grand public nécessite une compréhension approfondie du comportement des utilisateurs et je n'avais pas accès à des points de données importants. Une solution potentielle aurait été de réduire la dépendance à Spotify (ou à son alternative Soundcloud) en hébergeant indépendamment la musique et en fournissant un lecteur multimédia. Des sites comme [8tracks](http://8tracks.com/) ou [Resident Advisor](https://www.residentadvisor.net/) suivent cette approche. Cela implique des complications supplémentaires, y compris la gestion des droits musicaux, et ne semblait pas valable étant donné le potentiel limité.

Les APIs nous permettent de tirer parti des plateformes existantes et de construire des solutions qui n'auraient pas été possibles autrement. Elles peuvent également nous placer dans une position de faible levier où l'on dépend d'une plateforme externe pour notre existence ou pour l'accès à des données cruciales.

#### **Lancer des projets avec une poussée de publicité**

Avec Funkavinci, je suis tombé dans un piège classique de l'ingénieur en évitant la publicité. Ayant des standards élevés pour le produit et conservant encore des traces de vieilles tendances perfectionnistes, je pensais que l'application n'était pas prête pour le grand public. Je n'ai donc pas fait d'effort réel en marketing et ne l'ai partagée que dans quelques forums en ligne.

J'ai maintenant appris que la publicité d'un projet dès le début peut être très utile. Cela aidera à créer une communauté précoce d'utilisateurs qui informeront vos décisions. De plus, et peut-être plus important dans les premiers jours, cela vous fournira un sentiment de responsabilité et de motivation accrues.

#### **Choisir des noms faciles à prononcer et à épeler**

Comme le dit le proverbe : « il n'y a que deux choses difficiles en informatique : l'invalidation du cache et le nommage des choses. » Il en va de même pour les produits. J'ai choisi le nom Funkavinci car il évoquait l'image d'un DaVinci funky et parce qu'il était audacieux. Voir plusieurs personnes lutter pour le prononcer ou l'écrire m'a appris une leçon précieuse.

Avec cela, je dis adieu à un projet amusant et passe au suivant.

_Vous voulez dire bonjour ? Contactez-moi sur [Twitter](https://twitter.com/sinahab)._