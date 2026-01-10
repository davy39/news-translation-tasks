---
title: Comment éviter la frustration en choisissant le bon sélecteur JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T21:48:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-frustration-by-choosing-the-right-javascript-selector-73c64c3906b6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*M2VaorJmMb0RLa5m
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment éviter la frustration en choisissant le bon sélecteur JavaScript
seo_desc: 'By Jonathan Sexton

  A quick guide on how selectors affect your code

  While working on a project, I ran into an issue in my code. I was attempting to
  define multiple HTML elements into a collection and then change those elements based
  on some preset con...'
---

Par Jonathan Sexton

#### Un guide rapide sur la façon dont les sélecteurs affectent votre code

En travaillant sur un projet, je suis tombé sur un problème dans mon code. J'essayais de définir plusieurs éléments HTML dans une collection, puis de modifier ces éléments en fonction de certaines conditions prédéfinies. J'ai lutté pendant environ quatre heures de temps de codage (sur deux jours) en débogant mon code et en essayant de comprendre pourquoi je n'obtenais pas le résultat souhaité.

Il s'avère que j'avais utilisé _document.querySelectorAll()_ pour assigner mes éléments à une variable, puis j'essayais de modifier ces éléments. Le seul problème est que ce sélecteur JavaScript particulier retourne une **liste de nœuds [static](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)**. Comme il ne s'agit pas d'une représentation en direct des éléments, je n'ai pas pu les modifier plus tard dans mon code.

### **Hypothèses**

Dans cet article, je suppose que quelques choses sont vraies :

* Vous travaillez en JavaScript "vanille" (sans framework / bibliothèque)
* Vous avez une compréhension de base des éléments / sélecteurs JavaScript
* Vous avez une compréhension de base du DOM

### Le cœur du sujet

Au cas où j'aurais supposé trop de choses, j'ai fourni des liens vers des matériaux pertinents dans l'article que j'espère être utiles.

JavaScript est un écosystème si vaste et riche qu'il n'est pas surprenant qu'il existe de nombreuses façons d'accomplir la même tâche. Selon votre tâche, la manière dont elle est accomplie compte dans une certaine mesure.

Vous pouvez creuser un trou avec vos mains, mais il est beaucoup plus facile et plus efficace de le faire avec une pelle.

