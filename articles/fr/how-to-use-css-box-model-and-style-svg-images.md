---
title: Comment utiliser le modèle de boîte CSS et styliser les images SVG
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-03T17:29:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-box-model-and-style-svg-images
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-tiger-lily-4483610--1-.jpg
tags:
- name: CSS
  slug: css
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: Comment utiliser le modèle de boîte CSS et styliser les images SVG
seo_desc: "By Njoku Samson Ebere\nEvery programmer who wants to write clean CSS and\
  \ build great user interfaces should understand the CSS Box Model. \nBefore I understood\
  \ the foundations of CSS, I would often write unnecessary styles for margins and\
  \ padding.   \nC..."
---

Par Njoku Samson Ebere

Tout programmeur qui souhaite écrire du CSS propre et créer de grandes interfaces utilisateur devrait comprendre le **modèle de boîte CSS**. 

Avant de comprendre les bases du CSS, j'écrivais souvent des styles inutiles pour les **marges** et les **remplissages**.   
  
Le modèle de boîte CSS constitue la base du style de tout élément sur un site web. Comprendre ce concept vous aidera à cibler les éléments HTML et à écrire moins de lignes de code, propres et faciles à maintenir.  
  
Cet article vous apprendra à cibler les propriétés de tout élément HTML et à appliquer le bon style. Vous apprendrez également ce que sont les images SVG et comment les styliser.

## Qu'est-ce que le modèle de boîte CSS ?

Le modèle de boîte CSS est la relation entre un **élément HTML** et les espaces autour de lui - son **remplissage, bordure** et **marge**.

* Le remplissage est l'espace qui entoure un élément HTML donné
* La bordure est l'espace qui entoure le remplissage
* La marge est l'espace qui entoure la bordure

En d'autres termes, le **remplissage** entoure l'élément HTML, la **bordure** enferme le remplissage, et la **marge** contient la bordure. L'image ci-dessous l'illustre :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/jsm663u6fvzpq4b5buzr.jpg)
_Illustration du modèle de boîte CSS_

Assez de théorie - traduisons le diagramme en code.

## Codons

%[https://www.youtube.com/watch?v=BWIpVT-QHbA&t=12s]

Vous pouvez obtenir votre code de départ [ici](https://github.com/EBEREGIT/box-model-tutorial/tree/starter-code) en clonant le dépôt.  
  
Sinon, vous devrez créer un nouveau fichier HTML et copier le code suivant dans le fichier (si vous ne voulez pas cloner le dépôt ou ne savez pas comment utiliser Git).

```
<!DOCTYPE html>
<html>
  <head>
    <title>Tutoriel sur le modèle de boîte</title>
    <style>
    </style>
  </head>
  <body>
    <img src="https://www.w3schools.com/howto/img_avatar2.png" />
  </body>
</html>
```

Le code ci-dessus est une plaque de base HTML de base. Il contient un `title` et un élément `img`. J'ai obtenu l'image de [w3schools](https://www.w3schools.com/).

Chargez le fichier dans un navigateur, et vous devriez obtenir le résultat suivant :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/0qm111t5yctvgkks36ea.JPG)
_Aperçu avec marge_

Remarquez que l'image est venue avec un espace par défaut autour d'elle. C'est la marge par défaut. Retirons-la.   
  
Entrez le CSS suivant dans la balise `style` de votre fichier HTML :

```
   body{
     margin: 0;
   }
```

Ce code supprime toutes les marges autour de l'image. Remarquez qu'il n'y a plus d'espace entre les bords du navigateur et le contenu dans l'image ci-dessous.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/ruru86w57zd4k512kv2o.JPG)
_Aperçu sans marge_

Maintenant, passons à l'essentiel.  
  
Ajoutez une bordure avec le code suivant :

```
  img{
    border: 5px solid red;
  }
```

Ce code ajoute une bordure rouge autour du contenu. La largeur de la bordure est de 5 pixels.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/plb3mv3dxg4oju57ok1r.JPG)
_Aperçu avec bordure_

Et ajoutez un peu de remplissage avec le code ci-dessous :

```
  img{
    border: 5px solid red;
    padding: 20px;
  }
```

Le code ci-dessus crée maintenant un espace entre le contenu et la bordure. Cet espace est appelé **remplissage**. Il fait 20 pixels de large.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/01zjji5x4ypu18rpo5u9.JPG)
_Aperçu avec remplissage_

