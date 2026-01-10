---
title: Comment créer un éditeur de texte collaboratif en utilisant Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T01:11:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-collaborative-text-editor-using-swift-df7402c82510
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Y-djx_fBY4GWJoNR6pVAw.jpeg
tags:
- name: coding
  slug: coding
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment créer un éditeur de texte collaboratif en utilisant Swift
seo_desc: 'By Neo Ighodaro

  Text editors are increasingly popular these days, whether they’re embedded in a
  website comment form or used as a notepad. There are many different editors to choose
  from. In this post, we are not only going to learn how to build a be...'
---

Par Neo Ighodaro

Les éditeurs de texte sont de plus en plus populaires ces jours-ci, qu'ils soient intégrés dans un formulaire de commentaire de site web ou utilisés comme bloc-notes. Il existe de nombreux éditeurs différents parmi lesquels choisir. Dans cet article, nous allons non seulement apprendre à créer une belle application mobile d'éditeur de texte sur iOS, mais aussi comment rendre possible la collaboration sur une note en temps réel en utilisant Pusher.

Veuillez noter, cependant, que pour garder l'application simple, l'article ne couvrira pas les éditions concurrentes. Par conséquent, une seule personne peut éditer à la fois tandis que les autres regardent.

L'application fonctionnera en déclenchant un événement lorsqu'un texte est saisi. Cet événement sera envoyé à Pusher puis récupéré par l'appareil du collaborateur et mis à jour automatiquement.

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

