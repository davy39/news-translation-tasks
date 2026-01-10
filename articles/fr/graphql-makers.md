---
title: L'API que je souhaite que les implémentations JavaScript GraphQL prennent en
  charge
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-10T18:24:02.000Z'
originalURL: https://freecodecamp.org/news/graphql-makers
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-10-at-11.27.12-AM.png
tags:
- name: api
  slug: api
- name: coding
  slug: coding
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
seo_title: L'API que je souhaite que les implémentations JavaScript GraphQL prennent
  en charge
seo_desc: 'By Samer Buna

  The GraphQL schema language is great! It is certainly the best way to communicate
  anything about a GraphQL service. No wonder all documentations now use it!

  The Schema Language

  Imagine that you’re building a blog app (with GraphQL) that...'
---

Par Samer Buna

Le langage de schéma GraphQL est génial ! C'est certainement la meilleure façon de communiquer quoi que ce soit sur un service GraphQL. Pas étonnant que toutes les documentations l'utilisent maintenant !

## Le langage de schéma

Imaginez que vous construisez une application de blog (avec GraphQL) qui a des "Articles" et des "Commentaires". Vous pouvez commencer à réfléchir à son schéma d'API en vous basant sur ce que vous prévoyez pour son interface utilisateur. Par exemple, la page principale aura probablement une liste d'articles et un élément de cette liste pourrait afficher un titre, un sous-titre, le nom de l'auteur, la date de publication, la longueur (en minutes de lecture) et une image mise en avant. Une version simplifiée de Medium lui-même si vous voulez :

