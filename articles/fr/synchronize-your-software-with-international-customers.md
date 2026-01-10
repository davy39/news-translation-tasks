---
title: Comment gérer les fuseaux horaires et synchroniser votre logiciel avec des
  clients internationaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-07T16:51:45.000Z'
originalURL: https://freecodecamp.org/news/synchronize-your-software-with-international-customers
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/steven-hille-VP25o26erko-unsplash.jpg
tags:
- name: i18n
  slug: i18n
- name: internationalization
  slug: internationalization
- name: programing
  slug: programing
- name: Web Development
  slug: web-development
seo_title: Comment gérer les fuseaux horaires et synchroniser votre logiciel avec
  des clients internationaux
seo_desc: 'By Jérémy Bardon

  When you develop some software you may not think about timezones at first. Unless
  you live in a country which has to deal with multiple time zones, such as the United
  States or Russia.

  I recently came across an issue involving timezo...'
---

Par Jérémy Bardon

Lorsque vous développez un logiciel, vous ne pensez peut-être pas aux fuseaux horaires au début. Sauf si vous vivez dans un pays qui doit gérer plusieurs fuseaux horaires, comme les États-Unis ou la Russie.

Je suis récemment tombé sur un problème impliquant les fuseaux horaires. Il y avait des tests unitaires qui faisaient des assertions sur des dates qui fonctionnaient dans mon bureau en France mais qui ne fonctionnaient pas au Maroc pour les nouveaux membres de notre équipe.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1-2.png)
_Voici le test unitaire qui fonctionne en France mais pas au Maroc_

C'était l'occasion pour moi d'apprendre à gérer correctement les dates et les heures pour un logiciel international. Dans cet article, je vais présenter les problèmes de fuseaux horaires et partager quelques règles à suivre.

## Introduction rapide aux fuseaux horaires

Comme la Terre est une sorte de sphère, le soleil se lève au Japon alors qu'il se couche en Amérique. Si tout le monde utilisait l'heure globale, disons que `09:00` serait le lever du soleil au Japon, mais pour les Américains, ce serait le coucher du soleil. Pas très pratique.

