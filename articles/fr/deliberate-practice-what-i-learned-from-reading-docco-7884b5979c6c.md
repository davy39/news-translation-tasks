---
title: 'Pratique délibérée : Ce que j''ai appris en lisant docco'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-30T12:34:05.000Z'
originalURL: https://freecodecamp.org/news/deliberate-practice-what-i-learned-from-reading-docco-7884b5979c6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*azMxh52KWiwS_hDt17PRMw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Pratique délibérée : Ce que j''ai appris en lisant docco'
seo_desc: 'By Anthony Ng

  I was browsing through open source projects, trying to find the next one I would
  study. I came upon underscore and its annotated source code.

  The annotated source code amazed me. On the right side of the page was the source
  code. On the...'
---

Par Anthony Ng

Je parcourais des projets open source, essayant de trouver le prochain que j'étudierais. Je suis tombé sur `underscore` et son [code source annoté](http://underscorejs.org/docs/underscore.html).

Le code source annoté m'a impressionné. Sur le côté droit de la page se trouvait le code source. Sur le côté gauche de la page se trouvaient des notes expliquant chaque bloc de code. C'était une connaissance que je n'aurais pas obtenue en lisant le code source par moi-même. Je voulais savoir ce qui avait produit cette belle documentation et j'ai trouvé `docco`.

### Qu'est-ce que docco ?

`[docco](https://github.com/jashkenas/docco)` est un "générateur de documentation de style programmation lettrée". C'est un programme qui prend votre code source et crée une documentation annotée.

Notez que `docco` ne génère que la mise en page de la documentation. Les commentaires de votre code source servent d'annotations.

### Comment utiliser docco ?

J'ai une fonction incroyable pour laquelle je veux créer une documentation. J'ai inclus des commentaires descriptifs qui serviront d'annotations.

Pour utiliser `docco`, je vais l'installer localement avec `npm install --save-dev docco`.

La commande `docco` accepte les noms de fichiers, pour lesquels elle générera une documentation. Mon programme est enregistré sous `app.js`, donc je vais exécuter `./node_modules/.bin/docco app.js`.

