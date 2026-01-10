---
title: 'Comment comprendre les opérateurs RxJS en mangeant une pizza : zip, forkJoin
  et combineLatest expliqués avec des exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T18:44:45.000Z'
originalURL: https://freecodecamp.org/news/understand-rxjs-operators-by-eating-a-pizza
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/download.jpeg
tags:
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
seo_title: 'Comment comprendre les opérateurs RxJS en mangeant une pizza : zip, forkJoin
  et combineLatest expliqués avec des exemples'
seo_desc: 'By Samuel Teboul

  What is RxJS?


  Reactive programming is an asynchronous programming paradigm concerned with data
  streams and the propagation of change - Wikipedia

  RxJS is a library for reactive programming using observables that makes it easier
  to co...'
---

Par Samuel Teboul

# Qu'est-ce que RxJS ?

> _La programmation réactive est un paradigme de programmation asynchrone concerné par les flux de données et la propagation du changement_ - **Wikipedia**

> RxJS est une bibliothèque pour la programmation réactive utilisant des observables qui facilite la composition de code asynchrone ou basé sur des callbacks - **Documentation RxJS**

Les concepts essentiels dans RxJS sont :

* **Un Observable** est un flux de données
* **Les Observers** peuvent enregistrer jusqu'à 3 callbacks :

1. _next_ est appelé 1:M fois pour pousser de nouvelles valeurs vers l'observer
2. _error_ est appelé au plus 1 fois lorsqu'une erreur se produit
3. _complete_ est appelé au plus 1 fois à la complétion

* **Subscription** "démarre" le flux observable

Sans souscription, le flux ne commencera pas à émettre des valeurs. C'est ce que nous appelons un **observable froid**. 

C'est similaire à s'abonner à un journal ou un magazine... vous ne commencerez pas à les recevoir tant que vous ne vous êtes pas abonné. Ensuite, cela crée une relation 1 à 1 entre le producteur (observable) et le consommateur (observer).

![Image](https://lh3.googleusercontent.com/_ro6f-oBp5o-e98sRUYOhfC6T_j79UOqNyfzLse5MfSs4WItSaYoHHK6TS7MlN1O5pSZsN98hA6af6L0j_MHh5F7bL8_Vm3fiya9Vw3Xwr4E0DI9IijKqN6VivRX__bkw7ze30EnzjY)

# Que sont les opérateurs RxJS ?

Les opérateurs sont des fonctions pures qui permettent un style de programmation fonctionnelle pour traiter les collections avec des opérations. Il existe deux types d'opérateurs :

* Opérateurs de création
* Opérateurs pipeables : transformation, filtrage, limitation de débit, aplatissement

Les Subjects sont un type spécial d'Observable qui permet aux valeurs d'être **multidiffusées** à de nombreux Observers. Alors que les Observables simples sont **unicast** (chaque Observer abonné possède une exécution indépendante de l'Observable), les Subjects sont multidiffusés. C'est ce que nous appelons un **observable chaud**.

Dans cet article, je vais me concentrer sur les opérateurs `zip`, `combineLatest` et `forkJoin`. Ce sont des opérateurs de combinaison RxJS, ce qui signifie qu'ils nous permettent de joindre des informations provenant de plusieurs observables. L'ordre, le temps et la structure des valeurs émises sont les principales différences entre eux.

Examinons chacun d'eux individuellement.

# zip()

* `zip` ne commence pas à émettre tant que chaque observable interne n'a pas émis au moins une valeur
* `zip` émet tant que les valeurs émises peuvent être collectées à partir de tous les observables internes
* `zip` émet les valeurs sous forme de tableau

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_oY4pB5RbNeloyauM1tpWmg.png)

Imaginons que vous êtes avec Mario et Luigi, deux de vos meilleurs amis, dans le meilleur restaurant italien de Rome. Chacun de vous commande une boisson, une pizza et un dessert. Vous spécifiez au serveur de apporter les boissons en premier, puis les pizzas, et enfin les desserts.

Cette situation peut être représentée avec 3 observables différents, représentant les 3 commandes différentes. Dans cette situation spécifique, le serveur peut utiliser l'opérateur `zip` pour apporter (émettre) les différents éléments de commande par catégorie.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_ve5RtSu2eH7b3pe8lJQ9rg.png)

**⚠️⚠️⚠️ Avertissement ⚠️⚠️⚠️**

Si vous retournez dans le même restaurant italien avec votre petite amie, mais qu'elle ne veut pas manger, voici ce qui se passera :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_8g5NLq3fTBekvu6gvnfJcw.png)

Si le `serveur$` utilise l'opérateur `zip`, vous n'aurez que votre boisson !

Pourquoi ?

Parce que, lorsque le `serveur$` émet les boissons, l'observable `petiteamie$` est complet et aucune autre valeur ne peut être collectée à partir de celui-ci. Heureusement, le `serveur$` peut utiliser un autre opérateur pour nous afin que nous ne romptions pas avec notre petite amie ?

# combineLatest()

* `combineLatest` ne commence pas à émettre tant que chaque observable interne n'a pas émis au moins une valeur
* Lorsque n'importe quel observable interne émet une valeur, émet la dernière valeur émise de chacun

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_TrJG2NP6PgA0HJMj598lpQ.png)

