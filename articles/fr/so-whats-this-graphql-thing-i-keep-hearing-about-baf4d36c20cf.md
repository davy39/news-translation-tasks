---
title: Alors, qu'est-ce que ce truc GraphQL dont je n'arrête pas d'entendre parler
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-11T15:41:46.000Z'
originalURL: https://freecodecamp.org/news/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uF2-YU2quykHIs4tKXy7sw.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Alors, qu'est-ce que ce truc GraphQL dont je n'arrête pas d'entendre parler
  ?
seo_desc: 'By Sacha Greif

  If you’re like me, you probably go through three stages when hearing about a new
  technology:

  1. Dismissal


  One more JavaScript library?! Just use jQuery already!


  2. Interest


  Hmm, maybe I should check out this new library I keep heari...'
---

Par Sacha Greif

Si vous êtes comme moi, vous passez probablement par trois étapes lorsque vous entendez parler d'une nouvelle technologie :

#### 1. Rejet

> Encore une bibliothèque JavaScript ?! Utilisez simplement jQuery !

#### 2. Intérêt

> Hmm, peut-être que je **devrais** vérifier cette nouvelle bibliothèque dont je n'arrête pas d'entendre parler...

#### 3. Panique

> Aidez-moi ! Je dois apprendre cette nouvelle bibliothèque **maintenant** ou je serai complètement obsolète !

Le truc pour maintenir votre santé mentale dans ces temps qui évoluent rapidement est d'apprendre de nouvelles choses entre les étapes deux et trois, une fois que votre intérêt est piqué mais alors que vous êtes encore en avance sur la courbe.

C'est pourquoi maintenant est le moment parfait pour apprendre ce qu'est exactement ce truc GraphQL dont vous n'arrêtez pas d'entendre parler.

### Les Bases

En résumé, GraphQL est **une syntaxe qui décrit comment demander des données**, et est généralement utilisé pour charger des données d'un serveur vers un client. GraphQL a trois caractéristiques principales :

* Il permet au client de spécifier exactement les données dont il a besoin.
* Il facilite l'agrégation de données provenant de plusieurs sources.
* Il utilise un système de types pour décrire les données.

Alors, comment GraphQL a-t-il commencé ? À quoi ressemble-t-il en pratique ? Et comment commencez-vous à l'utiliser ? Lisez la suite pour le découvrir !

