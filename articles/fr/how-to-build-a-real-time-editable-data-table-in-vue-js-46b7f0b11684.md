---
title: Comment créer un tableau de données éditable en temps réel dans Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-22T19:56:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-editable-data-table-in-vue-js-46b7f0b11684
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1LI9TzwDU1l6IyJFBRcULw.jpeg
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment créer un tableau de données éditable en temps réel dans Vue.js
seo_desc: 'By Peter Mbanugo

  In data-driven applications, a data table is used to display data in a tabular format
  with the ability to edit and delete records in place. When you’re working with Vue,
  there are different open-sourced components that can be used to...'
---

Par Peter Mbanugo

Dans les applications basées sur les données, un tableau de données est utilisé pour afficher les données dans un format tabulaire avec la possibilité de modifier et de supprimer des enregistrements en place. Lorsque vous travaillez avec [Vue](https://vuejs.org/), il existe [différents composants open-source](https://github.com/vuejs/awesome-vue#table) qui peuvent être utilisés pour ajouter facilement un tableau de données à votre application.

De nombreuses applications aujourd'hui ont des fonctionnalités en temps réel, et vous pouvez vous demander comment vous pouvez synchroniser l'édition et la suppression de données en temps réel. Il existe trois options pour cela :

1. Utiliser [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Ce n'est pas une bonne option si certains de vos utilisateurs utilisent des navigateurs qui ne supportent pas encore WebSocket.
2. Utiliser une bibliothèque qui abstrait ces différences entre navigateurs avec un mécanisme de repli, comme [Socket.IO](https://socket.io/), [SignalR](http://www.asp.net/signalr), et [SockJS](https://github.com/sockjs/sockjs-client). Avec cette option, vous devrez gérer le serveur qui gère un grand nombre de connexions ouvertes et traiter la mise à l'échelle.
3. Utiliser un service qui fournit une bibliothèque qui fait la même chose que l'option précédente, mais gère le serveur et met à l'échelle de manière appropriée. C'est une option préférable pour les entreprises et les équipes qui adoptent (ou ont adopté) l'approche serverless.

Je vais vous montrer comment créer un tableau de données éditable en temps réel dans Vue.js en utilisant [Hamoni Sync](https://www.hamoni.tech/) comme service de synchronisation d'état en temps réel. L'image ci-dessous montre ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/JKuAr28AYFl1z-bZJR2jNTO3l8e1glrYOqc0)

Pour suivre ce tutoriel, vous aurez besoin d'avoir quelques connaissances de base de Vue. Si vous n'avez aucune connaissance de Vue, vous pouvez lire mon [précédent article](https://dev.to/pmbanugo/from-vanillajs-to-vuejs-a-guide-to-vue-essentials-5gii) pour vous mettre à niveau avec Vue.js. Vous aurez également besoin des outils suivants :

1. [Node.js & npm](https://nodejs.org/en/download/) (suivez le lien pour télécharger un installeur pour votre OS)
2. [Vue CLI](https://www.npmjs.com/package/vue-cli) pour échafauder un nouveau projet Vue. Si vous ne l'avez pas, exécutez `npm install -g vue-cli@2.9.6` depuis la ligne de commande pour l'installer.

### Installation du projet

Nous allons installer le projet en utilisant Vue CLI et un [modèle](https://github.com/vuetifyjs/simple) de [Vuetify](https://vuetifyjs.com/en/). Ouvrez la ligne de commande et exécutez la commande `vue init vuetifyjs/simple realtime-datatable-vue`. Vous serez invité à entrer un nom et un auteur, alors acceptez la valeur par défaut en appuyant sur Entrée pour chaque invite. Cela va échafauder un nouveau projet Vue avec un seul fichier `index.html`.

Ce fichier contient des références de script à Vue et Vuetify. Vuetify est un [Material Design](https://material.io/) Component pour Vue.js. Il dispose d'un composant `v-data-table` avec des fonctionnalités pour le tri, la recherche, la pagination, l'édition en ligne, les infobulles d'en-tête et la sélection de lignes.

### Ajouter le composant de tableau de données

Ouvrez le fichier `index.html` avec votre éditeur de texte (ou IDE). Remplacez le contenu de la ligne **50** par ce qui suit :

```
<div>    <v-dialog v-model="dialog" max-width="500px">    <v-btn slot="activator" color="primary" dark class="mb-2">Nouvel élément</v-btn>    <v-card>        <v-card-title>        <span class="headline">{{ formTitle }}</span>        </v-card-title>        <v-card-text>        <v-container grid-list-md>            <v-layout wrap>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.name" label="Nom du dessert"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.calories" label="Calories"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.fat" label="Gras (g)"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.carbs" label="Glucides (g)"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.protein" label="Protéines (g)"></v-text-field>            </v-flex>            </v-layout>        </v-container>        </v-card-text>        <v-card-actions>        <v-spacer></v-spacer>        <v-btn color="blue darken-1" flat @click.native="close">Annuler</v-btn>        <v-btn color="blue darken-1" flat @click.native="save">Enregistrer</v-btn>        </v-card-actions>    </v-card>    </v-dialog>    <v-data-table :headers="headers" :items="desserts" hide-actions class="elevation-1">    <template slot="items" slot-scope="props">        <td>{{ props.item.name }}</td>        <td class="text-xs-right">{{ props.item.calories }}</td>        <td class="text-xs-right">{{ props.item.fat }}</td>        <td class="text-xs-right">{{ props.item.carbs }}</td>        <td class="text-xs-right">{{ props.item.protein }}</td>        <td class="justify-center layout px-0">        <v-btn icon class="mx-0" @click="editItem(props.item)">            <v-icon color="teal">edit</v-icon>        </v-btn>        <v-btn icon class="mx-0" @click="deleteItem(props.item)">            <v-icon color="pink">delete</v-icon>        </v-btn>        </td>    </template>    </v-data-table></div>
```

Le code ci-dessus ajoute un composant `v-dialog` pour afficher une boîte de dialogue afin de collecter des données pour de nouveaux enregistrements ou de modifier un enregistrement existant. Il ajoute également le `v-data-table` qui rend le tableau. Nous devons définir les données et les méthodes utilisées par ces composants. Après la ligne **126**, ajoutez le code suivant aux propriétés de données :

```
dialog: false,headers: [    {        text: 'Dessert (portion de 100g)',        align: 'left',        sortable: false,        value: 'name'    },    { text: 'Calories', value: 'calories' },    { text: 'Gras (g)', value: 'fat' },    { text: 'Glucides (g)', value: 'carbs' },    { text: 'Protéines (g)', value: 'protein' },    { text: 'Actions', value: 'name', sortable: false }],desserts: [],editedIndex: -1,editedItem: {    name: '',    calories: 0,    fat: 0,    carbs: 0,    protein: 0},defaultItem: {    name: '',    calories: 0,    fat: 0,    carbs: 0,    protein: 0},listPrimitive: null
```

La propriété de données `desserts` contiendra les données à afficher dans le tableau. La propriété `editedItem` contiendra les valeurs pour l'enregistrement en cours de modification, et `editedIndex` contiendra l'index de l'enregistrement en cours de modification.

Ajoutez les propriétés suivantes après la définition de la propriété `data`, après la ligne **189** :

```
computed: {    formTitle() {        return this.editedIndex === -1 ? 'Nouvel élément' : 'Modifier l\'élément'    }},
```

```
watch: {    dialog(val) {        val || this.close()    }},
```

Nous avons ajouté une propriété `computed` et `watch`. La propriété `computed` définit `formTitle` qui donne un titre au composant de dialogue en fonction de la valeur de `editedIndex`. La propriété `watch` surveille `dialog` pour savoir quand sa valeur change. Si la valeur change pour false, elle appelle la fonction `close()` qui sera définie plus tard.

### Ajouter Hamoni Sync

À ce stade, nous devons ajouter Hamoni Sync. Il est utilisé pour synchroniser l'état de l'application et gère la résolution des conflits pour éviter qu'un utilisateur ne remplace les données d'un autre utilisateur. Pour utiliser Hamoni Sync, vous devrez vous inscrire pour obtenir un compte et un identifiant d'application. Suivez ces étapes pour créer une application dans Hamoni.

1. Inscrivez-vous et connectez-vous au tableau de bord Hamoni [dashboard](https://dashboard.hamoni.tech/).
2. Entrez le nom de votre application préféré dans le champ de texte et cliquez sur le bouton créer. Cela devrait créer l'application et l'afficher dans la section de la liste des applications.
3. Cliquez sur le bouton « Show Account ID » pour voir votre identifiant de compte.

![Image](https://cdn-media-1.freecodecamp.org/images/xuqPh053ZqsE3kInM55NSiY41ZG05f7VWED4)

En dessous de la référence de script à Vuetify à la ligne **139**, ajoutez une référence à Hamoni Sync :

```
<script src="https://unpkg.com/hamoni-sync@0.4.0/hamoni.dev.js"><;/script>
```

Ensuite, nous devons initialiser Hamoni Sync une fois que le composant Vue est monté. Ajoutez une propriété `mounted` en dessous de la propriété `watch` :

```
mounted: function () {    let hamoni = new Hamoni("ACCOUNT_ID", "APP_ID");
```

```
    hamoni.connect().then(() => {        hamoni          .get("vue-table")          .then(primitive => {            this.listPrimitive = primitive            this.desserts = [...primitive.getAll()]            this.subscribeToUpdate()          }).catch(error => {              if (error === "Error getting state from server") {                this.initialise(hamoni);              }              else {                 alert(error);              }          })    }).catch(alert)},
```

Dans le code ci-dessus, nous initialisons Hamoni Sync avec un compte et un identifiant d'application. Remplacez les espaces réservés de chaîne par le compte et l'identifiant d'application du tableau de bord. Ensuite, il est connecté au serveur Hamoni en appelant `hamoni.connect()` qui retourne une promesse.

Une fois connecté, nous appelons `hamoni.get()` avec le nom de l'état stocké dans Hamoni. Afin de récupérer un état de Hamoni, il doit avoir été créé, sinon il retournera une erreur. Ce que j'ai fait ici, c'est gérer cette erreur dans le bloc catch, de sorte qu'il appelle une autre fonction pour initialiser l'état dans Hamoni Sync.

Si l'appel pour obtenir un état d'application réussit, il retourne un objet qui sera utilisé pour modifier les données contenues dans cet état. Cet objet est appelé une primitive Sync. Il existe trois types de primitives Sync :

1. [Value Primitive](https://docs.hamoni.tech/value-primitive.html) : Ce type d'état contient des informations simples représentées avec des types de données comme les chaînes, les booléens ou les nombres. Il est mieux adapté pour des cas tels que le compte de messages non lus, les bascules, etc.
2. [Object Primitive](https://docs.hamoni.tech/object-primitive.html) : L'état d'objet représente des états qui peuvent être modélisés comme un objet JavaScript. Un exemple d'utilisation pourrait être le stockage du score d'un jeu.
3. [List Primitive](https://docs.hamoni.tech/list-primitive.html) : Cela contient une liste d'objets d'état. Un objet d'état est un objet JavaScript. Vous pouvez mettre à jour un élément en fonction de son index dans la liste.

Nous avons utilisé une primitive de liste pour cet exemple. Nous appelons `primitive.getAll()` pour obtenir l'état et le passer à `desserts`. Après cela, il appelle la fonction `subscribeToUpdate()`. Cette fonction sera utilisée pour s'abonner aux événements de changement d'état de Hamoni Sync.

Ajoutez le code suivant après la propriété `mounted` à la ligne **215** :

```
methods: {  initialise(hamoni) {    hamoni.createList("vue-table", [      {        name: 'Yaourt glacé',        calories: 159,        fat: 6.0,        carbs: 24,        protein: 4.0      },      {        name: 'Sandwich à la crème glacée',        calories: 237,        fat: 9.0,        carbs: 37,        protein: 4.3      },      {        name: 'Éclair',        calories: 262,        fat: 16.0,        carbs: 23,        protein: 6.0      }    ]).then(primitive => {      this.listPrimitive = primitive      this.desserts = this.listPrimitive.getAll()      this.subscribeToUpdate();    }).catch(alert)  },
```

```
  subscribeToUpdate() {    this.listPrimitive.onItemAdded(item => {      this.desserts.push(item.value)    })
```

```
    this.listPrimitive.onItemUpdated(item => {      // mettre à jour l'élément à item.index      this.desserts.splice(item.index, 1, item.value);    })
```

```
    this.listPrimitive.onItemDeleted(item => {      // supprimer l'élément à item.index      this.desserts.splice(item.index, 1);    })  },
```

```
  editItem(item) {    this.editedIndex = this.desserts.indexOf(item)    this.editedItem = Object.assign({}, item)    this.dialog = true  },
```

```
  deleteItem(item) {    const index = this.desserts.indexOf(item)    confirm('Êtes-vous sûr de vouloir supprimer cet élément ?') && this.listPrimitive.delete(index)  },
```

```
  close() {    this.dialog = false    setTimeout(() => {      this.editedItem = Object.assign({}, this.defaultItem)      this.editedIndex = -1    }, 300)  },
```

```
  save() {    if (this.editedIndex > -1) {      this.listPrimitive.update(this.editedIndex, this.editedItem)    } else {      this.listPrimitive.push(this.editedItem)    }
```

```
    this.close()  }}
```

Le code ci-dessus définit les fonctions que nous avons référencées jusqu'à présent.

La fonction `initialise()` crée la primitive de liste avec le nom `vue-table`.

Les fonctions `subscribeToUpdate()` contiennent du code pour gérer lorsqu'un élément est ajouté, mis à jour ou supprimé de la primitive de liste.

La fonction `deleteItem()` supprime un élément de la primitive de liste en appelant `listPrimitive.delete(index)` avec l'index de l'élément à supprimer.

La fonction `save()` appelle `listPrimitive.push(editedItem)` pour ajouter un nouvel élément à la primitive de liste, et appelle `listPrimitive.update(editedIndex, editedItem)` pour mettre à jour l'enregistrement à un certain index.

C'est tout le code nécessaire pour atteindre notre objectif d'un tableau de données éditable en temps réel. Ouvrez le fichier `index.html` dans votre navigateur et l'application est prête à être utilisée !

![Image](https://cdn-media-1.freecodecamp.org/images/FObytUBfPksl2aGCLfy0dQSUOv10LjBJ68ok)

### C'est tout !

Nous avons créé un tableau de données éditable en temps réel dans Vue.js. [Hamoni Sync](https://dev.to/pmbanugo/hamoni.tech) facilite l'ajout de fonctionnalités en temps réel. [Vuetify](https://vuetifyjs.com/en/) et [Hamoni Sync](https://www.npmjs.com/package/hamoni-sync) ont tous deux des packages npm si vous travaillez avec un système de build et utilisez des composants de fichier unique. Vous pouvez trouver le code source sur [GitHub](https://github.com/pmbanugo/realtime-datatable-vue).

### Ressources

* [Hamoni Sync](https://www.hamoni.tech/) ([docs](https://dev.to/pmbanugo/docs.hamoni.tech))
* [Vuetify](https://vuetifyjs.com/en/)
* [Vue CLI](https://www.npmjs.com/package/vue-cli)
* [Introduction aux essentiels de Vue.js](https://dev.to/pmbanugo/from-vanillajs-to-vuejs-a-guide-to-vue-essentials-5gii)