---
title: Comment fonctionne la propriété Z-index – Ordre d'empilement des éléments en
  CSS
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2023-02-09T22:48:03.000Z'
originalURL: https://freecodecamp.org/news/z-index-property-and-stacking-order-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/stacked-books-1.jpg
tags:
- name: CSS
  slug: css
- name: DOM
  slug: dom
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la propriété Z-index – Ordre d'empilement des éléments
  en CSS
seo_desc: "If you're a front-end engineer, you've probably faced weird z-index bugs\
  \ and ended up spending hours trying to fix them. \nChange one property here and\
  \ you have your header flying away from where it was meant to be. \nWell, we can\
  \ attribute this to the..."
---

Si vous êtes un ingénieur front-end, vous avez probablement rencontré des bugs étranges avec z-index et fini par passer des heures à essayer de les corriger. 

Changez une propriété ici et vous voyez votre en-tête s'envoler loin de l'endroit où il était censé être. 

Eh bien, nous pouvons attribuer cela au fait que le débogage CSS peut être assez difficile et que la plupart du temps, nous le faisons à l'aveugle. Nous changeons des propriétés en espérant voir les bugs se résoudre magiquement, mais ils ne le font pas. 

Contrairement à JavaScript qui vous crie dessus, vous donnant des indices sur ce que vous faites, CSS se contente de vous regarder faire n'importe quoi et espère silencieusement que vous allez comprendre.

L'une des nombreuses façons de devenir vraiment bon en CSS est de rechercher et de comprendre le mécanisme derrière certaines propriétés CSS que vous utilisez tous les jours. 

Cela vous donnera une connaissance technique claire et concise sur la façon d'implémenter certains designs compliqués. Cela vous donnera également un aperçu de la façon de résoudre certains bugs difficiles et inexplicables que vous pourriez rencontrer en écrivant du code.

## Le problème avec la propriété Z-index en CSS

Nous pouvons tous convenir que l'une des propriétés CSS les plus étranges, les plus déroutantes et les moins intuitives est le `z-index`. 

Lorsque j'ai commencé à apprendre CSS, certains instructeurs m'ont dit que vous utilisez `z-index` lorsque vous voulez qu'un certain élément DOM (Document Object Model) soit au-dessus d'un autre. Cela semble simple, n'est-ce pas ? 

Je l'ai pensé – mais l'expérience de la vie a une façon de nous faire savoir que les choses ne sont pas toujours aussi faciles que nous le pensions.

Ne pas comprendre comment la propriété `z-index` fonctionne réellement en coulisses m'a conduit à un trou de lapin frustrant de bugs inexplicables liés à `z-index`. J'ai donc commencé à augmenter la valeur `z-index` à des nombres énormes comme le célèbre `99999` pour voir si je pouvais obtenir le résultat souhaité.

Parfois cela fonctionne, mais d'autres fois cela ne fonctionne pas, ce qui peut être la chose la plus ennuyeuse parce que cela a fonctionné l'autre fois. 

Une autre situation est lorsque cela fonctionne bien au début, mais ensuite, à mesure que vous avancez dans votre travail, vous rencontrez à nouveau le même problème sur une autre partie de votre application. Vous vous retrouvez donc à faire le défaut – augmenter le nouveau `z-index` jusqu'à `99999999`, un nombre encore plus grand que le précédent.

Au fond de votre cœur en tant que développeur professionnel, vous savez que ce n'est pas correct. C'est un désordre (et personnellement, je déteste le code CSS désordonné). Mais vous savez aussi que vous n'avez aucune idée de la façon d'aborder le problème qui conduira à une solution permanente et à une victoire dans vos guerres de `z-index`.

Si vous lisez cet article et que vous voulez comprendre le `z-index` une fois pour toutes, vous êtes au bon endroit. 

Je vais vous aider à démystifier le `z-index`. À la fin de ce guide, j'espère que vous saurez comment corriger les bugs difficiles de `z-index` et comment le `z-index` fonctionne réellement. Vous aurez également une compréhension plus profonde et plus fondamentale de la façon dont les navigateurs rendent les éléments DOM et comment cela se rapporte au z-index. 

Prêt ? Plongeons directement.

