---
title: Tutoriel de stylisation de la barre de défilement CSS – Comment créer une barre
  de défilement personnalisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-27T00:37:38.000Z'
originalURL: https://freecodecamp.org/news/css-scrollbar-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/CSS-scrollbar-thumbnail.png
tags:
- name: CSS
  slug: css
- name: user experience
  slug: user-experience
seo_title: Tutoriel de stylisation de la barre de défilement CSS – Comment créer une
  barre de défilement personnalisée
seo_desc: "By Charles M.\nHave you ever visited a website with a custom scrollbar\
  \ and wondered how they did it? After reading this article you will understand just\
  \ about everything there is to know about customizing and styling scrollbars using\
  \ CSS. \nIn this tut..."
---

Par Charles M.

Avez-vous déjà visité un site web avec une barre de défilement personnalisée et vous êtes-vous demandé comment ils l'avaient fait ? Après avoir lu cet article, vous comprendrez à peu près tout ce qu'il y a à savoir sur la personnalisation et la stylisation des barres de défilement à l'aide de CSS. 

Dans ce tutoriel, vous allez :

* Apprendre les propriétés CSS natives disponibles pour styliser une barre de défilement dans le navigateur
* Créer quatre barres de défilement uniques à l'aide de CSS
* Découvrir certaines bibliothèques externes qui offrent un support multi-navigateur pour les barres de défilement personnalisées