Tapez le code suivant pour ajouter une marge :

```
  img{
    border: 5px solid red;
    padding: 20px;
    margin: 20px;
  }
```

Vous vous souviendrez que nous avons supprimé la marge lorsque nous avons défini la marge à 0px. Le code ci-dessus ajoute maintenant notre marge personnalisée qui fait 20 pixels de large. Il crée un espace entre la bordure rouge et les bords du navigateur.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/7aowqpgt6or44ivtzz0y.JPG)
_Aperçu avec bordure_

Vous pouvez obtenir le code de cette section [ici](https://github.com/EBEREGIT/box-model-tutorial) ou copier le code ci-dessous :

```
<!DOCTYPE html>
<html>
  <head>
    <title>Tutoriel sur le modèle de boîte</title>
    <style>
        body{
            margin: 0;
        }

        img{
            border: 5px solid red;
            padding: 20px;
            margin: 20px;
        }
    </style>
  </head>
  <body>
    <img src="https://www.w3schools.com/howto/img_avatar2.png" />
  </body>
</html>
```

Le projet est en ligne ici - [https://eberegit.github.io/box-model-tutorial/](https://eberegit.github.io/box-model-tutorial/).  
  
OUI ! Nous l'avons fait. Nous avons réussi !

## Comment styliser les images SVG

Maintenant que vous comprenez comment fonctionne le modèle de boîte CSS, essayons de styliser un élément HTML important - un SVG. C'est un peu différent des autres éléments, mais les principes sont les mêmes.

Les [images SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) sont des ressources légères qui peuvent aider à accélérer vos applications. Cette section vous aidera à voir les SVG sous un angle convivial et à construire de meilleures applications.  
  
Les fichiers SVG se composent d'éléments tels que les éléments `<g>` et `<path>`. Vous n'avez pas à les mémoriser. Vous pouvez inspecter l'image SVG dans votre navigateur pour voir les différentes parties et comment vous pouvez cibler l'élément que vous voulez.  
  
Ces éléments ont un attribut `border` (représenté comme **stroke**) et `background-color` (**fill**). Nous allons examiner ceux-ci dans un instant.  
  
Vous pouvez télécharger l'image SVG pour ce tutoriel [ici](https://freesvg.org/volleyball-player-caricature). Et vous pouvez obtenir le projet de départ [ici](https://github.com/EBEREGIT/styling-svg-images/tree/starter-project).  
  
Dans le projet de départ, j'ai déjà :

1. Ajouté le fichier `SVG` téléchargé au répertoire du projet.
2. Créé un fichier `index.html`.
3. Copié et collé le code SVG du fichier SVG dans le fichier `index.html`.
4. Créé un fichier `style.css` avec le code suivant pour centrer tout le contenu :

```
body{
    text-align: center;
}
```

Si vous exécutez le projet dans un navigateur, vous devriez obtenir le résultat suivant :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/l55mafu2iaj3xpcsrd3q.JPG)
_Projet de départ_

## Comment styliser l'image SVG

### Rendre l'image réactive

Modifiez les propriétés `width` et `height` de l'élément SVG à 50% et 100vh, respectivement, dans le fichier `index.html` pour rendre l'image réactive comme suit :

```
<svg
        version="1.1"
        id="volleyball"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px"
        y="0px"
        width="50%"
        height="100vh"
        viewBox="0 -0.5 167 267"
        enable-background="new 0 -0.5 167 267"
        xml:space="preserve"
      >

      ...

</svg>
```

Maintenant, votre sortie devrait ressembler à ceci :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/y326rifv946zsphrabtq.JPG)
_L'image occupe maintenant toute la page et est également réactive_

Cela a l'air bien, continuons !

### Comment changer la couleur de la bordure

L'image SVG que nous utilisons dans ce tutoriel contient un élément `<g>`, un élément `<path>` et un élément `<circle>`.  
  
Nous allons cibler l'ensemble du `path` et du `circle` à la fois et leur donner des `border-colors` et une `width` avec le code suivant :

