---
title: Comment penser comme un programmeur
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-09-28T20:57:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-think-like-a-programmer-3ae955d414cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*otgsthXHixWZ8Xs_a4cl_g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment penser comme un programmeur
seo_desc: '“I don’t get JavaScript. I can’t make components from scratch. My mind
  goes blank when I stare at a blank JavaScript file. I guess I can’t do it because
  I don’t know how to think like a programmer.”

  Sounds familiar? You’re not alone, my friend. Many ...'
---

"Je ne comprends pas JavaScript. Je ne peux pas créer de composants à partir de zéro. Mon esprit devient vide lorsque je regarde un fichier JavaScript vide. Je suppose que je ne peux pas le faire parce que je ne sais pas comment **penser comme un programmeur**."

Cela vous semble familier ? Vous n'êtes pas seul, mon ami. Beaucoup de personnes qui essaient d'apprendre JavaScript comme premier langage de programmation font face au même problème.

En fait, même les développeurs qui codent déjà dans un autre langage rencontrent le même problème avec JavaScript. Au lieu de dire « Je ne peux pas penser comme un programmeur », ils disent « Je ne peux pas penser en JavaScript ».

Mais c'est fini. Que aujourd'hui soit le jour où vous apprenez à penser comme un programmeur.

### Vous pouvez déjà penser comme un programmeur.

Avez-vous essayé des exercices simples sur JavaScript sur des plateformes comme freeCodeCamp, Code Academy ou Code Wars ?

Si oui, vous savez déjà comment penser comme un programmeur.

La vraie raison pour laquelle votre esprit devient vide lorsque vous faites face à votre fichier JavaScript est probablement due au **syndrome de la page blanche du codeur**. Vous avez peur d'écrire du JavaScript qui ne fonctionne pas. Vous avez peur de faire face aux erreurs. Vous ne savez pas comment commencer.

Surmonter le syndrome de la page blanche du codeur est simple. Vous pouvez suivre ces quatre étapes :

1. Décomposer le problème en problèmes plus petits
2. Trouver des solutions à vos petits problèmes
3. Assembler les solutions de manière cohérente
4. Refactoriser et améliorer

Examinons de plus près chacune de ces étapes.

### Étape 1 : Décomposer le problème en problèmes plus petits.

Comment mettez-vous un éléphant dans le réfrigérateur ?

Voici ce que la plupart des gens répondraient :

1. Ouvrir le réfrigérateur
2. Mettre l'éléphant à l'intérieur
3. Fermer le réfrigérateur

Problème résolu.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PGDaDsFOBO6-NdQv.jpg)

Cette réponse est le meilleur exemple de pourquoi vous êtes bloqué lorsque vous faites face à un fichier JavaScript vide. **Elle saute des étapes**.

Si vous réfléchissez de manière logique à la question, vous verrez quelques problèmes flagrants qui restent sans réponse :

1. De quel réfrigérateur parlons-nous ?
2. De quel type d'éléphant parlons-nous ?
3. Si l'éléphant est trop gros pour entrer dans le réfrigérateur, que faites-vous ?
4. Où trouvez-vous l'éléphant en premier lieu ?
5. Comment transportez-vous l'éléphant jusqu'à votre réfrigérateur ?

Lorsque vous codez, vous devez répondre à chaque petite question à laquelle vous pouvez penser. C'est pourquoi la première étape consiste à décomposer votre problème en morceaux plus petits.

### Étape 2 : Trouver des solutions à vos petits problèmes.

La deuxième étape consiste à trouver une solution à chacun de vos petits problèmes. Ici, il est important d'être aussi détaillé que possible.

