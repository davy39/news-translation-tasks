---
title: Comment créer une entrée OTP dans Vue 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-24T15:00:18.000Z'
originalURL: https://freecodecamp.org/news/create-otp-input-vue-3
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/otp-article-header.jpg
tags:
- name: forms
  slug: forms
- name: vue
  slug: vue
seo_title: Comment créer une entrée OTP dans Vue 3
seo_desc: 'By Paul Akinyemi

  OTP inputs are one of the most fun components you can use in your app. They make
  the dry process of filling in yet another form a little more engaging.

  In this article, you’ll learn how to build an OTP input from scratch in Vue 3. By...'
---

Par Paul Akinyemi

Les entrées OTP sont l'un des composants les plus amusants que vous pouvez utiliser dans votre application. Elles rendent le processus aride de remplissage d'un autre formulaire un peu plus engageant.

Dans cet article, vous apprendrez à créer une entrée OTP à partir de zéro dans Vue 3. À la fin de ce tutoriel, vous aurez construit une entrée OTP qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/finished-otp-demo.gif)

Voici un aperçu des étapes que le tutoriel suivra :

* Installation du projet
* Construction des bases
* Ajout de fonctionnalités
* Finitions
* Conclusion

## Prérequis

Pour suivre facilement ce tutoriel, vous devez avoir les éléments suivants :

* Une compréhension de base de Vue 3 et de JavaScript vanilla
* Node.js 16+ installé sur votre machine
* Une connaissance de base de CSS

## Qu'est-ce qu'une entrée OTP ?

Au cas où vous ne seriez pas familier avec le terme, une entrée OTP est un composant de formulaire pour les chaînes de caractères. Chaque caractère de la chaîne est tapé dans une boîte séparée, et le composant bascule entre les boîtes à mesure que vous tapez (au lieu de devoir cliquer dans chaque boîte).

Elle est appelée entrée OTP car elles sont généralement utilisées pour permettre aux utilisateurs de taper un OTP (One Time Password) qu'ils ont reçu via un autre canal, généralement par e-mail ou SMS.

## Installation du projet

Ce projet n'utilisera aucune bibliothèque externe, donc toute l'installation dont vous avez besoin est de créer une application Vue avec [Vite](https://vitejs.dev/).

Créez le projet Vue en exécutant la commande suivante dans une fenêtre de terminal :

```sh
npm init vue@3

```

Si vous n'avez pas installé `create-vue` sur votre appareil, cette commande l'installera. Ensuite, elle vous présentera une série d'options. Les options vous permettent de spécifier le nom du projet et de sélectionner les modules complémentaires que vous souhaitez inclure.

Appellez le projet `otp-input` et ne sélectionnez aucun module complémentaire, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/otp-input-install.png)

Après avoir fait cela, exécutez :

```sh
cd otp-input
npm install
npm run dev

```

Après le démarrage du serveur de développement, vous devriez voir quelque chose comme ceci dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/otp-input-finish-setup.png)

Ouvrez l'URL que Vite vous donne dans votre navigateur, et passons aux choses amusantes.

## Comment construire les bases

Si vous ouvrez le dossier `otp-input` dans votre éditeur, il devrait avoir une structure de fichiers comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-121.png)

Vous allez ajuster cette configuration pour quelque chose de plus approprié. Commencez par ouvrir `src/App.vue` et remplacez son contenu par ceci :

```html
<template>
</template>

<script setup>

</script>

<style>

</style>

```

Ensuite, sélectionnez tous les fichiers à l'intérieur de `src/components` et supprimez-les, et créez un fichier à l'intérieur des composants appelé `OTP.vue`. Sur les appareils Linux/Mac, vous pouvez faire cela en exécutant la commande suivante dans une nouvelle fenêtre de terminal :

```sh
rm -rfv src/components
mkdir src/components
touch src/components/OTP.vue

```

Ensuite, supprimez le dossier `src/assets`, et retirez la ligne suivante de `src/main.js` :

```js
import './assets/main.css'

```

Ensuite, ouvrez `components/OTP.vue`, et placez le modèle de départ pour votre OTP à l'intérieur :

```html
<template>
  <div ref="otpCont">
    <input
      type="text"
      class="digit-box"
      v-for="(el, ind) in digits"
      :key="el+ind"
      v-model="digits[ind]"
      :autofocus="ind === 0"
      :placeholder="ind+1"
      maxlength="1"
    >
  </div>
</template>

```

