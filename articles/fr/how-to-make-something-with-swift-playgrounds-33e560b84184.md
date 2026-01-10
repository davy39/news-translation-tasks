---
title: Comment créer quelque chose avec Swift Playgrounds
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-12T16:10:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-something-with-swift-playgrounds-33e560b84184
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5bqGKBRTdwhMZ-PIX9ON2Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment créer quelque chose avec Swift Playgrounds
seo_desc: 'By Harshita Arora

  Just a few days ago, I finished my WWDC 2018 scholarship submission. It was so much
  fun creating Alice in codeLand. This was my first year applying for WWDC scholarships,
  and I hope to get in!

  Alice in codeLand is a three-in-one. It...'
---

Par Harshita Arora

Il y a quelques jours à peine, j'ai terminé ma soumission pour la [bourse WWDC 2018](https://developer.apple.com/wwdc/scholarships/). Ce fut tellement amusant de créer [Alice in codeLand](https://github.com/harshitaarora/Alice-in-codeLand). C'était ma première année de candidature pour les bourses WWDC, et j'espère être acceptée !

Alice in codeLand est un trois-en-un. C'est un simulateur de hacker/codage qui ressemble au terminal Mac OS que vous pouvez utiliser hors ligne. C'est aussi une histoire drôle d'une hackeuse nommée Alice qui a tenté d'accéder sans autorisation au portail WWDC d'Apple après avoir réussi à pirater toothtube.com (une plateforme de partage de vidéos pour les critiques de dentifrice) et macaroonsarethebest.com (une plateforme sociale pour les amateurs de macarons comme moi). Et enfin, c'est une démonstration technique des injections SQL (une technique de piratage) pour que les gens apprennent la sécurité de l'information et le processus étape par étape des injections SQL après avoir découvert si un site web est vulnérable ou non.

Depuis 2017, Apple a lancé le défi aux candidats aux bourses de créer une expérience interactive dans Swift Playgrounds.

Quand j'ai commencé, j'étais assez confuse. Je n'avais jamais rien créé dans Playgrounds auparavant, car j'ai toujours travaillé avec des projets Xcode (qui vous permettent de créer de vraies applications iOS). J'avais seulement utilisé Playgrounds lorsque j'ai commencé à apprendre Swift pour apprendre et coder des concepts de programmation de base. Les instructeurs dans mes cours en ligne l'utilisaient, mais ces cours ne duraient que deux semaines, et je n'ai jamais créé de graphiques ou d'animations dans ceux-ci.

Il m'a donc fallu un certain temps pour me familiariser avec Playgrounds. Avec le recul, j'aurais pu économiser la moitié du temps si j'avais su où chercher les bonnes réponses et comment commencer à travailler avec eux.

Ce post est donc pour tous les futurs candidats aux bourses WWDC, car il semble qu'Apple continuera à donner cette tâche pour la bourse chaque année. Même si vous n'avez rien à voir avec les bourses WWDC, je pense que Swift Playgrounds est un outil génial pour construire et prototyper quelque chose rapidement.

Note : Ce post suppose que vous avez une expérience en Swift et dans les frameworks iOS comme UIKit. Si vous avez déjà construit des applications iOS, ce serait un énorme bonus !

Commençons !

### Alors, qu'est-ce que Swift Playgrounds, et pourquoi s'en soucier ?

Swift Playgrounds est une application iPad introduite par Apple en 2014 qui vous aide à apprendre à coder en Swift. C'est aussi un outil dans Xcode pour créer des Playgrounds. Vous pouvez exécuter des Playgrounds créés dans Xcode sur un iPad et vice-versa.

La différence entre l'application iPad et l'outil Xcode est que sur l'iPad, les Playgrounds que vous créez peuvent accéder à des fonctionnalités comme la caméra, l'écran tactile, etc. Mais lors de l'exécution d'un Playground sur Xcode, vous ne pouvez pas faire cela. Plus d'informations sur Swift Playgrounds [ici](https://developer.apple.com/swift-playgrounds/).

Bien que les concepts et exemples de ce post utilisent Xcode, les Playgrounds peuvent également être créés et exécutés sur l'application iPad.

### Quelques concepts à apprendre

#### 1. Comment exécuter/jouer des Playgrounds, et commencer avec eux

