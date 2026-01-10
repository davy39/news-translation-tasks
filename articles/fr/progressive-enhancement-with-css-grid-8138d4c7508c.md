---
title: Amélioration Progressive avec CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T18:16:46.000Z'
originalURL: https://freecodecamp.org/news/progressive-enhancement-with-css-grid-8138d4c7508c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W_qmeZuel90pFUHZ89TfZQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Amélioration Progressive avec CSS Grid
seo_desc: 'By Dominic Fraser

  CSS Grid (Grid) has been out for some time now, with full support in major modern
  browsers. I’ll leave others to dive into why it’s so great and what new design possibilities
  it makes so easy to explore. If you have been looking for...'
---

Par Dominic Fraser

CSS Grid (Grid) existe depuis un certain temps maintenant, avec un [support complet](https://caniuse.com/#search=css%20grid) dans les principaux navigateurs modernes. Je laisserai à d'autres le soin d'explorer pourquoi c'est si génial et quelles nouvelles possibilités de design cela rend si faciles à explorer. Si vous avez cherché la meilleure façon de supporter les designs web responsives, je n'ai pas encore vu quelqu'un qui n'aime pas Grid. Il est simple à utiliser, tout en étant extrêmement puissant et flexible.

Mais, je vous entends dire, beaucoup de nos utilisateurs n'utilisent pas les versions les plus récentes des navigateurs, ou se trouvent dans des marchés où Chrome/Firefox ne détiennent pas une part majoritaire. Et, vraiment, est-ce que réécrire tout notre ancien code en vaut vraiment la peine ?

Je ressentais la même chose, jusqu'à ce que j'entende une excellente conférence donnée par [Natalya Shelburne](https://twitter.com/natalyathree). Elle a décrit comment elle a commencé à utiliser [CSS Grid aux côtés de Bootstrap](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4), sans perdre le support des anciens navigateurs, en **améliorant** plutôt qu'en **supprimant** l'ancien CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/DWlI6bjdjAkRW7ulEUC81RdWpFspo3qM46E8)
_[ScotlandCSS](https://twitter.com/rachelandrew" rel="noopener" target="_blank" title="">Rachel Andrew</a> par <a href="https://twitter.com/chicgeek" rel="noopener" target="_blank" title="">Laura Kishimoto</a> à <a href="http://scotlandcss.com/" rel="noopener" target="_blank" title=")_

Importamment, cela se fait sans utiliser de polyfills JavaScript, mais en utilisant du CSS pur. Comme le mentionne Rachel Andrew :

> _Comme nous le savons déjà, **les navigateurs qui ne supportent pas grid sont plus anciens**, plus lents ou des navigateurs souvent trouvés sur des appareils moins puissants dans les marchés émergents. Pourquoi forcer un tas de JavaScript sur ces appareils ?_

Natalya décrit comment les "[requêtes de fonctionnalités](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)" peuvent être utilisées pour implémenter Grid dans les navigateurs qui le supportent, sans perdre les fonctionnalités existantes. MDN fait référence à cela comme à l'"[amélioration progressive](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/CSS_Grid_and_Progressive_Enhancement)", déclarant que :

> Il est worth noter que vous n'avez pas à utiliser grid de manière _tout ou rien_. Vous pourriez commencer par simplement améliorer des éléments dans votre design avec grid, qui pourraient autrement s'afficher en utilisant une méthode plus ancienne.

### Utilisation de Grid

Alors, comment procéder ?

Dans un précédent article, j'ai décrit une approche simple pour "[garder votre pied de page où il appartient](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c)." Cela évite les problèmes rencontrés lorsque le contenu principal d'une page est trop petit pour pousser un pied de page en bas de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/Ums6BuchBW-nqPBRODUiKzPx7HvwKDa19BNj)
_De "[Comment garder votre pied de page où il appartient](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c" rel="noopener" target="_blank" title=")"_

Cela offre une chance de montrer comment une requête de fonctionnalité peut être utilisée pour passer à l'utilisation de Grid.

**Il est important de noter** que ceci est un exemple de **comment** vous pourriez passer à l'utilisation de Grid dans une base de code existante, **pas pourquoi** c'est un outil puissant. Cet exemple est utilisé parce qu'il est petit — il est donc possible de comprendre le **comment** sans les distractions trouvées dans une base de code plus grande.

Réalistement, Grid n'apporte pas de grande amélioration ici. Les avantages de l'utilisation d'un nouvel outil devraient être discutés, plutôt que de simplement l'implémenter parce que c'est cool !

L'exemple est ci-dessous. Plus d'explications sur le code [ici](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c).

```html
<!DOCTYPE html>
<html>
 <head>
   <link rel="stylesheet" type="text/css" href="main.css" />
 </head>
<body>
 <div id="page-container">
   <div id="content-wrap">
     <!-- tout le reste du contenu de la page -->
   </div>
   <footer id="footer"></footer>
 </div>
</body>
</html>
```

Il y a deux parties principales pour ajouter Grid :

* ajouter les nouvelles propriétés de grid nécessaires
* remplacer les propriétés qui ne sont plus nécessaires.

`main.css` :

```css
#page-container {
  position: relative;
  min-height: 100vh;
}
#content-wrap {
  padding-bottom: 2.5rem;    /* Hauteur du pied de page */
}
#footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 2.5rem;            /* Hauteur du pied de page */
}
```

`main.css` peut être étendu pour **ajouter** :

```css
@supports (display: grid) {
    #page-container {
        position: static;               // remplacer
        display: grid;                  // nouveau   
        grid-template-rows: 1fr auto;   // nouveau
        grid-template-columns: 100%;    // nouveau
    }
    
    #content-wrap {
        padding-bottom: 0;              // remplacer
    }
    #footer {
        position: static;               // remplacer 
        height: auto;                   // remplacer
    }
}
```

`position` est réinitialisé à sa valeur [par défaut](https://developer.mozilla.org/en-US/docs/Web/CSS/position) de `static`, et le `padding` et la `height` sont réinitialisés à des valeurs qui n'interfèrent pas avec la nouvelle mise en page.

`min-height: 100vh` n'est pas référencé. Il est également utilisé par Grid, donc il n'a pas besoin d'être modifié.

Trois nouvelles propriétés `grid` liées sont ajoutées. L'utilisation d'une seule [unité fractionnaire](https://css-tricks.com/snippets/css/complete-guide-grid/#fr-unit) `1fr` garantit que le premier élément enfant de `page-container` (dans ce cas `content-wrap`) remplira tout l'espace restant que la hauteur `auto` du deuxième élément enfant `footer` n'occupe pas.

Et c'est tout ! Maintenant, les navigateurs qui supportent Grid utiliseront le code dans la requête de fonctionnalité, tout en continuant à supporter pleinement les navigateurs qui ne le supportent pas. Cela permet même d'ajouter Grid à des composants individuels un à la fois — une équipe peut voir à quel point le processus est simple sans un énorme investissement en temps.

Espérons que cela illustre l'approche incrémentale qui peut être adoptée pour utiliser Grid.

#### Utilisations plus complexes

Le pouvoir de ce que Grid offre est mieux vu dans les exemples plus complexes [écrits par Natalya](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4) qui ont inspiré cet article de mise à jour. Cela montre le pouvoir de ce que Grid peut offrir lorsqu'il est utilisé à plus grande échelle.

### Conseils rapides

Le code de repli peut être testé sans accès à un ancien navigateur ou émulateur. Modifiez temporairement `@supports (display: grid)` par une valeur inexistante, par exemple `gridNO`, afin que le code de repli soit utilisé.

Firefox propose certains outils formidables que Chrome n'a pas actuellement. Il s'agit des "Paramètres d'affichage de la grille" activés dans l'onglet "Inspecteur". Ces paramètres aident à illustrer visuellement comment Grid est exécuté, ce qui est idéal pour les mises en page complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/P2Ilh7vTFUoXlcn31P1q1rfT5LcWOV4iLkBV)
_Outils de développement Firefox sous Inspecteur_

Enfin, j'ai été inspiré par une déclaration de Rachel Andrew :

> Cela ne devrait pas avoir la même apparence dans tous les navigateurs, cela devrait être une bonne expérience dans tous les navigateurs.

Le défaut de nombreuses entreprises est de s'efforcer de reproduire une expérience identique dans chaque navigateur. Mais est-il judicieux de considérer que sur des navigateurs plus anciens et plus lents, une approche plus simple pourrait en fait offrir une meilleure expérience ?

Merci d'avoir lu 😊 J'espère que cela vous inspirera à essayer d'utiliser Grid non seulement dans des projets greenfield, mais aussi aux côtés de tout ce que vous pourriez utiliser aujourd'hui !

### Ressources

* [De Bootstrap à CSS Grid](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4)
* [Maintenir le pied de page en bas avec CSS-Grid](https://dev.to/niorad/keeping-the-footer-at-the-bottom-with-css-grid-15mf)
* [Un guide complet de Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
* [CSS Grid Layout et Amélioration Progressive](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/CSS_Grid_and_Progressive_Enhancement)
* [Utilisation de CSS Grid : Support des navigateurs sans Grid](https://www.smashingmagazine.com/2017/11/css-grid-supporting-browsers-without-grid/)

Voici quelques autres articles que j'ai écrits récemment :

* [Utilisation de Pa11y CI et Drone comme gardiens des tests d'accessibilité](https://hackernoon.com/using-pa11y-ci-and-drone-as-accessibility-testing-gatekeepers-a8b5a3415227)
* [Simulation de requêtes HTTP avec Nock](https://codeburst.io/testing-mocking-http-requests-with-nock-480e3f164851)