---
title: Tout ce que je sais sur la typographie web responsive
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2016-01-18T03:55:28.000Z'
originalURL: https://freecodecamp.org/news/everything-i-know-about-responsive-web-typography-c774c2138f5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*y46Tvi_apZUxaZnxQzQ_sg.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: typography
  slug: typography
- name: UX
  slug: ux
seo_title: Tout ce que je sais sur la typographie web responsive
seo_desc: "Responsive typography is a tough nut to crack. This was the best method\
  \ I could come up with when I first started creating responsive websites:\np {\n\
  \  font-size: 16px;\n}\n\n@media (min-width: 800px) {\n  p {\n    font-size: 18px;\n\
  \  }\n}\n\n/* Repeat for h1 -..."
---

La typographie responsive est un défi difficile à relever. Voici la meilleure méthode que j'ai pu trouver lorsque j'ai commencé à créer des sites web responsives :

```css
p {
  font-size: 16px;
}

@media (min-width: 800px) {
  p {
    font-size: 18px;
  }
}

/* Répéter pour h1 - h6 et autres groupes de types */
```

J'ai appris beaucoup plus sur la typographie depuis et j'ai adopté des bonnes pratiques comme l'utilisation d'unités relatives, de rythmes verticaux et d'échelles de typographie significatives.

Ces nouvelles pratiques étaient merveilleuses. Elles ont rendu mes sites web plus agréables à l'œil. Cependant, leur mise en œuvre a été une expérience horrible.

J'ai dû écrire du code complexe et j'ai eu du mal à créer des sites web responsives sous une pression temporelle énorme.

Maintenant, après des mois de travail, j'ai enfin créé une solution que je suis heureux de partager avec vous. Elle s'appelle Typi.

Typi est génial car il me permet d'utiliser les pratiques que j'ai apprises, et en même temps, il résout la plupart des problèmes que j'ai rencontrés en 3 étapes simples. Laissez-moi vous expliquer ces trois étapes en vous présentant les pratiques que j'utilise lorsque je travaille avec la typographie responsive.

### Pratique 1 : Augmenter la taille de la police et la hauteur de ligne de votre texte principal à mesure que la taille de l'écran augmente.

Lire sur mobile et sur desktop sont deux expériences complètement différentes. Vous tenez sans doute votre appareil plus près de vous lorsque vous lisez sur mobile, car l'écran est plus petit.

Votre écran de bureau sera plus éloigné de vous par rapport au mobile. Par conséquent, la même taille de police sur le bureau semble légèrement plus petite en raison de la distance plus grande.

Pour augmenter la lisibilité et compenser la perte de taille due à la distance, nous augmentons la taille de la police.

J'ai d'abord découvert cette pratique grâce à l'article [responsive typography basics](https://ia.net/know-how/responsive-typography-the-basics) sur [ia.net](http://ia.net/). Je vous suggère vivement de consulter cet article si vous n'êtes pas familier avec ce dont je parle.

Une implémentation de cette pratique en Sass peut ressembler à ceci :

```css
html {
  font-size: 16px;
  
  @media (min-width: 800px) {
    font-size: 18px;
  }
  
  @media (min-width: 1200px) {
    font-size: 20px;
  }
}
```

Note : lorsque nous augmentons les tailles de police, nous devons également augmenter la hauteur de ligne pour permettre plus d'espace entre les lignes de texte. Avec Sass, cela peut ressembler à ceci :

```css
html {
  font-size: 16px;
  line-height: 1.3;
    
  @media (min-width: 800px) {
    font-size: 18px;
  }
    
  @media (min-width: 1200px) {
    font-size: 20px;
    line-height: 1.4;
  }
}
```

### Pratique 2 : Utiliser une échelle modulaire pour votre typographie

Il est difficile de choisir la taille de police de vos éléments typographiques (<h1> à <h6>), surtout si vous essayez de les inventer. Une échelle modulaire, également appelée échelle de typographie, est un outil que vous pouvez utiliser pour vous aider à choisir de bonnes tailles de typographie qui s'intègrent bien avec le reste de votre page.

Il s'agit d'une séquence de nombres liés les uns aux autres par un ratio (un nombre). Elle peut être créée en multipliant (ou en divisant) la taille de police de votre texte principal par le ratio. Le nombre résultant est ensuite multiplié (ou divisé) à nouveau par le ratio.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3so2OEKM6Cicnkg8.png)

