---
title: Combien pouvez-vous cURL ? Une introduction rapide et facile à un outil utile.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T01:36:06.000Z'
originalURL: https://freecodecamp.org/news/how-much-can-you-curl-3c88e2fed3f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tpMS_RxArawIV5OGqtTOHg.jpeg
tags:
- name: api
  slug: api
- name: command line
  slug: command-line
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Combien pouvez-vous cURL ? Une introduction rapide et facile à un outil
  utile.
seo_desc: 'By Miguel Bustamante

  On a good day I can flex a 20 lb weight…twice. Probably. But that’s not the type
  of curling we’re talking about!

  Curl (or cURL), on the other hand, is a small but powerful tool for transferring
  files and data over URLs. On a smal...'
---

Par Miguel Bustamante

Un bon jour, je peux soulever un poids de 20 lb… deux fois. Probablement. Mais ce n'est pas le type de curling dont nous parlons !

Curl (ou cURL), en revanche, est un petit mais puissant outil pour transférer des fichiers et des données via des URLs. À plus petite échelle, il est idéal pour tester les APIs REST. Et, bien que la plupart des développeurs web puissent opter pour d'autres outils comme [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) de Google, cURL s'utilise en ligne de commande et peut vous donner l'impression d'être un vrai hacker informatique avec des compétences dignes de David Lightman (pour les fans de "War Games").

CURL signifie "client" et "URL", car c'est un programme exécuté côté client qui envoie des requêtes HTTP aux URLs. Puisqu'il est open source, vous pouvez le télécharger [ici](https://curl.haxx.se/). Ou, si vous avez déjà [Gitbash](https://git-scm.com/downloads) installé sur votre machine, il est automatiquement inclus.

Pour les besoins de cette introduction rapide, nous aurons besoin d'un serveur qui nous permettra de faire des requêtes, et il semble que [JSON Placeholder](https://jsonplaceholder.typicode.com/) réponde parfaitement à nos besoins. Il s'agit d'une fausse API REST qui, bien que nos requêtes ne modifieront pas réellement la base de données du serveur, nous renverra tout de même la réponse appropriée. Alors, ouvrez cette console et commençons à hacker !

### **Get**

Pour commencer, nous allons essayer une simple requête HTTP "get". Faites défiler jusqu'à la section "Resources" dans JSON Placeholder et examinons les types d'objets sur lesquels nous pouvons faire une requête.

![Image](https://cdn-media-1.freecodecamp.org/images/kCyy9EJv0wgDBRMWbcAqFbKHNZF8-Ux9u3z5)
_Objets à requêter_

Super ! Nous pouvons appeler ces objets en ajoutant "/", puis l'objet que nous voulons dans l'URL. Le nombre à droite de la ligne nous indique combien d'éléments nous obtiendrons avec cette requête. Pour commencer, demandons quelques utilisateurs. Tapez la ligne suivante dans la console :

```
curl https://jsonplaceholder.typicode.com/users
```

Vous devriez voir les dix utilisateurs promis sous forme d'objets JSON. Mais peut-être que je veux seulement le cinquième utilisateur. Nous ajouterons "/5" après l'URL pour obtenir l'utilisateur avec l'ID 5.

```
curl https://jsonplaceholder.typicode.com/users/5
```

Nous voyons l'objet JSON du cinquième utilisateur. Bien, essayons de poster un utilisateur sur le serveur.

### **Post**

"Poster" est le processus de soumission de données au serveur pour qu'elles soient sauvegardées dans la base de données. Pour faire cela avec cURL, examinons ses options. Tapez :

```
curl --help
```

et vous devriez obtenir une série d'options intéressantes que nous pouvons utiliser dans le terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/mKtjAzBrGPgeLjJRjW7fExC3SgYeUK2s8JNB)
_Options pour cURL_

Pour nos besoins, il semble que l'option "-d" ou "--data" fonctionnerait bien. Si nous retournons à la page d'accueil du placeholder, dans la section "Routes", il est indiqué que nous pourrions faire une requête POST à "[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)". Avec cette information, nous allons poster notre propre objet via la console :

```
curl -d "title=Greatest Post Ever Written&body=Body of the Greatest post ever written" https://jsonplaceholder.typicode.com/posts
```

Maintenant, vous verrez le post être "créé" dans la base de données, et il a un ID de 101.

![Image](https://cdn-media-1.freecodecamp.org/images/-zEjFQuC3q32sqCBzwxYpLwvlpsLatdXsf7h)

### **Update**

Parfois, nous devons modifier des objets dans la base de données. Nous ne pouvons modifier que les éléments déjà sauvegardés dans la base de données, et comme il s'agit d'une fausse API REST, notre post n'a pas été réellement sauvegardé. Alors, modifions un post qui existe. Essayons le 56ème. Tapez :

```
curl https://jsonplaceholder.typicode.com/posts/56
```

Et vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/z1-dbP08TUfRBpWmLQgvybxekbAQiBCJ-T8S)
_Post 56_

Il est sauvegardé avec un texte étrange de [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) que nous devrions probablement changer en quelque chose d'intelligible. Nous allons avoir besoin de quelques autres options avec notre commande ici. D'abord, nous devons dire à cURL que c'est une requête "put". Donc, en regardant notre option "--help", il semble que nous puissions utiliser "-X" pour dire à cURL que nous voulons utiliser une commande "PUT".

Ensuite, nous voulons toujours utiliser l'option "-d" pour les nouvelles données que nous prévoyons d'utiliser. Assemblons le tout. Tapez :

```
curl -X PUT -d "title=This is a new title" https://jsonplaceholder.typicode.com/posts/56
```

Et voilà, nous avons changé le titre du post avec l'ID 56 en ce que nous voulions.

![Image](https://cdn-media-1.freecodecamp.org/images/4eOxfEfuubfhDr2FQrC3zu29M4Z8hwLFJonG)
_Nouveau titre pour le post 56_

### **DELETE**

Et maintenant, nous en arrivons à la suppression. Ahh, la suppression. Si tout le reste échoue, détruisez tout ! Nous allons voir un peu du même code que nous avons vu dans la commande PUT, mais tout ce dont nous avons besoin est de donner à cURL une requête DELETE et l'URL du post que nous devons supprimer.

```
curl -X DELETE https://jsonplaceholder.typicode.com/posts/56
```

Remarquez que vous ne recevez rien en retour sauf une nouvelle ligne. Peut-être que sur certaines consoles vous verrez un hash vide ("{}"). Cela indique qu'il n'y a rien à retourner car il a été supprimé.

### Conclusion

Nous n'avons abordé que quelques commandes cURL à un niveau très superficiel. C'est un outil pratique qui peut être utile lorsque vous travaillez sur une intégration complète d'API dans votre application. Je vous suggère de consulter le [manuel](https://curl.haxx.se/docs/manual.html) pour plus de lectures et de jouer avec les différentes options pour voir ce qui pourrait répondre à vos besoins.