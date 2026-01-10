---
title: Mises en page Web – Comment utiliser CSS Grid et Flex pour créer une page Web
  réactive
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2022-10-21T23:12:52.000Z'
originalURL: https://freecodecamp.org/news/web-layouts-use-css-grid-and-flex-to-create-responsive-webpages
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/WebLayouts-1.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Mises en page Web – Comment utiliser CSS Grid et Flex pour créer une page
  Web réactive
seo_desc: "Your web layout is to your website what a floor plan is to a building.\
  \ Without them, you’re just building castles in the air. \nThe first thing to do\
  \ when you have a website or application to build or design is to decide on the\
  \ layout. This is importa..."
---

La mise en page de votre site web est à votre site ce qu'un plan de sol est à un bâtiment. Sans eux, vous construisez des châteaux en l'air. 

La première chose à faire lorsque vous avez un site web ou une application à construire ou à concevoir est de décider de la mise en page. Cela est important car c'est dans cette mise en page que vous spécifiez comment les éléments sont disposés afin que vous puissiez les évaluer de la manière et de la hiérarchie prévues.

En gros, le but de toute mise en page web est de réduire la confusion, d'améliorer l'utilisabilité et de donner finalement à vos utilisateurs une expérience agréable. Certains des principaux éléments d'une mise en page sont la navigation, les menus et le contenu. 

En développement web et front-end, avoir une mise en page en tête avant de construire peut vous aider à décider quel module de mise en page CSS utiliser : Flexbox ou Grid.

Dans cet article, nous allons apprendre ce que sont chacun de ces outils et la meilleure façon de les utiliser en construisant une page de destination simple mais belle.

## Ce que nous allons construire