Expliquons cela.

Le modèle commence par une div conteneur à laquelle vous avez attaché une référence appelée `otpCont`. À l'intérieur du conteneur, vous avez une entrée de texte avec un `v-for` dessus. Le `v-for` rendra une entrée pour chaque élément d'une collection que nous avons appelée `digits`, et attachera une liaison bidirectionnelle avec l'élément de `digits` qui partage son index.

La première entrée rendue aura l'attribut `autofocus`, le placeholder pour chaque entrée est son index plus un, et chaque entrée a une longueur maximale d'un caractère.

Ensuite, le script pour le composant. Placez le code suivant dans `OTP.vue` :

```html
<script setup>
  import { ref, reactive } from 'vue';

  const props = defineProps({
    default: String,

    digitCount: {
      type: Number,
      required: true
    }
  });

  const digits = reactive([])

  if (props.default && props.default.length === props.digitCount) {
    for (let i =0; i < props.digitCount; i++) {
      digits[i] = props.default.charAt(i)
    }
  } else {
    for (let i =0; i < props.digitCount; i++) {
      digits[i] = null;
    }
  }

  const otpCont = ref(null)

</script>

```

Après l'importation, ce code définit deux props : un nombre requis `digitCount` qui contrôle le nombre d'entrées, et une chaîne optionnelle `default`.

Ensuite, il crée le tableau réactif `digits` dont le modèle a besoin. Si la prop `default` a été fournie et que sa longueur correspond à la prop `digitCount`, `digits` est initialisé en utilisant les caractères dans `default`. Sinon, les éléments de `digits` sont remplis avec `null`.

Enfin, le code crée la référence `otpCont` à partir du modèle.

La dernière tâche pour cette section est de donner un peu de style aux entrées. Placez ce qui suit à la fin de `OTP.vue` :

```html
<style scoped>
.digit-box {
    height: 4rem;
    width: 2rem;
    border: 2px solid black;
    display: inline-block;
    border-radius: 5px;
    margin: 5px;
    padding: 15px;
    font-size: 3rem;
}

.digit-box:focus {
  outline: 3px solid black;
}

</style>

```

Et cela crée la forme de base de votre OTP.

Ensuite, vous allez modifier la page d'accueil de votre application pour rendre l'entrée. Remplacez le contenu de `src/App.vue` par ce qui suit :

```html
<template>
  <otp 
    :digit-count="4"
  ></otp>

</template>

<script setup>
import otp from "./components/OTP.vue";
</script>


```

Si vous ouvrez l'application dans le navigateur, vous devriez voir les entrées séparées rendues comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/otp-init-form.png)

## Comment ajouter des fonctionnalités

Pour l'instant, vous n'avez pas vraiment une entrée OTP. Vous devez manuellement basculer le focus entre les champs, et il n'y a pas de validation. Ensuite, vous allez écrire la logique pour corriger cela.

Ouvrez `components/OTP.vue`, et ajoutez un gestionnaire d'événements de pression de touche à la balise d'entrée :

```js
 @keydown="handleKeyDown($event, ind)"

```

Maintenant, créez la fonction `handleKeyDown` à la fin de la section `script setup` comme suit :

```js
const handleKeyDown = function (event, index) {
    if (event.key !== "Tab" && 
        event.key !== "ArrowRight" &&
        event.key !== "ArrowLeft"
    ) {
      event.preventDefault();
    }
    
    if (event.key === "Backspace") {
      digits[index] = null;
      
      if (index != 0) {
        (otpCont.value.children)[index-1].focus();
      } 

      return;
    }

    if ((new RegExp('^([0-9])$')).test(event.key)) {
      digits[index] = event.key;

      if (index != props.digitCount - 1) {
        (otpCont.value.children)[index+1].focus();
      }
    }
  }

```

Décomposons cette fonction. Le gestionnaire d'événements est appelé chaque fois qu'une touche est pressée alors qu'un des champs de saisie est en focus.

Si la touche pressée n'est pas tab ou l'une des touches fléchées horizontales, la fonction appellera `preventDefault()`, et passera au bloc if suivant.

Si la touche pressée était Backspace, la valeur du tableau `digit` à l'index de l'entrée cible sera définie sur null. Ensuite, si l'entrée cible n'était pas la première entrée, le code déplace le focus sur son frère précédent.

