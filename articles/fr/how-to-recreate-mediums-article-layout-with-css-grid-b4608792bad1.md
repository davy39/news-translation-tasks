---
title: Comment recréer la mise en page des articles de Medium avec CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T18:19:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-recreate-mediums-article-layout-with-css-grid-b4608792bad1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YgYXxuC1tzrUdurfhirtww.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Design
  slug: design
- name: responsive design
  slug: responsive-design
- name: 'tech '
  slug: tech
seo_title: Comment recréer la mise en page des articles de Medium avec CSS Grid
seo_desc: 'By Per Harald Borgen

  When people think of CSS Grid they normally envision image grid layouts and full
  web pages. However, CSS Grid is actually a superb technology for laying out articles
  as well, as it allows you to do things which previously was tri...'
---

Par Per Harald Borgen

Lorsque les gens pensent à CSS Grid, ils imaginent généralement des mises en page de grilles d'images et des pages web complètes. Cependant, CSS Grid est en réalité une technologie excellente pour la mise en page d'articles, car elle permet de faire des choses qui étaient auparavant difficiles à réaliser.

Dans ce tutoriel, je vais expliquer comment recréer la célèbre mise en page des articles de Medium en utilisant CSS Grid.

Note : J'ai également participé à la création d'un cours gratuit en 13 parties sur CSS Grid chez Scrimba. Accédez au cours [ici](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article).

![Cliquez sur l'image pour accéder au cours complet sur CSS Grid.](https://cdn-media-1.freecodecamp.org/images/1*nKjp3EQrrQidw76w0qqB9A.png)
_[Cliquez ici pour accéder au cours complet sur CSS Grid.](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_recreate_medium_layout_article)_

Dans le cours, mon collègue [Magnus Holm](https://medium.com/u/1a7998d688dd) expliquera comment créer une mise en page d'article en utilisant CSS Grid. Donc, si vous préférez regarder plutôt que lire, assurez-vous de consulter son screencast.

### Le contenu

Nous allons commencer avec un fichier HTML de base, qui contient le type de contenu que vous trouverez typiquement dans un article de Medium. Par exemple, titre, paragraphes, sous-titres, images, citations, etc. Voici un extrait :

```html
<article>

<h1>Exécuter n'importe quel package NPM dans le navigateur localement</h1>

<p>JavaScript n'a jamais eu de solution officielle pour distribuer des packages, et chaque plateforme web (Rails, Django, etc.) a sa propre idée de la façon de structurer et de packager JavaScript. Au cours des dernières années, NPM a commencé à devenir le moyen canonique de distribution, avec Webpack comme système de build, mais il n'y a aucun moyen de charger des packages NPM dans le navigateur sans un composant côté serveur.</p>

<blockquote>

<p>Scrimba est une plateforme pour des screencasts de codage interactifs où vous pouvez exécuter le code à tout moment.</p>

</blockquote>

<figure>

<img src="https://mave.me/img/projects/full\_placeholder.png">

</figure>

```

Si vous ouvrez ce fichier sur un site web sans ajuster aucune mise en page, il ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*78oGaexa4dc4cox9b3TIwA.png)

Pas particulièrement élégant. Alors, corrigeons cela avec CSS Grid. Nous le ferons étape par étape pour que ce soit facile à suivre.

### Configuration de base pour les marges

La première chose que nous devons faire est de transformer toute la balise `article` en une grille et de lui donner au moins trois colonnes.

```css
article {  
    display: grid;  
    grid-template-columns: 1fr 740px 1fr;  
}

```

Les première et dernière colonnes sont responsives et agissent comme des marges. Elles contiendront de l'espace blanc dans la plupart des cas. La colonne du milieu est fixée à 740 pixels et contiendra le contenu de l'article.

Remarquez que nous ne définissons pas les lignes, car elles seront simplement aussi hautes qu'elles doivent l'être pour s'adapter à leur contenu. Chaque bloc de contenu dans l'article (paragraphe, image, titre) obtiendra sa propre ligne.

L'étape suivante consiste à s'assurer que tout le contenu de la grille commence à la deuxième ligne de colonne par défaut.

```css
article > \* {  
    grid-column: 2;  
}

```

Nous avons maintenant le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7OmrcS4aCFyiqPBK93IpJg.png)

Nous pouvons immédiatement voir que cela semble mieux, car l'espace blanc de chaque côté rend le texte plus facile à lire.

Cependant, cet effet aurait pu être obtenu tout aussi facilement en définissant les propriétés de marge gauche et droite sur auto. Alors, pourquoi utiliser CSS Grid ?

Eh bien, le problème survient lorsque nous voulons imiter les fonctionnalités d'image de Medium. Par exemple, créer des images en pleine largeur, comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tv8dyhSJfSjtcevJ3rfK6g.jpeg)

Si nous avions utilisé `margin: 0 auto`, cela nous aurait forcés à appliquer des marges négatives aux images pour qu'elles occupent toute la largeur du site web, ce qui est une solution peu élégante.

Avec CSS Grid, cela devient un jeu d'enfant, car nous utiliserons simplement des colonnes pour définir la largeur. Pour que notre image occupe toute la largeur, nous lui dirons simplement de s'étendre de la première à la dernière ligne de colonne.

