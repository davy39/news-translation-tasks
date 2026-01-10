---
title: Comment commencer avec la réalité augmentée en Swift, la manière facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T22:09:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-ar-in-swift-the-easy-way-7399fe1c82f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gf3uExB7i8IDfN-s3_tcLw.png
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment commencer avec la réalité augmentée en Swift, la manière facile
seo_desc: 'By Ranadhir Dey

  If you look around, this is the golden era of technology. Every keynote adds something
  new to the existing stack of technologies. It’s exciting to see how these emerging
  technologies have enhanced the boundaries of our imagination. As...'
---

Par Ranadhir Dey

Si vous regardez autour de vous, c'est l'âge d'or de la technologie. Chaque keynote ajoute quelque chose de nouveau à la pile existante de technologies. C'est passionnant de voir comment ces technologies émergentes ont repoussé les limites de notre imagination. En tant que développeur, nous devons être fiers d'être les premiers utilisateurs de ces technologies.

Mais chaque nouvelle technologie vient avec une courbe d'apprentissage assez raide. Vous ne pouvez pas simplement regarder une keynote ou une vidéo sur YouTube et commencer à développer une application. Mais la bonne nouvelle est qu'avec la réalité augmentée en Swift, il est remarquablement facile de travailler avec des applications AR basiques. Apple a fait la plupart du travail difficile pour vous. Suivez le guide et vous verrez à quel point cela peut être facile.

### **Commençons...**

Dans ce tutoriel, nous allons apprendre les outils et techniques nécessaires de la réalité augmentée en Swift qui nous permettront de créer une application qui décore votre sol avec des carrelages et des textures en bois. L'application finale ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vO7XUgbwu9-jNCpzzBts8M-Q4ObnFsVmSCBB)

Commençons par créer une application **single view** dans Xcode et nommons-la Home Decor.

![Image](https://cdn-media-1.freecodecamp.org/images/vcKpo7OKMJJrjoVC4NUEaj3CK0ZTDVn1B9kc)

### **Ajout des permissions de la caméra**

La toute première chose que nous allons faire est de naviguer vers le fichier info.plist et d'activer l'utilisation de la caméra. La capacité de la caméra est la première chose dont vous avez besoin pour une application AR. Trouvez la clé Camera Usage Description, comme sur l'image ci-dessous, et donnez-lui un message approprié. Ce message apparaîtra au tout premier lancement de l'application lors de la demande des permissions de la caméra à l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/nXNhGVVjq4c-CAFVSXuDotT1p4OI44-GWugJ)

### **Ajout des capacités ARKit à l'application**

Allez dans Main.storyboard. Faites glisser et déposez une vue ARKit SceneKit sur le ViewController et épinglez l'ARSCNView aux bords du ViewController.

