---
title: Conception Web Responsive – Comment Rendre un Site Attrayant sur Téléphones
  et Tablettes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-14T18:47:34.000Z'
originalURL: https://freecodecamp.org/news/responsive-web-design-how-to-make-a-website-look-good-on-phones-and-tablets
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/curve-design-futuristic-lines-911738.jpg
tags:
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
seo_title: Conception Web Responsive – Comment Rendre un Site Attrayant sur Téléphones
  et Tablettes
seo_desc: "By Adam Henson\nIn the rapidly evolving landscape of connected devices,\
  \ responsive web design continues to be crucial in web development. \nNot long ago\
  \ the term \"responsive web design\" was non-existent. But today, most of us have\
  \ had to adopt it to so..."
---

Par Adam Henson

Dans le paysage en rapide évolution des appareils connectés, la conception web responsive reste cruciale dans le développement web. 

Il n'y a pas si longtemps, le terme "conception web responsive" n'existait pas. Mais aujourd'hui, la plupart d'entre nous ont dû l'adopter dans une certaine mesure. 

[Selon Statistica](https://www.statista.com/statistics/275814/mobile-share-of-organic-search-engine-visits/), en 2019, 61 % de toutes les visites de recherche Google ont lieu sur un appareil mobile. En septembre 2020, [Google modifiera son algorithme de recherche](https://webmasters.googleblog.com/2020/03/announcing-mobile-first-indexing-for.html) pour privilégier les sites web adaptés aux mobiles.

**Dans cet article, je vais aborder les points suivants :**

* Qu'est-ce que la conception web responsive ?
* La balise meta viewport et son rôle
* Techniques efficaces utilisées dans la conception web responsive pour accommoder les appareils mobiles et tablettes
* Outils pour aider à simuler et surveiller l'expérience utilisateur sur mobile et tablette

## Qu'est-ce que la Conception Web Responsive (RWD) ?

La conception web responsive est une approche qui se concentre sur l'environnement de l'utilisateur d'un site web. L'environnement de l'utilisateur dépendra de l'appareil avec lequel il se connecte à Internet. 

Il existe de nombreuses caractéristiques d'appareils qui offrent des opportunités pour une approche centrée sur l'utilisateur. Certaines d'entre elles incluent : 

* la connexion réseau 
* la taille de l'écran 
* le type d'interaction (écrans tactiles, pavés tactiles)
* la résolution graphique. 

Avant que la conception web responsive ne devienne populaire, de nombreuses entreprises géraient un site web entièrement séparé qui recevait le trafic redirigé en fonction de l'agent utilisateur. 

Mais dans la conception web responsive, le serveur envoie toujours le même code HTML à tous les appareils, et le CSS est utilisé pour modifier le rendu de la page sur l'appareil.

Quelle que soit la stratégie adoptée, la première étape pour créer un site web pour téléphone ou tablette est de s'assurer que le navigateur connaît l'intention. C'est là que la balise meta viewport entre en jeu.

## La Balise Meta Viewport pour Identifier un Site Mobile

La balise meta viewport indique au navigateur comment ajuster la page à la largeur de chaque appareil. 

Lorsque l'élément meta viewport est absent, les navigateurs mobiles afficheront les pages web avec les paramètres par défaut du bureau. Cela entraîne une expérience apparemment zoomée, non responsive. 

Voici une implémentation standard :

```html
<meta name="viewport" content="width=device-width,initial-scale=1"/>
```

Maintenant que le navigateur sait ce qu'il se passe, nous pouvons utiliser des techniques populaires pour rendre notre site web responsive. ?

## Les Media Queries CSS pour Différentes Tailles et Orientations d'Écran

Si vous êtes nouveau dans la conception web responsive, les media queries sont la première et la plus importante fonctionnalité CSS à apprendre. Les media queries vous permettent de styliser des éléments en fonction de la largeur du viewport. Une stratégie CSS populaire consiste à écrire d'abord les styles mobiles et à construire par-dessus avec des styles plus complexes, spécifiques au bureau. 

Les media queries sont une partie importante de la conception web responsive, couramment utilisées pour les mises en page de grille, les tailles de police, les marges et les espacements qui diffèrent selon la taille et l'orientation de l'écran. 

Voici un exemple d'un cas d'utilisation courant de stylisation mobile first dans lequel une colonne a une largeur de 100 % pour les petits appareils, mais dans les viewports plus grands, elle est de 50 %.

```css
.column {
  width: 100%;
}

@media (min-width: 600px) {
  .column {
    width: 50%;
  }
}
```

Le code ci-dessus est un exemple simple, mais ce qu'il fait est assez intéressant.

1. En considérant d'abord le mobile, l'élément "column" est défini pour avoir une largeur de 100 % ;
2. En utilisant une media query `min-width`, nous définissons des règles spécifiquement pour les viewports avec une largeur minimale de `600px` (viewports plus larges que `600px`). Ainsi, pour les viewports plus larges que `600px`, notre élément colonne aura une largeur qui est de 50 % de celle de son parent.

Bien que les media queries soient essentielles pour la conception web responsive, de nombreuses autres nouvelles fonctionnalités CSS sont également de plus en plus adoptées et supportées dans les navigateurs. Flexbox est l'une de ces nouvelles fonctionnalités CSS importantes en termes de conception web responsive.

## Qu'est-ce que Flexbox ?

Vous vous demandez peut-être - "que fait Flexbox" ? La meilleure question est - "que ne peut pas faire Flexbox" ? Quel est le moyen le plus simple de centrer verticalement avec CSS ? Flexbox. Comment créer une mise en page de grille responsive ? Flexbox. Comment pouvons-nous atteindre la paix mondiale ? Flexbox.

Le module de mise en page Flexbox (Flexible Box) fournit un moyen plus efficace de disposer, aligner et distribuer l'espace entre les éléments dans un conteneur, même lorsque leur taille est dynamique (d'où le mot "flex").

