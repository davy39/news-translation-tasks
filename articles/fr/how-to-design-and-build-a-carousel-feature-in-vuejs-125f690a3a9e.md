---
title: Comment concevoir et construire une fonctionnalité de carrousel dans VueJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T18:04:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-and-build-a-carousel-feature-in-vuejs-125f690a3a9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DbM53D4CMawSuTN7V9AEqg.png
tags:
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Vue.js
  slug: vuejs
seo_title: Comment concevoir et construire une fonctionnalité de carrousel dans VueJS
seo_desc: 'By Fabian Hinsenkamp

  A carousel, slideshow, or slider — however you call it this class of UI — has become
  one of the core elements used in modern web development. Today, it’s almost impossible
  to find any Website or UI library which doesn’t come with...'
---

Par Fabian Hinsenkamp

Un carrousel, diaporama ou slider — peu importe comment vous appelez cette classe d'interface utilisateur — est devenu l'un des éléments de base utilisés dans le développement web moderne. Aujourd'hui, il est presque impossible de trouver un site web ou une bibliothèque d'interface utilisateur qui ne soit pas équipé d'un type de carrousel ou d'un autre.

Pourquoi donc ? En fait, les carrousels méritent vraiment leur popularité. Ils permettent aux utilisateurs de parcourir le contenu disponible sans faire défiler verticalement ou sans mouvements de souris lourds. Par conséquent, les utilisateurs gagnent du temps et peuvent se concentrer sur le contenu affiché, car les carrousels maintiennent la charge cognitive à un minimum.

**C'est une raison suffisante pour apprendre à construire un carrousel dans VueJS !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*fWQBrTW-CQ3r47e9HtGrRg.gif)

Tous mes tutoriels gravite autour des applications Vue progressives. Celui-ci ne fait pas exception ! Créer des applications progressives signifie offrir une expérience utilisateur pour les utilisateurs mobiles proche des applications natives, incluant des performances excellentes, des fonctionnalités natives comme les notifications push, une expérience hors ligne et bien plus encore. Dans un monde où la majorité des utilisateurs expérimentent le Web via des appareils mobiles, il n'y a plus d'excuse pour ne pas construire des applications progressives !

Bien sûr, vous pouvez toujours utiliser le carrousel dans n'importe quelle application Vue. Vous n'avez pas non plus besoin d'expérience préalable avec VueJS ou les applications Web progressives pour ce tutoriel !

Vous trouverez le code complet ici :

[https://github.com/fh48/vue-pwa-carousel](https://github.com/fh48/vue-pwa-carousel)

### Quelle est notre vision pour le carrousel ?

La première chose que nous allons faire est de nous faire une idée générale des types de composants que nous voulons construire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sq_XDCNnG63BCNWP_zojnA.png)

Il y en a quelques-uns très simples :

* **Card** → elle contient les informations de chaque élément du carrousel.
* **Carousel** → parent qui contient toute la logique
* **ArrowButton** → aide à naviguer entre plusieurs cartes.
* **Indicator** → montre le nombre de cartes et celle qui est actuellement visible.

### Installation initiale

Si vous voulez apprendre comment configurer un projet, cette section est pour vous. Dans le cas contraire, continuez simplement avec la section suivante.

```
vue init pwa vue-pwa-carousel
```

Nous serons invités à choisir une configuration prédéfinie — je recommande la configuration suivante :

```
? Project name vue-pwa-carousel? Project short name: fewer than 12 characters to not be truncated on homescreens (default: same as name) vue-pwa-carousel? Project description A simple tax calculator ? Author Fabian Hinsenkamp? Vue build runtime? Install vue-router? No? Use ESLint to lint your code? No? Pick an ESLint preset Standard? Setup unit tests with Karma + Mocha? No? Setup e2e tests with Nightwatch? No
```

Exécutez `yarn` dans le dossier racine du projet pour installer toutes les dépendances. Maintenant, nous avons un projet configuré qui inclut les technologies de base dont nous avons besoin pour construire notre carrousel. De plus, il inclut déjà un Service Worker qui pré-cache tous nos fichiers statiques et permet aux utilisateurs d'accéder à l'application même lorsqu'ils sont hors ligne.

Vous pouvez voir à quoi ressemble l'application modèle en exécutant `yarn start`.

Pour tester l'apparence du carrousel sur mobile, nous devons exposer notre build de développement aux appareils mobiles via une URL publique. Il existe de nombreuses façons de le faire, mais ici nous utilisons `ngrok` car il est facile à configurer et fait simplement son travail.

```
yarn global add ngrok
```

Ensuite, nous devons exécuter notre serveur de développement et ngrok dans deux terminaux séparés.

### Construisons la Card !

