---
title: Développement Web pour Débutants – Apprenez les bases du HTML et du CSS pour
  construire votre première page web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-14T17:13:14.000Z'
originalURL: https://freecodecamp.org/news/web-development-for-beginners-basic-html-and-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/halgatewood-com-tZc3vjPCk-Q-unsplash--1-.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Développement Web pour Débutants – Apprenez les bases du HTML et du CSS
  pour construire votre première page web
seo_desc: 'By Vasyl Lagutin

  Have you ever wondered how websites are built and designed? Do you want to learn
  the art of web development but you''re not that tech savvy – yet?

  Well, then this tutorial is for you. It''s an introduction to Web Development for
  beginn...'
---

Par Vasyl Lagutin

Vous êtes-vous déjà demandé comment les sites web sont construits et conçus ? Voulez-vous apprendre l'art du développement web mais vous n'êtes pas encore très calé en technologie ?

Eh bien, ce tutoriel est fait pour vous. C'est une introduction au développement web pour les débutants afin que vous puissiez apprendre les bases même si vous êtes totalement novice en la matière.

# **Les bases du HTML – la structure d'une page web**

HTML signifie Hyper-Text Markup Language. Avant d'approfondir le fonctionnement du HTML, essayons de comprendre ce que signifie réellement `Hyper-Text Markup Language`.

`Hyper-Text` (Hypertexte) fait référence aux hyperliens que vous voyez sur un texte, une image ou un marque-page qui redirige vers une autre page, un fichier, un document ou une autre partie d'une page web.

Un langage de balisage (markup language) est simplement un langage informatique qui contient des balises (tags) définissant des éléments au sein d'un document. Un exemple de balise pourrait être le titre d'un blog, qui est normalement écrit avec une balise `h`.

Il existe de nombreuses autres balises, dont certaines que nous découvrirons plus tard.

Vous pouvez simplement considérer le HTML comme la structure d'une page web. Par exemple, supposons que vous deviez construire une maison. La première étape de la construction devrait être d'édifier sa charpente et sa structure globale, n'est-ce pas ?

Vous allez prévoir le sous-sol, les murs, la pelouse, le garage, et ainsi de suite. C'est ainsi que vous pouvez imaginer le HTML – ce sont les blocs de construction d'une page web.

Sur un site web, cela peut être la barre de navigation (navbar), le corps principal/contenu, le pied de page (footer), la barre latérale (sidebar) et toutes les divisions structurelles de la page. Tout cela est basé sur le HTML.

## Comment débuter avec le HTML

Il existe de nombreux éditeurs de code, comme VS Code, Sublime Text 3, Atom et Brackets. Tout cela peut vous sembler étrange. Nous allons donc commencer par utiliser `Notepad` (le Bloc-notes), que vous utilisez peut-être déjà d'une manière ou d'une autre pour prendre des notes.

Voyons comment vous créeriez la structure d'une page web simple en HTML avec un code de base.

Nous allons concevoir une page web comportant plusieurs sections : une barre de navigation (navbar), le corps principal avec un titre, un paragraphe et une image, et un pied de page (footer).

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Titre de la page</title>
    </head>
    <body>

        <nav>Ceci est la barre de navigation (Navbar) de ma page web</nav>

        <h1>Mon premier titre</h1>
        <p>Mon premier paragraphe.</p>

        <img src = "https://miro.medium.com/max/1584/1*lJ32Bl-lHWmNMUSiSq17gQ.png"/>

        <footer>
          <p>Pied de page (Footer)</p>
        </footer>

    </body>
