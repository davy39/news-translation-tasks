---
title: Comment créer une vue dégradée belle et réutilisable en Swift avec IBDesignable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T20:21:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-beautiful-reusable-gradient-view-in-swift-with-ibdesignable-981aebb43d30
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SP9Gb25wmrEb0Jj3yqKiHA.jpeg
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
seo_title: Comment créer une vue dégradée belle et réutilisable en Swift avec IBDesignable
seo_desc: 'By Lee Dowthwaite

  This tutorial will demonstrate how to create a versatile, @IBDesignable gradient
  view class in Swift 4. You can drop the CAGradientView into storyboards and preview
  at design time. Or add it programmatically. You can set the colors ...'
---

Par Lee Dowthwaite

Ce tutoriel démontrera comment créer une classe de vue dégradée `@IBDesignable` polyvalente en Swift 4. Vous pouvez glisser-déposer la CAGradientView dans les storyboards et la prévisualiser au moment de la conception. Ou l'ajouter par programmation. Vous pouvez définir les couleurs pour deux arrêts de dégradé (début et fin) et la direction du dégradé (en degrés). Ces propriétés sont entièrement contrôlables depuis l'inspecteur IB.

### Pourquoi vous en avez besoin

Les designers adorent les dégradés. Admettons-le, comme les arrière-plans flous et les ombres portées, ils entrent et sortent de la mode avec le vent changeant. Ils tendent à être plus subtils de nos jours, donc ils nécessitent une bonne quantité de bidouillage pour les obtenir juste comme il faut.

Créer un dégradé implique une quantité raisonnable de travail. Le peaufiner jusqu'à ce que votre designer soit satisfait peut être un processus chronophage. Ce tutoriel vous montre comment construire un composant de vue dégradée que vous pouvez glisser-déposer dans les storyboards et prévisualiser directement depuis Interface Builder.

Vos designers vous en seront reconnaissants, et vous vous épargnerez beaucoup de temps.

### Ce que vous allez construire

Il est facile de dire que vous allez construire une vue dégradée, mais quelles sont les exigences exactes ? Définissons-les :

* Elle doit être une sous-classe de `UIView`
* Elle doit être `@IBDesignable` pour pouvoir être prévisualisée dans Xcode/Interface Builder
* Elle doit être entièrement configurable soit en code soit dans Interface Builder

### Obtenir le projet d'exemple

Pour suivre correctement ce tutoriel, vous aurez besoin du projet d'exemple que vous pouvez [télécharger depuis GitHub](https://github.com/leedowthwaite/LDGradientView).

Lorsque vous chargez le projet dans Xcode et ouvrez la scène exemple ViewController dans le storyboard, vous pourrez sélectionner la vue dégradée et l'éditer dans l'Inspecteur d'attributs, comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/VI4tU7BOgz3h0xqjKZwfSoSjaEoPHQZJ4jvr)

### À propos des couches de dégradé

**NOTE :** Ceci n'est pas destiné à être une introduction à `CAGradientLayer`. Si vous avez besoin d'une introduction plus basique, veuillez lire mon tutoriel [Maîtriser CAGradientLayer en Swift](https://appcodelabs.com/creating-an-ibdesignable-gradient-view-in-swift-2) qui explique tout ce dont vous avez besoin.

Il existe plusieurs façons d'obtenir un effet de dégradé dans iOS, mais dans ce tutoriel, nous utiliserons `CAGradientLayer`. Il s'agit d'une sous-classe de `CALayer`, un objet Core Animation qui fait partie de la hiérarchie des couches de la vue. Dans iOS, les `UIView` sont décrites comme des **vues soutenues par des couches** car leur apparence est contrôlée par leur propriété `layer`. Chaque vue a une couche, et tout comme chaque `UIView` peut avoir plusieurs sous-vues, chaque couche peut avoir plusieurs sous-couches.

Ce que cela signifie en termes pratiques, c'est que chaque vue peut avoir un arbre de couches arbitrairement complexe pour ajouter une complexité visuelle à la vue. Lorsque l'on travaille intensément avec Core Animation, à un moment donné, le développeur doit tracer la distinction entre l'ajout de complexité au niveau `CALayer` et l'ajout d'une nouvelle `UIView` pour obtenir le même effet. Habituellement, la démarcation entre les vues et les couches est assez évidente. Souvent parce qu'une propriété d'une vue est requise pour la fonctionnalité de l'application (par exemple, un `UILabel` ou `UIButton` est requis).

Lorsque nous créons des interfaces utilisateur riches avec beaucoup de graphiques subtils, il peut devenir trop facile d'augmenter la complexité de la hiérarchie des couches. En général, vous devriez éviter cela car les couches ne peuvent être gérées que dans le code, pas dans les storyboards. La logique de gestion de la hiérarchie des couches peut devenir assez ingérable.

Pour les besoins de ce tutoriel, vous ajouterez une seule `CAGradientLayer` en tant que sous-couche sur la propriété `layer` de la vue. Cela donne une correspondance un-à-un entre les vues et les couches. Cela encapsule bien chaque couche de dégradé à l'intérieur d'une UIView afin qu'elle puisse être disposée dans un storyboard.

### Définition de la sous-classe de vue

Le cœur de ce tutoriel est une vue dégradée appelée `LDGradientView`. Il s'agit d'une sous-classe de `UIView` et est définie comme suit :

```
@IBDesignable class LDGradientView: UIView {   // ... }
```

La classe est marquée comme `@IBDesignable`, ce qui signifie qu'elle peut être prévisualisée dans Interface Builder (l'éditeur de storyboard de Xcode).

