---
title: Comment construire un système de design avec SwiftUI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-09T23:42:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-design-system-with-swiftui
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/preview-1.png
tags:
- name: Design
  slug: design
- name: Design Systems
  slug: design-systems
- name: iOS
  slug: ios
- name: Swift
  slug: swift
- name: SwiftUI
  slug: swiftui
- name: 'tech '
  slug: tech
seo_title: Comment construire un système de design avec SwiftUI
seo_desc: 'By Vince MingPu Shao

  Building a design system to support one product is not easy - it has to be robust
  and flexible at the same time for scalability. Though challenging, lots of great
  resources have shared useful principles and approaches that help t...'
---

Par Vince MingPu Shao



Construire un système de design pour supporter un produit n'est pas facile - il doit être robuste et flexible en même temps pour être scalable. Bien que ce soit un défi, de [nombreuses](https://www.designbetter.co/design-systems-handbook/building-design-system) [ressources](https://lightningdesignsystem.com/design-tokens/) [formidables](https://medium.com/eightshapes-llc/tokens-in-design-systems-25dd82d58421) [ont](https://www.youtube.com/watch?v=wDBEc3dJJV8) partagé des principes et des approches utiles qui aident les équipes à construire un bon système, tant visuellement que programmatiquement. En s'appuyant sur leurs travaux, cet article tente de contribuer à un domaine encore inexploré en se concentrant sur la construction d'un bon système en `SwiftUI`.

## Pourquoi j'écris cet article

