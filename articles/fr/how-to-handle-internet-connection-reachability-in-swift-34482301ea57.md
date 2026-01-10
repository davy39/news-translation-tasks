---
title: Comment gérer la disponibilité de la connexion Internet en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T18:15:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-internet-connection-reachability-in-swift-34482301ea57
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yRw9lns3oUletanc3gUBeA.png
tags:
- name: internet
  slug: internet
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment gérer la disponibilité de la connexion Internet en Swift
seo_desc: 'By Neo Ighodaro

  More often than not, mobile applications need an active internet connection to function
  properly. It is normal, however, for the internet connection to be lost. In cases
  like these, it is up to the developer to come up with ways to ma...'
---

Par Neo Ighodaro

Le plus souvent, les applications mobiles nécessitent une connexion Internet active pour fonctionner correctement. Il est cependant normal que la connexion Internet soit perdue. Dans ces cas, c'est au développeur de trouver des moyens de rendre l'expérience supportable, ou au moins, de notifier l'utilisateur.

Dans cet article, nous allons voir comment détecter les problèmes de connexion Internet en Swift, et quelques façons de les gérer.

Voici l'application exemple que nous allons construire et comment elle gère différents scénarios de connectivité Internet :

![Image](https://cdn-media-1.freecodecamp.org/images/mVMX39hAMJRBGeo3-gn5koLvThXvN17bZyLE)

### Prérequis

Pour pouvoir suivre cet article, vous aurez besoin des prérequis suivants :

* [Xcode](https://developer.apple.com/xcode/) installé sur votre machine.
* Connaissance du langage de programmation Swift.
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installé sur votre machine.

Lorsque vous avez les prérequis ci-dessus, plongeons-nous dans le sujet.

### Configuration de notre espace de travail

Avant de commencer, nous allons créer un terrain de jeu (playground). C'est ici que nous allons écrire tous nos cas d'utilisation et les gérer.

Swift dispose de sa propre implémentation de Reachability pour détecter les problèmes de connexion, mais nous allons utiliser une [bibliothèque tierce](https://github.com/tonymillion/Reachability). Nous faisons cela parce que c'est plus facile et que l'API est plus expressive que celle intégrée.

Ouvrez Xcode et configurez un nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/lDZ0nerqBJ40Ta8ZQs4DBDOkxahc8i2eVBxQ)

Ce projet sera un simple terrain de jeu avec lequel nous pouvons expérimenter.

Pour détecter lorsque la connexion passe hors ligne, nous allons utiliser le package [**Reachability.swift**](https://github.com/ashleymills/Reachability.swift). Il s'agit d'un "remplacement pour la Reachability d'Apple, réécrite en Swift avec des fermetures".

Ouvrez votre terminal et exécutez la commande suivante :

```
$ pod init
```

Cela créera un nouveau fichier `Podfile` où nous pourrons déclarer les dépendances Cocoapods. Ouvrez le fichier `Podfile` et remplacez son contenu par le code ci-dessous :

```
platform :ios, '9.0'
```

```
target 'nom_du_projet' do    use_frameworks!    pod 'ReachabilitySwift'    pod 'Alamofire'end
```

> **_Vous devez remplacer_** `**nom_du_projet**` **par le nom de votre projet.**

Enregistrez le fichier et exécutez la commande suivante pour installer les Pods dans votre projet :

```
$ pod install
```

Lorsque l'installation est terminée, ouvrez le fichier `*.xcworkspace` à la racine de votre projet. Cela lancera Xcode.

### Création de notre Network Reachability Manager

Créez une nouvelle classe `NetworkManager`. Cette classe stockera le statut du réseau et servira de simple proxy au package `Reachability`. Dans le fichier, collez le code ci-dessous :

```
import Foundationimport Reachability
```

```
class NetworkManager: NSObject {
```

```
    var reachability: Reachability!
```

```
    static let sharedInstance: NetworkManager = {         return NetworkManager()     }()
```

```
    override init() {        super.init()
```

```
        // Initialiser la reachability        reachability = Reachability()!
```

```
        // Enregistrer un observateur pour le statut du réseau        NotificationCenter.default.addObserver(            self,            selector: #selector(networkStatusChanged(_:)),            name: .reachabilityChanged,            object: reachability        )
```

```
        do {            // Démarrer le notificateur de statut du réseau            try reachability.startNotifier()        } catch {            print("Impossible de démarrer le notificateur")        }    }
```

```
    @objc func networkStatusChanged(_ notification: Notification) {        // Faire quelque chose globalement ici !    }
```

```
    static func stopNotifier() -> Void {        do {            // Arrêter le notificateur de statut du réseau            try (NetworkManager.sharedInstance.reachability).startNotifier()        } catch {            print("Erreur lors de l'arrêt du notificateur")        }    }
```

```
    // Le réseau est accessible    static func isReachable(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection != .none {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Le réseau est inaccessible    static func isUnreachable(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .none {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Le réseau est accessible via WWAN/Cellular    static func isReachableViaWWAN(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .cellular {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Le réseau est accessible via WiFi    static func isReachableViaWiFi(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .wifi {            completed(NetworkManager.sharedInstance)        }    }]
```

Dans la classe ci-dessus, nous avons défini plusieurs fonctions d'assistance qui nous aideront à démarrer avec la surveillance du statut du réseau. Nous avons une `sharedInstance` qui est un singleton et que nous pouvons appeler si nous ne voulons pas créer plusieurs instances de la classe `NetworkManager`.

Dans la méthode `init`, nous créons une instance de `Reachability` puis nous enregistrons une notification en utilisant la classe `NotificationCenter`. Maintenant, chaque fois que le statut du réseau change, le rappel spécifié par `NotificationCenter` (qui est `networkStatusChanged`) sera appelé. Nous pouvons utiliser cela pour faire quelque chose de global qui est activé lorsque le réseau est inaccessible.

Nous avons défini d'autres fonctions d'assistance qui faciliteront généralement l'exécution de code, en fonction du statut de notre connexion Internet. Nous avons `*isReachable*`, `*isUnreachable*`, `*isReachableViaWWAN*` et `*isReachableViaWiFi*`.

L'utilisation de l'un de ces assistants ressemblera généralement à ceci :

```
NetworkManager.isReachable { networkManagerInstance in  print("Le réseau est disponible")}
```

```
NetworkManager.isUnreachable { networkManagerInstance in  print("Le réseau est indisponible")}
```

> **_Ce n'est pas un écouteur d'événements et ne s'exécutera qu'une seule fois. Pour utiliser un écouteur afin de détecter les changements de réseau en temps réel, vous devrez utiliser_** `NetworkManager.sharedInstance.reachability.whenReachable`**. Nous montrerons un exemple plus tard dans l'article.**

Maintenant que nous avons une classe de gestion, voyons comment nous pouvons l'utiliser dans une application.

### Gestion de la disponibilité du réseau au lancement de l'application

Parfois, votre application dépend fortement d'une connexion Internet et vous devez détecter le statut au lancement. Voyons comment nous pouvons gérer cela en utilisant la classe `NetworkManager`.

Créez un nouveau contrôleur appelé `LaunchViewController`. Nous traiterons la première vue du contrôleur dans le storyboard comme le contrôleur de lancement. Nous allons essayer de détecter si l'appareil de l'utilisateur est en ligne et, si ce n'est pas le cas, nous allons créer une page hors ligne pour gérer cela afin que l'utilisateur ne puisse pas accéder à l'application du tout.

Dans le `LaunchController`, remplacez le contenu par le code suivant :

```
import UIKit
```

```
class LaunchViewController: UIViewController {    let network: NetworkManager = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()
```

```
        NetworkManager.isUnreachable { _ in            self.showOfflinePage()        }    }
```

```
    private func showOfflinePage() -> Void {        DispatchQueue.main.async {            self.performSegue(                withIdentifier: "NetworkUnavailable",                 sender: self            )        }    }}
```

Dans cette classe, nous utilisons la méthode `*isUnreachable*` de notre `NetworkManager` pour déclencher la méthode `showOffline` lorsque le réseau est indisponible. Créons ce contrôleur de vue. Créez un nouveau contrôleur de vue appelé `OfflineViewController`.

Ouvrez le fichier `Main.storyboard` et définissez la classe personnalisée de la première vue sur `LaunchViewController`.

Ensuite, créez un nouveau contrôleur de vue dans le storyboard. Définissez `OfflineViewController` comme classe personnalisée pour ce nouveau contrôleur de vue. Créez maintenant un segue manuel appelé `NetworkUnavailable` entre le nouveau contrôleur de vue et le `LaunchViewController`. Lorsque vous avez terminé, vous devriez avoir quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0i0-0rCSRzRgpa1oUqpcDfOXw3qWEUb5C8G7)

Maintenant, exécutons l'application. Notez, cependant, que avant d'exécuter votre application, votre machine de développement doit être hors ligne car le simulateur iOS utilise la connexion Internet de la machine. Lorsque vous exécutez l'application, vous devriez obtenir la page hors ligne que nous avons créée.

Maintenant, créons un contrôleur de vue qui apparaît lorsqu'il y a une connexion.

### Gestion des événements lorsque l'appareil se connecte

Maintenant que nous avons créé un contrôleur de vue hors ligne et qu'il fonctionne lorsque l'appareil est hors ligne, gérons ce qui se passe lorsque l'appareil est de nouveau en ligne.

Créez un nouveau contrôleur de navigation dans le storyboard sous le contrôleur de vue hors ligne. Nous allons créer un contrôleur qui affiche les derniers posts de Reddit. Créez une nouvelle classe de contrôleur de vue appelée `PostsTableViewController`. Faites-en maintenant la classe personnalisée pour le contrôleur de vue attaché au contrôleur de navigation.

Maintenant, créez un segue manuel appelé `MainController` du contrôleur de navigation vers le contrôleur de vue de lancement et le contrôleur de vue hors ligne. Vous devriez avoir quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nU2vrOq897dT-Q2NBQFl9AqqFICaW81aaUny)

Maintenant, ouvrez la classe `LaunchViewController` et ajoutez ce qui suit en bas de la méthode `viewDidLoad` :

```
NetworkManager.isReachable { _ in    self.showMainPage()}
```

Ensuite, ajoutez la méthode ci-dessous au contrôleur :

```
private func showMainPage() -> Void {    DispatchQueue.main.async {        self.performSegue(            withIdentifier: "MainController",             sender: self        )    }}
```

Cela garantira que lorsque l'application est lancée, elle vérifiera la connectivité et, si la connexion est disponible, elle présentera le `PostsTableViewController`. Sinon, elle présentera le `OfflineViewController`.

Super ! Mais que se passe-t-il lorsque l'utilisateur a atteint le `OfflineViewController` et que le réseau revient en ligne ? Gérons ce scénario.

Ouvrez le `OfflineViewController` et remplacez le code par le code ci-dessous :

```
import UIKit 
```

```
class OfflineViewController: UIViewController {    let network = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()
```

```
        // Si le réseau est accessible, afficher le contrôleur principal        network.reachability.whenReachable = { _ in            self.showMainController()        }    }
```

```
    override func viewWillAppear(_ animated: Bool) {        super.viewWillAppear(animated)
```

```
        navigationController?.setNavigationBarHidden(true, animated: animated)    }
```

```
    override func viewWillDisappear(_ animated: Bool) {        super.viewWillDisappear(animated)
```

```
        navigationController?.setNavigationBarHidden(false, animated: animated)    }
```

```
    private func showMainController() -> Void {        DispatchQueue.main.async {            self.performSegue(withIdentifier: "MainController", sender: self)        }    }}
```

Dans le contrôleur ci-dessus, vous pouvez voir, dans la méthode `viewDidLoad`, que nous définissons la complétion `whenReachable` pour afficher le contrôleur principal. Cela signifie que, tant qu'il est hors ligne, vous surveillez lorsque l'appareil se reconnecte. Lorsqu'il se reconnecte, présentez le `PostsTableViewController`.

Nous remplaçons également les méthodes `viewWillAppear` et `viewWillDisappear` pour nous assurer que la barre de navigation ne s'affiche pas sur le contrôleur de vue hors ligne.

#### **Récupération des posts depuis l'API Reddit en Swift**

Maintenant, ajoutons la logique qui récupérera les données de Reddit et les affichera sur notre `PostsTableViewController`. Ouvrez le fichier et remplacez le contenu par le code ci-dessous :

```
import UIKitimport Alamofire
```

```
struct RedditPost {    let title: String!    let subreddit: String!}
```

```
class PostsTableViewController: UITableViewController {    var posts = [RedditPost]()
```

```
    let network = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()        navigationItem.title = "Derniers Posts"
```

```
        // Récupérer les posts puis recharger la table        fetchPosts { posts in            self.posts = posts            self.tableView.reloadData()        }    }
```

```
    private func fetchPosts(completion: @escaping (_ posts: [RedditPost]) -> Void) -> Void {        // Envoyer une requête à l'API Reddit        Alamofire.request("https://api.reddit.com").validate().responseJSON { response in            switch response.result {            case .success(let JSON):                let data = JSON as! [String:AnyObject]                guard let children = data["data"]!["children"] as? [AnyObject] else { return }                var posts = [RedditPost]()
```

```
                // Parcourir les posts Reddit puis assigner un post au tableau des posts                for child in 0...children.count-1 {                    let post = children[child]["data"] as! [String: AnyObject]
```

```
                    posts.append(RedditPost(                        title: post["title"] as! String,                        subreddit: "/r/" + (post["subreddit"] as! String)                    ))                }
```

```
                DispatchQueue.main.async {                    completion(posts)                }            case .failure(let error):                print(error)            }        }    }
```

```
    override func didReceiveMemoryWarning() {        super.didReceiveMemoryWarning()    }
```

```
    // MARK: - Table view data source    override func numberOfSections(in tableView: UITableView) -> Int {        return 1    }
```

```
    // Retourner le nombre de posts disponibles    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {        return self.posts.count    }
```

```
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {        let cell = tableView.dequeueReusableCell(withIdentifier: "PostCell", for: indexPath)        let post = posts[indexPath.row] as RedditPost        cell.textLabel?.text = post.title        cell.detailTextLabel?.text = post.subreddit        return cell    }}
```

Dans la méthode `fetchPosts`, nous utilisons `Alamofire` pour envoyer une requête GET à l'API Reddit. Nous analysons ensuite la réponse et l'ajoutons à la structure `RedditPost` que nous avons créée en haut du fichier. Cela rend les données que nous passons à la `tableView` cohérentes.

### Gestion des événements lorsque l'appareil passe hors ligne

Maintenant, gérons un autre scénario. Imaginez que, tout en consultant les derniers posts de Reddit, vous perdez la connectivité. Que se passe-t-il ? Affichons à nouveau la page hors ligne lorsque cela se produit.

Comme précédemment, créez un segue manuel appelé `NetworkUnavailable` du `PostsTableViewController` vers le `OfflineViewController`. Ajoutez maintenant ce code en bas de la méthode `viewDidLoad` :

```
network.reachability.whenUnreachable = { reachability in    self.showOfflinePage()}
```

Ajoutez maintenant la méthode ci-dessous au contrôleur :

```
private func showOfflinePage() -> Void {    DispatchQueue.main.async {        self.performSegue(withIdentifier: "NetworkUnavailable", sender: self)    }}
```

Cela écoutera lorsque l'appareil passera hors ligne et, si cela se produit, il affichera `showOfflinePage`.

C'est tout ! Nous avons pu gérer les événements hors ligne et en ligne en utilisant notre NetworkManager en Swift.

### Conclusion

Dans cet article, nous avons examiné comment nous assurer que votre application peut gérer les événements en ligne et hors ligne lorsqu'ils se produisent. Vous pouvez toujours implémenter cela de la manière que vous souhaitez. Si vous avez des questions ou des commentaires, laissez-les ci-dessous dans les commentaires.

Le code source de ce terrain de jeu est disponible sur [GitHub](https://github.com/neoighodaro/Handling-internet-connection-reachability-in-Swift).

Cet article a été publié pour la première fois sur [Pusher](https://blog.pusher.com/handling-internet-connection-reachability-swift/).