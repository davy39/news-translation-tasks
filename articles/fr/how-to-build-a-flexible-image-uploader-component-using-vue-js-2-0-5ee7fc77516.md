---
title: Comment créer un composant de téléchargement d'images flexible en utilisant
  Vue.js 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T23:22:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-flexible-image-uploader-component-using-vue-js-2-0-5ee7fc77516
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OxNFaMGEzAXIHkmZACzVhQ.jpeg
tags:
- name: coding
  slug: coding
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment créer un composant de téléchargement d'images flexible en utilisant
  Vue.js 2.0
seo_desc: 'By Cathy Ha

  I’ve been coding with [Vue.js 2.0](http://Vue.js 2.0) for about half a year now,
  and it’s pretty awesome. It’s incredibly intuitive and simple. The partitioning
  between HTML/CSS/Javascript makes both learning and coding a breeze.

  But the ...'
---

Par Cathy Ha

Je code avec [Vue.js 2.0](http://Vue.js 2.0) depuis environ six mois maintenant, et c'est plutôt génial. C'est incroyablement intuitif et simple. La partition entre HTML/CSS/JavaScript rend l'apprentissage et le codage très faciles.

Mais le problème (et le plaisir) de coder avec un framework relativement nouveau est le manque de tutoriels pour ce que vous voulez construire. Surtout lorsque vous avez une idée spécifique en tête.

J'ai rencontré ce problème lorsque j'ai essayé de construire un téléchargeur de photos de profil pour [Torneo](http://www.torneo.ca). Bien sûr, j'aurais pu utiliser un package sophistiqué, mais où est le plaisir dans cela ?

Ainsi, en modifiant et en combinant [deux](https://alligator.io/vuejs/file-select-component/) [excellents](https://scotch.io/tutorials/how-to-handle-file-uploads-in-vue-2) tutoriels, j'ai créé mon propre **composant de téléchargement d'images réutilisable**.

_Consultez le [dépôt git](https://github.com/cathyhax/image-uploader/tree/master) pour tout le code._

### Comportement souhaité

J'ai créé le composant avec les objectifs suivants en tête :

* Le composant doit être capable d'être activé par n'importe quel élément de son composant parent pour télécharger des images
* Nous devons pouvoir voir un aperçu de l'image dans le composant parent
* L'image téléchargée doit être enregistrée au format FormData pour être envoyée au back-end
* Le composant doit vérifier une limite de taille dans l'image téléchargée (cela peut également être fait dans le back-end, mais c'est un peu plus rapide dans le front-end)
* Un fichier à la fois (notez que [ce tutoriel](https://scotch.io/tutorials/how-to-handle-file-uploads-in-vue-2) explique comment gérer plusieurs fichiers — il vous suffit de quelques boucles)

### Étape 1 : Installation

Nous allons commencer par installer le modèle webpack-simple. Nous allons également installer [Vuetify](https://vuetifyjs.com/en/) pour gagner du temps sur le style. Notez que tout ce qui est enveloppé dans <v-> provient de Vuetify. Comme leurs balises sont assez explicites, je ne vais pas trop m'attarder dessus. Je vous laisse [lire leur documentation](https://vuetifyjs.com/en/getting-started/quick-start).

```
# installer le vue-clinpm install vue-cli -g# initier le webpack-simple, et suivre les instructionsvue init webpack-simple image-upload
```

```
# installer les dépendancesnpm install
```

```
# installer Vuetifynpm install vuetify --save
```

![Image](https://cdn-media-1.freecodecamp.org/images/6rqRIITH5v4r7neZhfMbAMJmpTiNTxZY6WZb)
_Une légère célébration_

### **Étape 2 : Créer le modèle de téléchargement d'image**

Super ! Maintenant que nous avons les modèles configurés et installés, nous pouvons supprimer tout contenu de remplissage. Ensuite, nous pouvons créer un nouveau fichier de composant pour le téléchargeur d'images.

```
<template>  <div>
```

```
    <!-- emplacement pour que le composant parent active le sélecteur de fichiers -->    <div @click="launchFilePicker()">      <slot name="activator"></slot>    </div>
```

```
    <!-- entrée d'image : le style est défini sur caché et une référence est assignée pour qu'il puisse être déclenché -->    <input type="file"       ref="file"       :name="uploadFieldName"       @change="onFileChange(          $event.target.name, $event.target.files)"       style="display:none">
```

```
    <!-- boîte de dialogue d'erreur affiche toute erreur potentielle -->    <v-dialog v-model="errorDialog" max-width="300">      <v-card>        <v-card-text class="subheading">{{errorText}}</v-card-text>        <v-card-actions>          <v-spacer></v-spacer>          <v-btn @click="errorDialog = false" flat>Compris !</v-btn>        </v-card-actions>      </v-card>    </v-dialog>
```

```
  </div></template>
```

1. Pour rendre le composant de téléchargement d'images capable d'être activé par n'importe quel élément du composant parent, nous pouvons tirer parti de la fonctionnalité de ["slot"](https://vuejs.org/v2/guide/components-slots.html) de Vue.
2. Puisque nous voulons que le "déclencheur" pour l'entrée soit dans le composant parent, nous voulons la fonctionnalité de l'entrée de fichier dans le composant enfant, sans pouvoir le voir. Nous pouvons changer le style de l'entrée en "display:none" pour le cacher.
3. L'entrée d'image est assignée à une "réf" afin que lorsque le slot est cliqué, nous puissions activer l'entrée d'image par sa référence.
4. Pour rendre le téléchargeur d'images plus convivial, nous pouvons utiliser une boîte de dialogue pour afficher toute erreur potentielle.

![Image](https://cdn-media-1.freecodecamp.org/images/rt-C1o7SHEIhEa4qZCHHLWutfGltKOLeQu0w)

Ensuite, nous pouvons utiliser un peu de magie Vue.js dans la partie JavaScript pour donner vie à notre composant :

```
<script>
```

```
  export default {
```

```
    name: 'image-input',
```

```
    data: ()=> ({      errorDialog: null,      errorText: '',      uploadFieldName: 'file',      maxSize: 1024    }),
```

```
    props: {          // Utilisez "value" ici pour activer la compatibilité avec v-model      value: Object,    },
```

```
    methods: {      launchFilePicker(){        this.$refs.file.click();      },
```

```
      onFileChange(fieldName, file) {        const { maxSize } = this        let imageFile = file[0]          //vérifier si l'utilisateur a réellement sélectionné un fichier        if (file.length>0) {          let size = imageFile.size / maxSize / maxSize          if (!imageFile.type.match('image.*')) {            // vérifier si le téléchargement est une image            this.errorDialog = true            this.errorText = 'Veuillez choisir un fichier image'          } else if (size>1) {            // vérifier si la taille est supérieure à la limite de taille            this.errorDialog = true            this.errorText = 'Votre fichier est trop volumineux ! Veuillez sélectionner une image de moins de 1 Mo'          } else {            // Ajouter le fichier dans FormData et transformer le fichier en URL d'image            let formData = new FormData()            let imageURL = URL.createObjectURL(imageFile)            formData.append(fieldName, imageFile)
```

```
            // Émettre FormData et l'URL de l'image au composant parent            this.$emit('input', { formData, imageURL })          }        }      }    }  }</script>
```

5. Pour rendre le composant de téléchargement d'images compatible avec v-model, utilisez "value" dans les props. Toutes les données émises par le composant seront capturées dans la prop "value".

6. Lorsque l'activateur d'entrée de fichier dans le composant parent est cliqué, "this.$refs.file.click()" est utilisé pour activer le sélecteur de fichiers.

7. Une fois que l'utilisateur a choisi quelque chose dans le sélecteur de fichiers / fermé le sélecteur de fichiers, nous devons vérifier :

* Si l'utilisateur a réellement sélectionné un fichier
* Si le fichier est une image
* Si le fichier est supérieur à la limite de taille (souvent une bonne idée lorsqu'il s'agit de téléchargements utilisateur)

8. Si le fichier que l'utilisateur a sélectionné est correct, créez un élément FormData et ajoutez le fichier dans l'élément en utilisant un nom que votre serveur accepterait. De plus, convertissez le fichier image en une [URL d'objet](https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL) afin que le composant parent puisse le lire pour un aperçu.

9. Émettez les données (FormData pour le téléchargement vers le serveur, et imageURL pour l'aperçu) au composant parent.

### Étape 3 : Créer le composant parent

![Image](https://cdn-media-1.freecodecamp.org/images/62ZYpFxJIzdgxHdotiXCuCAfmUAJpI4nl7C6)
_Un aperçu du produit final, pour vous encourager à continuer la lecture_

Dans le composant parent, nous pouvons visualiser la fonctionnalité du composant enfant.

```
<template>  <v-app id="app" class="mt-0">    <v-container grid-list-xl>      <image-input v-model="avatar">        <div slot="activator">          <v-avatar size="150px" v-ripple v-if="!avatar" class="grey lighten-3 mb-3">            <span>Cliquez pour ajouter un avatar</span>          </v-avatar>          <v-avatar size="150px" v-ripple v-else class="mb-3">            <img :src="avatar.imageURL" alt="avatar">          </v-avatar>        </div>      </image-input>      <v-slide-x-transition>        <div v-if="avatar && saved == false">          <v-btn class="primary" @click="uploadImage" :loading="saving">Enregistrer l'avatar</v-btn>        </div>      </v-slide-x-transition>    </v-container>  </v-app></template>
```

1. Enveloppez l'élément activateur dans un <div/> et laissez le composant enfant savoir qu'il appartient à l'emplacement que nous avons nommé "activator".
2. Utilisez [v-if et v-else](https://vuejs.org/v2/guide/conditional.html) de Vue pour afficher une invite de téléchargement ou l'aperçu de l'avatar selon que l'utilisateur a sélectionné un fichier ou non.
3. Affichez conditionnellement un bouton pour enregistrer les modifications de l'utilisateur.

_Presque terminé !_ Ensuite, il est temps d'ajouter un peu de JavaScript au composant parent :

```
<script>import ImageInput from './components/ImageInput.vue'
```

```
export default {  name: 'app',  data () {    return {      avatar: null,      saving: false,      saved: false    }  },  components: {    ImageInput: ImageInput  },  watch:{    avatar: {      handler: function() {        this.saved = false      },      deep: true    }  },  methods: {    uploadImage() {      this.saving = true      setTimeout(() => this.savedAvatar(), 1000)    },    savedAvatar() {      this.saving = false      this.saved = true    }  }}</script>
```

4. Dans la partie script, importez le composant enfant.

5. Lorsque l'utilisateur clique sur "enregistrer", téléchargez l'avatar sur le serveur (notez que je simule un téléchargement dans le code ci-dessus. En réalité, nous utilisons [axios](https://github.com/axios) pour télécharger le fichier sur le serveur. Le back-end enregistre ensuite le fichier dans un système de fichiers et transmet le chemin du fichier dans les données).

![Image](https://cdn-media-1.freecodecamp.org/images/XfCSI5PrA9VekPsJGcMK5lcd9z7nkG4BPXZD)
_Vous êtes plutôt génial pour être arrivé aussi loin _

C'est tout ! Il y a beaucoup de place pour améliorer ce composant — comme passer des props pour redimensionner l'image téléchargée, gérer plusieurs fichiers, etc. Si vous voyez des points potentiels d'amélioration ou repérez une erreur dans mon code, s'il vous plaît laissez un commentaire !

_Encore une fois, n'hésitez pas à consulter le [dépôt git](https://github.com/cathyhax/image-uploader/tree/master) pour tout le code._

Enfin, un plug éhonté ici : si vous êtes intéressé par le sport, consultez [Torneo](https://www.torneo.ca) — une startup liée au sport que j'ai aidé à développer.