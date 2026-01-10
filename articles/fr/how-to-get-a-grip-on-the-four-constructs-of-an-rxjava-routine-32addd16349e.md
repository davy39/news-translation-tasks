---
title: Comment maîtriser les quatre éléments d'une routine RxJava
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:17:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-grip-on-the-four-constructs-of-an-rxjava-routine-32addd16349e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EqESoVsAoU6eWUMYIA4wxA.png
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: mobile app development
  slug: mobile-app-development
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment maîtriser les quatre éléments d'une routine RxJava
seo_desc: 'By Ayusch Jain


  This article was originally posted here.


  RxJava has become the single most important weapon in the android development arsenal.
  Every developer in 2019 must start using it in their apps if they haven’t already.
  According to the offic...'
---

Par Ayusch Jain

> [_Cet article a été initialement publié ici_](https://www.ayusch.com/understanding-rxjava-basics)_._

RxJava est devenu l'outil le plus important dans l'arsenal du développement Android. Chaque développeur en 2019 doit commencer à l'utiliser dans ses applications s'il ne l'a pas déjà fait. Selon la définition officielle de RxJava :

> _"RxJava est une implémentation de machine virtuelle Java des [Reactive Extensions](http://reactivex.io/) : une bibliothèque pour composer des programmes asynchrones et basés sur des événements en utilisant des séquences observables."_

Cette définition peut sembler intimidante avec tous les termes techniques tels que machine virtuelle Java, Reactive Extensions, asynchrone basé sur des événements, séquences observables, etc. Mais devinez quoi ? Vous avez utilisé toutes ces choses dans vos tâches quotidiennes de développement Android sans le savoir.

> _Remarque : Je suppose que si vous cherchez à plonger profondément dans RxJava, vous avez une bonne connaissance du langage de programmation Java. Sinon, vous pouvez trouver diverses [écoles en ligne](https://www.microverse.org/) qui peuvent vous aider avec cela._

### Pour commencer

Commençons par la **machine virtuelle Java (ou JVM)**. Vous êtes-vous déjà demandé comment votre code écrit en utilisant l'alphabet anglais est traduit en pixels à l'écran ? Comment vos changements de couleur dans le code se traduisent par des changements de couleur à l'écran ? Eh bien, tout cela est fait par la JVM.

Tout d'abord, votre code source est compilé en Bytecode par le compilateur. Ensuite, la JVM prend ce Bytecode et le convertit en quelque chose que la machine peut comprendre. Dans d'autres [langages](https://www.ayusch.com/understanding-rxjava-basics), le compilateur convertit le code pour un système particulier, mais le compilateur de Java convertit le code source en Bytecode qui peut être exécuté sur n'importe quelle machine avec une JVM.

Maintenant, comprenez-vous pourquoi Kotlin peut être utilisé pour écrire des applications Android ? Si ce n'est pas le cas, soyez à l'affût de mon prochain article.

### **Reactive Extensions**

Les Reactive Extensions ou ReactiveX existent depuis longtemps. Ce n'est rien d'autre qu'une API qui facilite la programmation réactive.

Sans le savoir, nous avons écrit du code réactif tout au long. Par exemple, lorsqu'un clic sur un bouton se produit, il déclenche un certain bloc de code dans votre fichier source. C'est de la programmation réactive ! Un morceau de code a réagi à un événement (un clic sur un bouton dans ce cas).

[Reactive Extensions](https://www.ayusch.com/understanding-rxjava-basics) n'est pas spécifique à un langage de programmation, mais plutôt une méthodologie qui a été implémentée dans des langages tels que Java (RxJava), JavaScript (RxJS), C# (Rx.NET), Scala (RxScala) et bien d'autres ! Vous voyez donc que ReactiveX n'est pas spécifique à un langage, mais plutôt un modèle de conception qui peut être implémenté dans n'importe quel langage.

### Les éléments de RxJava

RxJava repose essentiellement sur 4 éléments :

* Observable
* Scheduler
* Observer
* Subscriber

Ces 4 composants sont présents dans toutes les routines RxJava. Bien qu'ils ne soient pas obligatoires, je vous recommande de vous y tenir en tant que débutant. Une fois que vous serez à l'aise avec RxJava, vous pourrez jeter les règles par la fenêtre et commencer à expérimenter. Mais avant d'atteindre ce niveau, restez fidèle aux bases.

Examinons donc chacun de ces éléments plus en détail.

#### **Observable**

Un Observable est exactement ce à quoi il ressemble : quelque chose qui peut être observé. Un observable (bouton) dans RxJava est surveillé par un Observer (code qui s'exécute lors d'un clic sur un bouton) qui réagit à tout événement émis (événement de clic sur un bouton) par l'observable. Ce modèle facilite les opérations concurrentes, car le thread principal n'a pas besoin d'être bloqué en attendant que l'observable émette des événements. L'observateur est toujours prêt à réagir dès que l'observable émet.

RxJava suit le modèle de l'observateur dans lequel un Observer (expliqué plus tard) s'abonne à un Observable qui émet des événements/données et réagit en conséquence. Les concepts de RxJava sont mieux expliqués à l'aide de diagrammes de Marble. En voici un pour vous :

![Image](https://cdn-media-1.freecodecamp.org/images/qhMY4gqVCAcxjxD-bn35bEFAABTt9PDiNAtG)

Dans ReactiveX, de nombreuses instructions peuvent s'exécuter en parallèle et leurs résultats sont ensuite capturés, dans un ordre arbitraire, par des "observateurs". Plutôt que d'appeler une méthode, vous définissez un mécanisme pour récupérer et transformer les données, sous la forme d'un "Observable". Ensuite, vous abonnez un observateur à celui-ci, moment auquel le mécanisme précédemment défini se met en action avec l'observateur prêt à capturer et à répondre à ses émissions dès qu'elles sont prêtes.

Un avantage de cette approche est que lorsque vous avez un ensemble de tâches qui ne dépendent pas les unes des autres, vous pouvez les démarrer toutes en même temps plutôt que d'attendre que chacune se termine avant de commencer la suivante. Ainsi, l'ensemble de vos tâches ne prend que le temps de la tâche la plus longue dans le lot.

#### [**Schedulers _(important)_**](https://www.ayusch.com/understanding-rxjava-basics)

L'une des fonctionnalités super cool de RxJava est qu'elle permet une concurrency instantanée. La **concurrency** est vraiment difficile à comprendre. Même aujourd'hui, c'est l'un des sujets les plus complexes en informatique et est vraiment difficile à implémenter.

Les génies qui ont écrit RxJava ont abstrait toutes ces complexités pour nous, nous offrant des API relativement plus simples à utiliser. RxJava gère la concurrency à l'aide de Schedulers. Dans la routine RxJava, nous avons un opérateur nommé

```
subscribeOn()
```

> **_Il dit essentiellement :_** Voici un observable et un observateur, prenez-les et établissez leur connexion sur ce thread particulier.

Tout cela peut être réalisé avec du Java pur en utilisant des Threads, Handlers, Executors, etc., mais les Schedulers sont simplement une manière élégante de le gérer.

Généralement, la plupart des opérations sont déléguées au thread IO. Mais il existe de nombreux autres types de schedulers. Voici quelques-uns des plus couramment utilisés :

* **Schedulers.io():** utilisé pour les tâches IO non computationnelles telles que la gestion de fichiers, les appels réseau, la gestion de bases de données, etc. Ce pool de threads est destiné à être utilisé pour les tâches asynchrones.
* **Schedulers.computation():** Comme son nom l'indique, il est destiné à être utilisé pour les tâches nécessitant beaucoup de calculs, telles que le traitement d'images, le traitement de jeux de données, etc. Il dispose d'autant de threads que de processeurs disponibles. Mais vous devez être prudent lors de son utilisation, car cela peut entraîner une dégradation des performances en raison du changement de contexte dans les threads.
* **Schedulers.from(Executor ex):** crée et retourne un scheduler personnalisé soutenu par un exécutant spécifique.
* **Schedulers.mainThread():** Hé, je n'ai pas oublié les développeurs Android ? Cela est fourni par la bibliothèque RxAndroid et nous fournit le thread principal. Faites attention à ne pas effectuer de tâches longues sur ce thread, car il est synchrone et peut entraîner des ANR.

Il existe également un opérateur nommé

```
observeOn()
```

Comme nous l'avons vu ci-dessus, **subscribeOn()** indique à l'Observable source quel thread utiliser pour émettre des éléments — ce thread poussera les émissions jusqu'à notre Observer. Cependant, s'il rencontre un observeOn() quelque part dans la chaîne, il basculera et transmettra les émissions en utilisant ce Scheduler pour les opérations restantes (en aval).

### **Observer/Subscriber**

Comme un artiste a besoin d'un public, l'observable a également besoin de quelqu'un pour l'observer pendant qu'il émet des éléments. Il peut y avoir des émissions sans observateur (recherchez les observables chauds et froids sur Google), mais c'est une histoire pour une autre fois.

Un **observer** s'abonne à l'observable à l'aide de la méthode subscribe(). Dès que l'observateur s'abonne, il est prêt à recevoir des notifications de l'observable.

Il fournit trois méthodes pour gérer les notifications :

* **onNext():** Dans cette méthode, la notification est livrée à l'abonné sans aucune erreur.
* **onError():** Une erreur est envoyée à l'abonné dans onError décrivant l'erreur.
* **onComplete():** Cela est appelé à la fin lorsque la source a terminé l'émission.

Selon que vous observiez sur le thread principal ou un thread séparé, vous recevrez les émissions dans le onNext dans le thread principal ou un nouveau thread.

Lorsque qu'un Subscriber s'abonne à un Publisher, dans RxJava2, une instance Disposable est retournée qui peut être utilisée pour annuler/disposer un Subscriber externement via Disposable::dispose().

Voici un diagramme pour vous aider à mieux comprendre cette relation :

[caption id="attachment_1032" align="aligncenter" width="1340"]

![Image](https://cdn-media-1.freecodecamp.org/images/pElm1-RWq8hbX1KQU-eFlfpxQud0esO0k1Xf)

Source de l'image [[Mindorks](https://mindorks.com/course/learn-rxjava/public/chapter/id/2/page/id/7)][/caption]

### Dois-je même utiliser RxJava ?

Au lieu de faire mon plaidoyer verbalement, je vous laisse décider. Il suffit de parcourir le code ci-dessous.

#### Java

```
List<Integer> temp = Arrays.asList(5,8,9,20,30,40);List<Integer> javaList = new ArrayList<>();
```

```
for(Integer i: temp){    if(i>10)        javaList.add(i);}
```

#### RxJava

```
List<Integer> rxlist = Stream.of(5, 8, 9, 20, 30, 40).filter(x -> x > 10).        collect(Collectors.toList());
```

#### Java

```
TPExecutor.execute(() -> api.getUserDetails(userId))        .runOnUIAfterBoth(TPExecutor.execute(() -> api.getUserPhoto(userId)), p -> {            // Faites votre tâche        });
```

#### RxJava

```
Observable.zip(api.getUserDetails2(userId), api.getUserPhoto2(userId), (details, photo) -> Pair.of(details, photo))        .subscribe(p -> {            // Faites votre tâche.        });
```

#### **AsyncTask**

```
private class MyTask extends AsyncTask<String, Integer, Boolean>{    @Override    protected Boolean doInBackground(String... paths)    {        for (int index = 0; index < paths.length; index++)        {            boolean result = copyFileToExternal(paths[index]);
```

```
            if (result == true)            {                // mettre à jour l'UI                publishProgress(index);            }            else            {                // arrêter le processus en arrière-plan                return false;            }        }
```

```
        return true;    }
```

```
    @Override    protected void onProgressUpdate(Integer... values)    {        super.onProgressUpdate(values);        int count = values[0];        // cela mettra à jour mon textview pour montrer le nombre de fichiers copiés        myTextView.setText("Total files: " + count);    }
```

```
    @Override    protected void onPostExecute(Boolean result)    {        super.onPostExecute(result);        if (result)        {            // afficher une boîte de dialogue de succès            ShowSuccessAlertDialog();        }        else        {            // afficher une boîte de dialogue d'échec            ShowFailAlertDialog();        }    }}
```

#### **RxJava**

```
Observable.fromArray(getPaths())        .map(path -> copyFileToExternal(path))        .subscribeOn(Schedulers.io())        .observeOn(AndroidSchedulers.mainThread())        .subscribe(aInteger -> Log.i("test", "update UI"),                throwable -> ShowFailAlertDialog),        () -> ShowSuccessAlertDialog());
```

Vous pouvez voir que le code RxJava est beaucoup plus lisible et concis (les expressions lambda peuvent sembler un peu intimidantes si vous ne les connaissez pas, mais une fois que vous commencez à les utiliser, ce code vous semblera naturel). Et il existe de nombreux autres exemples où les opérateurs RxJava libèrent leur puissance sur la programmation Java traditionnelle.

### Inconvénients

Je n'ai trouvé aucun inconvénient à utiliser RxJava jusqu'à présent — juste qu'il a une courbe d'apprentissage vraiment **abrupte**. Si vous n'êtes pas déjà familier avec le modèle Observer, **Java 8** (non obligatoire mais vraiment utile), les lambdas, etc., vous trouverez le code RxJava vraiment intimidant.

Mais à mesure que vous commencez à corriger votre code avec RxJava, vous commencerez lentement à vous y habituer et vous réaliserez que la plupart des éléments dans RxJava restent les mêmes.

[Ce post contient une liste complète de ressources pour vous aider à démarrer.](https://blog.mindorks.com/a-complete-guide-to-learn-rxjava-b55c0cea3631)

_Aimez ce que vous avez lu ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp**, et **LinkedIn**._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), et [Instagram](https://www.instagram.com/androidville/) où je réponds aux questions liées au **développement mobile, en particulier Android et Flutter**._

![Image](https://cdn-media-1.freecodecamp.org/images/NNWIaau9-uWSJFA1fHCjrcfMrOQo-fMAWAZm)