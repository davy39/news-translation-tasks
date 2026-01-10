---
title: Comment créer un raccourcisseur d'URL simple avec seulement HTML et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-11T06:15:10.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-url-shortener-with-just-html-and-javascript-6ea1ecda308c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8L64PM8OQXszS_rH.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un raccourcisseur d'URL simple avec seulement HTML et JavaScript
seo_desc: 'By Palash Bauri

  You might have used a URL shortener before, such as bit.ly, goo.gl. They are useful
  for shortening long URLs so that you can easily share them with your friends, family
  or co-workers.

  You might be wondering how these things work. To u...'
---

Par Palash Bauri

Vous avez peut-être déjà utilisé un raccourcisseur d'URL, comme [bit.ly](https://bit.ly), [goo.gl](https://goo.gl). Ils sont utiles pour raccourcir les longues URL afin que vous puissiez facilement les partager avec vos amis, votre famille ou vos collègues.

Vous vous demandez peut-être comment ces outils fonctionnent. Pour comprendre cela, nous devons examiner de plus près un raccourcisseur d'URL — nous allons donc en construire un simple ! Avec cette tâche, nous allons apprendre de nouvelles choses ainsi que comprendre comment fonctionne un raccourcisseur d'URL.

Aujourd'hui, nous allons construire un raccourcisseur d'URL simple qui n'a pas besoin d'un système de base de données pour l'héberger. Au lieu de cela, nous utiliserons [jsonstore.io](https://jsonstore.io). Je vais supposer que vous connaissez déjà les bases de HTML et JavaScript.

Alors sans plus attendre, commençons à construire...

### Commencez avec le HTML

Nous n'aurons besoin que d'une zone de texte, d'un bouton et d'une balise script pour créer notre raccourcisseur d'URL.

Tout d'abord, créez un fichier HTML appelé `index.html`, car il n'y a besoin que de ces deux éléments (une zone de texte et un bouton).

Alors commençons à ajouter nos trois éléments principaux :

```
<html> <body> <input type="url" id="urlinput"> <button onclick="shorturl()">Raccourcir l'URL</button> <script src="main.js"></script> </body></html>
```

Comme je vous l'ai montré dans le code ci-dessus, j'ai créé un fichier HTML simple. À l'intérieur des balises body, il n'y a que trois éléments : un `input`, un `button` et un `script`.

Le premier élément est `input` où nous taperons/collerons notre longue URL. Je lui ai donné un identifiant `urlinput` pour qu'il soit facile d'y accéder en JavaScript.

L'élément suivant est un `button`. Lorsque nous cliquons sur ce bouton, notre longue URL sera raccourcie car elle a une fonction `onclick` qui sera exécutée lorsque nous cliquerons sur le bouton. Et à l'intérieur de la fonction `shorturl()`, il y aura des commandes nécessaires pour raccourcir l'URL.

À la fin, nous avons un `script` appelé `main.js` où tout notre code JavaScript principal sera. La fonction `shorturl()` mentionnée ci-dessus s'y trouvera également.

Donc, pour l'instant, notre partie HTML est complète. Commençons à écrire un peu de JavaScript.

### Commencez à écrire un peu de JavaScript

Comme nous l'avons montré ci-dessus, nous aurons besoin de JavaScript pour créer notre raccourcisseur d'URL.