Le dégradé lui-même est défini comme une propriété privée de la classe :

```
// la couche de dégradé private var gradient: CAGradientLayer?
```

Cette propriété est créée par la fonction ci-dessous. Elle définit la propriété `frame` du dégradé sur les limites de la vue, occupant ainsi toute la vue. Cela est conforme à la correspondance un-à-un entre la vue et la couche.

```
// créer une couche de dégradé private func createGradient() -> CAGradientLayer {   let gradient = CAGradientLayer()   gradient.frame = self.bounds  return gradient }
```

Elle est ensuite ajoutée en tant que sous-couche de la couche de la vue comme montré :

```
// Créer un dégradé et l'installer sur la couche private func installGradient() {   // s'il y a déjà un dégradé installé sur la couche, le supprimer  if let gradient = self.gradient {    gradient.removeFromSuperlayer()  }   let gradient = createGradient()  self.layer.addSublayer(gradient)  self.gradient = gradient}
```

Ce sont toutes deux des fonctions privées car la hiérarchie des couches d'une vue devrait être son propre domaine.

Si vous installez la vue dégradée dans une hiérarchie complexe, ou toute supervue qui utilise des contraintes, alors chaque fois que le cadre est défini, la vue doit se mettre à jour. Vous pouvez le faire en ajoutant ces méthodes :

```
override var frame: CGRect {  didSet {    updateGradient()  }}
```

```
override func layoutSubviews() {  super.layoutSubviews()  // ceci est crucial lorsque des contraintes sont utilisées dans les supervues  updateGradient()}
```

```
// Mettre à jour un dégradé existant    private func updateGradient() {        if let gradient = self.gradient {            let startColor = self.startColor ?? UIColor.clear            let endColor = self.endColor ?? UIColor.clear            gradient.colors = [startColor.cgColor, endColor.cgColor]            let (start, end) = gradientPointsForAngle(self.angle)            gradient.startPoint = start            gradient.endPoint = end            gradient.frame = self.bounds        }    }
```

Enfin, nous avons également besoin d'un moyen d'instancier la vue et d'appeler la fonction `installGradient`. Nous le faisons à partir de l'un des deux initialiseurs, le premier pour initialiser depuis Interface Builder, et le second pour l'instanciation programmatique :

```
// initialiseurs required init?(coder aDecoder: NSCoder) {  super.init(coder: aDecoder)  installGradient() } 
```

```
override init(frame: CGRect) {  super.init(frame: frame)  installGradient() }
```

### Définition d'un dégradé

Maintenant, vous avez une sous-classe `UIView` qui peut installer une `CAGradientLayer`, mais cela n'accomplit pas grand-chose. Faisons en sorte que la vue dégradée travaille pour nous...

Il y a deux propriétés principales de `CAGradientLayer` que votre vue personnalisée manipulera. Ce sont :

* Les couleurs du dégradé
* La direction du dégradé

### Définition des couleurs

Les couleurs sont définies comme une propriété sur `CAGradientLayer` :

```
// Un tableau d'objets CGColorRef définissant la couleur de chaque arrêt de dégradé. Animatable.var colors: [Any]?
```

### Une note sur les arrêts de dégradé

Les points auxquels la couleur change dans un dégradé sont appelés _arrêts de dégradé_. Les dégradés prennent en charge un comportement assez complexe et peuvent avoir un nombre illimité d'arrêts. Programmer ce comportement est simple. Créer une interface `@IBInspectable` pour cela, cependant, est plus difficile.

Il serait relativement trivial d'ajouter un ou deux autres arrêts de dégradé. Résoudre le problème général d'un nombre arbitraire d'arrêts est plus difficile. La solution serait probablement moins utilisable que de faire le même travail directement dans le code.

