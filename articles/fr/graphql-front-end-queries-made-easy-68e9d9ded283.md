---
title: 'GraphQL : les requêtes front-end simplifiées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T19:34:31.000Z'
originalURL: https://freecodecamp.org/news/graphql-front-end-queries-made-easy-68e9d9ded283
coverImage: https://cdn-media-1.freecodecamp.org/images/1*49DDRZhUWvVnH-QNHuSUSw.png
tags:
- name: GraphQL
  slug: graphql
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'GraphQL : les requêtes front-end simplifiées'
seo_desc: 'By Rasheed Bustamam

  If you’ve been reading about the latest trends in front-end development, you may
  have heard some buzz about something called GraphQL. In this article, we will cover
  what GraphQL is (and isn’t), some best practices behind GraphQL, ...'
---

Par Rasheed Bustamam

Si vous avez lu les dernières tendances en matière de développement front-end, vous avez peut-être entendu parler de quelque chose appelé GraphQL. Dans cet article, nous allons couvrir ce qu'est GraphQL (et ce qu'il n'est pas), quelques bonnes pratiques derrière GraphQL, et surtout, pourquoi il facilite grandement votre travail en tant que développeur front-end.

*Remarque : Cet article n'est pas destiné à être un tutoriel sur GraphQL. Il est simplement destiné à décrire pourquoi GraphQL facilite votre travail en tant que développeur front-end.*

### Qu'est-ce que GraphQL ?

GraphQL est un langage de requête créé par Facebook. Il vous permet, en tant que développeur front-end, d'écrire des requêtes qui ont exactement la forme de données que vous souhaitez.

Il est important de noter que malgré le nom « GraphQL », il n'est *pas* destiné à être un langage de base de données. En fait, j'ai utilisé GraphQL avec de nombreuses bases de données, y compris SQL, MongoDB, et même une API REST connectée à une base de données (et je ne sais même pas dans quel langage la base de données était écrite).

Au lieu de cela, GraphQL sur le serveur vous permet de définir comment vous souhaitez récupérer vos données. Ensuite, sur le client, vous pouvez exécuter une requête qui a exactement la forme de données que vous souhaitez, et les données que vous recevez auront la même forme que la requête.

Par exemple :

La réponse que vous recevez ressemblera à quelque chose comme ceci :

Il y aura d'autres métadonnées dans la réponse, mais vous pouvez déjà voir à quel point GraphQL est puissant — pas besoin de normaliser vos données sur le client. Le travail est poussé vers le serveur.

Puisque cet article est plus orienté vers les développeurs front-end, je n'entrerai pas dans trop de détails sur le fonctionnement de GraphQL sur le serveur. Cependant, ce qui fait que la « magie » se produit est le schéma GraphQL, qui vous permet de définir des types utilisés à la fois sur le serveur et le client. Voici un exemple de schéma pour une application hypothétique :

En regardant simplement le schéma, vous pouvez déjà savoir quelle sera la forme de vos données et quels types sont attendus. Cela vous permet, en tant que développeur front-end, de connaître plusieurs propriétés importantes d'une requête, telles que si elle prend des arguments, si c'est une liste ou simplement une « entité », et si c'est une entité spécifique, quels champs cette entité possède (dans ce cas, l'entité `User` a les champs `name` et `email`).

Dans le cas de la requête `user`, nous pouvons voir qu'elle prend un argument appelé `username`, qui a un type `String`. Le `!` indique que le champ est requis, donc si il n'est pas fourni, une erreur sera levée.

En tant que développeur front-end, vous ne travaillerez probablement pas trop avec le schéma, mais il servira de document important qui vous permettra de savoir quelles requêtes vous êtes autorisé à faire.

Comparez cela à d'autres normes d'API, telles que Swagger pour les API REST — vous devez faire confiance à la personne qui a écrit la documentation pour qu'elle l'ait bien écrite, avec tous les cas limites et types documentés. Swagger n'implique pas exactement de vérification de type pour différents champs et autres, donc vous pouvez avoir un fichier YAML Swagger valide qui reste incroyablement difficile à naviguer.

Cependant, tout schéma GraphQL valide en lui-même sera immensément utile pour savoir avec quels types de données vous travaillez, même s'il n'est pas correctement commenté et documenté.

