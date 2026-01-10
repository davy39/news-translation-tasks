---
title: Comment créer une application de chat iOS avec SlackTextViewController
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T17:31:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ios-chat-app-with-slacktextviewcontroller-e3d3291a46a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mMawypMnD9wpQ0wPEnls-A.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment créer une application de chat iOS avec SlackTextViewController
seo_desc: 'By Neo Ighodaro

  Nowadays, many applications offer in-app chat and messenger features to their users.
  The in-app messenger can be useful for things like live support chatting or in-app
  messaging with other application users.

  In this article, we are go...'
---

Par Neo Ighodaro

De nos jours, de nombreuses applications offrent des fonctionnalités de chat et de messagerie intégrées à leurs utilisateurs. Le messager intégré peut être utile pour des choses comme le chat de support en direct ou la messagerie intégrée avec d'autres utilisateurs de l'application.

Dans cet article, nous allons explorer comment utiliser [Pusher Chatkit](https://pusher.com/chatkit) (qui est en bêta au moment de la rédaction de cet article) et `SlackTextViewController` pour créer une application de chat.

💡 `SlackTextViewController` est un sous-classe de UIViewController prêt à l'emploi avec une vue de saisie de texte extensible et d'autres fonctionnalités de messagerie utiles. Il est destiné à être un remplacement pour UITableViewController et UICollectionViewController.

Une compréhension de base de Swift et Node.js est nécessaire pour suivre ce tutoriel.

Voici un enregistrement d'écran de notre application en action :

![Image](https://cdn-media-1.freecodecamp.org/images/tuuFe65YZjnOYX03SCCEcyEQWWef7DVWZmxh)

### Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* [Xcode 7](https://developer.apple.com/xcode/) ou une version ultérieure.
* Connaissance de Swift et de l'interface builder de Xcode.
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installé sur votre machine.
* [Node.js et NPM](https://docs.npmjs.com/getting-started/installing-node) installés sur votre machine.
* Connaissance de base de JavaScript (Node.js et Express).
* Une application Pusher Chatkit. Créez-en une [ici](https://pusher.com/chatkit).

En supposant que vous avez tous les prérequis, commençons.

### Création de notre application Chatkit

Allez sur la page Chatkit, créez un compte et créez une application Chatkit depuis le tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/oqZr8dokqzVohttVR8jQa-gsSEEs3nIMzwbP)

Suivez l'assistant "Getting Started" jusqu'à la fin pour vous aider à créer un nouveau compte utilisateur et une nouvelle salle de chat.

![Image](https://cdn-media-1.freecodecamp.org/images/oh9t0zylJ1ZhCNnHBUfPImyYXSLMO7wfp3kL)

Dans le même écran, après avoir terminé l'assistant "Get Started", cliquez sur "Keys" pour obtenir le **Instance Locator** et la **Key** de votre application. Vous aurez besoin de ces valeurs pour faire des requêtes à l'API Chatkit.

C'est tout ! Maintenant, créons un backend qui aidera notre application à communiquer avec l'API Chatkit.

### Création d'un backend Node.js pour Pusher Chatkit

Avant de créer notre application iOS, créons un backend Node.js pour l'application. L'application communiquera avec le backend pour faire des choses comme récupérer le token requis pour faire des requêtes.

Ouvrez votre terminal et créez un nouveau répertoire où l'application web résidera. Dans cette application web, nous définirons quelques routes qui contiendront la logique pour faire des requêtes à l'API Chatkit.

Exécutez la commande suivante pour créer le répertoire qui contiendra notre application web :

```bash
$ mkdir ChattrBackend
```

Créez un nouveau fichier `package.json` à la racine du répertoire et collez le contenu suivant :

```json
{
  "main": "index.js",
  "dependencies": {
    "body-parser": "^1.17.2",
    "express": "^4.15.3",
    "pusher-chatkit-server": "^0.5.0"
  }
}
```

Maintenant, ouvrez le terminal et exécutez la commande suivante pour commencer à installer les dépendances :

```bash
$ npm install
```

Lorsque l'installation est terminée, créez un nouveau fichier `index.js` et collez le contenu suivant :

```js
// Importation des bibliothèques
const express    = require('express');
const bodyParser = require('body-parser');
const app        = express();
const Chatkit    = require('pusher-chatkit-server');
const chatkit    = new Chatkit.default(require('./config.js'))

// Middlewares Express
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// --------------------------------------------------------
// Crée un nouvel utilisateur en utilisant l'API Chatkit
// --------------------------------------------------------
app.post('/users', (req, res) => {
  let username = req.body.username;
  chatkit.createUser(username, username)
    .then(r => res.json({username}))
    .catch(e => res.json({error: e.error_description, type: e.error_type}))
})

// --------------------------------------------------------
// Génère un token et le retourne
// --------------------------------------------------------
app.post('/auth', (req, res) => {
  let resp = chatkit.authenticate({grant_type: req.body.grant_type}, req.query.user_id)
  res.json(resp)
});

// --------------------------------------------------------
// Index
// --------------------------------------------------------
app.get('/', (req, res) => {
  res.json("Ça marche !");
});

// --------------------------------------------------------
// Gestion des erreurs 404
// --------------------------------------------------------
app.use((req, res, next) => {
  let err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// --------------------------------------------------------
// Lancement de l'application
// --------------------------------------------------------
app.listen(4000, function(){
  console.log('App listening on port 4000!')
});
```

Dans le code ci-dessus, nous avons une application Express exemple. L'application a deux routes principales. La route `/users` crée un nouvel utilisateur en utilisant l'API Chatkit. L'utilisateur créé peut ensuite demander un token en utilisant la route `/auth`. Les tokens sont utilisés pour valider l'identité d'un utilisateur faisant une requête à l'API Chatkit.

Enfin, créons un fichier `config.js` dans le même répertoire racine. C'est ici que nous définirons les clés Chatkit. Collez le contenu suivant dans le fichier :

```js
module.exports = {
  instanceLocator: "PUSHER_CHATKIT_INSTANCE_LOCATOR",
  key: "PUSHER_CHATKIT_KEY",
}
```

N'oubliez pas de remplacer `*PUSHER_CHATKIT_*``_INSTANCE_LOCATOR_` et `_PUSHER_CHATKIT_KEY_` par les valeurs réelles de votre application Chatkit. Vous pouvez trouver les valeurs dans la section "Keys" du tableau de bord Chatkit.

Maintenant, nous avons terminé la création de l'application Node.js. Exécutez la commande suivante pour démarrer l'application Node.js :

```bash
$ node index.js
```

> _💡 Vous pouvez vouloir garder la fenêtre de terminal ouverte et lancer une autre fenêtre de terminal pour garder le serveur Node.js en cours d'exécution._

### Création de notre application iOS

Lancez Xcode et créez un projet "Single View App".

![Image](https://cdn-media-1.freecodecamp.org/images/NGOKI9JYYUzLnPNJ6XnFCO6MRUuwReGnVVvz)

### Installation de nos packages Cocoapods

Lorsque vous avez créé l'application, fermez Xcode et lancez une nouvelle fenêtre de terminal. `cd` à la racine du répertoire de votre application mobile. Exécutez la commande suivante pour initialiser Cocoapods sur le projet :

```bash
$ pod init
```

Cela créera un nouveau `Podfile`. Dans ce fichier, nous pouvons définir nos dépendances Cocoapods. Ouvrez le fichier et collez ce qui suit :

```
platform :ios, '10.0'

target 'Chattr' do
  use_frameworks!
  
  pod 'PusherChatkit', '~> 0.4.0'
  pod 'Alamofire', '~> 4.5.1'
  pod 'SlackTextViewController', git: 'https://github.com/slackhq/SlackTextViewController.git', branch: 'master'
end
```

Maintenant, exécutez `pod install` pour installer les dépendances.

> _⚠️ `SlackTextViewController` a un bug dans iOS 11 où la vue de texte [ne répond pas aux clics](https://github.com/slackhq/SlackTextViewController/issues/604). Bien qu'il ait été corrigé dans la version `1.9.6`, cette version n'était pas disponible pour Cocoapods au moment de la rédaction de cet article, donc nous avons dû utiliser la branche master dans le Podfile._

Lorsque l'installation est terminée, ouvrez le nouveau fichier `.xcworkspace` qui a été généré par Cocoapods à la racine de votre projet. Cela lancera Xcode.

### Configuration de notre application iOS

Dans Xcode, ouvrez le fichier `AppDelegate.swift` et remplacez le contenu du fichier par le code suivant :

```swift
import UIKit

struct AppConstants {
    static let ENDPOINT    = "http://localhost:4000"
    static let INSTANCE_LOCATOR = "PUSHER_CHATKIT_INSTANCE_LOCATOR"
}

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        window?.backgroundColor = UIColor.white
        return true
    }
}
```

Dans la structure `AppConstants`, nous avons défini `ENDPOINT` et `INSTANCE_LOCATOR`. L'`ENDPOINT` est l'URL du serveur web distant où réside votre application Node.js. L'`INSTANCE_LOCATOR` contient le localisateur d'instance fourni pour votre application Chatkit dans le tableau de bord Pusher Chatkit.

Maintenant, concentrons-nous sur la création du storyboard et des autres parties.

### Création du storyboard et des contrôleurs de notre application

Ouvrez le fichier `Main.storyboard` et, dans celui-ci, nous allons créer l'interface de l'application. Nous aurons quatre scènes sur notre storyboard. Elles ressembleront à quelque chose comme la capture d'écran ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/wg6UnEs7hsLjvkyl2yB5278LoxlBDyeeIq2v)

Dans la première scène du View Controller, créons un `LoginViewController` et relions-le à la scène du View Controller dans le storyboard. Créez le nouveau View Controller et collez le code suivant :

```swift
import UIKit
import Alamofire

class LoginViewController: UIViewController {
    var username: String!
    @IBOutlet weak var loginButton: UIButton!
    @IBOutlet weak var textField: UITextField!
}

extension LoginViewController {
    // MARK: Initialisation
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.loginButton.isEnabled = false
        
        self.loginButton.addTarget(self, action: #selector(loginButtonPressed), for: .touchUpInside)
        self.textField.addTarget(self, action: #selector(typingUsername), for: .editingChanged)
    }
    
    // MARK: Navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) -> Void {
        if segue.identifier == "loginSegue" {
            let ctrl = segue.destination as! UINavigationController
            let actualCtrl = ctrl.viewControllers.first as! RoomListTableViewController
            actualCtrl.username = self.username
        }
    }
    
    // MARK: Aides
    @objc func typingUsername(_ sender: UITextField) {
        self.loginButton.isEnabled = sender.text!.characters.count >= 3
    }
    
    @objc func loginButtonPressed(_ sender: Any) {
        let payload: Parameters = ["username": self.textField.text!]
        
        self.loginButton.isEnabled = false
        
        Alamofire.request(AppConstants.ENDPOINT + "/users", method: .post, parameters: payload).validate().responseJSON { (response) in
            switch response.result {
            case .success(_):
                self.username = self.textField.text!
                self.performSegue(withIdentifier: "loginSegue", sender: self)
            case .failure(let error):
                print(error)
            }
        }
    }
}
```

Dans le code ci-dessus, nous avons défini deux `@IBOutlet`s que nous allons connecter à la scène du View Controller dans le storyboard. Dans la méthode `prepare`, nous préparons la navigation vers le `RoomListTableViewController` en définissant la propriété `username` dans cette classe. Dans le gestionnaire `loginButtonPressed`, nous envoyons une requête à l'application Node.js que nous avons créée précédemment pour créer le nouvel utilisateur.

Ouvrez le storyboard et liez la première scène à la classe `LoginViewController`. Ajoutez un `UIButton` et un `UITextField` à la scène du contrôleur de vue. Maintenant, connectez le `UITextField` à la propriété `textField` en tant que sortie de référence. Connectez également le `UIButton` à la propriété `loginButton` en tant que sortie de référence.

Ensuite, ajoutez un Navigation Controller au storyboard. Créez un segue manuel entre le View Controller et le Navigation Controller et définissez l'ID de ce segue sur `loginSegue`.

![Image](https://cdn-media-1.freecodecamp.org/images/9GKGHuu5Z28crbh1KiLYVZ4LZfwGvTzan0b7)

Ensuite, créez un nouveau contrôleur appelé `RoomListTableViewController`. Dans le fichier `Main.storyboard`, définissez cette nouvelle classe comme la classe personnalisée pour le TableViewController attaché au Navigation Controller. Maintenant, dans la classe `RoomListTableViewController`, remplacez le contenu par le code suivant :

```swift
import UIKit
import PusherChatkit

class RoomListTableViewController: UITableViewController {
    var username: String!
    var selectedRoom: PCRoom?
    var currentUser: PCCurrentUser!
    var availableRooms = [PCRoom]()
    var activityIndicator = UIActivityIndicatorView()
}

// MARK: - Initialisation -
extension RoomListTableViewController: PCChatManagerDelegate {
    override func viewDidLoad() -> Void {
        super.viewDidLoad()
        self.setNavigationItemTitle()
        self.initActivityIndicator()
        self.initPusherChatkit()
    }
    
    private func setNavigationItemTitle() -> Void {
        self.navigationItem.title = "Salons"
    }
    
    private func initActivityIndicator() -> Void {
        self.activityIndicator = UIActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
        self.activityIndicator.activityIndicatorViewStyle = UIActivityIndicatorViewStyle.gray
        self.activityIndicator.center = self.view.center
        self.view.addSubview(self.activityIndicator)
        self.activityIndicator.startAnimating()
    }
    
    private func initPusherChatkit() -> Void {
        self.initPusherChatManager { [weak self] (currentUser) in
            guard let strongSelf = self else { return }
            strongSelf.currentUser = currentUser
            strongSelf.activityIndicator.stopAnimating()
            strongSelf.tableView.reloadData()
        }
    }
    
    private func initPusherChatManager(completion: @escaping (_ success: PCCurrentUser) -> Void) -> Void {        
        let chatManager = ChatManager(
            instanceId: AppConstants.INSTANCE_LOCATOR,
            tokenProvider: PCTokenProvider(url: AppConstants.ENDPOINT + "/auth", userId: username)
        )
        chatManager.connect(delegate: self) { (user, error) in
            guard error == nil else { return }
            guard let user = user else { return }
            // Obtenir une liste de toutes les salles. Tentative de rejoindre la salle.
            user.getAllRooms { rooms, error in
                guard error == nil else { return }
                self.availableRooms = rooms!
                rooms!.forEach { room in
                    user.joinRoom(room) { room, error in
                        guard error == nil else { return }
                    }
                }
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            }
            DispatchQueue.main.async {
                completion(user)
            }
        }
    }
}

// MARK: - Surcharges de UITableViewController -
extension RoomListTableViewController {
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.availableRooms.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let roomTitle = self.availableRooms[indexPath.row].name
        let cell = tableView.dequeueReusableCell(withIdentifier: "RoomCell", for: indexPath)
        cell.textLabel?.text = "\(roomTitle)"
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.selectedRoom = self.availableRooms[indexPath.row]
        self.performSegue(withIdentifier: "segueToRoomViewController", sender: self)
    }
}

// MARK: - Navigation -
extension RoomListTableViewController {
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) -> Void {
        if segue.identifier == "segueToRoomViewController" {
            let roomViewController = segue.destination as! RoomViewController
            roomViewController.room = self.selectedRoom
            roomViewController.currentUser = self.currentUser
        }
    }
}
```

Cette classe est destinée à montrer toutes les salles de chat disponibles auxquelles les utilisateurs peuvent se connecter et discuter. Voyons ce que font certaines parties de la classe.

La première extension contient les initialisateurs. Dans la méthode `viewDidLoad`, nous définissons le titre du contrôleur, l'indicateur d'activité et Pusher Chatkit.

Dans `initPusherChatManager`, nous initialisons un `tokenProvider` qui récupère un token depuis notre endpoint Node.js. Nous créons ensuite un `chatManager` avec le localisateur d'instance de notre application Chatkit et le `tokenProvider`, et nous nous connectons à Chatkit.

Dans la deuxième extension, nous surchargeons certaines méthodes du contrôleur de table view. Nous faisons cela pour pouvoir afficher les noms des canaux dans les lignes. Dans la dernière méthode de la deuxième extension à la ligne `100`, nous appelons la méthode `performSegue(withIdentifier: "segueToRoomViewController", sender: self)` qui naviguera vers la page d'un nouveau View Controller.

La dernière extension contient la méthode `prepare`. Cela prépare le View Controller vers lequel nous naviguons avant d'y arriver. Maintenant, créons le View Controller et le segue nécessaires pour y accéder.

Pour notre dernière scène de storyboard, créez une classe `RoomViewController`. Dans le fichier `Main.storyboard`, faites glisser un View Controller final sur le tableau.

Définissez la classe personnalisée du nouveau contrôleur de vue sur `RoomViewController`. Créez également un segue manuel depuis le contrôleur de table view vers celui-ci et nommez le segue `segueToRoomViewController` :

![Image](https://cdn-media-1.freecodecamp.org/images/eR6lukLiKrke4ZOFwzenwJzG2nBMm8dENZmj)

Ouvrez la classe `RoomViewController` et remplacez le contenu par ce qui suit :

```swift
import UIKit
import PusherChatkit
import SlackTextViewController

class RoomViewController: SLKTextViewController, PCRoomDelegate {
    var room: PCRoom!
    var messages = [Message]()
    var currentUser: PCCurrentUser!
    override var tableView: UITableView {
        get { return super.tableView! }
    }
}

// MARK: - Initialisation -
extension RoomViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        self.subscribeToRoom()
        self.setNavigationItemTitle()
        self.configureSlackTableViewController()
    }
    
    private func subscribeToRoom() -> Void {
        self.currentUser.subscribeToRoom(room: self.room, roomDelegate: self)
    }
    
    private func setNavigationItemTitle() -> Void {
        self.navigationItem.title = self.room.name
    }
    
    private func configureSlackTableViewController() -> Void {
        self.bounces = true
        self.isInverted = true
        self.shakeToClearEnabled = true
        self.isKeyboardPanningEnabled = true
        self.textInputbar.maxCharCount = 256
        self.tableView.separatorStyle = .none
        self.textInputbar.counterStyle = .split
        self.textInputbar.counterPosition = .top
        self.textInputbar.autoHideRightButton = true
        self.textView.placeholder = "Entrez un message...";
        self.shouldScrollToBottomAfterKeyboardShows = false
        self.textInputbar.editorTitle.textColor = UIColor.darkGray
        self.textInputbar.editorRightButton.tintColor = UIColor(red: 0/255, green: 122/255, blue: 255/255, alpha: 1)
        self.tableView.register(MessageCell.classForCoder(), forCellReuseIdentifier: MessageCell.MessengerCellIdentifier)
        self.autoCompletionView.register(MessageCell.classForCoder(), forCellReuseIdentifier: MessageCell.AutoCompletionCellIdentifier)
    }
}

// MARK: - Surcharges de UITableViewController -
extension RoomViewController {
    override class func tableViewStyle(for decoder: NSCoder) -> UITableViewStyle {
        return .plain
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if tableView == self.tableView {
            return self.messages.count
        }
        return 0
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return self.messageCellForRowAtIndexPath(indexPath)
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        if tableView == self.tableView {
            let message = self.messages[(indexPath as NSIndexPath).row]
            if message.text.characters.count == 0 {
                return 0
            }
            let paragraphStyle = NSMutableParagraphStyle()
            paragraphStyle.lineBreakMode = .byWordWrapping
            paragraphStyle.alignment = .left
            let pointSize = MessageCell.defaultFontSize()
            let attributes = [
                NSAttributedStringKey.font: UIFont.systemFont(ofSize: pointSize),
                NSAttributedStringKey.paragraphStyle: paragraphStyle
            ]
            var width = tableView.frame.width - MessageCell.kMessageTableViewCellAvatarHeight
            width -= 25.0
            let titleBounds = (message.username as NSString!).boundingRect(
                with: CGSize(width: width, height: CGFloat.greatestFiniteMagnitude),
                options: .usesLineFragmentOrigin,
                attributes: attributes,
                context: nil
            )
            let bodyBounds = (message.text as NSString!).boundingRect(
                with: CGSize(width: width, height: CGFloat.greatestFiniteMagnitude),
                options: .usesLineFragmentOrigin,
                attributes: attributes,
                context: nil
            )
            var height = titleBounds.height
            height += bodyBounds.height
            height += 40
            if height < MessageCell.kMessageTableViewCellMinimumHeight {
                height = MessageCell.kMessageTableViewCellMinimumHeight
            }
            return height
        }
        return MessageCell.kMessageTableViewCellMinimumHeight
    }
}

// MARK: - Surcharges -
extension RoomViewController {
    override func keyForTextCaching() -> String? {
        return Bundle.main.bundleIdentifier
    }
    
    override func didPressRightButton(_ sender: Any!) {
        self.textView.refreshFirstResponder()
        self.sendMessage(textView.text)
        super.didPressRightButton(sender)
    }
}

// MARK: - Méthodes de délégué -
extension RoomViewController {
    public func newMessage(message: PCMessage) {
        let msg = self.PCMessageToMessage(message)
        let indexPath = IndexPath(row: 0, section: 0)
        let rowAnimation: UITableViewRowAnimation = self.isInverted ? .bottom : .top
        let scrollPosition: UITableViewScrollPosition = self.isInverted ? .bottom : .top
        DispatchQueue.main.async {
            self.tableView.beginUpdates()
            self.messages.insert(msg, at: 0)
            self.tableView.insertRows(at: [indexPath], with: rowAnimation)
            self.tableView.endUpdates()
            self.tableView.scrollToRow(at: indexPath, at: scrollPosition, animated: true)
            self.tableView.reloadRows(at: [indexPath], with: .automatic)
            self.tableView.reloadData()
        }
    }
}

// MARK: - Aides -
extension RoomViewController {
    private func PCMessageToMessage(_ message: PCMessage) -> Message {
        return Message(id: message.id, username: message.sender.displayName, text: message.text)
    }
    
    private func sendMessage(_ message: String) -> Void {
        guard let room = self.room else { return }
        self.currentUser?.addMessage(text: message, to: room, completionHandler: { (messsage, error) in
            guard error == nil else { return }
        })
    }
    
    private func messageCellForRowAtIndexPath(_ indexPath: IndexPath) -> MessageCell {
        let cell = self.tableView.dequeueReusableCell(withIdentifier: MessageCell.MessengerCellIdentifier) as! MessageCell
        let message = self.messages[(indexPath as NSIndexPath).row]
        cell.bodyLabel().text = message.text
        cell.titleLabel().text = message.username
        cell.usedForMessage = true
        cell.indexPath = indexPath
        cell.transform = self.tableView.transform
        return cell
    } 
}
```

La classe ci-dessus étend `SlackTableViewController` qui lui donne automatiquement accès à certaines fonctionnalités intéressantes de ce contrôleur. Dans le code ci-dessus, nous avons divisé la classe en 5 extensions. Prenons chaque extension et expliquons un peu ce qui s'y passe.

Dans la première extension, nous nous abonnons à la salle, définissons le nom de la salle comme titre de la page et configurons le `SlackTableViewController`. Dans la méthode `configureSlackTableViewController`, nous personnalisons simplement des parties de notre `SlackTableViewController`.

Dans la deuxième extension, nous surchargeons les méthodes du contrôleur de table view. Nous définissons également le nombre de sections, le nombre de lignes et définissons le `Message` à afficher sur chaque ligne. Et enfin, nous calculons également la hauteur dynamique de chaque cellule, en fonction des caractères du message.

Dans la troisième extension, nous avons la fonction `didPressRightButton` qui est appelée chaque fois que l'utilisateur appuie sur envoyer pour envoyer un message.

Dans la quatrième extension, nous avons les fonctions disponibles depuis le `PCRoomDelegate`. Dans la fonction `newMessage`, nous envoyons le message à Chatkit puis nous rechargeons la table pour afficher les nouvelles données ajoutées.

Dans la cinquième et dernière extension, nous définissons des fonctions qui sont destinées à être des aides. La méthode `PCMessageToMessage` convertit un `PCMessage` en notre propre structure `Message` (nous la définirons plus tard). La méthode `sendMessage` envoie le message à l'API Chatkit. Enfin, nous avons la méthode `messageCellForRowAtIndexPath`. Cette méthode récupère simplement le message attaché à une ligne particulière en utilisant l'`indexPath`.

Maintenant, créez une nouvelle classe appelée `MessageCell`. Ce sera la classe de vue où nous personnaliserons tout ce qui concerne l'apparence d'une seule cellule de chat. Dans le fichier, remplacez le contenu par celui ci-dessous :

```swift
import UIKit
import SlackTextViewController

struct Message {
    var id: Int!
    var username: String!
    var text: String!
}

class MessageCell: UITableViewCell {
    static let kMessageTableViewCellMinimumHeight: CGFloat = 50.0;
    static let kMessageTableViewCellAvatarHeight: CGFloat = 30.0;
    static let MessengerCellIdentifier: String = "MessengerCell";
    static let AutoCompletionCellIdentifier: String = "AutoCompletionCell";
    var _titleLabel: UILabel?
    var _bodyLabel: UILabel?
    var _thumbnailView: UIImageView?
    var indexPath: IndexPath?
    var usedForMessage: Bool?
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        self.selectionStyle = .none
        self.backgroundColor = UIColor.white
        configureSubviews()
    }
    
    func configureSubviews() {
        contentView.addSubview(thumbnailView())
        contentView.addSubview(titleLabel())
        contentView.addSubview(bodyLabel())
        let views: [String:Any] = [
            "thumbnailView": thumbnailView(),
            "titleLabel": titleLabel(),
            "bodyLabel": bodyLabel()
        ]
        
        let metrics = [
            "tumbSize": MessageCell.kMessageTableViewCellAvatarHeight,
            "padding": 15,
            "right": 10,
            "left": 5
        ]
        contentView.addConstraints(NSLayoutConstraint.constraints(
            withVisualFormat: "H:|-left-[thumbnailView(tumbSize)]-right-[titleLabel(>=0)]-right-|",
            options: [],
            metrics: metrics,
            views: views
        ))
        contentView.addConstraints(NSLayoutConstraint.constraints(
            withVisualFormat: "H:|-left-[thumbnailView(tumbSize)]-right-[bodyLabel(>=0)]-right-|",
            options: [],
            metrics: metrics,
            views: views
        ))
        contentView.addConstraints(NSLayoutConstraint.constraints(
            withVisualFormat: "V:|-right-[thumbnailView(tumbSize)]-(>=0)-|",
            options: [],
            metrics: metrics,
            views: views
        ))
        if (reuseIdentifier == MessageCell.MessengerCellIdentifier) {
            contentView.addConstraints(NSLayoutConstraint.constraints(
                withVisualFormat: "V:|-right-[titleLabel(20)]-left-[bodyLabel(>=0@999)]-left-|",
                options: [],
                metrics: metrics,
                views: views
            ))
        }
        else {
            contentView.addConstraints(NSLayoutConstraint.constraints(
                withVisualFormat: "V:|[titleLabel]|",
                options: [],
                metrics: metrics,
                views: views
            ))
        }
    }
    
    // MARK: Getters
    override func prepareForReuse() {
        super.prepareForReuse()
        selectionStyle = .none
        let pointSize: CGFloat = MessageCell.defaultFontSize()
        titleLabel().font = UIFont.boldSystemFont(ofSize: pointSize)
        bodyLabel().font = UIFont.systemFont(ofSize: pointSize)
        titleLabel().text = ""
        bodyLabel().text = ""
    }
    
    func titleLabel() -> UILabel {
        if _titleLabel == nil {
            _titleLabel = UILabel()
            _titleLabel?.translatesAutoresizingMaskIntoConstraints = false
            _titleLabel?.backgroundColor = UIColor.clear
            _titleLabel?.isUserInteractionEnabled = false
            _titleLabel?.numberOfLines = 0
            _titleLabel?.textColor = UIColor.gray
            _titleLabel?.font = UIFont.boldSystemFont(ofSize: MessageCell.defaultFontSize())
        }
        return _titleLabel!
    }
    
    func bodyLabel() -> UILabel {
        if _bodyLabel == nil {
            _bodyLabel = UILabel()
            _bodyLabel?.translatesAutoresizingMaskIntoConstraints = false
            _bodyLabel?.backgroundColor = UIColor.clear
            _bodyLabel?.isUserInteractionEnabled = false
            _bodyLabel?.numberOfLines = 0
            _bodyLabel?.textColor = UIColor.darkGray
            _bodyLabel?.font = UIFont.systemFont(ofSize: MessageCell.defaultFontSize())
        }
        return _bodyLabel!
    }
    
    func thumbnailView() -> UIImageView {
        if _thumbnailView == nil {
            _thumbnailView = UIImageView()
            _thumbnailView?.translatesAutoresizingMaskIntoConstraints = false
            _thumbnailView?.isUserInteractionEnabled = false
            _thumbnailView?.backgroundColor = UIColor(white: 0.9, alpha: 1.0)
            _thumbnailView?.layer.cornerRadius = MessageCell.kMessageTableViewCellAvatarHeight / 2.0
            _thumbnailView?.layer.masksToBounds = true
        }
        return _thumbnailView!
    }
    
    class func defaultFontSize() -> CGFloat {
        var pointSize: CGFloat = 16.0
        let contentSizeCategory: String = String(describing: UIApplication.shared.preferredContentSizeCategory)
        pointSize += SLKPointSizeDifferenceForCategory(contentSizeCategory)
        return pointSize
    }
}
```

Dans le code ci-dessus, nous créons une classe qui étend `UITableViewCell`. Cette classe va être utilisée par `SlackTextViewController` comme la classe pour chaque ligne de message. Elle a été enregistrée dans le `RoomsViewController` lors de la configuration du `SlackTextViewController`.

### Test de notre application Pusher Chatkit

Pour instruire votre application iOS de se connecter à votre serveur Node.js local, vous devrez apporter quelques modifications. Dans le fichier `info.plist`, ajoutez les clés comme indiqué ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qAMemv7zym0pkVKfCpIHasRrbriKfLfd-nk2)

Avec cette modification, vous pouvez construire et exécuter votre application et elle communiquera directement avec votre application web locale. Maintenant, vous pouvez exécuter votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/UXT6rND2AbsLzLU2cekBI9WuOAgfBmmBlmF6)

### Conclusion

Dans ce tutoriel, nous avons pu créer une application de chat simple en utilisant `SlackTextViewController` et la puissance du SDK Pusher Chatkit. Espérons que vous avez appris une ou deux choses sur la façon dont vous pouvez intégrer Pusher Chatkit dans les technologies existantes et comment il peut alimenter la messagerie dans votre application.

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/ios-chat-slacktextviewcontroller/).