Dans le même restaurant, le `serveur$` intelligent décide maintenant d'utiliser l'opérateur `combineLatest`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_GHNM2srLwN4Wihm7U8bcQg.png)

**⚠️⚠️⚠️ Avertissement ⚠️⚠️⚠️**

Avec `combineLatest`, l'**ordre** des observables internes fournis est important.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/4.png)

Si `vous$` est fourni en premier au `serveur$`, il émettra une seule valeur `["Tiramisu", "Sprite"]`. 

Cela se produit parce que `combineLatest` ne commence pas à émettre tant que chaque observable interne n'a pas émis au moins une valeur. `petiteamie$` commence à émettre lorsque le premier observable interne émet sa dernière valeur. Ensuite, `combineLatest` émet les dernières valeurs collectées à partir des deux observables internes.

# forkJoin()

* `forkJoin` émet la dernière valeur émise de chaque observable interne après qu'ils **aient tous** terminé
* `forkJoin` n'émettra jamais si l'un des observables ne termine pas

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_O-Uis5OrgaeUrh6JSgHkTg.png)

Lorsque vous allez au restaurant et commandez une pizza, vous ne voulez pas connaître toutes les étapes de la préparation de la pizza. Si le fromage est ajouté avant les tomates ou l'inverse. Vous voulez simplement votre pizza ! C'est là que `forkJoin` entre en jeu.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_tB1kiVeQ2kpicnNjFnN_dA.png)

**⚠️⚠️⚠️ Avertissement ⚠️⚠️⚠️**

* Si l'un des observables internes génère une erreur, toutes les valeurs sont perdues
* `forkJoin` ne termine pas

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_zLaN2lzWlASOC3X7f-k3kA.png)

* Si vous ne vous souciez que du moment où **tous** les observables internes se terminent avec succès, vous pouvez attraper l'erreur de l'**extérieur**
* Ensuite, `forkJoin` termine

![Image](https://www.freecodecamp.org/news/content/images/2020/05/2.png)

* Si vous ne vous souciez pas que les observables internes se terminent avec succès ou non, vous devez attraper les erreurs de chaque observable interne individuel
* Ensuite, `forkJoin` termine

![Image](https://www.freecodecamp.org/news/content/images/2020/05/3.png)

Personnellement, lorsque je vais au restaurant avec des amis, je ne me soucie pas si l'un d'eux reçoit une pizza brûlée. Je veux simplement la mienne ? donc je demanderai au `serveur$` d'attraper les erreurs des observables internes individuellement.

# Conclusion

Nous avons couvert beaucoup de choses dans cet article ! De bons exemples sont importants pour mieux comprendre les opérateurs RxJS et comment les choisir judicieusement. 

Pour les opérateurs de combinaison comme `zip`, `combineLatest` et `forkJoin`, l'ordre des observables internes que vous fournissez est également crucial, car il peut vous conduire à des comportements inattendus.

Il y a beaucoup plus à couvrir dans RxJS et je le ferai dans de futurs articles.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RHYpi9BEvKatE0NRsHfnOw.gif)

J'espère que vous avez apprécié cet article ! ?

? Vous pouvez [me suivre sur Twitter](https://twitter.com/tSamoss) pour être informé des nouveaux articles de blog sur Angular/RxJS et des conseils sympas !