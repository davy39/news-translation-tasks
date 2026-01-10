---
title: Comment j'ai doublé l'autonomie de la batterie de mon Mac en fermant littéralement
  un seul onglet dans un navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-17T09:40:58.000Z'
originalURL: https://freecodecamp.org/news/how-i-doubled-the-battery-life-on-my-mac-by-literally-closing-one-tab-in-a-browser-d96f2c5374db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dZXvMSeVmswJhC6n41sywg.jpeg
tags:
- name: Apple
  slug: apple
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: Comment j'ai doublé l'autonomie de la batterie de mon Mac en fermant littéralement
  un seul onglet dans un navigateur
seo_desc: 'By Primož Cigler

  Today I want to share a quick and easy hack that doubled the time-on-battery on
  my laptop.

  It is so easy to do once you know where to look.

  I spend most of the time on my laptop in the browser. This is mostly because I read
  stuff, st...'
---

Par Primož Cigler

Aujourd'hui, je veux partager un truc rapide et facile qui a **doublé** l'autonomie de la batterie de mon ordinateur portable.

C'est si facile à faire une fois que vous savez où regarder.

Je passe la plupart de mon temps sur mon ordinateur portable dans le navigateur. C'est surtout parce que je lis des choses, je reste sur les réseaux sociaux ou je développe des sites web. J'utilise Chrome pour cela, je n'ouvre rarement un autre navigateur — la plupart du temps pour des tests seulement.

Chrome est généralement connu pour ne pas être une application économe en énergie, donc c'est un compromis, mais je le trouve beaucoup mieux (surtout pour le développement) que tout autre chose.

Depuis un certain temps, j'ai commencé à remarquer que la batterie ne durait pas aussi longtemps qu'auparavant lorsque j'ai acheté cet ordinateur portable il y a un an et demi. Il est normal qu'elle perde de sa puissance avec le temps. Mais un jour, il y a environ 2 semaines, alors que j'étais alité malade, j'ai décidé de vérifier ce qui drainait ma batterie si rapidement et si je pouvais le réparer.

Heureusement, OS X est livré avec le Moniteur d'activité, qui vous donne également un aperçu des applications qui ont le plus d'impact sur l'autonomie de votre batterie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jyqZUpAeyky4R__u17In5g.png)
_Moniteur d'activité_

Si vous triez la liste par la colonne _Impact énergétique moyen_, vous trouverez les applications les plus problématiques. Dans mon cas, Google Chrome. Vous pouvez résoudre le problème facilement en quittant l'application, mais comme je l'ai mentionné, ce n'était pas viable dans mon cas, car je veux utiliser Chrome.

La capture d'écran ci-dessus a été prise au moment où j'écris ceci et elle montre Chrome "réparé". **Au moment où je suis allé l'analyser pour la première fois, la valeur _Impact énergétique moyen_ pour Chrome était bien supérieure à 100, autour de 140**.

#### Alors, comment ai-je réussi à la réduire à environ un tiers ?

C'était assez simple. J'ai littéralement dû **fermer un seul onglet** dans Chrome, qui utilisait beaucoup de CPU.

Ma barre d'outils dans Chrome ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gSEMiCKnrfv0GqE6ZqfXmg.png)

J'ai quelques onglets épinglés que je veux toujours ouverts et puis viennent les onglets qui "viennent et partent".

Il y a un outil peu connu dans Chrome, qui vous permet d'analyser combien de ressources les **onglets individuels consomment**. Il s'appelle **Gestionnaire des tâches** et vous pouvez le trouver dans **Menu > Plus d'outils > Gestionnaire des tâches**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TZVAsQTukJ-e8fKjSfJrdQ.png)
_Où trouver le Gestionnaire des tâches dans Chrome_

Une fois ouvert, il révèlera des détails plus fins sur le CPU et la RAM utilisés dans Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S-clN-DWtvEWEoaJ7utjGA.png)
_Gestionnaire des tâches de Chrome_

Ce qui vous intéresse, c'est le CPU — c'est ce qui draine votre batterie.

> Trouvez les onglets qui sont constamment gourmands en CPU et tuez-les sans pitié !

Dans mon cas, j'avais les taux de change (USD vers EUR) ouverts tout le temps. C'était [cette page](http://www.xe.com/currencycharts/?from=EUR&to=USD&view=1M). Et regardez cela, lorsque j'ai cette page ouverte et épinglée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fy5van6rRHkJBPKTEAh46g.png)
_L'onglet XE.com est tellement gourmand en CPU (l'onglet était inactif lorsque j'ai créé la capture d'écran)_

C'était un choix évident. Je peux vivre sans onglet épinglé sur les taux de change, si cela fait durer mon ordinateur portable deux fois plus longtemps.

Si vous avez l'impression que la batterie de votre ordinateur portable a du mal à cause de Chrome, consultez le Gestionnaire des tâches de Chrome. Tuez les sites web les plus gourmands sans pitié et notifiez leurs développeurs. Ils font probablement des choses sales en JavaScript qui drainent votre batterie comme l'enfer.

_Vous pouvez me suivre sur [Twitter](https://twitter.com/primozcigler), mais nous savons tous les deux que Twitter est très bruyant. Alors vous pouvez [me laisser votre email](http://eepurl.com/bLlBLj) et je vous enverrai occasionnellement des choses que je trouve utiles._