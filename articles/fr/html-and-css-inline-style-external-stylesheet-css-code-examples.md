---
title: HTML et CSS – Style en ligne, feuille de style externe, exemples de code CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-12T18:47:27.000Z'
originalURL: https://freecodecamp.org/news/html-and-css-inline-style-external-stylesheet-css-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Htmlcss.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: HTML et CSS – Style en ligne, feuille de style externe, exemples de code
  CSS
seo_desc: 'When you''re learning about web development, you probably hear about HTML
  and CSS pretty quickly. Well, what are these tools and how do you use them?

  You can think of HTML as the structure and framing of a house. And when you want
  to make that structu...'
---

Lorsque vous apprenez le développement web, vous entendez probablement parler de HTML et CSS assez rapidement. Mais quels sont ces outils et comment les utiliser ?

Vous pouvez considérer le HTML comme la structure et l'ossature d'une maison. Et lorsque vous voulez rendre cette structure attrayante, vous ajoutez de la peinture, de la décoration et d'autres éléments. Cette décoration, c'est le CSS.

## Comment styliser le code HTML ?

HTML signifie HyperText Markup Language. C'est un document basé sur du texte conçu pour être affiché dans un navigateur. Pour rendre les textes et autres éléments intégrés contenus dans le HTML attrayants, vous devez ajouter du CSS, ou Cascading Style Sheets.

Il existe 3 façons différentes de styliser votre HTML : 
* les styles en ligne, 
* les styles internes (également connus sous le nom de CSS intégré), et 
* les feuilles de style externes. 

Dans ce tutoriel, nous explorerons ces trois méthodes de stylisation en profondeur. Nous examinerons également leurs avantages et inconvénients afin que vous puissiez commencer à les utiliser dans vos projets de codage et choisir celle qui vous convient le mieux.

## Modèle HTML

Pour faciliter les choses dans ce tutoriel, j'ai préparé un modèle HTML simple que nous allons styliser :

```html
<article>
    <p class="paragraph-one">
      freeCodeCamp est l'une des meilleures plateformes pour apprendre à coder
    </p>
    <p class="paragraph-two">
      Apprendre à coder est gratuit sur freeCodeCamp, c'est pourquoi ils l'appellent
      freeCodeCamp
    </p>
    <p class="paragraph-three">
      freeCodeCamp génère de l'argent grâce aux dons afin de payer les employés
      et de maintenir les serveurs.
    </p>
    <p id="paragraph-four">
      Si vous êtes suffisamment généreux, envisagez de rejoindre ceux qui ont
      fait des dons à freeCodeCamp
    </p>
    <p class="paragraph-five">
      Chez freeCodeCamp, il ne s'agit pas seulement de taper sur un éditeur de code,
      il y a un forum comme StackOverflow, où vous pouvez poser des questions sur
      vos problèmes de codage et obtenir des réponses de la part des autres membres.
    </p>
</article>
```

