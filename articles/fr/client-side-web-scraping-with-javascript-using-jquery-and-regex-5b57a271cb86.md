---
title: Web scraping côté client avec JavaScript en utilisant jQuery et Regex
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T20:15:31.000Z'
originalURL: https://freecodecamp.org/news/client-side-web-scraping-with-javascript-using-jquery-and-regex-5b57a271cb86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*osMYA6WEFDoZdZOUTRJXkQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Web scraping côté client avec JavaScript en utilisant jQuery et Regex
seo_desc: 'By Codemzy

  When I was building my first open-source project, codeBadges, I thought it would
  be easy to get user profile data from all the main code learning websites.

  I was familiar with API calls and get requests. I thought I could just use jQuery
  t...'
---

Par Codemzy

Lorsque je construisais mon premier projet open-source, codeBadges, je pensais qu'il serait facile d'obtenir les données de profil des utilisateurs de tous les principaux sites d'apprentissage de la programmation.

J'étais familier avec les appels API et les requêtes get. Je pensais que je pourrais simplement utiliser jQuery pour récupérer les données des différentes API et les utiliser.

```js
var name = 'codemzy';

$.get('https://api.github.com/users/' + name, function(response) {
  var followers = response.followers;
});
```

Eh bien, c'était facile. Mais il s'avère que tous les sites web n'ont pas une API publique à partir de laquelle vous pouvez simplement récupérer les données que vous voulez.

