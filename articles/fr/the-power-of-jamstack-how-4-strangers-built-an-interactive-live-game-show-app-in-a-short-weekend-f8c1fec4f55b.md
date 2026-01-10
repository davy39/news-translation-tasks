---
title: 'La puissance de JAMstack : Comment 4 inconnus ont construit une application
  interactive de jeu télévisé en un week-end'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-25T02:45:44.000Z'
originalURL: https://freecodecamp.org/news/the-power-of-jamstack-how-4-strangers-built-an-interactive-live-game-show-app-in-a-short-weekend-f8c1fec4f55b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9SP9vOKQCKZ6z_4klt6SUA.png
tags:
- name: GraphQL
  slug: graphql
- name: hackathons
  slug: hackathons
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'La puissance de JAMstack : Comment 4 inconnus ont construit une application
  interactive de jeu télévisé en un week-end'
seo_desc: 'By Tadas Antanavicius

  Question: What can you do with the following?


  Saturday + Sunday

  16 hours of brainstorm, design, and dev time

  4 strangers who met at breakfast on Saturday morning

  Hacking space, free food, and a slew of hackathon goodies from th...'
---

Par Tadas Antanavicius

### Question : Que pouvez-vous faire avec les éléments suivants ?

* Samedi + Dimanche
* 16 heures de brainstorming, de design et de développement
* 4 inconnus qui se sont rencontrés lors du petit-déjeuner du samedi matin
* Un espace de hacking, de la nourriture gratuite et une multitude de goodies de hackathon offerts par les organisateurs du [freeCodeCamp/Netlify JAMstack 2018 Hackathon](https://medium.freecodecamp.org/winners-from-the-2018-freecodecamp-jamstack-hackathon-at-github-2a39bd1db878) organisé chez GitHub

### Réponse : Une application web fonctionnelle de "Game Show" en direct.

* Construite sur les épaules d'au moins 18 logiciels libres significatifs (estimation conservative)
* Environ 80 joueurs simultanés lors de la démonstration finale en direct
* 4 dollars de dépenses totales (pour un nom de domaine)
* Un grand prix de 500 dollars parmi les 28 équipes et des centaines de participants avec des soumissions

Le pitch final pour WITWorld par l'équipe Where In The World :

> _Application web de "Game Show" qui présente des photos curatées d'images provenant de quelque part dans le monde à un public en direct et participant. Dans chaque jeu, le public est invité à épingler l'emplacement où la photo a été prise sur une carte. Plus un joueur est proche de l'emplacement réel, plus il monte dans le classement._

[Voir le dépôt ici.](https://github.com/tadasant/where-in-the-world)

Le terme "**site statique**" vient avec beaucoup de bagages. Cela semble être un vestige des premiers jours d'Internet, lorsque les pages web statiques étaient considérées comme "affichant les mêmes informations pour tous les utilisateurs, dans tous les contextes" — une phraséologie qui figure toujours sur l'entrée Wikipedia [Static web page](https://en.wikipedia.org/wiki/Static_web_page) au moment de la rédaction de cet article.

Ainsi, lorsque nous disons que la fondation fondamentale d'une application [JAMstack](https://jamstack.org/) est qu'elle est centrée autour d'un site web statique, cela est sûr de soulever beaucoup de sourcils. Après tout, la nature personnalisée et riche en informations du web d'aujourd'hui semble suggérer que les pages web statiques ne sont pas une option viable.

Cette mentalité a conduit à une prolifération de développeurs full stack. Les bootcamps et les programmes du monde entier prêchent la nécessité de compétences full stack comme MERN (MongoDB, Express, React et Node).

Il y a certainement de la valeur dans une telle approche — mais il y a _une autre façon_.

Entrez JAMstack. Sa mission : **autonomiser l'ingénieur front-end**.

Meilleures performances. Sécurité accrue. Mise à l'échelle facile. Tout cela avec juste JavaScript, des API et du Markup.

Le besoin d'apprendre une pile complète de technologies comme MERN pour pouvoir produire des applications techniques précieuses n'est plus la seule voie. La grande majorité des cas d'utilisation commerciaux n'ont pas besoin que vous réinventiez la roue sur le back-end. L'authentification est un problème résolu. Accepter les paiements est un problème résolu. Et ainsi de suite : vous pouvez vous concentrer sur devenir un magicien de CSS et JavaScript pour construire votre application et assembler des API éprouvées, vraies et sécurisées pour combler les lacunes.

Chaque nouvelle API apporte un monde de nouvelles possibilités de cas d'utilisation — chacune plus dynamique que la précédente.

Et en effet, l'équipe Where In The World s'est lancée pour montrer exactement ces possibilités.

### Montrer JAMstack, et montrer le monde

Oui, c'est notre slogan un peu cliché pour ce que WITWorld apporte à la table.

Alors que [Jeff](https://www.jeffappareti.com/), [Tyler](https://twitter.com/TJVickOH), [Gabe](https://twitter.com/GabeGreenfield) et moi nous sommes rencontrés lors du petit-déjeuner (merci, GitHub, pour l'approvisionnement sans fond de délicieuses friandises), nous avons échangé des idées sur ce que nous pourrions faire.

> _En voici une. C'est une de ces idées qui va être soit vraiment bonne, soit vraiment, vraiment mauvaise. Connaissez-vous HQ Trivia ? …_

Juste après la fin de la keynote post-petit-déjeuner, Jeff nous a chuchoté :

> _Hé, appelons cela « Where In The World »_

Et nous étions partis.

### Lors d'un hackathon, vous construisez pour la démonstration

L'une des meilleures décisions que nous avons prises tôt a été de choisir notre étoile polaire, de couper le superflu et de nous concentrer uniquement sur un objectif. Cet objectif — comme cela devrait être le cas dans presque tous les hackathons — était : construisons les étapes dont nous avons besoin pour la démonstration. Rien de plus, rien de moins.

Cela signifie que ce ne sera pas une application prête pour la production. Cela signifie que nos clés API sont codées en dur dans notre code côté client. Cela signifie que notre application explose si l'un des joueurs décide d'appuyer sur le bouton « Retour » de son navigateur. L'espacement CSS est incorrect. Notre palette de couleurs était en retard d'une semaine pour Halloween. Des spaghettis, mais ça marche ? Expédié.

[Notre dépôt est disponible publiquement](https://github.com/tadasant/where-in-the-world), mais s'il vous plaît, s'il vous plaît, ne regardez pas notre code. C'est un vrai bazar. Le fait que notre dernier commit soit arrivé à 17h56 alors que la date limite pour le code était 18h00 en dit assez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-gB9a4ipPBUi0tq-1yf7tQ.png)
_La configuration CI basée sur les webhooks sans douleur de Netlify a rendu ce commit de 17h56 en direct sur [https://witworld.live/](https://witworld.live/" rel="noopener" target="_blank" title=") une minute plus tard_

### Avec JAMstack, nous nous appuyons sur les épaules de géants

Dès le début, nous avions une idée approximative de la manière dont WITWorld allait techniquement voir le jour. Il était clair que les abonnements GraphQL devraient être au cœur de celui-ci : les sockets étaient le meilleur moyen de créer une application web "live", et GraphQL a soigneusement emballé le concept dans un "abonnements".

Un seul problème : aucun de nous n'avait jamais écrit d'abonnement GraphQL auparavant.

[Hasura](https://hasura.io/) à la rescousse.

Hasura fournit "un serveur GraphQL et des déclencheurs d'événements sur une base de données Postgres en quelques minutes" et était l'un des sponsors du hackathon.

Convertir notre application du modèle classique de lecture-écriture push-pull en temps réel via des websockets était une simple affaire, selon les mots de la documentation de Hasura :

> _Vous pouvez transformer n'importe quelle requête en abonnement en remplaçant simplement `query` par `subscription` comme type d'opération._

Et quelques lignes de configuration Apollo pour insérer le point de terminaison de websocket pratique de Hasura.

Ce n'est qu'un exemple. Nous avons vécu ce paradigme simple "2 lignes de code et la fonctionnalité majeure XYZ est prête à l'emploi" encore et encore :

* `[create-react-app](https://github.com/facebook/create-react-app)` de Facebook nous a donné une structure d'application web complète, prête pour la production, avec quelques appels de ligne de commande
* Déployer cette application sur un CDN mondial sur [Netlify](https://www.netlify.com/) était une question de clics autour d'une belle interface utilisateur
* La combinaison de [Apollo](https://www.apollographql.com/) et des spécifications [GraphQL](https://graphql.org/) signifiait qu'une norme claire existait pour chaque type d'opération de données côté client
* `[styled-components](https://www.styled-components.com/)` a gardé la (quantité admise manquante de) CSS dans notre application facile à utiliser et modulaire
* [Google Maps API](https://cloud.google.com/maps-platform/) signifiait que nous avions une carte mondiale interactive intégrée dans notre application après une heure de lecture de sa documentation
* [Les fonctions de Netlify](https://www.netlify.com/docs/functions/) — une abstraction sur AWS Lambda — nous ont donné un endroit parfait pour centraliser nos opérations de "maître de jeu", cruciales pour une démonstration fluide

Sans oublier toutes les petites bibliothèques npm FOSS que nous avons utilisées afin de ne pas passer trop de temps à comprendre ce que signifient réellement la latitude et la longitude, entre autres morceaux de colle.

N'oublions pas tout le travail qui a été mis dans les navigateurs modernes comme Chrome et Firefox, ou les personnes responsables des webhooks Netlify-Slack qui nous ont alertés chaque fois que notre build échouait, ou la présence révolutionnaire de React elle-même. Même des outils comme Heroku que nous avons touchés pour un seul clic pour déployer une instance Hasura — c'est un témoignage de leur impressionnante performance qu'ils fonctionnent si bien que nous réalisons à peine leur rôle majeur.

Le meilleur : **aucun des éléments ci-dessus ne coûte un seul dollar à utiliser**. Pas à l'échelle d'un hackathon en tout cas.

### Par-dessus tout, nous avons eu de la chance

![Image](https://cdn-media-1.freecodecamp.org/images/1*A5FfZzJG1JGoACoxjXlrmQ.png)
_(De gauche à droite) Tadas, Gabe, Jeff et Tyler. L'Octocat de GitHub nous surveillait manifestement._

Pour le reste du week-end, si l'un de ces scénarios ne s'était pas déroulé en notre faveur, nous ne parlerions probablement pas beaucoup de WITWorld aujourd'hui :

* 2 minutes avant de monter présenter la démonstration finale, Tyler a découvert un bug dans notre configuration de présentation qui aurait continué à afficher la même image pour chaque jeu.
Une minute plus tard, il l'avait diagnostiqué et réparé.
* Notre application était (est) pleine de failles de sécurité et de bugs.
Quelqu'un aurait pu effacer notre base de données en deux secondes pendant l'une des démonstrations.
* Nous avons choisi un nom d'équipe qui commence par "W". Cela signifiait que nous avions la chance de faire l'interview de jugement en dernier, et la présentation finale en dernier.
Avec tout le processus étant une course contre la montre, chaque minute de préparation supplémentaire était précieuse.
* Vous souvenez-vous de votre colocataire de collège sélectionné aléatoirement ? Probablement une chance sur deux que ce soit une expérience terrible.
Et puis il y a nous : 4 inconnus qui ont miraculeusement survécu au week-end sans un seul désaccord.
* Notre large éventail de compétences et d'aptitudes signifiait que nous n'étions jamais bloqués sur un problème de développement particulier pendant plus d'une courte période avant que quelqu'un n'intervienne et ne répare rapidement les problèmes qu'il avait rencontrés à un moment donné dans son propre travail.
Les projets de hackathon sont bien connus pour exploser à cause d'un bug ennuyeux que personne ne peut résoudre pendant des heures — nous avons somehow évité tout cela.
* Nous n'avions jamais testé notre application avec plus d'une poignée de personnes avant de monter sur scène pour gérer 70+.
Notre croyance que Heroku pouvait gérer autant de connexions websocket sur son niveau gratuit était une foi aveugle.

Je pourrais continuer. Le week-end a été une montagne russe, et pourtant, encore et encore, les choses se sont simplement mises en place.

### WITWorld restera comme un projet open source

Comme nous n'avons pas de plans concrets pour l'avenir de WITWorld, l'avenir immédiat nous verra nettoyer la base de code, mettre en place une licence MIT et quelques problèmes structurés, et la pousser au point d'être une vitrine publique raisonnable de la technologie JAMstack.

Les contributeurs de tous niveaux de compétence sont les bienvenus ! Nous aimerions vous garder dans la boucle, que vous souhaitiez contribuer ou simplement suivre les progrès. [Rejoignez la liste de diffusion](http://eepurl.com/dNYsno).

### JAMstack est introduit par une communauté formidable

Au début des années 2000, vous deviez acheter votre propre espace de rack de serveur pour mettre en place un site web. AWS et d'autres fournisseurs de cloud avaient retourné ce concept d'ici 2010.

Aujourd'hui, nous sommes à l'étape suivante de cette évolution : vous n'avez pas besoin d'un expert back-end ou DevOps pour lancer votre prochaine idée d'application. Netlify et le reste de l'économie des API sont sur le point d'avoir tourné cette page d'ici 2020.

Un énorme merci à ceux qui ont participé au hackathon :

* Benjamin Dunphy de [Real World React](https://www.realworldreact.com/) — organisateur de hackathon extraordinaire
* Quincy Larson de [freeCodeCamp](https://www.freecodecamp.org/) — âme de la fête et humble bâtisseur de l'empire freeCodeCamp
* Matt Biilman et Phil Hawksworth de [Netlify](https://www.netlify.com/) — points bonus pour avoir également organisé [JAMstack_conf](https://jamstackconf.com/)
* Brian Douglas de [GitHub](https://github.com/) — hôte gracieux et fournisseur de nourriture
* Tous les sponsors d'API : Hasura, Fauna, Formspree, Clarifai et Pilon

Avec beaucoup, beaucoup plus de personnes derrière les scènes.

Des événements comme ce hackathon et la JAMstack_conf correspondante ne sont que le début. Nous attendons avec impatience l'avenir radieux de la communauté JAMstack !

Un grand merci à Jeff Appareti, Gabe Greenfield et Tyler Vick pour avoir révisé les brouillons de cet article. Et pour avoir été une équipe formidable avec laquelle passer le week-end.

Cet article a été publié à l'origine sur [tadasant.com](https://tadasant.com/blog/power-of-jamstack-live-game-show-application)