Vous pouvez télécharger des Playgrounds open-source [ici](https://github.com/wwdc/2017/), [ici](https://github.com/wwdc/2018/), et [ici](https://github.com/uraimo/Awesome-Swift-Playgrounds). Pour les jouer, cliquez sur Assistant Editor dans Xcode et sélectionnez "Live View" si ce n'est pas automatiquement sélectionné.

Une live view est l'endroit où la sortie ou les résultats de votre code sont affichés. Lorsque vous créez un objet dans votre code que vous souhaitez afficher dans la live view, vous devez assigner la propriété Live View de la page Playground à cet objet.

![Image](https://cdn-media-1.freecodecamp.org/images/5M2s06ZDoVHN2zw6LTYA0SRdIxGEjNdvFsfk)
_La Live View d'Alice in codeLand_

Voici le code pour assigner la propriété Live View de la page Playground à un objet UIView. Vous pouvez également assigner une classe ou un contrôleur de vue.

Vous devrez importer le framework PlaygroundSupport pour cela, ainsi que UIKit.

```
let view = UIView(frame: CGRect(x: 0, y:0, width: 1024, height: 768)
```

```
PlaygroundPage.current.live = view 
```

Dans le volet de navigation, vous verrez qu'il y a deux dossiers : Sources (pour tout le code auxiliaire) et Resources (pour toutes les images et les ressources audio).

D'après mon expérience, glisser un fichier Swift depuis la bibliothèque d'objets ne fonctionne pas dans Playgrounds pour une raison quelconque. Au lieu de cela, cliquez avec le bouton droit sur le dossier Sources et cliquez sur "New file" pour créer un nouveau fichier Swift.

#### 2. Comment créer une vue ?

Les Playgrounds n'ont pas de Storyboards. Vous pouvez créer une vue (UIView) de n'importe quelle taille (max 1024 x 768) de manière programmatique.

J'en ai créé une dans l'exemple ci-dessus.

#### 3. Qu'est-ce que PlaygroundSupport ?

[PlaygroundSupport](https://developer.apple.com/documentation/playgroundsupport) est un framework pour faire des choses comme accéder à une page de playground et gérer son exécution, gérer les vues en direct, et partager et accéder à des données persistantes.

En gros, vous devez importer ce framework pour pouvoir assigner la propriété de vue en direct de la page de playground à un objet que vous avez créé.

#### 4. Créer une documentation riche avec Markup

Swift Playgrounds vous permet de créer une belle documentation (plus facile à lire que les commentaires réguliers) en utilisant un langage appelé Markup.

La syntaxe de base pour Markup pour une documentation riche est la suivante :

1. Utilisez "//: stuff" pour les commentaires simples, ce qui, si vous remarquez, signifie simplement un " : " supplémentaire après le // (qui est utilisé pour les commentaires réguliers).
2. Utilisez "/*: stuff */" pour les commentaires multi-lignes.
3. Précédez une ligne d'un hashtag, par exemple, "#stuff" pour créer un titre.
4. Encadrez le texte à l'intérieur d'un astérisque, par exemple, "*stuff*" pour l'afficher en italique.
5. Encadrez le texte à l'intérieur de deux astérisques, par exemple, "**stuff**" pour l'afficher en gras.

Après avoir écrit le contenu dans la syntaxe, il est au format de balisage brut. Et pour l'afficher au format de balisage rendu (la vraie documentation riche), allez dans l'Éditeur, et sous "Playground Settings", sélectionnez "Render Documentation".

![Image](https://cdn-media-1.freecodecamp.org/images/n5m6eQHLvKsHGXO4gpaydOKMw5gulHBnyhMH)
_Exemple de format de balisage brut_

![Image](https://cdn-media-1.freecodecamp.org/images/BYK47HDw37dl0q4ej6Sx0x6ucbx1rxtX9oE8)
_Documentation rendue_

Lisez plus sur Markup [ici](https://developer.apple.com/library/content/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497).

### Commencer en construisant un Playground simple

D'accord, mettons les mains dans le cambouis en écrivant du code ! Créons un simulateur de hacker comme hackertyper.com ! :-D

Commençons par créer notre arrière-plan pour le simulateur de hacker. Ensuite, en utilisant la méthode [shouldChangeTextIn](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618630-textview), nous changerons le texte affiché dans la vue de texte en chaînes d'un tableau avec le code que nous voulons afficher lorsque l'utilisateur entre un texte. Cela crée essentiellement un simulateur de hacker qui fait apparaître du code à l'écran après avoir appuyé sur n'importe quelle touche.

```
import PlaygroundSupportimport UIKit
```

```
let arrayOfStrings = ["Alices-MacBook-Pro:~ Alice$", "override func viewDidLoad() {", "super.viewDidLoad()", "makeBackgroundGradient()", "addGradientToPortfolio()", "addGradientToTopBar()", "addGradientToTopBar()", "setupPopup()", "addTradeButton.titleLabel?.minimumScaleFactor = 0.5;", "addTradeButton.titleLabel?.minimumScaleFactor = 0.5;"]
```

```
var variableThatChanges : Int = 0
```

```
let frameOfMainView = CGRect(x: 0, y: 0, width: 1024, height: 768)
```

```
class MainViewController: UIViewController, UITextViewDelegate {
```

```
override func viewDidLoad() {
```

```
let view = UITextView(frame: CGRect(x: 0, y:0, width: 1024, height: 768))
```

```
self.view.frame = frameOfMainViewview.backgroundColor = .blackview.textColor = .greenview.font = UIFont(name: "Courier", size: 20)view.isEditable = trueview.delegate = self self.view.addSubview(view)
```

```
} 
```

```
func textView(_ textView: UITextView,
```

```
shouldChangeTextIn range: NSRange,
```

```
replacementText text: String) -> Bool {
```

```
if variableThatChanges == (arrayOfStrings.count - 1)
```

```
{
```

```
variableThatChanges = 0
```

```
}
```

```
let text = textView.text ?? ""
```

```
textView.text = text + "\n" + arrayOfStrings[variableThatChanges]
```

```
variableThatChanges += 1
```

```
return false
```

```
}
```

```
}
```

```
let master = MainViewController()
```

```
master.preferredContentSize = frameOfMainView.size
```

```
PlaygroundPage.current.liveView = master
```

Voici le code ci-dessus. Copiez-collez-le dans un Playground. Exécutez la vue en direct, et vous verrez un fond noir. Cliquez n'importe où sur le fond, et vous verrez un clavier apparaître dans l'interface utilisateur. Appuyez sur n'importe quelle touche et il vous montrera le code des chaînes.

Et voilà — vous avez créé un simulateur de hacker de base en moins de 50 lignes de code ! Maintenant, c'est à vous de jouer et d'être créatif avec Playgrounds ! ;)

### Quelques ressources géniales à consulter pour en apprendre plus

1. [Documentation Apple](https://developer.apple.com/swift/resources/).
2. Vidéos des sessions WWDC. Consultez [celle-ci](https://developer.apple.com/videos/play/wwdc2014/408/), [celle-ci](https://developer.apple.com/videos/play/wwdc2015/405/), [celle-ci](https://developer.apple.com/videos/play/wwdc2016/408/), et [celle-ci](https://developer.apple.com/videos/play/wwdc2017/408/), dans cet ordre.
3. [Playgrounds en profondeur à RWDevCon 2017.](https://videos.raywenderlich.com/courses/81-rwdevcon-2017-vault-tutorials/lessons/16?_ga=2.88303579.1903739137.1521645549-332591240.1521522583)
4. [La vidéo des Kaseys](https://youtu.be/rL9A0LeGxFg)
5. [Tutoriel Code tutsplus](https://code.tutsplus.com/tutorials/rapid-interactive-prototyping-with-xcode-playgrounds--cms-26637)
6. [Soumissions WWDC 2017](http://github.com/wwdc/2017/) et [WWDC 2018](https://github.com/wwdc/2018). Aussi, [awesome Swift Playgrounds](https://github.com/uraimo/Awesome-Swift-Playgrounds) à consulter et pour obtenir des idées.
7. [Un court chapitre d'un excellent livre.](http://www.techotopia.com/index.php/An_Introduction_to_Swift_Playgrounds)

C'est tout pour l'instant ! Suivez-moi sur [Medium](https://medium.com/@harshitaisanerd) ou [Twitter](https://twitter.com/aroraharshita33.). Téléchargez [une application](https://apple.co/2DUzTqa) que j'ai créée ! Découvrez une [startup géniale](https://www.producthunt.com/posts/cryptoshirt-by-woppal) que je conseille ! :)