Dans l'exemple ci-dessous, nous combinons les media queries comme expliqué ci-dessus pour créer une grille responsive. 

```html
<style>
  main {
    background: #d9d7d5;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  div {
    background: #767775;
    flex-basis: 100%;
    height: 100px;
    margin-bottom: 0.5rem;
  }

  @media (min-width: 600px) {
    main {
      flex-wrap: nowrap;
    }

    div {
      flex-basis: 33%;
    }
  }
</style>
<main>
  <div></div>
  <div></div>
  <div></div>
</main>
```

Nous accomplissons les actions suivantes avec ce code :

1. Établir une mise en page flexbox avec `display: flex` dans notre élément conteneur `main`.
2. Styliser pour le mobile first. Nous définissons l'élément `main` sur `flex-wrap: wrap`, ce qui permet aux éléments enfants de s'enrouler dans notre mise en page flexbox comme illustré ci-dessous dans la figure 1. Nous définissons `flex-basis: 100%` sur nos éléments `div` pour nous assurer qu'ils englobent 100 % de la largeur du parent dans la mise en page flexbox (figure 1).
3. Styliser pour les appareils plus grands comme les tablettes et les ordinateurs de bureau. Nous utilisons une media query similaire à notre exemple dans la section précédente pour définir notre élément conteneur `main` sur `flex-wrap: nowrap`. Cela garantit que les éléments enfants ne s'enroulent pas et qu'ils maintiennent une colonne dans un type de mise en page en ligne. En définissant `div` sur `flex-basis: 33%` dans la media query, nous établissons des colonnes qui représentent 33 % de la largeur du parent.
4. Dans cet exemple, la magie apparaîtrait sur les appareils plus grands avec nos règles de media query et flexbox combinées. Parce que nous avons défini `display: flex`, et parce que nous n'avons pas remplacé la règle dans la media query, nous avons une mise en page flexbox pour le mobile, la tablette et le bureau. Les règles de media query `flex-basis: 33%` et `display: flex` héritées nous donneront une mise en page flexbox reconnaissable comme vu dans la figure 2. Dans le passé, pour atteindre ce type de mise en page en colonnes, nous devions faire un sérieux travail et écrire des lignes de CSS complexes.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/grid-mobile-1.png)
_Figure 1 : Exemple de grille flexbox mobile_

