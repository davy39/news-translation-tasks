---
title: Guide Markdown – Comment écrire des articles en langage Markdown
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2022-08-22T22:16:38.000Z'
originalURL: https://freecodecamp.org/news/markdown-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Markdown-cheatsheet.png
tags:
- name: HTML
  slug: html
- name: markdown
  slug: markdown
- name: markup
  slug: markup
seo_title: Guide Markdown – Comment écrire des articles en langage Markdown
seo_desc: 'As a developer, you have likely heard of HTML, which stands for HyperText
  Markup Language.

  And you may know that HTML is a language used to create websites – but what does
  markup mean?

  Markup languages are languages that use tags to define different ...'
---

En tant que développeur, vous avez probablement entendu parler de [HTML](https://en.wikipedia.org/wiki/HTML), qui signifie **H**yper**T**ext **M**arkup **L**anguage.

Et vous savez peut-être que HTML est un langage utilisé pour créer des sites web – mais que signifie **markup** ?

Les [langages de balisage](https://techterms.com/definition/markup_language) sont des langages qui utilisent des balises pour définir différents éléments dans un document texte. La plupart des gens sont familiers avec les **éditeurs de texte enrichi** – des programmes qui permettent aux utilisateurs d'ajouter des formats supplémentaires, des images et des liens à leurs documents.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-30.png align="left")

*Une capture d'écran de l'interface graphique du logiciel Microsoft Word (un éditeur de texte enrichi).*

Mais les langages de balisage utilisent des balises comme :

* <p> est une balise de paragraphe.
  
* <b> rend le texte en gras.
  

Il existe plusieurs langages de balisage comme [XML](https://en.wikipedia.org/wiki/XML), [HTML](https://en.wikipedia.org/wiki/HTML), et le sujet de cet article : **Markdown**.

Les développeurs utilisent généralement le Markdown pour la documentation – et il est souvent inclus dans la plupart des dépôts. Par exemple, j'ai utilisé le Markdown pour écrire cet article sur freeCodeCamp.

Alors, explorons tout ce que nous pouvons faire avec le Markdown.

**Avertissement :** Il n'existe pas d'organisme unificateur ou de spécification pour standardiser le Markdown – juste quelques bonnes pratiques largement acceptées. Donc, les résultats peuvent varier en fonction du parseur Markdown que vous utilisez pour ce guide.

# Guide Markdown

Voici quelques-unes des méthodes les plus couramment utilisées pour manipuler du texte en Markdown.

# Comment créer des en-têtes en Markdown

Il existe six niveaux d'en-têtes en Markdown, de H1 à H6. Je vais vous montrer comment ils s'affichent visuellement, ainsi que la manière de les créer en utilisant le Markdown.

Les H1 sont les plus grands et sont généralement les en-têtes "principaux", et chaque en-tête après H1 devient plus petit.

# Balise H1

`# H1 tag`

## Balise H2

`## H2 tag`

### Balise H3

`### H3 tag`

#### Balise H4

`#### H4 tag`

##### Balise H5

`##### H5 tag`

###### Balise H6

`###### H6 tag`

# Comment ajouter une emphase typographique en Markdown

Les manières courantes d'ajouter une emphase au texte sont le gras, l'italique et le barré. Combiner trop d'emphase peut rendre les mots beaucoup moins clairs, alors choisissez judicieusement comment vous souhaitez mettre en emphase chaque partie de texte.

Il existe également des notations en indice et en exposant que vous utiliserez pour écrire les noms de divers composés chimiques, par exemple. Vous pouvez également les utiliser dans le cadre de notations mathématiques.

**Comment mettre du texte en gras :**

Ajoutez des doubles astérisques autour de votre texte. Cela rendra ce texte en gras. Comme ceci : `**Texte en gras**`

*Comment mettre votre texte en italique :*

Ajoutez des astérisques simples autour de votre texte pour le mettre en italique, comme ceci : `*Italique*`

Comment <s>barrer</s> certains textes :

Si vous voulez "barrer quelque chose" dans le texte, utilisez la méthode de barré, comme ceci : `~~Barrer~~`.

### Comment écrire des indices en Markdown

Si vous voulez écrire le symbole chimique de l'eau, par exemple, vous pouvez faire un indice "2" en tapant `H~2~0`.

Cela donne : H<sub>2</sub>0.

### Comment écrire des exposants en Markdown

Disons que vous voulez écrire un exposant - ou un superscript. Vous faites cela comme ceci : `X^2^` ce qui donne : X<sup>2</sup>.

# Comment faire des listes en Markdown

Il existe plusieurs types de listes en Markdown. Par exemple, vous pouvez avoir des listes ordonnées et des listes non ordonnées.

Les listes ordonnées sont couramment utilisées lorsque vous voulez suivre des étapes dans un certain ordre (comme suivre une recette : cuire le poulet...servir le plat). Mais les listes non ordonnées fonctionnent bien pour des choses qui ne nécessitent pas d'étapes séquentielles comme une recette (une liste de courses, par exemple).

### Comment faire une liste non ordonnée en Markdown

Voici à quoi ressemble la liste non ordonnée.

* Huile de piment
  
* Riz
  
* Oignons verts
  

Et voici comment vous la créez en Markdown :

```javascript
- Huile de piment
- Riz
- Oignons verts
```

### Comment faire une liste ordonnée en Markdown

Voici à quoi ressemble la liste ordonnée.

1. Premier élément
  
2. Deuxième élément
  

Et voici comment vous la créez en Markdown :

```javascript
1. Premier élément 
2. Deuxième élément
```

# Comment créer des liens en Markdown

Les deux manières les plus courantes de lier des éléments dans des documents Markdown sont soit par des hyperliens, soit par des images. Les deux peuvent aider à rendre votre écriture beaucoup plus claire et plus éloquente, et doivent être utilisés lorsque cela est approprié.

Voici à quoi ressemble un hyperlien dans le texte :

[Site de Kealan](https://www.kealanparr.com)

Et voici comment vous créeriez ce lien en Markdown :

`[Site de Kealan](https://www.kealanparr.com)`

Vous placez le texte que vous voulez lier entre crochets (ici, "Site de Kealan"), et vous les suivez immédiatement de parenthèses contenant l'URL.

Disons que vous voulez inclure une image dans un article. Pour qu'elle apparaisse comme ceci :

![Vue de formations rocheuses naturelles formant une vallée se terminant par une route traversante avec un ciel bleu.](https://images.unsplash.com/photo-1660866838784-6c5158c0f979?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80 align="left")

Vous utilisez simplement la notation suivante :

```javascript
![Vue de formations rocheuses naturelles formant une vallée se terminant par une route traversante avec un ciel bleu.](https://images.unsplash.com/photo-1660866838784-6c5158c0f979?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80)
```

C'est similaire à un lien régulier, mais vous incluez le point d'exclamation avant les crochets.

## Comment utiliser le HTML dans le Markdown

Vous pouvez utiliser du HTML régulier dans les documents Markdown (selon le parseur utilisé).

N'hésitez donc pas à insérer tout HTML valide que vous souhaitez.

## Comment ajouter de l'espacement en Markdown

Si vous voulez ajouter une ligne horizontale pour diviser des sections d'un document, vous pouvez en faire une comme ceci :

---

En utilisant trois tirets comme ceci :

```javascript
---
```

## Comment créer des tableaux en Markdown

Les tableaux sont pratiques dans vos articles. Pour faire un tableau qui ressemble à ceci :

| Nom   | Âge |
| ---   | --- |
| Kealan| 25  |
| Jake  | 28  |

Voici la notation que vous utiliseriez :

```javascript
| Nom   | Âge |
| ----- | --- |
| Kealan| 25  |
| Jake  | 28  |
```

Le seul vrai "piège" dont vous devez être conscient lors de la création d'un tableau Markdown est de garder les barres verticales (|) alignées verticalement. Ensuite, votre tableau Markdown apparaîtra comme ci-dessus dans cet article. Une image pour rendre cela plus clair est :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-139.png align="left")

*Un tableau Markdown est affiché, avec Nom et Âge comme en-têtes et Kealan, Jake et 25 & 28 comme valeurs.*

## **Comment ajouter du code et de la syntaxe en Markdown**

Ajouter des extraits de code à votre Markdown peut être incroyablement utile si vous créez de la documentation pour les développeurs, par exemple.

Voici un exemple très simple en JavaScript, mais presque tous les langages de programmation modernes sont supportés (avec la coloration syntaxique, etc.).

```javascript
console.log('exemple de log')
```

```javascript
console.log('exemple de log')
```

Il suffit de taper les trois accents graves suivis du langage de programmation, puis d'appuyer sur Entrée pour commencer à écrire votre code. Terminez le bloc de code avec trois accents graves.

# Comment ajouter des citations en Markdown

Lorsque vous référencez le travail de quelqu'un d'autre, il est attendu et courtois de le créditer. Une manière facile de le faire est de le citer.

Si vous voulez ajouter des citations en Markdown :

> "Ceci est une citation, de quelqu'un qui est très sage" - Anonyme

Il suffit d'ajouter ce symbole, qui le rend comme la citation ci-dessus :

`> "Ceci est une citation, de quelqu'un qui est très sage" - Anonyme`

# Conclusion

J'espère que cela a été une référence utile pour vous, et que vous avez appris une nouvelle fonctionnalité de Markdown que vous n'aviez pas vue auparavant.

Il existe beaucoup plus de fonctionnalités (sans même compter toutes les variations HTML que vous pourriez créer), mais cet article a couvert les fonctionnalités les plus utilisées.