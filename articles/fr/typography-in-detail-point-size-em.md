---
title: 'Guide ultime de la typographie : Taille des caractères, Majuscules vs Minuscules,
  Tirets cadratin et demi-cadratin, et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T23:14:00.000Z'
originalURL: https://freecodecamp.org/news/typography-in-detail-point-size-em
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d4a740569d1a4ca36f3.jpg
tags:
- name: toothbrush
  slug: toothbrush
- name: typography
  slug: typography
seo_title: 'Guide ultime de la typographie : Taille des caractères, Majuscules vs
  Minuscules, Tirets cadratin et demi-cadratin, et plus'
seo_desc: 'Typography is a field that deals with the written word and how letters
  and characters are presented.

  The same letters can be styled in different ways to convey different emotions. And
  there are all kinds of tradeoffs around style versus readability.

  ...'
---

La typographie est un domaine qui traite de la présentation des mots écrits et de la manière dont les lettres et les caractères sont affichés.

Les mêmes lettres peuvent être stylisées de différentes manières pour transmettre différentes émotions. Et il existe toutes sortes de compromis entre le style et la lisibilité.

Dans cet article, nous examinerons certains des détails plus petits - mais toujours importants - liés à la typographie, comme la taille des caractères, les lettres majuscules et minuscules, les tirets cadratin et demi-cadratin, le crénage, et plus encore.

## **Taille des caractères**

La taille des caractères est une manière d'introduire une standardisation en typographie. Le point est la plus petite unité de mesure.

En typographie métallique, la taille des caractères fait référence à la hauteur du corps métallique sur lequel un caractère d'une police est coulé. En typographie numérique, le corps métallique est remplacé par une boîte invisible appelée _cadratin_. Chaque caractère s'insère dans ce cadratin ou cette boîte. **La taille du cadratin d'une police est égale à sa taille en points.**

```css
html{
  font-size:16px;
}

body{
  font-size:1em;  // 1em est égal à 16px
}
```

La taille des caractères est également utilisée pour mesurer l'interligne (hauteur de ligne), la longueur de ligne et d'autres éléments, en plus de la taille de la police.

En typographie numérique, **un point est égal à 1/72 de pouce**. Douze points font un pica. Six picas font un pouce. Une manière courante de représenter les picas et les points est la suivante :

* 1 pica = 1p
* 1 point = 1 pts ou p1
* 6 picas et 3 points = 6p3
* 7-point Open Sans avec 9 points d'interligne = 7/9 Open Sans

La taille optimale des caractères pour l'impression est généralement comprise entre 10 et 12 points, tandis que pour le web, la taille optimale est comprise entre 15 et 25 points.

En CSS, vous devriez définir la taille de la police en ems ou en rems plutôt qu'en pixels, car les premiers sont scalables par nature. Récemment, il y a eu beaucoup de discussions sur la typographie fluide en utilisant les nouvelles unités vw et vh.

