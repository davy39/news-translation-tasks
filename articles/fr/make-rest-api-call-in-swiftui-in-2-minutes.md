---
title: Comment faire un appel simple à une API REST GET asynchrone dans SwiftUI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-02T18:32:23.000Z'
originalURL: https://freecodecamp.org/news/make-rest-api-call-in-swiftui-in-2-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Frame-12-3.png
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: Swift
  slug: swift
- name: SwiftUI
  slug: swiftui
seo_title: Comment faire un appel simple à une API REST GET asynchrone dans SwiftUI
seo_desc: 'By Saamer Mansoor

  In this tutorial for beginners, you will learn the basics of using SwiftUI to make
  API calls using the popular Internet Chuck Norris DataBase (ICNDB) as an example.
  It will display a joke quickly and easily using Swift and SwiftUI. ...'
---

Par Saamer Mansoor

Dans ce tutoriel pour débutants, vous apprendrez les bases de l'utilisation de SwiftUI pour faire des appels d'API en utilisant la populaire base de données Internet Chuck Norris (ICNDB) comme exemple. Il affichera une blague rapidement et facilement en utilisant Swift et SwiftUI. 

Vous verrez comment le framework multiplateforme SwiftUI nous permet d'utiliser exactement le même code sur iOS, iPadOS, macOS, watchOS, App Clips et tvOS, ce qui aurait été impossible autrement.

En plus de cela, vous utiliserez [async-await](https://developer.apple.com/documentation/swift/swift_standard_library/concurrency/updating_an_app_to_use_swift_concurrency) qui a été introduit dans Swift 5.5, et qui fonctionne pour les systèmes d'exploitation plus récents, y compris les iPhones exécutant iOS > v15.0. Cela simplifie vraiment notre travail de réalisation d'appels réseau de données de manière asynchrone au clic d'un bouton sans bloquer le thread de l'interface utilisateur. 

Je vais partager les modifications de code que vous devrez apporter en premier. Ensuite, dans la section suivante, je vais partager une brève analyse du code afin que les débutants puissent également comprendre ce qui se passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Group-1-1.png)
_Application tvOS exécutant le code affichant un bouton qui récupère la blague au clic_

## Comment faire des appels d'API dans Swift et SwiftUI

Tout d'abord, vous aurez besoin d'un Mac pour installer Xcode. Une fois installé, ouvrez Xcode et créez un nouveau projet. Ensuite, sélectionnez "App" pour iOS, macOS, tvOS ou watchOS.

### ContentView

Mettez simplement à jour votre fichier SwiftUI ContentView existant pour ajouter un bouton et utiliser la variable _State_ pour actualiser le texte affiché lorsque la blague est retournée par l'API ICNDB :

```swiftui
import Foundation
import SwiftUI
struct ContentView: View {
    @State private var joke: String = ""
    var body: some View {
        Text(joke)
        Button {
            Task {
                let (data, _) = try await URLSession.shared.data(from: URL(string:"https://api.chucknorris.io/jokes/random")!)
                let decodedResponse = try? JSONDecoder().decode(Joke.self, from: data)
                joke = decodedResponse?.value ?? ""
            }
        } label: {
            Text("Récupérer une blague")
        }
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
struct Joke: Codable {
    let value: String
}
```

### Récupérer une blague !

Si vous appuyez sur build/play, l'application se construira sur la plateforme que vous avez sélectionnée ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-01-at-4.42.11-AM.png)
_Captures d'écran des applications watchOS, macOS et iOS exécutant exactement le même code_

## Analyse du code

Si vous allez à l'URL de la blague aléatoire, vous remarquerez que les données sont au format JSON. Vous pouvez copier cela et utiliser un JSON Linter pour voir sa structure afin de déterminer quelle propriété de l'objet Joke est nécessaire. 

Sur cette base, vous déterminez le code ci-dessus. Vous utilisez le protocole Codable (aka interfaces) pour passer d'un objet de données JSON à une classe ou une structure Swift réelle, et vous créez des propriétés pour les données que vous souhaitez stocker (value dans notre cas). 

JSONDecoder nous aide à analyser la chaîne JSON en utilisant l'objet Codable. Cela fonctionne indépendamment de la plateforme car la page qui se charge au lancement de l'application a le même nom _ContentView_ quelle que soit la plateforme.

### App Clips

[App Clips](https://developer.apple.com/app-clips/) sont la dernière méthode d'Apple pour utiliser la fonctionnalité native d'une application à l'aide d'un "App Clip Code" sans avoir à télécharger l'application complète depuis l'App Store.

Les App Clips fonctionnent de manière similaire à une application iOS – la seule différence est que vous ne créez pas un nouveau projet App Clip. Vous devez simplement ajouter l'App Clip en tant que cible à une application iOS existante en allant dans Fichier->Nouveau->Cible->iOS->App Clip lorsqu'une application iOS existante est ouverte dans Xcode. 

Si vous vous demandez à propos des [Widgets](https://support.apple.com/en-us/HT207122) iPhone/iPad, eh bien, ils ne s'animent pas. Ainsi, les clics sur les boutons ouvriront simplement l'application correspondante et ne pourront pas mettre à jour le texte via une API externe de manière indépendante. 

## Conclusion

Dans cet article, vous avez appris comment faire des appels d'API RESTful GET à partir de SwiftUI de la manière la plus simple possible ! 

N'hésitez pas à me contacter si vous avez des questions. J'ai compris cela en utilisant un autre article et j'ai pensé à le simplifier davantage. Donc, pour plus de détails et des moyens de rendre ce code plus complexe, consultez cet article :

%[https://www.raywenderlich.com/25013447-async-await-in-swiftui]