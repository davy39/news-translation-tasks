---
title: 'Tutoriel CSS Grid : Apprenez à prototyper des sites web rapidement avec CSS
  Grid'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-30T19:23:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-prototype-websites-quickly-with-css-grid-ffc9cba08583
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Tutoriel CSS Grid : Apprenez à prototyper des sites web rapidement avec
  CSS Grid'
seo_desc: 'By Per Harald Borgen

  The CSS Grid module is a fantastic tool for creating mockups of websites. It allows
  you to experiment with the layout faster than any other system I’ve tried.

  In this article, I’ll teach you how.

  I’ve also created a free CSS Grid...'
---

Par Per Harald Borgen

Le module CSS Grid est un outil fantastique pour créer des maquettes de sites web. Il vous permet d'expérimenter avec la mise en page plus rapidement que tout autre système que j'ai essayé.

Dans cet article, je vais vous apprendre comment faire.

J'ai également créé un cours gratuit sur CSS Grid. [Cliquez ici pour y accéder.](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites)

Alternativement, consultez [cet article](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098), qui explique ce que vous apprendrez tout au long du cours :

[**Vous voulez apprendre CSS Grid ? Voici mon cours complet gratuit. Joyeux Noël !**](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098)

### Notre grille

Nous allons commencer par une grille très basique qui imite un site web classique :

![J'ai stylisé un peu notre exemple, mais cela n'a rien à voir avec CSS Grid, donc je ne vais pas en parler.](https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png)

J'ai stylisé un peu notre exemple, mais cela n'a rien à voir avec CSS Grid, donc je ne vais pas en parler.

Tout d'abord, je vais expliquer le HTML et le CSS dont nous avons besoin pour que cela fonctionne, que j'ai divisé en quatre parties. Une fois que vous les aurez comprises, nous passerons aux expérimentations de mise en page.

Si vous êtes complètement nouveau dans CSS Grid, vous pourriez vouloir parcourir [mon article d'introduction de 5 minutes sur le sujet.](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228)

#### 1. Le balisage

La première chose dont nous avons besoin est un peu de HTML. Un conteneur (l'élément que nous allons transformer en grille) et les éléments (en-tête, menu, contenu, pied de page).

```html
<div class="container">  
  <div class="header">HEADER</div>  
  <div class="menu">MENU</div>  
  <div class="content">CONTENT</div>  
  <div class="footer">FOOTER</div>  
</div>

```

#### 2. Configuration de base en CSS

Ensuite, nous devons configurer notre grille et spécifier le nombre de lignes et de colonnes dont nous avons besoin. Voici le premier CSS pour le faire :

```css
.container {  
    display: grid;      
    grid-template-columns: repeat(12, 1fr);  
    grid-template-rows: 50px 350px 50px;  
    grid-gap: 5px;  
}

```

Je vais ajouter plus tard, mais je veux d'abord que vous compreniez cela.

Voici ce que dit le code ci-dessus : créez une grille avec douze colonnes, chacune ayant une largeur d'une unité de fraction (1/12 de la largeur totale). Créez trois lignes, où la première aura une hauteur de 50px, la deuxième de 350px et la troisième de 50px. Enfin, ajoutez un espace entre les éléments de la grille.

#### 3. Ajout de grid-template-areas

La fonctionnalité qui nous permettra d'expérimenter avec la mise en page très facilement s'appelle _template areas_.

Pour l'ajouter à la grille, nous allons simplement donner au conteneur une propriété `grid-template-areas`. La syntaxe peut être un peu étrange, car elle est différente de toute autre syntaxe CSS. La voici :

```css
.container {  
    display: grid;  
    grid-gap: 5px;      
    grid-template-columns: repeat(12, 1fr);  
    grid-template-rows: 50px 350px 50px;  
    grid-template-areas:  
        "h h h h h h h h h h h h"  
        "m m c c c c c c c c c c"  
        "f f f f f f f f f f f f";}

```

La logique derrière la propriété `grid-template-areas` est que vous créez une représentation visuelle de votre grille dans le code. Comme vous pouvez le voir, elle a trois lignes et douze colonnes, tout comme nous l'avons défini dans `grid-template-columns` et `grid-template-rows`.

Chaque ligne représente une rangée et chacun des caractères (h, m, c, f) représente une cellule de grille.

Chacune des quatre lettres forme maintenant une `grid-area` rectangulaire.

Comme vous l'avez peut-être deviné, j'ai choisi les caractères `h`, `m`, `c`, `f` parce que notre grille se compose de `header`, `menu`, `content` et `footer`. J'aurais pu les appeler comme je voulais, bien sûr, mais il est logique d'utiliser le premier caractère des éléments qu'ils décrivent.

#### 4. Donner des zones aux éléments

Maintenant, nous devons connecter ces caractères avec nos éléments dans la grille. Pour cela, nous allons utiliser la propriété `grid-area` :

```css
.header {  
    grid-area: h;  
}

.menu {  
    grid-area: m;  
}

.content {  
    grid-area: c;  
}

.footer {  
   grid-area: f;  
}

```

Cela donne la mise en page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png)

### Expérimentation avec la mise en page

Maintenant, nous avons enfin atteint la beauté de cette fonctionnalité, car nous pouvons expérimenter avec la mise en page très facilement. Il suffit de changer les caractères de la propriété `grid-template-areas`. Par exemple, déplaçons le menu vers le côté droit :

```css
grid-template-areas:  
        "h h h h h h h h h h h h"  
        "c c c c c c c c c c m m"  
        "f f f f f f f f f f f f";

```

Ce qui donne cette mise en page :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DXjJkGRM_aVa2lVTOj0NyQ.png)

Nous pouvons utiliser des points pour créer des cellules de grille vides.

```css
grid-template-areas:  
        ". h h h h h h h h h h ."  
        "c c c c c c c c c c m m"  
        ". f f f f f f f f f f .";

```

Voici à quoi cela ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uf_PFaU_EA82a-eBA7DHmw.png)

Je vous recommande maintenant de consulter [ce screencast de mon cours CSS Grid](https://scrimba.com/c/c2gd3T2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites), où vous pourrez expérimenter avec le code vous-même.

### Ajout de la réactivité

Combiner cela avec la réactivité est également une fonctionnalité exceptionnelle, car cela n'aurait tout simplement pas été possible à faire avec seulement HTML et CSS auparavant. Supposons que vous voulez le menu à côté de l'en-tête lorsqu'il est vu sur mobile. Alors vous pouvez simplement faire comme ceci :

```css
@media screen and (max-width: 640px) {  
    .container {  
    grid-template-areas:  
            "m m m m m m h h h h h h"  
            "c c c c c c c c c c c c"  
            "f f f f f f f f f f f f";}  
}

```

Et cela donnera le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NDx9-qlf2I3YHv5Kjs4HOQ.gif)

Rappelez-vous que tous ces changements sont faits avec du CSS pur, sans toucher au HTML. Nous pouvons réorganiser comme nous le souhaitons, indépendamment de la manière dont les balises div sont disposées dans le balisage.

Cela s'appelle l'indépendance de l'ordre source, et c'est un énorme pas en avant pour CSS.

Cela permet au HTML d'être ce pour quoi il était destiné : le balisage pour le contenu. Et non pour le style, car c'est le travail de CSS.

Si vous êtes intéressé à en apprendre davantage sur CSS Grid, [cliquez ici](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) pour consulter mon cours complet.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites)_