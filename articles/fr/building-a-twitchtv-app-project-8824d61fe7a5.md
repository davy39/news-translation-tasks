---
title: Création d'une application de statut TwitchTV
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-21T22:48:31.000Z'
originalURL: https://freecodecamp.org/news/building-a-twitchtv-app-project-8824d61fe7a5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9j9Qs6T6aOVoclHT5bKILw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Création d'une application de statut TwitchTV
seo_desc: 'By Ayo Isaiah

  Last week, I tackled the last of the Intermediate Front-End Projects which involved
  building a TwitchTv App using the Twitch API to display the status of a set of Twitch
  Streamers.

  These were the user stories for this project:


  ​Users c...'
---

Par Ayo Isaiah

La semaine dernière, j'ai abordé le dernier des projets intermédiaires de Front-End qui consistait à créer une [application TwitchTv](https://www.freecodecamp.com/challenges/use-the-twitchtv-json-api) en utilisant l'API Twitch pour afficher le statut d'un ensemble de streamers Twitch.

Voici les histoires utilisateur pour ce projet :

1. Les utilisateurs peuvent voir si Free Code Camp est actuellement en streaming sur Twitch.tv.
2. Les utilisateurs peuvent cliquer sur le statut affiché et être redirigés directement vers la chaîne Twitch.tv de Free Code Camp.
3. Si un streamer Twitch est actuellement en streaming, les utilisateurs peuvent voir des détails supplémentaires sur ce qu'ils diffusent.
4. Les utilisateurs verront une notification de remplacement si un streamer a fermé son compte Twitch (ou si le compte n'a jamais existé).

#### Design

Le design de mon application est assez similaire à l'[application exemple](https://codepen.io/FreeCodeCamp/full/Myvqmo/) donnée dans la description du projet.

La seule différence majeure est l'entrée de recherche en haut de la page que j'ai ajoutée pour la cinquième histoire utilisateur (plus d'informations à ce sujet ci-dessous).

J'ai utilisé [Skeleton](http://getskeleton.com/) pour aider avec le style de base et la réactivité afin que tout soit beau sur desktop et mobile.

Pour les photos de profil, j'ai utilisé des images de fond au lieu de balises <img>. Cela est dû au fait qu'en définissant simplement la taille de l'arrière-plan sur cover, cela permet à l'image de s'adapter à la taille de son conteneur, peu importe les dimensions.

C'est quelque chose que j'ai appris en travaillant sur le projet [Random Quote Generator](http://ayoisaiah.com/random-quote-generator/) et c'était agréable de le mettre à nouveau en pratique ici.

![Image](https://cdn-media-1.freecodecamp.org/images/Te2UyJHHenHzhMOW6VdlOxMoBvNopa2dduPY)

### Processus de réflexion

Tout d'abord, j'ai créé un tableau de streamers Twitch et utilisé une boucle for pour parcourir le tableau et faire des requêtes AJAX consécutives afin de pouvoir récupérer les données pour chaque streamer.

```
var twitchStreamers = ["dreamhackcs", "skyzhar", "freecodecamp", "faceittv", "comster404", "brunofin", "terakilobyte", "robotcaleb", "sheevergaming", "esl_sc2", "ogamingsc2", "jacksofamerica"];
```

```
...
```

```
for (var i = 0; i < twitchStreamers.length; i++) {        ajax();}
```

```
...
```

```
function ajax () {        $.ajax({            url: "https://api.twitch.tv/kraken/streams/" + twitchStreamers[i] + "?callback=?",            dataType: "jsonp",            data: {                format: "json"            },
```

```
            success: function (data) {                fetchData(data);            },
```

```
            error: function () {                console.log("unable to access json");            }        });    }
```

Si la requête AJAX est réussie, elle appelle une autre fonction _fetchData()_ qui récupère simplement les données requises à partir de la sortie JSON telles que le nom d'utilisateur, le statut, l'URL et l'image de profil pour chaque chaîne et appelle la fonction _updateHTML()_ qui prend simplement les données et met à jour le DOM.

```
function fetchData (data) {
```

```
        if (data.stream === null) {            url = data._links.channel.substr(38);            updateOfflineUsers();        }
```

```
        else if (data.status == 422 || data.status == 404) {            status = data.message;            updateHTML(".unavailable");        }
```

```
        else {            if (data.stream.channel.logo !== null) {                picture = 'url("' + data.stream.channel.logo + '")';            }
```

```
            else {                picture = 'url("https://cdn.rawgit.com/ayoisaiah/freeCodeCamp/master/twitch/images/placeholder-2.jpg")';            }            url = data._links.channel.substr(38);            status = "<a href='https://twitch.tv/" + url + "' target='_blank'" + "'>" + data.stream.channel.display_name +  "</a>" + " est actuellement en streaming " + data.stream.game;            updateHTML(".online");        }    }
```

Pour les streamers hors ligne, il y avait une étape supplémentaire. J'ai dû faire un autre appel API en utilisant [https://api.twitch.tv/kraken/channels/](https://api.twitch.tv/kraken/channels/) pour récupérer les données de chaque chaîne car le premier appel (en utilisant [https://api.twitch.tv/kraken/streams/)](https://api.twitch.tv/kraken/streams/)) ne fournissait aucune information sur les streamers hors ligne sauf le fait qu'ils n'étaient pas actifs à ce moment-là.

```
function updateOfflineUsers () { //Si les utilisateurs sont hors ligne, faire une nouvelle requête ajax pour trouver les informations de l'utilisateur        $.ajax({            url: "https://api.twitch.tv/kraken/channels/" + url,            dataType: "jsonp",            data: {format: "json"},            success: function (json) {                status = "La chaîne " + "'<a href='" + json.url + "' target='_blank'" + "'>" + json.display_name + "</a>'" + " est actuellement hors ligne";                if (json.logo !== null) {                    picture = 'url("' + json.logo + '")';                }                else {                    picture = 'url("https://cdn.rawgit.com/ayoisaiah/freeCodeCamp/master/twitch/images/placeholder-2.jpg")';                }                updateHTML(".offline");            }        });    }
```

Une fois que j'ai mis tout cela en place, les quatre histoires utilisateur étaient terminées et j'étais prêt à partir. À ce stade, j'ai marqué le projet comme terminé, mais peu après, j'ai pensé qu'il serait vraiment cool d'étendre un peu la fonctionnalité de l'application.

C'est à ce moment-là que j'ai ajouté une cinquième histoire utilisateur :

* Les utilisateurs peuvent rechercher des streamers TwitchTv et voir s'ils sont en ligne ou non.

J'ai donc créé une fonction de recherche qui prend l'entrée de l'utilisateur et l'utilise pour faire l'appel API :

```
function search () {        $(".online, .offline, .unavailable").empty();        showAll();          var searchQuery = $(".search-twitch").val();        var user = searchQuery.replace(/[^A-Z0-9_]/ig, "");        $.ajax({            url: "https://api.twitch.tv/kraken/streams/" + user,            dataType: "jsonp",            data: {                format: "json"            },
```

```
            success: function (data) {                fetchData(data);                                }        });    }
```

J'ai utilisé un peu de regex pour supprimer les caractères spéciaux et les espaces de la requête de l'utilisateur, ne laissant que les chiffres, les lettres et les tirets bas. Je pense que c'est important car Twitch n'autorise pas les caractères spéciaux (comme $, &, etc.) ou les espaces dans les noms d'utilisateur, il était donc nécessaire de les filtrer.

Cela aide également si un utilisateur recherche quelque chose comme "free code camp" (en séparant les mots entiers avec des espaces) au lieu de "freecodecamp", cela retourne toujours le résultat pertinent attendu.

![Image](https://cdn-media-1.freecodecamp.org/images/5TCiHaHqv212jU3pcBj5ALPzaMZyjyf7BOMI)

Donc, c'était à peu près tout pour ce projet. Vous pouvez voir la [version finale](http://codepen.io/ayoisaiah/full/MyGjpz/) sur Codepen.

#### Principale leçon

Même si j'écris cet article de blog, plusieurs façons d'améliorer l'expérience utilisateur sur mon application continuent de me venir à l'esprit, donc ma principale leçon de ce projet est :

**Le logiciel n'est jamais terminé.** [C'est un processus et il évolue toujours](http://scripting.com/davenet/1995/09/03/wemakeshittysoftware.html).

#### Prochaines étapes

En ce moment, je travaille dur pour terminer la section [Intermediate Algorithm Scripting](https://www.freecodecamp.com/map-aside#nested-collapseIntermediateAlgorithmScripting) sur FCC dans les prochains jours afin de pouvoir passer rapidement à la section Advanced Algorithm.

Mon objectif (à court terme) reste d'obtenir la [certification Front-End](http://www.freecodecamp.com/challenges/claim-your-front-end-development-certificate) d'ici la fin mai et si tout se passe bien, je devrais pouvoir l'obtenir d'ici là. Souhaitez-moi bonne chance.

*Si vous souhaitez me contacter ou me connecter, vous pouvez me trouver sur [Twitter](https://twitter.com/ayisaiah) ou [m'envoyer un email](mailto:ayisaiah@gmail.com). Une version de cet article a été publiée sur mon [blog personnel](http://www.ayoisaiah.com/twitch-tv-project/).*