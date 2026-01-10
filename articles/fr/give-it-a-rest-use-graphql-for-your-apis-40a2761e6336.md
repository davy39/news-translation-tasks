---
title: 'Donnez-lui un REST : utilisez GraphQL pour vos APIs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-05T22:44:13.000Z'
originalURL: https://freecodecamp.org/news/give-it-a-rest-use-graphql-for-your-apis-40a2761e6336
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IvCDlfi3vQfgyKO1eFv4jA.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Donnez-lui un REST : utilisez GraphQL pour vos APIs'
seo_desc: 'By David Celis

  In the world of API architecture, REST has been the reigning ruler for a decade
  or more. Chances are that you use software built on a REST API multiple times per
  day on your phone, computer, or some other device. Maybe you’ve even work...'
---

Par David Celis

Dans le monde de l'architecture des APIs, REST a été le souverain incontesté pendant une décennie ou plus. Il est probable que vous utilisiez plusieurs fois par jour des logiciels construits sur une API REST, que ce soit sur votre téléphone, votre ordinateur ou un autre appareil. Peut-être avez-vous même travaillé sur une API REST ou écrit la vôtre ! Malgré la popularité de REST, il présente cependant quelques défauts flagrants.

### Qu'est-ce que REST ?

Dans les APIs REST, le serveur définit un ensemble spécifique de ressources qu'un client peut demander, et ces ressources sont définies par des URLs uniques. Par exemple, dans l'API d'une plateforme de microblogging générique, l'URL `/users/1` peut désigner le premier utilisateur du système, `/users/1/posts` pourrait retourner une collection de tous les posts que cet utilisateur a écrits, et `/users/1/posts/327` pourrait retourner un seul post. REST a de nombreuses nuances et une spécification bien documentée pour le comportement, mais les ressources basées sur les URLs couvrent l'idée de base. Ce qui est finalement important, c'est que le _serveur_ définit la structure des données que le client peut demander.

### Qu'est-ce qui ne va pas avec REST ?

Imaginez que vous travaillez pour la société susmentionnée Generic Microblogginator™ en tant que développeur d'applications mobiles. On vous donne la tâche d'écrire la vue mobile pour le profil d'un utilisateur, qui doit afficher des informations sur l'utilisateur et lister ses posts. Ce n'est pas trop difficile ; il suffit de frapper le point de terminaison `/users/{id}` pour obtenir les informations sur l'utilisateur, et `/users/{id}/posts` pour obtenir la liste des posts.

Vous livrez la vue mobile et attendez d'être ✨ébloui✨ par tous les retours des clients et les avis sur l'application. La semaine suivante, une fois que tous les avis sont arrivés, vous recevez une nouvelle exigence. That Other Microblogger™ affiche quelques commentaires sur chaque post dans leur vue de profil. Pourquoi ne pas faire de même ? Heureusement, votre API dispose déjà d'un point de terminaison pour obtenir les commentaires d'un post de blog : `/users/{id}/posts/{id}/comments`. Vous modifiez la vue pour frapper ce point de terminaison pour chaque post que vous affichez sur la page de profil d'un utilisateur, et vous avez terminé.

Mais maintenant votre application est lente, et cela nous amène à l'un des principaux problèmes avec les APIs REST :

### Trop de requêtes HTTP

Admettons-le : les applications client restent rarement simples. Plus souvent qu'autrement, chaque client a un ensemble de exigences assez spécifiques qui reflètent les données dont ils ont besoin de votre système. Si vous ne fournissez qu'une seule manière absolue de demander des données, vous aurez des clients qui essaieront de faire entrer un pieu rhomboïdal dans un trou en forme de diamant.

Dans notre exemple précédent, notre application mobile deviendra de plus en plus lente avec chaque post qu'un utilisateur écrit. Si un utilisateur a vingt posts listés sur son profil, nous émettons _22 requêtes API_. Une pour les informations sur l'utilisateur, une pour sa liste de posts, et ensuite vingt requêtes pour obtenir les commentaires de chaque post.

À mesure que vous ajoutez plus de composants à l'interface de votre application mobile, ce problème s'aggravera. Avec chaque nouveau composant d'interface utilisateur vient un nouvel appel API ou une nouvelle personnalisation des points de terminaison API existants. Vous pouvez imbriquer des objets les uns dans les autres pour éviter des appels API supplémentaires, mais à mesure que votre vue devient plus complexe, vous finirez inévitablement par imbriquer des données non pertinentes. Vous vous retrouverez avec des points de terminaison qui ne décrivent pas une seule ressource mais, au contraire, une vue de plusieurs ressources. Maintenant, votre API ne semble plus si RESTful.

Encore pire, vous devrez supporter les anciens points de terminaison tant qu'il y aura des versions anciennes de clients en circulation, sous peine de risquer de casser ces clients. Cela conduit à un autre problème majeur avec REST :

### La « versioning » des APIs REST est une douleur

La structure des réponses des APIs REST est importante. Les clients se construisent autour de la connaissance que chaque ressource a une structure spécifique. Lorsque Generic Microblogginator™ a lancé leur API pour la première fois, voici à quoi ressemblait la réponse pour obtenir un seul post :

Après un certain temps, vous décidez qu'il y a quelques choses que vous souhaitez améliorer dans la structure d'un post dans l'API. Les posts sont sur le point d'obtenir des catégories, donc vous devrez les ajouter en tant que nouveau champ. Vous avez également reçu des retours indiquant que le format de `published_at` n'est pas très convivial. Les clients JavaScript peuvent le parser correctement, mais vous préféreriez que n'importe quel outil puisse parser vos timestamps facilement, donc vous décidez de le changer en format ISO-8601. Une fois tout cela fait, vous voulez que la nouvelle structure ressemble à ceci :

