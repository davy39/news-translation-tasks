---
title: La manière facile de commencer à tester automatiquement votre site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T17:31:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-start-automatically-testing-your-website-8629ea8df04a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pCkwM6MSt-hyDEDaAifufg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La manière facile de commencer à tester automatiquement votre site web
seo_desc: 'By Adam Kelly

  Manually running the same tests on Chrome, Safari, and Firefox multiple times can
  be time-consuming and tedious.

  Some testing tasks can be automated to handle these tasks more efficiently. This
  article will cover what sorts of tests can...'
---

Par Adam Kelly

Exécuter manuellement les mêmes tests sur Chrome, Safari et Firefox plusieurs fois peut être chronophage et fastidieux.

Certaines tâches de test peuvent être automatisées pour gérer ces tâches plus efficacement. Cet article couvrira les types de tests qui peuvent être automatisés et comment vous pouvez les implémenter en utilisant Node.js et Nightwatch.

Nightwatch se connecte à un WebDriver (tel que Selenium). Il fonctionne via une API REST. Par exemple, l'initialisation est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VU8YPJRqwqwcxywKFP4KuA.png)
_Comment Nightwatch se connecte à Selenium_

### Prérequis

Vous devez avoir Java installé. Vous pouvez vérifier cela en exécutant

```
$ java -version
```