Ce n'est pas destiné à critiquer Swagger ou à dire qu'il est terrible — utilisé correctement, Swagger peut être très utile. Mais c'est le bémol — il doit être utilisé correctement, et comme les développeurs ont tendance à avancer extrêmement vite, une documentation appropriée peut souvent passer au second plan par rapport à la construction de nouvelles fonctionnalités/API passionnantes.

### Comment utiliser GraphQL sur le client

C'est amusant. Côté client, il existe de nombreuses façons d'utiliser GraphQL.

L'une des façons les plus populaires d'utiliser GraphQL est d'utiliser une bibliothèque appelée [**apollo-client**](https://github.com/apollographql/apollo-client). Apollo Client peut interfacer avec [React](https://www.apollographql.com/docs/react/), [Vue](https://github.com/akryum/vue-apollo), [Angular](https://www.apollographql.com/docs/angular/), et plus encore.

Maintenant, Apollo Client a récemment mis à jour vers la version 2.0. Elle n'est absolument *pas* rétrocompatible avec la version 1.0, avec de nombreux packages changeant de noms et des API entières changeant. Je me familiarise lentement avec la version 2.0, mais il y a encore certaines choses que je pouvais faire dans la 1.0 que je ne peux plus faire dans la 2.0, comme l'intégration de Redux dans mes applications React. Pour cette raison, je considérerais 1.0 et 2.0 comme des façons entièrement différentes d'utiliser GraphQL sur le client.

Cependant, le concept global est le même : enveloppez toute votre application dans un Apollo Provider (similaire à ce que vous feriez avec Redux), et maintenant tous vos composants ont accès au client, et peuvent écrire des requêtes et des mutations vers le serveur.

Apollo Client fait beaucoup de choses « derrière les scènes » que vous attendez *devraient* être standard mais qui ne le sont apparemment pas. Un exemple est le « batching » des requêtes. Si je charge un composant qui charge deux requêtes différentes, par défaut, deux requêtes différentes sont envoyées. Cependant, Apollo Client a l'option de « batcher » ces requêtes, ce qui place les deux requêtes dans une seule demande et l'envoie au serveur, économisant ainsi quelques requêtes HTTP.

Apollo Client dispose également d'une fonctionnalité de cache très robuste, qui fait que les composants récupèrent d'abord les données depuis le cache. Ensuite, il envoie réellement une requête si le cache est obsolète (généralement 100 ms, mais cela peut être configuré).

Voici un exemple d'instanciation d'un Apollo Client et d'exécution d'une requête :

Cela n'utilise même pas React. Si vous deviez implémenter React, vous pourriez alors attacher la requête au composant React afin qu'il reçoive les données de la requête en tant que props.

L'autre façon d'utiliser GraphQL sur le client est d'utiliser [**Relay**](https://facebook.github.io/relay/), qui ne fonctionne qu'avec React. Désolé pour les développeurs Vue, vous ne pouvez pas utiliser Relay.

Je n'ai pas trop utilisé Relay, mais il a définitivement une courbe d'apprentissage plus raide qu'Apollo. Il semble que vous deviez « DIY » pour beaucoup de choses, comme la mise en cache et même l'implémentation du schéma. Vous pouvez jeter un œil à certains des [exemples ici](https://github.com/relayjs/relay-examples) pour avoir un aperçu de comment Relay fonctionne, et comment il est similaire et différent d'Apollo.

Une fois que vous avez configuré Relay, il fonctionne en réalité très similaire à la façon dont Apollo Client et react-apollo fonctionnent ensemble, en ce sens qu'il envoie les données en tant que props au composant.

### Conclusion

J'espère que cet article vous a été utile pour décider si vous devriez utiliser GraphQL ou non. Pour moi, simplement connaître la forme des données entrantes facilite énormément mon travail front-end. Et si les données n'arrivent pas correctement, alors je les modifie dans le schéma côté back-end, et je mets à jour tout code serveur nécessaire.

Si cet article a piqué votre intérêt pour apprendre GraphQL, je vous suggère de jeter un œil plus approfondi au tutoriel officiel GraphQL : [How to GraphQL](https://www.howtographql.com/).

Amusez-vous bien à faire des requêtes !