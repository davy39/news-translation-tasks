---
title: HTML pour débutants
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-05T14:19:09.000Z'
originalURL: https://freecodecamp.org/news/html-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/ht-ml.jpeg
tags:
- name: HTML
  slug: html
- name: youtube
  slug: youtube
seo_title: HTML pour débutants
seo_desc: "HTML is used to create web pages. \nThis article will teach you the basics\
  \ of HTML. I also created a 45-minute video course on the freeCodeCamp.org YouTube\
  \ channel that teaches you HTML in the context of creating an actual web page.\n\
  If you are just le..."
---

HTML est utilisé pour créer des pages web. 

Cet article vous enseignera les bases de HTML. J'ai également créé un cours vidéo de 45 minutes sur la chaîne YouTube de freeCodeCamp.org (https://youtu.be/916GWv2Qs08) qui vous enseigne HTML dans le contexte de la création d'une page web réelle.

Si vous apprenez HTML, je recommande de lire cet article et de regarder le cours vidéo.

HTML signifie Hyper Text Markup Language. Chaque site web sur internet utilise HTML & CSS. La plupart utilisent également JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-187.png)
_HTML partout !_

Dans un site web, HTML est la structure, CSS est le style, et JavaScript est la fonctionnalité.

Voici un excellent diagramme interactif de [codeanalagies.com](https://blog.codeanalogies.com/2018/05/09/the-relationship-between-html-css-and-javascript-explained/). Déplacez le curseur d'avant en arrière.

<iframe src="https://blog.codeanalogies.com/wp-admin/admin-ajax.php?action=h5p_embed&id=1" width="726" height="478" frameborder="0" allowfullscreen="allowfullscreen" title="House to Page Structure- HTML, CSS, JS"></iframe><script src="https://blog.codeanalogies.com/wp-content/plugins/h5p/h5p-php-library/js/h5p-resizer.js" charset="UTF-8"></script>

Vous pouvez voir le HTML qui compose un élément d'une page web en cliquant droit sur un élément et en sélectionnant "Inspecter".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-190.png)

## Structure HTML

Voici le HTML qui compose une page web très basique :

```html
<!DOCTYPE html>
<html>
<head>
  <title>Mon premier site web !</title>
</head>
<body>
  <p>Ceci est un site web incroyable !</p>
  <img src="cat-picture.jpg" alt="Internet est alimenté par des images de chats.">
</body>
</html>
```

Décomposons les choses encore plus.

### Éléments

HTML est composé d'éléments HTML. Un élément est un composant individuel de HTML.

Voici un élément HTML du code ci-dessus :

```html
<p>Ceci est un site web incroyable !</p>
```

### Balises

Les balises HTML marquent le début et la fin d'un élément (et sont considérées comme faisant partie de l'élément). Les balises sont des conteneurs. Elles vous disent quelque chose sur le contenu entre les balises d'ouverture et de fermeture.

Dans l'élément ci-dessus, les balises sont `<p>` (balise d'ouverture) et `</p>` (balise de fermeture). Vous remarquerez que la balise de fermeture a un `/`. Cette balise particulière est une balise de paragraphe. Elle spécifie un paragraphe dans le document HTML. Les mots entre les balises d'ouverture et de fermeture sont un paragraphe.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/html-tag-attributes.png)
_Anatomie d'une balise HTML. Source : [clearlydecoded.com](https://clearlydecoded.com/anatomy-of-html-tag)_

### Types d'éléments

Les éléments peuvent être soit des éléments conteneurs (ils contiennent du contenu) soit des éléments autonomes, parfois appelés éléments auto-fermants.

Les éléments de paragraphe sont des conteneurs : `<p>Salut, je contiens du contenu</p>`

Les éléments d'image sont autonomes : `<img src="beau.jpg" />`

Remarquez dans l'élément autonome `img`, il n'y a pas de balise de fermeture mais il y a un `/` avant le crochet angulaire final.

### Attributs

