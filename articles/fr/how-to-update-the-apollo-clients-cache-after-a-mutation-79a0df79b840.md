---
title: Comment mettre à jour le cache d'Apollo Client après une mutation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T18:12:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-the-apollo-clients-cache-after-a-mutation-79a0df79b840
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CbevjJN6IQBk7gbh38V-2g.png
tags:
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment mettre à jour le cache d'Apollo Client après une mutation
seo_desc: 'By ric0

  The Apollo Client and its cache

  The Apollo Client is used to fetch data from any GraphQL server. The client is small,
  yet flexible with many awesome features of which the most appreciated one might
  be the automatic cache updates that come wit...'
---

Par ric0

### Apollo Client et son cache

Le [Apollo Client](https://www.apollographql.com/docs/react/) est utilisé pour récupérer des données depuis n'importe quel serveur GraphQL. Le client est petit, mais flexible avec de nombreuses fonctionnalités impressionnantes, dont la plus appréciée est probablement les mises à jour automatiques du cache qui accompagnent le client.

En gros, Apollo Client inspecte automatiquement le trafic des requêtes et des mutations pour vous et utilise la dernière version des données qu'il voit dans une réponse afin que le cache local soit toujours à jour.

### Une simple mise à jour

Prenons, par exemple, une requête qui demande tous les articles :

```
query articles { articles {    id    title    published     author {       name    }  }}
```

Nous obtenons ces données en retour :

```
{  data: {    articles: [      {        id: '6543757061',        title: 'Does It Pay to Be a Writer?',        published: true,        author: {          name: 'John Doe',        }      },      {        id: '6543757062',        title: 'The Genius of Insomnia',        published: true,        author: {          name: 'Mike Kinski',        }      }    ]  }}
```

Plus tard, nous modifions le titre de l'article avec l'id "6543757061" :

```
// MUTATIONmutation updateArticle($id: ID! $title: String) {  updateArticle(id: $id, title: $title) {    id    title    published    author {      name    }  }}
```

```
// _update-article.js...this.props.mutate({  mutation: UPDATE_ARTICLE,  variables: {    id: '6543757061',    title: 'I am a new title',   },});...
```

Résultat :

```
articles: [      {        id: '6543757061',        title: 'I am a new title',        published: true,        author: {          name: 'John Doe',        }      },      {        id: '6543757062',        title: 'The Genius of Insomnia',        published: true,        author: {          name: 'Mike Kinski',        }      }    ]
```

Après que la mutation a réussi, notre cache est mis à jour automatiquement pour deux raisons :

* nous avons inclus l'id de l'article dans la réponse de la mutation
* nous avons inclus le titre dans la réponse

En effet, si le champ `id` des deux résultats correspond, alors le champ `title` partout dans notre UI sera mis à jour automatiquement.

En gros, vous devriez faire en sorte que les résultats de votre mutation contiennent toutes les données nécessaires pour mettre à jour les requêtes précédemment récupérées.

C'est aussi pourquoi il est une bonne pratique d'utiliser des [fragments](https://www.apollographql.com/docs/react/advanced/fragments.html) pour partager des champs parmi toutes les requêtes et mutations qui sont liées.

Cependant, la mise à jour du nom de l'auteur n'aurait pas le même résultat que le précédent car nous n'avons pas de champ `id` dans l'`author`. Pour que cela fonctionne, la requête et la mutation devraient inclure l'id de l'auteur également :

```
idtitlepublishedauthor {  id  name}
```

### Cas d'utilisation étendus

Cependant, ce qui précède est le seul type de scénario où la mise à jour en place est plus que suffisante. En effet, il existe de nombreuses autres situations courantes que la mise à jour automatique ne couvre pas, telles que :

* création d'article
* suppression d'article
* listes filtrées d'articles

et ainsi de suite.

Généralement, tout cas où vous devez mettre à jour votre cache d'une manière qui dépend des données actuellement dans votre cache.

Ce sont des cas qui ne peuvent être résolus que de deux manières :

* rafraîchir le navigateur** après la mutation :D
* accéder directement au cache local en utilisant la fonction `update` qui vous permet de mettre à jour manuellement le cache après qu'une mutation se produise sans récupérer à nouveau les données

** en considérant que vous utilisez la politique de récupération `cache-first` par défaut [fetchPolicy](https://www.apollographql.com/docs/react/api/react-apollo.html#graphql-config-options-fetchPolicy)

Bien que [refetchQueries](https://www.apollographql.com/docs/react/api/react-apollo.html#graphql-mutation-options-refetchQueries) serait la troisième option, `update` est la méthode recommandée par Apollo pour mettre à jour le cache après une requête. Elle est expliquée en détail [ici](https://www.apollographql.com/docs/react/api/react-apollo.html#graphql-mutation-options-update).

### Utilisation de la fonction update

Cependant, parce que l'utilisation de la fonction update vous donne un contrôle total sur le cache, vous permettant de faire des changements à votre modèle de données en réponse à une mutation de la manière que vous souhaitez, cela devient rapidement complexe de gérer votre propre cache.

La tentation serait de désactiver le cache Apollo par défaut, mais cela ne devrait jamais être le cas.

Abordons les défis les plus courants auxquels vous pourriez être confronté lorsque vous commencez à gérer votre propre cache directement.

#### Utilisez toujours un bloc try/catch

La plupart des exemples que vous voyez, également dans la documentation officielle d'Apollo, ressemblent à ce qui suit :

```
const query = gql`{ todos { ... } }`export default graphql(gql`  mutation ($text: String!) {    createTodo(text: $text) { ... }  }`, {  options: {    update: (proxy, { data: { createTodo } }) => {      const data = proxy.readQuery({ query });      data.todos.push(createTodo);      proxy.writeQuery({ query, data });    },  },})(MyComponent);
```

C'est cool, mais que se passe-t-il si la requête n'a pas encore été récupérée, donc n'est pas dans votre cache comme vous l'aviez supposé ? `proxy.readQuery` lancerait une erreur et l'application planterait.

Être sûr que la requête est là ne serait sûr que dans des scénarios simples. Vous devez utiliser un bloc try/catch :

```
update: (proxy, { data: { createTodo } }) => {      try {        const data = proxy.readQuery({ query });        data.todos.push(createTodo);        proxy.writeQuery({ query, data });      }      catch(error) {        console.error(error);      }},
```

Sinon, vous devriez être sacrément sûr que la requête serait déjà dans le cache.

Le message ici est que vous feriez mieux de ne pas faire d'hypothèses du tout. Comme [Dan Abramov](https://twitter.com/dan_abramov) l'a parfaitement expliqué dans son [article de blog](https://overreacted.io/the-elements-of-ui-engineering/) :

> Nous ne pouvons pas prédire les interactions exactes des utilisateurs et leur ordre. À tout moment, notre application peut se trouver dans l'un d'un nombre ahurissant d'états possibles. Nous faisons de notre mieux pour rendre le résultat prévisible et limité par notre conception. Nous ne voulons pas regarder une capture d'écran de bug et nous demander "comment cela a-t-il pu se produire".

Gardez à l'esprit que `proxy.readQuery` et `proxy.writeQuery` peuvent tous deux lancer des erreurs indépendamment. Par exemple, vous pouvez lire avec succès une requête depuis le cache tandis que l'opération d'écriture lancera une erreur en raison d'un champ manquant dans les données, plus souvent qu'autrement ce champ manquant serait `__typename`.

#### Définissez toujours les variables utilisées dans la requête

Imaginez maintenant que nous avons une mutation qui crée un nouvel article déjà marqué comme publié.

Généralement, des exemples simples montrent une seule requête récupérant tous les articles qui sont ensuite filtrés sur le Client (ex. articles.filter(article => article.published))

Pour illustrer notre propos, supposons plutôt que nous avons une requête qui récupère depuis le serveur uniquement les articles publiés.

À ce stade, après que la mutation du nouvel article est terminée, nous devons lire/écrire la requête mise en cache en utilisant la variable `published: true` pour correspondre à la requête exacte que nous devons mettre à jour dans le cache.

```
update: (proxy, { data: { createPublishdedArticles } }) => {      try {        const data = proxy.readQuery({ query, variables: { published: true } });        data.articles.push(createPublishdedArticles);        proxy.writeQuery({ query, variables: { published: true }, data });      }      catch(error) {        console.error(error);      }},
```

C'est tout. Bien que ce cas d'utilisation soit gérable, puisque nous n'avons qu'une seule variable booléenne, cela devient assez délicat une fois que vous avez des cas d'utilisation plus compliqués, qui incluent plusieurs requêtes et variables.

### Complexité croissante

Jusqu'à présent, nous n'avons couvert que des cas de base. Lors du développement de n'importe quelle application, les choses deviennent facilement plus exigeantes en termes de gestion du cache.

En effet, bien que l'utilisation d'Apollo Client pour mettre à jour le cache local devient exponentiellement compliquée lorsqu'elle doit inclure plusieurs variables, inclure plusieurs requêtes ou couvrir des scénarios où la mise à jour en place d'Apollo peut ne pas être suffisante :

* Ajouter/supprimer d'une liste
* Déplacer d'une liste à une autre
* Mettre à jour une liste filtrée

et ainsi de suite.

#### Mettre à jour plus d'une requête après une mutation

Il arrive généralement qu'après une mutation, nous voulons mettre à jour plus d'une seule requête. Par exemple, imaginons que nous récupérons tous les articles dans le composant de tableau de bord, mais aussi les articles publiés et non publiés dans deux autres composants différents.

Apollo client n'écrira pas seulement chaque requête dans le cache, mais le fera de sorte que la même requête avec différentes variables soit stockée comme 2 entrées différentes. Par exemple, voici nos deux requêtes :

```
// query 1query articles { articles {    id    title    published     author {       name    }  }}// will be stored as: articles
```

```
// query 2query articles($where: JSON) { articles(where: $where) {    id    title    published     author {       name    }  }}/* will be stored as:articles({"where":{"published":true,"sort":"asc"})
```

```
when the query is invoked with:{ variables: { where: { published: true, sort: "asc" } } }*/
```

Ce sont 2 requêtes différentes dans le cache d'Apollo comme on pourrait s'y attendre. Cependant, nous voulons également récupérer tous les articles non publiés. Pour ce faire, nous devons invoquer "query 2" avec les variables `where: { published: false, sort: 'asc' }`

En faisant cela, vous vous retrouvez avec 3 entrées dans le cache :

```
articlesarticles({"where":{"published":true,"sort":"asc"}})articles({"where":{"published":false,"sort":"asc"}})
```

Pourquoi est-ce important ? Si vous allez ajouter un nouvel article et souhaitez mettre à jour le cache local après la mutation, vous devrez lire plus d'une requête et également la même requête plusieurs fois (une fois pour chaque ensemble de variables). Comme ceci :

```
// STEP #1// update 'articles'try {  const dataQuery = proxy.readQuery({    query: getArticles  });
```

```
  dataQuery.articles.push(newArticle);
```

```
  proxy.writeQuery({    query: getArticles,    data: dataQuery  });}catch(error) {  console.error(error);}
```

```
// STEP #2// articles({"where":{"published":true,"sort":"asc"}})try {  const dataQuery = proxy.readQuery({    query: getArticles,    variables: {      {        where:{          published: true,          sort: "asc",        },      },    },  });
```

```
  dataQuery.articles.push(newArticle);
```

```
  proxy.writeQuery({    query: getArticles,    variables: {      {        where:{          published: true,          sort: "asc",        },      },    },    data: dataQuery  });}catch(error) {  console.error(error);}
```

```
// STEP #3// articles({"where":{"published":false,"sort":"asc"}})try {  const dataQuery = proxy.readQuery({    query: getArticles,    variables: {      {        where:{          published: false,          sort: "asc",        },      },    },  });
```

```
  dataQuery.articles.push(newArticle);
```

```
  proxy.writeQuery({    query: getArticles,    variables: {      {        where:{          published: false,          sort: "asc",        },      },    },    data: dataQuery  });}catch(error) {  console.error(error);}
```

Vous devriez déjà voir où cela mène et à quel point il est facile d'ajouter plus de code standard pour chaque combinaison de requêtes/variables.

#### Ordre et valeurs des variables

Il est également important de noter que l'ordre des variables est très important.

Ces deux requêtes suivantes ne sont pas considérées comme identiques et seront stockées séparément dans le cache :

```
// Calling a query
```

```
export default graphql(gql`  query ($width: Int!, $height: Int!) {    dimensions(width: $width height: $height) {    ...   }   ...  }`, {  options: (props) => ({    variables: {      width: props.size,      height: props.size,    },  }),})(MyComponent);
```

```
// Calling the same query above, but with a different order of variables fieldsexport default graphql(gql`  query ($width: Int!, $height: Int!) {     dimensions(width: $width height: $height) {    ...   }   ...  }`, {  options: (props) => ({    variables: {      height: props.size,      width: props.size,    },  }),})(MyComponent);
```

Cela se termine avec la même requête stockée deux fois dans le cache avec un ordre différent de variables :

```
dimensions({"width":600,"height":600})dimensions({"height":600,"width":600})
```

Invoquez à nouveau la même requête avec des props.size différentes et vous obtenez une entrée supplémentaire dans le cache :

```
dimensions({"width":600,"height":600})dimensions({"height":600,"width":600})dimensions({"height":100,"width":100})
```

Fou, n'est-ce pas ? Vous voyez comment cela peut facilement échapper à tout contrôle si abordé naïvement.

#### Cas particuliers

Si cela ne suffisait pas, il y a encore plus.

Lorsque vous définissez une requête avec des variables, vous les utilisez généralement aussi.

Considérons l'exemple suivant :

```
query articles($sort: String, $limit: Int) {    articles(sort: $sort, limit: $limit) {      _id      title      published      flagged    }  }
```

Vous allez probablement l'invoquer comme ceci :

```
export default graphql(gql`${ABOVE_QUERY}`, {  options: (props) => ({    variables: {      sort: props.sort,      limit: props.limit,    },  }),})(MyComponent);
```

Mais que se passe-t-il si elle est appelée soit sans objet de variables du tout (l'objet de variables n'est pas présent), soit si un objet de variables vide a été passé, comme `variables: {}`. Cela peut se produire lorsque les variables sont construites de manière programmatique.

Par exemple :

```
export default graphql(gql`${ABOVE_QUERY}`, {  options: (props) => ({    variables: props.varObj, // props.varObj peut être un objet vide  }),})(MyComponent);
```

stocke `articles({"sort":null,"limit":null})` dans le cache ;

tandis que :

```
export default graphql(gql`${ABOVE_QUERY}`)(MyComponent);
```

stocke `articles({})` dans le cache.

Les cas particuliers ci-dessus sont plus le résultat d'un comportement indésirable/inattendu que fait exprès. Cependant, il est bon de garder à l'esprit comment cette requête se terminera dans le cache et sous quelle forme.

#### Déplacer des éléments entre les requêtes mises en cache

Il pourrait également y avoir le cas où nous voulons dépublier un article. Cela signifierait le déplacer de la requête publiée à celle non publiée.

En gros, nous devons d'abord sauvegarder l'élément de la liste publiée, puis le supprimer et enfin ajouter l'élément sauvegardé à la liste non publiée. Voyons comment cela peut être fait :

```
const elementToMoveId = '1';let elementToMove;
```

```
try {  const dataQueryFrom = proxy.readQuery({    query: getArticles,    variables: {      {        where:{          published: true,          sort: "asc",        },      },    },  });  elementToMove = dataQueryFrom.articles.filter(item => item.id === elementToMoveId)[0];  dataQueryFrom.articles  = dataQueryFrom.articles.filter(item => item.id !== elementToMoveId)
```

```
proxy.writeQuery({    query: getArticles,    variables: {      {        where:{          published: true,          sort: "asc",        },      },    },    data: dataQueryFrom  });}catch(error) {  console.error(error);}
```

```
if (elementToMove) {  try {    const dataQueryTo = proxy.readQuery({      query: getArticles,      variables: {        {          where:{            published: false,            sort: "asc",          },         },      },    });
```

```
   dataQueryTo.articles.push(elementToMove);
```

```
proxy.writeQuery({      query: getArticles,      variables: {        {          where:{            published: true,            sort: "asc",          },        },      },      data: dataQueryTo,    });  }  catch(error) {    console.error(error);  }}
```

### Apollo Cache Updater

Comme vous le voyez, il y a beaucoup de choses à faire pour gérer des cas d'utilisation très courants.

Il y a beaucoup de code à écrire et il est sujet à des erreurs.

Pour ces raisons, j'ai publié [Apollo Cache Updater](https://github.com/ecerroni/apollo-cache-updater), un [package npm](https://github.com/ecerroni/apollo-cache-updater) qui est un helper sans dépendances pour mettre à jour le cache d'Apollo après une mutation. Cela m'a aidé à rester sain d'esprit tout en gérant le cache :)

Il essaie de découpler la vue de la couche de cache en configurant le comportement de mise en cache des résultats de la mutation via la variable `update` d'Apollo.

Le but est de couvrir tous les scénarios ci-dessus en passant simplement un objet de configuration.

Ce qu'il fait, après que vous avez probablement exécuté plusieurs requêtes avec différentes variables, pagination, etc., est d'itérer sur chaque objet dans ROOT_QUERY en effectuant des actions en votre nom que vous avez définies dans l'objet de configuration que vous avez passé.

### Conclusions

Gérer le cache est difficile, dans n'importe quelle langue. Apollo Client nous donne de nombreux avantages, mais dans des scénarios plus complexes, il nous laisse, développeurs, gérer tout par nous-mêmes. Apollo Cache Updater essaie d'atténuer un peu cette douleur en attendant une solution officielle, facile à utiliser, pour ajouter/supprimer automatiquement des entrées aux requêtes mises en cache.

Obtenez le package npm [ici](https://github.com/ecerroni/apollo-cache-updater).