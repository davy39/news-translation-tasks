---
title: Comment tester unitairement votre premier composant Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T00:02:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-unit-test-your-first-vue-js-component-14db6e1e360d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HJnhZfsUqdgWcAMIlbqp-w.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
- name: Vue.js
  slug: vuejs
seo_title: Comment tester unitairement votre premier composant Vue.js
seo_desc: 'By Sarah Dayan

  In Build Your First Vue.js Component we made a star rating component. We’ve covered
  many fundamental concepts to help you create more complex Vue.js components.

  Yet, there’s one crucial point you need to build bulletproof components yo...'
---

Par Sarah Dayan

Dans [**Créez votre premier composant Vue.js**](https://frontstuff.io/build-your-first-vue-js-component), nous avons créé un composant d'évaluation par étoiles. Nous avons couvert de nombreux concepts fondamentaux pour vous aider à créer des composants Vue.js plus complexes.

Pourtant, il y a un point crucial dont vous avez besoin pour créer des composants à toute épreuve que vous pouvez utiliser en production : **les tests unitaires**.

### Pourquoi tester unitairement un composant ?

Les tests unitaires sont une partie **cruciale** de l'intégration continue. Ils rendent votre code beaucoup plus fiable en se concentrant sur de petites entités isolées et en s'assurant que celles-ci se comportent toujours comme prévu. Vous pouvez itérer en toute confiance sur votre projet sans craindre de casser des choses.

**Les tests unitaires ne sont pas limités aux scripts.** Tout ce que nous pouvons tester en isolation est testable unitairement, tant que vous respectez quelques bonnes pratiques. Ces pratiques incluent la responsabilité unique, la prévisibilité et le couplage lâche.

En tant qu'entités réutilisables de notre application, **les composants Vue.js sont de grands candidats pour les tests unitaires**. Nous allons tester celui que nous avons créé en tant qu'unité unique avec diverses entrées et interactions utilisateur, et nous assurer qu'il se comporte toujours comme nous l'attendons.

### Avant de commencer

Quelques choses ont changé depuis le [tutoriel initial](https://frontstuff.io/build-your-first-vue-js-component). [Vue CLI 3](https://cli.vuejs.org/) a été publié. [Vue Test Utils](https://vue-test-utils.vuejs.org/) — l'utilitaire officiel de test unitaire Vue.js — a mûri jusqu'à la version bêta. Dans le premier tutoriel, nous avons utilisé [webpack-simple](https://github.com/vuejs-templates/webpack-simple), un modèle de prototypage qui n'inclut pas les fonctionnalités de test. Pour ces raisons, la chose la plus simple à faire est d'effacer l'ardoise et de migrer le projet du tutoriel vers une installation plus récente de Vue.js.

J'ai recréé le projet du premier tutoriel afin que vous puissiez le télécharger directement depuis [GitHub](https://github.com/sarahdayan/star-rating-vue-js-tutorial). Ensuite, naviguez jusqu'au répertoire décompressé et installez les dépendances.

**Note :** assurez-vous d'installer [Node.js](https://nodejs.org/) avant d'aller plus loin :

```
cd chemin/vers/mon/projet npm install
```

Ensuite, exécutez le projet :

```
npm run serve
```

### Vue Test Utils et Jest

Pour ce tutoriel, nous utiliserons [Vue Test Utils](https://vue-test-utils.vuejs.org/), la boîte à outils de test officielle de Vue.js, ainsi que [Jest](https://jestjs.io/), un exécuteur de tests JavaScript soutenu par Facebook.

Vue Test Utils vous permet de monter des composants Vue en isolation et de simuler des interactions utilisateur. Il dispose de toutes les utilités nécessaires pour tester les composants à fichier unique, y compris ceux utilisant Vue Router ou Vuex.

Jest est un exécuteur de tests complet qui nécessite presque aucune configuration. Il fournit également une bibliothèque d'assertions intégrée.

Vue CLI 3 (que j'ai utilisé pour générer le [modèle](https://github.com/sarahdayan/star-rating-vue-js-tutorial)) vous permet de choisir votre exécuteur de tests préféré et le configure pour vous. Si vous souhaitez utiliser un autre exécuteur de tests (comme [Mocha](https://mochajs.org/)), installez [Vue CLI 3](https://cli.vuejs.org/) et générez votre propre projet de démarrage. Ensuite, vous pouvez migrer les fichiers sources de [mon modèle](https://github.com/sarahdayan/star-rating-vue-js-tutorial) directement dedans.

### Que devons-nous tester ?

Une approche courante des tests unitaires est de **se concentrer uniquement sur l'API publique** (aka tests de boîte noire). En ignorant les détails d'implémentation, vous permettez aux internes de changer sans avoir à adapter les tests. Après tout, ce que vous voulez faire est **vous assurer que votre API publique ne cassera pas**. Ce qui se passe sous le capot est testé indirectement, mais tout ce qui compte est que l'API publique reste fiable.

C'est également la recommandation officielle des [guides Vue Test Utils](https://vue-test-utils.vuejs.org/guides/#common-tips). Par conséquent, nous ne testerons que ce à quoi nous pouvons accéder depuis l'extérieur du composant :

* les interactions utilisateur
* les changements de props

Nous ne testerons pas directement les propriétés calculées, les méthodes ou les hooks. Celles-ci seront testées implicitement en testant l'interface publique.

### Configuration d'un fichier de spécification

Comme avec les tests réguliers, chaque composant a un fichier de spécification qui décrit tous les tests que nous voulons exécuter.

Les spécifications sont des fichiers JavaScript. Par convention, ils ont le même nom que les composants qu'ils testent, plus un suffixe `.spec`.

Allez-y et créez un fichier `test/unit/Rating.spec.js` :

```
// Rating.spec.js
```

```
import { shallowMount } from '@vue/test-utils'import Rating from '@/components/Rating'
```

```
describe('Rating', () => {  // vos tests vont ici})
```

Nous avons importé notre composant `Rating` et `shallowMount`. Ce dernier est une fonction Vue Test Utils qui nous permet de monter notre composant sans monter ses enfants.

L'appel de la fonction `describe` enveloppe tous les tests que nous allons écrire — il décrit notre **suite de tests**. Il a son propre scope et peut lui-même envelopper d'autres suites imbriquées.

Assez parlé, **commençons à écrire des tests**.

### Identification des scénarios de test

Lorsque nous regardons `Rating` de l'extérieur, nous pouvons voir qu'il fait ce qui suit :

* il rend une liste d'étoiles qui est égale à la valeur de la prop `maxStars` que l'utilisateur passe
* il ajoute une classe `active` à chaque étoile dont l'index est inférieur ou égal à la prop `stars` que l'utilisateur passe
* il bascule la classe `active` sur une étoile lorsque l'utilisateur clique dessus et la retire sur les étoiles suivantes
* il bascule les icônes `star` et `star-o` lorsque l'utilisateur clique sur une étoile
* il rend un compteur si l'utilisateur définit la prop `hasCounter` sur `true`, le cache s'ils la définissent sur `false`, et affiche un texte indiquant combien d'étoiles sur le nombre maximum d'étoiles sont actuellement actives.

Remarquez que nous ne regardons que ce que le composant fait de l'extérieur. Nous ne nous soucions pas que cliquer sur une étoile exécute la méthode `rate`, ou que la propriété de données interne `stars` change. Nous pourrions les renommer, mais cela ne devrait pas casser nos tests.

### Notre premier test

Écrivons notre premier test. Nous devons d'abord monter manuellement notre composant avec `shallowMount`, et le stocker dans une variable sur laquelle nous effectuerons des assertions. Nous pouvons également passer des props via l'attribut `propsData`, sous forme d'objet.

Le composant monté est un objet qui vient avec une poignée de méthodes utilitaires utiles :

```
describe('Rating', () => {  const wrapper = shallowMount(Rating, {    propsData: {      maxStars: 6,      grade: 3    }  })  it('rend une liste d'étoiles avec la classe `active` égale à prop.grade', () => {    // notre assertion va ici  })})
```

Ensuite, nous pouvons écrire notre première assertion :

```
it('rend une liste d'étoiles avec la classe `active` égale à prop.grade', () => {  expect(wrapper.findAll('.active').length).toEqual(3)})
```

Analysons ce qui se passe ici. Tout d'abord, nous utilisons la fonction `[expect](https://jestjs.io/docs/en/expect#expectvalue)` de Jest, qui prend la valeur que nous voulons tester comme argument. Dans notre cas, nous appelons la méthode `[findAll](https://vue-test-utils.vuejs.org/api/wrapper/#findall-selector)` sur notre `wrapper` pour récupérer tous les éléments avec une classe `active`. Cela retourne un `[WrapperArray](https://vue-test-utils.vuejs.org/api/wrapper-array/)`, qui est un objet contenant un tableau de `[Wrappers](https://vue-test-utils.vuejs.org/api/wrapper/)`.

Un `WrapperArray` a deux propriétés : `wrappers` (les `Wrappers` contenus) et `length` (le nombre de `Wrappers`). Cette dernière est ce dont nous avons besoin pour avoir le nombre attendu d'étoiles.

La fonction `expect` retourne également un objet sur lequel nous pouvons appeler des méthodes pour tester la valeur passée. Ces méthodes sont appelées **matchers**. Ici, nous utilisons le matcher `toEqual` et lui passons la valeur attendue en argument. La méthode retourne un booléen, qui est ce qu'un test attend pour réussir ou échouer.

Pour résumer, ici nous disons que nous attendons que le nombre total d'éléments avec la classe `active` que nous trouvons dans notre wrapper soit égal à 3 (la valeur que nous avons assignée à la prop `grade`).

Dans votre terminal, exécutez votre test :

```
npm run test:unit
```

Vous devriez le voir réussir ?

Il est temps d'en écrire davantage.

### Simulation de l'entrée utilisateur

Vue Test Utils facilite la simulation de ce que les utilisateurs finissent par faire en production. Dans notre cas, les utilisateurs peuvent cliquer sur des étoiles pour les basculer. Nous pouvons simuler cela dans nos tests avec la méthode `trigger`, et déclencher tous types d'événements.

```
it('ajoute la classe `active` sur une étoile inactive lorsque l'utilisateur clique dessus', () => {  const fourthStar = wrapper.findAll('.star').at(3)  fourthStar.trigger('click')  expect(fourthStar.classes()).toContain('active')})
```

Ici, nous obtenons d'abord notre quatrième étoile avec `findAll` et `[at](https://vue-test-utils.vuejs.org/api/wrapper-array/#at-index)`, qui retourne un `Wrapper` à partir d'un `WrapperArray` à l'index passé (numérotation basée sur zéro). Ensuite, nous simulons l'événement `click` sur celle-ci — nous imitions l'action d'un utilisateur qui cliquerait ou taperait sur la quatrième étoile.

Puisque nous avons défini la prop `grade` à 3, la quatrième étoile devrait être inactive avant que nous cliquions, donc l'événement de clic devrait la rendre active. Dans notre code, cela est représenté par une classe `active` que nous ajoutons aux étoiles uniquement lorsqu'elles sont activées. Nous la testons en appelant la méthode `[classes](https://vue-test-utils.vuejs.org/api/wrapper/#classes-classname)` sur l'étoile, qui retourne ses noms de classe sous forme de tableau de chaînes. Ensuite, nous utilisons le matcher `[toContain](https://jestjs.io/docs/en/expect#tocontainitem)` pour nous assurer que la classe `active` est présente.

#### Configuration et nettoyage

Puisque nous avons déclenché un clic sur notre composant, nous avons muté son état. Le problème est que nous utilisons ce même composant pour tous nos tests. Que se passe-t-il si nous changeons l'ordre de nos tests et déplaçons celui-ci en première position ? Alors le deuxième test échouerait.

Vous ne voulez pas dépendre de choses fragiles comme l'ordre lorsqu'il s'agit de tests. Une suite de tests doit être robuste, et les tests existants ne doivent idéalement pas changer sauf si vous cassez l'API.

Nous voulons nous assurer que nous avons toujours un wrapper prévisible pour effectuer des assertions. Nous pouvons y parvenir avec des fonctions de configuration et de nettoyage. Ce sont des helpers qui nous permettent d'initialiser des choses avant d'exécuter des tests, et de nettoyer ensuite.

Dans notre cas, une façon de faire serait de créer notre wrapper avant chaque test et de le détruire ensuite.

```
let wrapper = null
```

```
beforeEach(() => {  wrapper = shallowMount(Rating, {    propsData: {      maxStars: 6,      grade: 3    }  })})
```

```
afterEach(() => {  wrapper.destroy()})
```

```
describe('Rating', () => {  // nous supprimons l'expression `const wrapper = 20
6`  // 20
6})
```

Comme leurs noms le suggèrent, `[beforeEach](https://jestjs.io/docs/en/api#beforeeachfn-timeout)` et `[afterEach](https://jestjs.io/docs/en/api#aftereachfn-timeout)` s'exécutent avant et après chaque test, respectivement. De cette façon, nous pouvons être sûrs à 100 % que nous utilisons un wrapper frais chaque fois que nous exécutons un nouveau test.

### Identifiants spéciaux pour les tests

Il n'est jamais bon de mélanger les sélecteurs pour le style et d'autres fins, comme les hooks de test.

Et si vous changez le nom de la balise ou de la classe ?

Et si vous n'avez pas d'identifiant spécifique sur un élément que vous voulez tester, comme dans notre cas, le compteur ?

Vous ne voulez pas polluer votre code de production avec des classes qui y seraient inutiles. Il serait beaucoup mieux d'avoir des hooks dédiés pour les tests, comme un attribut de données dédié, **mais uniquement pendant les tests**. De cette façon, un désordre n'est pas laissé dans la version finale.

Une façon de gérer cela est de créer une [directive Vue personnalisée](https://vuejs.org/v2/guide/custom-directive.html).

L'instance Vue a une méthode `directive` qui prend deux arguments — un **nom**, et un **objet de fonctions** pour chaque [hook du cycle de vie du composant](https://vuejs.org/v2/guide/custom-directive.html#Hook-Functions) lorsqu'il est injecté dans le DOM. Vous pouvez également passer une seule fonction si vous ne vous souciez pas d'un hook spécifique.

Créons un nouveau répertoire appelé `directives` dans `src/`, et ajoutons un fichier `test.js`. Nous allons exporter la fonction que nous voulons passer dans notre directive.

```
// test.js
```

```
export default (el, binding) => {  // faire des choses}
```

Un hook de directive peut prendre [plusieurs arguments](https://vuejs.org/v2/guide/custom-directive.html#Directive-Hook-Arguments) et, dans notre cas, nous n'avons besoin que des deux premiers : `el` et `binding`. L'argument `el` fait référence à l'élément auquel la directive est liée. L'argument `binding` est un objet qui contient les données que nous avons passées dans la directive. De cette façon, nous pouvons manipuler l'élément comme nous le souhaitons.

```
export default (el, binding) => {  Object.keys(binding.value).forEach(value => {    el.setAttribute(`data-test-${value}`, binding.value[value])  })}
```

Nous passons un objet à notre directive, afin que nous puissions générer des attributs de données commençant par `data-test-`. Dans la fonction de gestion, nous itérons sur chaque propriété de `binding`, et nous définissons un attribut de données — basé sur le nom et la valeur — sur notre élément.

Maintenant, nous devons enregistrer notre directive afin de pouvoir l'utiliser. Nous pouvons le faire globalement mais, dans notre cas, nous allons l'enregistrer localement — directement dans notre composant `Rating.vue`.

```
<script>import Test from '@/directives/test.js'
```

```
export default {  // 20
6  directives: { Test },  // 20
6}</script>
```

Notre directive est maintenant accessible sous le nom `v-test`. Essayez de définir la directive suivante sur le compteur :

```
<span v-test="{ id: 'counter' }" v-if="hasCounter">  {{ stars }} of {{ maxStars }}</span>
```

Maintenant, inspectez le HTML dans votre navigateur avec les outils de développement. Votre compteur devrait ressembler à ceci :

```
<span data-test-id="counter">2 of 5</span>
```

Super, ça marche ! Maintenant, nous n'en avons pas besoin en mode développement ni lorsque nous construisons le projet. Le seul but de cet attribut de données est de pouvoir cibler des éléments pendant les tests, donc nous voulons le configurer uniquement lorsque nous les exécutons. Pour cela, nous pouvons utiliser la variable d'environnement `NODE_ENV` fournie par Webpack, le bundler de modules qui alimente notre projet.

Lorsque nous exécutons des tests, `NODE_ENV` est défini sur `'test'`. Par conséquent, nous pouvons l'utiliser pour déterminer quand définir les attributs de test ou non.

```
export default (el, binding) => {  if (process.env.NODE_ENV === 'test') {    Object.keys(binding.value).forEach(value => {      el.setAttribute(`data-test-${value}`, binding.value[value])    })  }}
```

Actualisez votre application dans le navigateur et inspectez à nouveau le compteur : **l'attribut de données a disparu**.

Maintenant, nous pouvons utiliser la directive `v-test` pour tous les éléments que nous devons cibler. Prenons notre test précédent :

```
it('ajoute la classe `active` sur une étoile inactive lorsque l'utilisateur clique dessus', () => {  const fourthStar = wrapper.findAll('[data-test-id="star"]').at(3)  fourthStar.trigger('click')  expect(fourthStar.classes()).toContain('active')})
```

Nous avons remplacé le sélecteur `.star` par `[data-test-id="star"]`, ce qui nous permet de changer les classes à des fins de présentation sans casser les tests. Nous obtenons l'un des avantages du [principe de responsabilité unique](https://en.wikipedia.org/wiki/Single_responsibility_principle) et du couplage lâche — lorsque vos abstractions n'ont qu'une seule raison de changer, vous évitez toutes sortes d'effets secondaires gênants.

### Devrions-nous également utiliser ces hooks pour les classes que nous testons ?

Après avoir défini cette directive pour cibler les éléments à tester, vous vous demandez peut-être si vous devriez également l'utiliser pour remplacer les classes que nous recherchons activement. Regardons l'assertion de notre premier test :

```
expect(wrapper.findAll('.active').length).toEqual(3)
```

Devrions-nous utiliser `v-test` sur les éléments avec la classe `active`, et remplacer le sélecteur dans l'assertion ? **Excellente question**.

Les tests unitaires consistent à tester une chose à la fois. Le premier argument de la fonction `it` est une chaîne, avec laquelle nous décrivons ce que nous faisons **du point de vue du consommateur**.

Le test qui enveloppe notre assertion dit `rend une liste d'étoiles avec la classe active égale à prop.grade`. C'est ce que le consommateur attend. Lorsqu'ils passent un nombre à la propriété `grade`, ils s'attendent à récupérer un **nombre égal** d'étoiles actives ou sélectionnées. Pourtant, dans la logique de notre composant, la classe `active` est précisément ce que nous utilisons pour définir ce trait. Nous l'assignons en fonction d'une condition spécifique, afin de différencier visuellement les étoiles actives des autres. Ici, la présence de cette classe spécifique est exactement ce que nous voulons tester.

Donc, lorsque vous décidez si vous devez utiliser un sélecteur que vous avez déjà ou définir une directive `v-test`, posez-vous la question : **que suis-je en train de tester, et l'utilisation de ce sélecteur a-t-elle du sens pour une perspective de logique métier ?**

### En quoi est-ce différent des tests fonctionnels ou de bout en bout ?

Au premier abord, il peut sembler étrange de tester unitairement des composants. Pourquoi tester unitairement l'UI et les interactions utilisateur ? N'est-ce pas le rôle des tests fonctionnels ?

Il y a une différence fondamentale mais subtile à faire entre tester l'API publique d'un composant — aka du point de vue du **consommateur** — et tester un composant du point de vue de l'**utilisateur**. Tout d'abord, soulignons quelque chose d'important : **nous testons des fonctions JavaScript bien définies, pas des morceaux d'UI**.

Lorsque vous regardez un composant à fichier unique, il est facile d'oublier que le composant se compile en une fonction JavaScript. Nous ne testons pas le mécanisme sous-jacent de Vue qui, à partir de cette fonction, provoque des effets secondaires orientés UI comme l'injection de HTML dans le DOM. C'est ce que les tests propres à Vue prennent déjà en charge. Dans notre cas, notre composant n'est pas différent de toute autre fonction : **il accepte une entrée et retourne une sortie**. Ces causes et conséquences sont ce que nous testons, et rien d'autre.

Ce qui est déroutant, c'est que nos tests semblent un peu différents des tests unitaires réguliers. Habituellement, nous écrivons des choses comme :

```
expect(add(3)(4)).toEqual(7)
```

Il n'y a pas de débat ici. Entrée et sortie de données, c'est tout ce qui nous importe. Avec les composants, nous nous attendons à ce que les choses se rendent visuellement. Nous parcourons un DOM virtuel et testons la présence de nœuds. C'est aussi ce que vous faites avec des tests fonctionnels ou de bout en bout, avec des outils comme [Selenium](https://www.seleniumhq.org/) ou [Cypress.io](https://www.cypress.io/). Alors, en quoi cela diffère-t-il ?

Vous ne devez pas confondre **ce** que nous faisons pour récupérer les données que nous voulons tester et le **but** réel du test. **Avec les tests unitaires, nous testons des comportements isolés. Avec les tests fonctionnels ou de bout en bout, nous testons des scénarios**.

Un test unitaire s'assure qu'une **unité** du programme se comporte comme prévu. Il s'adresse au **consommateur** du composant — le programmeur qui utilise le composant dans son logiciel. Un test fonctionnel garantit qu'une **fonctionnalité** ou un **flux de travail** se comporte comme prévu, du point de vue de l'**utilisateur** — l'utilisateur final, qui consomme le logiciel complet.

### Aller plus loin

Je ne vais pas entrer dans le détail de chaque test, car ils partagent tous une structure similaire. Vous pouvez trouver le [fichier de spécification complet sur GitHub](https://github.com/sarahdayan/star-rating-vue-js-tutorial/blob/tests/tests/unit/Rating.spec.js), et je vous recommande fortement d'essayer de les implémenter vous-même d'abord. Les tests logiciels sont un art autant qu'une science, et nécessitent deux fois plus de pratique que de théorie.

Ne vous inquiétez pas si vous n'avez pas tout compris, ou si vous avez du mal à écrire vos premiers tests : **les tests sont notoirement difficiles**. De plus, si vous avez une question, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/frontstuff_io) !

Publié à l'origine sur [frontstuff.io](https://frontstuff.io/unit-test-your-first-vuejs-component).