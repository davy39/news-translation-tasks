---
title: Comment faire des mutations Apollo HOC de la bonne manière
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T06:39:43.000Z'
originalURL: https://freecodecamp.org/news/do-apollo-hoc-mutations-goodly-bb4effdbee94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C1932-kODhSC6ibR7kUxNA.jpeg
tags:
- name: apollo client
  slug: apollo-client
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment faire des mutations Apollo HOC de la bonne manière
seo_desc: 'By Lachlan Young

  Chances are, like many people, you’re coming to Apollo and GraphQL from a REST API
  background. Yet as you begin to explore the working examples of this stack and the
  different ways to implement it, you will no doubt be tripped up on ...'
---

Par Lachlan Young

Il est probable que, comme beaucoup de gens, vous veniez à Apollo et GraphQL d'un background d'API REST. Pourtant, alors que vous commencez à explorer les exemples fonctionnels de cette stack et les différentes façons de l'implémenter, vous serez sans doute confronté à une multitude de différences, qu'il s'agisse des bibliothèques d'Apollo ou de toute la mentalité 'obtenez vos données comme vous le souhaitez' autour de GraphQL et des composants de rendu d'Apollo.

Ce que je veux faire dans cet article, c'est aider à aborder deux des problèmes clés lors de l'écriture d'une mutation. Cela cible principalement les implémentations HOC, mais c'est plus ou moins la même chose pour les composants de rendu, en ajustant les clés d'objet en props.

Plus précisément, nous allons nous plonger directement dans l'optimisticResponse ainsi que les paramètres de mise à jour de votre mutation HOC. J'espère que cela vous rendra plus conscient des options que vous avez lorsque vous implémentez une mutation en tant que fonction prop.

**Important :** Si vous commencez tout juste avec Apollo, je vous implore de tout cœur d'implémenter leurs composants de rendu qu'ils ont publiés autour de la version 2.1. Les HOC sont obsolètes et, à ce titre, manquent de beaucoup de leur documentation, comme mentionné par quelques personnes [ici](https://github.com/apollographql/apollo-client/issues/3253).

### Réponse Optimiste

optimisticResponse est la manière dont nous gérons si notre application est en ligne ou non, ainsi que le statut de nos requêtes vers la base de données.

Si nous mutons notre base de données sans connexion, la réponse optimiste permet à la mutation d'exister avec des variables que nous attendons raisonnablement.

**Par exemple**, si nous supposons que nous allons ajouter cet utilisateur à la base de données :

```
{    userId: 123,    firstName: "Lachlan",    lastName: "Young",    status: "Hungry"}
```

Nous voudrions mettre à jour les détails de notre utilisateur avec les données ci-dessus. Cependant, à cause de la manière dont nos mutations fonctionnent (et cela est spécifique aux HOC mais peut également être appliqué aux composants de rendu), il y a un cycle de vie pour la mutation, passant de loading, à success/fail/can't connect.

Si à un moment donné la mutation échoue mais ne génère pas d'erreur, votre client Apollo sait que cela était dû à autre chose qu'à un mauvais objet. Par cela, je veux dire qu'il prend en compte votre statut hors ligne, le statut de la requête, et il rendra plutôt cet utilisateur dans le composant des détails de l'utilisateur, car il suppose qu'il est valide. Par conséquent, votre client est optimiste.

Lorsque vous vous reconnectez à Internet ou atteignez votre base de données, il mettra à jour la réponse avec les données valides. À l'intérieur de cette réponse, vous pouvez gérer des éléments comme les userId que vous générez sur le client, mettant ainsi à jour mon ID codé en dur de 123, par un UUID.

Si nous n'étions pas en ligne, nous pourrions toujours voir et interagir avec la requête comme prévu et tout changement serait mis en file d'attente pour ensuite muter le serveur lors de la reconnexion.

C'est une réponse optimiste.

### Mise à jour

En ce qui concerne la gestion de la réponse de la base de données, vous avez en fait accès à une propriété appelée **update**, et pour les HOC, cela ressemble à ceci :

```
update: (proxy, { data: { myDetails } }) => {    try {        // Lire les données de notre cache pour cette requête.        const data = proxy.readQuery({             query: gql`${GET_MY_DETAILS}`        });
```

```
        // Ajouter notre nouvelle requête de la mutation à la fin.        data.getMyDetails.push(myDetails);
```

```
        // Écrire nos données dans le cache.        proxy.writeQuery({             query: gql`${GET_MY_DETAILS}`,            data        });    } catch (err) {        console.log('Erreur lors de la mise à jour du cache : ', err.message);    }}
```

Essentiellement, cela vient après le champ optimisticResponse dans la mutation. Il gère directement ce qui se passe après avoir reçu une réponse, prenant en haut les arguments `proxy` et `data`. `Proxy` est littéralement notre client, cependant pour certaines configurations, vous pourriez être mieux servi en le référençant comme le cache. `Data` est la réponse de la mutation. Je l'ai déconstruit, dans ce cas, pour expliquer davantage l'objet myDetails.

**myDetails** se compose de tout ce qui est dans l'objet utilisateur ci-dessus, mais l'id sera maintenant un UUID valide au lieu de 123. Nous utilisons ensuite les méthodes du client Apollo pour lire et écrire et lire les détails que nous avons enregistrés dans notre cache. À partir de là, nous ajoutons nos nouveaux détails et les réécrivons dans le cache. De cette manière, après être retourné à mes détails depuis la page d'entrée, mes nouveaux détails seront instantanément disponibles car ils sont le point de vérité dans le cache.

### Informations supplémentaires

Au moment de l'écriture, toutes les props de rendu documentées [ici](https://www.apollographql.com/docs/react/api/react-apollo.html#mutation-props), ou vues ci-dessous pour la longévité, peuvent être appliquées à votre mutation HOC. Comme je l'ai mentionné dans l'introduction de cet article, la documentation HOC a effectivement été obsolète. Cependant, les options données ci-dessous peuvent toutes être implémentées en tant que clés de l'objet HOC.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSBBl-U4RRMGxZ6RavWDiL0RRlvTi5-h92MP)
_Props de Mutation **4/12/2018**_

Merci beaucoup d'avoir lu. Vous pouvez généralement me voir flotter autour du Slack Apollo dans les canaux #React-Apollo ou #Apollo-Client. Pour vous inscrire au Slack et obtenir des conseils plus spécifiques, cliquez [ici](https://www.apollographql.com/slack/).