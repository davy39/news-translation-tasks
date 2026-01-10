---
title: GraphQL VS REST – Avantages et Comparaisons de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-18T23:26:50.000Z'
originalURL: https://freecodecamp.org/news/graphql-vs-rest-benefits-and-code-example-comparisons
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60524e9d28094f59be25788f.jpg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: REST API
  slug: rest-api
seo_title: GraphQL VS REST – Avantages et Comparaisons de Code
seo_desc: "By Veronica Stork\nREST was not the first protocol for sending information\
  \ over the web. But for over a decade, it has dominated the API landscape. \nMore\
  \ recently, GraphQL, a newcomer designed by Facebook, has become more and more popular.\
  \ It is inten..."
---

Par Veronica Stork

REST n'était pas le premier protocole pour envoyer des informations sur le web. Mais depuis plus d'une décennie, il domine le paysage des API.

Plus récemment, GraphQL, un nouveau venu conçu par Facebook, est devenu de plus en plus populaire. Il est destiné à corriger certaines des faiblesses de REST, mais aucune technologie n'est parfaite.

Quels sont les avantages de GraphQL par rapport à REST, et pourquoi utiliseriez-vous l'un plutôt que l'autre dans votre projet ?

## Problèmes avec les API REST

Tout d'abord, discutons de certaines des faiblesses de REST et de la manière dont GraphQL tente de les résoudre. Il y en a trois principales : les allers-retours excessifs vers le serveur, la sur/sous-récupération et un manque général de flexibilité.

### Trop d'Allers-Retours vers le Serveur avec les API REST

Supposons que nous créons une application de médias sociaux. Le fil d'actualité pourrait afficher les publications les plus récentes de tous les utilisateurs, ainsi que les noms d'utilisateur et les photos de profil.

Avec REST, vous devriez, par exemple, envoyer une requête GET à _/api/posts_ pour obtenir les publications, ce qui retournerait probablement un objet JSON contenant le titre de la publication, le contenu, les tags, la date et peut-être l'ID de l'utilisateur.

Ensuite, vous devriez peut-être envoyer une requête GET à _/api/users/:id/_ pour chaque publication afin d'obtenir des informations sur les noms d'utilisateur, les avatars et toute autre information pertinente.

Lorsque vous considérez que vous faites peut-être une requête GET pour chaque utilisateur, cela fait beaucoup d'allers-retours pour une seule page !

Avec GraphQL, vous pouvez faire un seul aller-retour vers le serveur et obtenir tout ce dont vous avez besoin :

```js
query {
    posts {
        title,
        content,
        tags,
        date,
        user {
        	username,
            avatar,
            catchphrase,
            favorite_dog
        }
    }
}
```

À petite échelle, plusieurs allers-retours vers le serveur ne sont pas un gros problème. Mais une fois que vous travaillez avec une tonne de données, vous bénéficierez évidemment de la réduction des appels API au minimum. GraphQL rend cela facile à accomplir.

### Sur- et Sous-Récupération dans les API REST

Un problème lié est celui de la sur- et sous-récupération. Dans une API REST, lorsque vous appelez un endpoint, vous obtiendrez toujours les mêmes données en retour, que vous en ayez besoin ou non.

Supposons que nous avons juste besoin du nom d'utilisateur et de l'avatar de quelqu'un. Si _/user/:id_ retourne son nom d'utilisateur, son avatar, sa phrase d'accroche et sa race de chien préférée, vous obtiendrez toutes ces informations, que vous les vouliez ou non.

À l'autre extrémité du spectre, vous pouvez vous retrouver à sous-récupérer, ce qui nécessite de retourner vers le serveur pour plus d'informations, comme décrit dans la section précédente.

Pour afficher les publications d'un seul utilisateur, nous avons besoin à la fois des informations de l'utilisateur et du contenu des publications. Si je récupère l'utilisateur depuis l'endpoint utilisateur, je dois encore appeler l'endpoint des publications, et, en utilisant l'ID utilisateur, récupérer les publications.