## Qu'est-ce que le contexte d'empilement en CSS ?

Avant même de commencer à comprendre le `z-index` dans toute sa gloire, il sera à votre avantage si vous pouvez, pour un moment, faire semblant de ne rien savoir sur le `z-index`. Oubliez ce que vous savez à ce sujet, car à partir de maintenant, votre modèle mental sur le `z-index` est sur le point de changer.

Il n'y a pas de fumée sans feu, et le feu qui alimente la propriété `z-index` est un concept appelé **contexte d'empilement**. Dans la section suivante, nous allons passer en revue la signification de ce terme, ce qu'il signifie réellement en pratique, comment il fonctionne et comment il se rapporte au `z-index`.

Le contexte d'empilement est simplement un terme que nous utilisons pour définir comment le navigateur décide quels éléments dans le DOM viennent en premier et lesquels "rendre" au-dessus. 

Lorsque nous commençons à écrire un bloc de code HTML, un élément après l'autre, la manière naturelle dont le navigateur décide quel élément vient au-dessus est en vérifiant l'ordre des éléments DOM. Voir le bac à sable Codepen ci-dessous pour plus de détails :

%[https://codepen.io/developeraspire5/pen/eYjavqm]

```html
<div class="green-box">  </div>
<div class="pink-box">  </div>
<div class="blue-box">  </div>
```

```css
div{
  width: 100px;
  height: 100px;
  border: 3px solid;

}

.green-box{
  background-color: green;
}
.pink-box{
  background-color: hotpink;
  margin-top: -30px;
  margin-left: 20px;
}
.blue-box{
  background-color: blue;
  margin-top: -30px;
  margin-left: 40px;
}
```

Dans l'exemple ci-dessus, vous pouvez voir comment le navigateur empile les éléments DOM. Il le fait simplement en vérifiant l'ordre DOM de chaque élément, et en rendant l'élément ultérieur au-dessus de l'élément précédent. 

Pensez-y de cette manière – comment empilez-vous les livres ? Le dernier apparaît toujours au-dessus, le premier est toujours celui du bas. Lorsque vous voyez des livres empilés, vous savez déjà que celui du bas de la pile était le premier livre à être ajouté à la pile (il a commencé la pile) et celui du haut de la pile était le dernier à être ajouté à la pile.

Dans l'exemple ci-dessus, la boîte bleue est au-dessus car elle est la dernière de la pile telle qu'interprétée par le navigateur, tandis que la boîte verte est au bas de la pile car elle est le premier élément dans l'ordre DOM.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/stacked-books.jpg)
_Une représentation picturale de la façon dont le navigateur rend les éléments DOM - montrée comme des livres empilés._

Le processus de décision du navigateur sur quel élément DOM doit être peint et rendu au-dessus de l'autre élément est appelé le **contexte d'empilement**. Gardons cela à l'esprit car nous ferons référence à ce terme pendant le reste de l'article.

Chaque fois qu'un contexte d'empilement est créé, c'est un mémo envoyé au navigateur lui demandant de réévaluer les éléments DOM et de les rendre/empiler en conséquence.

Maintenant que nous avons vu et compris ce que signifie un contexte d'empilement et comment le navigateur rend les éléments DOM, passons à d'autres propriétés `CSS` qui ont la capacité d'affecter la façon dont le navigateur prend ces décisions.

## Éléments positionnés en CSS

Il y a une règle de base que je veux que vous vous souveniez toujours lorsque vous combattez quotidiennement avec `CSS`, surtout lorsque vous travaillez avec `z-index` et le contexte d'empilement : **"Les éléments positionnés viennent toujours au-dessus"**. 

Que signifie cela ? Découvrons-le ci-dessous :

%[https://codepen.io/developeraspire5/pen/OJwYmNB]

```html
<div class="green-box">  </div>
<div class="pink-box">  </div>
<div class="blue-box">  </div>
```

```css
div{
  width: 100px;
  height: 100px;
  border: 3px solid;

}

.green-box{
  background-color: green;
  position: relative;
}
.pink-box{
  background-color: hotpink;
  margin-top: -30px;
  margin-left: 20px;
}
.blue-box{
  background-color: blue;
  margin-top: -30px;
  margin-left: 40px;

}
```

Le voilà ! Que s'est-il passé ? Dans l'extrait de code Codepen que j'ai partagé ci-dessus, nous avons vu comment le navigateur a rendu les boîtes. En raison de leur ordre DOM, la boîte verte était plus bas dans la pile que ses pairs. 

Mais maintenant, elle est au-dessus des autres. À partir du résultat dans le bac à sable Codepen, nous pouvons clairement voir que la boîte verte est rendue au-dessus de la boîte rose. Comment ?

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-48.png)
_La boîte verte étant rendue au-dessus du reste des autres éléments_

Tout comme la règle de base l'a clairement indiqué, définir la propriété de position sur n'importe quel élément dans le DOM indique au navigateur de recalculer ses calculs. Ensuite, après ces calculs, le navigateur a décidé de rendre l'élément DOM avec la propriété de position au-dessus de tout autre élément, indépendamment de leur ordre DOM.

Il est également intéressant de noter que peu importe le nombre de valeurs `z-index` que nous ajoutons pour les autres éléments, ils ne viendront jamais au-dessus d'un élément positionné. Oui ! Je sais que vous venez d'avoir ce moment de révélation euphorique de "Donc c'était la cause de mon bug l'autre jour au travail". 

Vous pouvez jouer avec le bac à sable en ajoutant une propriété `z-index` aux autres éléments et en ajoutant une valeur élevée pour voir le résultat – allez jusqu'à 500 même. Je vous assure qu'aucun de ces éléments ne sera placé au-dessus de l'élément positionné.

**Note :** Cela ne s'applique pas à `position: static`. Cela est dû au fait que `position: static` est la valeur de position par défaut assignée par `CSS` à tous les éléments DOM. Vous pouvez le vérifier en modifiant le bac à sable ci-dessus pour avoir `position: static`.

Vous pensez probablement : "oh bien, que se passe-t-il si plus d'un élément a la propriété `position` définie. Si vous êtes confronté à ce scénario, qui gagne la guerre du contexte d'empilement ?".

Tout d'abord, j'aimerais que vous l'essayiez. Essayez de modifier le bac à sable ci-dessus et de définir les propriétés de position sur les deux autres éléments.

Lorsque cela se produit, nous avons simplement égalisé tous les éléments en définissant une propriété `position`. Lorsque le navigateur voit cela, il revient à sa manière par défaut d'empiler ces éléments en suivant leur ordre DOM. Il rend donc à nouveau l'élément ultérieur sur l'élément précédent, tout comme nous empilons des livres. Consultez l'extrait de code ci-dessous pour une compréhension appropriée.

%[https://codepen.io/developeraspire5/pen/oNMRwbQ]

```html
<div class="green-box">  </div>
<div class="pink-box">  </div>
<div class="blue-box">  </div>
```

```css
div{
  width: 100px;
  height: 100px;
  border: 3px solid;

}

.green-box{
  background-color: green;
  position: relative;
}
.pink-box{
  background-color: hotpink;
  margin-top: -30px;
  margin-left: 20px;
  position: relative;
}
.blue-box{
  background-color: blue;
  margin-top: -30px;
  margin-left: 40px;
  position: relative;

}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-49.png)

C'est ainsi que fonctionne le contexte d'empilement dans le navigateur. Adopter ce modèle mental est l'une des façons fondamentales de vraiment comprendre comment fonctionne le `z-index`.

À partir des explications ci-dessus et des extraits de code que nous avons vus, vous vous demandez peut-être : si le `z-index` ne fonctionne pas lorsque nous essayons de l'utiliser lorsque les éléments frères ont la propriété `position` définie, comment l'utilisons-nous alors ? 

Eh bien, ce que nous venons de vivre est la manière dont le navigateur décide du contexte d'empilement par défaut. Le `z-index` est simplement une propriété qui nous permet de remplacer cette valeur par défaut.

Mais cela vient avec ses propres règles. Nous allons explorer cela dans la section ci-dessous.

## Comment utiliser la propriété Z-index

Si nous cherchons à changer la façon dont les choses fonctionnent et à nous désengager de la manière par défaut dont le navigateur rend et empile les éléments DOM, `CSS` nous a fourni une propriété appelée `z-index`. Et nous pouvons l'utiliser pour y parvenir.

Tout d'abord, démystifions la propriété tout-puissante `z-index` : 

Le `z` dans `z-index` fait référence à l'`axe z`. L'`axe z` représente la partie tridimensionnelle d'un élément.

* `axe x` est gauche et droite
* `axe y` est haut et bas
* `axe z` est avant et arrière

Le modèle mental est que `z-index` fonctionne comme en 3D – les éléments avec un `z-index` plus élevé sont élevés et poussés plus près de la vue de l'utilisateur dans le navigateur afin qu'il semble qu'ils soient au-dessus/devant le reste des autres éléments. 

C'est la même façon dont fonctionnent les panneaux d'affichage 3D, en poussant les images plus près de nous optiquement afin que cela donne presque l'impression que les personnages de ces panneaux d'affichage sortent de l'écran. Le `z-index` partage le même concept qu'un panneau d'affichage 3D.

Tout comme chaque autre propriété CSS avec des valeurs par défaut, la valeur par défaut pour la propriété `z-index` est `auto`, qui peut être interprétée comme `zéro`. 

Lorsque nous utilisons `z-index` sur n'importe quel élément DOM, ajouter une valeur de 1 ou plus est un commandement/signal direct qui indique au navigateur de pousser cet élément DOM particulier afin qu'il se place juste devant ses frères.

Pour pouvoir utiliser `z-index` efficacement, il existe certaines règles qui guident son fonctionnement. Comprendre et bien assimiler comment ces règles s'appliquent est très important car cela vous rapproche d'un pas de la libération de la lutte avec `z-index` et des bugs inutiles. Consultez l'extrait de code ci-dessous :

%[https://codepen.io/developeraspire5/pen/PoBvjOP]

```html
<div class="green-box">  </div>
<div class="pink-box">  </div>
<div class="blue-box">  </div>
```

```css
div{
  width: 100px;
  height: 100px;
  border: 3px solid;

}

.green-box{
  background-color: green;
  z-index: 6;
}

.pink-box{
  background-color: hotpink;
  margin-top: -30px;
  margin-left: 20px;
}
.blue-box{
  background-color: blue;
  margin-top: -30px;
  margin-left: 40px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-52.png)
_Même après avoir ajouté une grande valeur de z-index à la boîte verte, elle ne vient toujours pas au-dessus de la boîte rose_

N'est-il pas surprenant que, après avoir défini une valeur `z-index` de `6` (un nombre relativement grand pour `z-index`), le contexte d'empilement ne change pas ? 

L'attente après avoir fait cela est de voir la boîte verte rendue au-dessus du reste des boîtes (puisque bien sûr nous savons que `z-index` est utilisé pour obtenir un élément au-dessus du reste).

Mais dans ce cas, cela ne fonctionne pas. Des moments comme celui-ci mènent à une frustration sans fin et à s'arracher les cheveux avec la question rhétorique : "Pourquoi ne fonctionne-t-il pas ?" et finalement une mauvaise journée au travail. 

Je vous présente la première règle du z-index :

### `z-index` ne fonctionne qu'avec les éléments positionnés.

Maintenant, je veux que vous alliez modifier le bac à sable et que vous définissiez `position: relative` sur la boîte verte et que vous voyiez le résultat. Essayez en modifiant le bac à sable Codepen ci-dessus.

Si vous l'avez fait, vous verrez immédiatement que la boîte verte est maintenant rendue au-dessus et que le navigateur a recalculé le contexte d'empilement et rendu les éléments DOM en conséquence via les nouvelles informations qu'il a reçues. Souvenez-vous toujours de cette première règle. Voir la première règle en action ci-dessous :

%[https://codepen.io/developeraspire5/pen/LYBoLrv]

```html
<div class="green-box">  </div>
<div class="pink-box">  </div>
<div class="blue-box">  </div>

```

```css
div{
  width: 100px;
  height: 100px;
  border: 3px solid;

}

.green-box{
  background-color: green;
  z-index: 6;
  position: relative;
}
.pink-box{
  background-color: hotpink;
  margin-top: -30px;
  margin-left: 20px;
}
.blue-box{
  background-color: blue;
  margin-top: -30px;
  margin-left: 40px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-50.png)
_Après avoir défini une propriété de position sur la boîte verte, le z-index fonctionne maintenant correctement, rendant la boîte verte au-dessus._



Prochaine étape est la deuxième règle – mais avant d'entrer dans les détails et de comprendre ce que fait cette règle, je veux vous présenter un petit bug. Et je veux que vous voyiez si vous savez ce qui se passe et si vous pouvez le résoudre. 

Si vous ne pouvez pas, ne vous inquiétez pas, car je vais l'expliquer en détail ci-dessous.

%[https://codepen.io/developeraspire5/pen/MWBdEXe]

```html
<body>
  <header> This is a header </header>
  <main> <p>Hello there I am the main </p>
    <button> Click me </button>
  
  </main>
  
</body>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@200..900&display=swap');
body{
  font-family: 'Mulish', sans-serif;
  
}
header {
  background-color: hotpink;
  text-align: center;
  padding: 30px;
  position: relative;
  z-index: 2;
}

main {
  text-align: center;
  background-color: blue;
  color: white;
  padding: 30px;
  position: relative;
  z-index: 1;

}
button {
  margin: 0 auto;
  width: 90px;
  border: none;
  text-align: center;
  padding: 8px;
  background: white;
  box-shadow: 1px 2px 8px hsl(0deg 0% 0% / 0.25);
  border-radius: 6px;
  
  position: absolute;
  z-index: 999999;
  top: -12px;
}

```

Dans l'extrait de code ci-dessus, nous avons vu un autre problème de `z-index` qui peut conduire à des heures de débogage sans même savoir ce qui ne va pas. 

En parcourant le code, nous pouvons voir que le `button` a un nombre exorbitant comme valeur de `z-index`, et pourtant il ne se place pas au-dessus de l'en-tête. Cela pourrait vous faire faire un pas en arrière et réfléchir à la première règle du `z-index` et dire "Mais c'est un élément positionné, pourquoi cela ne fonctionne-t-il pas ?".

Cela nous amène à la deuxième règle du `z-index` :

### Une propriété `z-index` dans un contexte d'empilement isolé n'est pas prise en compte en dehors du contexte d'empilement isolé.

Que signifie cela ? Laissez-moi le décomposer :

D'après le code ci-dessus, nous pouvons voir que le `main` a une propriété `position` et également une propriété `z-index`. La même chose s'applique à l'élément `header` – le navigateur a utilisé cette valeur et calculé le contexte d'empilement. Puisque le `header` a une valeur `z-index` plus élevée, il l'a rendu au-dessus. C'est aussi simple que cela.

Maintenant, le `button` est un enfant de `main` qui a également la propriété `position` définie. Il a également un `z-index` défini à un nombre encore plus élevé. 

En référence à la deuxième règle, puisque `main` a la propriété `z-index` qui crée ce que l'on appelle un **contexte d'empilement isolé**, l'élément `button` n'est pas pris en compte lorsque le navigateur essaie de calculer le nouveau contexte d'empilement.

Vous pouvez aller de l'avant et supprimer la propriété `z-index` sur l'élément `main` et voir ce qui se passe.

Si vous l'avez fait, vous avez probablement vu que immédiatement le `button` a été rendu au-dessus de l'élément `header`. 

Cela peut être assez déroutant au début, mais faites-moi confiance – lorsque vous l'utilisez et pratiquez davantage avec, cela restera. J'ai une analogie pour vous aider à créer un modèle mental lorsque vous pensez à cette deuxième règle :

### Analogie du capitaine

Dans un avion, il y a généralement 2 pilotes, tous deux également qualifiés pour piloter et commander un avion. Mais un seul de ces 2 pilotes est réellement choisi pour être le capitaine de ce vol spécifique. Tant que le pilote choisi n'est pas absent, malade ou blessé pendant le vol, il n'est pas nécessaire que le deuxième pilote assume le rôle de capitaine. 

Mais dans une situation où quelque chose de grave arrive au pilote choisi, le deuxième pilote est autorisé et mandaté pour être capitaine.

Utilisez cette même analogie sur le `main` et le `button`, `main` a déjà été assigné un capitaine en ayant la propriété `z-index`. À cause de cela, la propriété `z-index` du `button` devient inutile, peu importe à quel point nous augmentons les nombres.

Mais une fois que nous retirons la propriété `z-index` du `main`, le `button` est maintenant libre d'être le capitaine.

Au cas où vous auriez oublié ce que signifie un contexte d'empilement :

> Le contexte d'empilement est simplement un terme utilisé pour définir comment le navigateur décide quels éléments dans le DOM viennent en premier et lesquels "rendre" au-dessus.

Nous avons discuté en détail de la façon dont le contexte d'empilement fonctionne et comment il est créé, mais voici un résumé :

* Définir une propriété de position (relative, fixe ou absolue) sur un élément DOM.
* Définir la propriété `z-index` sur un élément DOM.
* Définir `opacity` à une valeur inférieure à `1`.
* Utiliser la propriété `isolation`.
* Utiliser les propriétés CSS `transform`, `filter`, `clip-path`, ou `perspective`.

Cela signifie simplement que l'utilisation de l'une des propriétés ci-dessus indique au navigateur de calculer et de voir quel élément DOM doit être rendu au-dessus du reste des éléments.

Vous pouvez lire plus sur le fonctionnement du contexte d'empilement [sur le MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

## Comment déboguer le Z-Index

Avant de conclure cet article, je veux vous présenter une nouvelle `propriété` que vous pouvez utiliser conjointement avec la propriété `z-index`. Elle vous aide à gérer les contextes d'empilement de manière plus agréable.

Je vais le faire en introduisant un bug afin que nous puissions voir comment le corriger. Consultez le bac à sable Codepen ci-dessous pour voir :

%[https://codepen.io/developeraspire5/pen/ZEjNaav]

```html
<body>
  <header> This is a header </header>
  <main>
        <button> Click here to suscribe </button>
    <p>Hello there I am the main </p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.   Reiciendis numquam sapiente veniam fugiat. Harum voluptatum est ab similique incidunt,Quae, amet rem. Minima vitae, accusantium corrupti dolorem perferendis qui magnam...[view the full code snippet on the codepen playground above</p>
  
  </main>
  
</body>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@200..900&display=swap');
body{
  font-family: 'Mulish', sans-serif;
  
}
header {
  background-color: hotpink;
  text-align: center;
  padding: 30px;
  position: sticky;
  top: 0;
  z-index: 2;
}

main {
  text-align: center;
  background-color: blue;
  color: white;
  padding: 30px;
  position: relative;
  min-height: 100vh;
}
button {
  border: none;
  text-align: center;
  padding: 8px;
  background: white;
  box-shadow: 1px 2px 8px hsl(0deg 0% 0% / 0.25);
  border-radius: 6px;
  
  position: sticky;
  top: 0;
  right: 20px;
  margin-left: 100rem;
  z-index: 2;  
}

```

Si vous exécutez le bac à sable ci-dessus et voyez le résultat, vous remarquerez un problème. Voici ce que j'essaie de faire :

Nous avons un blog, et dans chaque article de blog, nous voulons un bouton collant flottant qui dit "Cliquez ici pour vous abonner" car bien sûr nous voulons plus de spectateurs abonnés au blog. 

Nous faisons cela en ajoutant `position: sticky` sur le bouton afin qu'il soit toujours flottant et visible lorsque les utilisateurs lisent l'article du blog. Une fois qu'ils le voient suffisamment, peut-être décideront-ils de s'abonner.

Nous voulons également que ce bouton soit adhéré à l'article du blog lui-même, ce qui signifie que dès que l'article du blog n'est plus visible, il n'y a aucune raison pour que le bouton soit là. À cause de cela, nous avons fait du bouton un enfant de l'élément `main` qui contient l'article du blog. 

Bien que cela soit vrai, nous voulons également que le bouton soit au-dessus/devant le contenu de l'article du blog, flottant simplement au-dessus du texte des articles. Pour ce faire, nous avons ajouté une propriété `z-index`. Maintenant, parce que nous avons déjà une propriété `position`, nous étions très confiants que le bouton serait empilé au-dessus du contenu par le navigateur.

De la page, nous avons également ajouté un `header` collant, afin que le `header` soit collé à la page et ne défile jamais. Nous voulons également que le `header` soit au-dessus des autres éléments, afin que l'article du blog et tout autre élément DOM précédent glissent simplement sous le header.

Pour y parvenir, nous ajoutons une valeur `z-index` de `2` afin qu'il soit poussé plus haut dans la pile et plus près de l'écran qui le rend au-dessus des autres éléments DOM.

Après avoir fait cela et être satisfait de notre travail, nous remarquons que nous avons un bug (je déteste les bugs) : le bouton ne fait tout simplement pas ce que nous voulons qu'il fasse. 

Le bouton passe en fait au-dessus du `header` au lieu de descendre avec l'article du blog comme nous l'avions prévu. 

C'est une recette pour une frustration supplémentaire qui provoque un peu de tiraillement et de cris à l'écran de l'ordinateur avec "Pourquoi CSS est-il si difficile ?".

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-44.png)

Essayez de passer en revue le code et de comprendre quel est le vrai problème. Ensuite, revenez à cet article et nous le résoudrons ensemble.

Souvenez-vous de notre deuxième règle du `z-index` ? Où nous avons utilisé l'analogie du capitaine pour décrire comment les contextes d'empilement sont comparés ? C'est ce qui se passe ici.

En regardant le code, nous pouvons voir que nous avons créé 2 contextes d'empilement :

* Lorsque nous avons utilisé le `positioned` et le `z-index` sur l'élément `header`.
* Lorsque nous avons utilisé le `positioned` et le `z-index` sur l'élément `button`.

D'après les points ci-dessus, nous pouvons voir que ces deux éléments sont ceux qui sont comparés par le navigateur afin de créer le contexte d'empilement correct.

Souvenez-vous également que nous avons discuté que :

> Si deux éléments DOM ont exactement les mêmes propriétés pour créer un contexte d'empilement, le navigateur décide lequel vient au-dessus en suivant l'ordre DOM. Cela signifie que l'élément ultérieur vient au-dessus du précédent, tout comme dans une pile de livres.

C'est ainsi que le navigateur a décidé que le `button` doit venir au-dessus. Lorsque nous comparons avec le navigateur, nous voyons que :

* Le `header` a `position: sticky`, mais le `button` a également `position: sticky`. Peu importe quelle valeur est utilisée tant que l'élément utilise une propriété `position`.
* Le header a un `z-index` de 2 (parce qu'il veut venir au-dessus), et le bouton a également un `z-index` de 2 (parce qu'il veut être au-dessus du contenu du blog).

Cela a laissé le navigateur sans autre choix que de décider du gagnant en suivant l'ordre DOM, ce qui signifie que puisque le `button` est le dernier dans l'ordre DOM, il viendra au-dessus du `header`. Ouf ! Quel bug.

Comment résolvons-nous cela ? Nous pouvons revenir à notre analogie du capitaine :

> Dans un avion, il y a 2 pilotes, tous deux également qualifiés pour piloter et commander l'avion. Mais un seul de ces 2 pilotes est réellement choisi pour être le capitaine de ce vol. Tant que le pilote choisi n'est pas absent, malade ou blessé, il n'est pas nécessaire que le deuxième pilote assume le rôle de capitaine.   
>   
> Mais dans une situation où quelque chose de grave arrive au pilote choisi, le deuxième pilote est autorisé et mandaté pour être capitaine.

Souvenez-vous que le `button` est un enfant de `main` mais que le `main` n'a pas de `z-index`. Cela signifie qu'il n'est pas un capitaine, ce qui signifie également qu'il n'y a pas de **contexte d'empilement isolé** empêchant la propriété `z-index` du `button` d'être ignorée. Au lieu de cela, le navigateur la prendra en compte et la comparera avec l'élément `header` pour décider quel élément doit être rendu au-dessus.

Nous pouvons résoudre cela en appliquant la deuxième règle du `z-index` en créant simplement un contexte d'**empilement isolé**. Nous faisons cela en ajoutant une propriété `z-index` et en définissant également une propriété `position` sur l'élément `main`.  Voyons cela dans l'extrait de code ci-dessous :

%[https://codepen.io/developeraspire5/pen/yLqWpEZ]

```html
<body>
  <header> This is a header </header>
  <main>
        <button> Click here to suscribe </button>
    <p>Hello there I am the main </p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.   Reiciendis numquam sapiente veniam fugiat. Harum voluptatum est ab similique incidunt,Quae, amet rem. Minima vitae, accusantium corrupti dolorem perferendis qui magnam...[view the full code snippet on the codepen playground above</p>
  
  </main>
  
</body>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@200..900&display=swap');
body{
  font-family: 'Mulish', sans-serif;
  
}
header {
  background-color: hotpink;
  text-align: center;
  padding: 30px;
  position: sticky;
  top: 0;
  z-index: 2;
}

main {
  text-align: center;
  background-color: blue;
  color: white;
  padding: 30px;
  position: relative;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}
button {
  border: none;
  text-align: center;
  padding: 8px;
  background: white;
  box-shadow: 1px 2px 8px hsl(0deg 0% 0% / 0.25);
  border-radius: 6px;
  
  position: sticky;
  top: 0;
  right: 20px;
  margin-left: 100rem;
  z-index: 2;  
}

```

Tada ! Résolu.

Maintenant, nous avons confié le manteau de capitaine à `main` qui est un parent du `button`. Cela force le `button` à s'écarter. Et puisque le `z-index` sur le `header` est `2` (qui est un nombre plus grand que `1` que nous avons défini sur le `main`), le `button` passe maintenant sous le header avec l'article du blog. 

C'est parce que, comme l'a expliqué la deuxième règle du `z-index`, la valeur `z-index` sur le `button` n'a plus aucun effet sur la décision du contexte d'empilement prise par le navigateur.

Voici les 2 règles de la propriété `z-index` à nouveau :

1. **`z-index` ne fonctionne qu'avec les éléments positionnés.**
2. **Une propriété `z-index` dans un contexte d'empilement isolé n'est pas prise en compte en dehors du contexte d'empilement isolé.**

### Comment utiliser la propriété isolation

Bien que le code ci-dessus ait clairement résolu notre problème, nous sommes toujours laissés avec quelque chose que tout développeur déteste – c'est-à-dire, avoir des `z-index` éparpillés dans tout notre code, nous pouvons partir en vacances pendant un mois, revenir à notre code et rencontrer un autre bug de `z-index`. Nous pourrions oublier à quoi une valeur particulière de `z-index` était censée servir. Ensuite, nous la supprimerons, ce qui nous plongera dans un autre cycle sans fin de lutte contre les bugs.

Au lieu d'utiliser `position: relative; z-index: 1;` sur notre élément `main` pour créer le **contexte d'empilement isolé**, nous pouvons simplement faire ceci :   


![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-46.png)
_Utilisation de la propriété isolation pour résoudre le bug_

```css
main {
  isolation: isolate;
}
```

La propriété `isolation` ne fait qu'une seule chose : elle crée un contexte d'empilement.

C'est la manière la plus simple de créer un contexte d'empilement. Elle peut être utile lorsque vous souhaitez empêcher les valeurs `z-index` des éléments enfants d'affecter la mise en page d'une page web (sauf, bien sûr, lorsque nous voulons qu'elles le fassent). Cette propriété nous permet d'y parvenir sans le fardeau d'avoir le `z-index` partout dans notre code.

## Conclusion

Nous avons atteint la fin de cet article. Espérons que vous comprenez maintenant le mécanisme sous-jacent derrière la façon dont le navigateur empile les éléments dans le DOM (appelé contexte d'empilement). Vous devriez également savoir comment fonctionne la propriété `z-index`, les règles du `z-index`, comment utiliser efficacement ces règles.

J'espère que vous avez appris beaucoup de choses dans cet article, et j'ai hâte de vous voir gagner chaque bataille de `z-index` que vous pourriez rencontrer à l'avenir. Vous pouvez toujours revenir à cet article et le relire.

Pour plus de conseils CSS, suivez-moi sur [Twitter](https://twitter.com/developeraspire).

Merci d'avoir lu ! À la prochaine.