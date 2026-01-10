---
title: Comment créer un séparateur de section avec CSS
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2022-02-25T21:46:23.000Z'
originalURL: https://freecodecamp.org/news/section-divider-using-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/section-divider.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer un séparateur de section avec CSS
seo_desc: 'It''s always cool to have a fancy section divider on your website. And
  it''s even better if we can make them responsive and easy to adjust. This is what
  you will learn in this article.

  We will explore different section dividers made using only CSS and ...'
---

C'est toujours sympa d'avoir un séparateur de section élégant sur votre site web. Et c'est encore mieux si nous pouvons les rendre réactifs et faciles à ajuster. C'est ce que vous apprendrez dans cet article.

Nous explorerons différents séparateurs de section réalisés uniquement avec CSS et un code optimisé facile à manipuler.

Voici un exemple de séparateurs de section en action :

![Aperçu de 2 séparateurs de section appliqués à l'en-tête de FreeCodeCamp](https://www.freecodecamp.org/news/content/images/2022/02/image-90.png align="left")

*Aperçu de 2 séparateurs de section appliqués à l'en-tête de FreeCodeCamp*

Avant de plonger dans la partie technique, j'ai créé un [générateur en ligne](https://css-generators.com/section-divider/) pour les séparateurs de section. Tout ce que vous avez à faire est de sélectionner votre configuration et d'obtenir le code CSS en un rien de temps.

D'accord, je peux vous entendre dire : "Pourquoi un tutoriel ennuyeux ? Je vais simplement utiliser le générateur chaque fois que j'en ai besoin !"

Bien sûr, vous pouvez faire cela – mais il est toujours bon de savoir ce qui se passe sous le capot afin que vous compreniez le code que vous utilisez et que vous soyez capable de l'ajuster manuellement.

Ensuite, vous serez en mesure de créer votre propre séparateur personnalisé après avoir compris ceux que j'ai faits !

Alors, plongeons et apprenons comment c'est fait.

## Comment créer un séparateur incliné pour votre site web

![Illustration d'un séparateur incliné](https://www.freecodecamp.org/news/content/images/2022/02/slanted-divider.png align="left")

*Illustration d'un séparateur incliné*

Dans la figure ci-dessus, nous avons deux éléments séparés par un espace incliné. Pour obtenir cet effet, nous allons découper une partie de chacun. Regardons une illustration étape par étape pour mieux comprendre.

![Une illustration étape par étape pour créer un séparateur incliné](https://www.freecodecamp.org/news/content/images/2022/02/image-81.png align="left")

*Une illustration étape par étape pour créer un séparateur incliné*

Initialement, nous avons deux éléments placés l'un au-dessus de l'autre. Nous commençons d'abord par découper la partie inférieure de l'élément supérieur (étape (2)) en utilisant `clip-path` comme suit :

```css
clip-path: polygon(0 0,100% 0,100% 100%,0 calc(100% - 50px));
```

Nous avons un chemin à quatre points où nous rendons le coin inférieur gauche un peu plus haut pour créer l'effet de découpe. Vous pouvez remarquer l'utilisation de `calc(100% - 50px)` au lieu de `100%`.

Nous faisons de même pour le deuxième élément à l'étape (3) en utilisant :

```css
clip-path: polygon(0 0,100% 50px,100% 100%,0 100%);
```

Cette fois, nous abaissons le coin supérieur droit du même nombre de pixels (`50px` au lieu de `0`). Si vous n'êtes pas familier avec `clip-path`, voici une figure pour mieux voir les points.

![Illustration des points du clip-path](https://www.freecodecamp.org/news/content/images/2022/02/image-82.png align="left")

*Illustration des points du clip-path*

Les points ne sont rien d'autre que des coordonnées x,y dans un espace 2D avec la plage `[0 100%]`. Vous pouvez facilement identifier les quatre coins, et à partir de là, nous pouvons trouver n'importe quels autres points.

Enfin, nous ajoutons une `margin-top` négative au deuxième élément pour réduire l'espace et obtenir un écart égal à `10px`. Le code final sera :

```css
.top {
  clip-path: polygon(0 0,100% 0,100% 100%,0 calc(100% - 50px));
}
.bottom {
  clip-path: polygon(0 0,100% 50px,100% 100%,0 100%);
  margin-top: -40px;
}
```

C'est le code que vous obtiendrez à partir du [générateur en ligne](https://css-generators.com/section-divider/) que j'ai créé. Nous pouvons l'améliorer en introduisant des variables CSS :

```css
:root {
  --size: 50px; /* taille de la découpe */
  --gap: 10px;  /* l'écart */
}
.top {
  clip-path: polygon(0 0,100% 0,100% 100%,0 calc(100% - var(--size)));
}
.bottom {
  clip-path: polygon(0 0,100% var(--size),100% 100%,0 100%);
  margin-top: calc(var(--gap) - var(--size));
}
```

Comme je l'ai dit dans l'introduction, nous avons un code simple et facile à ajuster qui produit un séparateur de section réactif.

## Comment créer un séparateur de flèche en pleine largeur pour votre site web

![Illustration du séparateur de flèche en pleine largeur](https://www.freecodecamp.org/news/content/images/2022/02/image-83.png align="left")

*Illustration du séparateur de flèche en pleine largeur*

Celui-ci est assez similaire au séparateur précédent. Nous allons simplement traiter avec plus de points `clip-path`.

![Une illustration étape par étape pour créer un séparateur de flèche en pleine largeur](https://www.freecodecamp.org/news/content/images/2022/02/image-84.png align="left")

*Une illustration étape par étape pour créer un séparateur de flèche en pleine largeur*

Je pense que vous avez probablement l'idée maintenant. Nous suivons les mêmes étapes et nous terminons avec le code suivant :

```css
.top {
  clip-path: polygon(0 0,100% 0,100% calc(100% - 50px),50% 100%,0 calc(100% - 50px));
}
.bottom {
  clip-path: polygon(0 0,50% 50px,100% 0,100% 100%,0 100%);
  margin-top: -40px;
}
```

Et ci-dessous se trouve une autre illustration pour comprendre les nouveaux points que nous utilisons pour ce séparateur de section.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-85.png align="left")

*Illustration des points du clip-path*

À première vue, cela peut sembler difficile, mais c'est vraiment assez facile.

Nous créons des formes en reliant différents points à l'intérieur de l'espace 2D de notre élément. L'astuce est de créer 2 "formes de puzzle" (je viens de créer ce terme) pour créer l'illusion d'un séparateur de section. Avec un peu de pratique, vous pouvez facilement créer votre séparateur en suivant la même logique.

Avant de passer au suivant, voici le code utilisant des variables CSS :

```css
:root {
  --size: 50px; /* taille de la découpe */
  --gap: 10px;  /* l'écart */
}
.top {
  clip-path: polygon(0 0,100% 0,100% calc(100% - var(--size)),50% 100%,0 calc(100% - var(--size)));
}
.bottom {
  clip-path: polygon(0 0,50% var(--size),100% 0,100% 100%,0 100%);
  margin-top: calc(var(--gap) - var(--size));
}
```

Vous pouvez déjà voir un motif dans le code de nos séparateurs puisque nous utilisons la même technique. Deux `clip-path`, une `margin-top` négative, et deux variables CSS. C'est aussi simple que cela !

## Comment créer un séparateur de flèche pour votre site web

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-86.png align="left")

*Illustration du séparateur de flèche*

Ce séparateur est un peu plus délicat que les précédents car je vais ajouter une autre variable qui est l'angle de la flèche. La technique reste la même, mais nous aurons plus de mathématiques pour calculer les coordonnées des points.

Pour celui-ci, mon [générateur en ligne](https://css-generators.com/section-divider/) sera très utile (surtout si vous n'êtes pas à l'aise avec les formules mathématiques) afin que vous puissiez facilement obtenir les valeurs finales sans problème.

Pour les curieux, voici le code générique :

```css
:root {
  --size: 50px;   /* taille de la découpe */
  --gap: 10px;    /* l'écart */
  --angle: 90deg; /* angle de la flèche */
}
.top {
  clip-path: polygon(0 0,100% 0,100% calc(100% - var(--size)),calc(50% + tan(var(--angle)/2)*var(--size)) calc(100% - var(--size)),50% 100%,calc(50% - tan(var(--angle)/2)*var(--size)) calc(100% - var(--size)),0 calc(100% - var(--size)));
}
.bottom {
  clip-path: polygon(0 0,calc(50% - tan((180deg - var(--angle))/4)*var(--gap) - tan(var(--angle)/2)*var(--size)) 0,50% calc(var(--size) + (1/sin(var(--angle)/2) - 1)*var(--gap)),calc(50% + tan((180deg - var(--angle))/4)*var(--gap) + tan(var(--angle)/2)*var(--size)) 0,100% 0,100% 100%,0 100%);
  margin-top: calc(var(--gap) - var(--size));
}
```

Je peux vous entendre crier en voyant cela, mais ne vous inquiétez pas si vous ne comprenez pas tout. Je crée toujours différentes formes en utilisant `clip-path`, mais cette fois le calcul est un peu plus complexe.

Le code ci-dessus est un code CSS valide, mais au moment de l'écriture, il n'y a pas de support pour les fonctions trigonométriques, donc cela ne fonctionnera dans aucun navigateur. Soit vous calculez les valeurs manuellement, soit vous utilisez [le générateur en ligne](https://css-generators.com/section-divider/) pour obtenir les valeurs de `clip-path`.

Jusqu'à présent, nous avons créé 3 séparateurs différents en utilisant la même technique. Chaque fois, nous considérons une nouvelle forme en jouant avec les valeurs de `clip-path`. Vous pouvez créer n'importe quel séparateur en utilisant la même technique, et les combinaisons sont illimitées. La seule limite est votre imagination.

C'est un bon exercice pour se familiariser avec `clip-path`. Ce que je recommande, c'est d'utiliser un stylo et du papier pour dessiner la forme que vous avez en tête. Vous identifiez les différents points de votre forme. Ensuite, vous les convertissez en valeurs `clip-path`.

Vous pouvez trouver beaucoup d'outils en ligne qui peuvent vous aider. Mon préféré est : [https://bennettfeely.com/clippy/](https://bennettfeely.com/clippy/)

## Comment créer un séparateur arrondi pour votre site web

![Illustration du séparateur arrondi](https://www.freecodecamp.org/news/content/images/2022/02/image-87.png align="left")

*Illustration du séparateur arrondi*

Pour ce séparateur, nous allons utiliser `mask` au lieu de `clip-path`. La différence entre `clip-path` et `mask` est que `mask` repose sur des images pour découper/masquer des parties d'un élément. En parlant d'images, nous parlons aussi de dégradés.

Voici une illustration pour comprendre quel type de dégradés nous avons besoin :

![Illustration des dégradés utilisés avec la propriété mask](https://www.freecodecamp.org/news/content/images/2022/02/image-89.png align="left")

*Illustration des dégradés utilisés avec la propriété mask*

Pour le premier élément, nous avons besoin de deux dégradés : un `linear-gradient()` pour créer une forme rectangulaire en haut, laissant un espace en bas, et un `radial-gradient()` pour créer un cercle placé en bas. Les deux combinés nous donneront la forme finale pour le premier élément.

Le deuxième élément n'a besoin que d'un `radial-gradient()` pour créer un trou en haut pour compléter le puzzle.

Notre code sera :

```css
.top {
  mask: 
    linear-gradient(#000 0 0) top/100% calc(100% - 50px) no-repeat,
    radial-gradient(farthest-side,#000 98%,#0000) bottom/100px 100px no-repeat;
}
.bottom {
  mask: radial-gradient(60px at 50% -10px,#0000 98%,#000);
  margin-top: -40px;
}
```

Et avec les variables CSS, cela donnera :

```css
:root {
  --size: 50px; /* taille de la découpe */
  --gap: 10px;  /* l'écart */
}
.top {
  mask: 
    linear-gradient(#000 0 0) top/100% calc(100% - var(--size)) no-repeat,
    radial-gradient(farthest-side,#000 98%,#0000) bottom/calc(2*var(--size)) calc(2*var(--size)) no-repeat;
}
.bottom {
  mask: radial-gradient(calc(var(--gap) + var(--size)) at 50% calc(-1*var(--gap)),#0000 98%,#000);
  margin-top: calc(var(--gap) - var(--size));
}
```

Même avec la méthode de masque, le motif du code est toujours le même que celui utilisant clip-path.

## Conclusion

Maintenant, en plus d'avoir un [générateur en ligne cool pour les séparateurs de section](https://css-generators.com/section-divider/), vous connaissez aussi le secret derrière leur création.

Vous avez peut-être remarqué dans le générateur que chaque séparateur vient avec 2 directions, mais je n'ai expliqué qu'une seule pour chaque séparateur. Je l'ai fait exprès pour vous laisser essayer de comprendre quelles valeurs nous devons mettre à jour pour obtenir la direction opposée. Vous pouvez le faire – ce n'est pas difficile et vous apprendrez beaucoup en le faisant.

Je publierai plus de générateurs à l'avenir, alors marquez cette page : [https://css-generators.com/](https://css-generators.com/) et suivez-moi [sur Twitter](https://twitter.com/ChallengesCss) pour ne pas les manquer.