![Image](https://cdn-media-1.freecodecamp.org/images/zTDeTtBr0aKKlCARmCqeZ1fnRGso-ewAdAnd)
_404 : API non trouvée_

Mais juste parce qu'il n'y a pas d'API publique ne signifie pas que vous devez abandonner ! Vous pouvez utiliser le web scraping pour récupérer les données, avec seulement **un peu de travail supplémentaire**.

Voyons comment nous pouvons utiliser le web scraping côté client avec JavaScript.

Pour un exemple, je vais récupérer mes informations utilisateur de mon profil public freeCodeCamp. Mais vous pouvez utiliser ces étapes sur n'importe quelle page HTML publique.

La première étape pour extraire les données est de récupérer le code HTML complet de la page en utilisant une requête `.get` de jQuery.

```js
var name = "codemzy";

$.get('https://www.freecodecamp.com/' + name, function(response) {
  console.log(response);
});
```

Super, tout le code source de la page vient d'être enregistré dans la console.

Note : Si vous obtenez une erreur à ce stade du type `No 'Access-Control-Allow-Origin' header is present on the requested resource`, ne vous inquiétez pas. Faites défiler jusqu'à la section **Ne laissez pas CORS vous arrêter** de cet article.

C'était facile. En utilisant JavaScript et jQuery, le code ci-dessus demande une page à [www.freecodecamp.org](http://www.freecodecamp.org), comme le ferait un navigateur. Et freeCodeCamp répond avec la page. Au lieu qu'un navigateur exécute le code pour afficher la page, nous obtenons le code HTML.

Et c'est ce qu'est le web scraping, extraire des données de sites web.

D'accord, la réponse n'est pas exactement aussi nette que les données que nous obtenons d'une API.

![Image](https://cdn-media-1.freecodecamp.org/images/u8HicVak3E1qSTq9eYYtyTdHlbmylt6zkw4A)

Mais... nous avons les données, quelque part là-dedans.

Une fois que nous avons le code source, les informations dont nous avons besoin s'y trouvent, nous devons simplement récupérer les données dont nous avons besoin !

Nous pouvons rechercher dans la réponse pour trouver les éléments dont nous avons besoin.

Supposons que nous voulons savoir combien de défis l'utilisateur a complétés, à partir de la réponse de profil utilisateur que nous avons reçue.

Au moment de l'écriture, les défis complétés par un camper sont organisés dans des tableaux sur le profil utilisateur. Donc, pour obtenir le nombre total de défis complétés, nous pouvons compter le nombre de lignes.

Une façon est d'envelopper toute la réponse dans un objet jQuery, afin que nous puissions utiliser des méthodes jQuery comme `.find()` pour obtenir les données.

```js
// nombre de défis complétés
var challenges = $(response).find('tbody tr').length;
```

Cela fonctionne bien — nous obtenons le bon résultat. Mais ce n'est **pas une bonne façon** d'obtenir le résultat que nous recherchons. Transformer la réponse en un objet jQuery charge en fait toute la page, y compris tous les scripts externes, les polices et les feuilles de style de cette page... Oh oh !

Nous avons besoin de quelques morceaux de données. Nous n'avons vraiment pas besoin que la page se charge, et certainement pas toutes les ressources externes qui l'accompagnent.

Nous pourrions supprimer les balises de script et ensuite exécuter le reste de la réponse à travers jQuery. Pour ce faire, nous pourrions utiliser Regex pour rechercher des motifs de script dans le texte et les supprimer.

Ou mieux encore, pourquoi ne pas utiliser Regex pour trouver ce que nous cherchons en premier lieu ?

```js
// nombre de défis complétés
var challenges = response.replace(/<thead>[\s|\S]*?<\/thead>/g).match(/<tr>/g).length;
```

Et ça marche ! En utilisant le code Regex ci-dessus, nous supprimons les lignes d'en-tête du tableau (qui ne contenaient aucun défi), puis nous faisons correspondre toutes les lignes du tableau pour compter le nombre de défis complétés.

C'est encore plus facile si les données que vous voulez sont simplement là dans la réponse en texte brut. Au moment de l'écriture, les points des utilisateurs étaient dans le html comme `<h1 class="flat-top text-primary">[ 1498 ]</h1>` attendant simplement d'être extraits.

```js
var points = response.match(/<h1 class="flat-top text-primary">\[ ([\d]*?) \]<\/h1>/)[1];
```

Dans le motif Regex ci-dessus, nous faisons correspondre l'élément h1 que nous recherchons, y compris les `[ ]` qui entourent les points, et nous regroupons tout nombre à l'intérieur avec `([\d]*?)`. Nous obtenons un tableau en retour, le premier élément `[0]` est la correspondance entière et le second `[1]` est notre correspondance de groupe (nos points).

Regex est utile pour faire correspondre toutes sortes de motifs dans les chaînes, et c'est génial pour rechercher dans notre réponse afin d'obtenir les données dont nous avons besoin.

Vous pouvez utiliser le même processus en 3 étapes pour extraire les données de profil d'une variété de sites web :

1. Utilisez JavaScript côté client
2. Utilisez jQuery pour extraire les données
3. Utilisez Regex pour filtrer les données pour les informations pertinentes

Jusqu'à ce que je rencontre un problème, CORS.

![Image](https://cdn-media-1.freecodecamp.org/images/2uAuWzx-z3PkOAM5ESjcfsVdghMHXZStBlcu)
_CORS : Accès refusé_

### Ne laissez pas CORS vous arrêter !

CORS ou Cross-Origin Resource Sharing, peut être un vrai problème avec le web scraping côté client.

Pour des raisons de sécurité, les navigateurs restreignent les requêtes HTTP cross-origin initiées depuis des scripts. Et parce que nous utilisons JavaScript côté client sur le front-end pour le web scraping, des erreurs CORS peuvent survenir.

Voici un exemple essayant d'extraire des données de profil de CodeWars...

```js
var name = "codemzy";

$.get('https://www.codewars.com/users/' + name, function(response) {
  console.log(response);
});
```

Au moment de l'écriture, l'exécution du code ci-dessus vous donne une erreur liée à CORS.

S'il n'y a pas d'en-tête `Access-Control-Allow-Origin` de l'endroit où vous extrayez, vous pouvez rencontrer des problèmes.

La mauvaise nouvelle est que vous devez exécuter ces types de requêtes côté serveur pour contourner ce problème.

Quoooooooi, cela est censé être du web scraping côté client ?!

La bonne nouvelle est que, grâce à de nombreux autres développeurs formidables qui ont rencontré les mêmes problèmes, vous n'avez pas à toucher le back-end vous-même.

En restant fermement dans notre script front-end, nous pouvons utiliser des outils cross-domain tels que [Any Origin](http://anyorigin.com/), [Whatever Origin](http://www.whateverorigin.org/), [All Origins](http://multiverso.me/AllOrigins/), [crossorigin](https://crossorigin.me/) et probablement beaucoup d'autres. J'ai constaté que vous devez souvent tester quelques-uns de ces outils pour trouver celui qui fonctionnera sur le site que vous essayez d'extraire.

Revenons à notre exemple CodeWars, nous pouvons envoyer notre requête via un outil cross-domain pour contourner le problème CORS.

```js
var name = "codemzy";
var url = "http://anyorigin.com/go?url=" + encodeURIComponent("https://www.codewars.com/users/") + name + "&callback=?";

$.get(url, function(response) {
  console.log(response);
});
```

Et comme par magie, nous avons notre réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/mEAI00WFdz-ExqkAA2PYZKPsFusHpqn-yYXG)