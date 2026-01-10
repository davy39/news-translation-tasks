---
title: Comment utiliser Google Sheets et Google Apps Script pour créer votre propre
  CMS de blog
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T01:48:32.000Z'
originalURL: https://freecodecamp.org/news/use-google-sheets-and-google-apps-script-to-build-a-blog-cms-c2eab3fb0b2b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ee675JOtyd-tjE6cfk0Tg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment utiliser Google Sheets et Google Apps Script pour créer votre propre
  CMS de blog
seo_desc: 'By Daniel Ireson

  I recently stumbled across Google Apps Scripts, a platform that allows users to
  extend Google’s G Suite of online products through a scripting language derived
  from JavaScript. It’s analogous to VBA, which is built into most of Micro...'
---

Par Daniel Ireson

J'ai récemment découvert [Google Apps Scripts](https://developers.google.com/apps-script/), une plateforme qui permet aux utilisateurs d'étendre la suite G Suite de produits en ligne de Google grâce à un langage de script dérivé de JavaScript. C'est analogue à [VBA](https://msdn.microsoft.com/en-us/vba/office-shared-vba/articles/getting-started-with-vba-in-office), qui est intégré dans la plupart des produits Microsoft Office.

Google Apps Scripts est incroyablement puissant et permet de construire des systèmes complexes sur les services Google. Cela peut être un excellent choix lorsque vous devez rapidement prototyper une idée ou concevoir une solution personnalisable par des utilisateurs non techniques. Une excellente façon de créer une solution accessible est de construire sur des produits que les utilisateurs connaissent déjà.

Dans cet article, je vais vous guider à travers un exemple simple mais novateur de construction d'un « Système de Gestion de Contenu » (CMS) pour un blog en ligne en utilisant Google Sheets, Google Forms et Google Apps Script.

