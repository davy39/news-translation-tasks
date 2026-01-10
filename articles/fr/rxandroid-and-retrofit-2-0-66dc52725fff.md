---
title: RxAndroid et Retrofit 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-09-17T01:20:38.000Z'
originalURL: https://freecodecamp.org/news/rxandroid-and-retrofit-2-0-66dc52725fff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OlU3vLjcEhu-oKeGeAdqyA.png
tags:
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: Retrofit
  slug: retrofit
- name: rxjava
  slug: rxjava
seo_title: RxAndroid et Retrofit 2.0
seo_desc: 'By Ahmed Rizwan

  Ok, so this isn’t new or anything, but I thought let’s just make a simple tutorial
  with the new Retrofit 2.0. This should give us a starting point.

  This isn’t a tutorial for RxAndroid. If you don’t know much about RxAndroid, you
  shoul...'
---

Par Ahmed Rizwan

Bon, ce n'est pas nouveau ou quoi que ce soit, mais je me suis dit, faisons un simple tutoriel avec le nouveau Retrofit 2.0. Cela devrait nous donner un point de départ.

Ce n'est pas un tutoriel pour RxAndroid. Si vous ne savez pas grand-chose sur RxAndroid, vous devriez d'abord consulter [ceci](https://medium.com/@ahmedrizwan/rxandroid-and-kotlin-part-1-f0382dc26ed8).

Alors, commençons. Voici les choses dont vous aurez besoin avant de commencer :

1. [RxAndroid](https://github.com/ReactiveX/RxAndroid) et [Retrofit](https://github.com/square/retrofit)
2. [Gson](https://github.com/google/gson) (j'utiliserai Gson, vous pouvez utiliser d'autres parseurs également)
3. Une connexion Internet !

Donc, après avoir ajouté les dépendances, vos fichiers gradle devraient ressembler à quelque chose comme ceci (ignorez le plugin [Retrolambda](https://github.com/evant/gradle-retrolambda), je l'ai juste ajouté pour la concision du code parce que... Lambdas ! *_*):

Maintenant, vous vous demandez peut-être, qu'est-ce que Retrofit exactement ? Eh bien, Retrofit est un client HTTP, mais il est type-safe. Cela signifie que vous pouvez transformer une API HTTP en une interface Java. Cela rend ridiculement pratique l'interaction avec l'API.

### L'exemple de départ

Dans l'exemple, je vais utiliser l'API [OpenWeather](http://openweathermap.org) et je vais la garder aussi simple que possible. Je vais simplement obtenir la [prévision météo pour aujourd'hui](http://openweathermap.org/current) en trois étapes.

#### Étape 1 : Générer des classes de modèle Java (Pojo) à partir de JSON

Voici l'URL de l'API :

```
http://api.openweathermap.org/data/2.5/weather?q=London
```

Et la réponse retournée lorsque vous l'appelez est :

```
{ "coord": { "lon": -0.13, "lat": 51.51 }, "weather": [ { "id": 521, "main": "Rain", "description": "shower rain", "icon": "09d" } ], "base": "cmc stations", "main": { "temp": 289.49, "pressure": 993, "humidity": 67, "temp_min": 285.93, "temp_max": 291.15 }, "wind": { "speed": 8.7, "deg": 210, "gust": 14.4 }, "rain": { "1h": 1.02 }, "clouds": { "all": 40 }, "dt": 1442242382, "sys": { "type": 1, "id": 5091, "message": 0.0052, "country": "GB", "sunrise": 1442208848, "sunset": 1442254609 }, "id": 2643743, "name": "London", "cod": 200}
```

Cela semble assez désordonné, n'est-ce pas ? Eh bien, ne vous inquiétez pas, allez simplement sur ce site génial [website](http://www.jsonschema2pojo.org) et collez le JSON. Cela ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pD1QD3UiI0A4M9yidSIaVQ.png)

Si le JSON a trop de classes de modèle à générer, la chose la plus facile à faire est de générer un **Jar** et de le télécharger, de l'extraire, puis d'ajouter les fichiers. Sinon, cliquez simplement sur Aperçu, et copiez-collez les classes dont vous avez besoin. Supprimez l'annotation **@Generated("org.jsonschema2pojo")** de chaque classe de modèle, car cette annotation n'est pas reconnue par Android par défaut.

J'ai téléchargé le Jar car il y a beaucoup de classes. Et aussi parce que je suis paresseux. :)

Après avoir extrait et ajouté les classes, l'arborescence du projet ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HCtSwhgbB3ERajLMixmuyQ.png)

Jusqu'à présent, tout va bien !

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Aok7yzCTbxShebikqfTsw.png)
_Juste un raton laveur maléfique qui fait des siennes._

#### Étape 2 : Créer une interface Retrofit pour vos appels API

Pour Retrofit, vous devez créer une interface pour les endpoints de votre API.

Lors de la création de l'interface, vous devriez vous demander : quelle est exactement la signification de la vie ? Et deuxièmement : quelles informations ai-je besoin de l'API ?

Pour moi, la réponse aux deux questions est WeatherData (l'objet le plus haut). Maintenant, examinons l'URL :

```
http://api.openweathermap.org/data/2.5/weather?q=London
```

Il y a une **requête** à la toute fin, donc je vais faire ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*MDro75UsBFVQHUVFVgAtEg.png)

```
Note : dans Retrofit 2.0, la chaîne de chemin d'endpoint ne doit PAS commencer par "/"
```

```
@GET("/weather?") --> incorrect@GET("weather?")  --> correct
```

Maintenant, en tant que paramètre, je vais envoyer la valeur de la requête en utilisant l'annotation @Query.

Comme vous le remarquerez, je retourne l'**Observable** de WeatherData. C'est Rx là-dedans !

#### Étape 3 : Créer l'adaptateur Retrofit et l'instance WeatherService

Maintenant, dans notre activité, nous devons créer un adaptateur Retrofit en utilisant l'URL de base, ainsi que quelques autres informations. Une fois construit, nous pouvons initier un objet de l'interface **WeatherService**, puis appeler la méthode.

Jetez un coup d'œil à ce code délicieux :

La question ici est, qu'est-ce que ces méthodes _addCallAdapter_ et _addConverterFactory_ font là ?

Eh bien, afin que nos appels retournent le type **Observable**, nous devons définir l'adaptateur d'appel sur **RxJavaCallAdapter**.

Et addConverFactory est là pour dire à Retrofit quel type de convertisseur je veux qu'il utilise pour sérialiser le JSON. Je préfère le convertisseur GSON. Il y a d'autres convertisseurs disponibles également.

Donc, pour ces deux-là, vous devez ajouter leurs dépendances à votre gradle :

```
compile 'com.squareup.retrofit2:adapter-rxjava:2.0.2'compile 'com.squareup.retrofit2:converter-gson:2.0.0'
```

Maintenant, exécutez le code, et voilà ! Il journalisera la description météo.

### Un exemple différent

Alors oui... Un autre exemple ! Pourquoi pas ? Cette fois, je vais essayer l'API GitHub. Encore une fois, juste 3 étapes.

D'abord, l'URL de l'appel API :

```
https://api.github.com/users/ahmedrizwan
```

et la réponse :

```
{    "login": "ahmedrizwan",    "id": 4357275,    "avatar_url": "https://avatars.githubusercontent.com/u/4357275?v=3",    "gravatar_id": "",    "url": "https://api.github.com/users/ahmedrizwan",    "html_url": "https://github.com/ahmedrizwan",    "followers_url": "https://api.github.com/users/ahmedrizwan/followers",    "following_url": "https://api.github.com/users/ahmedrizwan/following{/other_user}",    "gists_url": "https://api.github.com/users/ahmedrizwan/gists{/gist_id}",    "starred_url": "https://api.github.com/users/ahmedrizwan/starred{/owner}{/repo}",    "subscriptions_url": "https://api.github.com/users/ahmedrizwan/subscriptions",    "organizations_url": "https://api.github.com/users/ahmedrizwan/orgs",    "repos_url": "https://api.github.com/users/ahmedrizwan/repos",    "events_url": "https://api.github.com/users/ahmedrizwan/events{/privacy}",    "received_events_url": "https://api.github.com/users/ahmedrizwan/received_events",    "type": "User",    "site_admin": false,    "name": "ahmed",    "company": null,    "blog": "https://medium.com/@ahmedrizwan",    "location": null,    "email": "ahmedrizwan@outlook.com",    "hireable": true,    "bio": null,    "public_repos": 19,    "public_gists": 0,    "followers": 25,    "following": 16,    "created_at": "2013-05-06T18:32:59Z",    "updated_at": "2016-07-08T11:29:26Z"}
```

Encore une fois, le JSON semble assez désordonné.

#### **Étape 1 : Générer les Pojos (Plain Old Java Objects)**

J'ai copié la réponse et l'ai collée [ici](http://www.jsonschema2pojo.org) (encore une fois) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gHJzvU0FcKSNWe6yTjSvLg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*67owad0Zun8o84QOrAWaUA.png)

Et j'ai cliqué sur Aperçu.

Ensuite, j'ai copié la classe Github dans mon projet. *la musique s'intensifie*

#### **Étape 2 : Créer une interface pour les endpoints**

Maintenant, examinez l'URL de l'API. Et je veux dire, examinez-la vraiment. Vous verrez que l'endpoint commence par users et se termine par le nom d'utilisateur.

```
https://api.github.com/users/ahmedrizwan
```

Donc, l'interface que j'ai créée ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jabUA4iGndv51G0d7Pi_9A.png)

J'ai créé une méthode d'appel, et j'ai utilisé l'annotation **@Path** pour remplacer la valeur de _{username}_ dans la chaîne EndPoint de manière dynamique.

#### **Étape 3 : Créer un adaptateur et une instance de GithubService**

Voici le beau code pour faire exactement cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gEbFR7b6wmJWNJg1sSe9sA.png)

Vous remarquerez que je mappe l'objet utilisateur à une chaîne (vous pouvez faire cela avec Rx. Donc, sa sortie devient :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hoXm3j3xqKF9HbEBWK73kQ.png)

Donc, c'est tout. Bien que l'article ne couvre pas tout ce que Retrofit et RxAndroid peuvent faire (bien sûr), j'espère qu'il vous donnera un bon départ.

Bon codage !