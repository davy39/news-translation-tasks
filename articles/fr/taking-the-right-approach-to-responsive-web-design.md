---
title: Comment adopter la bonne approche pour le Responsive Web Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-07T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/taking-the-right-approach-to-responsive-web-design
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/fcc-cover.jpg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Comment adopter la bonne approche pour le Responsive Web Design
seo_desc: 'By Kevin Powell

  I ran a poll on Twitter awhile ago, and the results surprised me.

  Not only did I expect the results to be the other way around, I thought that mobile-first
  would get at least 80% of the vote.


  Desktop-first wins with more than 61% of ...'
---

Par Kevin Powell

J'ai lancé un sondage sur Twitter il y a quelque temps, et les résultats m'ont surpris.

Non seulement je m'attendais à des résultats inverses, **je pensais que le mobile-first obtiendrait au moins 80 % des voix**.

![Sondage Twitter montrant que 61,5 % des personnes écrivent d'abord pour le desktop, avec 2 212 votes](https://www.freecodecamp.org/news/content/images/2020/04/image-5.png)
_Le desktop-first l'emporte avec plus de 61 % des voix !_

Dans les réponses, certaines personnes ont expliqué pourquoi elles écrivent d'abord pour le desktop. Les thèmes généraux de ces raisons :

* C'est tout ce que le designer a fourni
* C'est ainsi que leur équipe fonctionnait
* Ils ont appris le CSS en l'écrivant uniquement pour le desktop, donc cela semblait être la progression naturelle
* Les clients veulent voir la version desktop

## Qu'est-ce que le mobile-first

Le mobile-first consiste à **commencer par écrire notre CSS pour les appareils mobiles, puis à utiliser des media queries pour ajouter des styles pour les écrans plus grands**.

En général, cela signifie que les media queries utilisent un `min-width`. Nous utilisons des media queries pour ajouter ou écraser des styles pour un breakpoint donné et plus grand, comme dans cet exemple :

```css
.sales-points {
  padding: 3em 0;
}

@media (min-width: 600px) {
  .sales-points {
    display: flex;
    justify-content: space-between;
  }
}
```

Dans cet exemple, pour les petits écrans, nous appliquons simplement un peu de padding. En supposant que cette section du site contient des enfants, nous transformons ces enfants en colonnes à une largeur minimale de `600px`.

Ainsi, lorsque la viewport est de `600px` ou plus, nous aurons des colonnes. Le reste du temps, les éléments s'empilent.

Comme vous l'avez probablement deviné, **une approche desktop-first est l'inverse**. Notre CSS est écrit pour les grands écrans, puis nous utilisons des media queries pour apporter des modifications pour les tailles plus petites, généralement en utilisant des media queries `max-width`.

## Pourquoi le mobile-first est plus facile

**Les sites web sont naturellement responsives avant même que nous écrivions une seule ligne de CSS**.

Si vous retirez le CSS de n'importe quelle page sur Internet, même un site conçu pour une taille d'écran très spécifique en 2001, vous avez maintenant un site web responsive et mobile-friendly !

### Les styles desktop tendent à être plus complexes

Lorsque nous stylisons pour le desktop-first, nous ajoutons des largeurs, des colonnes et déplaçons des éléments. Nous ajoutons de la complexité. Nous le faisons pour de bonnes raisons, car nous avons plus d'espace à notre disposition.

Non seulement nous voulons tirer parti de cela pour rendre les choses plus intéressantes, mais **si nous ne rendions pas les choses plus complexes sur les grands écrans, elles n'auraient pas l'air très bien**. Même si vous avez un site web _très_ simple, vous ne voulez pas que le texte s'étire d'un côté à l'autre.

Regardez à quoi ressemblerait un article ici sur FCC News si le texte allait d'un côté à l'autre.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-6.png)

Nous pouvons tous convenir que vous ne liriez jamais quelque chose comme cela, n'est-ce pas ? Je dois littéralement bouger un peu la tête de gauche à droite pour lire une ligne complète sur mon écran. C'est terrible.

### Les mises en page mobiles tendent à être très simples, ce qui les rend très faciles à démarrer

Pour toutes les personnes qui m'ont répondu en disant que leurs clients préféraient voir la version desktop, ou qu'ils n'avaient reçu que des maquettes desktop de la part de leurs designers, je soutiendrais qu'il est toujours plus facile de commencer par le mobile-first.

Pour de nombreux sites, une fois que vous avez configuré votre typographie, vous êtes à 70 % du chemin. Des choses comme :

* `font-family`
* `font-size`
* `font-weight`
* `margin` (sur vos éléments de texte)

Ensuite, vous pouvez aller faire un peu de style de mise en page très basique sur vos éléments de mise en page, tels que :

* `padding`
* `background-color`
* `color`
* et peut-être quelques ajustements avec `margin`

**À ce stade, les choses auront l'air assez bien d'un point de vue mise en page sur les petits écrans**. Cela signifie que, sans écrire une seule media query, vous avez un site entièrement fonctionnel sur mobile.

Si vous vous sentiez particulièrement paresseux, ou si vous avez un site très simple, vous pourriez mettre un `max-width` sur votre conteneur et en avoir fini avec tout cela sans même avoir à vous soucier d'une media query !

La plupart du temps, nous voulons améliorer le jeu pour les tailles d'écran plus grandes, et c'est pourquoi je pense que le mobile-first est la voie à suivre. C'est la progression naturelle vers le haut.

## Comparaison du mobile-first au desktop-first

Ci-dessous se trouve un CodePen qui présente une mise en page _très_ simple réalisée en utilisant une approche desktop-first et mobile-first.

