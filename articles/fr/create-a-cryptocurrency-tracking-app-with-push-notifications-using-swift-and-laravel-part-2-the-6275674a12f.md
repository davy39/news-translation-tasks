---
title: Comment créer une application iOS de suivi de cryptomonnaies avec notifications
  push en utilisant Swift et Laravel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T16:39:02.000Z'
originalURL: https://freecodecamp.org/news/create-a-cryptocurrency-tracking-app-with-push-notifications-using-swift-and-laravel-part-2-the-6275674a12f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cQl1eHoplkcQF2dTaWo5FA.jpeg
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: iOS
  slug: ios
- name: Laravel
  slug: laravel
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment créer une application iOS de suivi de cryptomonnaies avec notifications
  push en utilisant Swift et Laravel
seo_desc: 'By Neo Ighodaro

  Part 2


  _Photo by [Unsplash](https://unsplash.com/photos/iGYiBhdNTpE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">André François McKenzie on <a href="https://unsplash.com/...'
---

Par Neo Ighodaro

#### Partie 2

![Image](https://cdn-media-1.freecodecamp.org/images/IGYplFvYpzyybbPqcGLune2bODwCxmj9bc8v)
_Photo par [Unsplash](https://unsplash.com/photos/iGYiBhdNTpE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">André François McKenzie</a> sur <a href="https://unsplash.com/search/photos/bitcoin?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Vous aurez besoin des éléments suivants installés sur votre machine : Xcode, le CLI Laravel, SQLite et Cocoapods. Une familiarité avec l'IDE Xcode sera utile. Vous devriez avoir terminé la première partie de la série.

Dans la [première partie](https://medium.freecodecamp.org/how-to-create-the-backend-of-a-crypto-tracking-app-using-swift-and-laravel-1d9122bc290b) de cet article, nous avons commencé à développer notre application d'alerte de cryptomonnaie. Nous avons développé le backend de l'application qui alimentera l'application iOS. Tel qu'il est, notre application backend peut retourner les paramètres pour un appareil basé sur son UUID, sauvegarder les paramètres pour un appareil basé sur son UUID et également déterminer quels appareils doivent recevoir des notifications push lorsque les devises sont mises à jour.

Dans cette partie, nous nous concentrerons sur la création de l'application iOS en utilisant Swift et Xcode.

### Prérequis

Pour suivre ce tutoriel, vous avez besoin des éléments suivants :

* Avoir terminé la [première partie](https://medium.freecodecamp.org/how-to-create-the-backend-of-a-crypto-tracking-app-using-swift-and-laravel-1d9122bc290b) de cet article.
* [Xcode](https://developer.apple.com/xcode) installé sur votre machine.
* Connaissance de l'IDE Xcode.
* Connaissance de base du [framework Laravel](https://laravel.com/).
* Connaissance de base du [langage de programmation Swift](http://developer.apple.com/swift).
* [CLI Laravel](https://laravel.com/docs/5.6/installation) installé sur votre machine.
* SQLite installé sur votre machine. [Guide d'installation](http://www.sqlitetutorial.net/download-install-sqlite/).
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installé sur votre machine.
* Application [Pusher Beams](https://pusher.com/beams) et [Channels](https://pusher.com/channels).

### Ce que nous allons construire

Nous avons déjà commencé par construire le backend de l'application en utilisant Laravel. Ensuite, nous allons construire l'application iOS en utilisant Swift. Si vous souhaitez tester les notifications push, vous devrez exécuter l'application sur un appareil physique.

### Comment l'application cliente fonctionnera

Pour l'application cliente, l'application iOS, nous allons créer une simple liste qui affichera les devises disponibles et les prix actuels en dollars. Chaque fois que le prix de la cryptomonnaie change, nous déclencherons un événement en utilisant Pusher Channels afin que les prix soient mis à jour.

À partir de l'application, vous pourrez définir un prix minimum et maximum pour être alerté. Par exemple, vous pouvez configurer l'application pour envoyer une notification push lorsque le prix d'un Etherium (ETH) descend en dessous de 500 $. Vous pouvez également configurer l'application pour recevoir une notification lorsque le prix du Bitcoin dépasse 5000 $.

### À quoi ressemblera l'application

Lorsque nous aurons terminé l'application, voici à quoi elle ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/ynnaEkKLDhpnaZBrt7pd4aw5gxGjUYK89hNT)

Commençons.

### Configuration de votre application cliente

Lancez Xcode et cliquez sur **Créer un nouveau projet Xcode**. Sélectionnez **Application à vue unique** et cliquez sur **Suivant**. Entrez votre **Nom de produit**, nous appellerons notre projet _cryptoalat_, et sélectionnez **Swift** dans les options **Langage**. Vous pouvez également modifier tout autre détail que vous souhaitez sur l'écran, puis cliquez sur **Suivant**.

### Installation des dépendances

Maintenant que vous avez votre projet Xcode, fermez Xcode et ouvrez une fenêtre de terminal. `cd` dans le répertoire du projet iOS dans le terminal et exécutez la commande suivante pour créer un Podfile :

```bash
$ pod init
```

> _Le Podfile est une spécification qui décrit les dépendances des cibles d'un ou plusieurs projets Xcode. Le fichier doit simplement être nommé Podfile. Tous les exemples dans les guides sont basés sur la version 1.0 de CocoaPods et suivantes. — [Guides CocoaPods](https://guides.cocoapods.org/using/the-podfile.html)_

Cela générera un nouveau fichier appelé `Podfile` à la racine de votre projet. Ouvrez ce fichier dans n'importe quel éditeur et mettez-le à jour comme suit :

```bash
// Fichier : Podfile
platform :ios, '11.0'

target 'cryptoalat' do
  use_frameworks!

  pod 'Alamofire', '~> 4.7.2'
  pod 'PushNotifications', '~> 0.10.8'
  pod 'PusherSwift', '~> 6.1.0'
  pod 'NotificationBannerSwift', '~> 1.6.3'
end

```

> _Si vous avez utilisé un nom de projet autre que cryptoalat, modifiez-le dans le Podfile pour qu'il corresponde au nom de la cible de votre projet._

Allez dans le terminal et exécutez la commande suivante pour installer vos dépendances :

```bash
$ pod install
```

Lorsque l'installation est terminée, vous aurez un fichier `*.xcworkspace` à la racine de votre projet. Ouvrez ce fichier dans Xcode et commençons à développer notre application d'alerte de cryptomonnaie.

### Construction de l'application iOS

#### Création de notre storyboard

La première chose que nous devons faire est de concevoir notre storyboard pour l'application. Voici à quoi nous voulons que le storyboard ressemble une fois terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/JZxbqFnKDBwtADJ8tJcYigBx9V0zq04dbu0N)

Ouvrez le fichier `Main.storyboard` et concevez-le comme indiqué ci-dessus.

Ci-dessus, nous avons trois scènes. La première scène, qui est le point d'entrée, est la scène de lancement. Nous dessinons ensuite un segue manuel avec un identifiant appelé **Main**. Ensuite, nous définissons le type de segue **Kind** sur **Present Modally**. Cela présentera la scène suivante qui est un contrôleur de vue de navigation. Les contrôleurs de navigation ont déjà un contrôleur de vue racine attaché par défaut.

Nous utiliserons ce contrôleur de vue attaché, qui est un `TableViewController`, comme vue principale pour notre application. Il listera les devises disponibles et nous montrera un champ de texte qui nous permet de changer le paramètre pour cette devise lorsqu'elle est tapée.

Dans la troisième scène, nous définissons l'identifiant de réutilisation des cellules sur **coin** et nous faisons glisser deux étiquettes vers la cellule prototype. La première étiquette sera pour le nom de la pièce et la deuxième étiquette sera pour le prix.

Maintenant que nous avons les scènes, créons quelques contrôleurs et classes de vue et connectons-les à nos scènes de storyboard.

#### Création de vos contrôleurs

Dans Xcode, créez une nouvelle classe `LaunchViewController` et collez le contenu du fichier ci-dessous :

```swift
import UIKit

class LaunchViewController: UIViewController {

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        SettingsService.shared.loadSettings {
            self.routeToMainController()
        }
    }

    fileprivate func routeToMainController() {
        performSegue(withIdentifier: "Main", sender: self)
    }
}

```

> _Définissez le contrôleur comme classe personnalisée pour la première scène dans le fichier `Main.storyboard`._

Dans le code, nous chargeons les paramètres à l'aide d'une classe `SettingsService` que nous créerons plus tard. Lorsque les paramètres sont chargés pour l'appareil, nous appelons la méthode `routeToMainController`, qui route l'application vers le contrôleur principal en utilisant le segue **Main** que nous avons créé précédemment.

Le contrôleur suivant que nous allons créer sera le `CoinsTableViewController`. Ce sera le contrôleur qui sera lié à la troisième scène, qui est la scène principale.

Créez le `CoinsTableViewController` et remplacez le contenu par le code suivant :

```swift
import UIKit
import PusherSwift
import NotificationBannerSwift

struct Coin {
    let name: String
    let rate: Float
}

class CoinsTableViewController: UITableViewController {

    var coins: [Coin] = []

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return coins.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let coin = coins[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "coin", for: indexPath) as! CoinTableViewCell

        cell.name.text = "1 \(coin.name) ="
        cell.amount.text = "$\(String(coin.rate))"

        return cell
    }
}

```

> _Définissez le contrôleur comme classe personnalisée pour la première scène dans le fichier `Main.storyboard`._

Ci-dessus, nous avons défini la structure `Coin` et elle a une propriété `name` et `rate`. Nous avons le contrôleur dans lequel nous définissons la propriété `coins` comme un tableau de `Coin`s. Nous avons ensuite un code standard qui accompagne la création d'un contrôleur de vue de tableau.

La méthode `numberOfSections` spécifie le nombre de sections que le tableau aura. Dans la première méthode `tableView`, nous retournons le nombre de `coins` disponibles et dans la deuxième méthode `tableView`, nous définissons comment nous voulons que chaque ligne soit gérée.

#### Création d'autres classes de support

Si vous avez remarqué dans le code ci-dessus, nous avons référencé une `CoinTableViewCell` comme classe pour chaque ligne dans la dernière méthode `tableView`. Créons cela.

Créez une classe `CoinTableViewCell` et collez le code suivant :

```swift
class CoinTableViewCell: UITableViewCell {
    @IBOutlet weak var name: UILabel!    
    @IBOutlet weak var amount: UILabel!
}

```

Ouvrez le fichier `Main.storyboard` et définissez la classe comme classe personnalisée pour la cellule prototype dans la troisième scène du fichier `Main.storyboard`. Une fois la classe définie, connectez les `@IBOutlet`s comme spécifié dans la classe de cellule ci-dessus.

La classe suivante que nous devons créer est `SettingsService`. Cette classe sera responsable de la mise à jour et de la récupération des paramètres pour l'appareil.

Créez une nouvelle classe `SettingsService` et remplacez le contenu par le code suivant :

```swift
import Foundation
import Alamofire
import NotificationBannerSwift

class SettingsService {
    static let key = "CryptoAlat"
    static let shared = SettingsService()

    var settings: Settings? {
        get {
            return self.getCachedSettings()
        }
        set(settings) {
            if let settings = settings {
                self.updateCachedSettings(settings)
            }
        }
    }

    private init() {}

    func loadSettings(completion: @escaping() -> Void) {
        fetchRemoteSettings { settings in
            guard let settings = settings else {
                return self.saveSettings(self.defaultSettings()) { _ in
                    completion()
                }
            }

            self.updateCachedSettings(settings)
            completion()
        }
    }

    fileprivate func defaultSettings() -> Settings {
        return Settings(
            btc_min_notify: 0, 
            btc_max_notify: 0, 
            eth_min_notify: 0, 
            eth_max_notify: 0
        )
    }

    func saveSettings(_ settings: Settings, completion: @escaping(Bool) -> Void) {
        updateRemoteSettings(settings, completion: { saved in
            if saved {
                self.updateCachedSettings(settings)
            }

            completion(saved)
        })
    }

    fileprivate func fetchRemoteSettings(completion: @escaping (Settings?) -> Void) {
        guard let deviceID = AppConstants.deviceIDFormatted else {
            return completion(nil)
        }

        let url = "\(AppConstants.API_URL)?u=\(deviceID)"
        Alamofire.request(url).validate().responseJSON { resp in
            if let data = resp.data, resp.result.isSuccess {
                let decoder = JSONDecoder()
                if let settings = try? decoder.decode(Settings.self, from: data) {
                    return completion(settings)
                }
            }

            completion(nil)
        }
    }

    fileprivate func updateRemoteSettings(_ settings: Settings, completion: @escaping(Bool) -> Void) {
        guard let deviceID = AppConstants.deviceIDFormatted else {
            return completion(false)
        }

        let params = settings.toParams()
        let url = "\(AppConstants.API_URL)?u=\(deviceID)"
        Alamofire.request(url, method: .post, parameters: params).validate().responseJSON { resp in
            guard resp.result.isSuccess, let res = resp.result.value as? [String: String] else {
                return StatusBarNotificationBanner(title: "Échec de la mise à jour des paramètres.", style: .danger).show()
            }

            completion((res["status"] == "success"))
        }
    }

    fileprivate func updateCachedSettings(_ settings: Settings) {
        if let encodedSettings = try? JSONEncoder().encode(settings) {
            UserDefaults.standard.set(encodedSettings, forKey: SettingsService.key)
        }
    }

    fileprivate func getCachedSettings() -> Settings? {
        let defaults = UserDefaults.standard
        if let data = defaults.object(forKey: SettingsService.key) as? Data {
            let decoder = JSONDecoder()
            if let decodedSettings = try? decoder.decode(Settings.self, from: data) {
                return decodedSettings
            }
        }

        return nil
    }
}

```

Ci-dessus, nous avons le `SettingsService`. La première méthode `loadSettings` charge les paramètres depuis l'API puis les sauvegarde localement. Si aucun paramètre n'est disponible à distance, elle appelle la méthode `defaultSettings` et sauvegarde la réponse vers l'API.

La méthode `saveSettings` sauvegarde les `Settings` à distance en utilisant `updateRemoteSettings` et localement en utilisant `updateCachedSettings`. La méthode `fetchRemoteSettings` récupère les paramètres depuis l'API et décode la réponse en utilisant l'[API Swift decodable](https://blog.pusher.com/swift-4-decoding-json-codable/).

Ensuite, définissons la structure `Settings` et faisons-la étendre `Codable`. Dans le même fichier pour le `SettingsService`, ajoutez ceci au-dessus de la définition de la classe `SettingsService` :

```swift
struct Settings: Codable {
    var btc_min_notify: Int?
    var btc_max_notify: Int?
    var eth_min_notify: Int?
    var eth_max_notify: Int?

    func toParams() -> Parameters {
        var params: Parameters = [:]

        if let btcMin = btc_min_notify { params["btc_min_notify"] = btcMin }
        if let btcMax = btc_max_notify { params["btc_max_notify"] = btcMax }
        if let ethMin = eth_min_notify { params["eth_min_notify"] = ethMin }
        if let ethMax = eth_max_notify { params["eth_max_notify"] = ethMax }

        return params
    }
}

```

Ci-dessus, nous avons une structure `Settings` simple qui se conforme à `Codable`. Nous avons également une méthode `toParams` qui convertit les propriétés en un type `Parameters` afin que nous puissions l'utiliser avec [Alamofire](https://github.com/Alamofire/Alamofire) lors de la réalisation de requêtes.

Une dernière classe que nous devons créer est `AppConstants`. Nous utiliserons cette classe pour conserver toutes les données que nous prévoyons de garder constantes et inchangées tout au long de la durée de vie de l'application.

Créez un fichier `AppConstants` et collez le code suivant :

```swift
import UIKit

struct AppConstants {
    static let API_URL = "http://127.0.0.1:8000/api/settings"
    static let deviceID = UIDevice.current.identifierForVendor?.uuidString
    static let deviceIDFormatted = AppConstants.deviceID?.replacingOccurrences(of: "-", with: "_").lowercased()
    static let PUSHER_INSTANCE_ID = "PUSHER_BEAMS_INSTANCE_ID"
    static let PUSHER_APP_KEY = "PUSHER_APP_KEY"
    static let PUSHER_APP_CLUSTER = "PUSHER_APP_CLUSTER"
}

```

> _Remplacez les clés `PUSHER_*` par les valeurs obtenues depuis le tableau de bord Pusher Channels et Beams._

#### Mise à jour des paramètres pour l'appareil

Maintenant que nous avons défini le service de paramètres, mettons à jour notre contrôleur afin que l'utilisateur puisse définir les prix minimum et maximum pour chaque devise.

Ouvrez la classe `CoinsTableViewController` et ajoutez la méthode suivante :

```swift
override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    let coin = coins[indexPath.row]

    var minTextField: UITextField?
    var maxTextField: UITextField?

    let title = "Gérer les alertes \(coin.name)"
    let message = "Une notification vous sera envoyée lorsque le prix dépasse ou descend en dessous du prix minimum et maximum. Définissez à zéro pour désactiver la notification."

    let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)

    alert.addTextField { textfield in
        minTextField = textfield
        textfield.placeholder = "Alerte lorsque le prix est en dessous"
    }

    alert.addTextField { textfield in
        maxTextField = textfield
        textfield.placeholder = "Alerte lorsque le prix est au-dessus"
    }

    alert.addAction(UIAlertAction(title: "Annuler", style: .cancel, handler: nil))

    alert.addAction(UIAlertAction(title: "Enregistrer", style: .default, handler: { action in
        guard let minPrice = minTextField?.text, let maxPrice = maxTextField?.text else {
            return StatusBarNotificationBanner(title: "Prix min ou max invalide", style: .danger).show()
        }

        var btcMin: Int?, btcMax: Int?, ethMin: Int?, ethMax: Int?

        switch coin.name {
        case "BTC":
            btcMin = Int(minPrice)
            btcMax = Int(maxPrice)
        case "ETH":
            ethMin = Int(minPrice)
            ethMax = Int(maxPrice)
        default:
            return
        }

        let settings = Settings(
            btc_min_notify: btcMin,
            btc_max_notify: btcMax,
            eth_min_notify: ethMin,
            eth_max_notify: ethMax
        )

        SettingsService.shared.saveSettings(settings, completion: { saved in
            if saved {
                StatusBarNotificationBanner(title: "Enregistré avec succès").show()
            }
        })
    }))

    present(alert, animated: true, completion: nil)
}

```

La méthode ci-dessus est automatiquement appelée lorsqu'une ligne est sélectionnée. Dans cette méthode, nous affichons un `UIAlertController` avec deux champs de texte pour le prix minimum et le prix maximum. Lorsque les prix sont soumis, le `SettingsService` que nous avons créé précédemment se charge de mettre à jour les valeurs à la fois localement et à distance.

#### Ajout de la prise en charge des mises à jour de cryptomonnaie en temps réel

Ouvrez le `CoinsTableViewController` et ajoutez la propriété `pusher` à la classe comme indiqué ci-dessous :

```
var pusher: Pusher!
```

Ensuite, remplacez la méthode `viewDidLoad` par le code suivant :

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    pusher = Pusher(
        key: AppConstants.PUSHER_APP_KEY, 
        options: PusherClientOptions(host: .cluster(AppConstants.PUSHER_APP_CLUSTER))
    )

    let channel = pusher.subscribe("currency-update")

    let _ = channel.bind(eventName: "currency.updated") { data in
        if let data = data as? [String: [String: [String: Float]]] {
            guard let payload = data["payload"] else { return }

            self.coins = []

            for (coin, deets) in payload {
                guard let currentPrice = deets["current"] else { return }
                self.coins.append(Coin(name: coin, rate: currentPrice))
            }

            Dispatch.main.async {
                self.tableView.reloadData()
            }
        }
    }

    pusher.connect()
}

```

Dans le code ci-dessus, nous utilisons le [SDK Swift de Pusher](https://pusher.com/docs/ios_quick_start) pour nous abonner à notre canal Pusher `currency-update`. Nous nous abonnons ensuite à l'événement `currency.updated` sur ce canal. Chaque fois que cet événement est déclenché, nous actualisons le prix de la cryptomonnaie en temps réel.

### Ajout de notifications push à notre nouvelle application iOS

Pour ajouter la prise en charge des notifications push, ouvrez la classe `AppDelegate` et remplacez le contenu par le suivant :

```swift
import UIKit
import PushNotifications

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        PushNotifications.shared.start(instanceId: AppConstants.PUSHER_INSTANCE_ID)
        PushNotifications.shared.registerForRemoteNotifications()
        return true
    }

    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        PushNotifications.shared.registerDeviceToken(deviceToken) {
            if let deviceID = AppConstants.deviceIDFormatted {
                try? PushNotifications.shared.subscribe(interest: "\(deviceID)_eth_changed")
                try? PushNotifications.shared.subscribe(interest: "\(deviceID)_btc_changed")
            }
        }
    }
}

```

Dans la classe ci-dessus, nous utilisons le [SDK Swift de Pusher Beams](https://docs.pusher.com/push-notifications/reference/ios) pour enregistrer l'appareil pour les notifications push. Nous nous abonnons ensuite aux intérêts `*_eth_changed` et `*_btc_changed`, où `*` est l'UUID unique de l'appareil.

Maintenant que nous avons terminé la logique de l'application, activons les notifications push sur l'application dans Xcode.

Dans le navigateur de projet, sélectionnez votre projet, puis cliquez sur l'onglet **Capacités**. [Activez les notifications push](http://help.apple.com/xcode/mac/current/#/devdfd3d04a1) en mettant le commutateur sur ON.

![Image](https://cdn-media-1.freecodecamp.org/images/4Kd00J1IvFFj633HSm-WbwTxm5pHFxhPRY82)

Cela créera un fichier d'autorisations à la racine de votre projet. Avec cela, vous avez provisionné votre application pour recevoir pleinement les notifications push.

### Permettre à notre application de se connecter localement

Si vous allez tester le backend de l'application en utilisant un serveur local, alors il y a une dernière chose que nous devons faire. Ouvrez le fichier `info.plist` et ajoutez une entrée au fichier `plist` pour permettre la connexion à notre serveur local :

![Image](https://cdn-media-1.freecodecamp.org/images/973kwkgkzdbbxkJQzMEePM3vR2yCwC2J-FRn)

C'est tout. Nous pouvons exécuter notre application. Cependant, **n'oubliez pas que pour démontrer les notifications push, vous aurez besoin d'un appareil iOS réel car les simulateurs ne peuvent pas recevoir de notifications push.** Si vous utilisez un appareil physique, vous devrez exposer votre API locale en utilisant [Ngrok](https://ngrok.com) puis changer l'`API_URL` **dans** `AppConstants`.

Chaque fois que vous souhaitez mettre à jour les prix des devises, exécutez la commande suivante manuellement dans votre application Laravel :

```bash
$ php artisan schedule:run
```

Voici un enregistrement d'écran de l'application en action :

![Image](https://cdn-media-1.freecodecamp.org/images/OBlHx04eWtcmomYWEAXfZlr3N2kM9ZC90Wym)

### Conclusion

Dans cet article, nous avons pu voir à quel point il est facile de créer un site web d'alerte de cryptomonnaie en utilisant Laravel, Swift, Pusher Channels et Pusher Beams. Le code source de l'application construite dans cet article est disponible sur [GitHub](https://github.com/neoighodaro/cryptocurrency-alert-ios-app).

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/cryptocurrency-tracking-swift-laravel-part-2).