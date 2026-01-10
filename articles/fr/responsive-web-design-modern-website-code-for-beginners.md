---
title: Conception Web Responsive – Code de Site Web Moderne pour Débutants
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-27T16:33:18.000Z'
originalURL: https://freecodecamp.org/news/responsive-web-design-modern-website-code-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/responsive-web-design.png
tags:
- name: Responsive Image
  slug: responsive-image
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Conception Web Responsive – Code de Site Web Moderne pour Débutants
seo_desc: "When the internet was still young, website visitors used desktop and then\
  \ laptop computers with wide screens to access websites. \nThen when smart phones\
  \ were developed, mobile phone users had to endlessly zoom and scroll to access\
  \ and view different ..."
---

Lorsque l'internet était encore jeune, les visiteurs des sites web utilisaient des ordinateurs de bureau puis des ordinateurs portables avec des écrans larges pour accéder aux sites web. 

Ensuite, lorsque les smartphones ont été développés, les utilisateurs de téléphones mobiles devaient zoomer et faire défiler sans fin pour accéder et voir différentes parties de ces mêmes sites web. 

Heureusement, ce n'est plus le cas de nos jours grâce à l'introduction révolutionnaire de la Conception Web Responsive.

Dans cet article, je vais vous guider à travers l'évolution de la Conception Web Responsive, les diverses intégrations qui l'ont rendue possible, et comment vous pouvez commencer à l'utiliser dans vos projets de codage pour une meilleure expérience utilisateur.

## Qu'est-ce que la Conception Web Responsive ?

La conception web responsive permet aux pages web de s'afficher correctement sur une grande variété de tailles d'écrans de dispositifs sans couper ou déformer le contenu. 

Cela ne signifie pas qu'un site web apparaîtra exactement de la même manière sur un téléphone que sur un ordinateur portable, par exemple. Plutôt, cela signifie que le contenu de la page web s'adapte à différentes tailles d'écrans – des grands écrans (ordinateurs de bureau et portables) aux écrans moyens (tablettes) aux écrans mobiles (téléphones de diverses tailles d'écrans). 

