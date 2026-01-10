---
title: Comment ajouter des animations de balayage à une CardView dans une application
  Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-15T16:09:53.000Z'
originalURL: https://freecodecamp.org/news/add-swipe-animations-to-a-card-view-in-android-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Swiping-Animation-Android-Views.gif
tags:
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: animation
  slug: animation
- name: animations
  slug: animations
- name: Kotlin
  slug: kotlin
seo_title: Comment ajouter des animations de balayage à une CardView dans une application
  Android
seo_desc: "By Gourav Khunger\nIf you're building an Android app, you should consider\
  \ adding animations. They can improve your app's user experience and increase retention.\
  \ \nThese days, if you see an app that has no animation, it can feel odd and out-dated.\
  \ And s..."
---

Par Gourav Khunger

Si vous développez une application Android, vous devriez envisager d'ajouter des animations. Elles peuvent améliorer l'expérience utilisateur de votre application et augmenter la rétention. 

De nos jours, si vous voyez une application sans animation, cela peut sembler étrange et dépassé. Et puisque les expériences interactives sont devenues la nouvelle norme, vous voudrez trouver des moyens de distinguer votre application.

## Ce que nous allons construire ici

Maintenant, il peut sembler difficile de faire ressortir votre application si vous avez quelque chose de basique comme une application de partage de citations (ce sur quoi nous allons travailler ici). Il peut être difficile d'accrocher l'utilisateur et de maintenir son intérêt.

Bien sûr, vous pourriez simplement ajouter deux boutons simples pour charger la citation suivante/précédente et en rester là. Mais c'est assez basique et n'importe quelle application pourrait le faire ! Même si vous construisez simplement un projet secondaire simple, il n'y a pas de compromis pour une bonne UX :)

Ce que nous allons faire dans ce tutoriel, c'est supprimer les boutons et avoir une logique où un utilisateur peut balayer la carte vers la gauche. Lorsqu'ils ont balayé suffisamment loin, l'application chargera une nouvelle carte avec une nouvelle citation.

À la fin de cet article, vous aurez appris comment créer une carte animée très fluide que l'utilisateur peut balayer et qui peut effectuer l'action de votre choix. Voici une démonstration de son fonctionnement :

