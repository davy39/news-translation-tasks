---
title: Comment configurer des histoires vidéo de type Instagram dans votre application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-22T22:01:31.000Z'
originalURL: https://freecodecamp.org/news/video-stories-and-caching-ios
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/1_gYkQNP0BaohLJ8hDKL1C6w-1.jpeg
tags:
- name: app development
  slug: app-development
- name: caching
  slug: caching
- name: ios app development
  slug: ios-app-development
- name: video
  slug: video
seo_title: Comment configurer des histoires vidéo de type Instagram dans votre application
seo_desc: 'By Agam Mahajan

  The article will teach you how you can show multiple videos in one view, like we
  see in Instagram Stories.

  We''ll also learn how to cache the videos in the user''s device to help save that
  user''s data and network calls and smooth out th...'
---

Par Agam Mahajan

Cet article vous apprendra à afficher plusieurs vidéos dans une seule vue, comme on le voit dans les Stories Instagram.

Nous apprendrons également comment mettre en cache les vidéos sur l'appareil de l'utilisateur pour aider à économiser ses données et les appels réseau, et améliorer son expérience.

Une note rapide : cette implémentation est pour iOS, mais la même logique peut être appliquée dans d'autres bases de code.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/ezgif.com-video-to-gif--5-.gif)

En général, chaque fois que nous voulons lire une vidéo, nous obtenons l'URL de la vidéo et présentons simplement `**AVPlayerViewController**` avec cette URL.

```swift
let videoURL = URL(string: "Sample-Video-Url")
let player = AVPlayer(url: videoURL!)
let playerViewController = AVPlayerViewController()
playerViewController.player = player
self.present(playerViewController, animated: true) {
    playerViewController.player.play()
}
```

Assez simple, n'est-ce pas ?

Mais l'inconvénient de cette implémentation est que vous **ne pouvez pas** la **personnaliser**. Ce qui, si vous travaillez pour une bonne entreprise de produits, sera une demande quotidienne. :D

Alternativement, nous pouvons utiliser `**AVPlayerLayer**` qui fera un travail similaire – mais il nous permet de personnaliser la vue et d'autres éléments.

```swift
let videoURL = URL(string: "Sample-Video-Url")
let player = AVPlayer(url: videoURL!)
let playerLayer = AVPlayerLayer(player: player)
playerLayer.frame = self.view.bounds
self.view.layer.addSublayer(playerLayer)
player.play()
```

Mais que faire si vous voulez combiner plusieurs vidéos, similaires aux **stories Instagram** ? Alors nous devons probablement approfondir un peu.

## Revenons à l'énoncé du problème

Maintenant, laissez-moi vous parler de mon cas d'utilisation.

Dans mon entreprise, Swiggy, nous voulons pouvoir afficher plusieurs vidéos, où chaque vidéo doit être montrée un certain nombre de fois.

En plus de cela, cela doit avoir une fonctionnalité de stories de type Instagram.

* La vidéo-2 doit se lire automatiquement de manière transparente après la vidéo-1, et ainsi de suite
* Elle doit sauter vers les vidéos correspondantes lorsque l'utilisateur appuie sur la gauche ou la droite.

Si vous pensez que la mise en cache pourrait être la réponse, ne vous inquiétez pas – j'y viendrai dans un instant.

### Plusieurs couches dans une seule vue

Tout d'abord, nous devons déterminer comment ajouter plusieurs vidéos dans une seule vue.

Ce que nous pouvons faire, c'est créer une seule `**AVPlayerLayer**` et lui assigner la première vidéo. Lorsque la première vidéo est terminée, nous assignons la vidéo suivante à la même `**AVPlayerLayer**`.

```swift
func addPlayer(player: AVPlayer) {
    player.currentItem?.seek(to: CMTime.zero, completionHandler: nil)
    playerViewModel?.player = player
    playerView.playerLayer.player = player
}
```

Pour sauter vers la vidéo précédente ou suivante, nous pouvons faire ce qui suit :

