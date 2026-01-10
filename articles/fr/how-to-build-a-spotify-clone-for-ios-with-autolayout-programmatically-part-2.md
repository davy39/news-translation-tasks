---
title: 'Comment construire programmatiquement un clone de Spotify pour iOS en utilisant
  AutoLayout : ajout de photos et mise à jour de l''UI'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-10T03:44:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-spotify-clone-for-ios-with-autolayout-programmatically-part-2
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/featured_image-4.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: app development
  slug: app-development
- name: autolayout
  slug: autolayout
- name: iOS
  slug: ios
- name: iOS13
  slug: ios13
- name: iphone
  slug: iphone
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: mobile
  slug: mobile
- name: programing
  slug: programing
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: User Interface
  slug: user-interface
seo_title: 'Comment construire programmatiquement un clone de Spotify pour iOS en
  utilisant AutoLayout : ajout de photos et mise à jour de l''UI'
seo_desc: "By Said Hayani\nThis is the second part of an article on building a Spotify\
  \ UI clone with autoLayout programmatically. If you missed the first part, no worries\
  \ - just please go and check it now. \nIn this article, we are going to add some\
  \ mocked pictur..."
---

Par Said Hayani

Il s'agit de la deuxième partie d'un article sur la création d'un clone de l'UI de Spotify avec AutoLayout de manière programmatique. Si vous avez manqué la première partie, pas de souci - il suffit d'aller [la consulter maintenant](https://www.freecodecamp.org/news/autolayout-programmatically-spotify-clone-in-swift/).

Dans cet article, nous allons ajouter des images simulées et essayer de faire en sorte que l'UI ressemble à celle de Spotify.

Voici ce que nous allons faire aujourd'hui ?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-09-at-9.55.19-PM-1.png)

Voici où nous nous sommes arrêtés dans la première partie :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/complet-layout-demo1.gif)

L'étape suivante consiste à créer des cellules personnalisées. Commençons donc par en créer une avec le nom `SubCustomCell`.

Tout d'abord, créez un nouveau fichier Swift dans le dossier du projet et nommez-le `SubCustomCell.swift`. Ce fichier contiendra notre cellule personnalisée qui représentera la Playlist. Après avoir créé le fichier, essayez d'ajouter le code ci-dessous et initialisez la cellule, peut-être avec `backgroundColor`, pour voir les changements d'UI lorsque nous enregistrons la cellule avec la `collectionView`.

```swift
import UIKit

class SubCustomCell: UICollectionViewCell {
        override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .red
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

Ensuite, nous enregistrons `SubCustomCell` à l'intérieur de `CustomCell.swift` dans le bloc `init`. Remplacez `UICollectionViewCell.self` par `SubCustomCell` comme ci-dessous.

```swift
 collectionView.register(SubCustomCell.self, forCellWithReuseIdentifier: cellId)
```

Nous devons également modifier la méthode `cellForItemAt` et la faire conformer à `SubCustomCell` comme suit.

```swift
 func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! SubCustomCell
        // cell.backgroundColor = .yellow
        
        return cell
    }
```

Vous devriez voir la couleur de fond changer en rouge.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-03-at-1.10.25-AM.png)
_Swift CustomCell_

Jusqu'à présent, tout devrait être simple et clair.

Maintenant, nous allons remplir les cellules avec des images simulées et créer un `ImageView` à l'intérieur de chaque cellule. J'ai déjà téléchargé quelques images aléatoires depuis [pexels.com](https://www.pexels.com/), mais n'hésitez pas à utiliser les images que vous souhaitez (y compris celles-ci). Vous pouvez les trouver dans les [fichiers du projet sur GitHub](https://github.com/hayanisaid/autoLayout-programmatically-in-swift).

Créons le `UIImageView` à l'intérieur de `SubCustomCell.swift` et ajoutons quelques contraintes.

```swift
    let ImageView : UIImageView = {
       let iv = UIImageView()
        iv.backgroundColor = .yellow
        return iv
        
    }()

```

Et ajoutez-le à la vue dans le bloc `init` en utilisant `addSubView`.

```swift
 override init(frame: CGRect) {
        super.init(frame: frame)
        addSubview(ImageView)
            
    }