![Animation montrant un balayage fluide pour actualiser l'animation sur une CardView Android.](https://www.freecodecamp.org/news/content/images/2021/11/iHxFjvI4x.gif)

Incroyable, n'est-ce pas ? Commençons !

## Prérequis

Pour ce tutoriel, nous utiliserons Kotlin comme langage de programmation pour notre application – mais vous pouvez facilement traduire le code en Java et cela fonctionnera de la même manière.

Pour référence, voici la carte de citation sur laquelle nous souhaitons activer la fonction de balayage.

![Vue de carte Android avec une citation.](https://www.freecodecamp.org/news/content/images/2021/11/9CVHyoJfV.png)

Il s'agit d'une `CardView` androidX avec un ensemble de `TextView` et une `ImageView`. Il y a aussi une `ProgressBar` qui s'affiche pendant le chargement d'une nouvelle citation.

Nous ne créerons pas le code XML pour l'interface utilisateur. Vous pouvez [obtenir la mise en page](https://github.com/gouravkhunger/QuotesApp/blob/main/app/src/main/res/layout/fragment_quote.xml) que j'ai utilisée ici depuis le dépôt GitHub, ou créer la vôtre.

[Voici le code complet](https://github.com/gouravkhunger/QuotesApp) de notre application Quotes, si vous souhaitez le consulter. Elle utilise le modèle de conception MVVM, mais cet article ne dépend pas du modèle que vous utilisez pour la logique métier de votre application, car nous travaillerons uniquement sur la partie UI.

Maintenant, nous sommes prêts à créer cette interface de balayage géniale !

## Comment gérer les balayages dans notre application

Pour gérer les balayages, nous devons d'abord définir un écouteur de toucher sur la carte. Chaque fois qu'une action est effectuée sur la carte, l'écouteur de toucher est appelé. Dans l'écouteur, nous ajouterons la logique pour effectuer les calculs et les animations.

Voici le schéma de l'écouteur de toucher que nous allons utiliser :

```kotlin
quoteCard.setOnTouchListener(
    View.OnTouchListener { view, event ->
        when (event.action) {
            MotionEvent.ACTION_MOVE -> {
            	// TODO: Gérer ACTION_MOVE
            }
            MotionEvent.ACTION_UP -> {
            	// TODO: Gérer ACTION_UP
            }
        }

        // requis pour contourner l'avertissement lint
        view.performClick()
        return@OnTouchListener true
    }
)
```

Ici, nous écoutons spécifiquement 2 actions sur la carte – `ACTION_MOVE` et `ACTION_UP`.

* L'événement `ACTION_MOVE` est appelé lorsque l'utilisateur commence à balayer la carte, c'est-à-dire à la déplacer.
* `ACTION_UP` est appelé lorsque l'utilisateur lève le doigt de la carte, c'est-à-dire lorsqu'il la relâche.

Il existe de nombreux autres événements d'action que nous pouvons remplacer, tels que `ACTION_DOWN` qui est appelé lorsqu'une personne prend la vue, mais nous n'en avons pas besoin pour cette fonctionnalité.

La configuration de base de la carte est terminée, alors déterminons la logique de balayage.

### Les mathématiques derrière l'action de balayage

Tout d'abord, repensons **ce que nous voulons réaliser**. La mise en œuvre de la fonctionnalité est plus facile lorsque vous savez exactement ce que vous souhaitez avoir. Votre code aura également plus de sens lorsque vos exigences sont claires.

Ici, nous avons une carte de citation. Nous voulons que les utilisateurs puissent la balayer uniquement vers la gauche, et si le seuil minimum pour charger une nouvelle citation est atteint, elle doit revenir à sa position d'origine et charger une nouvelle citation.

Maintenant, pour y parvenir, pensons en termes de carte. Définissons la position moyenne comme le centre de la carte.

![Position moyenne de la carte de citation](https://www.freecodecamp.org/news/content/images/2021/11/dEnpWr7e4.png)
_Position moyenne de la carte_

Nous voulons que la carte soit balayée si et seulement si l'utilisateur la balaye vers la gauche de la position moyenne.

![Animation illustrant l'utilisateur balayant vers la gauche de la carte de citation](https://www.freecodecamp.org/news/content/images/2021/11/7epeWn53S.gif)
_Balayage uniquement si déplacé vers la gauche de la position moyenne_

Alors, comment pouvons-nous faire en sorte que cela se produise ? 

Vous l'avez deviné – nous allons calculer la position moyenne et lors de l'événement `ACTION_MOVE`, nous vérifierons si l'utilisateur a balayé vers la gauche et déplacerons la carte en conséquence.

### Comment implémenter la logique de balayage

Pour implémenter la logique, nous devons d'abord avoir la position de départ de la carte, ce qui est assez facile à calculer. Nous veillerons simplement à ce qu'elle soit calculée par rapport à la largeur de l'écran complet, et non seulement à la largeur de la carte.

Placez ces lignes de code avant l'instruction `when(event.action)` :

```kotlin
quoteCard.setOnTouchListener(
    View.OnTouchListener { view, event ->
    
        // variables pour stocker la configuration actuelle de la carte de citation.
        val displayMetrics = resources.displayMetrics
        val cardWidth = quoteCard.width
        val cardStart = (displayMetrics.widthPixels.toFloat() / 2) - (cardWidth / 2)

        when (event.action) {
        	...
        }
        ...
    }
)
```

Tout d'abord, nous obtenons les `displayMetrics` à partir des ressources, ce qui nous donnera la largeur de l'écran en utilisant `displayMetrics.widthPixels.toFloat()`.

Ensuite, nous obtenons la `cardWidth` en utilisant la propriété `width` de la `quoteCard`.

Enfin, nous calculons la position de départ de la carte en utilisant la formule `(largeur de l'écran/2) - (cardWidth/2)`. Essentiellement, cela nous donne la coordonnée x de cette position de la carte :

![Animation mettant en évidence la position de départ de la carte de citation](https://www.freecodecamp.org/news/content/images/2021/11/NiH3lsseM.gif)
_Position de départ de la carte._

Maintenant, implémentons le code pour l'événement `ACTION_MOVE`.

### Comment gérer l'événement `ACTION_MOVE`

À l'intérieur du bloc `ACTION_MOVE`, nous initialisons d'abord la variable `newX` qui contient la nouvelle coordonnée x vers laquelle la carte a été balayée.

```kotlin
val newX = event.rawX

```

`event.rawX` nous donne la valeur absolue de la nouvelle coordonnée par rapport à la largeur de l'écran.

`newX` contiendra la coordonnée x où se trouve le doigt de l'utilisateur, à tout moment donné. La valeur `0.0` pour `newX` signifie que l'utilisateur a balayé vers la partie la plus à gauche de l'écran. Et pour mon émulateur, `1080.0` représente le bord le plus à droite de l'écran.

Puisque nous voulons que la carte soit balayée uniquement si `newX` est inférieur à la position moyenne de la carte, nous placerons une condition si ici pour vérifier que c'est le cas.

Pensez à cela avec des valeurs simples. Supposons que la position moyenne de la carte soit à la coordonnée x `540.0` (petite coordonnée x) et que l'utilisateur balaye vers `710.0` (coordonnée x plus grande). Mais nous ne voulons pas qu'ils puissent balayer vers la droite. Et si l'utilisateur balaye vers `320.0` (coordonnée x plus petite), alors nous devons effectuer le balayage et déplacer la carte vers la nouvelle position.

Voici le code pour implémenter la logique ci-dessus :

```kotlin
if (newX - cardWidth < cardStart) { // ou newX < cardStart + cardWidth
    quoteCard.animate().x(
        min(cardStart, newX - (cardWidth / 2))
    )
    .setDuration(0)
    .start()
}

```

Nous soustrayons `cardWidth` de `newX` car `newX` est une valeur absolue qui n'est pas relative à la carte. Elle a une valeur plus élevée car `cardStart` est vers le début de l'écran, et `newX` est initialement quelque part au milieu (un utilisateur balayerait généralement depuis le milieu).

Nous voulons comparer la valeur du **déplacement** dans la coordonnée x et la médiane à la valeur de `cardStart`, et non à la valeur de **`newX`**, nous en tenons donc compte en soustrayant `cardWidth`.

Ensuite, nous effectuons l'animation en utilisant `quoteCard.animate()` et nous changeons sa coordonnée x en utilisant la fonction `x()`.

Maintenant, pourquoi faisons-nous `min(cardStart, newX - (cardWidth/2))` ?

C'est très intéressant et intuitif à comprendre. Dès le début, nous insistons sur le fait que la carte doit se déplacer uniquement vers la gauche et non vers la droite. 

`newX - (cardWidth/2))` n'est rien d'autre que la distance balayée vers la gauche (donc la soustraction est impliquée – pour le côté droit, elle devrait être ajoutée).

La fonction `min()` ici retourne le minimum des deux valeurs fournies. Si la distance balayée est inférieure à `cardStart`, elle est retournée, sinon `cardStart` est utilisée. C'est la condition que nous voulons remplir et `min()` la rend vraiment facile à gérer.

`setDuration(0)` garantit que l'animation est effectuée instantanément (ce qui évite que le balayage ne semble saccadé). `start()` démarre réellement l'animation avec les propriétés données.

Cette animation dissipera tout doute que vous pourriez avoir sur son fonctionnement :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/other.gif)
_Visualisation du concept mentionné précédemment_

(Je n'ai pas d'expertise dans la création d'animations, c'est le meilleur que j'ai pu faire.)

Voici le code final pour l'événement `ACTION_MOVE` :

```kotlin
MotionEvent.ACTION_MOVE -> {
    // obtenir la nouvelle coordonnée de l'événement sur l'axe X
    val newX = event.rawX

    // effectuer le balayage uniquement si newX - cardWidth < cardStart, c'est-à-dire
    // la carte est balayée vers le côté gauche, pas vers le côté droit
    if (newX - cardWidth < cardStart) {
        quoteCard.animate()
            .x(
                min(cardStart, newX - (cardWidth / 2))
            )
        .setDuration(0)
        .start()
    }
}

```

Vous pouvez également inclure un `TextView` dans l'interface utilisateur qui reflète quand l'utilisateur doit relâcher la carte. Placez ce code à l'intérieur de l'instruction `if` ci-dessus également :

```kotlin
if (quoteCard.x < MIN_SWIPE_DISTANCE) textView.text = getString(R.string.releaseCard)
else textView.text = getString(R.string.infoText)

```

où `MIN_SWIPE_DISTANCE` est `-250` :

```kotlin
// -250 produit le meilleur résultat, n'hésitez pas à changer selon vos préférences
const val MIN_SWIPE_DISTANCE = -250 // L'utilisateur doit déplacer au moins -250 depuis la position moyenne pour charger une nouvelle citation

```

Maintenant, l'événement `ACTION_MOVE` est géré correctement. Écrivons le code pour gérer l'événement `ACTION_UP`, c'est-à-dire lorsque la carte est relâchée.

### Comment gérer l'événement `ACTION_UP`

Pour l'événement `ACTION_UP`, nous voulons que la carte revienne à sa position d'origine, attende environ `100` millisecondes, puis charge une nouvelle citation.

La logique pour animer la carte est similaire, mais cette fois nous allons faire en sorte que la durée de l'animation soit d'environ `150` millisecondes pour la rendre fluide.

Tout d'abord, créez une variable `currentX` qui contient la valeur actuelle de la coordonnée x de la carte de citation. Nous utiliserons cette variable plus tard.

```kotlin
var currentX = quoteCard.x

```

Ensuite, démarrez l'animation sur la carte. Passez la variable `cardStart` à la fonction `x()` pour la faire revenir à sa position d'origine et définissez la durée à `150`.

```kotlin
quoteCard.animate()
    .x(cardStart)
    .setDuration(150)
// continuation ci-dessous

```

Cette fois, nous définissons un écouteur sur l'animation. Un écouteur est quelque chose qui surveille l'animation. En l'utilisant, nous pouvons effectuer des actions sur divers événements d'animation tels que le démarrage, la fin, la reprise, et plus encore.

```kotlin
// continuation
.setListener(
    object : AnimatorListenerAdapter() {
        override fun onAnimationEnd(animation: Animator) {
            viewLifecycleOwner.lifecycleScope.launch(Dispatchers.Default) {
                delay(100)
                // vérifier si la distance de balayage était supérieure à
                // le balayage minimum requis pour charger une nouvelle citation
                if (currentX < MIN_SWIPE_DISTANCE) {
                    // Ajouter la logique pour charger une nouvelle citation si balayé de manière adéquate
                    viewModel.getRandomQuote()
                    currentX = 0f
                }
            }
        }
    }
)
.start()

```

Nous définissons un écouteur pour surveiller la fin de l'animation en remplaçant la fonction `onAnimationEnd()`. 

Dès que l'animation se termine, nous lançons une coroutine (similaire aux Threads en Java mais beaucoup plus efficace) avec un délai de 100 millisecondes. Elle vérifie ensuite si l'utilisateur avait balayé plus loin que la `MIN_SWIPE_DISTANCE` nécessaire pour charger une nouvelle citation. La variable `currentX` est utilisée pour la comparaison ici.

Si l'utilisateur balaye effectivement en dépassant la distance minimale, la coroutine est retardée de `100` millisecondes. Ensuite, le modèle de vue charge une nouvelle citation aléatoire depuis l'API, réinitialisant également la variable `currentX` à `0f`.

Le code final pour l'événement `ACTION_UP` ressemble à ceci :

```kotlin
MotionEvent.ACTION_UP -> {
    var currentX = quoteCard.x
    quoteCard.animate()
        .x(cardStart)
        .setDuration(150)
        .setListener(object : AnimatorListenerAdapter() {
            override fun onAnimationEnd(animation: Animator) {
                viewLifecycleOwner.lifecycleScope.launch(Dispatchers.Default) {
                    delay(100)
                    // vérifier si la distance de balayage était supérieure à
                    // le balayage minimum requis pour charger une nouvelle citation
                    if (currentX < MIN_SWIPE_DISTANCE) {
                    	// Ajouter la logique pour charger une nouvelle citation si balayé de manière adéquate
                        viewModel.getRandomQuote()
                        currentX = 0f
                    }
                }
            }
        })
        .start()
    textView.text = getString(R.string.infoText)
}

```

## Code final

Voici le code final pour le `onTouchListener()` complet :

```kotlin
quoteCard.setOnTouchListener(
    View.OnTouchListener { v, event ->

        // variables pour stocker la configuration actuelle de la carte de citation.
        val displayMetrics = resources.displayMetrics
        val cardWidth = quoteCard.width
        val cardStart = (displayMetrics.widthPixels.toFloat() / 2) - (cardWidth / 2)

        when (event.action) {
            MotionEvent.ACTION_UP -> {
                var currentX = quoteCard.x
                quoteCard.animate()
                    .x(cardStart)
                    .setDuration(150)
                    .setListener(
                        object : AnimatorListenerAdapter() {
                            override fun onAnimationEnd(animation: Animator) {
                                viewLifecycleOwner.lifecycleScope.launch(Dispatchers.Default) {
                                    delay(100)

                                    // vérifier si la distance de balayage était supérieure à
                                    // le balayage minimum requis pour charger une nouvelle citation
                                    if (currentX < MIN_SWIPE_DISTANCE) {
                                        // Ajouter la logique pour charger une nouvelle citation si balayé de manière adéquate
                                        viewModel.getRandomQuote()
                                        currentX = 0f
                                    }
                                }
                            }
                        }
                    )
                    .start()
                textView.text = getString(R.string.infoText)
            }
            MotionEvent.ACTION_MOVE -> {
                // obtenir la nouvelle coordonnée de l'axe X
                val newX = event.rawX

                // effectuer le balayage uniquement si newX < cardStart, c'est-à-dire,
                // la carte est balayée vers le côté gauche, pas vers le côté droit
                if (newX - cardWidth < cardStart) {
                    quoteCard.animate()
                        .x(
                            min(cardStart, newX - (cardWidth / 2))
                        )
                        .setDuration(0)
                        .start()
                    if (quoteCard.x < MIN_SWIPE_DISTANCE) 
                        textView.text = getString(R.string.releaseCard)
                    else textView.text = getString(R.string.infoText)
                }
            }
        }

        // requis pour contourner l'avertissement lint
        v.performClick()
        return@OnTouchListener true
    }
)
```

Félicitations ! Dans ce tutoriel, nous avons implémenté une animation qui permet à un utilisateur de balayer une carte contenant une citation pour obtenir une nouvelle citation.

N'oubliez pas de télécharger l'application et de la tester vous-même. Les étoiles et les contributions sur le [dépôt GitHub](https://github.com/gouravkhunger/QuotesApp) sont les bienvenues !

## Conclusion

Maintenant, vous avez appris comment animer une carte et gérer les écouteurs d'animation sur celle-ci. Cela aide à créer une meilleure UX qui fait ressortir votre application.

En utilisant les connaissances que vous avez acquises dans cet article, vous pouvez maintenant créer la plupart des animations suivantes pour les vues dans Android :

* **Créer des animations de glissement pour les vues Android de manière programmatique.**

Tout comme nous l'avons fait dans ce tutoriel.

* **Animation de gauche à droite**

C'est assez simple, il suffit de transformer la soustraction dans les variables en addition et les signes `<` dans les instructions `if` en signes `>`. Avec ces quelques ajustements ici et là, les animations de droite à gauche dans la vue de carte peuvent être transformées en animations de gauche à droite !

* **Vous pouvez également afficher et masquer des vues en utilisant des animations.**

Pour cela, vous devez suivre la position de départ et la position de fin, puis les animer avec `alpha()` de `0` à `1`. Pour un exemple, vous pouvez vous référer à ma bibliothèque [Accolib](https://github.com/gouravkhunger/AccoLib) pour créer des accordéons FAQ animés.

* **Les changements de mise en page animés de base peuvent être réalisés avec des animations de vue.**

Merci beaucoup d'avoir lu jusqu'ici, j'espère que cet article a ajouté de la valeur. Abonnez-vous à ma newsletter sur [Genics Blog](https://genicsblog.com) pour rester informé de mes futurs articles !