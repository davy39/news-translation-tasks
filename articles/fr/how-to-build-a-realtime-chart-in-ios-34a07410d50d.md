---
title: Comment créer un graphique en temps réel dans iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T02:38:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-chart-in-ios-34a07410d50d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DLK3pjfoFjF_hCEU7Lkf2g.jpeg
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
seo_title: Comment créer un graphique en temps réel dans iOS
seo_desc: 'By Neo Ighodaro

  Nowadays, gathering data is one of the keys to understanding how products are perceived.
  Gathering some data from users can help you build better products and understand
  your users. However, all the data in the world would be useless ...'
---

Par Neo Ighodaro

De nos jours, la collecte de données est l'une des clés pour comprendre comment les produits sont perçus. Collecter des données auprès des utilisateurs peut vous aider à construire de meilleurs produits et à comprendre vos utilisateurs. Cependant, toutes les données du monde seraient inutiles sans un moyen de les visualiser.

Dans cet article, nous allons explorer comment créer un graphique en temps réel simple dans iOS. Le graphique recevra des données et se mettra à jour en temps réel sur les écrans de tous ceux qui sont actuellement connectés à votre application. Nous supposerons que ce graphique surveille le nombre de visiteurs utilisant un site web. Commençons.

Pour contexte, voici un exemple de ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/paeVVTUrY7xK9gLwZL2xmcLbJhjbIcSpm8dw)

Veuillez noter : Une compréhension de base de Swift et Node.js est nécessaire pour suivre ce tutoriel.

### Conditions préalables pour construire un graphique en temps réel dans iOS

Avant de commencer ce tutoriel, vous devrez avoir les conditions préalables suivantes :