1. Quel réfrigérateur ? — le réfrigérateur qui se trouve dans votre cuisine
2. Quel type d'éléphant ? — l'[éléphant de brousse africain](https://en.wikipedia.org/wiki/African_elephant)
3. Que faire si l'éléphant est trop gros ? — Obtenir un pistolet rétrécisseur (?) pour rétrécir l'éléphant (?).
4. Où trouvez-vous l'éléphant ? — En Afrique
5. Comment transportez-vous l'éléphant ? — Mettez-le dans votre sac après l'avoir rétréci, puis prenez l'avion pour rentrer chez vous.

Parfois, vous devez creuser quelques couches pour obtenir la réponse dont vous avez besoin. Dans l'exemple ci-dessus, nous pouvons creuser plus profondément dans les réponses 3 et 4.

1. Où obtenez-vous le pistolet rétrécisseur ? — Empruntez-le au scientifique fou d'à côté.
2. Où en Afrique pouvez-vous trouver votre éléphant ? — Au parc national des éléphants d'Addo en Afrique du Sud.

Une fois que vous avez des réponses à tous vos petits problèmes, vous les assemblez pour résoudre votre grand problème.

### Étape 3 : Assembler les solutions de manière cohérente.

Donc, dans l'exemple de mettre-un-éléphant-dans-le-réfrigérateur, vous pouvez probablement suivre les étapes suivantes :

1. Obtenez un pistolet rétrécisseur du scientifique d'à côté
2. Prenez l'avion pour l'Afrique du Sud
3. Voyagez jusqu'au parc national des éléphants d'Addo
4. Trouvez un éléphant dans le parc
5. Tirez sur l'éléphant avec le pistolet rétrécisseur
6. Mettez l'éléphant rétréci dans votre sac
7. Retournez à l'aéroport
8. Prenez l'avion pour rentrer dans votre pays
9. Rendez-vous chez vous
10. Mettez l'éléphant dans votre réfrigérateur

Problème résolu.

Aussi intéressant que cela puisse paraître, vous ne capturerez probablement pas d'éléphants et ne les mettrez pas dans des réfrigérateurs avec JavaScript.

### Utilisons un exemple réel.

Disons que vous voulez créer un bouton qui, lorsqu'il est cliqué, affiche une barre latérale.

### Première étape — décomposer

Décomposez le composant en morceaux plus petits. Voici quelques problèmes que vous pourriez identifier :

1. Quelle est la structure de ce bouton ?
2. À quoi devrait ressembler le bouton ?
3. Que se passe-t-il lorsque le bouton est cliqué une fois ?
4. Que se passe-t-il lorsque le bouton est cliqué une deuxième fois ?
5. Que se passe-t-il lorsque le bouton est cliqué une troisième fois ?
6. Quelle est la structure de cette barre latérale ?
7. À quoi ressemble la barre latérale lorsqu'elle est affichée ?
8. À quoi ressemble la barre latérale lorsqu'elle est masquée ?
9. Comment la barre latérale apparaît-elle ?
10. Comment la barre latérale disparaît-elle ?
11. La barre latérale doit-elle s'afficher lorsque la page se charge ?

### Deuxième étape — créer des solutions pour les problèmes

Pour créer des solutions, vous devez avoir des connaissances sur le médium pour lequel vous créez. Dans notre cas, vous devez connaître suffisamment de HTML, CSS et JavaScript.

Ne vous inquiétez pas si vous ne connaissez pas la réponse à l'une de ces questions. Si vous les avez suffisamment décomposées, vous devriez pouvoir trouver une réponse via Google en cinq minutes.

Répondons à chacune des questions :

**Quelle est la structure de ce bouton ?**

La structure est une balise `<a>` avec une classe `.button`.

```
<a href="#" class="button">Cliquez-moi</a>
```

**À quoi devrait ressembler ce bouton ?**

Ce bouton devrait avoir le CSS suivant :

```
.btn {  display: inline-block;  font-size: 2em;  padding: 0.75em 1em;  background-color: #1ce;  color: #fff;  text-transform: uppercase;  text-decoration: none;}
```

**Que se passe-t-il lorsque le bouton est cliqué une fois ? Deux fois ? Trois fois ?**

La barre latérale devrait s'afficher lorsque le bouton est cliqué une fois. Cette barre latérale disparaît ensuite lorsque le bouton est cliqué une deuxième fois. Elle réapparaît lorsque le bouton est cliqué une troisième fois.

**Quelle est la structure de cette barre latérale ?**

La barre latérale devrait être une `<div>` qui contient une liste de liens :

```
<div class="sidebar">  <ul>    <li><a href="#">Lien 1</a></li>    <li><a href="#">Lien 2</a></li>    <li><a href="#">Lien 3</a></li>    <li><a href="#">Lien 4</a></li>    <li><a href="#">Lien 5</a></li>  </ul></div>
```

**À quoi ressemble la barre latérale lorsqu'elle est affichée ?**

La barre latérale devrait être placée à droite de la fenêtre. Elle doit être fixe pour que l'utilisateur la voie. Elle devrait faire 300px de large.

Lorsque vous avez fini de résoudre le problème, vous pourriez obtenir un CSS qui ressemble à ceci :

```
.sidebar {  position: fixed;  top: 0;  bottom: 0;  right: 0;  width: 300px;  background-color: #333;}.sidebar ul {  margin: 0;  padding: 0;}.sidebar li {  list-style: none;}.sidebar li + li {  border-top: 1px solid white;}.sidebar a {  display: block;  padding: 1em 1.5em;  color: #fff;  text-decoration: none;}
```

**À quoi ressemble la barre latérale lorsqu'elle est masquée ?**

La barre latérale devrait être décalée de 300px vers la droite, afin qu'elle soit hors de l'écran.

Lorsque vous répondez à cette question, deux autres peuvent surgir dans votre esprit :

1. Comment savez-vous si la barre latérale est affichée ou masquée ?
2. Comment stylisez-vous la barre latérale masquée ?

Répondons également à ces questions.

**Comment savez-vous si la barre latérale est affichée ou masquée ?**

Si la barre latérale a une classe `.is-hidden`, la barre latérale devrait être masquée. Sinon, elle devrait être visible.

**Comment stylisez-vous la barre latérale masquée ?**

Nous utilisons `translateX` pour décaler la barre latérale de 300px vers la droite, car `transform` est l'une des meilleures propriétés pour l'animation. Vos styles deviennent alors :

```
.sidebar.is-hidden {  transform: translateX(300px);}
```

**Comment la barre latérale apparaît-elle ?**

La barre latérale ne peut pas apparaître immédiatement. Elle doit se déplacer de la droite, où elle est masquée, vers la gauche, où elle est visible.

Si vous connaissez votre CSS, vous pourrez utiliser la propriété `transition`. Si vous ne la connaissez pas, vous pourrez trouver votre réponse via Google.

```
.sidebar {  /* autres propriétés */  transition: transform 0.3s ease-out;}
```

**Comment la barre latérale disparaît-elle ?**

Elle devrait disparaître de la même manière qu'elle apparaît, dans la direction opposée. Avec cela, vous n'avez pas besoin d'écrire de code CSS supplémentaire.

**La barre latérale doit-elle s'afficher lorsque la page se charge ?**

Non. Étant donné ce que nous avons, nous pouvons ajouter une classe `is-hidden` dans la structure de la barre latérale et la barre latérale devrait rester masquée.

```
<div class="sidebar is-hidden">  <!-- liens --></div>
```

**Maintenant, nous avons répondu à presque tout, sauf à une question — que se passe-t-il lorsque le bouton est cliqué une fois ? Deux fois ? Trois fois ?**

Notre réponse ci-dessus était trop vague. Nous savons que la barre latérale devrait apparaître lorsque vous cliquez dessus, mais comment ? La barre latérale devrait disparaître lorsque vous cliquez dessus à nouveau, mais comment ?

À ce stade, nous pouvons répondre à cette question à nouveau de manière plus détaillée. Mais avant cela, comment savez-vous lorsque vous avez cliqué sur un bouton ?

**Comment savoir lorsque vous cliquez sur un bouton.**

Si vous connaissez JavaScript, vous savez que vous pouvez ajouter un écouteur d'événement au bouton et écouter un événement `click`. Si vous ne le savez pas, vous pourrez le trouver sur Google.

Avant d'ajouter un écouteur d'événement, vous devez trouver le bouton dans la structure avec `querySelector`.

```
const button = document.querySelector('.btn')button.addEventListener('click', function() {  console.log('button is clicked!')})
```

**Que se passe-t-il lorsque le bouton est cliqué une fois ?**

Lorsque le bouton est cliqué une fois, nous devons supprimer la classe `is-hidden` pour que le bouton s'affiche. Pour supprimer une classe en JavaScript, nous utilisons `Element.classList.remove`. Cela signifie que nous devons d'abord sélectionner la barre latérale.

```
const button = document.querySelector('.btn')const sidebar = document.querySelector('.sidebar')button.addEventListener('click', function() {  sidebar.classList.remove('is-hidden')})
```

**Que se passe-t-il lorsque le bouton est cliqué deux fois ?**

Lorsque le bouton est cliqué à nouveau, nous devons ajouter la classe `is-hidden` à la barre latérale pour qu'elle disparaisse.

Malheureusement, nous ne pouvons pas détecter combien de fois un bouton est cliqué avec un écouteur d'événement. La meilleure façon est alors de vérifier si la classe `is-hidden` est déjà présente sur la barre latérale. Si elle l'est, nous la supprimons. Si elle ne l'est pas, nous l'ajoutons.

```
const button = document.querySelector('.btn')const sidebar = document.querySelector('.sidebar')button.addEventListener('click', function() {  if (sidebar.classList.contains('is-hidden')) {    sidebar.classList.remove('is-hidden')  } else {    sidebar.classList.add('is-hidden')  }})
```

Et avec cela, vous avez un prototype initial du composant.

[https://codepen.io/zellwk/pen/zdqmLe/](https://codepen.io/zellwk/pen/zdqmLe/)

### Quatrième étape — refactoriser et améliorer.

Nous avons incorporé la troisième étape, en assemblant nos solutions de manière cohérente, en cours de route. La dernière étape consiste à refactoriser et améliorer votre code. Cette étape peut ne pas vous venir naturellement pour l'instant. Cela demande des efforts et de la pratique avant de pouvoir dire si votre code peut être amélioré.

Alors, une fois que vous avez terminé les trois étapes, faites une pause et travaillez sur autre chose. Lorsque vous serez meilleur en JavaScript, vous remarquerez peut-être que vous avez manqué quelques détails en revenant.

Dans l'exemple ci-dessus, vous pouvez poser quelques questions supplémentaires :

1. Comment rendre ce composant de barre latérale accessible aux utilisateurs ayant des handicaps visuels ?
2. Comment rendre ce composant de barre latérale plus facile à utiliser pour les personnes utilisant des claviers ?
3. Pouvez-vous améliorer le code de quelque manière que ce soit ?

Pour le troisième point, si vous avez fait une recherche un peu plus approfondie, vous avez peut-être remarqué qu'il existe une méthode `toggle` qui supprime une classe si elle est présente. Si la classe n'est pas présente, la méthode `toggle` l'ajoute pour nous :

```
const button = document.querySelector('.btn')const sidebar = document.querySelector('.sidebar')button.addEventListener('click', function() {  sidebar.classList.toggle('is-hidden')})
```

### Conclusion

Penser comme un programmeur est simple. La clé est de savoir comment décomposer les problèmes en problèmes plus petits.

Lorsque vous avez terminé de décomposer le problème, trouvez des solutions à vos petits problèmes et codez-les. En cours de route, vous découvrirez d'autres problèmes auxquels vous n'aviez pas pensé auparavant. Résolvez-les également.

Au moment où vous aurez terminé d'écrire vos réponses à chaque petit problème, vous aurez la réponse à votre grand problème. Parfois, vous devrez peut-être assembler les étapes que vous avez écrites pour vos petits problèmes.

Enfin, le travail n'est pas terminé lorsque vous créez votre première solution. Il y aura toujours place à l'amélioration. Cependant, vous ne pourrez probablement pas voir les améliorations tout de suite. Faites une pause, travaillez sur autre chose et revenez plus tard. Vous pourrez alors poser de meilleures questions.

**Au fait, voulez-vous apprendre JavaScript mais ne savez pas comment commencer ? Si c'est le cas, essayez de suivre ce [JavaScript Roadmap](https://jsroadmap.com/) que j'ai construit pour vous. Vous y apprendrez comment surmonter vos barrières à l'apprentissage de JavaScript, et vous obtiendrez une feuille de route à suivre pour apprendre JavaScript correctement. Amusez-vous !**

(Si vous avez aimé cet article, j'apprécierais que vous me donniez quelques applaudissements et que vous le [partagiez](http://twitter.com/share?text=Great%20article%20by%20@zellwk:%20How%20to%20think%20like%20a%20programmer.&url=https://zellwk.com/blog/think/&hashtags=JavaScript,%20thinkLikeProgrammers). ?) Merci !

*Originalement publié sur [https://zellwk.com/blog/think/](https://zellwk.com/blog/think/).*