* Ajouter un geste de tapotement sur la vue
* Si l'emplacement du toucher 'x' est inférieur à la moitié de l'écran, alors assigner la vidéo précédente, sinon assigner la vidéo suivante

```swift
@objc func didTapSnap(_ sender: UITapGestureRecognizer) {
   let touchLocation = sender.location(ofTouch: 0, in: view)
   if touchLocation.x < view.frame.width/2 {
     changePlayer(forward: false)
     } 
   else {
     fillupLastPlayedSnap()
     changePlayer(forward: true)
    }
}
```

Nous y voilà. Nous avons maintenant notre propre fonctionnalité de vidéo Stories de type Insta.

%[https://youtu.be/13ZwNq4FnbM]

Mais notre tâche n'est pas encore terminée !

## Revenons à la mise en cache

Nous ne voulons pas que chaque fois qu'un utilisateur navigue d'une vidéo à une autre, elle commence à télécharger la vidéo depuis le début.

De plus, si la vidéo est montrée à nouveau dans la prochaine session, nous n'avons pas besoin de faire un autre appel serveur.

Si nous pouvons mettre en cache la vidéo, alors l'internet de l'utilisateur sera économisé. La charge sur le serveur sera également réduite.

Enfin, l'UX s'améliorera car l'utilisateur n'aura pas à attendre longtemps pour charger la vidéo.

**En tant que bon développeur, réduire l'utilisation d'internet d'un utilisateur devrait être notre priorité.**

![Image](https://www.freecodecamp.org/news/content/images/2024/08/less-data-usage-happy-customer.jpg)
_Moins d'utilisation de données, client heureux_

### Charger les vidéos **de manière asynchrone**

La première chose que nous pouvons utiliser pour charger les vidéos est **loadValuesAsynchronously**.

Selon [la documentation Apple](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronously), **loadValuesAsynchronously** :

> _Indique à l'actif de charger les valeurs de toutes les clés spécifiées (noms de propriétés) qui ne sont pas déjà chargées._

L'avantage ici est qu'il économise la vidéo jusqu'à ce qu'elle soit rendue. Ainsi, il ne téléchargera pas la vidéo depuis le début chaque fois que l'utilisateur navigue vers une vidéo précédente. Il ne téléchargera que la partie qui n'a pas été rendue précédemment.

**Regardons un exemple** : disons que nous avons Video_1 qui dure 15 secondes, et l'utilisateur a vu 10 secondes de cette vidéo avant de sauter à Video_2.

Maintenant, si l'utilisateur revient à Video_1 en appuyant à gauche, **loadValuesAsynchronously** aura ces 10 secondes de vidéo enregistrées et ne téléchargera que les 5 secondes restantes (non regardées).

```swift
func asynchronouslyLoadURLAssets(_ newAsset: AVURLAsset) {
	DispatchQueue.main.async {
            newAsset.loadValuesAsynchronously(forKeys: self.assetKeysRequiredToPlay) {
                for key in self.assetKeysRequiredToPlay {
                    var error: NSError?
                    if newAsset.statusOfValue(forKey: key, error: &error) == .failed {
                        self.delegate?.playerDidFailToPlay(message: "Impossible d'utiliser cet AVAsset car l'une de ses clés a échoué à se charger")
                        return
                    }
                }

                if !newAsset.isPlayable || newAsset.hasProtectedContent {
                    self.delegate?.playerDidFailToPlay(message: "Impossible d'utiliser cet AVAsset car il n'est pas lisible ou contient du contenu protégé")
                    return
                }
                let currentItem = AVPlayerItem(asset: newAsset)
                let currentPlayer = AVPlayer(playerItem: currentItem)
                self.delegate?.playerDidSuccesToPlay(playerDetail: currentPlayer)
            }

        }
```

Vous pouvez trouver plus de détails sur **loadValuesAsynchronously** à ce [lien](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronously).

Le piège ici est qu'il persiste les données vidéo pour cette session uniquement. Si l'utilisateur ferme et revient à l'application, la vidéo doit être téléchargée à nouveau.

Alors, quelles autres options avons-nous ?

### Enregistrer les vidéos sur l'appareil

Maintenant, vient **la mise en cache des vidéos** !

Lorsque la vidéo est entièrement rendue, nous pouvons exporter la vidéo et l'enregistrer sur l'appareil de l'utilisateur. Lorsque la vidéo réapparaît dans leur prochaine session, nous pouvons récupérer la vidéo de l'appareil et simplement la charger.

**AVAssetExportSession**
Selon [la documentation Apple](https://developer.apple.com/documentation/avfoundation/avassetexportsession) :

> _Un objet qui transcodifie le contenu d'un objet source d'actif pour créer une sortie de la forme décrite par un préréglage d'exportation spécifié._

Cela signifie que AVAssetExportSession agit comme un exportateur, grâce auquel nous pouvons enregistrer le fichier sur l'appareil de l'utilisateur. Nous devons donner l'URL de sortie et le type de fichier de sortie.

```swift
let exporter = AVAssetExportSession(asset: avUrlAsset, presetName: AVAssetExportPresetHighestQuality)
exporter?.outputURL = outputURL
exporter?.outputFileType = AVFileType.mp4

exporter?.exportAsynchronously(completionHandler: {
	print(exporter?.status.rawValue)
	print(exporter?.error)
})
```

Vous pouvez trouver plus de détails sur **AVAssetExportSession** à ce [lien](https://developer.apple.com/documentation/avfoundation/avassetexportsession).

Maintenant, la seule chose restante est de récupérer les données du cache et de charger la vidéo.

Avant de charger, vérifiez si la vidéo est présente dans le cache. Ensuite, récupérez cette URL locale et donnez-la à **loadValuesAsynchronously.**

```swift
if let cacheUrl = FindCachedVideoURL(forVideoId: videoId) {
	let cacheAsset = AVURLAsset(url: cacheUrl)
	asynchronouslyLoadURLAssets(cacheAsset)
}
else {
  asynchronouslyLoadURLAssets(newAsset)
}
```

La mise en cache aidera à réduire beaucoup l'utilisation des données de l'utilisateur ainsi que la charge du serveur (parfois jusqu'à des To de données).

## Autres cas d'utilisation pour la mise en cache

Quels autres cas d'utilisation pouvons-nous gérer avec la mise en cache ? Voici des exemples de façons dont vous pourriez utiliser la mise en cache ici :

### Assurer un stockage optimal

Avant d'enregistrer la vidéo sur l'appareil, vous devez vérifier si suffisamment d'espace de stockage est présent sur l'appareil pour le faire.

```swift
func isStorageAvailable() -> Bool {
   let fileURL = URL(fileURLWithPath: NSHomeDirectory() as String)
   do {
      let values = try fileURL.resourceValues(forKeys: [.volumeAvailableCapacityForImportantUsageKey, .volumeTotalCapacityKey])
      guard let totalSpace = values.volumeTotalCapacity,
      let freeSpace = values.volumeAvailableCapacityForImportantUsage else {
          return false
      }
      if freeSpace > minimumSpaceRequired {
         return true
      } else {
          // Capacité indisponible
          return false
      }  
    catch {}
    return false
}
```

### Supprimer les vidéos obsolètes

Vous pouvez avoir un horodatage pour chaque vidéo afin de pouvoir nettoyer les anciennes vidéos de la mémoire de l'appareil après un certain nombre de jours.

```swift
func cleanExpiredVideos() {
        let currentTimeStamp = Date().timeIntervalSince1970
        var expiredKeys: [String] = []
        for videoData in videosDict where currentTimeStamp - videoData.value.timeStamp >= expiryTime {
            // vidéo expirée. supprimer
            if let _ = popupVideosDict[videoData.key] {
                expiredKeys.append(videoData.key)
            }
        }
        for key in expiredKeys {
            if let _ = popupVideosDict[key] {
                popupVideosDict.removeValue(forKey: key)
                deleteVideo(ForVideoId: key)
            }
        }
    }
```

### Maintenir un nombre limité de vidéos

Vous pouvez vous assurer qu'un nombre limité de vidéos sont enregistrées dans le fichier à la fois. Disons 10.

Ensuite, lorsque la 11ème vidéo arrive, vous pouvez la faire supprimer la vidéo la moins vue et la remplacer par la nouvelle. Cela vous aidera également à ne pas consommer trop de mémoire de l'appareil de l'utilisateur.

```swift
func removeVideoIfMaxNumberOfVideosReached() {
        if popupVideosDict.count >= maxVideosAllowed {
            // supprimer la vidéo la moins récemment utilisée
            let sortedDict = popupVideosDict.keysSortedByValue { (v1, v2) -> Bool in
                v1.timeStamp < v2.timeStamp
            }
            guard let videoId = sortedDict.first else {
                return
            }
            popupVideosDict.removeValue(forKey: videoId)
            deleteVideo(ForVideoId: videoId)
        }
    }
```

### Mesurer l'impact

N'oubliez pas d'ajouter des logs, afin de pouvoir mesurer l'impact de votre fonctionnalité. J'ai utilisé un événement de log personnalisé New Relic pour ce faire :

```swift
 static func findCachedVideoURL(forVideoId id: String) -> URL? {
        let nsDocumentDirectory = FileManager.SearchPathDirectory.documentDirectory
        let nsUserDomainMask = FileManager.SearchPathDomainMask.userDomainMask
        let paths = NSSearchPathForDirectoriesInDomains(nsDocumentDirectory, nsUserDomainMask, true)
        if let dirPath = paths.first {
            let fileURL = URL(fileURLWithPath: dirPath).appendingPathComponent(folderPath).appendingPathComponent(id + ".mp4")
            let filePath = fileURL.path
            let fileManager = FileManager.default
            if fileManager.fileExists(atPath: filePath) {
                NewRelicService.sendCustomEvent(with: NewRelicEventType.statusCodes,
                                                                   eventName: NewRelicEventName.videoCacheHit,
                                                                   attributes: [NewRelicAttributeKey.videoSize: fileURL.fileSizeString])
                return fileURL
            } else {
                return nil
            }
        }
        return nil
    }
```

Pour convertir la taille du fichier en un format lisible, je récupère la taille du fichier et la convertis en Mo.

```swift
extension URL {
    var attributes: [FileAttributeKey : Any]? {
        do {
            return try FileManager.default.attributesOfItem(atPath: path)
        } catch let error as NSError {
            print("FileAttribute error: \(error)")
        }
        return nil
    }

    var fileSize: UInt64 {
        return attributes?[.size] as? UInt64 ?? UInt64(0)
    }

    var fileSizeString: String {
        return ByteCountFormatter.string(fromByteCount: Int64(fileSize), countStyle: .file)
    }
}
```

Voici comment vous pouvez mesurer votre impact :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-16-at-11.34.24-AM.png)

**Données totales économisées = nombre de requêtes * taille_vidéo = 2,4 Mo * 20,3 K ~ 49 Go**

Ce n'est que deux semaines de données. Faites le calcul pour toute l'année. ? Et cela continuera à augmenter de manière exponentielle au fil du temps.

C'est tout ! Vous avez maintenant construit votre propre mécanisme de mise en cache.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/yay.gif)

# Conclusion

Dans cet article, nous avons vu à quel point il est facile d'intégrer plusieurs vidéos dans une seule vue, offrant une fonctionnalité de story de type Instagram.

Nous avons également appris pourquoi et comment la mise en cache joue un rôle important ici. Nous avons vu comment elle aide l'utilisateur à économiser beaucoup de données et à avoir une expérience utilisateur fluide.

N'hésitez pas à me faire savoir si j'ai oublié quelque chose, ou si vous pouvez penser à d'autres cas d'utilisation.
Merci pour votre temps. :)