---
title: Comment tester vos applications Vue.js en moins de sept minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T16:15:41.000Z'
originalURL: https://freecodecamp.org/news/testing-vue-js-applications-vue-test-utils-39ec26ddaa4e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PkFvOQVwXsa-Rsd004WyDQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: Vue.js
  slug: vuejs
seo_title: Comment tester vos applications Vue.js en moins de sept minutes
seo_desc: 'By Mukul Khanna

  Before we dive into the implementation, let’s get a few concepts cleared.

  What is testing?

  Manually trying all possible inputs to a basic form validator can be cumbersome.

  It might not seem like a big deal for a small website. But for...'
---

Par Mukul Khanna

Avant de plonger dans l'implémentation, clarifions quelques concepts.

### Qu'est-ce que le test ?

Essayer manuellement toutes les entrées possibles pour un validateur de formulaire de base peut être fastidieux.

Cela peut ne pas sembler un gros problème pour un petit site web. Mais pour des applications web plus grandes et plus complexes composées de dizaines de composants avec leurs fonctions, routes, états, mutations et ainsi de suite, il n'est pas faisable ou conseillé de tester le fonctionnement de tous ces constituants.

Automatiser cette partie des évaluations basées sur des essais et erreurs du code que nous avons écrit est connu sous le nom de **test** ou **test automatisé**.

Edd Yerburgh, membre de l'équipe principale de Vue et mainteneur de vue-test-utils (anciennement **Avoriaz**), définit le test automatisé dans son [livre](https://livebook.manning.com#!/book/testing-vuejs-applications/chapter-1/v-3/point-1371-28-28-0) comme :

> Le test automatisé est la pratique d'écrire des programmes pour exécuter des tests contre le code de votre application. Une fois les programmes écrits, ils peuvent être exécutés automatiquement.

Il existe essentiellement trois types de tests :

1. Tests unitaires
2. Tests de bout en bout
3. Tests de snapshot

#### **Tests unitaires**

Ce sont des tests de base qui vérifient si les éléments atomiques du site web (composants Vue et fonctions) fonctionnent correctement. Edd les appelle **contrats de composants**. Chaque composant est censé fonctionner comme il l'a promis, et ces tests s'assurent qu'ils sont respectés.

#### **Tests de bout en bout (E2E)**

Les tests E2E testent l'ensemble du flux de travail du site web. On peut dire qu'un test E2E est composé de plusieurs tests unitaires granulaires. Ils sont lents, mais ils vérifient l'ensemble de la fonctionnalité du site web.

Mais ils sont également difficiles à déboguer car il est difficile de localiser les parties qui n'ont pas fonctionné comme elles auraient dû. Il pourrait y avoir plus d'une raison pour laquelle les tests ont échoué.

#### Tests de snapshot

Les bugs dans le code n'affectent pas seulement la fonctionnalité du site web, mais aussi le positionnement des composants dans l'UI. Les tests de snapshot vérifient ces changements dans l'apparence de l'application. Cela implique de rendre l'UI, de capturer une capture d'écran et de la comparer à une image de référence stockée avec le test. Le test échoue si les deux images ne correspondent pas.

