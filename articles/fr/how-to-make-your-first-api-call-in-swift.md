---
title: Comment faire un appel API en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-29T11:49:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-api-call-in-swift
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef3740569d1a4ca4004.jpg
tags:
- name: api
  slug: api
- name: iOS
  slug: ios
- name: Swift
  slug: swift
seo_title: Comment faire un appel API en Swift
seo_desc: 'By Ai-Lyn Tang

  If you are looking to become an iOS developer, there are some fundamental skills
  worth knowing. First, it''s important to be familiar with creating table views.
  Second, you should know how to populate those table views with data. Third,...'
---

Par Ai-Lyn Tang

Si vous souhaitez devenir développeur iOS, il y a certaines compétences fondamentales à connaître. Tout d'abord, il est important d'être familier avec la création de vues de tableau. Ensuite, vous devez savoir comment remplir ces vues de tableau avec des données. Enfin, il est idéal si vous pouvez récupérer des données à partir d'une API et utiliser ces données dans votre vue de tableau.

C'est ce troisième point que nous allons aborder dans cet article. Depuis l'introduction de `Codable` dans Swift 4, faire des appels API est beaucoup plus facile. Auparavant, la plupart des gens utilisaient des pods comme Alamofire et SwiftyJson (vous pouvez lire comment faire cela [ici](https://code.likeagirl.io/3-steps-to-make-your-first-api-call-836e43ed702c)). Maintenant, la méthode Swift est beaucoup plus agréable dès la sortie de la boîte, donc il n'y a aucune raison de télécharger un pod.

Passons en revue quelques éléments de base souvent utilisés pour faire un appel API. Nous allons d'abord aborder ces concepts, car ils sont des parties importantes pour comprendre comment faire un appel API.

* Gestionnaires de complétion
* `URLSession`
* `DispatchQueue`
* Cycles de rétention

Enfin, nous allons tout rassembler. J'utiliserai l'API open source [Star Wars API](https://www.swapi.co/) pour construire ce projet. Vous pouvez voir mon code de projet complet sur [GitHub](https://github.com/ailyntang/starwars/).

_Avertissement : Je suis nouveau dans le codage et je suis largement autodidacte. Je m'excuse si je représente mal certains concepts._

## Gestionnaires de complétion

![Image](https://www.freecodecamp.org/news/content/images/2019/10/pheobe.jpeg)
_Pauvre patiente Pheobe_

Vous vous souvenez de l'épisode de Friends où Pheobe est collée au téléphone pendant des jours en attendant de parler avec le service client ? Imaginez si, au tout début de cet appel téléphonique, une personne charmante nommée Pip disait : "Merci d'avoir appelé. Je ne sais pas combien de temps vous devrez attendre en ligne, mais je vous rappellerai lorsque nous serons prêts pour vous." Cela n'aurait pas été aussi drôle, mais Pip offre de devenir un gestionnaire de complétion pour Pheobe.

Vous utilisez un gestionnaire de complétion dans une fonction lorsque vous savez que cette fonction prendra un certain temps à s'exécuter. Vous ne savez pas combien de temps cela prendra, et vous ne voulez pas mettre votre vie en pause en attendant qu'elle se termine. Vous demandez donc à Pip de vous taper sur l'épaule lorsqu'elle est prête à vous donner la réponse. Ainsi, vous pouvez vaquer à vos occupations, faire des courses, lire un livre et regarder la télévision. Lorsque Pip vous tape sur l'épaule avec la réponse, vous pouvez prendre sa réponse et l'utiliser.

C'est ce qui se passe avec les appels API. Vous envoyez une requête URL à un serveur, lui demandant des données. Vous espérez que le serveur renvoie les données rapidement, mais vous ne savez pas combien de temps cela prendra. Au lieu de faire attendre patiemment votre utilisateur que le serveur vous donne les données, vous utilisez un gestionnaire de complétion. Cela signifie que vous pouvez dire à votre application d'aller faire d'autres choses, comme charger le reste de la page.

Vous dites au gestionnaire de complétion de taper sur l'épaule de votre application une fois qu'il a l'information que vous voulez. Vous pouvez spécifier ce que cette information est. Ainsi, lorsque votre application se fait taper sur l'épaule, elle peut prendre l'information du gestionnaire de complétion et faire quelque chose avec. Habituellement, ce que vous ferez, c'est recharger la vue de tableau pour que les données apparaissent à l'utilisateur.

Voici un exemple de ce à quoi ressemble un gestionnaire de complétion. Le premier exemple montre la configuration de l'appel API lui-même :

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
  // Configurer la variable lotsOfFilms
  var lotsOfFilms: [Film]
  
  // Appeler l'API avec du code
  
  // Utiliser les données de l'API pour assigner une valeur à lotsOfFilms  
  
  // Donner au gestionnaire de complétion la variable lotsOfFilms
  completionHandler(lotsOfFilms)
}
```

Maintenant, nous voulons appeler la fonction `fetchFilms`. Quelques points à noter :

* Vous n'avez pas besoin de référencer `completionHandler` lorsque vous appelez la fonction. La seule fois où vous référencez `completionHandler`, c'est à l'intérieur de la déclaration de la fonction.
* Le gestionnaire de complétion nous retournera des données à utiliser. Basé sur la fonction que nous avons écrite ci-dessus, nous savons que nous devons nous attendre à des données de type `[Film]`. Nous devons nommer les données afin de pouvoir nous y référer. Ci-dessous, j'utilise le nom `films`, mais cela pourrait être `randomData`, ou tout autre nom de variable que je souhaite.

Le code ressemblera à quelque chose comme ceci :

```swift
fetchFilms() { (films) in
  // Faire quelque chose avec les données que le gestionnaire de complétion retourne
  print(films)
}
```

## URLSession

`URLSession` est comme le gestionnaire d'une équipe. Le gestionnaire ne fait rien par lui-même. Son travail est de partager le travail avec les membres de son équipe, et ils feront le travail. Son équipe est composée de `dataTasks`. Chaque fois que vous avez besoin de données, écrivez au patron et utilisez `URLSession.shared.dataTask`.

Vous pouvez donner à `dataTask` différents types d'informations pour vous aider à atteindre votre objectif. Donner des informations à `dataTask` s'appelle l'initialisation. J'initialise mes `dataTasks` avec des URLs. Les `dataTasks` utilisent également des gestionnaires de complétion dans le cadre de leur initialisation. Voici un exemple :

```swift
let url = URL(string: "https://www.swapi.co/api/films")

let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in 
  // votre code ici
})

task.resume()
```

Les `dataTasks` utilisent des gestionnaires de complétion, et ils retournent toujours les mêmes types d'informations : `data`, `response` et `error`. Vous pouvez donner à ces types de données différents noms, comme `(data, res, err)` ou `(someData, someResponse, someError)`. Pour des raisons de convention, il est préférable de s'en tenir à quelque chose d'évident plutôt que de s'écarter avec de nouveaux noms de variables.

Commençons par `error`. Si le `dataTask` retourne une `error`, vous voudrez le savoir dès le départ. Cela signifie que vous pouvez diriger votre code pour gérer l'erreur avec élégance. Cela signifie également que vous ne vous donnerez pas la peine d'essayer de lire les données et de faire quelque chose avec elles, car il y a une erreur dans le retour des données.

Ci-dessous, je gère l'erreur très simplement en imprimant une erreur dans la console et en quittant la fonction. Il existe de nombreuses autres façons de gérer l'erreur si vous le souhaitez. Réfléchissez à la manière dont ces données sont fondamentales pour votre application. Par exemple, si vous avez une application bancaire et que cet appel API montre aux utilisateurs leur solde, vous voudrez peut-être gérer l'erreur en présentant une modale à l'utilisateur qui dit : "Désolé, nous rencontrons un problème en ce moment. Veuillez réessayer plus tard."

```swift
if let error = error {
  print("Erreur d'accès à swapi.co : /(error)")
  return
}
```

Ensuite, nous examinons la réponse. Vous pouvez convertir la réponse en `httpResponse`. Ainsi, vous pouvez examiner les codes d'état et prendre certaines décisions en fonction du code. Par exemple, si le code d'état est 404, alors vous savez que la page n'a pas été trouvée.

Le code ci-dessous utilise un `guard` pour vérifier que deux choses existent. Si les deux existent, alors il permet au code de continuer à l'instruction suivante après la clause `guard`. Si l'une des déclarations échoue, alors nous quittons la fonction. C'est un cas d'utilisation typique d'une clause `guard`. Vous vous attendez à ce que le code après une clause guard soit le flux des jours heureux (c'est-à-dire le flux facile sans erreurs).

```swift
  guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
    print("Erreur avec la réponse, code d'état inattendu : \(response)")
    return
  }
