---
title: Comment comprendre et travailler avec les marges CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-23T16:25:00.000Z'
originalURL: https://freecodecamp.org/news/css-margins
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Artboard-1.jpg
tags:
- name: CSS
  slug: css
- name: CSS Margins
  slug: css-margins
seo_title: Comment comprendre et travailler avec les marges CSS
seo_desc: 'By Kevin Powell

  CSS gets a bad rap for not behaving the way people expect. One of the things that
  throws people off the most are margins. They seem so simple, yet they have the potential
  to cause some really strange issues.

  For people just getting in...'
---

Par Kevin Powell

CSS a mauvaise réputation car il ne se comporte pas comme les gens s'y attendent. L'une des choses qui déroutent le plus les gens sont les marges. Elles semblent si simples, pourtant elles peuvent causer des problèmes vraiment étranges.

Pour les personnes qui commencent avec CSS, c'est facilement l'une de ces choses qui peuvent vous faire penser "ce langage est stupide et n'a aucun sens !" 

Je le vois tous les jours – à la fois en classe où les gens essaient de résoudre leurs problèmes d'espacement et dans les sections de commentaires de ma chaîne [YouTube](https://youtube.com/kevinpowell).

D'une certaine manière, les marges sont un microcosme de CSS en général. CSS semble si simple avec ses paires `propriété: valeur`, mais à mesure que vous progressez, vous réalisez qu'il y a beaucoup de choses en jeu.

Les marges semblent également si simples. Ajoutez une marge, et vous ajoutez un espace vide autour de cet élément. Mais soudain, elles se comportent différemment dans une situation par rapport à une autre, ou vous ajoutez un `margin-top` à un élément enfant, et c'est le parent qui se déplace vers le bas.

La frustration s'ensuit.

Dans cet article, j'espère éclairer un peu le fonctionnement des marges. Nous examinerons certains des problèmes courants qui surviennent, ainsi que des solutions simples à ces problèmes.

Pour aborder tout cela, j'utiliserai des exemples de mon [Bootcamp de Conception Web Responsive sur Scrimba](https://scrimba.com/p/gresponsive?utm_source=dev.to&utm_medium=referral&utm_campaign=gresponsive_margins_5_minute_article), d'où je tire cette mise en page simple :  


