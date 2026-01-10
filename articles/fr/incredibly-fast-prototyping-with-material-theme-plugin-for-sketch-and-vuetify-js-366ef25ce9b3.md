---
title: Comment créer un prototype en un temps record avec le Material Theme Plugin
  pour Sketch et Vuetify.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-10T23:58:55.000Z'
originalURL: https://freecodecamp.org/news/incredibly-fast-prototyping-with-material-theme-plugin-for-sketch-and-vuetify-js-366ef25ce9b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-QMWv7Bv0N6QOcSUCeBu-Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Material Design
  slug: material-design
- name: prototyping
  slug: prototyping
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment créer un prototype en un temps record avec le Material Theme Plugin
  pour Sketch et Vuetify.js
seo_desc: 'By Adam Wattis

  When developing an MVP (Minimum Viable Product), you intend to go from idea to prototype
  as fast as possible. The faster you can prototype your idea, the faster you are
  able to iterate upon it.

  As you’re moving from abstract idea to wo...'
---

Par Adam Wattis

Lors du développement d'un MVP (Minimum Viable Product), vous souhaitez passer de l'idée au prototype le plus rapidement possible. Plus vous pouvez prototyper votre idée rapidement, plus vous pouvez itérer rapidement.

Alors que vous passez d'une idée abstraite à un prototype fonctionnel, vous ne voulez généralement pas passer beaucoup de temps à créer un design personnalisé lorsque vous devriez vous concentrer sur la fonctionnalité de l'application. Pour résoudre ce problème, nous utilisons des frameworks comme Bootstrap pour obtenir rapidement une mise en page structurée avec une interface utilisateur qui a l'air "plutôt bien" sans trop d'efforts.

Ce que nous voulons vraiment atteindre, en termes de design, c'est créer **rapidement** une interface utilisateur qui soit **reconnaissable** et **cohérente**.

