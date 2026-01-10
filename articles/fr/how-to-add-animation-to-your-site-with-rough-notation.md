---
title: Comment utiliser la bibliothèque Rough Notation pour animer votre site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-02T16:52:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-animation-to-your-site-with-rough-notation
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/png_20220803_195955_0000.png
tags:
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: Web Development
  slug: web-development
seo_title: Comment utiliser la bibliothèque Rough Notation pour animer votre site
  web
seo_desc: "By Njong Emy\nI love animating websites. It's so fun when you just look\
  \ at a site, and there are cool animations that make everything look pretty. \n\
  Getting started with an animation library does not have to be hard. Anyone can add\
  \ a bit of animation t..."
---

Par Njong Emy

J'adore animer les sites web. C'est tellement amusant de regarder un site et de voir des animations cool qui rendent tout joli. 

Commencer avec une bibliothèque d'animation n'a pas besoin d'être difficile. Tout le monde peut ajouter un peu d'animation à son site, peu importe s'ils sont bons avec le front-end ou non.

Laissez-moi vous montrer comment vous pouvez commencer.

# Qu'est-ce que Rough Notation ?

Rough Notation est une bibliothèque d'animation JavaScript légère mais incroyable que vous pouvez utiliser pour commencer avec les animations assez rapidement. Et elle est open source ! 

La documentation est assez simple, ce qui en fait une excellente bibliothèque d'animation pour commencer.

Dans cet article, je vais vous guider à travers les étapes de base pour commencer avec Rough Notation, et nous allons construire un petit site avec quelques animations. 

Si vous aimez utiliser la bibliothèque, consultez leur super dépôt. Donnez-lui une étoile, et si vous aimez cet article, faites-leur savoir ! (Ce n'est pas sponsorisé. J'aime juste la bibliothèque :))

