---
title: Maîtriser la console JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-20T21:02:13.000Z'
originalURL: https://freecodecamp.org/news/commanding-the-javascript-console-4e1caaeab345
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wUSjXYVzyV0nerQIIe8GCA.png
tags:
- name: debugging
  slug: debugging
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Maîtriser la console JavaScript
seo_desc: 'By Kyle Gill

  Useful tricks for debugging, formatting, and efficiency

  The console is one of the first tools developers learn about. The console is the
  tool developers use when debugging their own applications. The law of the instrument
  states that it’...'
---

Par Kyle Gill

#### Astuces utiles pour le débogage, la mise en forme et l'efficacité

La console est l'un des premiers outils que les développeurs apprennent à utiliser. La console est l'outil que les développeurs utilisent pour déboguer leurs propres applications. La [loi de l'instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument) stipule qu'il est facile de développer une confiance excessive dans un outil familier.

> « Je suppose qu'il est tentant, si le seul outil que vous avez est un marteau, de traiter tout comme si c'était un clou. » - Maslow

La même idée peut être appliquée à la console. Dans un écosystème où les outils, les raccourcis clavier et les API coulent comme le lait et le miel en terre promise, il est difficile de justifier l'adoption d'un nouveau marteau lorsque l'ancien fonctionne très bien. Croyez-moi cependant, ces trucs à pointes à l'arrière de votre marteau [ne servent pas seulement à arracher des clous](https://www.familyhandyman.com/tools/hammers-aren-t-just-for-nails-101-ways-to-use-a-rip-hammer/view-all/).

Ce qui suit sont quelques-unes des astuces les plus simples que j'ai trouvées pour le débogage dans la console.

#### #1 : Envelopper les arguments

Si vous enveloppez l'argument passé dans `console.log` dans des {} vous afficherez les données que vous enregistrez sous forme d'objet. L'objet aura un nom clair pour vous indiquer ce que vous essayiez d'afficher.

Plutôt que de voir un tas d'objets avec des champs similaires comme id et name dans votre console comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FvyeehvzCpelNj-pKSHPcg.png)

Vous obtiendrez le nom de la variable devant les données imprimées comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HZ7WTogIsT071Ag1uK_6ag.gif)
_À bas l'ambiguïté !_

#### #2 : Copier des données dans le presse-papiers

Vous pouvez copier des données enregistrées dans la console vers le presse-papiers de votre ordinateur. Je trouve cela utile lorsque vous souhaitez manipuler un objet dans un REPL ou extraire des données que vous déboguez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yxRiSSUeqr7Z-HSK2iU_-Q.gif)

Faites un clic droit à côté des données que vous souhaitez copier et sélectionnez « Stocker en tant que variable globale ». Cela sauvegardera les données en tant que variable dans la console avec un nom temporaire. (Si c'est la première fois que vous le faites dans une fenêtre de console, ce sera `temp1`.) Ensuite, vous pouvez utiliser la commande `copy()` en mettant le nom `temp1` comme argument. Cela copie les données stockées dans votre presse-papiers que vous pouvez coller comme vous le feriez pour tout autre élément que vous copiez.

C'est particulièrement utile lorsqu'une requête de base de données ne retourne pas de données dans un format qui correspond à la manière dont vos données sont manipulées sur le frontend. Vous pouvez montrer comment les données sont mutées ou transformées.

#### #3 : Court-circuiter les expressions

Si vous court-circuitez une expression avec un `||`, vous pouvez rendre le refactoring de code ou l'ajout d'une instruction de débogage beaucoup plus rapide. Cela est particulièrement utile avec les fonctions fléchées sur une ligne où vous souhaitez voir quelles données vous recevez en tant qu'argument.

```
// CELA
someFunction = data => (  <div>    <Component data={data} />  </div>)
```

```
// DEVIENT...
someFunction = data => console.log(data) || (  <div>    <Component data={data} />  </div>)
```

```
// PLUTÔT QUE...
someFunction = data => {  console.log(data)    return (    <div>      <Component data={data} />    </div>  )}
```

Vous évitez d'envelopper toute la fonction dans des accolades et d'ajouter un return. Cela peut sembler sans importance jusqu'à ce que vous optimisiez les performances et que vous le fassiez mille fois en essayant de comprendre quel péché égrégieux de React vous avez commis.

#### #4 : Log, Error, Warn

En plus de `console.log()`, la console dispose de plusieurs autres fonctions pour imprimer des données dans la console dans différents formats prédéfinis. Parmi celles-ci :

* `console.log()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*uWQAooSF_gUIYa1SDaRVgQ.png)

* `console.warn()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNH6EhI8d-V0-Le7dP7gAA.png)

