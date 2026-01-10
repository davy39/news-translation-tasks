---
title: Les meilleurs exemples de jQuery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T00:23:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-jquery-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1b740569d1a4ca40dc.jpg
tags:
- name: jQuery
  slug: jquery
seo_title: Les meilleurs exemples de jQuery
seo_desc: 'jQuery is the most widely-used JavaScript library, and is used in more
  than half of all major websites. It''s motto is "write less, do more...!"

  jQuery makes web development easier to use by providing a number of ''helper'' functions.
  These help develop...'
---

jQuery est la bibliothèque JavaScript la plus largement utilisée, et est utilisée dans plus de la moitié de tous les principaux sites web. Sa devise est "écrivez moins, faites plus...!"

jQuery facilite le développement web en fournissant un certain nombre de fonctions 'd'aide'. Ces fonctions aident les développeurs à écrire rapidement des interactions DOM (Document Object Model) sans avoir besoin d'écrire manuellement autant de JavaScript eux-mêmes.

jQuery ajoute une variable globale avec toutes les méthodes de la bibliothèque attachées. La convention de nommage est d'avoir cette variable globale comme `$`. En tapant `$.` vous avez toutes les méthodes jQuery à votre disposition.

## Installation

Il existe deux principales façons de commencer à utiliser jQuery :

