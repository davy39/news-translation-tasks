---
title: Ce qui est journalisé dans la console lorsque vous modifiez des objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T19:44:37.000Z'
originalURL: https://freecodecamp.org/news/mutating-objects-what-will-be-logged-in-the-console-ffb24e241e07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PePMIr6hsZ70wtXX_mDCsw.png
tags:
- name: coding
  slug: coding
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Ce qui est journalisé dans la console lorsque vous modifiez des objets
seo_desc: 'By Boris Sever

  A lot of developers are not using a debugger while developing. Instead they are
  relying on their old friend console.log().

  It is important to note that the console shows the object’s value which is evaluated
  at the time of the first ex...'
---

Par Boris Sever

Beaucoup de développeurs n'utilisent pas de débogueur pendant le développement. Au lieu de cela, ils s'appuient sur leur vieil ami `console.log()`.

Il est important de noter que la console affiche la valeur de l'objet qui est évaluée au moment de la **première expansion** dans la console.

Tout d'abord, laissez-moi clarifier ce que je veux dire par expansion. Lorsque nous utilisons `console.log` sur un objet (ce qui inclut également les tableaux), la valeur de l'objet est réduite. Par exemple :

`console.log( "users: ", [{name: "John"}]);`

La console du navigateur ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NOVGoKXu4ZAHsqA2Uvzx4g.png)

Ensuite, lorsque vous cliquez sur le triangle, l'objet s'expand. À ce moment précis, la valeur de l'objet est évaluée et affichée.

Approfondissons ce sujet et examinons un exemple :

À la ligne 1, nous initialisons une nouvelle variable `users`, qui est un tableau d'objets.

À la ligne 6, nous écrivons la valeur de la variable `users` dans la console.

Ensuite, nous parcourons `users`, vérifions si l'utilisateur est valide, et selon le retour, nous désactivons l'utilisateur. Pour l'argument, supposons que `validateUser()` retourne `false` et que le code de la ligne 10 est exécuté.

Même si `map` crée un nouveau tableau, la modification de l'objet `user` modifie également l'objet `user` dans le tableau `users`. Il change parce qu'il a la même référence. (Pour une meilleure explication de ce qui se passe, consultez [cet article](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0)).

**La question est : que sera affiché dans la console qui est appelée à la ligne 6 ?**

Lorsque nous ouvrons cet exemple dans Chrome et Firefox, l'objet est réduit. Ensuite, lors de l'expansion, nous voyons les valeurs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zri_rWMD3yqBmrzCzw0UKQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*StVzIGl8SQnG1SBVNMBDMQ.png)

Enabled est défini sur `false`, même si la valeur était `true` au moment de la sortie. La raison en est que la valeur de l'objet est évaluée la première fois lorsque nous cliquons pour développer l'objet (lecture paresseuse).

> _Note : Chrome affichera une icône d'information qui indique : « La valeur ci-dessous a été évaluée juste maintenant. »_

Regardons maintenant Safari :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FsKGB4JmFTUCNXt6-HWckA.png)
_Safari (version 11.0.3)_

Hm, enabled est défini sur true. Nous pouvons donc voir qu'il y a certaines incohérences entre les navigateurs. Safari essaiera d'expander l'objet automatiquement. Si l'objet/tableau est trop grand, il se réduira et se comportera de la même manière que Chrome et Firefox.

Une façon de contourner cela est d'utiliser `JSON.stringify()`, par exemple :
`console.log("users", JSON.stringify(users, null, 2));`

ce qui produira la sortie suivante dans la console :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vpDy5W8XC9d9egowdnlrxw.png)

Malheureusement, avec cette approche, vous ne pouvez pas expander/rétracter un objet. La valeur ne sera pas modifiée.

Je suis un grand fan du paradigme de la programmation fonctionnelle et des variables immuables. Pour modifier l'objet, vous créez un clone qui est ensuite modifié. Dans ce cas, vous ne rencontreriez pas ce genre de « problème ». Nous pourrions donc écrire quelque chose comme ceci :

Dans la fonction map, nous clonons maintenant l'objet user que nous modifions et retournons.

Au cas où vous restez avec la mutation d'objets, [Zoran Jambor](https://www.freecodecamp.org/news/mutating-objects-what-will-be-logged-in-the-console-ffb24e241e07/undefined) a ajouté une autre solution astucieuse :
`console.log("users", ...users);`

Ainsi, le tableau users est déstructuré et une liste d'objets est affichée dans la console :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gwCP36E8dG742zoIvgm9TQ.png)

Mais ici aussi, nous devons être prudents. Si la valeur de l'objet a été modifiée, la sortie de la console changera lors de l'expansion :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RRgBmR9HwBbFdrVCU5AOww.png)

Si vous voulez être absolument sûr que l'objet, qui a été journalisé, a la même valeur qu'au moment du console.log, vous devrez en faire un clone profond. Par exemple, nous pourrions utiliser la fonction auxiliaire suivante au lieu d'écrire directement dans la console :

À la ligne 3, nous créons en fait un clone profond de l'objet, ce qui donne la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YZ4sbglklsKS_AFcWIufRQ.png)

Maintenant, la valeur de l'objet n'est pas modifiée lors de l'expansion.

Si vous utilisez un débogueur, l'ajout d'un point d'arrêt à la ligne 6 mettra en pause l'exécution. Vous verrez la valeur actuelle de l'objet. Si vous préférez la console la plupart du temps, sachez que l'objet/tableau est évalué lors de la première expansion.

Consultez [cet excellent article](https://medium.com/datadriveninvestor/stopping-using-console-log-and-start-using-your-browsers-debugger-62bc893d93ff) sur la façon d'utiliser le débogueur de votre navigateur.

Merci d'avoir lu. Veuillez le partager avec toute personne qui pourrait le trouver utile et laissez des commentaires. (C'est mon premier article sur Medium, et j'aimerais continuer à écrire et à m'améliorer.)