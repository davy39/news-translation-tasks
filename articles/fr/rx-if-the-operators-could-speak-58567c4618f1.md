---
title: Rx — Si les opérateurs pouvaient parler !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-13T20:51:00.000Z'
originalURL: https://freecodecamp.org/news/rx-if-the-operators-could-speak-58567c4618f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U9DEpj0xpch6t3VdCxAZVA.png
tags:
- name: Java
  slug: java
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: rx
  slug: rx
seo_title: Rx — Si les opérateurs pouvaient parler !
seo_desc: 'By Ahmed Rizwan

  If the operators could talk, how exactly would they tell us what they do?

  In order to take full advantage of Rx, you need a clear understanding of what Rx
  Operators are and what they do.

  This is what the Operators would be telling the...'
---

Par Ahmed Rizwan

Si les opérateurs pouvaient parler, comment nous diraient-ils exactement ce qu'ils font ?

Pour tirer pleinement parti de Rx, vous devez avoir une compréhension claire de ce que sont les opérateurs Rx et de ce qu'ils font.

Voici ce que les opérateurs diraient aux observables s'ils pouvaient parler lorsque nous les utilisons.

Pour cet article, je supposerai que vous savez déjà ce qu'est Rx. Sinon, allez [lire ceci](https://medium.com/@ahmedrizwan/rxandroid-and-kotlin-part-1-f0382dc26ed8#.vundiz1fq). Ou faites simplement une recherche Google sur Rx et vous trouverez une tonne d'articles, de tutoriels et de vidéos utiles.

### **Opérateurs de création**

#### [Create](http://reactivex.io/documentation/operators/create.html)

> Je vous dis quoi émettre, quand terminer, et quelle erreur lancer. Parce que je suis le patron.

#### [Defer](http://reactivex.io/documentation/operators/defer.html)

> Vous ne pouvez vous "créer" que lorsque quelqu'un s'abonne à vous. Et ce sera une toute nouvelle version de vous-même à chaque fois.

#### [Empty](http://reactivex.io/documentation/operators/empty-never-throw.html)

> Hmm. N'émettez rien. Et puis mourrez, s'il vous plaît.

#### [Never](http://reactivex.io/documentation/operators/empty-never-throw.html)

> N'émettez rien. Et ne... jamais... terminez.

#### [Throw](http://reactivex.io/documentation/operators/empty-never-throw.html)

> N'émettez rien, et puis lancez une erreur, d'accord ?

#### [From](http://reactivex.io/documentation/operators/from.html)

> Je vous donne quelques objets, puis vous les émettez directement vers moi.

#### [Interval](http://reactivex.io/documentation/operators/interval.html)

> Et si vous émettiez des éléments. Mais pas immédiatement. Envoyez-les un par un, après certains "intervalles".

#### [Just](http://reactivex.io/documentation/operators/just.html)

> J'ai besoin d'une seule chose de vous. Une seule.

#### [Range](http://reactivex.io/documentation/operators/range.html)

> Je vous donne une plage d'entiers, puis vous émettez toutes les valeurs de cette plage.

#### [Repeat](http://reactivex.io/documentation/operators/repeat.html)

> Et si vous émettiez cet objet de manière répétée.

#### [Start](http://reactivex.io/documentation/operators/start.html)

> D'accord. J'ai une fonction. Quand elle retourne, vous commencez à émettre. Mais seulement quand elle retourne. Compris ?

#### [Timer](http://reactivex.io/documentation/operators/timer.html)

> Donc vous avez un élément. Ne l'émettez pas tout de suite. Je vous dirai le moment exact où vous devez l'émettre. Ne vous précipitez pas.

### Opérateurs de transformation

#### [Buffer](http://reactivex.io/documentation/operators/buffer.html)

> D'accord, voici le marché. Peu importe ce que vous émettez normalement, ne l'émettez pas. Au lieu de cela, collectez les éléments en lots au fil du temps. Et envoyez des lots à la place. Parce que je veux des lots !

#### [FlatMap](http://reactivex.io/documentation/operators/flatmap.html)

> Donc, si vous avez des listes d'éléments et qu'il y a un autre observable rempli d'éléments, pouvez-vous vous "aplatir" vous et cet observable pour que vous puissiez simplement envoyer des éléments ?

#### [Map](http://reactivex.io/documentation/operators/map.html)

> Transforme chaque élément en un autre élément.

#### [Scan](http://reactivex.io/documentation/operators/scan.html)

> Transforme chaque élément en un autre élément, comme vous l'avez fait avec map. Mais incluez également l'élément "précédent" lorsque vous effectuez une transformation.

### Opérateurs de filtrage

#### [Debounce](http://reactivex.io/documentation/operators/debounce.html)

> N'émettez que si un certain temps est écoulé.

#### [Distinct](http://reactivex.io/documentation/operators/distinct.html)

> N'émettez que des éléments distincts. D'accord ?

#### [ElementAt](http://reactivex.io/documentation/operators/elementat.html)

> Je vous donne l'index. Vous émettez l'élément à cet index.

#### [Filter](http://reactivex.io/documentation/operators/filter.html)

> Je vous donne un critère. Vous me donnez les éléments qui passent le critère.

#### [First](http://reactivex.io/documentation/operators/first.html)

> Donnez-moi simplement le premier élément.

#### [IgnoreElements](http://reactivex.io/documentation/operators/ignoreelements.html)

> Ne, je répète, n'émettez pas un seul élément. Et puis mourrez.

#### [Last](http://reactivex.io/documentation/operators/last.html)

> Donnez-moi simplement le dernier élément.

#### [Sample](http://reactivex.io/documentation/operators/sample.html)