* **Inclure jQuery localement** : Téléchargez la bibliothèque jQuery depuis [jquery.com](https://jquery.com/) et incluez-la dans votre code HTML.
* **Utiliser un CDN** : Lien vers la bibliothèque jQuery en utilisant un CDN (Content Delivery Network).

```html
<head>
  <script src="/jquery/jquery-3.4.1.min.js"></script>
  <script src="js/scripts.js"></script>
</head>
```

```html
<head>
  <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="js/scripts.js"></script>
</head>
```

## Sélecteurs

jQuery utilise des sélecteurs de style CSS pour sélectionner des parties, ou des éléments, d'une page HTML. Il permet ensuite de faire quelque chose avec les éléments en utilisant des méthodes, ou des fonctions, jQuery.

Pour utiliser l'un de ces sélecteurs, tapez un signe dollar et des parenthèses après celui-ci : `$()`. C'est une abréviation pour la fonction `jQuery()`. À l'intérieur des parenthèses, ajoutez l'élément que vous souhaitez sélectionner. Vous pouvez utiliser des guillemets simples ou doubles. Après cela, ajoutez un point après les parenthèses et la méthode que vous souhaitez utiliser.

Dans jQuery, les sélecteurs de classe et d'ID sont similaires à ceux de CSS.

Voici un exemple de méthode jQuery qui sélectionne tous les éléments de paragraphe et ajoute une classe "selected" à ceux-ci :

```javascript
<p>Ceci est un paragraphe sélectionné par une méthode jQuery.</p>
<p>Ceci est également un paragraphe sélectionné par une méthode jQuery.</p>

$("p").addClass("selected");
```

Dans jQuery, les sélecteurs de classe et d'ID sont les mêmes que dans CSS. Si vous souhaitez sélectionner des éléments avec une certaine classe, utilisez un point (`.`) et le nom de la classe. Si vous souhaitez sélectionner des éléments avec un certain ID, utilisez le symbole dièse (`#`) et le nom de l'ID. Notez que HTML n'est pas sensible à la casse, il est donc préférable de garder le balisage HTML et les sélecteurs CSS en minuscules.

### Sélection par classe

Si vous souhaitez sélectionner des éléments avec une certaine classe, utilisez un point (.) et le nom de la classe.

```html
<p class="pWithClass">Paragraphe avec une classe.</p>
```

```javascript
$(".pWithClass").css("color", "blue"); // colorie le texte en bleu
```

Vous pouvez également utiliser le sélecteur de classe en combinaison avec un nom de balise pour être plus spécifique.

```html
<ul class="wishList">Ma liste de souhaits</ul>`<br>
```

```javascript
$("ul.wishList").append("<li>Nouveau mixeur</li>");
```

### Sélection par ID

Si vous souhaitez sélectionner des éléments avec une certaine valeur d'ID, utilisez le symbole dièse (#) et le nom de l'ID.

```html
<li id="liWithID">Élément de liste avec un ID.</li>
```

```javascript
$("#liWithID").replaceWith("<p>Chaussettes</p>");
```

Comme avec le sélecteur de classe, cela peut également être utilisé en combinaison avec un nom de balise.

```html
<h1 id="headline">Titre de l'actualité</h1>
```

```javascript
$("h1#headline").css("font-size", "2em");
```

### Sélection par valeur d'attribut

Si vous souhaitez sélectionner des éléments avec un certain attribut, utilisez `([attributeName="value"])`.

```html
<input name="myInput" />
```

```javascript
$("[name='myInput']").value("Test"); // définit la valeur de l'entrée sur "Test"
```

Vous pouvez également utiliser le sélecteur d'attribut en combinaison avec un nom de balise pour être plus spécifique.

```html
<input name="myElement" />`<br>
<button name="myElement">Bouton</button>
```

```javascript
$("input[name='myElement']").remove(); // supprime le champ d'entrée et non le bouton
```

### Sélecteurs qui agissent comme des filtres

Il existe également des sélecteurs qui agissent comme des filtres - ils commencent généralement par des deux-points. Par exemple, le sélecteur `:first` sélectionne l'élément qui est le premier enfant de son parent. Voici un exemple de liste non ordonnée avec quelques éléments de liste. Le sélecteur jQuery sous la liste sélectionne le premier élément `<li>` de la liste--l'élément de liste "One"--et utilise ensuite la méthode `.css` pour rendre le texte vert.

```html
   <ul>
      <li>Un</li>
      <li>Deux</li>
      <li>Trois</li>
   </ul>
```

```javascript
$("li:first").css("color", "green");
```

### Sélecteur d'attribut

Il existe des sélecteurs qui retournent des éléments qui correspondent à certaines combinaisons d'attributs comme _Attribute contains_, _Attribute ends with_, _Attribute starts with_, etc. Voici un exemple de liste non ordonnée avec quelques éléments de liste. Le sélecteur jQuery sous la liste sélectionne l'élément `<li>` de la liste--l'élément de liste "Un" car il a un attribut `data*` avec la valeur `"India"`--et utilise ensuite la méthode `.css` pour rendre le texte vert.

```html
   <ul>
      <li data-country="India">Mumbai</li>
      <li data-country="China">Beijing</li>
      <li data-country="United States">New York</li>
   </ul>
```

```javascript
$("li[data-country='India']").css("color", "green");
```

Un autre sélecteur de filtrage, `:contains(text)`, sélectionne les éléments qui contiennent un certain texte. Placez le texte que vous souhaitez correspondre entre les parenthèses. Voici un exemple avec deux paragraphes. Le sélecteur jQuery prend le mot "Moto" et change sa couleur en jaune.

```html
    <p>Bonjour</p>
    <p>Monde</p>
```

```javascript
$("p:contains('Monde')").css("color", "yellow");
```

De même, le sélecteur `:last` sélectionne l'élément qui est le dernier enfant de son parent. Le sélecteur jQuery ci-dessous sélectionne le dernier élément `<li>` de la liste--l'élément de liste "Trois"--et utilise ensuite la méthode `.css` pour rendre le texte jaune.

`$("li:last").css("color", "yellow");`

**Note :** Dans le sélecteur jQuery, `World` est entre guillemets simples car il est déjà à l'intérieur d'une paire de guillemets doubles. Utilisez toujours des guillemets simples à l'intérieur de guillemets doubles pour éviter de terminer accidentellement une chaîne.

### Sélecteurs multiples

Dans jQuery, vous pouvez utiliser plusieurs sélecteurs pour appliquer les mêmes changements à plus d'un élément, en utilisant une seule ligne de code. Vous faites cela en séparant les différents identifiants par une virgule. Par exemple, si vous souhaitez définir la couleur de fond de trois éléments avec les identifiants cat, dog et rat respectivement en rouge, faites simplement :

```text
$("#cat,#dog,#rat").css("background-color","red");
```

## Méthode HTML

La méthode `.html()` de jQuery obtient le contenu d'un élément HTML ou définit le contenu d'un élément HTML.

### Obtenir

Pour retourner le contenu d'un élément HTML, utilisez cette syntaxe :

```javascript
$('selector').html();
```

Par exemple :

```javascript
$('#example').html();
```

### Définir

Pour définir le contenu d'un élément HTML, utilisez cette syntaxe :

```javascript
$('selector').html(content);
```

Par exemple :

```javascript
$('p').html('Bonjour le monde !');
```

Cela définira le contenu de tous les éléments `<p>` à Bonjour le monde !

### Avertissement

La méthode `.html()` est utilisée pour définir le contenu de l'élément au format **HTML**. Cela peut être dangereux si le contenu est fourni par l'utilisateur. Envisagez d'utiliser la méthode `.text()` à la place si vous devez définir des chaînes non-HTML comme contenu.

## Méthode CSS

La méthode `.css()` de jQuery obtient la valeur d'une propriété de style calculée pour le premier élément dans l'ensemble des éléments correspondants ou définit une ou plusieurs propriétés CSS pour chaque élément correspondant.

### Obtenir

Pour retourner la valeur d'une propriété CSS spécifiée, utilisez la syntaxe suivante :

```js
    $(selector).css(propertyName);
```

Exemple :

```js
    $('#element').css('background');
```

Note : Ici, nous pouvons utiliser n'importe quel sélecteur CSS, par exemple : element(sélecteur de balise HTML), .element(sélecteur de classe), #element(sélecteur d'ID).

