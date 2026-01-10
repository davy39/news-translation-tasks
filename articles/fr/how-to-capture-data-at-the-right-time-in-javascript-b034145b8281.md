---
title: Comment capturer des données au bon moment en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:16:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-capture-data-at-the-right-time-in-javascript-b034145b8281
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TPwMsv_xEkHAdqJT
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment capturer des données au bon moment en JavaScript
seo_desc: 'By Jonathan Sexton

  I’ve always worked with the assumption that if I put enough time and effort towards
  anything, eventually I would get the outcome I desired. If I can throw enough hard
  work (and coffee :P) at my problem, I can build a great solution...'
---

Par Jonathan Sexton

J'ai toujours travaillé avec l'idée que si je mettais suffisamment de temps et d'efforts dans quoi que ce soit, j'obtiendrais finalement le résultat souhaité. Si je peux mettre assez de travail acharné (et de café :P) dans mon problème, je peux construire une excellente solution.

L'entêtement a été et continue d'être l'un de mes meilleurs et pires attributs. J'apprends qu'une approche lourde fonctionne rarement dans le monde de la programmation. Parfois, la situation exige des mains délicates et de la finesse pour obtenir le meilleur résultat. C'est la leçon que j'ai apprise, et la genèse de cet article.

J'espère qu'en partageant ce que j'ai appris (à la dure), cela vous fera gagner du temps et éviter des frustrations. Alors, sans plus attendre, voici la leçon de cette semaine sur le moment et l'endroit pour collecter des informations.

### Hypothèses

Je vais faire quelques hypothèses avant de commencer cet article, mais au cas où j'en ferais trop, j'ai fourni quelques liens. Si c'est votre première introduction à l'un de ces sujets, alors bienvenue ! Je serai plus qu'heureux de répondre à toutes les questions que vous pourriez avoir après avoir consulté quelques informations. Mes coordonnées se trouvent en bas de cet article.

