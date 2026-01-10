---
title: Comment créer de belles ombres de boîte en HTML et CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T16:57:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-beautiful-box-shadows-in-html-and-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Copy-of-Blue-and-White-Modern-Corporate-Travel-YouTube-Thumbnail.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: tailwind
  slug: tailwind
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: Comment créer de belles ombres de boîte en HTML et CSS
seo_desc: "By Manu Arora\nWhenever you're designing a card in HTML, box shadows play\
  \ a vital role in making the cards stand out. \nWhether its a pricing page card\
  \ or even an e-commerce product listing card, box shadows can make or break the\
  \ look and the entire me..."
---

Par Manu Arora

Lorsque vous concevez une carte en HTML, les ombres de boîte jouent un rôle vital pour faire ressortir les cartes. 

Qu'il s'agisse d'une carte de page de tarification ou même d'une carte de liste de produits e-commerce, les ombres de boîte peuvent faire ou défaire l'apparence et l'ensemble du message que les cartes doivent transmettre.

Aujourd'hui, comprenons comment créer de belles ombres de boîte et comment les faire ressortir.

## **Comprendre la syntaxe des ombres de boîte**

Voici la syntaxe de base pour une ombre de boîte :

```css
box-shadow: 1px 2px 3px 4px rgba(20,20,20,0.4);
```

Il y a 5 parties importantes dans l'extrait de code ci-dessus. Comprenons ce qu'elles signifient :

1. Décalage horizontal : `1px` dans l'exemple ci-dessus. Cela indique à quelle distance l'ombre sera de la carte horizontalement. Positif signifie à droite, négatif signifie à gauche.
2. Décalage vertical : `2px` dans l'exemple ci-dessus. Cela indique à quelle distance l'ombre sera de la carte verticalement. Positif signifie vers le bas, négatif signifie vers le haut.
3. Flou : `3px` dans l'exemple ci-dessus. Cela indique à quel point l'ombre sera floue. Un rayon plus élevé signifie plus de flou.
4. Étalement : `4px` dans l'exemple ci-dessus. Cela indique à quelle distance l'ombre s'étendra dans toutes les directions.
5. Couleur : `rgba(20,20,20,0.4)` dans l'exemple ci-dessus. Cela détermine la couleur de l'ombre. Si elle n'est pas fournie, la couleur de texte par défaut sera utilisée. Les valeurs de couleur peuvent être Hex, RGB ou HSL.

Voyons le code ci-dessus en action :

%[https://codepen.io/manuarora700/pen/BawrqZZ]

## Comment les ombres de boîte affectent les cartes

Considérons les deux exemples ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-02-at-7.34.18-PM.png)

Le premier exemple n'a pas d'ombre de boîte, tandis que le second exemple en a une. Le second semble sortir de l'écran (ce qui le fait un peu ressortir par rapport au premier.)  
  
Donc, si vous avez besoin que vos cartes se démarquent, les ombres de boîte peuvent vous aider à les faire vraiment ressortir.

Supposons que vous construisez une application e-commerce et que vous voulez que vos cartes de produits se démarquent. Les ombres de boîte peuvent vous aider à atteindre cet objectif et à faire remarquer vos produits à vos clients. 

Même si votre application web nécessite que vos cartes soient subtiles, vous pouvez toujours opter pour des ombres de boîte subtiles pour donner une sensation esthétique plus agréable aux cartes.

## **Comment utiliser plusieurs couches d'ombres de boîte**

Vous pouvez utiliser plus d'une couche d'ombres de boîte dans vos cartes – et vous le ferez probablement souvent.

La syntaxe pour créer plusieurs couches d'ombres de boîte ressemble à ceci :

```css
box-shadow: rgba(240, 46, 170, 0.4) -5px 5px, rgba(240, 46, 170, 0.3) -10px 10px, rgba(240, 46, 170, 0.2) -15px 15px, rgba(240, 46, 170, 0.1) -20px 20px, rgba(240, 46, 170, 0.05) -25px 25px;
```

Chaque ombre de boîte individuelle est séparée par une virgule (`,`). Vous pouvez en ajouter autant que vous voulez, mais je recommande de vous limiter à cinq au maximum.  
  
L'exemple ci-dessus ressemble à ceci :