Pour s'assurer que l'heure est coordonnée avec le soleil pour tout le monde, il est nécessaire de décaler l'heure globale selon votre emplacement. En conséquence, le globe est divisé en **fuseaux horaires** et chacun obtient un **décalage**. Ce décalage est un nombre de minutes à ajouter à l'heure globale pour obtenir l'heure de votre fuseau horaire. Il peut être positif ou négatif.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/2-2.png)
_Fuseaux horaires standard du monde — Illustration par [Wikimedia Commons](https://commons.wikimedia.org/wiki/User:Hellerick" rel="noopener">Hellerick</a> de <a href="https://en.wikipedia.org/wiki/File:Standard_World_Time_Zones.png" rel="noopener)_

L'heure globale est appelée [**UTC**](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)**,** ce qui signifie Temps Universel Coordonné. Vous avez peut-être aussi entendu parler du [**GMT**](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) qui est un fuseau horaire sans aucun décalage.

Par exemple, lorsque c'est `10:50` à l'UTC, c'est aussi `03:50` à San Francisco avec un décalage de `-0700` et `18:50` à Pékin avec un décalage de `+0800`. Pourtant, le décalage n'est pas seulement en heures entières : le décalage du Népal est `+0545`. Vous pouvez vérifier cela sur [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

En plus de ce décalage, qui vient avec le fuseau horaire, certains pays changent aussi l'heure deux fois par an. [**L'heure d'été ou DST**](https://en.wikipedia.org/wiki/Daylight_saving_time) ajoute une heure au décalage du fuseau horaire avant l'été. Ensuite, l'heure est réinitialisée à l'heure du fuseau horaire en hiver. Le but est de rendre la journée plus longue.

La manière la plus courante de déterminer un fuseau horaire est d'utiliser la [Base de données des fuseaux horaires IANA](https://www.iana.org/time-zones). Vous obtenez une chaîne telle que `Europe/Paris` suivant le modèle Zone/Ville. De plus, Microsoft maintient sa propre [Base de données des fuseaux horaires Microsoft](https://support.microsoft.com/en-us/help/973627/microsoft-time-zone-index-values) utilisée sur ses systèmes d'exploitation. Mais cela peut [causer des problèmes](https://devblogs.microsoft.com/dotnet/cross-platform-time-zones-with-net-core/) lors de l'exécution d'applications .NET Core multiplateformes.

IANA reste la référence. La base de données Microsoft n'est pas souvent mise à jour, elle contient moins d'historique, des noms de fuseaux horaires assez curieux (par exemple : `Romantic Standard Time`) et est sujette aux erreurs. Par exemple, essayez de ne pas confondre `Arab`, `Arabic` et `Arabian Standard Time`. Pour plus de détails sur chaque base de données et leurs différences, [consultez cet article](https://codeofmatt.com/what-is-a-time-zone/).

Une dernière chose : il existe de nombreuses façons d'écrire une date. Heureusement, la [**spécification ISO 8601**](https://en.wikipedia.org/wiki/ISO_8601) établit une règle commune pour le formatage des dates.

```
11 novembre 2018 à 00:51:43 (dans un fuseau horaire à UTC+00:00)
2018-11-05T12:51:43Z <- Z signifie UTC

11 novembre 2018 à 00:51:43 (dans un fuseau horaire à UTC +07:30)
2018-11-05T12:51:43+0730
```

## Comment les ordinateurs gèrent les dates

Les ordinateurs ne peuvent effectuer des opérations qu'en utilisant des nombres. Cela signifie que `2020-08-01 +1` n'est pas égal à `2020-08-02` et ne peut pas être traité.

Pour travailler plus facilement avec les dates, nous pouvons représenter les dates sous forme de nombres. C'est ce que sont les **timestamps**. C'est le nombre de millisecondes écoulées depuis une date prédéfinie (ou **époque**) jusqu'à la date spécifiée.

Bien, choisissons une époque alors ! En fait, l'époque commune a déjà été définie et sa valeur est le **1er janvier 1970 (minuit UTC)**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/3-2.png)

Pour vous assurer que vous avez compris, exécutez l'extrait précédent dans votre navigateur. Quoi ? Vous n'avez pas obtenu le même résultat ?

D'accord, j'ai un peu triché pour obtenir ce résultat… Je devrais obtenir `Thu Jan 01 1970 01:00 GMT+0100` parce que le fuseau horaire de mon ordinateur est réglé sur Europe/Paris.

En fait, ce moment avec un timestamp à zéro est minuit à Greenwich, mais aussi `05:45` à Mumbai et même `1969-12-31T16:30` à San Francisco lorsque vous considérez leur décalage de fuseau horaire.

> Règle #1 : Les timestamps sont uniquement pour l'enregistrement, pas pour l'affichage. Il est considéré en UTC car il n'inclut aucun décalage ou fuseau horaire.

Vous n'avez pas obtenu la date « correcte » auparavant parce que JavaScript utilise votre fuseau horaire local pour vous montrer la date/heure la plus précise.

Maintenant, essayez l'extrait suivant. Je suis sûr que vous obtiendrez le même résultat que moi :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/4-2.png)

Oui, le timestamp zéro est `1970-01-01T00:00:00` **à l'UTC** pour tout le monde autour du globe. Pourtant, ce n'est pas vrai si vous choisissez un autre fuseau horaire.

Pour résumer, `toString` affiche la date en utilisant votre fuseau horaire local tandis que `toUTCString` est basé sur l'UTC. De plus, ne vous laissez pas tromper par `toISOString` qui est le même que `toUTCString` mais sort le format ISO 8601 (son nom devrait être `toUTCISOString`).

Je recommande la [commande date](http://man7.org/linux/man-pages/man1/date.1.html) pour convertir un timestamp en secondes (pas en millisecondes) en une chaîne lisible. L'utilisation de cette commande avec l'option UTC garantit qu'elle ne tient pas compte du fuseau horaire de votre ordinateur/navigateur.

```bash
# Linux
$ date -d @1586159897 -u 
Mon Apr  6 07:58:17 UTC 2020

# Pour les utilisateurs d'Osx
$ date -r 1586159897 -u 
```

## Corrigons notre test unitaire

Le problème que j'ai rencontré avec les fuseaux horaires était dans mes tests unitaires. Prenez le temps de le lire et de comprendre ce qu'il est censé vérifier :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/6-2.png)

Dans ce test, le but est de vérifier que `setHours` définit les heures et les minutes de la date à zéro (minuit). Je choisis d'abord un timestamp aléatoire qui n'est pas à minuit. Ensuite, je compare le résultat avec le timestamp pour le même jour à minuit.

En fait, cela fonctionne – mais seulement si votre décalage de fuseau horaire est `+0200` (y compris l'heure d'été) à ce moment-là. Par exemple, cela ne fonctionne pas pour Africa/Casablanca (`+0100` y compris l'heure d'été). Voyons comment ces timestamps sont imprimés :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/7-2.png)

C'est ça, la date UTC pour les deux résultats n'est pas la même. Cela signifie également que les timestamps résultants ne sont pas les mêmes non plus.

Comme vous pouvez le voir, le décalage pour Paris est `+0200` et `+0100` pour Casablanca. Mais les deux affichent minuit avec `toString`. Cela signifie que la fonction `setHours` utilise le fuseau horaire de votre ordinateur pour effectuer l'opération. Et `toString` affiche la date en utilisant votre fuseau horaire.

Ce n'est pas le seul problème avec ce test : que se passe-t-il si vous exécutez ce test à San Francisco ? Exact, le jour serait `2020-07-31` pour les deux dates à cause du décalage `-0700`.

La manière la plus sûre de rendre ce test fiable et de le faire fonctionner partout dans le monde est d'utiliser une date dans votre fuseau horaire local. Vous n'utiliserez plus de timestamps pour définir les dates initiales.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/8-2.png)

Nous pouvons améliorer la règle précédente sur les timestamps :

> Règle #2 : Les dates sous forme de chaînes sont adaptées pour l'affichage en utilisant le fuseau horaire de l'utilisateur et pour les calculs. Elles ne sont pas en UTC mais incluent généralement un décalage.

## Gardez la date côté serveur

La règle sur les timestamps s'applique toujours côté serveur. Cependant, la deuxième règle sur l'utilisation des dates sous forme de chaînes ne peut pas être utilisée.

En effet, dans certains cas avec des technologies comme PHP, Java et Rails, les pages sont rendues côté serveur ([SSR](https://www.quora.com/What-is-the-difference-between-client-side-and-server-side-rendering-Why-is-server-side-rendering-required-for-React-and-Redux)). Cela signifie que tout le HTML est généré par le serveur et qu'il n'a aucune idée du fuseau horaire du client. Pensez au serveur – ce n'est rien de plus qu'un ordinateur sur le globe. Il a aussi son propre fuseau horaire mais il n'est pas nécessairement le même que celui du client.

> Règle #3 : Les serveurs peuvent soit connaître le fuseau horaire du client, soit envoyer une date en UTC. Le fuseau horaire du serveur n'a pas d'importance.

La nouvelle API Date/Heure de Java 8 est considérée comme l'une des API les plus compréhensibles et claires qui vous aide à gérer les dates. Je ne vais pas expliquer comment elle fonctionne ici, mais passons en revue quelques points intéressants.

`LocalDateTime`, `OffsetDateTime` et `ZonedDateTime` sont les 3 classes fournies pour calculer et afficher la date et l'heure. Plus de `Date` ou `DateTime` qui mélangent l'affichage de la date locale et de la date UTC.

Les exemples suivants sont extraits de [cet article génial](https://yawk.at/java.time/) (écrit par Jonas Konrad) qui décrit l'API Date/Heure de Java 8 avec une série d'exemples. Au fait, un grand merci à lui, il m'a gentiment permis de citer ses morceaux de code !

Regardons les différences entre les 3 classes :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/9-2.png)

Il y a une petite mais importante différence entre `OffsetDateTime` et `ZonedDateTime`, l'avez-vous remarquée ?

Comme son nom l'indique, `OffsetDateTime` n'est conscient que d'un décalage entre la date locale et l'UTC. Cela signifie qu'il gère l'heure d'été différemment d'une date qui est attachée à un fuseau horaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/10-2.png)

L'exemple avec un fuseau horaire semble être le bon comportement. En fait, les deux sont corrects car ajouter 1 jour peut signifier soit :

* Ajouter 1 jour et garder la même heure (gère l'heure d'été avec `ZonedDateTime`)
* Ajouter 24 heures à la date actuelle (avec `OffsetDateTime`).

Vous souvenez-vous de la Règle #1 sur les timestamps ? Vous ne devriez utiliser un timestamp UTC que pour l'enregistrement. L'API Java fournit une classe `Instant` qui est un timestamp que vous pouvez obtenir à partir de n'importe laquelle des trois classes utilisées pour afficher la date.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/11-2.png)

## Réflexions finales

Dans cet article, vous avez appris que les timestamps sont pour l'enregistrement (Règle #1) et les dates sous forme de chaînes sont pour l'affichage (Règle #2). Avez-vous remarqué que le nombre de secondes depuis l'époque est assez grand ?

C'est pourquoi après le [problème du bug de l'an 2000 (Y2K)](https://en.wikipedia.org/wiki/Year_2000_problem) vient le [problème Y2K38](https://en.wikipedia.org/wiki/Year_2038_problem) qui représente l'année 2038. À `2038-01-19T03:14:07Z`, le timestamp (en secondes) atteindra son maximum pour les entiers signés 32 bits `2,147,483,647`. Il deviendra alors un nombre négatif après l'ajout d'une seconde supplémentaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/5-2.jpg)
_Ce panneau indique janvier 1900 au lieu de janvier 2000 — Photo de [Wikipedia Commons](https://en.wikipedia.org/wiki/File:Bug_de_l%27an_2000.jpg" rel="noopener)_

Sur les forums, les gens disent qu'ils s'en moquent parce que leur logiciel ne sera pas utilisé pendant 20 ans sans être réécrit. Eh bien, cela peut être vrai, mais réfléchissons tout de même à quelques solutions (avec MySQL) :

* Mettre à jour le type `TIMESTAMP` vers des entiers signés 64 bits
* Enregistrer les dates UTC dans des colonnes `DATETIME` au lieu de `TIMESTAMP`

Les deux solutions ont leurs avantages et leurs inconvénients. La première semble être un hack qui reporte le problème plus tard. Pourtant, elle corrige le problème pour une période presque infinie (milliards d'années). Votre logiciel sera obsolète et ne sera plus utilisé lorsque le problème se reproduira.

La deuxième solution fonctionne également pendant très longtemps (jusqu'à `9999-12-31T23:59:59Z`).

L'utilisation de `TIMESTAMP` est recommandée pour les logs, tandis que `DATETIME` est meilleur pour les autres besoins. N'oubliez pas qu'un timestamp ne peut pas stocker une date antérieure à `1970-01-01T00:00:00Z` et pas après `2038-01-19T03:14:07Z`. Cela signifie que vous devriez utiliser `DATETIME` pour enregistrer des dates très anciennes ou futures.

De plus, dans MySQL, les `TIMESTAMP` sont stockés en UTC mais affichés selon un fuseau horaire spécifié (et convertis en UTC avant l'enregistrement). Ce mécanisme est pratique lorsque vous avez besoin d'obtenir une date locale et n'existe pas avec `DATETIME`.

Un dernier mot sur [moment.js](https://momentjs.com/), une bibliothèque populaire pour gérer les dates. J'ai d'abord expérimenté un problème et je voulais vous en avertir :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/12sq-2.png)

Les deux `console.log` afficheront `2020-08-02 00:00`. Si vous êtes habitué à la programmation fonctionnelle, vous vous attendez à ce que `hours` et `minutes` retournent un nouvel objet moment car ce sont des [fonctions pures](https://en.wikipedia.org/wiki/Pure_function). Ce n'est pas le cas – elles modifient la date d'entrée et la retournent pour un enchaînement facile.

Merci d'avoir lu jusqu'à la fin. J'espère que cette expérience m'a été utile. D'ailleurs, je ne suis pas très confiant quant au choix entre `TIMESTAMP` et `DATETIME`, alors n'hésitez pas à partager votre expérience !

**Si vous avez trouvé cet article utile, veuillez le partager sur les réseaux sociaux pour aider les autres à le trouver et pour montrer votre soutien !** 💡

**N'oubliez pas de consulter ma [page d'auteur](https://www.freecodecamp.org/news/author/jbardon/) pour les articles à venir** ✨