* Vous connaissez les bases du [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
* Vous connaissez les bases du [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
* Utilisation de la balise [<li](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)nk> dans votre fichier HTML pour lier à une feuille de style [externe](https://developer.mozilla.org/en-US/docs/Web/CSS)
* Vous connaissez les bases de [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript) — y compris la [déclaration de variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) et les [écouteurs d'événements](https://developer.mozilla.org/en-US/docs/Web/API/EventListener)
* Utilisation de la balise [<li](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)nk> dans votre fichier HTML pour lier à un fichier JavaScript [externe](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
* Vous comprenez qu'un fichier [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) est chargé ([rendu](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction)) de manière linéaire, de haut en bas

Ne vous inquiétez pas si vous n'êtes pas familier avec tout ce qui est sur la liste. Je vous fournirai quelques liens tout au long de l'article, alors commençons.

### Rendu du document HTML

Tout au long de cet article, je ferai référence au code ci-dessous. Il s'agit d'un simple modèle HTML avec des champs [<inp](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)ut> dans lesquels l'utilisateur peut fournir des données sur le coût d'un nouveau téléphone (hypothétique).

![Image](https://cdn-media-1.freecodecamp.org/images/cZDjEkR41W8xmODPjsRFtgXnvh7x5UFmgqEh)

Ici, vous pouvez voir que ma balise <link> en haut du document pointe vers ma feuille de style externe. La balise <script> en bas du document pointe vers mon fichier JavaScript externe.

Lorsque ce document est rendu (voir le lien ci-dessus pour une description détaillée du rendu du navigateur), la feuille de style CSS sera rendue avant le fichier JavaScript. Cela est dû au fait qu'une grande partie de JavaScript est utilisée pour manipuler les éléments [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

Si la balise <script> est placée ailleurs qu'en bas du document HTML, alors le fichier JavaScript sera chargé et tentera de modifier des éléments qui n'existent pas encore. C'est un problème pour nous. C'est pourquoi la balise <script> est placée juste au-dessus de la balise <body>.

Il existe des situations où vous souhaiteriez que le JavaScript se charge avant cela et soit donc placé dans la balise <head>. Cela dépasse le cadre de cet article — sachez simplement que c'est possible.

### Collecte des valeurs

Ci-dessous se trouve le code dans le fichier JavaScript qui correspond à la balise <script> dans le document HTML ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/7AVj09rS2PAR5ujAaa1F8DYrmEWaiS73JeFF)

Ci-dessus, vous pouvez voir que j'ai déclaré quelques variables avec différents sélecteurs. (Voici mon guide rapide sur le choix du bon sélecteur JavaScript pour votre situation). Je veux enregistrer les valeurs de ces variables dans la console.

Mon intention ici est d'obtenir la valeur des champs _money_ et _newPhone_ avant de manipuler ces valeurs dans les itérations ultérieures de mon code. Il y a juste un problème — la façon dont j'ai structuré mon code entraîne des valeurs de variables vides.

Lorsque mes instructions _console.log_ s'exécutent, je me retrouverai avec _undefined_ comme valeurs pour ces variables. Maintenant, pourquoi cela, pourriez-vous demander ? Reprenons comment le HTML est rendu dans le navigateur. Tout attend essentiellement son tour pour être rendu alors que le navigateur parcourt le HTML. Donc, lorsque mes champs <input> sont rendus, ils sont vides parce que l'utilisateur n'a pas encore fourni d'informations dans ces champs.

Ensuite, je sélectionne ces champs d'entrée avec `let money = document.getElementById("money").value;` et `let newPhone = document.querySelector("#newPhone").value;` les définissant respectivement à rien parce qu'ils n'ont pas encore de valeurs.

Après que le HTML ait été chargé, mes sélecteurs JavaScript ont fait leur magie, l'utilisateur modifie alors les données (fournit des informations dans le champ), mais les valeurs de mes sélecteurs JavaScript ne changent jamais.

### La Solution

La solution à ce problème est simple, mais il m'a fallu plus de temps pour la comprendre que je ne voudrais l'admettre. Je peux placer mes variables pour ces champs d'entrée dans mon [écouteur d'événements](https://developer.mozilla.org/en-US/docs/Web/API/EventListener). Cela garantira que les données de ces champs ne sont pas collectées avant que le clic ne se produise. Bien sûr, à ce moment-là, les informations auront été saisies dans les champs (après que le HTML ait été rendu) et notre JavaScript n'aura aucun problème à récupérer ces données.

![Image](https://cdn-media-1.freecodecamp.org/images/h624UmWSsTl0jtHQKxPlZn5B-Dx2oTEa607n)

Il existe, comme pour tous les concepts de programmation, de nombreuses façons différentes d'accomplir cette tâche. La méthode ci-dessus est simplement celle que j'ai utilisée pour la résoudre. Si vous avez une autre méthode et souhaitez la partager, je serais ravi que vous la partagiez avec moi.

### Conclusion

Bien sûr, il existe des situations plus compliquées que celle que j'ai décrite ici. J'espère que cela vous donnera une base solide sur le moment de collecter des données à partir du DOM et comment votre code est affecté par ce timing.

Peu importe comment vous décidez de résoudre vos problèmes particuliers avec JavaScript, j'espère que vous aurez tiré au moins quelque chose de cet article. Si je peux vous faire gagner même cinq minutes de votre temps, alors je considérerai cela comme une victoire.

Si vous aimez cet article ou s'il vous a aidé, envisagez de faire un don en applaudissements, car cela aide les autres à trouver mon travail. J'adorerais aussi avoir de vos nouvelles ! Laissez un commentaire ou envoyez-moi un message sur [Twitter](https://twitter.com/jj_goose) — je suis toujours heureux de me connecter avec des visages amicaux et des développeurs !

J'ai aussi un [blog](https://www.jonathansexton.me/blog) où je publie des articles techniques liés au développement web front-end. Vous pouvez vous inscrire à ma newsletter pour rester à jour sur toutes mes aventures d'écriture. Assurez-vous de passer et de dire bonjour !

Comme toujours, passez une journée fantastique remplie de codage, d'amour, de famille et de bonheur !