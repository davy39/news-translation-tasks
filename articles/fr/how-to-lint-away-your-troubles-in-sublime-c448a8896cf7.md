---
title: Comment utiliser le linting pour résoudre vos problèmes dans Sublime
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:25:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-lint-away-your-troubles-in-sublime-c448a8896cf7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ZmNxmpbn33gX8ppUsqM7w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser le linting pour résoudre vos problèmes dans Sublime
seo_desc: 'By Abdul Kadir

  Sublime is a lightweight text editor and is quite popular among many web developers.
  Now I know there are many sophisticated IDEs in the market with intellisense, code
  completion, and whatnot. But this post is for those who have remain...'
---

Par Abdul Kadir

Sublime est un éditeur de texte léger et est assez populaire parmi de nombreux développeurs web. Je sais qu'il existe de nombreux IDE sophistiqués sur le marché avec intellisense, complétion de code, et bien d'autres fonctionnalités. Mais cet article est pour ceux qui sont restés fidèles à leurs éditeurs de texte préférés ! Donc, si vous utilisez Sublime pour vos projets, vous pourriez apprécier certaines des fonctionnalités astucieuses qu'il offre. Le linting en est une.

Commençons par définir le terme « Linting ».

> Le linting est le processus de vérification de votre code pour détecter les erreurs potentielles. Cela peut concerner soit la syntaxe, soit le style de code.

Le processus de linting peut être effectué à trois étapes du développement :

1. Via votre éditeur (linting en direct)
2. À travers le processus de build
3. En utilisant un hook pre-commit dans le contrôle de version

Dans cet article, nous allons explorer le linting en direct dans l'éditeur. Il existe de nombreux linters populaires pour JavaScript comme JSHint, JSCS et ESLint. J'utiliserai ESLint, car ESLint supporte le code ES6, est hautement extensible et très facile à utiliser. Si vous êtes intéressé, vous pouvez consulter les comparaisons entre les différents linters [ici](https://www.sitepoint.com/comparison-javascript-linting-tools/) !

### Étape 1

Vous devez d'abord installer le package npm ESLint. La commande est la suivante :

```
npm install -g eslint
```

L'option « -g » permet d'installer le package globalement. Installez « npm » si vous ne l'avez pas déjà. Un fichier s'ouvrira dans Sublime vous demandant de télécharger deux autres plugins. Vous devez installer ces plugins en utilisant le Package Control de Sublime.

Ouvrez le Package Control en utilisant command/ctrl + shift + P et sélectionnez l'option « Package Control: Install Package ». Ensuite, téléchargez les deux plugins.

1. SublimeLinter-eslint
2. SublimeLinter-contrib-eslint

SublimeLinter est le framework qui fournit le linting. Il ne vient pas avec le support pour différents langages. Le Linter spécifique au langage doit être installé séparément.

Le plugin Sublime-contrib-eslint agit comme une interface entre ESLint et SublimeLinter. Vous pouvez vérifier la procédure d'installation sur leur [site principal](http://www.sublimelinter.com/en/latest/installation.html) si vous êtes bloqué quelque part.

Après avoir installé les plugins avec succès, vous devez redémarrer votre éditeur pour que les changements prennent effet. Maintenant, nous allons voir ESLint en action !

### **Étape 2**

Ouf ! Cela faisait beaucoup d'installations. Maintenant, enfin, vous pouvez découvrir l'incroyable puissance du Linting ! Ouvrez votre fichier dans Sublime et admirez le pouvoir... mais attendez, rien ne se passe. Pourquoi donc ? Ne vous inquiétez pas. Vous avez tout installé correctement, mais ESLint en lui-même ne fait rien. Vous devez fournir la configuration de base, et c'est un processus très simple. Voici comment faire :

1. Lancez le terminal dans le répertoire principal de votre projet
2. Tapez cette commande

```
eslint --init
```

Une invite apparaît vous posant quelques questions sur vos préférences de codage et un fichier « .eslintrc » est généré pour vous. Ce fichier contient les règles que vous venez de sélectionner. Vous pouvez ajouter des configurations supplémentaires si vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/NLI4ZiB25-cVRJZqWNGi6QpH1tEXHmWe9YZw)
_Avant de démarrer ESLint_

![Image](https://cdn-media-1.freecodecamp.org/images/zzhsvjiOWgBPjlRi7jvcSDRrxkI5Uqkzm3d7)
_ESLint en action_

Comme vous pouvez le voir, ESLint se plaint de l'indentation et du fait que la variable foo n'est utilisée nulle part. Vous pouvez vérifier toute erreur ou avertissement en survolant la partie surlignée du code ou en vérifiant le message dans la barre d'état de Sublime en bas.

C'est tout ! J'espère que vous avez pu suivre. Le linting est un outil assez cool pour détecter les erreurs dans votre code. Il garantit que vous suivez les directives de codage et écrivez un code propre à tout moment. J'espère que vous avez tous trouvé cet article utile, et comme toujours, bon codage !