Le dernier bloc if utilise une expression régulière pour tester si la touche pressée était l'un des chiffres de 0 à 9. Si c'était le cas, `digits` est mis à jour de manière appropriée, et le focus est déplacé vers l'entrée suivante.

Si vous ouvrez l'application dans votre navigateur maintenant, vous devriez voir que l'entrée OTP déplace automatiquement le focus entre les boîtes. De plus, elle n'accepte que les nombres comme entrée, et vous pouvez utiliser la touche tab pour naviguer entre les boîtes :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/midway-otp-demo.gif)

## Ajoutez les finitions

L'entrée OTP est maintenant presque complète, mais elle semble un peu simple. Ajoutons un dernier ensemble de fonctionnalités :

* L'entrée doit émettre la valeur OTP une fois que tous les champs sont remplis.
* Une petite animation de rebond doit se déclencher lorsque l'utilisateur entre une valeur.

Nous commencerons par la logique pour émettre la valeur OTP. Tout d'abord, vous allez modifier `App.vue` pour qu'il puisse afficher la valeur émise. Remplacez le contenu de `App.vue` par ce qui suit :

```html
<template>
  <otp 
    :digit-count="4"
    @update:otp="otpValue = $event"
  ></otp>

  <p>La valeur OTP actuelle est : {{ otpValue }} </p>
</template>

<script setup>
import otp from "./components/OTP.vue";
import { ref } from "vue";

otpValue = ref('')
</script>

```

Pas grand-chose n'a changé : vous avez simplement créé une variable réactive appelée `otpValue`, dit au modèle de la rendre, et ajouté un écouteur d'événements au composant OTP pour mettre à jour `otpValue`.

Ensuite, ouvrez `components/OTP.vue` et ajoutez le code suivant juste avant la fonction `handleKeyDown` :

```js
const emit = defineEmits(['update:otp']);

const isDigitsFull = function () {
  for (const elem of digits) {
    if (elem == null || elem == undefined) {
      return false;
    }
  }

  return true;
}

```

Ce code définit l'événement personnalisé `update:otp`, ainsi qu'une fonction `isDigitsFull`. `isDigitsFull` retourne `false` s'il y a une valeur `null` à l'intérieur de `digits` et `true` sinon.

Ajoutez ce qui suit à `handleKeyDown` à la fin du dernier bloc if :

```js
if (isDigitsFull()) {
  emit('update:otp', digits.join(''))
}

```

Chaque fois qu'un chiffre est pressé dans une boîte de saisie, ce code appelle la fonction d'aide `isDigitsFull` pour déterminer si toutes les boîtes de saisie sont remplies.

Si c'est le cas, il émet l'événement `update:otp`, combine la valeur de toutes les boîtes de saisie en une seule chaîne, et l'envoie comme valeur de l'événement.

Votre page rendue dans le navigateur devrait maintenant afficher la valeur OTP (complète) la plus récente :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/otp-semifinished-demo.gif)

Enfin, vous allez ajouter une animation à votre entrée OTP. Collez le CSS suivant à la fin de la balise style dans `components/OTP.vue` :

```css
.bounce {
  animation: pulse .3s ease-in-out alternate;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }

  100% {
    transform: scale(1.1);
  }
}

```

Et ajoutez ensuite la liaison de classe suivante à l'entrée dans le modèle :

```js
:class="{bounce: digits[ind] !== null}"

```

Et voici le code pour l'animation ! Voici comment cela fonctionne :

* La classe bounce pour chaque entrée est liée à `digits[index]`
* Si la valeur de `digits[index]` change, l'expression est réévaluée
* Si la nouvelle valeur n'est pas null, la classe bounce est appliquée
* Si elle est null, la classe bounce est supprimée
* Si la valeur ne change pas, l'expression n'est pas réévaluée, donc l'animation ne se déclenche pas.

Voici l'apparence finale de votre OTP :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/finished-otp-demo-1.gif)

Et vous avez terminé !

## Conclusion

Dans ce tutoriel, vous avez appris à créer une entrée OTP à partir de zéro dans Vue 3. Vous pouvez trouver le code source de ce composant [ici](https://github.com/Morgenstern2573/otp-input). J'espère que vous avez apprécié la lecture !

Si vous souhaitez voir plus de mes écrits, vous pouvez me suivre sur [Twitter](https://twitter.com/apexPaul09).