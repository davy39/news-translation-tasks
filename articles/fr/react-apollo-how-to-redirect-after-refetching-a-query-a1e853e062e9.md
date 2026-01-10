---
title: 'React + Apollo : Comment rediriger après avoir réexécuté une requête'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T04:42:56.000Z'
originalURL: https://freecodecamp.org/news/react-apollo-how-to-redirect-after-refetching-a-query-a1e853e062e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*z-LROfr9BoiuMhlra-_OZQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'React + Apollo : Comment rediriger après avoir réexécuté une requête'
seo_desc: 'By Jun Hyuk Kim

  GraphQL is hot, and for a good reason. In short, it is a query language that allows
  you to ask for exactly what you need from your API. This cuts any unnecessary data
  transfer that may occur with different methodologies.

  I was working...'
---

Par Jun Hyuk Kim

[GraphQL](https://graphql.org/) est très populaire, et pour une bonne raison. En bref, c'est un langage de requête qui vous permet de demander _exactement_ ce dont vous avez besoin depuis votre API. Cela évite tout transfert de données inutile qui peut survenir avec d'autres méthodologies.

Je travaillais sur un projet où j'utilisais un back-end GraphQL. J'ai décidé d'utiliser React et Apollo Client comme front-end pour communiquer avec mon back-end GraphQL. J'avais quelques difficultés à comprendre comment réexécuter ma requête, puis à rediriger ma page vers la page principale avec les données mises à jour. C'est là que les choses ont commencé à se compliquer un peu.

Le problème, pour moi, était de comprendre comment la mutation était réellement appelée et ce qui était retourné. Nous pouvons accéder à la mutation après l'avoir connectée via `graphql(mutation)(*VotreComposant*)` grâce à `this.props.mutate()`. Cette fonction retourne une Promesse. Nous pouvons enchaîner des fonctions `.then()` pour appeler des fonctions après la mutation. La fonction mutate peut également prendre des variables pour la mutation. Un exemple complet serait quelque chose comme ceci :

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  }})
```

Cela signifie que notre mutation prend deux variables, appelées title et content. Elles sont passées à notre mutation lorsque nous l'envoyons à notre serveur back-end. Supposons que notre mutation ajoute une note, avec un titre et un contenu. Pour clarifier les choses, je vais inclure un exemple simple de ce à quoi ressemblerait notre mutation :

```
const mutation = gql`  mutation AddNote($title: String, $content: String){    addNote(title:$title, content:$content){      title      content    }  }}`
```

```
// Notre composant doit également être connecté au client Apollo, donc // quelque chose comme ceci
```

```
export default graphql(mutation)(Component)
```

Alors, que se passe-t-il après que cette fonction se produise ? Notre back-end reçoit les informations, et la mutation se produit. Cependant, notre front-end ne sait pas que la mutation a eu lieu. Il ne réexécute pas la requête que nous avons précédemment récupérée (dans notre cas, peut-être quelque chose comme fetchAllNotes). C'est là que la fonction mutate devient très pratique. Nous pouvons passer une variable appelée `refetchQueries`, qui réexécutera toutes les requêtes que nous demandons.

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  },  refetchQueries:[{    query: fetchAllNotes  }]}).then(() => this.props.history.push('/notes'))
```

Dans ce cas, nous disons au client Apollo de réexécuter la requête `fetchAllNotes` après que la mutation se produise. Ensuite, nous redirigeons l'utilisateur vers le répertoire `/notes` (React-Router). Souvenez-vous que notre fonction mutate retourne une Promesse ? Cela devrait tout faire fonctionner, n'est-ce pas ? Eh bien... par conception, l'équipe Apollo a fait en sorte que `refetchQueries` se produise **en même temps** que l'instruction `.then`. Cela signifie que l'instruction .then peut se produire avant `refetchQueries`. Cela peut conduire à ce que le composant ayant besoin des informations mises à jour ne soit pas mis à jour.

Dans ce cas spécifique, ce qui se passerait, c'est que notre utilisateur serait redirigé _avant_ que `refetchQueries` ne se produise. Les informations ne seront pas mises à jour. C'est délicat parce que la fonction mutate retourne une Promesse. L'équipe Apollo l'a conçu de manière à ce que `refetchQueries` puisse se produire en même temps que n'importe quelle instruction `.then`. Alors, comment gérons-nous cela ?

L'équipe Apollo a réalisé que cela pourrait potentiellement poser un problème. Ils ont proposé une [solution](https://github.com/apollographql/apollo-client/pull/3169), qui permet à `refetchQueries` de prendre une variable qui permettrait de retourner une Promesse, et ainsi de se produire avant toute instruction `.then`. Notre code ressemblerait à quelque chose comme ceci :

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  },  refetchQueries:[{    query: fetchAllNotes,    variables:{      awaitRefetchQueries: true    }  }]}).then(() => this.props.history.push('/notes'))
```

Si cela a fonctionné pour vous, super ! On dirait que la correction a fonctionné ! Cependant, cela n'a pas fonctionné pour moi personnellement. De plus, comme cela n'est disponible que dans les versions plus récentes d'Apollo Client, cela ne sera pas disponible dans les anciennes versions d'Apollo Client.

J'ai dû faire un peu de résolution de problèmes avec les cycles de vie des composants React pour m'assurer que mon composant afficherait correctement les données mises à jour. La correction elle-même est assez courte et assez simple ! Sur mon composant Notes, qui affiche les notes et est connecté à la requête `fetchAllNotes` par la fonction `graphql`, j'ai ajouté une correction rapide pour m'assurer que mes données étaient correctement affichées.

```
componentDidUpdate(prevProps){  if(prevProps.data.notes && prevProps.data.notes.length !==     this.props.data.notes.length){    // Logique pour mettre à jour le composant avec les nouvelles données  }}
```

En gros, nous disons que lorsque le composant est mis à jour, nous voulons voir si la requête des notes a été précédemment complétée (en vérifiant si `prevProps.data.notes` existe) et si la longueur des données a changé. Cela permet à notre composant React de mettre à jour les informations une fois que la requête de réexécution est terminée.

Tout devrait fonctionner maintenant ! Espérons que la variable `awaitRefetchQueries` a fonctionné pour vous et devient plus connue, ce qui est une solution beaucoup plus élégante. Cependant, il est assez difficile de trouver des exemples/documentation sur la façon d'utiliser correctement `awaitRefetchQueries`. Pour l'instant, avoir une bonne compréhension des cycles de vie des composants React est suffisant pour vous aider à contourner les "pièges" d'Apollo + React !

N'hésitez pas à laisser vos commentaires ou questions dans les commentaires, et je ferai de mon mieux pour vous aider. Je ne suis en aucun cas un expert, mais j'adorerais résoudre des problèmes avec vous et vous aider à comprendre !