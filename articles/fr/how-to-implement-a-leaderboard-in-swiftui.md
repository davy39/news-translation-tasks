---
title: Comment implémenter un tableau des scores GameKit dans SwiftUI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-19T21:00:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-leaderboard-in-swiftui
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/IMG_45B142A26F90-1-copy.jpeg
tags:
- name: Apple
  slug: apple
- name: Games
  slug: games
- name: iOS
  slug: ios
- name: Swift
  slug: swift
- name: SwiftUI
  slug: swiftui
seo_title: Comment implémenter un tableau des scores GameKit dans SwiftUI
seo_desc: "By Saamer Mansoor\nIn this article we will talk about why and how to implement\
  \ the GameCenter's Leaderboard within your app. \nWhy GameCenter is Making a Huge\
  \ Revival\nYou can make iPhone games without a scoreboard, but leaderboards can\
  \ help make the ga..."
---

Par Saamer Mansoor

Dans cet article, nous allons parler de pourquoi et comment implémenter le [Tableau des scores de GameCenter](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/leaderboards/) dans votre application. 

## Pourquoi GameCenter connaît un énorme regain d'intérêt

Vous pouvez créer des jeux iPhone sans tableau des scores, mais les tableaux des scores peuvent aider à rendre le jeu plus compétitif, comme si les gens concouraient les uns contre les autres dans le monde entier. 

Au lieu de créer et de gérer votre propre backend, le Tableau des scores GameCenter vous permet de scalabiliser infiniment avec le trafic, de sauter une page de connexion entière pour l'autorisation, d'obtenir l'image, le nom et les amis jouant au même jeu – tout cela sans que vos utilisateurs aient à entrer quoi que ce soit. 

