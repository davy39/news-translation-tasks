---
title: Comment commencer la programmation compétitive en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:22:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-competitive-programming-in-javascript-76ad2e760efe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SPx_5yXieH6SA9dpkyosOw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment commencer la programmation compétitive en JavaScript
seo_desc: 'By Priyabrata Biswas

  If you’re not familiar with competitive programming, basically it is a mind sport
  with the aim of writing code to solve given problems. I was introduced to it in
  my freshman year by my seniors. As of this writing, I’m still not r...'
---

Par Priyabrata Biswas

Si vous n'êtes pas familier avec la [programmation compétitive](https://en.wikipedia.org/wiki/Competitive_programming), c'est essentiellement un sport mental dont le but est d'écrire du code pour résoudre des problèmes donnés. J'ai été initié à cela lors de ma première année par mes aînés. Au moment où j'écris ces lignes, je ne suis toujours pas vraiment doué pour cela ! Peut-être est-ce dû au fait que je n'aime pas coder en C++, ou peut-être suis-je une personne paresseuse qui ne prendra pas le temps d'apprendre suffisamment bien. Mais j'aime les algorithmes et les structures de données autant que j'aime JavaScript !

Donc, cette pensée prépostéreuse m'a traversé l'esprit encore et encore. 'Et si nous commencions à utiliser JavaScript dans l'arène compétitive ?' Il s'avère que cela ne semble pas être le territoire inexploré que je pensais. De nombreuses plateformes comme [HackerRank](https://www.hackerrank.com/), [CodeChef](https://www.codechef.com/), et [Codeforces](https://codeforces.com/) supportent JavaScript.

Je sais que C++ est beaucoup plus rapide comparé à JavaScript et peut allouer dynamiquement de la mémoire. C et C++ sont assez similaires en termes de performance, mais les programmeurs compétitifs utilisent principalement C++ en raison de sa [Standard Template Library](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/) (ou STL). Elle fournit des structures de données de programmation courantes comme les listes, les piles, les tableaux ainsi que des classes de conteneurs, des algorithmes et des itérateurs prêts à l'emploi.

Mais JavaScript offre quelque chose que C++ n'a pas :

> La liberté !

En tant que langage de script, JavaScript est intrinsèquement lent. Pourtant, c'est le langage le plus populaire. Selon l'enquête des développeurs de [Stack Overflow de 2018](https://insights.stackoverflow.com/survey/2018/), 69,8 % des répondants utilisent JavaScript pour leurs besoins de développement. Mais en même temps, il ne brille pas autant dans le cas de la programmation compétitive. La raison est qu'il n'a tout simplement pas été conçu pour cela !

En 1995, [Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich) a développé JavaScript uniquement pour ajouter de l'interactivité aux pages web comme la gestion d'un clic de souris.

Aujourd'hui, nous pouvons construire des serveurs, des jeux, des applications mobiles, des applications IoT et même le machine learning dans le navigateur est possible avec JavaScript. Alors, pourquoi se sentir honteux de l'utiliser en programmation compétitive ?

> « Toute application qui peut être écrite en JavaScript sera finalement écrite en JavaScript. » — [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

Vous vous souvenez de ce que je vous ai dit à propos de la STL et de la boîte à outils qu'elle fournit pour la programmation compétitive ? Je me suis demandé pourquoi [TC 39](https://www.ecma-international.org/memento/tc39.htm) ne venait pas avec quelque chose de similaire pour JavaScript !

![Image](https://cdn-media-1.freecodecamp.org/images/1*WscERe0SENQYJ-lh-NRHhw.jpeg)
_Eventuellement, j'ai eu une idée ! ?_

Avez-vous entendu parler du 'Node Package Manager' également connu sous le nom de '**npm**' ?

Eh bien, c'est le plus grand [registre de logiciels](https://www.npmjs.com/) au monde avec plus de 874 285 paquets (au moment de l'écriture) et c'est le gestionnaire de paquets par défaut pour Node.js.

> L'idée est de développer un paquet npm similaire à la STL de C++

### Présentation de Mathball

Mathball est un paquet npm pour la programmation compétitive en JavaScript implémentant des algorithmes optimisés pour une exécution plus rapide. Bon, maintenant j'exagère ! La vérité est qu'il ne supporte que 16 fonctions utilitaires implémentant des [approches par force brute](https://discuss.codechef.com/questions/281/brute-force-approach) jusqu'à présent. J'ai assemblé cette petite bibliothèque d'aide pour assister les gens en programmation compétitive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UbZwDVpX-diNhP4zdxLytg.png)
_Comment est le logo ! ?_

Vous pouvez obtenir le paquet assez facilement si vous avez Node.js et npm installés sur votre machine en tapant la commande suivante dans votre terminal :

```
npm install mathball
```

Vous pouvez accéder à toutes les utilités via un objet `mathball`, `M`, comme ceci :

Encore une fois, obtenir une fonction individuelle est aussi simple que ceci :

Maintenant, vous devez vous demander :

> Comment suis-je censé utiliser une bibliothèque tierce à l'intérieur d'une plateforme comme HackerRank ou CodeChef ?

La réponse est simple, il suffit de la **bundler** ! ?

Permettez-moi d'expliquer ce que je veux dire ! Supposons que vous essayez de résoudre ce problème particulier sur HackerRank :

[**Simple Array Sum | HackerRank**](https://www.hackerrank.com/challenges/simple-array-sum/problem)  
[_Calculer la somme des entiers dans un tableau._www.hackerrank.com](https://www.hackerrank.com/challenges/simple-array-sum/problem)

Ne soyez pas submergé par toutes ces lignes de code. Si vous avez déjà utilisé HackerRank, vous savez déjà que c'est juste pour gérer les entrées/sorties.

Tout d'abord, copiez et collez le contenu ci-dessus dans un fichier, `index.js`. Ensuite, dans le même répertoire, ouvrez le terminal et tapez :

```
npm install mathball
```

Ensuite, à l'intérieur du fichier `index.js`, modifiez ce qui suit :

Enfin, afin de bundler le tout dans un seul fichier, j'utilise Webpack mais vous êtes libre de choisir n'importe quel bundler de modules CommonJS !

Donc, créons un fichier `webpack.config.js` dans le même répertoire avec le code suivant :

Si vous n'avez pas déjà installé Webpack, veuillez l'installer comme suit :

```
npm install -g webpack webpack-cli
```

Enfin, tapez ce qui suit :

```
webpack --config ./webpack.config.js --mode=development
```

Maintenant, la commande ci-dessus créera un fichier nommé `bundle.js` dans le même répertoire. Donc, copiez et collez son contenu sur HackerRank et cliquez sur ***Submit Code***. C'est tout !

![Image](https://cdn-media-1.freecodecamp.org/images/1*XmAdDfmGO6yucBPyeSM1YQ.png)
_Bazinga ! ?_

### Épilogue

Cela n'a pas de sens de passer par tout ce non-sens juste pour calculer la somme d'un tableau... n'est-ce pas ? Donc, je dois avouer que les problèmes de programmation compétitive tendent à être beaucoup plus compliqués que cela.

> Je crois que la programmation compétitive consiste davantage à trouver des moyens de résoudre un problème qu'à simplement les résoudre !

Une fois que vous avez compris quel algorithme ou structure de données votre problème nécessite, le codage devient assez facile si vous avez une bibliothèque comme Mathball à votre disposition. De plus, vous n'avez pas à passer par toutes ces étapes de bundling à chaque fois que vous codez quelque chose. C'est essentiellement un processus de configuration unique. Codez simplement, et bundlez vos fichiers avec la dernière commande.

**Fait amusant** — vous pouvez utiliser Mathball dans votre projet aussi !

Je vais constamment améliorer Mathball et j'accueille sincèrement votre contribution. Ensemble, nous pouvons faire en sorte que Mathball fasse beaucoup plus ! Voici le [lien](https://github.com/pbiswas101/Mathball) vers le dépôt.

Le but de cet article était de promouvoir l'importance de la programmation compétitive dans la communauté JavaScript. Je pense que l'apprentissage des algorithmes et des structures de données nous prépare à nous soucier davantage de l'efficacité et de la complexité de notre base de code. Cela nous fait regarder deux fois pour détecter les fuites de mémoire et nous aide à devenir de meilleurs développeurs, en général.

Voici une liste de ressources qui m'ont inspiré pour entreprendre mon voyage de soutien à JavaScript dans la programmation compétitive :

1. [Pranay Dubey — JavaScript pour la programmation compétitive](https://www.youtube.com/watch?v=2OUw6jRYSKA)
2. [JavaScript pour la programmation algorithmique compétitive](https://hackernoon.com/javascript-for-algorithms-competitive-programming-45cf723cd16f)

Merci pour votre temps ! ✍️