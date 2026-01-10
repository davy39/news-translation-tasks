---
title: Comment écrire du code HTML et CSS plus rapidement avec Emmet
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-07-26T14:24:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-faster-html-and-css-using-emmet
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Copy-of-Copy-of-Copy-of-Copy-of-read-write-files-python.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Comment écrire du code HTML et CSS plus rapidement avec Emmet
seo_desc: 'Emmet is an essential development tool that helps you quickly create repetitive
  structures like lists, tables, or ordered elements with minimal typing. It is more
  like a shorthand that translates to multiple lines of HTML or a CSS attribute.

  Emmet is...'
---

Emmet est un outil de développement essentiel qui vous aide à créer rapidement des structures répétitives comme des listes, des tableaux ou des éléments ordonnés avec une saisie minimale. C'est plutôt une sorte de sténographie qui se traduit par plusieurs lignes de HTML ou un attribut CSS.

Emmet est intégré dans de nombreux éditeurs de texte comme VS Code. Cependant, vous pouvez également le télécharger pour votre éditeur de texte préféré depuis [ce](https://emmet.io/download/) lien. Emmet est également disponible dans certains IDE en ligne comme CodePen.

Regardez de près l'exemple ci-dessous. Voyez comment nous avons facilement généré dix lignes de code en utilisant uniquement les mots-clés `ol>li{This is a list}*10` ?

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet.gif)
_Emmet faisant sa magie_

Nous avons évité de copier et coller dix lignes puis de compter pour voir s'il y avait dix éléments. Faire cela manuellement introduit également une chance d'erreur humaine.

Dans ce tutoriel, nous allons apprendre quelques raccourcis Emmet qui génèrent rapidement du HTML et du CSS.

## Raccourcis Emmet pour HTML

### Comment créer des commentaires

Pour commenter une seule ligne, appuyez sur `Ctrl + /`.

Pour commenter plusieurs lignes, sélectionnez-les puis appuyez sur `Ctrl + /`.

### Multiplication dans Emmet

Vous pouvez créer plusieurs éléments en spécifiant le compte après `*`.

Par exemple, `p*10` générerait 10 éléments `p`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-s.gif)
_Créer n'importe quel nombre d'éléments en utilisant la multiplication_

### Comment créer des enfants directs

Vous pouvez créer des enfants directs en utilisant le symbole `>`.

`ol>li` créerait un `li` à l'intérieur de l'élément `ol`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-o.gif)
_Création d'enfants directs_

### Comment créer des frères

Vous pouvez créer des frères en utilisant le symbole `+`.

`div+p` créerait un élément `div` et un élément `p` au même niveau.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-xx.gif)
_Création de frères_

### Comment combiner les sélecteurs

Vous pouvez combiner le sélecteur de frères et le sélecteur d'enfants pour créer une structure. Par exemple, `div+p>span` résulterait en un `div` et un élément `p` au même niveau avec un élément `span` comme enfant du sélecteur `p` :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-ss.gif)
_Combinaison de sélecteurs_

### Comment coder des structures complexes en utilisant des crochets `()`

Les crochets `()` peuvent être utilisés pour séparer différentes parties de la structure.

En utilisant le raccourci Emmet `(main>div)+div>ul>li*5`, vous pouvez créer la structure complexe suivante :

```html
<main>
    <div></div>
</main>
<div>
    <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
</div>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-ds.gif)
_Création de structures complexes_

### Comment utiliser Emmet pour définir des IDs

Si vous voulez créer un élément `p` avec l'ID `news-section`, vous pouvez le faire en utilisant ce raccourci Emmet : `p#news-section`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-vv.gif)
_Emmet pour définir des IDs_

### Comment utiliser Emmet pour définir des Classes

Si vous voulez créer un élément `p` avec la classe `news-espanol`, vous pouvez le faire en utilisant ce raccourci Emmet : `p.news-espanol`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-ll.gif)
_Emmet pour définir des Classes_

### Comment créer des Attributs

Il est possible de créer des éléments avec certains attributs en utilisant Emmet.

Le raccourci Emmet `button[type=submit]` créerait cet élément bouton : `<button type="submit"></button>`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-bb.gif)
_Emmet pour définir des attributs_

### Comment ajouter du Contenu aux Éléments

Il est assez facile de fournir du contenu pour vos éléments en utilisant Emmet.

`p{This is a paragraph}` créerait un élément `p` avec le contenu "This is a paragraph".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-pp.gif)
_Emmet pour définir du contenu_

### Énumération

Dans Emmet, l'énumération fait généralement référence au processus de génération de plusieurs éléments HTML avec des nombres ou des alphabets séquentiels.

Voici un exemple d'énumération : `ul>li*5{List item number $}`.

Le `$` indique le point où l'énumération commence. Le `*5` signifie répéter cette structure cinq fois, avec les nombres incrémentant à chaque itération.

Voyons cela en action :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-pj.gif)

### Comment générer du texte Lorem Ipsum

Vous n'avez pas besoin de chercher sur Google le texte "Lorem ipsum" si vous utilisez Emmet.

`Lorem20` générerait un texte de 20 caractères.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-xxx.gif)
_Générer du texte lorem en utilisant Emmet_

### Comment Lier du CSS

Pour lier un fichier CSS, tapez `link` et appuyez sur entrée.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-gg.gif)
_Lier du CSS externe_

### Comment Lier du JavaScript

Pour lier du JavaScript, utilisez le raccourci Emmet `script:src`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/emmet-jjj.gif)
_Lier du JavaScript_

## Raccourcis Emmet pour CSS

Tout comme pour le HTML, Emmet est également disponible pour le CSS.

Voici les raccourcis Emmet pour certaines des propriétés couramment utilisées :

* `m10` → `margin: 10px;`
* `p-10` → `padding: -10px;`
* `m20p` → `margin: 20%;`
* `w100p` → `width: 100%;`
* `bgc#ff` → `background-color: #fff`
* `db` → `display: block;`
* `dib` → `display: inline-block;`
* `df` → `display: flex;`
* `tac` → `text-align: center;`
* `tar` → `text-align: right;`
* `c` → `color: #000;`
* `o` → `overflow: hidden;`
* `z` → `z-index: 1;`

## Conclusion

Si vous êtes dans le développement, je vous recommande vivement d'apprendre Emmet.

Vous passerez moins de temps à écrire du code et obtiendrez des résultats beaucoup plus rapides.

Je parie que une fois que vous commencerez à l'utiliser, votre expérience de développement passera à un tout nouveau niveau !

Quelle est votre chose préférée que vous avez apprise dans ce tutoriel ? Vous pouvez également me contacter sur l'une de ces [plateformes](https://zaira_.bio.link/). 📧

À bientôt dans le prochain tutoriel, bon codage 😁