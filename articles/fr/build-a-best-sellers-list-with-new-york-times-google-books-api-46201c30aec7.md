---
title: Créer une liste des meilleurs ventes avec l'API du New York Times et de Google
  Books
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T03:13:27.000Z'
originalURL: https://freecodecamp.org/news/build-a-best-sellers-list-with-new-york-times-google-books-api-46201c30aec7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bVvh3q1aNXWnfkjXNp_vwQ.png
tags:
- name: Digital Humanities
  slug: digital-humanities
- name: api
  slug: api
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
seo_title: Créer une liste des meilleurs ventes avec l'API du New York Times et de
  Google Books
seo_desc: 'By Andrew Bales

  A single API may not always have all of the data you need. In this article, we’ll
  walk through the steps to combine two APIs by using unique identifiers from the
  New York Times API to grab book covers from the Google Books API.

  You ca...'
---

Par Andrew Bales

Une seule API ne contient pas toujours toutes les données dont vous avez besoin. Dans cet article, nous allons passer en revue les étapes pour combiner deux API en utilisant des identifiants uniques de l'API du New York Times pour récupérer les couvertures de livres depuis l'API Google Books.

Vous pouvez trouver le projet complet sur [GitHub](https://github.com/agbales/best-sellers) et voir une démonstration sur [CodePen](https://codepen.io/agbales/full/LNWPYW/).

Voici les étapes que nous allons couvrir :

1. Récupérer les données des meilleurs ventes de livres depuis l'API du New York Times.
2. Ajouter les listings au DOM.
3. Interroger l'API Google Books avec les numéros ISBN pour ajouter des images de couverture aux listings.

À la fin du tutoriel, vous aurez une liste des meilleurs ventes ! Voici un aperçu :

![Image](https://cdn-media-1.freecodecamp.org/images/ckGF3oZ3cWjkItnuviz8K66gLSGPI3Va9xil)

### Attendez, mais pourquoi ?

J'ai commencé à travailler sur ce projet il y a un peu plus d'un an. J'apprenais à propos des API et je demandais des clés pour pratiquer l'accès et l'affichage de données.

En explorant l'API du _New York Times_, j'ai découvert qu'il était possible d'obtenir une liste des meilleurs ventes de livres. Pour chaque livre de la liste, l'API fournit un classement actuel et le nombre de semaines sur la liste. Elle offre également des informations comme un synopsis et un lien Amazon.

J'ai pu remplir les informations textuelles, mais la liste manquait de la composante visuelle naturelle des couvertures de livres. À l'époque, je ne voyais pas de voie claire à suivre, alors j'ai mis le projet de côté.

**C'est un cas où avoir accès à une API est utile, mais incomplet.**

Cette semaine, je suis revenu avec l'objectif d'ajouter des couvertures de livres. J'ai découvert que l'API Google Books retourne des miniatures pour les livres lorsqu'on fournit un ISBN, un numéro d'identification unique. Par chance, l'API du New York Times fournit cet ISBN.

Nous sommes en affaires !

### Mise en route

Tout d'abord, nous voulons générer une liste des meilleurs ventes de livres de fiction avec quelques informations sur chacun. Il serait bien d'afficher des informations sur la durée pendant laquelle le livre est resté sur la liste. Nous devons également voir la couverture et fournir un lien pour que les utilisateurs puissent en savoir plus sur le livre ou acheter une copie.

L'API du New York Times fournit toutes ces informations, à l'exception de la couverture du livre. Obtenez une clé API gratuite du [NYT](https://developer.nytimes.com) pour commencer.

Nous utiliserons l'[API Fetch](https://developers.google.com/web/updates/2015/03/introduction-to-fetch) pour obtenir les données des meilleurs ventes pour les œuvres de fiction en couverture rigide :

```
fetch('https://api.nytimes.com/svc/books/v3/lists.json?list-name=hardcover-fiction&api-key=' + apiKey, {    method: 'get',  })  .then(response => { return response.json(); })  .then(json => { console.log(json); });
```

Si vous inspectez le navigateur, vous verrez un objet JSON enregistré dans la console. Si vous n'avez jamais utilisé d'API auparavant, il sera utile de passer un moment à examiner cet objet. Creuser dans les données pour accéder exactement à ce que vous cherchez peut prendre un certain temps pour s'y habituer.

La réponse retourne 15 objets dans « results ». Chaque résultat est un livre. Pour plus de clarté, cet exemple utilise `.forEach()` pour creuser dans la réponse de l'API `nytimesBestSellers` en boucle sur chaque livre.

```
nytimesBestSellers.results.forEach(function(book) {  var isbn = book.isbns[1].isbn10;  var bookInfo = book.book_details[0];  var lastWeekRank = book.rank_last_week || 'n/a';  var weeksOnList = book.weeks_on_list || 'Nouveau cette semaine';
```

```
  // ...
```

```
});
```

Alors que nous parcourons chaque livre individuel, les variables sont définies sur les données de leur listing spécifique, que nous utiliserons lors de la création de l'entrée.

Dans la liste de code ci-dessus,

* le numéro ISBN est situé dans le tableau `isbns` du livre
* nous sélectionnons la version à 10 chiffres du numéro ISBN à `book_details[0]`
* le classement de la semaine dernière est à `rank_last_week` et par défaut à 'n/a'
* le nombre de semaines pendant lesquelles il a été sur la liste des meilleurs ventes, est à `weeks_on_list` et par défaut à « Nouveau cette semaine » pour les livres qui apparaissent sur la liste pour la première fois

Ensuite, nous pouvons créer un objet HTML à ajouter à la liste `best-seller-titles`. Assurez-vous que votre projet inclut [jQuery](https://jquery.com/). Sur CodePen, vous pouvez aller dans les paramètres et l'ajouter dans le panneau JavaScript.

```
var listing =   '<div id="' + book.rank + '" class="entry">' +     '<p>' +       '<img src="" class="book-cover" id="cover-' + book.rank + '">' +     '</p>' +     '<h2><a href="' + book.amazon_product_url + '" target="_blank">' + bookInfo.title + '</a></h2>' +    '<h4>Par ' + bookInfo.author + '</h4>' +    '<h4 class="publisher">' + bookInfo.publisher + '</h4>' +    '<p>' + bookInfo.description + '</p>' +     '<div class="stats">' +      '<hr>' +       '<p>Semaine dernière : ' + lastWeekRank + '</p>' +       '<p>Semaines sur la liste : ' + weeksOnList + '</p>' +    '</div>' +  '</div>';
```

```
$('#best-seller-titles').append(listing);
```

Remarquez que l'image est laissée vide. Sur [CodePen](https://codepen.io/agbales/pen/LNWPYW), j'ai ajouté une image de remplacement pour remplir les réponses non définies de Google.

Enfin, nous pouvons mettre à jour le numéro de classement du livre et transmettre le classement et le numéro ISBN à `updateCover()`.

```
$('#' + book.rank).attr('nyt-rank', book.rank);
```

```
updateCover(book.rank, isbn);
```

Nous pouvons maintenant écrire `updateCover()`, qui gérera la récupération de la miniature depuis l'API Google Books.

### API Google Books

Nous avons rassemblé les parties textuelles du listing, mais pour ajouter une couverture de livre, l'une des méthodes les plus simples que j'ai trouvées était d'utiliser l'API Google Books. Assurez-vous d'obtenir une clé API depuis [Google Books API](https://developers.google.com/books/).

En utilisant le numéro ISBN à 10 chiffres, nous pouvons obtenir une image de couverture de livre en miniature en utilisant à nouveau `fetch()`. Comme avant, nous devons creuser dans l'objet pour trouver le seul lien référençant l'image miniature que nous cherchons :

```
function updateCover(id, isbn) {  fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn + "&key=" + apiKey, {    method: 'get'  })  .then(response => { return response.json(); })  .then(data => {    var img = data.items[0].volumeInfo.imageLinks.thumbnail;    img = img.replace(/^http:\/\//i, 'https://');    $('#cover-' + id).attr('src', img);  })    .catch(error=> {       console.log(error);  });}
```

Une fois l'image sécurisée, `replace()` échange les liens HTTP contre des versions sécurisées HTTPS. Nous mettons ensuite à jour la couverture du livre en sélectionnant l'ID de couverture approprié et en mettant à jour sa source d'image.

### Style

J'ai ajouté des styles supplémentaires avec SASS. Si vous êtes plus à l'aise avec CSS ou SCSS, utilisez le bouton déroulant dans cette fenêtre pour compiler le code.

Le dernier morceau de JavaScript que vous verrez contrôle la mise à l'échelle du logo. Ce code est déclenché lorsque la fenêtre défile. Lorsque la fenêtre défile vers le bas, le logo se condense d'une hauteur de 80px à 35px.

```
$(window).scroll(function (event) {  var scroll = $(window).scrollTop();  if (scroll > 50) {    $('#masthead').css({'height':'50', 'padding' : '8'});    $('#nyt-logo').css({'height':'35'});  } else {    $('#masthead').css({'height':'100', 'padding':'10'});    $('#nyt-logo').css({'height':'80'});  }});
```

### Réflexions finales

C'était excitant de revenir à un projet et de construire sur ses fonctionnalités. Bien que j'aurais peut-être abordé ce problème différemment si j'avais commencé à partir de zéro, cet exemple montre une façon de prendre un appel API typique et d'ajouter à ce travail.

En fait, l'une des raisons pour lesquelles je voulais particulièrement partager ce projet était de me souvenir à quel point cela pouvait être frustrant pour moi lorsque j'ai commencé à travailler avec les API. Je me sentais submergé par la documentation, sans être sûr des fonctionnalités ou de la syntaxe qui me mèneraient dans la bonne direction. Je souhaitais souvent un exemple clair ou une marche à suivre pour quelque chose un peu au-delà du Hello World.

Les API fournissent chacune un service spécifique, et parfois il est nécessaire de les combiner. Ce n'est qu'une façon de rassembler plusieurs services, mais j'espère que cela sera une source d'inspiration pour ceux qui explorent des moyens de combiner des API pour créer un contenu plus riche.