![Image](https://www.freecodecamp.org/news/content/images/2021/04/crazy-scrollbar.PNG)
_Le summum du design de barre de défilement_

## Tutoriel Vidéo

Si vous préférez les tutoriels vidéo à la lecture, vous pouvez regarder à la place. Vous pouvez également utiliser la vidéo pour laisser des commentaires/questions et poster des liens vers vos propres barres de défilement personnalisées en utilisant quelque chose comme CodePen afin que d'autres puissent voir votre travail.

%[https://www.youtube.com/watch?v=Gp6c9lJgPUI]

## Avantages et inconvénients d'une barre de défilement personnalisée

Avant de plonger dans le code, je pense qu'il vaut la peine d'examiner certains compromis potentiels liés à la création d'une barre de défilement personnalisée pour votre site web ou votre application. 

L'avantage est que cela peut donner à votre site web une chance de se démarquer par rapport aux millions de sites web utilisant la barre de défilement par défaut du navigateur. Tout ce qui peut rendre votre site web ne serait-ce qu'un peu plus mémorable pour les visiteurs vous sera bénéfique à long terme.

D'un autre côté, de nombreux designers UI pensent que vous ne devriez jamais interférer avec les composants UI "standardisés" comme la barre de défilement. Si vous modifiez trop votre barre de défilement, cela peut dérouter les personnes utilisant votre site web ou votre application.

Si vous faites cela pour votre propre site web personnel, vous n'avez probablement pas à vous en soucier tant que vous aimez l'aspect visuel. 

D'un autre côté, si vous envisagez d'implémenter une barre de défilement personnalisée au travail ou pour un projet où vous voulez gagner de l'argent, vous devriez essayer l'A/B testing et prendre une décision basée sur les données en fonction des résultats. 

En fin de compte, la plupart d'entre nous écrivent du code pour générer des revenus pour une entreprise, vous devez donc toujours garder cela à l'esprit.

## Commencer

La première chose que vous devez faire est de créer une mise en page de base pour que la page soit suffisamment grande pour afficher réellement une barre de défilement dans votre navigateur web :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel='stylesheet' href="styles.css">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <h1>Personnalisation de la barre de défilement CSS</h1>
        <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      <p class="para">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      </p>
      </div>
</body>
</html>
```

Rien d'extraordinaire ici, juste un conteneur div de base avec le nom de classe `container` pour notre mise en page, un en-tête pour un titre, et un tas de paragraphes avec le nom de classe `para` pour remplir notre page.

Voici le CSS pour rendre les choses un peu plus élégantes :

```css
body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    
  }
  .para {
    font-size: 16px;
    padding: 20px;
    width: 70%;
  }
  
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
```

Votre page devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/layout-preview.PNG)

## Comment créer des barres de défilement personnalisées avec CSS

Une fois notre configuration terminée, nous pouvons passer à la partie amusante du tutoriel. La première partie de cette section consistera à apprendre les différentes propriétés CSS disponibles pour la stylisation. 

Dans la deuxième partie, nous implémenterons quatre types différents de barres de défilement pour vous donner des idées pour créer les vôtres.

### Propriétés CSS disponibles pour styliser les barres de défilement

Malheureusement, nous n'avons toujours pas de support multi-navigateur standardisé pour styliser les barres de défilement avec CSS. Firefox et les navigateurs basés sur Webkit comme Chrome, Edge et Safari ont des propriétés différentes pour le stylisme. 

Ce tutoriel se concentrera principalement sur les navigateurs Webkit, car ils offrent plus d'options de stylisation, mais nous aborderons également brièvement Firefox.

### Propriétés de stylisation CSS Webkit pour les barres de défilement

* `::-webkit-scrollbar` – la barre de défilement entière
* `::-webkit-scrollbar-track` – toute la zone de la barre de progression de la barre de défilement
* `::-webkit-scrollbar-thumb` – la section déplaçable de la barre de défilement

Les propriétés ci-dessous sont disponibles mais sont moins couramment utilisées :

* `::-webkit-scrollbar-button` – les boutons haut/bas à chaque extrémité de la barre de défilement
* `::-webkit-scrollbar-track-piece` – partie de la barre de défilement non couverte par le curseur (thumb)
* `::-webkit-scrollbar-corner` – coin inférieur où les barres de défilement horizontale et verticale se rejoignent

### Propriétés de stylisation CSS Firefox pour les barres de défilement

Il existe actuellement deux propriétés CSS disponibles pour styliser les barres de défilement dans Firefox

* `scrollbar-width` – contrôle la largeur de la barre de défilement, avec seulement deux options disponibles : `auto` ou `thin` 
* `scrollbar-color` – prend deux couleurs qui sont utilisées pour la coloration du curseur (thumb) et de la piste (track) de la barre de défilement dans cet ordre

Maintenant que vous connaissez vos options pour personnaliser les barres de défilement, mettons-les en pratique avec quelques exemples. 

### Barre de défilement thème sombre

Les sites web en thème sombre sont très à la mode en ce moment. Conserver la barre de défilement par défaut du navigateur pourrait sembler discordant pour les utilisateurs car elle ne s'intègre pas très bien avec un site web au thème sombre.

Utilisons nos nouvelles connaissances en CSS pour créer une barre de défilement de thème sombre avec une bordure arrondie inspirée du site web de CSS Tricks :

```css
html::-webkit-scrollbar {
      width: 20px; 
   }

html::-webkit-scrollbar-track {
    background-color: black;
  }

html::-webkit-scrollbar-thumb {
    background: #4e4e4e;
    border-radius: 25px;
  }
```

Le résultat est un peu difficile à voir sur la capture d'écran, mais la piste est noire et le curseur est d'une couleur gris foncé.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/dark-theme.PNG)

### Barre de défilement minimaliste

Pour cet exemple, vous allez créer une barre de défilement minimaliste. Ce type de barre de défilement fonctionnerait bien si vous recherchez un style simple et élégant pour votre site web.

La chose la plus importante à noter est que vous avez la possibilité d'utiliser les pseudo-éléments `hover` et `active` de CSS pour styliser davantage votre barre de défilement. Dans ce cas, la barre de défilement deviendra d'un gris plus foncé lorsque vous survolerez et ferez glisser le curseur.

```css
html::-webkit-scrollbar {
    width: 10px;
  }

html::-webkit-scrollbar-track {
    background: rgb(179, 177, 177);
    border-radius: 10px;
}

html::-webkit-scrollbar-thumb {
    background: rgb(136, 136, 136);
    border-radius: 10px;
  }

html::-webkit-scrollbar-thumb:hover {
    background: rgb(100, 100, 100);
    border-radius: 10px;
  }

html::-webkit-scrollbar-thumb:active {
    background: rgb(68, 68, 68);
    border-radius: 10px;
  }
```

Le résultat : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/minimalist.PNG)

### Barre de défilement à motifs

Dans cette section, l'accent est mis sur l'utilisation d'un dégradé linéaire répétitif pour créer un effet de motif sur notre piste de barre de défilement. La même chose pourrait être faite pour le curseur de la barre de défilement.

Une autre chose à remarquer est que vous pouvez styliser le curseur de la barre de défilement avec une bordure, que vous pouvez utiliser pour créer un certain nombre d'effets sympas. Dans ce cas, j'ai rendu la couleur d'arrière-plan du curseur transparente afin que vous puissiez voir le motif de la piste de la barre de défilement pendant que nous défilons.

```css
html::-webkit-scrollbar {
   	width: 20px;
  }
html::-webkit-scrollbar-track {
  	background-image: repeating-linear-gradient(45deg, red 0, red 1px, transparent 0, transparent 50%);
  	background-size: 10px 10px;
	}
html::-webkit-scrollbar-thumb {
    background: transparent;
    border-radius: 5px;
    border: 2px solid black;
    box-shadow: inset 1px 1px 5px black ;
   }
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/patterned.PNG)