Les attributs fournissent des informations supplémentaires sur les éléments HTML. Les attributs incluent `class`, `id`, `style`, `lang`, et `src` (source).

Voici un exemple d'un élément HTML avec l'attribut `id` :

```
<p id="info">Ceci est un site web incroyable !</p>
```

Quelques points à noter sur les attributs :

* Les attributs sont positionnés à l'intérieur de la balise d'ouverture, avant le crochet droit.
* Les attributs sont associés à des valeurs (dans cet exemple, la valeur est `info`).
* Les paires clé/valeur sont un concept important en programmation.
* Les attributs sont sélectionnés parmi un ensemble prédéfini d'attributs possibles en fonction de l'élément.
* Les valeurs sont assignées aux attributs et doivent être contenues à l'intérieur de guillemets.

Voici un autre exemple d'un élément avec un attribut :

```html
<div class="container">
   Un tas de trucs !
</div>
```

### Imbrication

Les éléments HTML s'imbriquent les uns dans les autres. L'élément qui s'ouvre en premier se ferme en dernier.

Lors de l'imbrication d'éléments, des espaces et des tabulations sont souvent utilisés pour montrer le niveau d'imbrication. Cependant, l'espacement n'est pas requis et est uniquement utilisé pour rendre le HTML plus facile à lire pour les humains.

Voici un exemple de HTML avec quelques niveaux d'éléments imbriqués :

```html
<body>
  <div class="outer-div">
    <p>Ceci est un site web incroyable !</p>
    
    <a href="https://www.freecodecamp.org">freeCodeCamp</a>

    <div class="inner-div">
      <ol>
        <li>Chose 1</li>
        <li>Chose 2</li>
        <li>Chose 3</li>
      </ol>
    </div>
  </div>
</body>
```

### Balises HTML courantes

Voici quelques balises courantes qui sont dans presque tous les documents HTML.

`doctype` : C'est le premier élément sur chaque page HTML. Il indique au navigateur de s'attendre à du HTML et quelle version utiliser. Pour la version la plus récente de HTML, l'élément doit ressembler à ceci : `<!doctype html>`

`html` : Après le doctype, tout le contenu de la page doit être contenu dans les balises `<html>`.

`head` : Cet élément contient le titre de la page et les métadonnées.

`body` : Cet élément contient tout le contenu visible dans une page.

`title` : Cet élément optionnel est le nom de votre page. Il est toujours imbriqué dans la balise `head`.

`div` : Cette balise est l'une des balises les plus utilisées. Elle est utilisée pour créer un conteneur de base d'autres éléments HTML ou de contenu.

`p` : Un paragraphe ou une section de texte.

`h1`-`h6` : Ces balises désignent différents niveaux de titres ou d'en-têtes.

`ol` : Crée une liste ordonnée (numérotée).

`ul` : Crée une liste non ordonnée.

`li` : Élément de liste.

### Liens

Les éléments d'ancrage (`<a></a>`) sont utilisés pour lier d'autres sites sur le web ou dans votre projet.

Cet élément lie à un autre site web :

`<a href="https://freecodecamp.com">freeCodeCamp</a>`

Cet élément lie à une autre page de votre site web :

`<a href="about.html">À propos de moi</a>`

L'élément `<link>` est un type de lien différent. Contrairement à l'élément d'ancrage, il spécifie les relations entre le document actuel et une ressource externe.

Il est souvent utilisé pour lier un fichier CSS avec un fichier HTML afin que le fichier CSS externe soit utilisé pour styliser le HTML.

Voici un exemple :

`<link src="main.css" rel='stylesheet' />`

### Commentaires

Comme tout autre bon langage de codage, HTML offre des commentaires. Ils fonctionnent comme des commentaires dans tout autre langage. Ils sont ignorés par le moteur du navigateur.

`<!-- Bonjour, je suis un commentaire. -->`

### Tableaux

Les tableaux sont un moyen de représenter des informations complexes dans un format de grille. Ils sont composés de lignes et de colonnes.