Surtout avec iOS 16, [Apple investit davantage pour l'améliorer](https://developer.apple.com/game-center/), et stimule davantage l'utilisation des applications, comme par le biais de notifications push lorsque votre ami bat votre score dans le jeu.

Dans mon parcours d'apprentissage de SwiftUI, j'ai créé et publié des applications, car selon moi c'est la meilleure façon d'apprendre. 

Il n'y avait pas beaucoup de documentation mise à jour sur la façon de faire tout cela, surtout aucune avec SwiftUI ni avec [l'avènement de async et await en Swift](https://www.freecodecamp.org/news/make-rest-api-call-in-swiftui-in-2-minutes/). J'ai donc consolidé et simplifié cela pour que tout le monde puisse créer des applications incroyables. N'hésitez pas à m'inviter à tester vos applications aussi !

### Prérequis :

* Vous aurez besoin d'un compte [Apple Developer](https://developer.apple.com/programs/) payant
* Vous devez créer l'[ID de l'application pour votre app](https://support.magplus.com/hc/en-us/articles/203808708-iOS-Creating-App-IDs) dans la section des profils de provisionnement du portail Apple Developer
* Vous devez [créer l'application dans le portail iTunes Connect](https://support.staffbase.com/hc/en-us/articles/115003481992-Creating-an-App-Profile-in-App-Store-Connect)

## Comment implémenter votre tableau des scores iOS en 6 étapes

La plupart de la logique de code pour le tableau des scores se trouve dans [ce fichier si vous voulez passer directement à cette partie](https://github.com/StairMasterClimber/mobile/blob/main/StairStepperMaster/StairStepperMaster/Views/LeadersTileView.swift). Voici les étapes à suivre :

### 1. Comment créer le tableau des scores dans App Store Connect

![image](https://user-images.githubusercontent.com/8262287/180824532-2e27ca8a-c1c0-4676-b439-f3ab09887271.png)
_Capture d'écran du portail Apple iTunes Connect_

Une fois que vous avez créé l'application dans le portail App Store Connect avec succès, allez dans l'onglet Services pour l'application -> et assurez-vous d'être dans la page GameCenter.

Ensuite, ajoutez un nouveau tableau des scores en utilisant le signe "+", qui peut être soit "Classique" (les scores ne sont jamais réinitialisés) soit "Récurrent" (les scores sont réinitialisés selon vos paramètres de fréquence).

La plupart des jeux préfèrent un tableau des scores récurrent afin que le tableau des scores ne soit pas encombré par d'anciens scores élevés impossibles à atteindre.

L'ID du tableau des scores que vous entrez là est celui que vous devez utiliser dans tous les endroits du code qui le demandent.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-122.png)
_Informations requises pour créer un nouveau tableau des scores_

### 2. Comment configurer l'authentification GameCenter

Tout d'abord, vous devrez authentifier les utilisateurs auprès de GameCenter pour que l'une de ces fonctionnalités puisse fonctionner.

Nous utiliserons donc ce code pour cela, qui vérifie essentiellement que vous (GKLocalPlayer.local) êtes authentifié, ou imprime une erreur s'il y en a une :

```
func authenticateUser() {
    GKLocalPlayer.local.authenticateHandler = { vc, error in
        guard error == nil else {
            print(error?.localizedDescription ?? "")
            return
        }
    }
}

```

Si l'utilisateur est authentifié, vous verrez une petite fenêtre contextuelle dans l'interface utilisateur. Sinon, l'utilisateur sera redirigé vers une page pour se connecter à son compte GameCenter.

![image](https://user-images.githubusercontent.com/8262287/180823235-cafefcfa-3d25-46e5-8524-d7f475b9a000.png)
_Un signe qui s'affiche lorsqu'un utilisateur est connecté_

### 3. Comment afficher les éléments du tableau des scores dans l'interface utilisateur

Pour obtenir les données du contrôleur de vue du tableau des scores de GameCenter (GKLeaderboard), vous devez utiliser `loadLeaderboards`.

Vous pouvez changer la fonction `loadEntries` de `.global` à `.friends` pour ne récupérer que vos amis.

Vous pouvez également récupérer l'image de chaque joueur en itérant sur chaque joueur et en effectuant un `loadPhoto`.

En utilisant `NSRang(1...5)`, vous pouvez choisir combien de joueurs afficher. Cela récupère les utilisateurs avec les 5 meilleurs scores du tableau des scores et ne retourne rien s'il n'y a pas d'utilisateurs, comme dans le cas où le cycle se rafraîchit pour un tableau des scores récurrent.

Voici à quoi pourrait ressembler la récupération de données depuis un tableau des scores si vous utilisez async-await :

```
func loadLeaderboard() async {
    playersList.removeAll()
    Task{
        var playersListTemp : [Player] = []
        let leaderboards = try await GKLeaderboard.loadLeaderboards(IDs: [leaderboardIdentifier])
        if let leaderboard = leaderboards.filter ({ $0.baseLeaderboardID == self.leaderboardIdentifier }).first {
            let allPlayers = try await leaderboard.loadEntries(for: .global, timeScope: .allTime, range: NSRange(1...5))
            if allPlayers.1.count > 0 {
                try await allPlayers.1.asyncForEach { leaderboardEntry in
                    var image = try await leaderboardEntry.player.loadPhoto(for: .small)
                    playersListTemp.append(Player(name: leaderboardEntry.player.displayName, score:leaderboardEntry.formattedScore, image: image))
                                print(playersListTemp)
                    playersListTemp.sort{
                        $0.score < $1.score
                    }
                }
            }
        }
        playersList = playersListTemp            
    }
}

```

![image](https://user-images.githubusercontent.com/8262287/180823292-2dee4f9a-4894-4442-9241-2ad1c84b1cf7.png)
_Vous pouvez obtenir les données du tableau des scores dans votre application_

### 4. Comment appeler la fonctionnalité dans SwiftUI lorsque la vue/page apparaît

Vous pouvez tirer parti de la fonction de cycle de vie `onAppear` [de la vue](https://www.hackingwithswift.com/quick-start/swiftui/how-to-respond-to-view-lifecycle-events-onappear-and-ondisappear) pour effectuer les appels d'authentification et de chargement, mais vous pouvez également le faire au toucher d'un bouton si vous préférez :

```
.onAppear(){
    if !GKLocalPlayer.local.isAuthenticated {
        authenticateUser()
    } else if playersList.count == 0 {
        Task{
            await loadLeaderboard()
        }
    }
}

```

### 5. Comment charger les scores soumis

Pour charger les scores, vous devez également les soumettre. La fonction `submitScore` peut vous aider à faire cela.

* La variable `flightsClimbed` doit contenir le score que vous souhaitez soumettre.
* GameKit s'assure de n'afficher que votre meilleur score pour la durée de vie du tableau des scores.
* L'`leaderboardId` contient la valeur que vous entrez manuellement dans votre compte App Store Connect :

```
func leaderboard() async{
    Task{
        try await GKLeaderboard.submitScore(
            flightsClimbed,
            context: 0,
            player: GKLocalPlayer.local,
            leaderboardIDs: ["com.tfp.stairsteppermaster.flights"]
        )
    }
    calculateAchievements()
}
```

### 6. Comment afficher le portail du contrôleur de vue GameCenter

Lorsque vous êtes connecté à GameCenter, une petite icône gênante apparaît en haut à droite de votre écran. Lorsque vous appuyez dessus, vous êtes redirigé vers le contrôleur de vue GameCenter. Heureusement, vous pouvez la masquer si elle ne fait pas partie de votre design, en utilisant `GKAccessPoint.shared.isActive = false`.

Puisque l'interface utilisateur de GameCenter est un `ViewController` UIKit et non une simple `View` SwiftUI, vous devez d'abord créer ce [UIViewControllerRepresentable](https://www.hackingwithswift.com/books/ios-swiftui/wrapping-a-uiviewcontroller-in-a-swiftui-view) (comme vous pouvez [le voir ici](https://github.com/StairMasterClimber/mobile/blob/main/StairStepperMaster/StairStepperMaster/Views/GameCenterView.swift)), pour lancer GameCenter en utilisant un bouton différent.

Une fois que vous avez ajouté ce fichier à votre projet, vous pouvez afficher le portail GameCenter simplement en utilisant ceci : `GameCenterView(format: gameCenterViewControllerState)` où gameCenterViewControllerState peut vous aider à accéder à une page de détail dans GameCenter.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Frame-3-3.png)
_Vue du tableau des scores de GameCenter_

## Points à garder à l'esprit lors de l'utilisation des tableaux des scores de GameCenter :

* Débogage du simulateur – Pour une raison quelconque, l'authentification auprès de GameCenter est extrêmement lente sur un simulateur, il peut donc être judicieux de créer une maquette de données lors de l'utilisation du simulateur.
* Défis – Vous ne pouvez plus émettre de défis GameKit à vos amis de manière programmatique [en raison de la dépréciation](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallenge). Au lieu de cela, vous devez les faire manuellement dans le tableau de bord GameCenter de l'utilisateur contre les réalisations GameKit. De plus, il n'y a aucun moyen de voir les défis que vous avez envoyés.
* Réalisations – Les tableaux des scores sont différents des réalisations GameKit, qui sont calculées et affichées différemment, mais [beaucoup plus faciles](https://github.com/StairMasterClimber/mobile/blob/18283a68e1c5cac4e270a85b03853887b3950156/StairStepperMaster/StairStepperMaster/Views/AchievementTileView.swift#L113). Celles-ci peuvent également être intégrées dans l'application, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Frame-2-2.png)
_Défis et réalisations GameKit_

## Conclusion

Vous pouvez essayer l'application gratuite et open-source [Stair Master Climber iPhone Santé & Fitness](https://stairmasterclimber.com/app) que j'ai partagée ci-dessus. J'adorerais savoir ce que vous en pensez afin que nous puissions apprendre ensemble.

N'hésitez pas à me contacter sur les [réseaux sociaux](https://twitter.com/StairMasterApp) ou par [email](mailto:hi@stairmasterclimber.com) si vous avez des questions.