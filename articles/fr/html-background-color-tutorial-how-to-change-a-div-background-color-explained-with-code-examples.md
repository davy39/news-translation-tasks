---
title: Tutoriel sur la couleur d'arrière-plan HTML – Comment changer la couleur d'arrière-plan
  d'une div, expliqué avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-07T02:28:33.000Z'
originalURL: https://freecodecamp.org/news/html-background-color-tutorial-how-to-change-a-div-background-color-explained-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b32740569d1a4ca2a54.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Tutoriel sur la couleur d'arrière-plan HTML – Comment changer la couleur
  d'arrière-plan d'une div, expliqué avec des exemples de code
seo_desc: "By Sarah Chima Atuonwu\nOne of the most common things you may have to do\
  \ as a web developer is to change the background-color of an HTML element. But it\
  \ may be confusing to do if you do not understand how to use the CSS background-color\
  \ property. \nIn ..."
---

Par Sarah Chima Atuonwu

L'une des tâches les plus courantes que vous aurez à effectuer en tant que développeur web est de changer la couleur d'arrière-plan (`background-color`) d'un élément HTML. Mais cela peut être déroutant si vous ne comprenez pas comment utiliser la propriété CSS `background-color`. 

Dans cet article, nous aborderons :

* la valeur par défaut de la couleur d'arrière-plan d'un élément HTML 
* comment changer la couleur d'arrière-plan d'une div, qui est un élément très courant
* quelles parties du modèle de boîte CSS sont affectées par la propriété `background-color`, et
* les différentes valeurs que cette propriété peut prendre. 

### Couleur d'arrière-plan par défaut d'un élément

La couleur d'arrière-plan par défaut d'une div est `transparent`. Ainsi, si vous ne spécifiez pas la couleur d'arrière-plan d'une div, elle affichera celle de son élément parent.

### Changer la couleur d'arrière-plan d'une Div

Dans cet exemple, nous allons changer les couleurs d'arrière-plan des divs suivantes.

```html
<div class="div-1"> J'aime le HTML </div>
<div class="div-2"> J'aime le CSS </div>
<div class="div-3"> J'aime le JavaScript </div>
```

Sans aucun style, cela ressemblera visuellement à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-12.22.48-PM.png)

Changeons la couleur d'arrière-plan des divs en ajoutant des styles aux classes. Vous pouvez suivre en essayant les exemples dans un fichier HTML.

```html
<style>
    .div-1 {
        background-color: #EBEBEB;
    }
    
    .div-2 {
    	background-color: #ABBAEA;
    }
    
    .div-3 {
    	background-color: #FBD603;
    }
</style>

<body>
    <div class="div-1"> J'aime le HTML </div>
    <div class="div-2"> J'aime le CSS </div>
    <div class="div-3"> J'aime le JavaScript </div>
</body>
```

Cela donnera le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.12.29-AM-1.png)

Génial ! Nous avons réussi à changer la couleur d'arrière-plan de cette div. Ensuite, apprenons-en plus sur cette propriété. Voyons comment la propriété background-color affecte les parties du modèle de boîte CSS.

### La couleur d'arrière-plan et le modèle de boîte CSS

Selon le modèle de boîte CSS, tous les éléments HTML peuvent être modélisés comme des boîtes rectangulaires. Chaque boîte est composée de 4 parties, comme le montre le diagramme ci-dessous. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.00-AM-1.png)
_Le modèle de boîte CSS_

Vous pouvez vous renseigner sur le modèle de boîte si vous ne le connaissez pas. La question est : quelle partie du modèle de boîte est affectée lorsque vous changez la couleur d'arrière-plan d'une div ? La réponse simple est la zone de remplissage (padding) et la zone de contenu. Confirmons cela à l'aide d'un exemple.

```html
<style>
    body {
        background-color: #ABBAEA;
    }
    .child {
        height: 200px;
        margin: 20px;
        border: 5px solid;
        background-color: #FBD603;
    }
</style>
<body>
    <div>
        <p>C'est la div parente qui contient la div que nous testons</p>

        <div class="child">
            <p>Cet exemple montre que le changement de la couleur d'arrière-plan d'une div n'affecte pas la bordure et la marge de la div.</p>
        </div>
    </div>
</body>
```

Cela donnera :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.10-AM-1.png)

D'après l'exemple ci-dessus, nous pouvons voir que la zone de marge (margin) et la zone de bordure (border) ne sont pas affectées par le changement de couleur d'arrière-plan. Nous pouvons changer la couleur de la bordure en utilisant la propriété border-color. La zone de marge reste transparente et reflète la couleur d'arrière-plan du conteneur parent. 

Enfin, discutons des valeurs que la propriété background-color peut prendre.

### Valeurs de background-color

Tout comme la propriété color, la propriété background-color peut prendre six valeurs différentes. Examinons les trois valeurs les plus courantes avec un exemple. Dans l'exemple, nous définissons la couleur d'arrière-plan de la div en rouge avec différentes valeurs.

```html
<style>
    /* Valeur par mot-clé / nom de la couleur */
    .div-1 {
        background-color: red;
    }
    
    /* Valeur hexadécimale */
    .div-2 {
       background-color: #FF0000;	 
    }
    
    /* Valeur RGB */
    .div-3 {
    	background-color: rgb(255,0,0);
    }
    
</style>

<body>
    <div class="div-1">
        <p>La propriété background peut prendre six valeurs différentes.</p>
    </div>

    <div class="div-2">
        <p>La propriété background peut prendre six valeurs différentes.</p>
    </div>

    <div class="div-3">
        <p>La propriété background peut prendre six valeurs différentes.</p>
    </div>
</body>
```

Remarquez qu'elles donnent toutes la même couleur d'arrière-plan. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.24-AM-1.png)

Les autres valeurs que la propriété `background-color` peut prendre incluent la valeur HSL, des valeurs de mots-clés spéciaux et des valeurs globales. Voici des exemples pour chacune d'elles.

```css
/* Valeur HSL */
background-color: hsl(0, 100%, 25%;

/* Valeurs de mots-clés spéciaux */
background-color: currentcolor;
background-color: transparent;

/* Valeurs globales */
background-color: inherit;
background-color: initial;
background-color: unset;
```

Vous pouvez en savoir plus sur chacune de ces valeurs [ici](https://developer.mozilla.org/en-US/docs/Web/HTML/Applying_color).

### Note supplémentaire

Lors de la définition de la couleur d'arrière-plan d'un élément, il est important de s'assurer que le rapport de contraste entre la couleur d'arrière-plan et la couleur du texte qu'il contient est suffisamment élevé. Ceci afin de garantir que les personnes malvoyantes puissent lire facilement le texte. 

Considérez ces deux divs.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.11.44-AM-1.png)

Le contraste entre la couleur d'arrière-plan de la première div et la couleur du texte n'est pas assez élevé pour que tout le monde puisse le voir. Ainsi, à moins que vous ne soyez le seul à utiliser le site web que vous construisez et que vous ayez une très bonne vue, vous devriez éviter de telles combinaisons de couleurs. 

La deuxième div a un bien meilleur rapport de contraste entre la couleur d'arrière-plan et la couleur du texte. Elle est donc plus accessible et plus claire à lire pour les gens.

## Conclusion

Dans cet article, nous avons vu comment changer la couleur d'arrière-plan d'une div. Nous avons également discuté des parties du modèle de boîte CSS qui sont affectées par le changement de background-color. Enfin, nous avons discuté des valeurs que la propriété background-color peut prendre. 

J'espère que vous avez trouvé cet article utile. Merci de m'avoir lu.