dans votre terminal. Si vous ne l'avez pas installé, allez [l'installer](https://www.java.com/en/download/help/download_options.xml).

Vous devez avoir une version assez récente de Safari, version 10 ou ultérieure. Pour utiliser Safari, vous devez également activer le menu développeur et activer l'option **Autoriser l'automatisation à distance**.

Enfin, vous devez également avoir [Node.js](https://nodejs.org/en/).

### Installation

> Note : Cela suppose que le site utilise déjà node.js. Si ce n'est pas le cas, vous devriez également l'initialiser avec un fichier `_package.json_`.

#### Installation

[**Nightwatch.js**](http://nightwatchjs.org/) est une manière plus facile d'écrire des tests que de les exécuter en utilisant Selenium.

Pour l'installer, `cd` dans votre projet, puis installez le module depuis npm dans vos dépendances de développement :

```
$ npm install --save-dev nightwatch
```

Maintenant, vous devez installer Selenium. La manière la plus facile de le faire est avec un autre module npm, `selenium-server` :

```
$ npm install --save-dev selenium-server
```

Nous voulons tester sur Chrome, Safari et Firefox, donc nous devons également installer leurs drivers. Le driver est ce qui est utilisé par Selenium pour contrôler les navigateurs. Le driver de Safari est intégré à MacOS, et les drivers de Chrome et Firefox peuvent être installés en utilisant npm :

```
$ npm install --save-dev chromedriver geckodriver
```

#### Configuration

Nightwatch est configuré en utilisant un fichier de configuration. Le fichier de configuration est un fichier JavaScript normal, que j'appellerai `nightwatch.conf.js`. Ce fichier peut être placé dans un dossier, tel que `tests`.

Copiez et collez cette configuration de base dans votre fichier `nightwatch.conf.js` :

Maintenant, vous avez votre framework de test automatisé configuré et vous êtes en mesure de commencer à écrire des tests !

### Que Pouvez/Devez-Vous Tester ?

Il existe deux types de tests que vous pouvez effectuer avec cette configuration :

1. Tests fonctionnels
2. Tests de régression

Les tests fonctionnels sont le type de tests qui tentent de voir si votre site web est conforme à toutes ses exigences. Habituellement, cela signifie implémenter des tests qui s'assurent qu'il possède toutes les fonctionnalités requises.

Par exemple, si le client veut un formulaire de connexion, vous pourriez écrire un test pour vérifier que lorsque vous êtes connecté, votre nom est visible sur la page web.

L'autre type de test est le test de régression. Cela est fait pour s'assurer que le site web que vous avez développé et testé auparavant fonctionne toujours de la même manière après avoir été modifié. Cela est particulièrement utile lorsque les clients peuvent modifier des parties de leur site web qui pourraient potentiellement causer des erreurs de fonctionnalité.

Par exemple, vous pourriez écrire un test pour vous assurer qu'une page a les bonnes balises meta et informations.

Une limitation à ce framework de test est qu'il teste le site web, pas le code. Par exemple, il ne peut pas tester qu'une requête DB a été faite, mais il pourrait tester qu'il y a une nouvelle ligne créée à partir de cette requête.

Cependant, vous pourriez utiliser d'autres frameworks de test unitaire en parallèle (tels que [Jest](https://facebook.github.io/jest/), [Mocha](https://mochajs.org/), et [Ava](https://github.com/avajs/ava)), pour tester votre logique et votre code de base.

### Écriture des Tests

Bienvenue dans la partie amusante des tests. Ah, je plaisante. **C'est tout amusant**.

En tout cas, les tests dans Nightwatch sont écrits en utilisant un module JavaScript normal. Dans le fichier `nightwatch.conf.js`, nous avons spécifié de chercher dans `tests/features` pour les tests.

Nightwatch prendra ce dossier et cherchera tous les fichiers JavaScript qu'il contient, puis essaiera de les exécuter en tant que tests.

Créons un test vraiment simple : nous testerons que le titre de [www.bing.com](http://www.bing.com) est `Bing`. Pourquoi vous iriez sur Bing en premier lieu est une question plus grande qui ne peut pas être abordée dans cet article.

Créez un nouveau fichier dans `tests/features` appelé `bing.test.js`, contenant le code suivant :

Maintenant, le test est créé !

Ici, `Title is Bing` est le nom du test. Cela est affiché lorsque les tests sont exécutés. `.verify` est utilisé pour effectuer réellement un test. `.waitForElementVisable` attend un sélecteur CSS ou un sélecteur Xpath pour spécifier les éléments auxquels vous faites référence.

Vous pouvez avoir plus d'un test dans le même fichier, et il est bon de garder les tests liés dans le même fichier.

Pour plus d'informations sur la création de tests, la documentation de Nightwatch est vraiment bonne. Si vous voulez savoir comment faire quelque chose, consultez [ceci](http://nightwatchjs.org/guide/#using-nightwatch) en premier. Consultez également la section "Above and Beyond" de ce guide.

### Exécution des Tests

Pour exécuter les tests que vous avez maintenant, allez dans le fichier `package.json`. Ajoutez ce qui suit :

```
"scripts": {  "nightwatch": "nightwatch -c tests/nightwatch.conf.js -e chrome,firefox,safari"}
```

Cela exécutera vos tests avec Chrome, Firefox et Safari.

Pour exécuter votre test, dans votre terminal, faites la commande :

```
$ npm run nightwatch
```

Si vous avez toujours le même test que ci-dessus, votre sortie devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*osMTcdZ_LyV0LXFqem2d6A.png)
_Sortie de la suite de tests_

Si vous obtenez des erreurs, consultez la section `Problèmes Courants` de cet article, ou recherchez l'erreur sur Google.

Et **voilà**, vous avez maintenant configuré et utilisé des tests de navigateur automatisés ! ?

### Au-delà

#### Bonnes Pratiques et Guides Plus Approfondis

Il existe de nombreuses bonnes ressources, mais voici quelques-unes de mes préférées :

* UI Testing with Nightwatch.js — Page Objects | [http://matthewroach.me/ui-testing-with-nightwatch-js-page-objects/](http://matthewroach.me/ui-testing-with-nightwatch-js-page-objects/)
* Writing UI Tests For TodoMVC APP | [https://blog.cloudboost.io/e2e-testing-with-nightwatch-part-two-aaa25a4dc033](https://blog.cloudboost.io/e2e-testing-with-nightwatch-part-two-aaa25a4dc033)
* Understanding the Command Queue | [https://github.com/nightwatchjs/nightwatch/wiki/Understanding-the-Command-Queue](https://github.com/nightwatchjs/nightwatch/wiki/Understanding-the-Command-Queue)
* Page Object API | [https://github.com/nightwatchjs/nightwatch/wiki/Page-Object-API](https://github.com/nightwatchjs/nightwatch/wiki/Page-Object-API)
* Nightwatch API | [http://nightwatchjs.org/api](http://nightwatchjs.org/api)
* Nightwatch.js Gotchas | [https://ericheikes.com/nightwatch-js-gotchas/](https://ericheikes.com/nightwatch-js-gotchas/)
* Nightwatch how to assert multiple elements | [https://stackoverflow.com/questions/27116103/nightwatch-js-how-to-assert-multiple-elements?rq=1](https://stackoverflow.com/questions/27116103/nightwatch-js-how-to-assert-multiple-elements?rq=1)

#### Testing With Edge Browser

Vous pouvez tester avec Edge en utilisant le [Microsoft WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Il est compatible avec Windows 10 et versions ultérieures.

Après avoir téléchargé le binaire, allez dans votre fichier `nightwatch.conf.js` et sous `"webdriver.gecko.driver"` mettez

```
"webdriver.edge.driver" : "location/of/binary/MicrosoftWebDriver.exe"
```

Ensuite, allez dans `test_settings` et ajoutez un autre objet sous `safari` :

```
edge: {  desiredCapabilities: {    browserName: 'MicrosoftEdge',    javascriptEnabled: true,    acceptSslCerts: true,    nativeEvents: true  }}
```

Enfin, allez dans votre `package.json` et changez le script `nightwatch` en :

```
"nightwatch": "nightwatch -c tests/nightwatch.conf.js -e chrome,firefox,safari,edge"
```

#### Utilisation avec CI

Cela dépasse le cadre de cet article, mais vous pouvez consulter :

* [https://github.com/dwyl/learn-nightwatch/issues/8](https://github.com/dwyl/learn-nightwatch/issues/8)
* Utilisation de Meteor, Travis CI et Nightwatch [https://github.com/zeroasterisk/meteor-travis-ci-nightwatch](https://github.com/zeroasterisk/meteor-travis-ci-nightwatch)
* Intégration de Selenium avec Jenkins [http://learn-automation.com/selenium-integration-with-jenkins/](http://learn-automation.com/selenium-integration-with-jenkins/)

### Problèmes Courants

#### Nightwatch Ne Trouve Pas Selenium

Si Nightwatch ne trouve pas Selenium, essayez d'exécuter votre fichier de configuration avec node. Si votre fichier de configuration, `nightwatch.conf.js` est dans le répertoire `tests`, exécutez :

```
$ node tests/nightwatch.conf.js
```

#### Popups Safari

Safari pourrait vous avertir qu'il est contrôlé. Autorisez-le simplement. Si le test a échoué ou a expiré, relancez-le.

#### Safari Ne Se Ferme Pas

Fermez-le simplement manuellement.

#### Pour afficher ce contenu web, vous devez installer l'environnement d'exécution Java

Je vous ai dit que vous deviez installer Java, alors allez [l'installer](https://www.java.com/en/download/help/download_options.xml).

#### ERREUR — Le port 4444 est occupé, veuillez choisir un port libre et le spécifier en utilisant l'option -port

Cela signifie que quelque chose utilise le port 4444. Vous pouvez soit arrêter ce processus, soit changer de port.

Pour voir quel processus utilise le port sur Mac, utilisez la commande

```
$ lsof -n -i4TCP:4444 | grep LISTEN
```

Vous pouvez ensuite tuer ce processus.

Si vous ne voulez pas tuer ce processus, allez dans le fichier `nightwatch.conf.js` et dans `selenium`, changez `port` pour un port inutilisé.