Lors de mon premier été à l'[ITP](https://tisch.nyu.edu/itp) à New York, j'ai eu la chance d'avoir l'opportunité de travailler en tant que stagiaire développeur iOS chez [Line Break Studio](https://www.linebreak.studio/). Une des tâches qui m'a été assignée est de construire un système de design en deux étapes : d'abord visuellement dans [Sketch](https://www.sketch.com/), puis programmatiquement en `SwiftUI`. L'expérience d'expérimenter avec ce nouveau framework et de construire un système de design avec celui-ci a été incroyable, mais aussi semée d'embûches. C'est pourquoi nous aimerions partager notre expérience avec la communauté, dans l'espoir de faciliter votre processus de développement.

---

## Qu'est-ce que [SwiftUI](https://developer.apple.com/documentation/swiftui)

Apple a publié ce nouveau framework révolutionnaire lors de la [WWDC 2019](https://developer.apple.com/videos/wwdc2019/?q=swiftui), qui est l'un des meilleurs des dernières années. Du point de vue d'un développeur web, l'expérience de développement de projet dans `SwiftUI` est plus proche de celle des frameworks et stacks front-end conventionnels.

C'est définitivement une avancée formidable car la programmation d'interfaces et la gestion des états sont considérablement plus faciles qu'auparavant. Et le meilleur aspect de cette amélioration est que l'on peut [intégrer UIKit et SwiftUI de manière fluide](https://developer.apple.com/tutorials/swiftui/interfacing-with-uikit). Pour apprendre les bases de SwiftUI, les [tutoriels officiels](https://developer.apple.com/tutorials/swiftui/tutorials) fournis par Apple sont très utiles.

%[https://youtu.be/aH7oWxfxpJY]

## Le projet de démonstration

À des fins de démonstration, j'ai mis en place une version simplifiée du système de design que nous avons construit chez [Line Break Studio](https://www.linebreak.studio/). Il s'agit d'un ensemble de composants **boutons** sous différentes formes, qui sont construits sur la base de deux parties de niveau inférieur : **typographie** et **palette de couleurs**.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/preview-record.gif)
_Vue de rendu dynamique du projet de démonstration_

Le projet est [public sur GitHub](https://github.com/vince19972/SwiftUI-Design-System-Demo), et j'utilise `Xcode 11 Beta 5` pour le développement. Une [base Airtable](https://airtable.com/shrHQdv9vQGz7UMQj) en tant que hub de gestion du système de design (lire [plus sur la gestion du flux de travail](https://www.vinceshao.com/blog/a-better-web-development-workflow-confluence-airtable-jira-and-abstract)) est également publique pour référence.

---

## Principes de construction d'un système de design

Le système de design en code est un middleware entre les designers et les développeurs. Le développeur du système prend les entrées du système de design sous forme visuelle et produit une API identique pour un développement ultérieur. Deux principes suivants doivent être reconnus pour compléter ce système en code :

### 1. Communiquer avec des [tokens](https://medium.com/eightshapes-llc/tokens-in-design-systems-25dd82d58421)

Fondamentalement, le but d'avoir un système de design en programme n'est pas de mieux gérer le code ou l'efficacité du développement, mais de s'assurer que la **vue** est cohérente avec les fichiers de design. Pour atteindre cet objectif, l'utilisation de tokens pour signifier une certaine couleur, police, taille ou tout autre élément visuel est cruciale pour maintenir la qualité de la communication entre les développeurs, les designers et les managers d'une équipe.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/lightning-token.png)
_[Tokens du Lightning Design System](https://www.lightningdesignsystem.com/design-tokens/) construit par Salesforce_

### 2. Niveaux de hiérarchie

Dans [l'article d'EightShapes](https://medium.com/eightshapes-llc/tokens-in-design-systems-25dd82d58421), il est souligné que nous devrions "Montrer les options en premier, puis les décisions ensuite", car "Vous ne pouvez pas prendre de décisions sans options."

![Image](https://www.freecodecamp.org/news/content/images/2019/09/eightshape-article.png)
_[Article d'EightShapes](https://medium.com/eightshapes-llc/tokens-in-design-systems-25dd82d58421) sur les tokens de design_

Ce type d'architecture d'ordonnancement réduit le degré de couplage entre les différents niveaux, offrant ainsi plus de flexibilité et de dynamisme pour les révisions possibles. La manière dont je structure les niveaux est dans cet ordre, du bas vers le haut : material → base → token. Mais cela peut être fait de toute manière qui convient à l'équipe.

---

## Plongeons dans le code

La section suivante est une liste de points forts que nous aimerions souligner en fonction de notre expérience. Veuillez [visiter le dépôt GitHub](https://github.com/vince19972/SwiftUI-Design-System-Demo) pour le code complet. Tous les retours ou critiques sont les bienvenus pour des améliorations.

### 1. Architecturer les niveaux de hiérarchie

Il existe deux façons d'empiler les matériaux de bas niveau pour construire des tokens de haut niveau :



* **Utiliser `enum` pour la sécurité des types et la lisibilité du code**

Les avantages de l'utilisation de enum dans le code en tant que wrapper de regroupement ou paramètre dans une fonction ont déjà été bien reconnus. Un point qui mérite d'être mentionné ici est la mise en œuvre des niveaux de hiérarchie.

Nous stockons toujours les valeurs brutes, y compris la taille de la police (`CGFloat`) et le nom de la police (`String`), au niveau le plus bas, car nous ne voulons pas les modifier. Mais parce que la valeur brute doit être un littéral dans enum, nous ne pouvons pas simplement assigner un `case` à être une valeur d'un autre enum.

Pour contourner ce problème, nous implémentons une fonction `getValue`, qui retourne la valeur brute dans le `switch` case lorsque cela est nécessaire.

<script src="https://gist.github.com/vince19972/8ff8635bdb7bfdf54b85ab711b55f634.js"></script>



* **Utiliser `struct` pour une structure plus facile**

Bien que enum soit formidable, nous n'avons pas besoin de sa fonctionnalité unique dans certains cas. Par exemple, parce que `Xcode` prend en charge le travail lourd de traitement des couleurs dynamiques, et qu'aucun paramètre d'option n'est requis dans l'API endpoint, nous pouvons configurer les palettes de couleurs par deux niveaux simples de struct.

<script src="https://gist.github.com/vince19972/70eee7d66735739aa31567efd7a0a475.js"></script>



### 2. Nommage clair et direct de l'endpoint `API`

La convention de nommage est un autre sujet vaste pour la discussion et le débat. En plus des conventions de base [Swift](https://swift.org/documentation/api-design-guidelines/), les deux seules règles que nous suivons sont, 1) pas d'acronyme et 2) garder cela simple. Par exemple, pour utiliser la typographie et le système de couleurs, au lieu de créer de nouveaux endpoints, nous faisons une extension des structs Font et Color. Cette approche réduit l'effort de mémorisation des noms d'API peu familiers pour les développeurs.

<script src="https://gist.github.com/vince19972/d0b132129a2f57b3588bfb942dabfe63.js"></script>



### 3. Gérer les ensembles de couleurs dynamiquement dans deux modes

Ainsi, le mode sombre est devenu une norme dans l'industrie, et les équipes [iOS](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/dark-mode/) et [Android](https://material.io/design/color/dark-theme.html) ont implémenté cette fonctionnalité. C'est une bonne tendance pour les utilisateurs, mais cela peut poser quelques défis aux designers et aux développeurs, notamment la gestion et le nommage des ensembles de couleurs, en particulier ceux en échelle de gris.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/material-dark.png)
_Guide du thème sombre de [Material Design](https://material.io/design/color/dark-theme.html)_

Pour penser et communiquer sur les couleurs en échelle de gris de manière dynamique, utiliser des termes comme _blanc_, _clair_, _noir_ ou _foncé_ ne fonctionne pas. Parce que si nous faisons référence à une couleur dynamique `#000000` (noir en HEX) _noir_ ou _foncé_ dans le `schéma de couleur clair`, comment parler de cette couleur particulière, qui devrait devenir `#FFFFFF` (blanc en HEX), dans le `schéma de couleur foncé` ? _defaultDark_ ou _lightDark_ ?

![Image](https://www.freecodecamp.org/news/content/images/2019/09/color-transition.png)
_Transition confuse des ensembles de couleurs_

Il est très confus de nommer les ensembles de couleurs dynamiques en échelle de gris avec l'approche conventionnelle. Pour éviter cette confusion, nous utilisons `theme` et `contrast` pour gérer un ensemble de couleurs dans les schémas `light` et `dark` à la place.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/airtable-color-1.png)
_Exemple de nommage des couleurs dans la base de démonstration [Airtable](https://airtable.com/shrHQdv9vQGz7UMQj)_

Notez qu'une couleur en échelle de gris n'a pas toujours besoin d'être inversée dans le mode de couleur opposé. Dans ces situations où la couleur claire reste claire et la couleur foncée reste foncée, nous la nommons simplement claire ou foncée.

Une fois que nous avons compris cette méthode de nommage, la gestion de cette architecture de palette de couleurs est facile dans `Xcode`. Pour créer un ensemble de couleurs, il suffit de créer un nouveau fichier `Asset Catalog` → ajouter un nouvel `Color Set` → et changer `Appearances` en `Any, Light, Dark`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/color-asset.png)
_Comment ajouter un asset de couleur dans Xcode_



### 4. Paramètres `environment`

Une fonctionnalité incroyable du framework SwiftUI est le [modificateur d'environnement](https://developer.apple.com/documentation/swiftui/environment), qui offre la possibilité de contrôler les [valeurs d'environnement](https://developer.apple.com/documentation/swiftui/environmentvalues) sur la vue cible. En termes de construction de système de design, cette capacité offre une approche pratique pour changer la police de l'application au niveau racine. Et l'autre avantage de l'utilisation de `environmentValue` est de changer et de tester les schémas de couleurs clairs et foncés en développement.

<script src="https://gist.github.com/vince19972/e9cd9d11cc198e80f51a99efabb7e927.js"></script>



### 5. `buttonStyle` et étiquette de bouton

Comparé aux anciens jours dans [UIKit](https://developer.apple.com/documentation/uikit), la construction de boutons réutilisables dans SwiftUI est considérablement plus facile. La [vue Button](https://developer.apple.com/documentation/swiftui/button) se compose de deux parties, qui sont la fermeture `action` (événement à déclencher lorsque le bouton est pressé) et `label` (corps du bouton). La vue peut ensuite être enchaînée avec un modificateur `buttonStyle`. Pour apprendre les détails sur la construction de boutons réutilisables, je recommande de lire le [tutoriel d'Alejandro](https://alejandromp.com/blog/2019/06/22/swiftui-reusable-button-style/), qui est complet et utile.

Dans nos composants de boutons personnalisés, la première étape consiste à créer deux structs, incluant `TokenButtonLabel` et `TokenButtonStyle`. Ces deux structs sont programmés selon les types de boutons que nous avons dans les fichiers de design. Par exemple, il n'y a que deux types d'étiquettes : icône et texte. Chaque type a une fonction `init` correspondante conçue avec différents paramètres pour les nouvelles instances.

<script src="https://gist.github.com/vince19972/78f3424ed8a39d2f7787a8c723d4b50b.js"></script>

D'autre part, il y a quatre principaux types de styles de boutons : icône circulaire, icône, capsule et texte. Pour suivre le protocole `ButtonStyle`, une fonction `makeBody` doit être implémentée. Cette fonction nous apporte une propriété `configuration`, fournissant une valeur native `isPressed` pour surveiller si le bouton est pressé ou non.

<script src="https://gist.github.com/vince19972/ffb1d1757fd847120611cc73f190d1be.js"></script>

Enfin, en s'appuyant sur `TokenButtonLabel` et `TokenButtonStyle`, l'endpoint de l'API du composant bouton sera `TokenButton` - un regroupement qui enveloppe le contenu et le style du bouton ensemble, conformément aux types de boutons dans le système de design visuel.

<script src="https://gist.github.com/vince19972/2ddb3ddc1709283da61e929c1076a7fb.js"></script>



### 6. `AnyView` comme wrapper

Alors que nous traitons la fonction `makeBody` apportée par le protocole `ButtonStyle`, nous avons trouvé un conseil utile pour travailler avec `View`. Pour stocker une vue dans une variable, l'annotation de type pourrait être indiquée comme `AnyView`, qui fonctionne comme un conteneur général de vues dans SwiftUI.

Dans notre cas, parce que nous voulons ajouter le modificateur d'opacité à `configuration.label` pour tous les types de boutons, au lieu de le faire de manière répétée dans chaque `switch` case, il est plus logique de chaîner le modificateur à la fin ensemble. Nous pouvons atteindre ce modèle en utilisant l'avantage de `AnyView` de cette manière :

<script src="https://gist.github.com/vince19972/ffb1d1757fd847120611cc73f190d1be.js"></script>



### 7. Construire un modificateur de vue avec une fonction `mutating`

Pour mettre à jour les styles des boutons dynamiquement, nous pouvons construire notre propre modificateur. D'abord, instanciez des propriétés d'état mutables personnalisées dans la vue, puis créez une fonction `mutating` qui retourne un type `Self` après avoir mis à jour la propriété d'état cible.

<script src="https://gist.github.com/vince19972/b0cfbcf08dfb28520b47201e3f490de4.js"></script>



### 8. Style de bordure délicat

Un inconvénient de SwiftUI est que le style d'une forme circulaire avec une bordure circulaire n'est pas du tout intuitif. J'ai lutté pendant un moment, et j'ai finalement trouvé une [solution ici sur StackOverflow](https://stackoverflow.com/questions/57269651/add-a-border-with-cornerradius-to-an-image-in-swiftui-xcode-beta-5). Un modificateur `clipShape` et un modificateur `overlay` sont nécessaires pour que cela fonctionne.

<script src="https://gist.github.com/vince19972/f41cd800660e6a714a84c588aecd12e5.js"></script>



---

## Conclusion

SwiftUI est une amélioration incroyable d'Apple. Bien que des défauts existent encore, construire un système de design robuste et flexible avec celui-ci, et encore plus des interfaces utilisateur compliquées dans iOS, est bien plus efficace que jamais. J'espère que cet article est utile pour toute équipe iOS essayant de construire des interfaces utilisateur, et je suis toujours ouvert à tout retour !

? Lisez plus de mes travaux sur [vinceshao.com](https://www.vinceshao.com) / Suivez-moi sur [Twitter](https://twitter.com/vincemingpushao) ou [LinkedIn](https://www.linkedin.com/in/vinceshao/)