```

Maintenant, faisons en sorte que `ImageView` occupe tout l'espace à l'intérieur de la cellule avec les contraintes ci-dessous.

```swift
 ImageView.translatesAutoresizingMaskIntoConstraints = false
            ImageView.topAnchor.constraint(equalTo: topAnchor).isActive = true
            ImageView.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
            ImageView.rightAnchor.constraint(equalTo: rightAnchor).isActive = true
            ImageView.bottomAnchor.constraint(equalTo: bottomAnchor).isActive = true
```

* `LeftAnchor` représente l'ancrage gauche de la cellule
* `rightAnchor` représente l'ancrage droit de la cellule
* `bottomAnchor` représente l'ancrage inférieur de la cellule
* `topAnchor` représente l'ancrage supérieur de la cellule

Et en rendant l'ancrage supérieur de `ImageView` égal à l'ancrage supérieur de la cellule (et en faisant de même pour les ancrages gauche, droit et inférieur de `ImageView`), cela fait en sorte que `ImageView` occupe tout l'espace de `SubCustomCell` (cellule).

Remarque : vous devez d'abord utiliser `translatesAutoresizingMaskIntoConstraints` pour pouvoir appliquer les contraintes aux éléments. N'oubliez pas non plus d'appeler la propriété `isActive` et de lui attribuer `true` - sans cela, les contraintes ne fonctionneront pas et rien ne changera.

`ImageView` devrait avoir une image, alors ajoutons-en une.

```swift
 let ImageView : UIImageView = {
       let iv = UIImageView()
        iv.backgroundColor = .yellow
        // nous avons un fichier >image1< à l'intérieur du projet
        iv.image = UIImage(named: "image1")
        iv.contentMode = .scaleAspectFill
        iv.clipsToBounds = true
      
        return iv
        
    }()
```

Et si vous construisez et exécutez l'application, vous devriez voir les résultats et l'image que nous avons ajoutés à `SubCustomCell`.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-03-at-1.37.51-AM.png)

Cool ?. Maintenant, il y a un élément que nous devons ajouter à `SubCustomCell` pour terminer. Nous avons besoin d'un titre qui représentera le titre de la playlist : `UILabel`.

Pour le titre, ce sera comme ceci :

```swift
 let TitleLabel : UILabel = {
        let lb = UILabel()
        lb.textColor = UIColor.lightGray
        lb.font = UIFont.systemFont(ofSize: 16)
        lb.font = UIFont.boldSystemFont(ofSize: 20)
        lb.text = "Musique du soir"
     
        return lb
    }()
```

J'ai simplement mis un texte aléatoire là-bas - vous pouvez mettre ce que vous voulez. L'étape suivante consiste à ajouter l'élément à la vue et à lui donner quelques contraintes. Le titre sera placé en bas de `ImageView`.

### Ajouter à la vue :

```swift
addSubview(TitleLabel)

```

### Appliquer les contraintes pour `ImageView` et `TitleLabel`

```swift
 ImageView.translatesAutoresizingMaskIntoConstraints = false
            ImageView.topAnchor.constraint(equalTo: topAnchor).isActive = true
            ImageView.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
            ImageView.rightAnchor.constraint(equalTo: rightAnchor).isActive = true
            ImageView.heightAnchor.constraint(equalToConstant: 240).isActive = true
            ImageView.bottomAnchor.constraint(equalTo: TitleLabel.topAnchor).isActive = true
            
           
           
            TitleLabel.translatesAutoresizingMaskIntoConstraints = false
            TitleLabel.topAnchor.constraint(equalTo: ImageView.bottomAnchor,constant: 10).isActive = true
            TitleLabel.leftAnchor.constraint(equalTo: leftAnchor, constant: 5).isActive = true
            TitleLabel.rightAnchor.constraint(equalTo: rightAnchor, constant: -5).isActive = true
```

Et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-06-at-1.45.10-AM.png)

Nous avons fait en sorte que l'image occupe la majeure partie de l'espace dans la cellule, et le reste est occupé par le titre. Comme vous pouvez le voir, vous pouvez faire défiler horizontalement dans chaque section et également verticalement sur tout l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/demo2.gif)

Maintenant, nous allons mettre des données simulées dans les cellules pour donner l'impression que c'est réel. Pour cela, j'ai créé un fichier `JSON` qui contient des données aléatoires pour les sections et les playlists.

Tout d'abord, créons deux structures, `Section` et `Playlist`. Nous créons un fichier séparé pour chaque structure.

`section.swift`

```swift
import Foundation
struct Section {
    var title : String
    var playlists : NSArray
    init(dictionary:[String : Any]) {
        self.title = dictionary["title"] as? String ?? ""
        self.playlists = dictionary["playlists"] as? NSArray ?? []
        
}
}


