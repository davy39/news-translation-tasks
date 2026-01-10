---
title: Comment appliquer des bordures aux chemins de découpe avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-12T17:46:38.000Z'
originalURL: https://freecodecamp.org/news/apply-borders-to-clip-paths-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screen-Shot-2023-04-05-at-7.04.59-PM-1.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Comment appliquer des bordures aux chemins de découpe avec CSS
seo_desc: "By Michael Frederick\nApplying borders to non-rectangular shapes in CSS\
  \ can be challenging. In this article, we will explore ways to apply different border\
  \ types to trapezoidal shapes in CSS. \nThe final shape we aim to achieve is a golden\
  \ dashed paral..."
---

Par Michael Frederick

Appliquer des bordures à des formes non rectangulaires en CSS peut être un défi. Dans cet article, nous allons explorer différentes façons d'appliquer divers types de bordures à des formes trapézoïdales en CSS.

La forme finale que nous cherchons à obtenir est une bordure en pointillés dorée en forme de parallélogramme, comme vous pouvez le voir dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screen-Shot-2023-04-05-at-7.09.30-PM.png)
_Parallélogramme avec bordure en pointillés utilisant CSS_

## **Étape 1 : Comment créer un parallélogramme**

Créons un peu de HTML et de CSS de base pour travailler. Dans cet article, nous utiliserons un parallélogramme comme forme de base, mais cette approche fonctionnerait également pour d'autres trapèzes.