```js
// D'abord, nous obtenons les informations de l'utilisateur
GET /api/users/42

{
    "username": "Mr. T",
    "avatar": "http://example.com/users/42/pic.jpg",
    "catchphrase": "I pity the fool",
    "favorite_dog": "beagle"
}

// Ensuite, nous obtenons leurs publications
GET /api/users/42/posts

{
    "posts": [{
        "title": "Hello World",
        "content": "Hi everyone!"
        "tags": "first post"
        "date": "July 1, 2020"
    }]
    // etc.
}

        
        
    
```

Comme nous l'avons vu dans l'exemple précédent, GraphQL résout ce problème en permettant à l'utilisateur d'utiliser un seul endpoint et de ne récupérer que ce dont il a besoin.

### Manque de Flexibilité dans les API REST

En développant le point précédent, REST repose sur la création d'API qui correspondent aux besoins du frontend. Si vous pouvez anticiper ce dont le frontend aura besoin lorsqu'il appelle un endpoint particulier, vous pouvez adapter précisément les données récupérées pour correspondre à cette vue.

Cela fonctionne bien lorsque la vue est relativement statique. Mais si votre frontend change fréquemment, vous voudrez une API avec plus de flexibilité dans les données qu'elle retourne.

De même, si votre API est utilisée par une variété de clients différents avec des besoins différents, l'inflexibilité d'une API REST ne conviendra pas à vos besoins.

GraphQL offre cette flexibilité en permettant la récupération de différentes configurations de données.

```js
// Si j'ai juste besoin du nom d'utilisateur et de l'avatar :

query {
	users {
    	username,
        avatar
    }
}

// Si j'ai besoin de leur race de chien préférée aussi.

query {
    users {
        username,
        avatar,
        favorite_dog
    }
}
    
```

## Devez-vous Utiliser REST ou GraphQL ?

Il peut sembler, d'après cet article, que GraphQL est toujours meilleur que REST, mais ce n'est pas nécessairement le cas. Chaque décision architecturale que vous prenez lors de la construction de votre application a ses avantages et ses inconvénients, et ceci n'est pas une exception.

Voici quelques éléments à considérer :

### Si vous avez besoin de quelque chose de facile à utiliser, choisissez GraphQL.

Faire du REST correctement a une courbe d'apprentissage, et si vous ne le connaissez pas déjà, vous aurez plus de facilité à créer une excellente API si vous utilisez GraphQL.

> En optant pour GraphQL, vous obtiendrez généralement une bien meilleure API que si vous tentiez de construire une API REST sans comprendre ses concepts. -[Zdenek "Z" Nemec](https://goodapi.co/blog/rest-vs-graphql)

### Si vous utilisez GraphQL, décidez comment vous allez gérer les erreurs

Les API REST sont mieux à même de tirer parti des fonctionnalités de rapport d'erreurs de HTTP. Si vous ne voulez pas obtenir un statut 200 OK pour les erreurs côté client (comme c'est courant dans GraphQL), vous devrez réfléchir un peu plus à la gestion des erreurs.

### REST peut être meilleur pour les microservices

Si vous utilisez des microservices en backend, REST pourrait mieux convenir à vos besoins, car il est conçu pour garder les préoccupations séparées.

Le "graph" unifié de données de GraphQL est génial si vous n'avez pas besoin d'utiliser différentes ressources disparates, éventuellement écrites dans différents langages de programmation, mais moins utile si vous avez un backend plus distribué.

### Considérez la mise en cache

La mise en cache est quelque chose qui est intégrée avec REST, mais que vous devrez gérer vous-même avec GraphQL. Toute l'efficacité accrue que vous pourriez obtenir grâce à la récupération plus ciblée de GraphQL pourrait être annulée si vous ne construisez pas de mise en cache là où c'est approprié.

## Conclusion

Comme pour tout, il y a des compromis à considérer lors du choix entre REST et GraphQL. Celui que vous choisirez pour votre projet dépendra de vos besoins et ressources.