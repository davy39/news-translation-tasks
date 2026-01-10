---
title: Comment créer une application de suivi de sourire super rapide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-23T18:02:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-super-quick-smile-tracking-app-16eee960888d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6zDrFfE7gE4IIoeiR3IJiw.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: software development
  slug: software-development
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment créer une application de suivi de sourire super rapide
seo_desc: 'By Jake Shelley

  ARKit might seem intimidating but it’s not so bad if you already have some basic
  experience building iOS apps.

  I’m a learn-by-doing type, so I’ve been playing around with ARKit, building basic
  apps to get familiar with it. In this pos...'
---

Par Jake Shelley

ARKit peut sembler intimidant, mais ce n'est pas si mal si vous avez déjà une expérience de base dans la création d'applications iOS.

Je suis du genre à apprendre en faisant, alors j'ai joué avec ARKit en construisant des applications basiques pour me familiariser avec. Dans cet article, je vais passer en revue ce que j'ai appris en créant une application simple de suivi de visage.

Je vais le faire en 3 parties :

1. **Installation initiale ▶** D'abord, obtenez les permissions de la caméra et assurez-vous que l'appareil peut utiliser ARKit.
2. **Suivi du sourire ▶** Commencez à suivre les sourires avec ARKit. C'est probablement ce pour quoi vous êtes ici.
3. **Interface utilisateur ▶** Ajoutez l'interface utilisateur pour notre application qui réagira aux sourires.

Au moment de l'écriture, le simulateur Xcode ne supporte pas la caméra avant, donc vous aurez besoin d'un appareil réel pour exécuter l'application. Votre appareil devra également avoir une caméra TrueDepth (iPhone X ou plus récent devrait convenir).