```css
article > figure {  
    grid-column: 1 / -1;  
    margin: 20px 0;  
}

```

Nous avons également défini une marge en haut et en bas. Et puis nous avons une belle image en pleine largeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*50nsmqw-saQJXQNb0nuhnA.png)

### Extension avec plus de colonnes

Cependant, cela ne nous mène pas jusqu'au bout, car Medium a quelques autres mises en page que nous devons prendre en compte. Regardons quelques-unes d'entre elles :

#### Images de taille moyenne

Il s'agit de l'option d'image entre l'image normale et celle en pleine largeur, que nous appellerons une image de _taille moyenne_. Elle ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kcNKt8kvMpl3c590yOMQpg.jpeg)

  
**_REMARQUE :_**_Si vous regardez sur mobile, cette image est identique à celle en pleine largeur. Dans cet article, nous nous concentrons uniquement sur la mise en page de bureau._

Cela nécessitera au moins deux nouvelles colonnes dans notre mise en page.

#### Citations

De plus, Medium place également une **ligne verticale** sur le côté gauche de l'article si vous ajoutez une citation :

⬅ Remarquez la ligne verticale. Nous devrons ajouter une colonne supplémentaire à notre grille à cause de cela.

Cela nécessite une petite colonne sur le côté gauche de la grille. Pour rendre les choses symétriques, nous ajouterons également une colonne similaire sur le côté droit.

Ainsi, pour supporter à la fois les **citations** et les **images de taille moyenne**, nous devrons diviser toute la largeur en sept colonnes au lieu de trois, comme ceci :

```css
article {  
    display: grid;  
    **grid-template-columns: 1fr 1fr 10px 740px 10px 1fr 1fr;**  
}

```

Si nous utilisons l'inspecteur Chrome, nous pouvons en fait voir les lignes de grille sous-jacentes (voir l'image ci-dessous). De plus, j'ai ajouté des pointeurs pour faciliter la reconnaissance des différentes colonnes.

![J'ai ajouté des pointeurs pour faciliter la reconnaissance des différentes colonnes.](https://cdn-media-1.freecodecamp.org/images/1*YgYXxuC1tzrUdurfhirtww.png)

  
J'ai ajouté des pointeurs pour faciliter la reconnaissance des différentes colonnes.

La première chose que nous devons faire est de faire en sorte que tous les éléments par défaut commencent à la quatrième ligne de colonne au lieu de la deuxième.

```css
article > \* {  
    grid-column: 4;  
}

```

Ensuite, nous pouvons créer l'image de _taille moyenne_ en faisant :

```css
article > figure {  
    grid-column: 2 / -2;  
    margin: 20px 0;  
}

```

Voici à quoi cela ressemble avec l'inspecteur Chrome activé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JabCqoB2CfZzy7toJcAj3A.png)

Les _citations_ sont facilement créées en faisant ce qui suit :

```css
article > blockquote {  
    grid-column: 3 / 5;  
    padding-left: 10px;  
    color: #666;  
    border-left: 3px solid black;  
}

```

Nous le faisons s'étendre de la troisième à la cinquième ligne de colonne. Nous ajoutons également `padding-left: 10px;` pour que le texte semble commencer à la quatrième ligne de colonne (la troisième colonne fait également 10 pixels de large). Voici à quoi cela ressemble sur la grille.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SiTYghcUyboIplQOfFQTqA.png)

### **Notes latérales**

Il y a une dernière chose que nous devons supporter. Medium a une manière assez agréable de signaler quel contenu de l'article est le plus mis en avant. Le texte devient vert et il obtient une _Note latérale_ sur le côté droit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LUik3S2fM6I5P0b_k8EmpQ.png)

L'élément de texte _Note latérale_ aurait été un cauchemar à créer si nous avions utilisé `margin: 0 auto;` au lieu de CSS Grid. Cela est dû au fait que l'élément se comporte différemment de tous les autres éléments de l'article. Au lieu d'apparaître sur une nouvelle ligne, il est censé apparaître sur le côté droit de l'élément précédent. Si nous n'avions pas utilisé CSS Grid, nous aurions probablement dû commencer à manipuler `position: absolute;` pour que cela fonctionne.

Mais avec CSS Grid, c'est super simple. Nous ferons simplement en sorte que ce type d'élément commence à la cinquième ligne de colonne.

```css
.aside {  
    grid-column: 5;  
}

```

Cela le placera automatiquement à droite de l'article :

![Remarque : Je n'ai pas mis en surbrillance le texte en vert, car cela n'a rien à voir avec CSS Grid.](https://cdn-media-1.freecodecamp.org/images/1*_6JkoriZRy1bpDDGc-YPig.png)

  
Remarque : Je n'ai pas mis en surbrillance le texte en vert, car cela n'a rien à voir avec CSS Grid.

Et c'est tout ! Nous avons maintenant recréé la plupart de la mise en page des articles de Medium en utilisant CSS Grid. Et c'était en fait assez facile. Notez cependant que nous n'avons pas abordé la réactivité, car cela nécessite un tout nouvel article en soi.

Consultez [ce terrain de jeu Scrimba pour voir tout le code.](https://scrimba.com/c/cedLJfW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_recreate_medium_layout_article)_