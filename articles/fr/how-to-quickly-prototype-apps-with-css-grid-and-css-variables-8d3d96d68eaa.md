---
title: Comment prototyper rapidement des applications avec CSS Grid et CSS Variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T16:01:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-prototype-apps-with-css-grid-and-css-variables-8d3d96d68eaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png
tags:
- name: Apps
  slug: apps-tag
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment prototyper rapidement des applications avec CSS Grid et CSS Variables
seo_desc: 'By Per Harald Borgen



  CSS Grid and CSS Variables are both huge wins for front-end developers. The former
  makes it dead simple to create website layouts, while the latter brings the power
  of variables to your stylesheets.

  In this tutorial, I’ll show ...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*mrEbsfQRmq0l32skF3kPOw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

CSS Grid et CSS Variables sont deux grandes avancées pour les développeurs front-end. Le premier simplifie grandement la création de mises en page de sites web, tandis que le second apporte la puissance des variables à vos feuilles de style.

**Dans ce tutoriel, je vais vous montrer comment les utiliser ensemble pour prototyper rapidement des designs d'applications.**

L'exemple que nous allons utiliser est tiré directement de [mon cours gratuit](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) sur la création d'une application de chat en utilisant React.js et l'[API Chatkit](http://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=css-grid-tut) :

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_css_var_grid_prototype)_

Si vous préférez regarder des screencasts interactifs plutôt que lire, [consultez les leçons 15 et 16 de mon cours ici](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype). Vous aurez également accès au code pour pouvoir expérimenter par vous-même. N'hésitez pas à le faire en suivant ce tutoriel.

### Installation du conteneur de grille

Notre application a été conçue en utilisant CSS Grid, un module qui facilite la construction de mises en page et leur réorganisation. Cela est particulièrement utile si vous tirez parti de la propriété `grid-template-areas`, dont je vous montrerai comment nous l'utilisons plus loin.

Commençons par examiner à quoi ressemble notre application de chat initiale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mrEbsfQRmq0l32skF3kPOw.png)

Si nous ouvrons les outils de développement dans Chrome, nous pourrons inspecter comment la grille sous-jacente a été construite. Comme vous pouvez le voir, elle comporte six lignes et six colonnes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_eNLVoRwxgaOftKEfv5i_w.png)

Le code pour créer une telle grille est le suivant :

```css
.app {  
  display:                grid;  
  grid-template-columns:  1fr 1fr 1fr 1fr 1fr 1fr;  
  grid-template-rows:     1fr 1fr 1fr 1fr 1fr 60px;  
}

```

Tout d'abord, nous définissons le conteneur comme étant une grille. Ensuite, nous disons que nous voulons six colonnes et que chacune d'entre elles doit avoir une largeur d'une unité de fraction (`1fr`). Une unité de fraction signifie _une partie de l'espace disponible_. Ici, nous divisons la largeur en six fractions de largeur égale et donnons à chaque colonne une fraction.

En ce qui concerne les lignes, nous ne les divisons pas toutes en hauteur égale, car la dernière ligne n'est pas aussi haute que les autres. Nous avons explicitement indiqué qu'elle doit être haute de `60px` au lieu de `1fr` :

```css
grid-template-rows: 1fr 1fr 1fr 1fr 1fr 60px;

```

Maintenant que nous avons établi la structure de notre grille, nous pouvons passer à la partie suivante : le positionnement.

### Positionnement des éléments de la grille

Chaque enfant direct d'un conteneur de grille est un élément de grille. Nous avons quatre éléments, chacun étant encadré dans un rectangle dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*p_s6nyIhS8XqWoSaLEkBow.png)

Pour placer les éléments dans les positions qu'ils ont ci-dessus, nous devons utiliser la propriété `grid-template-areas` et construire une représentation visuelle de la grille dans notre feuille de style :

```css
.app {  
  display:                grid;  
  grid-template-columns:  1fr 1fr 1fr 1fr 1fr 1fr;  
  grid-template-rows:     1fr 1fr 1fr 1fr 1fr 60px;  
  grid-template-areas:  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "n s s s s s";
}

```

Chacune des chaînes représente une ligne et chacun des caractères représente une cellule dans la grille. Les caractères ont une relation sémantique avec les éléments de grille qu'ils représentent (_liste des salles_, _liste des messages_, _formulaire de nouvelle salle_ et _formulaire d'envoi de message_).

Maintenant, pour positionner nos éléments selon nos `grid-template-areas`, nous devons utiliser les caractères comme leur valeur `grid-area`. Comme ceci :

```css
.new-room-form {  
  grid-area: n;  
}

.rooms-list {  
  grid-area: r;  
}

.message-list {  
  grid-area: m;  
}

.send-message-form {  
  grid-area: s;  
}

```

Ces classes ont bien sûr également été appliquées à nos éléments de grille dans notre HTML. Cependant, je n'entrerai pas dans les détails à ce sujet, car je suppose que vous savez comment ajouter des classes aux balises HTML.