Ça a l'air bien ! Malheureusement, l'un de vos changements cassera tous vos clients existants. Chaque client s'attend à ce que `published_at` soit dans le format moins convivial, donc c'est ainsi qu'ils essaieront de le parser. Si vous souhaitez mettre à jour un champ ou supprimer un champ, vous devez versionner votre API (que ce soit via l'URL ou un en-tête HTTP) et essayer de faire en sorte que les clients se mettent à jour. Il est peu probable que vous obteniez que chaque client se mette à jour, donc vous avez deux choix :

1. Être d'accord avec le fait de casser les anciennes versions des clients (y compris votre propre application)
2. Supporter les anciennes versions de votre API jusqu'au jour où votre entreprise décide d'[annoncer un nouveau chapitre dans leur incroyable voyage](https://ourincrediblejourney.tumblr.com).

La chose la plus facile à faire est simplement de laisser votre ancien code tranquille, ce qui signifie empiler de plus en plus de versions de vos versions d'API par-dessus les anciennes.

### Un challenger approche

Voici GraphQL, une technologie écrite par Facebook. Facebook était confronté à des problèmes majeurs avec le pipeline de données pour leurs applications mobiles. Leurs applications mobiles étaient autrefois des enveloppes autour de vues web et, à mesure que les applications mobiles augmentaient en complexité, elles ont commencé à souffrir de problèmes de performance et de plantages fréquents. Facebook s'est tourné vers l'écriture d'applications natives et s'est retrouvé à avoir besoin d'une nouvelle API pour récupérer des données pour leurs vues natives. Ils ont évalué REST et d'autres options mais, compte tenu de problèmes comme ceux décrits ci-dessus, ont finalement saisi l'opportunité de produire quelque chose de vraiment nouveau.

#### Qu'est-ce que GraphQL ?

GraphQL est, comme le nom pourrait le suggérer, un langage de requête. C'est aussi parfait pour les APIs. Il vous permet de définir vos données en utilisant un système de types complet, formant un schéma qui est auto-documenté. Il donne également aux clients un contrôle total sur les données qu'ils demandent.

#### Trop de requêtes HTTP ? Et si on faisait une seule requête HTTP ?

Avec GraphQL, les clients peuvent obtenir toutes les données dont ils ont besoin pour rendre une vue en utilisant une seule requête. Avec notre exemple précédent de page de profil, un client devrait émettre une requête pour obtenir les informations d'un utilisateur, une requête pour obtenir les posts de cet utilisateur, et ensuite une autre requête pour chaque post pour obtenir quelques commentaires. Avec GraphQL, ce client pourrait obtenir toutes les données ci-dessus avec une seule requête :

Boom! 💥 Il y a d'autres avantages à cela en plus du fait que nous sommes passés de 22 requêtes HTTP à une seule. Par exemple, votre utilisateur peut avoir d'autres informations attachées. Peut-être exposez-vous le timestamp de l'inscription d'un utilisateur. Peut-être qu'un autre client ne se soucie pas des catégories d'un post. Si un client n'a pas besoin de demander une donnée, _votre serveur non plus_. Donc, lorsqu'un client économise, vous pouvez aussi économiser en simplifiant vos propres requêtes de base de données.

#### Versioning ? Juste dépréciez !

Comme avec (la plupart des) APIs REST, vous pouvez ajouter des champs aux types GraphQL sans crainte. Pour supprimer des fonctionnalités, GraphQL inclut la dépréciation comme une fonctionnalité. Au lieu de supprimer complètement un champ et de casser les clients, vous pouvez déclarer un champ comme déprécié et le cacher des outils à mesure qu'il vieillit.

#### Documentation : vous n'aurez presque pas à vous en soucier

Permettez-moi d'être réaliste ici : je peux compter sur une main le nombre de fois où j'ai utilisé une API bien documentée. De nombreuses fois, les APIs restent non documentées ou mal documentées. Avec GraphQL, votre schéma est pratiquement auto-documenté. Tout ce que vous avez à faire est de donner à vos types et champs des descriptions lorsque nécessaire, et cela se fait dans le code lui-même. Les clients peuvent émettre des requêtes GraphQL spéciales pour introspecter le schéma de votre application et savoir, en une seule requête, toutes les données qu'ils peuvent demander, comment elles s'appellent et ce qu'elles décrivent. Les développeurs peuvent également utiliser des outils qui sont construits sur cette introspection comme [GraphiQL](https://github.com/graphql/graphiql), qui permet aux clients de tester leurs requêtes avec une mise en évidence de la syntaxe en direct et une détection des erreurs.

### Commencez avec GraphQL

Êtes-vous suffisamment convaincu pour essayer GraphQL ? Il existe de nombreuses ressources pour vous aider à commencer votre voyage :

* Consultez le [site officiel de GraphQL](http://graphql.org) pour la documentation et des exemples
* Jouez avec un exemple, l'[API GraphQL Star Wars](http://graphql-swapi.parseapp.com/?query=%7B%0A%20%20film(id%3A%20%22ZmlsbXM6MQ%3D%3D%22)%20%7B%0A%20%20%20%20title%0A%20%20%20%20releaseDate%0A%20%20%7D%0A%7D)
* La [Spécification GraphQL](http://facebook.github.io/graphql/) si vous êtes intéressé par les détails

Je vais également suivre ce post avec un autre, dans lequel nous créerons ensemble une petite API GraphQL, alors restez à l'écoute ! J'ai eu l'immense plaisir de travailler avec GraphQL chez GitHub et mon expérience me conduit à croire fermement que c'est l'outil d'API de l'avenir.