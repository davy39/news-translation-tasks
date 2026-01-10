---
title: Une introduction au développement piloté par les tests avec Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-17T15:45:21.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-tdd-with-vue-js-66544710b50c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*QphJEMJgj30s60_w
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Une introduction au développement piloté par les tests avec Vue.js
seo_desc: 'By Sarah Dayan

  Test-driven development (TDD) is a process where you write tests before you write
  the associated code. You first write a test that describes an expected behavior,
  and you run it, ensuring it fails. Then, you write the dumbest, most str...'
---

Par Sarah Dayan

Le développement piloté par les tests (TDD) est un processus où **vous écrivez les tests avant d'écrire le code associé**. Vous commencez par écrire un test qui décrit un comportement attendu, puis vous l'exécutez en vous assurant qu'il échoue. Ensuite, vous écrivez le code le plus simple et le plus direct possible pour faire passer le test. Enfin, vous refactorisez le code pour le rendre correct. Et vous répétez toutes ces étapes pour chaque test jusqu'à ce que vous ayez terminé.

Cette approche présente de nombreux avantages. Premièrement, **elle vous oblige à réfléchir avant de coder**. Il est courant de se précipiter pour écrire du code avant d'avoir établi ce qu'il doit faire. Cette pratique conduit à une perte de temps et à l'écriture de code compliqué. Avec le TDD, chaque nouveau morceau de code nécessite un test en premier, vous n'avez donc pas le choix de prendre le temps de définir ce que ce code doit faire avant de l'écrire.

Deuxièmement, **elle garantit que vous écrivez des tests unitaires**. Commencer par le code conduit souvent à écrire des tests incomplets, voire aucun test du tout. Une telle pratique se produit généralement en raison de l'absence de spécifications précises et exhaustives, ce qui conduit à passer plus de temps à coder que nécessaire. L'écriture de tests devient un effort coûteux, facile à négliger une fois le code de production prêt.

**Les tests unitaires sont essentiels pour construire un code robuste**. Les négliger ou les précipiter augmente les chances que votre code se casse en production à un moment donné.

### Pourquoi faire du TDD pour les composants ?

**Tester un composant peut être contre-intuitif**. Comme nous l'avons vu dans [Unit Test Your First Vue.js Component](https://frontstuff.io/unit-test-your-first-vuejs-component), cela nécessite un changement de mentalité pour comprendre comment tester les composants par rapport aux scripts simples, savoir quoi tester et comprendre la ligne entre les tests unitaires et les tests de bout en bout.

**Le TDD rend tout cela plus facile**. Au lieu d'écrire des tests en examinant tous les morceaux d'un projet terminé et en essayant de deviner ce que vous devriez couvrir, vous faites l'inverse. Vous partez des spécifications réelles, d'une liste de choses que le composant devrait _faire_, sans vous soucier de la manière dont il le fait. De cette façon, vous vous assurez que tout ce que vous testez est l'API publique, mais vous garantissez également que vous n'oubliez rien.

Dans ce tutoriel, nous allons construire **un sélecteur de couleurs**. Pour chaque nuance, les utilisateurs peuvent accéder au code de couleur correspondant, soit en hexadécimal, RGB ou HSL.