```

`playlist.swift`

```swift
//
//  playlist.swift
//  spotifyAutoLayout
//
//  Created by admin on 12/6/19.
//  Copyright © 2019 Said Hayani. All rights reserved.
//

import Foundation
struct PlayList {
    var title: String
    var image : String
    init(dictionary : [String : Any]) {
        self.title = dictionary["title"] as? String ?? ""
        self.image = dictionary["image"] as? String ?? ""
    }
   
}

```

Ensuite, à l'intérieur de `ViewController.swift`, nous créons une fonction qui récupère le JSON pour nous et stocke les résultats dans un tableau.

```swift

        print("tentative de récupérer Json")
        if let path = Bundle.main.path(forResource: "test", ofType: "json") {
            do {
                  let data = try Data(contentsOf: URL(fileURLWithPath: path), options: .mappedIfSafe)
                  let jsonResult = try JSONSerialization.jsonObject(with: data, options: .mutableLeaves)
                if let jsonResult = jsonResult as? [ Any] {
                            // faire des trucs
                    jsonResult.forEach { (item) in
                      
                        let section = Section(dictionary: item as! [String : Any])
                       // print("Récupération",section.playlists)
                        self.sections.append(section)
                    }
                    
                 
                  self.collectionView.reloadData()
                  }
              } catch {
                   // gérer l'erreur
              }
        }
    }
```

La fonction `fetchJson` est appelée dans la méthode `ViewDidLoad`. Nous avons également une variable appelée `sections` où nous stockons les résultats :

```swift
 var sections = [Section]()
```

L'étape suivante consiste à passer les données de `ViewController` à `CustomCell`. Pour cela, nous créons une variable à l'intérieur de `CustomCell` qui recevra les données pour chaque section :

```swift
 var section : Section?{
        didSet{
            print("section ✅",self.section)
        }
    }
```

Nous utilisons `cellForItemAt` à l'intérieur de la méthode `ViewController` pour passer les données directement à `CustomCell`.

```swift
override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! CustomCell
         
        cell.section = sections[indexPath.item]
         
        return cell
    }
```

Remarque : nous appelons toujours **`self`**.`collectionView.reloadData()` chaque fois que `fetchJson` est appelé, donc le bloc ci-dessous, à l'intérieur de `CustomCell`, sera également appelé. Vérifiez la console, `shift` + command + C :

```swift
 var section : Section? {
        didSet{
            print("section ✅",self.section)
        }
    }
```

La première chose que nous changeons est de définir le titre de la section :

```swift
 var section : Section? {
        didSet{
            print("section ✅",self.section)
            guard let section = self.section else {return}
            self.titleLabel.text = section.title
        }
    }
```

Et ensuite, vous devriez voir que chaque section a un titre spécifique à l'écran ?.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-06-at-3.23.32-AM.png)

Maintenant, il est temps de passer les données à `SubCustomCell`. Nous faisons la même chose que ci-dessus. Nous devons passer le tableau `playlists`, alors nous créons une variable nommée `playlists` à l'intérieur de `CustomCell`.

```swift
 var playlists : [PlayList]() //vide
```

Tout d'abord, nous parcourons les `playlists` depuis le `JSON`. Ensuite, nous ajoutons chaque playlist avec la variable `playlists`.

```swift
 var section : Section? {
        didSet{
            print("section ✅",self.section)
            guard let section = self.section else {return}
            self.titleLabel.text = section.title
            // ajouter au tableau playlists
             self.section?.playlists.forEach({ (item) in
                let playlist = PlayList(dictionary: item as! [String : Any])
                self.playlists.append(playlist)

            })
            self.collectionView.reloadData()
        }
    }
```

Attention ! Si vous essayez d'exécuter l'application, elle peut planter. Cela est dû au fait que nous avons oublié de définir le nombre de sections. Puisque nous recevons maintenant les données depuis JSON, le nombre devrait être dynamique en fonction du nombre de sections que nous avons. Le nombre de sections devrait être égal au nombre de sections à l'intérieur du `JSON`, donc nous devons modifier `numberOfItemsInSection` à l'intérieur de `ViewController` comme ci-dessous :

```swift
   override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return sections.count
    }