![Image](https://www.freecodecamp.org/news/content/images/2020/07/grid-desktop.png)
_Figure 2 : Exemple de grille flexbox desktop_

Flexbox offre un excellent moyen d'obtenir des mises en page variées et fluides. Dans certains cas, nous n'avons pas autant de liberté dans l'espace vertical. Nous devons peut-être faire tenir un élément dans une hauteur fixe. Dans cette situation, nous avons une autre technique à notre disposition - le défilement horizontal.

## Défilement Horizontal avec Overflow Scroll

Il peut arriver que vous ayez du contenu débordant du viewport sans moyen élégant de le gérer. Voici... overflow scroll à la rescousse. ? 

Les utilisations courantes de cette technique incluent les menus et tableaux défilants. Voici un exemple de menu défilant.

<menu style="margin: auto; max-width: 826px; background: #d9d7d5; padding: 0.25rem; overflow-y: scroll; white-space: nowrap;">
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">Conception Web Responsive</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">RWD</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">Menu responsive</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">Exemple de défilement</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">C'est beaucoup de contenu !</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">Oui</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">nous</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">avons</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">un autre</span>
  <span style="background: #767775; color: #ffffff; display: inline-block; margin: 0.25rem; padding: 0.5rem;">élément</span>
</menu>

```html
<style>
  menu {
    background: #d9d7d5;
    padding: 0.25rem;
    overflow-y: scroll;
    white-space: nowrap;
  }

  span {
    background: #767775;
    color: #ffffff;
    display: inline-block;
    margin: 0.25rem;
    padding: 0.5rem;
  }
</style>
<menu>
  <span>Conception Web Responsive</span>
  <span>RWD</span>
  <span>Menu responsive</span>
  <span>Exemple de défilement</span>
  <span>C'est beaucoup de contenu !</span>
  <span>Oui</span>
  <span>nous</span>
  <span>avons</span>
  <span>un autre</span>
  <span>élément</span>
</menu>
```

Comment avez-vous fait cela ? Plongeons plus profondément.

* `overflow-y: scroll` est l'ingrédient clé de cette recette. En le spécifiant, les éléments enfants déborderont de l'axe horizontal avec un comportement de défilement.
* Pas si vite ! Bien que vous puissiez penser que `overflow-y` serait suffisant, nous devons également dire au navigateur de ne pas envelopper les éléments enfants avec `white-space: nowrap` ?

Maintenant que nous avons quelques techniques de mise en page RWD dans notre manche, examinons les éléments qui posent des défis spécifiques à leur nature visuelle - les images et les vidéos.

## Images Responsive

En utilisant les attributs modernes des balises d'image, nous pouvons accommoder une gamme d'appareils et de résolutions. Voici un exemple d'image responsive.

```html
<style>
  img {
    max-width: 100%;
  }
</style>

<picture>
  <source type="image/webp" srcset="https://my-image.com/my-image-100.webp 1x, https://my-image.com/my-image-200.webp 2x">
  <source type="image/png" srcset="https://my-image.com/my-image-100.png 1x, https://my-image.com/my-image-200.png 2x">
  <img alt="mon image" src="https://my-image.com/my-image-200.png" loading="lazy" width="100" height="100">
</picture>
```

Cela fait beaucoup de choses. Décomposons cela :

1. En définissant `max-width: 100%`, l'image sera redimensionnée en fonction de la largeur de son conteneur.
2. En utilisant une combinaison de balises `picture`, `source` et `img`, nous ne rendons en réalité qu'une seule image et ne chargeons que l'image la mieux adaptée en fonction de l'appareil de l'utilisateur.
3. **WebP** est un format d'image moderne qui offre une compression supérieure pour les images sur le web. En utilisant `source`, nous pouvons référencer une image WebP pour les navigateurs qui la supportent, et une autre balise `source` pour référencer une version PNG des images qui ne supportent pas WebP.
4. `srcset` est utilisé pour indiquer au navigateur quelle image utiliser en fonction de la résolution de l'appareil.
5. Nous établissons le [chargement paresseux natif](https://web.dev/native-lazy-loading/) en utilisant la paire attribut/valeur `loading="lazy"`.

## Vidéo Responsive

La vidéo responsive est un autre sujet qui a inspiré un grand nombre d'articles et de documentations. 

Une stratégie clé pour établir des images et vidéos responsive, des iframes et d'autres éléments implique l'utilisation du ratio d'aspect. La boîte de ratio d'aspect n'est pas une technique nouvelle et est un outil assez utile à avoir dans sa manche en tant que développeur web.

[Cet article fournit une démonstration solide](https://css-tricks.com/fluid-width-video/) sur la façon d'obtenir des vidéos de largeur "fluide". Examinons le code et décomposons-le.

```html
<style>
  .videoWrapper {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 */
    height: 0;
  }

  .videoWrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
</style>

<div class="videoWrapper">
  <!-- Copié et collé depuis YouTube -->
  <iframe width="560" height="349" src="http://www.youtube.com/embed/n_dZNLr2cME?rel=0&hd=1" frameborder="0" allowfullscreen></iframe>
</div>
```

Dans cet exemple, nous avons une vidéo YouTube intégrée en tant qu'iframe et un conteneur `div` avec la classe `videoWrapper`. Ce code fait beaucoup de choses... creusons.

* `position: relative` sur l'élément conteneur permet aux éléments enfants d'utiliser le positionnement absolu par rapport à celui-ci.
* `height: 0` combiné avec `padding-bottom: 56.25%` est l'ingrédient clé ici, qui établit un comportement dynamique, imposant un ratio d'aspect `16:9`.
* `position: absolute`, `top: 0` et `left: 0` définis sur l'iframe créent un comportement dans lequel l'élément se positionne de manière absolue par rapport à son parent... le collant en haut à gauche.
* Et enfin, une largeur et une hauteur de 100 % rendent l'élément enfant, l'iframe, à 100 % de son parent. Le parent, `.videoWrapper`, prend le contrôle total de l'établissement de cette mise en page de ratio d'aspect.

Je sais... c'est beaucoup. Il y a plus que nous pouvons faire pour que les vidéos et les images soient au mieux sur les téléphones et les tablettes. Je vous encourage à faire des recherches sur ces sujets de manière indépendante en plus de cela.

D'accord, maintenant que nous sommes des maîtres de la conception web responsive, comment pouvons-nous tester ce que nous avons fait ? Heureusement, nous avons un certain nombre d'outils pour simuler et surveiller l'expérience utilisateur sur une variété d'appareils.

## Outils pour Simuler et Surveiller les Sites Web Responsive

Il existe une variété d'outils utiles pour nous aider à créer des sites web avec une conception web responsive. Voici quelques-uns que je trouve particulièrement utiles.

### Émulation Mobile avec Chrome DevTools

Les DevTools de Chrome fournissent une émulation mobile pour une gamme d'appareils tablettes et mobiles. Ils offrent également une option "responsive" qui vous permet de définir une taille de viewport personnalisée.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-12-at-6.19.18-PM.png)
_Figure 3 : Émulation d'appareils mobiles et tablettes avec Chrome DevTools_

### Surveillance des Performances de Site Mobile avec Foo

Lighthouse est un outil open-source qui fournit un moyen d'analyser les performances d'un site web spécifique à un appareil. 

[Foo utilise Lighthouse en arrière-plan pour surveiller les performances d'un site web et fournit des commentaires pour l'analyse](https://www.foo.software/lighthouse/). Vous pouvez configurer la surveillance pour les appareils de bureau et mobiles afin d'obtenir des commentaires continus sur la réactivité de votre site web. 

Par exemple, un rapport Lighthouse signalera les images qui sont incorrectement chargées en fonction de l'appareil.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-12-at-6.31.09-PM.png)
_Figure 4 : Rapport Lighthouse avec émulation d'appareil mobile_

## Conclusion

La conception web responsive continuera d'évoluer rapidement, mais si nous restons au courant des tendances actuelles, nous pouvons offrir la meilleure expérience à nos utilisateurs. J'espère que ces outils et techniques sont utiles !

Non seulement les utilisateurs de notre site web bénéficieront d'une conception polyvalente, mais les moteurs de recherche classeront également nos pages web plus haut.