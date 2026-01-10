---
title: Comment rendre vos animations Kotlin Android accessibles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T18:42:52.000Z'
originalURL: https://freecodecamp.org/news/accessible-a11y-kotlin-android-animations-7432bd23e395
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rkl9NhRSxPALXM13Fy4AXw.png
tags:
- name: Accessibility
  slug: accessibility
- name: Android
  slug: android
- name: Kotlin
  slug: kotlin
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment rendre vos animations Kotlin Android accessibles
seo_desc: 'By Dominic Fraser

  When researching examples for a first ever Android contribution, few examples existed
  for animations written in Kotlin. There were also few code examples of accessibility
  considerations within native animations.

  So here we go! Let’s...'
---

Par Dominic Fraser

Lors de la recherche d'exemples pour une première contribution Android, peu d'exemples existaient pour les animations écrites en Kotlin. Il y avait également peu d'exemples de code prenant en compte l'accessibilité dans les animations natives.

Alors c'est parti ! Examinons comment écrire une animation native 'expand' en Kotlin, et parlons de la manière d'aider ceux qui utilisent TalkBack ou un texte agrandi. Tout le code est disponible dans ce [dépôt d'exemple](https://github.com/dominicfraser/AnimationDemo), créant une seule activité avec une vue animée à l'intérieur. Le code sur lequel cela est basé a été co-écrit avec [Calum Turner](https://medium.com/@cajturner).

![Image](https://cdn-media-1.freecodecamp.org/images/DOxMse7xYjykVvHccIUtbKKFWD4NM69jIK9J)
_GIF du résultat final de l'application_

### Accessibilité Android (a11y)

Tous les appareils Android sont équipés d'un lecteur d'écran intégré nommé TalkBack. Celui-ci peut être activé depuis les paramètres de l'appareil et dispose également d'un guide d'utilisation pour la première fois. Des gestes sont utilisés pour naviguer autour de la page, avec des descriptions des éléments focalisés lues à voix haute. Sans cela, une application devient inutilisable pour de nombreux utilisateurs malvoyants.

Il est particulièrement important que les éléments corrects soient focalisables, aient des descriptions et que les changements de vue soient annoncés.

Dans le même menu des paramètres, la taille de base de la police par défaut peut être ajustée, avec une mise à l'échelle à partir de 1.0. Les vues doivent réagir à ce changement de taille de police, avec tous les éléments toujours présents et fonctionnels.

### Mise en page

Nous ne regarderons pas les spécificités de style de la mise en page ici car elles sont assez uniques à cet exemple, mais les touches d'accessibilité valent la peine d'être mises en évidence.

Deux propriétés sont utilisées : `android:contentDescription` et `android:importantForAccessibility`.

La `contentDescription` est ce qui est lu lorsqu'un élément obtient le focus. Pour toute ImageView qui obtient le focus, cela est essentiel, sinon un lecteur d'écran lira plutôt l'inutile 'unlabelled' à l'utilisateur.

Si cela était un bouton, il lirait '<description> bouton, double tap pour activer' par défaut, mais pour notre icône ImageView, nous spécifions manuellement l'action car nous n'avons pas ce comportement par défaut.

```
android:contentDescription="appuyez pour basculer les informations supplémentaires sur la personne"
```

Nous utilisons également `importantForAccessibility:no` pour désactiver le focus pour le TextView '+', car le texte sous les deux badges fournit une description et donc le '+' est plus confus que utile s'il est lu à voix haute.

Pour ces deux cas, le test manuel sur un appareil réel avec TalkBack activé est la meilleure indication pour savoir si le contexte a du sens sans les visuels.

### Animation d'expansion

Notre animation s'activera lors d'un appui sur une icône 'info', basculant l'expansion d'une section de détails.

Nous allons faire tout cela à l'intérieur d'une seule activité pour permettre de se concentrer simplement sur le code de l'animation. Dans une application réelle, la vue à laquelle cela est appliqué est plus susceptible d'être dans son propre fragment ou vue recyclée, donc une structure de code plus abstraite serait utilisée.

#### Définir un écouteur

Dans le `onCreate` de notre activité d'exemple, nous devons d'abord définir un écouteur sur notre icône et passer la vue qui doit être basculée.

```
infoIcon.setOnClickListener { toggleCardBody(root.personEntryBody) }
```

Nous définissons également une variable dans la classe pour suivre si la vue est basculée, en la définissant initialement comme fermée.

```
private var isToggled = false
```

#### Basculer l'animation d'expansion

Dans notre mise en page, nous avons défini la hauteur de `personEntryBody` à `0dp`.

Pour basculer cela en ouvert, nous devons connaître la nouvelle hauteur à définir, la durée de l'animation et la hauteur qu'elle doit avoir à chaque moment de l'animation.

Nous devons ensuite définir `isToggled` à son inverse et nous assurer que lorsqu'on appuie à nouveau, il fait l'inverse.

```kotlin
private fun toggleCardBody(body: View) {
    body.measure(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT)
    val maxHeight = body.measuredHeight + body.paddingTop + body.paddingBottom
    val startHeight = if (isToggled) maxHeight else 0
    val targetHeight = if (isToggled) 0 else maxHeight

    val expandAnimator = ValueAnimator
        .ofInt(startHeight, targetHeight)
        .setDuration(200)
    
    expandAnimator.addUpdateListener {
        val value = it.animatedValue as Int
        body.layoutParams.height = value
        body.requestLayout()
    }

    expandAnimator.doOnEnd {
        isToggled = !isToggled
    }

    expandAnimator.start()
}
```

Comme la hauteur lorsque la vue est initialement dessinée est 0, nous devons calculer sa nouvelle taille en remesurant sa mise en page.

Comme décrit dans la [documentation sur la mise en page des vues Android](https://developer.android.com/reference/android/view/View.html#layout), nous pouvons utiliser `measure()` avec les paramètres de mise en page que nous avons assignés à la vue pour remesurer chaque fois que l'icône d'information est appuyée.

Pour calculer la hauteur maximale, nous devons ajouter manuellement le remplissage supérieur et inférieur à cela, car ceux-ci ne sont pas inclus dans la hauteur mesurée.

Selon `isToggled`, nous savons si nous commençons à partir de 0 ou si nous commençons à partir de la hauteur maximale développée, et donc la hauteur cible opposée.

Nous utilisons un Value Animator pour passer de la valeur de départ à la valeur de fin cible, et définissons la durée en ms. Cette durée est basée purement sur des tests manuels ultérieurs pour le ressenti UX.

```kotlin
ValueAnimator
        .ofInt(startHeight, targetHeight)
        .setDuration(200)
```

Nous lions la durée à la hauteur avec un écouteur de mise à jour, demandant une nouvelle mise en page à dessiner après chaque mise à jour et ajustant la hauteur à chaque fois.

```kotlin
    expandAnimator.addUpdateListener {
        val value = it.animatedValue as Int
        body.layoutParams.height = value
        body.requestLayout()
    }

    expandAnimator.doOnEnd {
        isToggled = !isToggled
    }

    expandAnimator.start()
```

Comme nous utilisons Kotlin, nous ajoutons également la bibliothèque `[androidx](https://developer.android.com/kotlin/ktx#core-packages)` à notre `build.gradle` pour bénéficier de son extension `doOnEnd`. Cela nous permet d'inverser très facilement la variable `isToggled`.

Enfin, nous démarrons notre animation ! Nous avons déjà un corps qui s'étend et se contracte au toucher d'une icône !

#### Animations plus fluides

Bien que notre animation fonctionne techniquement telle quelle, une belle étape supplémentaire est d'ajouter un [interpolateur](https://thoughtbot.com/blog/android-interpolators-a-visual-guide) pour que le mouvement paraisse plus naturel.

```
expandAnimator.interpolator = FastOutSlowInInterpolator()
```

#### Améliorer notre accessibilité

Nous ajouterons deux dernières choses pour aider nos utilisateurs a11y.

Tout d'abord, nous pouvons aider à la navigation en utilisant un `[AccessibilityEvent](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent)`.

```kotlin
expandAnimator.doOnEnd {
    if (!isToggled)       body.sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_FOCUSED)
    isToggled = !isToggled
}
```

Cela signifie que lorsque l'animation passe de fermée à ouverte, le focus sautera immédiatement sur le premier élément du corps, dans ce cas la description. Dans la mise en page, nous définissons la description de l'action de l'icône d'information, mais comme nous ne pouvons pas nous fier à un indicateur visuel pour que l'utilisateur passe à l'élément suivant, nous pouvons gérer cela pour eux.

Ensuite, nous permettons différentes tailles de police. La hauteur mesurée retournée par `measure()` ne tient pas compte de la mise à l'échelle de la police définie dans les paramètres d'accessibilité de l'appareil, et donc lorsque la mise à l'échelle est grande, le bas de la description sera rogné car il est trop grand pour tenir.

Nous pouvons accéder à l'échelle de la police par programmation et mettre à l'échelle notre hauteur en fonction de cela. Nous la convertissons en entier car l'échelle de la police peut entraîner un flottant qui ne fonctionnerait pas comme une hauteur de mise en page.

```kotlin
val a11yFontScale = body.context.resources.configuration.fontScale
val maxHeight = ((body.measuredHeight + body.paddingTop + body.paddingBottom) * a11yFontScale).toInt()
```

### Terminé !

![Image](https://cdn-media-1.freecodecamp.org/images/hc7stdBCduA51zMGn0t2GuKzEjPTWNufj8jP)
_GIF du résultat final de l'application_

Et voilà, nous avons arrivé à notre animation finale ! Avec juste quelques lignes supplémentaires, nous avons grandement augmenté sa couverture a11y et avons une section d'expansion fluide révélant un badge Kotlin et Android 🏆

Merci d'avoir lu 😊

Voici quelques autres choses que j'ai écrites récemment :

* [Personnalisation des tests E2E CodeceptJS](https://codeburst.io/customising-codeceptjs-e2e-tests-1a2bf5f32f51?source=friends_link&sk=767140b587a6efd9d71f9e06c5dc3c4b)
* [Tester React avec Jest et Enzyme II](https://codeburst.io/testing-react-events-with-jest-and-enzyme-ii-46fbe4b8b589?source=friends_link&sk=e5e9c600c79cdac7fae802add95ff17d)

### Extras utiles

* [Joe Birch](https://www.freecodecamp.org/news/accessible-a11y-kotlin-android-animations-7432bd23e395/undefined) a écrit un excellent article sur androidx concernant [Exploring KTX for Android](https://medium.com/exploring-android/exploring-ktx-for-android-13a369795b51)
* [Tutoriel sur l'accessibilité Android : Getting Started](https://www.raywenderlich.com/240-android-accessibility-tutorial-getting-started)