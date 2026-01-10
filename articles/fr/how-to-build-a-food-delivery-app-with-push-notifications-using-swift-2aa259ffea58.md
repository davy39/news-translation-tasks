---
title: Comment créer une application de livraison de nourriture avec des notifications
  push en utilisant Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-04T15:55:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-food-delivery-app-with-push-notifications-using-swift-2aa259ffea58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VNPU-C62GXtPW31p0XjkYg.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une application de livraison de nourriture avec des notifications
  push en utilisant Swift
seo_desc: 'By Neo Ighodaro

  A basic understanding of Swift and Node.js is needed to follow this tutorial.

  Last mile delivery marketplaces make it easy to order food from a mobile device
  and have it delivered to a user’s door while it’s still hot.

  Marketplaces li...'
---

Par Neo Ighodaro

Une compréhension de base de Swift et Node.js est nécessaire pour suivre ce tutoriel.

Les places de marché de livraison du dernier kilomètre permettent de commander de la nourriture depuis un appareil mobile et de la faire livrer à la porte de l'utilisateur tant qu'elle est encore chaude.

Des places de marché comme Deliveroo, Postmates ou Uber Eats utilisent la localisation de votre appareil pour vous servir une liste de restaurants qui sont suffisamment proches de vous (et ouverts) afin que vous puissiez obtenir votre livraison dès que possible.

Cette expérience en temps réel entre le client, le restaurant et le livreur repose sur des notifications push transactionnelles pour faire passer la commande de la cuisine à la table de manière transparente. Les clients veulent des notifications push pour les alerter lorsque leur commande est en route et lorsqu'ils doivent rencontrer le livreur à la porte.

La configuration des notifications push peut être confuse et prendre du temps. Cependant, avec l'API [Push Notifications](https://pusher.com/push-notifications) de Pusher, le processus est beaucoup plus facile et rapide.

Dans cet article, nous allons examiner comment vous pouvez créer des applications sur iOS qui ont des notifications push transactionnelles. Pour cela, nous allons créer une application fictive de livraison de nourriture.

### Prérequis

