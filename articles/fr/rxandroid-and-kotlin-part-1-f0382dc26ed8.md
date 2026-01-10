---
title: RxAndroid et Kotlin (Partie 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-06-27T11:16:11.000Z'
originalURL: https://freecodecamp.org/news/rxandroid-and-kotlin-part-1-f0382dc26ed8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bTttcFdSLyvWIPg91OaNEw.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Kotlin
  slug: kotlin
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
seo_title: RxAndroid et Kotlin (Partie 1)
seo_desc: 'By Ahmed Rizwan

  When I first started using RxAndroid, I didn’t really get it. I mean, I grasped
  abstract concept. But I didn’t understand where I should be using it.

  But then I went through a few examples and read a few really good articles (recommen...'
---

Par Ahmed Rizwan

Lorsque j'ai commencé à utiliser [RxAndroid](https://github.com/ReactiveX/RxAndroid), je n'ai pas vraiment compris. Je veux dire, j'ai saisi le concept abstrait. Mais je ne comprenais pas où je devrais l'utiliser.

Mais ensuite, j'ai parcouru quelques exemples et lu quelques très bons articles (liste de lectures recommandées en bas de cet article.) J'ai enfin compris ! Et ma réaction a été à peu près :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjlr5GxQIx8o28U5nhtDxg.gif)
_Tel Rx. Tellement Réactif. Wow !_

En bref, vous pouvez utiliser Rx presque partout. Mais **vous ne devriez pas**. Vous devriez déterminer intelligemment où l'utiliser. Parce que dans certains cas, utiliser Rx peut être 100 fois plus productif que la programmation impérative normale. Et dans d'autres cas, ce n'est simplement pas nécessaire.

Je vais démontrer quelques exemples en **Kotlin** et en **Java**, afin que vous ayez une idée de ce qu'est Rx, ainsi qu'une comparaison des deux langages.

Maintenant, si vous n'êtes pas encore familier avec Kotlin, c'est une alternative awesometacular à Java, qui fonctionne incroyablement bien sur Android. Et oh, il est développé par JetBrains !

P.S. Il n'y a pas de points-virgules en Kotlin. *_*

Si vous voulez en savoir plus, consultez :

[Site officiel de Kotlin](http://kotlinlang.org)

[Commencer sur Android](http://kotlinlang.org/docs/tutorials/kotlin-android.html)

[Document de Jake Wharton sur Kotlin](https://docs.google.com/document/d/1ReS3ep-hjxWA8kZi0YqDbEhCqTt29hG8P44aA9W0DM8/edit?usp=sharing)

[Mon Blog](https://medium.com/@ahmedrizwan/android-programming-with-kotlin-6ce3f9b0cbe6) ;)

Maintenant, revenons à Rx.

Si vous avez déjà une bonne compréhension de Rx, vous pouvez sauter ce sujet. Sinon, continuez votre lecture.

Ok, alors qu'est-ce que Rx ? Eh bien, c'est de la "programmation réactive". La programmation réactive est, en termes simples, un modèle de programmation étroitement lié au **modèle d'observateur**, dans lequel les abonnés "réagissent" aux événements émis par ces observables.

Voici un diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oa7zxVaeyF4TO6Mres4E5w.png)

Rx est également un sous-ensemble de la **programmation fonctionnelle**. D'où le terme souvent utilisé de programmation réactive fonctionnelle. À mesure que les abonnés reçoivent des données, ils peuvent appliquer une séquence de **transformations** sur celles-ci, similaire à ce que nous pouvons faire avec les flux en Java 8.

Voici un autre diagramme utile :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ATqZ5sek2uAPfZMdmsWHSg.png)
_Transformations lorsque l'abonné reçoit des données de l'observable._

Nous pouvons même fusionner des flux les uns avec les autres. C'est aussi flexible que cela ! Donc pour l'instant, retenez simplement qu'il y a des tonnes de choses différentes que nous pouvons faire avec les données que nous (les abonnés) recevons des observables, à la volée.

Maintenant que le concept est quelque peu clair, revenons à RxJava.

Dans Rx, l'**abonné** implémente trois méthodes pour interagir avec l'**observable** :

1. onNext(Data) : Reçoit les données de l'observable
2. onError(Exception) : Est appelé si une exception est levée
3. onCompleted() : Est appelé lorsque le flux de données se termine

Cela peut être comparé aux **Iterables** en Java. La différence est que les iterables sont **basés sur la demande**, et les observables Rx sont **basés sur la poussée**. L'observable pousse les données vers ses abonnés.

Voici le tableau de comparaison :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6xrzAdP_wa6aR80UrNxiIw.png)

Une autre chose à noter est que Rx est **synchrone** par nature, ce qui signifie que vous devrez spécifier si vous voulez qu'il soit asynchrone. Vous pouvez le faire en appelant les méthodes **observeOn** et **subscribeOn**.

Ainsi, les observables poussent des **flux de données** vers leurs abonnés, et les abonnés peuvent consommer ces flux à l'aide des méthodes listées ci-dessus. Nous pouvons mieux comprendre les "flux" à l'aide des [Marble Diagrams](http://rxmarbles.com) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2-sTf0tHsmDlent1HLIhrg.png)
_Un diagramme de marbres représentant deux flux différents._

Les cercles sur ces flux représentent des **objets de données**. Et les flèches représentent le fait que les données circulent dans une direction de manière ordonnée.

Jetez un coup d'œil à ce diagramme de marbres :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ju5YD8bRZhdCGmptRQdmlw.png)
_Un mappage d'un flux._

Comme je l'ai mentionné précédemment, nous pouvons **transformer** les données (ainsi que les flux) en utilisant des [**opérateurs**](https://github.com/ReactiveX/RxJava/wiki/Alphabetical-List-of-Observable-Operators) comme map, filter et zip. L'image ci-dessus représente un mappage simple. Ainsi, après cette transformation, l'abonné à ce flux recevra la version transformée du flux. Cool, non ?

Vous devriez maintenant avoir une bonne compréhension de comment les choses fonctionnent dans Rx, alors passons à l'implémentation réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-nTq2bHQbJZctDZZoPnBYQ.png)

### Implémentation des Observables

La première chose que nous devons faire est de méditer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I6aMRP_WrXdse197zfBh1Q.jpeg)

Après cela, créer un observable n'est pas si difficile.

Il existe plusieurs façons de [créer des observables](https://github.com/ReactiveX/RxJava/wiki/Creating-Observables). J'en listerai trois ici :

1. **Observable.from()** crée un observable à partir d'un Iterable, d'un Future ou d'un Array.

```
//Kotlin
Observable.from(listOf(1, 2, 3, 4, 5))
//Java
Observable.from(Arrays.asList(1, 2, 3, 4, 5));
```

```
//Il émettra ces nombres dans l'ordre : 1 - 2 - 3 - 4 - 5 //Ce qui devrait être assez évident je suppose.
```

2. **Observable.just()** crée un observable à partir d'un objet ou de plusieurs objets :

```
Observable.just("Hello World!") //cela émettra "Hello World!" à tous ses abonnés
```

3. **Observable.create()** crée un observable à partir de zéro au moyen d'une fonction. Nous implémentons simplement l'interface OnSubscribe, puis nous disons à l'observable ce qu'il doit envoyer à ses abonnés :

```
//Kotlin
Observable.create(object : Observable.OnSubscribe<Int> {    override fun call(subscriber: Subscriber<in Int>) {        for(i in 1 .. 5)            subscriber.onNext(i)        subscriber.onCompleted()    }})
```

Et voici la version Java du même code :

```
//Java
Observable.create(new Observable.OnSubscribe<Integer>() {    @Override    public void call(final Subscriber<? super Integer> subscriber) {        for (int i = 1; i <= 5; i++)            subscriber.onNext(i);        subscriber.onCompleted();    }});
```

```
//En utilisant l'implémentation ci-dessus, nous disons à l'observateur ce qu'il //doit faire lorsqu'un abonné s'abonne à lui. D'où le nom "onSubscribe".
```

Le code que j'ai écrit ci-dessus est équivalent à l'exemple que j'ai écrit pour **Observable.from()**, mais comme vous pouvez le voir, nous avons un contrôle total sur ce qui doit être émis et quand le flux doit se terminer. Je peux également envoyer des exceptions capturées avec l'utilisation de **subscriber.onError(e)**.

Maintenant, nous avons juste besoin de quelques abonnés.

### Implémentation des Abonnés

Pour Android, pour s'abonner à un observable, nous disons d'abord à l'observable sur quels threads nous prévoyons de nous abonner et d'observer. RxAndroid nous donne des [**Schedulers**](https://github.com/ReactiveX/RxJava/wiki/The-RxJava-Android-Module), grâce auxquels nous pouvons spécifier les threads.

Alors prenons un simple observable "Hello World" par exemple. Ici, nous allons faire l'abonnement sur un **thread de travail**, et l'observation sur le **thread principal** :

```
//Kotlin
Observable.just("Hello World")          .subscribeOn(Schedulers.newThread())           //chaque abonnement va être sur un nouveau thread.          .observeOn(AndroidSchedulers.mainThread()))           //observation sur le thread principal          //Maintenant notre abonné !          .subscribe(object:Subscriber<String>(){            override fun onCompleted() {             //Terminé            }            override fun onError(e: Throwable?) {             //TODO : Gérer l'erreur ici            }            override fun onNext(t: String?) {             Log.e("Output",t);            }           })
```

```
//Java 
Observable.just("Hello World")        .subscribeOn(Schedulers.newThread())        .observeOn(AndroidSchedulers.mainThread())        .subscribe(new Subscriber<String>() {            @Override            public void onCompleted() {                //Terminé            }            @Override            public void onError(final Throwable e) {                //TODO : Gérer l'erreur ici            }            @Override            public void onNext(final String s) {                Log.e("Output",s);            }        });
```

```
//Vous pouvez obtenir plus d'informations sur les schedulers et les threads ici.
```

Alors... Que fait cela ?

Lorsque vous exécutez ce code, il affiche un message de log :

```
Output: Hello World!
```

Et c'est tout ! C'est à quel point l'abonnement est simple. Vous pouvez obtenir plus de détails sur subscribe [ici](http://reactivex.io/documentation/operators/subscribe.html).

### Un Exemple Pratique : Debounce

Alors maintenant vous avez une idée de comment vous pouvez créer quelques observables simples, n'est-ce pas ? Alors implémentons un de mes exemples Rx préférés. Je veux implémenter ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lyOcKYAvTjDnArAN4rEDNw.gif)

Dans cet exemple, je saisis du texte dans un **EditText**. Cela déclenche automatiquement une réponse dans laquelle j'imprime le texte.

Maintenant, la réponse pourrait être un appel à une API. Donc faire cet appel API à chaque fois que je tape un caractère serait gaspiller des ressources, puisque je n'ai besoin d'une réponse que pour le dernier caractère. Donc je devrais déclencher un appel seulement lorsque j'arrête de taper — disons une seconde après avoir fini de taper.

Alors comment faisons-nous cela en programmation non réactive ? Eh bien, ce n'est pas joli !

#### **Un Debounce Non-Réactif**

J'utilise un Timer, et je le planifie pour appeler la méthode **run()** après un délai de 1000 millisecondes dans la méthode **afterTextChanged()**. Oh, et n'oubliez pas d'ajouter **runOnUiThread()** également.

Conceptuellement, ce n'est pas si difficile, mais le code devient encombré. Encore plus en Java !

Version Java :

Version Kotlin :

#### **Solution Réactive**

Une solution réactive est beaucoup plus simple et sans code répétitif. Et il n'y a que 3 étapes à suivre.

1. Créer un observable
2. Ajouter l'opérateur Debounce avec un délai de 1000 millisecondes (1 seconde)
3. S'abonner à celui-ci

D'abord le code Java :

Maintenant le Kotlin ❤

#### Pour encore moins de code répétitif, utilisez RxBindings.

Maintenant, pour presque aucun code répétitif, nous pouvons utiliser [**RxBindings**](https://github.com/JakeWharton/RxBinding) qui a de nombreuses liaisons super-awesomes pour les widgets UI. Et cela fonctionne à la fois en Java et en Kotlin ! En utilisant les liaisons, le code devient :

Comme vous pouvez le voir, il y a très peu de code répétitif, et le code est beaucoup plus direct. Si je devais revenir à ce code dans quelques mois, cela ne me prendrait qu'une minute pour comprendre ce qui se passe. Et c'est inestimable !

Voici quelques ressources awesomes pour Rx que je recommande. Consultez-les !

[Page Officielle Rx](http://reactivex.io)

[Série Grokking RxJava par Dan Lew](http://blog.danlew.net/2014/09/15/grokking-rxjava-part-1/)

[Android Rx, et Kotlin : Une étude de cas](http://beust.com/weblog/2015/03/23/android-rx-and-kotlin-a-case-study/)

[Remplacer AsyncTasks par Rx](http://stablekernel.com/blog/replace-asynctask-asynctaskloader-rx-observable-rxjava-android-patterns/)

[Blog PhilosophicalHacker sur Rx](http://www.philosophicalhacker.com/2015/06/12/an-introduction-to-rxjava-for-android/)

[Implémentation de EventBus dans Rx](http://nerds.weddingpartyapp.com/tech/2014/12/24/implementing-an-event-bus-with-rxjava-rxbus/)

[RxKotlin](https://github.com/ReactiveX/RxKotlin)