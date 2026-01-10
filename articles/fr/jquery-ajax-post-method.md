---
title: Méthode JQuery Ajax POST
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-10T23:43:00.000Z'
originalURL: https://freecodecamp.org/news/jquery-ajax-post-method
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec8740569d1a4ca3f16.jpg
tags:
- name: Ajax
  slug: ajax
- name: jQuery
  slug: jquery
seo_title: Méthode JQuery Ajax POST
seo_desc: 'Sends an asynchronous http POST request to load data from the server. Its
  general form is:

  jQuery.post( url [, data ] [, success ] [, dataType ] )



  url : is the only mandatory parameter. This string contains the adress to which
  to send the request. ...'
---

Envoie une requête HTTP POST asynchrone pour charger des données depuis le serveur. Sa forme générale est :

```javascript
jQuery.post( url [, data ] [, success ] [, dataType ] )
```

* url : est le seul paramètre obligatoire. Cette chaîne contient l'adresse à laquelle envoyer la requête. Les données retournées seront ignorées si aucun autre paramètre n'est spécifié.
* data : Un objet simple ou une chaîne qui est envoyée au serveur avec la requête.
* success : Une fonction de rappel qui est exécutée si la requête réussit. Elle prend comme argument les données retournées. Elle reçoit également le statut textuel de la réponse.
* dataType : Le type de données attendu du serveur. Par défaut, il s'agit d'une supposition intelligente (xml, json, script, text, html). Si ce paramètre est fourni, alors le rappel de succès doit également être fourni.

#### **Exemples**

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'});
```

Demande `form.php` depuis le serveur, envoie des données supplémentaires et ignore le résultat retourné.

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}, function(response){ 
      alert("succès");
      $("#mypar").html(response.amount);
});
```

Demande `form.php` depuis le serveur, envoie des données supplémentaires et traite la réponse retournée (format json). Cet exemple peut être écrit sous cette forme :

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}).done(function(response){
      alert("succès");
      $("#mypar").html(response.amount);
});
```

L'exemple suivant envoie un formulaire en utilisant Ajax et place les résultats dans une div.

```html
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Démonstration de jQuery.post</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form action="/" id="searchForm">
  <input type="text" name="s" placeholder="Rechercher...">
  <input type="submit" value="Rechercher">
</form>
<!-- le résultat de la recherche sera affiché dans cette div -->
<div id="result"></div>
 
<script>
// Attacher un gestionnaire de soumission au formulaire
$( "#searchForm" ).submit(function( event ) {
 
  // Empêcher la soumission normale du formulaire
  event.preventDefault();
 
  // Obtenir certaines valeurs des éléments de la page :
  var $form = $( this ),
    term = $form.find( "input[name='s']" ).val(),
    url = $form.attr( "action" );
 
  // Envoyer les données en utilisant post
  var posting = $.post( url, { s: term } );
 
  // Placer les résultats dans une div
  posting.done(function( data ) {
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
});
</script>
 
</body>
</html>
```

L'exemple suivant utilise l'API GitHub pour récupérer la liste des dépôts d'un utilisateur en utilisant jQuery.ajax() et place les résultats dans une div.

```html
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Démonstration de jQuery Get</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form id="userForm">
  <input type="text" name="username" placeholder="Entrez le nom d'utilisateur GitHub">
  <input type="submit" value="Rechercher">
</form>
<!-- le résultat de la recherche sera affiché dans cette div -->
<div id="result"></div>
 
<script>
// Attacher un gestionnaire de soumission au formulaire
$( "#userForm" ).submit(function( event ) {
 
  // Empêcher la soumission normale du formulaire
  event.preventDefault();
 
  // Obtenir certaines valeurs des éléments de la page :
  var $form = $( this ),
    username = $form.find( "input[name='username']" ).val(),
    url = "https://api.github.com/users/"+username+"/repos";
 
  // Envoyer les données en utilisant post
  var posting = $.post( url, { s: term } );
 
  // Fonction Ajax pour envoyer une requête GET
  $.ajax({
    type: "GET",
    url: url,
    dataType:"jsonp",
    success: function(response){
        // Si la requête est réussie, alors la réponse représente les données

        $( "#result" ).empty().append( response );
    }
  });
  
});
</script>
 
</body>
</html>
```

### **jQuery.ajax()**

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

`$.ajax()` offre beaucoup plus d'options que l'on peut trouver [ici](http://api.jquery.com/jquery.ajax/)

#### **Plus d'informations :**

Pour plus d'informations, veuillez consulter le [site officiel](https://api.jquery.com/jquery.post/)