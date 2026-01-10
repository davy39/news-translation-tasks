---
title: Comment configurer votre application pour le mode sombre d'iOS 13
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-27T13:05:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-an-app-for-dark-mode-on-ios-13-untitled
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/app-developer.jpg
tags:
- name: app development
  slug: app-development
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
seo_title: Comment configurer votre application pour le mode sombre d'iOS 13
seo_desc: "By Shifa Martin\nApple launched the much-awaited iOS 13 updates globally\
  \ on September 19 across all iPhones launched within the past 4 years (back to the\
  \ iPhone 6s). \n\nOne of the biggest features of this update was the system-wide\
  \ iOS 13 dark mode. It..."
---

Par Shifa Martin

Apple a lancé les mises à jour tant attendues d'iOS 13 dans le monde entier le 19 septembre sur tous les iPhones sortis au cours des 4 dernières années (jusqu'à l'iPhone 6s). 

> L'une des plus grandes fonctionnalités de cette mise à jour était le mode sombre d'iOS 13 à l'échelle du système. Il est censé aider à réduire la fatigue oculaire causée par la lumière blanche émise par les écrans des smartphones.

Bien que cette fonctionnalité soit une joie pour les consommateurs finaux utilisant des appareils Apple, c'est une tâche pour les développeurs iOS de préparer une application prête pour le mode sombre d'iOS 13.

## Comment configurer votre application pour le mode sombre d'iOS 13 ?

