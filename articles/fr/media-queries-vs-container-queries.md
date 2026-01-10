---
title: Media Queries vs Container Queries – Lequel utiliser et quand ?
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-06-28T20:21:00.000Z'
originalURL: https://freecodecamp.org/news/media-queries-vs-container-queries
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/titleimage.png
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Media Queries vs Container Queries – Lequel utiliser et quand ?
seo_desc: As the web evolves, new tools and ideas are released with the goal of making
  our lives as web developers easier. This means we have to choose whether to stick
  with the old ways or discard them entirely for the shiny new stuff. But does this
  always de...
---

Alors que le web évolue, de nouveaux outils et idées sont publiés dans le but de faciliter notre vie en tant que développeurs web. Cela signifie que nous devons choisir entre rester avec les anciennes méthodes ou les abandonner entièrement pour les nouvelles technologies. Mais cela demande-t-il toujours une solution binaire ?

Dans des situations comme celles-ci, l'approche idéale est de comprendre les deux concepts – comparer et contraster leurs forces et faiblesses, puis décider de leurs applications les plus appropriées. C'est exactement ce que cet article fera avec les media queries et les container queries en CSS.

## Table des matières

* [Conception Web Réactive et Intrinsèque](#heading-conception-web-reactive-et-intrinseque)
* [Qu'est-ce que les media queries ?](#heading-quest-ce-que-les-media-queries)
* [Qu'est-ce que les container queries ?](#heading-quest-ce-que-les-container-queries)
* [Comparaison réelle et différences clés](#heading-comparaison-reelle-et-differences-cles)
* [Lequel utiliser et quand ?](#heading-lequel-utiliser-et-quand)
* [Conclusion](#heading-conclusion)

## Conception Web Réactive et Intrinsèque

Avant 2010, les développeurs web pouvaient se contenter de créer des sites qui fonctionnaient principalement sur desktop. Cela a duré jusqu'à ce qu'Ethan Marcotte introduise le concept de Responsive Web Design (RWD). Il est [défini par MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) comme _une façon de concevoir pour un web multi-appareils_. Cela a conduit à l'adoption des media queries comme composant du RWD.

Mais récemment, il y a eu un changement vers ce que Jen Simmons a défini comme l'Intrinsic Web Design – le besoin de créer des composants conscients du contexte. Et les container queries rendent cela possible.

## Qu'est-ce que les Media Queries ?

Les media queries sont des règles pour appliquer des styles spécifiés à un élément si certaines conditions sont remplies. Elles sont populaires pour s'assurer que les sites web sont réactifs sur divers appareils en interrogeant la largeur de la fenêtre d'affichage.

Les media queries sont caractérisées par une règle @media suivie d'une condition entre parenthèses et d'une expression entre crochets qui sera appliquée si la condition indiquée est remplie. Donc, si nous voulions changer la couleur de fond d'une div en fonction de la largeur de la fenêtre d'affichage d'un appareil, voici comment nous pourrions faire cela :

```css
/* Mobile */
@media (max-width: 480px) {
  .mysite {
    background-color: red;
  }
}
```

Dans le code ci-dessus, nous demandons que la <div> avec la classe mysite soit donnée une couleur de fond rouge si la fenêtre d'affichage atteint une largeur maximale de 480px.

**Astuce** : Max-width est utilisé pour supposer une conception desktop-first et cibler les écrans plus petits au fur et à mesure. Si c'était une conception mobile-first, nous utiliserions min-width pour cibler les écrans plus grands au fur et à mesure.

## Qu'est-ce que les Container Queries ?

Les container queries sont des règles pour appliquer des styles spécifiés à un élément en fonction de la taille de son conteneur parent. Elles répondent à une question de longue date des développeurs web qui voulaient la capacité de répondre aux changements au sein d'un conteneur individuel sur la page plutôt que de la fenêtre d'affichage entière.

```css
.header {
   container: mysite / inline-size;
}

@container mysite (min-width: 600px) {
   .maincard {
	   grid-template-column: 1fr 1fr;
    }
   .item {
       background-color: green;
    }
}

```

Comme vous pouvez le voir dans le code ci-dessus, nous définissons d'abord un conteneur dont nous voulons modifier les enfants. Dans notre cas, nous aimerions apporter des modifications à l'élément avec la classe item, dans le conteneur header. Vous pouvez faire cela en donnant un nom (optionnel) et un type au conteneur.

Ensuite, en utilisant la règle @container, nous vérifions les conditions et appliquons certains styles si elles sont remplies. Pour une largeur minimale de 600px, nous voulons du vert comme couleur de fond et deux colonnes de grille.

**Astuce** : Vous ne définissez pas un conteneur pour apporter des modifications directement à ce conteneur – mais à ses enfants. Cela signifie que si nous voulions apporter des modifications au conteneur header lui-même, nous devrions le nester dans un autre conteneur : par exemple, le conteneur A et interroger A pour affecter son enfant – header.

## Comparaison réelle et différences clés

Maintenant, avec une compréhension de leur fonctionnement, voyons-les en situation réelle. Le CodePen ci-dessous montre quatre éléments dans une mise en page. Les deux premiers sont stylisés avec des container queries tandis que les deux du bas sont stylisés avec des media queries. Vous pouvez redimensionner la fenêtre d'affichage pour voir comment les éléments répondent.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/mqvscq-demo.png)
_Démo CodePen des media et container queries : projet inspiré par Miriam Suzanne._

<p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="YzbaROw" data-pen-title="MQ vs CQ (from MS)" data-user="ophyboamah" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/ophyboamah/pen/YzbaROw">
  MQ vs CQ (from MS)</a> by Ophy Boamah (<a href="https://codepen.io/ophyboamah">@ophyboamah</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

### Différences clés entre les Media Queries et les Container Queries

![Image](https://www.freecodecamp.org/news/content/images/2024/06/comparetable.png)
_Résumé des principales différences, expliquées en détail ci-dessous_

### Basé sur la fenêtre d'affichage vs. Basé sur le conteneur

Les media queries appliquent des styles en fonction de la taille de la fenêtre d'affichage (la fenêtre du navigateur entière). Cela signifie que la mise en page change selon la taille globale de l'écran, ce qui la rend adaptée pour ajuster les designs pour différents appareils comme les téléphones mobiles, les tablettes et les ordinateurs de bureau.

Les container queries, en revanche, appliquent des styles en fonction de la taille de l'élément conteneur dans lequel ils sont placés. Cela permet aux composants individuels d'adapter leur apparence en fonction de leur propre taille plutôt que de la taille de la fenêtre d'affichage, ce qui les rend très flexibles et réutilisables dans différentes parties d'une page web.

### Modularité et Flexibilité

Puisque les media queries dépendent de la taille de la fenêtre d'affichage, elles peuvent être moins efficaces pour créer des composants véritablement modulaires. Ajuster les styles pour une partie d'une page peut affecter involontairement d'autres parties, surtout dans les mises en page complexes. De plus, elles peuvent être insuffisantes dans les scénarios où les composants doivent s'adapter indépendamment dans une mise en page plus large. Cela peut conduire à un CSS moins maintenable.

En revanche, les container queries favorisent la modularité et la flexibilité en permettant de définir des styles en fonction de la taille du conteneur. Cela signifie que vous pouvez créer des composants autonomes, adaptables et réutilisables dans diverses parties d'un site web sans changements inattendus, améliorant ainsi leur réutilisabilité.

Cela conduit à des designs plus adaptatifs où les composants peuvent ajuster leur propre mise en page et apparence, ce qui est utile dans les systèmes de design modernes basés sur les composants.

### Complexité et Maintenance

Dans les grands projets, la gestion de nombreuses media queries peut devenir fastidieuse. À mesure que le nombre de points de rupture et de cas particuliers augmente, le CSS peut devenir complexe et plus difficile à maintenir. Avec le temps, cela peut conduire à une base de code gonflée et difficile à gérer.

Les container queries peuvent simplifier la maintenance du CSS dans les grands projets. En gardant les styles spécifiques aux composants et conscients du contexte, le CSS reste plus organisé et modulaire. Cela réduit la complexité de la gestion des points de rupture globaux et facilite la maintenance, conduisant à une base de code plus organisée.

## Lequel utiliser et quand ?

![Image](https://www.freecodecamp.org/news/content/images/2024/06/finalsection.png)
_Media query vs container query (crédit image : <i>[web.dev](http://web.dev/)</i>)_

Tout ce que nous avons discuté dans les sections précédentes est destiné à vous aider à prendre une décision éclairée. Ayant vu comment ces deux concepts se comparent et contrastent, considérons maintenant les facteurs suivants :

### Compréhension et Confort

À quel point comprenez-vous chaque concept ? Les container queries sont relativement nouvelles, mais si vous passez du temps à les étudier et à expérimenter avec elles, comme avec les media queries, la courbe d'apprentissage n'est pas intimidante. Utilisez donc en production celle que vous comprenez et avec laquelle vous êtes le plus à l'aise, pour vous faciliter la vie.

### Exigences et Complexité du Projet

Quelle est l'approche de conception que vous utilisez et à quel point votre projet est-il complexe ? Parce que parfois l'approche de conception de votre projet déterminera lequel de ces deux concepts conviendra le mieux à vos besoins. De plus, plus le projet est complexe, plus il sera difficile de maintenir votre code, et vous voulez utiliser quelque chose que vous pouvez gérer.

### Tendances Futures et Collaboration

L'avenir de la conception réactive semble de plus en plus intrinsèque. Nous passons progressivement à une réactivité des composants basée sur les changements de leur contenu individuel, et les container queries excellent dans ce domaine.

Mais les media queries ne semblent pas disparaître de sitôt, vous pouvez donc les utiliser ensemble pour obtenir une réactivité parfaite sur de nombreux appareils différents.

## Conclusion

Le potentiel des container queries pour permettre la création de composants réutilisables en CSS est passionnant – mais cela peut ne pas être prêt à remplacer complètement les media queries pour rendre les pages web réactives pour l'instant.

Pour l'instant, notre meilleur pari est de les utiliser ensemble, et là où chacun a le plus de sens. Et vous pouvez être sûr de faire le bon choix en expérimentant davantage pour internaliser les avantages et les inconvénients de chacun.

Voici quelques ressources utiles :

* [freeCodeCamp sur les Media Queries](https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/)
* [Ahmad Shadeed sur les Container Queries](https://ishadeed.com/article/css-container-query-guide/)
* [Comment utiliser les Media Queries et les Container Queries](https://www.youtube.com/watch?v=2rlWBZ17Wes)