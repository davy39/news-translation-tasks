---
title: Comment optimiser votre code CSS pour des pages web plus rapides
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-01-26T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-your-css-code-for-faster-web-pages
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/csstitle.png
tags:
- name: CSS
  slug: css
- name: web performance
  slug: web-performance
seo_title: Comment optimiser votre code CSS pour des pages web plus rapides
seo_desc: 'CSS is more than just a tool for styling. It also determines how web pages
  render in a browser. Well-optimized CSS means faster loading times and a smoother
  user experience.

  In today''s digital landscape, the performance of a website is a key factor i...'
---

Le CSS est bien plus qu'un simple outil de stylisation. Il détermine également comment les pages web sont rendues dans un navigateur. Un CSS bien optimisé signifie des temps de chargement plus rapides et une expérience utilisateur plus fluide.

Dans le paysage numérique actuel, la performance d'un site web est un facteur clé de son succès. Écrire un code CSS efficace peut grandement influencer la rapidité avec laquelle vos pages web se chargent, impactant tout, de l'expérience utilisateur aux classements dans les moteurs de recherche.

Ce guide explore des stratégies efficaces pour vous aider à affiner votre CSS, garantissant que votre site web non seulement a une belle apparence, mais se charge également rapidement et fonctionne de manière fluide.

## Comment le CSS affecte les performances web

Lorsque qu'un utilisateur visite une page web, le navigateur récupère le HTML structurel du site et son CSS stylistique. Il s'agit d'un ensemble d'instructions détaillées sur la manière dont chaque partie de la page web doit apparaître.

Si le CSS est rempli de trop d'informations ou est trop complexe, c'est comme donner au navigateur une énigme qui prend plus de temps à résoudre. Cela peut entraîner des temps d'attente plus longs pour les utilisateurs, ce qui peut être frustrant.

C'est là que l'art de rationaliser le CSS entre en jeu. Il ne s'agit pas seulement de nettoyer le code, mais aussi de s'assurer que le navigateur peut préparer la page web plus rapidement.

Lorsque le CSS est rendu plus léger et plus simple, c'est comme donner au navigateur une carte claire et facile à suivre. Cela rend les pages web plus rapides à charger, rendant tout plus réactif.

## 1. Écrire un CSS plus court

Lorsque vous écrivez du CSS, utilisez le principe populaire de développement logiciel Ne vous répétez pas (DRY). Cela préconise la concision et la clarté dans votre code.

Cela est important ici, car en pratique, le CSS implique de répéter des propriétés sur divers sélecteurs. L'objectif devrait être d'identifier et de consolider ces propriétés répétitives. En faisant cela, vous éliminez les redondances, conduisant à un CSS plus propre et plus facile à gérer.

Par exemple, dans le code ci-dessous, plusieurs éléments (`h1` et `h2`) partagent la même taille de police et la même couleur.

```css
h1 {
    font-size: 20px;
    color: #fff;
}
h2 {
    font-size: 20px;
    color: #fff;
}
```

Ainsi, au lieu de déclarer ces propriétés séparément pour chaque sélecteur, vous pouvez les regrouper sous une classe commune. Cela non seulement rationalise votre feuille de style, mais rend également les mises à jour futures plus faciles et moins sujettes aux erreurs.

Vous pouvez réécrire le code ci-dessus pour qu'il ressemble à ceci :

```css
h1, h2 {
    font-size: 20px;
    color: #fff;
}
```

L'utilisation de propriétés raccourcies est une autre stratégie efficace pour minimiser la taille de votre CSS, rendant votre code plus efficace. Cela vous permet également de définir plusieurs propriétés CSS liées avec une seule déclaration. Voici comment vous pouvez écrire un CSS raccourci efficace :

Lorsque tous les côtés d'un élément ont la même valeur, utilisez cette valeur unique.

```css
/* Avant le raccourci */
.same-sides {
    padding-top: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    padding-left: 15px;
}

/* Après le raccourci */
.same-sides {
    padding: 15px;
}
```

Lorsque tous les côtés d'un élément ont des valeurs différentes, utilisez les quatre.

```css
/* Avant le raccourci */
.different-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 25px;
}

/* Après le raccourci */
.different-sides {
    padding: 10px 20px 15px 25px;
}
```

Lorsque le haut/bas et la droite/gauche ont la même valeur, utilisez deux valeurs.

```css
/* Avant le raccourci */
.two-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 10px;
    padding-left: 20px;
}

/* Après le raccourci */
.two-sides {
    padding: 10px 20px;
}
```

Lorsque seules les valeurs droite/gauche sont les mêmes mais le haut et le bas ne le sont pas, utilisez trois valeurs.

```css
/* Avant le raccourci */
.three-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 20px;
}

/* Après le raccourci */
.three-sides {
    padding: 10px 20px 15px;
}
```

## 2. Utiliser des sélecteurs CSS peu profonds

Les sélecteurs CSS peu profonds sont des sélecteurs directs et concis avec moins de niveaux d'éléments imbriqués qui ne creusent pas trop profondément dans la structure HTML.

Simplifier vos sélecteurs peut considérablement accélérer le rendu de votre page web, car les sélecteurs profondément imbriqués prennent plus de temps pour les navigateurs à évaluer, ce qui entraîne un rendu de page plus lent.

Considérez l'exemple dans le code ci-dessous : attribuer des valeurs de propriétés à un sélecteur profondément imbriqué comme `header nav ul li a` est fastidieux et provoquera des retards de rendu car le navigateur a besoin de temps pour vérifier chaque niveau (header, puis nav, puis ul, et ainsi de suite) pour trouver la bonne balise **`<a>`** à styliser).

