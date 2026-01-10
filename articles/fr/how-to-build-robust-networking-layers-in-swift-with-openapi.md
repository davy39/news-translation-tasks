---
title: Comment construire des couches réseau robustes en Swift avec OpenAPI
subtitle: ''
author: Sravan Karuturi
co_authors: []
series: null
date: '2025-07-22T18:00:06.724Z'
originalURL: https://freecodecamp.org/news/how-to-build-robust-networking-layers-in-swift-with-openapi
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753206547489/dce9a849-1ccd-4cb0-bca8-f879a5aadf5f.png
tags:
- name: OpenApi
  slug: openapi
- name: Swift
  slug: swift
- name: openapi generator
  slug: openapi-generator
- name: OpenAPI Specification
  slug: openapi-specification
- name: SwiftUI
  slug: swiftui
seo_title: Comment construire des couches réseau robustes en Swift avec OpenAPI
seo_desc: 'What is the Problem We’re Solving?

  For many app developers, including me, writing the networking layer of an application
  is a familiar and tedious process. You write and test your first call and after
  that, it involves a repetitive cycle of tasks.

  Th...'
---

## **Quel est le problème que nous résolvons ?**

Pour de nombreux développeurs d'applications, y compris moi-même, l'écriture de la couche réseau d'une application est un processus familier et fastidieux. Vous écrivez et testez votre premier appel, puis cela implique un cycle répétitif de tâches.

Voici à quoi cela ressemblerait dans le cas de Swift :

1. Vous créez une instance `URLSession`.

2. Vous créez un objet `URLRequest`.

3. Vous créez les modèles `@Codable` pour correspondre à l'entrée et à la sortie attendues du serveur.

Vous effectuez les étapes ci-dessus pour chaque point de terminaison API que vous avez sur votre backend et que votre application utilise. Non seulement ce processus est chronophage et peu stimulant pour les développeurs, mais il est également sujet aux erreurs.

Dans le cas ci-dessus, si un changement mineur était apporté à l'API backend - peut-être un champ renommé ou une nouvelle propriété - cela pourrait entraîner la rupture de l'application. Mais vous ne le sauriez pas avant de l'avoir envoyé à l'assurance qualité ou, dans le pire des cas, à votre consommateur. C'est là que la spécification OpenAPI émerge comme une solution moderne et robuste.

Dans ce tutoriel, vous apprendrez ce qu'est OpenAPI et comment il peut aider à améliorer votre processus de développement. Après cela, nous implémenterons OpenAPI en créant une petite application SwiftUI et en utilisant les méthodologies OpenAPI pour interagir avec l'API `JSONPlaceholder`. Commençons.

## **À qui s'adresse ce guide ?**

Ce guide est destiné à la fois aux nouveaux développeurs recherchant les meilleures pratiques et aux développeurs expérimentés cherchant à implémenter ou à en apprendre davantage sur la spécification OpenAPI. Commençons.

## Table des matières

