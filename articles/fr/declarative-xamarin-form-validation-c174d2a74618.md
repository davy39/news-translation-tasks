---
title: Comment implémenter la validation déclarative des formulaires Xamarin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T20:42:38.000Z'
originalURL: https://freecodecamp.org/news/declarative-xamarin-form-validation-c174d2a74618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wIHOFE3kSzR9ysT_PeSNbg.png
tags:
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Validation
  slug: validation
- name: xamarin forms
  slug: xamarin-forms
seo_title: Comment implémenter la validation déclarative des formulaires Xamarin
seo_desc: 'By Ameer Jhan

  If you have an existing Xamarin.Forms codebase and want to add validation without
  affecting your code behind or view model, then this is for you. ?

  What made me write this article?

  Our team designed and developed a Xamarin mobile app wi...'
---

Par Ameer Jhan

Si vous avez une base de code **Xamarin.Forms** existante et que vous souhaitez ajouter une validation sans affecter votre code-behind ou votre modèle de vue, alors cet article est fait pour vous. ?

### Qu'est-ce qui m'a poussé à écrire cet article ?

Notre équipe a conçu et développé une application mobile Xamarin avec plusieurs formulaires sans aucune validation, car nous avions peu de temps et nous étions satisfaits des validations back-end seules.

Avec le temps, notre besoin d'ajouter une validation front-end a grandi avec l'application. Nous avons donc décidé d'ajouter des validations sans affecter notre code-behind ou notre modèle de vue. Il n'y avait aucun article pour nous aider avec cette stratégie, alors j'ai décidé d'en écrire un.

### Prérequis

Je suppose que vous êtes à l'aise avec les **Behaviors** de **Xamarin**. Si ce n'est pas le cas, veuillez lire la documentation ci-dessous — elle est très simple et directe.

[**Xamarin.Forms Behaviors - Xamarin**](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/behaviors/)  
[_Les Behaviors vous permettent d'ajouter des fonctionnalités aux contrôles de l'interface utilisateur sans avoir à les sous-classer. Les Behaviors sont écrits_docs.microsoft.com](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/behaviors/)

### Ce que nous allons obtenir

Le résultat sera des validations hautement lisibles et déclaratives dans le XAML, en gardant le code-behind et le modèle de vue à l'écart de la validation !

### Points à noter

Lorsque le code est trop long pour être digéré en une seule explication, je le diviserai en plusieurs sections et utiliserai trois points de suspension (**…**) à la place du code des sections précédentes ou à venir.

### Quel est le plan ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*eO3Oa1jcdCXtPz-Y-bC1Vw.gif)

Nous pouvons bien planifier notre approche si nous réfléchissons aux choses de base qui se produisent lors de la validation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h8ib08-kXOGLsaZLy_E6Tw.png)

Le schéma ci-dessus est une représentation très abstraite de notre conception entière. Pour éclairer davantage le code réel, regardez l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wIHOFE3kSzR9ysT_PeSNbg.png)

### Assez parlé — codons !

L'interface suivante aide à maintenir la cohérence entre les différents validateurs que nous définissons.

Écrivons maintenant quelques implémentations pour quelques validateurs courants.

Certains validateurs peuvent nécessiter quelques paramètres supplémentaires. Par exemple, **FormatValidator** nécessite un paramètre de format, et ces paramètres peuvent être ajoutés en tant que champs dans la classe.

Il existe plusieurs façons d'afficher une erreur. Vous pouvez préférer l'afficher juste en dessous du contrôle, ou vous pouvez préférer l'afficher sous forme de résumé en haut du formulaire. Pour accommoder ces différents styles d'affichage des erreurs, nous définissons une interface pour maintenir la cohérence.

Pour simplifier, j'ai implémenté un style d'erreur très basique qui ajoute et supprime simplement une étiquette en dessous du contrôle en cours de validation.

Il est maintenant temps pour la partie **Xamarin Behavior**, qui assemble tout le code ci-dessus.

**_style:** Ce champ est initialisé avec notre implémentation personnalisée BasicErrorStyle. Cela nous aidera à afficher et supprimer l'erreur chaque fois que nécessaire.

**_view:** Il s'agit du contrôle sur lequel cette validation est placée.

**PropertyName:** Il s'agit de la propriété du contrôle qui doit être validée selon les règles de validation, par exemple la propriété Text d'un contrôle Entry ou la propriété SelectedItem d'un contrôle picker.

**Validators:** Il s'agit de la liste des règles de validation selon lesquelles la propriété du contrôle sera validée.

La méthode **Validate()** parcourt toutes les règles de validation et exécute la méthode Check sur la valeur de la propriété du contrôle. Si toutes les règles de validation passent, la méthode **RemoveError** est appelée sur _style. Sinon, la méthode **ShowError** est appelée sur _style.

La partie restante du code attache et détache simplement les méthodes **OnPropertyChanged, OnUnFocussed** aux événements PropertyChanged et UnFocussed du contrôle chaque fois que ce comportement est ajouté au XAML.

Lorsque ces événements sont déclenchés, ils appellent la méthode **Validate()** que nous avons définie précédemment, qui à son tour ajoute ou supprime l'erreur selon les besoins.

### Comment l'utiliser

