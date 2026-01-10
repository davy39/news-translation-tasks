---
title: Comment construire un serveur GraphQL complet avec Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-12T05:07:07.000Z'
originalURL: https://freecodecamp.org/news/graphql-zero-to-production-a7c4f786a57b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IZcJKz3761vChU1VFHfzkw.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment construire un serveur GraphQL complet avec Node.js
seo_desc: 'By Jack R. Scott

  So, you’re probably thinking — is this just another hullabaloo GraphQL tutorial
  that is just going to say a lot of big words but not actually help me implement
  anything?

  ✋ The answer is no.

  After reading many guides on how to build a...'
---

Par Jack R. Scott

Alors, vous vous dites probablement — est-ce juste un autre tutoriel GraphQL qui va utiliser beaucoup de grands mots mais ne va pas vraiment m'aider à implémenter quoi que ce soit ?

**✍️ La réponse est non.**

Après avoir lu de nombreux guides sur la façon de construire un serveur GraphQL, j'ai réalisé qu'aucun d'eux ne m'a complètement amené là où je voulais être. Quelle frustration.

Cela m'a pris beaucoup plus de temps que prévu pour être opérationnel.

Ainsi, je suis déterminé à vous donner un tutoriel qui va vraiment au-delà des bases et donne quelques idées sur la façon d'implémenter un serveur dans le monde réel. Ainsi, tout le monde peut profiter de la véritable belle sensation d'utiliser GraphQL.

**❓ Comment savez-vous que c'est légitime ?**