* `console.error()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*jPEvpMtNVWWIu_EvyegIiw.png)

#### #5 : Formatage personnalisé pour la sortie de la console

Vous pouvez faire plus que simplement implémenter le formatage intégré avec `console.log`, `warn` et `error`. Vous pouvez jouer le rôle d'artiste où la console est votre toile !

Peut-être essayer d'imprimer un joli cadre autour de la sortie que vous souhaitez mettre en évidence :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DOCtgY_O8f_1mAq3UzLtIQ.png)
_Compétences requises : HTML, CSS et expérience en informatique quantique_

Voici ce snippet :

Vous pouvez également stocker du CSS à utiliser comme styles dans une variable à appliquer à la sortie. Vous pouvez surprendre vos collègues avec une touche d'arc-en-ciel pour suivre tout ce que vous produisez. Si vous voulez des arcs-en-ciel énormes suivant tout, essayez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dDcJa9FRxivPU_-aP_3l5Q.png)
_Efficace pour exprimer sa frustration_

#### #6 : Imprimer du JSON sous forme de tableau

Peu connu de beaucoup, la console dispose d'une méthode intégrée pour imprimer des données tabulaires sous forme de tableau. Cela peut être idéal pour parcourir rapidement des données JSON.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iX3XXABKkojWkFk-UbuF1g.gif)

#### #7 : Compter facilement

La méthode `console.count()` peut rendre le suivi du nombre de fois où vous avez atteint un point dans votre code vraiment simple. Vous n'avez plus besoin de parsemer votre code de variables d'incrémentation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9303rNoYjFIpTUS42OnWwQ.gif)

> Astuce pro : vous pouvez remplacer « number » par une étiquette d'une variable et il comptera combien de fois la méthode count avec cette étiquette a été atteinte.

J'ai trouvé cela utile pour déboguer les conditions de course ou les re-rendus inutiles dans une application React.

#### #8 : Utiliser des éléments DOM

Vous pouvez sélectionner un élément DOM dans l'onglet Éléments et y accéder avec `$0`. Le navigateur conservera en fait un historique où `$0` représente la sélection actuelle. `$1` représente la sélection précédente. `$2` l'avant-dernière sélection et ainsi de suite jusqu'à 5 éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q3EbqExsRdUy2y3VuJDGNg.gif)
_Avec une vitesse de frappe d'environ 15 mots par minute_

Vous pourriez vous demander : quand vais-je jamais vouloir changer le innerHTML de mon application depuis la console ? Et la réponse serait probablement seulement lorsque vous voulez un exemple GIF vraiment simple pour un article de blog. Mais cela aussi a ses cas d'utilisation.

#### #9 : L'instruction Debugger

Si vous avez déjà ajouté un console.log, ouvert les outils du navigateur et ajouté un point d'arrêt, pour voir ce qui se passe lorsque le code atteint ce point, libérez-vous avec l'instruction `debugger`.

Si vous ajoutez `debugger` sur une ligne dans votre JavaScript, le navigateur s'arrêtera et ouvrira les outils de débogage et mettra en pause l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hv31lQMyiy6kVJ9teHQdnA.gif)
_Raccourci !_

Bien que ce ne soit pas une fonctionnalité de la console, c'est une chose importante à savoir. Enregistrer des informations dans la console n'est pas aussi efficace ou performant que les outils de débogage intégrés aux navigateurs (comme l'onglet Sources de Chrome ou l'onglet Debugger de Firefox). Pour améliorer davantage votre débogage, consultez des ressources qui approfondissent ces outils.

Cependant, la console reste un moyen vraiment rapide et efficace de voir le flux d'application dans les apps où de nombreuses méthodes de cycle de vie différentes et des re-rendus sont déclenchés, et améliorer la façon dont vous les utilisez aussi vous rendra un meilleur développeur.

### Merci d'avoir lu !

Si vous avez vos propres astuces, n'hésitez pas à les partager ! J'adorerais avoir de vos nouvelles ici dans les commentaires, sur Twitter ou par email.

Si vous avez trouvé ce que vous avez lu intéressant ou utile, n'hésitez pas à laisser un ou deux applaudissements, à vous abonner pour les futures mises à jour, ou à retweeter/partager ce tweet : ?