![simple medium](https://jscomplete.com/images/reads/misc/simple-medium.png)

Nous pouvons utiliser le langage de schéma pour planifier ce dont vous avez besoin jusqu'à présent pour cette page principale. Un schéma de base pourrait ressembler à ceci :

```
type Query {
  articleList: [Article!]!
}
type Article {
  id: ID!
  title: String!
  subTitle: String
  featuredImageUrl: String
  readingMinutes: Int!
  publishedAt: String!
  author: Author!
}
type Author {
  name: String!
}
```

Lorsque l'utilisateur navigue vers un article, il verra les détails de cet article. Nous aurons besoin que l'API prenne en charge un moyen de récupérer un objet Article par son id. Supposons qu'un article peut également avoir des éléments d'interface utilisateur riches comme des en-têtes et des extraits de code. Nous devrions prendre en charge un langage de formatage de texte riche comme Markdown. Nous pouvons faire en sorte que l'API renvoie le contenu d'un article en Markdown ou en HTML via un argument de champ (`format`: HTML). Planifions également d'afficher un compteur de "likes" dans cette vue.

Mettons toutes ces idées sur papier ! Le langage de schéma est le moyen structuré le plus concis pour les décrire :

```
type Query {
  # ...
  article(id: String!): Article!
}
enum ContentFormat {
  HTML
  MARKDOWN
}
type Article {
  # ...
  content(format: ContentFormat): String!
  likes: Int!
}
```

La vue d'interface utilisateur d'un article affichera également la liste des commentaires disponibles sur un article. Gardons la vue d'interface utilisateur des commentaires simple et prévoyons qu'elle ait un contenu textuel et des champs de nom d'auteur :

```
type Article {
  # ...
  commentList: [Comment!]!
}
type Comment {
  id: ID!
  content: String!
  author: Author!
}
```

Concentrons-nous uniquement sur ces fonctionnalités. C'est un bon point de départ qui n'est pas trivial. Pour offrir ces capacités, nous devrons implémenter une logique de résolution personnalisée pour les champs calculés comme `content(format: HTML)` et `readingMinutes`. Nous devrons également implémenter des relations de base de données 1-1 et 1-plusieurs.

Avez-vous remarqué comment j'ai élaboré toute la description du schéma jusqu'à présent en réfléchissant simplement en termes d'interface utilisateur ? N'est-ce pas génial ? Vous pouvez donner ce texte simple de langage de schéma aux développeurs front-end de votre équipe et ils peuvent commencer à construire l'application front-end tout de suite ! Ils n'ont pas besoin d'attendre votre implémentation serveur. Ils peuvent même utiliser certains des excellents outils disponibles pour avoir un serveur GraphQL simulé qui résout ces types avec des données de test aléatoires.

> Le schéma est souvent comparé à un contrat. Vous commencez toujours par un contrat.

## Construction d'un schéma GraphQL

Lorsque vous êtes prêt à commencer à implémenter votre service GraphQL, vous avez aujourd'hui 2 options principales (en JavaScript) :

1. Vous pouvez "construire" un schéma non exécutable en utilisant le texte complet du langage de schéma que nous avons, puis attacher un ensemble de fonctions de résolution pour rendre ce schéma exécutable. Vous pouvez le faire avec [GraphQL.js](https://graphql.org/graphql-js/) lui-même ou avec [Apollo Server](https://www.apollographql.com/docs/apollo-server/). Les deux prennent en charge cette méthode, communément appelée "schema-first" ou "SDL-first". Je vais l'appeler ici la "**méthode de chaîne de schéma complète**".
2. Vous pouvez utiliser des objets JavaScript instanciés à partir des diverses classes de constructeurs disponibles dans l'API GraphQL.js (comme `GraphQLSchema`, `GraphQLObjectType`, `GraphQLUnionType`, et beaucoup d'autres). Dans cette approche, vous n'utilisez pas du tout le texte du langage de schéma. Vous créez simplement des objets. Cette méthode est communément appelée "code-first" ou "resolvers-first", mais je ne pense pas que ces noms la représentent équitablement. Je vais l'appeler ici la "**méthode basée sur les objets**".

Les deux approches ont des avantages et des inconvénients.

Le langage de schéma est un excellent moyen, indépendant du langage de programmation, pour décrire un schéma GraphQL. C'est un format lisible par l'homme, facile à utiliser. Les développeurs front-end de votre équipe l'adoreront absolument. Il leur permet de participer à la conception de l'API et, plus important encore, de commencer à utiliser une version simulée de celle-ci tout de suite. Le texte du langage de schéma peut servir de première version de la documentation de l'API.

Cependant, le fait de s'appuyer complètement sur le texte complet du langage de schéma pour créer un schéma GraphQL présente quelques inconvénients. Vous devrez faire un effort pour rendre le code modulaire et clair, et vous devrez vous appuyer sur des modèles de codage et des outils pour maintenir la cohérence du texte du langage de schéma avec l'arborescence des résolveurs (également appelée carte des résolveurs). Ce sont des problèmes solubles.

Le plus gros problème que je vois avec la méthode de chaîne de schéma complète est que vous perdez une certaine flexibilité dans votre code. Vous n'avez pas d'objets associés aux types. Vous n'avez que des chaînes de caractères ! Et bien que ces chaînes rendent vos types plus lisibles, dans de nombreux cas, vous aurez besoin de flexibilité plutôt que de lisibilité.

La méthode basée sur les objets est flexible et plus facile à étendre et à gérer. Elle ne souffre d'aucun des problèmes mentionnés. Vous devez être modulaire avec elle parce que votre schéma est un ensemble d'objets. Vous n'avez pas non plus besoin de fusionner des modules ensemble car ces objets sont conçus et censés fonctionner comme un arbre.

Le seul problème que je vois avec la méthode basée sur les objets est que vous devez gérer beaucoup plus de code autour de ce qui est important à gérer dans vos modules (types et résolveurs). Beaucoup de développeurs voient cela comme du "bruit" et vous ne pouvez pas les blâmer. Nous allons travailler sur un exemple pour voir cela.

Si vous créez un service GraphQL de petite portée et bien défini, l'utilisation de la méthode de chaîne de schéma complète est probablement acceptable. Cependant, dans des projets plus grands et plus agiles, je pense que la méthode basée sur les objets, plus flexible et plus puissante, est la voie à suivre.

> Vous devriez toujours tirer parti du texte du langage de schéma même si vous utilisez la méthode basée sur les objets. Chez [jsComplete](https://jscomplete.com), nous utilisons la méthode basée sur les objets, mais chaque fois que le schéma est construit, nous utilisons la fonction `graphql.printSchema` pour écrire le schéma complet dans un fichier. Nous validons et suivons ce fichier dans le dépôt Git du projet et cela s'est avéré être une pratique très utile !

Pour comparer les 2 méthodes, j'ai implémenté un schéma exécutable pour l'exemple de blog que nous avons commencé en utilisant les deux. J'ai omis une partie du code pour plus de brièveté, mais j'ai gardé ce qui compte pour la comparaison.

### La méthode de chaîne de schéma complète

Nous commençons par le texte du langage de schéma qui définit 3 types personnalisés principaux (`Article`, `Comment`, et `Author`). Les champs sous le type principal `Query` sont `article` et `articleList` qui résoudront directement des objets à partir de la base de données. Cependant, puisque le schéma GraphQL que nous avons planifié a des fonctionnalités personnalisées autour d'un objet article et puisque nous avons des relations que nous devons également résoudre, nous aurons besoin d'avoir des résolveurs personnalisés pour les 3 types personnalisés principaux de GraphQL.

Voici quelques captures d'écran du code que j'ai écrit pour représenter la méthode de chaîne de schéma complète. J'ai utilisé Apollo Server ici, mais cela est également possible avec GraphQL.js vanilla (et un peu plus de code).

> Veuillez noter que ceci n'est qu'UNE façon d'implémenter la méthode de chaîne de schéma complète pour ce service. Il existe d'innombrables autres façons. Je présente simplement la manière modulaire la plus simple ici pour nous aider à comprendre les véritables avantages et inconvénients.

![gmapi1](https://jscomplete.com/images/reads/misc/gmapi1.png)

C'est bien ! Nous pouvons voir les types dans le schéma en un seul endroit. Il est clair où le schéma commence. Nous sommes en mesure de modulariser le code par type/fonctionnalité.

![gmapi2](https://jscomplete.com/images/reads/misc/gmapi2.png)

C'est vraiment bien ! Les résolveurs sont co-localisés avec les types qu'ils implémentent. Il n'y a pas de bruit. Ce fichier contient magnifiquement ce qui compte dans un format très lisible. J'adore !

> La modularité ici n'est possible qu'avec Apollo Server. Si nous devions faire cela avec GraphQL.js vanilla, nous devrions bidouiller des objets de données pour les rendre adaptés à être un "arbre de résolveurs". Le mélange entre les structures de données et le graphe des résolveurs n'est pas idéal.

**Quel est donc l'inconvénient ici ?**

Si vous utilisez cette méthode, alors tous vos types doivent être écrits de cette certaine manière qui repose sur le texte du langage de schéma. Vous avez moins de flexibilité. Vous ne pouvez pas utiliser de constructeurs pour créer **certains** types lorsque vous en avez besoin. Vous êtes bloqué dans cette approche basée sur les chaînes de caractères.

Si cela vous convient, ignorez le reste de cet article. Utilisez simplement cette méthode. Elle est tellement plus propre que l'alternative.

### La méthode basée sur les objets

Examinons maintenant l'approche basée sur les objets. Voici le point de départ d'un schéma exécutable construit en utilisant cette méthode :

![gmapi3](https://jscomplete.com/images/reads/misc/gmapi3.png)

Nous n'avons pas besoin d'un objet `resolvers` séparé. Les résolveurs font partie de l'objet de schéma lui-même. Cela les rend plus faciles à maintenir. Ce code est également plus facile à étendre et à analyser de manière programmatique !

C'est aussi beaucoup plus de code qui est plus difficile à lire et à comprendre ! Attendez de voir le reste du code. Je n'ai pas pu prendre la capture d'écran du type `Article` sur l'écran de l'ordinateur portable. J'ai dû utiliser un écran plus grand.

![gmapi4](https://jscomplete.com/images/reads/misc/gmapi4.png)

Pas étonnant que la méthode de chaîne de schéma complète soit populaire ! Il y a certainement beaucoup de "bruit" à gérer ici. Les types ne sont pas clairs au premier regard. Les résolveurs personnalisés sont mélangés dans un grand objet de configuration.

Ma partie préférée est lorsque vous devez créer une liste non nulle d'éléments non nuls comme `[Article!]!`. Avez-vous vu ce que j'ai dû écrire ?

`new GraphQLNonNull(new GraphQLList(new GraphQLNonNull(Article))),`

Cependant, bien que ce soit effectivement beaucoup plus de code qui est plus difficile à comprendre, c'est toujours une meilleure option que d'avoir une grande chaîne (ou plusieurs chaînes combinées en une) et un grand objet de résolveurs racine (ou plusieurs objets de résolveurs combinés en un). C'est mieux que d'avoir toutes les dépendances de votre application gérées en un seul point d'entrée.

Il y a beaucoup de puissance dans la modularisation de votre code en utilisant des objets (qui peuvent dépendre les uns des autres). C'est plus propre de cette façon et cela facilite également l'écriture de tests et de validations. Vous obtenez des messages d'erreur plus utiles lorsque vous déboguez des problèmes. Les éditeurs modernes peuvent fournir des indices plus utiles en général. Plus important encore, vous avez beaucoup plus de flexibilité pour faire quoi que ce soit avec ces objets. L'API des constructeurs GraphQL.js elle-même utilise également des objets JavaScript. Il y a tant de choses que vous pouvez faire avec eux.

Mais le bruit est également réel.

### La méthode basée sur les objets sans le bruit

Je reste avec la méthode basée sur les objets, mais je souhaite vraiment que les implémentations JavaScript GraphQL aient une meilleure API qui puisse nous donner une partie de la puissance de la méthode de chaîne de schéma complète.

Ne serait-ce pas bien si nous pouvions écrire la logique du type `Article` exactement comme nous l'avons fait dans la méthode de chaîne de schéma complète, mais de manière à générer le `GraphQLObjectType` flexible que nous pouvons brancher dans un schéma basé sur les objets ?

Quelque chose comme :

![gmapi5](https://jscomplete.com/images/reads/misc/gmapi5.png)

Ne serait-ce pas idéal ? **Nous obtenons les avantages de la méthode de chaîne de schéma complète pour ce type, mais sans verrouillage !** D'autres types dans le système peuvent être maintenus différemment. Peut-être que d'autres types seront construits dynamiquement en utilisant une logique de création différente !

Tout ce dont nous avons besoin pour que cela se produise est une méthode magique `**typeMakerMethod**` pour prendre les parties qui comptent et les transformer en `GraphQLObjectType` complet pour `Article`.

La méthode `typeMakerMethod` devra analyser une chaîne en un AST, utiliser cela pour construire un `GraphQLObjectType`, puis fusionner l'ensemble des fonctions de résolution personnalisées avec la configuration `fields` qui sera analysée à partir de la chaîne `typeDef`.

J'aime un défi, alors j'ai creusé un peu plus pour voir à quel point il serait difficile d'implémenter la méthode `typeMakerMethod`. Je savais que je ne pouvais pas utiliser la fonction `graphql.buildSchema` car elle ne parse qu'une seule chaîne de schéma complète pour créer un objet de schéma non exécutable. J'avais besoin d'une partie de plus bas niveau qui parse une chaîne qui a exactement UN type, puis y attache des résolveurs personnalisés. J'ai donc commencé à lire le code source de GraphQL.js pour chercher des indices. Quelques tasses de café plus tard, j'ai trouvé des réponses (en 2 endroits) :

![gmapi6](https://jscomplete.com/images/reads/misc/gmapi6.png)

C'est la méthode principale utilisée dans `buildSchema` pour construire UN type à partir d'un nœud de définition de type (que nous pouvons facilement obtenir en analysant la chaîne `typeDef`).

Et :

![gmapi7](https://jscomplete.com/images/reads/misc/gmapi7.png)

C'est à quel point il est facile d'étendre un type d'objet et d'attacher toute logique nécessaire dans `fields` et `interfaces` !

Tout ce que je devais faire était de rassembler quelques morceaux et le rêve pouvait devenir réalité.

**[Je l'ai fait](https://github.com/jscomplete/graphql-makers#readme).**

Mesdames et messieurs. Je vous présente la méthode magique "typeMakerMethod" (que j'ai nommée `objectType`) :

![gmapi8](https://jscomplete.com/images/reads/misc/gmapi8.png)

C'est tout (dans sa forme la plus basique) ! Cela prendra une chaîne `typeDef` qui définit un seul type GraphQL, un objet de résolveurs et une carte de dépendances (pour ce type), et cela renverra un `GraphQLObjectType` prêt à être branché dans votre schéma basé sur les objets comme s'il avait été défini normalement avec le constructeur d'objets.

Maintenant, vous pouvez utiliser la méthode basée sur les objets, mais vous avez la possibilité de définir CERTAINS types en utilisant une approche similaire à la méthode de chaîne de schéma complète. Vous avez le pouvoir.

**Que pensez-vous de cette approche ? J'adorerais avoir votre retour !**

> Veuillez noter que le code `objectType` ci-dessus est simplement le **cas d'utilisation de base**. Il existe de nombreux autres cas d'utilisation qui nécessitent un code supplémentaire. Par exemple, si les types ont des dépendances circulaires (`article` → `author` → `article`), alors cette version de `objectType` ne fonctionnera pas. Nous pouvons retarder le chargement des dépendances circulaires jusqu'à ce que nous soyons dans le `fields` thunk (qui est l'approche actuelle pour résoudre ce problème dans la méthode basée sur les objets). Nous pouvons également utiliser la syntaxe "extend" pour concevoir le schéma de manière à éviter les dépendances circulaires dès le départ. J'ai sauté cette partie pour garder l'exemple simple.

> Si vous souhaitez l'essayer, j'ai publié une version plus aboutie de `objectType` et quelques autres fonctions de création similaires sous le package npm [**graphql-makers**](https://www.npmjs.com/package/graphql-makers).

---

_Publié à l'origine sur_ [_https://jscomplete.com_](https://jscomplete.com/learn/19xfr-the-api-I-wish-graphql-implementations-supported) _le 9 juin 2019._