![Mise en page CSS utilisant des marges et du padding](https://thepracticaldev.s3.amazonaws.com/i/ys0g9szfhgnobs611j1w.png)

## Que sont les marges au juste ?

Avant de plonger dans le vif du sujet, je veux m'assurer que nous savons tous ce que sont réellement les marges ! 

Je vais supposer que nous savons tous que les marges font partie du modèle de boîte, la marge étant tout à fait à l'extérieur, venant après le contenu lui-même, le padding et la bordure.

Le MDN les explique très bien (l'accent est de moi) :

> La marge est la couche la plus externe, enveloppant le contenu, le padding et la bordure en tant qu'**espace blanc entre cette boîte et d'autres éléments**. Sa taille peut être contrôlée en utilisant la marge et les propriétés connexes.

En d'autres termes, c'est effectivement un espace vide que nous pouvons utiliser pour créer de l'espace entre une boîte et une autre dans notre mise en page.

## Gérer les feuilles de style de l'agent utilisateur

Les navigateurs viennent avec une quantité surprenante de CSS par défaut, que nous appelons _feuilles de style de l'agent utilisateur_. Ces styles sont la raison pour laquelle, sans aucun CSS de notre part, un `<h1>` est plus grand qu'un `<h2>`, et pourquoi le `<body>` a une marge que nous avons tendance à toujours supprimer.

Ces styles sont importants, mais ils entraînent également l'un des plus grands problèmes que les gens rencontrent avec les marges ! Les marges ne sont pas définies à `0` sur tous nos éléments, et cela peut causer toutes sortes de problèmes étranges que nous explorerons bientôt.

Les listes, les citations en bloc, les paragraphes et les titres ont tous une `marge` (parmi d'autres éléments). Bien que parfois ils ne soient qu'une légère gêne, la marge par défaut sur les paragraphes et les titres semble être celle qui cause le plus de problèmes dès le départ. 

Par défaut, les marges gauche et droite d'un élément de texte sont définies à `0`, mais ils viennent tous avec une `margin-top` et une `margin-bottom`.

Je dis souvent aux gens que ces marges supérieure et inférieure par défaut sont à peu près les mêmes que la `taille de police` de cet élément, puisque c'est vrai pour `<p>` ainsi que pour `<h3>` à `<h6>`. Pour `<h1>`, c'est en fait `0.67em` et pour `<h2>`, c'est `0.83em`. 

Cela signifie que l'espace existe entre les éléments de notre page même si nous n'avons pas explicitement défini une marge. 

Nous reviendrons à ces valeurs par défaut dans un instant. 

## Marges qui s'effondrent

Les marges qui s'effondrent sont souvent le début des maux de tête.

Lorsque deux éléments ont des marges **verticales** qui se touchent, elles fusionnent effectivement en une seule. 

C'est déjà un comportement étrange, et si on ajoute à cela le fait que cela ne concerne que les marges verticales (haut et bas), je comprends pourquoi les gens sont confus et agacés par elles.

Nous pouvons voir cela en action avec l'exemple suivant :

```css
p {
  font-size: 18px;
  margin-bottom: 40px;
}

.links {
  margin-top: 40px;
}

```

Pour aider à illustrer ce qui se passe ici, la classe `.links` est sur le dernier paragraphe (`<p class="links">`), qui contient les deux liens à l'intérieur.

Lorsque les gens font quelque chose comme cela, ils s'attendent à ce que la marge entre le paragraphe du milieu et les liens en dessous soit de 80px (`40px` + `40px`), mais en réalité, elle est de 40px. Les deux marges se touchent, donc elles fusionnent en une seule.

![Paragraphe et liens avec 40px d'espace entre eux](https://thepracticaldev.s3.amazonaws.com/i/8durzpm9lbaqs5384a8z.png)

Pour pousser encore plus loin, donnons à nos `<p>` une `margin-bottom` de `100px` :

```css
p {
  font-size: 18px;
  margin-bottom: 100px;
}

.links {
  margin-top: 40px;
}

```

Encore une fois, les deux marges ne s'additionnent pas, elles s'effondrent en une seule, donc l'espace total ici est de `100px`. 

![Paragraphe et liens avec 100px d'espace entre eux](https://thepracticaldev.s3.amazonaws.com/i/wyzg6p0e4hmhb6k56o3c.png)

### C'est une bonne chose

Dans des cas comme celui-ci, c'est en fait une bonne chose. Si plusieurs éléments ont des marges différentes, il n'est pas nécessaire d'additionner les marges pour voir la taille de l'écart entre les éléments, car nous pouvons compter sur le fait que **la marge la plus grande l'emporte toujours**.

Nous n'y pensons souvent même pas, cela fonctionne simplement comme nous nous y attendons.

### Quand ce n'est pas une bonne chose

Cela dit, une situation où l'effondrement des marges cause toutes sortes de confusion est lorsque le premier enfant d'un élément a un `margin-top` qui fusionne avec le `margin-top` du parent.

Regardons à nouveau cette même capture d'écran :

![Paragraphe et liens avec 100px d'espace entre eux](https://thepracticaldev.s3.amazonaws.com/i/wyzg6p0e4hmhb6k56o3c.png)

Il y a un espace blanc entre le haut de la fenêtre et la boîte noire. Cela ne provient pas du body (il est beaucoup plus grand que la marge de `8px` que le body aurait). 

Vous voulez deviner d'où cela vient ?

Cela provient en fait du `<h1>` en haut de cette boîte noire.

Vous vous souvenez quand j'ai mentionné que les _feuilles de style de l'agent utilisateur_ peuvent faire des choses étranges ?

Pour aider à expliquer exactement ce qui se passe ici, ajoutons une `margin-top` beaucoup plus grande au `h1`. 

```css
.card {
  background: #000;
  color: white;
  width: 560px;
  margin: 0 auto;
}

h1 {
  font-size: 24px;
  margin-top: 100px;
}

p {
  font-size: 18px;
  margin-bottom: 100px;
}

.links {
  margin-top: 10px;
}

```

Je vois les gens faire cela tout le temps, essayant de pousser le titre vers le bas _à l'intérieur_ de son parent. Cependant, au lieu de fonctionner comme prévu, nous obtenons un espace géant en haut de toute la carte !

![ h1 avec marge effondrée](https://thepracticaldev.s3.amazonaws.com/i/qho6vjkt5y1m0ugp67mq.png)

C'est parce que le `margin-top` sur le `<h1>` fusionne avec le `margin-top` sur l'élément parent. 

Il n'y a rien qui sépare le haut de l'enfant et le parent dans ce cas. Donc lorsque nous ajoutons `margin-top` à l'enfant, il touche le `margin-top` du parent. Et, comme nous l'avons vu ci-dessus, lorsque deux marges se touchent, elles fusionnent en une seule marge.

Ainsi, bien que nous donnions la marge à l'enfant, elle est appliquée au parent. 

C'est pour cela que les gens détestent CSS.

De même, dans le code ci-dessus, nous avons donné à tous les paragraphes une `margin-bottom`. Cette marge sur les éléments `p.link` touche la `margin-bottom` de l'élément `.card`, ce qui signifie que les deux fusionnent et que la marge affecte l'élément `.card` au lieu des liens.

![Élément Card avec marge effondrée](https://thepracticaldev.s3.amazonaws.com/i/diln7vboovivmqugvv45.png)

Bien que cela ne cause pas de problème pour le site que nous créons actuellement, cela pourrait poser problème si nous décidions plus tard d'ajouter d'autres éléments à la page.

## Le problème est que nous utilisons `margin` à mauvais escient

Si je veux de l'espace entre le haut de l'élément `.card` et les enfants à l'intérieur, je ne devrais pas utiliser `margin` de toute façon. 

Les débutants confondent souvent `margin` et `padding`. Ma règle générale est la suivante : si vous voulez un espace vide, utilisez `margin`. Si vous voulez plus d'arrière-plan, utilisez `padding`.

Dans ce cas, nous voulons que notre `.card` ait plus d'arrière-plan, donc nous ne devrions pas ajouter de `margin` à ses enfants. Au lieu de cela, nous devrions ajouter du `padding` à cet élément lui-même.

![Résultat de l'ajout de padding à l'élément parent](https://thepracticaldev.s3.amazonaws.com/i/enyvexftfy8h4ji7h8h1.png)

Dans l'image ci-dessus, nous pouvons voir le padding et la marge. Le `<h1>` en haut a toujours une marge, mais elle ne fusionne plus avec le `.card` car le `padding` a ajouté un tampon. Cela empêche les marges du `.card` et du `h1` de se toucher.

Comme le padding ajoute un espace suffisant entre les `<p>` et les `<h1>`, nous pouvons maintenant supprimer les marges que nous avions précédemment ajoutées.

![Site avec une marge-bottom plus grande sur le dernier élément enfant.](https://thepracticaldev.s3.amazonaws.com/i/4ukoaipasfd8ahal4796.png)

## Les marges ne s'effondrent pas toujours

Il existe quelques exceptions aux marges qui s'effondrent. Les descendants directs des parents grid et flex n'ont pas de marges qui s'effondrent. 

Cue le ?.

Mais il existe également une sorte de solution de contournement pour cela, ce qui nous ramène aux feuilles de style de l'agent utilisateur dont nous avons parlé au début.

## Il existe un moyen facile d'éviter même de penser aux marges qui s'effondrent

Tout d'abord, il y a ma règle générale dont j'ai parlé ci-dessus :

* Si vous avez besoin d'espace vide, utilisez `margin`
* Si vous avez besoin de plus d'arrière-plan, utilisez `padding`

Cela vous sortira des ennuis la plupart du temps. Mais ajoutons une règle supplémentaire à cela qui aidera encore plus :

* Essayez d'éviter `margin-top` sauf lorsque vous en avez vraiment besoin

Cette règle est un peu en conflit avec les styles de l'agent utilisateur, qui définissent un `margin-top` et un `margin-bottom` pour un tas d'éléments, ce qui est une raison pour laquelle je fais souvent quelque chose comme ceci :

```css
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul,
ol {
 margin: 0 0 1em 0;   
}
```

Cela élimine beaucoup des problèmes qui proviennent des marges qui s'effondrent d'elles-mêmes, ainsi que les différences dans votre mise en page lorsque certains endroits utilisent flex ou grid et d'autres non.

(Note : si vous inspectez le code ici sur freeCodeCamp, vous verrez qu'ils font quelque chose de similaire aussi !)

Ce n'est pas une solution parfaite, et j'utilise souvent un peu de `margin-top` sur certains sous-titres ou dans des situations spécifiques où c'est nécessaire. Mais je le fais très intentionnellement au lieu de laisser les styles de l'agent utilisateur potentiellement interférer de manière imprévue.

Ces leçons ne sont qu'un extrait de mon cours beaucoup plus large sur la conception web responsive. Pour continuer ce voyage de codage, [jetez un œil au cours](https://scrimba.com/p/gresponsive?utm_source=dev.to&utm_medium=referral&utm_campaign=gresponsive_margins_5_minute_article). 

Dans le cours, je couvre une introduction à la conception web responsive, et je plonge dans flexbox et grid, tout en essayant de montrer aux gens à quel point CSS est vraiment amusant une fois que vous commencez à comprendre comment cela fonctionne. 

Bon codage :)