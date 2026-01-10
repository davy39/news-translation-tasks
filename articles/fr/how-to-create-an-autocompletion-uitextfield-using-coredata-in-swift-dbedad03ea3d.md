---
title: Comment configurer un UITextField d'auto-complétion utile en utilisant CoreData
  dans Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T19:27:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-autocompletion-uitextfield-using-coredata-in-swift-dbedad03ea3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qC1j-oZGtDOy3lYhYaWbHA.png
tags:
- name: ios app development
  slug: ios-app-development
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment configurer un UITextField d'auto-complétion utile en utilisant
  CoreData dans Swift
seo_desc: 'By Emrick Sinitambirivoutin

  All you need to know to build your autocompletion search bar with a UITableView
  and CoreData.


  _Photo by [Unsplash](https://unsplash.com/@grohsfabian?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" ti...'
---

Par Emrick Sinitambirivoutin

#### _Tout ce que vous devez savoir pour créer votre barre de recherche avec autocomplétion avec une UITableView et CoreData._

![Image](https://cdn-media-1.freecodecamp.org/images/0*nzfy7hZivPO7PeN6)
_Photo par [Unsplash](https://unsplash.com/@grohsfabian?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Fabian Grohs</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Dans cet article, je vais présenter comment j'ai construit un champ de recherche personnalisé avec une fonctionnalité d'autocomplétion pour récupérer des données à partir de CoreData. C'est un composant dont j'avais besoin dans l'une de mes applications et qui peut être très utile dans de nombreux cas pour améliorer l'expérience de l'utilisateur.

#### Nous allons voir :

* Comment configurer une application simple avec un UITextField de recherche
* Comment configurer une TableView pour afficher les résultats de recherche
* Comment effectuer des requêtes en temps réel sur les collections CoreData

### 1. Configuration du projet

Créez simplement une application avec une seule vue avec les composants suivants (vérifiez CoreData lors de la création du projet !). Pour être plus concret, imaginons que cela soit pour une application de recommandations de voyage et que l'utilisateur doive fournir un nom de ville pour obtenir toutes les informations sur le lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lxJev437cZZQtFP8zQ2few.png)

**UILabel :** Nous l'appellerons _topLabel._ Nous n'en aurons pas besoin.

**UITextField :** C'est le champ que nous allons personnaliser pour avoir un champ de recherche avec autocomplétion, alors appelons-le _searchTextField._

**UIButton :** C'est le bouton qui sera pressé lorsque l'utilisateur trouvera le lieu qu'il souhaite. Appelons-le _searchButton._

La tableView sera ajoutée de manière programmatique afin que vous puissiez voir comment la configurer dans n'importe quelle situation.

_Pour avoir un rendu magnifique, j'ai ajouté une UIImageView en arrière-plan avec une merveilleuse image de plage._

Pour connecter tous ces composants à notre View Controller, sélectionnez chacun d'eux et faites glisser leur référence en utilisant (**Control (ou Ctrl)  + Click**) vers votre fichier swift principal du View Controller.

### 2. Configurer notre classe CustomSearchTextField

Pour créer notre nouvelle classe, nous créons un nouveau fichier appelé _CustomSearchTextField.swift._ C'est dans cette classe, qui hérite de UITextField, que nous allons intégrer toutes les fonctionnalités dont nous avons besoin pour implémenter notre champ de recherche avec autocomplétion.

#### Création de la TableView avec les résultats :

Pour pouvoir afficher les résultats de complétion, nous devons instancier une UITableView qui affichera les résultats les plus pertinents comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fi0M9cyXLSiMkhZihagKIg.png)

Pour ce faire, nous devons créer un objet tableView puis l'ajouter à la vue actuelle. Afin de gérer cet nouvel objet, nous devons substituer des méthodes spécifiques comme montré ci-dessous. Tout le code nécessaire pour construire la searchTableView sera géré par cette méthode : _buildSearchTableView()_.

L'instanciation de la tableView est aussi simple que la création d'un nouvel objet UITableView, mais afin d'accéder à toutes les fonctionnalités de cet nouvel objet tableView, nous devons hériter des méthodes TableViewDelegates et TableViewDataSource. Il est important de prêter attention à deux variables importantes :

* **Le délégué de la tableView :** Cette variable nous permettra de spécifier quel objet de la vue doit être informé lorsque des changements se produisent dans la tableView (dans notre cas, cet objet est notre SearchTextField qui est dans ce contexte l'objet _self_)
* **La source de données de la tableView :** Cette variable nous permettra de spécifier comment tous les composants de la tableView seront créés et à partir de quelles données. Ici encore, nous devons la définir sur _self_.

La définition de ces deux variables nous permet de gérer certaines actions liées à la UITableView au sein de notre classe CustomSearchTextField.

Maintenant que la tableView est créée, nous devons y ajouter des données, et plus concrètement, ces données seront stockées dans des cellules. Nous utilisons des méthodes héritées de la classe TableViewDataSource pour configurer nos cellules et les ajouter à la tableView. En plus de cela, la méthode TableViewDelegates nous permettra de déclencher l'endroit où l'utilisateur clique et affichera le contenu de la cellule correspondante dans la console.

Mais si vous essayez d'exécuter le code ci-dessus, rien ne se passera car le cadre de la tableView n'est pas défini et nous n'avons pas amené la vue au premier plan. Afin de corriger cela, nous devons maintenant ajouter une méthode _updateTableView()_ :

Notre TableView est configurée et devrait maintenant fonctionner parfaitement ! Mais à ce stade, nous devons ajouter des données dans notre dataList si nous voulons afficher quelque chose. Pour le faire simplement pour l'instant, nous allons simplement ajouter des données factices à notre liste : le texte que l'utilisateur entre dans notre barre de recherche.

Mais le but principal de tout cela est de donner à nos utilisateurs des résultats d'autocomplétion pendant qu'ils tapent dans notre barre de recherche, nous devons donc observer quand l'utilisateur tape une nouvelle lettre et mettre à jour les données de la tableView en conséquence.

Comme vous pouvez le voir ci-dessus, nous avons modifié la méthode _willMove()_ afin de définir comment gérer chacune des interactions de l'utilisateur avec le textField. Celle qui nous intéresse est lorsque le champ de texte change (lorsque l'utilisateur tape). Ainsi, chaque fois que cette action est activée, nous ajoutons des données à notre liste et nous mettons à jour notre tableView.

#### Améliorer l'expérience utilisateur :

Même si notre searchField ne recherche rien du tout, vous devez avoir remarqué que lorsque nous tapons et que les résultats commencent à s'afficher, tous les résultats sont en texte brut. Cela ne ressemble pas beaucoup à une barre de recherche avec autocomplétion. Pour être plus convivial, il serait bien de mettre en évidence la partie du texte que nous avons déjà tapée dans le champ de texte et également de filtrer les résultats pour qu'ils correspondent à ce que nous tapons réellement. **Faisons cela** ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*qC1j-oZGtDOy3lYhYaWbHA.png)

Il est temps de créer notre méthode de filtre. Cette méthode filtrera les éléments pertinents de la dataList (ceux correspondant à ce que l'utilisateur commence à taper). Nous utiliserons la classe _NSMutableAttributedString_ pour pouvoir mettre en évidence la partie du texte que l'utilisateur a tapée dans le champ de texte.

Tout d'abord, nous créons une classe _SearchItem_ qui représentera chacun de nos résultats filtrés. Comme nous construisons notre merveilleuse application de recommandations de voyage, nous considérerons que ces éléments sont des noms de villes. Voici la classe _SearchItem_ :

Nous devons maintenant changer notre variable globale et en ajouter une nouvelle pour stocker nos éléments filtrés :

Ensuite, créons notre méthode de filtre :

En convertissant notre chaîne en _NSString_, nous pouvons utiliser la méthode _range()_ qui retourne la plage de la première occurrence d'une chaîne donnée dans la chaîne. En utilisant cette méthode, nous savons à la fois si la chaîne correspond à ce que l'utilisateur tape et la position de la chaîne correspondante ! C'est tout ce dont nous avons besoin pour mettre en évidence cette partie de notre élément. Nous faisons cela en utilisant les méthodes _setAttributes_ et nous ajoutons ensuite notre élément à la resultsList. Enfin, nous rechargeons les données dans notre tableView.

Créons de nouvelles données de test pour essayer notre implémentation :

Tout devrait fonctionner parfaitement, nous avons presque terminé ! ?

### 3. Effectuer des requêtes vers CoreData

C'est bien d'avoir une belle barre de recherche avec une tableView personnalisée pour afficher nos résultats filtrés avec autocomplétion, mais sans données, ce n'est pas très utile ?.

Connectons notre champ de texte de recherche au stockage CoreData.

#### Créer une base de données CoreData :

Afin de stocker nos données persistantes, nous allons créer une nouvelle entité (table) dans notre base de données avec deux attributs (lignes). Pour ce faire, nous cliquons sur le fichier .xcdatamodeld dans l'explorateur de fichiers et créons une nouvelle entité nommée Cities, ajoutons les deux attributs dont nous avons besoin : cityName et countryName.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E2fkTUHuGvS0utH3PFAZtw.png)
_CustomSearchField..xcdatamodeld_

Ensuite, nous modifierons le type de notre dataList dans _CustomSearchField.swift_ pour qu'il s'agisse d'une liste de Cities au lieu d'une liste de SearchItems :

```
var dataList : [Cities] = [Cities]()
```

#### Effectuer des requêtes sur la base de données créée :

Maintenant, nous devons créer quelques méthodes pour gérer l'enregistrement et la récupération de nouvelles données dans la base de données. Pour ce faire, nous devons créer un contexte. Le contexte est une zone spécifique où nous allons stocker toutes nos modifications avant de les valider dans la base de données. Si vous utilisez git, c'est comme la zone de staging. Vous ajoutez d'abord votre fichier à la zone de staging, et lorsque vous êtes prêt avec vos modifications, vous les validez dans votre git.

Nous modifions le début de notre méthode _filter()_ afin de requêter les données qui correspondent à l'entrée de l'utilisateur au lieu de récupérer toutes les données de la base de données :

La dernière chose à ajouter est une nouvelle méthode _addData()_ pour remplir notre base de données. Attention, cette fonction ne doit être appelée qu'une seule fois car les données stockées deviendront persistantes, alors commentez la ligne correspondante dans votre code (juste avant la création de la tableView dans _buildSearchTableView()_) après le premier appel ! Même si l'application est redémarrée, les données seront toujours disponibles dans la mémoire interne de l'appareil.

### C'est tout ! Nous avons terminé ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*6XJ4ermJVit_NYHatv6loQ.gif)

J'ai commencé à plonger dans la programmation Swift il y a quelques semaines avec un MOOC intéressant que j'ai trouvé sur Udemy. Après avoir acquis les bases du développement Swift et Xcode, j'ai commencé à travailler sur mes propres projets avec toute la documentation utile que j'ai trouvée sur le web. Ce premier tutoriel est une opportunité pour moi de partager toutes ces connaissances que j'ai acquises, alors j'espère que cela vous a aidé !

Si vous avez une question, n'hésitez pas à me le dire dans les commentaires ! Et n'oubliez pas de me donner un applaudissement si vous avez aimé l'article ???

Tout le code du projet final est disponible ici :

[**sinitame/customSearchField-medium**](https://github.com/sinitame/customSearchField-medium)  
[_Source code for Medium article : How to create an autocompletion UITextField using CoreData in Swift github.com](https://github.com/sinitame/customSearchField-medium)