### Barre de défilement à dégradé « animé »

Cet exemple utilise un dégradé linéaire et une astuce avec box-shadow pour donner l'impression que la barre de défilement change de couleur à mesure que vous montez et descendez dans la page. Ce qui se passe réellement, c'est que l'arrière-plan de la piste de la barre de défilement est révélé sous le curseur.

Cela fonctionne parce que le box-shadow occupe tout l'espace de la barre de défilement, sauf là où se trouve le curseur. Comme le curseur est transparent, la couleur dégradée de l'arrière-plan transparaît.

```css
html::-webkit-scrollbar {
    width: 20px; 
  }
  
html::-webkit-scrollbar-track {
    background:  linear-gradient(0deg, rgba(255, 0, 0, 1) 0%, rgba(7, 0, 211, 1) 100%);
  }

html::-webkit-scrollbar-thumb {
    background: transparent;
    box-shadow: 0px 0px 0px 100vh black;
  }
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/animated.PNG)

## Limitations et alternatives aux barres de défilement personnalisées

Il y a clairement des problèmes avec la création de barres de défilement personnalisées. Le premier serait le manque de support multi-navigateur. D'autres problèmes seraient l'impossibilité d'ajouter des transitions ou des animations à la barre de défilement et le fait que votre barre de défilement personnalisée n'apparaîtra pas sur les appareils mobiles. 

Une alternative consiste à masquer la barre de défilement par défaut et à utiliser une bibliothèque, mais cela peut affecter les performances lorsqu'elle est utilisée comme barre de défilement principale pour votre page. Et il existe d'autres problèmes d'utilisabilité potentiels car ces bibliothèques s'appuient sur JavaScript pour imiter le comportement natif de la barre de défilement. 

Ci-dessous, je vais passer en revue deux bibliothèques open-source populaires pour créer des barres de défilement.

### Bibliothèque SimpleBar

%[https://github.com/Grsmto/simplebar]

Comme son nom l'indique, SimpleBar consiste à faciliter la création de barres de défilement personnalisées. Le seul véritable inconvénient ici est qu'elle ne supporte pas l'utilisation comme barre de défilement principale pour votre site web ou pour les éléments HTML table, textarea ou select. 

L'objectif principal de SimpleBar serait de créer des barres de défilement personnalisées pour des choses comme des applications de chat dynamiques ou tout autre type d'élément de page interne où vous voulez un défilement.

### Bibliothèque Overlay Scrollbars

%[https://github.com/KingSora/OverlayScrollbars]

Overlay Scrollbars est très similaire à SimpleBar mais présente l'avantage supplémentaire de supporter l'élément HTML body. Cela signifie que vous pouvez l'utiliser pour la barre de défilement principale de votre site web en plus de toutes les autres fonctionnalités que vous attendez, comme le support multi-navigateur et mobile.

## Conclusion

J'espère que cet article vous a donné une solide compréhension du fonctionnement de la stylisation des barres de défilement CSS. 

Si vous avez des questions, vous pouvez laisser un commentaire sur la vidéo YouTube et j'essaierai de vous aider. N'hésitez pas non plus à laisser des liens vers vos propres designs afin que d'autres personnes puissent les consulter.

Lien vers le dépôt GitHub : [https://github.com/renaissanceengineer/css-scrollbar-tutorial](https://github.com/renaissanceengineer/css-scrollbar-tutorial)