* [Qu'est-ce qu'OpenAPI et pourquoi devriez-vous vous en soucier ?](#heading-qu-est-ce-qu-openapi-et-pourquoi-devriez-vous-vous-en-soucier)

  * [Avantages pour les développeurs Swift (iOS)](#heading-avantages-pour-les-développeurs-swift-ios)

* [Un guide pratique pour implémenter cette solution](#heading-un-guide-pratique-pour-implémenter-cette-solution)

  * [Étape 1 : Créer un bon fichier openapi.yaml (la spécification)](#heading-étape-1-créer-un-bon-fichier-openapiyaml-la-spécification)

  * [Étape 2 : Configurer votre projet](#heading-étape-2-configurer-votre-projet)

  * [Étape 3 : Écrire un wrapper](#heading-étape-3-écrire-un-wrapper)

  * [Étape 4 : Appeler le wrapper et afficher les données](#heading-étape-4-appeler-le-wrapper-et-afficher-les-données)

* [Pièges potentiels](#heading-pièges-potentiels)

  * [Code généré verbeux ou laid](#heading-code-généré-verbeux-ou-laid)

  * [Spécifications volumineuses et problèmes de performance](#heading-spécifications-volumineuses-et-problèmes-de-performance)

  * [Fonctionnalités de spécification non supportées](#heading-fonctionnalités-de-spécification-non-supportées)

* [Conclusion : Adoptez le développement piloté par les spécifications](#heading-conclusion-adoptez-le-développement-piloté-par-les-spécifications)

## **Qu'est-ce qu'OpenAPI et pourquoi devriez-vous vous en soucier ?**

Au cœur, la spécification OpenAPI fournit une *interface standard et agnostique* pour décrire les API RESTful. Cette spécification, une fois remplie, permet aux humains et aux ordinateurs de découvrir et de comprendre les capacités d'un service sans avoir besoin d'accéder au code source ou aux requêtes réseau.

La puissance d'OpenAPI réside dans le fait qu'il agit comme un *contrat formel entre différentes parties du système*. Ce contrat aide à la fois les programmeurs frontend et backend en éliminant l'ambiguïté pendant le processus de conception. Cela a également l'avantage supplémentaire d'utiliser des générateurs de code pour générer du code boilerplate à la fois sur le backend et sur le client (ce que nous discuterons également aujourd'hui).

Traditionnellement, lorsque vous souhaitez créer une nouvelle API dans une équipe, soit le chef de projet, l'ingénieur frontend, soit l'ingénieur backend prend l'initiative de la demander. Ensuite, l'équipe backend la construit et la documente. Cela est ensuite utilisé par l'équipe frontend pour utiliser l'API.

`Un demandeur → Équipe backend → Documentation → Équipe frontend`

Si vous utilisez OpenAPI, lorsqu'une demande est faite pour une nouvelle API, elle est formalisée dans une spécification après des délibérations avec à la fois l'équipe frontend et l'équipe backend. Cela sert ensuite de source de vérité et est utilisé pour générer le code backend et frontend sans autant d'interdépendance.

`Un demandeur → Toutes les équipes → Spécification → Toutes les équipes.`

Cela non seulement rationalise le processus d'ajout de nouvelles API, mais fournit une source de vérité définitive pour chaque point de terminaison. Cela fait également en sorte que les ingénieurs frontend et backend ne soient pas désalignés sur un paramètre fourni dans le résultat étant un `Int` ou un `String`, etc. **Tout est dans la spécification.**

### **Avantages pour les développeurs Swift (iOS)**

L'adoption d'OpenAPI et de `swift-openapi-generator` apporte une multitude d'avantages tangibles au processus de développement Swift/App. Cela transforme la manière dont les applications interagissent avec les services web de plusieurs façons clés.

#### Réduction du temps et des coûts de développement

L'amélioration la plus immédiate que vous verrez est la réduction significative du code boilerplate que vous devez écrire. Le générateur automatise la création de ce que l'on appelle le code boilerplate ou le code cérémonial. Il s'agit de la logique répétitive pour les requêtes réseau, la gestion des réponses et les définitions de modèles de données.

En déléguant ce travail, les développeurs peuvent travailler sur les fonctionnalités principales de l'application, ce qui conduit à des cycles de développement plus rapides et plus intéressants.

#### Sécurité des types à la compilation

Cela a été une amélioration majeure pour moi personnellement. Au lieu de compter sur les clés "fortement" typées pour l'analyse JSON, nous travaillons maintenant avec des modèles fortement typés. Le générateur crée des types natifs Swift struct et enum directement à partir des schémas définis dans le document OpenAPI. Cela apporte la puissance d'un système fortement typé à la couche réseau et d'analyse.

Par exemple, si la valeur de retour d'une API est rendue optionnelle, au lieu de planter à l'exécution, nous échouerons à la compilation au moment de la construction. Cela nous oblige à résoudre ce problème immédiatement.

#### Collaboration et interopérabilité améliorées

Cela garantit que tous les développeurs sont sur la même longueur d'onde concernant un point de terminaison donné. Et comme cette spécification est agnostique, elle servira de langage universel pour toutes les équipes impliquées dans le projet - mobile, web et backend.

#### Autres outils

Une fois que vous avez une spécification, vous pouvez l'utiliser pour alimenter une grande variété d'outils. Vous pouvez générer une documentation interactive, créer des serveurs mock pour le développement frontend, et exécuter des tests automatisés.

D'accord, espérons que vous êtes convaincu - alors maintenant, comment implémentez-vous cela dans votre projet ?

## Un guide pratique pour implémenter cette solution

Nous allons maintenant examiner un exemple pratique afin que vous puissiez comprendre comment implémenter cela dans un projet. Cela implique :

* Créer un fichier openapi.yaml pour décrire la spécification de l'API.

* Configurer et intégrer `swift-openapi-generator` dans une application SwiftUI.

* Prototyper une application qui récupère et affiche une liste de posts depuis [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)

Pour suivre ce tutoriel, vous aurez besoin d'avoir Xcode installé et une compréhension de base de la programmation Swift et de SwiftUI pour le développement d'applications.

### Étape 1 : Créer un bon fichier openapi.yaml (la spécification)

La qualité d'une spécification est vraiment importante car elle détermine directement la qualité du code produit par `swift-openapi-generator`. Si vous n'avez pas une bonne spécification, vous pourriez rencontrer plusieurs problèmes que les développeurs se plaignent souvent, comme des noms de méthodes confus et longs.

Par exemple, cela pourrait générer quelque chose comme `get_all_my_meal_recipes_hyphen_detailed`. Cela pourrait se produire parce que le générateur est forcé de créer un nouveau nom basé sur le chemin de l'API si l'identifiant n'est pas fourni dans la spécification. Donc, au lieu de traiter ces problèmes un par un, nous allons créer une *bonne spécification claire* pour commencer.

Puisque nous utilisons `jsonplaceholder` comme notre serveur backend, nous sommes limités par les ajustements que nous pouvons faire - mais c'est un projet fantastique qui nous permet de simuler un serveur backend.

En général, un fichier OpenAPI.yaml contient :

1. OpenAPI Info et serveurs - Cela fournira les métadonnées sur l'API comme la version OpenAPI, quel serveur pointer pour les appels, etc.

2. Chemins - Cela fournira les points de terminaison disponibles. Dans notre cas, il peut contenir /posts comme l'un d'eux. Nous devons également mentionner le type de point de terminaison (get, post, put, etc.)

3. OperationID - Ce champ indique au générateur de créer une méthode claire avec ce nom.

4. Réponses - Cela définit les résultats possibles d'un appel API. Nous spécifierons la structure d'une réponse réussie 200 OK ou toute autre erreur ici.

5. Composants / Schémas - Cela définit tous les composants réutilisables et les modèles de données. Si nous avons un schéma Post défini ici, le générateur l'utilisera pour créer une structure Post en Swift pour correspondre à cela.

En gardant à l'esprit tous ces éléments, j'ai compilé un fichier yaml pour que nous l'utilisions pour ce tutoriel :

```yaml
# openapi.yaml
openapi: "3.0.3"
info:
  title: "JSONPlaceholder API"
  version: "1.0.0"
servers:
  - url: "https://jsonplaceholder.typicode.com"
paths:
  /posts:
    get:
      summary: "Get all posts"
      operationId: "getPosts"
      responses:
        "200":
          description: "A list of posts"
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Post"
components:
  schemas:
    Post:
      type: object
      required:
        - userId
        - id
        - title
        - body
      properties:
        userId:
          type: integer
        id:
          type: integer
        title:
          type: string
        body:
          type: string
```

La première ligne ici, `openapi: "3.0.3"`, indique simplement aux générateurs et aux parseurs que nous utilisons la version `3.0.3`.

Ensuite, nous avons quelques métadonnées supplémentaires - le nom et la version de l'API. Nous avons également le serveur que nous appelons avec nos API.

Après avoir défini ces métadonnées, nous définissons maintenant nos points de terminaison. Pour simplifier cet exemple, supposons que nous n'avons qu'un seul point de terminaison à appeler pour obtenir des posts. Nous représentons cela en disant `/posts` sous les chemins. Nous spécifions ensuite de quel type il s'agit en spécifiant `get:`.

Nous donnons une courte description de ce qu'il fait dans le `summary` et spécifions ensuite un `operationId` qui est ce que cette fonction sera appelée dans notre code généré. Nous spécifions également exactement quelle structure la réponse aura, c'est-à-dire un JSON d'un tableau de `Posts`.

Nous listons ensuite les composants que nous avons dans nos API comme le `Post`. Notez que nous utilisons le schéma `Post` dans la structure de réponse de retour avant de le définir plus loin. Les schémas dans les composants détermineront les structs de modèle que nous générerons à l'aide de ce fichier yaml.

### Étape 2 : Configurer votre projet

Créez un nouveau projet SwiftUI. Pour les besoins de ce tutoriel, nous utiliserons une application iOS - mais vous pouvez le faire avec n'importe quelle application. Sélectionnez Swift comme langage et SwiftUI pour l'interface.

![Écran de création d'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047209636/75cad7d3-f403-4285-8209-fd2bb65418e5.png align="center")

![Application SwiftUI de base après sa création](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047246793/3491aa5d-c35c-4157-adf2-789fe5e9cd96.png align="center")

Ajoutez le fichier `openapi.yaml` que nous venons de créer à ce projet. (Vous pouvez également créer ce fichier dans Xcode et copier, coller à partir du script ci-dessus.)

![Ajout du fichier openapi.yaml à notre projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047290178/fc31b759-b1c4-4b48-b58b-d90109614cd0.png align="center")

Maintenant, ajoutez les packages Swift suivants au projet. (**Note : Veuillez lire l'ensemble de la section sur l'ajout de packages avant de continuer.**)

1. Swift OpenAPI Generator - [https://github.com/apple/swift-openapi-generator](https://github.com/apple/swift-openapi-generator) - Le plugin générateur principal.

   ![Ajout de Swift OpenAPI Generator à notre projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047376776/b1d7b2d0-9b1f-45c8-8c74-4395a4c80dd9.png align="center")

   ![S'assurer qu'aucune cible n'est sélectionnée pour OpenAPIGenerator](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047411622/c6eca0c0-538e-40b5-a9b0-9fa044b60694.png align="center")

2. Swift OpenAPI Runtime - [https://github.com/apple/swift-openapi-runtime](https://github.com/apple/swift-openapi-runtime) - Cela contient les types et protocoles communs utilisés par le code généré par le plugin générateur.

   ![Ajout de OpenAPIRuntime à notre projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047457532/846ec488-cfed-4ca5-811b-c38dba0aaf30.png align="center")

3. Swift OpenAPI URLSession - [https://github.com/apple/swift-openapi-urlsession](https://github.com/apple/swift-openapi-urlsession) - Il s'agit d'une couche de transport qui permet au code généré d'utiliser Apple URLSession pour effectuer des requêtes réseau.

   ![Ajout de OpenAPIURLSession à notre projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1753047476699/9556047e-cc33-44b4-9980-0c692d4c1d01.png align="center")

Un point important à noter lors de l'ajout de ces packages est que **Swift OpenAPI Generator** ne doit **pas** être ajouté à votre cible de projet. Cela est dû au fait que nous utilisons cela uniquement pour générer le code, mais nous ne l'utilisons pas dans l'application.

Si vous obtenez cette erreur : `swift-openapi-generator/Sources/_OpenAPIGeneratorCore/PlatformChecks.swift:21:5 _OpenAPIGeneratorCore est uniquement destiné à être utilisé par swift-openapi-generator lui-même—votre cible ne doit pas lier cette bibliothèque ou l'outil de ligne de commande directement.` - alors vous avez fait cette erreur.

Le moyen le plus simple de corriger cela est de supprimer le package et de l'ajouter à nouveau. Ou vous pouvez aller dans `Projet → Cible → Phases de construction → Lier la bibliothèque binaire → Supprimer Swift OpenAPI Generator`.

![Où vérifier si vous rencontrez cette erreur](https://cdn.hashnode.com/res/hashnode/image/upload/v1753048265985/100428a4-e46a-4aa1-8fcf-4c74e26ffed6.png align="center")

Maintenant que nous avons ajouté ces plugins de générateur et d'exécution, nous devons donner au générateur quelques instructions sur ce qu'il doit générer. Vous pouvez le faire avec un fichier `openapi-generator-config.yaml`. Pour notre projet, utilisez le fichier suivant. Il est vraiment simple :

```yaml
generate:
  - types
  - client
```

Cela indique à notre générateur de générer les **types** - les structs, enums Swift, etc., à partir de la section schéma du fichier, et le **client** - la classe principale qui interagit avec la logique réseau.

![fichier openapi-generator-config.yaml](https://cdn.hashnode.com/res/hashnode/image/upload/v1753048237863/963d6bc0-a368-427b-add3-75dcf4bd3edf.png align="center")

Enregistrez cela dans un fichier `openapi-generator-config.yaml` comme indiqué.

Et enfin, nous voulons que le générateur s'exécute chaque fois que nous voulons construire cette application/cible. Nous pouvons spécifier cela dans l'onglet Phases de construction de la cible. Sous "Cible → Phases de construction → Exécuter les plugins d'outil de construction", ajoutez le plugin OpenAPIGenerator.

![Ajout du générateur dans la phase de construction](https://cdn.hashnode.com/res/hashnode/image/upload/v1753048334094/24e20adc-c6e0-4d66-965b-19d476a5ffd3.png align="center")

La première fois que le projet est construit après avoir défini cela, Xcode affichera une boîte de dialogue de sécurité. Cela nous permettra de "Faire confiance et activer" pour ce plugin. Il s'agit d'une confirmation unique qui donne à ce plugin la permission requise pour s'exécuter pendant le processus de construction.

![Boîte de dialogue de sécurité Faire confiance et activer pour le générateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1753048374405/6ff51ff4-d33a-4920-b95f-9fda0ee0aef4.png align="center")

Dès que vous construisez la deuxième fois après avoir donné ces permissions, vous générerez les fichiers. Vous ne verrez peut-être aucun changement dans la fenêtre Xcode elle-même. Mais si vous êtes curieux de voir le résultat, allez dans ce dossier.

`DerivedData → <NomDuProjet>*identifiant → Build → intermediates.noindex → BuildToolPluginIntermediates → <NomDeLaCible>.output → <NomDeLaCible> → OpenAPIGenerator → GeneratedSources`

Plus d'informations sur le dossier de données dérivées ici : [https://gayeugur.medium.com/derived-data-2e9468c6da9b](https://gayeugur.medium.com/derived-data-2e9468c6da9b) si vous êtes curieux.

Gardez à l'esprit que cet emplacement peut varier en fonction de la version de Xcode, de la version d'OpenAPI et des paramètres de votre projet. Mais vous n'avez pas besoin de vous soucier de l'emplacement du fichier.

Vous verrez trois fichiers appelés Client.swift, Types.swift et Server.swift.

![Fichiers générés](https://cdn.hashnode.com/res/hashnode/image/upload/v1753048508703/8fcec6bf-ad86-47de-b57c-7dca22256e06.png align="center")

Ce sont les fichiers que notre générateur a créés et remplis avec les types et fonctions dont nous avons besoin.

Dans la section suivante, nous discutons de la manière d'utiliser ces fichiers pour effectuer des appels au serveur.

### Étape 3 : Écrire un wrapper

Bien qu'il soit certainement possible de faire les appels au serveur en utilisant uniquement le code généré (type `Client`) dans toute notre application, une approche plus maintenable consiste à utiliser un wrapper autour de ces types. Cela fournira une interface stable et propre pour le reste de notre application à utiliser, et cela découple le code des fonctionnalités du code généré.

Je peux vous entendre penser : "Attendez une seconde. N'est-ce pas le but même de générer ce code pour éviter cette abstraction de code boilerplate ?"

Bien que cela ajoute une certaine abstraction par-dessus le code généré, il est précieux de l'avoir pour un certain nombre de raisons. En voici quelques-unes :

1. Meilleure dénomination. La structure `Post` générée s'appellera actuellement `Components.Schemas.Post`.

2. Si vous souhaitez un jour vous éloigner du générateur, une abstraction est vraiment utile.

3. Si vous souhaitez simuler cet appel serveur, vous pouvez le faire via l'abstraction.

4. Optimisation de l'interface utilisateur. Vous pourriez vouloir aplatir la structure d'un modèle pour réduire le nombre de variables calculées, etc.

Nous voulons donc envelopper cela dans un fichier appelé `WebService.swift` :

```swift
// WebService.swift
import Foundation
import OpenAPIURLSession

// Un modèle Post propre, spécifique à l'application.
// Cela découple les vues des types générés.
struct AppPost: Identifiable, Codable {
    let id: Int
    let title: String
    let body: String
}

class WebService {
    private let client: Client

    init() {
        // L'URL du serveur et le transport proviennent du code généré.
        // `Servers.Server1.url()` correspond à la première URL dans le tableau `servers` de la spécification.
        self.client = Client(
            serverURL: try! Servers.Server1.url(),
            transport: URLSessionTransport()
        )
    }

    func getPosts() async throws -> [AppPost] {
        // Appeler la méthode générée, qui a été nommée en utilisant `operationId`.
        let response = try await client.getPosts(.init())

        // La réponse générée est une enum sûre en termes de types couvrant tous les codes de statut documentés.
        switch response {
        case.ok(let okResponse):
            // Le corps est également une enum sûre en termes de types pour différents types de contenu.
            switch okResponse.body {
            case.json(let posts):
                // Mapper le `Components.Schemas.Post` généré vers notre modèle `AppPost` propre.
                return posts.map { post in
                    AppPost(id: post.id, title: post.title, body: post.body)
                }
            }
        // Le générateur force la gestion des autres réponses documentées.
        // Notre spécification simple n'a qu'un 200, donc toute autre réponse est non documentée.
        case.undocumented(statusCode: let statusCode, _):
            throw URLError(.badServerResponse, userInfo: ["statusCode": statusCode])
        }
    }
}
```

Passons en revue ce fichier pour comprendre ce que nous faisons.

Tout d'abord, nous importons `OpenAPIUrlSession` ainsi que `Foundation`. Cela nous permet d'appeler le serveur, d'obtenir une réponse et de parser cette réponse.

Ensuite, nous définissons la nouvelle structure `AppPost`. Cela est censé être la représentation d'un `Post` dans l'application. Dans le fichier `Types.Swift` généré, nous avons la structure `Post` générée. Cela est défini comme :

```swift
/// - Remarque : Généré à partir de `#/components/schemas/Post`.
        internal struct Post: Codable, Hashable, Sendable {
            /// - Remarque : Généré à partir de `#/components/schemas/Post/userId`.
            internal var userId: Swift.Int
            /// - Remarque : Généré à partir de `#/components/schemas/Post/id`.
            internal var id: Swift.Int
            /// - Remarque : Généré à partir de `#/components/schemas/Post/title`.
            internal var title: Swift.String
            /// - Remarque : Généré à partir de `#/components/schemas/Post/body`.
            internal var body: Swift.String
            /// Crée un nouveau `Post`.
            ///
            /// - Paramètres:
            ///   - userId:
            ///   - id:
            ///   - title:
            ///   - body:
            internal init(
                userId: Swift.Int,
                id: Swift.Int,
                title: Swift.String,
                body: Swift.String
            ) {
                self.userId = userId
                self.id = id
                self.title = title
                self.body = body
            }
            internal enum CodingKeys: String, CodingKey {
                case userId
                case id
                case title
                case body
            }
        }
```

Comme vous pouvez le voir, notre structure `AppPost` est différente de ce type généré. Nous omettons le `userId` puisque nous ne nous en soucions pas (au moins pour l'instant).

De retour à la classe `WebService`, nous voyons un attribut `client`. Il s'agit d'une variable de type généré qui nous permettra d'interagir avec les serveurs. Dans l'initialiseur de la classe `WebService`, nous créons un nouveau `Client` en utilisant la première URL de serveur que nous avons spécifiée dans le schéma et utilisons l'objet `URLSessionTransport` pour effectuer ces appels.

Nous définissons ensuite nos méthodes. Dans ce cas, notre fonction `getPosts()` qui retourne un tableau `[AppPost]`.

`let response = try await client.getPosts(.init())` appellera la fonction `getPosts()` sur l'objet `Client`. La fonction `Client.getPosts()` ici prend en entrée une structure appelée `Operations.getPosts.Input` qui est initialisée par le `.init()` passé ici.

Cette réponse générée est une enum sûre en termes de types couvrant tous les codes documentés. (Actuellement seulement `200` dans notre fichier yaml). Nous utilisons donc un simple switch pour examiner ces deux cas et utilisons davantage d'instructions switch pour obtenir la réponse appropriée. Vous pouvez voir à quel point cela est plus facile que de parser la réponse manuellement.

Une fois que nous obtenons la réponse `Components.Schemas.Post`, nous la mappons et la convertissons en tableau `[AppPost]` et la retournons.

Maintenant, utilisons ce wrapper pour afficher les données dans notre application.

### Étape 4 : Appeler le wrapper et afficher les données

Nous en sommes à l'étape finale. Nous allons utiliser le wrapper que nous avons créé pour afficher les posts récupérés. Nous allons également utiliser une variable d'état pour stocker notre tableau `AppPost` dans notre vue `ContentView`. Nous allons ensuite appeler `getPosts()` lorsque la vue est affichée pour la première fois à l'utilisateur.

```swift
// ContentView.swift
import SwiftUI

struct ContentView: View {
    @State private var posts: [AppPost] = []
    @State private var errorMessage: String?

    private let webService = WebService()

    var body: some View {
        NavigationStack {
            List(posts) { post in
                VStack(alignment:.leading, spacing: 8) {
                    Text(post.title)
                       .font(.headline)
                    Text(post.body)
                       .font(.subheadline)
                       .foregroundColor(.secondary)
                }
               .padding(.vertical, 4)
            }
           .navigationTitle("Posts")
           .task {
                await loadPosts()
            }
           .overlay {
                if let errorMessage {
                    ContentUnavailableView("Error", systemImage: "xmark.octagon", description: Text(errorMessage))
                } else if posts.isEmpty {
                    ProgressView()
                }
            }
        }
    }

    func loadPosts() async {
        self.errorMessage = nil
        do {
            self.posts = try await webService.getPosts()
        } catch {
            self.errorMessage = error.localizedDescription
        }
    }
}

#Preview {
    ContentView()
}
```

Vous pouvez voir les posts factices dans l'aperçu. Comme vous pouvez le voir, tout ce que nous avons eu à faire était d'appeler `webService.getPosts()` pour remplir la variable.

![Exécution du simulateur de l'application montrant les posts récupérés](https://cdn.hashnode.com/res/hashnode/image/upload/v1753053957409/b89d50e8-ab73-4484-beda-3a328a575144.png align="center")

Vous pourriez penser que c'est beaucoup de configuration pour une structure simple comme `Post` pour laquelle nous avons dû créer un wrapper appelé `AppPost` de toute façon. Mais si vous aviez dix types comme celui-ci et vingt points de terminaison à appeler ? Vous n'auriez pas à gérer beaucoup de code répétitif et sujet aux erreurs.

## Pièges potentiels

Malheureusement, aucun processus n'est parfait. Vous pourriez encore rencontrer de nombreux problèmes avec le code généré et cette méthode. J'ai listé certains d'entre eux ici et comment les gérer.

### Code généré verbeux ou laid

Si vous avez un code généré très verbeux ou laid, le problème est presque toujours l'absence d'`operationId` pour un chemin d'API. Si vous n'en spécifiez pas un, le générateur doit créer un nom à partir du chemin et de la méthode HTTP, ce qui donne des noms longs et encombrants. L'ajout d'un `operationId` clair atténuera ce problème.

### Spécifications volumineuses et problèmes de performance

Si vous avez un fichier de spécification très volumineux, la génération d'un client pour cette spécification complète peut augmenter considérablement le temps de compilation. Cela peut également entraîner des fichiers `Types.swift` et `Client.swift` absolument massifs.

Il existe une option de filtre dans le fichier `openapi-generator-config.yaml` qui permettra au générateur d'inclure uniquement les parties de la spécification pertinentes pour l'application afin d'améliorer les temps de construction, etc. Mais si vous voulez tout dans une API qui a des centaines de points de terminaison, le seul moyen de réduire les temps de compilation est d'éviter de régénérer cela à chaque fois et de découpler cette étape du processus de construction régulier.

### Fonctionnalités de spécification non supportées

Bien que le package Swift, `swift-openapi-generator`, soit robuste, il ne supporte pas toutes les fonctionnalités incluses dans la spécification. J'ai eu des problèmes avec certaines fonctionnalités de la version plus récente de la spécification (`3.1.1`) et j'ai dû rétrograder à `3.0.3` pour qu'elle fonctionne bien.

Il existe également des problèmes connus comme le manque de support pour certains types de schémas récursifs. Parfois, le générateur rencontre des erreurs et échoue, et d'autres fois, il génère des types incomplets - ce qui peut entraîner quelques heures de débogage (je parle par expérience).

Dans tous les cas, connaître les limites de ce générateur peut être utile pour éviter les problèmes qu'il pourrait causer. Gardez également à l'esprit qu'il s'améliore constamment grâce à sa nature open source.

## Conclusion : Adoptez le développement piloté par les spécifications

Dans ce guide, vous avez parcouru le chemin de l'adoption de `swift-openapi-generator` - de la compréhension de la puissance des contrats d'API à la création d'une application SwiftUI fonctionnelle. Vous avez également appris les défis réels de ce processus. Bien qu'il y ait une courbe d'apprentissage initiale, les avantages de cette approche sont profonds.

Le principe fondamental de cette approche est de favoriser une méthode plus disciplinée et plus robuste pour construire des applications. En faisant du document OpenAPI la seule source de vérité, vous vous assurez que le frontend et le backend sont parfaitement synchronisés en permanence.

L'utilisation de cette approche permet également d'obtenir un code plus sûr en termes de types et plus maintenable. Le résultat est moins de temps passé à écrire du code boilerplate et à déboguer des erreurs d'intégration aléatoires, et plus de temps passé à créer l'application elle-même.

Pour les développeurs prêts à explorer davantage, veuillez consulter le dépôt officiel `swift-openapi-generator` sur GitHub ici : [https://github.com/apple/swift-openapi-generator](https://github.com/apple/swift-openapi-generator).

Vous pouvez me suivre sur [GitHub](https://github.com/sravankaruturi) et [Hashnode](https://hashnode.com/@sravankaruturi) pour mes autres publications et projets.