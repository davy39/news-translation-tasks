---
title: Création de compétences Alexa en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-04T17:00:19.000Z'
originalURL: https://freecodecamp.org/news/building-alexa-skills-in-swift-3d596aa0ee95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1uxPyAsM7gCUf0YsWGYYgw.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: skills development
  slug: skills-development
- name: Swift
  slug: swift
seo_title: Création de compétences Alexa en Swift
seo_desc: 'By Claus Höfele

  How to use Swift to develop custom skills for the Amazon Echo

  The Alexa Voice Service is Amazon’s cloud service that understands natural language
  and allows users to interact with devices by using their voice. You usually associate
  Al...'
---

Par Claus Höfele

#### Comment utiliser Swift pour développer des compétences personnalisées pour Amazon Echo

Le service vocal Alexa est le service cloud d'Amazon qui comprend le langage naturel et permet aux utilisateurs d'interagir avec les appareils en utilisant leur voix. Vous associez généralement Alexa aux haut-parleurs activés par la voix d'Amazon, comme l'[Echo](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E), mais Alexa peut potentiellement fonctionner sur n'importe quel appareil connecté avec un microphone et un haut-parleur.

Contrairement à Siri d'Apple, dont les extensions sont [limitées à des domaines spécifiques](https://developer.apple.com/library/prerelease/content/documentation/Intents/Conceptual/SiriIntegrationGuide/), l'API d'Alexa permet aux développeurs de mettre en œuvre une large gamme de services vocaux personnalisés appelés « compétences ». Utiliser Swift permet aux développeurs iOS (comme moi) d'élargir leurs compétences existantes pour inclure la programmation côté serveur et participer à la tendance des interfaces utilisateur vocales.

### Ingrédients

En termes simples, Alexa envoie à votre compétence un message JSON avec l'intention de l'utilisateur et votre code répond avec un message JSON qui détermine ce qu'Alexa répondra à l'utilisateur.

Puisque je préfère implémenter cette fonctionnalité en Swift, j'utilise [AlexaSkillsKit](https://github.com/choefele/AlexaSkillsKit), une bibliothèque Swift que j'ai écrite. Elle prend en charge l'analyse des requêtes JSON d'Amazon, la génération des réponses appropriées et fournit des méthodes de commodité pour gérer les fonctionnalités d'Alexa.

Le code de votre compétence personnalisée peut s'exécuter soit en tant que service web autonome, soit en tant que fonction AWS Lambda. En utilisant Lambda, la plateforme de calcul sans serveur d'Amazon, Amazon prendra en charge la mise à l'échelle et l'exécution de votre code Swift — c'est la raison pour laquelle j'utiliserai ce type de déploiement pour la compétence finale. Comme vous le verrez, cependant, l'option de service web est vraiment utile lors du développement de votre compétence.