![Image](https://cdn-media-1.freecodecamp.org/images/Wrkahf5Etl-FNZ1wqzdKG4dK9lnJtfmjL6Nt)
_Design inspiré de [Chris Castillo](https://dribbble.com/shots/2908891-Custom-Color-Picker-Exploration" rel="noopener" target="_blank" title="">Custom Color Picker Exploration</a> par <a href="https://dribbble.com/_ChrisCastillo" rel="noopener" target="_blank" title=")_

Malgré sa simplicité apparente, il y a plusieurs petits morceaux de logique à tester. Ils nécessitent une certaine réflexion avant de se lancer dans le code.

Dans cet article, nous allons approfondir le TDD. Nous allons [mettre ensemble quelques spécifications](https://frontstuff.io/an-introduction-to-tdd-with-vuejs#heading-installation) avant d'écrire une seule ligne de code. Ensuite, nous allons [tester chaque fonctionnalité publique](https://frontstuff.io/an-introduction-to-tdd-with-vuejs#write-test-driven-code) de manière pilotée par les tests. Enfin, nous allons réfléchir à ce que nous avons fait et [voir ce que nous pouvons en apprendre](https://frontstuff.io/an-introduction-to-tdd-with-vuejs#afterthoughts).

### Avant de commencer

Ce tutoriel suppose que vous avez déjà construit quelque chose avec Vue.js auparavant et écrit des tests unitaires pour cela en utilisant [Vue Test Utils](https://vue-test-utils.vuejs.org/) et [Jest](https://jestjs.io/) (ou un exécuteur de tests similaire). Il n'ira pas plus loin dans les fondamentaux, alors assurez-vous d'être à jour d'abord. Si vous n'y êtes pas encore, je vous recommande de passer par [Build Your First Vue.js Component](https://frontstuff.io/build-your-first-vue-js-component) et [Unit Test Your First Vue.js Component](https://frontstuff.io/unit-test-your-first-vuejs-component).

**_TL;DR:_** _cet article va en profondeur dans le comment et le pourquoi. Il est conçu pour vous aider à comprendre chaque décision derrière le test d'un composant Vue.js réel avec TDD et vous apprendre à prendre des décisions de conception pour vos futurs projets. Si vous voulez comprendre tout le processus de réflexion, continuez à lire. Sinon, vous pouvez aller directement aux [réflexions finales](https://frontstuff.io/an-introduction-to-tdd-with-vuejs#afterthoughts) à la fin, ou regarder le code final sur [GitHub](https://github.com/sarahdayan/colorpicker-tdd-tutorial)._

### Écrire vos spécifications

Avant même d'écrire votre premier test, **vous devriez écrire un aperçu de ce que le composant devrait faire**. Avoir des spécifications rend les tests beaucoup plus simples, car vous réécrivez principalement chaque spécification sous forme de tests.

Réfléchissons aux différentes parties qui composent notre composant et à ce qu'elles devraient faire.

Tout d'abord, nous avons une collection de **nuances de couleurs**. Nous voulons pouvoir passer une liste de couleurs personnalisées et les afficher sous forme de nuances dans le composant. La première devrait être sélectionnée par défaut, et l'utilisateur final peut en sélectionner une nouvelle en cliquant dessus.

Deuxièmement, nous avons le **bouton de basculement du mode de couleur**. L'utilisateur final devrait pouvoir basculer entre trois modes : hexadécimal (par défaut), RGB et HSL.

Enfin, nous avons le **code de couleur de sortie**, où l'utilisateur final peut obtenir le code pour la nuance de couleur actuellement sélectionnée. Ce code est une combinaison de la nuance sélectionnée et du mode de couleur. Ainsi, par défaut, il devrait afficher la première nuance sous forme de valeur hexadécimale. Lorsque l'un de ces éléments change, le code doit être mis à jour en conséquence.

Comme vous pouvez le voir, nous n'allons pas trop dans les détails ; nous ne spécifions pas à quoi les étiquettes des modes de couleur devraient ressembler, ni à quoi ressemble l'état actif pour les nuances de couleur. Nous pouvons prendre la plupart des petites décisions à la volée, même en faisant du TDD. Pourtant, nous sommes passés **d'une simple définition de ce que le composant devrait être, à un ensemble complet de spécifications pour commencer**.

### Écrire du code piloté par les tests

Tout d'abord, vous devez créer un nouveau projet Vue avec [Vue CLI](https://cli.vuejs.org/). Vous pouvez consulter [Build Your First Vue.js Component](https://frontstuff.io/build-your-first-vue-js-component) si vous avez besoin d'un guide étape par étape.

Pendant le processus de création, sélectionnez manuellement les fonctionnalités et assurez-vous de cocher **Unit testing**. Choisissez Jest comme solution de test, et procédez jusqu'à ce que le projet soit créé, que les dépendances soient installées et que vous soyez prêt à commencer.

Nous aurons besoin d'utiliser des fichiers SVG comme composants, vous devez donc également installer le bon chargeur pour eux. Installez [vue-svg-loader](https://www.npmjs.com/package/vue-svg-loader) comme dépendance de développement, et ajoutez une règle pour cela dans votre fichier `vue.config.js`.

```
// vue.config.js

module.exports = {
  chainWebpack: config => {
    const svgRule = config.module.rule('svg')
    svgRule.uses.clear()
    svgRule.use('vue-svg-loader').loader('vue-svg-loader')
  }
}
```

Ce chargeur ne fonctionne pas bien avec Jest par défaut, ce qui fait que les tests échouent. Pour le corriger, créez un fichier `svgTransform.js` [comme documenté sur le site](https://vue-svg-loader.js.org/faq.html#how-to-use-this-loader-with-jest), et modifiez votre `jest.config.js` comme suit :

```
// svgTransform.js

const vueJest = require('vue-jest/lib/template-compiler')

module.exports = {
  process(content) {
    const { render } = vueJest({
      content,
      attrs: {
        functional: false
      }
    })
    
    return `module.exports = { render: ${render} }`
  }
}

// jest.config.js

module.exports = {
  // ...
  transform: {
    // ...
    '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2)$': 'jest-transform-stub',
    '^.+\\.svg$': '<rootDir>/svgTransform.js'
  },
  // ...
}
```

Notez que nous avons supprimé "svg" de la première expression régulière (celle qui est transformée avec `jest-transform-stub`). De cette façon, nous nous assurons que les SVG sont pris en charge par `svgTransform.js`.

De plus, vous devez installer [color-convert](https://www.npmjs.com/package/color-convert) comme dépendance. Nous en aurons besoin à la fois dans notre code et dans nos tests plus tard.

**Ne servez pas encore le projet**. Nous allons écrire des tests et nous appuyer sur leur réussite ou leur échec pour avancer. Nous ne voulons pas contrôler si ce que nous construisons fonctionne en le testant visuellement dans le navigateur, ni être distraits par son apparence.

Au lieu de cela, ouvrez votre projet et créez un nouveau composant `ColorPicker.vue` dans le répertoire `src/components/`. Dans `tests/unit/`, créez son fichier de spécification associé.

```
<!-- ColorPicker.vue -->

<template>
  <div></div>
</template>

<script>
export default {}
</script>

<style>
</style>

// ColorPicker.spec.js

import { shallowMount } from '@vue/test-utils'
import ColorPicker from '@/components/ColorPicker'

describe('ColorPicker', () => {
  // let's do this!
})
```

Dans votre terminal, exécutez la commande suivante pour lancer les tests :

```
npm run test:unit --watchAll
```

Pour l'instant, vous devriez obtenir une erreur car vous n'avez pas encore de tests. Ne vous inquiétez pas cependant ; nous allons corriger cela sous peu ? Notez l'utilisation du drapeau `-watchAll` dans la commande : Jest surveille maintenant vos fichiers. De cette façon, vous n'aurez pas à relancer les tests manuellement.

Le TDD se déroule en 3 étapes :

1. **Rouge** : vous écrivez un test qui décrit un comportement attendu, puis vous l'exécutez, en vous assurant qu'il échoue.
2. **Vert** : vous écrivez le code le plus simple et le plus direct possible pour faire passer le test.
3. **Refactorisation** : vous refactorisez le code pour le rendre correct.

### Étape 1 : Rouge

Il est temps d'écrire notre premier test ! Nous allons commencer par les nuances de couleurs. Pour plus de clarté, nous allons envelopper tous les tests pour chaque élément distinct dans leur propre suite, en utilisant un bloc `describe`.

Tout d'abord, nous voulons nous assurer que le composant affiche chaque couleur que nous fournissons sous forme de nuance individuelle. Nous passerions celles-ci sous forme de props, sous la forme d'un tableau de chaînes hexadécimales. Dans le composant, nous afficherions la liste sous forme de liste non ordonnée, et attribuerions la couleur de fond via un attribut `style`.

```
import { shallowMount } from '@vue/test-utils'
import ColorPicker from '@/components/ColorPicker'
import convert from 'color-convert'

let wrapper = null

const propsData = {
  swatches: ['e3342f', '3490dc', 'f6993f', '38c172', 'fff']
}

beforeEach(() => (wrapper = shallowMount(ColorPicker, { propsData })))
afterEach(() => wrapper.destroy())

describe('ColorPicker', () => {
  describe('Swatches', () => {
    test('displays each color as an individual swatch', () => {
      const swatches = wrapper.findAll('.swatch')
      propsData.swatches.forEach((swatch, index) => {
        expect(swatches.at(index).attributes().style).toBe(
          `background: rgb(${convert.hex.rgb(swatch).join(', ')})`
        )
      })
    })
  })
})
```

Nous avons monté notre composant `ColorPicker` et écrit un test qui s'attend à trouver des éléments avec une couleur de fond correspondant aux couleurs passées en props. **Ce test est destiné à échouer** : nous n'avons actuellement rien dans `ColorPicker.vue`. Si vous regardez votre terminal, vous devriez avoir une erreur indiquant qu'aucun élément n'existe à l'index 0. C'est génial ! **Nous venons de passer la première étape du TDD avec brio.**

### Étape 2 : Vert

Notre test échoue ; nous sommes sur la bonne voie. Maintenant, il est temps de le faire passer. Nous ne sommes pas très intéressés à écrire du code fonctionnel ou intelligent à ce stade, tout ce que nous voulons est de rendre Jest heureux. Actuellement, Vue Test Utils se plaint du fait que nous n'avons même pas d'élément à l'index 0.

```
[vue-test-utils]: no item exists at 0
```

La chose la plus simple que nous pouvons faire pour faire disparaître cette erreur est d'ajouter une liste non ordonnée avec une classe `swatch` sur l'élément de la liste.

```
<template>
  <div class="color-picker">
    <ul class="swatches">
      <li class="swatch"></li>
    </ul>
  </div>
</template>
```

Jest se plaint toujours mais l'erreur a changé :

```
Expected value to equal:
  "background: rgb(227, 52, 47);"
Received:
  undefined
```

Cela a du sens ; l'élément de la liste n'a pas d'attribut `style`. La chose la plus simple que nous pouvons faire à ce sujet est de coder en dur l'attribut `style`. Ce n'est pas ce que nous voulons à la fin, mais nous ne nous en soucions pas encore. Ce que nous voulons, c'est **que notre test passe au vert**.

Nous pouvons donc coder en dur cinq éléments de liste avec les attributs de style attendus :

```
<ul class="swatches">
  <li class="swatch" style="background: rgb(227, 52, 47);"></li>
  <li class="swatch" style="background: rgb(52, 144, 220);"></li>
  <li class="swatch" style="background: rgb(246, 153, 63);"></li>
  <li class="swatch" style="background: rgb(56, 193, 114);"></li>
  <li class="swatch" style="background: rgb(255, 255, 255);"></li>
</ul>
```

Le test devrait maintenant passer.

### Étape 3 : Refactorisation

À ce stade, nous voulons réorganiser notre code pour le rendre correct, sans casser les tests. Dans notre cas, nous ne voulons pas garder les éléments de liste et leurs attributs `style` codés en dur. Au lieu de cela, il serait préférable de recevoir les nuances sous forme de prop, d'itérer sur elles pour générer les éléments de liste, et d'assigner les couleurs comme leur fond.

```
<template>
  <div class="color-picker">
    <ul class="swatches">
      <li
        :key="index"
        v-for="(swatch, index) in swatches"
        :style="{ background: `#${swatch}` }"
        class="swatch"
      ></li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    swatches: {
      type: Array,
      default() {
        return []
      }
    }
  }
}
</script>
```

Lorsque les tests sont relancés, ils devraient toujours passer ? Cela signifie que **nous avons refactorisé le code avec succès sans affecter la sortie**. Félicitations, vous venez de compléter votre premier cycle TDD !

Maintenant, avant de passer au test suivant, réfléchissons un peu. Vous vous demandez peut-être :

> « N'est-ce pas un peu stupide ? Je savais que le test échouerait. Ne perds-je pas mon temps en l'exécutant quand même, puis en codant en dur la bonne valeur, en voyant le test passer, puis en rendant le code correct ? Ne puis-je pas passer directement à l'étape de refactorisation ? »

Il est compréhensible que vous vous sentiez confus par le processus. Pourtant, essayez de voir les choses sous un angle différent : le but ici n'est pas de _prouver_ que le test ne passe pas. Nous savons qu'il ne passera pas. Ce que nous voulons examiner, c'est ce que notre test _attend_, les rendre heureux de la manière la plus simple possible, et enfin écrire un code plus intelligent sans rien casser.

C'est toute l'idée du développement piloté par les tests : nous n'écrivons pas de code pour faire fonctionner les choses, **nous écrivons du code pour faire passer les tests**. En inversant la relation, nous garantissons des tests robustes avec un accent sur le résultat.

### Que testons-nous ?

Une autre question qui peut venir à l'esprit est **comment nous décidons de ce que nous testons**. Dans [Unit Test Your First Vue.js Component](https://frontstuff.io/unit-test-your-first-vuejs-component), nous avons vu que nous devrions seulement tester l'API publique de notre composant, et non l'implémentation interne. Strictement parlant, cela signifie que nous devrions couvrir **les interactions utilisateur** et **les changements de props**.

Mais est-ce tout ? Par exemple, est-ce acceptable que le HTML de sortie se casse ? Ou que les noms de classes CSS changent ? Sommes-nous sûrs que personne ne s'appuie sur eux ? Que vous ne le faites pas vous-même ?

**Les tests devraient vous donner confiance que vous ne livrez pas de logiciel cassé.** Ce que les gens peuvent faire avec votre programme ne devrait pas cesser de fonctionner de la manière dont ils s'attendent à ce qu'il fonctionne. Cela peut signifier différentes choses selon le projet et le cas d'utilisation.

Par exemple, si vous construisez ce panneau de couleurs comme un composant open source, vos utilisateurs sont d'autres développeurs qui l'utilisent dans leurs propres projets. Ils s'appuient probablement sur les noms de classes que vous fournissez pour styliser le composant à leur guise. **Les noms de classes deviennent une partie de votre API publique parce que vos utilisateurs s'appuient sur eux.**

Dans notre cas, nous ne faisons peut-être pas nécessairement un composant open source, mais nous avons une logique de vue qui dépend de noms de classes spécifiques. Par exemple, il est important que les nuances actives aient un nom de classe `active`, car nous allons nous appuyer sur lui pour afficher une coche, en CSS. Si quelqu'un change cela par accident, nous voulons le savoir.

Les scénarios de test pour les composants d'interface utilisateur dépendent fortement du cas d'utilisation et des attentes. Quel que soit le cas, ce que vous devez vous demander est **est-ce que je me soucie de cela si cela change** ?

### Prochains tests

#### Tester les nuances

Passons au test suivant. Nous nous attendons à ce que la première nuance de la liste soit celle qui est sélectionnée par défaut. De l'extérieur, **c'est quelque chose que nous voulons nous assurer de continuer à fonctionner de la même manière**. Les utilisateurs pourraient, par exemple, s'appuyer sur le nom de la classe active pour styliser le composant.

```
test('sets the first swatch as the selected one by default', () => {
  const firstSwatch = wrapper.find('.swatch')
  expect(firstSwatch.classes()).toContain('active')
})
```

Ce test aussi devrait échouer, car les éléments de la liste n'ont actuellement aucune classe. Nous pouvons facilement le faire passer en ajoutant la classe sur le premier élément de la liste.

```
<li
  :key="index"
  v-for="(swatch, index) in swatches"
  :style="{ background: `#${swatch}` }"
  class="swatch"
  :class="{ 'active': index === 0 }"
></li>
```

Le test passe maintenant ; cependant, nous avons codé en dur la logique dans le modèle. Nous pouvons refactoriser cela en externalisant l'index sur lequel la classe s'applique. De cette façon, nous pouvons le changer plus tard.

```
<template>
  <!-- ... -->
  <li
    :key="index"
    v-for="(swatch, index) in swatches"
    :style="{ background: `#${swatch}` }"
    class="swatch"
    :class="{ active: index === activeSwatch }"
  ></li>
  <!-- ... -->
</template>

export default {
  // ...
  data() {
    return {
      activeSwatch: 0
    }
  }
}
```

Cela nous conduit naturellement à notre troisième test. Nous voulons changer la nuance active chaque fois que l'utilisateur final clique dessus.

```
test('makes the swatch active when clicked', () => {
  const targetSwatch = wrapper.findAll('.swatch').at(2)
  targetSwatch.trigger('click')
  expect(targetSwatch.classes()).toContain('active')
})
```

Pour l'instant, rien ne se passe lorsque nous cliquons sur une nuance. Cependant, grâce à notre refactorisation précédente, nous pouvons faire passer ce test et même sauter l'étape de refactorisation.

```
<li
  :key="index"
  v-for="(swatch, index) in swatches"
  :style="{ background: `#${swatch}` }"
  class="swatch"
  :class="{ active: index === activeSwatch }"
  @click="activeSwatch = index"
></li>
```

Ce code fait passer le test et n'a même pas besoin d'une refactorisation. **C'est un effet secondaire heureux de faire du TDD** : parfois, le processus conduit à écrire de nouveaux tests qui n'ont pas besoin de refactorisations, ou même qui passent immédiatement.

Les nuances actives devraient montrer une coche. Nous allons l'ajouter maintenant **sans écrire de test** : au lieu de cela, nous contrôlerons leur visibilité via CSS plus tard. Cela est acceptable puisque nous avons déjà testé comment la classe `active` s'applique.

Tout d'abord, créez un fichier `checkmark.svg` dans `src/assets/`.

```
<svg viewBox="0 0 448.8 448.8">
  <polygon points="142.8 323.9 35.7 216.8 0 252.5 142.8 395.3 448.8 89.3 413.1 53.6"/>
</svg>
```

Ensuite, importez-le dans le composant.

```
import CheckIcon from '@/assets/check.svg'

export default {
  // ...
  components: { CheckIcon }
}
```

Enfin, ajoutez-le à l'intérieur des éléments de la liste.

```
<li ... >
  <check-icon />
</li>
```

Bien ! Nous pouvons maintenant passer à l'élément suivant de notre composant : **le mode de couleur**.

#### Tester le mode de couleur

Implémentons maintenant le bouton de basculement du mode de couleur. L'utilisateur final devrait pouvoir basculer entre hexadécimal, RGB et HSL. Nous définissons ces modes en interne, mais nous voulons nous assurer qu'ils s'affichent correctement.

Au lieu de tester les étiquettes des boutons, **nous allons nous appuyer sur les noms de classes**. Cela rend notre test plus robuste, car nous pouvons facilement définir un nom de classe comme faisant partie du contrat de notre composant. Cependant, les étiquettes des boutons devraient pouvoir changer.

Maintenant, vous pourriez être tenté de vérifier ces trois modes spécifiques, mais cela rendrait le test fragile. Et si nous les changions ? Et si nous en ajoutions un, ou en supprimions un ? Cela serait toujours la même logique, pourtant le test échouerait, nous forçant à aller le modifier.

Une solution pourrait être d'accéder aux données du composant pour itérer sur les modes dynamiquement. Vue Test Utils nous permet de le faire via la propriété [vm](https://vue-test-utils.vuejs.org/api/wrapper/#properties), mais encore une fois, cela couple étroitement notre test avec l'implémentation interne des modes. Si demain, nous décidions de changer la manière dont nous définissons les modes, le test se casserait.

Une autre solution est de continuer avec les tests en boîte noire et de s'attendre uniquement à ce que le nom de la classe corresponde à un _motif_ donné. Nous ne nous soucions pas que ce soit `color-mode-hex`, `color-mode-hsl` ou `color-mode-xyz`, tant que cela ressemble à ce que nous attendons de l'extérieur. Jest nous permet de faire cela avec des correspondances d'expressions régulières.

```
// ...
describe('Color model', () => {
  test('displays each mode as an individual button', () => {
    const buttons = wrapper.findAll('.color-mode')
    buttons.wrappers.forEach(button => {
      expect(button.classes()).toEqual(
        expect.arrayContaining([expect.stringMatching(/color-mode-\w{1,}/)])
      )
    })
  })
})
```

Ici, nous nous attendons à des éléments avec une classe qui suit le motif "color-mode-" + n'importe quel caractère de mot (dans ECMAScript, n'importe quel caractère dans `[a-zA-Z_0-9]`). Nous pourrions ajouter ou supprimer n'importe quel mode, et le test serait toujours valide.

Naturellement, pour l'instant, le test devrait échouer, car il n'y a pas encore de boutons avec la classe `color-mode`. Nous pouvons le faire passer en les codant en dur dans le composant.

```
<div class="color-modes">
  <button class="color-mode color-mode-hex"></button>
  <button class="color-mode color-mode-rgb"></button>
  <button class="color-mode color-mode-hsl"></button>
</div>
```

Nous pouvons maintenant refactoriser ce code en ajoutant les modes comme données privées dans notre composant et en itérant sur eux.

```
<template>
  <!-- ... -->
  <div class="color-modes">
    <button
      :key="index"
      v-for="(mode, index) in colorModes"
      class="color-mode"
      :class="`color-mode-${mode}`"
    >{{ mode }}</button>
  </div>
  <!-- ... -->
</template>

export default {
  // ...
  data() {
    return {
      activeSwatch: 0,
      colorModes: ['hex', 'rgb', 'hsl']
    }
  }
}
```

Bien ! Continuons.

Comme pour les nuances, nous voulons que le premier mode soit défini comme actif. Nous pouvons copier le test que nous avons écrit et l'adapter à ce nouveau cas d'utilisation.

```
test('sets the first mode as the selected one by default', () => {
  const firstButton = wrapper.find('.color-mode')
  expect(firstButton.classes()).toContain('active')
})
```

Nous pouvons faire passer ce test en ajoutant manuellement la classe sur le premier élément de la liste.

```
<button
  :key="index"
  v-for="(mode, index) in colorModes"
  class="color-mode"
  :class="[{ active: index === 0 }, `color-mode-${mode}`]"
>{{ mode }}</button>
```

Enfin, nous pouvons refactoriser en externalisant l'index sur lequel la classe s'applique.

```
<template>
  <!-- ... -->
  <button
    :key="index"
    v-for="(mode, index) in colorModes"
    class="color-mode"
    :class="[{ active: index === activeMode }, `color-mode-${mode}`]"
  >{{ mode }}</button>
  <!-- ... -->
</template>

export default {
  // ...
  data() {
    return {
      activeSwatch: 0,
      activeMode: 0,
      colorModes: ['hex', 'rgb', 'hsl']
    }
  }
}
```

Nous devons changer le mode actif chaque fois que l'utilisateur final clique sur le bouton associé, comme pour les nuances.

```
test('sets the color mode button as active when clicked', () => {
  const targetButton = wrapper.findAll('.color-mode').at(2)
  targetButton.trigger('click')
  expect(targetButton.classes()).toContain('active')
})
```

Nous pouvons maintenant ajouter une directive `@click` comme nous l'avons fait avec les nuances, et faire passer le test sans avoir à refactoriser.

```
<button
  :key="index"
  v-for="(mode, index) in colorModes"
  class="color-mode"
  :class="[{ active: index === activeMode }, `color-mode-${mode}`]"
  @click="activeMode = index"
>{{ mode }}</button>
```

#### Tester le code de couleur

Maintenant que nous avons terminé de tester les nuances et le code de couleur, nous pouvons passer au troisième et dernier élément de notre sélecteur de couleurs : **le code de couleur**. Ce que nous affichons ici est une combinaison des deux autres : la nuance sélectionnée définit la couleur que nous devons afficher, et le mode sélectionné détermine comment l'afficher.

Tout d'abord, nous voulons nous assurer que nous affichons initialement la nuance par défaut dans le mode par défaut. Nous avons les informations pour construire cela puisque nous avons implémenté les nuances et le mode de couleur.

Commençons par un test (qui échoue).

```
describe('Color code', () => {
  test('displays the default swatch in the default mode', () => {
    expect(wrapper.find('.color-code').text()).toEqual('#e3342f')
  })
})
```

Maintenant, faisons en sorte que cela passe en codant en dur le résultat attendu dans le composant.

```
<div class="color-code">#e3342f</div>
```

Bien ! Il est temps de refactoriser. Nous avons une couleur brute en mode hexadécimal, et nous sommes prêts à la sortir en format hexadécimal. La seule différence entre nos valeurs d'entrée et de sortie est que nous voulons préfixer cette dernière avec un caractère dièse. La manière la plus simple de le faire avec Vue est via une propriété `computed`.

```
<template>
  <!-- ... -->
  <div class="color-code">{{ activeCode }}</div>
  <!-- ... -->
</template>

export default {
  // ...
  computed: {
    activeCode() {
      return `#${this.swatches[this.activeSwatch]}`
    }
  }
}
```

Cela devrait garder le test au vert. Cependant, il y a un problème avec cette propriété calculée : elle ne fonctionne que pour les valeurs hexadécimales. Elle devrait continuer à fonctionner lorsque nous changeons la couleur, mais pas lorsque nous changeons le mode. Nous pouvons vérifier cela avec un autre test.

```
test('displays the code in the right mode when changing mode', () => {
  wrapper.find('.color-mode-hsl').trigger('click')
  expect(wrapper.find('.color-code').text()).toEqual('2°, 76%, 54%')
})
```

Ici, nous avons changé pour le mode HSL, mais nous obtenons toujours la sortie hexadécimale. Nous devons refactoriser notre code pour que notre propriété calculée `activeCode` soit non seulement consciente de la couleur actuelle, mais aussi du mode de couleur actuel. Une façon d'y parvenir est de créer des propriétés calculées pour chaque mode et de les proxyer via `activeCode` en fonction du mode sélectionné.

Tout d'abord, nous devrions simplifier l'accès à la couleur et au mode actuels. Actuellement, nous devons faire une recherche dans un tableau, ce qui est répétitif et rend le code difficile à lire. Nous pouvons utiliser des propriétés calculées pour envelopper cette logique.

```
export default {
  // ...
  computed: {
    // ...
    activeColorValue() {
      return this.swatches[this.activeSwatch]
    },
    activeModeValue() {
      return this.colorModes[this.activeMode]
    }
  }
}
```

Comme vous pouvez le voir, nous n'écrivons pas de tests pour ces propriétés calculées, car elles ne font pas partie de notre API publique. Nous les utiliserons plus tard dans nos propriétés calculées dédiées aux modes de couleur, qui elles-mêmes seront proxyées dans `activeCode`, que nous testons dans notre suite "Color code". **Tout ce qui nous importe, c'est que le code de couleur s'affiche comme prévu** afin que l'utilisateur puisse s'y fier. La manière dont nous y arrivons est un détail d'implémentation que nous devons pouvoir changer si nécessaire.

Nous pouvons maintenant écrire nos propriétés calculées dédiées pour chaque mode. Nous mapperons leur nom sur ceux dans `colorModes`, afin de pouvoir faire une recherche dans un tableau plus tard dans `activeCode` pour retourner le bon.

Pour la sortie hexadécimale, nous pouvons externaliser ce que nous avons actuellement dans `activeCode` et le refactoriser en utilisant `activeColorValue`.

```
export default {
  // ...
  computed: {
    // ...
    hex() {
      return `#${this.activeColorValue}`
    }
  }
}
```

Maintenant, modifions `activeCode` pour qu'il proxy la bonne propriété calculée en fonction du mode actif.

```
export default {
  // ...
  computed: {
    // ...
    activeCode() {
      return this[this.activeModeValue]
    }
  }
}
```

Cela ne devrait toujours pas faire passer notre dernier test, puisque nous n'avons pas écrit de propriété calculée pour celui-ci. Cependant, notre test qui vérifie si le mode par défaut s'affiche correctement passe toujours, ce qui est un bon signe que nous sommes sur la bonne voie.

Nous voulons maintenant écrire une propriété calculée qui retourne la sortie de couleur en mode HSL. Pour cela, nous allons utiliser `color-convert`, un package npm qui nous permet de convertir les couleurs dans de nombreux modes différents. Nous l'avons déjà utilisé dans nos tests, donc nous n'avons pas besoin de le réinstaller.

```
import convert from 'color-convert'

export default {
  // ...
  computed: {
    // ...
    hsl() {
      const hslColor = convert.hex.hsl(this.activeColorValue)
      return `${hslColor[0]}°, ${hslColor[1]}%, ${hslColor[2]}%`
    }
  }
}
```

Super, notre test passe ! Nous pouvons maintenant terminer cela en ajoutant le mode RGB manquant.

Cependant, comme vous pouvez le voir, nous ne testons actuellement pas la sortie de nos propriétés calculées de couleur de manière isolée, mais à travers d'autres tests. Pour rendre les choses plus propres, nous pourrions découpler cette logique du composant, l'importer en tant que dépendance et la tester séparément. Cela présente plusieurs avantages :

* cela empêche le composant de grandir chaque fois que nous voulons ajouter un mode de couleur,
* cela maintient les domaines séparés : le composant se concentre sur sa propre logique de vue, et l'utilitaire des modes de couleur s'occupe de tester chaque mode de manière exhaustive.

Tout d'abord, créez un nouveau fichier `color.js` dans le répertoire `src/utils/`, et un fichier de spécification correspondant dans `tests/unit/`.

```
// color.spec.js

import { rgb, hex, hsl } from '@/utils/color'

// color.js

import convert from 'color-convert'

export const rgb = () => {}

export const hex = () => {}

export const hsl = () => {}
```

Nous pouvons utiliser le TDD pour tester ces trois fonctions et nous assurer qu'elles retournent toujours la valeur attendue. Nous pouvons extraire la logique que nous avions dans notre composant Vue pour les deux dernières, et écrire la fonction RGB à partir de zéro.

Pour des raisons de brièveté, nous couvrirons les trois tests à la fois, mais le processus reste le même.

```
import { rgb, hex, hsl } from '@/utils/color'

const color = 'e3342f'

describe('color', () => {
  test('returns the color into RGB notation', () => {
    expect(rgb(color)).toBe('227, 52, 47')
  })
  test('returns the color into hexadecimal notation', () => {
    expect(hex(color)).toBe('#e3342f')
  })
  test('returns the color into HSL notation', () => {
    expect(hsl(color)).toBe('2°, 76%, 54%')
  })
})
```

Nous avons maintenant trois tests qui échouent. La première chose que nous pouvons faire est de retourner des valeurs codées en dur pour passer au vert.

```
export const rgb = () => '227, 52, 47'

export const hex = () => '#e3342f'

export const hsl = () => '2°, 76%, 54%'
```

Maintenant, nous pouvons commencer à refactoriser en migrant le code de notre composant Vue.

```
export const hex = () => `#${color}`

export const hsl = color => {
  const hslColor = convert.hex.hsl(color)
  return `${hslColor[0]}°, ${hslColor[1]}%, ${hslColor[2]}%`
}
```

Enfin, nous pouvons implémenter notre fonction `rgb`.

```
export const rgb = color => convert.hex.rgb(color).join(', ')
```

Tous les tests devraient rester au vert !

Nous pouvons maintenant utiliser les utilitaires `color` dans notre composant Vue et le refactoriser un peu. Nous n'avons plus besoin d'importer `color-convert` dans le composant, ni d'avoir des propriétés calculées dédiées pour chaque mode, ni même d'obtenir les valeurs de couleur et de mode actives. Tout ce que nous devons garder est `activeCode`, où nous pouvons stocker toute la logique nécessaire.

C'est un bon exemple où faire des tests en boîte noire nous aide : nous nous sommes concentrés sur le test de l'API publique ; ainsi **nous pouvons refactoriser les internes de notre composant sans casser les tests**. Supprimer des propriétés comme `activeColorValue` ou `hex` n'a pas d'importance, car nous ne les testions jamais directement.

```
// ...
import { rgb, hex, hsl } from '@/utils/color'

const modes = { rgb, hex, hsl }

export default {
  // ...
  computed: {
    activeCode() {
      const activeColor = this.swatches[this.activeSwatch]
      const activeMode = this.colorModes[this.activeMode]
      return modes[activeMode](activeColor)
    }
  }
}
```

Nous avons maintenant un code beaucoup plus concis dans notre composant, et une meilleure séparation des domaines, tout en respectant le contrat du composant.

Enfin, nous pouvons implémenter un test manquant : celui qui garantit que le code de couleur change chaque fois que nous cliquons sur une nouvelle nuance. Cela devrait déjà passer au vert, mais il est toujours essentiel pour nous de l'écrire, afin de savoir si cela se casse.

```
test('displays the code in the right color when changing color', () => {
  wrapper
    .findAll('.swatch')
    .at(2)
    .trigger('click')
  expect(wrapper.find('.color-code').text()).toEqual('#f6993f')
})
```

Et nous avons terminé ! Nous venons de construire un composant Vue entièrement fonctionnel en utilisant le TDD, sans nous appuyer sur la sortie du navigateur, **et nos tests sont prêts**.

### Contrôle visuel

Maintenant que notre composant est prêt, nous pouvons voir à quoi il ressemble et jouer avec dans le navigateur. Cela nous permet d'ajouter le CSS et de nous assurer que nous n'avons rien manqué.

Tout d'abord, montez le composant dans le fichier principal `App.vue`.

```
<!-- App.vue -->

<template>
  <div id="app">
    <color-picker :swatches="['e3342f', '3490dc', 'f6993f', '38c172', 'fff']"/>
  </div>
</template>

<script>
import ColorPicker from '@/components/ColorPicker'

export default {
  name: 'app',
  components: {
    ColorPicker
  }
}
</script>
```

Ensuite, exécutez l'application en exécutant le script suivant, et ouvrez-la dans votre navigateur à l'adresse `[http://localhost:8080/](http://localhost:8080/)`.

```
npm run serve
```

Vous devriez voir votre sélecteur de couleurs ! Il ne ressemble pas à grand-chose pour l'instant, mais il fonctionne. Essayez de cliquer sur les couleurs et de changer le mode de couleur ; vous devriez voir le code de couleur changer.

Pour voir le composant avec un style approprié, ajoutez le CSS suivant entre les balises `style` :

```
.color-picker {
  background-color: #fff;
  border: 1px solid #dae4e9;
  border-radius: 0.125rem;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  color: #596a73;
  font-family: BlinkMacSystemFont, Helvetica Neue, sans-serif;
  padding: 1rem;
}

.swatches {
  color: #fff;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: -0.25rem -0.25rem 0.75rem;
  padding: 0;
}

.swatch {
  border-radius: 0.125rem;
  cursor: pointer;
  height: 2rem;
  margin: 0.25rem;
  position: relative;
  width: 2rem;
}

.swatch::after {
  border-radius: 0.125rem;
  bottom: 0;
  box-shadow: inset 0 0 0 1px #dae4e9;
  content: '';
  display: block;
  left: 0;
  mix-blend-mode: multiply;
  position: absolute;
  right: 0;
  top: 0;
}

.swatch svg {
  display: none;
  color: #fff;
  fill: currentColor;
  margin: 0.5rem;
}

.swatch.active svg {
  display: block;
}

.color-modes {
  display: flex;
  font-size: 1rem;
  letter-spacing: 0.05rem;
  margin: 0 -0.25rem 0.75rem;
}

.color-mode {
  background: none;
  border: none;
  color: #9babb4;
  cursor: pointer;
  display: block;
  font-weight: 700;
  margin: 0 0.25rem;
  padding: 0;
  text-transform: uppercase;
}

.color-mode.active {
  color: #364349;
}

.color-code {
  border: 1px solid #dae4e9;
  border-radius: 0.125rem;
  color: #364349;
  text-transform: uppercase;
  padding: 0.75rem;
}
```

Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*e2w8W0MplRF7UPdc.gif)

Et nous avons terminé !

### Réflexions finales

#### Comment pouvons-nous améliorer cela ?

Pour l'instant, nous avons une suite de tests robuste. Même si nous n'avons pas une couverture à 100 %, nous pouvons nous sentir confiants avec notre composant qui sort dans la nature et évolue au fil du temps. Il y a encore quelques choses que nous pourrions améliorer, selon le cas d'utilisation.

Tout d'abord, vous avez peut-être remarqué que lorsque vous cliquez sur la nuance blanche, la coche ne s'affiche pas. Ce n'est pas un bug, mais plutôt un problème visuel : la coche est là, mais nous ne pouvons pas la voir parce qu'elle est blanche sur blanc. Vous pourriez ajouter un peu de logique pour corriger cela : lorsqu'une couleur est plus claire qu'un certain seuil (disons 90 %), vous pourriez ajouter une classe `light` sur la nuance. Cela vous permettrait ensuite d'appliquer un CSS spécifique et de rendre la coche sombre.

Heureusement, vous avez déjà tout ce dont vous avez besoin : le package `color-converter` peut vous aider à déterminer si une couleur est claire (avec les utilitaires HSL), et vous avez déjà un module utilitaire `color` pour stocker cette logique et la tester de manière isolée. Pour voir à quoi pourrait ressembler le code final, consultez le dépôt du projet sur [GitHub](https://github.com/sarahdayan/colorpicker-tdd-tutorial).

Nous pourrions également renforcer la suite en ajoutant quelques tests pour nous assurer que certaines classes attendues sont présentes. Cela ne teste pas la logique réelle, mais serait néanmoins particulièrement utile si quelqu'un s'appuyait sur ces noms de classes pour styliser le composant de l'extérieur. Encore une fois, tout dépend de votre cas d'utilisation : testez ce qui ne devrait pas changer sans que vous le sachiez, ne ajoutez pas de tests uniquement pour le plaisir.

#### Qu'avons-nous appris ?

Il y a plusieurs leçons à tirer de cette expérience TDD. Elle apporte beaucoup à la table mais met également en lumière quelques défis dont nous devons être conscients.

Tout d'abord, le TDD est **une manière fantastique d'écrire des tests robustes**, ni trop nombreux ni trop peu. Avez-vous déjà terminé un composant, passé aux tests et pensé _« par où commencer ? »_ ? Regarder du code terminé et déterminer quoi tester est difficile. Il est tentant de le faire rapidement, de négliger certaines parties critiques et de se retrouver avec une suite de tests incomplète. Ou vous pouvez adopter une approche défensive et tout tester, risquant de vous concentrer sur les détails d'implémentation et d'écrire des tests fragiles.

Adopter le TDD pour développer des composants d'interface utilisateur nous aide à nous concentrer exactement sur ce qu'il faut tester en **définissant, avant d'écrire une seule ligne de code, si cela fait partie du contrat ou non**.

Deuxièmement, **le TDD encourage les refactorisations, conduisant à une meilleure conception de logiciels**. Lorsque vous écrivez des tests après avoir codé, vous n'êtes généralement plus dans une dynamique de refactorisation. Vous pouvez corriger votre code si vous trouvez des problèmes lors des tests, mais à ce stade, vous avez probablement terminé avec l'implémentation. **C'est dans cette séparation entre l'écriture de code et l'écriture de tests que réside le problème.**

Avec le TDD, **vous créez une connexion plus profonde entre le code et les tests, avec un fort accent sur la fiabilité de l'API publique**. L'implémentation vient juste après avoir garanti le résultat. C'est pourquoi l'étape _verte_ est cruciale : vous devez d'abord faire passer votre test, puis vous assurer qu'il ne se casse jamais. Au lieu d'implémenter votre chemin vers une solution fonctionnelle, vous inversez la relation, en vous concentrant d'abord sur le contrat, et en permettant à l'implémentation de rester jetable. Parce que la refactorisation vient en dernier, et que vous avez établi le contrat, vous avez maintenant l'espace mental pour faire les choses correctement, nettoyer du code, adopter une meilleure conception, ou vous concentrer sur la performance.

Il est intéressant de noter que **le TDD est beaucoup plus facile à suivre avec des spécifications**. Lorsque vous avez déjà une vue d'ensemble claire de tout ce que le composant doit faire, vous pouvez traduire ces spécifications en tests. Certaines équipes utilisent des frameworks comme [ATDD](https://en.wikipedia.org/wiki/Acceptance_test%E2%80%93driven_development) (développement piloté par les tests d'acceptation), où les parties impliquées développent des spécifications à partir d'une perspective métier. Les spécifications finales, ou tests d'acceptation, sont une base parfaite pour écrire des tests en suivant le TDD.

D'un autre côté, se lancer dans le TDD pour tester des composants d'interface utilisateur peut être difficile au début et nécessiter quelques connaissances préalables avant de se lancer. Pour commencer, **vous devez avoir une bonne connaissance de vos bibliothèques de test** afin de pouvoir écrire des assertions fiables. Regardez le test que nous avons écrit avec une expression régulière : la syntaxe n'est pas la plus simple. Si vous ne connaissez pas bien la bibliothèque, il est facile d'écrire un test qui échoue pour de mauvaises raisons, ce qui finirait par entraver tout le processus TDD.

De même, vous devez être conscient de certains détails concernant les valeurs que vous attendez ; sinon, vous pourriez finir par lutter avec vos tests et faire des allers-retours ennuyeux. À ce sujet, les composants d'interface utilisateur sont plus difficiles que les bibliothèques sans rendu, en raison des diverses façons dont les spécifications du DOM peuvent être implémentées.

Prenez le premier test de notre suite par exemple : nous testons les couleurs de fond. Cependant, même si nous passons des couleurs hexadécimales, nous attendons des valeurs de retour RGB. C'est parce que Jest utilise [jsdom](https://github.com/jsdom/jsdom), une implémentation Node.js des normes DOM et HTML. Si nous exécutions nos tests dans un navigateur spécifique, nous pourrions avoir une valeur de retour différente. Cela peut être délicat lorsque vous testez différents moteurs. Vous devrez peut-être rechercher des utilitaires de conversion plus avancés ou utiliser des variables d'environnement pour gérer les diverses implémentations.

#### Est-ce que cela en vaut la peine ?

Si vous êtes arrivé jusqu'ici, vous avez probablement réalisé que **le TDD demande du temps**. Cet article lui-même fait plus de 6 000 mots ! Cela peut être un peu effrayant si vous êtes habitué à des cycles de développement plus rapides, et semble probablement impossible si vous travaillez souvent sous pression. Cependant, il est important de briser le mythe selon lequel le TDD doublerait le temps de développement pour un faible retour sur investissement, car cela est entièrement faux.

Le TDD nécessite de la pratique, et vous irez plus vite avec le temps. Ce qui semble maladroit aujourd'hui peut devenir une seconde nature demain, si vous le faites régulièrement. Je vous encourage à ne pas rejeter quelque chose parce que c'est nouveau et semble étrange : donnez-lui un peu de temps pour l'évaluer équitablement, puis prenez une décision.

Deuxièmement, **le temps passé à écrire du code piloté par les tests est du temps que vous ne passerez pas à corriger des bugs**.

Corriger des bugs est bien plus coûteux que de les prévenir. Si vous avez déjà dû corriger des bugs critiques en production, vous savez que cela ressemble à tenir une plaie ouverte sur un patient chirurgical d'une main, tout en essayant d'opérer avec l'autre. Dans le désert. La nuit. Avec un couteau suisse. C'est désordonné, stressant, sous-optimal, et comporte de grandes chances de tout gâcher dans le processus. Si vous voulez préserver votre santé mentale et la confiance que vos utilisateurs finaux ont dans votre logiciel, **vous voulez éviter ces situations à tout prix**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-ypCMc0eow3xfIdm.gif)

Les tests vous aident à attraper les bugs avant qu'ils n'atteignent la production, et le TDD vous aide à écrire de meilleurs tests. **Si vous pensez que vous devriez tester votre logiciel, alors vous devriez vous soucier de rendre ces tests utiles en premier lieu.** Sinon, tout cela n'est qu'une perte de temps.

Comme pour tout, je vous encourage à essayer le TDD avant de rejeter l'idée. Si vous rencontrez constamment des problèmes de production, ou si vous pensez pouvoir améliorer votre processus de développement, alors cela vaut la peine d'essayer. **Essayez-le pendant une période limitée, mesurez l'impact et comparez les résultats.** Vous pourriez découvrir une méthode qui vous aide à livrer de meilleurs logiciels et à vous sentir plus confiant en appuyant sur le bouton « Déployer ».