![initialPageView](https://www.freecodecamp.org/news/content/images/2021/08/initialPageView.png)

## Styles en ligne en HTML

Lorsque vous utilisez des styles en ligne, vous les ajoutez directement aux balises HTML avec l'attribut style.

Par exemple, dans notre code HTML, nous pouvons attribuer une couleur à l'un des paragraphes en écrivant le CSS directement dans la balise d'ouverture.

Il est également typique de supprimer le soulignement et la couleur par défaut attribués aux liens, nous pouvons donc le faire dans la balise d'ouverture `<a>`.

```html
<article>
   <p
     class="paragraph-one"
     style="color: darkmagenta; font-size: 2rem; text-align: center"
   >
     <a href="freecodecamp.org" style="text-decoration: none; color: crimson"
       >freeCodeCamp</a
     >
     est l'une des meilleures plateformes pour apprendre à coder
   </p>
   <p class="paragraph-two">
     Apprendre à coder est gratuit sur freeCodeCamp, c'est pourquoi ils l'appellent
     freeCodeCamp
   </p>
   <p class="paragraph-three">
     freeCodeCamp génère de l'argent grâce aux dons afin de payer les employés
     et de maintenir les serveurs.
   </p>
   <p id="paragraph-four">
     Si vous êtes suffisamment généreux, envisagez de rejoindre ceux qui ont
     fait des dons à freeCodeCamp
   </p>
   <p class="paragraph-five">
     Chez freeCodeCamp, il ne s'agit pas seulement de taper sur un éditeur de code,
     il y a un forum comme StackOverflow, où vous pouvez poser des questions sur
     vos problèmes de codage et obtenir des réponses de la part des autres membres.
   </p>
 </article>
```

Pouvez-vous voir que le premier paragraphe est maintenant moins lisible ? C'est l'un des inconvénients de l'utilisation des styles en ligne, que nous verrons ci-dessous.

Notre page web ressemble maintenant à la capture d'écran ci-dessous :

![inlineStyling](https://www.freecodecamp.org/news/content/images/2021/08/inlineStyling.png)

### Avantages des styles en ligne

- Bon pour les corrections rapides.
- Prend la spécificité la plus élevée, donc il remplace tout style défini avec un style en ligne ou des feuilles de style externes.
- Vous n'avez pas besoin de changer de fichier ou de faire défiler jusqu'à la section head pour modifier le CSS
- Les navigateurs téléchargent toujours les fichiers HTML, CSS et JavaScript avant d'afficher une page web, donc avec le CSS en ligne, il y a moins de fichiers à télécharger.

### Inconvénients des styles en ligne

- Rend le HTML désordonné, plus difficile à maintenir et moins lisible.
- Ne peut pas être réutilisé dans plusieurs fichiers HTML
- Vous pouvez finir par remplacer les styles internes ou les feuilles de style externes
- Vous avez des options de stylisation limitées


## Styles internes en HTML

Lorsque vous utilisez le style interne, vous intégrez les styles directement dans le fichier HTML à l'intérieur de la balise style. Vous les placez généralement dans le head, mais cela fonctionne partout, même en dehors des balises HTML d'ouverture et de fermeture (mais ne faites pas cela car c'est une mauvaise pratique).

Nous pouvons appliquer quelques styles internes à notre code HTML comme ceci :

```html
<style>
   * {
     padding: 0;
     margin: 0;
     box-sizing: border-box;
 }
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
   }

 .paragraph-two {
     font-size: 1.5rem;
      }

 .paragraph-one a {
      text-decoration: none;
      color: crimson;
      font-size: 2rem;
      font-weight: bolder;
     }
 </style>
</head>
 <body>
 <article>
   <p class="paragraph-one">
     <a href="freecodecamp.org">freeCodeCamp</a>
     est l'une des meilleures plateformes pour apprendre à coder
   </p>
   <p class="paragraph-two">
     Apprendre à coder est gratuit sur freeCodeCamp, c'est pourquoi ils l'appellent
     freeCodeCamp
   </p>
   <p class="paragraph-three">
     freeCodeCamp génère de l'argent grâce aux dons afin de payer les employés
     et de maintenir les serveurs.
  </p>
   <p id="paragraph-four">
     Si vous êtes suffisamment généreux, envisagez de rejoindre ceux qui ont
     fait des dons à freeCodeCamp
   </p>
   <p class="paragraph-five">
     Chez freeCodeCamp, il ne s'agit pas seulement de taper sur un éditeur de code,
     il y a un forum comme StackOverflow, où vous pouvez poser des questions sur
     vos problèmes de codage et obtenir des réponses de la part des autres membres.
   </p>
 </article>
```

Vous pouvez voir que nous avons maintenant plus d'options de stylisation lorsque nous utilisons des styles internes.

### Avantages des styles internes

- Réduit le nombre de fichiers que les navigateurs doivent télécharger
- Pas besoin de changer de fichier pour modifier le CSS
- Plus d'options de stylisation car vous pouvez utiliser des combinateurs, des sélecteurs de classe et des sélecteurs d'ID

Si vous vous demandez ce que sont les combinateurs, ce sont les symboles utilisés pour connecter différents sélecteurs. Un exemple est un espace (` `) pour sélectionner le descendant suivant d'un élément, comme un paragraphe (`p`) qui vient après un `div`.

Les sélecteurs de classe sont désignés par un point (`.`), et les sélecteurs d'ID sont désignés par un `#`.

### Inconvénients des styles internes

- Ils ne peuvent pas être réutilisés dans plusieurs fichiers HTML. Pour ajouter le même style à un autre fichier HTML, vous devez l'inclure dans le head à nouveau
- Cela augmente la taille du fichier HTML, ce qui peut entraîner des vitesses de chargement plus lentes.

Notre page web ressemble maintenant à ceci :
![internalStyling](https://www.freecodecamp.org/news/content/images/2021/08/internalStyling.png)

## Feuilles de style externes en HTML

Cela est considéré comme la meilleure façon de styliser votre code HTML. Les feuilles de style externes sont totalement séparées du HTML et vous les placez dans un fichier CSS (avec l'extension `.css`).

Pour utiliser des feuilles de style externes dans votre HTML, vous les liez dans le head avec la balise link.

La syntaxe de base de la balise link ressemble à ceci :

```html
<link rel="stylesheet" href="path-to-css-file">
```

Pour styliser notre code HTML, nous devons créer un fichier CSS et le lier. Une fois lié, notre fichier HTML complet ressemble maintenant à ceci :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Comment styliser HTML</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <article>
      <p class="paragraph-one">
        <a href="freecodecamp.org">freeCodeCamp</a>
        est l'une des meilleures plateformes pour apprendre à coder
      </p>
      <p class="paragraph-two">
        Apprendre à coder est gratuit sur freeCodeCamp, c'est pourquoi ils l'appellent
        freeCodeCamp
      </p>
      <p class="paragraph-three">
        freeCodeCamp génère de l'argent grâce aux dons afin de payer les employés
        et de maintenir les serveurs.
      </p>
      <p id="paragraph-four">
        Si vous êtes suffisamment généreux, envisagez de rejoindre ceux qui ont
        fait des dons à freeCodeCamp
      </p>
      <p class="paragraph-five">
        Chez freeCodeCamp, il ne s'agit pas seulement de taper sur un éditeur de code,
        il y a un forum comme StackOverflow, où vous pouvez poser des questions sur
        vos problèmes de codage et obtenir des réponses de la part des autres membres.
      </p>
    </article> 
</body>
</html>
```

Vous vous demandez peut-être pourquoi le chemin vers le fichier CSS est simplement `style.css`, qui est également le nom du fichier. C'est parce que les fichiers HTML et CSS sont dans le même répertoire. Si vous avez la feuille de style dans un autre dossier, vous devez inclure le nom du dossier avant le nom du fichier.

Appliquons quelques styles à notre HTML dans notre feuille de style externe :

![externalStyling](https://www.freecodecamp.org/news/content/images/2021/08/externalStyling.png)

### Avantages des feuilles de style externes

- Rend les styles réutilisables dans plusieurs fichiers HTML
- Plus facile à maintenir
- Il est mis en cache par le navigateur lors du chargement initial, ce qui facilite et accélère le rendu des pages après les chargements de pages suivants
- Il peut être hébergé sur un CDN, ce qui minimise la bande passante et peut être facilement transporté dans diverses régions du monde.

### Inconvénients des feuilles de style externes

- Cela augmente le nombre de fichiers que le navigateur doit télécharger
- Le navigateur doit faire des requêtes HTTP supplémentaires par fichier

## Conclusion

J'espère que ce tutoriel vous a aidé à apprendre les différentes façons de styliser votre HTML.

Et maintenant, vous connaissez également les avantages et les inconvénients de chaque méthode, afin de pouvoir choisir celle qui vous convient le mieux.

Merci d'avoir lu, et continuez à coder.