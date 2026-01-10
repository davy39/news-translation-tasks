---
title: Authentification par numéro de téléphone avec programmation réactive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T11:28:11.000Z'
originalURL: https://freecodecamp.org/news/phone-number-authentication-with-reactive-programming-6e89a2a651d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PyLjEXgdDViFQJarHsi7lw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Authentification par numéro de téléphone avec programmation réactive
seo_desc: 'By Jinwoo Choi

  Phone Number Authentication

  Many mobile applications require membership. Most of them provide user authentication.
  This is because you need to check whether the user in use is the same as the subscriber
  when preventing duplicate subscr...'
---

Par Jinwoo Choi

### Authentification par numéro de téléphone

De nombreuses applications mobiles nécessitent une adhésion. La plupart d'entre elles fournissent une authentification utilisateur. Cela est dû au fait qu'il est nécessaire de vérifier si l'utilisateur en cours d'utilisation est le même que l'abonné lors de la prévention des abonnements en double ou du changement de mot de passe.

La plupart des applications mobiles utilisent un numéro de téléphone pour authentifier les utilisateurs, puisqu'elles fonctionnent sur des téléphones mobiles. L'authentification par numéro de téléphone se compose de plusieurs étapes, ce qui signifie qu'une gestion d'état est requise. Vous devez également modifier l'interface utilisateur en conséquence. Cela nécessite également une gestion asynchrone des événements, telle que la demande d'un code de vérification et la transmission du code saisi par l'utilisateur au serveur.

Par conséquent, l'authentification par numéro de téléphone peut être un très bon sujet pour écrire sur les compétences en développement. Dans cet article, je vais d'abord implémenter l'authentification par numéro de téléphone de la manière habituelle. Ensuite, je présenterai la programmation réactive.

### Flux UI de l'authentification par numéro de téléphone

