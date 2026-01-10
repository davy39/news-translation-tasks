---
title: Comment créer de magnifiques mises en page extensibles sur iOS en utilisant
  Auto Layout et SnapKit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-22T14:10:58.000Z'
originalURL: https://freecodecamp.org/news/tutorial-creating-stretchy-layouts-on-ios-using-auto-layout-3fa974fa5e28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hrNh2x1YdmydgrIpc0cPlg.png
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: mobile
  slug: mobile
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer de magnifiques mises en page extensibles sur iOS en utilisant
  Auto Layout et SnapKit
seo_desc: 'By Enabled Solutions

  Check the image below. This is a cool effect.

  And it’s really easy to build in iOS using Auto Layout. I wanted to write about
  this because the effect is so simple. And Auto Layout makes its implementation so
  elegant that I think ...'
---

Par Enabled Solutions

Vérifiez l'image ci-dessous. C'est un effet cool.

Et c'est vraiment facile à construire sur iOS en utilisant Auto Layout. Je voulais écrire à ce sujet parce que l'effet est si simple. Et Auto Layout rend son implémentation si élégante que je pense que vous devriez en savoir plus à ce sujet.

![Image](https://cdn-media-1.freecodecamp.org/images/P7ieI8aLehAc0J0GmSO9KW2Udap-9Y5c-7z0)

Si vous voulez suivre, vous pouvez cloner le [projet de démonstration](https://github.com/TwoLivesLeft/StretchyLayout/tree/Step-1) à notre point de départ et implémenter l'effet au fur et à mesure de votre lecture. Vous aurez besoin de Xcode 9 car nous utilisons iOS 11 pour cet exemple.

```
git clone https://github.com/TwoLivesLeft/StretchyLayout.git
cd StretchyLayout
git checkout Step-1
```

Voici comment nous allons procéder :

* Commencez avec l'application de base non extensible
* Modifiez la hiérarchie des vues pour ajouter les contraintes nécessaires pour la rendre extensible
* Ajoutez des finitions à l'application

### L'application non extensible

Voici la hiérarchie des vues pour la version de base de l'application. Vous pouvez voir qu'elle a trois vues principales. Il y a l'en-tête `UIImageView`, qui est le conteneur pour le texte, et le long `UILabel` contenant notre contenu textuel. Les lignes rouges vives représentent nos contraintes Auto Layout. Il y a aussi un `UIScrollView` et la vue racine de notre contrôleur de vue.

![Image](https://cdn-media-1.freecodecamp.org/images/pdyGWD8y9lh5MPhgcWcNJD8Tg3nP8e1-fhwi)

Nous allons construire cela en utilisant un framework Auto Layout appelé [SnapKit](http://snapkit.io). SnapKit est un framework iOS simple qui rend l'API Auto Layout d'Apple... saine. Il est très simple à utiliser et rend la programmation avec Auto Layout vraiment agréable.

La plupart du code résidera dans `viewDidLoad` de notre classe `StretchyViewController`. Ci-dessous, vous pouvez voir comment les contraintes initiales sont définies.

Nos vues sont déclarées comme membres privés :

```
private let scrollView = UIScrollView()
private let infoText = UILabel()
private let imageView = UIImageView()
```

La vue de notre contrôleur de vue a une vue de défilement comme première sous-vue, suivie des vues de texte et d'image. Elle a également une vue de support qui nous fournit le fond rouge derrière le texte.

```
// Épingler les bords de la vue de défilement à
// la vue de notre contrôleur de vuescrollView.snp.makeConstraints { make in
```

```
make.edges.equalTo(view)}
```

```
// Épingler le haut de notre vue d'image à la vue de défilement
// épingler la gauche et la droite à la vue du contrôleur de vue
// lui donner une contrainte de ratio d'aspect en contraignant
// sa hauteur à sa largeur avec un multiplicateurimageView.snp.makeConstraints { make in
```

```
make.top.equalTo(scrollView)
make.left.right.equalTo(view)
make.height.equalTo(imageView.snp.width).multipliedBy(0.7)}
```

```
// Épingler la vue de support sous la vue d'image et à
// le bas de la vue de défilementtextContainer.snp.makeConstraints { make in
```

```
make.top.equalTo(imageView.snp.bottom)
make.left.right.equalTo(view)
make.bottom.equalTo(scrollView)}
```

```
// Épingler les bords du texte à la vue du conteneur de texte, cela
// forcera le conteneur de texte à grandir pour englober
// la hauteur du texteinfoText.snp.makeConstraints { make in
```

```
make.edges.equalTo(textContainer).inset(14)}
```

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-1`

### Une brève parenthèse

Nous avons utilisé SnapKit ci-dessus. SnapKit est génial — voici une introduction sur son fonctionnement.

Vous accédez à l'objet membre `snp` sur n'importe quel `UIView`.

Vous appelez `makeConstraints` qui accepte une fermeture, et la fermeture reçoit un objet `ConstraintMaker` (appelé `make` ici).

Vous utilisez ensuite l'objet `make` pour épingler les bords ou les ancres d'une vue à n'importe quelle autre vue, guide de mise en page ou constante.

```
myView.snp.makeConstraints { make in
```

```
make.edges.equalTo(view)}
```

Cela épinglera les bords de `myView` aux bords de `view`.

C'est lisible et concis. Utilisez cela au lieu de l'API Auto Layout par défaut.

### La rendre extensible

Alors, comment passer de ceci (non extensible) à ceci (extensible) ?

![Image](https://cdn-media-1.freecodecamp.org/images/2VpWTIPmixmNTjKV9M58hoLuGbf4SUVJoo5Y)

Il est important pour l'effet d'étirement qu'Auto Layout résolve les contraintes, peu importe que vos vues soient des frères et sœurs ou ailleurs dans la hiérarchie. Il n'est important que de savoir qu'elles ont un ancêtre commun.

Mais voici un élément clé : les vues dans les vues de défilement peuvent être contraintes par rapport aux vues en dehors des vues de défilement. C'est ainsi que nous allons faire fonctionner cela.

![Image](https://cdn-media-1.freecodecamp.org/images/BvE521wsOw9CcFWAY2N2Mv3K4SxFTc-7V1br)

Dans le diagramme ci-dessus, les lignes rouges vives représentent nos contraintes. Remarquez comment le haut de la vue d'image est maintenant épinglé tout en haut — en dehors de la vue de défilement — au haut de la vue racine. Mais son bas est épinglé au bas de la vue du conteneur d'image, qui **est** à l'intérieur de la vue de défilement. Cela signifie que lorsque la vue de défilement défile, notre vue d'image s'étirera pour satisfaire ses contraintes.

Donc, pour notre première étape, nous allons remplacer notre `UIImageView` par une vue de conteneur vide.

```
let imageContainer = UIView()
imageContainer.backgroundColor = .darkGray
scrollView.addSubview(imageContainer)
```

```
imageContainer.snp.makeConstraints { make in
```

```
make.top.equalTo(scrollView)
make.left.right.equalTo(view)
make.height.equalTo(imageContainer.snp.width).multipliedBy(0.7)}
```

Ensuite, nous allons ajouter notre vue d'image comme sous-vue de notre vue de défilement. Mais nous allons épingler son bord supérieur au bord **supérieur de notre vue** — et non au bord supérieur de notre vue de défilement. Le conteneur que nous venons d'ajouter ci-dessus est épinglé au bord supérieur de notre vue de défilement.

```
scrollView.addSubview(imageView)
```

```
imageView.snp.makeConstraints { make in
```

```
make.left.right.equalTo(imageContainer)
```

```
//** Ce sont les lignes clés ! **
make.top.equalTo(view)
make.bottom.equalTo(imageContainer.snp.bottom)}
```

Ci-dessus, vous pouvez voir les lignes qui font fonctionner cela. Notre vue de conteneur d'image défile exactement comme l'application non extensible d'origine. Mais nous avons ajouté notre vue d'image réelle au-dessus de ce conteneur. Et nous avons épinglé son bas au bas du conteneur, tandis que son **haut** est épinglé à la vue du contrôleur de vue.

Cela signifie que lorsque vous faites glisser vers le bas dans la vue de défilement, le haut de l'image « colle » au haut de l'écran et toute l'image devient simplement plus grande. Et parce que nous utilisons `imageView.contentMode = .scaleAspectFill`, nous allons voir le contenu de l'image se mettre à l'échelle dans la vue d'image lorsque nous faisons défiler la vue de défilement.

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-2`

#### Mais il y a un bug

Si vous exécutez ce code, en faisant glisser vers le bas sur l'écran avec votre doigt, vous obtenez l'effet souhaité : l'image se met à l'échelle et rebondit. Mais si vous faites défiler vers le haut pour lire le texte... eh bien, vous réaliserez que vous ne pouvez pas.

![Image](https://cdn-media-1.freecodecamp.org/images/PKBFntQvQNoGAEy9sJmdAion4wieEE9SFBw8)

Pourquoi ?

Parce que lorsque nous faisons défiler vers le haut, nous comprimons le `UIImageView` en une ligne de hauteur zéro. Son haut **doit** être égal au haut de la vue, et son bas **doit** être égal au haut de la vue de support de texte. Donc cela signifie que la vue de défilement continuera à « défiler », mais nous ne verrons pas les changements. Cela est dû au fait que la vue de support est coincée contre la vue d'image, qui refuse de se déplacer au-dessus du haut de la vue racine malgré le défilement de la vue de défilement.

Auto Layout résout techniquement nos contraintes, mais ce n'est pas ce que nous voulons.

#### Correction du bug

Nous devons changer la façon dont nous contraignons la vue d'image. Voici le changement :

```
imageView.snp.makeConstraints { make in
```

```
make.left.right.equalTo(imageContainer)
```

```
//** Notez les priorités
make.top.equalTo(view).priority(.high)
```

```
//** Nous ajoutons également une contrainte de hauteur
make.height.greaterThanOrEqualTo(imageContainer.snp.height).priority(.required)
```

```
//** Et gardez la contrainte de bas
make.bottom.equalTo(imageContainer.snp.bottom)}
```

Remarquez comment nous avons maintenant une contrainte de haut, une contrainte de bas, **et** une contrainte de hauteur ? C'est l'une des choses géniales à propos d'Auto Layout : nous pouvons avoir des contraintes conflictuelles et elles seront rompues dans l'ordre de priorité. Cela est nécessaire pour obtenir l'effet que nous voulons.

Tout d'abord, nous gardons notre contrainte originale. Le haut de notre vue d'image est épinglé au haut de notre vue. Nous donnons à cela une priorité de `.high`.

Nous ajoutons ensuite une contrainte supplémentaire : la hauteur de notre image doit être supérieure ou égale à la hauteur du conteneur d'image derrière elle (rappelons que notre conteneur d'image a la contrainte de ratio d'aspect). Cela a une priorité `.required`.

Alors, que se passe-t-il lorsque nous faisons défiler vers le haut ?

Eh bien, l'image **ne peut pas** devenir plus petite. Notre contrainte de hauteur a une priorité plus élevée que la contrainte de haut. Donc lorsque nous faisons défiler vers le haut, Auto Layout rompt la contrainte de priorité la plus basse afin de résoudre le système. Il rompt la contrainte de haut, et notre comportement de défilement revient à la normale. Cela nous permet de faire défiler vers le haut et de lire le texte.

Notez que vous pouvez également supprimer la contrainte de hauteur dans ce cas et simplement définir la priorité de la contrainte de haut à `.high`. Cela permettra à iOS de rompre la contrainte de haut **et** de compresser la vue d'image à une hauteur nulle. Étant donné le mode de contenu `.scaleAspectFill`, cela crée un effet de type parallaxe. Essayez-le. Vous pourriez préférer son apparence.

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-3`

### Polir les détails

Il y a trois problèmes gênants que nous devrions corriger pendant que nous y sommes.

#### 1. Texte en sur-défilement

Si nous faisons défiler au-delà du bas de la vue, nous pouvons voir l'arrière-plan gris laid de notre contrôleur de vue. Nous pouvons utiliser la même méthode pour étirer notre vue de support lorsque nous faisons défiler au-delà du bas de la vue.

![Image](https://cdn-media-1.freecodecamp.org/images/ZNWnV1m9P6ZhJ5c0qgiXy1UgXg9ZBFNbvGQX)

Je ne vais pas entrer dans le code, puisque c'est essentiellement la même technique que la vue d'image ci-dessus. Nous ajoutons une vue de support de texte supplémentaire derrière notre conteneur de texte, puis nous épinglons son bord inférieur au bord inférieur de la vue racine.

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-4`

#### 2. Respecter la zone sécurisée

Sur l'iPhone X, notre texte chevauche l'indicateur de la page d'accueil. Nous avons désactivé l'ajustement automatique de l'inset de contenu de notre vue de défilement afin de permettre à notre contenu d'image d'aller jusqu'en haut de l'écran. Nous devons donc gérer manuellement l'inset inférieur en utilisant la nouvelle propriété `safeAreaInsets` dans iOS 11.

Nous voulons également utiliser `safeAreaInsets` pour ajuster les indicateurs de défilement de notre vue de défilement. De cette façon, ils ne se heurteront pas aux bords courbés de l'écran sur l'iPhone X.

Pour corriger ces deux problèmes, nous allons remplacer `viewDidLayoutSubviews` et définir manuellement l'inset inférieur de la vue de défilement. iOS 11 le ferait normalement pour nous automatiquement, mais nous *ne voulons pas* insérer le haut. Nous voulons que notre image d'en-tête soit alignée derrière la barre d'état.

Nous avons dit à iOS 11 de ne pas toucher notre vue de défilement en définissant son comportement `contentInsetAdjustmentBehavior` sur `.never`.

```
override func viewDidLayoutSubviews() {
    super.viewDidLayoutSubviews()
```

```
    //** Nous voulons que les indicateurs de défilement utilisent tous les insets de la zone sécurisée
    scrollView.scrollIndicatorInsets = view.safeAreaInsets
```

```
    //** Mais nous voulons que l'inset de contenu réel respecte uniquement l'inset sécurisé inférieur
    scrollView.contentInset = UIEdgeInsets(top: 0, left: 0, bottom: view.safeAreaInsets.bottom, right: 0)}
```

Cela nous donne l'apparence suivante lorsque nous faisons défiler jusqu'à la fin. Remarquez que l'indicateur de défilement n'est plus perdu derrière la courbe, et nous obtenons beaucoup plus d'espace au-dessus de l'indicateur de la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/7azwhWaasaCNphR1hiJexWgXkSIxNQbaMZMb)

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-5`

#### 3. Masquer la barre d'état lorsque nécessaire

Notre texte chevauche la barre d'état lorsque nous faisons défiler vers le haut. Cela a l'air grossier.

![Image](https://cdn-media-1.freecodecamp.org/images/wI6hqWh8Ogt-C5zj7GRsjYAYwtK9Y9ogJs5E)

Masquons la barre d'état avec une animation cool lorsque l'utilisateur fait défiler le texte dans la zone de la barre d'état. C'est assez facile à détecter, et je pense que l'effet est super.

![Image](https://cdn-media-1.freecodecamp.org/images/EMUGspv-jImneDNzsRbuhvd1hW0ak5boKMka)

Comment faire cela ?

* Nous convertissons le rectangulaire de `textContainer` en coordonnées d'écran.
* Nous vérifions si le Y minimum de ce cadre est inférieur à l'inset supérieur de la zone sécurisée de la vue. Cela indique que le conteneur de texte se déplace dans la zone de la barre d'état.
* Si c'est le cas, nous masquons la barre d'état. Sinon, nous affichons la barre d'état.

Nous effectuons cette vérification dans la méthode `scrollViewDidScroll(_:)` du `UIScrollViewDelegate`. Nous faisons donc en sorte que notre `StretchyViewController` implémente ce délégué et se définisse comme le délégué pour sa vue de défilement.

Voici le code pour la vérification de la barre d'état :

```
//MARK: — Délégué de la vue de défilement
```

```
private var previousStatusBarHidden = false
```

```
func scrollViewDidScroll(_ scrollView: UIScrollView) {
    //** Nous gardons l'état précédent de la barre d'état masquée afin que
    // nous ne déclenchions pas un bloc d'animation implicite pour chaque image
    // dans laquelle la vue de défilement défile
    if previousStatusBarHidden != shouldHideStatusBar {
```

```
        UIView.animate(withDuration: 0.2, animations: {
            self.setNeedsStatusBarAppearanceUpdate()
        })
```

```
        previousStatusBarHidden = shouldHideStatusBar
    }
}
```

```
//MARK: — Apparence de la barre d'état
```

```
override var preferredStatusBarUpdateAnimation: UIStatusBarAnimation {
    //** Nous utilisons l'animation de glissement car elle fonctionne bien avec le défilement
    return .slide
}
```

```
override var prefersStatusBarHidden: Bool {
    return shouldHideStatusBar
}
```

```
private var shouldHideStatusBar: Bool {
    //** Voici où nous calculons si notre conteneur de texte
    // va heurter la zone sécurisée supérieure
    let frame = textContainer.convert(textContainer.bounds, to: nil)
    return frame.minY < view.safeAreaInsets.top
}
```

**Note :** Pour obtenir le code à ce stade, faites `git checkout Step-6`

### Ce que nous avons couvert

* Vous pouvez épingler presque n'importe quoi à n'importe quoi d'autre, et vos vues s'étireront pour satisfaire vos contraintes.
* Cela fonctionnera même si vous faites défiler.
* Les contraintes sont rompues dans l'ordre de priorité, alors n'ayez pas peur d'expérimenter avec des contraintes conflictuelles.
* Utilisez SnapKit !

Simeon Saëns dirige les activités de développement mobile d'[Enabled](http://enabled.com.au) avec un fort accent sur la conception et l'interaction homme-machine. Simeon est également appelé à rencontrer des clients pour comprendre leurs besoins et développer des solutions techniques. Suivez Simeon sur [Twitter](https://twitter.com/TwoLivesLeft)

#### Vous avez d'autres questions ? Tweetez-nous [@EnabledHQ](https://twitter.com/EnabledHQ)