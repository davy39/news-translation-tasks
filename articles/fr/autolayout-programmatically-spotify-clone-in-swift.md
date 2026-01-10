---
title: Comment créer un clone de Spotify pour iOS avec AutoLayout de manière programmatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-03T01:04:14.000Z'
originalURL: https://freecodecamp.org/news/autolayout-programmatically-spotify-clone-in-swift
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/featured_image-2.png
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: mobile app development
  slug: mobile-app-development
- name: programing
  slug: programing
- name: Swift
  slug: swift
- name: technology
  slug: technology
- name: Xcode
  slug: xcode
seo_title: Comment créer un clone de Spotify pour iOS avec AutoLayout de manière programmatique
seo_desc: 'By Said Hayani

  In this post we will try to re-create the Spotify home screen layout in Swift programmatically.
  Why programmatically? I think it''s always good to know how to build things in different
  ways, and I like to write code to do things program...'
---

Par Said Hayani

Dans cet article, nous allons essayer de recréer la disposition de l'écran d'accueil de Spotify en Swift de manière programmatique. Pourquoi de manière programmatique ? Je pense qu'il est toujours bon de savoir comment construire des choses de différentes manières, et j'aime écrire du code pour faire les choses de manière programmatique. Ces compétences sont particulièrement utiles si vous travaillez en équipe ou utilisez le contrôle de version. 

    

![Image](https://www.freecodecamp.org/news/content/images/2019/11/spotify-demo.gif)

Voici l'écran d'accueil réel de l'application mobile Spotify. Pour atteindre ce type de disposition, nous allons utiliser `UICollectionView`, et nous pourrions également utiliser `TabBarController` pour créer le navigateur à onglets.

> Prérequis de base : assurez-vous d'avoir Xcode +10 installé et Swift +4.

Commençons par créer un nouveau projet Xcode en utilisant Xcode :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-10-31-at-8.03.13-PM.png)

Et la première chose que nous devons faire dans `ViewController.swift` est de changer la superclasse en `UICollectionViewController` au lieu de `UIViewController` car notre classe sera basée sur `collectionView`.

```swift
//
//  ViewController.swift
//  spotifyAutoLayout
//
//  Created by admin on 10/31/19.
//  Copyright © 2019 Said Hayani. All rights reserved.
//

import UIKit

class ViewController: UICollectionViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        collectionView.backgroundColor = .purple
        // Do any additional setup after loading the view.
    }


}

```

Si vous essayez d'exécuter l'application, la construction échouera. Nous devons ajouter du code au fichier `AppDelegate.swift` dans la fonction `didFinishLaunchingWithOptions` avant l'instruction `return` :

```swift
  let layout = UICollectionViewFlowLayout()
        window = UIWindow()
        window?.rootViewController = ViewController(collectionViewLayout: layout)
```

Et le code devrait ressembler à ceci :

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        let layout = UICollectionViewFlowLayout()
        window = UIWindow()
        window?.rootViewController = ViewController(collectionViewLayout: layout)
        return true
    }
```

Maintenant, vous devriez pouvoir exécuter l'application et voir la `backgroundColor` changée en `purple` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/first-look.png)

L'étape suivante consiste à distribuer la disposition et à diviser l'espace également entre les sections.

Définissons les méthodes de notre `CollectionView`.

Les étapes :

* Enregistrer une cellule réutilisable avec un identifiant unique
* Définir le nombre d'éléments dans la section
* Utiliser la cellule enregistrée   

Pour utiliser certaines des méthodes de `CollectionView`, nous devons toujours nous conformer à `UICollectionViewDelegateFlowLayout` en tant que superclasse et obtenir l'autocomplétion des méthodes. Commençons donc par enregistrer la CollectionViewCell.

À l'intérieur de `View.DidLoad()`, nous appelons la méthode `collectionView.register()` pour enregistrer la cellule réutilisable :

```swift
  collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: cellId)
```

Ensuite, nous définissons le nombre de cellules que nous aurons à l'intérieur de `collectionView` en utilisant `numberOfItemsInSection`. Pour l'instant, nous avons juste besoin de faire 5 éléments :

```swift
 override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 5
    }
```

L'étape suivante consiste à définir la cellule réutilisable en utilisant `cellForItemAt` qui doit retourner `UICollectionViewCell` et avoir un identifiant unique appelé `cellId`. Le code ressemble à ceci :

```swift
 override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
        cell.backgroundColor = .red
        return cell
    }
```

Le code complet devrait ressembler à ceci :

```swift
import UIKit

