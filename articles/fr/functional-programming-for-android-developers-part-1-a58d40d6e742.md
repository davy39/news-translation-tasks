---
title: Programmation Fonctionnelle pour les Développeurs Android — Partie 1
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-20T07:51:31.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-1-a58d40d6e742
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DCzEYU60hk2pO7WCJj3GoQ.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Programmation Fonctionnelle pour les Développeurs Android — Partie 1
seo_desc: 'By Anup Cowkur

  Lately, I’ve been spending a lot of time learning Elixir, an awesome functional
  programming language that is friendly to beginners.

  This got me thinking: why not use some of the concepts and techniques from the functional
  world in Andr...'
---

Par Anup Cowkur

Récemment, j'ai passé beaucoup de temps à apprendre [Elixir](http://elixir-lang.org/), un langage de programmation fonctionnelle génial qui est accessible aux débutants.

Cela m'a fait réfléchir : pourquoi ne pas utiliser certains des concepts et techniques du monde fonctionnel en programmation Android ?

Lorsque la plupart des gens entendent le terme _Programmation Fonctionnelle_, ils pensent aux publications de Hacker News qui parlent de Monades, de Fonctions d'Ordre Supérieur et de Types de Données Abstraits. Cela semble être un univers mystique éloigné des tracas du programmeur quotidien, réservé uniquement aux hackers les plus puissants descendus du royaume de Númenor.

Eh bien, _n'importe quoi_ ! Je suis ici pour vous dire que vous aussi pouvez l'apprendre. Vous aussi pouvez l'utiliser. Vous aussi pouvez créer de belles applications avec cela. Des applications qui ont des bases de code élégantes, lisibles et qui ont moins d'erreurs.

Bienvenue dans la Programmation Fonctionnelle (PF) pour les développeurs Android. Dans cette série, nous allons apprendre les fondamentaux de la PF et comment nous pouvons les utiliser en Java et en Kotlin. L'idée est de garder les concepts ancrés dans la pratique et d'éviter autant que possible le jargon académique.

La PF est un sujet vaste. Nous allons apprendre uniquement les concepts et techniques utiles pour écrire du code Android. Nous pourrions aborder quelques concepts que nous ne pouvons pas utiliser directement pour des raisons de complétude, mais j'essaierai de garder le matériel aussi pertinent que possible.

Prêt ? C'est parti.

### Qu'est-ce que la Programmation Fonctionnelle et pourquoi devrais-je l'utiliser ?

Bonne question. Le terme _Programmation Fonctionnelle_ est un terme générique pour une gamme de concepts de programmation que le surnom ne rend pas tout à fait justice. À sa base, c'est un style de programmation qui traite les programmes comme l'évaluation de fonctions mathématiques et évite l'_état mutable_ et les _effets de bord_ (nous parlerons de ces derniers bientôt).

À sa base, la PF met l'accent sur :