Et c'est tout ce qu'il faut pour créer un [code source annoté](https://newyork-anthonyng.github.io/articles/deliberate_practice/002_docco/tutorial/docs/app.html) !

Par défaut, `docco` placera toute la documentation générée dans un nouveau répertoire `docs`. Vous pouvez configurer `docco` pour utiliser différents CSS ou différentes mises en page. [Consultez cette mise en page `linear` du code annoté](https://newyork-anthonyng.github.io/articles/deliberate_practice/002_docco/tutorial/linearDocs/app.html).

Consultez le [README.md](https://github.com/jashkenas/docco) de `docco` pour voir ce que vous pouvez personnaliser.

Je vais commencer à utiliser `docco` pour annoter tous les futurs projets Open Source sur lesquels je travaillerai.

### Qu'est-ce que la programmation lettrée ?

Avec la [programmation lettrée](https://en.wikipedia.org/wiki/Literate_programming), vous voulez exprimer la logique de votre programme en langage clair. Une personne devrait pouvoir le lire comme un livre et comprendre ce qui se passe.

Cela signifie que la documentation doit suivre le même ordre que la logique du programme, et non le même ordre que le code source. Nous écrivons des programmes dans un ordre qui rend notre compilateur heureux. Parfois, cet ordre n'est pas le même que la logique de notre programme.

Donc, `docco` ne génère pas de documentation de programmation lettrée dans son sens le plus vrai. `docco` génère sa documentation dans le même ordre que son code source. Mais je pense toujours que ce code source annoté est précieux. Considérez-le comme du pseudocode pour votre code.

### Décomposer les choses et les remettre ensemble

Lorsque vous commencez à comprendre un nouveau projet, investissez du temps dans la mise en place d'une boucle de rétroaction. Cela peut être la mise en place de la suite de tests, afin que vous puissiez modifier le code source et voir ce qui se casse. Cela peut être trouver un moyen rapide d'exécuter le code source à partir de votre terminal pour voir vos journaux de console. Je ne commencerais pas à parcourir le code source tant que vous n'avez pas un moyen de créer cette boucle de rétroaction.

C'est ce qui rend le développement piloté par les tests si efficace et agréable pour moi. Vous voyez ce que fait votre code instantanément. Sans boucle de rétroaction, vous coderez dans le noir.

J'exécutais le code source de `docco` dans mon terminal en exécutant `node docco.js app.js`, où `app.js` était un fichier factice. J'ai pu voir les résultats de mes `console.log` en exécutant cette commande. [Voici à quoi ressemblait mon beau code source](https://github.com/newyork-anthonyng/articles/blob/master/deliberate_practice/002_docco/docco.js), avec plus de 150 lignes de mes propres commentaires.

### Travaillez sur des projets que vous utiliserez régulièrement

Kent Dodds a écrit [un excellent article](https://medium.com/@kentcdodds/what-open-source-project-should-i-contribute-to-7d50ecfe1cb4) sur la contribution aux projets Open Source. Sa suggestion est de ne travailler que sur des projets que vous utiliserez régulièrement. C'est ainsi que j'ai choisi les projets sur lesquels j'ai travaillé. J'ai décidé de créer ma propre version de `docco` parce que c'était quelque chose que je voudrais utiliser moi-même.

J'ai également décidé de ne pas utiliser `docco` lui-même parce que sa maintenance semblait être morte. Le dernier commit datait-il de plus de 2 ans ? Y avait-il des problèmes non résolus depuis des années ? Y avait-il beaucoup de Pull Requests ignorées ? Ce sont de bons indicateurs que ce projet peut être mort ou non maintenu.

Plus important encore, je voulais créer et publier [docco-lite](https://www.npmjs.com/package/@newyork.anthonyng/docco-lite) pour l'expérience d'apprentissage.

### Des bibliothèques incroyables existent en dehors du navigateur également

Je me suis concentré sur le monde du front-end. Je sais qu'il n'y a pas de pénurie de bibliothèques et de frameworks disponibles pour moi. J'ignorais les bibliothèques incroyables disponibles en dehors du monde du front-end.

Voici quelques bibliothèques incroyables que `docco` a utilisées.

#### 1. fs-extra

`[fs-extra](https://github.com/jprichardson/node-fs-extra)` est une version améliorée du module du système de fichiers (fs). C'était très cool de créer des répertoires et des fichiers, au lieu de créer des `<div>` et des `<h1>`.

#### 2. commander

`[commander](https://github.com/tj/commander.js)` est une bibliothèque qui crée des interfaces de ligne de commande.

#### 3. chalk

`[chalk](https://github.com/chalk/chalk)` vous permet de styliser vos chaînes de terminal ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*-6itgHDqK9P2M0axvIjk0Q.png)
_Sortie chalk magnifique_

#### 4. highlightjs

`[highlightjs](https://highlightjs.org/)` peut créer du HTML à partir d'une chaîne de code. Avec cette sortie HTML, vous pouvez ajouter du CSS pour styliser vos extraits de code.

### Modèles JavaScript

Dans le bootcamp de General Assembly, j'ai appris Handlebars avant les Angular/React sophistiqués. Handlebars est un langage de modélisation JavaScript simple, qui met JavaScript dans votre HTML. Si vous avez un projet simple, parfois un langage de modélisation simple est suffisant pour vous aider. L'utilisation de React peut ne pas avoir de sens.

J'ai travaillé avec React pendant la dernière année. La simplicité et la puissance de l'utilisation des modèles JavaScript m'ont surpris. La bibliothèque `underscore` fournit un moyen simple d'utiliser la modélisation JavaScript.

Si vous voulez inclure JavaScript dans votre modèle, utilisez `<%` %>.

Si vous voulez que JavaScript soit rendu comme du texte, utilisez `<%=` %> (notez le signe égal (=)).

Vous pouvez même vous lancer et utiliser des boucles for avec des modèles JavaScript.

Maintenant, mettons tout cela ensemble en utilisant la méthode `template` de `underscore`.

Nous n'avons pas eu besoin de webpack, Babel, ou du DOM virtuel. Le bon vieux temps de la construction d'une page web ?.

### Créez des PR précieuses

Contribuer à un projet Open Source devrait apporter de la valeur à quelqu'un. Vous pourriez aider les autres en corrigeant des bugs, en ajoutant des fonctionnalités, ou en mettant à jour la documentation. Vous pourriez vous aider vous-même en travaillant sur un projet où vous apprenez quelque chose de nouveau.

Mais assurez-vous que le travail que vous faites n'est pas gaspillé.

Jetez un coup d'œil au [dépôt UMD](https://github.com/umdjs/umd).

![Image](https://cdn-media-1.freecodecamp.org/images/1*AZIP7NRwRvNYDQ_weX7Juw.png)
_README.md du dépôt UMD_

Nous pouvons voir quelques problèmes de formatage Markdown dans le README.md. Ce serait une opportunité parfaite pour créer une Pull Request pour corriger cela.

Mais avant de le faire, vérifions que nos efforts ne sont pas gaspillés. Vérifions les Pull Requests en attente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sg3FV6VrrMjI4yo6Y8RTMQ.png)
_Pull Requests pour le dépôt UMD_

Remarquez comment il y a 11 Pull Requests en attente qui corrigent la même chose.

C'est génial que les gens se soucient assez de ce projet pour corriger sa documentation. Mais créer une 12ème Pull Request pour corriger le README.md n'aidera personne.

La même chose peut être dite avant de créer une Pull Request pour ajouter une nouvelle fonctionnalité ou corriger un bug. Vous devriez créer un problème sur Github d'abord. La fonctionnalité peut ne pas être souhaitée, donc le temps passé sur la Pull Request est gaspillé. Le bug que vous avez trouvé pourrait en fait être un bug dans votre propre code, plutôt qu'un bug dans le code source de la bibliothèque.

Créer des problèmes aide également à éviter le travail duplicatif effectué par d'autres contributeurs Open Source. Avant de créer un nouveau problème, parcourez les autres problèmes ouverts et fermés pour vous assurer qu'il n'est pas déjà corrigé.

### Réduire les barrières avec la programmation lettrée

Il est précieux de réduire la barrière pour contribuer aux projets Open Source. Il y a beaucoup de facteurs intimidants lorsque l'on commence un projet Open Source.

Quelle est la structure du répertoire ? Que dois-je télécharger pour configurer mon environnement ? Quelles connaissances de base dois-je avoir pour comprendre la logique du programme ?

Un Code de Conduite est quelque chose qui devient un élément de base dans les projets Open Source (voir [le code de conduite de Facebook](https://code.facebook.com/pages/876921332402685/open-source-code-of-conduct) comme exemple). J'espère que le code source annoté deviendra également un élément de base dans les projets futurs.

Quels sont vos réflexions sur le Code Source Annoté ? Est-ce quelque chose que vous aimeriez voir dans plus de projets ? Laissez un commentaire ci-dessous !

* Jetez un coup d'œil à mon [code docco annoté](https://newyork-anthonyng.github.io/articles/deliberate_practice/002_docco/tutorial/docs/annotatedDocco.html).