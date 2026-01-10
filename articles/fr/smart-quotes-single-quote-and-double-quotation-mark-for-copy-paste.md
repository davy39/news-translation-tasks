---
title: Guillemets typographiques – Guillemet simple et double pour copier + coller
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-10T14:31:24.000Z'
originalURL: https://freecodecamp.org/news/smart-quotes-single-quote-and-double-quotation-mark-for-copy-paste
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/smartQuotes-1.png
tags:
- name: HTML
  slug: html
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: Guillemets typographiques – Guillemet simple et double pour copier + coller
seo_desc: "Smart quotes are commonly used punctuation marks in HTML and in writing.\
  \ Knowing how to use them correctly can make a significant difference in the clarity\
  \ and professionalism of your writing. \nSo in this article, you will get access\
  \ to the commonly ..."
---

Les guillemets typographiques sont des signes de ponctuation couramment utilisés en HTML et en rédaction. Savoir comment les utiliser correctement peut faire une différence significative dans la clarté et le professionnalisme de votre écriture.

Dans cet article, vous aurez donc accès aux guillemets couramment utilisés que vous pourrez copier et coller dans vos articles, documents et HTML.

Mais ce n'est pas tout. Vous aurez également accès aux caractères Unicode, aux entités HTML et CSS de tous les guillemets typographiques. Assurez-vous de consulter la fin de cet article pour apprendre à utiliser les entités HTML et CSS ainsi que les caractères Unicode des guillemets typographiques.

Avant de vous montrer un tableau contenant tous les guillemets typographiques, voyons d'abord comment les utiliser en HTML et CSS.


## Ce que nous allons couvrir
- [Comment utiliser les guillemets typographiques (guillemets) en HTML et CSS](#heading-comment-utiliser-les-guillemets-typographiques-guillemets-en-html-et-css)
- [Tableau des guillemets typographiques, leurs caractères Unicode, codes HTML et CSS](#heading-tableau-des-guillemets-typographiques-leurs-caracteres-unicode-codes-html-et-css)
- [Conclusion](#heading-conclusion)

## Comment utiliser les guillemets typographiques (guillemets) en HTML et CSS
Pour utiliser les guillemets typographiques en HTML et CSS, vous avez besoin de leurs caractères Unicode. Par exemple, le code Unicode pour les guillemets est `U+0022`. Ainsi, pour l'utiliser en HTML, retirez la partie `U+`, faites précéder les autres lettres ou chiffres par `&#x`, et terminez par un point-virgule (`;`) comme ceci :

```bash
&#x0022;
```

Cela se traduit par ceci : &#x0022;

En CSS, vous devez à nouveau retirer la partie `U+` et la remplacer par une barre oblique inverse (`\`). Voici donc comment utiliser un guillemet en CSS :

```bash
\0022
```

Mais il y a un piège à l'utilisation des caractères Unicode en CSS. Pour les rendre visibles sur une page web, vous devez créer un pseudo-élément et faire en sorte que le caractère Unicode soit le contenu :

```css
element::after {
  content: '\0022';
}
```

## Tableau des guillemets typographiques, leurs caractères Unicode, codes HTML et CSS
Le tableau ci-dessous contient les guillemets disponibles pour une utilisation en HTML et autres écrits :

| Nom du guillemet | Symbole | Unicode | Code HTML | Code CSS | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Guillemet   | `"` | `U+0022` | `&#x0022` | `\0022`  | 
| Guillemet simple inversé haut | `` | `U+201B` | `&#x201B` | `\201B` |
| Guillemet double inversé haut | `` | `U+201F` | `&#x201F` | `\201F` |
| Guillemet pleine largeur | `` | `U+FF02` | `&#xFF02` | `\FF02` |
| Guillemet simple droit | `` | `U+2019` | `&#x2019` | `\2019` |
| Guillemet simple gauche | `` | `U+2018` | `&#x2018` | `\2018` |
| Guillemet simple bas | `` | `U+201A` | `&#x201A` | `\201A` |
| Guillemet double prime | ``   | `U+301E` | `&#x301E` | `\301E` |
| Guillemet double prime inversé | `` | `U+301D` | `&#x301D` | \301D|
| Guillemet double prime bas | `` | `U+301F` | `&#x301F` | `\301F` |
| Guillemet double droit | `` | `U+201D` | `&#x201D` |`\201D`|
| Guillemet double gauche |`` | `U+201C` | `&#x201C` | `\201C` |
| Guillemet double bas | `` | `U+201E` | `&#x201E` | `\201E` |
| Guillemet double bas inversé | `` | `U+2E42` | `&#x2E42` | `\2E42` |
| Ornement de guillemet double angle pointant à droite lourd | `` | `U+276F` | `&#x276F` | `\276F` |
| Ornement de guillemet double angle pointant à gauche lourd | `` | `U+276E` | `&#x27CE` | `\27CE` |
| Guillemet simple angle pointant à droite  | `
` | `U+203A` | `&#x203A` | `\203A` |
| Guillemet simple angle pointant à gauche | `	` | `U+2039` | `&#x2039` | `\2039` |
| Ornement de guillemet simple virgule basse lourde | `` | `U+275F` | `&#x275F` | `\275F` |
| Ornement de guillemet simple virgule lourde | `` | `U+275C` | `&#x275C` | `\275C` |
| Ornement de guillemet simple virgule tournée lourde | `` | `U+275B` | `&#x275B` | `\275B` |
| Ornement de guillemet double virgule tournée lourde | `` | `U+275D` | `&#x275D` | `\275D` |
| Ornement de guillemet double virgule lourde | `` | `U+275E` | `&#x275E` | `\275E` | 
| Guillemet double angle pointant à droite | `` | `U+00BB` | `&#x00BB` | `\00BB` |
| Guillemet double angle pointant à gauche | `
` | `U+00AB` | `&#x00AB` | `\00AB` |
| Apostrophe pleine largeur | `` | `U+FF07` | `&#xFF07` | `\FF07` |

Remarque : si vous avez un Mac, vous ne pourrez peut-être pas voir le "guillemet double bas inversé" et le "guillemet simple virgule basse lourde". Voici à quoi ils sont censés ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-10-at-7.20.26-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-10-at-7.20.35-AM.png)

## Conclusion

J'espère que cet article vous aide à en savoir plus sur les guillemets typographiques disponibles et comment les utiliser dans vos fichiers HTML et CSS, ainsi que dans d'autres écrits.

Essayez de partager l'article avec vos amis et votre famille afin qu'ils puissent également avoir accès aux guillemets typographiques.

Merci.