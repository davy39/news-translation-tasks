---
title: Comment améliorer vos compétences en débogage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T17:17:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-debugging-skills-abb5b363bdb8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*akKmLhkA0fJ__-hb3Bp8WA.jpeg
tags:
- name: careers
  slug: careers
- name: Computer Science
  slug: computer-science
- name: debugging
  slug: debugging
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: Comment améliorer vos compétences en débogage
seo_desc: 'By Nick Karnik

  All of us write code that breaks at some point. That is part of the development
  process. When you run into an error, you may feel that you don’t know what to do.
  However, even the most seasoned developers introduce errors and bugs that...'
---

Par Nick Karnik

Nous écrivons tous du code qui ne fonctionne pas à un moment donné. Cela fait partie du processus de développement. Lorsque vous rencontrez une erreur, vous pouvez avoir l'impression de ne pas savoir quoi faire. Cependant, même les développeurs les plus expérimentés introduisent des erreurs et des bugs qui cassent leur code. Nous sommes humains après tout.

L'important est d'apprendre de ces erreurs et d'éviter de les répéter en développant des techniques pour améliorer vos compétences en programmation et en débogage. Les erreurs sont principalement logiques ou syntaxiques. Certaines se manifestent via des exceptions ou des plantages, tandis que d'autres ne peuvent être observées qu'en utilisant le logiciel.

### Voici quelques-unes des erreurs que commettent les développeurs

#### Ne pas journaliser les messages

L'un des scénarios les moins utiles que vous pouvez rencontrer est lorsque votre programme plante et qu'il n'y a aucun message d'erreur pour indiquer ce qui s'est mal passé. La première étape consiste à identifier si le programme plante au démarrage ou pendant l'exécution. Vous pouvez y parvenir en imprimant un simple message de journalisation dans le terminal au début de votre code.

Si vous ne voyez pas votre message de journalisation, votre programme plante probablement pendant le chargement et il s'agit peut-être d'un problème lié à une dépendance ou à la construction.

Si vous voyez votre message, vous devez réduire la zone générale du plantage. La meilleure façon est de placer stratégiquement quelques messages de journalisation dans votre programme en fonction de la quantité d'informations que vous avez sur le chemin d'exécution au moment où il plante. Ensuite, tout ce que vous avez à faire est de voir quels messages sont imprimés.

#### Ne pas lire les messages d'erreur

Les messages d'exception sur le front-end sont généralement affichés sur l'interface utilisateur ou la console de développement. Parfois, ces messages sont visibles dans le back-end via le terminal ou des fichiers de journalisation. Peu importe où ces erreurs se produisent, les nouveaux développeurs sont intimidés par elles et ne prennent pas le temps de les lire.

C'est la raison numéro un pour laquelle le débogage prend plus de temps pour de nombreux développeurs. La première chose que vous devriez faire est de prendre le temps de lire le message d'erreur devant vous, de le laisser s'imprégner et de le traiter minutieusement.

#### Ne pas lire les fichiers de journalisation du système

Certains programmes génèrent des fichiers de journalisation ou écrivent dans le journal des événements du système. Il y a souvent des informations utiles dans ces journaux. Même si cela ne vous dit pas exactement ce qui ne va pas, il peut y avoir un message d'avertissement ou d'erreur, ou même un message de succès, fournissant un indice sur ce qui s'est passé avant que l'erreur ne se produise.

#### Ne pas écrire de journaux de trace

Le traçage consiste à suivre le flux de votre programme et les données. L'écriture de messages de trace dans votre programme aide à simplifier le processus de débogage. Les journaux de trace sont un moyen facile de suivre l'exécution du programme tout au long de l'exécution de votre application.

#### Ne pas faire de changements incrémentiels, les construire et les tester

De nombreux développeurs écrivent de gros morceaux de code avant de les construire et de les tester. Le temps nécessaire pour trouver des bugs augmente proportionnellement à la quantité de code qui a été modifiée. Vous devriez vous efforcer de faire des changements incrémentiels, de les construire et de les tester aussi fréquemment que possible. Cela garantira que vous ne vous retrouverez pas dans une situation où beaucoup de code a été écrit avant de découvrir que votre programme ne fonctionne pas.

Souvent, je refactorise même mon code pour simplifier ce que j'ai écrit.

#### Ne pas écrire d'automatisation de tests

Les tests unitaires et l'automatisation des tests de bout en bout vous permettent de détecter les erreurs potentielles au fur et à mesure qu'elles se produisent. L'une des raisons pour lesquelles le code existant se casse est que les développeurs refactorisent leur code lorsqu'ils ont une faible couverture de tests, ce qui signifie que toutes les modifications ne sont pas testées automatiquement.

#### Ne pas utiliser la méthode d'élimination

Si vous n'êtes pas en mesure d'identifier la cause racine de votre problème, vous devez utiliser la méthode d'élimination. Vous pouvez commenter de nouveaux blocs de code pour voir si les erreurs s'arrêtent. L'élimination de blocs de code vous aidera à vous rapprocher du diagnostic du problème.

Vous pouvez formuler une certaine hypothèse et essayer de la prouver ou de l'infirmer. Souvent, une simple supposition peut vous empêcher de trouver des bugs.

#### Copier et coller depuis StackOverflow

Souvent, les développeurs copient et collent du code depuis Stack Overflow sans comprendre ce qu'il fait. Cela a tant d'effets néfastes. Tout d'abord, il est important que vous fassiez attention à ce qui entre dans votre application.

Plus souvent que je ne le voudrais, lorsque j'écris une question sur StackOverflow et que je réfléchis à la manière de l'articuler efficacement, je finis par répondre à ma propre question !

De même, parfois lorsque je parle à d'autres membres de l'équipe, je finis par répondre à ma propre question. Cela se produit parce que cela vous force à réfléchir à votre solution.

#### Ne pas résoudre leur problème à nouveau

L'une des techniques de débogage les plus réussies que j'ai trouvées est d'essayer de parcourir votre solution encore et encore et, dans certains cas, d'essayer de réimplémenter certaines fonctionnalités à partir de zéro. Cela vous force à trouver des problèmes potentiels en recréant votre implémentation.

#### Ne pas revenir en arrière

Normalement, si vous pouvez isoler les symptômes à une zone spécifique, vous pouvez commencer à remonter la pile d'appels pour vérifier toutes les variables et les valeurs attendues. Cela peut rapidement vous amener à découvrir des parties de votre programme où les choses se comportent de manière inattendue.

#### Ne pas apprendre le débogueur

Enfin, le meilleur investissement que vous puissiez faire en vous-même est d'apprendre à utiliser un débogueur. Tous les IDE sont livrés avec des débogueurs puissants. Ils suivent les mêmes concepts de base. Ils vous permettent d'arrêter programmatiquement l'exécution de votre application, soit au démarrage, soit dans une partie spécifique du flux du programme.

Il existe également de nombreux outils de débogage qui peuvent aider dans ce processus.

Si cet article vous a été utile, ??? et suivez-moi sur Twitter.

[**Extensions GitHub pour booster votre productivité**](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)
[_Voici les extensions GitHub que j'utilise. Elles vous permettront d'améliorer votre productivité sur GitHub. Veuillez partager votre..._medium.freecodecamp.org](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)