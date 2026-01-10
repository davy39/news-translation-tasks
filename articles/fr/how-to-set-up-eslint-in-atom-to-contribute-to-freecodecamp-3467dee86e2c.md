---
title: Comment configurer ESLint dans Atom pour contribuer à l'Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-05T15:44:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-eslint-in-atom-to-contribute-to-freecodecamp-3467dee86e2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9VCSFevPWwOvEfQV8HqnOg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment configurer ESLint dans Atom pour contribuer à l'Open Source
seo_desc: 'By Steven Gilbert

  If you want to contribute to open source projects like freeCodeCamp, first you’ll
  need to set up linting.

  Most projects have their own style standards for JavaScript, and these will be automatically
  enforced by linting tools like ES...'
---

Par Steven Gilbert

Si vous souhaitez contribuer à des projets open source comme freeCodeCamp, vous devrez d'abord configurer le linting.

La plupart des projets ont leurs propres normes de style pour JavaScript, et celles-ci seront automatiquement appliquées par des outils de linting comme [**ESLint**](http://eslint.org/)**.**

Configurons ESLint pour qu'il s'exécute dans [Atom](https://github.com/atom/atom), l'un des éditeurs de code les plus populaires.

Avant de commencer, voici quelques hypothèses que je fais :

* Vous avez suivi les [directives de contribution de Free Code Camp](https://github.com/FreeCodeCamp/FreeCodeCamp/blob/staging/CONTRIBUTING.md#setup-linting) jusqu'à la partie qui dit **Configuration du Linting.**
* Et donc, vous avez installé les **prérequis** nécessaires (notamment Node.js et npm).
* Vous avez au moins une compréhension de base de l'utilisation de la **ligne de commande** et de **git**.
* Vous utilisez [Atom](https://atom.io/) comme éditeur de texte (bien que cet article puisse être utile même si vous ne l'utilisez pas, vous devrez simplement consulter la documentation de [votre éditeur de texte](http://eslint.org/docs/user-guide/integrations) pour les instructions concernant ESLint).

### **Qu'est-ce que le linting exactement ?**

> « **Le linting** est le processus d'exécution d'un programme qui analysera le code pour détecter les erreurs potentielles. » — [Oded](https://stackoverflow.com/questions/8503559/what-is-linting) sur Stack Overflow

Et **ESLint** est un _outil de linting_ spécifique au code JavaScript. Vous utilisez ESLint pour trouver du code problématique (« erreurs ») écrit en JavaScript.

Au fait, le « ES » dans le nom d'ESLint vient de « ECMAScript », qui est le nom officiel du langage JavaScript.

Imaginez ESLint comme votre grand-mère vous disant comment vivre votre vie. Elle pointe vos erreurs et vous dit de les corriger. Vous écoutez grand-mère, car grand-mère sait.

Ces « erreurs » peuvent être _objectives_, ce qui signifie qu'elles sont causées par du code qui ne respecte pas, par exemple, la syntaxe de JavaScript (ou tout autre langage de programmation que vous lintez). De cette manière, vous diriez que le linter détecte les erreurs de syntaxe.

Je dis « erreurs objectives » car ces erreurs sont inhérentes à JavaScript lui-même. Si vous oubliez un point-virgule à la fin d'une déclaration de variable, c'est objectivement une erreur selon les auteurs de JavaScript — même si cela n'empêche pas votre programme de s'exécuter (voir [insertion automatique de point-virgule](https://stackoverflow.com/questions/2846283/what-are-the-rules-for-javascripts-automatic-semicolon-insertion-asi)).

Ou ces erreurs peuvent être _subjectives_, ce qui signifie que _vous_ (et non le [Comité Technique 39](https://www.ecma-international.org/memento/TC39.htm), l'organisme de normalisation d'ECMAScript) avez défini un ensemble de règles que votre code doit suivre. Ces règles de codage sont couramment résumées dans un **guide de style JavaScript**, qui est un document déclarant une sorte de bonnes pratiques de codage. Free Code Camp, parmi de nombreux autres projets logiciels, utilise des guides de style.

Le guide de style JavaScript d'[Airbnb](https://github.com/airbnb/javascript) est l'un des plus populaires pour les développeurs JavaScript, et le guide de style de Free Code Camp est basé sur celui-ci.

Le but de suivre un guide de style est d'avoir une « norme d'écriture » que les développeurs de votre projet suivent pour garder le code propre, simple et cohérent. Cela ressemble au concept du [**AP Stylebook**](https://en.wikipedia.org/wiki/AP_Stylebook) que suivent les journalistes. La seule différence est que le AP Stylebook est un guide de style pour la grammaire anglaise, tandis que le guide de style d'Airbnb est pour JavaScript.

Une fois que vous avez clarifié comment le code doit être écrit pour votre projet logiciel (c'est-à-dire que vous avez choisi un guide de style ou créé le vôtre), vous êtes prêt à configurer vos _règles de linting_ pour ESLint.

La façon dont ESLint fonctionne est que vous lui dites quelles règles (c'est-à-dire que vous prenez les règles de votre guide de style et les convertissez en _règles de linting_) il doit connaître et à quoi il doit faire attention, afin qu'ESLint puisse vous taper sur l'épaule et vous faire savoir lorsque vous écrivez du code problématique.

Pour informer ESLint de vos règles de linting, vous les configurez dans un [fichier de configuration](http://eslint.org/docs/user-guide/configuring) appelé `.eslintrc` ou `eslintConfig` ou `package.json`, que ESLint recherchera et lira automatiquement. Et pendant que vous développez, ESLint vous avertira du code problématique qui ne respecte pas ces règles afin que vous puissiez faire des révisions — pendant que vous codez. Ce qui est comme avoir grand-mère faire de la programmation en binôme avec vous.

Là où [ESLint](http://eslint.org/docs/user-guide/configuring) excelle, c'est qu'il est « _conçu pour être complètement configurable, ce qui signifie que vous pouvez désactiver chaque règle et exécuter uniquement avec une validation de syntaxe de base, ou mélanger et assortir les règles groupées et vos règles personnalisées pour rendre ESLint parfait pour votre projet_. » En d'autres termes, vous pouvez mélanger et assortir à la fois des règles objectives et subjectives.

Vous avez [des options](https://www.sitepoint.com/comparison-javascript-linting-tools/) en matière d'outils de linting JavaScript, mais dans cet article, nous nous concentrons sur ESLint car Free Code Camp le spécifie dans ses directives de contribution. Et il est largement utilisé ailleurs.

Vous avez également [des options](http://noeticforce.com/best-javascript-style-guide-for-maintainable-code) en matière de guides de style JavaScript. Celui d'Airbnb est un bon à connaître car il a plus de [45 000 étoiles sur GitHub](https://github.com/airbnb/javascript) au moment de la rédaction de cet article, et son utilisation est en croissance.

### **Configuration du Linting pour freeCodeCamp**

Il existe deux façons d'installer ESLint : [globalement et localement](https://www.npmjs.com/package/eslint). Nous allons nous concentrer sur l'installation **locale**, ce qui signifie pour votre répertoire de travail local, c'est-à-dire votre dépôt cloné de Free Code Camp.

1 : Ouvrez votre clone de Free Code Camp dans votre éditeur de texte (cela suppose que vous avez effectivement cloné Free Code Camp sur votre ordinateur)

2 : Dans le Terminal, utilisez `cd` (changer de répertoire) pour accéder à votre répertoire Free Code Camp

3 : Tapez `npm install eslint --save-dev` dans le Terminal

4 : Dans votre éditeur de texte Atom, allez dans **Préférences** > **Installer** > et tapez **linter-eslint** dans la boîte de recherche des packages

![Image](https://cdn-media-1.freecodecamp.org/images/suWrI14ZfgjkyFns6g97Sashp7UhgSjC8tL7)

Remarque : Vous pouvez également installer les packages Atom à partir de la ligne de commande en utilisant la commande `apm`. Voir [ces instructions](https://github.com/AtomLinter/linter-eslint) pour un exemple.

5 : Installez **linter-eslint** et **linter**.

6 : Dans votre répertoire Free Code Camp, fermez tous les fichiers `<nomdefichier>.js` et rouvrez-les

Et maintenant, la prochaine fois que vous écrivez du JavaScript, vous devriez voir ESLint fonctionner !

![Image](https://cdn-media-1.freecodecamp.org/images/w0FIY5QLVmC9avMYdgWxpkXR2HDPzQakW6gp)

Remarque : J'ai omis une étape importante : **configurer ESLint**, c'est-à-dire la partie où vous personnalisez ESLint et lui dites quelles sont vos règles de linting. Je l'ai fait car lorsque vous clonez le dépôt de Free Code Camp, il _contient déjà_ des fichiers de configuration ESLint, par exemple, voir `eslintrc` et `package.json`. Vous n'avez donc pas besoin de faire de configuration vous-même.

Dans le cas où vous travaillez sur un projet où vous devez configurer ESLint, je vous oriente vers les liens suivants :

* [Configurer ESLint](http://eslint.org/docs/user-guide/configuring).
* [Commencer avec ESLint v1.0](http://devnull.guru/get-started-with-eslint/)
* [npm, eslint](https://www.npmjs.com/package/eslint)
* La configuration ESLint partagée et extensible d'[Airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb)

Pour conclure :

1. Le linting est le processus de vérification du code problématique.
2. ESLint est un outil qui effectue le linting.
3. ESLint peut être un excellent outil d'apprentissage car il vous oblige à écrire un code propre et cohérent et à développer de bonnes habitudes de codage.
4. De nombreux projets open source vous demandent d'exécuter ESLint.
5. Vous devez avoir configuré ESLint dans votre éditeur de texte pour contribuer à Free Code Camp.
6. Si vous n'utilisez pas Atom, consultez la documentation de [votre éditeur de texte](http://eslint.org/docs/user-guide/integrations) pour savoir comment installer ESLint.
7. Restez sur la bonne voie.

Si vous avez des questions, vous pouvez me tweeter à [@gilbertginsberg](https://twitter.com/gilbertginsberg) ou me trouver sur [GilbertIndex](https://goo.gl/DgxjEj).