![Image](https://cdn-media-1.freecodecamp.org/images/1*YOEtnAFE5I6BatRw0swIqA.png)

Pendant le processus d'authentification, vous devez modifier l'interface utilisateur pour chaque étape. Par exemple, le bouton concerné doit être activé en fonction de la présence de la valeur d'entrée. Et le composant UI doit être affiché ou masqué selon l'étape d'authentification. De plus, le conseil doit être affiché pour correspondre à la situation. Cet article se concentre sur les trois cas suivants.

* Activer le bouton [Demander un code de vérification] lors de la saisie d'un numéro de téléphone (Étape 1)
* Masquer le champ de texte [Code de vérification] et le bouton [Authentifier] lorsque l'authentification est réussie (Étape 4)
* Afficher le message pertinent (conseil) lorsque l'authentification est terminée ou a échoué (Étape 5)

### Structure de base

Tout d'abord, nous allons définir une énumération avec cinq états pour chaque étape d'authentification comme suit. Nous la déclarons comme une propriété de la classe Swift et elle a un observateur didSet. Nous allons ajouter le code qui change l'UI selon l'étape d'authentification ici.

```
enum PhoneNumberVerifyStep {    case inputPhoneNumber, inputVerifyNumber, verifying, succeed, failed}
```

Les composants UI se composent de deux champs de texte, de deux boutons et d'une étiquette comme suit. Tous sont créés via InterfaceBuilder et connectés à IBOutlet. Comme mentionné précédemment, nous avons déclaré une propriété de classe pour stocker l'étape d'authentification nommée verifyStep, et nous avons ajouté un observateur didSet pour gérer les changements d'UI.

### Changer l'UI en fonction de l'étape d'authentification

Voici la partie qui change réellement l'UI. Définissez la propriété isHidden du champ de texte [Code de vérification] et du bouton [Authentification] selon la valeur modifiée de **verifyStep**, et changez le texte de l'étiquette [Conseil].

Après avoir appelé l'API Restful depuis la méthode d'action du bouton [Authentification], définissez la valeur appropriée pour **verifyStep** selon la réponse. **Puisque nous avons utilisé l'observateur didSet pour changer l'UI, il y a un avantage à séparer le code UI et le code de traitement des données.**

Le fait que le bouton [Demander un code de vérification] soit actif dépend de la valeur d'entrée en temps réel du champ de texte [Numéro de téléphone], et non de l'étape d'authentification. Par conséquent, nous ajoutons un gestionnaire d'action à **phoneNumberTextField** qui définit **isEnabled** de **requestVerifyNumberButton** selon la valeur d'entrée.

De cette manière, nous avons implémenté les changements d'UI selon l'étape d'authentification par numéro de téléphone de la manière habituelle. Maintenant, après avoir examiné certains des inconvénients de l'ancienne méthode, je vais modifier l'exemple et le faire de manière réactive, ce qui est le sujet de cet article.

Tout d'abord, **l'implémentation interne de l'observateur didSet dans verifyStep peut être trop grande**. Et le code qui configure une vue peut exister dans plusieurs cas de l'instruction Switch. De nombreuses parties doivent être modifiées pour supprimer une vue spécifique ou ajouter une nouvelle vue. Par-dessus tout, il est difficile à lire si le code devient plus long.

Changer la propriété d'activation du bouton selon la valeur d'entrée du champ de texte peut être gênant : **le gestionnaire d'événements de saisie de texte doit être ajouté en continu si le nombre de champs de texte et de boutons nécessitant un traitement similaire est augmenté**. Si vous devez ajouter une logique de validation en temps réel à la valeur d'entrée dans le champ de texte, l'intérieur du gestionnaire d'événements peut être compliqué.

Maintenant, améliorons ces inconvénients en appliquant la programmation réactive. Ici, nous utilisons la bibliothèque open source [**ReactiveCocoa**](https://github.com/ReactiveCocoa/ReactiveCocoa).

### Programmation réactive

La programmation réactive est le processus de construction d'un programme utilisant une fonction qui répond au flux de données de manière séquentielle dans le temps. Le concept de base n'est pas nouveau — considérons les cas d'utilisation suivants. Par exemple, l'événement de clic du bouton est essentiellement l'observation d'événements asynchrones et l'abonnement via des rappels. De plus, Cocoa a déjà fourni un certain nombre d'outils pour implémenter des modèles d'observateur pour les données ainsi que les événements UI.

> [**La programmation réactive est la programmation avec des flux de données asynchrones.**](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754#reactive-programming-is-programming-with-asynchronous-data-streams)

> En un sens, ce n'est rien de nouveau. Les bus d'événements ou vos événements de clic typiques sont vraiment un flux d'événements asynchrone, sur lequel vous pouvez observer et faire quelques effets secondaires. Le réactif est cette idée sur les stéroïdes. Vous êtes en mesure de créer des flux de données de tout, pas seulement à partir d'événements de clic et de survol.

Cependant, la programmation réactive va au-delà de l'utilisation des outils mentionnés ci-dessus, à l'utilisation du modèle d'observateur comme cœur de la programmation.

Elle abstrait le flux de tous les types de données primitives gérées par l'UI — Action de contrôle, Notification, Délégation et KVO, qui sont des outils de base fournis par Cocoa, en tant que flux. Elle fournit également des fonctions pour traiter et filtrer les données qui y circulent, ce qui peut être facilement utilisé dans divers domaines.

En d'autres termes, la programmation réactive est une **façon plus intégrée et plus facile de gérer le traitement en chaîne de réaction (et la programmation basée sur celle-ci) dû aux changements d'état** que les méthodes traditionnelles.

Fondamentalement, son codage orienté fonction vise à effectuer un rôle unique dans une fonction connectée à un flux. Cela évite les programmes d'état compliqués tels que l'observateur didSet de verifyStep de l'exemple précédent, et facilite la gestion des erreurs et le contrôle de la concurrence du traitement asynchrone. Voir [ReactiveX.io](http://reactivex.io/) pour plus d'informations.

### Implémenter la programmation réactive

D'accord, il est temps d'arrêter d'expliquer de longues théories ennuyeuses. À partir de maintenant, améliorons l'exemple d'authentification par numéro de téléphone en utilisant la bibliothèque open source ReactiveCocoa.

Tout d'abord, nous supprimons le code qui change l'UI selon l'étape d'authentification de l'exemple précédent, et il ne reste que le squelette de base de ViewController. Nous supprimons également l'observateur didSet pour verifyStep, le gestionnaire d'action d'édition pour le TextField, et la méthode d'action pour le bouton [Authentifier].

Implémentez le code suivant en utilisant ReactiveCocoa basé sur le squelette. L'ensemble du code a été joint car il n'était pas long. Regardons d'abord **Property** de ReactiveSwift, et regardons l'implémentation en divisant le processus d'étape d'authentification en trois types comme montré dans l'exemple précédent.

### (Mutable) Property de ReactiveSwift

Property est une classe fournie par ReactiveSwift, qui est la base de ReactiveCocoa. Elle fournit la capacité de gérer les données comme un flux. Par exemple, dans le code d'exemple, **verifyStep** est un Holder pour les données de type PhoneNumberVerifyStep. Il peut générer un signal lors du changement de la valeur, ou changer la valeur en réponse à d'autres changements de données.

```
var verifyStep = MutableProperty<PhoneNumberVerifyStep>(...)
```

C'est-à-dire, lorsque la valeur de Property (verifyStep) change, l'UI peut être changée. Ou lorsque la valeur d'entrée du TextField est changée, la valeur de la variable (verifyStep) peut être changée avec elle. **L'observateur didSet de la propriété de la classe Swift fournit une fonctionnalité similaire.** Cependant, MutableProperty a l'avantage de pouvoir **changer ou filtrer les valeurs passées à travers le flux** comme décrit ci-dessus, et de **se connecter avec le code de changement d'UI de manière beaucoup plus concise.**

### Liaison UI et opérateur <~ de ReactiveCocoa

ReactiveCocoa fournit Binding pour gérer facilement les changements d'UI dus aux changements de Property. Le composant UI peut créer un BindingTarget pour chacun de ses attributs configurables. Et cela a une forme de Command Pattern.

Par exemple, ReactiveCocoa fournit BindingTarget, qui est la commande qui change le texte de UILabel. Le BindingTarget est exécuté lorsqu'un Signal est généré à partir du flux et définit la valeur reçue comme texte de l'UILabel.

L'opérateur <~ est fourni pour faciliter la connexion du Signal au BindingTarget. Par exemple, le code ci-dessous définit la valeur (valeur d'entrée) passée depuis le Signal (qui est généré lorsque la valeur du textField change) comme texte de l'étiquette.

```
label.reactive.text <~ textField.reactive.continuousTextValues
```

**label.reactive.text** retourne une instance **BindingTarget** qui change le texte, et **textField.reactive.continuousTextValues** retourne une instance **Signal** qui déclenche un événement lorsque la valeur d'entrée change. L'instance **BindingTarget** et l'instance **Signal** sont liées via **<~**, donc lorsque la valeur d'entrée du textField change, le texte de l'étiquette change avec elle.

La liaison UI de ReactiveCocoa est également un concept important jouant un rôle clé dans l'implémentation de la conception MVVM. Cela est dû au fait qu'il est possible de séparer le code de traitement des données du code de traitement de l'UI en liant les propriétés du ViewModel avec les composants UI dans la Vue.

### Réaction en chaîne réactive

Revenons maintenant au code d'exemple et voyons comment la Property et la liaison UI sont utilisées. Commençons par le processus d'activation du bouton [Demander un code de vérification] lorsqu'un numéro de téléphone est saisi. Le BindingTarget du bouton s'abonne au Signal de changement de valeur d'entrée généré par les continuousTextValues du TextField décrit ci-dessus.

```
requestVerifyNumberButton.reactive.isEnabled <~     phoneNumberTextField.reactive.continuousTextValues    .map { !($0?.isEmpty ?? true) }
```

Le BindingTarget isEnabled de requestVerifyNumberButton a été lié au Signal de changement de valeur d'entrée de phoneNumberTextField et l'opérateur <~ a été utilisé dans le processus.

La propriété isEnabled du bouton est une propriété de type Bool. La valeur d'entrée du TextField est de type string, donc la valeur ne peut pas être directement assignée.

Par conséquent, lorsque la valeur de la chaîne est passée, elle est changée en un type Bool via la méthode map du Signal. Il est clair que **les données de flux**, qui est un avantage clé de la programmation réactive**, sont faciles à traiter et peuvent être exprimées de manière courte et concise.**

Examinons le changement d'état du bouton, du champ de texte et de l'étiquette en fonction de la valeur de verifyStep qui occupe la plus grande partie de l'exemple.

```
var verifyStep = MutableProperty<PhoneNumberVerifyStep>(...)
```

Tout d'abord, verifyStep est déclaré comme un MutableProperty. verifyStep peut maintenant servir de flux de données, et les composants UI peuvent s'abonner à un Signal de changement de valeur de celui-ci. La propriété value retourne la valeur primitive de verifyStep.

Ce qui suit est la liaison des composants UI au Signal de verifyStep. De même, l'opérateur <~ connecte le BindingTarget qui change les propriétés isHidden et text des composants UI avec le Signal de verifyStep. C'est-à-dire, si la valeur de verifyStep est changée, les attributs UI tels que isHidden et text sont changés en conséquence.

```
verifyNumberTextField.reactive.isHidden <~ verifyStep    .map { $0 == .succeed }
```

```
verifyButton.reactive.isHidden <~ verifyStep.map { $0 == .succeed }
```

```
statusLabel.reactive.isHidden <~ verifyStep.map { !$0.isVerifiedStep }
```

```
statusLabel.reactive.text <~ verifyStep.signal    .filter { $0.isVerifiedStep }.map { $0 == .succeed ? ... }
```

Utilisez la méthode **map** pour lier la valeur de type Enum appelée PhoneNumberVerifyStep à la propriété de type Bool. Utilisez la méthode **filter** pour vous assurer que le texte dans statusLabel change uniquement lorsque verifyStep est .succeed ou .failed.

Jusqu'à ce point, la réaction en chaîne entre les données et l'UI a été améliorée de manière réactive lors de l'implémentation de l'authentification par numéro de téléphone. Plus besoin d'observateurs didSet. **Les méthodes complexes de changement d'UI ont également disparu.**

L'approche réactive nous permet de définir comment un seul composant UI changera à l'avenir avec une représentation concise. Elle améliore également la lisibilité du code. De plus, il y a moins de choses à changer lors de l'ajout ou de la suppression de composants UI.

Enfin, voyons comment gérer l'événement de contrôle UI via ReactiveCocoa.

### Gestion des événements de contrôle UI avec ReactiveCocoa

ReactiveCocoa fournit également un moyen de gérer les événements de contrôle UI comme des flux. Comme les continuousTextValues du TextField que nous avons vus précédemment, ReactiveCocoa a ajouté une propriété qui retourne une instance Signal pour l'événement de contrôle du composant UI. Le Signal pour l'événement UI peut être lié au BindingTarget, ou il peut avoir un observateur directement.

```
verifyButton.reactive.controlEvents(.touchUpInside).observeValues {     self.api.getUsersVerify(...)        .on(value: { _ in            self.verifyStep.value = .succeed        })        .on(failed: { error in            self.verifyStep.value = .failed        })}
```

Dans l'exemple, nous avons ajouté l'observateur directement au Signal de l'événement UI. La méthode controlEvents a retourné un Signal pour l'événement touchUpInside, et le gestionnaire d'observateur a été ajouté via la méthode observeValues.

Le processus simple de changement du texte de l'étiquette lorsque le bouton est touché est possible par liaison via l'opérateur <~.

```
label.reactive.text <~ button.reactive.controlEvents(.touchUpInside)    .map { _ in "hello" }
```

Récapitulons le processus jusqu'à présent. Si un signal se produit lors de l'abonnement à un flux de l'événement UI, il appelle l'API distante. Changez la valeur de MutableProperty selon la valeur passée au gestionnaire de réponse de l'appel asynchrone. En même temps, un signal de changement de valeur est généré à partir du flux de MutableProperty, et l'UI qui est liée au signal de changement est modifiée.

Maintenant, nous avons changé l'exemple d'authentification par numéro de téléphone pour qu'il soit conforme à la définition de la programmation réactive. La plupart du traitement est effectué avec l'abonnement au flux et la liaison UI.

### Conclusion

Nous avons changé l'authentification traditionnelle par numéro de téléphone pour utiliser la programmation réactive. Ce n'est pas un nouveau concept — Swift et Cocoa fournissent déjà de nombreux outils pour le traitement asynchrone, la gestion des événements UI et l'implémentation du modèle d'observateur. Cependant, utiliser la manière réactive est plus élégante et concise que la manière classique. De plus, il y a un avantage à pouvoir l'utiliser pour concevoir la structure du programme comme MVVM.

Tout dans le monde de la programmation est lié à **la manière dont nous comprenons bien le code**. Il est important qu'il soit facile à maintenir. À cet égard, adopter l'approche réactive est une décision très intelligente. Il est vrai que c'est plutôt difficile à utiliser pour la première fois. Cependant, je suis convaincu que si vous vous y habituez, vous pouvez coder beaucoup plus succinctement qu'avant, et implémenter facilement l'UI et la logique utilisateur.

Regardons à nouveau les avantages de la programmation réactive :

* Le code qui répond aux changements de données spécifiques ou de composants UI est simplifié.
* Parce que vous n'avez pas à créer une méthode énorme de code concentré qui change l'UI, il devient plus facile de gérer de nouveaux états ou d'ajouter ou de supprimer des composants UI.
* Le codage fonctionnel vous permet d'écrire du code qui peut se concentrer sur les situations et les rôles.
* Avec l'observation et la liaison, vous pouvez séparer ViewController en ViewModel et View, ce qui est un facteur clé dans l'application de la conception MVVM.

J'espère que de nombreux développeurs pourront coder plus heureusement grâce à la programmation réactive. Merci d'avoir lu cette histoire.

J'écris sur le développement d'applications iOS en utilisant Swift. J'apprécierais également votre intérêt pour les articles suivants.

[**Syntaxe Promise avec ReactiveSwift**](https://medium.com/@JinwooChoi/promise-syntax-with-reactiveswift-ae9b397a1bef)
[_Utilisez ReactiveSwift pour écrire du code similaire à Promise en JavaScript._medium.com](https://medium.com/@JinwooChoi/promise-syntax-with-reactiveswift-ae9b397a1bef)
[**Utilisation des Enums en Swift**](https://medium.com/@JinwooChoi/using-enums-in-swift-7d9cd7729758)
[_Comment gérer les constantes, les valeurs brutes et les expressions d'un type Enum via Swift._medium.com](https://medium.com/@JinwooChoi/using-enums-in-swift-7d9cd7729758)
[**Passage de paramètres à l'API Restful avec Swift Codable**](https://medium.com/@JinwooChoi/passing-parameters-to-restful-api-with-swift-codable-d78eb78f7b1)
[_Comment non seulement les données reçues de l'API Restful, mais aussi les données à transmettre, peuvent être gérées facilement via..._medium.com](https://medium.com/@JinwooChoi/passing-parameters-to-restful-api-with-swift-codable-d78eb78f7b1)