![Image](https://cdn-media-1.freecodecamp.org/images/RzLJNwUM01VeOhjAN9UJAMlkQkKduJlrYyNr)

### Le Problème

GraphQL a vu le jour chez Facebook, mais même des applications beaucoup plus simples peuvent souvent rencontrer les limitations des API REST traditionnelles.

Par exemple, imaginez que vous devez afficher une liste de `posts`, et sous chaque post une liste de `likes`, incluant les noms d'utilisateurs et les avatars. Facile, vous modifiez votre API `posts` pour inclure un tableau `likes` contenant des objets utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/kc0xvmMmSaF46CcliELfM8B78hev9NT3QkDG)

Mais maintenant, il est temps de travailler sur votre application mobile, et il s'avère que le chargement de toutes ces données supplémentaires ralentit les choses. Vous avez donc maintenant besoin de _deux_ endpoints, un avec les `likes` et un sans.

Ajoutez un autre facteur à l'équation : il s'avère que bien que les `posts` soient stockés dans une base de données MySQL, les `likes` vivent dans un stockage Redis ! Que faites-vous maintenant ?!

Extrapolez ce scénario au nombre de sources de données et de clients API que Facebook doit gérer, et vous pouvez imaginer pourquoi les bonnes vieilles API REST commençaient à montrer leurs limites.

### La Solution

La solution que Facebook a trouvée est conceptuellement très simple : au lieu d'avoir plusieurs endpoints "stupides", avoir un seul endpoint "intelligent" qui peut prendre des requêtes complexes, puis masser la sortie des données dans la forme requise par le client.

En pratique, la couche GraphQL vit entre le client et une ou plusieurs sources de données, recevant les requêtes des clients et récupérant les données nécessaires selon vos instructions. Confus ? C'est l'heure de la métaphore !

L'ancien modèle REST est comme commander une pizza, puis faire livrer des courses, puis appeler votre pressing pour récupérer vos vêtements. Trois magasins, trois appels téléphoniques.

![Image](https://cdn-media-1.freecodecamp.org/images/Jj8EGashABUL26TOVeyh9Iy0Djx5IfKzJxAg)

GraphQL, en revanche, est comme avoir un assistant personnel : une fois que vous lui avez donné les adresses des trois endroits, vous pouvez simplement demander ce que vous voulez ("récupérez mon pressing, une grande pizza et deux douzaines d'œufs") et attendre qu'ils reviennent.

![Image](https://cdn-media-1.freecodecamp.org/images/K3n2ahghSoTRyLCWWxaSrBwxD11V07Nbx8Or)

En d'autres termes, GraphQL établit un langage standard pour parler à cet assistant personnel magique.

![Image](https://cdn-media-1.freecodecamp.org/images/PnWpUZBgc8W3xiqxR1bxxG4qsUglQ3nubk1a)
_Selon Google Images, l'assistant personnel typique est un alien à huit bras_

![Image](https://cdn-media-1.freecodecamp.org/images/4aw3Yit4eTTop1QE4iHXrUzaM9rZlDG8BrSA)

En pratique, une API GraphQL est organisée autour de trois blocs de construction principaux : le **schéma**, les **requêtes** et les **résolveurs**.

### Requêtes

La demande que vous faites à votre assistant personnel GraphQL est la **requête**, et elle ressemble à quelque chose comme ceci :

```
query {  stuff}
```

Nous déclarons une nouvelle requête en utilisant le mot-clé `query`, puis nous demandons un champ nommé `stuff`. Le grand avantage des requêtes GraphQL est qu'elles supportent les champs imbriqués, donc nous pouvons aller un niveau plus profond :

```
query {  stuff {    eggs    shirt    pizza  }}
```

Comme vous pouvez le voir, le client qui fait la requête n'a pas besoin de se soucier de quel "magasin" proviennent les données. Demandez simplement ce dont vous avez besoin, et laissez le serveur GraphQL s'occuper du reste.

Il est bon de noter que les champs de requête peuvent également pointer vers des **tableaux**. Par exemple, voici un motif courant lors de la requête pour une liste de posts :

```
query {  posts { # ceci est un tableau    title    body    author { # nous pouvons aller plus profond !      name      avatarUrl      profileUrl    }  }}
```

Les champs de requête supportent également les **arguments**. Si je veux afficher un post spécifique, je peux ajouter un argument `id` au champ `post` :

```
query {  post(id: "123foo"){    title    body    author{      name      avatarUrl      profileUrl    }  }}
```

Enfin, si je veux rendre cet argument `id` dynamique, je peux définir une **variable** et ensuite la réutiliser à l'intérieur de la requête (notez que nous **nommons** également la requête ici) :

```
query getMyPost($id: String) {  post(id: $id){    title    body    author{      name      avatarUrl      profileUrl    }  }}
```

Une bonne façon de mettre tout cela en pratique est d'utiliser [l'explorateur d'API GraphQL de GitHub](https://developer.github.com/early-access/graphql/explorer/). Par exemple, essayez la requête suivante :

```
query {  repository(owner: "graphql", name: "graphql-js"){    name    description  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/iKec132Qlhsc6lSTQJwWgxJEZCrYHCiJK4D5)
_L'autocomplétion GraphQL en action_

Remarquez que lorsque vous essayez de taper un nouveau nom de champ sous `description`, l'IDE proposera automatiquement des noms de champs possibles directement autocomplétés à partir de l'API GraphQL elle-même. Sympa !

![Image](https://cdn-media-1.freecodecamp.org/images/kwrsuL3NrieP9GUyeZe0BNdXNQfQJ-GP4txK)
_[L'Anatomie d'une Requête GraphQL](https://dev-blog.apollodata.com/the-anatomy-of-a-graphql-query-6dffa9e9e747" rel="noopener" target="_blank" title=")_

Vous pouvez en apprendre plus sur les requêtes GraphQL dans l'excellent article [Anatomie d'une Requête GraphQL](https://dev-blog.apollodata.com/the-anatomy-of-a-graphql-query-6dffa9e9e747).

### Résolveurs

Même le meilleur assistant personnel du monde ne peut pas aller chercher votre pressing si vous ne lui donnez pas une adresse.

De même, votre serveur GraphQL ne saura pas quoi faire avec une requête entrante à moins que vous ne le lui disiez en utilisant un **résolveur**.

Un résolveur indique à GraphQL comment et où récupérer les données correspondant à un champ donné. Par exemple, voici à quoi pourrait ressembler un résolveur pour le champ `post` ci-dessus (en utilisant le générateur de schéma [GraphQL-Tools](https://github.com/apollographql/graphql-tools) d'Apollo) :

```
Query: {  post(root, args) {    return Posts.find({ id: args.id });  }}
```

Nous mettons le résolveur sur `Query` parce que nous voulons interroger `post` directement au niveau racine. Mais vous pouvez également avoir des résolveurs pour les sous-champs, comme le champ `author` d'un `post` :

```
Query: {  post(root, args) {    return Posts.find({ id: args.id });  }},Post: {  author(post) {    return Users.find({ id: post.authorId})  }}
```

Et notez que vos résolveurs ne sont pas limités à retourner des documents de base de données. Par exemple, peut-être que vous voulez ajouter un `commentsCount` à votre type `Post` :

```
Post: {  author(post) {    return Users.find({ id: post.authorId})  },  commentsCount(post) {    return Comments.find({ postId: post.id}).count()   }}
```

Le concept clé à comprendre ici est qu'avec GraphQL, **votre schéma d'API et vos schémas de base de données sont découplés**. En d'autres termes, il n'y a peut-être pas de champs `author` et `commentsCount` dans notre base de données, mais nous pouvons les "simuler" grâce au pouvoir des résolveurs.

Comme vous l'avez vu, vous pouvez écrire n'importe quel code que vous voulez à l'intérieur d'un résolveur. C'est pourquoi vous pouvez également les faire _modifier_ le contenu de votre base de données, auquel cas ils sont connus sous le nom de résolveurs de **mutation**.

### Schéma

Toutes ces bonnes choses sont rendues possibles par le système de schéma typé de GraphQL. Mon objectif aujourd'hui est de vous donner un aperçu rapide plutôt qu'une introduction exhaustive, donc je ne vais pas entrer dans les détails ici.

Cela dit, je vous encourage à consulter la [documentation GraphQL](http://graphql.org/learn/schema/) si vous souhaitez en apprendre plus.

![Image](https://cdn-media-1.freecodecamp.org/images/RMHITVVG5FpGHiQ0qrxA9d0T3fdmyiUVK-Qk)

### Questions Fréquentes

Faisons une pause pour répondre à quelques questions courantes.

Vous là-bas, au fond. Oui, vous. Je vois que vous voulez demander quelque chose. Allez-y, ne soyez pas timide !

#### Quelle est la relation entre GraphQL et les bases de données de graphes ?

Pas grand-chose, en réalité, GraphQL n'a rien à voir avec les bases de données de graphes comme [Neo4j](https://en.wikipedia.org/wiki/Neo4j). La partie "graph" vient de l'idée de parcourir votre graphe d'API en utilisant des champs et des sous-champs ; tandis que "QL" signifie "langage de requête".

#### Je suis parfaitement heureux avec REST, pourquoi devrais-je passer à GraphQL ?

Si vous n'avez pas encore rencontré les points de douleur de REST que GraphQL est censé résoudre, alors je dirais que c'est une bonne chose !

Utiliser GraphQL au lieu de REST n'affectera probablement pas l'expérience utilisateur globale de votre application, donc le passage à GraphQL n'est en aucun cas une question de vie ou de mort. Cela dit, je recommande définitivement d'essayer GraphQL sur un petit projet annexe si vous en avez l'occasion.

#### Puis-je utiliser GraphQL sans React/Relay/*insérer une bibliothèque ici* ?

Oui, vous pouvez ! Puisque GraphQL est juste une spécification, vous pouvez l'utiliser avec n'importe quelle bibliothèque sur n'importe quelle plateforme, soit avec un client (par exemple, [Apollo](http://dev.apollodata.com/) a des clients GraphQL pour le web, iOS, Angular, etc.) ou en faisant vos propres appels à un serveur GraphQL.

#### GraphQL a été créé par Facebook, et je ne fais pas confiance à Facebook

Encore une fois, GraphQL est une spécification, ce qui signifie que vous pouvez utiliser des implémentations GraphQL sans exécuter une seule ligne de code écrite par Facebook.

Et bien que le soutien de Facebook soit définitivement un plus pour l'écosystème GraphQL, à ce stade, je crois que la communauté est suffisamment grande pour que GraphQL prospère même si Facebook devait arrêter de l'utiliser.

#### Cette histoire de "laisser le client demander les données dont il a besoin" ne me semble pas très sécurisée...

Puisque vous écrivez vos propres résolveurs, c'est à vous de traiter les préoccupations de sécurité à ce niveau.

Par exemple, si vous laissez le client spécifier un paramètre `limit` pour contrôler le nombre de documents qu'il reçoit, vous voudrez probablement limiter ce nombre pour éviter les attaques de type déni de service où les clients demandent des millions de documents encore et encore.

#### Alors, qu'ai-je besoin pour commencer ?

De manière générale, vous aurez besoin d'au moins deux composants pour exécuter une application alimentée par GraphQL :

* Un **serveur GraphQL** qui sert votre API.
* Un **client GraphQL** qui se connecte à votre endpoint.

Lisez la suite pour en apprendre plus sur les différentes options disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/dBStLo2QwiEcyXJqXKSUz2uJsHQAqEQXvhDU)

Maintenant que vous avez une idée assez claire de comment fonctionne GraphQL, parlons de quelques-uns des principaux acteurs dans ce domaine.

### Serveurs GraphQL

La première brique dont vous aurez besoin est un serveur GraphQL. [GraphQL lui-même](http://graphql.org/) n'est après tout qu'une spécification, ce qui laisse la porte ouverte à quelques implémentations concurrentes.

#### [GraphQL-JS](https://github.com/graphql/graphql-js) (Node)

C'est l'implémentation de référence originale de GraphQL. Vous pouvez l'utiliser avec [express-graphql](https://github.com/graphql/express-graphql) pour [créer votre serveur API](http://graphql.org/graphql-js/running-an-express-graphql-server/).

#### [GraphQL-Server](http://dev.apollodata.com/tools/graphql-server/) (Node)

L'équipe [Apollo](http://apollostack.com) a également sa propre implémentation tout-en-un de serveur GraphQL. Elle n'est pas aussi répandue que l'originale, mais elle est très bien documentée et supportée et gagne rapidement du terrain.

#### [Autres Plateformes](http://graphql.org/code/)

GraphQL.org a une [liste des implémentations GraphQL pour diverses autres plateformes](http://graphql.org/code/) (PHP, Ruby, etc.).

### Clients GraphQL

Bien que vous puissiez techniquement interroger votre API GraphQL directement sans avoir besoin d'une bibliothèque cliente dédiée, cela peut [définiment faciliter votre vie](https://dev-blog.apollodata.com/why-you-might-want-a-graphql-client-e864050f789c).

#### [Relay](https://facebook.github.io/relay/)

Relay est la boîte à outils GraphQL de Facebook. Je ne l'ai pas utilisé moi-même, mais d'après ce que j'ai entendu, il est principalement adapté aux besoins de Facebook et pourrait être un peu sur-ingénierisé pour la plupart des usages.

#### [Apollo Client](http://www.apollodata.com/)

Le nouveau venu dans ce domaine est [Apollo](http://apollostack.com), et il prend rapidement le dessus. La pile cliente Apollo typique est composée de deux briques :

* [Apollo-client](http://dev.apollodata.com/core/), qui vous permet d'exécuter des requêtes GraphQL dans le navigateur et de stocker leurs données (et qui a également sa propre [extension devtools](https://github.com/apollographql/apollo-client-devtools)).
* Un connecteur pour votre framework front-end de choix ([React-Apollo](http://dev.apollodata.com/react/), [Angular-Apollo](http://dev.apollodata.com/angular2/), etc.).

Notez que par défaut, Apollo-client stocke ses données en utilisant [Redux](http://redux.js.org), ce qui est génial puisque Redux est lui-même une bibliothèque de gestion d'état assez établie avec un écosystème riche.

![Image](https://cdn-media-1.freecodecamp.org/images/HRIep360VD0BwGBCpC23STDXeGAfotCuokDs)
_L'extension Chrome Apollo Devtools_

### Applications Open-Source

Bien que GraphQL soit relativement nouveau, il existe déjà quelques applications open-source prometteuses qui l'utilisent.

#### [VulcanJS](http://vulcanjs.org)

![Image](https://cdn-media-1.freecodecamp.org/images/5RiqXqZK1VwKGS3XLJQRoSfNdBwFQBBSrfOa)

Tout d'abord, un avertissement : je suis le responsable principal de [VulcanJS](http://vulcanjs.org). J'ai créé VulcanJS pour permettre aux gens de tirer parti de la puissance de la pile React/GraphQL sans avoir à écrire autant de code boilerplate. Vous pouvez le considérer comme "Rails pour l'écosystème web moderne", en ce sens qu'il vous permet de construire des applications CRUD (comme un [clone d'Instagram](https://www.youtube.com/watch?v=qibyA_ReqEQ)) en quelques heures.

#### [Gatsby](https://www.gatsbyjs.org/docs/)

Gatsby est un générateur de site statique React, qui est maintenant alimenté par GraphQL à partir de la [version 1.0](https://www.gatsbyjs.org/docs/). Bien que cela puisse sembler une combinaison étrange au premier abord, c'est en fait assez puissant. Pendant son processus de construction, Gatsby peut récupérer des données à partir de plusieurs API GraphQL, puis les utiliser pour créer une application React entièrement statique côté client.

### Autres Outils GraphQL

#### [GraphiQL](https://github.com/graphql/graphiql)

GraphiQL est un IDE très pratique dans le navigateur pour interroger les endpoints GraphQL.

![Image](https://cdn-media-1.freecodecamp.org/images/l09mSYV5JFlBO6a6ju7U9bgX3ps0gzx-Zz7L)
_GraphiQL_

#### [DataLoader](https://github.com/facebook/dataloader)

En raison de la nature imbriquée des requêtes GraphQL, une seule requête peut facilement déclencher des dizaines d'appels de base de données. Pour éviter de subir une perte de performance, vous pouvez utiliser une bibliothèque de regroupement et de mise en cache telle que DataLoader, développée par Facebook.

#### [Create GraphQL Server](https://blog.hichroma.com/create-graphql-server-instantly-scaffold-a-graphql-server-1ebad1e71840)

Create GraphQL Server est un utilitaire de ligne de commande qui facilite la création rapide d'un serveur GraphQL alimenté par un serveur Node et une base de données Mongo.

#### [GraphQL-up](https://www.graph.cool/graphql-up/)

Similaire à Create GraphQL Server, GraphQL-up vous permet de démarrer rapidement un nouveau backend GraphQL alimenté par le service [GraphCool](https://www.graph.cool).

### Services GraphQL

Enfin, il existe également un certain nombre d'entreprises "GraphQL-backend-as-a-service" qui s'occupent de tout le côté serveur pour vous, et qui pourraient être un bon moyen de tremper vos orteils dans l'écosystème GraphQL.

#### [Graphcool](http://graph.cool)

Une plateforme backend flexible combinant GraphQL et AWS Lambda, avec un plan développeur gratuit.

#### [Scaphold](https://scaphold.io/)

Un autre backend GraphQL en tant que service, qui offre également un plan gratuit. Il propose beaucoup des mêmes fonctionnalités que Graphcool.

![Image](https://cdn-media-1.freecodecamp.org/images/TO42Efs9IjxfDA3DOnUAz93mvKcPDL2kvOC-)

Il existe déjà plusieurs endroits où vous pouvez vous perfectionner en GraphQL.

#### [GraphQL.org](http://graphql.org/learn/)

Le site officiel GraphQL propose une excellente documentation pour vous aider à démarrer.

#### [LearnGraphQL](https://learngraphql.com/)

LearnGraphQL est un cours interactif mis en place par les gens de [Kadira](https://kadira.io/).

#### [LearnApollo](https://www.learnapollo.com/)

Un bon suivi de LearnGraphQL, LearnApollo est un cours gratuit réalisé par Graphcool.

#### [Le Blog Apollo](https://dev-blog.apollodata.com/)

Le blog Apollo propose de nombreux articles détaillés et bien écrits sur Apollo et GraphQL en général.

#### [GraphQL Weekly](https://graphqlweekly.com/)

Une newsletter sur tout ce qui concerne GraphQL, curatée par l'équipe Graphcool.

#### [Hashbang Weekly](http://hashbangweekly.okgrow.com/)

Une autre excellente newsletter, qui couvre également React et Meteor en plus de GraphQL.

#### [Freecom](https://www.graph.cool/freecom/)

Une série de tutoriels qui vous apprend à construire un clone d'Intercom en utilisant GraphQL.

#### [Awesome GraphQL](https://github.com/chentsulin/awesome-graphql)

Une liste assez exhaustive de liens et de ressources GraphQL.

![Image](https://cdn-media-1.freecodecamp.org/images/el3ur1jGys-NxfG08AMUMLwVp1AC2Z63etwT)

Alors, comment mettre en pratique vos nouvelles connaissances GraphQL ? Voici quelques recettes que vous pouvez essayer :

#### [Apollo + Graphcool + Next.js](https://github.com/zeit/next.js/tree/master/examples/with-apollo)

Si vous êtes déjà familiarisé avec Next.js et React, [cet exemple](https://github.com/zeit/next.js/tree/master/examples/with-apollo) vous permettra de configurer votre endpoint GraphQL en utilisant Graphcool, puis de l'interroger en utilisant Apollo.

#### [VulcanJS](http://docs.vulcanjs.org/)

Le [tutoriel Vulcan](http://docs.vulcanjs.org/) vous guidera à travers la configuration d'une simple couche de données GraphQL, à la fois sur le serveur et le client. Puisque Vulcan est une plateforme tout-en-un, c'est un bon moyen de commencer sans aucune configuration. Si vous avez besoin d'aide, n'hésitez pas à [passer par notre canal Slack](http://slack.vulcanjs.org/) !

#### [Tutoriel GraphQL & React](https://blog.hichroma.com/graphql-react-tutorial-part-1-6-d0691af25858#.o54ygcruh)

Le blog Chroma propose un [tutoriel en six parties](https://blog.hichroma.com/graphql-react-tutorial-part-1-6-d0691af25858#.o54ygcruh) sur la construction d'une application React/GraphQL en suivant une approche de développement pilotée par les composants.

![Image](https://cdn-media-1.freecodecamp.org/images/oSC8hmAc-NEMrjM7qJf4xnRRVvuCYLn9kiv8)

### Conclusion

GraphQL peut sembler complexe au premier abord car c'est une technologie qui touche à de nombreux domaines du développement moderne. Mais si vous prenez le temps de comprendre les concepts sous-jacents, je pense que vous découvrirez que beaucoup de choses ont du sens.

Que vous finissiez par l'utiliser ou non, je crois qu'il vaut la peine de prendre le temps de vous familiariser avec GraphQL. De plus en plus d'entreprises et de frameworks l'adoptent, et il pourrait très bien finir par devenir l'un des blocs de construction clés du web au cours des prochaines années.

D'accord ? Pas d'accord ? Des questions ? Faites-le moi savoir ici dans les commentaires. Et si vous avez apprécié cet article, envisagez de le ? et de le partager !