---
title: HTML Arrow – Symboles Unicode pour les flèches simples et doubles, gauche et
  droite
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-17T15:35:12.000Z'
originalURL: https://freecodecamp.org/news/html-arrow-symbol-unicode-for-single-and-double-arrows-left-and-right-arrows
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/unicode-for-arrows.png
tags:
- name: HTML
  slug: html
- name: unicode
  slug: unicode
seo_title: HTML Arrow – Symboles Unicode pour les flèches simples et doubles, gauche
  et droite
seo_desc: 'By Dillion Megida

  What are Unicodes?

  Unicodes are universal characters that represent different things. These could be
  symbols, characters, scripts, and many more forms of character combinations.

  Unicodes are adopted by many platforms (mobile and web...'
---

Par Dillion Megida

## Qu'est-ce que les Unicode ?

Les Unicode sont des caractères universels qui représentent différentes choses. Il peut s'agir de symboles, de caractères, de scripts et de nombreuses autres formes de combinaisons de caractères.

Les Unicode sont adoptés par de nombreuses plateformes (mobile et web) pour rendre les caractères disponibles partout.

## Pourquoi les Unicode sont-ils utiles ?

Les Unicode sont utiles car ils fournissent une norme pour la représentation des caractères sur différents systèmes et langues. 

L'Unicode représente également des caractères spéciaux qui ne sont pas disponibles dans [ASCII](https://en.wikipedia.org/wiki/ASCII) et nous aide à créer des affichages de caractères cohérents sur diverses plateformes.

Vous pouvez également appliquer des styles (couleurs, tailles) comme vous le feriez avec d'autres caractères.

## Comment utiliser les Unicode en HTML

Vous pouvez écrire la plupart des symboles Unicode de deux manières : en utilisant la référence hexadécimale ou en utilisant le nom de l'entité.

Les références hexadécimales sont généralement difficiles à lire, mais les noms d'entités sont généralement descriptifs pour le symbole Unicode que vous souhaitez écrire.

Pour les nombres hexadécimaux, vous les écrivez entre `&#` (un esperluette et un signe de nombre) et `;` (un point-virgule) comme ceci :

```html
&#[NUMBER];
```

Pour les noms d'entités, vous les écrivez entre `&` et `;` comme ceci :

```html
&[ENTITY];
```

Cette syntaxe est nécessaire pour que HTML comprenne que les caractères que vous écrivez ne sont pas simplement du texte mais des représentations de symboles Unicode.

## Unicode pour les flèches simples et doubles gauche et droite

Maintenant que nous avons brièvement examiné ce qu'est l'Unicode et comment l'utiliser en HTML, regardons quelques exemples.

Il existe de nombreux symboles avec des représentations Unicode que vous pouvez utiliser en HTML. Pour cet article, je vais partager quatre exemples de symboles de flèches.

Il existe différents symboles de flèches et valeurs Unicode pour eux. Les flèches utilisées ici ne sont que des exemples.

### Flèche gauche

Pour la flèche simple gauche :

La référence hexadécimale est **8592** et le nom de l'entité est **larr**. En HTML, cela s'écrirait comme suit :

```html
&#8592;
<!-- ou -->
&larr;
```

Ce code imprimera ceci sur une page :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-100.png)

Pour la flèche double gauche :

La référence hexadécimale est **8647** et le nom de l'entité est **llarr** écrit comme suit :

```html
&#8647;
<!-- ou -->
&llarr;
```

Cela donnera :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-99.png)

### Flèche droite
Pour la flèche simple droite :

La référence hexadécimale est **8594** et le nom de l'entité est **rarr** écrit comme suit :

```html
&#8594;
<!-- ou -->
&rarr;
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-98.png)

Pour la flèche double droite :

La référence hexadécimale est **8649** et le nom de l'entité est **rrarr** écrit comme suit :

```html
&#8649;
<!-- ou -->
&rrarr;
```

Cela donnera :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-101.png)

Vous pouvez utiliser des représentations Unicode pour imprimer de nombreux autres symboles en HTML. Vous pouvez soit utiliser la référence hexadécimale, soit le nom de l'entité du symbole, comme je vous l'ai montré dans cet article.