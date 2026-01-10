---
title: Comment créer une carte en temps réel avec Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-10T22:09:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-map-with-swift-67fb0e977e48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*56icJ6WPoNlPAcAlhzEZCg.jpeg
tags:
- name: iOS
  slug: ios
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment créer une carte en temps réel avec Swift
seo_desc: 'By Neo Ighodaro

  Realtime maps are very popular nowadays. Especially now that there are many on-demand
  transportation services like Uber and Lyft that have realtime location reporting.
  In this article, we are going to learn how to build a realtime map...'
---

Par Neo Ighodaro

Les cartes en temps réel sont très populaires de nos jours. Surtout maintenant qu'il existe de nombreux services de transport à la demande comme Uber et Lyft qui ont un suivi de localisation en temps réel. Dans cet article, nous allons apprendre comment créer une carte en temps réel sur iOS en utilisant Pusher.

Avant de continuer, assurez-vous d'avoir toutes les conditions préalables suivantes :

* Un MacBook (Xcode ne fonctionne que sur Mac).
* [Xcode](https://developer.apple.com/xcode/) installé sur votre machine.
* Connaissance de JavaScript (Node.js).
* Connaissance de Swift et de l'utilisation de Xcode. Vous pouvez commencer [ici](https://developer.apple.com/library/content/referencelibrary/GettingStarted/DevelopiOSAppsSwift/).
* [NPM et Node.js](https://docs.npmjs.com/getting-started/installing-node) installés localement.
* Le gestionnaire de paquets [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installé localement.
* Une clé API Google iOS. Voir [ici](https://developers.google.com/maps/documentation/ios-sdk/start#step_4_get_an_api_key) pour des instructions sur la façon d'obtenir une clé.
* Une application Pusher. Créez-en une [ici](https://pusher.com).

Une compréhension de base de Swift et de Node.js est nécessaire pour suivre ce tutoriel.

En supposant que vous avez toutes les conditions préalables, commençons. Voici un enregistrement d'écran de ce que nous allons créer :

![Image](https://cdn-media-1.freecodecamp.org/images/oNEt5czqqZUmTL5r6SvWAjv2QBSnWgYEr8RT)

Comme vous pouvez le voir dans la démo, chaque fois que la localisation est mise à jour, le changement est reflété sur les deux appareils. C'est ce que nous voulons reproduire. Commençons.

### Installation de notre application iOS

Lancez Xcode et créez un nouveau projet "Single-app". Vous pouvez nommer le projet comme vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/SykobSVDuoF5VSM3PZeNvC4sISPAbkoYUwIb)

Lorsque le projet est créé, fermez Xcode. Ouvrez votre terminal, `cd` vers le répertoire racine de votre application, et exécutez la commande suivante pour initialiser Cocoapods sur le projet :

```
$ pod init
```

La commande ci-dessus créera un fichier `Podfile` dans le répertoire racine de notre application. Dans ce `Podfile`, nous spécifierons les dépendances de notre projet et laisserons Cocoapods les récupérer et les gérer. Ouvrez le `Podfile` et remplacez le contenu du fichier par le contenu ci-dessous :

```
platform :ios, '10.0'
target 'nom_de_l_application' do    use_frameworks!
```

```
    pod 'GoogleMaps'
    pod 'Alamofire', '~> 4.4.0'
    pod 'PusherSwift', '~> 4.1.0'
end
```

> ⚠️ Assurez-vous de remplacer `nom_de_l_application` par le nom de votre application.

Exécutez la commande suivante pour commencer à installer les paquets que nous avons spécifiés dans notre `Podfile` :

```
$ pod install
```

Lorsque l'installation est terminée, ouvrez le fichier `*.xcworkspace` qui a été ajouté à la racine de votre répertoire d'application. Cela devrait lancer Xcode.

### Configuration de notre application simulateur Node.js

Avant de retourner à notre application iOS, nous devons créer une application Node.js simple. Cette application enverra des événements avec des données à Pusher. Les données envoyées à Pusher seront des coordonnées GPS simulées. Lorsque notre application iOS récupère les données de l'événement depuis Pusher, elle mettra à jour le marqueur de la carte avec les nouvelles coordonnées.

Créez un nouveau répertoire qui contiendra notre application Node.js. Ouvrez votre terminal et `cd` vers le répertoire de votre application Node.js. Dans ce répertoire, créez un nouveau fichier `package.json`. Ouvrez ce fichier et collez le JSON ci-dessous :

```
{
  "main": "index.js",
  "dependencies": {
    "body-parser": "^1.16.0",
    "express": "^4.14.1",
    "pusher": "^1.5.1"
  }
}
```

Exécutez maintenant la commande suivante pour installer les paquets NPM listés comme dépendances :

```
$ npm run install
```

Créez un nouveau fichier `index.js` dans le répertoire et collez le code ci-dessous dans le fichier :

```
//
// Charge les bibliothèques requises
//
let Pusher     = require('pusher');
let express    = require('express');
let bodyParser = require('body-parser');
//
// Initialise express et pusher
//
let app        = express();
let pusher     = new Pusher(require('./config.js'));
//
// Middlewares
//
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
```

```
//
// Génère 20 coordonnées GPS simulées et les envoie à Pusher
//
app.post('/simuler', (req, res, next) => {
  let loopCount = 0;
  let operator = 0.001000
  let longitude = parseFloat(req.body.longitude)
  let latitude  = parseFloat(req.body.latitude)
  let sendToPusher = setInterval(() => {
    loopCount++;
    // Calcule les nouvelles coordonnées et les arrondit à 6 décimales...
    longitude = parseFloat((longitude + operator).toFixed(7))
    latitude  = parseFloat((latitude - operator).toFixed(7))
    // Envoie à pusher
    pusher.trigger('mapCoordinates', 'update', {longitude, latitude})
    if (loopCount === 20) {
      clearInterval(sendToPusher)
    }
  }, 2000);
  res.json({success: 200})
})
```

```
//
// Index
//
app.get('/', (req, res) => {
  res.json("Ça marche !");
});
```

```
//
// Gestion des erreurs
//
app.use((req, res, next) => {
  let err = new Error('Not Found');
  err.status = 404;
  next(err);
});
```

```
//
// Lance l'application
//
app.listen(4000, function() {
  console.log('App listening on port 4000!')});
```

Le code ci-dessus est une application Express simple. Nous avons initialisé l'application `app` Express et l'instance `pusher`. Dans la route `/simuler`, nous exécutons une boucle à des intervalles de 2 secondes et interrompons la boucle après la 20ème exécution. Chaque fois que la boucle s'exécute, de nouvelles coordonnées GPS sont générées et envoyées à Pusher.

Créez un nouveau fichier `config.js` et collez le code ci-dessous dedans :

```
module.exports = {
  appId: 'PUSHER_APP_ID',
  key: 'PUSHER_APP_KEY',
  secret: 'PUSHER_APP_SECRET',
  cluster: 'PUSHER_APP_CLUSTER',
};
```

Remplacez les valeurs de `*PUSHER_APP_ID*`, `*PUSHER_APP_KEY*`, `PUSHER_APP_SECRET` et `PUSHER_APP_CLUSTER` par les valeurs dans le tableau de bord de votre application Pusher. Notre application Node.js est maintenant prête à simuler des coordonnées GPS lorsque notre application la déclenche.

Maintenant que nous avons terminé la création de l'application Node.js, nous pouvons revenir à la création de l'application iOS.

### Création des vues de notre carte en temps réel dans Xcode

Rouvrez Xcode avec notre projet et ouvrez le fichier `Main.storyboard`. Dans le `ViewController`, nous allons ajouter une `UIView`, et dans cette `UIView`, nous allons ajouter un bouton de simulation. Quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/rOVmC-h3c2R2xCeeuPcTlp8g7fG5Yr-tWJl6)

Créez une `@IBAction` à partir du bouton vers le `ViewController`. Pour ce faire, cliquez sur "Show the Assistant Editor" en haut à droite de l'ensemble d'outils Xcode. Cela divise l'écran en storyboard et éditeur de code. Maintenant, `ctrl` et faites glisser le bouton vers l'éditeur de code pour créer l'`@IBAction`. Nous appellerons la méthode `simulateMovement`.

![Image](https://cdn-media-1.freecodecamp.org/images/sirx-Tu8WaaGQUQVz4IKvuTdFlhZELT2qM0F)

Ensuite, cliquez sur le bouton "Show standard editor" dans la barre d'outils Xcode pour fermer l'écran divisé et afficher uniquement le `Main.storyboard`. Ajoutez une autre `UIView` à partir du bas de la dernière `UIView` jusqu'au bas de l'écran. Cette vue sera l'endroit où la carte sera affichée.

Définissez la classe personnalisée de la `UIView` dans l'inspecteur "Identity" sur `GMSMapView`. Maintenant, cliquez sur "Show the Assistant Editor" en haut à droite de l'ensemble d'outils Xcode. `ctrl` et faites glisser la `UIView` vers l'éditeur de code. Créez une `@IBOutlet` et nommez-la `mapView`.

Cliquez sur le bouton "Show standard editor" dans la barre d'outils Xcode pour fermer la vue divisée. Ouvrez le fichier `ViewController` et remplacez le contenu par le code ci-dessous :

```
//
// Import des bibliothèques
//
import UIKit
import PusherSwift
import Alamofire
import GoogleMaps
```

```
//
// Classe du contrôleur de vue
//
class ViewController: UIViewController, GMSMapViewDelegate {
  // Marqueur sur la carte
  var locationMarker: GMSMarker!
```

```
  // Coordonnées de départ par défaut
  var longitude = -122.088426
  var latitude  = 37.388064
```

```
  // Pusher
  var pusher: Pusher!
```

```
  // Vue de la carte
  @IBOutlet weak var mapView: GMSMapView!
```

```
  //
  // Se déclenche automatiquement lorsque la vue est chargée
  //
  override func viewDidLoad() {
    super.viewDidLoad()
```

```
    //
    // Crée une GMSCameraPosition qui indique à la carte d'afficher la coordonnée
    // à un niveau de zoom de 15.
    //
    let camera = GMSCameraPosition.camera(withLatitude:latitude, longitude:longitude, zoom:15.0)
    mapView.camera = camera
    mapView.delegate = self
```

```
    //
    // Crée un marqueur au centre de la carte.
    //
    locationMarker = GMSMarker(position: CLLocationCoordinate2D(latitude: latitude, longitude: longitude))
    locationMarker.map = mapView
```

```
    //
    // Se connecte à Pusher et écoute les événements
    //
    listenForCoordUpdates()
  }
```

```
  //
  // Envoie une requête à l'API pour simuler des coordonnées GPS
  //
  @IBAction func simulateMovement(_ sender: Any) {
    let parameters: Parameters = ["longitude":longitude, "latitude": latitude]
```

```
    Alamofire.request("http://localhost:4000/simuler", method: .post, parameters: parameters).validate().responseJSON { (response) in
      switch response.result {
      case .success(_):
        print("Simulation en cours...")
      case .failure(let error):
        print(error)
      }
    }
  }
```

```
  //
  // Se connecte à Pusher et écoute les événements
  //
  private func listenForCoordUpdates() {
    // Instancie Pusher
    pusher = Pusher(key: "PUSHER_APP_KEY", options: PusherClientOptions(host: .cluster("PUSHER_APP_CLUSTER")))
```

```
    // S'abonne à un canal Pusher
    let channel = pusher.subscribe("mapCoordinates")
```

```
    //
    // Écouteur et rappel pour l'événement "update" sur le canal "mapCoordinates"
    // sur Pusher
    //
    channel.bind(eventName: "update", callback: { (data: Any?) -> Void in
      if let data = data as? [String: AnyObject] {
        self.longitude = data["longitude"] as! Double
        self.latitude  = data["latitude"] as! Double
```

```
        //
        // Met à jour la position du marqueur en utilisant les données de Pusher
        //
        self.locationMarker.position = CLLocationCoordinate2D(latitude: self.latitude, longitude: self.longitude)
        self.mapView.camera = GMSCameraPosition.camera(withTarget: self.locationMarker.position, zoom: 15.0)
      }
    })
```

```
    // Se connecte à Pusher
    pusher.connect()
  }
}
```

Dans la classe de contrôleur ci-dessus, nous importons toutes les bibliothèques requises. Ensuite, nous instancions quelques propriétés sur la classe. Dans la méthode `viewDidLoad`, nous définissons les coordonnées sur la `mapView`, et ajoutons également le `locationMarker` à celle-ci.

Dans la même méthode, nous faisons un appel à `listenForCoordUpdates()`. Dans la méthode `listenForCoordUpdates`, nous créons une connexion à Pusher et écoutons l'événement `update` sur le canal `mapCoordinates`.

Lorsque l'événement `update` est déclenché, le rappel prend les nouvelles coordonnées et met à jour le `locationMarker` avec celles-ci. N'oubliez pas que vous devez changer `PUSHER_APP_KEY` et `PUSHER_APP_CLUSTER` par les valeurs réelles fournies pour votre application Pusher.

Dans la méthode `simulateMovement`, nous envoyons simplement une requête à notre serveur web local (l'application Node.js que nous avons créée précédemment). La requête instruira l'application Node.js de générer plusieurs coordonnées GPS.

> ❓ L'URL du point de terminaison que nous atteignons (h[ttp://localhost:3000/simuler)](http://localhost:3000/simuler) est un serveur web local. Cela signifie que vous devrez changer l'URL du point de terminaison lors de la création pour des cas réels.

### Configuration de Google Maps pour iOS

Nous devons configurer le SDK Google Maps iOS pour qu'il fonctionne avec notre application. Tout d'abord, [créez une clé SDK Google iOS](https://developers.google.com/maps/documentation/ios-sdk/start#step_4_get_an_api_key), puis, une fois que vous avez la clé API, ouvrez le fichier `AppDelegate.swift` dans Xcode.

Dans la classe, recherchez la classe ci-dessous :

```
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
  // Point de substitution pour la personnalisation après le lancement de l'application.
  return true
}
```

et remplacez-la par ceci :

```
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
  GMSServices.provideAPIKey("GOOGLE_IOS_API_KEY")
  return true
}
```

> ❓ Vous devez remplacer `GOOGLE_IOS_API_KEY` par la clé que vous avez obtenue lorsque vous avez créé la clé API Google iOS.

En haut du même fichier, recherchez `import UIKit` et ajoutez ce qui suit en dessous :

```
import GoogleMaps
```

Avec cela, nous avons terminé la configuration de Google Maps pour qu'il fonctionne sur iOS.

### Test de notre carte iOS en temps réel

Pour tester notre application, nous devons démarrer l'application Node.js, instruire iOS d'autoriser les connexions au serveur web local, puis exécuter notre application iOS.

Pour exécuter l'application Node.js, `cd` vers le répertoire de l'application Node.js en utilisant votre terminal et exécutez la commande suivante pour démarrer l'application Node :

```
$ node index.js
```

Maintenant, avant de lancer notre application, nous devons apporter quelques modifications finales pour que notre application iOS puisse se connecter à notre backend `localhost`. Ouvrez le fichier `info.plist` dans Xcode et apportez les ajustements suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/k0V9gHDnWihDnOigSrwEOias6xFVD0Di-5Td)

Cette modification permettra à notre application de se connecter à localhost. Pour être clair, cette étape ne sera pas nécessaire dans les environnements de production.

Maintenant, construisez votre application. Vous devriez voir que l'application iOS affiche maintenant la carte et le marqueur sur la carte. En cliquant sur le bouton de simulation, vous atteignez le point de terminaison qui envoie à son tour les nouvelles coordonnées à Pusher. Notre écouteur capture l'événement et met à jour le `locationMarker`, déplaçant ainsi notre marqueur.

### Conclusion

Dans cet article, nous avons vu comment nous pouvons utiliser Pusher et Swift pour créer une carte en temps réel sur iOS. J'espère que vous avez appris quelques choses sur la création d'applications iOS en temps réel. Si vous avez des questions ou des suggestions, n'hésitez pas à laisser un commentaire ci-dessous.

Cet article a été publié pour la première fois sur Pusher.