```

Enfin, vous gérez les données elles-mêmes. Remarquez que nous n'avons pas utilisé le gestionnaire de complétion pour l'`error` ou la `response`. C'est parce que le gestionnaire de complétion attend des données de l'API. S'il n'atteint pas la partie des données du code, il n'y a pas besoin d'invoquer le gestionnaire.

Pour les données, nous utilisons le `JSONDecoder` pour analyser les données de manière agréable. C'est assez ingénieux, mais nécessite que vous ayez établi un modèle. Notre modèle s'appelle `FilmSummary`. Si `JSONDecoder` est nouveau pour vous, alors jetez un coup d'œil en ligne pour savoir comment l'utiliser et comment utiliser `Codable`. C'est vraiment simple dans Swift 4 et au-dessus par rapport aux jours de Swift 3.

Dans le code ci-dessous, nous vérifions d'abord que les données existent. Nous sommes assez sûrs qu'elles devraient exister, car il n'y a pas d'erreurs et pas de réponses HTTP étranges. Ensuite, nous vérifions que nous pouvons analyser les données que nous recevons de la manière dont nous nous y attendons. Si nous le pouvons, alors nous retournons le résumé du film au gestionnaire de complétion. Au cas où il n'y aurait pas de données à retourner de l'API, nous avons un plan de secours avec un tableau vide.

```swift
if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
```

Ainsi, le code complet pour l'appel API ressemble à ceci :

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
    let url = URL(string: domainUrlString + "films/")!

    let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in
      if let error = error {
        print("Erreur lors de la récupération des films : \(error)")
        return
      }
      
      guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
        print("Erreur avec la réponse, code d'état inattendu : \(response)")
        return
      }

      if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
    })
    task.resume()
  }
```

