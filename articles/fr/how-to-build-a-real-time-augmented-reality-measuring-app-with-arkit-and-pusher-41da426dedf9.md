---
title: Comment créer une application de mesure en réalité augmentée en temps réel
  avec ARKit et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T18:36:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-augmented-reality-measuring-app-with-arkit-and-pusher-41da426dedf9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eQNtaPKg3c2ZoXcdquRgJg.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment créer une application de mesure en réalité augmentée en temps réel
  avec ARKit et Pusher
seo_desc: 'By Esteban Herrera

  Augmented reality (AR) is all about modifying our perception of the real world.

  Information about our environment and surrounding objects can be overlaid to enhance
  your current perception of reality. This information can presented...'
---

Par Esteban Herrera

La réalité augmentée (AR) consiste à modifier notre perception du monde réel.

Des informations sur notre environnement et les objets qui nous entourent peuvent être superposées pour améliorer votre perception actuelle de la réalité. Ces informations peuvent être présentées à l'utilisateur en temps réel, comme dans le cas d'un fil d'actualité lors d'un événement en direct.

Mais le flux d'informations peut également circuler dans l'autre sens. Nous pouvons envoyer les informations résultant de l'interaction avec l'expérience de réalité augmentée. Dans les deux cas, Pusher peut vous aider à envoyer et recevoir des données en temps réel.

Dans ce tutoriel, nous allons créer une application ARKit pour effectuer des mesures simples. Pendant la mesure, l'application créera une boîte 3D avec une largeur égale à la taille mesurée :

