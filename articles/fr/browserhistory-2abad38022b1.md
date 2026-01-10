---
title: L'Avenir de l'Historique du Navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-07T15:08:13.000Z'
originalURL: https://freecodecamp.org/news/browserhistory-2abad38022b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LQcSLDoKyWBuwAEgcwKNyw.png
tags:
- name: Browsers
  slug: browsers
- name: Design
  slug: design
- name: internet
  slug: internet
- name: search
  slug: search
- name: Web Design
  slug: web-design
seo_title: L'Avenir de l'Historique du Navigateur
seo_desc: 'By Patryk Adaś

  I am really unsatisfied with the current state of Browser History. I think that
  this is the most underestimated feature of every modern web browser. Let’s take
  the most popular browser as an example.

  Before we talk about browsers histo...'
---

Par Patryk Adaś

Je suis vraiment insatisfait de l'état actuel de l'historique des navigateurs. Je pense que c'est la fonctionnalité la plus sous-estimée de chaque navigateur web moderne. Prenons [le navigateur le plus populaire](http://www.w3schools.com/browsers/browsers_stats.asp) comme exemple.

Avant de parler de l'historique des navigateurs, nous devons comprendre comment nous avons tendance à naviguer de nos jours.

Parfois, je veux savoir comment convertir 1 pied en centimètres.