</html>
```

Dans le code ci-dessus, la déclaration `<!DOCTYPE html>` signifie que ce document est un fichier HTML5.

Le `5` ici fait simplement référence à la version, car le HTML a parcouru un long chemin et s'est amélioré par rapport à ses versions précédentes. La version `5` désigne sa version la plus récente et stable. Vous n'avez pas besoin de vous soucier des versions précédentes ici.

`<html>` agit comme l'élément racine de tous les éléments (titre, en-têtes, paragraphes, etc.) d'une page web HTML.

`<head>` contient les méta-informations (informations sur les informations telles que l'auteur, la date d'expiration, une liste de mots-clés, l'auteur du document) de la page.

Le `<title>` fait référence au titre de la page web que vous voyez dans le navigateur lorsque vous ouvrez une page web. Voici un exemple pour votre référence. Dans cette image, `Page Title` est l'élément qui fait référence à la balise title.

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/Screenshot_(1313).png](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot_-1313-.png)

`<body>` est l'endroit où se trouve tout le contenu de votre page web, comme le titre, les paragraphes, les images, toute l'interface utilisateur.

`<nav>` représente la barre de navigation, qui doit se trouver en haut, suivie du contenu du corps principal, puis enfin du `<footer>`.

Le corps principal est composé d'un titre représenté par une balise `<h1>` (le `1` avec le `h` représente la taille du titre. La taille du titre va de 1 à 6, 1 étant le plus grand et 6 le plus petit). Il est suivi d'une balise de paragraphe `<p>`, puis d'une balise d'image `<img>`, et enfin du pied de page, la dernière section d'une page web.

Notez que la balise image contient le mot-clé `src`. `src` fait référence à la source de l'image, qui dans ce cas est une image prise sur le web. C'est pourquoi nous avons joint le lien URL de l'image.

Toutes ces balises commencent par des chevrons d'ouverture `<>` et se terminent par des chevrons `</>`, comme vous pouvez le voir dans les extraits de code.

Vous pouvez obtenir plus de détails sur la [structure d'un document HTML ici](https://learn.coderslang.com/0041-html-document-structure/).

## Comment enregistrer des fichiers HTML et afficher les résultats

Il vous suffit de suivre ces deux étapes de base pour visualiser votre page web HTML.

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/Screenshot_(1319).png](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot_-1319-.png)

1. Enregistrez votre fichier HTML avec l'extension `.html`. Dans l'exemple que nous avons utilisé, nous avons enregistré le fichier sous le nom `Tutorial.html`.

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/Screenshot_(1322).png](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot_-1322-.png)

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/Screenshot_(1321).png](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot_-1321-.png)

2. Ouvrez le fichier dans n'importe quel navigateur (Chrome, Firefox, IE), et vous pourrez alors visualiser votre page web HTML.

## **Résultats de notre mise en page HTML de base**

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/_C__Users_wel_Desktop_Tutorial.html_(2).png](https://www.freecodecamp.org/news/content/images/2021/05/_C__Users_wel_Desktop_Tutorial.html_-2-.png)

Vous pouvez clairement voir les résultats, bien qu'il n'y ait pas encore de couleurs ou de style. Mais vous pouvez toujours voir que la structure est là – la barre de navigation suivie du corps principal contenant le contenu, suivi d'un pied de page en bas.

# Comment ajouter des couleurs, du style et de la puissance au HTML avec CSS

CSS signifie Cascading Style Sheets (Feuilles de style en cascade), qui sont les fichiers de feuilles de conception qui ajoutent des couleurs, du style et de la puissance à vos éléments structurels HTML.

Vous pouvez considérer le CSS comme la peinture, la décoration et les éléments de design que vous ajoutez pour rendre votre maison magnifique.

Il existe plusieurs façons d'ajouter du CSS à votre structure HTML. Explorons la technique la plus simple qui consiste à ajouter du CSS via la balise `<style>`.

```html
<head>
	<title>Titre de la page</title>
    
    <style>

    body {
      background-color: lightblue;
      margin: 0;
      text-align: center;
    }

    nav {
     background-color: black;
     width: 100%;
     color: white;
     height: 50px;
     padding-top: 25px;
    }

    h1 {
     color: black;
    }

    footer {
     background-color: gray;
     color: white;
     padding: 5px;
    }

    </style>
