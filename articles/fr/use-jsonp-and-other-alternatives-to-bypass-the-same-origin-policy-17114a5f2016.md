---
title: Comment utiliser le JSON padding (et autres options) pour contourner la Same
  Origin Policy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T00:00:51.000Z'
originalURL: https://freecodecamp.org/news/use-jsonp-and-other-alternatives-to-bypass-the-same-origin-policy-17114a5f2016
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zbemC10taSnmtxa1n2Tw0w.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment utiliser le JSON padding (et autres options) pour contourner la
  Same Origin Policy
seo_desc: 'By Anthony Ng

  In this article, we will be looking at what JSONP is, its drawbacks, and some alternatives
  to JSONP.

  You may have run into situations where you make an API call from one origin to another.
  For example, we have a page served from localho...'
---

Par Anthony Ng

Dans cet article, nous allons examiner ce qu'est JSONP, ses inconvénients et quelques alternatives à JSONP.

Vous avez peut-être rencontré des situations où vous effectuez un appel API d'une origine à une autre. Par exemple, nous avons une page servie depuis localhost:3000 qui appelle une API depuis localhost:8000.

**Note** : Nous ferons référence à localhost:3000 comme notre serveur client. Nous ferons référence à localhost:8000 comme notre serveur API.

Mais nous voyons cette erreur intimidante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hr7T_kBgvnZwzSDdGF3E9w.png)
_Erreur lors de la tentative d'appel fetch depuis le serveur client vers le serveur API_

C'est la Same-Origin Policy qui nous protège. Cette politique restreint la manière dont les ressources d'une origine interagissent avec les ressources d'une autre origine. C'est un mécanisme de sécurité critique dans le navigateur. Mais il existe des cas où nous voulons faire des requêtes cross-origin vers des ressources de confiance.

JSONP (JSON avec Padding) fournit une solution de contournement pour ce problème de Same-Origin Policy. Regardons comment JSONP est apparu.

### Plongée technique

Nous pouvons exécuter du code JavaScript à l'intérieur de notre fichier HTML avec des balises `<script>`.

Nous pouvons déplacer notre code JavaScript dans un fichier JavaScript séparé et le référencer avec notre balise script. Notre page web fait maintenant un appel réseau externe pour le fichier JavaScript. Mais fonctionnellement, tout fonctionne de la même manière.

Le fichier JavaScript n'a pas besoin d'avoir une extension `js`. Le navigateur interprétera le contenu comme du JavaScript si le Content-Type de la Réponse est JavaScript. (`text/javascript`, `application/javascript`).

La plupart des serveurs vous permettent de définir le type de contenu. Dans [Express](https://expressjs.com), vous feriez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*llfbidT6kG5hfSNdfc2nlw.png)
_Définition de l'en-tête Content-Type pour la Réponse_

Votre balise `<script>` peut référencer une URL qui n'a pas d'extension js.

Les balises script ne sont pas limitées par la Same-Origin Policy. Il existe d'autres balises, telles que `<img>` et `<video>`, qui ne sont pas limitées par la Same-Origin Policy. Ainsi, notre JavaScript peut résider sur une origine différente.

Le code à l'intérieur du fichier JavaScript a accès à tout ce qui est dans la portée. Vous pouvez utiliser des fonctions définies précédemment dans votre fichier HTML.

Vous pouvez passer des arguments comme vous le feriez pour un appel de fonction normal.

Dans l'exemple ci-dessus, nous avons passé une chaîne de caractères codée en dur. Mais nous pourrions également passer des données provenant d'une base de données. Notre serveur API peut construire le fichier JavaScript avec ces informations dynamiques.

C'est ce qu'est JSONP. Au lieu d'utiliser `[fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)` ou `[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)` pour faire un appel API afin de récupérer des données, nous avons utilisé une balise `<script>`. Parce que nous avons utilisé une balise `<script>`, nous avons pu contourner la Same-Origin Policy.

Comme je l'ai mentionné ci-dessus, JSONP signifie JSON avec Padding. Que signifie le padding ? Les réponses API normales retournent du JSON. Dans les réponses JSONP, nous retournons la réponse JSON entourée (ou rembourrée) avec une fonction JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zbemC10taSnmtxa1n2Tw0w.png)
_Représentation artistique de JSON avec Padding_

La plupart des serveurs vous permettent de spécifier le nom de votre fonction de padding.

Le serveur prend le nom de votre fonction de padding comme une requête. Il invoque votre fonction de padding avec les données JSON comme argument.

Vous n'êtes pas limité à passer des noms de fonctions comme votre callback. Vous pouvez passer du JavaScript en ligne dans votre requête.

Je n'ai pas pensé à une raison de faire cela.

### Alternatives à l'utilisation de JSONP

Il n'existe pas de spécification officielle pour JSONP. Je considère JSONP comme une astuce.

Les balises `<script>` ne peuvent faire que des requêtes GET. Donc JSONP ne peut faire que des requêtes GET.

[Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) a une spécification officielle et est la manière préférée de contourner la Same-Origin Policy.

Vous pouvez activer le Cross-Origin Resource Sharing en ajoutant un en-tête à notre Réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CdIror6QvF0F1e82W1WbPA.png)

Cela signifie que toutes les origines peuvent utiliser cette ressource sans craindre la Same-Origin Policy.

Parfois, vous n'avez pas le contrôle sur le code serveur. Vous ne pourriez pas inclure l'en-tête `Access-Control-Allow-Origin`. Une solution alternative est de faire en sorte que votre propre serveur proxy fasse la requête cross-origin pour vous. La politique Same-Origin ne s'applique qu'au navigateur. Les serveurs sont libres de faire des requêtes cross-origin.

Des questions ? Des commentaires ? Veuillez laisser un message ci-dessous.

### Ressources

* [Same Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
* [Dépôt Github avec des exemples JSONP et CORS](https://github.com/newyork-anthonyng/jsonp-example.)
* [Explication détaillée de JSONP](https://web.archive.org/web/20160304044218/http://www.json-p.org/)