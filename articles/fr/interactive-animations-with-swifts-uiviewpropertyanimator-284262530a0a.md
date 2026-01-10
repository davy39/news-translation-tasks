---
title: Comment implémenter des animations interactives avec UIViewPropertyAnimator
  de Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T17:19:36.000Z'
originalURL: https://freecodecamp.org/news/interactive-animations-with-swifts-uiviewpropertyanimator-284262530a0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3Xnoeplkg9w7hqZxuFIuLw.png
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment implémenter des animations interactives avec UIViewPropertyAnimator
  de Swift
seo_desc: 'By Trevor Phillips

  Let’s scrap the ugly UIView.animate(…) code and give it an upgrade, shall we?

  Here we’ll dive into a practical example using Apple’s UIViewPropertyAnimator to
  create smooth animations combined with user interaction.

  You can check o...'
---

Par Trevor Phillips

Abandonnons le code peu élégant `UIView.animate()` et donnons-lui une mise à niveau, d'accord ?

Ici, nous allons plonger dans un exemple pratique utilisant `UIViewPropertyAnimator` d'Apple pour créer des animations fluides combinées avec l'interaction utilisateur.

Vous pouvez consulter le résultat final de ces animations dans l'application gratuite [Bloq](https://apple.co/2v6dujl), qui utilise les techniques décrites ci-dessous comme base pour le gameplay.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MUioYOxvdIlmQCUt8Wuuzw.gif)
_Animations utilisant UIViewPropertyAnimator_

### Contexte

C'est une classe introduite dans iOS 10 qui offre plus de capacités que les fonctions traditionnelles `UIView.animate(...)` :

* Démarrer, arrêter, mettre en pause ou reprendre l'animation de manière programmatique à tout moment
* Ajouter des blocs d'animation et des blocs de complétion à l'animateur à votre guise
* Inverser l'animation à tout moment
* "Scrubber" l'animation, c'est-à-dire, définir de manière programmatique à quel point elle doit être avancée maintenant

### Mise en route

Tout d'abord, nous allons définir un contrôleur de vue personnalisé `BlockViewController` qui représentera chaque carré coloré dans le jeu. _Note_ : Je n'inclus pas le code pour les couleurs, les coins arrondis ou d'autres aspects qui ne sont pas pertinents pour ce tutoriel.

```
class BlockViewController: UIViewController {    var startingXOffset: CGFloat = 0    var endingXOffset: CGFloat = 0    var startingYOffset: CGFloat = 0    var endingYOffset: CGFloat = 0
```

```
    var topConstraint = NSLayoutConstraint()    var leadingConstraint = NSLayoutConstraint()
```

```
    var animationDirection: AnimationDirection = .undefined    var isVerticalAnimation: Bool {        return animationDirection == .up            || animationDirection == .down    }    var transitionAnimator: UIViewPropertyAnimator?    var animationProgress: CGFloat = 0}
```

Les propriétés `topConstraint` et `leftConstraint` définissent le décalage de la vue du contrôleur de vue par rapport aux côtés supérieur et gauche de sa supervue (respectivement).

Les propriétés `offset` sont utilisées par `UIViewPropertyAnimator` pour déterminer où l'animation doit commencer et où elle doit se terminer. Puisque les blocs dans le jeu peuvent se déplacer à la fois à gauche/droite et haut/bas, nous définissons à la fois les décalages `X` et `Y`.

Nous avons également une simple énumération `AnimationDirection` pour aider à la logique nécessaire pour les animations.

```
enum AnimationDirection: Int {    case up, down, left, right, undefined}
```

Maintenant, dans la fonction `viewDidLoad()` du contrôleur de vue, nous pouvons configurer les contraintes comme ceci :

```
topConstraint = view.topAnchor.constraint(equalTo: superview.topAnchor, constant: startingYOffset)
```

```
leadingConstraint = view.leadingAnchor.constraint(equalTo: superview.leadingAnchor, constant: startingXOffset)
```

```
topConstraint.isActive = true
```

```
leadingConstraint.isActive = true
```

```
let recognizer = UIPanGestureRecognizer()
```

```
recognizer.addTarget(self, action: #selector(viewPanned(recognizer:))) // sera défini plus tard !
```