Une implémentation de l'échelle modulaire au travail avec l'échelle ci-dessus peut ressembler à ceci :

```css
html { font-size: 16px }
h1 { font-size: 50px }
h2 { font-size: 37px }
h3 { font-size: 28px }
// ...
```

Bien sûr, ce ne sera pas si simple. Si vous vous souvenez de la première pratique dont nous avons parlé plus tôt dans cet article, vous remarquerez que la taille de police du corps doit changer lorsque la largeur de l'écran change.

Cela devient un problème lorsque vous devez changer les tailles de typographie de _tous vos éléments_ à _chaque point d'arrêt_ pour garantir que l'échelle reste cohérente.

```css
html {
  font-size: 16px;
  line-height: 1.3;
  @media (min-width: 800px) {
    font-size: 18px;
  }
    
  @media (min-width: 1200px) {
    font-size: 20px;
    line-height: 1.4;
  }
}

h1 {
  font-size: 50px;
  @media (min-width: 800px) {
    font-size: 56px;
  }
  @media (min-width: 1200px) {
    font-size: 63px;
  }
}

h2 {
  font-size: 37px;
  @media (min-width: 800px) {
    font-size: 42px;
  }
  @media (min-width: 1200px) {
    font-size: 47px;
  }
}

h2 {
  font-size: 28px;
  @media (min-width: 800px) {
    font-size: 32px;
  }
  @media (min-width: 1200px) {
    font-size: 35px;
  }
}
// ...
```

Beurk.

La solution ? Consultez la prochaine pratique.

Note : Si vous avez besoin d'aide pour choisir votre taille de police de départ et le ratio pour votre échelle modulaire, je vous suggère de lire cet [article sur la typographie significative](http://alistapart.com/article/more-meaningful-typography) par Tim Brown.

### Pratique 3 : Utiliser des unités de typographie relatives

Les unités relatives en CSS sont les pourcentages (%), les unités de viewport (vh, vw, vmin, vmax), l'unité em (em) et l'unité rem (rem). Celles couramment utilisées pour dimensionner la typographie sont **em** et **rem**.

Vous pouvez utiliser à la fois **em** et **rem** de la même manière pour résoudre le problème que nous avons rencontré dans la pratique 2. Pour convertir les pixels en em, nous prenons la taille de police cible et la divisons par la taille de base de la police.

Voici à quoi cela ressemblerait :

```css
html {
  font-size: 16px;
  @media (min-width: 800px) {
    font-size: 18px;
  }
  @media (min-width: 1200px) {
    font-size: 20px;
  }
}

h1 { font-size: 3.125em; } // 50 ÷ 16 = 3.125
h2 { font-size: 2.3125em;} // 37 ÷ 16 = 2.3125
h3 { font-size: 1.75em; } // 28 ÷ 16 = 1.75
// ...

// Note : Ce sont des valeurs approximatives.
// Les valeurs réelles dérivées de modularscale.com sont respectivement 3.129em, 2.3353em et 1.769em.
```

Beaucoup mieux maintenant !

Il y a encore quelques problèmes. Remarquez comment <h1> devient environ 63px lorsque la largeur de l'écran augmente à 1200px.

63px est assez grand. La lecture du texte <h1> commence à devenir inconfortable. Une meilleure décision pourrait être de le réduire à 47px à la place (taille de <h2>).

Lorsque cela se produit, vous pourriez vouloir diminuer la taille de l'élément <h2> puisque c'est une bonne pratique de mettre en évidence l'élément <h1>. Parfois, vous pourriez également avoir besoin de changer la hauteur de ligne.

Le code devient alors...

```css
html {
  font-size: 16px;
  @media (min-width: 800px) {
    font-size: 18px;
  }
  @media (min-width: 1200px) {
    font-size: 20px;
  }
}

h1 {
  font-size: 3.129em;
  line-height: 1.2;
  @media (min-width: 1200px) {
    font-size: 2.3353em;   
    line-height: 1.3;
  }
}

h2 {
  font-size: 2.3353em;
  @media (min-width: 1200px) {
    font-size: 1.769em;   
  }
}

h3 {
  font-size: 1.769em;
  @media (min-width: 1200px) {
    font-size: 1.33em;
  }
}

// ...
```