Les tableaux sont des éléments composés (similaires aux listes), ils sont composés de plusieurs éléments.

`table` : Élément de tableau.

`tr` : Ligne de tableau.

`td` : Cellule de tableau.

`th` : Cellule d'en-tête de tableau (optionnelle).

Voici un exemple de tableau. D'abord, vous verrez le HTML. Ensuite, vous verrez comment le HTML s'affiche.

```html
<table>
  <tr>
    <th>Prénom</th>
    <th>Nom</th>
    <th>Animal préféré</th>
  </tr>
  <tr>
    <td>Beau</td>
    <td>Carnes</td>
    <td>vache</td>
  </tr>
  <tr>
    <td>Quincy</td>
    <td>Larson</td>
    <td>chien</td>
  </tr>
</table>
```

<table>
  <tr>
    <th>Prénom</th>
    <th>Nom</th>
    <th>Animal préféré</th>
  </tr>
  <tr>
    <td>Beau</td>
    <td>Carnes</td>
    <td>vache</td>
  </tr>
  <tr>
    <td>Quincy</td>
    <td>Larson</td>
    <td>chien</td>
  </tr>
</table>

### C'est l'heure des questions !

1. Qu'est-ce qui ne va pas avec ce code ?

```html
<html>
	<head>
    <body>
    </head>
    
    </body>
</html>
```

<button id="button1" title="Cliquez pour afficher/masquer le contenu" type="button" onclick="if(document.getElementById('spoiler1').style.display=='none') {document.getElementById('spoiler1') .style.display='';document.getElementById('button1').innerText='Masquer la réponse'}else{document.getElementById('spoiler1') .style.display='none';document.getElementById('button1').innerText='Afficher la réponse'}">Afficher la réponse</button>
<div id="spoiler1" style="display:none">
    La balise de fermeture <code>head</code> devrait être avant la balise d'ouverture <code>body</code>.
</div>

2. Qu'est-ce qui ne va pas avec ce code ?

```html
<html>
  <head>
    <title>Le meilleur site jamais !!
  </head>
  <body>    
    <p>Découvrez ce contenu incroyable.</p>
  </body>
</html>
```

<button id="button2" title="Cliquez pour afficher/masquer le contenu" type="button" onclick="if(document.getElementById('spoiler2').style.display=='none') {document.getElementById('spoiler2') .style.display='';document.getElementById('button2').innerText='Masquer la réponse'}else{document.getElementById('spoiler2') .style.display='none';document.getElementById('button2').innerText='Afficher la réponse'}">Afficher la réponse</button>
<div id="spoiler2" style="display:none">
    Il n'y a pas de balise de fermeture <code>title</code>.
</div>

3. Qu'est-ce qui ne va pas avec ce code ?

```html
<p id=content>Découvrez ce contenu incroyable.</p>
```

<button id="button3" title="Cliquez pour afficher/masquer le contenu" type="button" onclick="if(document.getElementById('spoiler3').style.display=='none') {document.getElementById('spoiler3') .style.display='';document.getElementById('button3').innerText='Masquer la réponse'}else{document.getElementById('spoiler3') .style.display='none';document.getElementById('button3').innerText='Afficher la réponse'}">Afficher la réponse</button>
<div id="spoiler3" style="display:none">
    Il devrait y avoir des guillemets autour de la valeur "content".
</div>

## Conclusion

Vous avez maintenant appris les bases de la syntaxe HTML.

Ensuite, vous devriez regarder ce [cours accéléré sur HTML que j'ai créé](https://www.youtube.com/watch?v=916GWv2Qs08) qui enseigne HTML dans le contexte de la construction d'une page web simple.

%[https://www.youtube.com/watch?v=916GWv2Qs08]

Après avoir appris HTML, vous devriez apprendre CSS et JavaScript. J'ai également créé des cours sur ces sujets. Vous pouvez les regarder ensuite :

%[https://www.youtube.com/watch?v=ieTHC78giGQ]



%[https://www.youtube.com/watch?v=PkZNo7MFNFg&t=145s]