[Voici une version fonctionnelle](https://github.com/jackrobertscott/graphql-api-demo) de tout le code expliqué dans ce tutoriel. Allez-y, clonez-le et essayez-le. J'inclurai également un autre lien vers le dépôt à la fin de ce tutoriel. N'hésitez pas à faire des pull requests ou à starer le dépôt afin que nous puissions le rendre aussi bon que possible !

**❓ Note à part.**

GraphQL est super flexible. Il peut être implémenté d'un million de façons différentes — d'où toute cette confusion. Chacun a sa propre opinion et méthode pour construire des applications. C'est la mienne. Si vous avez des commentaires constructifs que je peux utiliser pour améliorer ce tutoriel — partagez-les !

D'accord, commençons !

### Un peu de contexte ❓

Avant de commencer, il est probablement bon de donner un peu de contexte pour les personnes qui ne savent pas déjà. GraphQL a été créé en 2012 par Facebook (merci encore). Il a été développé comme une alternative à la norme REST existante pour structurer les requêtes serveur.

**❓ Qu'est-ce que REST ?**

C'est cette chose que vous obtenez lorsque vous allez dormir... Attrapé !

![Image](https://cdn-media-1.freecodecamp.org/images/1*gIVNrG1C7dHjH9866IFJyw.jpeg)
_Pourquoi cet humain pense-t-il qu'il est drôle ?_

Honêtement, je veux garder cet article aussi succinct que possible. Donc pour aider à expliquer, voici un [lien utile](https://www.codecademy.com/articles/what-is-rest) vers un article qui explique le concept REST. La raison pour laquelle Facebook a créé GraphQL comme alternative était que la norme REST avait quelques problèmes clés :

1. Récupérer des objets complexes nécessite plusieurs appels au serveur — lent.
2. Vous obtenez plus que ce que vous demandez. REST spécifie généralement la forme des données sur le serveur. Par conséquent, vous obtenez un tas de données que vous n'utilisez même pas.
3. Il faut beaucoup de travail pour comprendre exactement quelles informations vous obtenez du serveur — pas très prévisible.

À l'époque, Facebook avait une tonne de développeurs passionnés qui aiment tester de nouveaux concepts. Donc ils en ont fait commencer à travailler sur un nouveau concept qui est devenu plus tard GraphQL. Ils voulaient demander à leurs serveurs exactement ce qu'ils voulaient et savoir qu'ils obtiendraient exactement cela en retour. Pas de superflu. ✨

Donc... ils ont créé un nouveau langage conçu spécifiquement pour les requêtes serveur. C'est pourquoi GraphQL est décrit comme « [Un langage de requête pour votre API](https://graphql.org/) ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*aIejg1WlHOhUngmLsILnjQ.png)

Le schéma ci-dessus est un exemple de requête GraphQL, ainsi qu'un exemple de réponse JSON. Je pourrais décrire ce qui se passe... mais c'est assez explicite.

Je ne vais pas aller beaucoup plus loin dans « qu'est-ce que GraphQL » car il y a beaucoup d'excellents articles sur ce sujet. Cependant, si vous souhaitez plus d'informations, [voici un article incroyable](https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf) qui vous donne un excellent aperçu des concepts et des fondamentaux de GraphQL.

Passons à la suite !

### Donnez-moi le code ! ❓✨

D'accord, d'accord... Vous êtes exigeant... Je passe au code. Mais avant de commencer, nous allons devoir [créer un nouveau dépôt Node.js](https://codeburst.io/getting-started-with-node-js-a-beginners-guide-b03e25bca71b) et installer quelques dépendances NPM.

💡 Astuce : consultez [Parcel.js](https://parceljs.org/) pour un bundler d'application génial qui vous aide à configurer votre environnement de développement en quelques secondes (assurez-vous de définir votre cible sur l'environnement `node`). [Parcel](https://parceljs.org/) est utilisé par [CodeSandbox](https://codesandbox.io/).

P.s. : Je suppose que vous savez déjà comment configurer un dépôt Node.js. Si ce n'est pas le cas, les concepts de cet article peuvent être un peu complexes pour vous. Vous pouvez toujours suivre pour obtenir une compréhension générale.

Nos dépendances NPM :

1. [apollo-server](https://www.npmjs.com/package/apollo-server)
2. [mongoose](https://www.npmjs.com/package/mongoose)
3. [graphql-tools](https://www.npmjs.com/package/graphql-tools)

**Attendez... ❓ qui est Apollo et pourquoi voulons-nous son serveur ?**

Pour être clair, Apollo n'est pas une personne. C'est un [groupe de développeurs de pointe](https://www.apollographql.com/) qui font des progrès incroyables dans le domaine de GraphQL. Ils ont créé un ensemble d'outils et de code prêts pour la production qui va rendre nos vies super faciles pour commencer à configurer nos serveurs GraphQL.

Super, maintenant que nos dépendances sont installées, commençons par créer un fichier index comme point d'entrée de notre application.

📄 Fichier : `src/index.ts`

J'ai ajouté un certain nombre de commentaires dans le code qui aideront à expliquer ce qui se passe dans le fichier. Essentiellement, nous avons créé un serveur et donné au serveur un schéma qui contient un type « vide » pour nos Requêtes (`type Query`) et un type « vide » pour nos Mutations (`type Mutation`).

* Vide signifie qu'il n'a pas de propriétés (pour l'instant).

Comme je l'ai dit avant, je veux m'assurer que cet article est aussi succinct que possible. Je suppose que vous êtes un peu familier avec l'écriture de schémas GraphQL de base. Mais si vous ne savez pas, [voici un lien sur le fonctionnement des schémas de base](http://graphql.github.io/learn/schema/#the-query-and-mutation-types).

Ensuite, nous allons configurer une table de base de données pour nos utilisateurs en utilisant mongoose. Nos utilisateurs auront quelques propriétés de base que nous pourrons utiliser pour les interroger plus tard.

📄 Fichier : `src/common/users/user.model.ts`

Dans le fichier ci-dessus, nous créons un modèle d'utilisateur en utilisant mongoose. Si vous n'êtes pas familier avec [mongoose](https://mongoosejs.com/), c'est un wrapper élégant que vous pouvez utiliser pour valider vos données lorsqu'elles sont insérées dans votre base de données. Il nous donne également des pouvoirs incroyables comme les propriétés virtuelles, l'interrogation facile des données, et plus encore.

Maintenant, nous avons un modèle que nous pouvons utiliser pour sauvegarder et demander des données à notre base de données, ainsi qu'un serveur qui exécute un serveur GraphQL vide. Tout ce que nous avons à faire est de connecter les deux ensemble !

![Image](https://cdn-media-1.freecodecamp.org/images/1*tHAnZewCOhGiUlQ2Bm4J1Q.jpeg)

Pour ce faire, nous allons créer un fichier qui contiendra 2 choses :

1. Un ensemble de types GraphQL — qui indique au client « quelles » données nous avons.
2. Un ensemble correspondant de fonctions de résolution GraphQL — qui indique au serveur « comment » faire les choses que nos types décrivent.

Je garde ces deux sections de code dans le même fichier car cela a facilité la vie lors du développement.

📄 Fichier : `src/common/users/user.schema.ts`

Oh là là ! C'est beaucoup à assimiler... Alors décomposons cela, en commençant par nos définitions de types :

* `type User { ... }` : c'est un type GraphQL simple. Cela nous indique simplement la forme de l'utilisateur afin que le client puisse l'interroger correctement. Vous pouvez trouver plus d'informations [ici dans la documentation](https://graphql.org/learn/schema/).
* `input UserFilterInput { ... }` : similaire à un objet « type », une entrée définit la structure d'un paramètre complexe, c'est-à-dire quelque chose de plus complexe qu'une `String`, `ID`, `Int`, `Float` ou `Boolean`.
* `extend type Query { ... }` : vous vous souvenez lorsque nous avons créé notre type de requête racine dans le fichier index ? Eh bien, cela s'y réfère. Nous étendons cette requête racine et définissons la fonctionnalité que nous voulons exposer à notre client. **Pourquoi faisons-nous cela ?** Pfff... Ce n'est pas comme si je voulais le faire de cette manière (c'est un peu bidouillé)... Malheureusement, c'était la meilleure façon de le faire parmi un certain nombre de mauvaises alternatives. N'hésitez pas à me donner une meilleure suggestion.
* `extend type Mutation { ... }` : de la même manière que nous étendons la requête racine, nous étendons également la mutation racine.

Maintenant, analysons ce qui se passe dans nos résolveurs d'utilisateurs :

* Les noms de nos fonctions de résolution correspondent aux noms des champs dans les `Query` et les `Mutation` dans les définitions de types. Cela aide Apollo à savoir quelles fonctions font quoi.
* `users: async (_, { filter = {} }) => { ..`. }` : Eh bien, cette ligne est un peu difficile à comprendre pour les développeurs qui ne l'ont jamais vue auparavant. Ne vous inquiétez pas, elle indique simplement que pour la propriété `users`, nous attribuons [une fonction anonyme](https://en.wikibooks.org/wiki/JavaScript/Anonymous_functions) qui utilise [async / await](https://javascript.info/async-await) pour interroger la base de données et retourner des utilisateurs. Simple, non ? Les arguments de la fonction correspondent aux arguments dans [la documentation du serveur Apollo que vous pouvez trouver ici](https://www.apollographql.com/docs/apollo-server/essentials/data.html).
* `await User.something()` : Cette syntaxe est la manière dont nous utilisons mongoose pour obtenir ou sauvegarder des données dans la base de données. C'est super simple une fois que vous avez compris, vous pouvez trouver [la documentation sur mongoose ici](https://mongoosejs.com/docs/index.html).
* `user.toGraph()` : C'est là que la plupart des gens seront confus. Cette fonction « toGraph » provient de notre fichier de modèle mongoose (trouvez-la dans le fichier de modèle où il est écrit `userSchema.method('toGraph', ...`). La raison pour laquelle nous avons besoin de cette fonction est que Mongoose ne retourne pas un simple objet JavaScript. Plutôt, il retourne un objet complexe avec certaines propriétés aléatoires que GraphQL n'aime pas. Ainsi, en utilisant la méthode `toGraph`, nous convertissons l'objet complexe en un objet simple que GraphQL peut traiter.

**❓ Wowzers ! C'était une surcharge cérébrale.**

Ne vous inquiétez pas si vous ne comprenez pas tout le code tout de suite. Vous pourrez cloner et expérimenter avec le [dépôt d'exemple](https://github.com/jackrobertscott/graphql-api-demo) sur votre ordinateur une fois que vous aurez terminé le tutoriel.

D'accord ! Maintenant, rassemblons tout cela dans le fichier index...

📄 Fichier : `src/index.ts`

Tout ce que nous avions à faire était d'importer nos définitions de types et nos résolveurs, puis nous les avons ajoutés à notre schéma. Si vous allez et démarrez votre application (espérons que vous aurez configuré un script de démarrage, par exemple `npm start`), vous devriez voir que votre application s'ouvrira sur [http://localhost:4000](http://localhost:4000).

**Dépannage :** n'oubliez pas d'installer et de démarrer votre base de données MongoDB. [Voici un lien vers un article](https://www.codecademy.com/articles/tdd-setup-mongodb-2) qui vous montre comment faire cela, si vous ne l'avez pas déjà fait.

Lorsque nous naviguons vers le serveur dans notre navigateur, nous voyons qu'Apollo nous a donné un petit outil utile appelé playground. Nous pouvons l'utiliser pour tester notre serveur GraphQL. Ci-dessous, un exemple de quelques requêtes que j'ai testées sur notre API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTEJESaA__GF8GJKoBv-rA.png)

> Vous vous demandez peut-être : que signifie `query GetAllUsers` ou `mutation AddUser` ?

Ne vous inquiétez pas, cela est purement là pour vous aider à déboguer votre application. Ce sont juste des noms par lesquels vous pouvez identifier vos requêtes GraphQL. Ils n'ajoutent aucune fonctionnalité supplémentaire à la requête ou à la mutation. Vous pouvez trouver plus d'informations sur [comment écrire des requêtes et des mutations ici](https://graphql.org/learn/queries/).

**❓ Hé [Jack](https://twitter.com/jacrobsco), il y a encore une chose dont je ne suis pas sûr. Quelle est la différence entre les Requêtes et les Mutations ?**

Excellente question ! J'avais un pressentiment que vous alliez demander. Pour vraiment comprendre cela, nous devons examiner ce qui se passe sous le capot de notre serveur. Beaucoup de gens suggèrent que les Requêtes sont l'équivalent d'une requête `GET`. Les Mutations sont pour toutes les autres, c'est-à-dire `POST`, `PUT`, `PATCH` et `DELETE`, mais ce n'est pas exactement vrai.

Examinons un exemple de 2 requêtes à notre serveur GraphQL à partir de notre playground Apollo GraphQL — qui vient avec Apollo Server directement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*60TibCKmU8VJo8-DZnUh9Q.png)

Comme vous pouvez le voir, les requêtes `query` et `mutation` sont toutes deux des requêtes `POST`. La raison en est qu'elles ont toutes deux la capacité de passer des variables dans leurs requêtes, par exemple `users (limit: $maxUsers) { ... }`.

La vraie différence entre les deux est que :

1. Les Requêtes sont exécutées en parallèle.
2. Les Mutations sont exécutées en série.

Ainsi, les requêtes peuvent être exécutées rapidement et les mutations peuvent être exécutées de manière fiable. Merci à [Prisma](https://www.prisma.io/blog/experimental-graphql-106b07424435/) pour l'aide sur ce point.

### ⏰ Il est temps de passer à un niveau supérieur !

Donc, nous avons fait un assez bon travail jusqu'à présent, nous savons comment :

* ✅ Créer un serveur de base.
* ✅ Créer un schéma mongoose qui valide nos données de base de données.
* ✅ Définir notre structure de données GraphQL sur le serveur en utilisant des définitions de types.
* ✅ Connecter notre schéma mongoose au serveur GraphQL en utilisant des résolveurs.
* ✅ Faire quelques requêtes et mutations via le playground Apollo.

Je dirais que c'est une bonne part de la bouteille de sauce — Kevin '07. Mais il manque encore quelques choses...

**❓ Et si nous avons des éléments de base de données liés, comment gérons-nous cela ?**

C'est en fait assez simple, faisons-le !

Tout d'abord, nous allons prétendre que chaque utilisateur est lié/attaché à un seul espace de travail. Dans cette situation, nous pourrions vouloir demander des informations de l'espace de travail lié à l'utilisateur, au même moment où nous demandons des informations sur cet utilisateur.

Pour ce faire, nous devons d'abord définir un nouveau modèle mongoose. Nous l'utiliserons pour sauvegarder et demander des espaces de travail à la base de données.

📄 Fichier : `src/common/workspace/workspace.model.ts`

De manière similaire à la façon dont nous avons créé nos utilisateurs, nous allons également créer un fichier de schéma pour nos espaces de travail afin qu'ils puissent être interrogés indépendamment.

📄 Fichier : `src/common/workspace/workspace.schema.ts`

Super, maintenant nous devons simplement mettre à jour le fichier index pour qu'il reconnaisse notre schéma et nos résolveurs GraphQL d'espace de travail. Note : pour fusionner les résolveurs, nous devons utiliser la fonction `merge` de lodash qui fusionne profondément deux objets ensemble.

📄 Fichier : `src/index.ts`

Une fois que vous avez implémenté le code ci-dessus, vous pourrez créer et interroger des espaces de travail tout comme nous l'avons fait avec nos utilisateurs ! Mais ce n'est pas beaucoup plus cool qu'avant. Ce qui sera vraiment cool, c'est lorsque nous interrogerons des données sur un espace de travail « à travers » l'objet utilisateur.

Pour ce faire, nous pouvons utiliser une fonctionnalité cool de mongoose qui nous permet de référencer des éléments de base de données les uns aux autres (par exemple, l'espace de travail à l'utilisateur). Ces références sont stockées sous forme de types `ObjectId` spéciaux. Allez-y et mettez à jour notre modèle d'utilisateur pour qu'il puisse sauvegarder l'ID d'un espace de travail pour nos utilisateurs.

📄 Fichier : `src/common/user/user.model.ts`

Enfin, nous devons mettre à jour notre fichier de schéma d'utilisateur pour qu'Apollo sache comment résoudre notre référence (imbriquée) à l'espace de travail de l'utilisateur.

📄 Fichier : `src/common/user/user.schema.ts`

Examinons les 2 principaux changements que nous venons d'apporter dans le fichier de schéma d'utilisateur :

1. Le `type User` a maintenant 2 propriétés supplémentaires : `workspaceId` (qui correspond au modèle Mongoose) et `workspace` (qui sera l'endroit où nous mettrons l'objet espace de travail lorsque nous l'interrogerons).
2. Il y a maintenant une propriété appelée `User` dans nos résolveurs. C'est l'une de mes parties préférées de GraphQL car elle vous permet de résoudre des propriétés individuelles d'un type. Dans l'exemple ci-dessus, nous résolvons la propriété `workspace` en prenant le workspaceId de l'utilisateur puis en utilisant Mongoose pour le récupérer de la base de données pour nous. C'est exactement la même chose que ce que nous faisions pour les résolveurs de requêtes régulières, mais cette fois, c'est un objet imbriqué.

Maintenant, nous pouvons retourner à notre playground et commencer à jouer avec la création et l'interrogation des utilisateurs et des espaces de travail ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*agNIJbcqZBHGgveZKuRiBA.png)

Oh yeah ! Nous avons couvert l'essentiel pour ce que vous pourriez transformer en un serveur entièrement fonctionnel.

**❓ Oh là là ! Vous êtes opérationnel avec GraphQL !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*IZcJKz3761vChU1VFHfzkw.jpeg)

### Autorisation ❓️

Donc, actuellement, nous avons une assez bonne API GraphQL. Mais il y a encore un problème : il n'y a aucune restriction sur qui peut accéder à nos données ! Pour corriger cela, nous devons ajouter l'authentification et l'autorisation.

**✍️ Attendez... l'authentification et l'autorisation ne sont pas la même chose ?**

C'est une idée fausse courante, mais importante à comprendre car elle vous aidera à construire de meilleures API :

* **Authentification** fait référence à l'identification de la personne qui demande des informations, c'est-à-dire déterminer quel utilisateur envoie une requête à l'API.
* **Autorisation** fait référence aux permissions disponibles pour ce demandeur, c'est-à-dire quels rôles l'utilisateur a et si ce rôle est suffisant pour permettre la requête.

**❓ Alors, comment l'implémentons-nous ?**

Une autre excellente question, vous êtes une personne vraiment curieuse ! Eh bien, il y a malheureusement de nombreuses façons de faire cela en fonction de la manière dont vous souhaitez que votre application fonctionne. Par exemple :

* Vous pourriez vouloir que les utilisateurs s'inscrivent uniquement avec l'authentification GitHub plutôt que de s'inscrire avec un email et un mot de passe.
* Vous pourriez avoir 3 rôles d'utilisateurs différents plutôt que 100 rôles d'utilisateurs très granulaires.
* Il pourrait ne pas y avoir d'utilisateurs du tout, votre application pourrait être utilisée de manière anonyme.

Dans tous les cas, la manière dont vous implémentez l'authentification et l'autorisation vous appartient. Mais si vous souhaitez un guide pour commencer, [voici un lien](https://www.prisma.io/blog/graphql-directive-permissions-authorization-made-easy-54c076b5368e/) vers un article génial de Prisma qui vous aide à commencer à ajouter l'authentification à votre API.

Pour faciliter un peu les choses, j'ai également ajouté une authentification de base à notre dépôt de démonstration que vous pouvez parcourir et vérifier. N'hésitez pas à améliorer le dépôt avec un meilleur exemple d'authentification et à soumettre une pull request !

> ~ [Voici un lien vers le dépôt de démonstration GraphQL](https://github.com/jackrobertscott/graphql-api-demo) ~

**❓ Wow ! Nous avons réussi à créer un serveur GraphQL ! Allez-y !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*DduhOox_qT0srXwxjnkK7A.jpeg)

Si vous avez aimé cet article, veuillez lui donner **quelques applaudissements** (vous pouvez en laisser jusqu'à 50) ou vous pouvez **commenter** si vous avez des questions, je ferai de mon mieux pour répondre ! 🙏

Suivez-moi sur [Twitter](https://twitter.com/jacrobsco).

Merci !

Plus de posts par Jack Scott.

* [Comment j'ai lancé une startup en 4 jours](https://medium.com/@jackrobertscott/startup-validation-done-right-6c7c62229e9)
* [Obtenir vos 100 premiers clients de startup](https://medium.com/@jackrobertscott/getting-your-first-100-startup-customers-8cafd0ee8e7d)
* [Au revoir Redux](https://hackernoon.com/goodbye-redux-26e6a27b3a0b)