> Je vous donne un intervalle. Vous me donnez uniquement les éléments les plus récents de cet intervalle.

#### [Skip](http://reactivex.io/documentation/operators/skip.html)

> D'accord, ignorez les premiers n éléments, voulez-vous ?

#### [SkipLast](http://reactivex.io/documentation/operators/skiplast.html)

> Ignorez les derniers n éléments. Oui, ceux-là.

#### [Take](http://reactivex.io/documentation/operators/take.html)

> N'émettez que les premiers n éléments.

#### [TakeLast](http://reactivex.io/documentation/operators/takelast.html)

> N'émettez que les derniers n éléments.

### Opérateurs de combinaison

#### [Merge](http://reactivex.io/documentation/operators/merge.html)

> Voici deux observables. Faisons semblant qu'ils ne sont qu'un seul observable.

#### [StartWith](http://reactivex.io/documentation/operators/startwith.html)

> Voici deux observables. Mais c'est moi qui vous dis avec lequel commencer.

#### [CombineLatest](http://reactivex.io/documentation/operators/combinelatest.html)

> Voici deux observables. Entre les deux, faites des paires des derniers éléments.

#### [Zip](http://reactivex.io/documentation/operators/zip.html)

> Voici deux observables. Mais je vous dis comment combiner leurs éléments (via une fonction, bien sûr).

### Gestion des erreurs

#### [Catch](http://reactivex.io/documentation/operators/catch.html)

> Après qu'une erreur est lancée, continuez avec les émissions.

#### [Retry](http://reactivex.io/documentation/operators/retry.html)

> Après qu'une erreur est lancée, redémarrez depuis le tout début.

### Utilitaires

#### [Delay](http://reactivex.io/documentation/operators/delay.html)

> Ajoutez simplement un délai avant de commencer à émettre, d'accord ?

#### [ObserveOn](http://reactivex.io/documentation/operators/observeon.html)

> Le code "d'observation" doit s'exécuter sur ce thread particulier.

#### [SubscribeOn](http://reactivex.io/documentation/operators/subscribeon.html)

> Le code "d'abonnement" doit s'exécuter sur ce thread particulier.

#### [Subscribe](http://reactivex.io/documentation/operators/subscribe.html)

> Vous pouvez commencer à émettre maintenant. *la musique s'intensifie*

#### [TimeInterval](http://reactivex.io/documentation/operators/timeinterval.html)

> D'accord, donc les observables envoient des éléments, n'est-ce pas ? Au lieu de cela, je veux que vous envoyiez les intervalles de temps. Comme les différences de temps entre chaque émission.

#### [TimeOut](http://reactivex.io/documentation/operators/timeout.html)

> Définissez un TimeOut sur chaque émission. Et si un élément n'est pas émis dans ce délai, lancez simplement une erreur _?_

### Conditionnels et booléens

#### [All](http://reactivex.io/documentation/operators/all.html)

> Si tous les éléments remplissent un certain critère, retournez vrai.

#### [Amb](http://reactivex.io/documentation/operators/amb.html)

> Voici au moins deux observables. Donnez-moi celui qui commence à émettre en premier.

#### [Contains](http://reactivex.io/documentation/operators/contains.html)

> Si je demande un élément, pouvez-vous me dire si vous l'avez déjà ?

#### [DefaultIfEmpty](http://reactivex.io/documentation/operators/defaultorempty.html)

> Lorsque vous n'avez rien à émettre, voici une valeur par défaut que vous pouvez renvoyer.

#### [SequenceEqual](http://reactivex.io/documentation/operators/sequenceequal.html)

> Voici deux observables. Retournez vrai si leurs éléments (et leur séquence) sont les mêmes.

#### [SkipUntil](http://reactivex.io/documentation/operators/skipuntil.html)

> Voici deux observables. Ignorez les éléments du premier jusqu'à ce que le second commence à émettre.

#### [SkipWhile](http://reactivex.io/documentation/operators/skipwhile.html)

> Je vous donne une condition. Vous émettez des éléments jusqu'à ce que cette condition devienne fausse.

#### [TakeUntil](http://reactivex.io/documentation/operators/takeuntil.html)

> Voici deux observables. Ne me donnez que les éléments du premier jusqu'à ce que le second commence à émettre.

### Opérateurs mathématiques

#### [Average](http://reactivex.io/documentation/operators/average.html)

> Donnez-moi une moyenne de vos éléments entiers.

#### [Count](http://reactivex.io/documentation/operators/count.html)

> Donnez-moi un compte de vos éléments.

#### [Max](http://reactivex.io/documentation/operators/max.html)

> N'émettez que l'élément de valeur maximale.

#### [Min](http://reactivex.io/documentation/operators/min.html)

> N'émettez que l'élément de valeur minimale.

#### [Reduce](http://reactivex.io/documentation/operators/reduce.html)

> Faites un scan, mais n'émettez que la valeur finale.

#### [Sum](http://reactivex.io/documentation/operators/sum.html)

> Retournez la somme de tous vos éléments.

### Opérateurs de conversion

#### [To](http://reactivex.io/documentation/operators/to.html)

> Convertissez un observable en une Liste, une Map ou un Tableau, ou ce que je vous dis de faire.

C'est tout pour l'instant. Il y a d'autres opérateurs également, que vous pouvez trouver [ici](http://reactivex.io/documentation/operators.html). Vous pouvez également consulter [RxMarbles](http://rxmarbles.com), qui propose des diagrammes sympas pour démontrer chaque opérateur.

En tout cas, merci d'avoir lu. J'espère que l'article vous a aidé à mieux comprendre ce que font chacune de ces commandes de manière amusante.

Bon codage !