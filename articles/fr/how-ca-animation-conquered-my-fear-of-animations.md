---
title: Comment CAAnimation m'a aidé à surmonter ma peur de créer des animations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-15T21:26:22.000Z'
originalURL: https://freecodecamp.org/news/how-ca-animation-conquered-my-fear-of-animations
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/67b2a9ba5e85822f237caae92111e938.gif
tags:
- name: animation
  slug: animation
- name: iOS
  slug: ios
seo_title: Comment CAAnimation m'a aidé à surmonter ma peur de créer des animations
seo_desc: 'By Agam Mahajan

  This article focuses on using CA Animations in iOS to make smooth animations.

  During my initial days working with iOS, I would get very nervous whenever a designer
  came up to me and asked for some animation in the app they were workin...'
---

Par Agam Mahajan

Cet article se concentre sur l'utilisation des animations CA dans iOS pour créer des animations fluides.

Lors de mes premiers jours de travail avec iOS, je devenais très nerveux chaque fois qu'un designer venait me voir et me demandait une animation dans l'application sur laquelle il travaillait.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/1_BWbcgO2n4v8FL4FhuGNelw.gif)
_Craaaaap_

Je pensais qu'il était facile de concevoir des animations – mais les implémenter, en revanche, était une tâche très difficile.

Je recevais de l'aide de Google, StackOverflow et de mes pairs pour l'implémentation.   
Au cours de ce processus, j'ai développé une phobie des animations et j'ai toujours essayé de les éviter. Mais tout cela a changé un jour.

## Découverte de CAAnimation

Une fois, j'ai dû animer une séquence d'images dans une vue. Alors, quelle a été ma première étape ? Évidemment, StackOverflow !

Le premier lien a fourni le code.

```swift
let image_1 = UIImage(named: "image-1")!
let image_2 = UIImage(named: "image-2")!
let image_3 = UIImage(named: "image-3")!
let images = [image_1, image_2, image_3]
let animatedImage = UIImage.animatedImage(with: images, duration: 2.0)
imageView.image = animatedImage
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/animation-image.gif)

Cela semble assez simple, non ? Si c'était si simple, je n'écrirais pas cet article.

Voici l'animation qui était requise :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/final-animation.gif)
_Objectif final_

Et comme cela a probablement été clair, j'en étais très loin. J'étais bloqué. Comment devrais-je faire autant de personnalisations dans cette animation et synchroniser le tout ?

Ensuite, mon collègue m'a conseillé d'essayer [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation). J'ai lu à ce sujet et je l'ai essayé sur un projet d'exemple. À ma grande surprise, c'était vraiment puissant et facile à utiliser.

## Qu'est-ce que Core Animation ?

Core Animation vous aide à exécuter plusieurs animations avec presque zéro utilisation du CPU.  
Il offre un taux de rafraîchissement élevé et de nombreuses personnalisations que vous pouvez utiliser avec très peu de code.

Vous pouvez trouver plus de détails dans la documentation ici : [https://developer.apple.com/documentation/quartzcore](https://developer.apple.com/documentation/quartzcore)

J'ai pu faire une implémentation de base en quelques heures :

```swift
func addAnimation(firstImageView: UIImageView, secondImageView: UIImageView) {
        let basicAnimation1 = getBasicAnimation(withInitialPostion: centerPosition, finalPos: finalPosition)
        firstImageView.layer.add(basicAnimation1, forKey: "position")        
        let basicAnimation2 = self.getBasicAnimation(withInitialPostion: self.initalPosition, finalPos: self.centerPosition)
        secondImageView.layer.add(basicAnimation2, forKey: "position")
        self.addNextImage(forImageView: firstImageView)
    }
    func getBasicAnimation(withInitialPostion initialPos: CGPoint, finalPos: CGPoint) -> CABasicAnimation {
        let basicAnimation = CABasicAnimation(keyPath: "position")
        basicAnimation.fromValue = NSValue(cgPoint: initialPos)
        basicAnimation.toValue = NSValue(cgPoint: finalPos)
        basicAnimation.duration = 1
        basicAnimation.isRemovedOnCompletion = false
        basicAnimation.fillMode = CAMediaTimingFillMode.forwards
        basicAnimation.timingFunction = CAMediaTimingFunction(name: CAMediaTimingFunctionName.easeInEaseOut)
        return basicAnimation
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/basic-animation.gif)
_Animation de base CA_

Pour cette implémentation, j'ai utilisé **CABasicAnimation**.

La classe **CABasicAnimation** vous aide à animer une propriété de couche (qui peut être la couleur de fond, l'opacité, la position, l'échelle) entre deux valeurs. Vous devez simplement donner une valeur de début et de fin, et le reste sera pris en charge. L'animation commence immédiatement dans la boucle suivante comme décrit plus en détail [ici](https://developer.apple.com/documentation/quartzcore/cabasicanimation).

### Revenons à notre problème. 

