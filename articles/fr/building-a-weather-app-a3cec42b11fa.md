---
title: Création d'une Application Météo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-29T20:28:43.000Z'
originalURL: https://freecodecamp.org/news/building-a-weather-app-a3cec42b11fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*59ubn1l9M0KjGGe2Bd9Sxw.jpeg
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: technology
  slug: technology
seo_title: Création d'une Application Météo
seo_desc: 'By Ayo Isaiah

  Last week I tackled Free Code Camp’s Show the Local Weather project, which involved
  building an app that displayed the weather wherever the user happened to be.

  I had to implement the following user stories:


  User can view the weather i...'
---

Par Ayo Isaiah

La semaine dernière, j'ai abordé le projet [Show the Local Weather](https://www.freecodecamp.com/challenges/show-the-local-weather) de Free Code Camp, qui consistait à construire une application affichant la météo là où se trouve l'utilisateur.

J'ai dû implémenter les histoires utilisateur suivantes :

* L'utilisateur peut voir la météo à son emplacement actuel.
* L'utilisateur peut basculer entre les unités de température (Celsius ou Fahrenheit).
* L'icône météo ou l'image de fond changera en fonction des conditions météorologiques.

J'ai décidé d'aller un peu plus loin en ajoutant une autre histoire utilisateur :

* L'utilisateur peut rechercher des informations météorologiques pour d'autres lieux.

#### Design

J'avais plusieurs idées pour le design de cette application et j'ai regardé quelques projets terminés (sans vérifier leur code, bien sûr) de la communauté pour voir ce que les autres affichaient dans leur application et comment cela ressemblait.

Trouver une mise en page finale était un peu délicat, mais j'ai trouvé utile de décider des éléments que je voulais afficher pour l'utilisateur et de construire à partir de là.

L'objectif ici était de garder les choses simples. J'ai décidé de montrer uniquement la température et la description météo en plus de l'heure locale.

J'ai également aimé l'icône météo animée dans le [projet exemple](http://codepen.io/FreeCodeCamp/full/bELRjV) et j'ai pensé que c'était une meilleure représentation de la météo actuelle qu'une image de fond, donc j'ai voulu l'implémenter dans mon application.

Comme d'habitude, j'ai tout noté dans mon [Workflowy](https://workflowy.com/invite/2dbe7482.lnx).

![Image](https://cdn-media-1.freecodecamp.org/images/0*pXrIhfKeyy9-l38u.png)

La configuration de tout était assez simple, sauf pour trouver un ensemble d'icônes animées approprié. J'ai dû chercher un peu avant de trouver [Skycons](https://darkskyapp.github.io/skycons/), que j'ai finalement utilisé.

L'autre chose avec laquelle j'ai eu du mal était de trouver une bonne palette de couleurs pour l'application, et c'est quelque chose avec lequel je lutte presque toujours. J'ai expérimenté différentes combinaisons avant d'arriver au produit final.

![Image](https://cdn-media-1.freecodecamp.org/images/0*e-_dbhFTqw7WMHwg.png)

#### Logique

Après avoir examiné un exemple de réponse API de [Open Weather](http://openweathermap.org/current#geo), j'ai compris que j'aurais besoin d'obtenir la longitude et la latitude de l'utilisateur pour pouvoir servir des informations météorologiques au chargement de la page.

Le moyen le plus simple de le faire était d'utiliser l'API de géolocalisation HTML5, qui était assez simple et avait déjà été couvert dans la section JSON et APIs du programme.

J'ai stocké les valeurs retournées dans des variables déjà déclarées et les ai utilisées pour faire la requête AJAX.

```
if (navigator.geolocation) {
```

```
    // Retourne la longitude et la latitude de l'utilisateur au chargement de la page en utilisant l'API de géolocalisation HTML5
```

```
    window.onload = function () {    var currentPosition;    function getCurrentLocation (position) {        currentPosition = position;        latitude = currentPosition.coords.latitude;        longitude = currentPosition.coords.longitude;
```

```
        // Requête AJAX
```

```
        $.getJSON("http://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&APPID=******************", function (data) {            var rawJson = JSON.stringify(data);            var json = JSON.parse(rawJson);            updateWeather(json); // Mettre à jour les paramètres météo        });    }
```

```
    navigator.geolocation.getCurrentPosition(getCurrentLocation);
```

```
    };
```

L'API Open Weather m'a donné un moyen de mettre à jour l'emplacement, la température et la description météo, mais je devais encore trouver un moyen de mettre à jour l'heure locale. Après quelques recherches, j'ai trouvé une autre API sur [Geonames.org](http://geonames.org/) qui s'en occupait.

```
$.getJSON('http://api.geonames.org/timezoneJSON?lat=' + latitude + '&lng=' + longitude + '&username=ayoisaiah', function(timezone) {            var rawTimeZone = JSON.stringify(timezone);            var parsedTimeZone = JSON.parse(rawTimeZone);            var dateTime = parsedTimeZone.time;            timeFull = dateTime.substr(11);            $(".local-time").html(timeFull); // Mettre à jour l'heure locale            timeHour = dateTime.substr(-5, 2);    });
```

La dernière chose que j'ai faite a été de mettre à jour l'icône météo en fonction des conditions de l'emplacement ou de la ville d'intérêt de l'utilisateur. J'ai décidé qu'une bonne façon de le faire était de vérifier la description météo et de changer l'icône en fonction de celle-ci.

J'ai donc considéré quelques scénarios possibles tels que ciel dégagé, nuageux, neige, ensoleillé, pluie, etc., et j'ai écrit une série de déclarations conditionnelles pour vérifier si la description météo contenait l'un de ces mots-clés et ensuite mettre à jour l'icône météo.

```
// Mettre à jour l'animation météo en fonction de la description météo retournée
```

```
    var weather = json.weather[0].description;
```

```
    if(weather.indexOf("rain") >= 0) {        skycons.set("animated-icon", Skycons.RAIN);    }
```

```
    else if (weather.indexOf("sunny") >= 0) {        skycons.set("animated-icon", Skycons.CLEAR_DAY);    }
```

J'ai découvert, à travers divers tests, que cette méthode n'est pas infaillible à 100 %, mais elle fonctionnait suffisamment bien pour que je m'y tienne.

Vous pouvez consulter le code complet et les effets sur [Codepen](http://codepen.io/ayoisaiah/full/LNLzgx/).

#### Principale leçon

Ma principale leçon de ce projet est que j'ai appris à accéder à chaque partie des données JSON retournées par la réponse de l'API et à les utiliser de différentes manières. Bien que ma méthodologie ait besoin d'être affinée, elle est destinée à s'améliorer avec plus de pratique.

#### Qu'est-ce qui suit...

Le prochain projet pour moi est l'application [Wikipedia Viewer](https://www.freecodecamp.com/challenges/build-a-wikipedia-viewer). Je suis déjà à moitié terminé au moment où j'écris cet article, donc il devrait être terminé d'ici jeudi au plus tard.

*Si vous souhaitez me contacter ou me connecter, vous pouvez me trouver sur [Twitter](https://twitter.com/ayisaiah) ou [m'envoyer un email](mailto:ayisaiah@gmail.com). Merci pour la lecture.*