### Définir

Pour définir une propriété CSS spécifiée, utilisez la syntaxe suivante :

```js
    $(selector).css(propertyName,value);
```

Exemple :

```js
    $('#element').css('background','red');
```

Pour définir plusieurs propriétés CSS, vous devrez utiliser la syntaxe littérale d'objet comme ceci :

```js
    $('#element').css({
        'background': 'gray',
        'color': 'white'
    });
```

Si vous souhaitez changer une propriété étiquetée avec plus d'un mot, référez-vous à cet exemple :

Pour changer `background-color` d'un élément

```js
    $('#element').css('background-color', 'gray');
```

## Méthode Click

La méthode Click de jQuery déclenche une fonction lorsqu'un élément est cliqué. La fonction est connue sous le nom de "handler" car elle gère l'événement de clic. Les fonctions peuvent affecter l'élément HTML qui est lié au clic en utilisant la méthode Click de jQuery, ou elles peuvent changer autre chose entièrement. La forme la plus utilisée est :

```javascript
$("#clickMe").click(handler)
```

La méthode click prend la fonction handler comme argument et l'exécute chaque fois que l'élément `#clickMe` est cliqué. La fonction handler reçoit un paramètre connu sous le nom d'[eventObject](http://api.jquery.com/Types/#Event) qui peut être utile pour contrôler l'action.

### Exemples

Ce code montre une alerte lorsque l'utilisateur clique sur un bouton :

```html
<button id="alert">Cliquez ici</button>
```

```javascript
$("#alert").click(function () {
  alert("Salut ! Je suis une alerte");
});
```

L'[eventObject](http://api.jquery.com/Types/#Event) a quelques méthodes intégrées, y compris `preventDefault()`, qui fait exactement ce qu'elle dit - arrête l'événement par défaut d'un élément. Ici, nous empêchons la balise d'ancrage d'agir comme un lien :

```html
<a id="myLink" href="www.google.com">Lien vers Google</a>
```

```javascript
$("#myLink").click(function (event) {
  event.preventDefault();
});
```

### Plus de façons de jouer avec la méthode click

La fonction handler peut également accepter des données supplémentaires sous la forme d'un objet :

```javascript
jqueryElement.click(usefulInfo, handler)
```

Les données peuvent être de n'importe quel type.

```javascript
$("element").click({firstWord: "Hello", secondWord: "World"}, function(event){
    alert(event.data.firstWord);
    alert(event.data.secondWord);
});
```

Invoquer la méthode click sans fonction handler déclenche un événement de clic :

```javascript
$("#alert").click(function () {
  alert("Salut ! Je suis une alerte");
});

$("#alert").click();
```

Maintenant, chaque fois que la page se charge, l'événement de clic sera déclenché lorsque nous entrerons ou rechargerons la page, et affichera l'alerte assignée.

De plus, vous devriez préférer utiliser `.on("click",...)` plutôt que `.click(...)` car le premier peut utiliser moins de mémoire et fonctionner pour les éléments ajoutés dynamiquement.

### Erreurs courantes