1. **Cocoapods** : pour installer, exécutez `gem install cocoapods` sur votre machine
2. **Xcode**
3. Une **application Pusher** : vous pouvez créer un compte et une application gratuits [ici](https://pusher.com)
4. Quelques connaissances du langage **Swift**
5. **Node.js**

Enfin, une compréhension de base de Swift et Node.js est nécessaire pour suivre ce tutoriel.

### Commencer avec notre application iOS dans Xcode

Lancez Xcode et créez un nouveau projet. J'appellerai le mien **Collabo**. Après avoir suivi l'assistant de configuration, et avec l'espace de travail ouvert, fermez Xcode puis `cd` à la racine de votre projet et exécutez la commande `pod init`. Cela devrait générer un `Podfile` pour vous. Changez le contenu du `Podfile` :

```
# Décommentez la ligne suivante pour définir une plateforme globale pour votre projet    platform :ios, '9.0'
```

```
    target 'textcollabo' do      # Commentez la ligne suivante si vous n'utilisez pas Swift et ne voulez pas utiliser de frameworks dynamiques      use_frameworks!
```

```
      # Pods pour anonchat      pod 'Alamofire'      pod 'PusherSwift'    end
```

Exécutez maintenant la commande `pod install` afin que le gestionnaire de packages Cocoapods puisse récupérer les dépendances nécessaires. Une fois cela terminé, fermez Xcode (si ouvert) puis ouvrez le fichier `.xcworkspace` qui se trouve à la racine de votre dossier de projet.

### Concevoir les vues pour notre application iOS

Nous allons créer quelques vues pour notre application iOS. Ce seront les éléments de base où nous allons attacher toute la logique. En utilisant le storyboard d'Xcode, faites en sorte que vos vues ressemblent un peu aux captures d'écran ci-dessous.

Ceci est le fichier **LaunchScreen.storyboard**. J'ai simplement conçu quelque chose de simple sans aucune fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/QzhBjZMrhJiM66feDQLG6npu-aYqA1VEgGlt)

Le prochain storyboard que nous allons concevoir est le **Main.storyboard**. Comme son nom l'indique, ce sera le principal. C'est ici que nous avons toutes les vues importantes qui sont attachées à une certaine logique.

![Image](https://cdn-media-1.freecodecamp.org/images/eibpbvrTnwGPiY9BGpN2dcvELgUgtczDbH-K)

Ici, nous avons trois vues.

La première vue est conçue pour ressembler exactement à l'écran de lancement, à l'exception d'un bouton que nous avons lié pour ouvrir la deuxième vue.

La deuxième vue est le contrôleur de navigation. Il est attaché à une troisième vue qui est un `ViewController`. Nous avons défini la troisième vue comme le contrôleur racine de notre contrôleur de navigation.

Dans la troisième vue, nous avons un `UITextView` qui est modifiable et qui est placé dans la vue. Il y a aussi une étiquette qui est censée être un compteur de caractères. C'est l'endroit où nous allons incrémenter les caractères à mesure que l'utilisateur tape du texte dans la vue de texte.

### Coder l'application d'éditeur de texte collaboratif iOS

Maintenant que nous avons créé avec succès les vues nécessaires pour que l'application se charge, la prochaine chose que nous allons faire est de commencer à coder la logique de l'application.

Créez un nouveau fichier de classe cocoa et nommez-le `TextEditorViewController` et liez-le à la troisième vue dans le fichier `Main.storyboard`. Le `TextViewController` doit également adopter le `UITextViewDelegate`. Maintenant, vous pouvez `ctrl+glisser` le `UITextView` et aussi `ctrl+glisser` le `UILabel` dans le fichier `Main.storyboard` vers la classe `TextEditorViewController`.

De plus, vous devez importer les bibliothèques `PusherSwift` et `AlamoFire` dans le `TextViewController`. Vous devriez avoir quelque chose de proche de ceci une fois que vous avez terminé :

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        @IBOutlet weak var textView: UITextView!        @IBOutlet weak var charactersLabel: UILabel!    }
```

Maintenant, nous devons ajouter quelques propriétés dont nous aurons besoin plus tard dans le contrôleur.

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        static let API_ENDPOINT = "http://localhost:4000";
```

```
        @IBOutlet weak var textView: UITextView!
```

```
        @IBOutlet weak var charactersLabel: UILabel!
```

```
        var pusher : Pusher!
```

```
        var chillPill = true
```

```
        var placeHolderText = "Commencez à taper..."
```

```
        var randomUuid : String = ""    }
```

Maintenant, nous allons diviser la logique en trois parties :

1. Événements de vue et de clavier
2. Méthodes UITextViewDelegate
3. Gestion des événements Pusher.

#### **Événements de vue et de clavier**

Ouvrez le `TextEditorViewController` et mettez-le à jour avec les méthodes ci-dessous :

```
override func viewDidLoad() {        super.viewDidLoad()        // Déclencheur de notification        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)        // Reconnaisseur de geste        view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(tappedAwayFunction(_:))))        // Définir le contrôleur comme délégué de textView        textView.delegate = self        // Définir l'ID de l'appareil        randomUuid = UIDevice.current.identifierForVendor!.uuidString        // Écouter les changements de Pusher        listenForChanges()    }    override func viewWillAppear(_ animated: Bool) {        super.viewWillAppear(animated)        if self.textView.text == "" {            self.textView.text = placeHolderText            self.textView.textColor = UIColor.lightGray        }    }    func keyboardWillShow(notification: NSNotification) {        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {            if self.charactersLabel.frame.origin.y == 1.0 {                self.charactersLabel.frame.origin.y -= keyboardSize.height            }        }    }    func keyboardWillHide(notification: NSNotification) {        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {            if self.view.frame.origin.y != 1.0 {                self.charactersLabel.frame.origin.y += keyboardSize.height            }        }    }
```

Dans la méthode `viewDidLoad`, nous avons enregistré les fonctions du clavier afin qu'elles répondent aux événements du clavier. Nous avons également ajouté des reconnaisseurs de gestes qui feront disparaître le clavier lorsque vous tapez à l'extérieur du `UITextView`. Et nous avons défini le délégué `textView` sur le contrôleur lui-même. Enfin, nous avons appelé une fonction pour écouter les nouvelles mises à jour (que nous créerons plus tard).

Dans la méthode `viewWillAppear`, nous avons simplement modifié le `UITextView` pour qu'il ait un texte de remplacement, car, par défaut, le `UITextView` n'a pas cette fonctionnalité. Je me demande pourquoi, Apple...

Dans les fonctions `keyboardWillShow` et `keyboardWillHide`, nous avons fait en sorte que l'étiquette de compteur de caractères monte avec le clavier et redescende avec lui, respectivement. Cela empêchera le clavier de couvrir l'étiquette lorsqu'il est actif.

#### **Méthodes UITextViewDelegate**

Mettez à jour le `TextEditorViewController` avec ce qui suit :

```
func textViewDidChange(_ textView: UITextView) {        charactersLabel.text = String(format: "%i Caractères", textView.text.characters.count)
```

```
        if textView.text.characters.count >= 2 {            sendToPusher(text: textView.text)        }    }
```

```
    func textViewShouldBeginEditing(_ textView: UITextView) -> Bool {        self.textView.textColor = UIColor.black
```

```
        if self.textView.text == placeHolderText {            self.textView.text = ""        }
```

```
        return true    }
```

```
    func textViewDidEndEditing(_ textView: UITextView) {        if textView.text == "" {            self.textView.text = placeHolderText            self.textView.textColor = UIColor.lightGray        }    }
```

```
    func tappedAwayFunction(_ sender: UITapGestureRecognizer) {        textView.resignFirstResponder()    }
```

La méthode `textViewDidChange` met simplement à jour l'étiquette de compteur de caractères et envoie également les changements à Pusher en utilisant notre API backend (que nous allons créer dans un instant).

La méthode `textViewShouldBeginEditing` est obtenue à partir du `UITextViewDelegate` et elle est déclenchée lorsque la vue de texte est sur le point d'être éditée. Ici, nous jouons simplement avec le texte de remplacement, comme dans la méthode `textViewDidEndEditing`.

Enfin, dans la méthode `tappedAwayFunction`, nous définissons le rappel d'événement pour le geste que nous avons enregistré dans la section précédente. Dans la méthode, nous faisons simplement disparaître le clavier.

#### **Gestion des événements Pusher**

Mettez à jour le contrôleur avec les méthodes suivantes :

```
func sendToPusher(text: String) {        let params: Parameters = ["text": text, "from": randomUuid]
```

```
        Alamofire.request(TextEditorViewController.API_ENDPOINT + "/update_text", method: .post, parameters: params).validate().responseJSON { response in            switch response.result {
```

```
            case .success:                print("Succès")            case .failure(let error):                print(error)            }        }    }
```

```
    func listenForChanges() {        pusher = Pusher(key: "PUSHER_KEY", options: PusherClientOptions(            host: .cluster("PUSHER_CLUSTER")        ))
```

```
        let channel = pusher.subscribe("collabo")        let _ = channel.bind(eventName: "text_update", callback: { (data: Any?) -> Void in
```

```
            if let data = data as? [String: AnyObject] {                let fromDeviceId = data["deviceId"] as! String
```

```
                if fromDeviceId != self.randomUuid {                    let text = data["text"] as! String                    self.textView.text = text                    self.charactersLabel.text = String(format: "%i Caractères", text.characters.count)                }            }        })
```

```
        pusher.connect()    }
```

Dans la méthode `sendToPusher`, nous envoyons la charge utile à notre application backend en utilisant `AlamoFire`, qui, à son tour, l'enverra à Pusher.

Dans la méthode `listenForChanges`, nous écoutons ensuite les changements apportés au texte et, s'il y en a, nous appliquons les changements à la vue de texte.

> _? R**emember to replace the key and cluster with the actual value you have gotten from your Pusher dashboard.**_

Si vous avez suivi le tutoriel de près, alors votre `TextEditorViewController` devrait ressembler à quelque chose comme ceci :

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        static let API_ENDPOINT = "http://localhost:4000";
```

```
        @IBOutlet weak var textView: UITextView!
```

```
        @IBOutlet weak var charactersLabel: UILabel!
```

```
        var pusher : Pusher!
```

```
        var chillPill = true
```

```
        var placeHolderText = "Start typing..."
```

```
        var randomUuid : String = ""
```

```
        override func viewDidLoad() {            super.viewDidLoad()
```

```
            // Notification trigger            NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)            NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)
```

```
            // Gesture recognizer            view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(tappedAwayFunction(_:))))
```

```
            // Set the controller as the textView delegate            textView.delegate = self
```

```
            // Set the device ID            randomUuid = UIDevice.current.identifierForVendor!.uuidString
```

```
            // Listen for changes from Pusher            listenForChanges()        }
```

```
        override func viewWillAppear(_ animated: Bool) {            super.viewWillAppear(animated)
```

```
            if self.textView.text == "" {                self.textView.text = placeHolderText                self.textView.textColor = UIColor.lightGray            }        }
```

```
        func keyboardWillShow(notification: NSNotification) {            if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {                if self.charactersLabel.frame.origin.y == 1.0 {                    self.charactersLabel.frame.origin.y -= keyboardSize.height                }            }        }
```

```
        func keyboardWillHide(notification: NSNotification) {            if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {                if self.view.frame.origin.y != 1.0 {                    self.charactersLabel.frame.origin.y += keyboardSize.height                }            }        }
```

```
        func textViewDidChange(_ textView: UITextView) {            charactersLabel.text = String(format: "%i Characters", textView.text.characters.count)
```

```
            if textView.text.characters.count >= 2 {                sendToPusher(text: textView.text)            }        }
```

```
        func textViewShouldBeginEditing(_ textView: UITextView) -> Bool {            self.textView.textColor = UIColor.black
```

```
            if self.textView.text == placeHolderText {                self.textView.text = ""            }
```

```
            return true        }
```

```
        func textViewDidEndEditing(_ textView: UITextView) {            if textView.text == "" {                self.textView.text = placeHolderText                self.textView.textColor = UIColor.lightGray            }        }
```

```
        func tappedAwayFunction(_ sender: UITapGestureRecognizer) {            textView.resignFirstResponder()        }
```

```
        func sendToPusher(text: String) {            let params: Parameters = ["text": text, "from": randomUuid]
```

```
            Alamofire.request(TextEditorViewController.API_ENDPOINT + "/update_text", method: .post, parameters: params).validate().responseJSON { response in                switch response.result {
```

```
                case .success:                    print("Succeeded")                case .failure(let error):                    print(error)                }            }        }
```

```
        func listenForChanges() {            pusher = Pusher(key: "PUSHER_KEY", options: PusherClientOptions(                host: .cluster("PUSHER_CLUSTER")            ))
```

```
            let channel = pusher.subscribe("collabo")            let _ = channel.bind(eventName: "text_update", callback: { (data: Any?) -> Void in
```

```
                if let data = data as? [String: AnyObject] {                    let fromDeviceId = data["deviceId"] as! String
```

```
                    if fromDeviceId != self.randomUuid {                        let text = data["text"] as! String                        self.textView.text = text                        self.charactersLabel.text = String(format: "%i Characters", text.characters.count)                    }                }            })
```

```
            pusher.connect()        }    }
```

Super ! Maintenant, nous devons créer le backend de l'application.

### Construire l'application backend Node

Maintenant que nous avons terminé la partie Swift, nous pouvons nous concentrer sur la création du backend Node.js pour l'application. Nous allons utiliser Express afin de pouvoir rapidement obtenir quelque chose de fonctionnel.

Créez un répertoire pour l'application web, puis créez quelques nouveaux fichiers.

Le fichier **index.js** :

```
let path = require('path');    let Pusher = require('pusher');    let express = require('express');    let bodyParser = require('body-parser');    let app = express();    let pusher = new Pusher(require('./config.js'));
```

```
    app.use(bodyParser.json());    app.use(bodyParser.urlencoded({ extended: false }));
```

```
    app.post('/update_text', function(req, res){      var payload = {text: req.body.text, deviceId: req.body.from}      pusher.trigger('collabo', 'text_update', payload)      res.json({success: 200})    });
```

```
    app.use(function(req, res, next) {        var err = new Error('Not Found');        err.status = 404;        next(err);    });
```

```
    module.exports = app;
```

```
    app.listen(4000, function(){      console.log('App listening on port 4000!');    });
```

Dans le fichier JS ci-dessus, nous utilisons Express pour créer une application simple. Dans la route `/update_text`, nous recevons simplement la charge utile et la transmettons à Pusher. Rien de compliqué là-dedans.

Créez également un fichier **package.json** :

```
{      "main": "index.js",      "dependencies": {        "body-parser": "^1.17.2",        "express": "^4.15.3",        "path": "^0.12.7",        "pusher": "^1.5.1"      }    }
```

Le fichier **package.json** est l'endroit où nous définissons toutes les dépendances NPM.

Le dernier fichier à créer est un fichier **config.js**. C'est ici que nous allons définir les valeurs de configuration pour notre application Pusher :

```
module.exports = {      appId: 'PUSHER_ID',      key: 'PUSHER_KEY',      secret: 'PUSHER_SECRET',      cluster: 'PUSHER_CLUSTER',      encrypted: true    };
```

> _? R**emember to replace the key and cluster with the actual value you have gotten from your Pusher dashboard.**_

Exécutez maintenant `npm install` dans le répertoire, puis `node index.js` une fois l'installation de npm terminée. Vous devriez voir un message _App listening on port 4000!_.

![Image](https://cdn-media-1.freecodecamp.org/images/TGJKpixfoUkwEIal-2tDPo25Rb7Bo8BuEWMa)

### Tester l'application

Une fois que vous avez votre serveur web local node en cours d'exécution, vous devrez apporter quelques modifications pour que votre application puisse communiquer avec le serveur web local. Dans le fichier `info.plist`, apportez les modifications suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/FARWGcIZQDh0lMGVsdWlhAmDwm1FIon921ch)

Avec cette modification, vous pouvez construire et exécuter votre application et elle communiquera directement avec votre application web locale.

### Conclusion

Dans cet article, nous avons couvert comment créer un éditeur de texte collaboratif en temps réel sur iOS en utilisant Pusher. Espérons que vous avez appris une ou deux choses en suivant ce tutoriel. Pour vous entraîner, vous pouvez étendre les statuts pour supporter plus d'instances.

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/collaborative-text-editor-swift/).