Alternativement, lui donner une classe directe `.nav-link` est simple et plus rapide pour que les navigateurs l'interprètent. Les sélecteurs de classe sont généralement plus efficaces que les balises imbriquées car le navigateur recherche simplement les éléments avec une classe et applique les styles, sans se soucier de leur position dans l'arborescence DOM.

```css
/* Moins efficace : Sélecteur profondément imbriqué */
header nav ul li a { 
   color: #000;
   font-size: 10px;
 }

/* Plus efficace : Sélecteur de classe */
.nav-link {
   color: #000;
   font-size: 10px;
}
```

## 3. Segmenter le code CSS

Segmenter votre code CSS en segments plus petits et plus ciblés, comme des fichiers séparés pour différents composants du site web et créer des styles spécifiques à chaque page, peut grandement améliorer les performances de votre site web. Cette approche non seulement facilite la recherche et l'édition de styles spécifiques, mais garantit également que les pages web ne chargent que le CSS dont elles ont besoin, évitant ainsi un volume inutile.

Les avantages clés les plus évidents sont une maintenabilité améliorée et un chargement plus rapide des pages. Les fichiers CSS plus petits sont plus faciles à gérer, un peu comme une boîte à outils bien organisée où tout est facile à trouver. Mais aussi, en chargeant uniquement le CSS essentiel pour chaque page, le navigateur a moins de travail à faire, améliorant ainsi l'expérience utilisateur.

### CSS Original

Supposons que vous avez un fichier CSS qui contient des styles pour diverses parties de votre site web :

```css
/* Styles pour la page d'accueil */
.homepage {
    background-color: #f0f0f0;
    padding: 10px;
}

/* Styles pour la page des services */
.services {
    background-color: #333;
    color: white;
}

/* Styles pour la page de contact */
.contact {
    background-color: #222;
    color: white;
    padding: 20px;
}
```

### CSS Segmenté

Maintenant, segmentons ce CSS en différents fichiers en fonction de leur objectif :

1. **Styles de la page d'accueil (homepage.css) :**

```css
.homepage {
    background-color: #f0f0f0;
    padding: 10px;
}
```

2. **Styles de la page des services (services.css) :**

```css
.services {
    background-color: #333;
    color: white;
}
```

3. **Styles de la page de contact (contact.css) :**

```css
.contact {
    background-color: #222;
    color: white;
    padding: 20px;
}
```

Chaque fichier CSS est axé sur une partie spécifique du site web. Maintenant, lorsqu'un utilisateur visite votre site web, chaque page ne charge que le CSS dont elle a besoin, améliorant ainsi les performances du site web.

## 4. Optimiser la livraison du CSS

Vous pouvez rendre vos fichiers CSS plus légers et plus rapides à charger en réduisant votre CSS, c'est-à-dire en supprimant les espaces et les lignes supplémentaires (c'est ce qu'on appelle la minification). Ensuite, vous pouvez compresser ces fichiers pour qu'ils soient plus petits et plus rapides à télécharger pour les utilisateurs.

Assurez-vous également que les styles les plus importants de votre site web se chargent en premier, afin que les gens voient votre page plus rapidement. Les autres styles peuvent se charger en arrière-plan sans ralentir les choses.

Vous pouvez également rendre votre site web plus rapide pour les personnes qui le visitent plus d'une fois, en enregistrant une partie de votre CSS dans leur navigateur (c'est ce qu'on appelle le cache). Cela signifie qu'il n'a pas besoin de se recharger à chaque visite.

De plus, si vous utilisez un CDN ou un réseau de serveurs, vos fichiers CSS peuvent être stockés dans de nombreux endroits à travers le monde pour se charger plus rapidement, peu importe où se trouvent vos utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/minifycss.png)
_Graphique comparant la taille de fichier entre un fichier CSS non minifié de 167 Ko et un fichier CSS minifié de 92 Ko_

### CSS Original

```css
/* Feuille de style principale */
/* Style de l'en-tête */
header {
  background-color: #333;
  color: white;
  padding: 10px;
}

/* Style de la navigation */
nav {
  background-color: #444;
  margin-top: 10px;
}
```

Le code CSS ci-dessus est lisible et bien commenté, mais il contient des espaces et des commentaires supplémentaires qui augmentent la taille du fichier.

### CSS Minifié

```css
header{background-color:#333;color:white;padding:10px}nav{background-color:#444;margin-top:10px;}
```

La version minifiée combine toutes les règles en une seule ligne, supprimant les espaces et les commentaires inutiles, ce qui réduit la taille du fichier pour un chargement plus rapide.

## Conclusion

Optimiser votre CSS accélère votre site web et améliore par conséquent l'expérience utilisateur globale.

En mettant en œuvre les pratiques décrites dans cet article, vous pouvez obtenir un CSS plus performant, plus efficace et plus facile à maintenir. Les économies de performance peuvent ne pas être significatives en modifiant quelques lignes, mais sur des centaines de lignes dans différentes feuilles de style, l'impact commencera à se faire sentir.

N'oubliez pas que la performance web est un processus continu. Passez régulièrement en revue et affinez votre CSS pour rester à jour avec les meilleures pratiques et les tendances émergentes.

### Ressources supplémentaires

* [MDN Web Docs sur CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Google Web Fundamentals](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency)
* [Web Performance In Action](https://www.oreilly.com/library/view/web-performance-in/9781617293771/)