* **Code déclaratif** — Les programmeurs devraient se soucier du _quoi_ et laisser le compilateur et l'environnement d'exécution se soucier du _comment_.
* **Explicité** — Le code devrait être aussi évident que possible. En particulier, les effets de bord doivent être isolés pour éviter les surprises. Le flux de données et la gestion des erreurs sont explicitement définis et des constructions comme les instructions _GOTO_ et les _Exceptions_ sont évitées car elles peuvent mettre votre application dans des états inattendus.
* **Concurence** — La plupart du code fonctionnel est concurrent par défaut grâce à un concept connu sous le nom de _pureté fonctionnelle_. L'accord général semble être que cette caractéristique en particulier est à l'origine de la popularité croissante de la programmation fonctionnelle, puisque les cœurs de CPU ne deviennent pas plus rapides chaque année comme ils le faisaient avant (voir [Loi de Moore](https://en.wikipedia.org/wiki/Moore's_law)) et nous devons rendre nos programmes plus concurrents pour tirer parti des architectures multi-cœurs.
* **Fonctions d'Ordre Supérieur** — Les fonctions sont des membres de première classe, tout comme tous les autres primitives du langage. Vous pouvez passer des fonctions comme vous le feriez avec une chaîne de caractères ou un entier.
* **Immuabilité** — Les variables ne doivent pas être modifiées une fois qu'elles sont initialisées. Une fois qu'une chose est créée, elle reste cette chose pour toujours. Si vous voulez la changer, vous créez une nouvelle chose. C'est un autre aspect de l'explicité et de l'évitement des effets de bord. Si vous savez qu'une chose ne peut pas changer, vous avez beaucoup plus de confiance dans son état lorsque vous l'utilisez.

Du code déclaratif, explicite et concurrent qui est plus facile à comprendre et conçu pour éviter les surprises ? J'espère avoir piqué votre curiosité.

Dans cette première partie de la série, commençons par certains des concepts les plus fondamentaux de la PF : _Pureté_, _Effets de bord_ et _Ordre_.

### Fonctions pures

Une fonction est pure si sa sortie dépend uniquement de son entrée et n'a pas d'_effets de bord_ (nous parlerons des effets de bord juste après cela). Voyons un exemple, voulez-vous ?

Considérons cette fonction simple qui additionne deux nombres. Elle lit un nombre depuis un fichier et l'autre nombre est passé en tant que paramètre.

**Java**

```
int add(int x) {    int y = readNumFromFile();    return x + y;}
```

**Kotlin**

```
fun add(x: Int): Int {    val y: Int = readNumFromFile()    return x + y}
```

La sortie de cette fonction ne dépend pas uniquement de son entrée. Selon ce que _readNumFromFile()_ retourne, elle peut avoir différentes sorties pour la même valeur de _x_. Cette fonction est dite _impure_.

Convertissons-la en une fonction pure.

**Java**

```
int add(int x, int y) {    return x + y;}
```

**Kotlin**

```
fun add(x: Int, y: Int): Int {    return x + y}
```

Maintenant, la sortie de la fonction dépend uniquement de ses entrées. Pour un _x_ et un _y_ donnés, la fonction retournera toujours la même sortie. Cette fonction est maintenant dite _pure_. Les fonctions mathématiques fonctionnent également de la même manière. La sortie d'une fonction mathématique dépend uniquement de ses entrées — c'est pourquoi la programmation fonctionnelle est beaucoup plus proche des mathématiques que le style de programmation habituel auquel nous sommes habitués.

P.S. Une entrée vide est toujours une entrée. Si une fonction ne prend aucune entrée et retourne la même constante à chaque fois, elle est toujours pure.

P.P.S. La propriété de toujours retourner la même sortie pour une entrée donnée est également connue sous le nom de _transparence référentielle_ et vous pourriez la voir utilisée lorsque l'on parle de fonctions pures.

### Effets de bord

Explorons ce concept avec le même exemple de fonction d'addition. Nous allons modifier la fonction d'addition pour qu'elle écrive également le résultat dans un fichier.

**Java**

```
int add(int x, int y) {    int result = x + y;    writeResultToFile(result);    return result;}
```

**Kotlin**

```
fun add(x: Int, y: Int): Int {    val result = x + y    writeResultToFile(result)    return result}
```

Cette fonction écrit maintenant le résultat du calcul dans un fichier. C'est-à-dire qu'elle modifie l'état du monde extérieur. Cette fonction est maintenant dite avoir un _effet de bord_ et n'est plus une fonction pure.

Tout code qui modifie l'état du monde extérieur — change une variable, écrit dans un fichier, écrit dans une base de données, supprime quelque chose, etc. — est dit avoir un effet de bord.

Les fonctions qui ont des effets de bord sont évitées en PF car elles ne sont plus pures et dépendent du _contexte historique_. Le contexte du code n'est pas autonome. Cela les rend beaucoup plus difficiles à comprendre.

Disons que vous écrivez un morceau de code qui dépend d'un cache. Maintenant, la sortie de votre code dépend de si quelqu'un a écrit dans le cache, de ce qui y a été écrit, de quand cela a été écrit, de si les données sont valides, etc. Vous ne pouvez pas comprendre ce que fait votre programme à moins de comprendre tous les états possibles du cache dont il dépend. Si vous étendez cela pour inclure toutes les autres choses dont votre application dépend — réseau, base de données, fichiers, entrée utilisateur, etc., il devient très difficile de savoir exactement ce qui se passe et de tout garder en tête à la fois.

Cela signifie-t-il que nous n'utilisons pas de réseau, de bases de données et de caches ? Bien sûr que non. À la fin de l'exécution, vous voulez que l'application fasse quelque chose. Dans le cas des applications Android, cela signifie généralement mettre à jour l'interface utilisateur afin que l'utilisateur puisse obtenir quelque chose d'utile de notre application.

La plus grande idée de la PF n'est pas de renoncer complètement aux effets de bord, mais de les contenir et de les isoler. Au lieu d'avoir notre application parsemée de fonctions qui ont des effets de bord, nous repoussons les effets de bord aux limites de notre système afin qu'ils aient le moins d'impact possible, rendant notre application plus facile à comprendre. Nous en parlerons en détail lorsque nous explorerons une _architecture fonctionnelle_ pour nos applications plus tard dans la série.

### Ordre

Si nous avons un ensemble de fonctions pures qui n'ont pas d'effets de bord, alors l'ordre dans lequel elles sont exécutées devient sans importance.

Disons que nous avons une fonction qui appelle 3 fonctions pures en interne :

**Java**

```
void doThings() {    doThing1();    doThing2();    doThing3();}
```

**Kotlin**

```
fun doThings() {    doThing1()    doThing2()    doThing3()}
```

Nous savons avec certitude que ces fonctions ne dépendent pas les unes des autres (puisque la sortie de l'une n'est pas l'entrée de l'autre) et nous savons également qu'elles ne changeront rien dans le système (puisqu'elles sont pures). Cela rend l'ordre dans lequel elles sont exécutées complètement interchangeable.

L'ordre d'exécution peut être réorganisé et optimisé pour des fonctions pures indépendantes. Notez que si l'entrée de _doThing2()_ était le résultat de _doThing1()_, alors celles-ci devraient être exécutées dans l'ordre, mais _doThing3()_ pourrait toujours être réorganisée pour s'exécuter avant _doThing1()_.

Qu'est-ce que cette propriété d'ordre nous apporte ? _La concurrence_, c'est ça ! Nous pouvons exécuter ces fonctions sur 3 cœurs CPU séparés sans nous soucier de tout gâcher !

Dans de nombreux cas, les compilateurs dans les langages fonctionnels purs avancés comme [Haskell](https://www.haskell.org/) peuvent déterminer en analysant formellement votre code s'il est concurrent ou non, et peuvent vous empêcher de vous tirer une balle dans le pied avec des interblocages, des conditions de course et autres. Ces compilateurs peuvent théoriquement également auto-paralléliser votre code (cela n'existe pas réellement dans aucun compilateur que je connaisse pour le moment, mais la recherche est en cours).

Même si votre compilateur ne regarde pas tout cela, en tant que programmeur, c'est génial de pouvoir dire si votre code est concurrent simplement en regardant les signatures des fonctions et d'éviter les bugs de threading désagréables en essayant de paralléliser du code impératif qui pourrait être rempli d'effets de bord cachés.

### Résumé

J'espère que cette première partie vous a intrigué à propos de la PF. Les fonctions pures, sans effets de bord, rendent le code beaucoup plus facile à comprendre et sont la première étape pour atteindre la concurrence.

Avant d'en arriver à la concurrence, nous devons apprendre l'_immuabilité_. Nous ferons exactement cela dans la partie 2 de cette série et verrons comment les fonctions pures et l'immuabilité peuvent nous aider à écrire du code concurrent simple et facile à comprendre sans recourir à des verrous et des mutex.

#### Lire la suite

[**Programmation Fonctionnelle pour les Développeurs Android — Partie 2**](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-2-5c0834669d1a)
[_Si vous n'avez pas lu la partie 1, veuillez la lire ici : medium.com_](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-2-5c0834669d1a)

_Si vous avez aimé cela, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux._

_Pour plus de réflexions sur la programmation, suivez-moi pour être informé lorsque j'écrirai de nouveaux articles._