%[https://codepen.io/kevinpowell/pen/ZEGdQgN]

Si vous ouvrez le pen et jouez avec la taille de la viewport, vous verrez que le résultat final est exactement le même.

Mais si le résultat final en utilisant l'une ou l'autre approche est exactement le même, pourquoi cela importe-t-il quelle approche vous prenez ?

### Le desktop-first peut conduire à un code redondant

Dans le pen ci-dessus, l'approche desktop-first utilise le code suivant :

```css
/*  desktop-first */
.desktop-first .sales-points {
  display: flex;
  justify-content: space-between;
}

.desktop-first .sales-point {
  width: 30%;
}

@media (max-width: 600px) {
  .desktop-first .sales-points {
    display: block;
  }

  .desktop-first .sales-point {
    width: 100%;
  }
}
```

Comme vous pouvez le voir dans le CodePen, cela fonctionne parfaitement bien, mais il y a beaucoup de code ici qui devient redondant lorsque nous utilisons une approche desktop-first.

Remarquez comment nous déclarons d'abord un `display: flex` pour le remettre ensuite à `display: block` par défaut dans la media query. De plus, pour nos colonnes, nous changeons la `width` puis, une fois de plus, revenons à la valeur par défaut plus tard.

L'approche mobile-first a beaucoup moins de code redondant. Comme il n'y avait pas de style pour le texte ou les couleurs de fond, il n'y a pas de style sauf ce dont j'ai besoin dans mes media queries !

```css
/*  mobile-first */
@media (min-width: 600px) {
  .mobile-first .sales-points {
    display: flex;
    justify-content: space-between;
  }

  .mobile-first .sales-point {
    width: 30%;
  }
}
```

## Revenir aux valeurs par défaut devrait être un signal d'alarme

Je réalise que certaines choses sont plus complexes que cela (et nous y viendrons bientôt), mais la plupart de ce qui m'inquiète ici est du point de vue de la mise en page.

Pour la mise en page que j'ai créée ci-dessus, je n'ai pas écrit une seule ligne de code pour l'approche mobile-first. Je me suis simplement basé sur la façon dont le document s'écoulait dès le départ. Dans l'approche desktop-first, je dois m'attaquer aux deux car je dois réinitialiser les choses à leur état par défaut.

Le fait que je réinitialise des choses comme `display` et `width` à leur état par défaut, pour moi, est un signal d'alarme. Cela signifie que j'écris quelque chose qui aurait pu être évité. Cela signifie que je perds mon temps.

## Certaines choses ne sont pas si simples

Certains composants ont un aspect complètement différent selon les tailles d'écran, comme les menus de navigation. D'autres fois, vous avez **des styles sur mobile qui doivent être écrasés pour le desktop et qui finissent par être redondants**.

Dans la vidéo ci-dessous, je rencontre exactement ce problème où je devais déplacer un élément en utilisant `position: absolute` pour les petits écrans. Plutôt que de devoir le positionner, puis de réinitialiser la position à la valeur par défaut pour les tailles d'écran plus grandes, il semblait logique d'utiliser une media query `max-width`.

Si vous lancez la vidéo, elle devrait commencer juste là où je traite ce problème si vous souhaitez le voir en action (17:41 au cas où elle ne commencerait pas au bon endroit).

%[https://youtu.be/_kF3k0vDMNA?t=1061]

Il y a donc parfois des exceptions, et il n'y a rien de mal à cela. Mon propos ici n'est pas que nous devrions être des robots qui font les choses d'une seule manière. Il y a des moments où différentes approches ont du sens, mais **j'aime à croire qu'avoir une règle générale aide**.

Alors, la prochaine fois que vous concevrez un site, **même si vous n'avez qu'une maquette desktop à suivre, essayez de commencer par le mobile**. Cela ne demande pas plus de travail du tout, et à long terme, je parie que cela vous fera économiser beaucoup de code redondant. C'est assez simple aussi !

1. Commencez par la typographie
2. Ajoutez les couleurs et le padding
3. Mettez tout ce qui est lié à la mise en page dans une media query `min-width`

Lorsque vous aurez terminé votre mise en page, non seulement vous aurez réalisé cette version desktop que votre client meurt d'envie de voir, mais vous serez également à 90 % du chemin pour votre version mobile, sans même y avoir vraiment pensé.

## Avez-vous du mal à rendre les choses responsives ?

Rendre les sites web responsives est un sujet que beaucoup de gens me disent trouver difficile. Pour aider, **j'ai créé un cours gratuit appelé [Conquering Responsive Layouts](https://courses.kevinpowell.co/conquering-responsive-layouts)**. Il est conçu comme un défi de 21 jours dans lequel nous aborderons un sujet par semaine, chacun s'ajoutant à ce que nous avons déjà appris.

Je réalise que nous sommes tous occupés avec les enfants, la famille, le travail et plus encore, donc chaque jour ne représentera que 10 à 30 minutes de leçons, avec 2 à 3 leçons par semaine. Entre-temps, vous aurez de petits défis à relever, vous progressant jusqu'à être à l'aise avec la création de mises en page responsives.

Le cours sera lancé le 13 avril et, comme il s'agit d'un cours de 21 jours, les inscriptions fermeront ce jour-là. [Cliquez ici pour vous inscrire](https://courses.kevinpowell.co/conquering-responsive-layouts) et commencez à maîtriser les mises en page responsives !

Si vous lisez ceci après coup, vous pouvez vous inscrire pour la prochaine session, mais il ne rouvrira pas avant quelques mois.