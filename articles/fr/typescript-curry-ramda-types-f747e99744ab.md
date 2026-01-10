---
title: Comment maîtriser les motifs avancés de TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T17:35:32.000Z'
originalURL: https://freecodecamp.org/news/typescript-curry-ramda-types-f747e99744ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s8OOdE6Qmx0HhbQwexsR1Q.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Ramda
  slug: ramda
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment maîtriser les motifs avancés de TypeScript
seo_desc: 'By Pierre-Antoine Mills

  Learn how to create types for curry and Ramda


  _Photo by [Unsplash](https://unsplash.com/photos/2jXkA7GAz9M?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">sergio sou...'
---

Par Pierre-Antoine Mills

#### Apprenez à créer des types pour curry et Ramda

![Image](https://cdn-media-1.freecodecamp.org/images/gHHbXSKPmkakVPjav7Z2U9wiAA7Jcdfhde3t)
_Photo par [Unsplash](https://unsplash.com/photos/2jXkA7GAz9M?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">sergio souza</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Malgré la popularité du currying et l'essor de la programmation fonctionnelle (et de TypeScript), il est encore fastidieux aujourd'hui d'utiliser le curry et d'avoir des **vérifications de types appropriées**. Même des bibliothèques célèbres comme Ramda ne fournissent pas de types génériques pour leurs implémentations de curry (mais nous le ferons).

Cependant, vous n'avez pas besoin de connaissances en programmation fonctionnelle pour suivre ce guide. Ce guide traite du currying, mais ce n'est qu'un sujet de mon choix pour vous enseigner des techniques avancées de TypeScript. Vous devez simplement avoir pratiqué un peu avec les types primitifs de TypeScript. Et à la fin de ce guide, vous serez un vrai magicien TS ?.

Si vous êtes un programmeur fonctionnel, vous utilisez probablement déjà le currying pour créer des compositions puissantes et des applications partielles... Et si vous êtes un peu en retard, il est temps de faire le saut dans la programmation fonctionnelle, de commencer à vous éloigner du paradigme impératif et de résoudre les problèmes plus rapidement, avec facilité, et de promouvoir la réutilisabilité dans votre base de code.

À la fin de ce guide, vous saurez comment créer des **types puissants** comme :

![Image](https://cdn-media-1.freecodecamp.org/images/0jtoHxd5Keq7fx457IldtUAfFG4ThZx8YoGq)

En fait, Ramda dispose de certains types médiocres pour curry. Ces types ne sont pas génériques, **codés en dur**, nous limitant à un certain nombre de paramètres. À partir de la version 0.26.x, il ne suit qu'un **maximum de 6 arguments** et ne nous permet pas d'utiliser sa célèbre fonctionnalité de **placeholder** très facilement avec TypeScript. Pourquoi ? C'est difficile, mais nous sommes d'accord pour dire que nous en avons assez et nous allons corriger cela !

![Image](https://cdn-media-1.freecodecamp.org/images/J6jdoXiM9B8ZUX02zbSXyE8-Aw-add4QIJP5)
_Source : [Giphy](https://giphy.com/gifs/glitch-falling-JWXIa2DAQNoQg" rel="noopener" target="_blank" title=")_

#### Qu'est-ce que le currying ?

Mais avant de commencer, assurons-nous que vous avez une compréhension très basique de ce qu'est le currying. Le currying est le processus de transformation d'une fonction qui prend plusieurs arguments en une série de fonctions qui prennent un argument à la fois. Eh bien, c'est la théorie.

Je préfère les exemples plutôt que les mots, alors créons une fonction qui prend deux nombres et qui retourne le résultat de leur addition :

![Image](https://cdn-media-1.freecodecamp.org/images/iMtzZhZle3U2g9OSU2m8KJuYqaKlyJSy9xbm)

La version curry de `simpleAdd` serait :

![Image](https://cdn-media-1.freecodecamp.org/images/XwJ0THXXpg29kt4ji36b7AwRcJPFB48JnYg-)

Dans ce guide, je vais d'abord expliquer comment créer des types TypeScript qui fonctionnent avec une implémentation standard de curry.

Ensuite, nous les ferons évoluer vers des **types plus avancés** qui peuvent permettre aux fonctions curry de prendre 0 ou plusieurs arguments.

Et enfin, nous pourrons utiliser des "écarts" qui abstraient le fait que nous ne sommes pas capables ou disposés à fournir un argument à un certain moment.

**TL;DR** : Nous allons créer des types pour "curry classique" et "curry avancé" (Ramda).

### Types de tuples

Avant de commencer à apprendre les techniques TypeScript les plus avancées, je veux juste m'assurer que vous connaissez les **tuples**. Les types de tuples vous permettent d'exprimer un tableau où le type d'un nombre fixe d'éléments est connu. Voyons un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/QEdtDxuaor9oABVKDXIz91aGwFeT7xyUQx8S)

Ils peuvent être utilisés pour imposer le type de valeurs à l'intérieur d'un tableau de taille fixe :

![Image](https://cdn-media-1.freecodecamp.org/images/k9PLODTdaIIJJjsEhHg5i3S-AYPF8jcrMlXr)

Et peuvent également être utilisés en combinaison avec des paramètres de repos (ou déstructuration) :

![Image](https://cdn-media-1.freecodecamp.org/images/hhoq8DXKwuEGzzFnkUlHnu8Roc3sDHhpszc8)

Mais avant de commencer à construire nos types de curry géniaux, nous allons faire un peu d'échauffement. Nous allons créer les premiers outils dont nous avons besoin pour construire l'un des types de curry les plus basiques. Allons-y.

Peut-être pourriez-vous deviner... Nous allons travailler beaucoup avec les types de tuples. Nous les utiliserons dès que nous aurons extrait les paramètres de la fonction "originale" curry. Alors, à des fins d'exemple, créons une fonction de base :

![Image](https://cdn-media-1.freecodecamp.org/images/J9peTtIATeaP8jp76F1Kj7dwI5uonYaxpBcj)

Nous avons extrait les types de paramètres de `fn00` grâce à la magie de `Parameters`. Mais ce n'est pas si magique lorsque vous le recodez :

![Image](https://cdn-media-1.freecodecamp.org/images/U39IDHFcnsZ-dLyoZv6Fbno1Q0GZxZA7Ky-A)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/r4JRkERGOwT3aAYa96iNWbljXlP3Xr4qAPex)

Bien, cela fonctionne comme `Parameters`. Ne soyez pas effrayé par `infer`, c'est l'un des mots-clés les plus puissants pour construire des types. Je vais l'expliquer plus en détail après que nous aurons pratiqué un peu plus :

#### Head

Plus tôt, nous avons appris qu'une fonction "curry classique" prend un argument à la fois. Et nous avons également vu que nous pouvons extraire les types de paramètres sous la forme d'un type de tuple, très pratique. Donc `Head` prend un type de tuple `T` et retourne le **premier type** qu'il contient. De cette façon, nous pourrons savoir quel type d'argument doit être pris à la fois.

![Image](https://cdn-media-1.freecodecamp.org/images/CHlmvskq9CbDrfVK8qEokxPJWHAoi0VK1OwK)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/3BllaJUgiKEujqHjG--NxRLVwAuLXGx8N1A1)

#### Tail

Une fonction "curry classique" consomme les arguments **un par un**. Cela signifie que lorsque nous avons consommé le `Head<Params<F>>`, nous devons d'une manière ou d'une autre passer au paramètre suivant qui n'a pas encore été consommé. C'est le but de `Tail`, il supprime commodément la première entrée qu'un tuple peut contenir.

À partir de TypeScript 3.4, nous ne pouvons pas simplement supprimer la première entrée d'un tuple. Donc, nous allons contourner ce problème en utilisant un tour très valide :

![Image](https://cdn-media-1.freecodecamp.org/images/LJIrVYehTvk0lnEforfoD-XfLHApWxHytjgu)

En utilisant les **types de fonction**, nous avons pu dire à TypeScript d'inférer le tuple que nous voulions. Si vous ne comprenez pas encore, ce n'est pas un problème, ce n'est qu'un échauffement, vous vous souvenez ?

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/s1M8asD9pTUySKKNzdN8ThS7tI3nccrUYEW0)

#### HasTail

Une fonction curry retournera une fonction jusqu'à ce que tous ses paramètres aient été **consommés**. Cette condition est atteinte lorsque nous avons appelé `Tail` suffisamment de fois pour qu'il ne reste plus de queue, plus rien à consommer :

![Image](https://cdn-media-1.freecodecamp.org/images/aBBaqEP52ccLHllwPYRywYqKm15CkqhWISj1)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/MSslnHhpafGiSGZIDIVtPskqgoP2ufaE4jEU)

### Mots-clés importants

Vous avez rencontré trois mots-clés importants : `**type**`, `**extends**` et `**infer**`. Ils peuvent être assez déroutants pour les débutants, alors voici les idées qu'ils véhiculent :

* `**extends**` :
Pour simplifier, vous pouvez penser à lui comme s'il s'agissait de notre cher vieux `**===**` de JavaScript. Lorsque vous le faites, vous pouvez voir une instruction `extends` comme un **ternaire simple**, et cela devient beaucoup plus simple à comprendre. Dans ce cas, `extends` est appelé un **type conditionnel**.
* `**type**` :
J'aime penser à un type comme s'il s'agissait d'une **fonction**, mais pour les types. Il a une entrée, qui sont des types (appelés **génériques**) et une sortie. La sortie dépend de la "logique" d'un type, et `extends` est ce bloc de logique, similaire à une clause `if` (ou ternaire).
* `**infer**` :
C'est la loupe de TypeScript, un bel outil d'inspection qui peut **extraire des types** qui sont piégés à l'intérieur de différentes sortes de structures !

Je pense que vous comprenez bien `extends` et `type`, c'est pourquoi nous allons pratiquer un peu plus avec `infer`. Nous allons extraire des types qui sont contenus à l'intérieur de différents types génériques. Voici comment faire :

#### Extraire le type d'une propriété d'un objet

![Image](https://cdn-media-1.freecodecamp.org/images/e7TW4m93Q3H1MNUwVGDTM0Ref93NWtRGYfyC)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/CWPhfFjc1-XnMUOy8RzZZ6q6iHwVR1WtZpzh)

**Extraire les types internes des types de fonction**

![Image](https://cdn-media-1.freecodecamp.org/images/7Dz648h0mzss0jbsAMu1LxHdZTWYEkTNBMzD)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/iqqzJqqwwFGHGB0lLjU3gpMamLtR3lmAT5j-)

**Extraire les types génériques d'une classe ou d'une interface**

![Image](https://cdn-media-1.freecodecamp.org/images/AaiIqlv-8HPqcnnItAEOCDwuiTlnIGVk38xq)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/7SwlN4zLQb-GkVU0z53bg5G0nZrWrTFhf8ek)

**Extraire les types d'un tableau**

![Image](https://cdn-media-1.freecodecamp.org/images/8qYXZ0XBi6NkAeQkOJAhTcN98KxyX1bHfgF0)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/3WNFqxUGSvt-TJpJ6MoJc6EqyvraHbyLN6pN)

**Extraire les types d'un tuple**

![Image](https://cdn-media-1.freecodecamp.org/images/Pb-j222BGW7K46xR9rgakjVeOwdFa2iG9k6N)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/jngjN2i1yCScQMVS6aHjYfPXAH1MZ5Y3ugYI)

Nous avons essayé d'inférer le type du **reste du tuple** dans un type `B`, mais cela n'a pas fonctionné comme prévu. C'est parce que TypeScript **manque** d'une fonctionnalité qui nous permettrait de **déconstruire** un tuple en un autre. Il y a une proposition active qui aborde ces problèmes et vous pouvez vous attendre à une manipulation améliorée pour les tuples dans le futur. C'est pourquoi `Tail` est construit de cette manière.

`infer` est très puissant et ce sera votre **principal outil** pour la manipulation de types.

![Image](https://cdn-media-1.freecodecamp.org/images/1A2co54z4low60cVicsPW57m979hefFOjD7i)
_Source : [Giphy](https://giphy.com/gifs/cheezburger-see-5K3Vw3jUqwV56" rel="noopener" target="_blank" title=")_

### Curry V0

L'échauffement ? est terminé, et vous avez les connaissances pour construire un "curry classique". Mais avant de commencer, résumons (encore) ce qu'il doit être capable de faire :

![Image](https://cdn-media-1.freecodecamp.org/images/VE5KCCPIbmYfSrGgTsB2UCa2HBLkzD59uq7D)

Notre premier type de curry doit prendre un tuple de **paramètres** `P` et un type de **retour** `R`. C'est une fonction **récursive** dont le type **varie** avec la **longueur** de `P` :

![Image](https://cdn-media-1.freecodecamp.org/images/CgIczre6OeRg6wAd2vGYnPYZoAUj4K6Id7Vn)

Si `HasTail` rapporte `false`, cela signifie que **tous** les paramètres ont été **consommés** et qu'il est temps de **retourner** le type de retour `R` de la fonction originale. Sinon, il reste des paramètres **à consommer**, et nous **récursons** dans notre type. Récurser ? Oui, `CurryV0` décrit une fonction qui a un type de retour de `CurryV0` tant qu'il y a une `Tail` (`HasTail<P> extends true`).

C'est aussi simple que cela. Voici la preuve, sans aucune implémentation :

![Image](https://cdn-media-1.freecodecamp.org/images/6psb7bd4KeXlfysR-QlqZuua7cJXrRdiz4PN)

![Image](https://cdn-media-1.freecodecamp.org/images/7T9oP6a4U46tlbK3a6OMnM7AHuikSwMglTOs)

Mais visualisons plutôt la récursion qui s'est produite ci-dessus, étape par étape :

![Image](https://cdn-media-1.freecodecamp.org/images/Keu0siYpxvmqzzNuh1iUsLaDI8hZwLm7JioR)

Et bien sûr, les indices de type fonctionnent pour un **nombre illimité** de paramètres ?:

![Image](https://cdn-media-1.freecodecamp.org/images/hbX-Y5WQPVnVVCPL02Gk7GI-VWCSjsPPnVf8)

### Curry V1

Bien, mais nous avons oublié de gérer le scénario où nous passons un **paramètre de repos** :

![Image](https://cdn-media-1.freecodecamp.org/images/5s8kSoNvfuZ9MOZiXd7QPH1N0sAXJQZbAkal)

Nous avons essayé d'utiliser un paramètre de repos, mais cela ne fonctionnera pas parce que nous attendions en fait un **seul** paramètre/argument que nous avons appelé plus tôt `**arg0**`. Donc nous voulons prendre au moins un argument `arg0` et nous voulons recevoir des arguments supplémentaires (optionnels) dans un paramètre de repos appelé `rest`. Permettons de prendre des paramètres de repos en l'améliorant avec `Tail` et `Partial` :

![Image](https://cdn-media-1.freecodecamp.org/images/sqex95FBdDbnidAj6eq2Q2HZYCDbTqGV4kPk)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/AeHZhJ110EifXklHor2T4OULadbnwBxIHYwT)

![Image](https://cdn-media-1.freecodecamp.org/images/5zjjyKorZYH5Ku93nwOiBFLUiLSySjtqjPCa)

Mais nous avons fait une horrible erreur : les arguments sont consommés très mal. Selon ce que nous avons écrit, cela ne produira pas une seule erreur TS :

![Image](https://cdn-media-1.freecodecamp.org/images/Bob3CnZ0vCZqpmvqNpCsU55y8enzw17npqri)

En fait, il y a un gros **problème de conception** parce que nous avons dit que nous forcerions la prise d'un seul `arg0`. D'une manière ou d'une autre, nous allons devoir **garder une trace** des arguments qui sont **consommés** à un moment donné. Donc, nous allons d'abord nous débarrasser de `arg0` et commencer à suivre les paramètres consommés :

![Image](https://cdn-media-1.freecodecamp.org/images/0uydMEZMPLc6-mr5YSZvzvEhCigKphy7bSTi)

Là, nous avons utilisé un **générique contraint** appelé `**T**` qui va **suivre** les arguments pris. Mais maintenant, c'est complètement cassé, il n'y a plus de vérifications de type parce que nous avons dit que nous voulions suivre des paramètres de type `**any[]**` (la contrainte). Mais pas seulement cela, `Tail` est complètement inutile parce qu'il ne fonctionnait bien que lorsque nous prenions un argument à la fois.

Il n'y a qu'une seule solution : **quelques outils supplémentaires** ?.

### Types récursifs

Les outils suivants vont être utilisés pour déterminer les prochains paramètres à consommer. Comment ? En suivant les paramètres consommés avec `T`, nous devrions être capables de **deviner ce qu'il reste**.

Attachez votre ceinture ! Vous allez apprendre une autre technique puissante ?:

#### Last

Prenez votre temps pour essayer de comprendre ce type complexe mais très court. Cet exemple prend un tuple comme paramètre et extrait sa dernière entrée :

![Image](https://cdn-media-1.freecodecamp.org/images/-Lz8QpB1iizm5Ht5AQXVopGg7spFsvcs3tTi)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/sB6a0YyguI4OIakTZKFLpn4UMN-4azlSCaQp)

Cet exemple démontre la puissance des types conditionnels lorsqu'ils sont utilisés comme **accès** à un type indexé. Un quoi ? Un type conditionnel qui accède aux types internes d'un type de manière commande. Pour une explication plus visuelle :

![Image](https://cdn-media-1.freecodecamp.org/images/xgzVrAX64CLiquY0yLF0qthPMfF21skZpnRo)

Cette technique est une approche **idéale** et un moyen sûr de faire de la **récursion** comme nous venons de le faire. Mais elle n'est pas seulement limitée à la récursion, c'est une manière agréable et visuelle d'**organiser** des **types conditionnels** complexes.

### Outils de base #1

Où en étions-nous ? Nous avons dit que nous avions besoin d'outils pour **suivre les arguments**. Cela signifie que nous devons savoir quels types de paramètres nous pouvons prendre, lesquels ont été consommés et lesquels sont les prochains à venir. Commençons :

#### Length

Pour faire l'analyse mentionnée ci-dessus, nous aurons besoin d'**itérer** sur les tuples. À partir de TypeScript 3.4.x, il n'existe pas de protocole d'itération qui pourrait nous permettre d'itérer librement (comme un `for`). Les types mappés peuvent mapper d'un type à un autre, mais ils sont trop limitants pour ce que nous voulons faire. Donc, idéalement, nous aimerions pouvoir manipuler une sorte de **compteur** :

![Image](https://cdn-media-1.freecodecamp.org/images/wYeuZrAjfFdM6B9NXAUv3rCt0Cc8cIHXP23E)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/2oF0r2YpVc-ukCwlfdbrXVCb-4upiPPMkXdC)

En **ajoutant** un tuple avec `any`, nous avons créé quelque chose qui pourrait être similaire à une variable qui peut être **incrémentée**. Cependant, `Length` ne concerne que la taille d'un tuple, donc il fonctionne également avec tout autre type de tuple :

![Image](https://cdn-media-1.freecodecamp.org/images/8zKoWai2QpSrTYWPq6DXtRR6eiwsgqT3AlCf)

#### Prepend

Il ajoute un type `E` au **début** d'un tuple `T` en utilisant notre premier tour TS :

![Image](https://cdn-media-1.freecodecamp.org/images/xh7GuVMyKVoNGQc43TrYy-ZTvMrJNYNj7ZJB)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/Z9ElT2pecidPyZKluv0V4pkzXDOljBqdRtAa)

Dans les exemples de `Length`, nous avons augmenté manuellement un compteur. Donc `Prepend` est le candidat idéal pour être la base d'un **compteur**. Voyons comment cela fonctionnerait :

![Image](https://cdn-media-1.freecodecamp.org/images/PpHPCHNCKbXVADtErbDfAMCY4HZq5YSstTEK)

#### Drop

Il prend un tuple `T` et supprime les premières entrées `N`. Pour ce faire, nous allons utiliser les mêmes techniques que nous avons utilisées dans `Last` et notre nouveau type de compteur :

![Image](https://cdn-media-1.freecodecamp.org/images/3iXvCx2E5qJAQ3INjsoT-8DwmBqjbLPZaQ0k)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/1TupbmvJtwskYCMImwUlAaMAei8DENnfL2t0)

Qu'est-il arrivé ?

Le type `Drop` va récurser jusqu'à ce que `Length<`;**I> m**atches la val`u`e de N que nous avons passée. En d'autres termes, le type de `i`ndex 0 est choisi par l'accès conditionnel jusqu'à ce que cette condition soit remplie. Et nous `used Prepend&l`t;any, I> so **that we** can increase a counter like we would do in a `loop. Thu`s, Length<I> is us**ed as a** recursion counter, and it is a way to freely iterate with TS.

### Curry V3

Cela a été un long et difficile chemin pour arriver ici, bien joué ! Il y a une récompense pour vous ?.

Maintenant, disons que nous avons suivi que 2 paramètres ont été consommés par notre curry :

![Image](https://cdn-media-1.freecodecamp.org/images/F2IJOT9pYiP-yYyC5c-qXEkbUUZfHg3XXkiA)

Parce que nous connaissons la quantité de paramètres consommés, nous pouvons deviner ceux qui restent encore à être consommés. Grâce à l'aide de `Drop`, nous pouvons faire cela :

![Image](https://cdn-media-1.freecodecamp.org/images/BOHkaHyXDA91p4oDFZw1bQuJUFNZa8EjhgJ3)

Il semble que `Length` et `Drop` soient des outils précieux. Alors, révisons notre version précédente de curry, celle qui avait un `Tail` cassé :

![Image](https://cdn-media-1.freecodecamp.org/images/uXP4yGlh8Eioxhzko8m9CMafcHHuNUfdUSvX)

Qu'avons-nous fait ici ?

D'abord, `Drop<Length<`T>, P> signifie que nous supprimons les paramètres consommés. Ensuite, si la longueur de `Drop<Length<T>, P>` n'est pas égale à 0, notre type de curry doit continuer à récurser avec les paramètres supprimés jusqu'à... Enfin, lorsque tous les paramètres ont été consommés, la longueur des paramètres supprimés est égale à 0, et le type de retour est R.

![Image](https://cdn-media-1.freecodecamp.org/images/t4FRePSoaR2dAZ4IC0GJkUxvm0S3bJdfUosX)
_Source : [Giphy](https://giphy.com/gifs/ice-goat-LumJYWwnr6fSg" rel="noopener" target="_blank" title=")_

### Curry V4

Mais nous avons une autre erreur ci-dessus : TS se plaint que notre `Drop` n'est pas de type `any[]`. Parfois, TS va **se plaindre** qu'un type n'est pas celui que vous attendiez, mais vous savez qu'il l'est ! Alors, ajoutons un autre outil à la collection :

#### Cast

Il demande à TS de **révérifier** un type `X` par rapport à un type `Y`, et le type `Y` ne sera appliqué que s'il échoue. De cette façon, nous sommes capables d'arrêter les plaintes de TS :

![Image](https://cdn-media-1.freecodecamp.org/images/0tjYGqAsnLhkMuRvnZJO0Vc450zaY3CGSafN)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/PNWd5VOWmkDXtc3GhpQiKDCl7yHi38W4C2NT)

Et voici notre curry précédent, mais sans aucune plainte cette fois :

![Image](https://cdn-media-1.freecodecamp.org/images/PUf9EeCVGQni5QaKgjsD694AvetAXOirWY2p)

Vous souvenez-vous plus tôt, lorsque nous avons perdu les vérifications de type parce que nous avons commencé à suivre les paramètres consommés avec `T extends any[]` ? Eh bien, cela a été corrigé en castant `T` en `Partial<`;P>. Nous avons ajouté une contrainte avec `Cast<T, Partial<P>>` !

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/TtZf06ws-uNqgtzb7R18yyTf4VpC08LbGVwa)

![Image](https://cdn-media-1.freecodecamp.org/images/RtUUGbB03dr9ZqLnQ5c6dNo7-9bMunXnfHHr)

![Image](https://cdn-media-1.freecodecamp.org/images/VwhBIFhYeITpAOfCeY2hqOazp0wedjPzEgQr)

### Curry V5

Peut-être pensiez-vous que nous étions capables de prendre des paramètres de repos. Eh bien, je suis très désolé de vous informer que nous n'en sommes pas encore là. Voici pourquoi :

![Image](https://cdn-media-1.freecodecamp.org/images/qJUVcf7HJye7spkqBobl9Nlg6afIsspcYhfM)

Parce que les paramètres de repos peuvent être **illimités**, la meilleure supposition de TS est que la longueur de notre tuple est un `number`, c'est plutôt intelligent ! Donc, nous **ne pouvons pas** utiliser `Length` tout en traitant avec des paramètres de repos. Ne soyez pas triste, ce n'est pas si grave :

![Image](https://cdn-media-1.freecodecamp.org/images/c-770wkJstOyLT4lV0DnwdM0LJqhDKY8zAO4)

Lorsque tous les paramètres non-repos sont consommés, `Drop<Length<`;T>,P> peut `seulement correspondre à [any[]]. Grâce à cela, nous avons utilisé` [any,any[] comme condition pour terminer la récursion.

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/QKEwC3TzYAW6nm8jHvtg9nWtWQbOBogY0bLW)

![Image](https://cdn-media-1.freecodecamp.org/images/4197K0vwe6DMbxp1QHp0hLGCgbDLv71zDqJp)

![Image](https://cdn-media-1.freecodecamp.org/images/M5msqRMawT7UuEeMQ80U02YrKI6mZxjKTwGp)

Tout fonctionne à merveille ?. Vous venez de vous procurer un type de curry intelligent, **générique**, **variadique**. Vous pourrez jouer avec très bientôt... Mais avant de le faire, que diriez-vous si je vous disais que notre type peut devenir encore plus génial ?

### Placeholders

À quel point génial ? Nous allons donner à notre type la capacité de **comprendre** l'application partielle de **n'importe quelle combinaison d'arguments**, à n'importe quelle position. Selon la documentation de Ramda, nous pouvons le faire en utilisant un **placeholder** appelé `_`. Il indique que pour toute fonction curry `f`, ces appels sont équivalents :

![Image](https://cdn-media-1.freecodecamp.org/images/8hxR2PKAItfGpkkI451SiG84L3o8JsQFvvnW)

Un placeholder ou "écart" est un objet qui abstrait le fait que nous ne sommes pas capables ou disposés à fournir un argument à un certain moment. Commençons par définir ce qu'est un placeholder. Nous pouvons directement prendre celui de Ramda :

![Image](https://cdn-media-1.freecodecamp.org/images/5qEGVxAeMGTSN77Itw2H9qFCQYqIZgKTgU72)

Plus tôt, nous avons appris à faire nos premières itérations de type en augmentant la longueur d'un tuple. En fait, c'est un peu déroutant d'utiliser `Length` et `Prepend` sur notre type de compteur. Et pour le rendre **plus clair**, nous allons nous référer à ce compteur comme un **itérateur** à partir de maintenant. Voici quelques nouveaux alias juste à cette fin :

#### Pos (Position)

Utilisez-le pour interroger la position d'un itérateur :

![Image](https://cdn-media-1.freecodecamp.org/images/2XiBFO4R97iAoam8JVXck1SIvt-yNFLojq0A)

#### Next (+1)

Il augmente la position d'un itérateur :

![Image](https://cdn-media-1.freecodecamp.org/images/hI4x2iy4H1smshUSP9KICQ6Lk9a-IYYXBS7m)

#### Prev (-1)

Il diminue la position d'un itérateur :

![Image](https://cdn-media-1.freecodecamp.org/images/OmpB2K2jHbNkx1Ms-W4YCSK0DkuKjf6dXEPl)

Testons-les :

![Image](https://cdn-media-1.freecodecamp.org/images/Lkedx1ruYGBRIwrO-S9HcdYSaWrYuDXOYjBG)

#### Iterator

Il crée un itérateur (notre type de compteur) à une position définie par `Index` et est capable de démarrer à partir de la position d'un autre itérateur en utilisant `From` :

![Image](https://cdn-media-1.freecodecamp.org/images/AJsinWfsGJmL6cV1-wGQXv137cng1eGL1mbE)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/kJbgjeGI0MHUhp6WtpVXhCG83m3FleLPFgOo)

### Outils de base #2

Bien, alors que faisons-nous ensuite ? Nous devons **analyser** chaque fois qu'un placeholder est passé comme argument. À partir de là, nous pourrons dire si un paramètre a été "sauté" ou "reporté". Voici quelques outils supplémentaires à cette fin :

#### Reverse

Croyez-le ou non, nous manquons encore de quelques outils de base. `Reverse` va nous donner la liberté dont nous avons besoin. Il prend un tuple `T` et le retourne dans l'autre sens dans un tuple `R`, grâce à nos tout nouveaux types d'itération :

![Image](https://cdn-media-1.freecodecamp.org/images/mV237zmN8G6M5OGxtkvsQLKCS5UIbtQCj4ff)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/16lb4ggNoGBQ328a-FaQUnBNlVYB0jFP4uqt)

#### Concat

Et de `Reverse`, `Concat` est né. Il prend simplement un tuple `T1` et le fusionne avec un autre tuple `T2`. C'est un peu ce que nous avons fait dans `test59` :

![Image](https://cdn-media-1.freecodecamp.org/images/eKKnFeG25Qso0D1O2Zqc4BGnZrRc7JOo683l)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/KTTlVtOGKv9Sx3phQnlCMcjz5WUI3nOQzSUZ)

#### Append

Activé par `Concat`, `Append` peut ajouter un type `E` à la fin d'un tuple `T` :

![Image](https://cdn-media-1.freecodecamp.org/images/Wl-T8NRPiEAwLXmZGCjaNLNAZltxNCIgl9w8)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/UMvrhshMeARwFndD-CUp0BNPh0Ew08STCXzV)

### Analyse des écarts

Nous avons maintenant assez d'outils pour effectuer des **vérifications de types complexes**. Mais cela fait un moment que nous avons discuté de cette fonctionnalité "écart", comment fonctionne-t-elle à nouveau ? Lorsqu'un écart est spécifié comme argument, son paramètre correspondant est **reporté** à l'étape suivante (à prendre). Alors définissons des types qui comprennent les écarts :

#### GapOf

Il vérifie la présence d'un placeholder dans un tuple `T1` à la position décrite par un itérateur `I`. S'il est trouvé, le type correspondant est **collecté** à la même position dans `T2` et reporté (sauvegardé) pour l'étape suivante via `TN` :

![Image](https://cdn-media-1.freecodecamp.org/images/SuAOfNSC7M1N0EMcE79GcpyON-fQsHvgzm68)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/qiwU1IXQv2b9zRz4VksfFzK9Y9HxfewhUDmy)

#### GapsOf

Ne soyez pas impressionné par celui-ci. Il appelle `Gap` sur `T1` et `T2` et stocke les résultats dans `TN`. Et lorsqu'il a terminé, il concatène les résultats de `TN` aux types de paramètres qui restent à être pris (pour le prochain appel de fonction) :

![Image](https://cdn-media-1.freecodecamp.org/images/Lop0oZKqLXoe7Wv15mXq9kEoEBdalufa-Tpb)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/6i2Xc1q6E6f3y8Agca4uOKkEKK5CbKjt6fDQ)

#### Gaps

Ce dernier morceau du puzzle doit être appliqué aux paramètres suivis `T`. Nous allons utiliser des **types mappés** pour expliquer qu'il est possible de remplacer n'importe quel argument par un **placeholder** :

![Image](https://cdn-media-1.freecodecamp.org/images/Ib8MHDLBtIhnPAoCobC8-G69cTew-umwBGXN)

Un type mappé permet d'itérer et de **modifier les propriétés** d'un autre type. Dans ce cas, nous avons modifié `T` de sorte que chaque entrée peut être du type placeholder. Et grâce à `?`, nous avons expliqué que chaque entrée de `T` est optionnelle. Cela signifie que nous n'avons plus besoin d'utiliser `Partial` sur les paramètres suivis.

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/E3fgCRtmWtHBFBv5vdxT7OdzCaXBkYWt2uoH)

Ugh, nous n'avons jamais dit que nous pouvions prendre `undefined` ! Nous voulions simplement pouvoir omettre une partie de `T`. C'est un **effet secondaire** de l'utilisation de l'opérateur `?`. Mais ce n'est pas si grave, nous pouvons corriger cela en remappant avec `NonNullable` :

![Image](https://cdn-media-1.freecodecamp.org/images/h6zieDXDvoLGLsl8LNP5aLC508Hgou04fw1x)

Alors, mettons les deux ensemble et obtenons ce que nous voulions :

![Image](https://cdn-media-1.freecodecamp.org/images/TlR8l43TjvH1FVVKOqqnob38k2PyMk1QZDDy)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/0wvpT0toDEO1MWpZqJnbiC9nl1QTnOKg8NBS)

### Curry V6

Nous avons construit les derniers outils dont nous aurons jamais besoin pour notre type de curry. Il est maintenant temps de mettre les dernières pièces ensemble. Juste pour vous rappeler, `Gaps` est notre nouveau remplacement pour `Partial`, et `GapsOf` remplacera notre précédent `Drop` :

![Image](https://cdn-media-1.freecodecamp.org/images/RtM7MwxrFcQmlr4oI0ZvOAT7R1Vb2WVz0KZs)

Testons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/tnIPwlUxOi4MFOeGA83BhsMdReeZsesE5YsP)

Afin de m'assurer que tout fonctionne comme prévu, je vais forcer les valeurs qui doivent être prises par la fonction d'exemple curry :

![Image](https://cdn-media-1.freecodecamp.org/images/Y9DQVOnURiopXB7ved6yQwawFzS8zjH-d9oT)

![Image](https://cdn-media-1.freecodecamp.org/images/tkeaGYZtras0kQcUjKSCHt9aqBgeYoZlLv7t)

Il y a juste un petit problème : il semble que nous soyons un peu en avance sur Ramda ! Notre type peut comprendre des utilisations de placeholder très complexes. En d'autres termes, les placeholders de Ramda ne **fonctionnent tout simplement pas** lorsqu'ils sont combinés avec des paramètres de repos ?:

![Image](https://cdn-media-1.freecodecamp.org/images/2IZ4S7mBajskuaaDrTdD2GXUAQEnCiZ1-jCp)

![Image](https://cdn-media-1.freecodecamp.org/images/NsZjbAymZITMsw0wKe0Q32LOspQGCGRJqVv5)

Cependant, même si cela semble parfaitement correct, cela entraînera un crash complet. Cela se produit parce que l'implémentation du curry de Ramda ne gère pas bien les combinaisons de **placeholders et de paramètres de repos**. C'est pourquoi j'ai ouvert un ticket avec Ramda sur Github, dans l'espoir que les types que nous venons de créer pourraient un jour fonctionner en harmonie avec la bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/gfN-AekkhygN4jzQF95nyvODxjc8D-BNUyyf)
_Source : [Giphy](https://giphy.com/gifs/jess-3osxYciDsUpfwZXZV6" rel="noopener" target="_blank" title=")_

### Curry

C'est très mignon, mais nous avons un dernier problème à résoudre : **les indices de paramètres**. Je ne sais pas pour vous, mais j'utilise beaucoup les indices de paramètres. C'est très utile de connaître les noms des paramètres avec lesquels vous travaillez. La version ci-dessus ne permet pas ces types d'indices. Voici la correction :

![Image](https://cdn-media-1.freecodecamp.org/images/j6cwCzOiM5lQBIaH-OKjbAzMa-VZ7quGpG63)

J'admets, c'est complètement affreux ! Cependant, nous avons des indices pour **Visual Studio Code**. Que avons-nous fait ici ? Nous avons simplement remplacé les types de paramètres `P` et `R` qui représentaient respectivement les types de paramètres et le type de retour. Et à la place, nous avons utilisé le **type de fonction** `F` à partir duquel nous avons extrait l'équivalent de `P` avec `Parameters<`;F>`;` et R `avec ReturnType<F>. Ainsi, TypeScript est capable de conserver le nom des paramètres, même après le currying :

![Image](https://cdn-media-1.freecodecamp.org/images/beEnT-ydrNb4m1QxH9HdcWzAym01d9P905lw)

Il y a juste une chose : lorsque nous utilisons des écarts, nous perdrons le nom d'un paramètre.

_Un mot pour les utilisateurs d'IntelliJ uniquement : Vous ne pourrez pas bénéficier d'indices appropriés. Je vous recommande de passer à Visual Studio Code dès que possible. Et il est piloté par la communauté, gratuit, beaucoup (beaucoup) plus rapide, et prend en charge les raccourcis clavier pour les utilisateurs d'IntelliJ. :)_

### DERNIERS MOTS

Enfin, je voudrais vous informer qu'il y a une proposition actuelle pour les [types variadiques](https://github.com/Microsoft/TypeScript/issues/5453). Ce que vous avez appris ici ne deviendra pas obsolète — cette proposition vise à faciliter les manipulations de types de tuples les plus **courantes**, donc c'est une très bonne chose pour nous. Dans un avenir proche, elle permettra des concaténations de tuples plus faciles comme les `Append`, `Concat` et `Prepend` que nous avons construits, ainsi que la déstructuration et une meilleure façon de décrire les paramètres de fonction variables.

C'est tout. Je sais que c'est beaucoup à digérer d'un coup, c'est pourquoi j'ai publié une [version développeur](https://github.com/pirix-gh/medium/blob/master/types-curry-ramda/src/index.ts) de cet article. Vous pouvez la cloner, la tester et la modifier avec TypeScript 3.3.x et versions ultérieures. Gardez-la à portée de main et apprenez-en jusqu'à ce que vous soyez plus à l'aise avec les différentes techniques ?.

**High-five ? si vous avez apprécié ce guide, et restez à l'écoute pour mon prochain article !**

**ÉDIT :** [Il est disponible pour Ramda 0.26.1](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/33628)

**Merci d'avoir lu**. Et si vous avez des questions ou des remarques, vous êtes les bienvenus pour laisser un commentaire.