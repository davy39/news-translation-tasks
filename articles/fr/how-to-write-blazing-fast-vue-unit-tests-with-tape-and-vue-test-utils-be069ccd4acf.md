---
title: Écrivez des tests unitaires ultra-rapides pour Vue avec Tape et Vue Test Utils
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T19:59:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-blazing-fast-vue-unit-tests-with-tape-and-vue-test-utils-be069ccd4acf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XgAqbm90jYFUxWA-8Z0zOw.png
tags:
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Écrivez des tests unitaires ultra-rapides pour Vue avec Tape et Vue Test
  Utils
seo_desc: 'By Edd Yerburgh

  Tape is the fastest framework for unit testing Vue components.

  In this article, we’ll see how to write Vue unit tests with Tape and Vue Test Utils.

  This tutorial is for users familiar with unit testing. If you’re new to unit testing
  c...'
---

Par Edd Yerburgh

Tape est le framework le plus rapide pour les [tests unitaires](https://github.com/eddyerburgh/vue-unit-test-perf-comparison) des composants Vue.

Dans cet article, nous verrons comment écrire des tests unitaires Vue avec Tape et Vue Test Utils.

Ce tutoriel s'adresse aux utilisateurs familiarisés avec les tests unitaires. Si vous débutez dans les tests unitaires, consultez [les tests unitaires des composants Vue](https://eddyerburgh.me/unit-test-vue-components-beginners) pour débutants.

### Qu'est-ce que Tape ?

Tape est un framework de test unitaire minimaliste qui génère le rapport de test au format [TAP](https://testanything.org/) (Test Anything Protocol).

Il dispose d'une API simple pour vérifier que votre JavaScript et vos composants Vue se comportent correctement.

### Pourquoi Tape ?

Il y a quelques semaines, j'ai effectué des tests de performance sur différents frameworks de test. Je voulais découvrir quel framework était le plus rapide pour tester les SFC Vue (Single File Components).

J'ai ajouté Tape pour être complet, et j'ai été surpris de constater qu'il était le framework le plus performant.

Pour exécuter des tests avec Tape, nous devons faire quelques configurations. Plongeons-nous directement dans le sujet.

### Initialisation du projet

J'ai créé un projet de démarrage simple pour commencer. Clonez le projet dans un répertoire :

```
git clone https://github.com/eddyerburgh/jest-vue-starter.git
```

Accédez-y et installez les dépendances :

```
cd jest-vue-starter && npm install
```

Lancez le serveur de développement avec `npm run dev` pour découvrir l'application.

C'est assez simple. Le principal objectif de ce tutoriel est de voir comment configurer Tape et Vue, et non d'écrire des tests complexes.

### Configuration de Tape et Vue Test Utils

La première chose à faire est d'installer Tape et Vue Test Utils :

```
npm install --save-dev tape @vue/test-utils
```

**Vue Test Utils est en version bêta, nous devons donc spécifier explicitement la version**

Vue Test Utils nécessite un environnement de navigateur pour s'exécuter. Cela ne signifie pas que nous devons exécuter les tests dans un navigateur (heureusement !).

Nous pouvons utiliser jsdom pour configurer un environnement de navigateur dans Node. Il ajoute des variables globales comme `document` et `window` à Node.

jsdom est un peu difficile à configurer. Heureusement, un développeur Node entreprenant a créé une bibliothèque wrapper appelée `browser-env`.

```
npm install --save-dev browser-env
```

Nous devons exécuter `browser-env` avant les tests. Tape nous permet de définir des fichiers à exécuter avant les tests, nous le ferons dans un instant.

Les SFC Vue doivent être compilés avant d'être testés. Nous pouvons utiliser `**require-hooks**` pour exécuter WebPack sur les fichiers lorsqu'ils sont requis dans Node. C'est une configuration simple.

Tout d'abord, installez `require-extension-hooks` et ses variantes :

```
npm install --save-dev require-extension-hooks require-extension-hooks-babel require-extension-hooks-vue
```

Créons ce fichier de configuration dont j'ai parlé plus tôt. Créez un répertoire `test`, et ajoutez un fichier `setup.js`. Le chemin final sera `test/setup.js`.

Nous y sommes presque. C'est du lourd.

Écrivons un test de base avec Tape. Créez un nouveau fichier appelé `List.spec.js` dans le répertoire de test. Chemin complet `test/List.spec.js`. Copiez le test ci-dessous dans le fichier :

Qu'est-ce qui se passe là ? Nous définissons un `test`, et obtenons un objet `t` dans le callback. L'objet `t` contient des méthodes d'assertion. Il a également une méthode `plan`. Nous devons indiquer à Tape combien de tests il doit attendre.

Maintenant, nous avons besoin d'un script pour exécuter les tests. Ouvrez le `package.json` et ajoutez ce script :

```
"unit": "tape ./test/specs/*.spec.js -r ./test/setup.js"
```

Cela indique à Tape d'exécuter tous les fichiers `.spec` dans `test/specs`. Le `-r` indique à Tape de `require` ou d'exécuter `test/setup` avant d'exécuter nos tests.

Exécutez les tests `unit` :

```
npm run unit
```

Hourra, nous avons un test qui passe. Mais oh là là—c'est une sortie de test assez moche ☁️

Vous vous souvenez que j'ai mentionné TAP plus tôt ? C'est TAP dans toute sa gloire nue. Plutôt moche, n'est-ce pas ? Ne vous inquiétez pas, nous pouvons l'embellir.

Installez `tap-spec` :

```
npm install --save-dev tap-spec
```

Nous pouvons rediriger notre sortie TAP de Tape. Modifiez le script `unit` pour rediriger la sortie vers `tap-spec` :

```
"unit": "tape ./test/specs/*.spec.js -r ./test/setup.js | tap-spec"
```

Et exécutez les tests à nouveau :

```
npm run unit
```

Beaucoup mieux ?

### Écriture de tests avec Tape et Vue Test Utils

Écrivons quelques tests alors. Puisque nous utilisons Vue Test Utils, les tests sont assez lisibles.

Dans `List.spec.js`, nous allons écrire un `test` qui passe un tableau `items` à `List`. Nous utiliserons la méthode `[shallow](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/shallow.md)` de Vue Test Utils pour monter le composant de manière superficielle. `shallow` retourne un `wrapper` contenant le composant monté. Nous pouvons utiliser `[findAll](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/wrapper/findAll.md)` pour rechercher les balises `<li>` dans l'arbre de rendu et vérifier combien il y en a.

Copiez le test ci-dessous dans `test/specs/List.spec.js`.

Regardez les tests passer avec `npm run unit`. Remarquez que nous avons un message d'erreur personnalisé pour notre assertion `t.equals`. Les messages par défaut ne sont pas très lisibles, il est donc préférable d'ajouter les nôtres.

Ajoutez maintenant un nouveau fichier `test/specs/MessageToggle.spec.js`. Ici, nous écrivons un test pour, vous l'aurez deviné, `MessageToggle.vue`.

Nous allons écrire deux tests maintenant. L'un vérifiera que la balise `<p>` rend un message par défaut. Nous utiliserons à nouveau `shallow` pour obtenir un wrapper contenant le composant monté, et la méthode `text` pour retourner le texte à l'intérieur de la balise `<p>`.

Le deuxième test est similaire. Nous vérifierons que le message change lorsque le bouton `toggle-message` est pressé. Pour cela, nous pouvons utiliser la méthode `[trigger](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/wrapper/trigger.md)`.

Copiez le code ci-dessous dans `test/specs/MessageToggle.spec.js` :

Exécutez les tests à nouveau avec `npm run unit`. Hourra—des tests verts ?

### Avantages et inconvénients de Tape

Maintenant que nous avons ajouté quelques tests, examinons les avantages et inconvénients de l'utilisation de Tape.

#### Avantages

* **C'est rapide**
 Vraiment très rapide ?
* **C'est simple**
 Vous pouvez lire le code source pour comprendre
* **Il utilise TAP**.
 Puisque TAP est un standard, il existe de nombreux programmes qui fonctionnent directement avec TAP
 Comme le module tap-spec, nous avons simplement redirigé du texte TAP vers lui et il l'a embelli pour nous
* **Assertions limitées**
 Des assertions limitées rendent vos assertions faciles à comprendre

#### Inconvénients

* **Assertions limitées**
 C'est aussi un inconvénient
 Vous pouvez obtenir des messages d'erreur utiles avec des assertions comme `hasBeenCalledWith`, cela est difficile à reproduire avec `t.equal`
* [Il plante](https://github.com/substack/tape/issues/389)
 Lorsque vous exécutez plus de 10000 tests
 Vous ne rencontrerez probablement pas ce problème. Mais cela pourrait être un critère d'exclusion pour un grand projet Vue
* **C'est basique**
 Vous devrez utiliser d'autres bibliothèques pour le mocking, le stubbing et le faking

Les avantages et inconvénients sont assez similaires. Tape est basique, et cela peut être une bonne ou une mauvaise chose selon à qui vous demandez.

Mais surtout, il est ultra-rapide !

Des tests unitaires rapides sont de bons tests unitaires.

### Appel à l'action

La meilleure façon de comprendre un nouveau framework de test est de l'utiliser.

Lors de votre prochain projet Vue, essayez Tape. Vous pouvez trouver une liste d'assertions dans le [README](https://github.com/substack/tape/) de Tape.

Amusez-vous ?

Vous pouvez trouver [le dépôt finalisé](https://github.com/eddyerburgh/tape-vue-example) sur GitHub.