---
title: Apprendre les meilleures pratiques iOS en construisant une application de recettes
  simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T18:39:27.000Z'
originalURL: https://freecodecamp.org/news/learn-ios-best-practices-by-building-a-simple-recipes-app-9bcbce4d10d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VOVTKtqru5Ssdd7L
tags:
- name: Apps
  slug: apps-tag
- name: iOS
  slug: ios
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprendre les meilleures pratiques iOS en construisant une application
  de recettes simple
seo_desc: 'By Khoa Pham

  I started iOS development when iOS 7 had been announced. And I have learned a bit,
  through working, advice from colleagues and the iOS community.

  In this article, I’d like to share a lot of good practices by taking the example
  of a simpl...'
---

Par Khoa Pham

J'ai commencé le développement iOS lorsque iOS 7 a été annoncé. Et j'ai appris quelques choses, à travers le travail, les conseils de collègues et la communauté iOS.

Dans cet article, je souhaite partager de nombreuses bonnes pratiques en prenant l'exemple d'une application de recettes simple. Le code source est disponible sur GitHub [Recettes](https://github.com/onmyway133/recipes).

L'application est une application maître-détail traditionnelle qui présente une liste de recettes ainsi que leurs informations détaillées.

Il existe des milliers de façons de résoudre un problème, et la manière dont un problème est abordé dépend également des goûts personnels. Espérons que, tout au long de cet article, vous apprendrez quelque chose d'utile — j'ai moi-même beaucoup appris lorsque j'ai réalisé ce projet.

J'ai ajouté des liens vers certains mots-clés où j'ai estimé qu'une lecture supplémentaire serait bénéfique. Alors n'hésitez pas à les consulter. Tout retour est le bienvenu.

Alors commençons...

Voici un aperçu de haut niveau de ce que vous allez construire.

![Image](https://cdn-media-1.freecodecamp.org/images/5uykDWLBm7zPyKF016T6gJloE8O8hsWy8foD)

### Pour commencer

Décidons des outils et des paramètres de projet que nous allons utiliser.

#### Version de Xcode et Swift

Lors de la [WWDC 2018](https://developer.apple.com/videos/wwdc2018/), Apple a introduit Xcode 10 avec Swift 4.2. Cependant, au moment de la rédaction, Xcode 10 est toujours en version bêta 5. Alors restons avec le stable Xcode 9 et Swift 4.1. Xcode 4.2 a quelques fonctionnalités intéressantes — vous pouvez jouer avec via ce super [Playground](https://github.com/ole/whats-new-in-swift-4-2). Il n'introduit pas de grands changements par rapport à Swift 4.1, donc nous pouvons facilement mettre à jour notre application dans un futur proche si nécessaire.

Vous devriez définir la version de Swift dans les paramètres du projet plutôt que dans les paramètres de la cible. Cela signifie que toutes les cibles du projet partagent la même version de Swift (4.1).

![Image](https://cdn-media-1.freecodecamp.org/images/Me5o1yP4nOiUIMN99jkG3AwYg8XjgGKWuw3H)

#### Version minimale d'iOS à supporter

En été 2018, iOS 12 est en bêta publique 5 et nous ne pouvons pas cibler iOS 12 sans Xcode 10. Dans cet article, nous utilisons Xcode 9 et le SDK de base est iOS 11. Selon les exigences et les bases d'utilisateurs, certaines applications doivent supporter d'anciennes versions d'iOS. Bien que les utilisateurs d'iOS tendent à adopter les nouvelles versions d'iOS plus rapidement que ceux qui utilisent Android, certains restent avec d'anciennes versions. Selon les conseils d'Apple, nous devons supporter les **deux versions les plus récentes**, qui sont iOS 10 et iOS 11. Selon les [mesures de l'App Store](https://developer.apple.com/support/app-store/) du 31 mai 2018, seulement 5% des utilisateurs utilisent iOS 9 et les versions antérieures.

![Image](https://cdn-media-1.freecodecamp.org/images/L24rFD0qfKPmxzJz36xhNKMTnzPafkimZVwW)

Cibler de nouvelles versions d'iOS signifie que nous pouvons tirer parti des nouveaux SDK, que les ingénieurs d'Apple améliorent chaque année. Le [site des développeurs Apple](https://developer.apple.com/documentation/uikit/views_and_controls?changes=latest_minor) a une vue améliorée du journal des modifications. Maintenant, il est plus facile de voir ce qui a été ajouté ou modifié.

![Image](https://cdn-media-1.freecodecamp.org/images/U9XtDqYFeQUZvM6T0x8k8XImCuYq0TN9DR7R)

Idéalement, pour déterminer quand abandonner le support des anciennes versions d'iOS, nous avons besoin d'analyses sur la façon dont les utilisateurs utilisent notre application.

#### Organisation du projet Xcode

Lorsque nous créons le nouveau projet, sélectionnez à la fois « Include Unit Tests » et « Include UI Tests » car il est recommandé d'écrire des tests tôt. Les changements récents dans le framework XCTest, en particulier dans les UI Tests, rendent les tests très faciles et assez stables.

![Image](https://cdn-media-1.freecodecamp.org/images/kJYaIgi0ZtafoQdIUj9l2SOxg5PmGH-sxDCG)

Avant d'ajouter de nouveaux fichiers au projet, prenez une pause et réfléchissez à la structure de votre application. Comment voulons-nous organiser les fichiers ? Nous avons quelques options. Nous pouvons organiser les fichiers par fonctionnalité/module ou par rôle/types. Chacune a ses avantages et ses inconvénients et je vais les discuter ci-dessous.

**Par rôle/type :**

* **Avantages :** Il y a moins de réflexion sur l'endroit où placer les fichiers. Il est également plus facile d'appliquer des scripts ou des filtres.
* **Inconvénients :** Il est difficile de corréler si nous voulons trouver plusieurs fichiers liés à la même fonctionnalité. Cela prendrait également du temps pour réorganiser les fichiers si nous voulons en faire des composants réutilisables à l'avenir.

**Par fonctionnalité/module**

* **Avantages :** Cela rend tout modulaire et encourage la composition.
* **Inconvénients :** Cela peut devenir désordonné lorsque de nombreux fichiers de différents types sont regroupés.

#### **Rester modulaire**

Personnellement, j'essaie d'organiser mon code par fonctionnalités/composants autant que possible. Cela facilite l'identification du code lié à corriger et l'ajout de nouvelles fonctionnalités à l'avenir. Cela répond à la question « Que fait cette application ? » au lieu de « Qu'est-ce que ce fichier ? » [Voici un bon article à ce sujet](http://merowing.info/2014/03/subjective-guide-to-writing-ios-apps-part-1-introduction/).

Une bonne règle de base est de rester cohérent, peu importe la structure que vous choisissez. 👍

### Structure de l'application Recettes

Voici la structure de l'application que notre application de recettes utilise :

#### **Source**

Contient les fichiers de code source, divisés en composants :

* **Fonctionnalités :** les principales fonctionnalités de l'application
* **Accueil :** l'écran d'accueil, affichant une liste de recettes et une recherche ouverte
* **Liste :** affiche une liste de recettes, y compris le rechargement d'une recette et l'affichage d'une vue vide lorsqu'une recette n'existe pas
* **Recherche :** gère la recherche et le débogage
* **Détail :** affiche les informations détaillées

#### **Bibliothèque**

Contient les composants principaux de notre application :

* **Flux :** contient FlowController pour gérer les flux
* **Adaptateur :** source de données générique pour `UICollectionView`
* **Extension :** extensions pratiques pour les opérations courantes
* **Modèle :** Le modèle dans l'application, analysé à partir de JSON

#### **Ressource**

Contient les fichiers plist, les ressources et les Storyboard.

### Conventions de code

Je suis d'accord avec la plupart des guides de style dans [raywenderlich/swift-style-guide](https://github.com/raywenderlich/swift-style-guide) et [github/swift-style-guide](https://github.com/github/swift-style-guide). Ceux-ci sont simples et raisonnables à utiliser dans un projet Swift. Consultez également les [Directives officielles de conception d'API](https://swift.org/documentation/api-design-guidelines/) créées par l'équipe Swift d'Apple sur la façon d'écrire un meilleur code Swift.

Quel que soit le guide de style que vous choisissez de suivre, la **clarté du code** doit être votre objectif le plus important.

L'indentation et la guerre des tabulations et des espaces sont un sujet sensible, mais encore une fois, cela dépend des goûts. J'utilise une indentation de quatre espaces dans les projets Android, et de deux espaces dans les projets iOS et React. Dans cette application Recettes, je suis une indentation cohérente et facile à comprendre, dont j'ai parlé [ici](https://medium.com/fantageek/indenting-swift-code-a55b04cc3a64) et [ici](https://medium.com/fantageek/using-camelcase-for-abbreviations-232eb67d872).

#### Documentation

Un bon code doit s'expliquer clairement afin que vous n'ayez pas besoin d'écrire des commentaires. Si un morceau de code est difficile à comprendre, il est bon de faire une pause et de le refactoriser en quelques méthodes avec des noms descriptifs pour que le morceau de code soit plus clair à comprendre. Cependant, je trouve que documenter les classes et les méthodes est également bon pour vos collègues et pour vous-même dans le futur. Selon les [directives de conception d'API Swift](https://swift.org/documentation/api-design-guidelines/),

**Écrivez un commentaire de documentation** pour chaque déclaration. Les informations obtenues en écrivant de la documentation peuvent avoir un impact profond sur votre conception, alors ne le remettez pas à plus tard.

Il est très facile de générer un modèle de commentaire `///` dans Xcode avec `Cmd+Alt+/`. Si vous prévoyez de refactoriser votre code en un framework pour le partager avec d'autres à l'avenir, des outils comme [jazzy](https://github.com/realm/jazzy) peuvent générer de la documentation pour que d'autres personnes puissent suivre.

#### Marquage des sections de code

L'utilisation de `MARK` peut être utile pour séparer les sections de code. Cela regroupe également les fonctions de manière agréable dans la barre de navigation. Vous pouvez également utiliser des groupes `extension`, des propriétés et des méthodes liées.

![Image](https://cdn-media-1.freecodecamp.org/images/BgVq-GPtOjMJXRMSkNZg-2ll67zrwiWKhjeA)

Pour un simple `UIViewController`, nous pouvons définir les MARK suivants :

```
// MARK: - Init
// MARK: - Cycle de vie de la vue
// MARK: - Configuration
// MARK: - Action
// MARK: - Données
```

#### Contrôle de source

Git est un système de contrôle de source populaire en ce moment. Nous pouvons utiliser le fichier modèle `.gitignore` de [gitignore.io/api/swift](https://www.gitignore.io/api/swift). Il y a des avantages et des inconvénients à [vérifier les dépendances](https://guides.cocoapods.org/using/using-cocoapods#should-i-check-the-pods-directory-into-source-control) (CocoaPods et Carthage). Cela dépend de votre projet, mais je tends à ne pas commiter les dépendances (node_modules, Carthage, Pods) dans le contrôle de source pour ne pas encombrer la base de code. Cela facilite également la révision des demandes de tirage.

Que vous vérifiiez ou non le répertoire Pods, le Podfile et Podfile.lock doivent **toujours** être conservés sous contrôle de version.

J'utilise à la fois iTerm2 pour exécuter des commandes et [Source Tree](https://www.sourcetreeapp.com/) pour visualiser les branches et la mise en scène.

#### Dépendances

J'ai utilisé des frameworks tiers, et j'ai également créé et contribué à de nombreux [open source](https://github.com/onmyway133/blog/issues/5). Utiliser un [framework](https://github.com/onmyway133/blog/issues/105) vous donne un [coup de pouce](https://github.com/onmyway133/blog/issues/85) au début, mais cela peut également vous limiter beaucoup à l'avenir. Il peut y avoir des changements triviaux qui sont très difficiles à contourner. La même chose se produit lors de l'utilisation de [SDK](https://medium.com/fantageek/dear-sdk-developers-d8e1434fb702). Ma préférence est de choisir des frameworks open source actifs. Lisez le code source et vérifiez les frameworks soigneusement, et consultez votre équipe si vous prévoyez de les utiliser. Un peu de prudence supplémentaire ne fait pas de mal.

Dans cette application, j'essaie d'utiliser le moins de dépendances possible. Juste assez pour démontrer comment gérer les dépendances. Certains développeurs expérimentés peuvent préférer [Carthage](https://github.com/Carthage/Carthage), un gestionnaire de dépendances car il vous donne un contrôle complet. Ici, je choisis [CocoaPods](https://github.com/CocoaPods/CocoaPods) car il est facile à utiliser et il a bien fonctionné jusqu'à présent.

Il y a un fichier appelé `.swift-version` de valeur `4.1` à la racine du projet pour indiquer à CocoaPods que ce projet utilise Swift 4.1. Cela semble simple mais m'a pris un certain temps à comprendre. ☔️

### Se lancer dans le projet

Créons quelques images de lancement et icônes pour donner au projet un bel aspect.

#### API

La manière facile d'apprendre le réseau iOS est à travers les services API publics gratuits. Ici, j'utilise food2fork. Vous pouvez vous inscrire pour un compte sur [http://food2fork.com/about/api](http://food2fork.com/about/api). Il y a beaucoup d'autres API géniales dans ce [dépôt public-api](https://github.com/toddmotto/public-apis).

Il est bon de garder vos identifiants dans un endroit sûr. J'utilise [1Password](https://1password.com/) pour générer et stocker mes mots de passe.

Avant de commencer à coder, jouons avec les API pour voir quels types de requêtes elles nécessitent et quelles réponses elles retournent. J'utilise l'outil [Insomnia](https://github.com/getinsomnia/insomnia) pour tester et analyser les réponses de l'API. Il est open source, gratuit et fonctionne très bien. 👍

![Image](https://cdn-media-1.freecodecamp.org/images/zAEUTPlfJFNsxOmtiHZJMqZgoFgCZKwVrIKU)

#### Écran de lancement

La première impression est importante, tout comme l'écran de lancement. La méthode préférée est d'utiliser `LaunchScreen.storyboard` au lieu d'une image de lancement statique.

Pour ajouter une image de lancement à `Asset Catalog`, ouvrez `LaunchScreen.storyboard`, ajoutez `UIImageView`, et épinglez-la aux bords de `UIView`. Nous ne devons pas épingler l'image à la zone de sécurité car nous voulons que l'image soit en plein écran. De plus, désélectionnez toutes les marges dans les contraintes Auto Layout. Définissez le `contentMode` de `UIImageView` sur `Aspect Fill` pour qu'il s'étire avec le bon ratio d'aspect.

![Image](https://cdn-media-1.freecodecamp.org/images/KKBkLUVqo3tKUERh-Dh6uuI9qmN0tPK7eXdC)
_Configurer la mise en page dans LaunchScreen._

#### Icône de l'application

Une bonne pratique consiste à fournir toutes les icônes d'application nécessaires pour chaque appareil que vous supportez, ainsi que pour des endroits comme les notifications, les paramètres et le Springboard. Assurez-vous que chaque image n'a pas de pixels transparents, sinon cela entraîne un fond noir. Ce conseil provient des [Directives de l'interface humaine - Icône de l'application](https://developer.apple.com/ios/human-interface-guidelines/icons-and-images/app-icon/).

**Gardez le fond simple et évitez la transparence**. Assurez-vous que votre icône est opaque et ne surchargez pas le fond. Donnez-lui un fond simple pour qu'il ne domine pas les autres icônes d'application à proximité. Vous n'avez pas besoin de remplir toute l'icône avec du contenu.

Nous devons concevoir des images carrées d'une taille supérieure à 1024 x 1024 pour que chacune puisse être réduite à des images plus petites. Vous pouvez le faire à la main, par script, ou utiliser cette petite [application IconGenerator](https://github.com/onmyway133/IconGenerator) que j'ai créée.

L'application IconGenerator peut générer des icônes pour iOS dans les applications iPhone, iPad, macOS et watchOS. Le résultat est le `AppIcon.appiconset` que nous pouvons glisser directement dans le catalogue d'actifs. Le catalogue d'actifs est la voie à suivre pour les projets Xcode modernes.

![Image](https://cdn-media-1.freecodecamp.org/images/miW2ny6NSc5Rh14PN1vSFrJgcfA--A9NIxV1)

#### Linting du code avec SwiftLint

Quelle que soit la plateforme sur laquelle nous développons, il est bon d'avoir un linter pour imposer des conventions cohérentes. L'outil le plus populaire pour les projets Swift est [SwiftLint](https://github.com/realm/SwiftLint), créé par les gens formidables de [Realm](https://realm.io/).

Pour l'installer, ajoutez `pod 'SwiftLint', '~> 0.25'` au Podfile. Il est également bon de spécifier la version des dépendances afin que `pod install` ne mette pas accidentellement à jour vers une version majeure qui pourrait casser votre application. Ensuite, ajoutez un fichier `.swiftlint.yml` avec votre configuration préférée. Une configuration d'exemple peut être trouvée [ici](https://github.com/realm/SwiftLint/blob/master/.swiftlint.yml).

Enfin, ajoutez une nouvelle phrase de script d'exécution pour exécuter `swiftlint` après la compilation.

![Image](https://cdn-media-1.freecodecamp.org/images/Z9PauRTgd0wFKxobzksYu16UqLoqeTKuOOAW)

#### Ressources typées

J'utilise [R.swift](https://github.com/mac-cain13/R.swift) pour gérer les ressources de manière sécurisée. Il peut générer des classes typées pour accéder aux polices, aux chaînes localisables et aux couleurs. Chaque fois que nous changeons les noms de fichiers de ressources, nous obtenons des erreurs de compilation au lieu d'un crash implicite. Cela nous empêche d'interférer avec les ressources qui sont activement utilisées.

```swift
imageView.image = R.image.notFound()
```

### Montrez-moi le code

Plongeons dans le code, en commençant par le modèle, les contrôleurs de flux et les classes de service.

#### Conception du modèle

Cela peut sembler ennuyeux, mais les clients sont simplement une manière plus joli de représenter la réponse de l'API. Le modèle est peut-être la chose la plus basique et nous l'utilisons beaucoup dans l'application. Il joue un rôle si important, mais il peut y avoir des bugs évidents liés à des modèles mal formés et à des hypothèses sur la manière dont un modèle doit être analysé qui doivent être considérés.

Nous devons tester chaque modèle de l'application. Idéalement, nous avons besoin de tests automatisés des modèles à partir des réponses de l'API au cas où le modèle aurait changé du backend.

À partir de Swift 4.0, nous pouvons faire en sorte que notre modèle se conforme à [Codable](https://developer.apple.com/documentation/swift/codable) pour le sérialiser facilement vers et depuis JSON. Notre modèle doit être immuable :

```swift
struct Recipe: Codable {
  let publisher: String
  let url: URL
  let sourceUrl: String
  let id: String
  let title: String
  let imageUrl: String
  let socialRank: Double
  let publisherUrl: URL

enum CodingKeys: String, CodingKey {
    case publisher
    case url = "f2f_url"
    case sourceUrl = "source_url"
    case id = "recipe_id"
    case title
    case imageUrl = "image_url"
    case socialRank = "social_rank"
    case publisherUrl = "publisher_url"
  }
}
```

Nous pouvons utiliser certains frameworks de test si vous aimez la syntaxe fantaisiste ou un style RSpec. Certains frameworks de test tiers peuvent avoir des problèmes. Je trouve que `XCTest` est suffisamment bon.

```swift
import XCTest
@testable import Recipes

class RecipesTests: XCTestCase {
  func testParsing() throws {
    let json: [String: Any] = [
      "publisher": "Two Peas and Their Pod",
      "f2f_url": "http://food2fork.com/view/975e33",
      "title": "No-Bake Chocolate Peanut Butter Pretzel Cookies",
      "source_url": "http://www.twopeasandtheirpod.com/no-bake-chocolate-peanut-butter-pretzel-cookies/",
      "recipe_id": "975e33",
      "image_url": "http://static.food2fork.com/NoBakeChocolatePeanutButterPretzelCookies44147.jpg",
      "social_rank": 99.99999999999974,
      "publisher_url": "http://www.twopeasandtheirpod.com"
    ]

let data = try JSONSerialization.data(withJSONObject: json, options: [])
    let decoder = JSONDecoder()
    let recipe = try decoder.decode(Recipe.self, from: data)

XCTAssertEqual(recipe.title, "No-Bake Chocolate Peanut Butter Pretzel Cookies")
    XCTAssertEqual(recipe.id, "975e33")
    XCTAssertEqual(recipe.url, URL(string: "http://food2fork.com/view/975e33")!)
  }
}
```

#### Meilleure navigation avec FlowController

Auparavant, j'utilisais [Compass](https://github.com/hyperoslo/Compass) comme [moteur de routage](https://medium.com/flawless-app-stories/url-routing-with-compass-d59c0061e7e2) dans mes projets, mais avec le temps, j'ai découvert que l'écriture de code de routage simple fonctionne également.

Le FlowController est utilisé pour gérer de nombreux composants liés à `UIViewController` pour une fonctionnalité commune. Vous pouvez lire [FlowController et Coordinator](https://github.com/onmyway133/blog/issues/106) pour d'autres cas d'utilisation et pour mieux comprendre.

Il y a le `AppFlowController` qui gère le changement de `rootViewController`. Pour l'instant, il démarre le `RecipeFlowController`.

```swift
window = UIWindow(frame: UIScreen.main.bounds)
window?.rootViewController = appFlowController
window?.makeKeyAndVisible()
appFlowController.start()
```

`RecipeFlowController` gère (en fait, il est) le `UINavigationController`, qui gère le push de `HomeViewController, RecipesDetailViewController, SafariViewController`.

```swift
final class RecipeFlowController: UINavigationController {
  /// Démarrer le flux
  func start() {
    let service = RecipesService(networking: NetworkService())
    let controller = HomeViewController(recipesService: service)
    viewControllers = [controller]
    controller.select = { [weak self] recipe in
      self?.startDetail(recipe: recipe)
    }
  }

private func startDetail(recipe: Recipe) {}
  private func startWeb(url: URL) {}
}
```

Le `UIViewController` peut utiliser `delegate` ou `closure` pour notifier `FlowController` des changements ou des prochains écrans dans le flux. Pour `delegate`, il peut y avoir besoin de vérifier lorsqu'il y a **deux** instances de la même classe. Ici, nous utilisons `closure` pour la simplicité.

#### Auto Layout

Auto Layout existe depuis iOS 5, il s'améliore chaque année. Bien que certaines personnes aient encore des problèmes avec lui, principalement à cause de contraintes de rupture confuses et de performances, mais personnellement, je trouve Auto Layout suffisamment bon.

J'essaie d'utiliser Auto Layout autant que possible pour créer une interface utilisateur adaptative. Nous pouvons utiliser des bibliothèques comme [Anchors](https://github.com/onmyway133/Anchors) pour faire de l'Auto Layout déclaratif et rapide. Cependant, dans cette application, nous allons simplement utiliser `NSLayoutAnchor` puisque c'est depuis iOS 9. Le code ci-dessous est inspiré de [Constrain](https://github.com/hyperoslo/Sugar/blob/master/Sources/iOS/Constraint.swift)t. N'oubliez pas que Auto Layout dans sa forme la plus simple implique de basculer `translatesAutoresizingMaskIntoConstraints` et d'activer les contraintes `isActive`.

```swift
extension NSLayoutConstraint {
  static func activate(_ constraints: [NSLayoutConstraint]) {
    constraints.forEach {
      ($0.firstItem as? UIView)?.translatesAutoresizingMaskIntoConstraints = false
      $0.isActive = true
    }
  }
}
```

Il existe en fait de nombreux autres moteurs de mise en page disponibles sur GitHub. Pour avoir une idée de celui qui serait adapté à utiliser, consultez le [LayoutFrameworkBenchmark](https://github.com/layoutBox/LayoutFrameworkBenchmark).

![Image](https://cdn-media-1.freecodecamp.org/images/r93zQ6c6e1t6m7zVN8OUX5j5DlrkvNJNXWWJ)

#### Architecture

L'architecture est probablement le sujet le plus médiatisé et discuté. Je suis un fan de l'exploration des architectures, vous pouvez voir plus de publications et de frameworks sur différentes architectures [ici](https://github.com/onmyway133/fantastic-ios-architecture).

Pour moi, toutes les architectures et les modèles définissent les rôles de chaque objet et comment les connecter. N'oubliez pas ces principes directeurs pour votre choix d'architecture :

* encapsuler ce qui varie
* favoriser la composition sur l'héritage
* programmer vers une interface, pas vers une implémentation

Après avoir joué avec de nombreuses architectures différentes, avec et sans Rx, j'ai découvert que le simple MVC est suffisamment bon. Dans ce projet simple, il y a juste `UIViewController` avec la logique encapsulée dans des classes d'assistance `Service`,

#### Massive View Controller

Vous avez peut-être entendu des gens plaisanter sur la taille massive de `UIViewController`, mais en réalité, il n'y a pas de contrôleur de vue massif. Ce sont simplement nous qui écrivons du mauvais code. Cependant, il existe des moyens de [l'alléger](http://khanlou.com/2014/09/8-patterns-to-help-you-destroy-massive-view-controller/).

Dans l'application de recettes que j'utilise,

* `Service` à injecter dans le contrôleur de vue pour effectuer une seule tâche
* `Vue générique` pour déplacer la déclaration de vue et de contrôles vers la couche `Vue`
* `Contrôleur de vue enfant` pour composer des contrôleurs de vue enfants pour construire plus de fonctionnalités

[Voici](http://khanlou.com/2014/09/8-patterns-to-help-you-destroy-massive-view-controller/) un très bon article avec 8 conseils pour alléger les gros contrôleurs.

#### Contrôle d'accès

La documentation SWIFT [documentation](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html) mentionne que « le contrôle d'accès restreint l'accès à certaines parties de votre code à partir du code dans d'autres fichiers sources et modules. Cette fonctionnalité vous permet de masquer les détails d'implémentation de votre code, et de spécifier une interface préférée à travers laquelle ce code peut être accédé et utilisé. »

Tout devrait être `private` et `final` par défaut. Cela aide également le [compilateur](https://developer.apple.com/swift/blog/?id=27). Lorsqu'on voit une propriété publique, nous devons la rechercher dans tout le projet avant de faire quoi que ce soit de plus avec elle. Si la propriété est utilisée uniquement dans une `classe`, la rendre `private` signifie que nous n'avons pas besoin de nous soucier si elle se casse ailleurs.

Déclarez les propriétés comme `final` lorsque cela est possible.

```swift
final class HomeViewController: UIViewController {}
```

Déclarez les propriétés comme `private` ou au moins `private(set)`.

```swift
final class RecipeDetailView: UIView {
  private let scrollableView = ScrollableView()
  private(set) lazy var imageView: UIImageView = self.makeImageView()
}
```

#### Propriétés paresseuses

Pour les propriétés qui peuvent être accédées à un moment ultérieur, nous pouvons les déclarer comme `lazy` et pouvons utiliser `closure` pour une construction rapide.

```swift
final class RecipeCell: UICollectionViewCell {
  private(set) lazy var containerView: UIView = {
    let view = UIView()
    view.clipsToBounds = true
    view.layer.cornerRadius = 5
    view.backgroundColor = Color.main.withAlphaComponent(0.4)

return view
  }()
}
```

Nous pouvons également utiliser des fonctions `make` si nous prévoyons de réutiliser la même fonction pour plusieurs propriétés.

```swift
final class RecipeDetailView: UIView {
  private(set) lazy var imageView: UIImageView = self.makeImageView()

private func makeImageView() -> UIImageView {
    let imageView = UIImageView()
    imageView.contentMode = .scaleAspectFill
    imageView.clipsToBounds = true
    return imageView
  }
}
```

Cela correspond également aux conseils de [Strive for Fluent Usage](https://swift.org/documentation/api-design-guidelines/).

Commencez les noms des méthodes de fabrication par « make », par exemple, `x.makeIterator()`.

#### Extraits de code

Certaines syntaxes de code sont difficiles à retenir. Envisagez d'utiliser des extraits de code pour générer automatiquement du code. Cela est pris en charge par Xcode et est la méthode préférée par les ingénieurs Apple lorsqu'ils font des démonstrations.

```swift
if #available(iOS 11, *) {
  viewController.navigationItem.searchController = searchController
  viewController.navigationItem.hidesSearchBarWhenScrolling = false
} else {
  viewController.navigationItem.titleView = searchController.searchBar
}
```

J'ai créé un [dépôt](https://github.com/hyperoslo/SwiftSnippets) avec quelques extraits Swift utiles que beaucoup apprécient utiliser.

#### Réseautage

Le réseautage en Swift est un problème résolu. Il y a des tâches fastidieuses et sujettes aux erreurs comme l'analyse des réponses HTTP, la gestion des files d'attente de requêtes, la gestion des requêtes de paramètres. J'ai vu des bugs sur les requêtes PATCH, les [méthodes HTTP en minuscules](https://github.com/onmyway133/blog/issues/115), … Nous pouvons simplement utiliser [Alamofire](https://github.com/Alamofire/Alamofire). Il n'y a pas besoin de perdre du temps ici.

Pour cette application, puisque c'est simple et pour éviter des dépendances inutiles. Nous pouvons simplement utiliser `URLSession` directement. Une ressource contient généralement une URL, un chemin, des paramètres et la méthode HTTP.

```swift
struct Resource {
  let url: URL
  let path: String?
  let httpMethod: String
  let parameters: [String: String]
}
```

Un service réseau simple peut simplement analyser `Resource` en `URLRequest` et dire à `URLSession` de l'exécuter

```swift
final class NetworkService: Networking {
  @discardableResult func fetch(resource: Resource, completion: @escaping (Data?) -> Void) -> URLSessionTask? {
    guard let request = makeRequest(resource: resource) else {
      completion(nil)
      return nil
    }

let task = session.dataTask(with: request, completionHandler: { data, _, error in
      guard let data = data, error == nil else {
        completion(nil)
        return
      }

completion(data)
    })

task.resume()
    return task
  }
}
```

Utilisez l'injection de dépendances. Permettez à l'appelant de spécifier `URLSessionConfiguration`. Ici, nous utilisons le paramètre par défaut de Swift pour fournir l'option la plus courante.

```swift
init(configuration: URLSessionConfiguration = URLSessionConfiguration.default) {
  self.session = URLSession(configuration: configuration)
}
```

J'utilise également [URLQueryItem](https://developer.apple.com/documentation/foundation/urlqueryitem) qui était disponible depuis iOS 8. Cela rend l'analyse des paramètres en éléments de requête plus agréable et moins fastidieuse.

#### Comment tester le code de réseautage

Nous pouvons utiliser [URLProtocol](https://developer.apple.com/documentation/foundation/urlprotocol) et [URLCache](https://developer.apple.com/documentation/foundation/urlcache) pour ajouter un stub pour les réponses réseau ou nous pouvons utiliser des frameworks comme [Mockingjay](https://github.com/kylef/Mockingjay) qui swizzle `URLSessionConfiguration`.

Je préfère utiliser le protocole pour tester. En utilisant le protocole, le test peut créer une requête mock pour fournir une réponse stub.

```swift
protocol Networking {
  @discardableResult func fetch(resource: Resource, completion: @escaping (Data?) -> Void) -> URLSessionTask?
}

final class MockNetworkService: Networking {
  let data: Data
  init(fileName: String) {
    let bundle = Bundle(for: MockNetworkService.self)
    let url = bundle.url(forResource: fileName, withExtension: "json")!
    self.data = try! Data(contentsOf: url)
  }

func fetch(resource: Resource, completion: @escaping (Data?) -> Void) -> URLSessionTask? {
    completion(data)
    return nil
  }
}
```

#### Implémentation du cache pour le support hors ligne

J'ai contribué et utilisé une bibliothèque appelée [Cache](https://github.com/hyperoslo/Cache) beaucoup. Ce dont nous avons besoin d'une bonne bibliothèque de cache est le cache mémoire et disque, la mémoire pour un accès rapide, le disque pour la persistance. Lorsque nous sauvegardons, nous sauvegardons à la fois en mémoire et sur disque. Lorsque nous chargeons, si le cache mémoire échoue, nous chargeons depuis le disque, puis nous mettons à jour la mémoire à nouveau. Il existe de nombreux sujets avancés sur le cache comme la purge, l'expiration, la fréquence d'accès. Lisez à leur sujet [ici](https://medium.com/hyperoslo/open-source-stories-from-cachable-to-generic-storage-in-cache-418d9a230d51).

Dans cette application simple, une classe de service de cache maison est suffisante et une bonne façon d'apprendre comment fonctionne le cache. Tout en Swift peut être converti en `Data`, donc nous pouvons simplement sauvegarder `Data` dans le cache. Swift 4 `Codable` peut sérialiser l'objet en `Data`.

Le code ci-dessous nous montre comment utiliser `FileManager` pour le cache disque.

```swift
/// Sauvegarder et charger des données en mémoire et en cache disque
final class CacheService {

/// Pour obtenir ou charger des données en mémoire
  private let memory = NSCache<NSString, NSData>()

/// L'URL du chemin qui contient les fichiers mis en cache (fichiers mp3 et fichiers image)
  private let diskPath: URL

/// Pour vérifier si un fichier ou un répertoire existe dans un chemin spécifié
  private let fileManager: FileManager

/// Assurez-vous que toutes les opérations sont exécutées en série
  private let serialQueue = DispatchQueue(label: "Recipes")

init(fileManager: FileManager = FileManager.default) {
    self.fileManager = fileManager
    do {
      let documentDirectory = try fileManager.url(
        for: .documentDirectory,
        in: .userDomainMask,
        appropriateFor: nil,
        create: true
      )
      diskPath = documentDirectory.appendingPathComponent("Recipes")
      try createDirectoryIfNeeded()
    } catch {
      fatalError()
    }
  }

func save(data: Data, key: String, completion: (() -> Void)? = nil) {
    let key = MD5(key)

serialQueue.async {
      self.memory.setObject(data as NSData, forKey: key as NSString)
      do {
        try data.write(to: self.filePath(key: key))
        completion?()
      } catch {
        print(error)
      }
    }
  }
}
```

Pour éviter les noms de fichiers mal formés et très longs, nous pouvons les hacher. J'utilise MD5 de [SwiftHash](https://github.com/onmyway133/SwiftHash), qui offre une utilisation très simple `let key = MD5(key)`.

#### Comment tester le Cache

Puisque je conçois les opérations `Cache` pour être asynchrones, nous devons utiliser `test expectation`. N'oubliez pas de réinitialiser l'état avant chaque test afin que l'état du test précédent n'interfère pas avec le test actuel. L'`expectation` dans `XCTestCase` rend le test du code asynchrone plus facile que jamais 👍

```swift
class CacheServiceTests: XCTestCase {
  let service = CacheService()

override func setUp() {
    super.setUp()

try? service.clear()
  }

func testClear() {
    let expectation = self.expectation(description: #function)
    let string = "Hello world"
    let data = string.data(using: .utf8)!

service.save(data: data, key: "key", completion: {
      try? self.service.clear()
      self.service.load(key: "key", completion: {
        XCTAssertNil($0)
        expectation.fulfill()
      })
    })

wait(for: [expectation], timeout: 1)
  }
}
```

#### Chargement d'images distantes

Je contribue également à [Imaginary](https://github.com/hyperoslo/Imaginary), donc je connais un peu son fonctionnement. Pour les images distantes, nous devons les télécharger et les mettre en cache, et la clé de cache est généralement l'URL de l'image distante.

Dans notre application de recettes, construisons un simple ImageService basé sur notre `NetworkService` et `CacheService`. En fait, une image est simplement une ressource réseau que nous téléchargeons et mettons en cache. Nous préférons la composition, donc nous inclurons `NetworkService` et `CacheService` dans `ImageService`.

```swift
/// Vérifier le cache local et récupérer l'image distante
final class ImageService {

private let networkService: Networking
  private let cacheService: CacheService
  private var task: URLSessionTask?

init(networkService: Networking, cacheService: CacheService) {
    self.networkService = networkService
    self.cacheService = cacheService
  }
}
```

Nous avons généralement des cellules `UICollectionView` et `UITableView` avec `UIImageView`. Et puisque les cellules sont réutilisées, nous devons annuler toute `tâche de requête` existante avant de faire une nouvelle requête.

```swift
func fetch(url: URL, completion: @escaping (UIImage?) -> Void) {
  // Annuler la tâche existante si elle existe
  task?.cancel()

// Essayer de charger depuis le cache
  cacheService.load(key: url.absoluteString, completion: { [weak self] cachedData in
    if let data = cachedData, let image = UIImage(data: data) {
      DispatchQueue.main.async {
        completion(image)
      }
    } else {
      // Essayer de demander depuis le réseau
      let resource = Resource(url: url)
      self?.task = self?.networkService.fetch(resource: resource, completion: { networkData in
        if let data = networkData, let image = UIImage(data: data) {
          // Sauvegarder dans le cache
          self?.cacheService.save(data: data, key: url.absoluteString)
          DispatchQueue.main.async {
            completion(image)
          }
        } else {
          print("Erreur de chargement de l'image à \(url)")
        }
      })

self?.task?.resume()
    }
  })
}
```

#### Rendre le chargement des images plus pratique pour UIImageView

Ajoutons une extension à `UIImageView` pour définir l'image distante à partir de l'URL. J'utilise `associated object` pour conserver ce `ImageService` et pour annuler les anciennes requêtes. Nous faisons bon usage de `associated object` pour attacher `ImageService` à `UIImageView`. Le but est d'annuler la requête actuelle lorsque la requête est déclenchée à nouveau. Cela est pratique lorsque les vues d'image sont rendues dans une liste déroulante.

```swift
extension UIImageView {
  func setImage(url: URL, placeholder: UIImage? = nil) {
    if imageService == nil {
      imageService = ImageService(networkService: NetworkService(), cacheService: CacheService())
    }

self.image = placeholder
    self.imageService?.fetch(url: url, completion: { [weak self] image in
      self?.image = image
    })
  }

private var imageService: ImageService? {
    get {
      return objc_getAssociatedObject(self, &AssociateKey.imageService) as? ImageService
    }
    set {
      objc_setAssociatedObject(
        self,
        &AssociateKey.imageService,
        newValue,
        objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC
      )
    }
  }
}
```

#### Source de données générique pour UITableView et UICollectionView

Nous utilisons `UITableView` et `UICollectionView` dans presque toutes les applications et nous effectuons presque toujours les mêmes choses de manière répétée.

* montrer le contrôle de rafraîchissement pendant le chargement
* recharger la liste en cas de données
* montrer l'erreur en cas d'échec.

Il existe de nombreux wrappers autour de `UITableView` et `UICollection`. Chacun ajoute une autre couche d'abstraction, ce qui nous donne plus de puissance mais applique des restrictions en même temps.

Dans cette application, j'utilise `Adapter` pour obtenir une source de données générique, pour créer une collection typée. Parce qu'au final, tout ce dont nous avons besoin est de mapper le modèle aux cellules.

J'utilise également [Upstream](https://github.com/hyperoslo/Upstream) basé sur cette idée. Il est difficile d'envelopper `UITableView` et `UICollectionView`, car de nombreuses fois, c'est spécifique à l'application, donc un wrapper mince comme `Adapter` est suffisant.

```swift
final class Adapter<T, Cell: UICollectionViewCell>: NSObject,
UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
  var items: [T] = []
  var configure: ((T, Cell) -> Void)?
  var select: ((T) -> Void)?
  var cellHeight: CGFloat = 60
}
```

#### Contrôleur et Vue

J'ai abandonné Storyboard à cause de nombreuses limitations et de nombreux problèmes. Au lieu de cela, j'utilise du code pour créer des vues et définir des contraintes. Ce n'est pas si difficile à suivre. La plupart du code boilerplate dans `UIViewController` est pour créer des vues et configurer la mise en page. Déplaçons ceux-ci vers la vue. Vous pouvez en lire plus à ce sujet [ici](https://github.com/onmyway133/blog/issues/37).

```swift
/// Utilisé pour séparer le contrôleur et la vue
class BaseController<T: UIView>: UIViewController {
  let root = T()

override func loadView() {
    view = root
  }
}

final class RecipeDetailViewController: BaseController<RecipeDetailView> {}
```

#### Gestion des responsabilités avec un contrôleur de vue enfant

Le conteneur de contrôleur de vue est un concept puissant. Chaque contrôleur de vue a une séparation des préoccupations et peut être composé ensemble pour créer des fonctionnalités avancées. J'ai utilisé `RecipeListViewController` pour gérer le `UICollectionView` et afficher une liste de recettes.

```swift
final class RecipeListViewController: UIViewController {
  private(set) var collectionView: UICollectionView!
  let adapter = Adapter<Recipe, RecipeCell>()
  private let emptyView = EmptyView(text: "No recipes found!")
}
```

Il y a le `HomeViewController` qui intègre ce `RecipeListViewController`

```swift
/// Afficher une liste de recettes
final class HomeViewController: UIViewController {

/// Lorsqu'une recette est sélectionnée
  var select: ((Recipe) -> Void)?

private var refreshControl = UIRefreshControl()
  private let recipesService: RecipesService
  private let searchComponent: SearchComponent
  private let recipeListViewController = RecipeListViewController()
}

```

#### Composition et Injection de Dépendances

J'essaie de construire des composants et de composer du code chaque fois que je le peux. Nous voyons que `ImageService` utilise `NetworkService` et `CacheService`, et que `RecipeDetailViewController` utilise `Recipe` et `RecipesService`.

Idéalement, les objets ne devraient pas créer de dépendances par eux-mêmes. Les dépendances devraient être créées à l'extérieur et transmises depuis la [racine](http://blog.ploeh.dk/2011/07/28/CompositionRoot/). Dans notre application, la racine est `AppDelegate` et `AppFlowController`, donc les dépendances devraient commencer à partir de là.

#### Sécurité du Transport des Applications

![Image](https://cdn-media-1.freecodecamp.org/images/r5BOdarxvcEd-ePhEgAzdKOp42u1SXIMPK01)

Depuis iOS 9, toutes les applications doivent adopter la [Sécurité du Transport des Applications](https://developer.apple.com/library/content/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html)

> _La Sécurité du Transport des Applications (ATS) impose les meilleures pratiques dans les connexions sécurisées entre une application et son backend. ATS empêche la divulgation accidentelle, fournit un comportement sécurisé par défaut et est facile à adopter ; elle est également activée par défaut dans iOS 9 et OS X v10.11. Vous devez adopter ATS dès que possible, que vous créiez une nouvelle application ou que vous mettiez à jour une application existante._

Dans notre application, certaines images sont obtenues via une connexion `HTTP`. Nous devons l'exclure de la règle de sécurité, mais uniquement pour ce domaine.

```
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSExceptionDomains</key>
  <dict>
    <key>food2fork.com</key>
    <dict>
      <key>NSIncludesSubdomains</key>
      <true/>
      <key>NSExceptionAllowsInsecureHTTPLoads</key>
      <true/>
    </dict>
  </dict>
</dict>
```

#### Une vue Scrollable personnalisée

Pour l'écran de détail, nous pouvons utiliser `UITableView` et `UICollectionView` avec différents types de cellules. Ici, les vues doivent être statiques. Nous pouvons les empiler en utilisant `UIStackView`. Pour plus de flexibilité, nous pouvons simplement utiliser `UIScrollView`.

```swift
/// Disposition verticale de la vue en utilisant Auto Layout dans UIScrollView
final class ScrollableView: UIView {
  private let scrollView = UIScrollView()
  private let contentView = UIView()

override init(frame: CGRect) {
    super.init(frame: frame)

scrollView.showsHorizontalScrollIndicator = false
    scrollView.alwaysBounceHorizontal = false
    addSubview(scrollView)

scrollView.addSubview(contentView)

NSLayoutConstraint.activate([
      scrollView.topAnchor.constraint(equalTo: topAnchor),
      scrollView.bottomAnchor.constraint(equalTo: bottomAnchor),
      scrollView.leftAnchor.constraint(equalTo: leftAnchor),
      scrollView.rightAnchor.constraint(equalTo: rightAnchor),

contentView.topAnchor.constraint(equalTo: scrollView.topAnchor),
      contentView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
      contentView.leftAnchor.constraint(equalTo: leftAnchor),
      contentView.rightAnchor.constraint(equalTo: rightAnchor)
    ])
  }
}
```

Nous épinglons le `UIScrollView` aux bords. Nous épinglons l'ancre gauche et droite de `contentView` à `self`, tout en épinglant l'ancre supérieure et inférieure de `contentView` à `UIScrollView`.

Les vues à l'intérieur de `contentView` ont des contraintes supérieures et inférieures, donc lorsqu'elles s'étendent, elles étendent également `contentView`. `UIScrollView` utilise les informations Auto Layout de ce `contentView` pour déterminer sa `contentSize`. Voici comment `ScrollableView` est utilisé dans `RecipeDetailView`.

```swift
scrollableView.setup(pairs: [
  ScrollableView.Pair(view: imageView, inset: UIEdgeInsets(top: 8, left: 0, bottom: 0, right: 0)),
  ScrollableView.Pair(view: ingredientHeaderView, inset: UIEdgeInsets(top: 8, left: 0, bottom: 0, right: 0)),
  ScrollableView.Pair(view: ingredientLabel, inset: UIEdgeInsets(top: 4, left: 8, bottom: 0, right: 0)),
  ScrollableView.Pair(view: infoHeaderView, inset: UIEdgeInsets(top: 4, left: 0, bottom: 0, right: 0)),
  ScrollableView.Pair(view: instructionButton, inset: UIEdgeInsets(top: 8, left: 20, bottom: 0, right: 20)),
  ScrollableView.Pair(view: originalButton, inset: UIEdgeInsets(top: 8, left: 20, bottom: 0, right: 20)),
  ScrollableView.Pair(view: infoView, inset: UIEdgeInsets(top: 16, left: 0, bottom: 20, right: 0))
])
```

#### Ajout de la fonctionnalité de recherche

À partir d'iOS 8, nous pouvons utiliser le [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller) pour obtenir une expérience de recherche par défaut avec la barre de recherche et le contrôleur de résultats. Nous encapsulerons la fonctionnalité de recherche dans `SearchComponent` afin qu'elle puisse être pluggable.

```swift
final class SearchComponent: NSObject, UISearchResultsUpdating, UISearchBarDelegate {
  let recipesService: RecipesService
  let searchController: UISearchController
  let recipeListViewController = RecipeListViewController()
}
```

À partir de [iOS 11](https://www.hackingwithswift.com/articles/5/how-to-adopt-ios-11-user-interface-changes-in-your-app), il y a une propriété appelée `searchController` sur `UINavigationItem` qui facilite l'affichage de la barre de recherche sur la barre de navigation.

```swift
func add(to viewController: UIViewController) {
  if #available(iOS 11, *) {
    viewController.navigationItem.searchController = searchController
    viewController.navigationItem.hidesSearchBarWhenScrolling = false
  } else {
    viewController.navigationItem.titleView = searchController.searchBar
  }

viewController.definesPresentationContext = true
}
```

Dans cette application, nous devons désactiver `hidesNavigationBarDuringPresentation` pour l'instant, car il est assez bogué. Espérons qu'il sera résolu dans les futures mises à jour d'iOS.

#### Comprendre le contexte de présentation

Comprendre le contexte de présentation est crucial pour la présentation du contrôleur de vue. Dans la recherche, nous utilisons le `searchResultsController`.

```swift
self.searchController = UISearchController(searchResultsController: recipeListViewController)
```

Nous devons utiliser [definesPresentationContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621456-definespresentationcontext) sur le contrôleur de vue source (le contrôleur de vue où nous ajoutons la barre de recherche). Sans cela, nous obtenons le `searchResultsController` présenté en plein écran !!!

> _Lors de l'utilisation du style currentContext ou overCurrentContext pour présenter un contrôleur de vue, cette propriété contrôle quel contrôleur de vue existant dans votre hiérarchie de contrôleurs de vue est réellement couvert par le nouveau contenu. Lorsqu'une présentation basée sur le contexte se produit, UIKit commence au contrôleur de vue présentateur et remonte la hiérarchie des contrôleurs de vue. Si elle trouve un contrôleur de vue dont la valeur de cette propriété est vraie, elle demande à ce contrôleur de vue de présenter le nouveau contrôleur de vue. Si aucun contrôleur de vue ne définit le contexte de présentation, UIKit demande au contrôleur de vue racine de la fenêtre de gérer la présentation._  
>   
> _La valeur par défaut de cette propriété est false. Certains contrôleurs de vue fournis par le système, comme UINavigationController, changent la valeur par défaut en true._

#### Débogage des actions de recherche

Nous ne devons pas exécuter de requêtes de recherche pour chaque frappe de l'utilisateur dans la barre de recherche. Par conséquent, un certain type de limitation est nécessaire. Nous pouvons utiliser `DispatchWorkItem` pour encapsuler l'action et l'envoyer à la file d'attente. Plus tard, nous pouvons l'annuler.

```swift
final class Debouncer {
  private let delay: TimeInterval
  private var workItem: DispatchWorkItem?

init(delay: TimeInterval) {
    self.delay = delay
  }

/// Déclencher l'action après un certain délai
  func schedule(action: @escaping () -> Void) {
    workItem?.cancel()
    workItem = DispatchWorkItem(block: action)
    DispatchQueue.main.asyncAfter(deadline: .now() + delay, execute: workItem!)
  }
}
```

#### Test du débogage avec l'attente inversée

Pour tester `Debouncer`, nous pouvons utiliser l'attente `XCTest` en mode [inversé](https://developer.apple.com/documentation/xctest/xctestexpectation/2806573-isinverted). Lisez-en plus à ce sujet dans [Unit testing asynchronous Swift code](https://www.swiftbysundell.com/posts/unit-testing-asynchronous-swift-code).

> _Pour vérifier qu'une situation ne se produit pas pendant le test, créez une attente qui est remplie lorsque la situation inattendue se produit, et définissez sa propriété isInverted sur true. Votre test échouera immédiatement si l'attente inversée est remplie._

```swift
class DebouncerTests: XCTestCase {
  func testDebouncing() {
    let cancelExpectation = self.expectation(description: "cancel")
    cancelExpectation.isInverted = true

let completeExpectation = self.expectation(description: "complete")
    let debouncer = Debouncer(delay: 0.3)

debouncer.schedule {
      cancelExpectation.fulfill()
    }

debouncer.schedule {
      completeExpectation.fulfill()
    }

wait(for: [cancelExpectation, completeExpectation], timeout: 1)
  }
}
```

#### Test de l'interface utilisateur avec UITests

Parfois, de petits refactorings peuvent avoir un grand effet. Un bouton désactivé peut entraîner des écrans inutilisables par la suite. UITest aide à garantir l'intégrité et les aspects fonctionnels de l'application. Le test doit être déclaratif. Nous pouvons utiliser le [modèle Robot](https://github.com/hyperoslo/tine-handel-ios/pull/318).

```swift
class RecipesUITests: XCTestCase {
  var app: XCUIApplication!

  override func setUp() {
    super.setUp()
    continueAfterFailure = false

    app = XCUIApplication()
  }

  func testScrolling() {
    app.launch()

    let collectionView = app.collectionViews.element(boundBy: 0)
    collectionView.swipeUp()
    collectionView.swipeUp()
  }

  func testGoToDetail() {
    app.launch()

    let collectionView = app.collectionViews.element(boundBy: 0)
    let firstCell = collectionView.cells.element(boundBy: 0)
    firstCell.tap()
  }
}
```

Voici quelques-uns de mes articles concernant les tests.

* [Exécuter des UITests avec la connexion Facebook dans iOS](https://hackernoon.com/running-uitests-with-facebook-login-in-ios-4ac998940c42)
* [Tester en Swift avec le modèle Given When Then](https://medium.com/fantageek/testing-in-swift-with-given-when-then-pattern-cd1a4e1737f9)

#### Garde du thread principal

Accéder à l'interface utilisateur depuis la file d'attente d'arrière-plan peut entraîner des problèmes potentiels. Auparavant, j'avais besoin d'utiliser [MainThreadGuard](https://github.com/onmyway133/MainThreadGuard), maintenant que Xcode 9 dispose de [Main Thread Checker](https://developer.apple.com/documentation/code_diagnostics/main_thread_checker), je l'ai simplement activé dans Xcode.

> _Le Main Thread Checker est un outil autonome pour les langages Swift et C qui détecte l'utilisation invalide d'AppKit, UIKit et d'autres API sur un thread d'arrière-plan. Mettre à jour l'interface utilisateur sur un thread autre que le thread principal est une erreur courante qui peut entraîner des mises à jour d'interface utilisateur manquantes, des défauts visuels, des corruptions de données et des plantages._

![Image](https://cdn-media-1.freecodecamp.org/images/4bc0GN3W1-qvXWACoymuVv7kg3wE6wsn0lZS)

#### Mesure des performances et des problèmes

Nous pouvons utiliser [Instruments](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html) pour profiler complètement l'application. Pour une mesure rapide, nous pouvons nous rendre dans l'onglet `Debug Navigator` et voir l'utilisation du CPU, de la mémoire et du réseau. Consultez [cet article cool](https://medium.com/@kazmiekr/what-every-ios-developer-should-be-doing-with-instruments-d1661eeaf64f) pour en savoir plus sur les instruments.

#### Prototypage avec Playground

Playground est la méthode recommandée pour prototyper et construire des applications. Lors de la WWDC 2018, Apple a introduit [Create ML](https://developer.apple.com/documentation/createml) qui supporte Playground pour entraîner des modèles. Consultez [cet article cool](https://medium.com/flawless-app-stories/playground-driven-development-in-swift-cf167489fe7b) pour en savoir plus sur le développement piloté par Playground en Swift.

### Où aller à partir de là

Merci d'être arrivé jusqu'ici. J'espère que vous avez appris quelque chose d'utile. La meilleure façon d'apprendre quelque chose est de simplement le faire. Si vous arrivez à écrire le même code encore et encore, faites-en un composant. Si un problème vous donne du fil à retordre, écrivez à ce sujet. Partagez votre expérience avec le monde, vous apprendrez beaucoup.

Je recommande de consulter l'article [Meilleurs endroits pour apprendre le développement iOS](https://medium.com/hyperoslo/best-places-to-learn-ios-development-85ebebe890cf) pour en savoir plus sur le développement iOS.

Si vous avez des questions, des commentaires ou des retours, n'oubliez pas de les ajouter dans les commentaires. Et si vous avez trouvé cet article utile, n'oubliez pas d'applaudir. 👏

Si vous aimez cet article, envisagez de visiter [mes autres articles](https://github.com/onmyway133/blog/issues/165) et [mes applications](https://onmyway133.github.io/) ❤️