![Image](https://cdn-media-1.freecodecamp.org/images/1*eR5j_AAOlOLRaTmNxm8hrQ.png)

Pour vous éviter quelques ajustements ennuyeux à l'application modèle, consultez simplement cette branche `00_basicSetup`. Elle inclut toutes les données et styles dont nous avons besoin pour rendre cette application significative et joli.

La Card fait vraiment une chose : elle montre les données actuellement sélectionnées. Ce qui, dans notre cas, est une _image_, un _titre_ et un peu de _texte_.

Clairement, nous ne voulons pas construire plusieurs cartes avec un contenu codé en dur. Au lieu de cela, nous voulons passer les données dynamiquement à la carte et simplement les rendre.

Sur la base de cette connaissance, nous pouvons maintenant créer notre fichier `Card.vue` dans le dossier `src/components`. De plus, nous pouvons déjà définir la structure HTML de base et les noms et leurs types de propriétés que nous voulons passer à la carte.

Attention : nous stockons toutes les icônes que nous voulons afficher localement dans notre dossier d'assets. Cela signifie que notre chemin reste le même, mais nous devons changer dynamiquement les noms de fichiers qui doivent être rendus. Par conséquent, toutes les propriétés sont de type `String`.

Ensuite, nous faisons en sorte que la **Card** rende le titre et le texte associé. Pour cela, nous utilisons la méthode la plus basique de liaison de données dans VueJS — la balise mustache.

Ce sont essentiellement des accolades autour de nos variables de prop. Dès que les données arrivent, `{{headline}}` et `{{text}}` seront remplacés par l'objet de données associé. Cela est toujours vrai, même lorsque de nouvelles données arrivent, après avoir rendu d'autres données auparavant.

Le rendu de l'image de manière dynamique est un peu plus délicat. Souvenez-vous, nous ne passons pas l'icône réelle mais seulement son nom de fichier.

Donc, nous voulons essentiellement consommer l'image comme un module, comme n'importe quel autre composant. Une image statique que nous pourrions consommer en l'important dans le bloc de script et en l'assignant à une variable. Cependant, nous avons un chemin changeant. Comme notre application utilise webpack, il existe un raccourci fantastique disponible pour charger ces images dynamiquement comme suit :

```
:src="require(`@/assets/svg/${imgName}`)"
```

La syntaxe `:` est la manière Vue de lier dynamiquement les attributs à une expression. Vous avez peut-être déjà vu le préfixe `v-bind:` dont `:` est le raccourci.

Maintenant, notre bloc `template` est complété et ressemble à ce qui suit.

Pour finaliser notre composant **Card**, nous devons simplement ajouter les styles préparés au bas du fichier.

```
<style src="../assets/styles/Card.css" scoped>
```

La dernière chose que nous devons faire pour cette section est de vérifier si la **Card** fonctionne réellement.

Alors, ajoutons-la simplement à notre composant `App.vue`. Cependant, gardez à l'esprit que nous devrons déplacer le composant dans le composant **Carousel** dans la section suivante.

Nous ajoutons ce qui suit aux blocs `<template>` et `<script>` de App.vue.

Quel résultat fantastique ! Surtout, puisque nous pouvons déjà changer dynamiquement ce que la **Card** doit afficher !

![Image](https://cdn-media-1.freecodecamp.org/images/1*X9YAXb78elPnqKN2da1SFQ.png)

Ensuite, nous construisons le **Carousel** pour avoir un composant dédié à la gestion de toute la logique autour de l'affichage de différentes **Cards** en fonction des entrées de l'utilisateur.

Consultez la branche `01_Card` si vous voulez commencer à partir d'ici ou comparer votre implémentation.

### Construisons le Carousel

Le **Carousel** sera notre composant parent réutilisable. Il encapsulera tous les composants et la logique pertinents.

Comme avec la Card précédemment, nous devrions nous concentrer sur la construction du composant de manière à ce qu'il puisse gérer un changement de données avec élégance. Par exemple, il devrait être capable de gérer des nombres variables de cartes qui lui sont passées.

Ensuite, nous verrons comment cette approche se traduit en code. Tout d'abord, nous commençons par créer un composant **Carousel** et faisons de la **Card** un enfant du **Carousel**.

Le bloc de modèle du nouveau composant héberge la **Card**, enveloppée dans deux éléments wrapper. Nous verrons plus tard pourquoi ceux-ci sont nécessaires.

Comme nous allons passer les données de plusieurs Cards au Carousel, nous devons spécifier que seul le `currentElement` est rendu.

Dans le bloc `<script>` suivant, nous devons définir lequel des Cards passés est le `currentElement` par défaut.

Pour cela, nous définissons initialement l'`currentElementIndex` à `0`. VueJS vient avec une fonctionnalité qui nous permet de calculer des variables dynamiquement. Nous l'utilisons pour sélectionner les données de la carte qui doit être rendue initialement.

Maintenant, nous devons simplement remplacer la **Card** par le **Carousel** dans notre fichier `App.vue`. Pour donner un peu plus de structure et de sens à notre page finale, enveloppons le carrousel dans un autre élément de section et plaçons-le avant l'autre section.

C'est notre implémentation de base. Ce n'est pas encore tout à fait un Carousel, mais nous allons changer cela en ajoutant les boutons fléchés pour basculer entre les objets que nous passons dans le tableau `cards` à notre **Carousel**.

Consultez le `02_Carousel` pour voir le code complet de cette section. Si vous avez codé, vous devriez voir ce qui suit devant vous.

### Construisons le ArrowButton

![Image](https://cdn-media-1.freecodecamp.org/images/1*oT4qITnEHmeHR6hXhoM7dQ.png)

Maintenant, nous construisons le composant **ArrowButton**, qui reçoit ses méthodes et le type d'icône de flèche de son parent. L'implémentation elle-même est simple.

Le composant est uniquement responsable du rendu des styles corrects et de l'icône. Toute la logique liée aux boutons est ajoutée au **Carousel**. De cette manière, nous avons créé un composant véritablement générique que nous pourrions utiliser dans n'importe quel contexte où nous voulons utiliser un bouton avec une icône de flèche.

Maintenant, dans **Carousel**, nous ajoutons deux méthodes pour naviguer entre nos objets de données de carte. Les méthodes sont simplement un autre objet exporté dans le bloc `<script>`.

Celles-ci augmentent ou diminuent simplement l'`currentElementIndex` de `1`. Nous utilisons l'index pour calculer la variable `currentElement`, donc chaque fois qu'une des méthodes est appelée, la carte suivante est affichée. Nous ajoutons également quelques conditions restrictives, car nous ne voulons pas que le Carousel boucle.

Maintenant, nous devons simplement ajouter les **ArrowButtons** pour compléter notre **Carousel** !

Voici comment nous utilisons les méthodes et les valeurs calculées pour implémenter l'un de nos **ArrowButtons**. Essayez d'implémenter le second en dessous du composant **Card**.

Au cas où vous seriez bloqué ou que quelque chose ne semble pas correct, consultez la branche `03_ArrowButton`. Si tout a fonctionné, votre carrousel devrait ressembler à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fD7AdSRaWe7JRtW_2RNd5A.gif)

### Construisons les Indicators !

![Image](https://cdn-media-1.freecodecamp.org/images/1*ILDy8sTuoLO9WdnpsKyACA.png)

La dernière fonctionnalité que nous allons ajouter sont les **Indicators**. Ceux-ci aident les utilisateurs à comprendre combien de Cards il y a et laquelle ils regardent actuellement. De plus, ceux-ci permettent à l'utilisateur de sélectionner des Cards individuelles directement.

Le composant reçoit trois propriétés. Le tableau des `elements` que nous utilisons pour créer un élément `<li>` pour chaque objet de données de carte.

`currentElementIndex` est requis pour ajouter une classe CSS qui met en évidence l'indicateur lié à la carte actuelle. De plus, il est utilisé pour désactiver le bouton de la carte actuelle. De cette manière, nous l'empêchons d'être sélectionnable via les touches de tabulation. De cette manière, nous fournissons au moins un minimum d'accessibilité.

`showElement` est la méthode qui est appelée lorsqu'un utilisateur clique sur un indicateur. Elle est passée de l'extérieur pour garder le composant aussi focalisé que possible. Comment un élément est affiché n'est clairement pas une préoccupation des **Indicators**.

Lorsque nous ajoutons les **Indicators** à `Carousel.vue`, il devient clair pourquoi nous avons créé deux wrappers pour la **Card**. Le HTML sémantique et clair est vital, surtout pour les grands projets avec un haut niveau de complexité.

Vous pouvez consulter le code complet à la branche `04_Indicators`.

### Ajoutons le swipe

Dernier point mais non des moindres, nous rendons notre **Carousel** compatible avec les mobiles. Une bonne application web progressive ne commence pas par la mise en cache des fichiers statiques, mais par la réactivité.

Comme nous manquons d'espace sur les petits écrans, nous masquons les **ArrowButtons** et permettons aux utilisateurs de balayer pour parcourir les **Cards**. Ici, les Indicators portent à nouveau leurs fruits, car ils fonctionnent sur mobile comme l'indicateur principal que les utilisateurs peuvent balayer pour voir plus de cartes.

Pour cela, nous ajoutons la bibliothèque suivante :

```
yarn add vue2-touch-events
```

Ensuite, nous ajoutons le nouvel attribut `v-touch` et une méthode de gestionnaire à la **Card**. Cela prend en charge les événements émis par les balayages.

### Conclusion

Fantastique, nous l'avons fait ! Nous avions la vision de construire un composant **Carousel** encapsulé et réutilisable, et nous l'avons fait !

Ce que nous pourrions encore ajouter pour améliorer l'UX sont quelques animations de balayage lors de la navigation dans les cartes.

Merci d'avoir lu ! _Si vous aimez cet article de blog, suivez-moi sur Twitter [@Fa_Hinse](https://twitter.com/Fa_Hinse) et_ _applaudissez s'il vous plaît ?_