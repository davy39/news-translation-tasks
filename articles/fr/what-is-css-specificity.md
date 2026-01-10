---
title: Spécificité CSS et quand utiliser la balise CSS !important
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-11T10:09:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-css-specificity
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98bd740569d1a4ca1bc5.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Development
  slug: web-development
seo_title: Spécificité CSS et quand utiliser la balise CSS !important
seo_desc: "By Sarah Chima Atuonwu\nCSS specificity is an important topic to understand\
  \ if you want to get better at CSS. It is the set of rules applied to CSS selectors\
  \ that determines which style is applied to an element. \nTo understand this better,\
  \ it's import..."
---

Par Sarah Chima Atuonwu

La spécificité CSS est un sujet important à comprendre si vous voulez vous améliorer en CSS. Il s'agit de l'ensemble des règles appliquées aux sélecteurs CSS qui détermine quel style est appliqué à un élément.

Pour mieux comprendre cela, il est important que nous comprenions un sujet connexe : la cascade en CSS.

## La nature en cascade du CSS

CSS signifie Cascading Style Sheets. "Cascading" signifie que l'**ordre** dans lequel les règles CSS sont appliquées à un élément **a réellement de l'importance**.

Idéalement, si deux règles sont appliquées au même élément, celle qui vient en dernier est celle qui sera utilisée. Utilisons un exemple pour comprendre cela.

Nous allons appliquer deux classes à un élément et donner à chaque classe une `background-color` différente.

```text
<p class="style1 style2"> Ceci est un paragraphe de test</p>
```

Voici le CSS :

```text
.style2 {
  background-color: red;
}

.style1 {
  background-color: yellow;
}
```

Voici le résultat :

<script async src="//jsfiddle.net/sarahchima/1vpme0a8/4/embed/result,html,css/"></script>

Remarquez que le `style1`, qui vient en dernier dans la feuille de style, est appliqué à l'élément. Vous pourriez vous attendre à ce que ce soit toujours ainsi que CSS applique les styles aux éléments, mais ce n'est pas toujours le cas.

Prenons cet exemple suivant.

```text
<p class="style1" id="paragraph"> Ceci est un paragraphe de test</p>
```

Le CSS ressemble à ceci :

```text
#paragraph {
  background-color: red;
}

.style1 {
  background-color: yellow;
}
```

Quel style pensez-vous être appliqué à l'élément ? Le `#paragraph` ou le `.style1` ?

Voici le résultat :

<script async src="//jsfiddle.net/sarahchima/hxbta4k3/2/embed/result,html,css/"></script>

Remarquez que le premier est appliqué. Le `#paragraph` est un sélecteur d'ID, tandis que le `style1` est un sélecteur de classe. Cela est dû au fait que la cascade fonctionne avec la spécificité pour déterminer quelles valeurs sont appliquées à un élément.

Alors, qu'est-ce que la spécificité CSS ?

## La spécificité CSS expliquée

Selon MDN, la spécificité est le moyen par lequel les navigateurs décident quelles valeurs de propriétés CSS sont les plus pertinentes pour un élément et, par conséquent, seront appliquées.

Simplement dit, si deux sélecteurs CSS s'appliquent au même élément, celui avec la spécificité la plus élevée est utilisé.

C'est pourquoi, dans notre exemple précédent, la valeur de propriété du sélecteur d'ID a été appliquée car elle a une valeur de spécificité plus élevée.

Alors, comment les spécificités des sélecteurs sont-elles calculées ?

## La hiérarchie de spécificité

Calculer les valeurs de spécificité des sélecteurs est assez délicat. Une façon de le calculer est d'utiliser un système de poids pour classer différents sélecteurs afin de créer une hiérarchie.

Nous allons attribuer des poids à chaque sélecteur pour mieux comprendre comment chaque sélecteur est classé. Commençons par le moins spécifique.

### Éléments et pseudo-éléments

Nous utilisons des sélecteurs d'éléments comme `a`, `p` et `div` pour styliser un élément sélectionné, tandis que les pseudo-éléments comme `::after` et `::before` sont utilisés pour styliser des parties spécifiques d'un élément.

```text
<!-- Ceci est un sélecteur d'élément-->
p { 
    color: red;
}

<!-- Ceci est un sélecteur de pseudo-élément-->
p::before {
    color: red;
}
```

Les sélecteurs d'éléments et de pseudo-éléments ont la spécificité la plus faible. Dans le système de poids de spécificité, ils ont une valeur de 1.

