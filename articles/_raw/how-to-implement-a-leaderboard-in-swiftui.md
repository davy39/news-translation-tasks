---
title: How to Implement a GameKit Leaderboard in SwiftUI
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
seo_title: null
seo_desc: "By Saamer Mansoor\nIn this article we will talk about why and how to implement\
  \ the GameCenter's Leaderboard within your app. \nWhy GameCenter is Making a Huge\
  \ Revival\nYou can make iPhone games without a scoreboard, but leaderboards can\
  \ help make the ga..."
---

By Saamer Mansoor

In this article we will talk about why and how to implement the [GameCenter's Leaderboard](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/leaderboards/) within your app. 

## Why GameCenter is Making a Huge Revival

You can make iPhone games without a scoreboard, but leaderboards can help make the game feel more competitive, like people are competing against one another around the World. 

Instead of creating and managing your own backend, the GameCenter Leaderboard allows you to scale with traffic infinitely, skip an entire login page for authorization, get the Image, Name, and friends playing the same game – all without your users having to enter anything. 

Especially with iOS 16, [Apple is investing more in improving it](https://developer.apple.com/game-center/), and driving more app usage, like through Push Notifications when your friend beats your score in the game.

In my journey of learning SwiftUI, I have been creating and publishing apps, because IMO that's the best way to learn. 

There wasn't much updated documentation on how to do a lot of this, especially none with SwiftUI nor with the [advent of async and await in Swift](https://www.freecodecamp.org/news/make-rest-api-call-in-swiftui-in-2-minutes/). So I consolidated and simplified it for everyone to build amazing apps. So feel free to invite me to test your apps too!

### Pre-Requisites:

* You'll need to have an [Apple Developer](https://developer.apple.com/programs/) paid account
* You have to create the [App Id for your app](https://support.magplus.com/hc/en-us/articles/203808708-iOS-Creating-App-IDs) in the provisioning profiles section of the Apple Developer Portal
* You have to [create the App in the iTunes Connect Connect](https://support.staffbase.com/hc/en-us/articles/115003481992-Creating-an-App-Profile-in-App-Store-Connect) portal

## How to Implement Your iOS Leaderboard in 6 Steps

Most of the code logic for the leaderboard is in [this file if you want to skip ahead](https://github.com/StairMasterClimber/mobile/blob/main/StairStepperMaster/StairStepperMaster/Views/LeadersTileView.swift). Here's the steps as follows:

### 1. How to Create the App Store Connect Leaderboard

![image](https://user-images.githubusercontent.com/8262287/180824532-2e27ca8a-c1c0-4676-b439-f3ab09887271.png)
_Screenshot from the Apple iTunes Connect Portal_

Once you have created the app in the App Store Connect portal successfully, go to the Services tab for the app -> and make sure you're in the GameCenter page.

Then add a new leaderboard using the "+" sign, which can either be "Classic" (scores never reset) or "Recurring" (scores reset based on your frequency settings).

Most games prefer a recurring leaderboard so that the leaderboard isn't cluttered with older impossible to reach high scores.

The LeaderboardID you input there is the one that you need to use in all the places in the code that ask for it.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-122.png)
_Details required to create a new Leaderboard_

### 2. How to Set Up GameCenter Authentication

First, you'll need to authenticate users to GameCenter in order for any of this functionality to work.

So we'll use this code to do that, which basically makes sure that you (GKLocalPlayer.local) are authenticated, or prints an error if there is one:

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

If the user is authenticated, you will see a little popup in the UI. If not, the user will be taken to a page to login to their GameCenter account.

![image](https://user-images.githubusercontent.com/8262287/180823235-cafefcfa-3d25-46e5-8524-d7f475b9a000.png)
_A sign that displays when a user is logged in_

### 3. How to Display Leaderboard Items in the UI

In order to get the data away from the GameCenter ViewController leaderboards (GKLeaderboard), you need to use the `loadLeaderboards` . 

You can switch up the `loadEntries` function from `.global` to `.friends` in order to only pull your friends. 

You can also retrieve the image for each player by iterating over each player and performing a `loadPhoto`. 

Using `NSRang(1...5)`, you can choose how many players to display. This pulls the users with the highest 5 scores from the leaderboard and returns none if there's no users, such as in the case when the cycle refreshes for a recurring Leaderboard.

This is what pulling data from a leaderboard could look like if you take advantage of async-await:

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
_You can get leaderboard data into your app_

### 4. How to Call Functionality in SwiftUI as the View/Page Appears

You can take advantage of the `onAppear` [lifecycle function of the view](https://www.hackingwithswift.com/quick-start/swiftui/how-to-respond-to-view-lifecycle-events-onappear-and-ondisappear) to actually make the calls to authenticate and load, but you can also do it on the tap of a button if you prefer that:

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

### 5. How to Load the Submitted Scores

In order to load the scores, you need to submit them as well. The `submitScore` function can help you with that.

* The `flightsClimbed` variable should contain the score that you would like to submit.
* GameKit makes sure to only display your best score for the life of the leaderboard.
* The `leaderboardId` contains the value that you manually enter in your App Store Connect account:

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

### 6. How to display the GameCenter ViewController Portal

When you're logged into GameCenter, a little annoying icon appears in the top right of your screen. When you tap on it, you are taken to the GameCenter ViewController. Luckily you can hide it if it's not part of your design, using `GKAccessPoint.shared.isActive = false`. 

Since the GameCenter UI is a UIKit `ViewController` and not a simple SwiftUI `View`, you need to create this [UIViewControllerRepresentable](https://www.hackingwithswift.com/books/ios-swiftui/wrapping-a-uiviewcontroller-in-a-swiftui-view) first (as you can [see here](https://github.com/StairMasterClimber/mobile/blob/main/StairStepperMaster/StairStepperMaster/Views/GameCenterView.swift)), to launch GameCenter using a different button, 

Once you add that file to your project, you can display the GameCenter portal simply using this: `GameCenterView(format: gameCenterViewControllerState)` where gameCenterViewControllerState can be help you go to a detail page in GameCenter.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Frame-3-3.png)
_GameCenter's Leaderboard View_

## Things to Keep in Mind While using GameCenter's Leaderboards:

* Simulator Debugging – For some reason the authenticate to GameCenter is extremely slow on a simulator, so it might make sense to even create a mock of data when using the simulator.
* Challenges – You can't programmatically issue GameKit Challenges to your friends anymore [due to deprecation](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallenge). Instead, you have to do those manually within the user's GameCenter dashboard against GameKit Achievements. Also, there's no way to view challenges you have sent. 
* Achievements – Leaderboards are different from the GameKit Achievements, which is calculated and displayed differently, but a [lot easier](https://github.com/StairMasterClimber/mobile/blob/18283a68e1c5cac4e270a85b03853887b3950156/StairStepperMaster/StairStepperMaster/Views/AchievementTileView.swift#L113). Those can also be pulled into the app as well, as you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Frame-2-2.png)
_GameKit Challenges and Achievements_

## Wrapping Up

You can try out the free open-source [Stair Master Climber iPhone Health & Fitness app](https://stairmasterclimber.com/app) that I shared above. I would love to know what you think so that we can learn together. 

Feel free to reach out to me on [social media](https://twitter.com/StairMasterApp) or by [email](mailto:hi@stairmasterclimber.com) if you have any questions.