À cette fin, j'espère vous "tendre une pelle" après avoir lu cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/IXLL54yngArOlJqNfITubIlTMhXOrsMuhVkk)
_"Une photo en pose longue d'un groupe de personnes sur une plage avec des enfants creusant un trou profond" par [Unsplash](https://unsplash.com/@khurtwilliams?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Khürt Williams</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### **Choisir le bon outil pour le travail**

J'ai eu la question, "Quel sélecteur d'éléments devrais-je utiliser ?" plusieurs fois. Jusqu'à présent, je n'avais pas eu beaucoup d'envie ou de besoin d'apprendre la différence tant que mon code produisait le résultat souhaité. Après tout, quelle importance a la couleur du taxi tant qu'il vous amène à votre destination en toute sécurité et à temps... n'est-ce pas ?

Commençons par quelques façons de sélectionner les éléments [**DOM**](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) en JavaScript. Il existe plus de façons (je crois) de sélectionner des éléments, mais celles listées ici sont de loin les plus courantes que j'ai rencontrées.

#### [**document.getElementById()**](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

Ces sélecteurs ne retourneront jamais qu'un (1) seul élément car, par leur nature, les ID sont uniques et il ne peut y en avoir qu'un seul (avec le même nom) sur la page à la fois.

Il retourne un objet qui correspond à la chaîne passée. Il retourne **null** si aucun ID correspondant n'est trouvé dans votre HTML.

> Exemple de syntaxe -> document.getElementById('main_content')

Contrairement à certains sélecteurs que nous verrons plus tard dans l'article, il n'est pas nécessaire d'utiliser un # pour désigner l'ID de l'élément.

#### [**_document.getElementsByTagName()_**](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName)

Remarquez le "S" dans elements — ce sélecteur retourne **plusieurs** éléments dans une **structure de type tableau** connue sous le nom de [HTML collection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) — tout le document est recherché, y compris le [nœud racine](https://javascript.info/dom-navigation) (l'objet document) pour un nom correspondant. Ce sélecteur d'éléments commence en haut du document et continue vers le bas, recherchant des balises qui correspondent à la chaîne passée.

Si vous souhaitez utiliser des méthodes de tableau [natives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), vous n'avez pas de chance. À moins que vous ne convertissiez les résultats retournés en un tableau pour itérer dessus, ou que vous utilisiez l'opérateur de propagation [ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) — tous deux dépassant le cadre de cet article. Mais je voulais que vous sachiez qu'il est possible d'utiliser des méthodes de tableau si vous le souhaitez.

> Exemple de syntaxe -> document.getElementsByTagName('header_links'). Ce sélecteur accepte également p, div, body, ou toute autre balise HTML valide.

#### [**_document.getElementsByClassName()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)

Sélecteur de nom de classe — remarquez à nouveau le "S" dans elements — ce sélecteur retourne **plusieurs** éléments dans une **structure de type tableau** connue sous le nom de [HTML collection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) de noms de classe. Il correspond à la chaîne passée (peut prendre plusieurs noms de classe, bien qu'ils soient séparés par un espace), recherche tout le document, peut être appelé sur n'importe quel élément, et ne retourne que les descendants de la classe passée.

De plus, aucun . (point) n'est nécessaire pour désigner le nom de la classe.

> Exemple de syntaxe : _document.getElementsByClassName('className')

#### [**_document.querySelector()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

Ce sélecteur ne retournera jamais qu'un (1) seul élément.

Seul le premier élément correspondant à la chaîne passée sera retourné. Si aucun élément correspondant à la chaîne fournie n'est trouvé, **null** est retourné.

> Exemple de syntaxe : _document.querySelector('#side_note')_ ou _document.querySelector('.header_links')

Contrairement à tous nos exemples précédents, ce sélecteur nécessite un . (point) pour désigner une classe ou un _#_ (octothorpe) pour désigner un ID et fonctionne avec tous les sélecteurs CSS.

#### [**_document.querySelectorAll()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)

Ce sélecteur retourne **plusieurs** éléments qui correspondent à la chaîne passée et les organise dans une autre **structure de type tableau** connue sous le nom de [node list](https://developer.mozilla.org/en-US/docs/Web/API/NodeList).

Comme pour certains des exemples précédents, la liste de nœuds ne peut pas utiliser les méthodes de tableau [natives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) comme [.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach). Donc, si vous souhaitez les utiliser, vous devez d'abord convertir la liste de nœuds en un tableau. Si vous ne souhaitez pas convertir, vous pouvez toujours itérer sur la liste de nœuds avec une instruction [for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).

La chaîne passée doit correspondre à un sélecteur CSS valide — id, noms de classe, types, attributs, valeurs d'attributs, etc.

> Exemple de syntaxe : _document.querySelectorAll('.footer_links')

### Conclusion

En choisissant le bon sélecteur pour vos besoins de codage, vous éviterez de nombreux pièges dans lesquels je suis tombé. Cela peut être incroyablement frustrant lorsque votre code ne fonctionne pas, mais en vous assurant que votre sélecteur correspond à vos besoins situationnels, vous n'aurez aucun problème à "creuser avec votre pelle" :)

Merci d'avoir lu cet article. Si vous l'avez apprécié, envisagez de faire un don de quelques applaudissements pour aider les autres à le trouver également. Je publie (en gérant activement mon emploi du temps pour écrire davantage) du contenu lié sur mon [blog](https://www.powerofgoose.com/blog). Je suis également actif sur [Twitter](https://twitter.com/jj_goose) et suis toujours heureux de me connecter avec d'autres développeurs !