Enfin, pour mes collègues membres du Copy Paste Club, [tout le code est disponible sur Github](https://github.com/JakeShelley1/SmileTracker).

#### **Installation initiale**

Commencez par ouvrir Xcode et créez un nouveau projet nommé « SmileTracker » (ou tout autre nom que vous préférez).

Avant de pouvoir nous lancer dans le suivi de visage, nous devons faire deux choses :

1. Assurez-vous que votre appareil supporte ARKit
2. Obtenez la permission d'accéder à la caméra de votre appareil

Dans votre nouveau projet, ouvrez `ViewController.swift`. Près du haut du fichier, sous `import UIKit`, ajoutez la ligne : `import ARKit`. Cela nous permettra d'accéder à toutes les fonctionnalités qu'Apple nous a fournies pour rendre le suivi de visage super facile.

Ajoutez maintenant le code suivant à l'intérieur de `viewDidLoad` :

```swift
guard ARFaceTrackingConfiguration.isSupported else {
    fatalError("L'appareil ne supporte pas le suivi de visage")
}
```

`ARFaceTrackingConfiguration.isSupported` est un booléen qui sera vrai si l'appareil exécutant l'application peut supporter le suivi de visage et faux sinon. Dans ce cas, si l'appareil ne peut pas supporter le suivi de visage, nous allons planter l'application avec une erreur fatale.

Ensuite, obtenons la permission d'utiliser la caméra. Ajoutez ce qui suit dans `viewDidLoad` sous notre instruction `guard` :

```swift
AVCaptureDevice.requestAccess(for: AVMediaType.video) { granted in
   if (granted) {
      DispatchQueue.main.async {
          // Nous allons implémenter cette fonction dans un instant
          self.setupSmileTracker()      
      }
   } else {      
      fatalError("L'utilisateur n'a pas accordé la permission de la caméra !")   
   }
}
```

Ici, nous demandons à l'appareil de demander les permissions de la caméra. Si l'utilisateur accorde les permissions, nous exécuterons la fonction qui configurera notre suivi de sourire (ne vous inquiétez pas de l'erreur, nous implémenterons cette fonction dans un instant).

Nous enveloppons la fonction dans `DispatchQueue.main.async` car nous ajouterons des éléments d'interface utilisateur dans cette fonction, ce qui ne peut être fait que dans le thread principal.

Nous devrons également ajouter une description d'utilisation de la caméra à notre `Info.plist`. Ouvrez `Info.plist` et ajoutez une nouvelle ligne (vous pouvez le faire en surlignant la dernière ligne et en appuyant sur `enter`).

Dans la ligne que vous venez de créer, ajoutez `Privacy — Camera Usage Description` dans la colonne `Key` et assurez-vous que la colonne `Type` est définie sur string. Vous pouvez laisser la colonne `Value` vide ou ajouter un message pour expliquer comment vous utiliserez la caméra à l'utilisateur.

Votre `Info.plist` devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/37EEOdiE1OAnLvGMi5SF4aU4ZL4KBlW8RSTu)

Si vous souhaitez tester votre application jusqu'à présent, vous pouvez commenter la ligne où nous appelons `setupSmileTracker()`. N'oubliez pas de la décommenter plus tard.

Si vous exécutez votre application maintenant, vous devriez voir une fenêtre contextuelle vous demandant d'activer les permissions de la caméra. **Si vous dites non, vous devrez aller dans les paramètres de l'application pour activer ces permissions afin que l'application puisse fonctionner.**

Si l'application plante, vérifiez la console pour l'un de nos deux messages d'erreur pour voir ce qui s'est mal passé.

#### Suivi du sourire

Ouvrez `ViewController.swift` et ajoutez la variable suivante en haut de `ViewController` :

```
class ViewController: UIViewController {   
   let sceneView = ARSCNView()
   
   override func viewDidLoad() {...}
}
```

`ARSCNView` est équipé d'une `ARSession` que votre iPhone utilise pour coordonner les expériences AR. Nous utiliserons la `ARSession` de `sceneView` pour analyser le visage de l'utilisateur à travers la caméra avant.

Ajoutez cette fonction à votre fichier sous `viewDidLoad` :

```
func setupSmileTracker() {   
   let configuration = ARFaceTrackingConfiguration()   
   sceneView.session.run(configuration)   
   sceneView.delegate = self   
   view.addSubview(sceneView)
}
```

Ici, nous avons créé une configuration pour gérer le suivi de visage et l'avons utilisée pour exécuter la `ARSession` de notre `sceneView`.

Ensuite, nous avons défini le délégué de `sceneView` sur self et l'avons ajouté à notre vue.

Xcode vous dira qu'il y a un problème puisque `ViewController` ne se conforme pas à `ARSCNViewDelegate`. Allez à l'endroit où `ViewController` est déclaré près du haut du fichier et changez la ligne en ce qui suit :

```
class ViewController: UIViewController, ARSCNViewDelegate {   
   ...
}
```

Ajoutez maintenant cette fonction `ARSCNViewDelegate` dans votre classe `ViewController` sous `setupSmileTracker` :

```swift
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {
   ...
}
```

`renderer` s'exécutera chaque fois que notre scène est mise à jour et nous fournit l'`ARAnchor` qui correspond au visage de l'utilisateur.

Pour faciliter la création d'expériences de suivi de visage, **Apple crée automatiquement un** `ARFaceAnchor` **et l'ajoute à notre session lorsque nous utilisons une** `ARFaceTrackingConfiguration` **pour l'exécuter.** Cet ARFaceAnchor est ensuite passé à `renderer` en tant qu'`ARAnchor`.

Ajoutez le code suivant à renderer :

```swift
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {   

  // 1      
   guard let faceAnchor = anchor as? ARFaceAnchor else { return }
   
   // 2   
   let leftSmileValue = faceAnchor.blendShapes[.mouthSmileLeft] as! CGFloat
   let rightSmileValue = faceAnchor.blendShapes[.mouthSmileRight] as! CGFloat
   
   // 3
   print(leftSmileValue, rightSmileValue)
}
```

Il se passe beaucoup de choses à l'intérieur de cette fonction, alors j'ai numéroté les étapes (style Ray Wenderlich).

Dans **l'étape 1**, nous convertissons l'`ARAnchor` en un `ARFaceAnchor` et l'assignons à la variable `faceAnchor`.

`ARFaceAnchor` contient des informations sur la position et l'orientation actuelles, la topologie et l'_expression faciale_ du visage que nous suivons.

`ARFaceAnchor` stocke des informations sur les expressions faciales dans sa variable `blendShapes`. `blendShapes` est un dictionnaire qui stocke des coefficients correspondant à diverses caractéristiques faciales. Si vous êtes intéressé, je vous suggère de [consulter la liste complète des caractéristiques faciales dans la documentation d'Apple](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation). (_Indice_ : si vous voulez ajouter le suivi des fronces de sourcils, vous trouverez un moyen de le faire ici.)

Dans **l'étape 2**, nous utilisons `faceAnchor.blendShapes` pour obtenir un CGFloat qui correspond à la quantité de sourire sur les côtés gauche et droit de la bouche de l'utilisateur en utilisant les clés `mouthSmileLeft` et `mouthSmileRight`.

Enfin, **l'étape 3** imprime simplement les deux valeurs pour que vous puissiez vous assurer que tout fonctionne correctement ?.

À ce stade, vous devriez avoir une application qui :

* Obtient les permissions de la caméra et du suivi de visage de l'utilisateur
* Utilise ARKit pour suivre les expressions faciales des utilisateurs
* Imprime combien l'utilisateur sourit sur les côtés gauche et droit de sa bouche dans la console

Nous avons fait beaucoup de progrès, alors prenons un moment pour nous assurer que tout fonctionne correctement.

Lorsque vous exécutez l'application pour la première fois, vous devriez être invité à accorder les permissions de la caméra. Assurez-vous de dire oui.

Vous serez ensuite envoyé à un écran vide, mais vous devriez commencer à voir des valeurs CGFloat imprimées dans la console (il peut y avoir un court délai avant de les voir).

Lorsque vous souriez à votre téléphone, vous devriez remarquer que les valeurs imprimées augmentent. Plus vous souriez, plus les nombres sont élevés.

Si tout fonctionne correctement, _félicitations_ ?! Si vous rencontrez une erreur, vérifiez à nouveau que votre appareil supporte le suivi de visage et que vous avez activé les permissions de la caméra. Si vous avez suivi ce tutoriel depuis le début, la console imprimera des erreurs dans les deux cas.

#### Interface utilisateur

Donc, nous suivons les visages, maintenant construisons l'interface utilisateur pour réagir aux sourires.

Tout d'abord, ajoutez un nouveau `UILabel` appelé `smileLabel` en haut du fichier, juste en dessous de `sceneView`.

```
class ViewController: UIViewController {   
   let sceneView = ARSCNView()      
   let smileLabel = UILabel()
   
   ...
}
```

Ce sera la vue qui réagira aux expressions faciales de l'utilisateur.

Ajoutez le code suivant à la fin de votre fonction `setupSmileTracker` :

```swift
smileLabel.text = "?"
smileLabel.font = UIFont.systemFont(ofSize: 150) 

view.addSubview(smileLabel)

// Définir les contraintes
smileLabel.translatesAutoresizingMaskIntoConstraints = false
smileLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
smileLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
```

Ici, nous ajoutons les propriétés de base de l'interface utilisateur à notre `smileLabel` et définissons ses contraintes pour qu'il soit au milieu de l'écran. Maintenant, lorsque vous exécutez l'application, vous devriez voir un émoji géant ? au milieu.

![Image](https://cdn-media-1.freecodecamp.org/images/0t8auH8IkMfU3ZWeKCG28hKVOpsCznKA9Q8N)

Une fois que vous voyez l'émoji apparaître, ajoutez la fonction suivante à votre `ViewController` :

```swift
func handleSmile(leftValue: CGFloat, rightValue: CGFloat) {
   let smileValue = (leftValue + rightValue)/2.0
   switch smileValue {      
   	  case _ where smileValue > 0.5:         
      	 smileLabel.text = "?"      
      case _ where smileValue > 0.2:         
         smileLabel.text = "?"      
      default:         
         smileLabel.text = "?"      
   }
} 
```

Cette fonction changera l'émoji dans notre `smileLabel` en fonction de la quantité de sourire de l'utilisateur dans la caméra. Nous calculons la `smileValue` en prenant la moyenne des valeurs de sourire gauche et droite qui nous sont données par notre `ARFaceAnchor` (très scientifique, je sais).

Insérez cette valeur dans l'instruction switch, et plus l'utilisateur sourit, plus notre émoji devient heureux.

Enfin, retournez à notre fonction `renderer` et ajoutez ceci à la fin pour insérer nos valeurs de sourire gauche et droite dans `handleSmile` :

```
DispatchQueue.main.async {   
   self.handleSmile(leftValue: leftSmileValue, rightValue: rightSmileValue)
}
```

Encore une fois, nous utilisons `DispatchQueue` car nous apportons des modifications à l'interface utilisateur, ce qui doit être fait dans le thread principal.

Lorsque vous exécutez l'application, vous devriez maintenant voir l'émoji changer en fonction de la quantité de sourire que vous lui adressez.

Dans le gif ci-dessous, j'ai ajouté mon visage pour que vous puissiez voir comment cela fonctionne avec la sortie de la caméra ainsi que l'émoji.

![Image](https://cdn-media-1.freecodecamp.org/images/54NIZPz4oKKzBmkNMjJw654tlemCDBH6ZRQA)
_J'ai ajouté la sortie de la caméra pour montrer comment cela fonctionne_

Votre application n'aura pas la sortie de la caméra, mais vous pouvez l'ajouter en ajoutant notre `ARSCNView`, `sceneView`, à la supervue et en lui donnant des dimensions.

#### Conclusion

J'espère que cet article vous a été utile pour commencer à créer des applications avec ARKit.

Si vous souhaitez étendre cette application, consultez la liste que j'ai mentionnée ci-dessus avec toutes les autres caractéristiques faciales que vous pouvez suivre. J'ai laissé un indice sur la façon d'étendre cela pour vérifier les fronces de sourcils également.

Revenez et commentez avec tous les projets intéressants que vous créez par vous-même, je commence tout juste à me familiariser avec ce sujet, donc je serais ravi de voir des applications plus complexes.

[J'ai publié tout le code de cette application sur Github](https://github.com/JakeShelley1/SmileTracker) pour les commentaires et les questions. Merci d'avoir lu et bonne chance !

---

_Merci beaucoup d'avoir lu ! Si vous avez aimé cette histoire, suivez-moi sur [Twitter](https://twitter.com/JakeShelley3) où je poste des mises à jour sur les histoires sur lesquelles je travaille et ce que je fais._