Pour cette raison, ce projet ne traite que des dégradés "simples". Ceux qui commencent avec une couleur sur un bord de la vue et s'estompent vers une autre couleur sur le bord opposé.

Si vous devez ajouter un autre arrêt, vous devriez pouvoir modifier le code assez facilement, mais cela rendrait le tutoriel trop compliqué.

Notre implémentation des arrêts de couleur est simplement :

```
// la couleur de début du dégradé @IBInspectable var startColor: UIColor? 
```

```
// la couleur de fin du dégradé @IBInspectable var endColor: UIColor?
```

Celles-ci sont exposées dans Interface Builder sous forme de contrôles de couleur.

### Définition de la direction

La direction du dégradé est définie par deux propriétés sur `CAGradientLayer` :

```
// Le point de fin du dégradé lorsqu'il est dessiné dans l'espace de coordonnées de la couche. Animatable.var endPoint: CGPoint
```

```
// Le point de départ du dégradé lorsqu'il est dessiné dans l'espace de coordonnées de la couche. Animatable.var startPoint: CGPoint
```

Les points de départ et de fin d'un dégradé sont définis dans l'**espace de dégradé unitaire**, ce qui signifie simplement que, quelles que soient les dimensions d'une `CAGradientLayer` donnée, dans l'espace de dégradé unitaire, nous considérons le coin supérieur gauche comme étant la position (0, 0) et le coin inférieur droit comme étant la position (1, 1), comme illustré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/-eJ1jThRc05m7Ri-F1sSMN6fGsIBcs5jaovy)

C'est le système de coordonnées `CAGradientLayer`.

La direction est la partie la plus difficile de la création d'un dégradé `@IBDesignable`. En raison du besoin d'un point de départ et d'un point de fin, du fait que les attributs `@IBInspectable` ne supportent pas le type de données `CGPoint`, sans parler du manque complet de validation des données dans l'interface utilisateur, nos options sont un peu limitées.

En essayant de trouver le moyen le plus simple de définir des directions de dégradé courantes, une chaîne de caractères semblait être un type de données potentiellement utile et peut-être des points cardinaux, par exemple "N", "S", "E", "W" pourraient être utiles. Mais pour les directions intermédiaires, devrait-il supporter "NW" ? Et "NNW" ou "WNW" ? Et au-delà ? Cela deviendrait immédiatement confus. Et cette façon de penser était clairement un long détour pour réaliser que la meilleure façon de décrire un angle sur la boussole était d'utiliser les degrés !

L'utilisateur peut oublier les espaces de dégradé unitaire. Toute la complexité est réduite à une seule propriété exposée à Interface Builder :

```
// l'angle du dégradé, en degrés dans le sens inverse des aiguilles d'une montre à partir de 0 (est/droite)@IBInspectable var angle: CGFloat = 270
```

Sa valeur par défaut (270 degrés) pointe vers le sud simplement pour correspondre à la direction par défaut de `CAGradientLayer`. Pour un dégradé horizontal, définissez-le sur 0 ou 180.

### Conversion de l'angle en espace de dégradé

C'est la partie la plus difficile. J'inclus le code et une description de son fonctionnement. Vous pouvez sauter cette partie si vous êtes simplement intéressé par l'utilisation de la classe.

La fonction de haut niveau pour convertir l'angle en points de départ et de fin de l'espace de dégradé ressemble à ceci :

```
// créer un vecteur pointant dans la direction de l'angle private func gradientPointsForAngle(_ angle: CGFloat) -> (CGPoint, CGPoint) {  // obtenir les points de départ et de fin du vecteur  let end = pointForAngle(angle)  let start = oppositePoint(end)  // convertir en espace de dégradé  let p0 = transformToGradientSpace(start)  let p1 = transformToGradientSpace(end)  return (p0, p1) }
```

Cela prend l'angle spécifié par l'utilisateur et l'utilise pour créer un vecteur pointant dans cette direction, comme illustré ci-dessous. L'angle spécifie la rotation du vecteur à partir de 0 degré. Par convention, le point est à l'est dans Core Animation, et augmente dans le sens inverse des aiguilles d'une montre.