</head>
```

## **Explication du CSS**

Vous pouvez voir que nous avons ajouté le CSS via la balise style à l'intérieur de la balise head du document dans le code ci-dessus. C'est une façon simple d'ajouter du CSS.

Décomposons cela et explorons les propriétés CSS que nous avons utilisées dans les quatre éléments individuels ci-dessus.

### L'élément body

```css
body {
  background-color: lightblue;
  margin: 0;
  text-align: center;
}
```

Le sélecteur CSS body fait référence à toute la structure de l'interface utilisateur que nous voyons. Nous avons ajouté quelques propriétés de style CSS :

* `background-color` qui ajoute la couleur d'arrière-plan – bleu clair ici
* `margin` qui gère les espaces de chaque côté de la structure de la page web
* `text-align center` ce qui signifie que tout le contenu sera aligné au centre dans ce cas.

Comme tout ce CSS s'applique à l'ensemble de la page web, tous les éléments internes observeront automatiquement ces propriétés CSS jusqu'à ce que leurs propres propriétés soient spécifiées et diffèrent de cette propriété globale.

### L'élément nav

```css
nav {
 background-color: black;
 width: 100%;
 color: white;
 height: 50px;
 padding-top: 25px;
}
```

Le sélecteur nav fait référence à la barre de navigation de la page web et lui applique des propriétés de design.

Nous avons défini sa couleur d'arrière-plan sur noir, sa largeur sur `100%` pour qu'elle occupe toute la largeur, sa couleur qui représente la couleur du texte ou des liens au sein de la barre de navigation, sa `height` (hauteur) sur `50px`, et nous lui avons donné un `padding-top` (marge intérieure supérieure) de `25px`.

Le `Padding` fait référence à l'espace entre le contenu et la bordure. Comme nous voulions que le texte soit centré verticalement, nous avons dû ajouter un padding de la moitié des pixels de la hauteur réelle de la barre de navigation, soit `50px (hauteur de la barre de navigation) / 2 = 25px`. Cela garantira que le texte à l'intérieur de la barre de navigation est aligné au centre.

### L'élément h1

```css
h1 {
 color: black;
}
```

Le sélecteur `h1` applique du CSS à la balise `h1`. Ici, nous avons appliqué la propriété `color` pour qu'elle soit `black` (noir).

### L'élément footer

```css
footer {
 background-color: gray;
 color: white;
 padding: 5px;
}
```

C'est le dernier sélecteur faisant référence au pied de page de notre page web. Ici, nous avons défini un ensemble de propriétés similaires à celles dont nous avons discuté précédemment pour la `navbar`, il n'y a donc rien de vraiment nouveau ici.

Et voilà !

# **À quoi ressemble la page web **après** avoir ajouté du CSS**

![Understanding%20Web%20design%20Basics%20with%20HTML%20&%20CSS%20f00187c06fae4c0582422f7947326b9b/_C__Users_wel_Desktop_Tutorial.html_(1).png](https://www.freecodecamp.org/news/content/images/2021/05/_C__Users_wel_Desktop_Tutorial.html_-1-.png)

Vous pouvez maintenant voir à quel point le CSS ajoute de la vie et de la puissance à notre structure HTML de base. N'est-ce pas incroyable ?

Ce ne sont que les bases du design web, mais c'est en fait assez amusant une fois qu'on les a apprises.

# **Conclusion**

Maintenant, vous avez appris les bases de la conception de sites web et vous pouvez voir à quel point cela peut être accessible, pratique, et comment cela se rapporte à de nombreux concepts de la vie réelle tels que la construction d'une maison.

Donc, si vous avez trouvé cela intéressant, vous devriez absolument explorer davantage le monde du design web. Vous pourriez commencer par en apprendre plus sur les [couleurs HTML](https://learn.coderslang.com/0028-html-colors-with-names-hex-and-rgb-codes/) et comment les utiliser.

Si vous souhaitez approfondir le développement web moderne, jetez un œil à mon [cours Full-Stack JavaScript](https://js.coderslang.com).