Pour créer un parallélogramme, vous pouvez utiliser un [générateur de chemins de découpe en ligne](https://bennettfeely.com/clippy/). Voici le code avec lequel nous allons travailler pour notre parallélogramme :

### **HTML**

```html
<div class="parallelogram"></div>
```

### **CSS**

```css
.parallelogram {
  background: blue;
  height: 500px;
  clip-path: polygon(0% 0%, 75% 0%, 100% 100%, 25% 100%);
}
```

### **Résultat**

![Image](https://lh3.googleusercontent.com/xpXiGBsCXGyPgGPs6J7lsMd5PjxmHTr7FydlwyNARNvtvZJXFA2fsxEScVhPWVU8hp0_NWXWIBPN9DYnMyRACHGhjVqI9wEJsQYfucX2PW4Nf4PabikgK5EzcVpuPbd0vHXoPX77E6KmZXtPl8vjtTM)
_Parallélogramme bleu_

## **Étape 2 : Comment ajouter une bordure solide au parallélogramme**

Maintenant que nous avons un parallélogramme qui suit approximativement la forme que nous recherchons, nous devons lui appliquer une bordure.

### **Essai 1 : Utilisation de la propriété de bordure CSS (échec !)**

C'est ici que l'implémentation commence à se compliquer. Si vous êtes comme moi, la première chose que vous allez essayer est d'appliquer la propriété de bordure CSS au parallélogramme. Voir le code et le résultat ci-dessous pour voir à quoi cela ressemble.

#### **HTML**

```html
<div class="parallelogram"></div>
```

#### **CSS**

```css
.parallelogram {
  background: transparent;
  height: 200px;
  clip-path: polygon(0% 0%, 75% 0%, 100% 100%, 25% 100%);
  border: dashed 5px gold; // tentative d'ajout d'une bordure
}
```

#### **Résultat**

![Bordure sur le chemin de découpe](https://lh6.googleusercontent.com/wEmj4La4dX5mSHdmZjhhM2e0zIdgzu_VLJvd01HSIRRKNY4GUhe1SeHLO90gdgU9BWJNvQeYbUqFXe67RP4cMd8joSpX9qU3GZfYdjD1AEK02ZnB9gefRYuJ51qMgTGVhaE2NQpUuoKYC4hZm-TyShA)
_Bordures en pointillés en haut et en bas_

Le problème dans l'exemple ci-dessus est que la [propriété CSS clip-path](https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path) ne change pas la forme réelle d'un élément de bloc – elle change simplement la portion d'un élément qui est rendue à l'écran.

Cela signifie que la propriété de bordure CSS qui est appliquée au parallélogramme est dessinée comme une bordure rectangulaire autour du conteneur du parallélogramme. Lorsque le clip-path est appliqué, les bordures gauche et droite disparaissent parce qu'elles ne sont pas dans la zone découpée. Les bordures supérieure et inférieure sont dans la zone découpée, donc elles apparaissent toujours.

### **Essai 2 : Simulation d'une bordure (succès !)**

Puisque la propriété de bordure CSS intégrée n'est pas suffisante, nous pouvons plutôt simuler une bordure en superposant deux parallélogrammes l'un sur l'autre, l'un légèrement plus petit que l'autre.

Pour ce faire, nous allons utiliser un conteneur positionné relativement avec un parallélogramme positionné absolument à l'intérieur.

Dans le code ci-dessous, le "small-parallelogram" a un retrait de 1 % du haut et du bas du parallélogramme extérieur. Cet effet est créé avec la propriété clip-path du small-parallelogram.

#### **HTML**

```html
<div class="parallelogram-container">
  <div class="parallelogram"></div>
  <div class="small-parallelogram"></div>
</div>
```

#### **CSS**

```css
.parallelogram-container {
  position: relative;
  height: 300px;
}

.parallelogram {
  height: 300px;
  clip-path: polygon(0% 0%, 75% 0%, 100% 100%, 25% 100%);
  background: rgb(208, 166, 23);
}

.small-parallelogram {
  position: absolute;
  background: white;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  clip-path: polygon(1% 1%, 74% 1%, 99% 99%, 26% 99%);
}
```

#### **Résultat**

![Image](https://lh4.googleusercontent.com/uK-1sTxkdaBTsWusEYbUXs2vl-fjmGqo8JyCB80O85_Y-44z0Q1qwJtaxyyXfVyZUwYaMZXGhO__g_0iZmBSbQxO9USb4mDusdznL0_CQOFNTgAC4X3Ydb0mskLQuVhTrYvkxPBxBCT4L1udQX-WIrs)
_Parallélogramme entièrement contouré_

Dans l'exemple ci-dessus, il y a deux parallélogrammes : un doré qui est recouvert par un blanc. Parce que le blanc a la même couleur de fond que le document et qu'il est légèrement plus petit que le doré, l'arrangement donne l'apparence d'un seul parallélogramme avec une bordure dorée.

## **Étape 3 : Comment créer un effet de bordure en pointillés**

Pour aller plus loin dans ce design, nous voulons faire apparaître la bordure dorée en pointillés. Ainsi, nous devons simuler un effet de bordure en pointillés.

### **Implémentation des bordures gauche et droite**

Pour rendre les bordures gauche et droite en pointillés, nous allons utiliser un fond de dégradé linéaire répétitif. Le dégradé alternera entre le doré et le blanc, donnant au parallélogramme l'apparence d'une bordure en pointillés sur ses côtés gauche et droit.

Mettez à jour le CSS de la div parallelogram en utilisant le code ci-dessous :

#### **CSS**

```css
.parallelogram {
  height: 300px;
  clip-path: polygon(0% 0%, 75% 0%, 100% 100%, 25% 100%);
  background: repeating-linear-gradient(rgb(208, 166, 23) 0px, rgb(208, 166, 23) 8px, white 8px, white 16px);
}
```

#### **Résultat**

![Bordure en pointillés simulée](https://lh3.googleusercontent.com/ibiMVlDwYXh5-NVSHetRI_oajcVThnEBJXV_-o7dJI8e1dpGeCe8y83yi68fKOW8qqkJAKu17DeW2tBg-4tI6KBShFiq1MLzr-CRdM7Rs2CPHX3XtUm6jR3-YVEPYBXRAGj84Y0N2avseAQW_L3HvGA)

### **Implémentation des bordures supérieure et inférieure**

Les bordures supérieure et inférieure nécessitent une approche séparée. Ici, nous allons générer une bordure [en utilisant un SVG](https://kovart.github.io/dashed-border-generator/), ce qui nous permet de contrôler l'espacement et la taille des pointillés.

Cela nécessitera l'introduction d'un autre parallélogramme positionné absolument pour l'effet. Voir la propriété background-image de la div **parallelogram-vertical-borders** ci-dessous pour voir comment le SVG est appliqué pour créer les bordures supérieure et inférieure.

Notez que dans cet exemple, j'ai réduit de moitié la largeur de la bordure. Je l'ai fait en modifiant la propriété "stroke-width" du fond SVG sur la div parallelogram-vertical-borders, et en réduisant de moitié la taille du dégradé linéaire répétitif sur la div parallelogram.

#### **HTML**

```html
<div class="parallelogram-container">
  <div class="parallelogram"></div>
  <div class="parallelogram-vertical-borders"></div>
  <div class="small-parallelogram"></div>
</div>
```

#### **CSS**

```css
.parallelogram-container {
  position: relative;
  height: 300px;
}

.parallelogram {
  height: 300px;
  clip-path: polygon(0% 1%, 75% 1%, 100% 100%, 25% 100%);
  background: repeating-linear-gradient(rgb(208, 166, 23) 0px, rgb(208, 166, 23) 8px, white 8px, white 16px);
  z-index: 1;
}

.parallelogram-vertical-borders {
  height: 300px;
  clip-path: polygon(0% 0%, 75% 0%, 100% 100%, 25% 100%);
  z-index: 1;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 5;
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='rgb(208, 166, 23)' stroke-width='4' stroke-dasharray='6%2c 14' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}

.small-parallelogram {
  position: absolute;
  background: white;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  clip-path: polygon(0.3% 1%, 74.5% 1%, 99.5% 99%, 25.2% 99%);
  z-index: 3;
}
```

#### **Résultat final**

![Ligne en pointillés CSS Parallélogramme](https://lh3.googleusercontent.com/zzVKzZkplxWl7AyOmuWv2o8CXpkxkQMySDAeq0bYAfQvCQ70j34L29oyOwHK7SkB0o_q8e2wTPYgP0BfnhIkzidmOCj731AB__mGtoocf8rD8EJr_wVWCIow_hqQ0uqwBtiMokCagAGcP7f0nAhK2P8)
_Contour en pointillés final du parallélogramme_

## **Conclusion**

Ajouter des bordures à des formes non rectangulaires en CSS peut être un défi, mais dans ce tutoriel, vous avez vu une façon de le faire.

Vous pouvez voir un exemple de travail en direct de l'implémentation de cet article sur la [page d'accueil de Flatirons](https://flatirons.com/).