Le blog sera conçu comme une application monopage avec pagination et la possibilité de filtrer par catégorie de publication. Les articles de blog seront stockés dans une feuille de calcul Google Sheets. Les nouveaux articles seront ajoutés via Google Forms, car il offre une interface conviviale. Google Apps Script sera utilisé pour construire une API afin de rendre le contenu de la feuille de calcul disponible dans un format facile à utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/07oxc4724ms4QIehmCYTvmw9-w3Y24UiSLU8)
_[https://danielireson.github.io/google-sheets-blog-cms](https://danielireson.github.io/google-sheets-blog-cms/" rel="noopener" target="_blank" title=")_

#### Avertissement

Je n'utilise pas cela en production, et je ne sais pas si cela passera à l'échelle. Considérez cela comme une preuve de concept pour montrer ce qui est possible. Vous devriez faire vos propres recherches si vous souhaitez l'utiliser dans un environnement de production. Je suspecte que le trafic sera limité si vous approchez des limites supérieures des quotas de service. Il y a une limite stricte de [20 000 requêtes URL](https://developers.google.com/apps-script/guides/services/quotas) par jour sur les scripts pour les comptes Google gratuits, et il peut y avoir d'autres limites en place.

### Stocker les données

Google Sheets sera utilisé comme une base de données en fichier plat pour stocker les articles de blog. Une base de données en fichier plat stocke les données en texte brut dans une seule table. En revanche, une base de données relationnelle capture les relations entre les tables et impose la structure de ces relations pour minimiser la duplication et maximiser l'intégrité des données.

Bien que plus limitée, une structure en fichier plat est facile à démarrer et convient à notre cas d'utilisation pour un petit blog.

#### Structure de la feuille de calcul

Chaque ligne représentera un nouvel article de blog, et les colonnes seront utilisées pour capturer les champs individuels des articles de blog. Dans une structure en fichier plat, il n'y a pas de concept de clés primaires et étrangères comme dans le modèle relationnel. Les informations capturées dans les colonnes, telles que la catégorie et l'auteur, seront dupliquées entre les articles de blog lorsqu'elles sont communes.

#### Pour commencer

Créez une nouvelle feuille de calcul Google Sheets et connectez-la à Google Forms en allant dans **Outils > Créer un formulaire** dans la barre de menu. Après avoir sélectionné cette option, vous serez présenté avec un éditeur pour définir les questions du formulaire. Celles-ci sont mappées aux colonnes de la feuille de calcul.

Pour ma démonstration, j'ai ajouté quatre questions pour **Titre**, **Catégorie**, **Auteur** et **Contenu**.

Chaque champ était de type texte sauf **Catégorie**, qui était un type radio avec quatre catégories hypothétiques : général, marketing, financier, technologie.

![Image](https://cdn-media-1.freecodecamp.org/images/a9K2JlG8UCudNKRgAUmyhtKtc3ASZ2vTVju7)
_[https://docs.google.com/forms/d/1QKthdGK9pznyojcZ4esrU1moky8_Wih4aqa7_uIQ0sw](https://docs.google.com/forms/d/1QKthdGK9pznyojcZ4esrU1moky8_Wih4aqa7_uIQ0sw/closedform" rel="noopener" target="_blank" title=")_

Lorsqu'un formulaire est soumis, une ligne est ajoutée à la feuille de calcul Google Sheets. Un champ **Horodatage** est automatiquement ajouté pour chaque ligne, que nous utiliserons pour calculer la date de publication.

Pour permettre les articles en brouillon, j'ai également ajouté un champ booléen **Publié ?** comme première colonne. L'API ne doit retourner que les articles avec une valeur **true**. Cela permet de réviser et d'éditer les articles avant leur publication.

![Image](https://cdn-media-1.freecodecamp.org/images/z3uEkxyDVTu9Co94vNxUODDqCdSCijV78rHv)
_[https://docs.google.com/spreadsheets/d/1xy6Hz8yagIW7zwdGGC0XICObIoZ_YYhRhnQ1T8GrQnE/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1xy6Hz8yagIW7zwdGGC0XICObIoZ_YYhRhnQ1T8GrQnE/edit?usp=sharing" rel="noopener" target="_blank" title=")_

### Construire l'API

Google Apps Script est basé sur la norme JavaScript ECMAScript 5 (ES5). Lors de la construction de l'API, nous ne pouvons pas utiliser les fonctionnalités ES6 comme les variables scopées, les fonctions fléchées ou les paramètres par défaut. Si vous n'êtes pas sûr de ce qui est disponible en ES5, je vous recommande de consulter les [docs MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript) sur les tableaux de compatibilité.

Malgré l'absence d'ES6, Google Apps Script peut encore être utilisé pour construire des applications raisonnablement complexes sur les produits G Suite.

#### Pour commencer

Vous pouvez accéder à l'éditeur en ligne de Google Apps Script en allant dans **Outils > Éditeur de script** dans la barre de menu de la feuille de calcul Google Sheets. Un éditeur de script s'ouvrira avec un fichier vide nommé **Code.gs**. Comme il s'agit d'une application simple, nous mettrons notre logique dans ce seul script, mais vous pouvez également facilement diviser votre application en scripts séparés.

#### Retourner une réponse

Nous pouvons utiliser les fonctions de rappel `doGet` et `doPost` pour répondre aux requêtes HTTP. Ce sont simplement des fonctions ordinaires que Google Apps Script cherche à invoquer lorsqu'une requête GET ou POST est respectivement faite à l'API.

Pour générer une réponse, nous utiliserons le [ContentService](https://developers.google.com/apps-script/guides/content). Un objet JavaScript peut être passé à `JSON.stringify` puis à `createTextOutput` sur ce service pour construire une réponse JSON. Si le type mime est défini sur `ContentService.MimeType.JSON`, cela définira de manière appropriée le type de contenu sur `application/json`.

Générer une réponse JSON est aussi simple que ce qui suit :

```
function doGet(e) {  var output = JSON.stringify({    status: 'success',    message: 'It worked',  });    return ContentService.createTextOutput(output)    .setMimeType(ContentService.MimeType.JSON);}
```

#### Analyser les requêtes

Le rappel `doGet` est toujours invoqué avec un événement généré à partir de la requête. À partir de cet événement, nous pouvons accéder aux paramètres de la chaîne de requête, que nous utiliserons pour prendre en charge diverses options de l'API. Une authentification simple sans état sera mise en œuvre via un paramètre `key`. Cela vérifiera simplement que la valeur du paramètre `key` correspond à une valeur de clé codée en dur. Les requêtes qui ne correspondent pas afficheront une réponse non autorisée.

Un paramètre `category` sera utilisé afin que les utilisateurs puissent demander des articles d'une seule catégorie. Cela leur évite d'avoir à filtrer par catégorie sur le front-end. La pagination sera également mise en œuvre via un paramètre `page`.

Ces options doivent être ajoutées à l'URL lors de la requête à l'API.

```
GET https://apiurl?key=abcdef&category=general&page=1
```

Cette requête générerait l'événement suivant :

```
{  "queryString": "key=abcdef&category=general&page=1",  "parameter": {},  "contextPath": "",  "parameters": {    "key": [      "abcdef"    ],    "category": [      "general"    ],    "page": [      "1"    ]  },  "contentLength": -1}
```

Authentifions d'abord l'événement. Nous le ferons en vérifiant que `key` a été fourni et qu'il correspond à la clé API définie.

```
var API_KEY = 'abcdef';
```

```
function doGet(e) {  if (!isAuthorized(e)) {    return buildErrorResponse('not authorized');  }      return buildSuccessResponse('authorized');}
```

```
function isAuthorized(e) {  return 'key' in e.parameters && e.parameters.key[0] === API_KEY;}
```

```
function buildSuccessResponse(message) {  var output = JSON.stringify({    status: 'success',    message: message  });    return ContentService.createTextOutput(output)   .setMimeType(ContentService.MimeType.JSON);}
```

```
function buildErrorResponse(message) {  var output = JSON.stringify({    status: 'error',    message: message  });    return ContentService.createTextOutput(output)   .setMimeType(ContentService.MimeType.JSON);}
```

La clé API est définie comme `abcdef` en haut du fichier. La fonction `isAuthorized` retourne une valeur booléenne pour l'authentification. Si cela retourne faux, un message `not authorized` est retourné via l'aide `buildErrorResponse`. Si `isAuthorized` retourne vrai, la fonction est autorisée à continuer jusqu'à ce qu'une réponse réussie soit retournée via `buildSuccessResponse`.

Un inconvénient que j'ai trouvé lors de la construction d'applications sur Google Apps Script est que vous n'avez pas la capacité de définir des codes de statut pour les réponses. Ceux-ci peuvent être utilisés pour indiquer si la réponse a réussi et si ce n'est pas le cas, pourquoi.

Par exemple, un code de statut [401 Non authentifié](https://httpstatuses.com/401) implique que les informations d'identification de l'utilisateur ne correspondaient pas et qu'ils devraient réessayer en utilisant des informations d'identification différentes. Les réponses ont toujours un code de statut [200 OK](https://httpstatuses.com/200) lors de l'utilisation de `doGet`, même pour les réponses non réussies gérées. Je contourne cela en ajoutant une valeur `status` à toutes les réponses de l'API. Pour cet exemple simple, le statut peut être soit `success` soit `error`, mais il est facile de voir comment ce modèle pourrait être étendu pour d'autres statuts plus granulaires si nécessaire.

Créons deux fonctions pour analyser les paramètres `category` et `page`. Si un `page` numérique valide n'est pas fourni, sa valeur par défaut doit être `1`. De même, si une catégorie n'est pas fournie, la valeur par défaut doit être définie sur `null`, auquel cas les articles de toutes les catégories doivent être retournés.

```
function getPageParam(e) {  if ('page' in e.parameters) {    var page = parseInt(e.parameters['page'][0]);    if (!isNaN(page) && page > 0) {      return page;    }  }    return 1}
```

```
function getCategoryParam(e) {  if ('category' in e.parameters) {    return e.parameters['category'][0];  }    return null}
```

#### Lire depuis la feuille de calcul

Google Apps Script rend disponibles divers objets globaux qui peuvent être utilisés pour interagir avec les produits G Suite. Nous utiliserons le [SpreadsheetService](https://developers.google.com/apps-script/reference/spreadsheet/) pour charger notre feuille de calcul par ID et lire les articles de blog. La manière la plus simple de rechercher un ID de feuille de calcul est de vérifier l'URL de Google Sheets.

```
https://docs.google.com/spreadsheets/d/{id}/edit
```

Après avoir chargé la feuille de calcul via la méthode `openById` sur le `SpreadsheetService` global, nous devons obtenir la plage de données active de la première feuille de travail. Pour retourner les articles les plus récents en premier, nous devons trier sur la colonne **Horodatage**, qui est la deuxième colonne.

```
var SPREADSHEET_ID = '12345';var spreadsheet = SpreadsheetApp.openById(SPREADSHEET_ID);var worksheet = spreadsheet.getSheets()[0];var rows = worksheet.getDataRange() .sort({column: 2, ascending: false}) .getValues();
```

Le tableau `rows` de `getDataRange` contient à la fois les en-têtes de colonnes comme premier élément du tableau et les lignes d'articles de blog comme éléments de tableau suivants. Les en-têtes peuvent être mappés aux articles de blog afin que l'API puisse retourner des objets d'articles de blog complets plutôt que simplement les valeurs des colonnes.

```
var headings = rows[0].map(String.toLowerCase);var posts = rows.slice(1);var postsWithHeadings = addHeadings(posts, headings);
```

```
function addHeadings(posts, headings) {  return posts.map(function(postAsArray) {    var postAsObj = {};        headings.forEach(function(heading, i) {      postAsObj[heading] = postAsArray[i];    });        return postAsObj;  });}
```

#### Filtrer les articles non pertinents

Les articles de blog ne doivent être retournés que si leur catégorie correspond à celle demandée, et les articles de toutes les catégories doivent être retournés si une catégorie n'a pas été demandée. Les articles de blog ne doivent également être retournés que s'ils ont une valeur **Publié** de **true**.

Créons une fonction pour supprimer les articles en brouillon par un [filtre de tableau](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) :

```
var postsPublic = removeDrafts(postsWithHeadings);
```

```
function removeDrafts(posts, category) {  return posts.filter(function(post) {    return post['published'] === true;  });}
```

Et une autre fonction pour `filter` sur la catégorie de l'article :

```
var category = getCategoryParam(e);var postsFiltered = filter(postsPublic, category);
```

```
function filter(posts, category) {  return posts.filter(function(post) {    if (category !== null) {      var c1 = post['category'].toLowerCase()      var c2 = category.toLowerCase()      return c1 === c2;    } else {      return true;    }  });}
```

#### Pagination des réponses

Pour des raisons de performance, nous devons limiter le nombre maximum d'articles retournés par une seule réponse de l'API. Le client doit pouvoir demander la page suivante d'articles en augmentant le paramètre de requête `page`.

Mettons cela en œuvre via une fonction de pagination qui retourne un objet contenant les articles de blog filtrés sous `posts` et les liens de pagination sous `pages`. S'il y a plus de résultats ou des résultats précédents, `pages` contient le numéro de page approprié sous `next` et `previous` respectivement.

```
var RESULTS_PER_PAGE = 5;var page = getPageParam(e)var paginated = paginate(postsFiltered, page);
```

```
function paginate(posts, page) {  var postsCopy = posts.slice();  var postsChunked = [];  var postsPaginated = {    posts: [],    pages: {      previous: null,      next: null    }  };    while (postsCopy.length > 0) {    postsChunked.push(postsCopy.splice(0, RESULTS_PER_PAGE));  }    if (page - 1 in postsChunked) {    postsPaginated.posts = postsChunked[page - 1];  } else {    postsPaginated.posts = [];  }
```

```
  if (page > 1 && page <= postsChunked.length) {    postsPaginated.pages.previous = page - 1;  }    if (page >= 1 && page < postsChunked.length) {    postsPaginated.pages.next = page + 1;  }    return postsPaginated;}
```

Notre aide `buildSuccessResponse` de plus tôt peut être mise à jour pour gérer `posts` et `pages`. L'API devrait alors être prête pour le déploiement.

```
function buildSuccessResponse(posts, pages) {  var output = JSON.stringify({    status: 'success',    data: posts,    pages: pages  });    return ContentService.createTextOutput(output)    .setMimeType(ContentService.MimeType.JSON);}
```

#### Déployer l'API

Avec le script finalisé, l'API peut être rendue publique en allant dans **Publier > Déployer comme application web** dans la barre de menu de l'éditeur de script. Assurez-vous que l'application est exécutée **comme** moi et que **toute personne, même anonyme** a accès.

Le déploiement retournera une URL qui ressemblera à celle ci-dessous :

```
https://script.google.com/macros/s/{id}/exec
```

Ajoutez la clé API à l'URL puis entrez-la dans votre navigateur web pour vérifier que l'API fonctionne correctement. Espérons que vous devriez voir une réponse JSON avec trois clés de premier niveau : `status`, `posts`, `pages`.

```
https://script.google.com/macros/s/{id}/exec?key=abcdef
```

### Résumé

Si vous avez suivi, vous devriez maintenant avoir un CMS fonctionnel construit sur Google Sheets, Google Forms et Google Apps Script. Ce n'est pas avancé, mais c'était facile à démarrer et répond aux exigences de base d'un CMS. Le connecter à un front-end était hors du cadre de cet article, mais si vous voulez voir comment cela est fait, vous devriez consulter la démonstration que j'ai mise ensemble [sur GitHub](https://github.com/danielireson/google-sheets-blog-cms).

La prochaine fois que vous êtes sur le point d'utiliser la technologie à la mode du jour, je vous défie de prendre quelques instants pour réfléchir s'il existe une solution plus simple qui peut être construite en utilisant des logiciels existants. Cette solution ne sera peut-être pas entièrement fonctionnelle, mais elle vous mènera souvent [à 80 % du résultat pour 20 % de l'effort](https://en.wikipedia.org/wiki/Pareto_principle), ce qui dans de nombreux cas sera suffisant. J'espère que cet article de blog l'a démontré et que vous avez appris une ou deux choses sur Google Apps Script en cours de route.

#### [Voir la démonstration](https://danielireson.github.io/google-sheets-blog-cms)

#### [Voir le projet sur GitHub](https://github.com/danielireson/google-sheets-blog-cms)

![Image](https://cdn-media-1.freecodecamp.org/images/mja7cLraj-m84aPQRLYXru7c3tIBYr38l9XS)