%[https://codepen.io/manuarora700/pen/WNZzaJJ]

Remarquez les 5 couches sous les cartes qui sont dans l'ordre décroissant d'opacité. Lorsque cela est fait correctement, cela peut donner un look complètement différent à vos cartes. 

Maintenant, cette carte spécifique peut ne pas sembler parfaite car elle est conçue pour expliquer un certain concept. Mais rendons-la plus intéressante en ajoutant des couleurs aux ombres.  
  
Vous souvenez-vous que nous avons parlé d'ajouter des couleurs en utilisant la syntaxe `rgba()` ? Mettons cela en pratique ici.

%[https://codepen.io/manuarora700/pen/jOGzeev]

Ici, au lieu d'utiliser les valeurs `rgba(0,0,0,0,2)` qui indiquent la couleur (Noir dans cet extrait), je les ai remplacées par `rgba(240, 46, 170, 0.2)` avec une opacité variable dans l'ordre décroissant. C'est une façon d'ajouter des couleurs – la limite est votre imagination.

## **Comment utiliser les ombres de boîte colorées** 

Même si les couleurs peuvent vous aider en faisant ressortir visuellement vos cartes, elles ne sont pas toujours la meilleure option. Parfois, une simple ombre grise fonctionne merveilleusement sur un fond blanc. Mais cela dépend totalement du thème de votre site web.

Considérons une simple application de blog avec beaucoup d'espace blanc et du contenu textuel général. Si vous avez une carte qui affiche des blogs sur le site web, la meilleure façon sera d'ajouter une ombre de boîte simple mais subtile aux cartes pour leur donner un bon effet de relief.  
  
Par exemple : considérons les cartes ci-dessous prises directement de mon [site web](https://manuarora.in), où j'ai listé tous les blogs que j'ai écrits pour freeCodeCamp jusqu'à présent.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-02-at-7.57.17-PM.png)

Mon site web est simple et fait un travail – il met en avant ma personnalité et ce que je fais. Si je vais ajouter une ombre de boîte rouge aux boîtes ci-dessus, cela peut ne pas sembler si bien. Mais si j'utilise une ombre grise avec une certaine quantité de flou, cela aide simplement à la faire ressortir sans être trop voyante.

Alors, comment les utiliser correctement ? Regardons un exemple.

%[https://codepen.io/manuarora700/pen/jOGzeev]

Dans l'exemple ci-dessus :

* Couleur de fond : `rgb(251 113 133);`
* Ombre de boîte : `box-shadow: rgba(254, 205, 211, 0.1) 0px 4px 16px, rgba(254,205,211,0.1) 0px 8px 24px, rgba(254,205,211, 0.1) 0px 16px 56px;`

L'ombre de boîte est une teinte plus claire de la couleur de fond que nous avons utilisée dans l'exemple ci-dessus. Et il y a trois couches d'ombres. 

Lorsque nous avons une couleur de fond, il est généralement bon d'avoir des ombres colorées d'une teinte plus claire de la couleur de fond utilisée. Cela semble mieux que d'avoir une ombre blanche ou noire unie.

## **Comment utiliser les ombres intérieures**

Tous les exemples ci-dessus couvraient des ombres qui étaient 'à l'extérieur' de la carte que nous essayions de styliser. Mais que faire si nous voulions avoir des ombres à l'intérieur ?

Vous pouvez utiliser des ombres de boîte `inset` si vous voulez avoir des ombres de boîte dans le conteneur.

Considérons l'exemple ci-dessous :

%[https://codepen.io/manuarora700/pen/ZEXxqgd]

Le code pour l'ombre est : 

```css
box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
```

Le mot-clé `inset` est utilisé pour spécifier que nous voulons utiliser l'ombre `vers l'intérieur` et non le comportement par défaut qui est `vers l'extérieur`.

Vous pouvez utiliser intelligemment les ombres de boîte intérieures dans vos applications web qui ont des informations importantes à afficher. Comme des puits, ou une alerte que vous essayez de montrer. Dans ce cas, l'élément semble être intégré dans la page web.

## **Exemples d'ombres de boîte**

Créer des ombres de boîte est difficile, non pas parce que c'est compliqué, mais parce que cela nécessite des connaissances en design pour en tirer le meilleur parti. 

J'ai récemment créé une application qui est une liste sélectionnée de belles ombres de boîte qui peuvent aider vos cartes à se démarquer. Actuellement, le projet est classé [n°2 sur ProductHunt](https://www.producthunt.com/posts/tailwind-box-shadows) et aide de nombreux développeurs à rendre leurs cartes belles et efficaces.

Vous pouvez trouver le projet ici : [Tailwind Box Shadows](https://manuarora.in/boxshadows). 

Actuellement, vous pouvez trouver des ombres de boîte en CSS Vanilla et en code Tailwind JIT. Cliquez pour copier et coller et c'est fait. Il y a aussi un utilitaire d'aide pour convertir les ombres de boîte CSS en ombres de boîte Tailwind.

## **Conclusion**

J'ai utilisé des ombres de boîte dans presque tous mes [projets](https://manuarora.in/projects). C'est la chose la plus sous-estimée que j'ai jamais rencontrée. Une bonne disposition d'ombres de boîte peut vraiment améliorer les aspects visuels de votre application.

Si vous avez aimé l'article, essayez d'implémenter ces ombres dans votre application et faites-moi savoir quels changements cela a apporté à votre application.

Si vous avez des commentaires, vous pouvez me contacter sur mon [Twitter](https://twitter.com/mannupaaji) et/ou mon [Site Web Personnel](https://manuarora.in).