Pour aider les développeurs avec ce problème, voici des informations utiles et des étapes montrant comment ils peuvent préparer une application iOS existante pour le [mode sombre d'iOS 13](https://www.apple.com/ae/ios/ios-13/).

* Ce n'est pas trop difficile à implémenter le mode sombre d'iOS 13 malgré son échelle à l'échelle du système.
* Activer le mode sombre d'iOS 13 sur votre application existante est également simple, principalement grâce au dernier SDK iOS 13. 

Lorsque vous utilisez la dernière version pour créer des applications pour le mode sombre d'iOS 13, le système d'exploitation mettra automatiquement à jour les interrupteurs, les boutons et les vues de tableau parmi d'autres contrôles système. Notez cependant que les images et les couleurs de texte ne s'ajusteront pas automatiquement pour le mode sombre.

Cependant, il est toujours incroyable de voir qu'un changement à l'échelle du système comme le mode sombre est si facile à implémenter. Il y a de plus petits changements de code et plus de travail que vous pourrez faire avec le mode sombre d'iOS 13 dans ce temps économisé.

## Comment adapter les couleurs pour le mode sombre d'iOS 13

Tout d'abord, commençons par changer les couleurs du système pour le mode sombre d'iOS 13 :

Il y a maintenant de nouvelles couleurs système ajoutées dans UIColor, dont une est une couleur de label. L'utilisation de ces nouvelles couleurs aide à supporter le mode sombre et d'autres modes de contraste élevé dans iOS 13.

```js
label.color = UIColor.secondaryLabel
```

Généralement, vous devriez utiliser des couleurs système pour le mode sombre d'iOS 13, qui s'adaptent automatiquement aux changements de l'interface pour maintenir la cohérence entre les applications. Cependant, les développeurs peuvent également choisir d'implémenter le mode sombre avec des couleurs personnalisées. 

> Les couleurs du catalogue d'actifs introduites avec iOS 11 rendent beaucoup plus facile la prise en charge du mode sombre en ajoutant des versions sombres d'un ensemble personnalisé de couleurs. 

Vous n'avez qu'à sélectionner une couleur préférée dans le catalogue, puis changer les Apparences en Any, Dark depuis l'Inspecteur d'attributs. 

C'est tout ! Maintenant vous avez un mode sombre personnalisé pour iOS 13 prêt pour votre application mobile.

## Dépannage du mode sombre d'iOS 13 

Supposons que votre application ne suit pas le mode sombre d'iOS 13. Que ferez-vous ? Voici quelques étapes simples pour résoudre ce problème.

### Étape 1

Vous devrez savoir si l'application est mise à jour ou non. 

Si l'application ne fonctionne pas avec le mode sombre d'iOS 13 ou ne le supporte pas, mettez simplement à jour l'application via l'Apple Store.

### Étape 2 

Vérifiez si le mode sombre de votre application iOS a été activé ou non. 

Si ce n'est pas le cas, allez dans Réglages - Affichage et luminosité - vérifiez si "Sombre" est activé ou non.

### Étape 3  

Si votre application est entièrement mise à jour, mais ne fonctionne pas avec le mode sombre d'iOS 13, vérifiez alors les paramètres dans l'application. *Voir l'image :*

![Image](https://www.freecodecamp.org/news/content/images/2019/09/app-not-following-ios-13s-dark-mode-check-these-settings.w1456-3.jpg)

Si vous avez besoin de plus d'aide pour configurer votre mode sombre d'iOS 13, obtenez-la auprès des [équipes de développement dédiées](https://www.valuecoders.com/dedicated-development-teams). Et c'est ainsi que je vais vous aider. 

Lisez également des conseils pour le [développement d'applications mobiles sur iOS](https://www.valuecoders.com/blog/technology-and-apps/11-tips-successful-mobile-app-development-businesses-android-ios/). J'espère que toutes ces informations vous seront utiles. 

*Voyons ce que vous devez faire ensuite.*

## Adapter les images pour le mode sombre d'iOS 13

La plupart des images ont fière allure en mode sombre d'iOS 13, et parfois elles ressortent de manière à vraiment mettre en valeur les détails. Cependant, vous pourriez encore trouver certaines images qui semblent un peu décalées ou inadaptées au mode sombre. 

> La bonne nouvelle est que vous pouvez ajuster les images pour le mode sombre de la même manière que le texte est ajusté. 

Tout ce que vous avez à faire est de sélectionner l'image dans le catalogue et, comme précédemment, changer les attributs en Any, Dark dans l'Inspecteur d'attributs. Ajoutez maintenant l'apparence sombre de l'image et c'est fait.

## Détecter programmatiquement les changements dans le mode sombre d'iOS 13

Les développeurs pourraient rencontrer des situations où ils doivent implémenter des changements d'apparence en mode sombre d'iOS 13 de manière programmatique. Voici comment cela se fait :

```js
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) 
{
    super.traitCollectionDidChange(previousTraitCollection)

    let userInterfaceStyle = traitCollection.userInterfaceStyle // Soit .unspecified, .light, ou .dark
    // Mettez à jour votre interface utilisateur en fonction de l'apparence
}
```

> Le fait de substituer traitCollectionDidChange aide à détecter les changements d'apparence.

> Ensuite, nous devons simplement ouvrir traitCollection.userInterfaceStyle.

**Vous pouvez également vérifier si l'apparence existante utilise une nouvelle méthode que vous venez d'implémenter :**

```js
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    let hasUserInterfaceStyleChanged = previousTraitCollection.hasDifferentColorAppearance(comparedTo: traitCollection) // Bool
    // Mettez à jour votre interface utilisateur en fonction de l'apparence
}
```

## Substituer le style de l'interface utilisateur

### Application complète

Le système opte automatiquement pour toute application liée au SDK iOS 13.0 ou ultérieur pour les apparences claires et sombres. 

Si vous avez besoin de plus de temps pour travailler sur la prise en charge du mode sombre de votre application ou si vous souhaitez garder votre application dans un seul style, vous pouvez vous désister en incluant la clé UIUserInterfaceStyle (avec une valeur Light ou Dark) dans le fichier Info.plist de votre application. 

La définition de cette clé amène le système à ignorer la préférence de l'utilisateur et à appliquer toujours l'apparence spécifique à votre application.

> **Remarque :** La prise en charge du mode sombre d'iOS 13 est fortement encouragée. Utilisez la clé UI UserInterfaceStyle pour vous désister uniquement temporairement pendant que vous travaillez sur les améliorations de la prise en charge du mode sombre de votre application.

### Écrans spécifiques

Dans iOS 13, vous pouvez maintenant substituer le style de l'interface utilisateur sur des vues ou des contrôleurs de vue spécifiques. Par exemple, vous pouvez vouloir qu'un certain contrôleur de vue soit en mode sombre d'iOS 13, tandis que le reste de votre application est en mode clair.

Pour substituer le style de l'interface utilisateur, il suffit de substituer cette variable dans la vue supérieure ou le contrôleur de vue et elle se propagera aux sous-vues :

```js
// À l'intérieur d'un UIViewController
override func viewDidLoad() 
{
    super.viewDidLoad()

    // Adoptez toujours un style d'interface sombre.    
    overrideUserInterfaceStyle = .dark
}
```

### Remarques finales

Merci d'avoir lu l'article ! Ici, nous avons exploré comment configurer une application pour le mode sombre d'iOS 13. 

iOS 13 mode sombre apporte avec lui une manière unique et sans stress d'utiliser un smartphone. Peut-être verrons-nous un avenir où le mode sombre remplacera le mode par défaut avec les arrière-plans plus blancs. 

En suivant ces directives de codage et ces conseils, vous pouvez facilement configurer votre application pour le mode sombre sur iOS 13. 

**Si vous avez besoin d'une aide experte, n'hésitez pas à [nous contacter](https://www.valuecoders.com/contact) avec des [développeurs iOS](https://www.valuecoders.com/hire-developers/hire-ios-developers) pour les questions liées au mode sombre d'iOS 13.**   

**S**uivez sur Twitter pour **plus** de mises à jour : **[https://twitter.com/ValueCoders](https://twitter.com/ValueCoders)**