![Image](https://cdn-media-1.freecodecamp.org/images/3Zbc8a23p4y7pKpzdDsCmxiy-epvY-7l2Cvu)

Parfois, en revanche, je veux savoir pourquoi et comment les choses se produisent.

Pour le second type de recherche, le modèle standard de récupération de correspondances ne suffit pas vraiment.

#### Problème

Je peux rechercher le terme dans Google, mais je n'obtiendrai pas un seul résultat qui répond à ma question. Au contraire, j'obtiendrai beaucoup de résultats, et tous ces résultats auront des morceaux d'informations qui me sont pertinents.

Ensuite, je vais explorer l'internet, en collectant de nombreux onglets en cours de route. Certains de ces onglets seront des impasses, donc je les ferme.

Certains de ces onglets seront pertinents et auront vingt liens supplémentaires, donc je les ouvre tous, et de cette manière, je continue à naviguer.

![Image](https://cdn-media-1.freecodecamp.org/images/sdqxpVVN6iLU-HDDFSI2M2ov7vtUJHVRrNbZ)
_Onglets, onglets, onglets_

Ensuite, après un certain temps, j'ai un nuage de pages dans ma tête que j'ai visitées et la réponse est plus ou moins complète.

**Mais si j'essaie de revisiter cela plus tard, c'est impossible. Je peux me souvenir de ce que j'ai trouvé, mais ce n'était pas une progression linéaire, donc mon historique de navigateur est inutile.**

Malgré le fait que nous vivions dans une société axée sur les données, alors que de plus en plus de bases de données sont mises en ligne, les informations complexes et variées disponibles à découvrir dépendent de la qualité de nos recherches.

De manière formelle, nous sommes passés du [**Modèle Classique de Récupération**](https://en.wikipedia.org/wiki/Standard_Boolean_model), à ce qu'on appelle, [**Recherche par Cueillette**](https://en.wikipedia.org/wiki/Cognitive_models_of_information_retrieval#Berrypicking).

![Image](https://cdn-media-1.freecodecamp.org/images/kq3EfxFUeLeWb1wntudhJaJawNOoGdjTAyvR)
_Modèle Classique de Récupération_

La requête n'est pas satisfaite par un seul ensemble final récupéré, mais par une série de sélections de références individuelles et de morceaux d'informations à chaque étape de la recherche en constante modification.

En d'autres termes, nous ne recherchons généralement pas quelque chose qui mène à un seul résultat répondant à notre question, mais nous recherchons des termes puis explorons l'internet, en reliant des morceaux de la réponse au fur et à mesure que nous lisons à travers le réseau d'onglets que notre recherche commence pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/bfDZQyAshRHDuNX4RLXVvqYkR8az7d-gdMjT)
_Recherche par Cueillette_

Nos besoins de recherche, et par conséquent notre historique de navigateur, ne sont plus satisfaits par une seule requête. Nous passons par une variété de sources, chaque nouveau morceau d'information nous donnant de nouvelles idées et directions à suivre. Sans que nous le sachions jamais, nos requêtes de recherche fluctuent constamment.

![Image](https://cdn-media-1.freecodecamp.org/images/-PZnFv6lzqobD-nn87cTRtPsjtDYqeoZXJeC)
_Historique Actuel de Google Chrome_

Malheureusement, notre solution actuelle pour trouver une page web non marquée consiste à retracer nos propres pas à travers différents liens.

Cela exige que les utilisateurs aient suffisamment d'informations pour décrypter la page souhaitée parmi toutes les autres en reconnaissant les en-têtes, les URLs obscures ou les horodatages.

L'historique de notre navigateur devrait refléter notre comportement sur l'internet et nous aider à comprendre le processus derrière celui-ci. Il est crucial de vraiment comprendre et de remettre en question la manière dont nous utilisons l'internet, et sans les outils appropriés, cela n'est pas possible.

#### Solution

Je trouve des réponses dans les cartes.

![Image](https://cdn-media-1.freecodecamp.org/images/UgFIwp8RE5sFo5ZFDHjIgG3pDF1Yx6FeiCw2)
_Page Principale_

![Image](https://cdn-media-1.freecodecamp.org/images/EKCbMxudMvj1vOh1F7ph8R54uO317fBT0mM-)
_:hover_

En haut, il y a une timeline, les positions sont toujours affichées chronologiquement, mais les utilisateurs peuvent également voir les connexions.

Non seulement c'est une approche différente pour parcourir notre propre contenu, il est maintenant possible de voir les schémas de mes requêtes de recherche et comportements. De cette manière, notre historique de navigateur ne remplit pas seulement une fonction de récupération, mais écrit également un récit.

Je comprendrai enfin pourquoi j'ai fini par lire sur l'influence des plantes sur les propriétés du sol, alors que j'ai commencé avec une requête sur le BBQ du Texas.

Avec cette méthode, je suis en mesure de voir d'un coup d'œil comment différentes pièces d'information sont connectées, comment elles se rapportent les unes aux autres et comment j'ai formé des conclusions. Je vois comment j'ai réellement cogné les choses qui sont pertinentes. Il ne s'agit pas seulement de l'objectif, mais aussi du voyage.

Dans l'interface proposée, avec une simple action de survol, je reçois des pièces essentielles d'information. Je suis en mesure de comprendre mon processus de pensée et les points d'intérêt. Il est également plus facile de se souvenir de la page grâce à des schémas de couleurs particuliers et des sections méta.

![Image](https://cdn-media-1.freecodecamp.org/images/uS98aCp5AzUUav4iC-EkcthYwsDedM7kIPqp)
_Page Unique_

Disons que j'ai déjà trouvé ce que je cherchais et que je suis satisfait de mon processus de récupération d'informations.

Combien de fois ai-je visité ce site web ? Combien de temps ai-je passé à l'utiliser ? Quand ai-je vu quelque chose d'intéressant ? À quelle fréquence le visite-je ? À quoi ressemble mon trafic généré, du point de vue d'une page particulière ?

![Image](https://cdn-media-1.freecodecamp.org/images/uvDfyeWH951-UfwVjzrxjdM7eXMlJEnFveOJ)
_Menu déroulant Supprimer_

Ils disent de [ne jamais faire confiance à une personne avec un historique vide](https://twitter.com/davidwalshblog/status/535608920908115968).

![Image](https://cdn-media-1.freecodecamp.org/images/3RdQ71ITn210Me0thEnFVqqkOxG63waFoZnc)
_Recherche_

Google est l'un des meilleurs moteurs de recherche disponibles et pourtant, dans l'historique du navigateur, il n'y a même pas de place pour l'auto-suggestion. Comment cela se fait-il ?

J'adorerais rechercher par sujet, dates, couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/5OmsuEIWT39ZWi5--jCprileKve8zNJVOhIV)
_Recherches_

Afin de recréer notre expérience — ou simplement de voir les sujets généraux de nos intérêts — il serait utile de fournir aux utilisateurs une liste des recherches passées. Une fois que vous avez cliqué sur un résultat de recherche particulier, il s'étendrait avec les liens visités basés sur cette requête précise, et vous redirigerait vers la carte avec le chemin mis en évidence.

![Image](https://cdn-media-1.freecodecamp.org/images/S45tdCAfOZ-mSsN46vsBrym8SiHHCxuCQNER)
_Analytique_

Actuellement, je manque vraiment de l'écran d'analytique. Il est crucial de pouvoir comprendre son propre comportement, surtout qu'il n'y a plus de distinction entre hors ligne et en ligne. La [**Bulle de Filtrage**](https://en.wikipedia.org/wiki/Filter_bubble) montre que les informations que nous voyons sont sélectives.

Nous devenons séparés des informations qui ne sont pas d'accord avec notre point de vue. En conséquence, nous sommes de plus en plus confortables dans notre propre domaine. Nous avons arrêté de nous poser des questions.

Je veux voir combien de temps je passe à naviguer sur Internet, comment je collecte les informations, et comment je forme mes opinions.

Nous vivons à une époque où la compréhension de vos comportements de navigateur et de vos schémas de recherche devient cruciale dans le processus cognitiviste.

[_Je suppose qu'il est tentant, si le seul outil que vous avez est un marteau, de traiter tout comme si c'était un clou._](https://en.wikipedia.org/wiki/Law_of_the_instrument)

_Bibliographie et inspiration :_

[1](http://theory.isthereason.com/?p=1790) [2](https://developer.chrome.com/extensions/history) [3](https://www-s.acm.illinois.edu/macwarriors/projects/trailblazer/)

_Si vous souhaitez collaborer, n'hésitez pas à [écrire](mailto:patryk.adas@gmail.com)._