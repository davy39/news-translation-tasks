---
title: Insuffler de l'air au guide de style JavaScript d'AirBnB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-11T21:24:07.000Z'
originalURL: https://freecodecamp.org/news/adding-some-air-to-the-airbnb-style-guide-3df40e31c57a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9nMBMt-OugnruBr_M-WuEQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Insuffler de l'air au guide de style JavaScript d'AirBnB
seo_desc: 'By Alex Moldovan

  No one sets out to write ugly, inconsistently-styled code. It just sort of happens.

  Even as the only developer on a project, the more time that passes and the more
  code you crank out, the harder it gets harder to maintain a consisten...'
---

Par Alex Moldovan

Personne ne se lance dans l'écriture de code mal structuré et incohérent. Cela arrive simplement.

Même en tant que seul développeur sur un projet, plus le temps passe et plus vous produisez de code, plus il devient difficile de maintenir un style de code cohérent.

C'est pourquoi vous avez besoin d'un guide de style.

J'ai vécu directement à quel point les équipes peuvent accomplir davantage après avoir adopté un guide de style.

Vous n'avez plus besoin de prendre de petites décisions de style tout au long de la journée. Il suffit de consulter le guide de style.

Et lorsqu'un collègue doit maintenir votre code, c'est un code propre qu'il peut lire et comprendre.

Adopter un guide de style est l'une des choses les plus simples que vous puissiez faire pour améliorer la maintenabilité de votre code — ce qui, en fin de compte, augmente la productivité de votre équipe. Alors explorons la manière la plus populaire de le faire.

#### Entrez AirBnB + ESLint