![Image](https://www.freecodecamp.org/news/content/images/2022/10/homepage-2.png)
_conception de la page de destination_

Consultez-le sur Codepen [ici](https://codepen.io/ophyboamah/pen/KKRLoJr).

## Fonctionnalités du projet

1. Mise en page Web : Créer une belle page de destination
2. Réactivité mobile

## Prérequis

* Connaissance de base du HTML et du CSS.
* Un IDE (éditeur de texte) comme VS Code
* Un navigateur web

## Installation

1. Créez un dossier pour votre projet et ouvrez-le dans un IDE.
2. Dans votre dossier de projet, créez les fichiers index.html et style.css.
3. Créez un dossier d'assets pour stocker les images.
4. Dans votre fichier index.html, créez votre modèle HTML de base et liez votre fichier CSS et l'URL de la police dans la balise `<head>`.

## Ressources

1. **Police** : [https://fonts.googleapis.com/css2?family=Epilogue:wght@500;700&family=Poppins:wght@400;500;700&display=swap](https://fonts.googleapis.com/css2?family=Epilogue:wght@500;700&family=Poppins:wght@400;500;700&display=swap)
2. **Image de bureau** : [https://i.postimg.cc/0Nt97Bhf/image-hero-desktop.png](https://i.postimg.cc/0Nt97Bhf/image-hero-desktop.png)
3. **Image mobile** : [https://i.postimg.cc/ZnYfhwwW/image-hero-mobile.png](https://i.postimg.cc/ZnYfhwwW/image-hero-mobile.png)
4. **Logo du client (Databiz)** : [https://i.postimg.cc/gJ9Y84m6/client-databiz.png](https://i.postimg.cc/gJ9Y84m6/client-databiz.png)
5. **Logo du client (Audiophile)** : [https://i.postimg.cc/15DDqYSD/client-audiophile.png](https://i.postimg.cc/15DDqYSD/client-audiophile.png)
6. **Logo du client (Meet)** : [https://i.postimg.cc/5ybQqfbv/client-meet.png](https://i.postimg.cc/5ybQqfbv/client-meet.png)
7. **Logo du client (Maker)** : [https://i.postimg.cc/g2NsxByN/client-maker.png](https://i.postimg.cc/g2NsxByN/client-maker.png)

# Comment utiliser Flexbox

Généralement, les éléments HTML s'alignent selon leur style d'affichage par défaut. Cela signifie que, sans style externe avec CSS, les éléments de bloc comme `p` et `div` commenceront sur une nouvelle ligne. Les éléments en ligne comme `input` et `span`, en revanche, sont disposés les uns à côté des autres sur la même ligne.

Cependant, le concept de Flexbox vous permet de placer facilement ces éléments soit horizontalement, soit verticalement dans ce qui est souvent appelé une dimension. Pour y parvenir, au moins deux éléments sont nécessaires : **conteneur flex** et **élément flex**. Ceux-ci font référence à un élément parent et à un élément enfant, respectivement.

En conception réactive, le but de Flexbox est de permettre aux conteneurs et à leurs éléments enfants de remplir les espaces définis ou de se réduire en fonction des dimensions d'un appareil.

## Flex-direction et axes

Flex-direction est une propriété importante de CSS Flexbox, car c'est ce qui détermine la direction dans laquelle les éléments flex sont disposés. Il le fait en indiquant l'axe principal d'un conteneur flex.

Il existe deux axes principaux, à savoir **axe principal** et **axe transversal**. L'axe principal est la direction définie de la manière dont vos éléments flex sont placés dans le conteneur flex, tandis que l'axe transversal est toujours l'axe du côté opposé à l'axe principal. 

Il peut être dangereux d'essayer d'utiliser le concept des axes x et y des mathématiques pour comprendre cela. Cela est principalement dû au fait que dans Flexbox, l'axe principal peut être vertical ou horizontal, toujours en fonction de la valeur de la flex-direction.

Les valeurs acceptées par la propriété flex-direction incluent row (qui est la valeur par défaut), row-reverse, column et column-reverse. Pour les besoins de ce projet, nous allons examiner row et column.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/flexdirection.png)
_flex-direction: row_

Lorsque l'attribut flex-direction a une valeur de row, l'axe principal est horizontal et l'axe transversal est vertical, comme le montre l'image ci-dessus. Cela signifie que les éléments flex seront disposés horizontalement. 

Puisque row est la valeur par défaut, si vous affichez un conteneur comme flex mais ne spécifiez pas la flex-direction, les éléments flex seront automatiquement en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/flexdirectioncolumn.png)
_flex-direction: column_

Lorsque l'attribut flex-direction a une valeur de column, l'axe principal est vertical et l'axe transversal est horizontal, comme le montre l'image ci-dessus. Cela signifie que les éléments flex seront disposés verticalement. 

## Comment construire la barre de navigation

Maintenant que nous savons comment fonctionne Flexbox, commençons à construire notre barre de navigation. Nous allons d'abord fournir le contenu à l'intérieur, c'est-à-dire les éléments de menu et le logo. Nous leur donnerons des classes descriptives afin de pouvoir facilement les référencer dans notre fichier CSS.

```html
<nav>
      <h2 class="logo">snap</h2>
      <ul class="menu-items">
        <li>Fonctionnalités</li>
        <li>Entreprise</li>
        <li>Carrières</li>
        <li>À propos</li>
      </ul>
      <ul class="cta-btns">
        <li>Connexion</li>
        <li>Inscription</li>
      </ul>
</nav>
```

L'image ci-dessous est le résultat du code ci-dessus. Parce que `<ul>` et `<li>` sont des éléments de bloc, chacun des éléments que nous avons spécifiés à l'intérieur d'eux sera affiché sur une nouvelle ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/preflexx-1.png)
_Sortie du contenu de la barre de navigation_

L'affichage de la mise en page Flexbox est déclaré sur les conteneurs parents et affecte les éléments enfants. Cela signifie que si vous aviez une liste de courses dans une liste non ordonnée, display flex ne peut pas être appliqué sur les `<li>` qui sont des éléments enfants dans ce cas. Au lieu de cela, pour les afficher comme flex, vous devriez d'abord créer un conteneur parent et l'appliquer à celui-ci. 

Dans notre code CSS ci-dessous, nous définissons le style et la taille de la police pour notre projet ainsi que notre logo de barre de navigation. Nous affichons également nos éléments de navigation et certains des éléments à l'intérieur de ceux-ci comme flex. 

```css
* {
  font-family: "Epilogue", sans-serif;
  font-size: 0.85rem;
}

.logo {
  font-size: 1.3rem;
}

nav,
.cta-btns,
.menu-items {
  display: flex;
}
```

L'image ci-dessous est le résultat du code ci-dessus. Les éléments ont été affichés comme flex. Pourtant, parce que nous n'avons pas spécifié la flex-direction, ils sont automatiquement disposés en ligne. 

Mais comme vous pouvez le voir ci-dessous en utilisant la règle (ligne rouge), les éléments flex ne sont pas alignés comme ils devraient l'être. Corrigons cela en apprenant un autre élément flex important.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/displayflex.png)
_Flex sans alignement_

### Comment utiliser l'attribut `align-items`

Il s'agit d'un attribut Flexbox qui contrôle la disposition des éléments flex sur l'axe transversal. Les valeurs qu'il prend sont flex-start, flex-end et center en fonction des besoins d'alignement de l'élément. L'image ci-dessous montre comment chacun d'eux fonctionne. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/align-items-1.png)
_Crédit image : freeCodeCamp_

D'après l'image ci-dessus, nous pouvons voir que si nous voulons nous assurer que les éléments flex à l'intérieur de notre `<nav>` sont correctement alignés, sur cet élément, nous devons donner à l'attribut align-items une valeur de center. Nous devons donc ajouter un attribut _align-items_ et une valeur de _center_ à notre conteneur flex comme montré dans le code CSS ci-dessous :

```css
nav,
.cta-btns,
.menu-items {
  display: flex;
  align-items: center;
}
```

Comme vous pouvez le voir dans l'image ci-dessous, les éléments flex sont maintenant alignés comme ils devraient l'être. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/aligncenter.png)
_Flex avec alignement central_

Mais une fois de plus, il manque quelque chose. Nous voulons que nos éléments soient bien répartis sur la barre de navigation : le logo à l'extrême gauche, la connexion et l'inscription à l'extrême droite, et le reste au milieu. 

Nous pouvons y parvenir avec l'attribut `justify-content`. Apprenons-en davantage à ce sujet ensuite, puis mettons-le en œuvre.

### Comment utiliser l'attribut `justify-content`

Il s'agit d'un attribut Flexbox qui contrôle la disposition des éléments flex sur l'axe principal. Il définit également comment les navigateurs distribuent l'espace entre et autour des éléments flex dans un conteneur flex. 

Pour atteindre la réactivité, il aide à allouer tout espace excédentaire restant après que les éléments flex ont été disposés.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/justifycontentstyles.png)
_styles justify-content_

D'après les styles associés aux différentes valeurs de l'attribut justify-content, nous pouvons voir que les deux derniers sont plus similaires à ce que nous essayons d'atteindre. 

Nous pouvons soit opter pour l'espace autour ou l'espace entre et fournir un peu de rembourrage sur les côtés pour pousser les éléments aux extrémités extrêmes des bords. Nous donnons également à l'attribut list-style une valeur de none pour supprimer les points devant les éléments de la liste.

```css
li {
  list-style: none;
}

nav {
  justify-content: space-between;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/justifycontent-2.png)
_sortie de la barre de navigation justify-content_

Maintenant que nous avons placé les éléments à leurs positions souhaitées, nous devons créer de légers espaces entre eux. Dans ce cas, nous allons donner à chaque élément de liste une marge droite de 1rem. Nous définissons également d'autres styles comme la taille des polices, la couleur et une bordure pour l'élément d'inscription. 

```css
nav {
  margin: 0 1.5rem 1.5rem 1.5rem;
  justify-content: space-between;
}

.logos-section {
  display: flex;
}

.menu-items li,
.cta-btns li {
  font-size: 0.7rem;
  margin-right: 1rem;
  color: hsl(0, 0%, 41%);
}

.cta-btns li:nth-last-child(1) {
  border: 1px solid gray;
  padding: 0.2rem 0.7rem;
  border-radius: 0.3rem;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/justifyandstyles-1.png)
_Barre de navigation avec styles_

Après avoir implémenté le code ci-dessus, voici l'apparence finale de notre barre de navigation. Et cela marque la fin de notre section Flexbox. Ensuite, nous construirons la dernière partie de notre page de destination avec CSS Grid.

# Comment utiliser CSS Grid

CSS Grid est un outil révolutionnaire pour créer des mises en page web. Il vous aide à créer des mises en page simples et complexes. La principale différence est que tandis que Flexbox aide à l'arrangement unidimensionnel des éléments, CSS grid est capable de faire des arrangements bidimensionnels. 

Le concept des axes que nous avons appris sous Flexbox s'applique toujours ici. Vous pouvez utiliser CSS Grid pour organiser les éléments sur l'axe principal et l'axe transversal en même temps. 

En résumé, Flexbox vous permet d'organiser les éléments horizontalement (en ligne) ou verticalement (en colonne). Mais avec CSS Grid, vous pouvez aligner les éléments à la fois verticalement et horizontalement.

La mise en page CSS Grid est déclarée uniquement sur les éléments parents ou les conteneurs. En effet, tous ses enfants deviennent des éléments de grille. Une fois que vous avez le conteneur cible, vous lui donnez un attribut d'affichage et une valeur de grille. La taille des lignes et des colonnes d'une grille peut être déterminée avec `grid-template-rows` et `grid-template-columns`, respectivement.

## Comment construire la page d'accueil

Tout comme nous l'avons fait avec la barre de navigation, commençons par définir notre contenu dans une section `<main>` dans notre fichier HTML. 

En regardant notre image cible, nous avons deux sections principales : la section de gauche contiendra du texte et des logos tandis que la section de droite contiendra une image héroïque. C'est pour la vue web de notre projet. 

Commençons par définir notre contenu. La section avec la classe text-side contient : un en-tête, un texte de paragraphe, un bouton et un logo. La section avec la classe img-side ne contient qu'une image.

```html
<main>
      <section id="text-side">
        <h1>Make <br />remote work</h1>
        <p>
          Get your team in sync, no matter your location. Streamline processes,
          create team rituals, and watch productivity soar.
        </p>
        <button>Learn more</button>
        <div class="clients-logos">
          <img src="./assets/images/client-databiz.svg" />
          <img src="./assets/images/client-audiophile.svg" />
          <img src="./assets/images/client-meet.svg" />
          <img src="./assets/images/client-maker.svg" />
        </div>
      </section>
      <section class="img-side">
        <img src="./assets/images/image-hero-desktop.png" />
      </section>
    </main>
```

Dans la section principale, nous avons créé les deux sections dont nous avions besoin et leur avons donné des identifiants descriptifs : text-side et img-side. 

Dans le text-side, nous avons ajouté un en-tête, un texte de paragraphe, un bouton et une div pour afficher les logos des clients. La seule chose dont nous avons besoin pour le img-side est l'image d'affichage.

```css
/* Logos des clients */
.clients-logos img {
  width: 5rem;
  margin-right: 1rem;
}

.clients-logos {
  margin-top: 4rem;
}

.clients-logos img:nth-child(2) {
  width: 3rem;
}

/* Principal */
main h1 {
  font-size: 3rem;
}

main p {
  font-size: 0.7rem;
  width: 18rem;
  color: hsl(0, 0%, 41%);
  line-height: 0.9rem;
}

main button {
  background-color: hsl(0, 0%, 8%);
  color: #fff;
  border: none;
  font-size: 0.7rem;
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  margin-top: 1rem;
}

#text-side {
  margin-top: 3rem;
}
/* Image héroïque */
.img-side img {
  width: 20rem;
}
```

Dans notre fichier CSS, nous devons styliser la div des logos des clients ainsi que les éléments enfants. Nous définissons également une taille de police pour l'en-tête et le paragraphe. Ensuite, nous stylisons notre bouton et attribuons une largeur à notre image.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/pregrid1-2.png)
_affichage de la page d'accueil pré-grille_

L'image ci-dessus montre comment notre page web apparaîtra après avoir défini le contenu et stylisé uniquement l'en-tête, le bouton et les logos – c'est-à-dire que nous n'avons pas encore déclaré notre conteneur comme une grille. Parce que presque tous les éléments que nous avons ici sont des éléments de bloc, nous les voyons s'aligner les uns sur les autres.

## Modèles de grille : lignes et colonnes

La propriété `grid-template-columns` spécifie le nombre et les largeurs des colonnes dans une grille, définissant une colonne de conteneur de grille en spécifiant la taille de ses pistes et les noms de ligne. 

La propriété `grid-template-rows` est l'opposé direct. Elle spécifie le nombre et les hauteurs des lignes dans une grille, définissant également une ligne de conteneur de grille en spécifiant la taille de ses pistes et les noms de ligne. 

Comme vous pouvez le voir dans l'image ci-dessous, `grid-template-rows` dispose les éléments du haut vers le bas de l'écran de l'appareil. `grid-template-columns` dispose les éléments du côté gauche vers le côté droit de l'écran de l'appareil. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/CSS-Grid.png)

Pour notre projet, nous allons utiliser `grid-template-columns` puisque nous voulons disposer nos deux sections côte à côte, en laissant chaque section occuper une partie égale de la largeur globale du projet. Nous faisons cela en l'assignant comme attribut sur le même conteneur que nous avons spécifié un affichage de grille.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/displaygrid.png)
_display: grid_

Maintenant que les deux sections à l'intérieur de notre balise `<main>` ont été placées de manière égale en utilisant grid-template-columns, nous avons deux dernières choses à faire. 

Nous devons les aligner horizontalement, en positionnant les deux éléments au centre de la page, avec l'espace supplémentaire à gauche de l'image, réparti uniformément des deux côtés. Nous devons également les aligner verticalement en positionnant les deux au centre de la page, avec l'espace supplémentaire en bas, réparti uniformément au-dessus et en dessous.

## Aligner et justifier dans CSS Grid

Bonne nouvelle – nous n'avons pas à apprendre de nouveaux concepts pour atteindre nos alignements souhaités dans les mises en page CSS Grid. Parce que, heureusement, `align-items` et `justify-content`, comme nous l'avons appris précédemment, ne sont pas exclusifs à Flebox. Vous pouvez également les utiliser pour positionner les éléments à la fois horizontalement et verticalement.

```css
main {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  height: 70vh;
  align-items: center;
  justify-content: center;
  margin-left: 8rem;
}
```

Comme vous pouvez le voir dans le code ci-dessus, nous avons seulement dû donner la valeur center aux attributs align-items et justify-content sur la balise parente (conteneur de grille). 

Pour nous assurer de voir l'effet de la position au centre parfait, nous avons également dû spécifier une hauteur pour la section. L'image ci-dessous est le résultat final de notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/homepage-4.png)
_Apparence finale de la page de destination_

## Comment le rendre réactif

Jusqu'à présent, tout ce que nous avons construit est pour le web. Mais pour les utilisateurs qui souhaitent accéder à la page de destination sur mobile, nous devons rendre notre projet accessible sur des écrans plus petits. Dans notre cas, nous visons des écrans qui sont supérieurs à 300px mais inférieurs à 480px. 

Comme vous pouvez le voir dans le code ci-dessous, nous masquons nos éléments de navigation et affichons un emoji avec la classe mobile-nav. À côté de cela, nous masquons l'image d'en-tête de bureau et affichons l'image d'en-tête mobile. 

```css
/* Réactif */
@media (min-width: 300px) and (max-width: 480px) {
  * {
    font-size: 1rem;
  }

  body {
    height: 100vh;
    width: 100vw;
    overflow-y: hidden;
    overflow-x: hidden;
  }

  nav {
    margin: 0 1.5rem 0 1.5rem;
  }

  nav ul {
    display: none;
  }
  
  .mobile-nav {
    display: block;
    margin-right: 2rem;
  }

  main {
    display: grid;
    grid-template-columns: 100%;
    margin: 0 auto;
  }

  /* Logos des clients */
  .clients-logos {
    margin-top: 2rem;
  }
  
  .desktop-logos {
    display: none;
  }
  
  .mobile-logos {
    display: block;
  }

  /* Images */
  .desktop-img {
    display: none;
  }
  .mobile-img {
    display: block;
    margin-top: 3rem;
  }

  .cta-btns,
  .menu-items {
    display: none;
  }

  main h1 {
    font-size: 2.5rem;
  }

  /* Logos des clients */
  .clients-logos img {
    width: 4.5rem;
    margin-right: 0.8rem;
  }

  .attribution {
    width: 13rem;
    margin: 8rem auto 0 auto;
    text-align: center;
  }
}
```

## Code complet du projet

Voici le projet que nous avons construit ensemble dans cet article :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/homepage-3.png)

Voici le code HTML complet :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- affiche le site correctement en fonction de l'appareil de l'utilisateur -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Epilogue:wght@500;700&family=Poppins:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css" />
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="./images/favicon-32x32.png"
    />

    <title>Web Layout | Landing Page</title>

    <!-- N'hésitez pas à supprimer ces styles ou à les personnaliser dans votre propre feuille de style 👍 -->
  </head>
  <body>
    <nav>
      <div class="logos-section">
        <h2 class="logo">snap</h2>
        <ul class="menu-items">
          <li>
            Fonctionnalités<svg
              width="10"
              height="6"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke="#686868"
                stroke-width="1.5"
                fill="none"
                d="m1 1 4 4 4-4"
              />
            </svg>
          </li>
          <li>
            Entreprise<svg
              width="10"
              height="6"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke="#686868"
                stroke-width="1.5"
                fill="none"
                d="m1 1 4 4 4-4"
              />
            </svg>
          </li>
          <li>Carrières</li>
          <li>À propos</li>
        </ul>
      </div>
      <ul class="cta-btns">
        <li>Connexion</li>
        <li>Inscription</li>
      </ul>
      <p class="mobile-nav">🌚</p>
    </nav>
    <main>
      <section id="text-side">
        <h1>Make <br />remote work</h1>
        <p>
          Get your team in sync, no matter your location. Streamline processes,
          create team rituals, and watch productivity soar.
        </p>
        <button>Learn more</button>
        <div class="clients-logos">
          <img src="https://i.postimg.cc/gJ9Y84m6/client-databiz.png" />
          <img src="https://i.postimg.cc/15DDqYSD/client-audiophile.png" />
          <img src="https://i.postimg.cc/5ybQqfbv/client-meet.png" />
          <img src="https://i.postimg.cc/g2NsxByN/client-maker.png" />
        </div>
      </section>
      <section id="img-side">
        <img
          class="desktop-img"
          src="https://i.postimg.cc/0Nt97Bhf/image-hero-desktop.png"
        />
        <img
          class="mobile-img"
          src="https://i.postimg.cc/ZnYfhwwW/image-hero-mobile.png"
        />
      </section>
    </main>
    <div class="attribution">
      Challenge by
      <a href="https://www.frontendmentor.io?ref=challenge" target="_blank"
        >Frontend Mentor</a
      >. Coded by <a href="https://codehemaa.com">Ophy Boamah</a>.
    </div>
  </body>
</html>
```

Voici le code CSS complet :

```css
* {
  font-family: "Epilogue", sans-serif;
  font-size: 1.3rem;
}

.logo {
  font-size: 1.3rem;
}

li {
  list-style: none;
}

nav,
.cta-btns,
.menu-items {
  display: flex;
  align-items: center;
}

nav {
  margin: 0 1.5rem 1.5rem 1.5rem;
  justify-content: space-between;
}

.mobile-nav {
    display: none;
}

.logos-section {
  display: flex;
}

.menu-items li,
.cta-btns li {
  font-size: 0.7rem;
  margin-right: 1rem;
  color: hsl(0, 0%, 41%);
}

.cta-btns li:nth-last-child(1) {
  border: 1px solid gray;
  padding: 0.2rem 0.7rem;
  border-radius: 0.3rem;
}

/* Logos des clients */
  
.clients-logos img {
  width: 8rem;
  margin-right: -3rem;
}

.clients-logos {
  margin-top: 1rem;
  margin-left: -2rem;
  display: flex;
  width: 10rem;
}

.clients-logos img:nth-child(2) {
  width: 7rem;
}

/* Principal */
main {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  height: 70vh;
  align-items: center;
  justify-content: center;
  margin-left: 8rem;
}
/* Images */
.desktop-img {
  display: block;
}
.mobile-img {
  display: none;
}

main h1 {
  font-size: 3rem;
}

main p {
  font-size: 0.7rem;
  width: 18rem;
  color: hsl(0, 0%, 41%);
  line-height: 0.9rem;
}

main button {
  background-color: hsl(0, 0%, 8%);
  color: #fff;
  border: none;
  font-size: 0.7rem;
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  margin-top: 1rem;
}

#text-side {
  margin-top: 3rem;
}
/* Image héroïque */
#img-side img {
  width: 20rem;
}