### Classes, attributs et pseudo-classes

Voici des exemples de classes, d'attributs et de pseudo-classes :

```text
<!-- Ceci est un sélecteur de classe-->
.person { 
    color: red;
}

<!-- Ceci est un sélecteur d'attribut-->
[type="radio"] { 
    color: red;
}

<!-- Ceci est un sélecteur de pseudo-classe-->
:focus {
    color: red;
}
```

Ils ont une spécificité plus élevée que les sélecteurs d'éléments et de pseudo-éléments. Dans notre système de poids de spécificité, ils ont une valeur de 10.

### Sélecteurs d'ID

Les sélecteurs d'ID sont utilisés pour cibler un élément en utilisant l'ID de l'élément.

```text
<!-- Ceci est un sélecteur d'ID-->
#header {
    color: red;
}
```

Les sélecteurs d'ID ont une spécificité plus élevée que les classes et les éléments. Dans notre système de poids de spécificité, ils ont une valeur de 100.

### Styles en ligne

Les styles en ligne sont appliqués directement sur l'élément dans le document HTML. Voici un exemple :

```text
<p style="color: red">Ceci est un paragraphe</p>
```

Les styles en ligne ont la spécificité la plus élevée. Dans notre système de poids de spécificité, ils ont une valeur de 1000.

Voici un résumé des poids :

```text
Styles en ligne                               - 1000
Sélecteurs d'ID                                -  100
Classes, attributs et pseudo-classes           -   10
Éléments et pseudo-éléments                    -    1 
```

Essayons de comprendre cela.

Les valeurs de propriété des sélecteurs avec un poids plus élevé seront toujours appliquées par rapport à un sélecteur avec un poids inférieur.

Les styles en ligne ont le poids le plus élevé et leur valeur de propriété remplace toute autre valeur de sélecteur appliquée à un élément.

Par exemple, si nous avons un élément et pour la même propriété `color`, il y a un style en ligne. Si les sélecteurs de classe et d'ID ont également des valeurs pour la même propriété, le style en ligne l'emporte.

```text
<p style="color: red" class="yellow" id="paragraph">Ceci est un paragraphe</p>
```

La feuille de style :

```text
#paragraph {
    color: green;
}

.yellow {
    color: yellow;
}
```

Voici le résultat :

<script async src="//jsfiddle.net/sarahchima/nrmL6ygz/3/embed/result,html,css/"></script>

La même chose se produit lorsqu'un sélecteur d'ID et un sélecteur de classe ont des valeurs pour la même propriété. La valeur de propriété du sélecteur d'ID sera appliquée.

Notez que les poids ne s'appliquent que lorsque différents sélecteurs ont des valeurs pour la **même `propriété`**.

### Plusieurs sélecteurs d'éléments

Il arrive que plus d'un sélecteur soit utilisé pour cibler un élément. Par exemple, pour une liste comme celle-ci :

```text
<ul class="list">
    <li>Premier élément</li>
    <li>Deuxième élément</li>
    <li>Troisième élément</li>
</ul>
```

Vous pouvez cibler les éléments de la liste comme ceci :

```text
.list > li { 
    color: green;
}
```

ou comme ceci :

```text
ul > li {
    color: red;
}
```

Dans un cas où les deux sélecteurs sont utilisés sur la même feuille de style, quel style sera appliqué aux éléments de la liste ?

Revenons à notre système de poids pour calculer la spécificité des deux sélecteurs.

Pour `.list > li`, le poids d'un sélecteur de classe est `10` et le poids d'un sélecteur d'élément est `1`. Leur somme combinée est `11`.

Pour `ul > li`, le poids d'un sélecteur d'élément est `1`. Il y a deux sélecteurs d'éléments utilisés, donc leur somme est `2`.

Quelle valeur de couleur pensez-vous sera appliquée ?

Si vous avez dit que la couleur du sélecteur `.list>li` sera appliquée, vous avez raison. Il a une valeur de spécificité plus élevée que l'autre sélecteur.

<script async src="//jsfiddle.net/sarahchima/6xjp54yh/1/embed/result,html,css/"></script>

Essayons un autre exemple. Étant donné cet élément :

```text
<div class="first-block" id="div-1"> 
    <div class="second-block" id="div-2">
        <p class="text" id="paragraph">Ceci est un paragraphe</p>
    </div>
</div>
```