```
view.addGestureRecognizer(recognizer)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JdV9LVgcCFp9BJynQf-EwA.png)

#### Fonctions d'assistance

Configurons également quelques fonctions "d'assistance" qui seront utiles plus tard. Les fonctions suivantes échangeront les valeurs de décalage :

```
private func swapXConstraints() {    let tmp = endingXOffset    endingXOffset = startingXOffset    startingXOffset = tmp}
```

```
private func swapYConstraints() {    let tmp = endingYOffset    endingYOffset = startingYOffset    startingYOffset = tmp}
```

Celle-ci sera utile pour réinitialiser l'animation :

```
private func nullifyAnimations() {    transitionAnimator = nil    animationDirection = .undefined}
```

Et voici une fonction pour inverser l'animateur :

```
private func reverseAnimation() {    guard let animator = transitionAnimator else { return }    animator.isReversed = !animator.isReversed}
```

Si l'animation est _déjà_ en cours d'exécution et que `isReversed` est `true`, alors nous savons que l'animation est en cours d'exécution dans la direction inversée. Si l'animation n'est _pas_ en cours d'exécution et que `isReversed` est `true`, l'animation s'exécutera dans la direction inversée lorsqu'elle sera démarrée.

Enfin, cette petite fonction prend `velocity` représentée comme un `CGPoint`, et détermine quelle direction, le cas échéant, l'animation doit prendre en fonction de la composante x ou y de la vitesse qui est la plus grande en magnitude :

```
private func directionFromVelocity(_ velocity: CGPoint) -> AnimationDirection {    guard velocity != .zero else { return .undefined }    let isVertical = abs(velocity.y) > abs(velocity.x)    var derivedDirection: AnimationDirection = .undefined    if isVertical {        derivedDirection = velocity.y < 0 ? .up : .down    } else {        derivedDirection = velocity.x < 0 ? .left : .right    }    return derivedDirection}
```

### Interaction utilisateur

**Passons à l'essentiel : les animations et l'interaction utilisateur !**

Dans `viewDidLoad()`, nous avons attaché un reconnaisseur de geste de panoramique à la vue du `BlockViewController`. Ce reconnaisseur de geste appelle la fonction `viewPanned(recognizer: UIPanGestureRecognizer)` lorsque son état change.

```
@objcfunc viewPanned(recognizer: UIPanGestureRecognizer) {  switch recognizer.state {  case .began:    animationProgress = transitionAnimator?.fractionComplete ?? 0  case .changed:    didChangePan(recognizer: recognizer) // décrit ci-dessous  case .ended:    didEndPan(recognizer: recognizer) // décrit ci-dessous default:    break  }}
```

Vous vous souvenez comment j'ai mentionné la capacité de "scrubbing" de `UIViewPropertyAnimator` ? La propriété `fractionComplete` nous permet d'obtenir et de définir à quel point l'animateur doit être avancé avec ses animations. Cette valeur varie de 0.0 à 1.0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GwhivLJau6FrlhsRvhDtxg.gif)
_"Attraper" l'animation à mi-chemin_

La `animationProgress` est capturée dans `recognizer.state = .began` car nous pouvons avoir une situation comme montré ci-dessus, où un geste de panoramique est initié à mi-chemin de l'animation. Dans ce cas, nous voulons "attraper" l'animation dans son état actuel. La propriété `animationProgress` est utilisée pour permettre ce comportement d'"attrapage".

La fonction `viewPanned(recognizer: UIPanGestureRecognizer)` délègue la plupart de sa logique à deux fonctions, décrites ci-dessous. Notre code va devenir un peu plus complexe, donc pour une meilleure lisibilité et une mise en évidence de la syntaxe, je vais passer à [Github Gists](https://gist.github.com/) maintenant.

Les commentaires décrivent ce qui se passe. Notez que nous commençons réellement l'animation (si elle n'existe pas) lorsque l'état dans `viewPanned(recognizer: UIPanGestureRecognizer)` est `changed` plutôt que `began`. Cela est dû au fait que la vitesse lorsque `state = .began` est toujours nulle. Nous ne pouvons pas déterminer la direction de l'animation jusqu'à ce que la vitesse soit non nulle, d'où l'attente jusqu'à `state = .changed` pour démarrer l'animation.

Lorsque nous appelons `transitionAnimator.continueAnimation(...)` nous disons essentiellement, "D'accord animateur, l'utilisateur a terminé d'interagir, alors allez et terminez votre travail maintenant !" Passer `nil` pour le paramètre de timing et `0` pour le facteur de durée ne fera _pas_ terminer l'animation instantanément. Elle s'animera toujours en douceur jusqu'à la fin.

#### La logique, expliquée

À la fin de cette fonction, voyez-vous la variable `isOpposite` et une logique confuse concernant `animator.isReversed` ? Comprenons ce qui se passe ici.

```
private func oppositeOfInitialAnimation(velocity: CGPoint) -> Bool {    switch animationDirection {    case .up:        return velocity.y > 0    case .down:        return velocity.y < 0    case .left:        return velocity.x > 0    case .right:        return velocity.x < 0    case .undefined:        return false    }}
```

La variable `isOpposite` utilise la fonction d'assistance ci-dessus. Elle prend simplement une vitesse en entrée et retourne `true` si cette vitesse va à l'opposé de la direction actuelle de l'animation.

Ensuite, nous avons une instruction if-else avec deux scénarios :

**Cas 1** : Le geste de panoramique s'est terminé dans la direction inverse de sa direction initiale, mais l'animateur n'a pas été inversé. Cela signifie que nous devons inverser l'animateur avant d'appeler `transitionAnimator.continueAnimation(...)`.

**Cas 2** : Le geste de panoramique s'est terminé dans sa direction _initiale_, mais l'animateur a été _inversé_ à un moment donné. Cela signifie que, encore une fois, nous devons inverser l'animateur avant d'appeler `transitionAnimator.continueAnimation(...)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7drca2ayKwLj7k8FHtvKuA.gif)
_Presque là !_

### Animation

Dans `didChangePan(...)` nous avons appelé `beginAnimation()` si l'animateur de transition était `nil`. Voici l'implémentation de cette fonction :

Les choses importantes qui se passent sont :

* Nous informons un délégué qu'il doit définir `startingXOffset`, `endingXOffset`, `startingYOffset`, et `endingYOffset`
* Nous initialisons le `transitionAnimator` avec un bloc d'animation qui met à jour les contraintes de la vue, puis appelons `layoutIfNeeded()`
* Nous configurons le bloc de complétion de l'animateur (décrit ci-dessous)
* Si l'animation a été initiée de manière programmatique (aucun geste de panoramique impliqué), nous appelons `transitionAnimator.continueAnimation(...)` pour permettre à l'animation de se terminer seule
* Si l'animation a été initiée à partir d'un geste de panoramique, nous mettons immédiatement _en pause_ l'animation plutôt que de lui permettre de se terminer. Cela est dû au fait que la progression de l'animation sera ajustée dans `didChangePan(...)`

#### Complétion de l'animation

La dernière fonction à aborder est `configureAnimationCompletionBlock()`, décrite ci-dessous :

Si l'animateur a terminé là où il a commencé, nous réinitialisons les contraintes à ce qu'elles étaient avant l'animation.

Si l'animateur a terminé comme prévu, dans une position différente, nous échangeons les contraintes. Cela permet à la vue d'être animée d'avant en arrière, encore et encore.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XnrqYkX8KdP0UBce4l4Jmw.gif)
_Balayez d'avant en arrière après avoir échangé les contraintes dans le bloc de complétion_

Enfin, nous faisons une vérification rapide pour nous assurer que si l'état de `position` est `.end`, la vue a réellement changé de position. Lors du développement de l'application, j'ai rencontré un comportement bogué, mais cela a résolu le problème.

### Résumé

Le code d'exemple `BlockViewController` [peut être trouvé ici](https://gist.github.com/trevphil/859a139ed6549f1022330b2eb1ceff75), mais veuillez garder à l'esprit qu'il est sorti de son contexte d'une application plus large. Il ne fonctionnera pas tel quel.

Pour plus de projets intéressants allant de Node.js à Raspberry Pi, n'hésitez pas à [consulter mon site web](https://trevphil.com/projects). Ou [téléchargez Bloq gratuitement](https://apple.co/2v6dujl) sur l'App Store.