Pour implémenter cela, j'ai pris deux vues d'image et j'y ai ajouté deux images séparées. Ensuite, je les ai animées l'une après l'autre en utilisant CAAnimation.

Vous pouvez trouver le code source [ici](https://gist.github.com/agammahajan1/e9b550f0275418459982246d1ee905d5).

Si vous examinez le dernier gif, vous verrez que quelque chose ne va pas. Avant que la première image d'une boîte cadeau ne sorte de la vue, les écouteurs clignotent brièvement puis l'image se déplace vers le haut. 

Pourquoi cela se produit-il ?

C'est parce que dès que nous ajoutons l'animation à la vue d'image, nous ajoutons l'image suivante à cette vue (lignes numéros 5 et 6) :

```swift
private func addAnimation(firstImageView: UIImageView, secondImageView: UIImageView) {
    let basicAnimation1 = getBasicAnimation(withInitialPostion: centerPosition, finalPos: finalPosition)
    firstImageView.layer.add(basicAnimation1, forKey: "position")    
    let basicAnimation2 = self.getBasicAnimation(withInitialPostion: self.initalPosition, finalPos: self.centerPosition)
    secondImageView.layer.add(basicAnimation2, forKey: "position")
    self.addNextImage(forImageView: firstImageView)
}
```

Ici, nous luttons avec le problème de la synchronisation des deux images dans l'animation. Mais il y a toujours une solution avec CAAnimation.

### Transactions CA

Les transactions CA nous aident à synchroniser plusieurs animations ensemble. Cela garantit que toutes les animations que nous avons regroupées commencent toutes au même moment.

De plus, vous pouvez donner un bloc de complétion à vos animations, qui sera exécuté lorsque toutes vos animations dans un groupe seront terminées.  
  
Vous pouvez en lire plus à ce sujet [ici](https://developer.apple.com/documentation/quartzcore/catransaction).

```swift
private func addAnimation(firstImageView: UIImageView, secondImageView: UIImageView) {
    CATransaction.begin()
    CATransaction.setCompletionBlock {
        self.addNextImage(forImageView: firstImageView)
    }
    let basicAnimation1 = getBasicAnimation(withInitialPostion: centerPosition, finalPos: finalPosition)
    firstImageView.layer.add(basicAnimation1, forKey: "position")
    CATransaction.commit()
    
    let basicAnimation2 = self.getBasicAnimation(withInitialPostion: self.initalPosition, finalPos: self.centerPosition)
    secondImageView.layer.add(basicAnimation2, forKey: "position")
}
```

Vous commencez par écrire `CATransaction.begin()`. Ensuite, écrivez toutes vos animations que vous souhaitez synchroniser. Enfin, appelez `CATransaction.commit()` qui démarrera l'animation dans le bloc.

Voyons à quoi ressemble notre animation maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ezgif.com-video-to-gif.gif)
_Transaction CA_

Une dernière chose que je devais faire était d'ajouter l'effet de ressort à l'animation. Heureusement, CAAnimation avait aussi une solution pour cela.

### Animation de ressort CA

> L'animation de ressort CA, lorsqu'elle est ajoutée à une couche, donne un effet de ressort, de sorte qu'elle semble être tirée vers une cible par un ressort.   
>   
> Plus la couche est éloignée de la cible, plus l'accélération vers elle est grande.  
>   
> Elle permet de contrôler des attributs basés sur la physique tels que l'amortissement et la rigidité du ressort. – [Docs](https://developer.apple.com/documentation/quartzcore/caspringanimation)

Vous pouvez en lire plus dans la documentation Apple : [https://developer.apple.com/documentation/quartzcore/caspringanimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)  
  
Implémentons-le dans notre code existant :

```swift
private func getSpringAnimation(withInitialPostion initialPos: CGPoint, finalPos: CGPoint) -> CASpringAnimation {
    let basicAnimation = CASpringAnimation(keyPath: "position")
    basicAnimation.fromValue = NSValue(cgPoint: initialPos)
    basicAnimation.toValue = NSValue(cgPoint: finalPos)
    basicAnimation.duration = basicAnimation.settlingDuration
    basicAnimation.damping = 14
    basicAnimation.initialVelocity = 5
    basicAnimation.isRemovedOnCompletion = false
    basicAnimation.fillMode = CAMediaTimingFillMode.forwards
    return basicAnimation
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ezgif.com-video-to-gif--1-.gif)
_Voilà_

Mon travail est terminé ici.

En résumé, voici quelques-uns des avantages de l'utilisation des animations CA :

* Elles sont faciles à utiliser et à implémenter
* Il y a beaucoup de personnalisations disponibles
* Il est possible de synchroniser plusieurs animations
* Presque aucune utilisation du CPU

Ce ne sont là que quelques-uns des avantages. Les possibilités sont infinies.

Maintenant, chaque fois que des exigences d'animation se présentent, je me sens confiant pour les concevoir et les implémenter. Et j'espère que vous vous sentez de la même manière après avoir lu ceci.  
N'hésitez pas à laisser des suggestions ou des commentaires.