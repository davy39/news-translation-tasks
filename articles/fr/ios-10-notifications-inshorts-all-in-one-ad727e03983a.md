---
title: Tout ce que vous avez toujours voulu savoir sur les notifications dans iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-04T16:54:51.000Z'
originalURL: https://freecodecamp.org/news/ios-10-notifications-inshorts-all-in-one-ad727e03983a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KCLG3VkqwWXdgV2CXwp3Kg.jpeg
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Tout ce que vous avez toujours voulu savoir sur les notifications dans
  iOS
seo_desc: 'By Payal Gupta

  Pretty Little Alerts..?


  Notifications are a way to inform users when new data becomes available for their
  apps, even when the app is not running in the foreground.

  For example, a messaging app might let the user know when a new messag...'
---

Par Payal Gupta

#### De jolies petites alertes..?

![Image](https://cdn-media-1.freecodecamp.org/images/1*KCLG3VkqwWXdgV2CXwp3Kg.jpeg)

Les notifications sont un moyen d'informer les utilisateurs lorsque de nouvelles données deviennent disponibles pour leurs applications, même lorsque l'application n'est pas en cours d'exécution au premier plan.

Par exemple, une application de messagerie peut informer l'utilisateur lorsqu'un nouveau message est arrivé, et une application de calendrier peut informer l'utilisateur d'un rendez-vous à venir.

Avec la sortie de **iOS-10**, Apple a introduit de nouveaux frameworks pour prendre en charge les notifications, qu'elles soient locales ou distantes. Cette version était axée sur les **notifications personnalisées**.

Sans perdre de temps, plongeons rapidement dans les détails.

### Types de notifications

Nous pouvons classer les notifications en deux catégories :

* **Notifications locales** — l'application configure les détails de la notification localement et transmet ces détails au système. Le système gère ensuite la livraison de la notification lorsque l'application n'est pas au premier plan.
* **Notifications distantes** — vous utilisez l'un de vos serveurs d'entreprise pour pousser des données vers les appareils des utilisateurs via le service Apple Push Notification (APNs).

Plus loin dans l'article, nous verrons comment nous pouvons obtenir les deux types de notifications. Commençons d'abord par une introduction à ce nouveau framework de notification que nous pouvons utiliser pour notre cause.

### Qu'y a-t-il de nouveau dans iOS-10 pour les notifications ?

Avec la sortie de **iOS-10**, Apple a introduit deux nouveaux frameworks pour gérer les notifications :

* [**User Notifications Framework**](https://developer.apple.com/documentation/usernotifications) — gère les notifications locales et distantes.
* [**User Notifications UI Framework**](https://developer.apple.com/documentation/usernotificationsui) — personnalise l'apparence de l'interface de notification du système.

Nous utiliserons ces deux frameworks et certaines API spécifiques à la plateforme pour configurer nos notifications.

Avec les frameworks, l'[**Notification service app extension**](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension) a également été introduit, ce qui vous permet de modifier le contenu des notifications distantes avant qu'elles ne soient livrées.

Apple permet également de personnaliser l'interface utilisateur de votre notification via l'[**Notification content extension**](https://developer.apple.com/documentation/usernotificationsui/customizing_the_appearance_of_notifications).

Est-ce trop à retenir ? Oui... sûrement. Mais ne vous inquiétez pas. Nous verrons tout étape par étape avec le code pertinent. Prenez-le simplement avec facilité. ?

### D'abord les premières choses — configurez-le !

#### Demander l'autorisation

Pour que notre application notifie l'utilisateur de quoi que ce soit, nous devons savoir si la personne qui l'utilise veut vraiment cela en premier lieu. Peut-être qu'ils n'aiment pas que leur téléphone sonne et affiche des alertes tout le temps ? ou peut-être qu'ils veulent vraiment les mises à jour, mais pas ce son irritant...naahhh!⚡️

Donc, avant tout, nous devons obtenir la permission de l'utilisateur que nous allons notifier. Et c'est assez simple — juste deux lignes de code et nous avons terminé :

Vous devez écrire ce code dans la méthode `AppDelegate` — `application:didFinishLaunchingWithOptions:` avant de retourner.

**Veuillez noter :** Parce que le système sauvegarde la réponse de l'utilisateur, les appels à la méthode `[requestAuthorization(options:completionHandler:)](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649527-requestauthorization)` lors des lancements ultérieurs ne demandent pas à nouveau à l'utilisateur.

#### Ajout de catégories et d'actions — Notifications actionnables

Le framework des notifications utilisateur prend en charge l'ajout de catégories et d'actions aux notifications.

**Catégories** — Définissent les types de notifications que l'application prend en charge et communiquent au système comment nous voulons qu'une notification soit présentée.

**Actions** — Chaque catégorie peut avoir jusqu'à quatre actions associées. Les actions sont essentiellement des boutons personnalisés, qui, lorsqu'on appuie dessus, ferment l'interface de notification et transmettent l'action sélectionnée à l'application pour un traitement immédiat.

D'accord ! Et que signifie cela..??? Un peu de code pourrait vous aider à mieux comprendre :

Dans le code ci-dessus, nous avons simplement créé une catégorie nommée INVITATION avec quatre actions différentes — **remindLater**, **accept**, **decline**, et **comment**.

Les catégories et les actions sont identifiées de manière unique par leurs identifiants. Chaque fois qu'une notification avec une catégorie est livrée, le système présente la notification avec toutes les actions associées à cette catégorie une fois que l'utilisateur l'a développée. Voici à quoi cela ressemblera : ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*RAR8fwTQ_py7jtqmr7-zUw.png)

Définissez toutes les catégories et actions juste en dessous de l'endroit où vous avez configuré les notifications dans la méthode `application:didFinishLaunchingWithOptions:`.

Incluez l'identifiant de catégorie (par exemple, INVITATION) lors de la planification de votre notification, qu'elle soit locale ou distante. Nous verrons comment faire cela dans la section suivante.

### Planification des notifications locales

Maintenant que nous avons terminé la configuration de nos notifications, voyons comment en planifier une **à partir de l'application**.

La planification d'une notification locale nécessite seulement trois étapes simples :

1. Préparer le contenu
2. Ajouter un déclencheur — quand la notification doit être déclenchée
3. La planifier pour la livraison

Passons rapidement au code, afin de ne pas nous perdre avec tout ce qui se passe ici. LOL ?

Dans le code ci-dessus, avec le reste du contenu, nous avons également fourni un `categoryIdentifier` pour prendre en charge les notifications actionnables. Dans le cas où nous ne le ferions pas, le système adopterait son comportement par défaut.

C'est tout. C'est tout ce dont nous avons besoin. Et oui, cela fonctionne définitivement...hehehe.? Essayez-le avant d'aller plus loin. Vous pouvez télécharger l'exemple [ici](https://github.com/pgpt10/Notifications).

**Veuillez noter :** Les applications se comportent différemment en arrière-plan et au premier plan chaque fois qu'une notification est livrée.

1. **Application non exécutée / Application en arrière-plan** — le système affiche les notifications locales directement à l'utilisateur. Nous ne recevons aucun rappel dans l'application pour cela.
2. **Application au premier plan** — le système donne à l'application l'opportunité de gérer la notification en interne. *Le système désactive les notifications pour les applications au premier plan par défaut*.

Lorsque l'application est au premier plan pendant la livraison de la notification, nous recevons le rappel dans la méthode `UNUserNotificationCenterDelegate` — `[userNotificationCenter(_:willPresent:withCompletionHandler:)](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649518-usernotificationcenter)` où vous pouvez décider de gérer la notification silencieusement ou d'alerter l'utilisateur à ce sujet.

N'oubliez pas de faire en sorte que `AppDelegate` se conforme au protocole `UNUserNotificationCenterDelegate` et de le définir comme délégué de l'objet partagé `[UNUserNotificationCenter](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter)` dans `application:didFinishLaunchingWithOptions:`.

```
let center = UNUserNotificationCenter.current()
```

```
center.delegate = self
```

Nous avons terminé avec les notifications locales pour l'instant. Passons à la manière dont nous pouvons planifier une notification depuis l'extérieur de notre application. Avant cela, voyons comment répondre aux actions personnalisées.

#### Répondre aux actions de l'utilisateur

Configurer les notifications ? ✔ Planifier les notifications ? ✔

Et si l'utilisateur appuie sur une notification ou une action personnalisée dans la notification ? Où cela mènera-t-il ? Dans les deux cas, le système informe l'application du choix de l'utilisateur.

Chaque fois que l'utilisateur effectue une action dans la notification, la réponse est envoyée à la méthode `UNUserNotificationCenterDelegate` — `[userNotificationCenter(_:didReceive:withCompletionHandler:)](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter)`, où nous pouvons fournir une gestion spécifique à chaque action.

**Veuillez noter :** si l'application n'est pas en cours d'exécution lorsqu'une réponse est reçue, le système lance l'application en arrière-plan pour traiter la réponse.

### Notifications distantes

Notification push ou notifications distantes, peu importe comment nous les appelons, sont parmi les plus fréquemment utilisées avec de nombreux cas d'utilisation.

Que ce soit les médias sociaux, le calendrier ou l'une des applications utilitaires, nous pouvons les voir presque partout. Des applications d'actualités nous informant du dernier contenu, à Medium lui-même nous alertant des derniers articles publiés.

Vous êtes-vous déjà demandé comment ils font cela ? Notifications locales ?? Cela pourrait être... cela fait la même chose — n'est-ce pas ? Peut-être pouvons-nous faire plus de configuration dans la notification locale elle-même et la faire fonctionner ?

Mais Medium, par exemple, n'a pas accès à l'application sur notre appareil personnel, alors comment pourrait-il planifier des notifications ? Exactement ! Il ne peut pas. C'est quelque chose de différent et quelque chose de plus que les notifications locales.

D'accord, comment se fait-il que nous envoyons la notification depuis un point et l'affichons à un autre point — cela répondra-t-il à notre question ? Oui, cela le fera sûrement. Mais comment faire cela ? **Notifications distantes** c'est.

C'est exactement ce qu'ils font. C'est la fonctionnalité qui a résolu LE GRAND PROBLÈME de « Rester à jour ».

#### **Terminologie**

* [**APNs**](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) — la pièce maîtresse de la fonctionnalité des notifications distantes. Il s'agit d'un service cloud qui permet aux applications tierces approuvées installées sur les appareils Apple d'envoyer des notifications push depuis un serveur distant aux utilisateurs via une connexion sécurisée.
* **Jeton de l'appareil** — Un jeton spécifique à l'application qui est globalement unique et identifie une combinaison app-appareil. Il permet la communication entre le Fournisseur, APNs et l'Appareil.
* **Fournisseur** — Serveur qui envoie réellement la notification distante incluant le jeton de l'appareil et d'autres informations à APNs.

**Note importante :** **Ne mettez jamais en cache les jetons de l'appareil dans votre application.** Au lieu de cela, obtenez-les du système lorsque vous en avez besoin.

APNs émet un nouveau jeton de l'appareil pour votre application lorsque certains événements se produisent. Le jeton de l'appareil est garanti d'être différent, par exemple, lorsqu'un utilisateur restaure un appareil à partir d'une sauvegarde, lorsqu'un utilisateur installe votre application sur un nouvel appareil, et lorsqu'un utilisateur réinstalle le système d'exploitation.

Lorsque vous tentez de récupérer un jeton de l'appareil mais qu'il n'a pas changé, la méthode de récupération retourne rapidement.

**Veuillez noter :** La capacité d'APNs à livrer des notifications distantes à une application non exécutée nécessite que l'application ait été lancée au moins une fois.

#### **Comment cela fonctionne-t-il réellement**

Ci-dessous se trouve une explication rapide de la manière dont toutes les technologies ci-dessus fonctionnent ensemble en synchronisation pour compléter le flux de travail des notifications distantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RC5Ahc9Lj2LHrTWTQ8XxVQ.png)

1. **App** s'enregistre auprès de **APNs**
2. **APNs** envoie le jeton de l'appareil à **Device** qui l'envoie ensuite à **App**
3. **App** envoie ce jeton de l'appareil à **Provider**
4. **Provider** envoie des notifications avec ce jeton de l'appareil à **APNs** qui les envoie ensuite à **Device** qui les envoie ensuite à **App**.

Si une notification pour votre application arrive avec l'appareil allumé mais avec l'application non exécutée, le système peut toujours afficher la notification. Si l'appareil est éteint lorsque APNs envoie une notification, APNs conserve la notification et réessaie plus tard.

#### Gérer cela dans l'application

Maintenant que nous sommes conscients de ce que sont les notifications distantes et de ce dont nous avons besoin pour les faire fonctionner, passons maintenant à la manière dont nous pouvons faire en sorte que notre application les prenne en charge. Parce que rien ne se fait tout seul ?. Nous devons faire quelques configurations pour qu'elles fonctionnent.

Pour pouvoir gérer les notifications distantes, notre application doit :

1. **Activer les notifications distantes dans les capacités** — un seul clic et vous avez terminé cette étape. Dans l'onglet **Capacités** de notre projet Xcode, activez l'option **Push Notifications**. Assurez-vous que Push Notifications est ajouté à l'ID d'application que nous utilisons pour le projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jxD3SJUZFNwwN6iUpNgCIA.png)

**2.** **S'inscrire au service Apple Push Notification (APNs) et recevoir un jeton de l'appareil spécifique à l'application**

Demander à s'inscrire à APNs est rapide et facile. Il suffit d'ajouter le code ci-dessous dans la méthode `UIApplicationDelegate` — `application:didFinishLaunchingWithOptions:` avant de retourner.

```
UIApplication.shared.registerForRemoteNotifications()
```

Il y a maintenant deux possibilités : soit nous nous inscrivons avec succès, soit le processus échoue.

En cas d'inscription réussie, APNs envoie un jeton de l'appareil spécifique à l'application à l'appareil dans la méthode `UIApplicationDelegate` — `[application:didRegisterForRemoteNotificationsWithDeviceToken:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application?language=objc)`.

En cas d'échec, nous recevons un rappel dans la méthode `UIApplicationDelegate` — `[application:didFailToRegisterForRemoteNotificationsWithError:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622962-application?language=objc)`.

**3. Envoyer le jeton de l'appareil au serveur du fournisseur de notifications**

Pour l'instant, nous avons reçu le jeton de l'appareil de APNs. Maintenant, nous devons envoyer ce jeton à notre fournisseur, qui l'utilisera lors de l'envoi de notifications à notre appareil.

Puisque nous n'avons pas de fournisseur pour l'instant, nous pouvons utiliser [Easy APNs Provider](https://itunes.apple.com/us/app/easy-apns-provider-push-notification-service-testing-tool/id989622350?mt=12) pour tester nos notifications push. Plus loin, nous verrons comment exactement nous pouvons utiliser cet outil.

Pour l'instant, téléchargez-le et installez-le sur votre Mac.

**4. Implémenter la prise en charge de la gestion des notifications distantes entrantes**

Nous avons notre jeton de l'appareil, et notre fournisseur le connaît également. Ensuite, le fournisseur enverra la notification incluant ce jeton et d'autres informations, et nous la recevrons sur notre appareil.

Maintenant quoi ? Que se passera-t-il lorsqu'elle arrivera ? Comment apparaîtra-t-elle sur l'appareil ? Que se passera-t-il lorsque nous appuierons dessus ? Et toutes les actions que nous avons configurées précédemment ? Pouvez-nous les obtenir ici ?

Trop de questions ??? Ne vous inquiétez pas. Nous aurons des réponses à toutes ces questions une par une.

**Que se passera-t-il lorsqu'elle arrivera ?** Nous recevrons un rappel dans la méthode `UIApplicationDelegate` — `[application(_:didReceiveRemoteNotification:fetchCompletionHandler:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)`. Elle indique à l'application qu'une notification distante est arrivée, indiquant qu'il y a des données à récupérer.

**Comment apparaîtra-t-elle sur l'appareil ?** Elle apparaîtra avec l'interface de notification par défaut. Si la **charge utile** de la notification est configurée avec une **catégorie**, elle apparaîtra comme une notification actionnable avec toutes les actions attachées à cette catégorie. Nous discuterons de la charge utile dans la section suivante.

**Que se passera-t-il lorsque nous appuierons dessus ?** Même chose que pour les notifications locales. La méthode `UNUserNotificationCenterDelegate` — `[userNotificationCenter(_:didReceive:withCompletionHandler:)](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter)` est appelée avec l'objet de réponse.

#### Gérer cela sur le fournisseur

Nous avons couvert la plupart des choses dont nous avons besoin pour intégrer les notifications push dans notre application. Bien que nous sachions comment les gérer dans l'application, nous manquons encore de les gérer sur le fournisseur.

Nous avons le fournisseur. Il sait quel jeton de l'appareil utiliser, mais cela seul ne fera pas apparaître une notification sur notre appareil avec un titre et d'autres détails. Cela ne fera pas non plus apparaître d'actions.

Ainsi, l'envoi de notifications depuis le fournisseur nécessite les éléments suivants :

1. Un **jeton de l'appareil**
2. **Certificat APNs** — nous pouvons l'obtenir à partir du compte développeur
3. **Charge utile** — toute donnée personnalisée que vous souhaitez envoyer à votre application, et qui inclut des informations sur la manière dont le système doit notifier l'utilisateur. Il s'agit simplement d'un **dictionnaire JSON** avec quelques paires clé-valeur. L'illustration ci-dessous pourrait vous aider à mieux le comprendre.

Voyons ce qu'il y a dans ce **dictionnaire JSON** :

1. **Dictionnaire aps** — le plus important. Contient des **clés définies par Apple** et est utilisé pour déterminer comment le système qui reçoit la notification doit alerter l'utilisateur.
2. **Dictionnaire alert** — c'est un élément plutôt explicite. Fournit le contenu de la notification.
3. **Catégorie** — pour les notifications actionnables. Toutes les actions attachées à cette catégorie seront disponibles dans les notifications.
4. **Content-available** — Pour prendre en charge une notification de mise à jour en arrière-plan, définissez cette clé sur 1.
5. **Mutable-content** — Pour activer la modification d'une notification via **Notification Service App Extension**, définissez-la sur 1.

[Ici](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1) vous pouvez lire plus sur la personnalisation de la charge utile selon vos besoins. [Ceci](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html#//apple_ref/doc/uid/TP40008194-CH17-SW1) est une référence aux clés que nous pouvons ajouter dans le dictionnaire aps.

### **_Notification Service App Extension_**

À ce stade, nous savons ce que sont les **notifications distantes**, comment elles fonctionnent, ce dont nous avons besoin pour les faire fonctionner — presque tout ! Puisque nous venons de les faire fonctionner parfaitement ✌️.

Maintenant, la question est, que faire si nous voulons modifier un contenu dans la notification reçue du fournisseur, avant de la présenter sur l'appareil ? Que faire si la notification contient un lien vers une image que nous devons télécharger avant de la livrer à l'utilisateur ? Pouvez-nous faire cela avec ce que nous savons déjà ? Nous n'avons pas accès au fournisseur... alors comment allons-nous faire ?

Nous ne pouvons pas vraiment. **Nous ne pouvons pas changer ce que nous recevons, mais nous pouvons définitivement changer ce que nous présentons.**

C'est de cela qu'il s'agit avec **Notification Service App Extension** — modifier le contenu des notifications distantes avant la livraison. C'est aussi simple que cela en a l'air. Pas de code compliqué, rien. C'est vraiment très simple.

#### Ajout de l'extension Notification Service au projet

Les extensions dans un projet Xcode sont ajoutées en tant que cible. Sélectionnez **Fichier** — **Nouveau** — **Cible** — **Notification Service Extension.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*_p2o1WUXo-0YX_uL8iAs1A.png)

#### Prérequis

Avant de commencer à modifier le contenu, il y a certaines restrictions sur le moment où le contenu est autorisé à être modifié.

Le contenu ne peut être modifié que si :

* La notification distante est configurée pour afficher une alerte.
* Le **dictionnaire aps** de la notification distante inclut la clé **mutable-content** avec la valeur définie sur 1.

Nous ne pouvons pas modifier les notifications silencieuses ou celles qui ne font que jouer un son ou badger l'icône de l'application.

Ainsi, pour prendre en charge toute modification dans le contenu des notifications, ces conditions doivent être remplies.

#### **Modification du contenu**

La cible d'extension de service de notification par défaut fournie par Xcode contient une sous-classe de la classe `[UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension)` pour que nous puissions la modifier.

Elle contient deux méthodes :

1. `[didReceive(_:withContentHandler:)](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648229-didreceive)` — apportez les modifications nécessaires à la notification et informez le système lorsque vous avez terminé. Cette méthode dispose d'une quantité limitée de temps (environ 30 secondes) pour effectuer sa tâche et exécuter le bloc de complétion fourni.
2. `[serviceExtensionTimeWillExpire()](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648227-serviceextensiontimewillexpire)` — Nous informe que l'extension est sur le point d'être terminée. Nous donne une dernière chance de soumettre nos modifications. Si nous ne mettons pas à jour le contenu de la notification avant l'expiration du temps, le système affiche le contenu original.

Regardons un exemple. Nous allons changer le **body** dans **payload** dans **Code Snippet 7** en « _Adresse : Sea Shells Apartments, Mumbai_ ».

Toute l'implémentation par défaut des deux méthodes est fournie par l'extension elle-même. Nous devons simplement apporter les modifications que nous voulons, comme à la ligne 8 dans l'extrait de code ci-dessus. Juste une seule ligne de code pour l'instant. De même, vous pouvez modifier d'autres champs selon vos besoins.

### Notification Content Extension

Avoir une interface utilisateur accrocheuse est toujours mieux qu'une interface utilisateur par défaut simple. Ajouter quelques couleurs et quelques polices jolies n'est jamais une mauvaise idée. Nous allons faire de même avec nos notifications pour les rendre Wow!?

Et et et… **Apple** est encore là pour nous sauver. **Notification content extension** c'est. Cela présente une interface personnalisée pour une notification **locale** **ou** **distant** livrée.

#### Ajout de l'extension Notification Content au projet

Je pense que nous savons déjà comment faire cela. N'est-ce pas ? Nous allons faire la même chose que ce que nous avons fait pour ajouter **Notification Service Extension**. Sélectionnez **Fichier** — **Nouveau** — **Cible** — **Notification Content Extension.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*5QBuMXXIn9e896Bg0Az2Iw.png)

#### Ajout de quelques clés au fichier Info.plist de l'extension

Pour prendre en charge l'interface utilisateur personnalisée pour les notifications locales et distantes, nous devons apporter quelques modifications au fichier **Info.plist** de l'extension de contenu.

1. **UNNotificationExtensionCategory (obligatoire)** — Une chaîne ou un tableau de chaînes. Chaque chaîne contient l'identifiant d'une catégorie déclarée par l'application. **Catégorie**, je dois dire, est vraiment vraiment importante pour les notifications. L'interface utilisateur personnalisée n'apparaîtra que pour les notifications appartenant aux catégories spécifiées.
2. **UNNotificationExtensionInitialContentSizeRatio (obligatoire)** — Un nombre à virgule flottante qui représente la taille initiale de la vue du contrôleur de vue exprimée comme un **ratio de sa hauteur à sa largeur**. C'est le contrôleur de vue que nous utiliserons pour créer une interface utilisateur personnalisée. Nous en discuterons dans la section à venir.
3. **UNNotificationExtensionDefaultContentHidden — si vrai** : montrer uniquement le contenu personnalisé. **Si faux** : montrer le contenu personnalisé + le contenu par défaut.
4. **UNNotificationExtensionOverridesDefaultTitle — si vrai** : définir le titre de la notification sur le titre du contrôleur de vue. **Si faux** : le titre de la notification est défini sur le nom de l'application.

Voici une illustration qui peut nous aider à mieux comprendre les clés ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SiSHq4lvgJA58h4N9DToIA.png)

Dans l'illustration ci-dessus, les clés dans **Info.plist** sont configurées comme suit :

1. **UNNotificationExtensionCategory** — INVITATION
2. **UNNotificationExtensionInitialContentSizeRatio** — 1
3. **UNNotificationExtensionDefaultContentHidden** — false
4. **UNNotificationExtensionOverridesDefaultTitle** — false

#### Création de l'interface utilisateur personnalisée

L'extension de contenu de notification nous fournit un `UIViewController` qui se conforme au protocole `[UNNotificationContentExtension](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension)`. Ce contrôleur présente l'interface de la notification. Le fichier `Storyboard` dans l'extension contient un seul ViewController que nous pouvons utiliser pour créer l'interface utilisateur que nous voulons que la notification présente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TjlQ9z2HaTKIzx-M5ISJSg.png)

Une fois que nous avons créé l'interface utilisateur, nous devons connecter les éléments dans le `NotificationViewController` afin de remplir les détails. Chaque fois qu'une notification arrive avec une **catégorie** attendue, nous recevons un rappel dans la méthode `UNNotificationContentExtension` — `[didReceive(_:)](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/1648525-didreceive)`. C'est l'endroit où nous pouvons ajouter des détails à notre interface utilisateur personnalisée.

Nous avons presque terminé avec l'interface utilisateur personnalisée de notre notification. Juste une chose de plus. Puisque l'interface utilisateur personnalisée est attachée à la **catégorie** des notifications, qui peut avoir des actions attachées. Et… vous avez raison ! ? Nous obtiendrons nos actions automatiquement sans aucune gestion personnalisée. Brillant !?

**Contenu + Belle Interface Utilisateur + Actions Personnalisées** — Tout est fait. Que pouvons-nous demander de plus ? Apple, tu es génial !?

![Image](https://cdn-media-1.freecodecamp.org/images/1*q8FG_H9ZcnMbg_SiGySsFQ.png)

Un dernier point : nous pouvons ajouter une gestion aux actions personnalisées dans l'extension également. Le système appelle la méthode `[didReceive(_:completionHandler:)](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/1845197-didreceive)` pour répondre à toute action sélectionnée. Si notre contrôleur de vue n'implémente pas cette méthode, le système livre l'action sélectionnée à votre application pour la gestion.

Si elle est implémentée, nous devons gérer toutes les actions possibles dans cette méthode. Une chose qui est importante ici est la fermeture `completion`.

`completion` : Le bloc à exécuter lorsque vous avez terminé l'exécution de l'action. Vous devez appeler ce bloc à un moment donné pendant votre implémentation. Le bloc n'a pas de valeur de retour.

La fermeture accepte un seul paramètre `dismiss` de type `[UNNotificationContentExtensionResponseOption](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextensionresponseoption)`. Nous fournissons les options suivantes :

1. `doNotDismiss` — Ne pas fermer l'interface de notification.
2. `dismiss` — Fermer l'interface de notification.
3. `dismissAndForwardAction` — Fermer l'interface de notification et transmettre la notification à l'application.

Cela résume nos notifications. Trop de choses à retenir ? **La pratique fait le progrès** ?. Essayez de créer vos propres notifications maintenant !

### Projet d'exemple

Vous pouvez télécharger le projet d'exemple [ici](https://github.com/pgpt10/Notifications).

Et l'exemple de projet pour **Notification Content Extension** peut être trouvé [ici](https://github.com/pgpt10/RichNotificationSample).

### Lecture complémentaire

N'oubliez pas de lire mes autres articles :

1. [Tout sur Codable dans Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
2. [Coloriez-le avec des DÉGRADÉS — iOS](https://hackernoon.com/color-it-with-gradients-ios-a4b374c3c79f)
3. [Coder pour iOS 11 : Comment glisser-déposer dans les collections et les tableaux](https://hackernoon.com/drag-it-drop-it-in-collection-table-ios-11-6bd28795b313)
4. [Tout ce que vous devez savoir sur les Today Extensions (Widget) dans iOS 10](https://hackernoon.com/app-extensions-and-today-extensions-widget-in-ios-10-e2d9fd9957a8)
5. [Sélection de UICollectionViewCell simplifiée..!!](https://hackernoon.com/uicollectionviewcell-selection-made-easy-41dae148379d)

N'hésitez pas à laisser des commentaires si vous avez des questions.