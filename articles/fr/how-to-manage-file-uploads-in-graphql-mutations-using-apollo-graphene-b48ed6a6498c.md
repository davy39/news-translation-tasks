---
title: Comment gérer les téléchargements de fichiers dans les mutations GraphQL avec
  Apollo/Graphene
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T12:00:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-file-uploads-in-graphql-mutations-using-apollo-graphene-b48ed6a6498c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xCKDdyMn2NKAiufB7jtTwg.png
tags:
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment gérer les téléchargements de fichiers dans les mutations GraphQL
  avec Apollo/Graphene
seo_desc: 'By Lucas McGartland

  GraphQL is an amazing way to query and manipulate data. You describe your data,
  ask for what you want, and get predictable results. The problem is, GraphQL only
  handles serializable data out of the box—there’s no way to upload fil...'
---

Par Lucas McGartland

GraphQL est une manière incroyable d'interroger et de manipuler des données. Vous décrivez vos données, demandez ce que vous voulez, et obtenez des résultats prévisibles. Le problème est que GraphQL ne gère que les données sérialisables par défaut—il n'y a aucun moyen de télécharger des fichiers directement dans vos mutations.

Mais que se passerait-il s'il existait un moyen de combiner la puissance de GraphQL avec la facilité de télécharger des fichiers dans une requête multipartite ? @jaydenseric a trouvé une solution : [**graphql-multipart-request-spec**](https://github.com/jaydenseric/graphql-multipart-request-spec)

> Si vous voulez simplement le code pour faire fonctionner cela, allez à la fin de cet article pour trouver des implémentations JavaScript et Python de la spécification pour Apollo et Graphene.

### Gestion des téléchargements de fichiers avec GraphQL sans téléchargements multipartites (l'ancienne méthode)

GraphQL vanilla ne supporte pas l'envoi de fichiers bruts dans vos mutations. Les données que vous pouvez demander et manipuler sont limitées à ce que vous pouvez sérialiser sur le réseau. En pratique, cela ressemble à des types de base : **nombres, booléens et chaînes de caractères**. Ceux-ci fonctionnent très bien—vous pouvez construire presque tout ce dont vous avez besoin avec des types de données de base.

Mais que faire si vous devez exécuter une mutation qui prend un fichier comme argument ? Par exemple : télécharger une nouvelle photo de profil. Voici comment vous pourriez gérer le problème avec GraphQL ordinaire :

#### Option 1 : Encodage Base64

Encodez l'image en Base64 et envoyez-la sur le réseau sous forme de chaîne dans votre mutation. Cela présente plusieurs inconvénients :

1. Un fichier encodé en Base64 sera environ 33 % plus grand que le binaire d'origine.
2. L'encodage et le décodage du fichier sont des opérations plus coûteuses.
3. Complexité à se souvenir d'encoder et de décoder correctement.

#### Option 2 : Requêtes de téléchargement séparées

Exécutez un serveur séparé (ou une API) pour télécharger des fichiers. Téléchargez le fichier dans la première requête, puis passez l'URL de stockage résultante dans votre mutation (la deuxième requête).

Cependant, si vous devez télécharger plusieurs fichiers, vous devrez attendre que tous les téléchargements soient terminés avant de pouvoir passer les URL (pour les identifier) dans votre mutation, ce qui force un processus synchrone et lent. Cela ajoute également une autre couche de complexité pour gérer toutes ces requêtes séparément dans votre client.

1. Ce n'est pas asynchrone.
2. C'est complexe à gérer avec l'autre serveur de téléchargement.

> Ne serait-il pas cool de simplement passer un fichier dans les paramètres de la mutation ?

### La spécification des requêtes multipartites (la nouvelle méthode)

C'est là que la spécification des requêtes multipartites entre en jeu. Cette spécification d'extension GraphQL vous permet d'imbriquer des fichiers n'importe où dans les mutations GraphQL comme ceci :

```
{  query: `    mutation($file: Upload!) {      uploadFile(file: $file) {        id      }    }  `,  variables: {    file: File // somefile.jpg  }}
```

Comme vous pouvez le voir, ajouter un fichier est aussi simple que d'ajouter n'importe quel autre type de paramètre de mutation. Pour implémenter cette spécification, vous devez installer deux parties : une qui s'exécute sur le client, et une autre qui s'exécute sur le serveur. Voici ce qu'elles font :

* La spécification client définit comment mapper les objets de fichier dans une mutation vers une clé qui localise où ils se trouvent dans une requête multipartite.
* La spécification serveur définit comment analyser cette carte et rendre les fichiers réaccessibles en fonction de la clé fournie dans la carte.

Ainsi, dans apollo-client, vous pouvez exécuter une mutation qui ressemble à ceci :

```
this.props.mutate({variables: {file: yourFile}})
```

### Implémentations de la spécification des requêtes multipartites

Si vous cherchez à implémenter la spécification des requêtes multipartites avec Apollo, vous pouvez facilement l'intégrer avec ces packages écrits par Jayden Seric. Ceux-ci sont pour l'écosystème JavaScript et Apollo.

[**jaydenseric/apollo-upload-client**](https://github.com/jaydenseric/apollo-upload-client)
[_apollo-upload-client - Améliore Apollo Client pour des téléchargements de fichiers intuitifs via les mutations GraphQL._github.com](https://github.com/jaydenseric/apollo-upload-client)[**jaydenseric/apollo-upload-server**](https://github.com/jaydenseric/apollo-upload-server)
[_apollo-upload-server - Améliore Apollo GraphQL Server pour des téléchargements de fichiers intuitifs via les mutations GraphQL._github.com](https://github.com/jaydenseric/apollo-upload-server)

Si vous exécutez votre API GraphQL via Graphene et Django, vous pouvez implémenter la spécification en Python en remplaçant votre vue GraphQL par ce package que j'ai écrit ici :

[**lmcgartland/graphene-file-upload**](https://github.com/lmcgartland/graphene-file-upload)
[_graphene-file-upload - Améliore Graphene Django GraphQL Server pour des téléchargements de fichiers intuitifs via les mutations GraphQL._github.com](https://github.com/lmcgartland/graphene-file-upload)

### Conclusion

Cette spécification est un moyen facile d'ajouter une capacité de téléchargement de fichiers à votre application GraphQL. Concentrez-vous moins sur la manière d'obtenir vos fichiers, et plus sur ce que vous pouvez faire avec eux !

Si vous voulez discuter davantage, parler de GraphQL ou de belles polices, **contactez-moi sur Twitter @[lucasmcgartland](https://twitter.com/lucasmcgartland).** Ou trouvez-moi ailleurs sur le web ci-dessous :

> [Site Web](http://www.lucasmcgartland.com) | [Email](mailto:luke@thebeeinc.com) | [LinkedIn](https://www.linkedin.com/in/lucasmcgartland/) | [Twitter](https://twitter.com/lucasmcgartland) | [Dribbble](https://dribbble.com/lucasmcgartland)

#### Lectures complémentaires :

* [https://medium.com/@danielbuechele/file-uploads-with-graphql-and-apollo-5502bbf3941e](https://medium.com/@danielbuechele/file-uploads-with-graphql-and-apollo-5502bbf3941e)