![Image](https://cdn-media-1.freecodecamp.org/images/1*faxCWiiC5i0D70YwDtwLxA.gif)

Oui, l'attente est enfin terminée ! Vous pouvez maintenant ajouter ces validations à votre XAML en important les espaces de noms XAML nécessaires.

Si vous exécutez l'application maintenant, vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5yLoqd4n7YXnarwHpkA4Ng.gif)

### Valider l'ensemble du formulaire

Voici le prochain défi : comment savoir si l'ensemble du formulaire est valide ? C'est-à-dire, comment savoir que tous les contrôles du formulaire contiennent des données valides ?

Pour y parvenir, nous créons un autre comportement appelé **ValidationGroupBehavior**, dans lequel nous regroupons les contrôles à valider ensemble pour valider un formulaire entier.

**_validationBehaviors:** il s'agit d'une liste de comportements de validation provenant de divers contrôles à valider.

**IsValidProperty:** il s'agit d'une propriété liable à laquelle vous pouvez accéder dans le XAML pour vérifier si le formulaire est valide ou non.

Nous exposons deux méthodes, à savoir **Add()** et **Remove(),** pour aider les contrôles à s'ajouter ou à se supprimer d'un groupe de validation particulier.

Nous exposons également une méthode, **Update(),** pour aider les contrôles à actualiser la validité du formulaire chaque fois que leurs données changent. Cette méthode exécute à son tour toutes les validations dans **_validationBehaviors** et définit la valeur de la propriété **IsValid** en conséquence.

### Refactorisation de notre ValidationBehavior

Faisons un peu de refactorisation de notre classe ValidationBehavior pour accommoder le regroupement de validation des contrôles :

Nous avons ajouté une propriété appelée **Group** pour stocker le groupe de validation auquel appartient le contrôle. Les méthodes **Group.Add()** et **Group.Remove()** sont appelées lorsque ce comportement est attaché ou détaché, respectivement, d'un contrôle. À son tour, cela ajoute ou supprime le contrôle d'un groupe de validation particulier. Chaque fois que le contrôle perd le focus, il met à jour la validité du groupe en appelant la méthode **Group.Update()**.

### **ValidationGroupBehavior en action**

Mettez à jour le fichier XAML comme indiqué ci-dessous pour voir l'efficacité des groupes de validation :

Le code ci-dessus ajoute le **ValidationGroupBehavior** à l'élément parent de tous les contrôles, puis il ajoute sa référence à la propriété **Group** du **Validator** dans le contrôle. Vous pouvez ensuite utiliser la propriété **IsValid** du groupe de validation pour activer ou désactiver un bouton de soumission. Sympa, non ?

Si vous exécutez l'application maintenant, vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SBHPeDHSnbAUrewSoqn6pw.gif)

### Qu'en est-il des validateurs asynchrones ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1YQKAMnGRv5rfERe9TNxyA.gif)

Je peux entendre la question bourdonner dans votre esprit. Une bonne chose à propos de notre conception est qu'elle peut être étendue très facilement avec peu d'effort. Cela peut être réalisé en déclarant simplement une autre interface comme indiqué ci-dessous :

Vous pouvez maintenant créer une implémentation pour un validateur asynchrone, par exemple **AsyncUserExists**, qui retourne une tâche qui se résout en un booléen. Ajoutez une nouvelle propriété à **ValidationBehavior** appelée **AsyncValidators** et ajoutez des validateurs asynchrones à cette propriété. Une petite addition de async et await au processus de validation résoudra notre problème.

### Avons-nous enfin terminé ?

Nous avons couvert pas mal d'informations de manière très simple. Mais il y a quelques fonctionnalités sympas que vous pouvez essayer vous-même :

* Debounce pour les validateurs asynchrones
* Vérifier si le contrôle est modifié (l'utilisateur a tapé quelque chose) ou non avant d'afficher une erreur

### Confus ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*f7rU8GMQ234_69Lx5rWOyw.gif)

Si vous êtes confus ou avez des zones d'ombre, n'hésitez pas à me contacter dans les commentaires. Vous pouvez également vous référer à mon application de démonstration sur GitHub que j'ai liée ci-dessous.

[**ameerthehacker/XamarinFormValidationDemo**](https://github.com/ameerthehacker/XamarinFormValidationDemo)  
[_XamarinFormValidationDemo - Il s'agit d'une application de démonstration pour mon blog medium sur les validations de formulaires xamarin_github.com](https://github.com/ameerthehacker/XamarinFormValidationDemo)

### TL;DR

Si vous êtes paresseux comme moi, ou si vous ne voulez pas écrire beaucoup pour obtenir la fonctionnalité ci-dessus, alors vous pouvez attendre que je développe un package NuGet pour les validations de formulaires Xamarin en utilisant la stratégie ci-dessus. Vous êtes les bienvenus pour contribuer, et je l'ai lié ci-dessous.

[**ameerthehacker/XamarinFormValidation**](https://github.com/ameerthehacker/XamarinFormValidation)  
[_XamarinFormValidation - Validations déclaratives, flexibles et hautement configurables dans Xamarin sans effort :hearts:_github.com](https://github.com/ameerthehacker/XamarinFormValidation)

Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements ?