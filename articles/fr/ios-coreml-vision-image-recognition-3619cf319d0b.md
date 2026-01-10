---
title: Comment créer une application iOS de reconnaissance d'images avec CoreML et
  les API Vision d'Apple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-01T18:54:19.000Z'
originalURL: https://freecodecamp.org/news/ios-coreml-vision-image-recognition-3619cf319d0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vm51CWzLgOE2mTHwWdQENw.png
tags:
- name: image recognition
  slug: image-recognition
- name: iOS
  slug: ios
- name: Machine Learning
  slug: machine-learning
- name: mobile app development
  slug: mobile-app-development
- name: 'tech '
  slug: tech
seo_title: Comment créer une application iOS de reconnaissance d'images avec CoreML
  et les API Vision d'Apple
seo_desc: 'By Mark Mansur

  With the release of CoreML and new Vision APIs at this year’s Apple World Wide Developers
  Conference, machine learning has never been easier to get into. Today I’m going
  to show you how to build a simple image recognition app.

  We will ...'
---

Par Mark Mansur

Avec la sortie de [CoreML](https://developer.apple.com/documentation/coreml) et des nouvelles API Vision lors de la conférence mondiale des développeurs Apple de cette année, le machine learning n'a jamais été aussi facile à prendre en main. Aujourd'hui, je vais vous montrer comment créer une application simple de reconnaissance d'images.

Nous allons apprendre comment accéder à la caméra de l'iPhone et comment transmettre ce que la caméra voit à un modèle de machine learning pour analyse. Nous allons tout faire de manière programmatique, sans utiliser de storyboards ! Fou, je sais.

Voici un aperçu de ce que nous allons accomplir aujourd'hui :

```swift
//
//  ViewController.swift
//  cameraTest
//
//  Créé par Mark Mansur le 2017-08-01.
//  Copyright © 2017 Mark Mansur. Tous droits réservés.
//
import UIKit
import AVFoundation
import Vision

class ViewController: UIViewController, AVCaptureVideoDataOutputSampleBufferDelegate {
    let label: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Label"
        label.font = label.font.withSize(30)
        return label
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupCaptureSession()
        
        view.addSubview(label)
        setupLabel()
    }
    
    func setupCaptureSession() {
        let captureSession = AVCaptureSession()
        
        // recherche des dispositifs de capture disponibles
        let availableDevices = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInWideAngleCamera], mediaType: AVMediaType.video, position: .back).devices
        
        // configuration du dispositif de capture, ajout de l'entrée à notre session de capture
        do {
            if let captureDevice = availableDevices.first {
                let captureDeviceInput = try AVCaptureDeviceInput(device: captureDevice)
                captureSession.addInput(captureDeviceInput)
            }
        } catch {
            print(error.localizedDescription)
        }
        
        // configuration de la sortie, ajout de la sortie à notre session de capture
        let captureOutput = AVCaptureVideoDataOutput()
        captureOutput.setSampleBufferDelegate(self, queue: DispatchQueue(label: "videoQueue"))
        captureSession.addOutput(captureOutput)
        
        let previewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
        previewLayer.frame = view.frame
        view.layer.addSublayer(previewLayer)
        
        captureSession.startRunning()
    }
    
    // appelé chaque fois qu'une image est capturée
    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        guard let model = try? VNCoreMLModel(for: Resnet50().model) else {return}
        
        let request = VNCoreMLRequest(model: model) { (finishedRequest, error) in
            
            guard let results = finishedRequest.results as? [VNClassificationObservation] else { return }
            guard let Observation = results.first else { return }
            
            DispatchQueue.main.async(execute: {
                self.label.text = "\(Observation.identifier)"
            })
        }
        guard let pixelBuffer: CVPixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
        
        // exécute la requête
        try? VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:]).perform([request])
    }
    
    func setupLabel() {
        label.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        label.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -50).isActive = true
    }
}
```

### 👋🏻 Étape 1 : Créer un nouveau projet.

Lancez Xcode et créez une nouvelle application à vue unique. Donnez-lui un nom, peut-être « ImageRecognition ». Choisissez Swift comme langage principal et enregistrez votre nouveau projet.

### 👋 Étape 2 : Dire adieu au storyboard.

Pour ce tutoriel, nous allons tout faire de manière programmatique, sans avoir besoin du storyboard. Peut-être que j'expliquerai pourquoi dans un autre article.

Supprimez `main.storyboard`.

Accédez à `info.plist` et faites défiler jusqu'à Deployment Info. Nous devons dire à Xcode que nous n'utilisons plus le storyboard.

Supprimez l'interface principale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W-p1_py_aMgNrnBh4ljJOg.png)

Sans le storyboard, nous devons créer manuellement la fenêtre de l'application et le contrôleur de vue racine.

Ajoutez ce qui suit à la fonction `application()` dans `AppDelegate.swift` :

```swift

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Point de substitution pour la personnalisation après le lancement de l'application.
        
        window = UIWindow()
        window?.makeKeyAndVisible()
        let vc = ViewController()
        
        window?.rootViewController = vc
        return true
    }
```

Nous créons manuellement la fenêtre de l'application avec `UIWindow()`, créons notre contrôleur de vue et disons à la fenêtre de l'utiliser comme contrôleur de vue racine.

L'application devrait maintenant se construire et s'exécuter sans le storyboard 😊

### ⚙️ Étape 3 : Configurer AVCaptureSession.

Avant de commencer, importez UIKit, AVFoundation et Vision. L'objet AVCaptureSession gère l'activité de capture et manage le flux de données entre les dispositifs d'entrée (comme la caméra arrière) et les sorties.

Nous allons commencer par créer une fonction pour configurer notre session de capture.

Créez `setupCaptureSession()` à l'intérieur de `ViewController.swift` et instanciez une nouvelle `AVCaptureSession`.

```swift
func setupCaptureSession() {
        
        // crée une nouvelle session de capture
        let captureSession = AVCaptureSession()
}
```

N'oubliez pas d'appeler cette nouvelle fonction depuis `ViewDidLoad()`.

```swift
override func viewDidLoad() {
        super.viewDidLoad()
        
        setupCaptureSession()
}
```

Ensuite, nous allons avoir besoin d'une référence à la caméra arrière. Nous pouvons utiliser un `DiscoverySession` pour interroger les dispositifs de capture disponibles en fonction de nos critères de recherche.

Ajoutez le code suivant :

```swift
// recherche des dispositifs de capture disponibles
let availableDevices = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInWideAngleCamera], mediaType: AVMediaType.video, position: .back).devices

```

`AvailableDevices` contient maintenant une liste des dispositifs disponibles correspondant à nos critères de recherche.

Nous devons maintenant obtenir l'accès à notre `captureDevice` et l'ajouter comme entrée à notre `captureSession`.

Ajoutez une entrée à la session de capture.

```swift
// obtenir le dispositif de capture, ajouter l'entrée du dispositif à la session de capture
do {
    if let captureDevice = availableDevices.first {
        captureSession.addInput(try AVCaptureDeviceInput(device: captureDevice))
    }
} catch {
    print(error.localizedDescription)
}
```

Le premier dispositif disponible sera la caméra arrière. Nous créons un nouveau `AVCaptureDeviceInput` en utilisant notre dispositif de capture et l'ajoutons à la session de capture.

Maintenant que nous avons configuré notre entrée, nous pouvons commencer à voir comment sortir ce que la caméra capture.

Ajoutez une sortie vidéo à notre session de capture.

```swift
// configuration de la sortie, ajout de la sortie à notre session de capture
let captureOutput = AVCaptureVideoDataOutput()
captureSession.addOutput(captureOutput)
```

`AVCaptureVideoDataOutput` est une sortie qui capture la vidéo. Elle nous donne également accès aux images capturées pour le traitement avec une méthode déléguée que nous verrons plus tard.

Ensuite, nous devons ajouter la sortie de la session de capture comme sous-couche à notre vue.

Ajoutez la sortie de la session de capture comme sous-couche à la vue du contrôleur de vue.

```swift
let previewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
previewLayer.frame = view.frame
view.layer.addSublayer(previewLayer)

captureSession.startRunning()
```

Nous créons une couche basée sur notre session de capture et ajoutons cette couche comme sous-couche à notre vue. `CaptureSession.startRunning()` commence le flux des entrées vers les sorties que nous avons connectées précédemment.

### 📷 Étape 4 : Permission d'utiliser la caméra ? Permission accordée.

Presque tout le monde a ouvert une application pour la première fois et a été invité à permettre à l'application d'utiliser la caméra. À partir d'iOS 10, notre application plantera si nous ne demandons pas à l'utilisateur avant d'essayer d'accéder à la caméra.

Accédez à `info.plist` et ajoutez une nouvelle clé nommée `NSCameraUsageDescription`. Dans la colonne valeur, expliquez simplement à l'utilisateur pourquoi votre application a besoin d'un accès à la caméra.

Maintenant, lorsque l'utilisateur lance l'application pour la première fois, il sera invité à permettre l'accès à la caméra.

### 🔊 Étape 5 : Obtenir le modèle.

Le cœur de ce projet est très probablement le modèle de machine learning. Le modèle doit être capable de prendre une image et de nous retourner une prédiction de ce qu'est l'image. Vous pouvez trouver des modèles entraînés gratuits [ici](https://developer.apple.com/machine-learning/). Celui que j'ai choisi est ResNet50.

Une fois que vous avez obtenu votre modèle, faites-le glisser et déposez-le dans Xcode. Il générera automatiquement les classes nécessaires, vous fournissant une interface pour interagir avec votre modèle.

### 🏛 Étape 6 : Analyse d'image.

Pour analyser ce que la caméra voit, nous devons somehow obtenir l'accès aux images capturées par la caméra.

Se conformer au `AVCaptureVideoDataOutputSampleBufferDelegate` nous donne une interface pour interagir et être notifié chaque fois qu'une image est capturée par la caméra.

Conformez `ViewController` au `AVCaptureVideoDataOutputSampleBufferDelegate`.

Nous devons dire à notre sortie vidéo que ViewController est son délégué de tampon d'échantillon.

Ajoutez la ligne suivante dans `SetupCaptureSession()` :

```swift
captureOutput.setSampleBufferDelegate(self, queue: DispatchQueue(label: "videoQueue"))

```

Ajoutez la fonction suivante :

```swift
func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        guard let model = try? VNCoreMLModel(for: Resnet50().model) else { return }
        let request = VNCoreMLRequest(model: model) { (finishedRequest, error) in
            guard let results = finishedRequest.results as? [VNClassificationObservation] else { return }
            guard let Observation = results.first else { return }
            
            DispatchQueue.main.async(execute: {
                self.label.text = "\(Observation.identifier)"
            })
        }
        guard let pixelBuffer: CVPixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
        
        // exécute la requête
        try? VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:]).perform([request])
    }
```

Chaque fois qu'une image est capturée, le délégué est notifié en appelant `captureOutput()`. C'est un endroit parfait pour faire notre analyse d'image avec CoreML.

Tout d'abord, nous créons un `VNCoreMLModel` qui est essentiellement un modèle CoreML utilisé avec le framework Vision. Nous le créons avec un modèle Resnet50.

Ensuite, nous créons notre requête de vision. Dans le gestionnaire d'achèvement, nous mettons à jour le UILabel à l'écran avec l'identifiant retourné par le modèle. Nous convertissons ensuite l'image qui nous est passée d'un `CMSampleBuffer` en un `CVPixelBuffer`. Qui est le format dont notre modèle a besoin pour l'analyse.

Enfin, nous exécutons la requête Vision avec un `VNImageRequestHandler`.

### 📝 Étape 7 : Créer une étiquette.

La dernière étape consiste à créer un `UILabel` contenant la prédiction du modèle.

Créez un nouveau `UILabel` et positionnez-le en utilisant des contraintes.

```swift
let label: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Label"
        label.font = label.font.withSize(30)
        return label
    }()

func setupLabel() {
        label.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        label.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -50).isActive = true
}
```

N'oubliez pas d'ajouter l'étiquette comme sous-vue et d'appeler `setupLabel()` depuis `ViewDidLoad()`.

```swift
view.addSubview(label)
setupLabel()
```

Vous pouvez télécharger le projet terminé depuis [GitHub ici](https://github.com/markmansur/CoreML-Vision-demo).

Aimez ce que vous voyez ? Donnez un pouce en l'air 👍 à cet article, suivez-moi sur [Twitter](https://twitter.com/MarkMansur2), [GitHub](https://github.com/markmansur), ou consultez [ma page personnelle](http://markmansur.me/).