![Image](https://cdn-media-1.freecodecamp.org/images/EETacSgjgl9tezcM9zybNQIJe7fdeYp0-bgy)

Le point de fin est trouvé en appelant `pointForAngle()`, défini comme suit :

```
private func pointForAngle(_ angle: CGFloat) -> CGPoint {  // convertir les degrés en radians  let radians = angle * .pi / 180.0  var x = cos(radians)  var y = sin(radians)  // (x,y) est en termes de cercle unitaire. Extrapoler au carré unitaire pour obtenir la longueur complète du vecteur  if (fabs(x) > fabs(y)) {    // extrapoler x à la longueur unitaire    x = x > 0 ? 1 : -1 y = x * tan(radians)  } else {    // extrapoler y à la longueur unitaire    y = y > 0 ? 1 : -1    x = y / tan(radians)  }   return CGPoint(x: x, y: y) }
```

Cette fonction semble plus compliquée qu'elle ne l'est. À sa base, elle prend simplement le sinus et le cosinus de l'angle pour déterminer le point de fin sur un cercle unitaire. Parce que les fonctions trigonométriques de Swift (comme la plupart des autres langages) nécessitent que les angles soient spécifiés en radians plutôt qu'en degrés, nous devons d'abord faire cette conversion. Ensuite, la valeur x est calculée par `x = cos(radians)`, et la valeur y par `y = sin(radians)`.

Le reste de la fonction concerne le fait que le point résultant est sur le cercle unitaire. Les points dont nous avons besoin, cependant, sont dans un carré unitaire. Les angles le long des points cardinaux (c'est-à-dire 0, 90, 180 et 270 degrés) donneront le résultat correct, au bord du carré. Pour les angles intermédiaires, le point sera en retrait par rapport au bord du carré. Le vecteur doit être extrapolé au bord du carré pour donner l'apparence visuelle correcte. Cela est illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Maintenant que nous avons le **point de fin** dans un carré unitaire signé, le **point de départ** du vecteur est trouvé par la fonction simple ci-dessous. Parce que le point est dans un espace unitaire signé, il est trivial de trouver le point de départ en inversant simplement le signe des composantes du point de fin.

```
private func oppositePoint(_ point: CGPoint) -> CGPoint {  return CGPoint(x: -point.x, y: -point.y) }
```

Notez qu'une autre façon d'y parvenir aurait été d'ajouter 180 degrés à l'angle d'origine et d'appeler à nouveau `pointForAngle()`. Mais la méthode d'inversion de signe est si simple qu'elle est légèrement plus efficace à faire de cette manière.

Maintenant que nous avons les points de départ et de fin dans l'espace unitaire signé, il ne reste plus qu'à les traduire dans l'espace de dégradé non signé. L'espace unitaire a un axe y qui augmente vers le nord. Alors que dans l'espace Core Animation, y augmente vers le sud. Ainsi, la composante y doit être inversée dans le cadre de cette traduction. L'emplacement (0, 0) dans notre espace unitaire signé devient (0.5, 0.5) dans l'espace de dégradé. La fonction est très simple :

```
private func transformToGradientSpace(_ point: CGPoint) -> CGPoint {  // le point d'entrée est dans l'espace unitaire signé : (-1,-1) à (1,1)  // convertir en espace de dégradé : (0,0) à (1,1), avec l'axe Y inversé   return CGPoint(x: (point.x + 1) * 0.5, y: 1.0 - (point.y + 1) * 0.5) }
```

### Félicitations !

Et c'est tout le travail difficile terminé — ouf ! Félicitations pour être arrivé jusqu'ici — allez vous chercher un café pour célébrer...

### Support d'Interface Builder

Tout ce qui reste de la classe de vue dégradée est la fonction `prepareForInterfaceBuilder()`. Cette fonction n'est exécutée que depuis Interface Builder lorsqu'il doit rendre une vue. Une vue `@IBDesignable` bien conçue peut en fait fonctionner assez bien sans elle. Il y aura des moments — par exemple lors de l'ajout d'une nouvelle vue à un storyboard — où elle ne se rendra pas correctement jusqu'à ce que cette fonction soit présente. Vous pouvez forcer son exécution en sélectionnant la vue dans le storyboard et en choisissant **Editor|Debug Selected Views** dans le menu.

Notre implémentation de la fonction s'assure simplement que le dégradé est installé et mis à jour.

```
override func prepareForInterfaceBuilder() {   super.prepareForInterfaceBuilder()  installGradient()  updateGradient() }
```

### Merci d'avoir lu !

Le code de ce projet est librement disponible [sur GitHub](https://github.com/leedowthwaite/LDGradientView).

[Lee Dowthwaite est un développeur iOS chevronné](https://appcodelabs.com/signup) qui a développé des applications de haut profil pour de nombreux clients de premier plan depuis 2010.

_Publié à l'origine sur [appcodelabs.com](https://appcodelabs.com/create-ibdesignable-gradient-view-swift) le 10 décembre 2017._