## Cycles de rétention

_NB : Je suis extrêmement nouveau dans la compréhension des cycles de rétention ! Voici l'essentiel de ce que j'ai recherché en ligne._

Les cycles de rétention sont importants à comprendre pour la gestion de la mémoire. Fondamentalement, vous voulez que votre application nettoie les morceaux de mémoire dont elle n'a plus besoin. Je suppose que cela rend l'application plus performante.

Il y a beaucoup de façons dont Swift vous aide à faire cela automatiquement. Cependant, il y a de nombreuses façons dont vous pouvez accidentellement coder des cycles de rétention dans votre application. Un cycle de rétention signifie que votre application conservera toujours la mémoire pour un certain morceau de code. Généralement, cela se produit lorsque vous avez deux choses qui ont des pointeurs forts l'une vers l'autre.

Pour contourner cela, les gens utilisent souvent `weak`. Lorsque l'un des côtés du code est `weak`, vous n'avez pas de cycle de rétention et votre application pourra libérer la mémoire.

Pour notre usage, un modèle courant est d'utiliser `[weak self]` lors de l'appel de l'API. Cela garantit que, une fois que le gestionnaire de complétion retourne un certain code, l'application peut libérer la mémoire.

```swift
fetchFilms { [weak self] (films) in
  // code ici
}
```

## DispatchQueue

Xcode utilise différents threads pour exécuter du code en parallèle. L'avantage des threads multiples signifie que vous n'êtes pas bloqué en attendant qu'une chose se termine avant de pouvoir passer à la suivante. Espérons que vous commencez à voir les liens avec les gestionnaires de complétion ici.

Ces threads semblent également être appelés files d'attente de distribution. Les appels API sont gérés sur une file d'attente, généralement une file d'attente en arrière-plan. Une fois que vous avez les données de votre appel API, il est probable que vous souhaitiez montrer ces données à l'utilisateur. Cela signifie que vous voudrez actualiser votre vue de tableau.

