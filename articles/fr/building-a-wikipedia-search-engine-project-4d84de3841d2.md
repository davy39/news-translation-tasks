---
title: Création d'une application de recherche Wikipedia
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-12T15:43:31.000Z'
originalURL: https://freecodecamp.org/news/building-a-wikipedia-search-engine-project-4d84de3841d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t0FLqKuduU0MH0tT6mvG9w.jpeg
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: learning
  slug: learning
- name: General Programming
  slug: programming
seo_title: Création d'une application de recherche Wikipedia
seo_desc: 'By Ayo Isaiah

  I just finished Free Code Camp’s Wikipedia Viewer app, where you pull articles side-by-side
  from Wikipedia using the MediaWiki Web API.

  The agile user stories were:


  Users can type queries in a search box and view the resulting Wikipedi...'
---

Par Ayo Isaiah

Je viens de terminer l'application [Wikipedia Viewer](https://www.freecodecamp.com/challenges/build-a-wikipedia-viewer) de Free Code Camp, où vous récupérez des articles côte à côte depuis Wikipedia en utilisant l'API Web MediaWiki.

Les histoires d'utilisateurs agiles étaient :

* Les utilisateurs peuvent taper des requêtes dans une boîte de recherche et voir les entrées Wikipedia résultantes.
* Les utilisateurs peuvent voir des articles Wikipedia aléatoires en cliquant sur un bouton.

J'ai terminé ce projet assez rapidement, car je savais exactement quoi faire après avoir regardé l'API MediaWiki, ce qui était peut-être grâce à mon expérience avec le [Projet Météo](http://www.ayoisaiah.com/weather-app/).

#### Design

![Image](https://cdn-media-1.freecodecamp.org/images/TC-gTYPg3lFv5q4LkFi5hnNb0y9OdMgEaTd1)

En réfléchissant à des idées de design pour ce projet, j'ai décidé de regarder la page d'accueil de Google et sa page de résultats de recherche pour voir comment ils géraient les choses. J'ai fini par prendre la plupart de mon inspiration de design chez eux, comme vous le verrez.

Tout d'abord, la page d'accueil a le titre, la boîte de recherche et les boutons au centre de la page. Le bouton "J'ai de la chance" vous envoie vers une page Wikipedia aléatoire, ce qui a rempli la deuxième histoire d'utilisateur.

Lorsque la page se charge, le focus est donné à la boîte de recherche afin que l'utilisateur puisse commencer à taper sa requête immédiatement, grâce au JavaScript suivant :

```
window.onload = function() { document.getElementById("wiki-search-input").focus();};
```

Une chose que j'ai un peu expérimentée est l'affichage de la page des résultats dès que vous commencez à taper dans la boîte de recherche, en imitant cette fonctionnalité sur Google search.

![Image](https://cdn-media-1.freecodecamp.org/images/bul6ePnr10cm5B4Bd8Phw-n92T3doIbodTTr)

J'ai pu reproduire cela sur mon application, mais je n'étais pas sûr de son fonctionnement sur les écrans tactiles car, lors de mes tests, la page ne répondait pas aux pressions sur les touches de mon téléphone.

Pour éviter un comportement inattendu, j'ai abandonné cette idée et j'ai affiché la page des résultats uniquement lorsque la requête était entièrement saisie et que le bouton "rechercher" ou la touche Entrée était pressée. Cela a bien fonctionné sur toutes les plateformes mobiles et de bureau que j'ai testées.

Dans l'ensemble, mon design n'est pas révolutionnaire, mais tant qu'il s'adapte correctement à tous les types d'appareils, c'est assez bien pour moi.

#### Logique

En plongeant dans le code qui a récupéré les résultats de Wikipedia, ce n'était pas si difficile d'utiliser l'API, pour être honnête.

J'ai essayé de relever ce défi en utilisant la méthode jQuery _$.getJSON_ pour faire l'appel API comme je l'ai fait avec l'API Open Weather, mais elle a retourné un message d'erreur concernant le partage de ressources cross-origin (CORS).

En enquêtant davantage, j'ai trouvé une autre méthode jQuery _$.ajax()_ sur Stack Overflow qui a fonctionné. Apparemment, je devais spécifier le dataType comme "JSONP" (JSON avec Padding) pour que cela fonctionne.

```
function ajax (keyword) {  $.ajax({     url: "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + keyword + "&prop=info&inprop=url&utf8=&format=json",    dataType: "jsonp",   success: function(response) {       console.log(response.query);       if (response.query.searchinfo.totalhits === 0) {         showError(keyword);       }
```

```
       else {         showResults(response);       }  },
```

```
   error: function () {    alert("Erreur lors de la récupération des résultats de recherche, veuillez actualiser la page");   }  });
```

```
}
```

J'ai découvert que l'URL et le titre de chaque page étaient presque exactement les mêmes. La seule différence était que les espaces dans le titre étaient remplacés par des traits de soulignement dans l'URL.

Ainsi, "JavaScript Libraries" devient "JavaScript_Libraries" dans l'URL.

Simplement en récupérant chaque titre, j'ai remplacé les espaces par des traits de soulignement en utilisant un peu de Regex (que je ne connais pas très bien encore, je l'admets) et je l'ai attaché au résultat de recherche correspondant.

```
var title = callback.query.search[m].title;var url = title.replace(/ /g, "_");
```

```
$(".title-" + m).html("<a href=https://en.wikipedia.org/wiki/" + url + "' target='_blank'>" + callback.query.search[m].title + "</a>");
```

La dernière chose que j'ai faite a été de créer une fonction d'erreur afin que si une requête d'utilisateur ne correspond à aucun résultat, elle affiche simplement quelques conseils sur la page pour aider l'utilisateur à améliorer sa recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/nxBqsMnB8FPT8Y-Wxw8XjAQAeWW-NcW1AtQn)

Comme vous pouvez le voir, la communauté open source de Free Code Camp n'a pas encore d'article Wikipedia (malgré le fait d'avoir plus de 300 000 membres). Si vous êtes un contributeur fréquent de Wikipedia, voici [la demande d'article en attente](https://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Education#Open_source_community_focused_on_coding_education_wants_your_help) pour que vous en créiez un.

Donc, c'était à peu près tout pour ce projet. Vous pouvez voir le résultat final sur [Codepen](http://codepen.io/ayoisaiah/full/Kzvrbp).

#### Qu'est-ce qui suit

Je suis à moitié terminé avec le projet Twitch API au moment où j'écris ceci. La plupart du design est fait, il ne me reste plus qu'à comprendre quelques choses avec l'API.

Alors qu'un nouveau semestre à mon université commence cette semaine, les choses pourraient devenir un peu plus lentes avec Free Code Camp, mais cela ne devrait pas m'empêcher de mettre quelques heures chaque jour.

Si vous voulez me contacter ou vous connecter avec moi, vous pouvez me trouver sur [Twitter](https://twitter.com/ayisaiah) ou [m'envoyer un email](mailto:ayisaiah@gmail.com).

Merci d'avoir lu.

Une version de cet article a été initialement publiée sur [mon blog personnel](http://ayoisaiah.com).