![Image](https://cdn-media-1.freecodecamp.org/images/r2Gl95lvS3RrdUTyl5B-zZnYBDHzhDSyZyA1)
_[La pyramide des tests](https://livebook.manning.com/#!/book/testing-vuejs-applications/chapter-1/v-3/156" rel="noopener" target="_blank" title=")_

Ces tests aident également les développeurs à écrire une documentation appropriée du code, ce qui est assez utile dans les applications à grande échelle avec plusieurs contributeurs.

Maintenant que nous avons établi que le test peut nous aider à gagner beaucoup de temps et à optimiser notre code, voyons comment les tests sont configurés, créés et exécutés.

Nous utiliserons **vue-test-utils** comme bibliothèque d'utilitaires de test pour Vue.js. Maintenant, nous devons également choisir un exécutant de test. Il y en a beaucoup parmi lesquels choisir, mais Jest et Mocha-Webpack sont tous deux également bons. Ils ont simplement quelques compromis entre la configuration initiale et le support pour les SFC (composants à fichier unique).

Nous utiliserons la configuration **mocha-webpack** pour cette démonstration.

### **Création du projet**

```
npm install vue
```

```
npm install --global vue-cli
```

```
vue init webpack vue-testing
```

```
cd vue-testing
```

```
npm install
```

```
npm run dev 
```

En utilisant les commandes ci-dessus, créez un projet Vue webpack dans lequel nous allons configurer l'environnement de test.

![Image](https://cdn-media-1.freecodecamp.org/images/PgscjiR-rzsjW-igS5mBhwBcLJgSR4x25KL1)

#### **Installation des dépendances**

Pour installer [vue-test-utils](https://github.com/vuejs/vue-test-utils), mocha et mocha-webpack :

```
npm install --save-dev @vue/test-utils
```

```
npm install --save-dev mocha mocha-webpack
```

Pour émuler un sous-ensemble d'un environnement de navigateur pour exécuter nos tests, nous installerons [jsdom](https://github.com/jsdom/jsdom) et [jsdom-globa](https://github.com/rstacruz/jsdom-global)l :

```
npm install --save-dev jsdom jsdom-global
```

Certaines des dépendances que nous allons importer dans nos tests sont difficiles pour webpack à bundler. Donc, pour pouvoir les supprimer du processus de bundling et pour augmenter la vitesse de démarrage des tests, nous installons **node-externals** :

```
npm install --save-dev webpack-node-externals
```

Vue recommande [expect](https://github.com/Automattic/expect.js) comme bibliothèque d'assertion qui décide essentiellement si le test échoue ou réussit en fonction de l'argument qu'il reçoit.

```
npm install --save-dev expect
```

Nous devons le rendre globalement accessible pour éviter de l'importer dans chaque test. Nous créons un répertoire nommé **test** dans le répertoire racine et créons un fichier nommé **test/setup.js**. Importez les modules avec **require** :

```
//setup.js
```

```
require('jsdom-global')()
```

```
global.expect = require('expect')
```

Nous pouvons également inclure la couverture de code dans les résultats des tests en utilisant le plugin **istanbul** pour obtenir un rapport comme celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/RJll7uceQ3TW8cMj9piJI0Lk7-JTh8hdKxvX)

Il est utilisé pour décrire le degré auquel le code source d'une application est exécuté lorsqu'une suite de tests particulière s'exécute.

```
npm install --save-dev nyc babel-plugin-istanbul
```

Également dans le **.babelrc** dans le tableau **plugins**, ajoutez **istanbul** :

```
//.babelrc
```

```
plugins": ["transform-vue-jsx", "transform-runtime", "istanbul"]
```

Nous avons donc installé toutes les dépendances, et il est temps de faire les configurations finales avant de pouvoir commencer à écrire les tests.

Dans **package.json**, nous devons ajouter un script **test** qui exécute le test :

```
//package.json
```

```
"scripts":{
```

```
"test": "cross-env NODE_ENV=test nyc mocha-webpack --webpack-config build/webpack.base.conf.js --require test/setup.js test/**/*.spec.js"
```

```
}
```

Nous devons également spécifier les fichiers qui doivent être inclus pour la couverture de code dans le **package.json** :

```
//package.json
```

```
"nyc":{    "include":[      "src/**/*.(js|vue)" ],    "instrument":false,    "sourceMap":false}
```

La dernière configuration avant d'écrire le test serait d'ajouter ce qui suit dans **webpack.base.conf.js** :

```
//webpack.base.conf.js
```

```
if (process.env.NODE_ENV === 'test'){  module.exports.externals = [require('webpack-node-externals')()]  module.exports.devtool = 'inline-cheap-module-source-map'}
```

Nous pouvons effectuer notre test sur le composant Vue intégré qui vient avec le boilerplate webpack.

Chaque fichier de test aura une extension **'spec.js'**.

Dans le répertoire de test, nous ajoutons un fichier de test **testOne.spec.js**

```
//testOne.spec.js
```

```
import {shallow} from '@vue/test-utils'
```

```
import HelloWorld from '../src/components/HelloWorld.vue'
```

Nous commençons par importer **shallow** depuis **vue-test-utils**. **Shallow** crée un [wrapper](https://vue-test-utils.vuejs.org/en/api/wrapper/) pour le composant Vue sur lequel nous voulons exécuter le test. Ce wrapper est un objet qui contient le composant monté et des méthodes pour tester des parties du code. Ensuite, nous importons le composant Vue sur lequel nous exécutons le test.

```
//testOne.spec.js
```

```
describe('HelloWorld.vue',function(){        it('Vérification du texte de la balise <h2>',function(){                const wrapper = shallow(HelloWorld)        const h2= wrapper.find('h2')        expect(h2.text()).toBe('Essential Links')        })})
```

Ensuite, nous créons ce que nous pouvons appeler une **suite de tests**, en utilisant la méthode **describe()** du framework de test de Mocha. Cette suite de tests regroupe essentiellement plusieurs cas de test en un seul tout en fournissant quelques informations sur les tests et le composant.

Dans cette fonction describe, nous rappelons une fonction qui spécifie les cas de test en utilisant la fonction **it()**. Chaque méthode it() décrit un cas de test avec le but du test comme premier paramètre suivi d'une fonction de rappel définissant le test.

Ensuite :

* Nous créons un wrapper du composant Vue
* Utilisons sa méthode **find()** pour obtenir tous les éléments de la balise <h2>
* Comparons son texte avec ce qu'il est censé être.

Hourra ! Notre test est prêt à être exécuté.

```
npm run test
```

![Image](https://cdn-media-1.freecodecamp.org/images/U2cWkbO4QNdUel3SyeDq8zTLzjYH0Xco0saV)

Donc, notre test a réussi — le code a pu trouver une balise <h2> dans le composant HelloWorld.vue avec 'Essential Links' comme texte.

Maintenant, si nous changeons le test attendu en autre chose, le test échouera.   
Je l'ai changé en :

```
expect(h2.text()).toBe('Essential Linx')
```

et le test échoue. L'erreur de test échoué est assez descriptive, cependant, et vous pouvez voir ce que le code attendait et ce qu'il reçoit :

![Image](https://cdn-media-1.freecodecamp.org/images/y1-YwOLTgYsJbbC8IxZ8ukWdaBsYf8xPdgaT)

Nous pouvons ajouter plusieurs cas de test dans un seul fichier de test en utilisant plusieurs méthodes **it()** et en attendant différentes conditions.

```
describe('HelloWorld.vue',function(){    
```

```
it('Vérification du texte de la balise <h2>',function(){        const wrapper = shallow(HelloWorld)                const h2 = wrapper.find('h2')        expect(h2.text()).toBe('Essential Links')        }),    
```

```
it('Vérification du texte de la balise <h1>',function(){        const wrapper = shallow(HelloWorld)        const h1 = wrapper.find('h1')        expect(h1.text()).toBe('Welcome to Your Vue.js App')        })
```

```
})
```

Ici, nous testons également si la balise <h1> rend ce qu'elle est censée rendre.

Donc, c'était un test assez basique qui vous donne juste une compréhension de la façon dont les tests sont configurés, codés et exécutés sans même ouvrir le navigateur ou démarrer le serveur.

Le lien vers le dépôt GitHub est [ici](https://github.com/mukulkhanna/vue-testing).

### Conclusion

Le livre d'Edd Yerburgh 'Testing Vue.js Applications' m'a beaucoup aidé à obtenir une vision plus large de l'importance des tests et de la façon de les implémenter. Je le recommande à quiconque veut apprendre les tests au-delà du contenu de niveau débutant et vraiment plonger dedans.

Autre que cela, j'ai passé quelque temps sur les concepts de TDD (Test Driven Development) et j'ai hâte d'écrire un tutoriel pour débutants sur le monde du TDD avec Vue.js.

Veuillez laisser un ou deux applaudissements si vous avez aimé l'article. Merci :)