class ViewController: UICollectionViewController, UICollectionViewDelegateFlowLayout {
    let cellId : String = "cellId"

    override func viewDidLoad() {
        super.viewDidLoad()
        collectionView.backgroundColor = .purple
        collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: cellId)

    }


    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 5
    }
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
        cell.backgroundColor = .red
        return cell
    }

}
```

Vous devriez pouvoir voir 5 éléments avec des arrière-plans rouges à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/cellItem.png)

## Ajouter une largeur et une hauteur personnalisées aux cellules

Maintenant, nous devons placer les cellules dans le bon ordre et leur donner une `width` et une `height`. Chaque cellule prendra la `width` de l'écran comme `width`.

Nous avons la chance d'avoir la méthode `sizeForItemAt` afin de pouvoir donner aux cellules une `width` et une `height` personnalisées. C'est une méthode qui doit retourner un type `CGSize` :

```swift
 func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let width = view.frame.width
        let height = CGFloat(200)
        
        return CGSize(width: width, height: height)
    }
```

Nous avons donc fait en sorte que la `Cell` prenne la `width` de l'écran en utilisant `view.frame.width` et une `height` personnalisée qui est de type `CGFloat`.

Maintenant, vous pouvez voir le résultat ci-dessous dans votre simulateur :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-10-31-at-9.05.46-PM.png)

Tout semble bien jusqu'à présent. Cette fois, créons une cellule personnalisée qui peut être réutilisable. Créez un nouveau fichier Swift nommé `CustomCell` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-10-31-at-11.52.10-PM.png)

`CustomCell.swift` devrait ressembler à ceci :

```swift

import UIKit

class CustomCell: UICollectionViewCell {
    override init(frame: CGRect) {
        super.init(frame: frame)
        
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```

Maintenant, les prochaines choses que nous devons faire sont de modifier deux méthodes pour supporter la cellule réutilisable, `collectionView.register` et `cellForItemAt`. Commençons par modifier la méthode d'enregistrement. Remplacez `UICollectionViewCell.self` par `CustomCell` :

```swift
 collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: cellId)

```

Ensuite, nous devons caster `cellForItemAt` pour qu'il se conforme à `CustomCell` comme ci-dessous :

```swift
  let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! CustomCell
```

Si vous exécutez l'application, vous ne remarquerez probablement aucun changement, alors donnez à la CustomCell une couleur d'arrière-plan `backgroundColor = .yellow`. N'oubliez pas de supprimer la ligne `cell.backgroundColor = .red` dans `cellForItemAt`. Vous devriez voir la couleur d'arrière-plan changée en jaune ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-01-at-12.13.20-AM.png)

Maintenant, il est temps de mettre un peu de sel dans `CutomCell` :D

Si vous regardez l'écran d'accueil de Spotify, chaque section qui est une `CustomCell` dans notre exemple contient un titre de section, des sous-cellules, et est horizontale :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/spotify-demo-1.gif)

## Ajouter un titre de section

Ajoutons une étiquette de titre à la cellule. Créez l'élément `titleLabel` à l'intérieur de la classe `CutomCell` :

```swift
let titleLabel: UILabel = {
        let lb  = UILabel()
        lb.text = "Titre de la section"
        lb.font = UIFont.boldSystemFont(ofSize: 14)
        lb.font = UIFont.boldSystemFont(ofSize: 14)
        
        return lb
    }()
```

Ensuite, ajoutez l'élément à la vue à l'intérieur du bloc `init()` :

```swift
addSubview(titleLabel)
```

Si vous exécutez l'application, vous ne verrez aucun changement, et c'est parce que nous n'avons pas encore mis de contrainte à l'élément. Alors, ajoutons quelques contraintes – ajoutez cette propriété `lb.translatesAutoresizingMaskIntoConstraints = false` à `titleLabel` pour pouvoir appliquer des contraintes à l'élément :

Après avoir ajouté `titleLabel` à la vue, nous définissons les contraintes :

```swift
 addSubview(titleLabel)
titleLabel.topAnchor.constraint(equalTo: topAnchor, constant: 8).isActive = truetitleLabel.leftAnchor.constraint(equalTo: leftAnchor,constant: 8 ).isActive = true
```

Assurez-vous toujours d'ajouter la propriété `.isActive = true` – sans elle, la contrainte ne fonctionnera pas !		

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-01-at-12.32.55-AM.png)

Avant de passer à la partie suivante, changeons d'abord la couleur d'arrière-plan de l'écran en noir et supprimons également la couleur jaune des cellules :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-01-at-12.46.01-AM.png)

Maintenant vient la grande partie : mettre des sous-cellules dans chaque cellule. Pour y parvenir, nous allons ajouter un `CollectionView` à l'intérieur de `CustomCell`.

Pour ajouter un `CollectionView` à l'intérieur de `UICollectionViewCell`, nous devons ajouter les propriétés `UICollectionViewDelegate`, `UICollectionViewDelegateFlowLayout` et `UICollectionViewDataSource` en tant que superclasse à `CustomCell`.

Créons l'élément `collectionView` comme n'importe quelle vue simple :

```swift