Beurk. Retour à la case départ :(

C'est là que [Typi](https://github.com/zellwk/typi) entre en jeu. Faisons une pause dans les pratiques et voyons comment Typi peut vous aider.

### Utilisation de Typi

Typi est une bibliothèque Sass qui vous permet de définir les propriétés de taille de police et de hauteur de ligne de tous vos éléments typographiques dans des cartes Sass séparées. Ces cartes peuvent ensuite être utilisées pour générer le code que nous voyons dans la situation ci-dessus. Voici comment cela fonctionne.

Tout d'abord, vous devez configurer une carte $typi. Elle ressemble à ceci :

```css
$typi: (
  null: 16px,
  small: 18px,
  large: 20px
);
```

null, small et large sont des points d'arrêt.

Typi recherche automatiquement une carte $breakpoints pour créer vos requêtes média (ce qui signifie qu'il peut s'intégrer parfaitement avec [mappy-breakpoints](https://github.com/zellwk/mappy-breakpoints), une bibliothèque que j'ai créée pour aider avec les requêtes média).

```css
$breakpoints: (
  small: 800px,
  large: 1200px
);
```

Une fois la carte $typi configurée, nous appelons le mixin typi-base() dans le sélecteur html.

```css
html {
  @include typi-base();
}
```

Ce mixin typi-base() crée les mêmes styles que nous avons écrits pour la balise <html> dans la Pratique 2. La seule différence est que les tailles de police sont indiquées en pourcentages.

```css
html {
  font-size: 100%; /* Cela signifie 16px */
}

@media all and (min-width: 800px) {
  html {
    font-size: 112.5%; /* Cela signifie 18px */
  }
}

@media all and (min-width: 1200px) {
  html {
    font-size: 125%; /* Cela signifie 20px */
  }
}
```

Nous avons également mentionné qu'il pourrait être nécessaire de changer les valeurs de hauteur de ligne lorsque la taille de la police change. Vous pouvez changer les valeurs de hauteur de ligne facilement dans Typi en fournissant une deuxième valeur de hauteur de ligne à chaque point d'arrêt qui le nécessite :

```css
$typi: (
  null: (16px, 1.3), // Définit la hauteur de ligne à 1.3
  small: 18px,
  large: (20px, 1.4) // Définit la hauteur de ligne à 1.4
);
```

Le CSS résultant de notre carte $typi mise à jour est :

```css
html {
  font-size: 100%; /* Cela signifie 16px */
  line-height: 1.3;
}

@media all and (min-width: 800px) {
  html {
    font-size: 112.5%; /* Cela signifie 18px */
  }
}

@media all and (min-width: 1200px) {
  html {
    font-size: 125%; /* Cela signifie 20px */
    line-height: 1.4;
  }
}
```

Après avoir créé la carte $typi, nous pouvons créer d'autres cartes de polices en utilisant le même format. Voici un exemple :

```css
$h1-map: (
  null: (3.129em, 1.2),
  large: (2.3353em, 1.3)
  );

$h2-map: (
  null: 2.3353em,
  large: 1.769em
  );

$h3-map: (
  null: 1.769em,
  large: 1.333em
  );
// ...
```

Ensuite, nous appelons chacune de ces cartes de polices en utilisant le mixin typi :

```css
h1 { @include typi($h1-map) }
h2 { @include typi($h2-map) }
h3 { @include typi($h3-map) }
// ...
```

Le CSS résultant serait :

```css
h1 {
  font-size: 3.129em;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  h1 {
    font-size: 2.3353em;
    line-height: 1.3;
  }
}

h2 {
  font-size: 2.3353em;
}

@media (min-width: 1200px) {
  h2 {
    font-size: 1.769em;
  }
}

h3 {
  font-size: 1.769em;
}

@media (min-width: 1200px) {
  h3 {
    font-size: 1.333em;
  }
}
```

Plutôt bien, non ? Vous devrez [télécharger Typi](https://github.com/zellwk/typi) pour jouer avec. (Il n'est pas encore disponible sur Sassmeister ou Codepen)

**ASTUCE** : Vous pouvez utiliser le mixin Sass de l'échelle modulaire si vous ne voulez pas écrire des valeurs em exactes (comme 1.769em) dans différentes cartes de polices.

Pour ce faire, vous devez [télécharger la bibliothèque](https://github.com/modularscale/modularscale-sass) et l'importer dans votre fichier Sass. Ensuite, modifiez les cartes de polices pour qu'elles utilisent la fonction ms().

```css
$h1-map: (
  null: (ms(4) 1.2),
  large: (ms(3), 1.3)
  );

$h2-map: (
  null: ms(3),
  large: ms(2)
  );

$h3-map: (
  null: ms(2),
  large: ms(1)
  );
// ...
```

En résumé, [**Typi**](https://github.com/zellwk/typi) facilite la typographie responsive en vous aidant à **écrire les propriétés de taille de police et de hauteur de ligne à différents points d'arrêt**.

Maintenant que j'ai fini de vous présenter Typi, passons à la suite et parlons des deux dernières pratiques (et de quelques problèmes pour lesquels je n'ai pas encore trouvé de solution).

### Pratique 4 : Appliquer des rythmes verticaux

Les rythmes verticaux sont un concept issu du design imprimé, où nous gardons les espaces verticaux entre les éléments d'une page cohérents (et relatifs) les uns par rapport aux autres. L'idée est similaire à l'utilisation d'une échelle de typographie — pour permettre aux éléments de votre page de s'écouler harmonieusement.

En pratique, nous utilisons souvent la propriété de hauteur de ligne du texte principal comme base pour un rythme vertical cohérent. Supposons que le texte principal de votre site web ait une **hauteur de ligne de 25px**. Vous ferez deux choses :

1. Définir **l'espace blanc vertical entre les éléments** à un **multiple de 25px**
2. Définir **la hauteur de ligne de tous les éléments de texte** à un **multiple de 25px**

Voici à quoi cela pourrait ressembler en CSS (Note : Cela n'a pas encore pris en compte les trois pratiques que j'ai mentionnées ci-dessus)

```css
html {
  font-size: 18px;
  line-height: 25px;
}

// Réinitialise les marges
body, h1, p {
  margin: 0;
}

h1 {
  font-size: 63px;
  line-height: 75px;
  margin: 25px 0;
}

p + p {
  margin-top: 25px;
}
```

%[https://codepen.io/zellwk/pen/WrjOoa]

Cela a l'air plutôt bien ! Allons plus loin en transformant le code ci-dessus en unités relatives. En faisant cela, vous rencontrerez le grand débat entre em et rem.

### Em vs Rem

Essayons d'abord de convertir le code en **ems**, puis en **rems**. Au fait, les [bonnes pratiques indiquent que les valeurs de hauteur de ligne doivent être sans unité](https://css-tricks.com/almanac/properties/l/line-height/).

```css
html {
  font-size: 1.125em;
  line-height: 1.4; // Cela représente 25.2px pour être précis
}

// Réinitialise les marges
body, h1, p {
  margin: 0;
}

h1 {
  // la taille de la police est de 63.147px pour être plus précis
  font-size: 3.5082em; // 63.147 ÷ 18 = 3.5082em
  line-height: 1.1972; // 75.6 ÷ 63.147 = 1.1972
  margin: 0.3991em 0; // 25.2 ÷ 63.147 = 0.3991
}

p + p {
  margin-top: 1.4em;
}
```

Faites particulièrement attention à la manière dont nous avons converti la propriété de marge sur l'élément <h1> en ems.

Remarquez comment nous avons utilisé 63.147px comme base pour la division ? Cela doit être fait car les tailles **calculées avec des ems sont relatives à la taille de police actuelle**. Cela cause souvent de la confusion et implique beaucoup de calculs complexes.

Maintenant, voici le hic. Même si nous avons essayé d'être aussi précis que possible, les navigateurs ne semblent pas coopérer avec nous. Vous remarquerez que nos rythmes verticaux commencent à devenir bizarres.

%[https://codepen.io/zellwk/pen/jWmKKZ]

Deux problèmes ont contribué à ce comportement bizarre.

Premièrement, nous ne sommes pas précis et exacts à 100 % avec nos calculs. Nous pourrions être plus précis (comme 10 décimales), mais cela rendrait notre code très laid.

Deuxièmement, différents navigateurs gèrent les problèmes d'arrondi des sous-pixels différemment. Cela signifie que nous ne pourrons jamais obtenir des rythmes parfaits en pixels, peu importe nos efforts.

Eh bien, je ne veux pas insister sur l'arrondi des sous-pixels car il n'y a pas grand-chose que nous puissions faire. Examinons plutôt comment l'unité rem gère ces calculs complexes, d'accord ?

```css
html {
  font-size: 1.125rem;
  line-height: 1.4; // Cela représente 25.2px pour être précis
}

// Réinitialise les marges
body, h1, p {
  margin: 0;
}

h1 {
  font-size: 3.5082rem; // 63.147 ÷ 18 = 3.5082
  line-height: 1.1972; // 75.6 ÷ 63.147 = 1.1972
  margin: 1.4rem 0; // 25.2 ÷ 18 = 1.4
}

p + p {
  margin-top: 1.4rem;
}
```

Remarquez comment nous avons utilisé 1.4rem sur la propriété de marge au lieu de 0.3991em ? L'unité **rem rend les calculs** avec les rythmes verticaux **beaucoup plus simples**.

**Cela ne signifie pas que vous devez passer aveuglément à l'unité rem** cependant. Les unités rem et em sont toutes deux utiles, et elles doivent être utilisées à des fins différentes. J'écrirai sur ce sujet un autre jour. Pour l'instant, revenons aux rythmes verticaux.

Maintenant que nous avons converti nos rythmes verticaux en unités relatives, voyons comment cela se comporte lorsque nous le combinons avec la première pratique (les tailles de police et les hauteurs de ligne doivent changer lorsque les tailles d'écran changent).

Nous allons garder cet exemple aussi simple que possible en utilisant une seule requête média. Nous allons également utiliser l'unité rem.

```css
html {
  font-size: 1.125em;
  line-height: 1.4;
    
  @media (min-width: 1200px) {
    font-size: 1.25em; // cela représente 20px
    // Légère modification des hauteurs de ligne à 1200px
    line-height: 1.45 // cela représente 29px
  }
}

// Réinitialise les marges
body, h1, p {
  margin: 0;
}

h1 {
  font-size: 3.5082em;
  line-height: 1.1972;
  margin: 1.45rem 0;
    
  @media (min-width: 1200px) {
    // la taille de la police est maintenant de 70.164px
    line-height: 1.24; // 29px * 3 ÷ 70.164 = 1.24
    margin: 1.45rem 0;
  }
}

p + p {
  margin-top: 1.4em;
  @media (min-width: 1200px) {
    margin-top: 1.45em
  }
}
```

Beurk. Nous devons peut-être ajouter 20 000 requêtes média pour changer la marge et la hauteur de ligne de tous nos éléments avec juste ce changement dans la propriété de hauteur de ligne sur <html>. Nous n'avons même pas encore parlé des propriétés de remplissage ou de bordure !

### (╯°□°）╯︵ ┻━┻

Donc, voici ce que j'ai réalisé. **Il est impossible d'appliquer des rythmes verticaux responsives parfaits sur différents navigateurs**. Du moins, pas avec la technologie actuelle.

Ce que nous pouvons faire à la place :

1. Nous pouvons nous contenter des propriétés de hauteur de ligne des principaux éléments typographiques en estimant et en utilisant Typi.
2. Essayez de ne pas changer la propriété de hauteur de ligne de votre texte principal si possible. Les choses deviendront plus faciles lorsque les [variables CSS](http://caniuse.com/#search=css%20var) seront enfin supportées dans tous les principaux navigateurs.

### Pratique 5 : Garder les mesures de texte entre 45 et 75 caractères

Oh, celle-ci est facile. Rappelez-vous simplement ceci : un caractère fait environ 0,5em. Une mesure de texte entre 45 et 75 caractères signifie que la largeur de votre élément de texte doit être comprise entre 22,5em et 37,5em.

D'après mon expérience, je suis surtout préoccupé par le dépassement de texte de 75 caractères. Si votre texte descend en dessous de 45 caractères, peut-être est-il temps de changer les tailles de police.

```css
article {
  max-width: 30em;
  /* N'importe où entre 22,5em et 37,5em. Utilisez votre discrétion */
}
```

### Conclusion

La typographie responsive est difficile. Il n'y a toujours pas de réponses parfaites sur lesquelles nous pouvons nous appuyer, mais essayons de nous en contenter pour l'instant.

Au fait, voici à nouveau le lien vers [Typi](https://github.com/zellwk/typi) si vous voulez jouer avec.

> Cet article est d'abord apparu sur mon blog à l'adresse [www.zell-weekeat.com](http://zell-weekeat.com). Consultez-le si vous voulez plus d'articles comme celui-ci.