L'écosystème JavaScript offre une grande variété d'[outils](https://www.sitepoint.com/comparison-javascript-linting-tools/) et de [guides de style](http://noeticforce.com/best-javascript-style-guide-for-maintainable-code). Cela ne devrait surprendre personne. Avec JavaScript, nous nous attendons à une grande variété de tout.

Mais à mesure que l'écosystème mûrit, les développeurs expérimentés commencent à aspirer à la « manière standard » de faire les choses que les écosystèmes plus solidifiés offrent.

Vous êtes bien sûr libre de passer quelques jours à explorer l'écosystème JavaScript et à comparer différents outils, mais je vais essayer de vous faire gagner du temps : [ESLint](http://eslint.org/) est l'outil de linting JavaScript le plus populaire, et le [guide de style d'AirBnB](https://github.com/airbnb/javascript) est le guide de style le plus largement utilisé.

Pour plus de détails sur l'ajout d'ESLint à votre projet, consultez [ce lien](http://eslint.org/docs/user-guide/configuring).

Une fois que vous avez réglé cela, vous pouvez configurer votre projet pour appliquer le guide de style d'AirBnB en installant leur package npm :

```
npm install --save-dev eslint-config-airbnb
```

Ajoutez la ligne suivante dans votre fichier _.eslintrc_ :

```
"extends": "airbnb"
```

Et voilà ! Votre code est maintenant soumis aux règles du guide de style JavaScript le plus populaire. Bon codage !

#### Les standards sont surévalués

Bien que je sois d'accord avec la plupart des règles du guide de style, voici une liste de substitutions que j'ai compilées. Voici à quoi ressemblent les fichiers _.eslintrc_ dans les dossiers racines des projets :

Permettez-moi d'expliquer en détail la raison derrière chacune de ces personnalisations.

#### Indentation

La guerre des tabulations contre les espaces peut potentiellement ruiner des amitiés, et même saboter des relations romantiques.

Je préfère indenter mon code avec 4 espaces, même si une grande majorité des configurations préfèrent une indentation de 2.

Ma raison est que pour écrire du code propre, des indentations plus grandes vous donnent une meilleure représentation visuelle de la profondeur de la imbrication dans vos fonctions, et du nombre de branches différentes que vous avez.

Vous ne devriez définitivement pas imbriquer du code plus profondément que 3 ou 4 niveaux dans un fichier JavaScript (c'est une mauvaise pratique). Ainsi, avoir 4 espaces offre une meilleure lisibilité, tout en préservant d'autres règles comme garder votre code dans une limite de 80 ou 120 caractères par ligne.

De plus, l'indentation est l'une des règles qui apporte plus d'« air » au guide de style par défaut d'AirBnB. En conséquence, votre code ne s'entasse pas aussi mal sur le côté gauche de l'éditeur.

#### Espacement

C'est probablement la plus grande déviation par rapport au standard. Je déteste le code encombré. J'ai commencé à écrire du code avec un espacement supplémentaire il y a plus de 2 ans, et je ne suis jamais revenu en arrière.

Alors, que signifient ces règles ? Eh bien, jetez un coup d'œil au code suivant. Il respecte techniquement les règles du guide de style officiel d'AirBnB.

Je sais, c'est un peu confus. J'ai essayé de trouver une fonction de complexité moyenne dans l'une de mes bases de code, mais j'ai dû en obfusquer une grande partie, alors n'essayez pas de comprendre la logique derrière le code (parce qu'il n'y en a pas). Essayez simplement de le lire. Essayez de vous concentrer, par exemple, sur les variables qui sont utilisées à plusieurs endroits, lorsque des paramètres sont passés à des fonctions, et où se trouvent les appels de fonction.

Maintenant, jetez un coup d'œil au même code, mais avec les règles d'espacement supplémentaires appliquées :

Je ne dis pas que c'est maintenant hautement lisible, mais vous pouvez plus facilement identifier où vous avez des paramètres envoyés à des fonctions — surtout autour des fonctions currifiées.

Vérifiez également la différence entre l'indentation à 2 et à 4 espaces dans les deux exemples.

Au début, ces techniques peuvent ne pas sembler être une grande amélioration. Je vous encourage à les essayer. Je pense que vous verrez rapidement quelle différence cela fait.

#### Guerre des guillemets

Alors que les deux premières catégories avaient des arguments clairs, je dois dire que la décision entre les guillemets **simples** et **doubles** est hautement subjective.

Ma préférence pour les guillemets doubles vient probablement du fait que je travaille beaucoup avec React, où vous mélangez JavaScript avec des [balises JSX](https://facebook.github.io/react/docs/jsx-in-depth.html). Comme JSX est plus proche de HTML, la tendance est d'ajouter des attributs entre guillemets doubles. J'ai donc commencé à utiliser des guillemets doubles pour tout, simplement pour la cohérence.

Une chose que j'ai remarquée est que vous êtes beaucoup plus susceptible d'avoir besoin d'écrire un guillemet simple à l'intérieur d'une chaîne de texte anglais qu'un guillemet double (« Je suis ici », « Ne fais pas ça »). Les guillemets doubles peuvent donc être plus pratiques dans ces cas.

#### Organisation du code

Le guide de style officiel d'AirBnB a une règle « no-use-before-define », qui génère une erreur si vous essayez d'utiliser quelque chose avant de le définir. C'est une bonne règle — surtout pour les variables — car vous ne devriez pas dépendre du hoisting, et vous devriez garder à l'esprit le problème de la [zone morte temporelle](http://jsrocks.org/2015/01/temporal-dead-zone-tdz-demystified/) lorsque vous utilisez let et const.

Je préfère permettre aux fonctions d'être utilisées avant d'être définies. La raison est simple : la plupart du temps, vous allez décomposer vos fonctions en sous-fonctions plus petites. Cependant, la règle « no-use-before-define » vous dira de placer ces sous-fonctions **avant** la fonction originale.

Mais vos sous-fonctions sont là pour abstraire des parties de l'algorithme. Elles ne devraient pas vous déranger lorsque vous ouvrez un fichier contenant votre **fonction de haut niveau**, que vous utilisez à l'extérieur du fichier.

Bien sûr, cela est discutable. Mais cela a un impact sur le débogage. Lorsque vous parcourez du code et que vous trouvez un appel à une fonction différente, idéalement, vous devriez pouvoir regarder en dessous, ou — pire des cas — faire défiler quelques sous-fonctions et trouver ce que vous cherchez.

Cela, en combinaison avec la règle d'AirBnB sur la [déclaration de fonction contre l'expression de fonction](http://eslint.org/docs/rules/func-style), peut vous donner la liberté de structurer vos modules ou bibliothèques de fonctions comme vous le souhaitez, tout en vous assurant de ne pas appeler accidentellement une fonction non initialisée.

#### Const plutôt que let

Voici une autre petite déviation par rapport au guide de style. Vous pouvez remarquer dans ma configuration :

```
"prefer-const": 1
```

Dans la configuration d'AirBnB, cela est défini sur **2**, ce qui signifie _erreur_, tandis que **1** signifie _avertissement_.

Maintenant, si vous ne comprenez pas pourquoi vous devriez préférer const à let, vous pouvez en lire plus à ce sujet [ici](https://medium.freecodecamp.com/start-writing-modern-javascript-code-f98eccb4841#7d2a) et [ici](https://medium.com/javascript-scene/javascript-es6-var-let-or-const-ba58b8dcde75#.4ufsdmvkl).

Concernant ma déviation, je préfère un avertissement, car il existe des situations où vous ne changez pas l'affectation d'une variable, mais vous changez beaucoup de son contenu.

Jetez un coup d'œil à ce code :

Les règles vous diront que cela est correct — _hash_ devrait être _const_ car il n'est pas réaffecté. Mais cela n'a jamais vraiment eu de sens pour moi. Je devrais être conscient qu'il y a beaucoup de changements à l'intérieur de _hash_.

Je vais donc utiliser _let_ pour signaler le fait que la variable est sujette à changement. _const_ et _let_ devraient donner plus de sens à vos variables et ne devraient pas cacher la vérité de quelque manière que ce soit.

#### Complexité du code

Vous pouvez utiliser la [complexité cyclomatique du code](https://reactjsnews.com/composing-components) pour calculer la complexité de chacune de vos fonctions.

Décider d'un niveau maximum de complexité est délicat. Idéalement, il devrait être aussi bas que possible, ce qui signifie que vos fonctions devraient avoir au plus 1 ou 2 possibilités de branchement.

Il est logique d'avoir ce nombre aussi bas que possible du point de vue de la réutilisation du code et des tests. Mais il y a des moments où il est plus difficile de décomposer les fonctions. C'est pourquoi je vois la complexité plus comme un avertissement que comme une erreur.

L'important ici est de limiter le nombre de fonctions qui atteignent cette limite de complexité maximale. Même dans une base de code de taille moyenne, je n'aimerais pas voir plus de 10 fonctions qui enfreignent cette règle. J'ai donc choisi la valeur maximale de 5, afin de mettre en évidence ces fonctions. Je ciblerai ces fonctions lorsque j'aurai le temps de faire du refactoring.

La complexité peut être résolue de plusieurs manières. Le refactoring en fonctions plus petites est la solution évidente. Une autre option consiste à transformer vos instructions _switch_ en affectations de mappage.

Nous avons eu plusieurs débats au sein de notre équipe, et nous avons fini par utiliser 5 comme valeur de référence pour la règle de complexité maximale. Mais dans certains cas, nous descendons à 4, juste pour être sûrs que nous écrivons du code propre et simple.

#### Une note sur React

Parce que je travaille beaucoup avec React, et que la configuration d'AirBnB contient également un grand nombre de règles dans ce domaine, je voulais inclure certaines de mes préférences ici aussi.

L'objectif principal de mes substitutions React est de limiter la différenciation entre les modules JavaScript réguliers et les composants React, ainsi qu'entre le code JavaScript et le JSX. C'est pourquoi je choisis une indentation similaire et l'utilisation de guillemets doubles pour tous les attributs JSX. Et c'est pourquoi je préfère laisser tous mes fichiers avec l'extension .js.

Enfin, concernant les [composants de classe vs les composants de factory](https://reactjsnews.com/composing-components), je tends à préférer ces derniers. Je ne vois aucun avantage à utiliser des classes à ce stade. Je pourrais écrire un futur article pour expliquer pourquoi je ressens cela.

C'est à peu près tout ! J'espère que vous avez apprécié la lecture. Je suis ouvert à vos retours ci-dessous.

Si vous avez aimé l'article, cliquez sur le cœur vert ci-dessous, et je saurai que mes efforts ne sont pas vains.