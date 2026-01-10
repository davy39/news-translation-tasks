---
title: Cibler le clic du bouton "Effacer" (X) sur un champ de saisie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/targeting-click-of-clear-button-x-on-input-field
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a98740569d1a4ca2689.jpg
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: toothbrush
  slug: toothbrush
seo_title: Cibler le clic du bouton "Effacer" (X) sur un champ de saisie
seo_desc: 'jQuery makes it easy to get your project up and running. Though it''s fallen
  out of favor in recent years, it''s still worth learning the basics, especially
  if you want quick access to its powerful methods.

  But while jQuery is a powerful library, it ca...'
---

jQuery facilite le démarrage de votre projet. Bien qu'il soit moins populaire ces dernières années, il vaut toujours la peine d'apprendre les bases, surtout si vous voulez un accès rapide à ses méthodes puissantes.

Mais bien que jQuery soit une bibliothèque puissante, elle ne peut pas tout faire. C'est là qu'une bonne compréhension de vanilla JavaScript s'avère utile.

Disons que vous avez un projet [Wikipedia Viewer](https://www.freecodecamp.org/learn/coding-interview-prep/take-home-projects/build-a-wikipedia-viewer) comme ceci :

```html
<div class="search">
  <p id="text">Rechercher sur Wikipedia</p>
  <input id="searchbox" type="search"></input>
  <button id="searchbutton">Rechercher</button>
  <a href="https://en.wikipedia.org/wiki/Special:Random" target="_blank"><button id="searchbutton">Article Aléatoire</button></a>
  <div class="resultingarticles"></div>
</div>
```

```js
$("#searchbox").keyup(function(event) {
  if(event.keyCode === 13) {
    $("#searchbutton").click();
  };
});

$("#searchbutton").click(function() {
  
  var searchInput = document.getElementById("searchbox").value;
  searchInput = searchInput.toLowerCase();
  
  if(searchInput !== "") {
  
    var myRequest = new XMLHttpRequest();
    myRequest.open('GET','https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch='+ searchInput + '&utf8=&format=json&origin=*');
  
      myRequest.onload = function() {
      var searchResults = JSON.parse(myRequest.responseText);
      
      $(".resultingarticles").empty();  
        
      for(i=0; i<10; i++) {
        var articleTitle = searchResults.query.search[i].title;
        var articleSnippet = searchResults.query.search[i].snippet;
        var articleId = searchResults.query.search[i].pageid;
        var articleLink = "https://en.wikipedia.org/?curid=" + articleId;
        $(".resultingarticles").append("<a href='" + articleLink + "' target='_blank'>" + "<div class='article'>" + "<p>"+articleTitle+"</p>" + "<p>" + articleSnippet + "</p>" + "</div>" + "</a>");
      };
        
      };
    
    myRequest.send();
    
  };
});
```

Tout fonctionne comme prévu – vous pouvez entrer du texte dans la barre de recherche, appuyer sur Entrée ou le bouton "Rechercher", et voir une liste d'articles Wikipedia.

Comme vous utilisez `type="search"` sur votre élément `input`, le navigateur Chrome ajoutera automatiquement un "X" à la fin de la saisie s'il y a du texte et que vous survolez la saisie. Notez que d'autres navigateurs peuvent gérer `type="search"` différemment.

Lorsque vous cliquez sur le "X", le texte disparaît.

Mais disons que vous avez déjà une liste d'articles, et que lorsque vous effacez le texte, vous voulez aussi effacer les articles affichés :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-13-19-24.gif)

Il s'avère que cliquer sur le "X" dans la barre de recherche déclenche un événement "search". jQuery ne supporte pas l'événement "search", vous devrez donc écrire un écouteur d'événement en vanilla JavaScript :

```js
document.getElementById("searchbox").addEventListener("search", function(event) {
  $(".resultingarticles").empty();  
});
```

Maintenant, lorsqu'un événement de recherche est déclenché, vous pouvez utiliser jQuery pour vider l'élément `div` contenant les articles :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-13-19-29.gif)