Vous pouvez [consulter la documentation de Rough Notation ici](https://github.com/rough-stuff/rough-notation).

## Commençons à animer

### Comment coder le HTML/CSS

Nous ne pouvons pas animer quelque chose que nous ne voyons pas. Donc, pour commencer, nous allons créer une page statique assez simple avec un peu de HTML et de CSS minimal.

Pour l'instant, notre HTML aura l'air fade. Pas grand-chose ne se passe. Juste un élément bien centré avec une police Poppins.

```html
<div class="main">
        
        <header>
            <h1 class="header">Aloha. Bonjour. Salut.</h1>
        </header>

        <main>
            <p>Aujourd'hui, nous allons animer ceci avec <scan class="rough-notation">Rough Notation</scan></p>

            <p>Ceci est un site assez simple. Si vous aimez cela, consultez Rough Notation sur <scan class="link">Github</scan>. Ils sont open source, et ils sont incroyables !</p>

            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maiores omnis molestias voluptas, odit laboriosam esse distinctio provident pariatur accusamus cum?</p>

            <h2>Un peu sur Rough Notation</h2>
            <ul class="list">
                <li>C'est open source.</li>
                <li>C'est facile à commencer.</li>
                <li>Je l'adore !</li>
            </ul>
        </main>
    </div>
```

Dans le code ci-dessus, remarquez les classes que j'ai ajoutées à certains des éléments. C'est ainsi que nous sélectionnons les éléments à animer. 

Notre CSS lui-même est minimal, mais voici à quoi il ressemble et à quoi ressemble notre page :

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');
*{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body{
    font-family: 'Poppins', sans-serif;
}
.main{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 10px;
    margin: 40px;
}
h1{
    margin-bottom: 10px;
}
p{
    margin-bottom: 15px;
}
ul{
    margin: 20px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-from-2022-08-01-17-31-32.png)
_Capture d'écran de notre page statique nue. Il y a un en-tête h1 qui dit 'Aloha. Bonjour. Salut.' Quelques autres paragraphes composent la page et il y a une liste non ordonnée qui énonce trois petits faits sur Rough Notation._

### Ajoutons un peu de JavaScript

Attendez, c'est la partie intéressante ! Pour que nos animations aient un quelconque effet, nous avons besoin d'un fichier JavaScript. Créez-en un simplement, et liez-le à votre HTML comme vous le feriez normalement. 

Maintenant, voyons comment fonctionne Rough Notation.

La documentation offre plusieurs façons d'ajouter la bibliothèque à nos projets. Pour simplifier, nous allons charger le module ES directement. 

[Consultez le dépôt et la documentation ici](https://github.com/rough-stuff/rough-notation). 

Donc, essentiellement, nous allons ajouter une balise de script supplémentaire à notre HTML pour qu'elle ressemble à ceci :

```html
<script type="module" src="https://unpkg.com/rough-notation?module"></script>

```

Maintenant que Rough Notation est partiellement présent dans notre projet, nous pouvons nous plonger dans notre fichier JavaScript et l'importer. La première ligne de notre document JavaScript ressemblerait à ceci :

```javascript
import { annotate } from 'rough-notation';
```

Maintenant que Rough Notation est complètement configuré, sélectionnons ce que nous voulons animer sur la page. Basé sur les classes que nous avons ajoutées aux éléments, nous aurions ce qui suit :

```javascript
const header = document.querySelector('.header');
const roughNotation = document.querySelector('.rough-notation');
const link = document.querySelector('.link');
const list = document.querySelector('.list');

```

L'étape suivante est ce qui donnera vie à notre page. Supposons que je veux mettre en surbrillance l'en-tête en rose clair. J'écrirais ce code :

```javascript
const annotation = annotate(header, { type: 'highlight' , color:'pink'});
annotation.show();

```

Nous assignons la variable annotation à une fonction appelée `annotate`. La fonction annotate prend deux paramètres – l'élément que nous voulons annoter, et un objet. 

L'objet peut prendre quelques attributs. Dans ce cas, nous en avons deux : le type d'annotation que nous voulons sur l'en-tête, et la couleur.

Et juste pour mentionner quelques autres types d'annotations que nous pouvons faire :

* Surligner
* Cercle
* Souligner
* Crochets
* Boîte
* Barré
* Rayé

Revenons à notre animation d'en-tête. La dernière ligne est `annotation.show()` qui affiche simplement notre animation.

Si nous sauvegardons notre page et vérifions notre navigateur, rien ne se passe. Cela aurait dû fonctionner (selon la documentation), mais nous n'obtenons rien. 

J'ai trouvé une solution au problème dans une vidéo YouTube, et pour que l'animation prenne vie, nous devons ajuster la ligne d'importation dans notre fichier JavaScript.

Vous pouvez donc la mettre à jour comme ceci :

```javascript
import { annotate } from "https://unpkg.com/rough-notation?module";
```

Si vous êtes comme moi et aimez ouvrir des issues pour vous plaindre (je plaisante) des projets open source, n'hésitez pas à ouvrir une issue sur le dépôt Rough Notation si l'animation ne fonctionne pas pour vous non plus. Mais n'ouvrez une issue que si personne ne vous a devancé. Donc vérifiez d'abord les issues ouvertes et fermées récentes. Que le meilleur ouvreur d'issue gagne :)

Si vous actualisez après avoir corrigé le problème que nous avions, notre en-tête obtient une belle surbrillance rose. Vous la voyez joliment balayer la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-from-2022-08-01-18-24-31.png)
_Capture d'écran de notre site maintenant, avec l'en-tête surligné en rose._

Joli, n'est-ce pas ?

Allons-y et ajoutons quelques animations supplémentaires :

```javascript
const annotation = annotate(header, { type: 'highlight' , color:'pink'});
const annotation2 = annotate(roughNotation, {type:'circle', color:'yellow', padding:7});
const annotation3 = annotate(link, { type: 'box' , color:'blue', padding:7});
const annotation4 = annotate(list, { type: 'bracket' , color:'red', brackets:['left', 'right'], strokeWidth:5});

const array = annotationGroup([annotation, annotation2, annotation3, annotation4]);
array.show();
```

Cette fois, nous avons ajouté pas mal de choses. Mais ne vous laissez pas submerger. Nous allons le parcourir étape par étape.

Tout d'abord, nous avons ajouté un `padding` à notre animation `annotation2`. Tout comme nous l'avons vu avec l'en-tête, le `roughNotation` (qui est la classe `rough-notation` dans notre HTML) obtient un cercle jaune avec un padding de 7. 

Mais le padding n'est pas le seul nouvel attribut que nous avons introduit. `annotation4` a quelques nouvelles choses que nous devons apprendre. Le paramètre objet a un attribut, `brackets`, avec un tableau comme valeur. `left` et `right` indiquent que nous voulons des crochets d'ouverture et de fermeture des deux côtés de l'élément. Il a aussi `strokeWidth`, qui détermine l'épaisseur des crochets.

Puisque nous devons "afficher" l'animation de chaque élément, ce qui devient un peu ennuyeux si nous devons animer beaucoup de choses, j'ai créé un tableau, j'y ai stocké chaque animation, puis j'ai "affiché" le tableau en une seule fois. C'est pratique et cela fait gagner beaucoup de temps. 

Nous avons donc introduit `annotationGroup`. Pour que cela prenne effet, nous allons l'ajouter à notre ligne d'importation comme ceci :

```javascript
import { annotate, annotationGroup } from "https://unpkg.com/rough-notation?module";
```

Donc... notre site final ressemble à ceci :

![Capture d'écran finale avec toutes les animations mises en place.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-from-2022-08-01-19-46-08.png)

Les animations fonctionneront mieux sur votre navigateur, car vous pouvez actualiser et les voir prendre effet les unes après les autres.

# Conclusion

Écrire cela était amusant ! Et j'espère que vous avez non seulement appris quelque chose de nouveau, mais que vous l'avez aussi essayé.

Assurez-vous de consulter le dépôt et la documentation de Rough Notation, car ils couvrent bien plus que ce que nous avons discuté dans cet article.

Bonne animation !