* Un Mac avec Xcode installé. [Téléchargez Xcode ici](https://developer.apple.com/xcode/).
* Connaissance de l'utilisation de Xcode.
* Connaissance de [Swift](https://developer.apple.com/swift/).
* Un compte Pusher. [Créez-en un ici](https://dash.pusher.com/authenticate/register?ref=pn-food-delivery-ios).
* Connaissance de base de JavaScript/Node.js ([Consultez ce tutoriel](https://www.w3schools.com/nodejs/default.asp)).
* Cocoapods [installé sur votre machine](https://guides.cocoapods.org/using/getting-started.html).

Une fois que vous avez les exigences, commençons.

### Construction de notre application — planification

Avant de commencer à construire notre application, nous devons faire un peu de planification sur la façon dont nous voulons que l'application fonctionne.

Nous allons créer trois applications :

* L'application backend (Web utilisant Node.js).
* L'application client (iOS utilisant Swift).
* L'application admin (iOS utilisant Swift).

#### L'application backend

Ce sera l'API. Pour simplifier, nous n'ajouterons aucune sorte d'authentification à l'API. Nous appellerons l'API depuis nos applications iOS. L'API doit être capable de fournir l'inventaire de nourriture, les commandes, et aussi gérer les commandes. Nous enverrons également des notifications push depuis l'application backend.

#### L'application client

Ce sera l'application qui sera avec le client. C'est là que l'utilisateur pourra commander de la nourriture. Pour simplifier, nous n'aurons aucune sorte d'authentification, et tout sera direct. Un client doit être capable de voir l'inventaire et de commander une ou plusieurs choses depuis cet inventaire. Ils doivent également être capables de voir la liste de leurs commandes et le statut de chaque commande.

![Image](https://cdn-media-1.freecodecamp.org/images/3krQt-kt9jm5O04uxE3DA-F6igGoVOfOGQvc)

#### L'application admin

Ce sera l'application que l'entreprise fournissant le service utilisera pour remplir les commandes. L'application affichera les commandes disponibles, et l'admin pourra définir le statut pour chaque commande.

![Image](https://cdn-media-1.freecodecamp.org/images/M-AivxSQOePKppLEk5EeIY34mhwRY2tfsB4P)

### Construction de l'application backend (API)

La première chose que nous voulons construire est l'API. Nous allons ajouter tout ce qui est nécessaire pour supporter nos applications iOS, puis nous ajouterons les notifications push plus tard.

Pour commencer, créez un répertoire de projet pour l'API. Dans le répertoire, créez un nouveau fichier appelé `package.json`. Dans le fichier, collez ce qui suit :

```json
{
  "main": "index.js",
  "scripts": {},
  "dependencies": {
    "body-parser": "^1.18.2",
    "express": "^4.16.2"
  }
}
```

Ensuite, exécutez la commande suivante dans votre terminal :

```bash
$ npm install
```

Cela installera toutes les dépendances listées. Ensuite, créez un fichier `index.js` dans le même répertoire que le fichier `package.json` et collez le code suivant :

```js
// --------------------------------------------------------
// Pull in the libraries
// --------------------------------------------------------

const app = require('express')()
const bodyParser = require('body-parser')

// --------------------------------------------------------
// Helpers
// --------------------------------------------------------

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}


// --------------------------------------------------------
// In-memory database
// --------------------------------------------------------

var user_id = null

var orders = []

let inventory = [
    {
        id: uuidv4(),
        name: "Pizza Margherita",
        description: "Comprend des tomates, de la mozzarella en tranches, du basilic et de l'huile d'olive extra vierge.",
        amount: 39.99,
        image: 'pizza1'
    },
    {
        id: uuidv4(),
        name: "Frites au fromage et bacon",
        description: "Comprend des tomates, du bacon, du fromage, du basilic et de l'huile",
        amount: 29.99,
        image: 'pizza2'
    }
]


// --------------------------------------------------------
// Express Middlewares
// --------------------------------------------------------

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))


// --------------------------------------------------------
// Routes
// --------------------------------------------------------

app.get('/orders', (req, res) => res.json(orders))

app.post('/orders', (req, res) => {
    let id = uuidv4()
    user_id = req.body.user_id
    let pizza = inventory.find(item => item["id"] === req.body.pizza_id)

    if (!pizza) {
        return res.json({status: false})
    }

    orders.unshift({id, user_id, pizza, status: "Pending"})
    res.json({status: true})
})

app.put('/orders/:id', (req, res) => {
    let order = orders.find(order => order["id"] === req.params.id)

    if ( ! order) {
        return res.json({status: false})
    }

    orders[orders.indexOf(order)]["status"] = req.body.status

    return res.json({status: true})
})

app.get('/inventory', (req, res) => res.json(inventory))
app.get('/', (req, res) => res.json({status: "success"}))


// --------------------------------------------------------
// Serve application
// --------------------------------------------------------

app.listen(4000, _ => console.log('App listening on port 4000!'))
```

Le code ci-dessus est une application Express simple. Tout est auto-explicatif et comporte des commentaires pour vous guider.

Dans la première route, `/orders`, nous affichons la liste des commandes disponibles à partir du magasin de données en mémoire. Dans la deuxième route, `POST /orders`, nous ajoutons simplement une nouvelle commande à la liste des `orders`. Dans la troisième route, `PUT /orders/:id`, nous modifions simplement le statut d'une seule commande à partir de la liste des `orders`. Dans la quatrième route, `GET /inventory`, nous listons l'inventaire disponible à partir de la liste des `inventory` dans la base de données.

Nous avons terminé avec l'API pour l'instant, et nous y reviendrons lorsque nous devrons ajouter le code de notification push. Si vous souhaitez tester que l'API fonctionne, exécutez la commande suivante dans votre terminal :

```bash
$ node index.js
```

Cela démarrera un nouveau serveur Node écoutant sur le port **4000**.

### Construction de l'application client

La prochaine chose que nous devons faire est de construire l'application client dans Xcode. Pour commencer, lancez Xcode et créez un nouveau projet 'Single Application'. Nous nommerons notre projet **PizzaareaClient.**

Une fois le projet créé, quittez Xcode et créez un nouveau fichier appelé `Podfile` à la racine du projet Xcode que vous venez de créer. Dans le fichier, collez le code suivant :

```
platform :ios, '11.0'
target 'PizzareaClient' do
  use_frameworks!
  pod 'PusherSwift', '~> 5.1.1'
  pod 'Alamofire', '~> 4.6.0'
end
```

Dans le fichier ci-dessus, nous avons spécifié les dépendances dont le projet a besoin pour fonctionner. **N'oubliez pas de changer le** `target` **ci-dessus par le nom de votre projet.** Maintenant, dans votre terminal, exécutez la commande suivante pour installer les dépendances :

```bash
$ pod install
```

Après l'installation, ouvrez le fichier workspace Xcode qui a été généré par Cocoapods. Cela devrait relancer Xcode.

Lorsque Xcode a été relancé, ouvrez le fichier `Main.storyboard`. Dans celui-ci, nous allons créer le storyboard pour notre application client. Ci-dessous, une capture d'écran de la manière dont nous avons conçu notre storyboard :

![Image](https://cdn-media-1.freecodecamp.org/images/zJda6PSzrhuKuO0HJp6LGAskHp4Cq6ZOXeAh)

La première scène est le contrôleur de vue de navigation, qui a un contrôleur de vue de tableau comme contrôleur racine. Le contrôleur de navigation est le contrôleur initial qui est chargé lorsque l'application est lancée.

#### Création de la scène de liste de pizzas

La deuxième scène est le contrôleur de vue qui liste l'inventaire que nous avons disponible.

![Image](https://cdn-media-1.freecodecamp.org/images/ABGbx7OWNOls3lH9WUDhqPWLdvh8aKmSytUE)

Créez un nouveau fichier dans Xcode appelé `PizzaTableListViewController.swift`, faites-en la classe personnalisée pour la deuxième scène, et collez le code suivant :

```swift
import UIKit
import Alamofire

class PizzaListTableViewController: UITableViewController {
    var pizzas: [Pizza] = []
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.title = "Sélectionner une Pizza"
        fetchInventory { pizzas in
            guard pizzas != nil else { return }            
            self.pizzas = pizzas!
            self.tableView.reloadData()
        }
    }
    
    private func fetchInventory(completion: @escaping ([Pizza]?) -> Void) {
        Alamofire.request("http://127.0.0.1:4000/inventory", method: .get)
            .validate()
            .responseJSON { response in
                guard response.result.isSuccess else { return completion(nil) }
                guard let rawInventory = response.result.value as? [[String: Any]?] else { return completion(nil) }
                let inventory = rawInventory.flatMap { pizzaDict -> Pizza? in
                    var data = pizzaDict!
                    data["image"] = UIImage(named: pizzaDict!["image"] as! String)
                    return Pizza(data: data)
                }
                completion(inventory)
            }
    }
    
    @IBAction func ordersButtonPressed(_ sender: Any) {
        performSegue(withIdentifier: "orders", sender: nil)
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return pizzas.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Pizza", for: indexPath) as! PizzaTableViewCell
        cell.name.text = pizzas[indexPath.row].name
        cell.imageView?.image = pizzas[indexPath.row].image
        cell.amount.text = "$\(pizzas[indexPath.row].amount)"
        cell.miscellaneousText.text = pizzas[indexPath.row].description
        return cell
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100.0
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        performSegue(withIdentifier: "pizza", sender: self.pizzas[indexPath.row] as Pizza)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "pizza" {
            guard let vc = segue.destination as? PizzaViewController else { return }
            vc.pizza = sender as? Pizza
        }
    }    
}
```

Dans la méthode `viewDidLoad`, nous appelons la méthode `fetchInventory` qui utilise `Alamofire` pour récupérer l'inventaire depuis notre API backend. Ensuite, nous sauvegardons la réponse dans la propriété `orders` du contrôleur.

Le `ordersButtonPressed` est lié au bouton `Orders` de la scène. Cela présente simplement la scène avec la liste des commandes en utilisant un segue nommé `orders`.

Les méthodes `tableView*` implémentent les méthodes disponibles pour le protocole `UITableViewDelegate` et devraient vous être familières.

La méthode finale `prepare` envoie simplement la `pizza` au contrôleur de vue lors de la navigation. Mais cette `pizza` n'est envoyée que si le contrôleur de vue chargé est le `PizzaViewController`.

Avant de créer la troisième scène, créez une classe `PizzaTableViewCell.swift` et collez ce qui suit :

```swift
import UIKit

class PizzaTableViewCell: UITableViewCell {

    @IBOutlet weak var pizzaImageView: UIImageView!
    @IBOutlet weak var name: UILabel!
    @IBOutlet weak var miscellaneousText: UILabel!
    @IBOutlet weak var amount: UILabel!

    override func awakeFromNib() {
        super.awakeFromNib()
    }
}
```

> _⚠️ Assurez-vous que la classe personnalisée des cellules dans la deuxième scène est `PizzaTableViewCell`, et que l'identifiant réutilisable est `Pizza`._

#### Création de la scène de vue de pizza

La troisième scène de notre storyboard est la scène de vue de pizza. C'est là que l'inventaire sélectionné peut être visualisé.

![Image](https://cdn-media-1.freecodecamp.org/images/nCiNzgOrcEPUdlBSH550pNDCgV-azkegd0Gu)

Créez un fichier `PizzaViewController.swift`, faites-en la classe personnalisée pour la scène ci-dessus, et collez le code suivant :

```swift
import UIKit
import Alamofire

class PizzaViewController: UIViewController {

    var pizza: Pizza?
    
    @IBOutlet weak var amount: UILabel!
    @IBOutlet weak var pizzaDescription: UILabel!
    @IBOutlet weak var pizzaImageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.title = pizza!.name
        pizzaImageView.image = pizza!.image
        pizzaDescription.text = pizza!.description
        amount.text = "$\(String(describing: pizza!.amount))"
    }
    
    @IBAction func buyButtonPressed(_ sender: Any) {
        let parameters = [
            "pizza_id": pizza!.id,
            "user_id": AppMisc.USER_ID
        ]
        
        Alamofire.request("http://127.0.0.1:4000/orders", method: .post, parameters: parameters)
            .validate()
            .responseJSON { response in
                guard response.result.isSuccess else { return self.alertError() }
                
                guard let status = response.result.value as? [String: Bool],
                      let successful = status["status"] else { return self.alertError() }
                      
                successful ? self.alertSuccess() : self.alertError()
            }
    }
    
    private func alertError() {
        return self.alert(
            title: "Achat non réussi !",
            message: "Impossible de compléter l'achat, veuillez réessayer plus tard."
        )
    }
    
    private func alertSuccess() {
        return self.alert(
            title: "Achat réussi",
            message: "Vous avez commandé avec succès, votre commande sera confirmée bientôt."
        )
    }
    
    private func alert(title: String, message: String) {
        let alertCtrl = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alertCtrl.addAction(UIAlertAction(title: "Okay", style: .cancel) { action in
            self.navigationController?.popViewController(animated: true)
        })
        
        present(alertCtrl, animated: true, completion: nil)
    }
}
```

Dans le code ci-dessus, nous avons plusieurs `@IBOutlet` et un seul `@IBAction`. Vous devez lier les outlets et les actions au contrôleur depuis le storyboard.

Dans le `viewDidLoad`, nous définissons les outlets pour qu'ils affichent les valeurs correctes en utilisant la `pizza` envoyée depuis le contrôleur de vue précédent. La méthode `buyButtonPressed` utilise `Alamofire` pour passer une commande en envoyant une requête à l'API. Les méthodes restantes gèrent l'affichage de la réponse d'erreur ou de succès de l'API.

#### Création de la scène de liste des commandes

La scène suivante est la scène de liste des commandes. Dans cette scène, toutes les commandes sont listées afin que l'utilisateur puisse les voir ainsi que leur statut :

![Image](https://cdn-media-1.freecodecamp.org/images/3SbIJ7MTiFjyzdwHKcEr4mD2-fZO18YpcMPo)

Créez un fichier `OrderTableViewController.swift`, faites-en la classe personnalisée pour la scène ci-dessus, et collez le code suivant :

```swift
import UIKit
import Alamofire

class OrdersTableViewController: UITableViewController {
    var orders: [Order] = []
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.title = "Commandes"
        fetchOrders { orders in
            self.orders = orders!
            self.tableView.reloadData()
        }
    }
    
    private func fetchOrders(completion: @escaping([Order]?) -> Void) {
        Alamofire.request("http://127.0.0.1:4000/orders").validate().responseJSON { response in
            guard response.result.isSuccess else { return completion(nil) }
            guard let rawOrders = response.result.value as? [[String: Any]?] else { return completion(nil) }
            let orders = rawOrders.flatMap { ordersDict -> Order? in
                guard let orderId = ordersDict!["id"] as? String,
                      let orderStatus = ordersDict!["status"] as? String,
                      var pizza = ordersDict!["pizza"] as? [String: Any] else { return nil }
                pizza["image"] = UIImage(named: pizza["image"] as! String)
                return Order(
                    id: orderId,
                    pizza: Pizza(data: pizza),
                    status: OrderStatus(rawValue: orderStatus)!
                )
            }
            completion(orders)
        }
    }
    
    @IBAction func closeButtonPressed(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return orders.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "order", for: indexPath)
        let order = orders[indexPath.row]
        cell.textLabel?.text = order.pizza.name
        cell.imageView?.image = order.pizza.image
        cell.detailTextLabel?.text = "$\(order.pizza.amount) - \(order.status.rawValue)"
        return cell
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100.0
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        performSegue(withIdentifier: "order", sender: orders[indexPath.row] as Order)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "order" {
            guard let vc = segue.destination as? OrderViewController else { return }
            vc.order = sender as? Order
        }
    }
}
```

Le code ci-dessus est similaire au code dans le `PizzaTableViewController` ci-dessus. Cependant, au lieu de récupérer l'inventaire, il récupère les `orders`. Au lieu de passer la `pizza` dans la dernière méthode, il passe l'`order` au contrôleur suivant. Le contrôleur comprend également une méthode `closeButtonPressed` qui ferme simplement le contrôleur et revient à la scène de liste d'inventaire.

#### Création de la scène de statut de commande

La scène suivante est la scène de commande. Dans cette scène, nous pouvons voir le statut de la commande :

![Image](https://cdn-media-1.freecodecamp.org/images/oZoE1RCIhgL0Zn2sgFSvjGexgbfzB2aHA2Dm)

> _⚠️ La scène ci-dessus a une vue invisible juste au-dessus de l'étiquette de statut. Vous devez utiliser cette vue pour créer un `@IBOutlet` vers le contrôleur._

Créez un fichier `OrderViewController.swift`, faites-en la classe personnalisée pour la scène ci-dessus, et collez le code suivant :

```swift
import UIKit

class OrderViewController: UIViewController {
    var order: Order?
    @IBOutlet weak var status: UILabel!
    @IBOutlet weak var activityView: ActivityIndicator!
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.title = order?.pizza.name
        activityView.startLoading()
        switch order!.status {
        case .pending:
            status.text = "Traitement de la commande"
        case .accepted:
            status.text = "Préparation de la commande"
        case .dispatched:
            status.text = "La commande est en route !"
        case .delivered:
            status.text = "Commande livrée"
            activityView.strokeColor = UIColor.green
            activityView.completeLoading(success: true)
        }
    }
}
```

Dans le code ci-dessus, nous faisons tout le travail dans notre méthode `viewDidLoad`. Nous y avons la classe `ActivityIndicator`, que nous allons créer ensuite, référencée en tant qu'`@IBOutlet`.

### Création d'autres parties de l'application

Nous utilisons une bibliothèque tierce appelée `[ActivityIndicator](https://github.com/abdulKarim002/activityIndicator)`, mais comme le package n'est pas disponible via Cocoapods, nous avons opté pour le créer nous-mêmes et l'importer.

Créez un nouveau fichier dans Xcode appelé `ActivityIndicator` et collez [le code du dépôt ici](https://raw.githubusercontent.com/abdulKarim002/activityIndicator/master/libTest/activityIndicator.swift) dedans.

Ensuite, créez un nouveau fichier `Order.swift` et collez le code suivant :

```swift
import Foundation

struct Order {
    let id: String
    let pizza: Pizza
    var status: OrderStatus
}

enum OrderStatus: String {
    case pending = "Pending"
    case accepted = "Accepted"
    case dispatched = "Dispatched"
    case delivered = "Delivered"
}
```

Enfin, créez un fichier `Pizza.swift` et collez le code suivant :

```swift
import UIKit

struct Pizza {
    let id: String
    let name: String
    let description: String
    let amount: Float
    let image: UIImage
    init(data: [String: Any]) {
        self.id = data["id"] as! String
        self.name = data["name"] as! String
        self.amount = data["amount"] as! Float
        self.description = data["description"] as! String
        self.image = data["image"] as! UIImage
    }
}
```

C'est tout pour l'application client. Une dernière chose que nous devons faire, cependant, est de modifier le fichier `info.plist`. Nous devons ajouter une entrée au fichier `plist` pour permettre la connexion à notre serveur local :

![Image](https://cdn-media-1.freecodecamp.org/images/w1yAAzsiaZIydYlqEJugz0c7-4afGKj-pXIP)

Passons à l'application admin.

### Construction de l'application admin

Lancez une nouvelle instance de Xcode et créez un nouveau projet 'Single Application'. Nous nommerons notre projet **PizzaareaAdmin.**

Une fois le projet créé, quittez Xcode et créez un nouveau fichier appelé `Podfile` à la racine du projet Xcode que vous venez de créer. Dans le fichier, collez le code suivant :

```
platform :ios, '11.0'

target 'PizzareaAdmin' do
  use_frameworks!
  pod 'PusherSwift', '~> 5.1.1'
  pod 'Alamofire', '~> 4.6.0'
end
```

Dans le fichier ci-dessus, nous avons spécifié les dépendances dont le projet a besoin pour fonctionner. **N'oubliez pas de changer le** `**target**` **ci-dessus par le nom de votre projet.**

Maintenant, dans votre terminal, exécutez la commande suivante pour installer les dépendances :

```bash
$ pod install
```

Après l'installation, ouvrez le fichier workspace Xcode qui a été généré par Cocoapods. Cela devrait relancer Xcode.

Lorsque Xcode a été relancé, ouvrez le fichier `Main.storyboard`. Dans celui-ci, nous allons créer le storyboard pour notre application client. Ci-dessous, une capture d'écran de la manière dont nous avons conçu notre storyboard :

![Image](https://cdn-media-1.freecodecamp.org/images/5m2t8kieea7YqqAzbY1SRou74ze49cqnth7-)

Ci-dessus, nous avons un contrôleur de vue de navigation qui est le contrôleur de vue initial.

#### Création de la scène de liste des commandes

La scène de liste des commandes est censée montrer la liste des commandes des clients. À partir de là, nous pouvons changer le statut de chaque commande lorsque nous le souhaitons.

Créez un nouveau fichier dans Xcode appelé `OrdersListViewController.swift`, faites-en la classe personnalisée pour la deuxième scène, et collez le code suivant :

```swift
import UIKit
import Alamofire

class OrdersTableViewController: UITableViewController {
    var orders: [Order] = []
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.title = "Commandes des clients"
        fetchOrders { orders in
            self.orders = orders!
            self.tableView.reloadData()
        }
    }
    
    private func fetchOrders(completion: @escaping([Order]?) -> Void) {
        Alamofire.request("http://127.0.0.1:4000/orders").validate().responseJSON { response in
            guard response.result.isSuccess else { return completion(nil) }
            guard let rawOrders = response.result.value as? [[String: Any]?] else { return completion(nil) }
            let orders = rawOrders.flatMap { ordersDict -> Order? in
                guard let orderId = ordersDict!["id"] as? String,
                      let orderStatus = ordersDict!["status"] as? String,
                      var pizza = ordersDict!["pizza"] as? [String: Any] else { return nil }
                pizza["image"] = UIImage(named: pizza["image"] as! String)
                return Order(
                    id: orderId,
                    pizza: Pizza(data: pizza),
                    status: OrderStatus(rawValue: orderStatus)!
                )
            }
            completion(orders)
        }
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return orders.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "order", for: indexPath)
        let order = orders[indexPath.row]
        cell.textLabel?.text = order.pizza.name
        cell.imageView?.image = order.pizza.image
        cell.detailTextLabel?.text = "$\(order.pizza.amount) - \(order.status.rawValue)"
        return cell
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100.0
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let order: Order = orders[indexPath.row]
        let alertCtrl = UIAlertController(
            title: "Changer le statut",
            message: "Changez le statut de la commande en fonction de la progression.",
            preferredStyle: .actionSheet
        )
        alertCtrl.addAction(createActionForStatus(.pending, order: order))
        alertCtrl.addAction(createActionForStatus(.accepted, order: order))
        alertCtrl.addAction(createActionForStatus(.dispatched, order: order))
        alertCtrl.addAction(createActionForStatus(.delivered, order: order))
        alertCtrl.addAction(createActionForStatus(nil, order: nil))
        present(alertCtrl, animated: true, completion: nil)
    }
    
    private func createActionForStatus(_ status: OrderStatus?, order: Order?) -> UIAlertAction {
        let alertTitle = status == nil ? "Annuler" : status?.rawValue
        let alertStyle: UIAlertActionStyle = status == nil ? .cancel : .default
        let action = UIAlertAction(title: alertTitle, style: alertStyle) { action in
            if status != nil {
                self.setStatus(status!, order: order!)
            }
        }
        if status != nil {
            action.isEnabled = status?.rawValue != order?.status.rawValue
        }
        return action
    }
    
    private func setStatus(_ status: OrderStatus, order: Order) {
        updateOrderStatus(status, order: order) { successful in
            guard successful else { return }
            guard let index = self.orders.index(where: {$0.id == order.id}) else { return }
            self.orders[index].status = status
            self.tableView.reloadData()
        }
    }
    
    private func updateOrderStatus(_ status: OrderStatus, order: Order, completion: @escaping(Bool) -> Void) {
        let url = "http://127.0.0.1:4000/orders/" + order.id
        let params = ["status": status.rawValue]
        Alamofire.request(url, method: .put, parameters: params).validate().responseJSON { response in
            guard response.result.isSuccess else { return completion(false) }
            guard let data = response.result.value as? [String: Bool] else { return completion(false) }
            completion(data["status"]!)
        }
    }
}
```

Le code ci-dessus est similaire au code dans le `PizzaListTableViewController` de l'application client, alors consultez-le si vous avez besoin d'explications supplémentaires.

Il y a une méthode `createActionForStatus`, qui est une aide pour créer et configurer un objet `UIAlertAction`. Il y a une méthode `setStatus` qui tente simplement de définir le statut pour une commande. Et puis il y a la méthode `updateOrderStatus` qui envoie la requête de mise à jour en utilisant `Alamofire` à l'API.

Ensuite, créez les classes `Order.swift` et `Pizza.swift` comme nous l'avons fait précédemment dans l'application client :

```swift
// Order.swift
import Foundation

struct Order {
    let id: String
    let pizza: Pizza
    var status: OrderStatus
}

enum OrderStatus: String {
    case pending = "Pending"
    case accepted = "Accepted"
    case dispatched = "Dispatched"
    case delivered = "Delivered"
}

// Pizza.swift
import UIKit

struct Pizza {
    let id: String
    let name: String
    let description: String
    let amount: Float
    let image: UIImage
    init(data: [String: Any]) {
        self.id = data["id"] as! String
        self.name = data["name"] as! String
        self.amount = data["amount"] as! Float
        self.description = data["description"] as! String
        self.image = data["image"] as! UIImage
    }
}
```

C'est tout pour l'application admin. Une dernière chose que nous devons faire, cependant, est de modifier le fichier `info.plist` comme nous l'avons fait dans l'application client.

### Ajout de notifications push à notre application iOS de livraison de nourriture

À ce stade, l'application fonctionne comme prévu dès la sortie de la boîte. Nous devons maintenant ajouter des notifications push à l'application pour la rendre plus engageante même lorsque l'utilisateur n'utilise pas actuellement l'application.

> _⚠️ Vous devez être [inscrit au programme Apple Developer](https://developer.apple.com/programs/enroll/) pour pouvoir utiliser la fonctionnalité de notifications push. De plus, les notifications push ne fonctionnent pas sur les simulateurs, vous aurez donc besoin d'un appareil iOS réel pour tester._

L'API [Push Notifications](https://pusher.com/push-notifications) de Pusher offre un support de première classe pour les applications iOS natives. Vos instances d'application iOS s'abonnent à des **Intérêts**, puis vos serveurs envoient des notifications push à ces intérêts. Chaque instance d'application abonnée à cet intérêt recevra la notification, même si l'application n'est pas ouverte sur l'appareil à ce moment-là.

Cette section décrit comment vous pouvez configurer une application iOS pour recevoir des notifications push transactionnelles concernant vos commandes de livraison de nourriture via Pusher.

#### Configurer APNs

Pusher s'appuie sur le service de notification push Apple (APNs) pour livrer des notifications push aux utilisateurs d'applications iOS en votre nom. Lorsque nous livrons des notifications push, nous utilisons votre clé APNs. Cette page vous guide à travers le processus d'obtention d'une clé APNs et comment la fournir à Pusher.

Rendez-vous sur le tableau de bord du développeur Apple en cliquant [ici](https://developer.apple.com/account) puis créez une nouvelle clé comme indiqué ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/hHxQgS8RO9zvYKL0v80GSOoeN7JUi4WER5m5)

Lorsque vous avez créé la clé, téléchargez-la. Gardez-la en sécurité car nous en aurons besoin dans la section suivante.

> _⚠️ Vous devez garder la clé générée en sécurité car vous ne pouvez pas la récupérer si vous la perdez._

#### Création de votre application Pusher

La prochaine chose que vous devez faire est de créer une nouvelle application de notification push Pusher depuis le [tableau de bord Pusher](https://dash.pusher.com).

![Image](https://cdn-media-1.freecodecamp.org/images/QjfWkFAytWWVCMOus6KjtUsmdRJgGkWj6sii)

Lorsque vous avez créé l'application, vous devriez être présenté avec un assistant de démarrage rapide qui vous aidera à configurer l'application.

Pour configurer les notifications push, vous devrez obtenir une clé APNs d'Apple. Il s'agit de la même clé que celle que nous avons téléchargée dans la section précédente. Une fois que vous avez la clé, téléchargez-la dans l'assistant de démarrage rapide.

![Image](https://cdn-media-1.freecodecamp.org/images/o-lnCbdylBZvsx1n0RSkjfz-RIh8PnLIBZaP)

Entrez votre identifiant d'équipe Apple. Vous pouvez obtenir l'identifiant d'équipe [ici](https://developer.apple.com/account/#/membership). Cliquez sur continuer pour passer à l'étape suivante.

#### Mise à jour de votre application client pour supporter les notifications push

Dans votre application client, ouvrez le `Podfile` et ajoutez le pod suivant à la liste des dépendances :

```
pod 'PushNotifications'
```

Exécutez maintenant la commande `pod install` comme vous l'avez fait précédemment pour intégrer le package de notifications. Lorsque l'installation est terminée, créez une nouvelle classe `AppMisc.swift` et collez ce qui suit :

```swift
class AppMisc {
  static let USER_ID = NSUUID().uuidString.replacingOccurrences(of: "-", with: "_")
}
```

Dans la petite classe ci-dessus, nous générons un identifiant utilisateur pour la session. Dans une application réelle, vous auriez généralement un identifiant utilisateur réel après authentification.

Ouvrez ensuite la classe `AppDelegate` et importez le package `PushNotifications` :

```swift
import PushNotifications
```

Maintenant, dans le cadre de la classe `AppDelegate`, ajoutez ce qui suit :

```swift
let pushNotifications = PushNotifications.shared

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
  self.pushNotifications.start(instanceId: "PUSHER_NOTIF_INSTANCE_ID")
  self.pushNotifications.registerForRemoteNotifications()
  return true
}

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
  self.pushNotifications.registerDeviceToken(deviceToken) {
    try? self.pushNotifications.subscribe(interest: "orders_" + AppMisc.USER_ID)
  }
}
```

> _📱 Remplacez_ `_PUSHER_PUSH_NOTIF_INSTANCE_ID_` _par la clé qui vous est donnée par l'application Pusher._

Dans le code ci-dessus, nous configurons les notifications push dans la méthode `application(didFinishLaunchingWithOptions:)` puis nous nous abonnons dans la méthode `application(didRegisterForRemoteNotificationsWithDeviceToken:)`.

Ensuite, nous devons activer les notifications push pour l'application. Dans le navigateur de projet, sélectionnez votre projet, et cliquez sur l'onglet **Capabilities**. [Activez les notifications push](http://help.apple.com/xcode/mac/current/#/devdfd3d04a1) en mettant le commutateur sur ON.

![Image](https://cdn-media-1.freecodecamp.org/images/t6ImqJhVo3Cha-jqTsTZgmky60-9Dfbw1EJ0)

#### Mise à jour de votre application admin pour supporter les notifications push

Votre application admin doit également être capable de recevoir des notifications push. Le processus est similaire à la configuration ci-dessus. La seule différence sera l'intérêt auquel nous allons nous abonner dans `AppDelegate`, qui sera **orders**.

#### Mise à jour de votre API pour envoyer des notifications push

Les notifications push seront publiées en utilisant notre API de serveur backend, qui est écrite en Node.js. Pour cela, nous utiliserons le [SDK Node.js](https://docs.pusher.com/push-notifications/reference/server-sdk-node). `cd` dans le répertoire du projet backend et exécutez la commande suivante :

```bash
$ npm install pusher-push-notifications-node --save
```

Ensuite, ouvrez le fichier `index.js` et importez le package `pusher-push-notifications-node` :

```js
const PushNotifications = require('pusher-push-notifications-node');

let pushNotifications = new PushNotifications({
    instanceId: 'PUSHER_PUSH_NOTIF_INSTANCE_ID',
    secretKey: 'PUSHER_PUSH_NOTIF_SECRET_KEY'
});
```

Ensuite, nous voulons ajouter une fonction helper qui retourne un message de notification basé sur le statut de la commande. Dans le fichier `index.js`, ajoutez ce qui suit :

```js
function getStatusNotificationForOrder(order) {
    let pizza = order['pizza']
    switch (order['status']) {
        case "Pending":
            return false;
        case "Accepted":
            return `⏳ Votre "${pizza['name']}" est en cours de traitement.`
        case "Dispatched":
            return `😋🍕 Votre "${order['pizza']['name']}" est en route`
        case "Delivered":
            return `🍕 Votre "${pizza['name']}" a été livrée. Bon appétit.`
        default:
            return false;
    }
}
```

Ensuite, dans la route `PUT /orders/:id`, ajoutez le code suivant avant l'instruction return :

```js
let alertMessage = getStatusNotificationForOrder(order)

if (alertMessage !== false) {
   pushNotifications.publish([`orders_${user_id}`], {
        apns: { 
            aps: {
                alert: {
                    title: "Informations sur la commande",
                    body: alertMessage,
                }, 
                sound: 'default'
            } 
        }
    })
    .then(response => console.log('Just published:', response.publishId))
    .catch(error => console.log('Error:', error));
}
```

Dans le code ci-dessus, nous envoyons une notification push à l'intérêt `**orders_${user_id}**` (`user_id` est l'ID généré et passé au serveur backend depuis le client) chaque fois que le statut de la commande est modifié. Ce sera une notification qui sera captée par notre application client, puisque nous nous sommes abonnés à cet intérêt précédemment.

Ensuite, dans la route `POST /orders`, ajoutez le code suivant avant l'instruction return :

```js
pushNotifications.publish(['orders'], {
    apns: {
        aps: {
            alert: {
                title: "⏳ Nouvelle commande arrivée",
                body: `Une commande pour ${pizza['name']} a été passée.`,
            },
            sound: 'default'
        }
    }
})
.then(response => console.log('Just published:', response.publishId))
.catch(error => console.log('Error:', error));
```

Dans ce cas, nous envoyons une notification push à l'intérêt **orders**. Cela sera envoyé à l'application admin qui est abonnée à l'intérêt **orders**.

C'est tout ce qu'il y a à ajouter des notifications push en utilisant Pusher. Voici des enregistrements d'écran de nos applications en action :

![Image](https://cdn-media-1.freecodecamp.org/images/bo5b8nCf2hIuXCT0gsE-Y3aLHE5ajDDDYVZ-)

## Conclusion

Dans cet article, nous avons créé un système de livraison de nourriture de base et nous avons utilisé cela pour démontrer comment utiliser Pusher pour envoyer des notifications push dans plusieurs applications en utilisant la même application Pusher. Espérons que vous avez appris comment vous pouvez utiliser Pusher pour simplifier le processus d'envoi de notifications push à vos utilisateurs.

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/food-delivery-notifications-swift/).