L'événement de clic n'est lié qu'aux éléments actuellement dans le DOM au moment de la liaison, donc tout élément ajouté par la suite ne sera pas lié. Pour lier tous les éléments dans le DOM, même s'ils seront créés plus tard, utilisez la méthode `.on()`.

Par exemple, cet exemple de méthode click :

```javascript
$("element").click(function() {
  alert("J'ai été cliqué !");
});
```

Peut être changé en cet exemple de méthode on :

```javascript
$(document).on("click", "element", function() {
  alert("J'ai été cliqué !");
});
```

### Obtenir l'élément à partir d'un événement de clic

Cela s'applique à la fois à jQuery et à JavaScript, mais si vous configurez votre déclencheur d'événement pour cibler une classe, vous pouvez récupérer l'élément spécifique qui a déclenché l'événement en utilisant le mot-clé `this`.

jQuery facilite grandement (et est compatible avec plusieurs navigateurs) la traversée du DOM pour trouver les parents, les frères et sœurs et les enfants de cet élément.

Supposons que j'ai une table pleine de boutons et que je veux cibler la ligne dans laquelle se trouve ce bouton, je peux simplement envelopper `this` dans un sélecteur jQuery et obtenir ensuite son `parent` et le parent de son parent comme ceci :

```javascript
$( document ).on("click", ".myCustomBtnClassInATable", function () {
    var myTableCell = $(this).parent();
    var myTableRow = myTableCell.parent();
    var myTableBody = myTableRow.parent();
    var myTable = myTableBody.parent();
    
    // vous pouvez également enchaîner tout cela pour obtenir ce que vous voulez en une seule ligne
    var myTableBody = $(this).parent().parent().parent();
});
```

Il est également intéressant de vérifier les données de l'événement pour l'événement de clic, que vous pouvez obtenir en passant n'importe quel nom de variable à la fonction dans l'événement de clic. Vous verrez probablement un `e` ou `event` dans la plupart des cas :

```javascript
$( document ).on("click", ".myCustomBtnClassInATable", function (e) { 
    // obtenir plus d'informations sur la variable d'événement dans la console
    console.log(e);
});
```

## Méthode Mousedown

L'événement mousedown se produit lorsque le bouton gauche de la souris est enfoncé. Pour déclencher l'événement mousedown pour l'élément sélectionné, utilisez cette syntaxe : `$(selector).mousedown();`

La plupart du temps, cependant, la méthode mousedown est utilisée avec une fonction attachée à l'événement mousedown. Voici la syntaxe : `$(selector).mousedown(function);` Par exemple :

```text
$(#example).mousedown(function(){
   alert("Example was clicked");
});
```

Ce code fera en sorte que la page alerte "Example was clicked" lorsque #example est cliqué.

## Méthode Hover

La méthode hover de jquery est une combinaison des événements `mouseenter` et `mouseleave`. La syntaxe est la suivante :

```text
$(selector).hover(inFunction, outFunction);
```

La première fonction, inFunction, s'exécutera lorsque l'événement `mouseenter` se produira. La deuxième fonction est facultative, mais s'exécutera lorsque l'événement `mouseleave` se produira. Si une seule fonction est spécifiée, l'autre fonction s'exécutera pour les événements `mouseenter` et `mouseleave`. Voici un exemple plus spécifique.

```text
$("p").hover(function(){
    $(this).css("background-color", "yellow");
}, function(){
    $(this).css("background-color", "pink");
});
```

Ainsi, le survol du paragraphe changera sa couleur de fond en jaune et l'inverse la ramènera à rose.

## Méthode Animate

La méthode animate de jQuery facilite la création d'animations simples en utilisant seulement quelques lignes de code. La structure de base est la suivante :

```javascript
$(".selector").animate(properties, duration, callbackFunction());
```

Pour l'argument `properties`, vous devez passer un objet javascript avec les propriétés CSS que vous souhaitez animer comme clés et les valeurs que vous souhaitez animer comme valeurs. Pour la `duration`, vous devez entrer la quantité de temps en millisecondes que l'animation doit prendre. La `callbackFunction()` est exécutée une fois que l'animation est terminée.

### Exemple

Un exemple simple ressemblerait à ceci :

```javascript
$(".awesome-animation").animate({
	opacity: 1,
	bottom: += 15
}, 1000, function() {
	$(".different-element").hide();
});
```

