---
title: Sélecteurs CSS – Aide-mémoire pour les classes, noms et sélecteurs enfants
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-29T15:22:20.000Z'
originalURL: https://freecodecamp.org/news/css-selectors-cheat-sheet-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/laura-adai-s6U7Gq93UU8-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Sélecteurs CSS – Aide-mémoire pour les classes, noms et sélecteurs enfants
seo_desc: 'CSS selectors target and select the HTML elements you want to style.

  Specifically, CSS selectors allow you to select multiple elements at once.

  They are helpful when you want to apply the same styles to more than one HTML element,
  because you will no...'
---

Les sélecteurs CSS ciblent et sélectionnent les éléments HTML que vous souhaitez styliser.

Plus précisément, les sélecteurs CSS vous permettent de sélectionner plusieurs éléments à la fois.

Ils sont utiles lorsque vous souhaitez appliquer les mêmes styles à plusieurs éléments HTML, car cela vous évite de vous répéter en écrivant les mêmes lignes de code pour différents éléments.

Les sélecteurs CSS sont également utiles lorsque vous souhaitez effectuer une modification : vous n'avez besoin de la faire qu'à un seul endroit, ce qui vous fait gagner beaucoup de temps.

Les sélecteurs CSS font partie des premières choses que vous devez apprendre lorsque vous commencez à écrire du code CSS.

Il existe de nombreux sélecteurs disponibles, ainsi que plusieurs façons différentes de les utiliser — bien plus que vous ne l'imaginez.

Cela dit, ne vous inquiétez pas : vous n'avez pas besoin de tout mémoriser.

Cet aide-mémoire couvre les sélecteurs les plus couramment utilisés que vous devez connaître pour débuter. Ajoutez-le à vos favoris pour pouvoir y revenir chaque fois que vous aurez besoin d'un rappel rapide lors de votre prochain projet de conception web.

Voici ce que nous allons aborder :