Notez que, par défaut, Lambda ne prend en charge que le code écrit en JavaScript (Node.js), Python et Java. Mais il est facile d'étendre cela aux exécutables écrits dans n'importe quel langage de programmation que vous souhaitez. Mon article [Serverless Swift](https://medium.com/@claushoefele/serverless-swift-2e8dce589b68#.ts7aama46) fournit un guide étape par étape sur la façon de procéder.

En résumé, vous aurez besoin des éléments suivants pour votre compétence Alexa :

* Une implémentation de la fonctionnalité de votre compétence en Swift utilisant [AlexaSkillsKit](https://github.com/choefele/AlexaSkillsKit)
* Une fonction Lambda configurée avec votre code Swift en utilisant la [Console AWS](https://aws.amazon.com/console/)
* Une compétence Alexa configurée dans la [Console Alexa](https://developer.amazon.com/edw/home.html) qui déclenche votre fonction Lambda

Notez que la Console Alexa et la Console AWS sont deux services distincts auxquels vous devez vous inscrire.

### Le Projet Exemple

Pour simplifier vos premiers pas, j'ai créé un dépôt avec une application exemple. [swift-lambda-app](https://github.com/choefele/swift-lambda-app) contient du code et des scripts pour vous aider à démarrer rapidement avec l'écriture d'une compétence Alexa personnalisée en Swift et son déploiement sur AWS Lambda.

L'application exemple utilise une structure de répertoire standard du gestionnaire de paquets Swift et un [fichier de package](https://github.com/choefele/swift-lambda-app/blob/master/Package.swift), ainsi _swift build_, _swift test_ et _swift package generate-xcodeproj_ fonctionnent comme prévu. Consultez la [documentation SPM](https://github.com/apple/swift-package-manager/blob/master/Documentation/Usage.md) pour plus d'informations.

Il y a trois cibles :

* **AlexaSkill** : il s'agit d'une bibliothèque avec le code qui implémente la compétence Alexa personnalisée. C'est une bibliothèque séparée afin qu'elle puisse être utilisée par les deux autres cibles. De plus, les bibliothèques ont `ENABLE_TESTABILITY` activé par défaut, ce qui vous permet d'accéder aux méthodes et propriétés internes dans vos tests unitaires.
* **Lambda** : L'exécutable en ligne de commande pour le déploiement sur Lambda. Ce programme utilise _stdin_ et _stdout_ pour traiter les données.
* **Server** (macOS uniquement) : Pour simplifier l'implémentation d'une compétence Alexa personnalisée, le serveur fournit une interface HTTP à la cible AlexaSkill. Ce serveur HTTP peut être exposé publiquement via [ngrok](https://ngrok.com/) et configuré dans la console Alexa, ce qui vous permet de développer et de déboguer une compétence Alexa avec du code s'exécutant sur votre ordinateur de développement. Cette cible est uniquement pour macOS car il n'était pas possible de séparer proprement les dépendances des cibles et je ne voulais pas lier les bibliothèques destinées au développement serveur à l'exécutable Lambda utilisé pour le déploiement.

Pour le développement, je recommande une approche de [Développement piloté par les tests](https://en.wikipedia.org/wiki/Test-driven_development) contre la cible de bibliothèque, car cela donne le retour le plus rapide pour les modifications de code. Le téléchargement vers Lambda pour vérifier rapidement les modifications n'est pas vraiment une option en raison des temps de téléchargement lents. Exposer votre fonctionnalité via HTTPS comme décrit ci-dessous, cependant, vous permet de tester et de déboguer votre fonctionnalité d'une manière légèrement différente.

### Implémentation d'une compétence Alexa personnalisée

Commencez par implémenter le protocole _RequestHandler_. AlexaSkillsKit analyse les requêtes d'Alexa et transmet les données aux méthodes requises par ce protocole.

```
public protocol RequestHandler {        func handleLaunch(request: LaunchRequest, session: Session, next: @escaping (StandardResult) -> ())
```

```
    func handleIntent(request: IntentRequest, session: Session, next: @escaping (StandardResult) -> ())
```

```
    func handleSessionEnded(request: SessionEndedRequest, session: Session, next: @escaping (VoidResult) -> ())}
```

Par exemple, une [requête de lancement](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/custom-standard-request-types-reference#launchrequest) entraînerait AlexaSkillsKit appelant la méthode _handleLaunch()_.

```
import Foundationimport AlexaSkillsKit
```

```
public class AlexaSkillHandler : RequestHandler {    public init() {}    public func handleLaunch(request: LaunchRequest, session: Session, next: @escaping (StandardResult) -> ()) {        let standardResponse = generateResponse(message: "Hello Swift")        next(.success(standardResponse: standardResponse, sessionAttributes: session.attributes))    }}
```

Dans le gestionnaire de requêtes, votre compétence personnalisée peut implémenter toute logique requise par votre compétence. Pour permettre un code asynchrone (par exemple, appeler un autre service HTTP), le résultat est transmis via le rappel _next_. _next_ prend une énumération qui est soit _.success_ et contient une réponse Alexa, soit _.failure_ en cas de problème.

Pour garder les choses simples, nous allons renvoyer un message qu'Alexa dira à haute voix à l'utilisateur :

```
func generateResponse(message: String) -> StandardResponse {    let outputSpeech = OutputSpeech.plain(text: message)    return StandardResponse(outputSpeech: outputSpeech)}
```

### Débogage de votre code avec un serveur HTTP local

L'invocation d'un _RequestHandler_ dans le cadre d'un serveur Swift est effectuée via l'API HTTPS d'Amazon, où le service Alexa appelle votre serveur avec une requête POST. Dans le code suivant, [Kitura](https://github.com/IBM-Swift/Kitura) est utilisé comme framework web, mais tout autre framework web fonctionnerait tout aussi bien :

```
import Foundationimport AlexaSkillsKitimport AlexaSkillimport Kiturarouter.all("/") { request, response, next in    var data = Data()    let _ = try? request.read(into: &data)    let requestDispatcher = RequestDispatcher(requestHandler: AlexaSkillHandler())    requestDispatcher.dispatch(data: data) { result in        switch result {        case .success(let data):            response.send(data: data).status(.OK)        case .failure(let error):            response.send(error.message).status(.badRequest)        }        next()    }}Kitura.addHTTPServer(onPort: 8090, with: router)Kitura.run()
```

Pour exécuter un serveur HTTPS local :

* Assurez-vous que l'exemple se construit en exécutant _swift build_
* Générez un projet Xcode avec _swift package generate-xcodeproj_
* Ouvrez le projet Xcode généré, sélectionnez le schéma Server et exécutez le produit (CMD-R). Cela démarrera un serveur sur le port 8090
* Installez ngrok via _brew cask install ngrok_. Cet outil vous permet d'exposer un serveur HTTP local sur Internet
* Exécutez _ngrok http 8090_ et copiez l'URL HTTPS générée par ngrok (elle ressemble à https://c4ba192c.ngrok.io)

![Image](https://cdn-media-1.freecodecamp.org/images/oTg3tdnBl-Ko4ksBBstFqLLFq29Ek2GcB-6g)

ngrok expose votre serveur local à l'internet public, permettant ainsi au service vocal Alexa d'appeler votre compétence personnalisée s'exécutant dans Xcode.

### Configuration de la compétence Alexa

Pour connecter votre compétence personnalisée à Alexa :

* Allez dans la [console Alexa](https://developer.amazon.com/edw/home.html#/skills/list) et créez une nouvelle compétence
* Type de compétence : Modèle d'interaction personnalisé
* Intention : `{"intents": [{"intent": "TestIntent"}]}`
* Énoncés d'exemple : « TestIntent test swift »
* Certificat SSL : Sélectionnez « Mon point de terminaison de développement est un sous-domaine d'un domaine qui possède un certificat générique d'une autorité de certification »
* Type de point de terminaison de service : _HTTPS (utilisez l'URL de ngrok)_

Vous pouvez maintenant tester la compétence dans le simulateur de service de la console Alexa en utilisant l'énoncé « test swift ». Cela appellera votre serveur local, vous permettant de modifier et de déboguer votre code tout en interagissant avec le service Alexa.

![Image](https://cdn-media-1.freecodecamp.org/images/eQLxWIDrhg7aBhMOERXzLRPohltuzaqNim54)

### Exécution de tests pour votre code

Avant de télécharger sur Lambda, il est utile d'exécuter vos tests unitaires dans un environnement Linux et d'exécuter des tests d'intégration qui simulent l'environnement d'exécution. L'exemple fournit [_run-unit-tests.sh_](https://github.com/choefele/swift-lambda-app/blob/master/run-unit-tests.sh) pour faire le premier et [_run-integration-tests.sh_](https://github.com/choefele/swift-lambda-app/blob/master/run-integration-tests.sh) pour faire le second.

_run-unit-tests.sh_ construit et teste la cible Lambda à l'intérieur d'un conteneur Docker Swift basé sur Ubuntu car il n'y a actuellement pas de compilateur Swift pour Amazon Linux (basé sur RHEL). Les exécutables construits sur différentes distributions Linux sont compatibles les uns avec les autres si vous fournissez toutes les dépendances nécessaires à l'exécution du programme. Pour cette raison, le script capture toutes les bibliothèques partagées nécessaires à l'exécution de l'exécutable en utilisant _ldd_.

Pour prouver que le package résultant fonctionne, _run-integration-tests.sh_ exécute une version de release du code Swift à l'intérieur d'un conteneur Docker qui se rapproche de l'environnement d'exécution de Lambda (malheureusement, [Amazon ne fournit que quelques images Docker](https://hub.docker.com/_/amazonlinux/) qui ne correspondent pas nécessairement à ce que [Lambda utilise](http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html)).

L'intégration avec Lambda est effectuée via un petit [script Node.js](https://github.com/choefele/swift-lambda-app/blob/master/Shim/index.js) qui utilise le module _child_process_ pour exécuter l'exécutable Swift. Le script suit les recommandations d'Amazon pour [exécuter des exécutables arbitraires dans AWS Lambda](https://aws.amazon.com/blogs/compute/running-executables-in-aws-lambda/).

Après avoir [configuré Travis](https://github.com/choefele/swift-lambda-app/blob/master/.travis.yml), vous pouvez exécuter le même script d'intégration également pour chaque commit.

### Déploiement de votre code sur Lambda

Pour Lambda, vous devez créer un exécutable qui prend les entrées de _stdin_ et écrit les sorties dans _stdout_. Cela peut être fait avec le code suivant :

```
import Foundationimport AlexaSkillsKitimport AlexaSkilldo {    let data = FileHandle.standardInput.readDataToEndOfFile()    let requestDispatcher = RequestDispatcher(requestHandler: AlexaSkillHandler())    let responseData = try requestDispatcher.dispatch(data: data)    FileHandle.standardOutput.write(responseData)} catch let error as MessageError {    let data = error.message.data(using: .utf8) ?? Data()    FileHandle.standardOutput.write(data)}
```

Notez que ce code utilise le même _RequestHandler_ que celui utilisé pour le serveur HTTP, minimisant ainsi les différences avec l'environnement de développement.

Pour déployer votre code sur Lambda :

* Exécutez _run-integration-tests.sh_ pour produire un fichier zip à .build/lambda/lambda.zip avec tous les fichiers nécessaires à télécharger sur Lambda
* Créez une nouvelle fonction Lambda dans la [Console AWS](https://console.aws.amazon.com/lambda/home) dans la région US East/N. Virginia (pour l'Europe, utilisez EU/Irlande)
* Utilisez un déclencheur Alexa Skills Kit
* Runtime : NodeJS 4.3
* Type d'entrée de code : Fichier ZIP (téléchargez le fichier lambda.zip de l'étape précédente)
* Handler : index.handler
* Rôle : Créer à partir d'un modèle ou utiliser un rôle existant

Une fois que vous avez téléchargé la fonction Lambda, vous pouvez utiliser les actions de test dans la Console AWS, par exemple en utilisant une action Start Session.

![Image](https://cdn-media-1.freecodecamp.org/images/HB448STSmeJW0tYbqsWJToGOV2gJjRQsWkcV)

### Configuration de la compétence Alexa pour Lambda

Après avoir créé la fonction Lambda, vous pouvez maintenant créer une compétence Alexa. Si vous avez précédemment créé une compétence Alexa pour le serveur HTTP local — la seule différence est le point de terminaison du service :

* Allez dans la [console Alexa](https://developer.amazon.com/edw/home.html#/skills/list) et créez une nouvelle compétence
* Type de compétence : Modèle d'interaction personnalisé
* Intention : `{"intents": [{"intent": "TestIntent"}]}`
* Énoncés d'exemple : « TestIntent test swift »
* Type de point de terminaison de service : _AWS Lambda ARN_ (utilisez l'ARN pour la fonction Lambda de la Console AWS)

Vous pouvez maintenant tester la compétence dans la Console Alexa en utilisant l'énoncé « test swift ». Plus de détails sur la configuration des compétences Alexa peuvent être trouvés sur le [portail des développeurs d'Amazon](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/overviews/steps-to-build-a-custom-skill).

### Conclusion

Consultez le dépôt [swift-lambda-app](https://github.com/choefele/swift-lambda-app) sur GitHub pour le code et les scripts permettant de développer et de déployer une compétence Alexa simple en Swift. Dans de futurs articles, je fournirai plus de détails sur la façon d'écrire des compétences utiles. En attendant, vous pouvez parcourir la [documentation d'Amazon](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference) ou me contacter sur [Twitter](https://twitter.com/claushoefele) si vous avez des questions.