## Méthode Hide

Dans sa forme la plus simple, **.hide()** masque l'élément correspondant immédiatement, sans animation. Par exemple :

```javascript
$(".myclass").hide()
```

masquera tous les éléments dont la classe est _myclass_. N'importe quel sélecteur jQuery peut être utilisé.

### .hide() comme méthode d'animation

Grâce à ses options, **.hide()** peut animer la largeur, la hauteur et l'opacité des éléments correspondants simultanément.

* La durée peut être fournie en millisecondes, ou en utilisant les littéraux slow (600 ms) et fast(200ms). par exemple :
* Une fonction peut être spécifiée pour être appelée une fois l'animation terminée, une fois par élément correspondant. Ce rappel est principalement utile pour enchaîner différentes animations. Par exemple

```javascript
$("#myobject").hide(800)
```

```javascript
$("p").hide( "slow", function() {
  $(".titles").hide("fast");
  alert("No more text!");
});
```

## Méthode Show

Dans sa forme la plus simple, **.show()** affiche l'élément correspondant immédiatement, sans animation. Par exemple :

```javascript
$(".myclass").show();
```

affichera tous les éléments dont la classe est _myclass_. N'importe quel sélecteur jQuery peut être utilisé.

Cependant, cette méthode ne remplace pas `!important` dans le style CSS, comme `display: none !important`.

### .show() comme méthode d'animation

Grâce à ses options, **.show()** peut animer la largeur, la hauteur et l'opacité des éléments correspondants simultanément.

* La durée peut être fournie en millisecondes, ou en utilisant les littéraux slow (600 ms) et fast(200ms). par exemple :
* Une fonction peut être spécifiée pour être appelée une fois l'animation terminée, une fois par élément correspondant. par exemple

```javascript
$("#myobject").show("slow");
```

```javascript
$("#title").show( "slow", function() {
  $("p").show("fast");
});
```

## Méthode Toggle de jQuery

Pour afficher/masquer des éléments, vous pouvez utiliser la méthode `toggle()`. Si l'élément est masqué, `toggle()` l'affichera et vice versa. Utilisation :

```javascript
$(".myclass").toggle()
```

## Méthode Slide Down

Cette méthode anime la hauteur des éléments correspondants. Cela fait glisser les parties inférieures de la page vers le bas, faisant place aux éléments révélés. Utilisation :

```javascript
$(".myclass").slideDown(); // développera l'élément avec l'identifiant myclass pendant 400 ms.
$(".myclass").slideDown(1000); // développera l'élément avec l'identifiant myclass pendant 1000 ms.
$(".myclass").slideDown("slow"); // développera l'élément avec l'identifiant myclass pendant 600 ms.
$(".myclass").slideDown("fast"); // développera l'élément avec l'identifiant myclass pendant 200 ms.
```

## Méthode Load

La méthode load() charge des données depuis un serveur et place les données retournées dans l'élément sélectionné.

**Note :** Il existe également une méthode d'événement jQuery appelée load. Celle qui est appelée dépend des paramètres.

### Exemple

```javascript
$("button").click(function(){
    $("#div1").load("demo_test.txt");
});
```

## Chaînage

Le chaînage jQuery permet d'exécuter plusieurs méthodes sur la même sélection jQuery, le tout sur une seule ligne.

Le chaînage nous permet de transformer des instructions multi-lignes :

```javascript
$('#someElement').removeClass('classA');
$('#someElement').addClass('classB');
```

En une seule instruction :

```javascript
$('#someElement').removeClass('classA').addClass('classB');
```

## Méthode Ajax Get

Envoie une requête HTTP GET asynchrone pour charger des données depuis le serveur. Sa forme générale est :

```javascript
jQuery.get( url [, data ] [, success ] [, dataType ] )
```

* `url` : Le seul paramètre obligatoire. Cette chaîne contient l'adresse à laquelle envoyer la requête. Les données retournées seront ignorées si aucun autre paramètre n'est spécifié.
* `data` : Un objet simple ou une chaîne envoyée au serveur avec la requête.
* `success` : Une fonction de rappel exécutée si la requête réussit. Elle prend comme argument les données retournées. Elle reçoit également le statut texte de la réponse.
* `dataType` : Le type de données attendu du serveur. Par défaut, il s'agit de Intelligent Guess (xml, json, script, text, html). Si ce paramètre est fourni, le rappel de succès doit également être fourni.