Et tout cela en conservant le même contenu (juste peut-être arrangé différemment pour s'adapter à chaque écran).

## L'Évolution de la Conception Web Responsive

Dans le passé, les gens utilisaient principalement des ordinateurs de bureau et des portables pour voir du contenu en ligne, car les sites web étaient optimisés pour ces écrans uniquement. 

Mais à mesure que de plus en plus de personnes ont commencé à utiliser des téléphones mobiles pour surfer sur le web, les gens ont commencé à se plaindre de l'affichage et des mises en page médiocres qu'ils voyaient. 

Cela signifiait une chose pour les concepteurs et développeurs web : les sites web devaient être optimisés pour le mobile, aussi ! 

Au cours de la dernière décennie, le nombre d'utilisateurs de sites web sur mobile a commencé à dépasser celui des ordinateurs de bureau et des portables pour la première fois. Ainsi, tout le monde, des géants de la technologie aux petites entreprises, a commencé à adopter une approche de conception web responsive.

Les développeurs et concepteurs ont également créé le tout nouveau design mobile-first. Cela signifiait que les développeurs créaient d'abord les sites web pour les dispositifs mobiles, et ensuite pour les ordinateurs de bureau. 

Cela signifiait souvent un site web séparé pour les dispositifs mobiles et les grands écrans, avec le même système de serveur mais des domaines différents. 

Le site web original, par exemple, pouvait être `examplewebsite.com`, et la version mobile serait `examplewebsite.mobi`, ou `m.examplewebsite.com`. 

Le dispositif de l'utilisateur était détecté par des scripts prêts à l'emploi et ensuite le domaine approprié était rendu. Cette pratique existe encore aujourd'hui.

Outre la méthode à deux domaines, les concepteurs et développeurs web peuvent créer un site web pour une taille d'écran particulière en premier (il peut s'agir d'un ordinateur de bureau, d'une tablette ou d'un mobile), puis ajouter ce que l'on appelle des media queries pour faire en sorte que le site web s'adapte à différentes tailles d'écrans. C'est l'approche mobile-first.

## Comment Rendre Votre Site Responsive 

Intégrer des approches de conception web responsive dans un projet inclut chaque partie du code – dans l'élément HTML `<head>`, la structure HTML, le CSS, et même le JavaScript. 
    
Je vais décrire ces processus aussi clairement et en autant de détails que possible.

### Définir le Viewport dans le Head

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Puisque HTML joue un rôle énorme dans la définition de la structure d'une page web, il a définitivement quelque chose à voir avec le fait de rendre les sites web réactifs (adaptés) à différentes tailles d'écrans.

Vous devrez inclure l'élément meta viewport vide dans la section head de toute page web que vous souhaitez optimiser pour différentes tailles d'écrans. 

Cela indique au navigateur de rendre la largeur de la page web à la largeur exacte du dispositif. Ainsi, si le dispositif a une largeur de 1200px, la largeur de la page web sera de 1200px. Si le dispositif a une largeur de 720px, la largeur de la page web sera de 720px, et ainsi de suite.

Cela évite les zooms avant et arrière ennuyeux que les utilisateurs de téléphones mobiles connaissaient dans le passé, ce qui n'était pas bon pour l'expérience utilisateur. 

Voici comment un site web apparaît sur les petits téléphones sans l'élément `<meta>` viewport : 

![without-meta-viewport](https://www.freecodecamp.org/news/content/images/2021/08/without-meta-viewport.gif)

Et voici comment le même site web avec l'élément `<meta>` viewport apparaît sur les petits téléphones :

![with-meta-viewport](https://www.freecodecamp.org/news/content/images/2021/08/with-meta-viewport.gif)

Si vous vous demandez quel est ce site web, il s'agit d'un modèle de site web portfolio gratuit que j'ai créé pour les débutants. Je le mettrai bientôt à la disposition de tous les lecteurs de freeCodeCamp – donc, restez à l'écoute. :)

Mais l'élément `<meta>` viewport n'est pas tout ce dont vous avez besoin pour faire en sorte qu'un site web s'adapte à différentes tailles d'écrans. Il y a plus.

### Les Media Queries CSS

L'outil le plus crucial que vous utiliserez pour rendre vos sites responsives est les Media Queries CSS3. Les media queries vous permettent d'écrire le même code CSS de différentes manières pour plusieurs écrans. 

Avec les media queries, vous indiquez au navigateur d'afficher le contenu d'une manière particulière sur un écran particulier.

La syntaxe de base d'une media query ressemble à ceci : 

```css
@media screen and (max-width: 720px) {
  /*Les codes CSS vont ici*/
}
```

Cela indique au navigateur d'exécuter le code CSS écrit dans la media query lorsque la largeur de l'écran est inférieure à un point d'arrêt de 720 pixels. Le point d'arrêt peut généralement être n'importe quelle valeur entre 1200 pixels et 320 pixels. 

Dans les extraits de code ci-dessous, j'instruis le navigateur de changer la `background-color` en gris foncé, et la `color` en bleu lorsque la largeur de l'écran est inférieure à 768 pixels.

```html
<body>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam
      mollitia, consequuntur aliquid nobis vitae soluta maiores expedita ipsam
      delectus molestiae!
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur
      architecto temporibus sed officiis vero, quisquam, corrupti quis veritatis
      dolor amet nostrum quam! Voluptates nam architecto enim neque nemo
      consectetur molestias unde fugit dolorum alias temporibus expedita
      doloribus deserunt laborum asperiores illum saepe, voluptate rerum quia
      sit facilis consequuntur perferendis aperiam. Nobis reiciendis debitis
      consequuntur placeat maiores voluptas, quos esse eum.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Minus fugiat,
      nemo rem facere cumque error. Aliquam consequatur nobis cupiditate atque!
      Fugiat amet facere magni, nulla pariatur ut ullam, vel est eum voluptatum
      dicta quis dignissimos labore repellendus. Maiores deserunt quas tempore
      impedit, corporis quae amet blanditiis voluptatum laudantium magni ipsa!
    </p>
</body>
```

```css
 @media screen and (max-width: 768px) {
        body {
          background-color: #333;
          color: #3498db;
        }
     }
```

![media-queries](https://www.freecodecamp.org/news/content/images/2021/08/media-queries.gif)

Plusieurs autres points d'arrêt existent pour différents dispositifs. 

- 320 - 480px pour les petits téléphones tels que l'iPhone 6, 7, et 5 

- 478 - 768px pour les tablettes et iPads

- 1025 - 1200px pour les ordinateurs de bureau et les grands écrans

Certains écrans extra-larges et téléviseurs peuvent prendre plus de 1200px.

### Texte Responsive

Puisque la taille du texte ne sera pas la même sur un téléphone mobile que sur un ordinateur de bureau, le texte doit être mis à l'échelle lorsque la largeur de l'écran du dispositif diminue.

Vous pouvez faire cela dans la media query pour chaque écran. Et l'une des façons de le rendre plus facile est d'utiliser des unités relatives (%, rem, et em) au lieu d'une unité absolue telle que px. 

Dans les extraits de code HTML et CSS ci-dessous, j'instruis le navigateur de faire en sorte que la taille de la police du texte soit de 3rem sur les grands écrans, et de 1.5rem sur les écrans dont la largeur est inférieure à 768 pixels :

```html
<p>
   Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam
   mollitia, consequuntur aliquid nobis vitae soluta maiores expedita ipsam
   delectus molestiae!
</p>

<p>
   Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur
   architecto temporibus sed officiis vero, quisquam, corrupti quis veritatis
   dolor amet nostrum quam! Voluptates nam architecto enim neque nemo
   consectetur molestias unde fugit dolorum alias temporibus expedita
   doloribus deserunt laborum asperiores illum saepe, voluptate rerum quia
   sit facilis consequuntur perferendis aperiam. Nobis reiciendis debitis
   consequuntur placeat maiores voluptas, quos esse eum.
</p>

<p>
   Lorem ipsum dolor sit amet consectetur, adipisicing elit. Minus fugiat,
   nemo rem facere cumque error. Aliquam consequatur nobis cupiditate atque!
   Fugiat amet facere magni, nulla pariatur ut ullam, vel est eum voluptatum
   dicta quis dignissimos labore repellendus. Maiores deserunt quas tempore
   impedit, corporis quae amet blanditiis voluptatum laudantium magni ipsa!
</p>
```

```css
@media screen and (max-width: 768px) {
        p {
          font-size: 1.5rem;
        }
      }
```

![responsive-text](https://www.freecodecamp.org/news/content/images/2021/08/responsive-text.gif)

### Images Responsive

Tout comme le texte, les images doivent également être mises à l'échelle lorsque la largeur de l'écran diminue. 

Les images ont une largeur et une hauteur fixes, donc lorsqu'elles sont plus grandes que la largeur du viewport (largeur de l'écran), un utilisateur doit généralement faire défiler pour voir le tout, ce qui crée une mauvaise expérience utilisateur. 

Les développeurs contournent ce problème en définissant une largeur maximale de 100 % pour toutes les images et en les affichant comme des éléments de niveau bloc (les images sont des éléments en ligne par défaut). 

Vous pouvez définir cela pour les images dans votre code individuellement, mais pour favoriser les principes DRY (Do not repeat yourself), vous devriez le faire dans vos réinitialisations pour toutes les images.

```css
 img {
        display: block;
        max-width: 100%;
      }
```

Une autre façon de rendre les images responsives est d'utiliser l'élément picture en HTML. Avec cet élément, vous pouvez indiquer au navigateur d'afficher différentes images qui correspondent à la largeur sur différents dispositifs.

```html
<picture>
      <source
        media="(max-width: 1100px)"
        srcset="freecodecamp-large-logo.jpg"
      />
      <source
        media="(max-width: 900px)"
        srcset="freecodecamp-medium-logo.jpg"
      />
      <source media="(max-width: 760px)" srcset="freecodecamp-small-logo.jpg" />
      <img
        src="freecodecamp-large-logo.jpg"
        alt="freeCodeCamp"
        style="max-width: 100%"
      />
</picture>
```

- Sur un écran de taille 1100px de largeur et en dessous, freecodecamp-large-logo sera affiché
- Sur un écran de taille 900px de largeur et en dessous, freecodecamp-medium-logo sera affiché
- Sur un écran de taille 760px de largeur et en dessous, freecodecamp-small-logo sera affiché 

Si la largeur de l'écran ne remplit aucune des conditions, freecodecamp-large-logo sera affiché. 

![responsive-image](https://www.freecodecamp.org/news/content/images/2021/08/responsive-image.gif)

### Mise en Page Responsive

La mise en page de toute page web détermine comment le contenu est affiché dans le navigateur. 

Dans le passé, les développeurs devaient utiliser des tableaux, qui n'étaient pas faciles à contrôler. Ensuite sont venus `float` et `clearfix`, qui étaient également difficiles à gérer.

L'introduction de CSS Grid et Flexbox a révolutionné les mises en page et a donné plus de pertinence à la conception responsive.

#### Flexbox

Avec CSS flexbox, la conception responsive a gagné plus de pertinence car, avec lui, vous n'avez pas à ajouter trop de media queries contrairement à lorsque vous utilisez des floats pour une mise en page. 

Dès qu'un affichage flex est assigné à l'élément conteneur, la direction de l'élément est rendue sur la ligne par défaut. 

Vous pouvez ensuite utiliser une media query pour définir la direction en colonne pour les petits écrans avec la propriété flex-direction. La valeur de la propriété flex-direction doit être explicitement définie en colonne.

Vous pouvez également disposer la manière dont vous voulez que le contenu de la page web soit rendu avec des propriétés telles que flex-grow et flex-shrink. Ces deux propriétés font en sorte que l'élément qu'elles contiennent grandit à mesure que la largeur du viewport (largeur) de l'écran augmente et rétrécit à mesure que le viewport diminue. N'est-ce pas génial ? 

Dans les extraits de code ci-dessous, la direction des différents morceaux de texte dans leurs conteneurs respectifs sera une ligne sur les écrans dont la largeur est supérieure à 768 pixels, et une colonne lorsque la largeur est inférieure à 768 pixels. 

J'ai pu le faire en affichant tous les éléments à l'intérieur de l'élément body comme flex.

```html
<body>
    <div class="container-one">
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam
            mollitia, consequuntur aliquid nobis vitae soluta maiores expedita ipsam
            delectus molestiae!
        </p>
    </div>
      
    <div class="container-two">
        <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur
        architecto temporibus sed officiis vero, quisquam, corrupti quis veritatis
        dolor amet nostrum quam! Voluptates nam architecto enim neque nemo
        consectetur molestias unde fugit dolorum alias temporibus expedita
        doloribus deserunt laborum asperiores illum saepe, voluptate rerum quia
        sit facilis consequuntur perferendis aperiam. Nobis reiciendis debitis
        consequuntur placeat maiores voluptas, quos esse eum.
        </p>
    </div>

    <div class="container-three">
        <p>
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Minus fugiat,
        nemo rem facere cumque error. Aliquam consequatur nobis cupiditate atque!
        Fugiat amet facere magni, nulla pariatur ut ullam, vel est eum voluptatum
        dicta quis dignissimos labore repellendus. Maiores deserunt quas tempore
        impedit, corporis quae amet blanditiis voluptatum laudantium magni ipsa!
        </p>
    </div> 
</body>
```

```css
body {
          display: flex;
      }

      div {
          border: 2px solid #2ecc71;
          margin-left: 6px;
      }

      @media screen and (max-width: 768px) {
        body {
          flex-direction: column;
        }
    }
```

![flexbox](https://www.freecodecamp.org/news/content/images/2021/08/flexbox.gif)

#### CSS Grid

CSS grid est plus ou moins une forme hybride et plus puissante de flexbox. Beaucoup ont soutenu que tout ce que vous faites avec Flexbox, vous pouvez le faire en moins de lignes de code avec Grid.

Avec CSS grid, vous pouvez créer des grilles flexibles de manière plus directe car vous pouvez définir les colonnes et les lignes que vous voulez avec la propriété grid-auto-flow définie sur colonne ou ligne.

Vous pouvez faire la même chose que nous avons faite dans l'exemple Flexbox de cette manière avec Grid : 

```css
body {
          display: grid;
          grid-auto-flow: column;
          gap: 6px;
      }

      div {
          border: 2px solid #2ecc71;
          margin-left: 6px;
      }

      @media screen and (max-width: 768px) {
        body {
            grid-auto-flow: row;
        } 
     }
```

![grid-1](https://www.freecodecamp.org/news/content/images/2021/08/grid-1.gif)

Vous pouvez en apprendre plus sur Flexbox et Grid dans le programme CSS de freeCodeCamp.

## Conclusion

Alors que les utilisateurs d'internet accèdent désormais aux sites web sur des téléphones mobiles plus que sur des ordinateurs de bureau et des portables, la conception responsive est la voie à suivre lorsqu'il s'agit de créer des sites web modernes.

Connaître les meilleures pratiques de la Conception Responsive vous distinguera des autres développeurs, car vous serez en mesure de créer des sites web qui s'adaptent à différentes tailles d'écrans au sein des mêmes fichiers HTML, CSS et JavaScript. 

J'espère que cet article vous a donné les informations dont vous avez besoin pour créer des sites web responsives dans le monde réel.

Merci d'avoir lu, et continuez à coder.