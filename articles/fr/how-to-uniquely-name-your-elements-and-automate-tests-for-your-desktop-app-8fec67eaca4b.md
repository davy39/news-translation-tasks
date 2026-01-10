---
title: Comment nommer de manière unique vos éléments et automatiser les tests pour
  votre application de bureau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T20:43:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-uniquely-name-your-elements-and-automate-tests-for-your-desktop-app-8fec67eaca4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N9MfB3_mghGuOlRHX5YAzw.jpeg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment nommer de manière unique vos éléments et automatiser les tests
  pour votre application de bureau
seo_desc: 'By Vinicius de Melo Rocha

  Motivation

  Writing automated tests for Desktop applications is not an easy task. Especially
  when it uses Windows Presentation Foundation (WPF). This allows so many possibilities
  of nested control and complex grids and menus....'
---

Par Vinicius de Melo Rocha

### Motivation

Écrire des tests automatisés pour les applications de bureau n'est pas une tâche facile. Surtout lorsqu'elles utilisent Windows Presentation Foundation (WPF). Cela permet tant de possibilités de contrôles imbriqués et de grilles et menus complexes.

Ici chez [Clemex](https://www.clemex.com/), nous utilisons un outil pour automatiser les tests de bureau qui repose sur la propriété WPF `[FrameworkElement.Name](https://msdn.microsoft.com/en-us/library/system.windows.frameworkelement(v=vs.110).aspx)` pour interagir avec l'application. Parce que nous devons créer des contrôles dynamiques basés sur des données de collection, ils peuvent finir par avoir le même nom pour plusieurs éléments d'interface utilisateur.

Par exemple, le code suivant génère un menu basé sur une collection de panneaux.

En inspectant l'arborescence des éléments, nous verrions que nous avons maintenant plusieurs éléments avec le même nom : « MenuBtn ».

Pour éviter cette situation et avoir des noms uniques pour chaque bouton, nous avons trouvé quatre approches différentes.

* Utilisation du Code-Behind
* Utilisation de la liaison de données
* Utilisation des propriétés attachées
* Utilisation des index de collection

### Utilisation du Code-Behind

En supposant que nous avons accès à un identifiant unique dans le contexte de données des éléments. L'approche la plus simple consiste à utiliser l'événement `Loaded` de `FrameworkElement` pour définir un nom unique en utilisant le modèle code-behind.

Maintenant, lorsque nous vérifions l'arborescence des éléments, nous verrons que nous avons des noms uniques pour chaque bouton.

### Utilisation de la liaison de données

L'utilisation de la liaison de données rend notre code beaucoup plus propre, ainsi que plus facile à lire et à comprendre. Si nous essayons une approche similaire en utilisant la liaison de données, nous pourrions finir avec un code source comme suit :

Malheureusement, si nous essayons de construire ce code, nous obtiendrons une erreur de compilation avec le message :

> Les MarkupExtensions ne sont pas autorisées pour les valeurs de propriété Uid ou Name, donc '{Binding Panel.PanelType, StringFormat='MenuBtn{0}'}' n'est pas valide.

Cette restriction nous empêche de lier directement à la propriété `Name`.

### Utilisation des propriétés attachées

Pour surmonter la limitation de la tentative précédente, nous pouvons définir une nouvelle propriété qui définirait le nom pour nous. Pour ajouter de nouvelles propriétés aux contrôles existants, nous pouvons utiliser [Attached Properties](https://docs.microsoft.com/en-us/dotnet/framework/wpf/advanced/attached-properties-overview).

L'événement `OnValueChanged` se déclenche chaque fois que la valeur de notre propriété change. Lorsque cela se produit, nous obtenons la nouvelle valeur et la définissons comme nom de `FrameworkElement`. Nous donnons à notre propriété attachée le nom `Name`. Cela pourrait être n'importe quoi, comme `CustomName` ou `TestName`.

Pour utiliser la nouvelle propriété, nous devons ajouter un espace de noms au XAML et attacher la propriété à notre bouton.

Notre code se compilera maintenant sans aucun problème, et nous aurons des noms uniques pour chaque élément.

### Utilisation des index de collection

Dans l'exemple précédent, nous avons créé des noms uniques en ajoutant la propriété `Id`. Il existe d'autres scénarios où nous n'avons pas d'ID sur l'élément pour créer un nom d'élément unique. Pour cela, nous pouvons utiliser l'index de la collection.

Essayons de lier notre collection de boutons à une liste de chaînes.

Pour y parvenir, nous pouvons utiliser la même `AttachedProperty` avec un convertisseur. Il recherchera l'index de l'élément à l'intérieur de la collection.

Dans le XAML, nous utiliserons maintenant [MultiBinding](https://msdn.microsoft.com/en-us/library/system.windows.data.multibinding(v=vs.110).aspx) car nous avons besoin à la fois de l'élément et de la collection.

En regardant l'arborescence des éléments, nous pouvons voir que nos boutons sont nommés `MenuBtn00`, `MenuBtn01` et ainsi de suite.

### Résumé

Générer des noms uniques pour les contrôles WPF créés dynamiquement peut être fait de manière élégante en utilisant des propriétés attachées et en utilisant la multi-liaison avec un convertisseur personnalisé.