```

Nous faisons la même chose avec la même méthode à l'intérieur de `CustomCell.swift` - mais ici, nous considérons le nombre de `playlists` à la place.

```swift
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return  self.playlists.count
    }
```

La dernière étape que nous devons compléter est de passer chaque objet `playlist` à `SubCustomCell` dans `cellForItemAt` dans `CustomCell.swift`.

```swift
 func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! SubCustomCell
        // ici ?
        cell.playlist = playlists[indexPath.item]
        return cell
    }
```

Et nous allons récupérer ces données à l'intérieur de `SubCustomCell` via la variable `playlist` et enfin afficher le titre et l'image de la playlist.

```swift
var playlist : PlayList? {
           didSet{
               print("Playlist ?",self.playlist)
            guard let playlist = self.playlist else {return}
            // L'image ?
            self.ImageView.image = UIImage(named: playlist.image)
            // le titre de la playlist ?
            self.TitleLabel.text = self.playlist?.title
               
           }
       }
```

Je pense que tout devrait fonctionner correctement maintenant, comme ci-dessous ?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/demo3.gif)

Une dernière mise à jour de l'UI : nous devons ajouter un peu de remplissage et de marges aux titres des `section` et `playlist` et rendre la playlist un peu plus petite.

Commençons par ajouter un peu de remplissage pour les titres de section. Pour cela, nous devons simplement donner à la propriété `constant` une valeur numérique à l'intérieur de la cellule de section `CustomCell` et dans `setupSubCells` :

```swift
 collectionView.topAnchor.constraint(equalTo: titleLabel.bottomAnchor,constant: 15).isActive = true
```

Et si vous voyez toute la `collectionView` arriver en bas du `titleLabel`, tout ce que nous devons faire est d'ajouter plus d'espace en ajoutant `15` :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/paddingForTitles-1.png)

Ensuite, nous passons au titre de la `playlist`. Cela sera à l'intérieur de `SubCustomCell`, et nous devons simplement ajouter plus d'espace en bas de l'ImageView.

```swift
 ImageView.bottomAnchor.constraint(equalTo: TitleLabel.topAnchor,constant: -15).isActive = true
```

Nous avons déjà la constante là. Pour qu'elle fonctionne, la valeur doit être `-15`

![Image](https://www.freecodecamp.org/news/content/images/2019/12/demo4.gif)

Enfin, la playlist doit être un peu plus petite. C'est facile : nous faisons simplement en sorte que la hauteur et la largeur de la cellule `playlist` soient égales à la hauteur de la cellule `section` divisée par 2, comme ci-dessous :

`CustomCell.swift`

```swift
 func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        
        let width = frame.height / 2
        let height = frame.height / 2
        
        return CGSize(width: width, height: height)
        
    }
```

Faites également en sorte que la hauteur de l'ImageView soit égale à `150`.

```swift
  //SubCutomCell.swift
  ImageView.heightAnchor.constraint(equalToConstant: 150).isActive = true
```

Et voilà ?.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Screen-Shot-2019-12-09-at-9.55.19-PM.png)

Parfait ! Je pense que c'est suffisant pour aujourd'hui - je ne veux pas rendre cet article trop long. Nous aurons donc une autre partie où nous ajouterons la `TabBar` et la description, ainsi que quelques icônes pour la playlist.

**Voir le** [**code source complet sur GitHub**](https://github.com/hayanisaid/autoLayout-programmatically-in-swift)**?.**

Merci pour votre temps. J'espère n'avoir rien oublié. Si c'est le cas, veuillez me mentionner sur [Twitter](https://twitter.com/SaidHYN), ou si vous avez des questions ou une addition à cet article, les portes sont toujours ouvertes à tous. Merci ??.

**[Abonnez-vous](https://webege.us16.list-manage.com/subscribe?u=311846a57d1e1a666287ad128&id=2b386b2ebb)** _à ma liste de diffusion pour être informé lorsque la troisième partie de ce tutoriel sera publiée._



> Au fait, j'ai récemment travaillé avec un groupe solide d'ingénieurs logiciels pour l'une de mes applications mobiles. L'organisation était excellente, et le produit a été livré très rapidement, beaucoup plus vite que d'autres entreprises et freelances avec lesquels j'ai travaillé, et je pense que je peux honnêtement les recommander pour d'autres projets. Envoyez-moi un email si vous souhaitez entrer en contact - [said@devsdata.com](mailto:said@devsdata.com).