1. [Sélecteurs CSS simples](#simples)
    1. [Sélecteur universel](#universel)
    2. [Sélecteur de type](#type)
    3. [Sélecteur de classe](#classe)
    4. [Sélecteur d'ID](#id)
2. [Sélecteurs d'attributs](#attribut)
    1. [Le sélecteur `[attribute]`](#attr-1)
    2. [Le sélecteur `[attribute="value"]`](#attr-2)
    3. [Le sélecteur `[attribute^="value"]`](#attr-3)
    4. [Le sélecteur `[attribute$="value"]`](#attr-4)
    5. [Le sélecteur `[attribute*="value"]`](#attr-5)
    6. [Le sélecteur `[attribute~="value"]`](#attr-6)
4. [Sélecteur de regroupement CSS](#regroupement)
5. [Combinateurs CSS](#combinateurs)
    1. [Combinateur de descendant](#descendant)
    2. [Combinateur d'enfant direct](#enfant)
    3. [Combinateur de frère général](#frere-general)
    4. [Combinateur de frère adjacent](#frere-adjacent)
6. [Sélecteurs de pseudo-classes](#pseudo-classe)
    1. [Sélecteurs de pseudo-classes pour les liens](#liens)
    2. [Sélecteurs de pseudo-classes pour les champs](#champs)
    3. [Sélecteurs de pseudo-classes pour la position](#position)
7. [Sélecteurs de pseudo-éléments](#elements)
    1. [Le pseudo-élément `::before`](#element-1)
    2. [Le pseudo-élément `::after`](#element-2)
    3. [Le pseudo-élément `::first-letter`](#element-3)
    4. [Le pseudo-élément `::first-line`](#element-4)

## Sélecteurs CSS simples <a name="simples"></a>

Les sélecteurs vous permettent de cibler et de sélectionner des parties spécifiques de votre document à des fins de stylisation.

Les sélecteurs simples sélectionnent directement un ou plusieurs éléments :

- En utilisant le sélecteur universel, `*`.
- Basé sur le nom/type de l'élément.
- Basé sur la valeur de la classe de l'élément.
- Basé sur la valeur de l'ID de l'élément.

En apprenant comment fonctionnent les sélecteurs les plus simples, vous pourrez comprendre comment utiliser les plus complexes.

Les sélecteurs simples seront le plus souvent ceux que vous utiliserez le plus et ceux avec lesquels vous serez le plus familier si vous avez un peu d'expérience dans l'écriture de code CSS.

### Sélecteur universel CSS <a name="universel"></a>

Le sélecteur universel, également connu sous le nom de caractère générique, sélectionne tout — chaque élément du document.

Pour utiliser le sélecteur universel, utilisez le caractère astérisque, `*`.

```css
* {
    propriété: valeur;
}
```

Vous pouvez utiliser le sélecteur universel pour réinitialiser les marges internes (padding) et externes (margin) par défaut du navigateur à zéro en haut de votre fichier avant d'ajouter d'autres styles :

```css
* {
    padding: 0;
    margin:  0;
}
```

### Sélecteur de type CSS <a name="type"></a>

Le sélecteur de type CSS sélectionne tous les éléments HTML du type spécifié.

Pour l'utiliser, mentionnez le nom de l'élément HTML.

Par exemple, si vous vouliez appliquer un style à chaque paragraphe du document HTML, vous spécifieriez l'élément `p` :

```css
p {
    propriété: valeur;
}
```

Le code ci-dessus correspond et sélectionne *tous* les éléments `p` du document et les stylise.

### Sélecteur de classe CSS <a name="classe"></a>

Le sélecteur de classe correspond et sélectionne les éléments HTML en fonction de la valeur de leur classe donnée. Plus précisément, il sélectionne chaque élément du document possédant ce nom de classe spécifique.

Avec le sélecteur de classe, vous pouvez sélectionner plusieurs éléments à la fois et les styliser de la même manière sans avoir à copier et coller les mêmes styles pour chacun séparément.

Les classes sont réutilisables, ce qui en fait une bonne option pour pratiquer le développement DRY. DRY est un principe de programmation qui signifie « Don't Repeat Yourself » (Ne vous répétez pas). Comme son nom l'indique, l'objectif est d'éviter d'écrire du code répétitif autant que possible.

Pour sélectionner des éléments avec le sélecteur de classe, utilisez le caractère point, `.`, suivi du nom de la classe.

```css
.ma_classe {
    propriété: valeur;
}
```

Dans le code ci-dessus, les éléments ayant une classe `ma_classe` sont sélectionnés et stylisés en conséquence.

### Sélecteur d'ID CSS <a name="id"></a>

Le sélecteur d'ID sélectionne un élément HTML en fonction de la valeur de son attribut ID.

Gardez à l'esprit que l'ID d'un élément doit être unique dans un document, ce qui signifie qu'il ne doit y avoir qu'un seul élément HTML avec cette valeur d'ID donnée. Vous ne pouvez pas utiliser la même valeur d'ID sur un autre élément que celui-ci.

Pour sélectionner un élément avec un ID spécifique, utilisez le caractère dièse, `#`, suivi du nom de la valeur de l'ID :

```css
#mon_id {
    propriété: valeur;
}
```

Le code ci-dessus ne correspondra qu'à l'élément unique ayant la valeur d'ID `mon_id`.

Il convient de mentionner qu'il est préférable d'essayer de limiter l'utilisation de ce sélecteur et d'opter plutôt pour le sélecteur de classe. Appliquer des styles à l'aide du sélecteur d'ID n'est pas idéal car les styles ne sont pas réutilisables.

## Sélecteurs d'attributs CSS <a name="attribut"></a>

De nombreux éléments HTML possèdent des attributs.

Les attributs HTML :

- Fournissent des informations supplémentaires sur les éléments HTML.
- Sont toujours spécifiés dans la balise de début (ou d'ouverture).
- Viennent généralement par paires nom/valeur telles que `nom="valeur"`.
- La `valeur` dans une paire nom/valeur doit être entourée de guillemets.

L'un des attributs HTML les plus populaires que vous ayez pu rencontrer est l'attribut `href`, qui est ajouté à la balise d'ouverture `<a>` et spécifie l'URL vers laquelle la balise `<a>` pointe :

```html
<a href="https://www.freecodecamp.org/">Le meilleur endroit pour apprendre à coder gratuitement !</a>
```

La valeur du `href`, `https://www.freecodecamp.org/`, est l'URL vers laquelle l'utilisateur sera dirigé lorsqu'il cliquera sur le texte du lien, `Le meilleur endroit pour apprendre à coder gratuitement !`.

Le sélecteur d'attribut correspond et sélectionne les éléments HTML en fonction de la présence d'un attribut ou d'une valeur d'attribut spécifique.

Il existe différents types de sélecteurs d'attributs.

Voici quelques-uns des sélecteurs d'attributs les plus courants.

### Le sélecteur `[attribute]` <a name="attr-1"></a>

Pour utiliser le sélecteur d'attribut, utilisez une paire de crochets, `[]`, pour sélectionner l'attribut que vous souhaitez.

La syntaxe générale des sélecteurs d'attributs est la suivante :

```css
element[attribute]
```

Ce sélecteur sélectionne un élément si l'attribut donné existe.

Dans l'exemple suivant, les éléments qui possèdent l'attribut `attr` sont sélectionnés, quelle que soit la valeur spécifique de `attr` :

```css
a[attr] {
    propriété: valeur;
}
```

Dans l'exemple ci-dessus, les éléments `a` avec le nom d'attribut `attr` sont sélectionnés, peu importe la valeur de `attr`.

Cela dit, vous pouvez être plus spécifique avec votre stylisation.

### Le sélecteur `[attribute="value"]` <a name="attr-2"></a>

Vous pouvez spécifier la valeur de l'attribut en utilisant la syntaxe suivante :

```css
element[attribute="value"]
```

Ainsi, si vous souhaitez styliser les éléments `a` avec un attribut `attr` qui a une valeur **exacte** de `1`, vous feriez ceci :

```css
a[attr="1"] {
    propriété: valeur;
}
```

Ce code ci-dessus correspond aux éléments `a` où le nom de l'attribut `attr` a une valeur exacte de `1`.

### Le sélecteur `[attribute^="value"]` <a name="attr-3"></a>

Vous pouvez également spécifier que la valeur de l'attribut **commence** par un caractère spécifique en utilisant la syntaxe suivante :

```css
element[attribute^="value"]
```

Par exemple, si vous vouliez sélectionner et styliser tous les éléments `a` qui ont un attribut `attr` avec une valeur qui commence par `www`, vous feriez ceci :

```css
a[attr^="www"] {
    propriété: valeur;
}
```

Le code ci-dessus sélectionne tous les éléments `a` où le nom de l'attribut `attr` a une valeur qui commence par `www`.

### Le sélecteur `[attribute$="value"]` <a name="attr-4"></a>

Vous pouvez également spécifier que la valeur de l'attribut **se termine** par un caractère spécifique en utilisant la syntaxe suivante :

```css
element[attribute$="value"]
```

Par exemple, si vous vouliez sélectionner les éléments `a` qui ont un nom d'attribut `attr` avec une valeur qui se termine par `.com`, vous feriez ceci :

```css
a[attr$=".com"] {
    propriété: valeur;
}
```

### Le sélecteur `[attribute*="value"]` <a name="attr-5"></a>

Vous pouvez également spécifier que la valeur de l'attribut contient une sous-chaîne spécifique — ce sélecteur est connu sous le nom de sélecteur d'attribut contenant une sous-chaîne et possède la syntaxe suivante :

```css
element[attribute*="value"]
```

Dans ce cas, la chaîne `value` doit être présente dans la valeur de l'attribut, suivie de n'importe quel nombre d'autres caractères — `value` n'a pas besoin d'être un mot entier.

Par exemple, si vous vouliez sélectionner les éléments `a` qui ont un attribut `attr` avec une valeur contenant la chaîne `free`, vous feriez ceci :

```css
a[attr*="free"] {
    propriété: valeur;
}
```

Le code ci-dessus sélectionne les éléments `a` avec un nom d'attribut `attr` lorsque la chaîne `free` est présente dans la valeur de l'attribut — même en tant que sous-chaîne (une sous-chaîne est un mot à l'intérieur d'un autre mot).

Tant que la valeur de l'attribut contient `free`, alors l'élément HTML est sélectionné — cela pourrait correspondre à un attribut `attr` avec une valeur de `free`, `freeCodeCamp` ou `freediving`, par exemple.

### Le sélecteur `[attribute~="value"]` <a name="attr-6"></a>

Vous pouvez également spécifier que le sélecteur correspond à une valeur d'attribut qui contient un mot entier en utilisant la syntaxe suivante :

```css
element[attribute~= "value"]
```

Dans ce cas, la chaîne `value` doit être un mot entier.

Par exemple, si vous vouliez sélectionner les éléments `a` qui ont un nom d'attribut `attr` avec une valeur contenant le mot `free`, vous feriez ceci :

```css
a[attr~= "free"] {
    propriété: valeur;
}
```

Le code ci-dessus correspondrait à un attribut `attr` avec une valeur de `free` entourée de différents types d'espaces blancs.

Le code ne sélectionnerait pas les éléments avec une valeur `attr` de `freeCodeCamp` ou `freediving` comme vous l'avez vu dans l'exemple précédent, car `free` doit être un mot entier à lui seul — et non une sous-chaîne.

## Sélecteur de regroupement CSS <a name="regroupement"></a>

Avec le sélecteur de regroupement, vous pouvez cibler et styliser plus d'un élément à la fois.

Pour utiliser le sélecteur de regroupement, utilisez une virgule, `,`, pour regrouper et séparer les différents éléments que vous souhaitez sélectionner.

Par exemple, voici comment vous cibleriez plusieurs éléments tels que des `div`, des `p` et des `span` tous en même temps pour leur appliquer les mêmes styles :

```css
div, p, span {
    propriété: valeur;
}
```

Le code ci-dessus correspond à tous les éléments `div`, `p` et `span` de la page, et ces trois éléments partageront le même style.

## Combinateurs CSS <a name="combinateurs"></a>

Les combinateurs vous permettent de combiner deux éléments en fonction de la relation entre les éléments et de leur emplacement dans le document.

Essentiellement, vous pouvez combiner deux sélecteurs simples d'une manière qui explique la relation entre ces sélecteurs CSS. Les combinateurs sont un type de sélecteur qui spécifie et décrit la relation entre les deux sélecteurs.

Il existe quatre types de combinateurs :

- Le combinateur de descendant.
- Le combinateur d'enfant direct.
- Le combinateur de frère général.
- Le combinateur de frère adjacent.

### Combinateur de descendant <a name="descendant"></a>

Comme son nom l'indique, le combinateur de descendant ne sélectionne que les descendants de l'élément spécifié.

Essentiellement, vous mentionnez d'abord l'élément parent, laissez un espace, puis mentionnez le descendant du premier élément, qui est l'élément enfant du parent. L'élément enfant est un élément situé à l'intérieur de l'élément parent.

Prenons l'exemple suivant :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="main.css">
  <title>Document</title>
</head>
<body>
  <div>
    <h2>Je suis un titre de niveau 2</h2>
    <p>Je suis un paragraphe à l'intérieur d'un div</p>
    <span>Je suis un span</span>
    <p>Je suis un paragraphe à l'intérieur d'un div</p>
  </div>
  <p>Je suis un paragraphe à l'extérieur d'un div</p>
</body>
</html>
```

Dans l'exemple ci-dessus, le `div` est le parent, et le `h2`, le `span` et les deux `p` sont les éléments enfants car ils sont à l'intérieur du `div`. Il y a également un paragraphe à l'extérieur du `div`.

Si vous vouliez styliser uniquement les paragraphes qui sont à l'intérieur du `div`, voici ce que vous feriez :

```css
div p {
    propriété: style;
}
```

Dans l'exemple ci-dessus, seuls les deux paragraphes à l'intérieur du `div` qui contiennent le texte `Je suis un paragraphe à l'intérieur d'un div` sont stylisés. Les deux autres éléments enfants et le paragraphe à l'extérieur du `div` avec le texte `Je suis un paragraphe à l'extérieur d'un div` ne sont pas stylisés.

### Combinateur d'enfant direct <a name="enfant"></a>

Le combinateur d'enfant direct, également connu sous le nom de descendant direct, ne sélectionne que les enfants directs du parent.

Pour utiliser le combinateur d'enfant direct, spécifiez l'élément parent, puis ajoutez le caractère `>` suivi des enfants directs de l'élément parent que vous souhaitez sélectionner.

Prenons l'exemple suivant :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="main.css">
  <title>Document</title>
</head>
<body>
  <div>
    <a href="#">Je suis un lien</a>
    <a href="#">Je suis un lien</a>
    <p><a href="#">Je suis un lien à l'intérieur d'un paragraphe</a></p>
  </div>
</body>
</html>
```

Il y a un `div` qui est l'élément parent.

À l'intérieur de l'élément parent, il y a deux éléments `a` qui sont les enfants directs du `div`.

Il y a également un autre élément `a` à l'intérieur d'un élément `p`. L'élément `p` est un enfant du `div`, mais l'élément `a` à l'intérieur du paragraphe n'est *pas* un enfant direct du `div`.

Ainsi, pour accéder uniquement aux éléments `a` qui sont des enfants directs de `div`, vous feriez ceci :

```css
div > a  {
    propriété: valeur;
}
```

Le code ci-dessus correspond aux éléments `a` directement imbriqués dans l'élément `div` et qui sont des enfants immédiats.

### Combinateur de frère général <a name="frere-general"></a>

Le combinateur de frère général sélectionne les frères.

Vous pouvez spécifier le premier élément et un second qui vient après le premier. Le second élément n'a pas besoin de venir juste après le premier.

Pour utiliser le combinateur de frère général, spécifiez le premier élément, puis utilisez le caractère `~` suivi du second élément qui doit suivre le premier.

Prenons l'exemple suivant :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="main.css">
  <title>Document</title>
</head>
<body>
  <div>
    <p>Je suis un paragraphe à l'intérieur d'un div</p>
  </div>
  <p>Je suis un paragraphe à l'extérieur d'un div</p>
  <h3>Je suis un titre de niveau trois</h3>
  <p>Je suis un paragraphe à l'extérieur d'un div</p>
</body>
</html>
```

Le `div` possède un élément `p` imbriqué à l'intérieur. Cet élément `p` spécifique est un enfant de `div`.

Il y a également deux paragraphes avec le texte `Je suis un paragraphe à l'extérieur d'un div` et un élément `h3`. Ces trois éléments sont tous des frères de l'élément `div`.

Ainsi, pour sélectionner les éléments `p` qui sont des frères de l'élément `div`, vous feriez ceci :

```css
div ~ p {
    propriété: valeur;
}
```

Le code ci-dessus stylise les deux éléments `p` qui viennent après le `div`.

Il stylise même l'élément `p` qui ne vient pas directement après l'élément `div`, comme le `p` qui suit l'élément `h3`. Il le fait parce qu'il vient tout de même après le `div`.

### Combinateur de frère adjacent <a name="frere-adjacent"></a>

Le combinateur de frère adjacent est plus spécifique que le combinateur de frère général.

Ce sélecteur ne correspond qu'aux frères *immédiats*. Les frères immédiats sont les frères qui viennent juste après le premier élément.

Pour utiliser le combinateur de frère adjacent, spécifiez le premier élément, puis ajoutez le caractère `+` suivi de l'élément que vous souhaitez sélectionner et qui suit immédiatement le premier élément.

Revenons à l'exemple de la section précédente :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="main.css">
  <title>Document</title>
</head>
<body>
  <div>
    <p>Je suis un paragraphe à l'intérieur d'un div</p>
  </div>
  <p>Je suis un paragraphe à l'extérieur d'un div</p>
  <h3>Je suis un titre de niveau trois</h3>
  <p>Je suis un paragraphe à l'extérieur d'un div</p>
</body>
</html>
```

Bien que l'élément `p` qui suit l'élément `h3` soit un frère de l'élément `div`, il n'est pas un frère *direct* comme l'élément `p` qui précède le `h3`.

Ainsi, pour cibler uniquement l'élément `p` qui vient directement après le `div`, vous feriez ceci :

```css
div + p {
    propriété: valeur;
}
```

## Sélecteurs de pseudo-classes <a name="pseudo-classe"></a>

Les sélecteurs de pseudo-classes sélectionnent des éléments qui se trouvent dans un état spécifique.

Voici quelques exemples d'états dans lesquels l'élément peut se trouver :

- L'élément est survolé par le pointeur de la souris.
- L'élément est le premier de son type.
- Le lien a déjà été visité depuis ce navigateur spécifique.
- Le lien n'a *pas* encore été visité depuis ce navigateur spécifique.
- La case à cocher/le bouton radio a été coché.

Les sélecteurs de pseudo-classes commencent par deux-points, `:`, suivis d'un mot-clé qui reflète l'état de l'élément spécifié.

La syntaxe générale ressemble à ceci :

```css
element:pseudo-class-name {
    propriété: valeur;
}
```

### Sélecteurs de pseudo-classes pour les liens <a name="liens"></a>

Il existe des sélecteurs basés sur les informations d'état des liens.

Le sélecteur `:link` applique un style lorsque l'élément n'a pas encore été visité :

```css
a:link {
    propriété: valeur;
}
```

Le sélecteur `:visited` s'applique lorsque l'élément a déjà été visité dans le navigateur actuel :

```css
a:visited {
    propriété: valeur;
}
```

Le sélecteur `:hover` s'applique lorsque le pointeur de la souris survole un élément :

```css
a:hover {
    propriété: valeur;
}
```

Le sélecteur `:focus` s'applique lorsqu'un utilisateur a accédé à un élément via la touche tabulation :

```css
a:focus {
    propriété: valeur;
}
```

Le sélecteur `:active` s'applique lorsque l'élément est sélectionné après avoir été cliqué et pendant que le bouton de la souris est maintenu enfoncé :

```css
a:active {
    propriété: valeur;
}
```

### Sélecteurs de pseudo-classes pour les champs <a name="champs"></a>

Le sélecteur `:focus` que vous avez vu précédemment pour les liens est également utilisé pour les champs de saisie (inputs) :

```css
input:focus {
    propriété: valeur;
}
```

Le sélecteur `:required` sélectionne les champs qui sont obligatoires. Les champs obligatoires possèdent l'attribut `required`.

```css
input:required {
    propriété: valeur;
}
```

Le sélecteur `:checked` sélectionne les cases à cocher ou les boutons radio qui ont été cochés :

```css
input:checked {
    propriété: valeur;
}
```

Le sélecteur `:disabled` sélectionne les champs qui sont désactivés. Les champs désactivés possèdent l'attribut `disabled`. De nombreux navigateurs stylisent par défaut les champs désactivés avec une couleur grise estompée :

```css
input:disabled {
    propriété: valeur;
}
```

### Sélecteurs de pseudo-classes pour la position <a name="position"></a>

Le sélecteur de premier enfant, `:first-child`, sélectionne le premier élément, qui sera le premier enfant à l'intérieur du conteneur parent.

Par exemple, voici comment vous sélectionneriez un élément `a` lorsqu'il est le premier enfant dans le conteneur parent :

```css
a:first-child {
    propriété: valeur;
}
```

Le sélecteur de dernier enfant, `:last-child`, sélectionne le dernier élément, qui sera le dernier enfant à l'intérieur du conteneur parent.

Voici comment vous sélectionneriez un élément `a` lorsqu'il est le dernier enfant dans le conteneur parent :

```css
a:last-child {
    propriété: valeur;
}
```

Le sélecteur `:nth-child()` sélectionne un élément enfant à l'intérieur d'un conteneur en fonction de sa position dans un groupe de frères.

Il prend un entier comme argument et sélectionne un élément en fonction de la valeur donnée. La syntaxe générale du sélecteur ressemble à ceci :

```css
a:nth-child(n) {
    propriété: valeur;
}
```

Le sélecteur `:nth-child()` est utile lorsque vous souhaitez sélectionner des éléments basés sur une expression, comme la sélection d'éléments pairs ou impairs :

```css
a:nth-child(even) {
    propriété: valeur;
}
```

Le sélecteur de premier du type, `:first-of-type`, sélectionne les éléments qui sont les premiers de ce type spécifique dans le conteneur parent.

Par exemple, voici comment vous sélectionneriez le premier `p` à l'intérieur d'un `div` :

```css
p:first-of-type {
    propriété: valeur;
}
```

Le sélecteur de dernier du type, `:last-of-type`, sélectionne les éléments qui sont les derniers de ce type spécifique dans le conteneur parent.

Par exemple, voici comment vous sélectionneriez le dernier `p` à l'intérieur d'un `div` :

```css
p:last-of-type {
    propriété: valeur;
}
```

## Sélecteurs de pseudo-éléments <a name="elements"></a>

Les sélecteurs de pseudo-éléments sont utilisés pour styliser une partie spécifique d'un élément — vous pouvez les utiliser pour insérer du nouveau contenu ou modifier l'apparence d'une section spécifique du contenu.

Par exemple, vous pouvez utiliser un pseudo-élément pour styliser la première lettre ou la première ligne d'un élément différemment. Vous pouvez également utiliser des pseudo-éléments pour ajouter du nouveau contenu avant ou après l'élément sélectionné.

Contrairement aux pseudo-classes qui sont précédées d'un seul caractère `:`, les pseudo-éléments sont précédés de deux caractères `:`. 

Les caractères `::` sont suivis d'un mot-clé qui vous permet de styliser une partie spécifique de l'élément sélectionné.

La syntaxe générale ressemble à ceci :

```css
element::pseudo-element-selector {
    propriété: valeur;
}
```

Assurez-vous d'utiliser les caractères `::` au lieu de `:` lors de l'utilisation des sélecteurs de pseudo-éléments — cela aidera à distinguer les pseudo-classes des pseudo-éléments.

Voyons maintenant certains des pseudo-éléments les plus courants que vous rencontrerez.

### Le pseudo-élément `::before` <a name="element-1"></a>

Vous pouvez utiliser le pseudo-élément `::before` pour insérer du contenu avant un élément :

```css
p::before {
    propriété: valeur;
}
```

### Le pseudo-élément `::after` <a name="element-2"></a>

Et vous pouvez utiliser le pseudo-élément `::after` pour insérer du contenu à la fin d'un élément :

```css
p::after {
    propriété: valeur;
}
```

### Le pseudo-élément `::first-letter` <a name="element-3"></a>

Vous pouvez également utiliser le pseudo-élément `::first-letter` pour sélectionner la première lettre d'un paragraphe, ce qui est utile lorsque vous souhaitez styliser la première lettre d'une certaine manière :

```css
p::first-letter {
    propriété: valeur;
}
```

### Le pseudo-élément `::first-line` <a name="element-4"></a>

Et vous pouvez utiliser le pseudo-élément `::first-line` pour sélectionner la première ligne d'un paragraphe :

```css
p::first-line {
    propriété: valeur;
}
```

## Conclusion

Nous espérons que vous avez trouvé cet aide-mémoire des sélecteurs CSS les plus utilisés utile.

Pour en savoir plus sur la conception web, consultez la [Certification Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/) de freeCodeCamp. Grâce à des leçons interactives, vous apprendrez le HTML et le CSS en construisant 15 projets pratiques et 5 projets de certification.

Merci de nous avoir lu, et bon codage !