    let collectionView : UICollectionView = {
        // init the layout
        let layout = UICollectionViewFlowLayout()
        // set the direction to be horizontal
        layout.scrollDirection = .horizontal
        
        // the instance of collectionView
        
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
       
        // Activate constaints
      
        cv.translatesAutoresizingMaskIntoConstraints = false
        
        return cv
        
    }()
```

Remarquez que nous ajoutons `layout` au `collectionView` en tant que couche dans l'initialiseur comme nous l'avons fait la première fois avec le `viewController.swift`. Ici, nous spécifions également la direction du `FlowLayout` pour qu'elle soit `.horizontal`.

Ajoutons l'élément `collectionView` à la vue en tant que sous-vue.

Nous allons créer une fonction qui fait cela pour nous afin de rendre le code un peu plus propre.

```swift
    fileprivate  func setupSubCells(){
        // add collectionView to the view
        addSubview(collectionView)
 
        collectionView.dataSource = self
        collectionView.delegate = self
        // setup constrainst
        // make it fit all the space of the CustomCell
        collectionView.topAnchor.constraint(equalTo: titleLabel.bottomAnchor).isActive = true
        collectionView.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
        collectionView.bottomAnchor.constraint(equalTo: bottomAnchor).isActive = true
        collectionView.rightAnchor.constraint(equalTo: rightAnchor).isActive = true
    }

```

Assurez-vous de définir le délégué à `self` pour le `collectionView` et la source de données également :

  `collectionView.dataSource = self`

   `collectionView.delegate = self` 

Ensuite, appelez la fonction dans le bloc `init`.

Xcode affichera certaines erreurs si vous essayez de construire l'application car nous ne nous conformons pas aux protocoles `UICollectionViewDelegate` et `UICollectionViewDelegateFlowLayout`. Pour corriger cela, nous devons d'abord enregistrer la sous-cellule en tant que cellule réutilisable.

Créez une variable en haut de la classe et donnez-lui un nom de `cellId` afin que nous puissions l'utiliser lorsque nous avons besoin de l'identifiant de cellule : 

`let cellId : String = "subCellID"`

```swift
collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: cellId)
```

Maintenant, il nous manque deux méthodes pour faire disparaître les erreurs : `numberOfItemsInSection` qui définit le nombre de cellules dans la section et `cellForItemAt` qui définit la cellule réutilisable. Ces méthodes sont nécessaires pour que `collectionView` fonctionne correctement :

```swift
 // number of cells
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
       return  4
    }
    
    // reusable Cell
     func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
         cell.backgroundColor = .yellow
        
        return cell
    }
```

Les résultats devraient ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-01-at-1.40.42-AM.png)

Comme vous pouvez le voir, les `collectionView` sont en violet en arrière-plan et les sous-cellules sont jaunes.

Les dernières choses que nous pouvons faire avant de terminer cet article sont de faire en sorte que les `subCells` aient la hauteur de la section et la largeur. Encore une fois, nous utilisons `sizeForItemAt` pour définir la `height` et la `width` de la cellule.

```swift
 func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        
        let width = frame.height
        let height = frame.height
        
        return CGSize(width: width, height: height)
        
    }
```

Et nous y voilà ?:

![Image](https://www.freecodecamp.org/news/content/images/2019/11/complet-layout-demo1.gif)

GÉNIAL ! Je vais m'arrêter à ce stade pour que cet article ne soit pas trop long. Je ferai une deuxième partie où nous allons ajouter quelques images simulées et les remplir avec des données.

### Code source complet ? [ici](https://github.com/hayanisaid/autoLayout-programmatically-in-swift)

S'il vous plaît, si vous avez des ajouts, des questions ou des corrections, postez-les dans les commentaires ci-dessous ? ou contactez-moi sur [Twitter](https://twitter.com/SaidHYN).

**[Abonnez-vous](https://webege.us16.list-manage.com/subscribe?u=311846a57d1e1a666287ad128&id=2b386b2ebb)** à ma liste de diffusion pour être informé lorsque la deuxième partie de ce tutoriel sera publiée.