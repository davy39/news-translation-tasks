---
title: Comment utiliser les props dans Vue.js
date: '2021-08-11T19:51:52.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/how-to-use-props-in-vuejs
posteditor: ''
proofreader: ''
author: Joel Olawanle
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Yellow-and-Purple-Geometric-Covid-19-General-Facts-Twitter-Post.png
tags:
- name: Vue.js
  slug: vuejs
seo_desc: 'We use props to pass information/data from a parent component to child
  components. In this article, I will explain everything you need to know about props
  and why you should use props in Vue.js.

  Here''s a brief outline of what we''ll cover in this guid...'
---


Par Joel Olawanle

<!-- more -->

Nous utilisons les props pour transmettre des informations ou des données d'un composant parent à des composants enfants. Dans cet article, j'expliquerai tout ce que vous devez savoir sur les props et pourquoi vous devriez les utiliser dans Vue.js.

Voici un bref aperçu de ce que nous allons aborder dans ce guide :

-   [Que sont les props dans Vue.js ?](#heading-que-sont-les-props-dans-vue-js)
-   [Comment déclarer des props dans un composant](#heading-comment-declarer-des-props-dans-un-composant)
-   [Comment travailler avec plusieurs props](#heading-comment-travailler-avec-plusieurs-props)
-   [Les types de props dans Vue.js](#heading-les-types-de-props-dans-vue-js)
-   [Comment passer des données aux props](#heading-comment-passer-des-donnees-aux-props)
-   [Comment passer des fonctions aux props](#heading-comment-passer-des-fonctions-aux-props)
-   [Comment valider les props](#heading-comment-valider-les-props)
-   [Comment définir des valeurs par défaut pour les props](#heading-comment-definir-des-valeurs-par-defaut-pour-les-props)

## Que sont les props dans Vue.js ?

"Props" est un mot-clé spécial qui signifie propriétés. Elles peuvent être déclarées sur un composant pour passer des données d'un composant parent vers l'un de ses composants enfants.

C'est beaucoup plus simple que d'utiliser des bibliothèques de gestion d'état comme Vuex pour les applications Vue.js.

Les données dans les props ne circulent que dans un seul sens : du haut (le composant parent) vers le bas (les composants enfants). Cela signifie simplement que vous ne pouvez pas passer de données d'un enfant à un parent.

Une autre chose à garder à l'esprit est que les props sont en lecture seule et ne peuvent pas être modifiées par le composant enfant car le composant parent "possède" cette valeur.

Pour équilibrer les choses : les composants parents passent des props aux composants enfants, tandis que les composants enfants émettent des événements vers les composants parents.

## Comment déclarer des props dans un composant

Voyons maintenant comment nous pouvons déclarer des props à l'intérieur d'un composant.

```
Vue.component('user-detail', {
  props: ['name'],
  template: '<p>Hi {{ name }}</p>'
})
.js
```

ou, dans un composant monofichier (SFC) Vue :

```
<template>
  <p>{{ name }}</p>
</template>

<script>
export default {
  props: ['name']
}
</script>
```

Dans le code ci-dessus, nous avons déclaré une prop appelée `name` que nous pouvons appeler dans la section template de notre application.

Note : Il s'agit du composant enfant et cette prop va recevoir des données du composant parent. J'expliquerai cela plus en détail plus tard.

## Comment travailler avec plusieurs props

Vous pouvez avoir plus d'une prop en les ajoutant au tableau des props, comme ceci :

```
Vue.component('user-detail', {
  props: ['firstName', 'lastName'],
  template: '<p>Hi {{ firstName }} {{ lastName }}</p>'
})
```

ou, dans un composant monofichier Vue :

```
<template>
  <p>Hi {{ firstName }} {{ lastName }}</p>
</template>

<script>
export default {
  props: [
    'firstName', 
    'lastName'
  ],
}
</script>
```

## Les types de props dans Vue.js

Pour spécifier le type de prop que vous souhaitez utiliser dans Vue, vous utiliserez un objet au lieu d'un tableau. Vous utiliserez le nom de la propriété comme clé de chaque propriété, et le type comme valeur.

Si le type de données passées ne correspond pas au type de la prop, Vue envoie une alerte (en mode développement) dans la console avec un avertissement. Les types valides que vous pouvez utiliser sont :

-   String
-   Number
-   Boolean
-   Array
-   Object
-   Date
-   Function
-   Symbol

```
Vue.component('user-detail', {
  props: {
    firstName: String,
    lastName: String
  },
  template: '<p>Hi {{ firstName }} {{ lastName }}</p>'
})
```

ou, dans un composant monofichier Vue :

```
<template>
  <p>Hi {{ firstName }} {{ lastName }}</p>
</template>

<script>
export default {
  props: {
    firstName: String,
    lastName: String
  },
}
</script>
```

## Comment passer des données aux props dans Vue

L'objectif principal de l'utilisation des props est de transmettre des données/informations. Vous pouvez soit passer votre valeur en tant que propriété de données en utilisant `v-bind`, comme dans ce code :

```
<template>
  <ComponentName :title=title />
</template>

<script>
export default {
  //...
  data() {
    return {
      title: 'Understanding Props in vuejs'
    }
  },
  //...
}
</script>
```

ou comme une valeur statique comme ceci :

```
<ComponentName title="Understanding Props in vuejs" />
```

Supposons que nous construisions une application qui possède de nombreux boutons avec des textes ou des couleurs de fond différents. Au lieu de répéter la syntaxe du bouton dans tous nos fichiers, il est préférable de créer un composant bouton puis de passer le texte ou les couleurs de fond en tant que props.

Voici le composant parent :

```
<template>
  <div id="app">
    <Button :name='btnName' bgColor='red' />
    <Button :name='btnName' bgColor='green' />
    <Button :name='btnName' bgColor='blue' />
  </div>
</template>

<script>
import Button from './components/Button'

export default {
  name: 'App',
  data(){
    return{
      btnName:"Joel",
    }
  },
  components: {
    Button
  }
}
</script>
```

Et voici le composant enfant :

```
<template>
  <button class="btn" :style="{backgroundColor:bgColor}">{{name}}</button>
</template>
<script>
export default {
  name: 'Button',
  props:{
    name:String,
    bgColor:String
  }
}
</script>
```

Le code ci-dessus vous montre comment utiliser à la fois une propriété de données et des valeurs statiques lorsque vous récupérez des données d'un composant parent pour les utiliser dans un composant enfant.

**Note :** vous pouvez également utiliser un opérateur ternaire à l'intérieur de la valeur de la prop pour vérifier une condition et passer une valeur qui en dépend.

```
<template>
  <div id="app">
    <Button :tagUser="signedUp ? 'Logout' : 'Login'" bgColor='red' />
  </div>
</template>
<script>
import Button from './components/Button'
export default {
  name: 'App',
  data(){
    return{
      signedUp: true,
    }
  },
  components: {
    Button
  }
}
</script>
```

Dans le code ci-dessus, nous vérifions la propriété de données `signedUp`. Si elle est vraie, la donnée envoyée sera **Logout**, sinon ce sera **Login**.

## Comment passer des fonctions aux props

Passer une fonction ou une méthode à un composant enfant en tant que prop est relativement simple. C'est fondamentalement le même processus que pour passer n'importe quelle autre variable.

Cependant, il existe des raisons pour lesquelles vous ne devriez pas utiliser les props comme fonctions – vous devriez plutôt utiliser `emit`. Cet article explique correctement [pourquoi][1].

```
<template>
  <ChildComponent :function="newFunction" />
</template>
```

```
<script>
export default {
  methods: {
    newFunction() {
      // ...
    }
  }
};
</script>
```

## Comment valider les props dans Vue

Vue rend la validation des props très facile. Tout ce que vous avez à faire est d'ajouter la clé `required` et sa valeur à la prop. Nous pouvons valider à la fois avec le type de prop et en utilisant `required` :

```
props: {
  name: {
    type: String,
    required: true
  }
}
```

## Comment définir des valeurs par défaut pour les props

Avant de conclure cet article, voyons maintenant comment définir des valeurs par défaut pour nos props. Les valeurs par défaut sont rendues si le composant enfant n'est pas en mesure de récupérer les données du composant parent.

Vue vous permet de spécifier une valeur par défaut, tout comme nous avons spécifié `required` précédemment.

```
props: {
  name: {
    type: String,
    required: true,
    default: 'John Doe'
  },
  img: {
    type: String,
    default: '../image-path/image-name.jpg',
   },
}
```

Vous pouvez également définir la valeur par défaut comme un objet. Et cela peut être une fonction qui renvoie une valeur appropriée, plutôt que d'être la valeur réelle elle-même.

## Conclusion

Dans cet article, nous avons appris à quoi servent les props et comment elles fonctionnent dans Vue.js.

En résumé, nous utilisons les props pour transmettre des données des composants parents aux composants enfants. Le composant enfant émet également des événements vers le(s) composant(s) parent(s) au cas où vous auriez besoin d'envoyer des données ou des événements de l'enfant vers le parent.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-50.png)

Merci de m'avoir lu !

**Liens utiles**

-   [Vue.js Component Props - flaviocopes][2]
-   [Props - Documentation Vue][3]

[1]: https://michaelnthiessen.com/pass-function-as-prop/
[2]: https://flaviocopes.com/vue-props/
[3]: https://vuejs.org/v2/guide/components-props.html