Avec cela en place, nous sommes prêts à commencer à expérimenter avec la mise en page. En échangeant simplement quelques caractères dans la valeur `grid-template-areas`, nous sommes capables de complètement réorganiser la mise en page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ufM_xVxd2GJ79JeOGd2v1w.gif)

Dans le gif ci-dessus, j'essaie quatre mises en page différentes en changeant les positions de l'élément _liste des salles_ et de l'élément _formulaire de nouvelle salle_. La seule chose que je change est la propriété `grid-template-areas`.

Ci-dessous se trouvent les quatre variations. Essayez de voir si vous pouvez associer chacune d'elles à sa mise en page correspondante :

```css
grid-template-areas:  
    "n m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r s s s s s";

grid-template-areas:  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "n s s s s s";

grid-template-areas:  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "s s s s s n";

grid-template-areas:  
    "m m m m m n"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "s s s s s r";

```

Si vous [suivez mon cours sur l'application de chat React.js](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype), vous obtiendrez votre propre copie du code, afin de pouvoir modifier la mise en page exactement comme vous le souhaitez.

### Changer les couleurs avec les variables CSS

Maintenant, nous allons changer les couleurs de l'application en utilisant les variables CSS. Si vous n'avez pas encore été exposé aux variables CSS, jetez un coup d'œil rapide aux images ci-dessous, car elles résument l'essentiel :

![Image](https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*de4-CIacmaMo9PO6PlTkyQ.png)

Comme vous pouvez le voir sur l'image ci-dessus, cela rend votre code plus facile à lire, car le nom de la variable est plus sémantique que la valeur hexadécimale. Deuxièmement, cela vous donne également plus de flexibilité si vous souhaitez changer la couleur.

Voyons comment nous avons stylisé notre application en utilisant les variables CSS, en commençant par nos déclarations de variables :

```css
:root {  
  --main-color:            #5ea3d0;  
  --secondary-color:       white;  
  --main-text-color:       #3e5869;  
  --secondary-text-color:  #b0c7d6;  
  --new-room-form:         #d9e1e8;  
  --send-message-form:     #F5F5F5;  
}

```

Ces variables sont réutilisées 17 fois dans l'ensemble de notre feuille de style. Mais au lieu de passer en revue tous ces endroits, regardons comment la `--main-color` est utilisée comme couleur de fond à la fois dans les messages et dans la barre latérale gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1W0jteJO2F9bdBqw_IC1aQ.png)

Voici comment cela se traduit dans le code :

```css
.rooms-list {  
  background: var(--main-color);}

.message-text {  
  background: var(--main-color);  
}

```

La beauté des variables est que nous pouvons maintenant changer la déclaration, et ce changement affectera l'ensemble de l'application. Par exemple, faisons :

```css
:root {  
  --main-color: red;  
}

```

... ce qui donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zsR6ihPeq1AcaOWdglTL-Q.png)

Ce que nous pouvons faire maintenant, c'est simplement changer toutes les déclarations de variables dans le `:root`, et ainsi changer l'apparence et la sensation de notre application.

Par exemple, trouvons une belle palette en ligne et utilisons-la simplement dans notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qHtPYV_gzrQr-5F7-lJqA.png)

Nous allons remplacer certaines des couleurs dans notre `:root` par celles de la palette ci-dessus :

```css
:root {  
  --main-color: #5ea3d0;  
  --secondary-color: white;  
  --main-text-color: #3e5869;  
  --secondary-text-color: #b0c7d6;  
  --new-room-form: #d9e1e8;  
  --send-message-form: #F5F5F5;  
}

```

Cela donne un type de chat complètement différent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NB4_DfXxI_ZnqDSPI4QEiA.png)

### Combinaison de Grid et Variables

Si nous combinons cela avec le changement de la mise en page en utilisant CSS Grid, nous obtenons deux applications de chat uniques qui se ressemblent à peine. Faisons cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrcUX5S8Eip5NmZ72L62eQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

Voici à quoi ressemble notre point de départ par rapport à notre exemple final.

```css
:root {  
  --main-color:           #ff66ff;  
  --secondary-color:      #fbd8fb; 
  --main-text-color:      #3e5869;  
  --secondary-text-color: #d8b2ff;  
  --new-room-form:        #ffb2ff;  
  --send-message-form:    #d8b2ff; 
}

.app {  
  display: grid;  
  grid-template-columns: repeat(6, 1fr);  
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 60px;  
  grid-template-areas:  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m n n"  
    "f f f f f f"; 
}

```

Plutôt cool, n'est-ce pas ?

Je vous recommande maintenant de suivre [mon cours complet](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype). Dans ce cours, je vous guiderai à travers la création de cette application en utilisant React.js et [l'API Chatkit](http://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=css-grid-tut). Je partagerai bien sûr le code complet avec vous afin que vous puissiez expérimenter ce design par vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zcRbKlNUmWNxStHWrQJEOw.png)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) - la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) si vous souhaitez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_css_var_grid_prototype)_