### Exemples

Demander `resource.json` depuis le serveur, envoyer des données supplémentaires et ignorer le résultat retourné :

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'});
```

Demander `resource.json` depuis le serveur, envoyer des données supplémentaires et gérer la réponse retournée (format json) :

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'}, function(response) {
     alert("success");
     $("#mypar").html(response.amount);
});
```

Cependant, `$.get` ne fournit aucun moyen de gérer les erreurs.

L'exemple ci-dessus (avec gestion des erreurs) peut également être écrit comme :

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'})
     .done(function(response) {
           alert("success");
           $("#mypar").html(response.amount);
     })
     .fail(function(error) {
           alert("error");
           $("#mypar").html(error.statusText);
     });
```

### Équivalent Ajax GET

`$.get( url [, data ] [, success ] [, dataType ] )` est une fonction Ajax abrégée, équivalente à :

```javascript
$.ajax({
     url: url,
     data: data,
     success: success,
     dataType: dataType
});
```

## Méthode Ajax Post

Envoie une requête HTTP POST asynchrone pour charger des données depuis le serveur. Sa forme générale est :

```javascript
jQuery.post( url [, data ] [, success ] [, dataType ] )
```

* url : Il s'agit du seul paramètre obligatoire. Cette chaîne contient l'adresse à laquelle envoyer la requête. Les données retournées seront ignorées si aucun autre paramètre n'est spécifié.
* data : Un objet simple ou une chaîne qui est envoyée au serveur avec la requête.
* success : Une fonction de rappel qui est exécutée si la requête réussit. Elle prend comme argument les données retournées. Elle reçoit également le statut texte de la réponse.
* dataType : Le type de données attendu du serveur. Par défaut, il s'agit de Intelligent Guess (xml, json, script, text, html). Si ce paramètre est fourni, alors le rappel de succès doit également être fourni.

#### Exemples

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'});
```

demande `form.php` depuis le serveur, envoie des données supplémentaires et ignore le résultat retourné

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}, function(response){ 
      alert("success");
      $("#mypar").html(response.amount);
});
```

demande `form.php` depuis le serveur, envoie des données supplémentaires et gère la réponse retournée (format json). Cet exemple peut être écrit dans ce format :

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}).done(function(response){
      alert("success");
      $("#mypar").html(response.amount);
});
```

L'exemple suivant envoie un formulaire en utilisant Ajax et place les résultats dans une div

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery.post demo</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form action="/" id="searchForm">
  <input type="text" name="s" placeholder="Search...">
  <input type="submit" value="Search">
</form>
<!-- the result of the search will be rendered inside this div -->
<div id="result"></div>
 
<script>
// Attach a submit handler to the form
$( "#searchForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    term = $form.find( "input[name='s']" ).val(),
    url = $form.attr( "action" );
 
  // Send the data using post
  var posting = $.post( url, { s: term } );
 
  // Put the results in a div
  posting.done(function( data ) {
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
});
</script>
 
</body>
</html>
```

L'exemple suivant utilise l'API github pour récupérer la liste des dépôts d'un utilisateur en utilisant jQuery.ajax() et place les résultats dans une div

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery Get demo</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form id="userForm">
  <input type="text" name="username" placeholder="Enter gitHub User name">
  <input type="submit" value="Search">
</form>
<!-- the result of the search will be rendered inside this div -->
<div id="result"></div>
 
<script>
// Attach a submit handler to the form
$( "#userForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    username = $form.find( "input[name='username']" ).val(),
    url = "https://api.github.com/users/"+username+"/repos";
 
  // Send the data using post
  var posting = $.post( url, { s: term } );
 
  //Ajax Function to send a get request
  $.ajax({
    type: "GET",
    url: url,
    dataType:"jsonp",
    success: function(response){
        //if request if made successfully then the response represent the data

        $( "#result" ).empty().append( response );
    }
  });
  
});
</script>
 
</body>
</html>
```

### Équivalent Ajax POST

`$.post( url [, data ] [, success ] [, dataType ] )` est une fonction Ajax abrégée, équivalente à :

```javascript
$.ajax({
  type: "POST",
  url: url,
  data: data,
  success: success,
  dataType: dataType
});
```