**Étape 0 :** comme je l'ai mentionné, nous utiliserons **jsonstore.io** pour stocker des informations sur notre longue URL. Nous aurons besoin d'une URL de **point de terminaison** **jsonstore.io** pour stocker les données, vous pouvez donc visiter [jsonstore.io](https://jsonstore.io) où vous verrez quelque chose comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Z7nKP7sEB4Lu2PGz64A9-WkBvLlitPw3z64e)

Sous le texte _This Is Your Endpoint_, vous pouvez voir une zone de texte avec une longue URL comme celle-ci :

`[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1)`

Cliquez sur le bouton violet _COPY_.

Alors maintenant, commençons à écrire un peu de JavaScript...

Créez un fichier JavaScript appelé `main.js` et commencez à suivre les étapes ci-dessous.

Tout d'abord, nous devons garder le lien copié comme une variable :

```
var endpoint = "https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1";
```

Ensuite, nous devons générer une chaîne aléatoire afin que nous puissions créer un lien entre l'URL courte et l'URL longue.

> _Supposons que nous avons une URL aléatoire `abcd`, notre raccourcisseur d'URL simple est hébergé sur [https://shortner.com](https://shortner.com) et nous avons raccourci l'URL [https://google.com](https://google.com) avec cette URL aléatoire. Donc, chaque fois que nous allons sur [https://shortner.com/#abcd](https://shortner.com/#abcd), nous serons redirigés vers [https://google.com](https://google.com)_

Alors, maintenant, nous allons créer une fonction appelée `getrandom()` :

```
function getrandom(){    var random_string = Math.random().toString(32).substring(2, 5) + Math.random().toString(32).substring(2, 5);    return random_string}
```

Ne vous inquiétez pas, je vais vous aider à comprendre le code ci-dessus.

Tout d'abord, nous avons initié une fonction appelée `getrandom`. Ensuite, nous avons initialisé une variable appelée `random_string` et lui avons donné une valeur.

`Math` est un objet JavaScript intégré qui nous permet d'effectuer des tâches mathématiques sur des nombres. Tout d'abord, nous avons appelé la fonction `random` de `Math`, `Math.random()` retourne un nombre aléatoire entre 0 (inclus) et 1 (exclus).

> _Vous pouvez en apprendre davantage sur l'objet `Math` à partir d'[ici](https://www.w3schools.com/js/js_math.asp)._

Ensuite, nous transformons le nombre retourné en une chaîne en utilisant `toString()` et nous lui donnons un argument de 32 afin que nous obtenions une chaîne correcte et non une chaîne binaire, hexadécimale ou octale.

Ensuite, nous utilisons `substring(2,5)` pour découper la chaîne et maintenir la taille de la chaîne. Ensuite, nous suivons à nouveau la même procédure pour obtenir un autre morceau de chaîne aléatoire, et enfin nous ajoutons les deux morceaux de la chaîne en utilisant `+`.

Et n'oubliez pas d'ajouter une instruction `return` qui retourne notre chaîne aléatoire.

> _Rappelez-vous, ce n'est pas la seule façon de générer des chaînes aléatoires. Vous pouvez également utiliser la méthode mentionnée ci-dessous pour atteindre l'objectif :_

```
function getrandom() {    var text = "";    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";   
```

```
    for (var i = 0; i < 5; i++)        text += possible.charAt(Math.floor(Math.random() * possible.length));    return text;}
```

Maintenant, retournez à `index.html` et ajoutez JQuery car il sera plus facile d'atteindre nos objectifs si nous utilisons JQuery. Ajoutez-le à la fin de la balise body mais avant la balise de script `main.js`.

Maintenant, retournez à nouveau à `main.js`.

Créons une fonction appelée `geturl` qui prendra la valeur de la zone de texte, la vérifiera et retournera la valeur :

```
function geturl(){     var url = document.getElementById("urlinput").value;     var protocol_ok = url.startsWith("http://") || url.startsWith("https://") || url.startsWith("ftp://");     if(!protocol_ok){         newurl = "http://"+url;         return newurl;     }else{         return url;     }}
```

Dans la fonction `geturl`, nous stockons d'abord la valeur de la zone de texte dans la variable `url`. Ensuite, nous vérifions si les protocoles d'URL sont corrects ou non. Si le protocole ne commence pas par `http://`, `https://` ou `ftp://`, nous ajoutons `http://` au début de l'URL puis retournons l'URL.

> En fait, ce n'est pas une méthode sûre. Vous devriez utiliser une regex pour valider vos URL ! Mais je veux garder cet article facile à comprendre.

Maintenant, nous aurons besoin d'une autre fonction pour changer le hash dans la barre de localisation, alors créons-la :

```
function genhash(){    if (window.location.hash == ""){        window.location.hash = getrandom();    }}
```

Tout d'abord, nous vérifions si l'emplacement du hash est vide. S'il est vide, nous ajoutons un hash aléatoire à la barre de localisation.

> _Exemple : si notre URL est [https://example.com/#abcd](https://example.com/#abcd), la valeur de `window.location.hash` sera `#abcd`._

Ensuite, nous travaillerons sur notre fonction principale `shorturl()`, alors allons-y...

```
function shorturl(){    var longurl = geturl();    genhash();    send_request(longurl);}
```

Tout d'abord, nous stockons la longue URL dans la variable `longurl`. Ensuite, nous ajoutons un hash aléatoire à la barre de localisation afin que nous puissions utiliser l'URL comme URL courte. Ensuite, nous appelons la fonction `send_request()` avec un argument `longurl`. Dans cette fonction, nous envoyons une requête JSON à **jsonstore** pour stocker la longue URL avec un lien vers l'URL courte. Alors maintenant, créons la fonction `send_request()`.

```
function send_request(url) {    this.url = url;    $.ajax({        'url': endpoint + "/" + window.location.hash.substr(1),        'type': 'POST',        'data': JSON.stringify(this.url),        'dataType': 'json',        'contentType': 'application/json; charset=utf-8'    })}
```

Ici, nous utilisons JQuery pour envoyer la requête JSON à **endpoint+"/" + notre hash de chaîne aléatoire de la barre de localisation.** Par exemple :

`[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd)`

Ainsi, chaque fois que nous envoyons une requête GET à l'URL mentionnée ci-dessus, nous obtiendrons la longue URL comme `data`.

**Important** : ajoutez la fonction `send_request()` avant la fonction `shorturl()`, sinon cela ne fonctionnera pas.

> _Pour en savoir plus sur la fonction Ajax de JQuery, allez [ICI](https://www.w3schools.com/jquery/ajax_ajax.asp). Pour en savoir plus sur JSON, allez [ICI](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)._

Maintenant, nous utiliserons le code pour obtenir la longue URL liée à l'URL courte entrée dans la barre d'adresse :

```
var hashh = window.location.hash.substr(1)
```

```
if (window.location.hash != "") {    $.getJSON(endpoint + "/" + hashh, function (data) {        data = data["result"];
```

```
if (data != null) {            window.location.href = data;        }
```

```
});
```

Ensuite, le code mentionné ci-dessus sera exécuté chaque fois que nous mettons l'URL courte dans la barre d'adresse (par exemple, [https://shorturl.com/#abcd](https://shorturl.com/#abcd)).

Tout d'abord, nous stockons la valeur de hachage de l'URL dans la variable `hashh`.

> _Exemple : si notre URL courte est [https://shorted.com/#abcd](https://shorted.com/#abcd), la valeur du hachage sera **#abcd.**_

Ensuite, nous vérifions si l'emplacement du hachage est vide ou non. S'il n'est pas vide, nous envoyons une requête GET à l'adresse, `endpoint` + `hashh`.

> _Exemple :_[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd)

Et comme d'habitude, si tout est correct, nous obtiendrons la longue URL à partir des données qui sont des données de tableau JSON, et à partir de celles-ci, nous extrayons le résultat avec `data["result"]`.

> _La valeur des données sera similaire à ceci `{"result":longurl,"ok":true}`, où la longue URL est l'URL que vous avez raccourcie._

Notre raccourcisseur d'URL est presque complet ! Copiez-collez une longue URL dans la zone de texte puis cliquez sur le bouton **Raccourcir l'URL** ! Copiez le lien de la barre d'adresse — c'est votre URL courte !

![Image](https://cdn-media-1.freecodecamp.org/images/KdWpDkClj9ekuuHM47166AbVxkxAT0GlFXvN)

### Quelques astuces utiles

* Nous pouvons ajouter une fonction pour copier automatiquement l'URL courte lorsque l'utilisateur clique sur le bouton **Raccourcir l'URL** en utilisant des bibliothèques comme [SimpleCopy](https://github.com/kyle-rb/simplecopy), ou [ClipboardJS](https://clipboardjs.com/) — elles copieront l'URL courte qui se trouve actuellement dans la barre de localisation.
* Si vous utilisez SimpleCopy, nous pouvons ajouter `simplecopy(window.location.href);` à la fin de la fonction `shorturl()` pour copier l'URL courte chaque fois qu'elle raccourcit une URL.
* Ce raccourcisseur d'URL simple repose sur des bibliothèques tierces comme **jsonstore**, il n'est donc pas judicieux de raccourcir certaines URL longues confidentielles avec celui-ci.
* Vous pouvez héberger l'ensemble du projet sur des pages Github/Gitlab et configurer un simple CNAME. C'est tout — votre tout nouveau raccourcisseur d'URL personnel est prêt ! Vous pouvez utiliser n'importe quel service d'hébergement de site statique pour héberger votre raccourcisseur d'URL.
* Vous pouvez trouver le code source complet du projet sur [GITHUB](https://github.com/bauripalash/simpleurlshortener)

C'est tout pour aujourd'hui ! C'est mon premier guide technique, alors je m'excuse pour toute erreur.

Si vous trouvez des problèmes ou des erreurs, faites-le moi savoir dans les commentaires ci-dessous ?.

Ou contactez-moi sur [Facebook](http://fb.me/bauripalash) ou [Twitter !](https://twitter.com/bauripalash)

Paix !