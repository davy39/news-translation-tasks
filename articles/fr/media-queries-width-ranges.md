---
title: Comment définir des plages de largeur pour vos requêtes média CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-06T16:32:00.000Z'
originalURL: https://freecodecamp.org/news/media-queries-width-ranges
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/amirali-mirhashemian-jh5XyK4Rr3Y-unsplash-1.jpg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Comment définir des plages de largeur pour vos requêtes média CSS
seo_desc: 'By Caleb Olojo

  A media query is a feature of CSS. It lets you create and implement layouts that
  adapt to the properties of the device you''re using. Some of these properties include
  the height and width of a page.

  In this short guide, you''ll see how y...'
---

Par Caleb Olojo

Une requête média est une fonctionnalité de CSS. Elle vous permet de créer et d'implémenter des mises en page qui s'adaptent aux propriétés de l'appareil que vous utilisez. Certaines de ces propriétés incluent la hauteur et la largeur d'une page.

Dans ce court guide, vous verrez comment définir plusieurs propriétés de largeur dans une règle de requête média. Pour l'instant, examinons d'abord les fondamentaux.

## Comment fonctionnent les requêtes média en CSS

Maintenant que vous avez une idée de base de ce qu'est une requête média, examinons comment cette fonctionnalité particulière de CSS fonctionne réellement.

Une requête média de base ressemble à ceci :

```css
@media only screen and (max-width: 576px) {
    // faire quelque chose
}

@media only screen and (min-width: 576px) {
    // faire quelque chose à nouveau
}
```

Cela signifie que les styles écrits à l'intérieur des règles média ci-dessus ne fonctionneront ou ne seront efficaces qu'aux propriétés de largeur spécifiées ci-dessus.

Littéralement, vous dites qu'à cette largeur particulière (c'est-à-dire la propriété `max-width` de `576px`), CSS, appliquez les styles que je vais écrire ici à cette largeur seule, à partir d'une largeur initiale de `0px`.

## Propriétés max-width et min-width

Il y a deux choses à garder à l'esprit lorsque vous créez des requêtes média pour différentes tailles d'écran : les propriétés `max-width` et `min-width`.

Lorsque une propriété `max-width` est passée dans une requête média, CSS l'interprète comme une largeur commençant à zéro – c'est-à-dire si aucune propriété de largeur minimale n'a encore été définie. Nous en arriverons là bientôt.

Une fois que la propriété `max-width` reçoit une valeur qui lui est assignée, tous les styles à l'intérieur de cette requête média particulière seront appliqués à tout appareil dont la taille d'écran s'étend de `0px` à la largeur maximale spécifiée.

La propriété `min-width`, en revanche, prend la valeur initiale que vous lui avez assignée et applique les styles à l'intérieur de la règle média jusqu'à ce que le `max-width` suivant soit fourni. Par exemple :

```css
@media only screen and (min-width: 576px) {
    // appliquer les styles ici à partir de cette largeur minimale de
    // 576px (appareils de taille moyenne)
}
```

Les styles écrits dans la requête média ci-dessus ne seront applicables qu'aux appareils dont la largeur est supérieure ou égale à la largeur minimale spécifiée.

## Comment définir la plage de largeur pour une requête média

La méthode que nous venons de discuter pour créer des requêtes média en appliquant une seule propriété de `width` ne résout qu'un seul problème.

En définissant une "plage de largeur", vous avez une certaine flexibilité lors de la création de mises en page qui vous donne une réactivité sur toutes les largeurs d'appareils.

Définir une "plage de largeur" particulière n'est pas différent de la manière dont les requêtes média sont créées. La seule différence est l'ajout de plus d'expressions de fonctionnalités média (c'est-à-dire les tailles de largeur d'écran).

Regardez :

```css
@media only screen and (min-width: 360px) and (max-width: 768px) {
	// faire quelque chose dans cette plage de largeur.
}
```

La requête média ci-dessus ne fonctionnera que pour l'expression de fonctionnalité (la taille d'écran de l'appareil mobile pour lequel vous écrivez un style) fournie ci-dessus.

Elle prend la première expression de largeur fournie comme valeur initiale et la seconde comme valeur finale.

Vous vous souvenez de la différence entre la propriété `max-width` et `min-width` que nous avons vue ci-dessus ? Nous disons simplement au navigateur d'appliquer les styles CSS que nous écrirons à l'intérieur de cette règle aux appareils mobiles avec des tailles d'écran de `360px` à `768px`.

En termes simples, nous créons des mises en page qui seront réactives des petites largeurs d'appareils aux largeurs moyennes, comme les tablettes ou les appareils mobiles.

Vous pouvez consulter certains points de rupture média disponibles dans la [documentation de Bootstrap](https://getbootstrap.com/docs/5.0/layout/breakpoints/). Essayez de jouer avec eux en définissant les plages de tailles d'écran que vous préférez.

## Essayez les requêtes média avec Flexbox

Vous avez vu comment créer une requête média de base qui prend en compte plusieurs expressions de tailles d'écran. Et vous avez vu la différence entre les propriétés `max-width` et `min-width` et comment les appliquer.

Dans cette section, nous allons voir comment créer une mise en page simple dont l'apparence change à différents points de rupture média (tailles d'écran). Nous commencerons par créer le balisage qui contiendra la mise en page.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Exemple de requête média</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="container">
      <div class="boxes box1">
        <h1>Première boîte</h1>
        <p>
		Informations dans la première boîte
        </p>
      </div>
      <div class="boxes box2">
        <h1>Deuxième boîte</h1>
        <p>
          Informations dans la deuxième boîte
        </p>
      </div>
  </body>
</html>

```

L'extrait ci-dessus affichera deux boîtes avec leurs informations respectives lorsque les styles seront appliqués. Vous pouvez consulter l'exemple de code complet [ici](https://gist.github.com/Caleb335/ed730da8fb43af4d29b0a1368f5e112b), si vous le souhaitez.

```css
.container {
  display: flex;
  flex-wrap: wrap;
  width: 980px;
  margin: 0 auto;
  margin-top: 40px;
}

@media only screen and (min-width: 320px) and (max-width: 576px) {
  .container {
    width: 100%;
    padding-left: 23px;
    flex-direction: column-reverse;
  }
  .boxes {
    width: 100%;
  }
}
```

En regardant le fichier CSS, vous remarquerez que la requête média a une largeur minimale de `320px` et une largeur maximale de `576px`. Cela signifie simplement que tous les styles qui iront dans cette règle ne seront applicables qu'aux appareils avec des largeurs extra-petites et petites.

La mise en page des boîtes change également dans cette plage de largeur particulière. Cela est dû au fait que le sélecteur `.container` a sa propriété `flex-direction` changée de `row` à `column-reverse`.

Vous pouvez décider d'expérimenter avec les autres valeurs qui peuvent être assignées à la propriété `flex-direction`. Consultez-les [ici](https://www.w3schools.com/cssref/css3_pr_flex-direction.asp).

## Conclusion

Sans définir une plage de largeur, les styles CSS de l'extrait [ci-dessus](#max-width-et-min-width) seront appliqués à tous les appareils avec une taille d'écran minimale de `576px` et plus.

Lorsque vous définissez une plage de largeur, vous obtenez un meilleur contrôle en tant que développeur. Vous serez en mesure de spécifier quels styles doivent être appliqués à un appareil avec une taille d'écran particulière, ce qui donne à votre application une meilleure réactivité.

Merci d'avoir lu cet article. N'hésitez pas à le partager s'il vous a aidé à comprendre pourquoi vous devriez définir des plages de largeur lors de la création de requêtes média.