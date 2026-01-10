---
title: Quelle longueur dois-je donner à ma clé API ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-20T11:04:45.000Z'
originalURL: https://freecodecamp.org/news/how-long-should-i-make-my-api-key-833ebf2dc26f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BbHKX6Db55smgYEUJj-qZg.png
tags:
- name: api
  slug: api
- name: Elixir
  slug: elixir
- name: Erlang
  slug: erlang
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Quelle longueur dois-je donner à ma clé API ?
seo_desc: 'By Sam Corcos

  Calculating collision probabilities of hashed values


  Say you built an API that generates public keys, and these keys all need to be unique
  and hard to guess. The most common way to do this is to use a hash function to generate
  a random...'
---

Par Sam Corcos

#### Calcul des probabilités de collision des valeurs hachées

![Image](https://cdn-media-1.freecodecamp.org/images/1*BbHKX6Db55smgYEUJj-qZg.png)

Disons que vous avez construit une API qui génère des clés publiques, et que ces clés doivent toutes être uniques et difficiles à deviner. La méthode la plus courante pour cela est d'utiliser une fonction de hachage pour générer une série aléatoire de nombres et de lettres. Un hachage typique ressemble à quelque chose comme le texte ci-dessous.

> _AFGG2piXh0ht6dmXUxqv4nA1PU120r0yMAQhuc13i8_

Une question qui revient souvent est : « Quelle doit être la longueur de mon hachage pour garantir l'unicité ? » La plupart des gens pensent que ce calcul est difficile. Ils optent donc pour un nombre très grand, comme un hachage de 50 chiffres. L'équation pour approximer la probabilité de collision est en réalité assez simple.

### Comment calculer ?

Supposons que vous utilisez un bon algorithme cryptographique (c'est-à-dire [pas Math.random de JavaScript](https://medium.com/@betable/tifu-by-using-math-random-f1c308c4fd9d#.1ypwox7l4)). Chaque langage possède un bon package crypto pour générer des hachages aléatoires. Avec Phoenix, vous pouvez utiliser le package Erlang **:crypto**.

Il n'y a que deux informations dont vous avez besoin pour effectuer le calcul :

1. Combien de valeurs de hachage uniques possibles pouvez-vous créer avec les entrées données ? Nous attribuerons cela à la variable _N_.
2. Combien de valeurs pourriez-vous éventuellement devoir générer durant la durée de vie de votre projet ? Nous attribuerons cela à la variable _k_.

Pour calculer la première valeur, additionnez tous les caractères possibles qui peuvent entrer dans votre hachage. Élevez-le à la puissance de la longueur de votre hachage.

Par exemple, si votre valeur de hachage contient des nombres, des lettres minuscules et majuscules, cela fait un total de 62 caractères (10 + 26 + 26) que nous pouvons utiliser. Si nous générons un hachage de seulement 3 caractères de long, alors :

_N_ = 62³ = **238 328** valeurs possibles

Pour calculer la deuxième valeur, vous devez réfléchir à ce que fait votre application et faire quelques hypothèses raisonnables.

Disons que votre application génère un hachage pour attribuer à chacun de vos clients. Supposons également que votre application est très niche. Dans le meilleur des cas, votre application aura 1000 clients au cours de sa durée de vie. Ensuite, pour des raisons de sécurité, nous multiplierons cela par 10. Nous supposons que vous pourriez avoir besoin de générer 10 000 valeurs au cours de la vie de votre application.

_k_ = **10 000** limite supérieure pour les valeurs possibles à créer

Nous devons maintenant calculer. Il existe de nombreux algorithmes que nous pouvons utiliser. Nous utiliserons l'une des [approximations simples](https://fr.wikipedia.org/wiki/Problème_des_anniversaires#Approximations), où _e_ est la constante mathématique (la base du logarithme naturel), et _k_ et _N_ sont les mêmes valeurs que ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jET4z0dP--QnXA3AjpvEKA.png)

L'équation de base nous donne la probabilité que toutes les valeurs soient uniques. Ensuite, nous soustrayons ce résultat de 1 pour obtenir les chances que vous ayez une collision. Si vous n'avez pas envie d'écrire votre propre équation, j'en ai fourni une ci-dessous écrite en JavaScript.

Ainsi, dans l'exemple ci-dessus, **calculate(N, k)** donne une probabilité de **environ 100%** que vous aurez une collision. Donc pour ce cas d'utilisation, vous devriez utiliser un hachage de plus de 3 caractères de long.

Maintenant, si nous prenions cet exemple mais changions la longueur de notre hachage de 3 à 5, nous obtiendrions un _N_ qui est _beaucoup_ plus grand (les exponentielles sont bonnes comme ça).

_N_ = 62⁵ = ~**900 000 000**

En supposant la même valeur _k_, notre nouvelle probabilité de collision est réduite à seulement **5,4 %**. Et si nous passions de 5 caractères à 10 ?

_N_ = 62¹⁰ = **~800 000 000 000 000 000**

Oui, cela fait ~800 billions de hachages uniques. Ce qui réduit vos chances de collision à 0,000000000062 %. Cela représente environ une **chance sur 50 milliards** que vous ayez un conflit. Et cela avec un hachage de 10 chiffres — quelque chose comme : BwQ1W6soXk.

Pour un autre exemple, disons que vous êtes une entreprise de traitement de données qui traite de nombreuses transactions. Supposons que vous traitiez 1 million de processus par seconde et que vous devez générer un hachage pour chacun d'eux. Supposons également que vous pensez que cette entreprise pourrait fonctionner pendant les 100 prochaines années.

_k = ~_3 000 000 000 000 000

Cela représente environ **3 quadrillions** de hachages que vous devez créer et qui doivent tous être uniques. C'est beaucoup de données ! Mais même avec ce nombre extrêmement grand à gérer, vous n'avez besoin que d'un hachage de **21 chiffres** pour garantir une **chance sur 10 millions** de collision sur la durée de vie du projet.

Ainsi, la prochaine fois que vous vous inquiétez de la longueur de votre hachage pour garantir l'unicité, sachez que vous n'avez pas besoin d'un hachage aussi long que vous le pensez. De plus, vous pouvez effectuer le calcul vous-même sans trop d'effort.

_Sam Corcos est le développeur principal et cofondateur de [Sightline Maps](http://sightlinemaps.com), la plateforme la plus intuitive pour l'impression 3D de cartes topographiques, ainsi que de [LearnPhoenix.io](http://learnphoenix.io), un site de tutoriels intermédiaires-avancés pour construire des applications de production scalables avec Phoenix et React._