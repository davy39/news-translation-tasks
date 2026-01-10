---
title: Un guide étape par étape pour créer des infobulles en CSS pur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-03T14:46:47.000Z'
originalURL: https://freecodecamp.org/news/a-step-by-step-guide-to-making-pure-css-tooltips-3d5a3e237346
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8RpaP4J1KI-RaxdIdMXHNg.gif
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
seo_title: Un guide étape par étape pour créer des infobulles en CSS pur
seo_desc: 'By Youssouf El Azizi

  I recently worked through a short tutorial about creating simple tooltips using
  pure CSS (and no additional HTML element or JavaScript). I later used this technique
  in my own project, and figured out some tricks to improve upon i...'
---

Par Youssouf El Azizi

J'ai récemment suivi un court tutoriel sur la création d'infobulles simples en utilisant uniquement du CSS (sans élément HTML supplémentaire ni JavaScript). J'ai ensuite utilisé cette technique dans mon propre projet et j'ai découvert quelques astuces pour l'améliorer.

Cet article est un tutoriel étape par étape qui vous aidera à comprendre ces astuces CSS afin que vous puissiez également créer des infobulles en CSS pur.

À la fin de cet article, vous saurez comment ajouter une infobulle à n'importe quel élément en ajoutant un simple attribut.

### Le problème

J'avais besoin de créer une infobulle personnalisée pour mon projet.

J'ai commencé par rechercher sur Google « CSS Tooltip Generator ». J'ai trouvé plusieurs générateurs. Leur approche consistait à ajouter une balise span avec une position absolue à l'intérieur de l'élément pour lequel vous souhaitez une infobulle.

Mais j'avais déjà un projet autrement complet. Je ne voulais pas revenir en arrière et ajouter tous ces éléments span dans mon projet. Cela prendrait du temps et compliquerait mon HTML. Il devait y avoir une meilleure façon.

Enfin, j'ai trouvé un tutoriel incroyable sur YouTube concernant les infobulles. L'astuce intelligente qu'il utilisait était de créer une infobulle en utilisant les sélecteurs CSS `::before` et `::after`. Vous pouvez regarder la vidéo [ici](https://www.youtube.com/watch?v=M4lQwiUvGlY&t=157s).

Cette astuce était intelligente et propre, mais elle n'était pas assez générique.

### Améliorer la solution

Dans cette partie, je vais rendre cette astuce plus générique et nous allons découvrir davantage certaines propriétés CSS. Voici ce que nous voulons finalement pouvoir faire :

```
<button tooltip="contenu de l'infobulle ici"> cliquez ici !! </button>
```

Non seulement cela, mais nous voulons également pouvoir spécifier facilement la position de l'infobulle :

```
<button tooltip="contenu de l'infobulle ici" tooltip-position="left"> cliquez ici !! </button>
```

Tout d'abord — comme mentionné dans la vidéo — nous allons ajouter des pseudo-éléments `before` et `after` au bouton.

`::after` et `::before` sont des pseudo-éléments qui permettent d'insérer du contenu sur une page à partir de CSS avant ou après le contenu de l'élément. Ils fonctionnent comme ceci :

```
div::after { content: "after";}
div::before { content: "before";}
```

Le résultat ressemble à ceci :

```
<div> before <!-- contenu de la div ici --> after</div>
```

### Passons en revue cela étape par étape

**Étape 1 :** nous allons ajouter un attribut tooltip comme ceci :

```
<button tooltip="infobulle simple ici"> cliquez ici !! </button> 
```

Nous avons besoin des pseudo-éléments `::after` et `::before`. Ceux-ci seront un simple rectangle avec le contenu de l'infobulle. Nous créons un simple rectangle avec CSS en ajoutant une bordure autour d'un élément vide que nous créons avec la propriété `content`.

Le pseudo-élément `::before` est utilisé pour afficher le contenu de l'infobulle. Nous l'ajoutons avec la propriété `content` et extrayons la valeur de l'attribut tooltip. La valeur pour content peut être une chaîne, une valeur d'attribut de l'élément comme dans notre exemple, ou même une image avec `url(path/image.png)`.

Pour que cela fonctionne, la position de l'élément bouton doit être relative. En d'autres termes, la position de tous les éléments à l'intérieur du bouton est relative à la position de l'élément bouton lui-même.

Nous ajoutons également quelques astuces de positionnement pour centrer l'infobulle avec la propriété transform et voici le résultat.

Voici notre CSS :

**Étape 2 :** nous jouons simplement avec les pseudo-éléments `::before` et `::after` pour créer une position d'infobulle. Notre HTML de bouton ressemblera à ceci :

```
<button tooltip="infobulle ici" tooltip-position="left"> cliquez ici !! </button>
```

La position de l'infobulle peut être : right, left, top ou bottom.

**Étape 3 :** dans cette dernière étape, nous allons ajouter une simple animation au survol de l'infobulle.

Ce CodePen montre le résultat final (et vous pouvez cliquer pour voir le code final) :

### Si vous êtes familier avec React, consultez mon article :

[**Présentation de reactjs-popup ? — Modales, Infobulles et Menus — Tout en un**](https://hackernoon.com/introducing-reactjs-popup-modals-tooltips-and-menus-all-in-one-227de37766fa)  
[C_et article donne un aperçu simple de ce que vous pouvez faire avec reactjs-popup et comment l'utiliser efficacement._hackernoon.com](https://hackernoon.com/introducing-reactjs-popup-modals-tooltips-and-menus-all-in-one-227de37766fa)

Merci d'avoir lu ! Si vous pensez que d'autres personnes devraient lire cela, appuyez sur le bouton ?, tweetez et partagez l'article. N'oubliez pas de me suivre sur Medium pour être informé de mes futurs articles.

> **Lisez plus d'histoires [https://elazizi.com/](https://elazizi.com/)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*LPHtw2Z8OsGaAfjNWSrm9w.gif)