![Image](https://cdn-media-1.freecodecamp.org/images/mw2nLyGFYWFvXMOtDFrZqCHentFfkfQu2LFu)

Créez un IBOutlet dans la classe ViewController, et nommez-le sceneView. Dès que vous faites cela, une erreur indiquant **undeclared ARSCNView** apparaîtra, car notre contrôleur de vue ne reconnaît rien de type ARSCNView. Pour résoudre cela, et pour utiliser d'autres fonctionnalités d'ARKit, nous devons importer ARKit dans le contrôleur de vue.

![Image](https://cdn-media-1.freecodecamp.org/images/vqFrntUcNDJ0ySI-E9hIWjLttHQ3bv24PPRU)

Maintenant, passez du storyboard au fichier view controller.swift. Déclarez une propriété de type ARWorldTrackingConfiguration avant la méthode viewDidLoad() et nommez-la config. Et notre contrôleur de vue ressemblera à ceci (j'ai supprimé la méthode didReceiveMemoryWarning) :

```
import UIKit
import ARKit
```

```
class ViewController: UIViewController {
```

```
@IBOutlet weak var sceneView: ARSCNView!
let config = ARWorldTrackingConfiguration()
```

```
override func viewDidLoad() {
    super.viewDidLoad()
}
```

### **Autoriser le débogage**

Cette variable config déterminera les configurations de la session de la scène. Nous verrons son utilisation plus tard dans la section. Maintenant, dans la méthode viewDidLoad après super.viewDidLoad(), ajoutez ce qui suit :

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

Ici, nous activons les options de débogage pour notre sceneView, qui n'est rien d'autre que la vue de la caméra avec les capacités du framework AR. ARSCNDebugOptions.showWorldOrigin affichera l'origine du monde à l'écran. Cela nous aidera à trouver le point de référence de toutes les autres positions. ARSCNDebugOptions.showFeaturePoints affichera tous les points à l'écran que la caméra AR a reconnus dans les environs.

Maintenant, pour démarrer la session AR, nous devons exécuter une session dans notre sceneView avec les configurations mentionnées dans la variable config. Juste en dessous de la ligne sceneView.debugOptions, écrivez :

```
sceneView.session.run(config)
```

Maintenant, exécutez l'application sur votre appareil (pas sur un simulateur, car il n'a pas de caméra). L'alerte demandant les permissions de la caméra avec le message que vous avez écrit apparaîtra, et vous devez l'autoriser. Attendez un peu pendant qu'il charge l'origine du monde.

![Image](https://cdn-media-1.freecodecamp.org/images/nfQfMj9tFFxVpQ02jfMQpFttyDtiWLo-HAJV)

Si vous êtes ici, vous avez déjà une application AR en cours d'exécution. Félicitations !

### **Comment fonctionnent les axes AR**

La barre rouge ou l'axe X est utilisée pour positionner les objets à gauche ou à droite de l'origine du monde. La barre verte ou l'axe Y est utilisée pour positionner les objets en haut ou en bas de l'origine du monde. Et la barre bleue ou l'axe Z est utilisée pour déterminer à quelle distance un objet sera placé de l'origine du monde.

Une valeur positive de X positionnera un objet à droite de l'origine du monde, et une valeur négative le placera à gauche. Une valeur positive pour Y le placera en haut et une valeur négative le placera en bas de l'origine du monde. Une valeur positive pour Z le placera plus près, et une valeur négative le placera plus loin de l'origine du monde.

### **Ajout d'un objet virtuel**

Ajoutons quelques objets virtuels à la scène. Une capsule 3D serait un bon choix. Déclarez un capsuleNode de type [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode?changes=_8) et donnez-lui une géométrie de [capsule](https://developer.apple.com/documentation/scenekit/scncapsule?changes=_5). Donnez-lui une hauteur de 0,1 mètre et un rayon de 0,03 mètre.

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1))
```

Maintenant, positionnez-la à 0,1 mètre à gauche de l'origine du monde, à 0,1 mètre au-dessus de l'origine du monde et à 0,1 mètre de l'origine du monde :

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

Maintenant, ajoutez le nœud à la scène :

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

La sceneView contient une scène qui est responsable de contenir tous les objets 3D au format SCNNode qui formeront la scène 3D. Nous ajoutons la capsule au nœud racine de la scène. La position du nœud racine est exactement alignée sur la position de l'origine du monde. Cela signifie que sa position est (0,0,0).

Actuellement, notre méthode viewDidLoad ressemble à ceci :

```
override func viewDidLoad() {
```

```
super.viewDidLoad()
```

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

```
sceneView.session.run(config)
```

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1))
```

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

```
}
```

Maintenant, exécutez l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/oWdSpOkroOQI7EuYJZ8-HAix6Xdg2tim75NN)

Cool ! Nous avons juste positionné un objet virtuel dans le monde réel. Vous pouvez jouer avec différentes positions et différentes [géométries](https://developer.apple.com/documentation/scenekit/scngeometry) pour explorer davantage. Maintenant, faisons tourner la capsule de 90 degrés autour de l'axe Z afin qu'elle repose à plat sur l'axe X et changeons sa couleur en bleu.

### **Angles d'Euler**

Les angles d'Euler sont responsables de l'angle d'affichage d'un SCNNode. Nous verrons comment les utiliser pour faire tourner la capsule.

Chaque SCNGeometry peut avoir des matériaux ajoutés, qui définissent l'apparence de la géométrie. Les matériaux ont une propriété diffuse qui, lorsqu'elle est définie, étale son contenu sur toute la géométrie.

Dans viewDidLoad, ajoutez les lignes suivantes après avoir défini la position de la capsule.

```
capsuleNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue //1
capsuleNode.eulerAngles = SCNVector3(0,0,Double.pi/2)//2
```

Ici, dans la première ligne, nous définissons la couleur bleue pour le tout premier matériau du nœud qui s'étalera sur la capsule et la fera paraître bleue. Dans la ligne 2, nous définissons l'angle d'Euler Z à 90 degrés radians. Enfin, notre vue se charge et ressemble à ceci :

```
override func viewDidLoad() {
```

```
super.viewDidLoad()
```

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

```
sceneView.session.run(config)
```

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1))
```

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

```
capsuleNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue //1
```

```
capsuleNode.eulerAngles = SCNVector3(0,0,Double.pi/2)//2
```

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

```
}
```

Maintenant, exécutez l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/KRIWB1PKTsTUtgcALCZrbEIKFxyFAsOOJr3M)

Super ! Une capsule bleue couchée sur le mur ! Vous pouvez même ajouter des textures comme contenu diffus pour faire paraître un objet plus réaliste. Nous utiliserons cela dans la prochaine section lorsque nous placerons les textures des carrelages sur le sol.

Maintenant que nous avons réussi à placer des objets virtuels dans le monde réel, il est temps de décorer notre vrai sol avec des carrelages virtuels. Pour obtenir l'effet de sol, nous utiliserons une géométrie [SCNPlane](https://developer.apple.com/documentation/scenekit/scnplane). SCNPlane n'a pas de profondeur comme les autres géométries 3D, ce qui en fait un choix parfait pour notre application.

### **Délégations ARSCENEView**

Avant de commencer la détection du sol, nous allons explorer certaines méthodes de délégué de notre sceneView pour comprendre quelles capacités nous avons pour interagir avec une session AR en cours.

```
func renderer(SCNSceneRenderer, didAdd: SCNNode, for: ARAnchor)
```

Chaque fois que nous déplaçons ou inclinons notre appareil avec une session AR en cours, ARKit essaie de trouver différents ARAnchors dans les environs. Un [ARAnchor](https://developer.apple.com/documentation/arkit/aranchor) contient des informations sur une position et une orientation du monde réel qui peuvent être utilisées pour placer un objet.

Une fois qu'un ancrage différent est trouvé, un nouveau nœud est ajouté à la scène avec les mêmes informations pour accommoder cet ancrage nouvellement trouvé. Cette méthode de délégué nous informera de cela. Nous l'utiliserons pour trouver toutes les positions sur le sol afin de placer les carrelages.

```
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor)
```

La plupart du temps, tous les nœuds qui sont ajoutés à partir des ancrages appartiennent au même objet. Supposons que vous vous déplaciez autour du sol et que l'appareil trouve un certain nombre d'ancrages à différentes positions. Il essaie d'ajouter tous les nœuds pour ces ancrages, car il pense que tous ces ancrages appartiennent à des objets différents.

Mais ARKit reconnaît finalement que tous ces ancrages appartiennent au même sol, il met donc à jour le tout premier nœud de sol en ajoutant les dimensions des autres nœuds dupliqués. Cette méthode de délégué nous informera de cela.

```
func renderer(SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)
```

Après avoir mis à jour le premier nœud unique avec les dimensions de tous les autres nœuds dupliqués, ARKit supprime tous les nœuds dupliqués et la méthode de délégué nous en informe. Nous utiliserons toutes les méthodes de délégué ci-dessus dans notre application (et leur but deviendra plus clair).

### **Détection du plan**

Actuellement, notre scène essaie de rassembler tous les ancrages qu'elle rencontre, car c'est le comportement par défaut. Mais comme un sol est une surface horizontale, nous ne sommes intéressés que par les ancrages qui se trouvent sur des plans horizontaux. Retournez donc à notre méthode viewDidLoad et écrivez le code ci-dessous **avant** d'exécuter la session (c'est-à-dire avant la ligne sceneView.session.run(config)).

```
config.planeDetection = .horizontal
```

Dans la méthode viewDidLoad, vous pouvez supprimer tout ce qui se trouve après sceneView.session.run(config) car cela servait à placer la capsule à l'écran et nous n'en avons plus besoin. Puisque nous allons utiliser toutes les méthodes de délégué mentionnées ci-dessus, nous devons faire de notre viewController un délégué de la sceneView. Avant l'accolade fermante de la méthode viewDidLoad(), ajoutez la ligne suivante.

```
sceneView.delegate = self
```

Vous devriez obtenir une erreur maintenant, car notre contrôleur de vue ne se conforme toujours pas au délégué de la sceneView. Pour implémenter cela, créons une extension du contrôleur de vue à la fin du fichier ViewController.swift.

```
extension ViewController:ARSCNViewDelegate{}
```

La méthode de délégué didAdd SCNNode sera déclenchée chaque fois qu'une partie du sol est découverte et qu'un nouveau nœud est ajouté à la scène en fonction de l'ancrage. Dans cette méthode, nous créerons un nœud de sol et l'ajouterons en tant qu'enfant du nœud récemment ajouté à la position de l'ancrage.

[ARArchor](https://developer.apple.com/documentation/arkit/aranchor) peut être de quatre types différents pour résoudre quatre objectifs différents. Ici, nous ne sommes intéressés que par ARPlaneAnchor qui détecte les plans horizontaux ou verticaux.

### **Création de nœuds de sol AR**

Créons une fonction qui recevra un ARPlaneAnchor en tant que paramètre, créera un nœud de sol à la position de l'ancrage et le retournera.

```
func createFloorNode(anchor:ARPlaneAnchor) ->SCNNode{
```

```
let floorNode = SCNNode(geometry: SCNPlane(width: CGFloat(anchor.extent.x), height: CGFloat(anchor.extent.z))) //1
```

```
floorNode.position=SCNVector3(anchor.center.x,0,anchor.center.z)                                               //2
```

```
floorNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue                                             //3
```

```
floorNode.geometry?.firstMaterial?.isDoubleSided = true                                                        //4
```

```
floorNode.eulerAngles = SCNVector3(Double.pi/2,0,0)                                                    //5
```

```
return floorNode                                                                                               //6
```

```
}
```

Passons en revue la fonction ligne par ligne et discutons-en plus en détail. Veuillez suivre la description de chaque ligne, car c'est la partie la plus délicate.

1. Nous créons un nœud avec une géométrie de SCNPlane qui a la taille de l'ancrage. L'étendue de ARPlaneAnchor contient les informations de position. Le fait que l'étendue.z ait été utilisée comme hauteur et non l'étendue.y peut être un peu déroutant. Si vous visualisez qu'un cube 3D est placé sur un sol et que vous voulez le rendre plat le long d'une surface 2D, vous changeriez le y en zéro et il deviendrait plat. Maintenant, pour obtenir la longueur de cette surface 2D, vous considéreriez le z, n'est-ce pas ? Notre sol est plat, donc nous avons besoin d'un nœud plat et non d'un cube.

2. Nous définissons la position du nœud. Comme nous n'avons pas besoin d'élévation, nous mettons y à zéro.

3. Définissez la couleur du sol en bleu.

4. La couleur du matériau ne sera affichée que sur un seul côté, sauf si nous mentionnons spécifiquement qu'il est double face.

5. Par défaut, le plan sera placé verticalement. Pour le rendre horizontal, nous devons le faire tourner de 90 degrés.

### **Implémentation des méthodes de délégué**

Maintenant, implémentons la méthode de délégué didAdd SCNNode.

```
func renderer(_ renderer: SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor) {
```

```
guard let planeAnchor = anchor as? ARPlaneAnchor else {return} //1
```

```
let planeNode = createFloorNode(anchor: planeAnchor) //2
```

```
node.addChildNode(planeNode) //3
```

```
}
```

À la ligne 1, nous vérifions si l'ancrage est un ARPlaneAnchor, car nous ne traiterons que ce type d'ancrage.

À la ligne 2, un nouveau nœud est créé en fonction de l'ancrage. À la ligne 3, il est ajouté au nœud.

Maintenant, dans le délégué didUpdate SCNNode, nous allons supprimer tous nos nœuds de sol. Nous allons faire cela parce que les dimensions du nœud actuel ont été modifiées et que les anciens nœuds de sol ne correspondront plus. Ensuite, nous allons à nouveau ajouter un nouveau nœud de sol à ce nœud mis à jour.

```
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {
```

```
guard let planeAnchor = anchor as? ARPlaneAnchor else {return}
```

```
node.enumerateChildNodes { (node, _) in
```

```
node.removeFromParentNode()
```

```
}
```

```
let planeNode = createFloorNode(anchor: planeAnchor)
```

```
node.addChildNode(planeNode)
```

```
}
```

Dans la méthode de délégué didRemove SCNNode, nous voulons nettoyer tous nos nœuds indésirables de manière civilisée.

```
func renderer(_ renderer: SCNSceneRenderer, didRemove node: SCNNode, for anchor: ARAnchor) {
```

```
guard let _ = anchor as? ARPlaneAnchor else {return}
```

```
node.enumerateChildNodes { (node, _) in
```

```
node.removeFromParentNode()
```

```
}
```

```
}
```

Ouf ! C'est tout ! Exécutez l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/3wVNiLmgzrS3Hjqr7lyE4wQJIssiklvQKZOk)

### **Ajout de l'effet de carrelage**

Attendez, quoi ? Un sol bleu ? Non, nous n'avons pas encore complètement terminé. Juste un petit changement et nous aurons un sol magnifique !

Pour changer le sol bleu en carrelage, nous avons besoin d'une texture. Faisons une recherche sur Google pour une texture de carrelage de sol. J'ai recherché "wooden floor texture" et j'ai trouvé de belles images de texture. Enregistrez l'une d'entre elles sur votre Mac et glissez-la dans les Assets.xcassets.

![Image](https://cdn-media-1.freecodecamp.org/images/k9pct70eqbORC5u5WnCgSPOb5cYSmN9hoKmC)

Je l'ai nommée WoodenFloorTile. Vous pouvez la nommer comme vous le souhaitez. Retournez au fichier ViewController.swift. Dans la fonction createFloorNode, au lieu de définir UIColor.blue comme contenu diffus, faites-en une UIImage avec le nom que vous avez donné à l'image dans le dossier des assets.

```
floorNode.geometry?.firstMaterial?.diffuse.contents = UIImage(named: "WoodenFloorTile")
```

Maintenant, exécutez l'application et attendez que l'origine du monde se charge. Une fois le sol détecté, déplacez-vous pour mettre à jour les informations du nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/aO7-9zVFW65MANwJfIgAmwT0OaX6xXIIYEEx)

Wow, vous avez vraiment un sol magnifique ! Vous pouvez télécharger plusieurs textures et les placer dans une listeView. Cela vous permet de changer le sol en fonction de la texture sélectionnée, comme cela a été montré dans la première partie.

[Téléchargez le projet complet depuis GitHub ici.](https://github.com/ranadhirdey/Home-Decor)

Maintenant que vous avez un beau sol, il vous manque probablement de beaux meubles pour donner à votre pièce un superbe look ! Nous travaillerons là-dessus plus tard.