```
path{
    stroke: red;
    stroke-width: 2px;
}

circle{
    stroke: darkblue;
}
```

Vérifiez si votre sortie correspond à la mienne ci-dessous :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/sa8p8g8815lm6u2hb5fy.JPG)
_Contour ajouté_

Remarquez que nous avons changé la couleur de la bordure du `path` en `red` avec une `width` réduite. Ensuite, nous avons changé la couleur de la bordure du `circle` en bleu foncé. C'est génial !

### Comment changer le fond

Nous pourrions changer la couleur de fond pour les `paths` et les `circles` comme nous l'avons fait avec la `border`, mais faisons quelque chose de différent. Nous allons donner à chaque `path` et `circle` des couleurs de fond différentes.  
  
Chaque `path` et `circle` a un `id` unique.  
  
Ajoutons le code suivant à notre fichier `styles.css` pour donner aux `path` et `circle` des couleurs de fond différentes avec le code suivant :

```
#torso{
    fill: blue;
}

#left_leg{
    fill: green;
}

#left_arm{
    fill: indigo;
}

#right_arm{
    fill: yellow;
}

#ball{
    fill: hotpink;
}

#head{
    fill: olive;
}
```

J'ai maintenant un joueur de volley-ball qui ressemble à un clown :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/6yrdytn4p7hzm3qib64k.JPG)
_Remplissage ajouté_

Si votre clown ressemble au mien, alors procédons...

### Comment ajouter un attribut de survol

Pour ajouter une propriété de survol, ajoutez le code suivant au fichier `styles.css` :

```
path:hover{
    stroke: black;
    stroke-width: 10px;
}

circle:hover{
    stroke: black;
    stroke-width: 10px;
}
```

Ma sortie est l'image GIF que vous voyez ci-dessous :

![Image](https://dev-to-uploads.s3.amazonaws.com/i/arr2k0echobmtrgo01ro.gif)
_Survol ajouté_

  
Avec le clown qui ressemble à cela, faisons une dernière chose.

### Comment ajouter des balises d'ancrage

Maintenant, nous allons envelopper chaque `path` et `circle` avec une balise d'ancrage.  
  
Donnez à la balise `anchor` un `title` (représenté comme `xlink:title`) et un attribut href (comme `xlink:href`) de la manière suivante :

```
<a xlink:title="un titre" xlink:href="une url">
  <path> codes ici </path>
</a>

<a xlink:title="un titre" xlink:href="une url">
  <circle> codes ici </circle>
</a>
```

Allez-y et utilisez n'importe quel `title` et `URL` de votre choix. J'ai ajouté mes profils de réseaux sociaux et d'autres sites web que j'ai construits. Consultez le mien ci-dessous :  


![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1680184339979_ezgif.com-video-to-gif.gif)
_Résultat final_

  
En plus de changer la largeur du contour, nous pouvons voir des `labels`, et chaque partie de l'`image` est liée à un site web différent.  
  
Les attributs `xlink:title` et `xlink:href` ajoutent un `label` et une `URL` individuellement.  
  
Tous les codes de cette section sont [ici](https://github.com/EBEREGIT/styling-svg-images). Le projet est en ligne [ici](https://eberegit.github.io/styling-svg-images/)  
  
**VOUS ÊTES GÉNIAL !**

## Conclusion

Le CSS devient un peu plus facile lorsque vous comprenez les bases. Cet article visait à vous les enseigner.   
  
Vous avez appris la différence entre **marge** et **remplissage**. Vous avez également vu comment ils sont liés. Une fois que vous comprenez cela, déplacer des éléments autour de la page devient facile. En résumé, utilisez le remplissage pour déplacer un élément dans son conteneur ou son axe et utilisez une marge pour créer un espace entre les éléments.  
  
J'ai apprécié de disséquer cette image SVG avec vous. Vous savez maintenant comment travailler avec n'importe quelle image SVG qui se présente à vous. Elles peuvent différer, mais le principe est de comprendre comment leurs éléments sont nommés. Ensuite, vous pouvez cibler ces éléments dans votre style.  
  
Essayez d'autres images SVG et voyez comment elles se présentent.