Je vais vous montrer une méthode super rapide pour passer d'une idée abstraite à un design, puis à un prototype fonctionnel avec Material Design. Material Design est le système de design open source de Google qu'ils utilisent pour toutes leurs applications. Cela le rend reconnaissable car il est intuitif et facile à naviguer, et la plupart des gens sont déjà familiers avec lui. Si ce n'est pas déjà fait, vous devriez absolument découvrir ce qu'est [Material Design](https://material.io/).

En utilisant le plugin Material Design pour Sketch, nous allons créer notre propre système Material Design personnalisable. Cela inclura un excellent ensemble de composants qui nous permettra de créer rapidement des designs cohérents pour notre application prototype. L'application que nous allons créer est une simple application de rappels.

Nous allons utiliser le framework front-end Vue.js avec la bibliothèque de composants Material Design Vuetify.js pour réaliser nos designs d'application. Commençons !

### Création du système de design

[Téléchargez](https://material.io/tools/theme-editor/) ce plugin pour Sketch. Une fois installé, allez simplement dans Plugins > Material > Open Theme Editor pour voir l'éditeur de thème Material Design. Cliquez sur "Create New Theme", et nous choisissons de commencer avec le thème Baseline.

Nous avons maintenant notre système Material Design de composants Sketch.

![Image](https://cdn-media-1.freecodecamp.org/images/LuaHmcKZg8RwSJmcVazNctiDo75Sdf0KqHwP)
_Votre bibliothèque de composants._

Dans l'éditeur de thème, vous pouvez changer la couleur primaire et secondaire, changer la police, changer la forme des coins des éléments et inclure des icônes personnalisées. Pour cet exemple, nous ne changerons aucun de ces éléments et nous en resterons aux valeurs par défaut.

Nous avons maintenant créé notre système de design. Comme vous pouvez le voir, il est indiqué que le document est une **bibliothèque**. Cela signifie que toute modification que vous apportez à ce fichier Sketch affectera vos maquettes et mettra à jour tous vos designs avec ces modifications. N'est-ce pas génial ?

Avant de continuer, nous allons également installer le plugin Sketch Material, qui ajoutera certains modules que nous utiliserons bientôt.

### **Maquettes**

Commençons par ouvrir un nouveau document Sketch, puis créons un nouveau plan de travail iPhone et enregistrons-le sous **MaterialReminders.sketch**. C'est ici que nous créerons nos designs pour notre application. Mais d'abord, explorons la riche bibliothèque de composants à notre disposition.

Sous **Insert > Symbols**, vous devriez voir la bibliothèque de composants que nous venons de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/vxaJm-KKTX25ZzXOZV1KeHcchXY63uvpyN12)
_Explorez tous les composants de notre bibliothèque et imaginez les possibilités !_

Tellement de composants ! Nous pouvons maintenant commencer à créer nos designs. Mais d'abord, nous devons décomposer les fonctionnalités que nous voulons pour cette application de rappels. Nous la gardons simple et ajoutons uniquement la possibilité de :

* Ajouter un nouveau rappel
* Supprimer un rappel
* Cocher un rappel de votre liste de tâches
* Décocher un rappel de votre liste de tâches complétées

Fantastique, accélérons les choses et commençons à déposer quelques composants dans notre premier plan de travail iPhone.

Nous commençons par une barre de navigation supérieure. Déposez-la et placez-la, puis redimensionnez-la pour qu'elle s'adapte à l'écran. Nous devons changer la première icône en "Icon / Add / Filled" pour l'icône de menu et changer la couleur de l'icône en blanc. Ensuite, changez toutes les autres icônes en aucune, puisque nous n'en aurons pas besoin. Nous changeons également le titre en Rappels.

![Image](https://cdn-media-1.freecodecamp.org/images/ZCb-U7Is9ahlpicmLCUmc93MeN4CpWUj-FhF)
_La personnalisation pour vos besoins devient super facile avec les remplacements de symboles._

Nous allons maintenant commencer à déposer quelques rappels factices. Nous allons créer nos rappels comme une liste, alors trouvons un composant adapté. Nous utiliserons "List / Single Line / Indent / Body 2".

Maintenant, nous allons centrer l'objet de la liste, supprimer le diviseur inférieur, définir le texte sur "Corvées" et enfin changer l'icône en "Icon / Checked Circle / Outlined".

![Image](https://cdn-media-1.freecodecamp.org/images/9Prfl9hSretZJqgP0l-AhgJ0ey7uVXKSZVmR)

Ajoutez un titre en insérant un champ de texte, puis utilisez le module Plugins > Sketch Material > Typography pour changer le style en Subhead.

![Image](https://cdn-media-1.freecodecamp.org/images/tINK-Ts33QE0vIUe4orSqhCF8oNVsP4t3-p2)
_Lors de la sélection d'un champ de texte et de l'accès au module Typography, vous pouvez cliquer sur un style pour l'appliquer._

Cela commence à avoir l'air plutôt bien jusqu'à présent ! Mais nous sommes maintenant confrontés à un problème. Nous voulons également inclure des contrôles de liste à **droite** dans chaque objet de liste, car nous voulons ajouter un bouton de suppression là. Mais les développeurs de Google n'ont pas inclus de remplacement pour cela dans le composant Sketch. Pas de souci, nous allons résoudre cela en allant dans notre fichier de bibliothèque et en ajoutant notre icône au symbole, mettant ainsi à jour tout notre projet.

Allez dans la bibliothèque et trouvez le composant de liste que nous avons utilisé dans la page Material Components. Ensuite, double-cliquez dessus pour accéder à son symbole. Cliquez sur l'icône à gauche pour qu'elle soit en focus, puis copiez-collez et déplacez-la vers la droite. C'est fait.

![Image](https://cdn-media-1.freecodecamp.org/images/S8X8VqUhxaBO0GjO92TkQz0-sxDn3UjSCKh1)

Lorsque nous revenons à notre projet, nous pouvons maintenant voir que dans le coin supérieur droit, il est écrit "Library Updates Available".

![Image](https://cdn-media-1.freecodecamp.org/images/0FUd44ijqurPseWYOj3eSPZiHhjhDgO1ckiU)
_Des modifications ont été détectées dans la bibliothèque. Vous pouvez choisir de mettre à jour vos designs avec ces nouvelles modifications._

Maintenant, nous devrions pouvoir changer l'icône de droite en "Icon / Close / Filled" qui sera le bouton pour supprimer un rappel complètement de la liste.

Pour créer une liste de rappels, nous copions simplement et collons plusieurs objets de liste, changeons leur texte, puis changeons le titre que nous avons ajouté en Todo.

![Image](https://cdn-media-1.freecodecamp.org/images/-TrerR8NqmxuW9wOCg9wz2aDGTyPiUzzzdOA)
_La liste Todo est complète._

Ensuite, nous copions et collons cette liste entière pour créer la liste Complétée. Dans cette nouvelle liste, vous devez changer le titre en "Complétée", puis changer toutes les icônes à gauche pour qu'elles soient remplies au lieu d'être en contour.

![Image](https://cdn-media-1.freecodecamp.org/images/AcZpO-zEL-N5FIEcPk5yDThcsL83K50ozWQt)
_Sélectionnez tous les éléments de la liste pour changer les icônes de tous en même temps._

Nous avons presque terminé avec nos maquettes. Pour accélérer les choses, j'ai simplement changé la couleur de notre plan de travail en #FAFAFA et ajouté un "Shadow / 00dp" derrière chacune de mes listes.

![Image](https://cdn-media-1.freecodecamp.org/images/JoFxDKR5zSuNcGsBZgh9em9RRu15tH2hkYoQ)
_Maquette terminée._

Cette vue de maquette est maintenant complète. La suivante que nous devons créer est la boîte de dialogue qui apparaît lorsque vous appuyez sur le bouton d'ajout.

Nous commençons par copier et coller le plan de travail sur lequel nous avons travaillé pour créer une copie exacte. Ensuite, nous utilisons les modules Dialogue et Form sous "Plugins / Sketch Material" pour créer une boîte de dialogue et un formulaire séparément. Ceux-ci sont ensuite combinés et une boîte opaque est placée derrière. J'ai remplacé le bouton d'action transparent dans la boîte de dialogue par un bouton de couleur primaire.

![Image](https://cdn-media-1.freecodecamp.org/images/aelleiqG6FnghDdfwGT9YtRF7jnYn8OfMvrp)

Nous avons maintenant terminé avec Sketch. Bien sûr, nous pourrions ajouter plus de fonctionnalités et étendre nos maquettes encore plus, mais nous allons garder cela simple pour l'instant. La prochaine étape consiste à écrire le code qui deviendra notre application !

### Vue avec Vuetify

Maintenant, la partie amusante — le codage. Nous allons utiliser Vue.js, qui est une bibliothèque d'interface utilisateur front-end écrite en JavaScript. Elle est vraiment facile à apprendre, et consulter leur [site web](https://vuejs.org/v2/guide/) serait une première étape. Pour implémenter Material Design, nous allons utiliser la bibliothèque de composants [Vuetify.js](https://vuetifyjs.com/en/getting-started/quick-start) qui inclut un ensemble de composants Vue ainsi qu'un système de grille pour organiser facilement votre mise en page.

Nous commençons simplement en copiant et collant le balisage d'exemple qui se trouve sur la page de démarrage de Vuetify. Voyons ce que cela fait pour nous.

Lorsque vous regardez le HTML, commencez par l'extérieur et travaillez vers l'intérieur.

Nous avons nos balises `<head></head>` et `<body></body>`. À l'intérieur de la balise `<head></head>`, nous avons des balises `<link>` qui vont importer le fichier vuetify.min.css requis et les polices Google.

Dans le `<body></body>`, nous avons un `<div></div>` et à l'intérieur de celui-ci, nous avons quelques composants Vuetify, par exemple `<v-app></v-app>` et `<v-content></v-content>`, qui sont signifiés par le "v-" dans leurs noms.

Plus bas, vous avez deux balises `<script></script>` qui importent les modules Vue.js et Vuetify.js dans notre page.

![Image](https://cdn-media-1.freecodecamp.org/images/q0VKlrkzc1mWE6qa2hyVy2sBYK0gLKlTtDin)

Enfin, après les instructions d'importation, il y a une troisième balise `<script></script>` qui crée une nouvelle instance Vue(). C'est ici que nous allons écrire tout notre code JavaScript.

Nous pouvons voir que l'instance s'accroche à '#app' qui est l'ID de la balise `<div></div>` dans notre HTML. Cela permet à notre instance Vue de savoir où injecter notre interface utilisateur.

À l'intérieur de la balise `<v-content></v-content>`, nous allons bientôt placer tous nos composants Vuetify. Mais d'abord, nous allons enregistrer ce que nous avons pour l'instant sous index.html, puis ouvrir le fichier dans notre navigateur, où nous devrions voir "Hello world".

Nous continuons en cherchant dans la documentation de Vuetify le HTML dont nous avons besoin pour le composant de la barre de navigation supérieure. La balise que nous cherchons est `<v-toolbar app></v-toolbar>`. Nous devons également ajouter un `<v-btn></v-btn>` à l'intérieur de cette barre de navigation afin de pouvoir appuyer dessus pour afficher la boîte de dialogue permettant d'ajouter de nouveaux rappels.

Dans ce bouton, nous allons également ajouter un événement `@click=` qui définira `addModal` sur `true`, ce qui fera apparaître la boîte de dialogue modale. Nous ajoutons cela entre les balises `<v-content></v-content>` :

```
<v-toolbar app color="primary">  <v-btn color="primary darken-1" icon @click="addModal = true">    <v-icon>add</v-icon>  </v-btn>  <v-toolbar-title>    Rappels  </v-toolbar-title></v-toolbar>
```

Ensuite, nous devons ajouter le HTML pour la boîte de dialogue. Cela se trouvera juste après la balise `<v-toolbar-title></v-toolbar-title>`, mais toujours à l'intérieur de la balise `<v-toolbar></v-toolbar>`. Voici la boîte de dialogue :

```
<v-dialog v-model='addModal'>  <v-card>    <v-card-title>Ajouter un rappel</v-card-title>    <v-card-text>      <v-container grid-list-md>        <v-layout wrap>          <v-flex md12>            <v-text-field v-model="newTask" label="Nouvelle tâche"></v-text-field>          </v-flex>          <v-flex md12>            <v-btn color="primary" @click="add">Ajouter</v-btn>          </v-flex>        </v-layout>      </v-container>    </v-card-text>  </v-card></v-dialog>
```

Ici, nous ajoutons un `<v-card-title>` avec "Ajouter un rappel" comme titre. Ensuite, nous utilisons le système de grille de Vuetify pour créer une liste qui s'étend sur toutes les 12 colonnes. Nous ajoutons un `<v-text-field>` qui se lie à 'newTask' et a une étiquette qui dit "Nouvelle tâche". Il y aura également un bouton qui, via l'événement @click, déclenchera la fonction 'add' que nous allons écrire dans un instant.

Après avoir enregistré les modifications de votre document, vous devriez obtenir quelque chose comme ceci lorsque vous actualisez votre page index.html dans votre navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/Sehm8NfdIO65eutcubldfukWd9A1kYIaAhob)

Ne vous inquiétez pas si la boîte de dialogue ne fonctionne pas encore — nous devons d'abord ajouter la fonctionnalité à l'intérieur de notre instance `Vue()`. Nous faisons cela en ajoutant ce qui suit à notre instance juste après `el: '#app'` mais séparé par une virgule :

```
el: '#app',data: {  addModal: false,  newTask: ''}
```

L'objet **data** est l'endroit où nous allons stocker l'état de notre application. Avec cette modification, notre boîte de dialogue devrait maintenant fonctionner. Enregistrez et actualisez la page.

![Image](https://cdn-media-1.freecodecamp.org/images/2fjdoJY-cmsKeXhu4y4-lEpYUzbocHiWwDYB)

Maintenant, chaque fois que vous cliquez pour ouvrir votre boîte de dialogue modale, l'état interne dans `data: {}` est défini sur `addModal: true`, ce qui affiche ensuite la modale. De même, chaque fois que vous écrivez un message dans la zone de texte de la boîte de dialogue, il sera enregistré dans `newTask` puisque le `<v-text-field></v-text-field>` est lié à celui-ci via v-model=.

Nous allons maintenant ajouter le code pour la fonction `add` qui enregistrera tout ce qui se trouve dans `newTask` dans notre liste de rappels à venir. Cette fonction doit être située à l'intérieur de l'objet **methods**, que nous allons ajouter après notre objet `data: {}` dans l'instance Vue.

La fonction ressemblera à ceci :

```
add() {  if (this.newTask !== '') {    this.tasks.unshift({text: this.newTask, completed: false})    this.addModal = false    this.newTask = ''  }}
```

Après avoir enfermé la fonction à l'intérieur de l'objet `method: {}` , le code devrait maintenant ressembler à ceci :

```
new Vue({  el: '#app',  data: {    addModal: false,    newTask: '',    },  methods: {    add() {      if (this.newTask !== '') {        this.tasks.unshift({text: this.newTask, completed: false})        this.addModal = false        this.newTask = ''      }    }  }});
```

Lorsque la fonction `add()` est déclenchée, elle ajoutera notre tâche de `newTask` à notre liste de tâches pas encore créée, sauf si elle est vide. Elle fermera ensuite la boîte de dialogue en définissant `this.addModal = false` et réinitialisera `newTask` à vide.

Créons notre liste de tâches afin de pouvoir commencer à entrer quelques rappels. À l'intérieur de l'objet `data`, placez ce code :

```
tasks: [   // Quelques données factices   {    text: 'Corvées',    completed: false   },   {    text: 'Plus de corvées',    completed: false   }]
```

Ce seront nos rappels factices. Comme vous pouvez le voir, nous avons une clé `completed` qui est définie sur `true` ou `false` afin que nous puissions différencier les tâches qui sont terminées de celles qui ne le sont pas. Cela signifie également que nous ne pouvons pas simplement afficher notre liste `tasks` telle quelle dans notre interface utilisateur, car nous afficherions alors les tâches terminées et non terminées ensemble.

La façon dont nous allons résoudre ce problème est avec les **propriétés calculées**. Elles fonctionnent en surveillant constamment les changements dans votre application et en retournant une valeur calculée basée sur ces changements.

Nous avons besoin de deux propriétés calculées : une pour la liste `todo` et une pour la liste `done` qui sépareront respectivement les tâches incomplètes et complétées. Nous ajoutons `computed: {}` après notre `methods: {}` et nous y plaçons les propriétés calculées `todo: function() {}` et `done: function() {}` . La fonction `todo` retournera `this.tasks.filter(function(task) {return !task.completed})` et la fonction `done` retournera l'inverse en supprimant le `!` (qui signifie "non") devant `task.completed`. Le code devrait ressembler à ceci :

```
computed: {  done: function() {   return this.tasks.filter(function(task) {return task.completed})  },  todo: function() {   return this.tasks.filter(function(task) {return !task.completed})  }}
```

Nous sommes maintenant prêts à rendre nos deux listes dans notre interface utilisateur. Cela va être un peu de balisage, mais ne vous inquiétez pas, nous allons le parcourir ensemble. Nous allons remplacer `<v-container>Hello world</v-container>` en le sélectionnant puis en collant ce qui suit à sa place :

```
<v-container grid-list-md>  <v-layout row wrap>    <v-flex xs12>      <v-list>        <v-subheader>Tâches à faire</v-subheader>        <v-list-tile v-for="task in todo">          <v-list-tile-action>            <v-btn icon ripple @click="complete(task)">              <v-icon v-if="task.completed">check_circle</v-icon>              <v-icon v-else>check_circle_outline</v-icon>            </v-btn>            </v-list-tile-action>          <v-list-tile-title>            {{task.text}}          </v-list-tile-title>          <v-list-tile-action>            <v-btn icon ripple @click="remove(task)">              <v-icon color="grey lighten-1">cancel</v-icon>            </v-btn>          </v-list-tile-action>        </v-list-tile>      </v-list>    </v-flex>              <v-flex xs12>      <v-list>        <v-subheader>Tâches complétées</v-subheader>        <v-list-tile v-for="task in done">          <v-list-tile-action>            <v-btn icon ripple @click="complete(task)">              <v-icon v-if="task.completed">check_circle</v-icon>              <v-icon v-else>check_circle_outline</v-icon>            </v-btn>            </v-list-tile-action>          <v-list-tile-title>            {{task.text}}          </v-list-tile-title>          <v-list-tile-action>            <v-btn icon ripple @click="remove(task)">              <v-icon color="grey lighten-1">cancel</v-icon>            </v-btn>          </v-list-tile-action>        </v-list-tile>      </v-list>    </v-flex>  </v-layout></v-container>
```

Pour commencer, nous ajoutons `grid-list-md` à notre conteneur. Ensuite, nous ajoutons `<v-layout row wrap></v-layout>` et `<v-flex xs12></v-flex>` et ajoutons nos deux balises `<v-list></v-list>` avec un `<v-subheader></v-subheader>` dans chacune. Cela crée notre mise en page de base sous forme de deux listes.

Ensuite, nous allons ajouter `<v-list-tile v-for="task in todo"></v-list-tile>` où l'instruction v-for= parcourt chaque tâche dans notre propriété calculée todo. Même chose pour la propriété done. Alors que nous parcourons chaque liste, nous allons rendre chaque élément de la liste. Chaque élément affichera le task.text et aura deux boutons : un pour déclencher la fonction complete() et un pour déclencher la fonction remove().

Continuons en écrivant ceux-ci à l'intérieur de notre objet `method`.

```
complete(task) {  task.completed ? task.completed = false : task.completed = true},remove(task) {  this.tasks = this.tasks.filter(function(x){return x !== task})},
```

Le corps de la fonction `complete` contient un opérateur ternaire qui basculera le bouton de complétion sur chaque rappel. Chaque fois que `task.completed` est défini sur `true` pour un rappel, toute l'interface utilisateur sera mise à jour et déplacera ce rappel vers la liste "Complétée".

Vous devriez maintenant avoir un vrai prototype fonctionnel de notre application de rappels !

### Réflexions finales

Dans cet article, je n'ai pas essayé de montrer comment construire spécifiquement une application de rappels inutile avec des fonctionnalités limitées (bien que ce soit exactement ce que j'ai fait). Plutôt, que vous pouvez utiliser ces outils que je vous ai présentés pour construire très rapidement une collection de maquettes et ensuite, avec une configuration minimale, créer un prototype réel et fonctionnel à partir de ces designs.

Avec cela en place, vous pouvez maintenant ajuster votre bibliothèque de composants, construire vos designs, puis les implémenter rapidement en code au fur et à mesure.

Vous pouvez trouver le fichier Sketch terminé et le code [ici](https://github.com/adamwattis/MaterialReminders). Je recommande également fortement de plonger plus profondément dans les outils dont j'ai parlé pour réaliser pleinement leur potentiel.

J'espère que vous avez apprécié cet article et que vous le trouverez utile. Commentez si vous avez des questions ou faites-moi savoir ce que vous en avez pensé.