* Un MacBook Pro.
* [Xcode](https://developer.apple.com/xcode/) installé sur votre machine.
* Connaissance de base de [Swift](https://developer.apple.com/swift/) et utilisation de Xcode.
* Connaissance de base de JavaScript (Node.js).
* [Node.js](https://docs.npmjs.com/getting-started/installing-node) et NPM installés sur votre machine.
* [Cocoapods](http://www.raywenderlich.com/12139/introduction-to-cocoapods) installé sur votre machine.
* Une application [Pusher](https://pusher.com)

Lorsque vous avez toutes les conditions préalables, nous pouvons commencer.

### Préparation à la création de notre application de graphique en temps réel dans Xcode

Lancez Xcode sur votre Mac et créez un nouveau projet (appelez-le comme vous voulez). Suivez l'assistant de nouvelle application et créez une nouvelle application **Single-page**. Une fois le projet créé, fermez Xcode et lancez votre application terminal.

Dans le terminal, `cd` à la racine du répertoire de l'application. Ensuite, exécutez la commande `pod init`. Cela générera un **Podfile**. Mettez à jour le contenu du Podfile avec le contenu ci-dessous (remplacez `PROJECT_NAME` par le nom de votre projet) :

```
platform :ios, '9.0'target 'PROJECT_NAME' do  use_frameworks!    pod 'Charts', '~> 3.0.2'  pod 'PusherSwift', '~> 4.1.0'  pod 'Alamofire', '~> 4.4.0'end
```

Enregistrez le Podfile et retournez dans votre terminal pour exécuter la commande : `pod install`.

L'exécution de cette commande installera tous les packages tiers dont nous avons besoin pour construire notre application de graphique iOS en temps réel.

Le premier package qu'il installera est [Charts](https://github.com/danielgindi/Charts), qui est un package pour créer de beaux graphiques sur iOS. Le deuxième package est le SDK Pusher swift. Le dernier package est [Alamofire](https://github.com/Alamofire/Alamofire), un package pour faire des requêtes HTTP sur iOS.

Une fois l'installation terminée, ouvrez le fichier `**.xcworkspace**` dans la racine de votre répertoire de projet. Cela devrait lancer Xcode. Maintenant, nous sommes prêts à commencer à créer notre application iOS.

### Création des vues de notre application de graphique en temps réel dans Xcode

Pour commencer, nous allons créer les vues nécessaires pour notre application de graphique en temps réel. Ouvrez le fichier **Main.storyboard** et commençons à concevoir notre vue.

Tout d'abord, créez une vue rectangulaire d'un bord à l'autre en haut du View Controller dans le storyboard. Dans cette vue, ajoutez un bouton et ajoutez le titre « Simuler les visites ». Ensuite, créez une autre vue qui est également un rectangle, s'étendant de la fin de la première vue ci-dessus au bas de l'écran. Cette vue sera l'endroit où nous rendrons le graphique en temps réel.

Lorsque vous avez terminé de créer les vues, vous devriez avoir quelque chose comme ce qui est montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/huuI0xR6kxUoSTaWfQCKN4NddLbtIkv8G5C6)

En l'état actuel, les vues ne font rien. Connectons quelques fonctionnalités à la vue de l'application de graphique iOS.

### Ajout de fonctionnalités de base à notre application de graphique iOS

Comme dit précédemment, les vues et les boutons de notre application ne sont pas connectés à notre `ViewController`, alors corrigeons cela.

Dans Xcode, alors que le storyboard est encore ouvert, cliquez sur le bouton « Show the Assistant Editor » en haut à droite de la page pour diviser la vue en storyboard et vue de code. Maintenant, cliquez une fois sur le bouton que vous avez créé, et tout en maintenant `ctrl`, cliquez et faites glisser le lien vers l'éditeur de code. Ensuite, créez un `@IBaction` comme vu dans les images ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qREVxZDqIVLbvbXVMEVNpFnVfrWtMGNBRoKz)

![Image](https://cdn-media-1.freecodecamp.org/images/-xNvKpDLIWBBQnEvmE4gWWFzOiCy0Raw9eAJ)

Lorsque le lien est complet, vous devriez voir quelque chose comme ceci ajouté à l'éditeur de code :

```
@IBAction func simulateButtonPressed(_ sender: Any) {}
```

Super ! Maintenant que vous avez créé le premier lien, nous devrons créer un autre lien vers la vue du graphique.

Sur votre storyboard, cliquez sur la vue et dans l'onglet « Identity Inspection », assurez-vous que la vue est connectée à `LineChartView` comme vu ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/8cXCATmAKj7FvkFjOAeRvzBh0qxhjU76cNuN)

Maintenant que la vue est connectée à une classe de vue, répétez la même opération que nous avons faite précédemment pour lier le bouton. Seulement cette fois, au lieu de créer un `@IBAction`, nous créerons un `@IBOutlet`. Les images sont montrées ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ryie0CqwHghtuz3m68Rp-3NFRbwWeumv4-kT)

![Image](https://cdn-media-1.freecodecamp.org/images/AEUIIpDFJsNUkZQG7aOZ4FPZmj8fMuziPfHZ)

Lorsque le lien est complet, vous devriez voir quelque chose comme ceci ajouté à l'éditeur de code :

```
@IBOutlet weak var chartView: LineChartView!
```

Enfin, en haut du `ViewController`, importez le package Charts. Vous pouvez ajouter le code ci-dessous juste sous `import UIKit` dans le `ViewController`.

```
import Charts
```

Maintenant que nous avons lié les deux éléments à notre code, chaque fois que le bouton **Simuler les visites** est pressé, la fonction **simulateButtonPressed** sera appelée.

### Ajout de fonctionnalités en temps réel à notre application de graphique iOS

La dernière pièce du puzzle sera d'afficher un graphique et de le faire mettre à jour en temps réel sur tous les appareils visualisant le graphique.

Pour y parvenir, nous ferons ce qui suit :

* Créer une fonction qui met à jour notre graphique en fonction des nombres.
* Faire en sorte que notre bouton de requête appelle le backend, qui à son tour enverra des données simulées à Pusher.
* Créer une fonction qui écoute les événements de Pusher et, lorsqu'un événement est reçu, déclenche la fonction de mise à jour du graphique que nous avons créée précédemment.

### Créer une fonction de déclenchement pour mettre à jour notre graphique

Créons la fonction qui met à jour notre graphique en fonction des nombres qui lui sont fournis. Ouvrez le `ViewController`, et dans celui-ci, déclarez une propriété de classe juste sous la déclaration de classe. Nous utiliserons cette propriété pour suivre les visiteurs :

```
var visitors: [Double] = []
```

Ensuite, nous ajouterons la fonction qui effectuera la mise à jour réelle de la vue du graphique :

```
private func updateChart() {    var chartEntry = [ChartDataEntry]()
```

```
    for i in 0..<visitors.count {        let value = ChartDataEntry(x: Double(i), y: visitors[i])        chartEntry.append(value)    }        let line = LineChartDataSet(values: chartEntry, label: "Visiteur")    line.colors = [UIColor.green]
```

```
    let data = LineChartData()    data.addDataSet(line)
```

```
    chartView.data = data    chartView.chartDescription?.text = "Compte des visiteurs"}
```

Dans le code ci-dessus, nous déclarons `chartEntry` où nous avons l'intention de stocker toutes nos données de graphique. Ensuite, nous parcourons les `visitors` disponibles et, pour chacun d'eux, nous ajoutons un nouveau `ChartDataEntry(x: Double(i), y: visitors[i])` qui indique au graphique les positions X et Y.

Nous définissons la couleur dans laquelle le graphique en ligne sera affiché. Nous créons le `LineChartData` et ajoutons la `line` qui contient nos points de données. Enfin, nous ajoutons les données à la `chartView` et définissons la description de la vue du graphique.

### Faire en sorte que notre bouton de simulation appelle un endpoint

La prochaine chose que nous devons faire est de faire en sorte que notre bouton de requête déclenche un backend, qui à son tour enverra des données simulées à Pusher.

Pour ce faire, nous devons mettre à jour le contrôleur de vue une fois de plus. Dans le `ViewController`, importez le package Alamofire juste sous le package Charts :

```
import Alamofire
```

Maintenant, remplacez la fonction `simulateButtonPressed` par le code ci-dessous :

```
@IBAction func simulateButtonPressed(_ sender: Any) {    Alamofire.request("http://localhost:4000/simulate", method: .post).validate().responseJSON { (response) in        switch response.result {        case .success(_):           _ = "Succès"        case .failure(let error):           print(error)        }    }}
```

Dans le code ci-dessous, nous utilisons Alamofire pour envoyer une requête POST à [http://localhost:4000/simulate](http://localhost:4000/simulate), qui est un serveur web local (nous créerons ce backend bientôt). Dans une application réelle, cela pointera généralement vers un serveur web réel.

Cet endpoint ne prend aucun paramètre afin de garder le tutoriel simple. Nous n'avons pas non plus besoin de faire quoi que ce soit avec la réponse. Nous avons juste besoin que la requête POST soit envoyée chaque fois que le bouton de simulation des visites est pressé.

### Intégrer les fonctionnalités en temps réel en utilisant Pusher

Pour faire fonctionner tout cela, nous allons créer une fonction qui écoute les événements de Pusher et, lorsqu'un événement est reçu, nous enregistrons la valeur dans `visitors` et déclenchons ensuite la fonction de mise à jour du graphique que nous avons créée précédemment.

Pour ce faire, ouvrez le `ViewController` et importez le SDK `PusherSwift` sous le package Alamofire en haut :

```
import PusherSwift
```

Ensuite, nous déclarerons une propriété de classe pour l'instance Pusher. Nous pouvons le faire juste sous la ligne de déclaration `visitors` :

```
var pusher: Pusher!
```

Puis, après avoir déclaré la propriété, nous devons ajouter la fonction ci-dessous à la classe afin qu'elle puisse écouter les événements :

```
private func listenForChartUpdates() {    pusher = Pusher(        key: "PUSHER_KEY",         options: PusherClientOptions(            host: .cluster("PUSHER_CLUSTER")        )    )    let channel = pusher.subscribe("visitorsCount")    channel.bind(eventName: "addNumber", callback: { (data: Any?) -> Void in       if let data = data as? [String: AnyObject] {           let count = data["count"] as! Double           self.visitors.append(count)           self.updateChart()       }    })    pusher.connect()}
```

Dans le code ci-dessus, nous instancions Pusher et passons notre clé et le cluster (vous pouvez obtenir votre clé et votre cluster depuis le tableau de bord de votre application Pusher). Nous nous abonnons ensuite au canal `visitorsChannel` et nous lions à l'événement `addNumber` sur ce canal.

Lorsque l'événement est déclenché, nous exécutons la logique dans le callback qui ajoute simplement le compte à `visitors` et appelle ensuite la fonction `updateChart`, qui met à jour le graphique réel en temps réel.

Enfin, nous appelons `pusher.connect()` qui établit la connexion à Pusher.

Dans la fonction `viewDidLoad`, ajoutez simplement un appel à la méthode `listenForChartUpdates` :

```
override func viewDidLoad() {    super.viewDidLoad()    // ...stuff        listenForChartUpdates()}
```

C'est tout ! Nous avons créé notre application dans Xcode et nous sommes prêts pour les tests. Cependant, pour tester, nous devons créer le backend auquel nous envoyons une requête `POST` lorsque le bouton est cliqué. Pour créer ce backend, nous utiliserons Node.js. Faisons cela maintenant.

### Création du service backend pour notre application de graphique iOS en temps réel

Pour commencer, créez un répertoire pour l'application web, puis créez quelques nouveaux fichiers à l'intérieur du répertoire :

Fichier : **index.js**

```
// -------------------------------------------------------// Require Node dependencies// -------------------------------------------------------
```

```
let Pusher     = require('pusher');let express    = require('express');let bodyParser = require('body-parser');let app        = express();
```

```
// Instantiate Pusherlet pusher     = new Pusher(require('./config.js'));
```

```
// -------------------------------------------------------// Load express middlewares// -------------------------------------------------------
```

```
app.use(bodyParser.json());app.use(bodyParser.urlencoded({ extended: false }));
```

```
// -------------------------------------------------------// Simulate multiple changes to the visitor count value,// this way the chart will always update with different// values.// -------------------------------------------------------
```

```
app.post('/simulate', (req, res, next) => {    var loopCount = 0;    let sendToPusher = setInterval(function(){    let count = Math.floor((Math.random() * (100 - 1)) + 1)    pusher.trigger('visitorsCount', 'addNumber', {count:count})    loopCount++;    if (loopCount === 20) {        clearInterval(sendToPusher);    }    }, 2000);    res.json({success: 200})})
```

```
// Handle indexapp.get('/', (req, res) => {    res.json("It works!");});
```

```
// Handle 404'sapp.use((req, res, next) => {    let err = new Error('Not Found');    err.status = 404;    next(err);});
```

```
// -------------------------------------------------------// Serve application// -------------------------------------------------------
```

```
app.listen(4000, function(){    console.log('App listening on port 4000!')});
```

Le fichier ci-dessus est une application Express simple écrite en JavaScript. Nous instancions tous les packages dont nous avons besoin et configurons Pusher en utilisant un fichier de configuration que nous créerons bientôt. Ensuite, nous créons une route `/simulate` et dans cette route, nous déclenchons l'événement `addNumber` dans le canal `visitorCount`. C'est le même canal et événement que l'application écoute.

Pour faciliter les choses, nous utilisons `setInterval` pour envoyer un compte de visiteurs aléatoire au backend Pusher toutes les 2000 millisecondes. Après 20 boucles, la boucle s'arrête. Cela devrait être suffisant pour tester notre application.

Créez le fichier suivant **config.js** :

```
module.exports = {    appId: 'PUSHER_APP_ID',    key: 'PUSHER_APP_KEY',    secret: 'PUSHER_APP_SECRET',    cluster: 'PUSHER_APP_CLUSTER',};
```

Dans ce fichier, nous déclarons simplement les dépendances.

Ouvrez le terminal et `cd` à la racine du répertoire de l'application web. Exécutez les commandes ci-dessous pour installer les dépendances NPM et exécuter l'application respectivement :

```
$ npm install$ node index.js
```

Lorsque l'installation est terminée et que l'application est prête, vous devriez voir la sortie ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/gTvq-SQMzsRUv7V3-pRpPCI86EImjbY-fB8Z)

### Test de l'application

Une fois que votre serveur web local Node est en cours d'exécution, vous devrez apporter quelques modifications pour que votre application puisse communiquer avec le serveur web local. Dans le fichier `info.plist`, apportez les modifications suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/kVCEsKQ9oIKlWITzxNKQ8hOSBxc16eA60bkA)

Avec cette modification, vous pouvez construire et exécuter votre application et elle communiquera directement avec votre application web locale.

### Conclusion

Cet article vous a montré comment vous pouvez combiner Pusher et le package Charts pour créer une application de graphique iOS en temps réel. Il existe de nombreux autres types de graphiques que vous pouvez créer en utilisant le package, mais pour être bref, nous avons fait le plus simple. Vous pouvez explorer les autres types de graphiques et même passer plusieurs points de données par requête.

Cet article est d'abord apparu sur le [blog de Pusher](https://pusher.com/tutorials/chart-swift/).