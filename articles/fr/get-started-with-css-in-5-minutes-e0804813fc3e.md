---
title: Apprendre le CSS en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T22:59:16.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-css-in-5-minutes-e0804813fc3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s2XVUr_QAwNKET1JPOZeEg.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre le CSS en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen

  A quick tutorial on the design language of the web.


  _Want to take our free CSS course? Click here!_

  CSS (Cascading Style Sheets) is what makes web pages look good and presentable.
  It’s an essential part of modern web development...'
---

Par Per Harald Borgen

#### Un tutoriel rapide sur le langage de design du web.

![Image](https://cdn-media-1.freecodecamp.org/images/V1j9VppYwp81V7cTFYNrnRG4ubi5lgXUWEZc)
_Voulez-vous suivre notre cours gratuit sur le CSS ? [Cliquez ici !](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_5_minute_article)_

Le CSS (Cascading Style Sheets) est ce qui rend les pages web belles et présentables. C'est une partie essentielle du développement web moderne et une compétence indispensable pour tout designer et développeur web.

Dans cet article, je vais vous donner une rapide introduction pour vous aider à commencer avec le CSS.

**Nous avons également lancé un cours complet gratuit sur le CSS sur Scrimba.** **[Cliquez ici pour le découvrir.](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article)**

Je suppose que vous avez une compréhension basique du HTML, mais à part cela, il n'y a pas de prérequis pour ce tutoriel.

### Installation

Commençons par apprendre comment nous pouvons inclure le CSS dans nos projets. Il y a typiquement trois façons de le faire.

#### 1. CSS en ligne

Tout d'abord, nous pouvons inclure le CSS directement dans nos éléments HTML. Pour cela, nous utilisons l'attribut `style` et nous lui fournissons des propriétés.

```html
<h1 style="color: blue"> Bonjour le monde ! </h1>
```

Ici, nous lui donnons la propriété `color`, et nous définissons la valeur à `blue`, ce qui donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ig1ubv9fGhYQauKUsi18YQ.png)

Nous pouvons également définir plusieurs propriétés à l'intérieur de la balise `style` si nous le souhaitons. Cependant, je ne veux pas continuer sur cette voie, car les choses deviennent désordonnées si notre HTML est encombré de beaucoup de CSS à l'intérieur.

C'est pourquoi la deuxième méthode pour inclure le CSS a été introduite.

#### 2. CSS interne

L'autre façon d'inclure le CSS est d'utiliser l'élément `style` dans la section `head` du document HTML. Cela s'appelle le style interne.

```html
<head>  
    <style>  
        h1 {  
            color: blue;  
        }  
    </style>  
</head>
```

Dans l'élément style, nous pouvons donner le style à nos éléments HTML en sélectionnant le ou les éléments et en fournissant des attributs de style. Tout comme nous avons appliqué la propriété `color` à l'élément `h1` ci-dessus.

#### 3. CSS externe

La troisième et la plus recommandée façon d'inclure le CSS est d'utiliser une feuille de style externe. Nous créons une feuille de style avec une extension `.css` et nous incluons son lien dans le document HTML, comme ceci :

```html
<head>  
    <link rel="stylesheet" href="style.css">  
</head>
```

Dans le code ci-dessus, nous avons inclus le lien du fichier `style.css` en utilisant l'élément `link`. Nous écrivons ensuite tout notre CSS dans une feuille de style séparée appelée `style.css` afin qu'elle soit facilement gérable.

```css
h1 {  
   color: blue;  
}
```

Cette feuille de style peut également être importée dans d'autres fichiers `HTML`, ce qui est idéal pour la réutilisabilité.

### Sélecteurs CSS

Comme nous l'avons discuté précédemment, le CSS est un langage de design utilisé pour styliser les éléments HTML. Et afin de styliser les éléments, vous devez d'abord les sélectionner. Vous avez déjà vu un aperçu de comment cela fonctionne, mais plongeons un peu plus profondément dans les sélecteurs CSS, et regardons trois façons différentes de sélectionner les éléments HTML.

#### 1. Élément

La première façon de sélectionner un élément HTML est simplement d'utiliser le nom, ce que nous avons fait ci-dessus. Voyons comment cela fonctionne :

```css
h1 {  
    font-size: 20px;  
}  
p {  
    color: green;  
}  
div {  
    margin: 10px;  
}
```

L'exemple ci-dessus est presque auto-explicatif. Nous sélectionnons différents éléments comme `h1`, `p`, `div` et leur donnons différents attributs de style. Le `font-size` contrôle la taille du texte, `color` définit la couleur du texte, et `margin` ajoute de l'espacement autour de l'élément.

#### 2. Classe

Une autre façon de sélectionner les éléments HTML est d'utiliser l'attribut de classe. En HTML, nous pouvons assigner différentes classes à nos éléments. Chaque élément peut avoir plusieurs classes, et chaque classe peut également être appliquée à plusieurs éléments.

Voyons cela en action :

```html
<div class='container'>  
    <h1> Ceci est un titre </h1>  
</div>
```

```css

.container {  
    margin: 10px;  
}
```

Dans le code ci-dessus, nous avons assigné la classe `container` à l'élément div. Dans la feuille de style, nous sélectionnons notre classe en utilisant le format `.className` et lui donnons une marge de `10px`.

#### 3. ID

Comme les classes, nous pouvons également utiliser les ID pour sélectionner les éléments HTML et leur appliquer un style. La seule différence entre une classe et un ID est qu'un ID ne peut être assigné qu'à un seul élément HTML.

```html
<div>  
    <p id='para1'> Ceci est un paragraphe </p>  
</div>
```

```css

#para1 {  
    color: green;  
    font-size: 16px;  
}
```

L'exemple ci-dessus montre comment nous assignons un ID à l'élément paragraphe et utilisons ensuite le sélecteur d'ID dans la feuille de style pour sélectionner le paragraphe et lui appliquer le style.

### Polices et Couleurs

Le CSS nous offre littéralement des centaines d'options pour jouer avec les polices et les couleurs et rendre nos éléments HTML jolis. Nous pouvons choisir parmi deux types de noms de familles de polices :

**1. Famille générique :** un groupe de familles de polices avec un look similaire (comme 'Serif' ou 'Monospace')

**2. Famille de polices :** une famille de polices spécifique (comme 'Times New Roman' ou 'Arial')

Pour les couleurs, nous pouvons utiliser des noms de couleurs prédéfinis, ou des valeurs RGB, HEX, HSL, RGBA, HSLA.

```html
<div class='container'>  
    <h1 class='heading1'>  
        Le CSS est trop cool !!!  
    </h1>  
</div>
```

```css
.container {  
    width: 500px;  
    height: 100px;  
    background-color: lightcyan;  
    text-align: center;  
}

.heading1 {  
    font-family: 'Courier New';  
    color: tomato;  
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*OBQCn1lDTG8cskhUYwNTDg.png)

Comme vous pouvez le voir dans l'exemple ci-dessus, nous avons un élément div avec la classe `container`. À l'intérieur de ce div, il y a une balise `h1` avec du texte à l'intérieur.

Dans la feuille de style, nous sélectionnons la classe container et définissons sa `width`, `height`, `background-color`, et `text-align`.

Enfin, nous sélectionnons la classe `.heading1` — qui est appliquée à la balise `h1` — et lui donnons les attributs `font-family` et `color`.

### Conclusion

Vous pourriez vous sentir un peu submergé par toutes ces informations, mais ne vous inquiétez pas.

Consultez simplement notre [cours d'introduction gratuit au CSS sur Scrimba](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article) et vous serez un ninja du design web en moins d'une heure.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_5_minute_article)_