En savoir plus ici : [Typography fluide](https://www.smashingmagazine.com/2016/05/fluid-typography/)

Rappelez-vous, différentes polices définies à la même taille de point n'auront pas l'air d'être de la même taille en raison de leurs caractéristiques individuelles, à savoir la hauteur des x, la modulation des traits ou le contraste et la largeur des caractères.

## **Majuscules et minuscules**

Les majuscules (UC) sont également appelées capitales. Il s'agit d'une police de caractères plus grands. Les minuscules (LC) sont une police de petits caractères. Tant que la touche Maj n'est pas enfoncée et que le verrouillage des majuscules n'est pas actif, tout ce qui est tapé est en minuscules. Les majuscules et minuscules sont souvent synonymes de majuscules et minuscules.

De nombreuses langues ont deux représentations écrites différentes de leurs lettres, **majuscules** et **minuscules**, également connues sous le nom de formes majuscules et minuscules.

Les lettres majuscules et minuscules sont souvent mélangées dans le même texte. L'utilisation des cas est décidée par la grammaire, mais une variété de [styles de casse](https://en.wikipedia.org/wiki/Letter_case#Case_styles) existe également. Certains styles de casse sont courants en programmation informatique, appelés [conventions de nommage](https://guide.freecodecamp.org/javascript/naming-convention-for-javascript), comme CamelCase et snake_case.

## **Majuscules :**

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

## **Minuscules :**

a b c d e f g h i j k l m n o p q r s t u v w x y z

La capitalisation est importante pour les raisons suivantes :

* Mots de passe : les mots de passe sont sensibles à la casse, donc la capitalisation ajoute un niveau de sécurité supplémentaire.
* Mesures : Lors de la manipulation de mesures informatiques et d'autres mesures, la capitalisation est importante pour identifier le type exact de mesure. Par exemple, "Mb" (abréviation de Megabit) et "MB" (abréviation de Megabyte) sont deux types de mesures différents avec des valeurs différentes.
* Commandes
* Noms de fichiers, répertoires et chemins.

## **Cadratins et demi-cadratins**

Les cadratins et demi-cadratins sont une forme de marque de ponctuation appelée "tiret". Bien qu'ils soient similaires en apparence à un trait d'union, ils servent à des fins différentes.

### **Tiret cadratin**

Utilisez un tiret cadratin pour indiquer une pause dans la phrase. Substituez-le à une virgule ou pour indiquer une pause dans une phrase. Ils sont également utilisés pour attribuer une citation à un locuteur. Un tiret cadratin a une largeur d'un cadratin—la largeur d'une taille de point d'une police. Ne mettez aucun espace avant et après un tiret cadratin.
Par exemple : Le bruit de la maison du voisin—ça me tue.

* Commande pour un tiret cadratin sur un mac : Shift-Option-Tiret
* Commande pour un tiret cadratin sur Microsoft Word : Alt + Ctrl + (moins)
* Tiret cadratin en HTML : `&mdash;` ou `&#8212;`

### **Tiret demi-cadratin**

Utilisez un tiret demi-cadratin comme remplacement du mot "à" ou pour indiquer une plage de nombres. Un tiret demi-cadratin a la moitié de la largeur d'un tiret cadratin. Ne mettez aucun espace avant et après un tiret demi-cadratin.
Par exemple : La première guerre mondiale a duré de 1914–1918.

* Commande pour un tiret demi-cadratin sur un mac : Option-Tiret
* Commande pour un tiret demi-cadratin sur Microsoft Word : Ctrl + (moins)
* Tiret demi-cadratin en HTML : `&ndash;` ou `&#8211;`

## **Crénage et approche**

Le crénage fait référence à l'espacement entre deux caractères individuels dans un mot.

L'approche fait référence à l'espacement entre les mots.

Certaines polices ne sont pas conçues pour être crénées ou approchées trop lâchement et vice versa. Si l'on crène ou approche trop serré ou trop lâche, on risque de sacrifier la lisibilité et la lisibilité.

Lors de la décision de la manière de crénage ou d'approche de votre texte, il est conseillé de considérer d'abord l'échelle à laquelle le texte sera interactif. Si le texte doit être imprimé, à quelle distance du texte imprimé se trouvera le lecteur ? Sera-t-il en train de conduire ? Sera-t-il lu sur un écran rétroéclairé ?

On devrait également considérer le positif et le négatif lors de l'approche et du crénage. Une approche trop serrée ou trop lâche peut entraîner des relations figure/fond maladroites qui distrairont l'utilisateur.

## **Lisibilité et lisibilité**

### **Lisibilité**

**Lisibilité** signifie être capable de différencier les différents caractères dans un texte. Un texte lisible implique qu'il peut être facilement interprété. Regardez les caractéristiques uniques d'une police lors de la considération de la lisibilité. Certaines des considérations sont les suivantes :

* Vous devriez utiliser chaque police selon son _contexte et son usage prévu_. Étudiez son histoire et ses meilleurs cas d'utilisation. Par exemple : Garamond est mieux utilisé pour de grands corps de texte imprimés tandis que Georgia est mieux pour l'écran.
* Gardez à l'esprit si la police est pour le _texte d'affichage ou le texte de corps_.
* La hauteur des x d'une police est la taille du 'x' minuscule dans une police. Une police avec une _hauteur des x moyenne à élevée_ donne un texte lisible même à petites tailles.
* Conventionnellement, les polices **serif** sont plus lisibles pour le texte de corps que leurs homologues sans serif.

### **Lisibilité**

**Lisibilité** signifie organiser des groupes de mots ou des blocs de texte de manière à rendre le texte plus accessible. L'idée est de réduire la quantité d'effort nécessaire pour lire un corps de texte.

Stephen Coles remarque que la lisibilité ne pose pas seulement la question de "Pouvez-vous le lire ?" mais aussi **"Voulez-vous le lire ?"**.

Jason Santa Maria souligne dans son livre _On Web Typography_ que la lecture n'est pas une activité linéaire. Nous lisons dans un mouvement de va-et-vient appelé **saccades**, qui est le mouvement de nos yeux sautant d'un point à un autre. De plus, un texte avec des mots familiers le rend plus facile à lire. Voici quelques points de base à retenir lors de la considération de la lisibilité :

* **Contraste** fait référence au changement d'épaisseur du trait dans différentes parties de la lettre. Plus le contraste est élevé, plus le changement de trait est important. Utilisez des polices de contraste moyen à faible pour de longs corps de texte.
* **Hauteur de ligne** fait référence à la distance entre deux lignes de texte. Vous ne voulez pas rendre le bloc de texte ni trop serré ni trop lâche. Vous pouvez contrôler la hauteur de ligne en CSS avec la propriété 'line-height'. Pour la plupart des textes, vous pouvez la définir entre 1,2 et 1,5 (sans unités).
* **Longueur de ligne** (mesure) fait référence au nombre moyen de caractères dans une ligne de texte. Une grande longueur de ligne entrave la lisibilité en rendant difficile pour nos yeux de scanner le texte. Habituellement, environ 45 à 75 caractères par ligne est optimal pour un corps de texte. Si vous prévoyez d'augmenter la longueur de ligne au-delà de cela, pensez également à augmenter la hauteur de ligne afin qu'il y ait suffisamment d'espace entre deux lignes de texte. En CSS, vous pouvez définir la largeur du conteneur, et en utilisant l'unité em, vous pouvez vous approcher d'un nombre défini de caractères, en fonction du rapport largeur/hauteur de la police. Exemple : width: 35em;
* **Approche** fait référence à l'ajustement de l'espace entre les caractères dans un texte. Ajouter de l'approche signifie ajouter de l'espace blanc entre les caractères et vice versa. À petites tailles de police, c'est-à-dire moins de 10 pts, ajouter de l'approche aide à améliorer la lisibilité. De même, pour les grands titres, utilisez une approche négative pour rapprocher les lettres. Vous pouvez contrôler l'approche en CSS via la propriété 'letter-spacing'. Par exemple : letter-spacing: 0.05em;
* **Taille de la police** fait référence à la taille de la police utilisée dans un texte. Pour l'affichage mobile, utilisez des tailles d'au moins 12px. Vous pouvez contrôler la taille de la police en CSS via la propriété 'font-size'. Exemple : font-size: 48px;

Comme vous pouvez le voir, vous devez prendre en compte de nombreux facteurs pour assurer une lisibilité et une lisibilité optimales. Rappelez-vous, il n'y a pas de règles strictes pour aucun des facteurs décrits ci-dessus. Ce sont de simples directives qui pourraient vous aider à mieux entraîner votre œil typographique.

## **Couleur et valeur tonale**

En théorie des couleurs, une valeur tonale est produite en ajoutant du blanc, du gris ou du noir à une couleur sélectionnée. Cela ne change pas la teinte mais modifie la saturation. Lors de la discussion sur la valeur tonale, il y a trois termes principaux qui doivent être discutés : Teinte, Ton et Ombre.

La teinte est l'ajout de blanc à une couleur. La teinte peut être utilisée pour mettre en évidence une zone ainsi que pour commencer à créer l'illusion de profondeur sur un objet.

Le ton est l'ajout de gris à une couleur. La couleur tonale crée une couleur plus sourde et moins saturée.

L'ombre est l'ajout de noir à une couleur. L'ombre peut être utilisée pour assombrir une zone pour créer l'illusion de profondeur sur un objet.

En modifiant la valeur tonale d'une couleur, vous pouvez créer l'illusion de profondeur dans les images ainsi que modifier le niveau de saturation pour mieux appliquer la couleur pour une émotion ou une humeur souhaitée.

## Plus sur la typographie :

* [Anatomie des formes de lettres en typographie](https://www.freecodecamp.org/news/typography-anatomy-of-letterforms/)
* [Grille de 8 points : typographie sur le web](https://www.freecodecamp.org/news/8-point-grid-typography-on-the-web-be5dc97db6bc/)
* [Pourquoi la typographie peut faire ou défaire votre design](https://www.freecodecamp.org/news/typography-can-make-your-design-or-break-it-7be710aadcfe/)