%[https://www.youtube.com/watch?v=osby8WfvPQA]

Elle enverra également les mesures en temps réel à Pusher :

%[https://www.youtube.com/watch?v=gRX3sHiV9Hg]

Une note de prudence. Les mesures sont basées sur les capacités de détection de plan d'ARKit. Elles ne sont pas parfaites dans certaines situations, comme en cas de faible éclairage ou lorsqu'une surface n'est pas entièrement plate. Les résultats ne seront pas complètement précis tout le temps. Ils sont proches, mais peuvent varier.

Pour ce tutoriel, vous aurez besoin de :

* Un appareil avec un processeur A9 ou ultérieur (iPhone 6s ou mieux, iPhone SE, tout iPad Pro, ou l'iPad 2017)
* [iOS 11 bêta 5](https://9to5mac.com/2017/06/26/how-to-install-ios-11-public-beta-on-your-eligible-iphone-ipad-or-ipod-touch/)
* [Xcode 9 bêta 5](https://developer.apple.com/download/) (ou supérieur)
* Un compte [Pusher](https://pusher.com/) gratuit

Pour référence, vous pouvez trouver le code source de ce projet sur [Git](https://github.com/eh3rrera/ARKitAnimation)Hub.

Commençons.

### Configuration du projet Xcode

Ouvrez Xcode et créez une nouvelle **Single View App** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4RAguNwZTCeOUirUbQau-w.png)

Nous choisissons cette option car nous allons configurer manuellement une vue AR ainsi que d'autres contrôles.

Entrez les informations du projet, en choisissant **Swift** comme langage :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qbOQVk-dMp1jSyn61g27CQ.png)

Créez le projet et fermez-le. Nous allons utiliser [CocoaPods](https://cocoapods.org/) pour installer les dépendances du projet. Ouvrez une fenêtre de terminal et allez dans le répertoire racine de votre projet. Si vous n'avez pas CocoaPods installé, exécutez :

```bash
sudo gem install cocoapods
```

Une fois installé, créez le fichier `Podfile` avec la commande :

```
pod init
```

Modifiez ce fichier pour définir la plateforme sur iOS 11 et ajouter les dépendances du projet :

```
# Uncomment the next line to define a global platform for your project

platform :ios, '11.0'

target 'MeasureARPusher' do

# Comment the next line if you're not using Swift 
# and don't want to use dynamic frameworks

use_frameworks!

# Pods for MeasureARPusher

pod 'PusherSwift', :git => 'https://github.com/pusher/pusher-websocket-swift.git', :branch => 'swift-3.2'
end
```

Au moment de la rédaction de cet article, la [bibliothèque Swift de Pusher](https://github.com/pusher/pusher-websocket-swift) pour Xcode 9 et Swift 3.2/4 est encore en [développement](https://github.com/pusher/pusher-websocket-swift/pull/145). La version actuelle génère quelques erreurs, nous devons donc utiliser la version pour Swift 3.2 depuis la branche `swift-3.2`.

Une fois que vous avez modifié `Podfile`, exécutez la commande suivante pour installer les dépendances :

```
pod install
```

Ouvrez maintenant l'espace de travail Xcode au lieu du fichier de projet :

```
open MeasureARPusher.xcworkspace
```

Nous devons changer la version de Swift de 4.0 (par défaut) à Swift 3.2 pour que Pusher puisse compiler sans erreurs. Dans le navigateur de projet, sélectionnez **Pods**. Dans la section **Targets**, sélectionnez **PusherSwift**. Dans l'onglet **Build Settings**, recherchez l'option **Swift Language Version**. Changez-la pour Swift 3.2 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WtjhYNU06qtBuBs2voOEZg.png)

Si vous construisez votre projet à ce stade, l'opération devrait réussir.

Sélectionnez la **Information Property List**. Ajoutez une ligne de type **Privacy — Camera Usage Description** (`NSCameraUsageDescription`) et donnez-lui une description. Cela permet à ARKit d'accéder à la caméra :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gC9DNj85bGQR12GKrAF_uA.png)

Enfin, configurez une équipe pour pouvoir exécuter l'application sur votre appareil :

![Image](https://cdn-media-1.freecodecamp.org/images/1*chrOmMGpjZVjdTgPbtkHXw.png)

Maintenant, commençons par construire l'interface utilisateur.

### Construction de l'interface utilisateur

Allez dans `Main.storyboard` et faites glisser une _ARKit SceneKit View_ vers la vue :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pevseQO488OwrK9daZvGtA.png)

Ensuite, ajoutez des contraintes à tous les côtés de cette vue pour qu'elle remplisse tout l'écran. Vous faites cela en appuyant sur la touche `ctrl` tout en faisant glisser une ligne vers chaque côté et en choisissant leading, top, trailing, et bottom vers la supervue, avec une valeur de `0` :

%[https://www.youtube.com/watch?v=qTpjmRjlriI]

Ajoutez un bouton. Changez son type en **Add Contact** dans l'**Attributes inspector**. Donnez-lui une couleur **Tint** blanche, et ajoutez une contrainte verticale et une horizontale pour le centrer au milieu de l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nUaOTrdCDgeG-SLq1dcNXA.png)

Ajoutons un interrupteur pour contrôler quand l'application est en mode mesure. Définissez son état initial sur Off dans l'inspecteur d'attributs. Ajoutez une contrainte de bas et de fin avec une valeur de `-20` pour placer le contrôle dans la partie inférieure droite de l'écran. Vous pouvez le placer au centre inférieur ou dans une autre partie de l'écran si vous préférez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HAgfKwrsGm1ZUmrZ5sUc7Q.png)

Maintenant, ajoutez une vue de texte. Désactivez ses comportements **Editable** et **Selectable** dans l'inspecteur d'attributs. Changez sa couleur de fond. J'ai choisi une couleur blanche avec 50 % d'opacité.

Ajoutez une contrainte de hauteur avec une valeur de 90. Ajoutez des contraintes de début, de haut et de fin avec la valeur 0 pour qu'elle reste fixe en haut de l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JbDlm-LQrK3-T97wILiQvg.png)

Dans `ViewController.swift`, importez les bibliothèques SceneKit et ARKit :

```swift
import SceneKit

import ARKit
```

Ensuite, créez deux `IBOutlets`, un pour la vue de scène et un autre pour la vue de texte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y0JGX6NshNNYHj8_mQJpPQ.png)

Enfin, une action sur le contrôle de l'interrupteur pour l'événement `changeValue` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6uUKy6VvTqKIQCIIGqDHoQ.png)

Et maintenant, nous sommes prêts à commencer à coder l'application.

### Construction d'une application de mesure

Commençons par faire en sorte que `ViewController.swift` implémente `ARSCNViewDelegate` et définissons les variables dont nous allons avoir besoin :

```swift
class ViewController: UIViewController, ARSCNViewDelegate {
  ...
  var box: Box!
  var status: String!
  var startPosition: SCNVector3!
  var distance: Float!
  var trackingState: ARCamera.TrackingState!
  enum Mode {
    case waitingForMeasuring
    case measuring
  }
  ...
}
```

Où :

* `box` représente la boîte 3D qui va être dessinée lors de la mesure. Nous passerons en revue cette classe plus tard. Pour l'instant, créez-la pour éliminer l'erreur.
* `status` est un texte qui nous indique si l'application est prête ou non à prendre des mesures (si l'application a détecté des plans ou non).
* `startPosition` représente la position de départ de la mesure.
* `distance` est la distance calculée entre le départ et la position actuelle (la mesure elle-même).
* `trackingState` contient l'état actuel de suivi de la caméra.
* `Mode` est une énumération pour indiquer les états possibles de l'application.

Ajoutons une autre propriété pour suivre l'état de l'application, et faisons quelques choses en fonction de la valeur définie :

```swift
var mode: Mode = .waitingForMeasuring {
  didSet {
    switch mode {
      case .waitingForMeasuring:
        status = "NOT READY"
      case .measuring:
        box.update(
          minExtents: SCNVector3Zero, maxExtents: SCNVector3Zero)
        box.isHidden = false
        startPosition = nil
        distance = 0.0
        setStatusText()
    }
  }
}
```

Si `waitingForMeasuring` est défini, nous supposerons que l'application n'est pas prête. Ne vous inquiétez pas, si c'est le cas, le statut changera immédiatement. Si le mode est défini sur measuring, nous réinitialiserons la taille de la boîte. Nous passerons en revue la méthode update plus tard. Nous afficherons si la boîte est cachée, réinitialiserons la `startPosition` et les variables `distance`, et appellerons la méthode qui affiche la valeur de ces variables.

Voici la définition de la méthode `setStatusText()` :

```swift
func setStatusText() {
  var text = "Status: \(status!)\n"
  text += "Tracking: \(getTrackigDescription())\n"
  text += "Distance: \(String(format:"%.2f cm", distance! * 100.0))"
  statusTextView.text = text
}

func getTrackigDescription() -> String {
  var description = ""
  if let t = trackingState {
    switch(t) {
      case .notAvailable:
        description = "TRACKING UNAVAILABLE"
      case .normal:
        description = "TRACKING NORMAL"
      case .limited(let reason):
        switch reason {
          case .excessiveMotion:
            description = 
              "TRACKING LIMITED - Too much camera movement"
          case .insufficientFeatures:
            description = 
              "TRACKING LIMITED - Not enough surface detail"
          case .initializing:
            description = "INITIALIZING"
        }
    }
  }
  return description
}
```

Cette méthode définit le texte de la vue de texte sur l'état de mesure de READY ou NOT READY. Elle affiche une description de l'état de suivi de la caméra AR avec l'aide de la méthode `getTrackingDescription()`. Et la (dernière) distance calculée en centimètres. Remarquez que nous devons multiplier la valeur par `100.0`.

Ensuite, nous avons la méthode `viewDidLoad()`, où nous définissons les valeurs initiales, entre autres :

```swift
override func viewDidLoad() {
  super.viewDidLoad()
  
  // Set the view's delegate
  sceneView.delegate = self
  
  // Set a padding in the text view
  statusTextView.textContainerInset = 
      UIEdgeInsetsMake(20.0, 10.0, 10.0, 0.0)
      
  // Instantiate the box and add it to the scene
  box = Box()
  box.isHidden = true;
  sceneView.scene.rootNode.addChildNode(box)
  
  // Set the initial mode
  mode = .waitingForMeasuring
  
  // Set the initial distance
  distance = 0.0
  
  // Display the initial status
  setStatusText()
}
```

Dans la méthode `viewWillAppear`, créez et exécutez une [session](https://developer.apple.com/documentation/arkit/arsession) avec [plane detection](https://developer.apple.com/documentation/arkit/arworldtrackingsessionconfiguration.planedetection). Cela est important car les points du plan seront les éléments que nous utiliserons pour mesurer les choses :

```swift
override func viewWillAppear(_ animated: Bool) {
  super.viewWillAppear(animated)
  
  // Create a session configuration with plane detection
  let configuration = ARWorldTrackingConfiguration()
  configuration.planeDetection = .horizontal
  
  // Run the view's session
  sceneView.session.run(configuration)
}
```

De plus, remplacez la méthode `viewWillDisappear` pour mettre en pause la session lorsque nécessaire :

```swift
override func viewWillDisappear(_ animated: Bool) {
  super.viewWillDisappear(animated)
  
  // Pause the view's session
  sceneView.session.pause()
}
```

Utilisez la méthode suivante pour savoir quand l'état de suivi de la caméra a changé. Enregistrez une référence à cet état :

```swift
func session(_ session: ARSession, cameraDidChangeTrackingState camera: ARCamera) {
  trackingState = camera.trackingState
}
```

Ces méthodes font partie des rappels qui accompagnent le protocole [ARSCNViewDelegate](https://developer.apple.com/documentation/arkit/arscnviewdelegate).

Maintenant, voici la partie intéressante.

La méthode :

```swift
(void)renderer:(id <SCNSceneRenderer>)renderer updateAtTime:(NSTimeInterval)time
```

Elle est appelée exactement une fois par image, comme `60` fois par seconde. Nous allons donc appeler une autre méthode pour utiliser le test de collision afin de détecter un plan avec lequel nous pouvons interagir. Lorsque cela se produit, nous changerons l'état de NOT READY à READY.

L'implémentation ressemble à ceci :

```swift
func renderer(_ renderer: SCNSceneRenderer, updateAtTime time: TimeInterval) {
  // Call the method asynchronously to perform
  //  this heavy task without slowing down the UI
  DispatchQueue.main.async {
    self.measure()
  }
}

func measure() {
  let screenCenter : CGPoint = CGPoint(
      x: self.sceneView.bounds.midX, y: self.sceneView.bounds.midY)
  let planeTestResults = sceneView.hitTest(
      screenCenter, types: [.existingPlaneUsingExtent])
  if let result = planeTestResults.first {
    status = "READY"
  } else {
    status = "NOT READY"
  }
  ...
}
```

Le point de référence sera toujours le centre de l'écran. C'est pourquoi nous plaçons ce bouton avec le signe plus. Nous obtiendrons les coordonnées du centre de l'écran pour effectuer un test de collision contre un plan existant. Si un résultat est obtenu, cela signifie que nous pouvons commencer à mesurer.

Il existe [quatre types d'objets](https://developer.apple.com/documentation/arkit/arhittestresult.resulttype) que nous pouvons trouver dans une recherche :

* [featurePoints](https://developer.apple.com/documentation/arkit/arhittestresult.resulttype/2875708-featurepoint)  
 Un point automatiquement identifié par ARKit comme faisant partie d'une surface continue, mais sans ancrage correspondant.
* [estimatedHorizontalPlane](https://developer.apple.com/documentation/arkit/arhittestresult.resulttype/2887460-estimatedhorizontalplane)  
Une surface plane du monde réel détectée par la recherche et sans ancrage correspondant. L'orientation est perpendiculaire à la gravité.
* [existingPlane](https://developer.apple.com/documentation/arkit/arhittestresult.resulttype/2875738-existingplane)  
Un ancrage de plan déjà dans la scène, sans tenir compte de la taille du plan.
* [existingPlaneUsingExtent](https://developer.apple.com/documentation/arkit/arhittestresult.resulttype/2887459-existingplaneusingextent)  
Un ancrage de plan déjà dans la scène, en respectant la taille limitée du plan.

L'option la plus facile serait d'utiliser les points de repère. Ils représentent des caractéristiques notables détectées dans l'image de la caméra. Ils sont détectés plus rapidement que les plans et il y en a plus.

Cependant, cela nous donnera des résultats très instables. Les points de repère sont des résultats intermédiaires de l'analyse de scène qu'ARKit utilise pour effectuer le suivi du monde. Il est donc recommandé de faire un test de collision contre les ancrages de plan existants en premier.

S'il y a une collision et que le mode est en mesure, nous devons changer le statut en _MEASURING_. Et extraire la position sous forme de vecteur de trois éléments (x, y, z) à partir de la matrice de transformation du résultat :

```swift
func measure() {
  ...
  if let result = planeTestResults.first {
    status = "READY"
    if mode == .measuring {
      status = "MEASURING"
      let worldPosition = SCNVector3Make(
        result.worldTransform.columns.3.x,      
        result.worldTransform.columns.3.y,
        result.worldTransform.columns.3.z
      )
      ...
    }
  } ...
}
```

Si `startPosition` est `nil` (la première mesure), nous utilisons `worldPosition` pour définir sa valeur ainsi que la position de la boîte :

```swift
func measure() {
  ...
  if let result = planeTestResults.first {
    status = "READY"
    if mode == .measuring {
      ...
      let worldPosition = SCNVector3Make(
        result.worldTransform.columns.3.x, 
        result.worldTransform.columns.3.y, 
        result.worldTransform.columns.3.z
      )
      if startPosition == nil {
        startPosition = worldPosition
        box.position = worldPosition
      }
      ...
    }
  } ...
}
```

Nous pouvons calculer la distance entre `startPosition` et `worldPosition` (la position actuelle) dans un espace 3D en utilisant le [théorème de Pythagore](https://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space) et redimensionner la boîte en conséquence :

```swift
func measure() {
  ...
  if let result = planeTestResults.first {
    status = "READY"
    if mode == .measuring {
      ...
      distance = calculateDistance(
          from: startPosition!, to: worldPosition
      )
      box.resizeTo(extent: distance)
      ...
    }
  } ...
}

func calculateDistance(from: SCNVector3, to: SCNVector3) -> Float {
  let x = from.x - to.x
  let y = from.y - to.y
  let z = from.z - to.z
  return sqrtf( (x * x) + (y * y) + (z * z))
}
```

Mais les mathématiques ne sont pas encore terminées. Nous ne mesurerons pas toujours des lignes droites. Pour prendre des mesures dans toutes les directions et faire suivre la boîte 3D, nous devons prendre en compte la rotation dans l'axe Y.

Nous pouvons obtenir l'angle (en radians) entre deux vecteurs en utilisant [atan2](https://en.wikipedia.org/wiki/Atan2) de cette manière :

```swift
func measure() {
  ...
  if let result = planeTestResults.first {
    status = "READY"
    if mode == .measuring {
      ...
      let angleInRadians = calculateAngleInRadians(
          from: startPosition!, to: worldPosition
      )
      box.rotation = SCNVector4(x: 0, y: 1, z: 0, 
          w: -(angleInRadians + Float.pi)
      )
    }
  } ...
}
...

func calculateAngleInRadians(from: SCNVector3, to: SCNVector3) -> Float {
  let x = from.x - to.x
  let z = from.z - to.z
  return atan2(z, x)
}
```

Cependant, la fonction `atan2` retourne un angle de 0° à +/- 180°. Comme nous traitons avec des radians, nous devons ajouter la valeur de PI pour la normalisation (PI en radians est égal à 180°).

De plus, notez que la propriété de rotation de la boîte 3D prend un vecteur de quatre éléments. Les trois premiers composants sont l'axe (nous devons tourner sur l'axe Y). Le quatrième est la rotation en radians.

N'oublions pas l'action pour le contrôle de l'interrupteur. Il change simplement le mode en fonction de son état :

```swift
@IBAction func switchChanged(_ sender: UISwitch) {
  if sender.isOn {
    mode = .measuring
  } else {
    mode = .waitingForMeasuring
  }
}
```

Pour la boîte 3D, si vous ne l'avez pas déjà fait, créez la classe en étendant [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode) :

```swift
import SceneKit

class Box: SCNNode {

}
```

Définissons également deux fonctions statiques en dehors de la classe qui nous aideront à ajouter et à soustraire deux vecteurs :

```swift
class Box: SCNNode {

}

func + (left: SCNVector3, right: SCNVector3) -> SCNVector3 {
  return SCNVector3Make(
      left.x + right.x, left.y + right.y, left.z + right.z
  )
}

func - (left: SCNVector3, right: SCNVector3) -> SCNVector3 {
  return SCNVector3Make(
      left.x - right.x, left.y - right.y, left.z - right.z
  )
}
```

Ajoutez les constructeurs requis :

```swift
class Box: SCNNode {
  override init() {
    super.init()
  }
  
  required init?(coder aDecoder: NSCoder) {
    fatalError("init(coder:) has not been implemented")
  }
}
```

Ajoutons une variable paresseuse pour qu'elle soit initialisée jusqu'à la première fois qu'elle est utilisée. Elle contiendra une référence à la boîte 3D ([SCNBox](https://developer.apple.com/documentation/scenekit/scnbox)) à l'intérieur d'un nœud de type [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode) :

```swift
class Box: SCNNode {
  lazy var box: SCNNode = makeBox()
  ...
  
  func makeBox() -> SCNNode {
    let box = SCNBox(
        width: 0.01, height: 0.01, length: 0.01, chamferRadius: 0
    )
    return convertToNode(geometry: box)
  }
  
  func convertToNode(geometry: SCNGeometry) -> SCNNode {
    for material in geometry.materials {
      material.lightingModel = .constant
      material.diffuse.contents = UIColor.white
      material.isDoubleSided = false
    }
    let node = SCNNode(geometry: geometry)
      self.addChildNode(node)
      return node
    }
}
```

En théorie, nous pourrions utiliser n'importe quelle forme primitive dérivée de [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry). Mais en pratique, SCNBox est plus facile à utiliser car nous pouvons définir ses dimensions des axes X, Y et Z en définissant ses propriétés de largeur, hauteur et longueur. Dans ce cas, nous utilisons des valeurs petites pour que la boîte soit affichée avec une bonne taille.

De plus, notez que nous attribuons une couleur blanche uniforme à la boîte. Vous pouvez utiliser des textures ou configurer le matériau d'autres manières pour lui donner un aspect plus poli.

Dans la méthode `resizeTo`, nous obtenons les éléments de la boîte de délimitation du nœud et définissons l'axe X à la distance fournie :

```swift
func resizeTo(extent: Float) {
  var (min, max) = boundingBox
  max.x = extent
  update(minExtents: min, maxExtents: max)
}
```

La méthode `update` prend les éléments `min` et `max` modifiés pour mettre à jour la largeur de la boîte et la position du nœud :

```swift
func update(minExtents: SCNVector3, maxExtents: SCNVector3) {
  guard let scnBox = box.geometry as? SCNBox else {
    fatalError("Geometry is not SCNBox")
  }
  
  // Normalize the bounds so that min is always < max
  let absMin = SCNVector3(
      x: min(minExtents.x, maxExtents.x), 
      y: min(minExtents.y, maxExtents.y), 
      z: min(minExtents.z, maxExtents.z)
  )
  
  let absMax = SCNVector3(
      x: max(minExtents.x, maxExtents.x), 
      y: max(minExtents.y, maxExtents.y), 
      z: max(minExtents.z, maxExtents.z)
  )
  
  // Set the new bounding box
  boundingBox = (absMin, absMax)
  
  // Calculate the size vector
  let size = absMax - absMin
  
  // Take the absolute distance
  let absDistance = CGFloat(abs(size.x))
  
  // The new width of the box is the absolute distance
  scnBox.width = absDistance
  
  // Give it a offset of half the new size so they box remains fixed
  let offset = size.x * 0.5
  
  // Create a new vector with the min position 
  // of the new bounding box
  let vector = SCNVector3(x: absMin.x, y: absMin.y, z: absMin.z)
  
  // And set the new position of the node with the offset
  box.position = vector + SCNVector3(x: offset, y: 0, z: 0)
}
```

À ce stade, vous aurez une application de mesure AR fonctionnelle. Mais ajoutons la bibliothèque Pusher pour publier ces mesures en temps réel.

### Envoi des données mesurées avec Pusher

Si vous ne l'avez pas déjà fait, créez un compte gratuit sur [Pusher](https://pusher.com/). Allez dans votre tableau de bord et créez une application. Choisissez un nom, le cluster le plus proche de votre emplacement, et _iOS_ comme votre technologie front-end :

![Image](https://cdn-media-1.freecodecamp.org/images/1*W4vC1sJShhacn_MK4JMqQw.png)

Cela vous donnera un exemple de code pour commencer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4itzMt0FciChOXrM5KuU6A.png)

Enregistrez votre clé, votre secret et les valeurs de cluster, car nous en aurons besoin plus tard.

Enfin, allez dans l'onglet **App Setting**, cochez l'option **Enable client events** et cliquez sur **Update** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CTXdVhCb2_dtcaoORNsjLA.png)

Ce que nous allons faire, c'est publier un événement [client](https://pusher.com/docs/client_api_guide/client_events) pour envoyer la mesure calculée en temps réel.

Les événements sont le principal moyen d'emballer les messages dans Pusher. Tous ces événements n'ont pas besoin d'aller vers un serveur web pour validation ou persistance lors de l'utilisation de Pusher.

Dans certains cas, comme dans cette application, les événements peuvent être envoyés directement du client à Pusher, et de là, à tous les autres clients connectés au canal. Cependant, il y a [certaines choses que nous devons prendre en compte](https://pusher.com/docs/client_api_guide/client_events#trigger-events) :

* Les événements clients doivent être activés pour l'application (comme nous l'avons fait).
* L'utilisateur doit être abonné au canal sur lequel l'événement est déclenché.
* Les événements clients ne peuvent être déclenchés que sur les canaux [privés](https://pusher.com/docs/private_channels) et [présence](https://pusher.com/docs/presence) car ils nécessitent une authentification.
* Les événements clients doivent être préfixés par `client-`.
* Ne publiez pas plus de [10 messages par seconde par client (connexion)](https://pusher.com/docs/client_api_guide/client_events#rate_limit). Tout événement déclenché au-dessus de cette limite de débit sera rejeté.

Dans `ViewController`, importons la bibliothèque Pusher et instancions l'objet. Nous définirons une variable pour le canal et une autre variable pour contrôler le taux des événements déclenchés :

```swift
...
import PusherSwift
class ViewController: UIViewController, ARSCNViewDelegate {
  ...
  let pusher = Pusher(
    key: "<YOUR_PUSHER_APP_KEY>",
    options: PusherClientOptions(
      authMethod: .inline(secret: "<YOUR_PUSHER_APP_SECRET>"),
      host: .cluster("YOUR_PUSHER_APP_CLUSTER")
    )
  )
  
  var channel: PusherChannel!
  var sendingTime : TimeInterval = 0
  ...
}
```

Nous devons utiliser un canal privé authentifié pour les événements clients. La bibliothèque Swift de Pusher fournit les méthodes d'authentification suivantes avec l'option `authMethod` :

* `endpoint(authEndpoint:String)`  
Le client effectuera une requête POST à l'endpoint que vous spécifiez.
* `authRequestBuilder(authRequestBuilder:AuthRequestBuilderProtocol)`  
Vous spécifiez un objet qui se conforme au protocole [AuthRequestBuilderProtocol](https://github.com/pusher/pusher-websocket-swift/blob/master/Source/AuthRequestBuilderProtocol.swift).
* `inline(secret:String)`  
Le secret de votre application afin que les requêtes d'authentification n'aient pas besoin d'être faites à votre endpoint d'authentification. Au lieu de cela, les abonnements peuvent être authentifiés directement à l'intérieur de la bibliothèque et utilisés pour le développement.
* `authorizer(authorizer:Authorizer)`   
Vous spécifiez un objet qui se conforme au protocole [Authorizer](https://github.com/pusher/pusher-websocket-swift/blob/master/Source/Authorizer.swift) pour fournir les informations d'authentification appropriées.
* `noMethod`   
Si vous n'avez pas besoin de définir une méthode d'authentification, c'est la valeur par défaut.

Vous pouvez apprendre à créer un [endpoint d'authentification sur cette page](https://pusher.com/docs/authenticating_users#implementing_endpoints). Pour simplifier, nous utilisons l'option `inline` qui ne nécessite pas de serveur pour l'authentification.

Dans la méthode `viewDidLoad`, abonnez-vous à un canal privé. N'oubliez pas d'utiliser le préfixe `private-` et connectez-vous à Pusher :

```swift
override func viewDidLoad() {
  ...
  
  // subscribe to channel and connect
  channel = pusher.subscribe("private-channel")
  pusher.connect()
}
```

Ajoutons également à la classe une fonction pour envoyer un événement client. N'oubliez pas d'utiliser le préfixe `client-` :

```swift
func sendPusherEvent() {
  channel.trigger(eventName: "client-new-measurement", 
      data: String(format: "%.2f cm", distance * 100.0)
  )
}
```

Rappelez-vous que la méthode `renderer` et la fonction `measure` sont exécutées une fois par image. Idéalement, cela fait 60 fois par seconde. Pour limiter le nombre d'événements clients envoyés à Pusher, nous allons utiliser le paramètre `TimeInterval` de la méthode `renderer`. Cela nous indique le moment auquel la scène est mise à jour.

Modifiez la méthode `measure` pour passer le paramètre comme son argument :

```swift
func renderer(_ renderer: SCNSceneRenderer, updateAtTime time: TimeInterval) {
  // Call the method asynchronously to perform
  //  this heavy task without slowing down the UI
  DispatchQueue.main.async {
    self.measure(time: time)
  }
}

func measure(time: TimeInterval) {
  ...
}
```

Maintenant, ajoutez le bloc `if` suivant après avoir défini la rotation de la boîte :

```swift
func measure(time: TimeInterval) {
  ...
  if let result = planeTestResults.first {
    status = "READY"
    if mode == .measuring {
      ...
      box.rotation = SCNVector4(x: 0, y: 1, z: 0, 
          w: -(angleInRadians + Float.pi)
      )
      
      // Only send the Pusher event after the specified interval
      if time > sendingTime {
        sendPusherEvent();
        sendingTime = time + TimeInterval(0.2)
      }
    }
  } ...
}
```

Au premier lancement, le temps sera supérieur à `sendingTime`. Mais ensuite, nous ajoutons `0.2` secondes (ou 200 millisecondes) au temps pour définir la nouvelle valeur de `sendingTime`. De cette manière, nous pouvons être sûrs que l'événement Pusher sera exécuté au plus 5 fois par seconde.

Cependant, en raison de cette différence de temps, la dernière mesure ne sera probablement pas envoyée. Nous pouvons donc appeler la méthode `sendPusherEvent` lorsque l'utilisateur termine la mesure :

```swift
@IBAction func switchChanged(_ sender: UISwitch) {
  if sender.isOn {
    mode = .measuring
  } else {
    mode = .waitingForMeasuring
    sendPusherEvent()
  }
}
```

Bien sûr, nous pourrions simplement envoyer la dernière mesure à Pusher pour éviter le problème. Mais quel serait l'intérêt d'envoyer une seule valeur ?

### Test de l'application

Lancez l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*iV0MR66U1aIb5JRdK5bMCg.png)

Il peut prendre plusieurs secondes pour s'initialiser et trouver un plan afin que le statut puisse passer à _READY_. Déplacez lentement votre appareil et surveillez l'état de suivi de la caméra pour accélérer un peu le processus.

Une fois qu'il est _READY_, vous pourrez prendre des mesures et les voir en temps réel sur votre appareil :

%[https://www.youtube.com/watch?v=osby8WfvPQA]

Et sur la console de débogage de votre tableau de bord Pusher [dashboard](https://dashboard.pusher.com) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sVWT74fO78OLswbSAgf04A.png)

### Conclusion

Dans ce tutoriel, vous avez appris à créer une application de mesure de base avec ARKit et à utiliser Pusher pour envoyer des événements clients depuis une application _iOS_.

Le suivi des caractéristiques du monde réel est une partie importante d'une expérience de réalité augmentée. Cependant, parfois les résultats ne sont pas précis car l'environnement peut être difficile à mesurer. Dans la [documentation ARKit](https://developer.apple.com/documentation/arkit/understanding_augmented_reality), vous pouvez trouver des conseils pour améliorer l'expérience AR.

N'oubliez pas que vous pouvez trouver le projet complet sur [ce dépôt GitHub](https://github.com/eh3rrera/MeasureARKitPusher).