Les vues de tableau font partie de l'interface utilisateur, et toutes les manipulations de l'interface utilisateur doivent être effectuées dans la file d'attente de distribution principale. Cela signifie que quelque part dans votre fichier de contrôleur de vue, généralement dans le cadre de la fonction `viewDidLoad`, vous devez avoir un morceau de code qui indique à votre vue de tableau de s'actualiser.

Nous voulons que la vue de tableau s'actualise uniquement lorsqu'elle a de nouvelles données de l'API. Cela signifie que nous utiliserons un gestionnaire de complétion pour nous taper sur l'épaule et nous dire quand cet appel API est terminé. Nous attendrons ce signal avant d'actualiser le tableau.

Le code ressemblera à quelque chose comme ceci :

```swift
fetchFilms { [weak self] (films) in
  self.films = films

  // Recharger la vue de tableau en utilisant la file d'attente de distribution principale
  DispatchQueue.main.async {
    tableView.reloadData()
  }
}
```

## viewDidLoad vs viewDidAppear

Enfin, vous devez décider où appeler votre fonction `fetchfilms`. Elle sera à l'intérieur d'un contrôleur de vue qui utilisera les données de l'API. Il y a deux endroits évidents où vous pourriez faire cet appel API. L'un est à l'intérieur de `viewDidLoad` et l'autre est à l'intérieur de `viewDidAppear`.

Ce sont deux états différents pour votre application. Ma compréhension est que `viewDidLoad` est appelé la première fois que vous chargez cette vue au premier plan. `viewDidAppear` est appelé chaque fois que vous revenez à cette vue, par exemple lorsque vous appuyez sur le bouton de retour pour revenir à la vue.

Si vous vous attendez à ce que vos données changent entre les moments où l'utilisateur naviguera vers et depuis cette vue, alors vous voudrez peut-être placer votre appel API dans `viewDidAppear`. Cependant, je pense que pour presque toutes les applications, `viewDidLoad` est suffisant. Apple recommande `viewDidAppear` pour tous les appels API, mais cela semble excessif. J'imagine que cela rendrait votre application moins performante car elle ferait beaucoup plus d'appels API que nécessaire.

## Combiner toutes les étapes

Premièrement : écrire la fonction qui appelle l'API. Ci-dessus, il s'agit de `fetchFilms`. Cela aura un gestionnaire de complétion, qui retournera les données qui vous intéressent. Dans mon exemple, le gestionnaire de complétion retourne un tableau de films.

Deuxièmement : appeler cette fonction dans votre contrôleur de vue. Vous faites cela ici parce que vous voulez mettre à jour la vue en fonction des données de l'API. Dans mon exemple, j'actualise une vue de tableau une fois que l'API retourne les données.

Troisièmement : décider où dans votre contrôleur de vue vous souhaitez appeler la fonction. Dans mon exemple, je l'appelle dans `viewDidLoad`.

Quatrièmement : décider quoi faire avec les données de l'API. Dans mon exemple, j'actualise une vue de tableau.

À l'intérieur de `NetworkManager.swift` (cette fonction peut être définie dans votre contrôleur de vue si vous le souhaitez, mais j'utilise le modèle MVVM).

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
    let url = URL(string: domainUrlString + "films/")!

    let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in
      if let error = error {
        print("Erreur lors de la récupération des films : \(error)")
        return
      }
      
      guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
        print("Erreur avec la réponse, code d'état inattendu : \(response)")
        return
      }

      if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
    })
    task.resume()
  }
```

À l'intérieur de `FilmsViewController.swift` :

```swift
final class FilmsViewController: UIViewController {
  private var films: [Film]?

  override func viewDidLoad() {
    super.viewDidLoad()
    
    NetworkManager().fetchFilms { [weak self] (films) in
      self?.films = films
      DispatchQueue.main.async {
        self?.tableView.reloadData()
      }
    }
  }
  
  // autre code pour le contrôleur de vue
}
```

Bon sang, nous y sommes arrivés ! Merci de m'avoir suivi.