.attribution {
  font-size: 0.7rem;
  text-align: center;
  margin-top: 5.5rem;
}

.attribution a {
  color: hsl(228, 45%, 44%);
  font-size: 0.7rem;
}

/* Réactif */
@media (min-width: 300px) and (max-width: 480px) {
  * {
    font-size: 1rem;
  }

  body {
    height: 100vh;
    width: 100vw;
    overflow-y: hidden;
    overflow-x: hidden;
  }

  nav {
    margin: 0 1.5rem 0 1.5rem;
  }

  nav ul {
    display: none;
  }
  
  .mobile-nav {
    display: block;
    margin-right: 2rem;
  }

  main {
    display: grid;
    grid-template-columns: 100%;
    margin: -3rem auto 0 auto;
  }

  /* Logos des clients */
  .clients-logos {
    margin-top: 2rem;
  }
  
  .clients-logos img {
  width: 30rem;
}

.clients-logos {
  margin-top: 1rem;
  display: flex;
}

.clients-logos img:nth-child(2) {
  width: 7rem;
}

  /* Images */
  .desktop-img {
    display: none;
  }
  .mobile-img {
    display: block;
    margin-top: 3rem;
  }

  .cta-btns,
  .menu-items {
    display: none;
  }

  main h1 {
    font-size: 2.5rem;
  }

  /* Logos des clients */
  .clients-logos img {
    width: 4.5rem;
    margin-right: 0.8rem;
  }

  .attribution {
    width: 13rem;
    margin: 10rem auto 0 auto;
    text-align: center;
  }
}

```

## Conclusion

En tant que développeur web, les mises en page doivent être la première chose à laquelle vous pensez avant d'écrire du code. Heureusement, CSS Grid et Flexbox ont révolutionné la façon dont nous structurons et construisons les mises en page des sites web et des applications web. 

Cela rend ces concepts indispensables à connaître afin que vous puissiez spécifier l'arrangement des éléments sur le web. Nous avons discuté des fondamentaux, afin que vous puissiez facilement construire sur cette connaissance et créer de belles pages web et applications. 

Merci d'avoir lu 👋🏾. J'espère que vous avez trouvé cela utile.