et ces styles

```text
#div-1 > .second-block > .text {
    color: blue
}

.first-block > #div-2 > #paragraph {
    color: red
}
```

Essayez de calculer la spécificité et devinez quelle valeur de `color` sera appliquée.

Voici le résultat :

<script async src="//jsfiddle.net/sarahchima/7brp4nmg/4/embed/result,html,css/"></script>

Utilisons notre système de poids pour comprendre pourquoi la valeur de couleur du deuxième sélecteur est appliquée.

Pour `#div-1 > .second-block > .text`, nous avons un sélecteur d'ID et deux sélecteurs de classe. La somme de leurs poids est `100 + 10 + 10 = 120`.

Pour `.first-block > #div-2 > #paragraph`, nous avons un sélecteur de classe et deux sélecteurs d'ID. La somme de leurs poids est `10 + 100 + 100 = 210`.

C'est pourquoi la valeur du dernier sélecteur est utilisée.

Vous pouvez essayer cet exemple par vous-même pour être sûr de bien comprendre.

```text
<div class="first-block" id="div1">
    <ul class="first-list" id="list1">
        <li class="first-list-item" id="listItem1">Premier 
            <span class="first-span" id="span1">élément</span>
        </li>
    </ul>
</div>
```

Quelle couleur sera appliquée au `span` si les styles suivants sont dans la feuille de style ?

```text
div#div1 > .first-list > #list-item > span {
    color: red;
}

#list > #list-item > #span {
    color: purple;
}

#div1 > #list > .first-list-item > .first-span {
    color: light-blue;
}
```

Essayez de calculer la spécificité et comparez-la avec le résultat que vous obtenez lorsque vous exécutez le code.

Avant de conclure cet article, il y a quelques points importants à noter.

## Points importants sur la spécificité CSS

Le poids attribué à un sélecteur nous donne une idée des règles appliquées à un élément. Cependant, cela ne suffit pas toujours.

Par exemple, vous pourriez supposer que si vous utilisez plus de 10 classes (poids >= 100) pour cibler un élément, les valeurs de propriété remplaceront celles d'un sélecteur d'ID. Mais ce n'est pas vrai. Tant que le sélecteur avec plus de 10 classes n'a pas de sélecteur d'ID, le sélecteur d'ID aura toujours la priorité.

Appliquer `!important` à la valeur de propriété de n'importe quel sélecteur en fait la valeur qui sera appliquée à l'élément. Cela se produit indépendamment du rang du sélecteur dans la hiérarchie de spécificité.

Utilisons un exemple pour comprendre cela.

```text
<p class="blue" id="paragraph" style="color: green"> Ceci est un paragraphe </p>
```

Si les styles suivants sont appliqués

```text
p {
    color: red !important;
}
.blue {
    color: blue;
}

#paragraph {
    color: purple;
}
```

La valeur du sélecteur d'élément `p` sera utilisée en raison du `!important` attaché à la valeur.

Cependant, si un autre sélecteur a la balise `!important` attachée à la même propriété, la valeur du sélecteur ultérieur est utilisée.

<script async src="//jsfiddle.net/sarahchima/2weo7cyr/4/embed/result,html,css/"></script>

C'est pourquoi `!important` doit être évité car il rend difficile la substitution d'un style.

En général, pour styliser un élément spécifique, il est plus conseillé d'utiliser une classe. Cela facilite la substitution des styles si vous devez le faire un jour.

## Résumé

De cet article, nous pouvons voir que la spécificité CSS est un sujet important à comprendre car elle peut vous faire économiser des heures de débogage.

Avec cette connaissance, vous pouvez facilement découvrir pourquoi vos styles ne sont pas appliqués.

Voici les points majeurs à retenir de cet article :

* En raison de la nature en cascade du CSS, si deux règles sont appliquées au même élément, celle qui vient en dernier est celle qui sera utilisée.
* La spécificité CSS est un ensemble de règles qui déterminent quel style est appliqué à un élément.
* Le système de poids est une façon de calculer la spécificité de différents sélecteurs. Voici un résumé des poids :

```
Styles en ligne                               - 1000
Sélecteurs d'ID                                -  100
Classes, attributs et pseudo-classes           -   10
Éléments et pseudo-éléments                    -    1 
```

* `!important` remplace tous les autres styles indépendamment de la spécificité du sélecteur où il est utilisé.

J'espère que vous avez apprécié la lecture de cet article.