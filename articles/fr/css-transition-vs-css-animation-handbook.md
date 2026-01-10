---
title: Guide CSS Transition vs Animation – Comment animer des éléments en CSS
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-09-12T00:20:36.000Z'
originalURL: https://freecodecamp.org/news/css-transition-vs-css-animation-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/How-to-Animate-Elements-in-CSS-Cover.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: handbook
  slug: handbook
- name: transitions
  slug: transitions
seo_title: Guide CSS Transition vs Animation – Comment animer des éléments en CSS
seo_desc: "CSS transitions and animations provide smooth, gradual ways to change an\
  \ element's style. But they work in different ways.\nHere are the main distinctions\
  \ between them:\n\n    \n        \n            CSS Transition\n            CSS Animation\n\
  \        \n    \n..."
---

Les transitions et animations CSS offrent des moyens fluides et progressifs pour changer le style d'un élément. Mais elles fonctionnent différemment.

Voici les principales distinctions entre elles :

<table>
    <thead>
        <tr>
            <th>Transition CSS</th>
            <th>Animation CSS</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <ul>
                    <li>
                        Crée des transitions fluides d'une valeur CSS à une autre.
                    </li>
                    <li>
                        Vous avez besoin de déclencheurs pour exécuter les transitions CSS. Par exemple, vous pouvez utiliser la <code>:hover</code> <a href="https://codesweetly.com/css-pseudo-selectors">pseudo-classe</a> pour exécuter des transitions lorsqu'un pointeur de l'utilisateur survole un élément.
                    </li>
                    <li>
                        La transition n'a que deux états : un état initial et un état final. Vous ne pouvez pas créer d'étapes intermédiaires.
                    </li>
                    <li>Ne s'exécute qu'une seule fois.</li>
                    <li>Idéale pour les changements de style de base.</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>
                        Anime le changement de style d'une image clé CSS à une autre.
                    </li>
                    <li>Les animations CSS n'ont pas besoin de déclencheurs.</li>
                    <li>L'animation vous permet de créer plusieurs états.</li>
                    <li>
                        Vous pouvez exécuter plusieurs itérations d'animation—même à l'infini.
                    </li>
                    <li>Idéale pour les changements de style dynamiques.</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

Ce guide utilise des exemples pour expliquer les deux techniques d'animation afin que vous puissiez comprendre leurs similitudes et différences.

## Table des matières

1. [Qu'est-ce que les transitions CSS ?](#heading-quest-ce-que-les-transitions-css)
2. [Catégories des propriétés de transition CSS](#heading-categories-des-proprietes-de-transition-css)
    * [Quelles sont les propriétés de transition CSS requises ?](#heading-quelles-sont-les-proprietes-de-transition-css-requises)
    * [Qu'est-ce que la propriété CSS `transition-property` ?](#heading-quest-ce-que-la-propriete-css-transition-property)
    * [Qu'est-ce que la propriété CSS `transition-duration` ?](#heading-quest-ce-que-la-propriete-css-transition-duration)
    * [Exemples des propriétés de transition CSS requises](#heading-exemples-des-proprietes-de-transition-css-requises)
    * [Quelles sont les propriétés de transition CSS optionnelles ?](#heading-quelles-sont-les-proprietes-de-transition-css-optionnelles)
    * [Qu'est-ce que la propriété CSS `transition-timing-function` ?](#heading-quest-ce-que-la-propriete-css-transition-timing-function)
    * [Qu'est-ce que la propriété CSS `transition-delay` ?](#quest-ce-que-la-propriete-css-transition-delay)
    * [Exemples des propriétés de transition CSS optionnelles](#heading-exemples-des-proprietes-de-transition-css-optionnelles)
3. [Raccourci pour définir les propriétés de transition CSS](#heading-raccourci-pour-definir-les-proprietes-de-transition-css)
4. [Qu'est-ce que l'animation CSS ?](#heading-quest-ce-que-lanimation-css)
    * [Composants des animations CSS](#heading-composants-des-animations-css)
    * [Qu'est-ce que les @keyframes CSS ?](#heading-quest-ce-que-les-keyframes-css)
5. [Quelles sont les propriétés d'animation CSS ?](#heading-quelles-sont-les-proprietes-danimation-css)
    * [Qu'est-ce que la propriété CSS `animation-name` ?](#heading-quest-ce-que-la-propriete-css-animation-name)
    * [Qu'est-ce que la propriété CSS `animation-duration` ?](#heading-quest-ce-que-la-propriete-css-animation-duration)
    * [Qu'est-ce que la propriété CSS `animation-timing-function` ?](#heading-quest-ce-que-la-propriete-css-animation-timing-function)
    * [Qu'est-ce que la propriété CSS `animation-delay` ?](#heading-quest-ce-que-la-propriete-css-animation-delay)
    * [Qu'est-ce que la propriété CSS `animation-iteration-count` ?](#heading-quest-ce-que-la-propriete-css-animation-iteration-count)
    * [Qu'est-ce que la propriété CSS `animation-direction` ?](#heading-quest-ce-que-la-propriete-css-animation-direction)
    * [Qu'est-ce que la propriété CSS `animation-play-state` ?](#heading-quest-ce-que-la-propriete-css-animation-play-state)
    * [Qu'est-ce que la propriété CSS `animation-fill-mode` ?](#heading-quest-ce-que-la-propriete-css-animation-fill-mode)
6. [Qu'est-ce que la propriété CSS `animation` ?](#quest-ce-que-la-propriete-css-animation)
7. [Choses importantes à savoir sur les transitions et animations CSS](#heading-choses-importantes-a-savoir-sur-les-transitions-et-animations-css)
8. [Conclusion](#heading-conclusion)

Sans plus attendre, discutons des transitions CSS.

## Qu'est-ce que les transitions CSS ?

Les **transitions CSS** offrent un moyen fluide et progressif de changer la valeur d'une propriété CSS spécifique.

Ainsi, au lieu de permettre aux navigateurs de changer la valeur d'une propriété immédiatement, les transitions CSS font en sorte que le changement se produise en douceur sur une période spécifiée.

Par exemple, supposons que vous souhaitiez changer la taille d'un élément au survol. Dans ce cas, vous avez deux options :

1. Implémenter le changement sans transitions CSS.
2. Utiliser les transitions CSS pour passer en douceur de la taille initiale de l'élément à son nouvel état.

Regardons quelques exemples des deux options.

### Comment changer la taille d'une image au survol de la souris sans utiliser les transitions CSS

```css
img {
  width: 40%;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-dsymqf)

Le code ci-dessus change instantanément la taille de l'image de sa largeur initiale (`40%`) à sa nouvelle dimension (`100%`) car nous n'avons pas utilisé de transitions CSS.

Avec les transitions CSS, vous obtiendrez une expérience beaucoup plus agréable. Voyons un exemple ci-dessous.

### Comment changer la taille d'une image au survol de la souris avec les transitions CSS

```css
img {
  width: 40%;
  transition: width 3s ease-out 0.4s;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-ufwgbu)

La propriété `transition` a appliqué une transition fluide et progressive de `width: 40%` à `width: 100%` sur l'image.

## Catégories des propriétés de transition CSS

Nous avons deux catégories de propriétés de transition CSS :

* Propriétés de transition _requises_
* Propriétés de transition _optionnelles_

Discutons des deux.

### Quelles sont les propriétés de transition CSS requises ?

Les deux propriétés requises dont vous avez besoin pour créer des transitions CSS sont :

* `transition-property`
* `transition-duration`

#### Qu'est-ce que la propriété CSS transition-property ?

La propriété CSS `transition-property` spécifie la propriété CSS que vous souhaitez faire passer de son état initial à son nouvel état.

#### Qu'est-ce que la propriété CSS transition-duration ?

La propriété CSS `transition-duration` définit la durée pendant laquelle les navigateurs doivent compléter la transition de l'élément sélectionné. En d'autres termes, `transition-duration` définit le temps total de début à fin.

**Notez ce qui suit :**

* La propriété `transition-duration` n'accepte que le temps en millisecondes (ms) ou en secondes (s).
* Zéro seconde (`0s`) est la valeur par défaut de `transition-duration`. Par conséquent, aucun [événement de transition](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event) ne se produira si vous ne définissez pas de propriété `transition-duration`.
* `transition-duration` n'accepte que zéro (`0`) ou une valeur numérique positive. Les navigateurs ignoreront la déclaration de durée si vous fournissez autre chose.

### Exemples des propriétés de transition CSS requises

Voici quelques exemples des deux propriétés de transition CSS requises.

#### Comment faire passer la largeur d'un élément en trois secondes

```css
img {
  width: 40%;
  transition-property: width;
  transition-duration: 3s;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-cq27rd)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le `transition-property` indique aux navigateurs de faire passer la `width` de l'`img` de sa valeur initiale (`40%`) à son nouvel état (`100%`).
2. Nous avons utilisé la propriété `transition-duration` pour définir une durée de trois secondes (`3s`) du début à la fin de la transition.

Par conséquent, au lieu d'un changement instantané de la largeur initiale de l'image (`40%`) à sa nouvelle taille (`100%`), les navigateurs feront la transition en douceur entre l'ancien et le nouvel état en trois secondes (`3s`).

#### Comment faire passer la taille d'une police en cinq secondes

```css
p {
  font-size: 1rem;
  transition-property: font-size;
  transition-duration: 5s;
}

p:hover {
  font-size: 7rem;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-huvkzp)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le `transition-property` informe les navigateurs de faire passer la `font-size` de l'élément `p`.
2. Nous avons utilisé la propriété `transition-duration` pour définir une durée de cinq secondes (`5s`) du début à la fin de la transition.

Par conséquent, au lieu d'un changement immédiat de la taille initiale de la police du paragraphe (`1rem`) à sa nouvelle taille (`7rem`), les navigateurs feront la transition en douceur entre l'ancien et le nouvel état en cinq secondes (`5s`).

Discutons maintenant des propriétés de transition CSS optionnelles.

### Quelles sont les propriétés de transition CSS optionnelles ?

Les deux propriétés de transition CSS optionnelles sont :

* `transition-timing-function`
* `transition-delay`

#### Qu'est-ce que la propriété CSS transition-timing-function ?

La propriété CSS `transition-timing-function` définit le timing d'implémentation (vitesse) de la transition de l'élément sélectionné.

En d'autres termes, le `transition-timing-function` spécifie la vitesse pour implémenter la transition à divers intervalles de sa durée.

Les valeurs que la propriété `transition-timing-function` accepte sont :

* `ease` : Commence la transition lentement. Puis, accélère et la termine lentement. `ease` est la valeur par défaut de la propriété `transition-timing-function`. Elle est équivalente à `cubic-bezier(0.25,0.1,0.25,1)`.
* `ease-in` : Commence la transition lentement avec une augmentation progressive de la vitesse. Elle est égale à `cubic-bezier(0.42,0,1,1)`.
* `ease-out` : Commence rapidement et termine la transition lentement. Elle est équivalente à `cubic-bezier(0,0,0.58,1)`.
* `ease-in-out` : Commence et termine la transition lentement. Elle est égale à `cubic-bezier(0.42,0,0.58,1)`.
* `linear` : Commence et termine la transition en utilisant une vitesse constante tout au long de la durée de la transition. Elle est équivalente à `cubic-bezier(0,0,1,1)`.
* `cubic-bezier(p1, p2, p3, p4)` : Vous permet de définir les valeurs de la [courbe cubic-bezier](https://www.cssportal.com/css-cubic-bezier-generator/).

### Qu'est-ce que la propriété CSS transition-delay ?

La propriété CSS `transition-delay` définit combien de temps le navigateur doit attendre avant de commencer la transition.

**Notez ce qui suit :**

* La propriété `transition-delay` doit être en millisecondes (ms) ou en secondes (s).
* `0s` est la valeur par défaut de `transition-delay`. Elle fait que la transition commence immédiatement à partir du moment où les navigateurs l'appliquent à un élément HTML.
* Une valeur négative fait que la transition commence immédiatement à partir du temps spécifié. Par exemple, supposons qu'un élément a une valeur `transition-delay` de `-3s`. Dans ce cas, la transition commencerait immédiatement à 3 secondes.
* Une valeur positive fait que la transition commence après que le temps de retard spécifié se soit écoulé. Par exemple, supposons qu'un élément a une valeur `transition-delay` de `3s`. Dans ce cas, la transition commencerait après un retard de 3 secondes.

### Exemples des propriétés de transition CSS optionnelles

Voici quelques exemples des deux propriétés de transition CSS optionnelles.

#### Comment faire passer la largeur d'un élément avec une vitesse ease-out

```css
img {
  width: 40%;
  transition-property: width;
  transition-duration: 3s;
  transition-timing-function: ease-out;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-tqzgmf)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le `transition-property` informe les navigateurs de faire passer la largeur de l'élément `img`.
2. Nous avons utilisé la propriété `transition-duration` pour définir une durée de trois secondes (`3s`) du début à la fin de la transition.
3. Nous avons utilisé la propriété `transition-timing-function` pour commencer la transition rapidement et la terminer lentement.

#### Comment faire passer la largeur d'un élément avec une vitesse linéaire

```css
img {
  width: 40%;
  transition-property: width;
  transition-duration: 3s;
  transition-timing-function: linear;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-1gqwai)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le `transition-property` informe les navigateurs de faire passer la largeur de l'élément `img`.
2. Nous avons utilisé la propriété `transition-duration` pour définir une durée de trois secondes (`3s`) du début à la fin de la transition.
3. La propriété `transition-timing-function` indique aux navigateurs de faire passer de la largeur initiale de l'élément à sa nouvelle taille en utilisant une vitesse de transition constante tout au long.

#### Comment faire passer la largeur d'un élément avec un retard de deux secondes

```css
img {
  width: 40%;
  transition-property: width;
  transition-duration: 3s;
  transition-timing-function: linear;
  transition-delay: 2s;
}

img:hover {
  width: 100%;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-ejjufi)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le `transition-property` informe les navigateurs de faire passer la propriété `width` de l'élément `img`.
2. Nous avons utilisé la propriété `transition-duration` pour définir une durée de trois secondes (`3s`) du début à la fin de la transition.
3. La propriété `transition-timing-function` fait passer la largeur de l'élément `img` en utilisant une vitesse de transition constante.
4. Nous avons utilisé la propriété `transition-delay` pour appliquer un retard de deux secondes (`2s`) au temps de démarrage de la transition.

Maintenant que nous connaissons les propriétés de transition CSS, nous pouvons discuter de leur définition avec une syntaxe raccourcie.

## Raccourci pour définir les propriétés de transition CSS

Nous utilisons la propriété `transition` comme raccourci pour les propriétés `transition-property`, `transition-duration`, `transition-timing-function` et `transition-delay`.

En d'autres termes, au lieu d'écrire :

```css
img {
  transition-property: width;
  transition-duration: 3s;
  transition-timing-function: linear;
  transition-delay: 2s;
}
```

Vous pouvez alternativement utiliser la propriété `transition` pour raccourcir votre code comme suit :

```css
img {
  transition: width 3s linear 2s;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-vtvbpo)

Voici la syntaxe de la propriété `transition` :

```css
transition: <property-name> <duration> <timing-function> <delay>;
```

Notez que vous pouvez utiliser la propriété `transition` pour faire passer l'état de plusieurs propriétés CSS.

**Voici un exemple :**

```css
img {
  width: 40%;
  opacity: 0.4;
  transition: width 3s linear, opacity 4s ease-out, transform 5s;
}

img:hover {
  width: 100%;
  opacity: 1;
  transform: rotate(45deg);
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-transitions/js-ajygzm)

L'extrait ci-dessus a utilisé des virgules (`,`) pour séparer chacune des propriétés de transition que nous appliquons à l'élément `img`.

Donc, maintenant que nous savons ce que sont les transitions CSS et comment elles fonctionnent, nous pouvons discuter des animations CSS.

## Qu'est-ce que l'animation CSS ?

Les **animations CSS** offrent un moyen fluide et progressif d'animer les changements de style d'un élément d'une image clé à une autre.

### Composants des animations CSS

Les animations CSS se composent de deux composants :

1. Images clés
2. Propriétés d'animation

### Qu'est-ce que les @keyframes CSS ?

Les **@keyframes** définissent les styles que vous souhaitez que les navigateurs appliquent en douceur à un élément à certains moments clés (images) spécifiés.

### Syntaxe des @keyframes CSS

Une règle CSS @keyframes [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/At-rule) se compose des éléments suivants :

1. Un mot-clé `@keyframes`
2. Le nom des `@keyframes`
3. Un bloc de zéro ou plusieurs images clés
4. Le sélecteur du moment clé de l'animation
5. Les déclarations de style du moment clé

**Voici une illustration :**

![Anatomie de la règle CSS @keyframes](https://www.freecodecamp.org/news/content/images/2023/09/css-animation-keyframes-illustration-codesweetly.png)
_Une règle CSS @keyframes se compose d'un mot-clé, d'un nom et d'un bloc d'images clés_

### Exemples de @keyframes CSS

Voici des exemples de @keyframes CSS.

#### Comment définir les images clés de `change-color`

```css
@keyframes change-color {
  /* La première image clé */
  0% {background-color: purple;}
  /* La dernière image clé */
  100% {background-color: yellow;}
}
```

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons créé la règle @keyframes nommée `change-color`.
2. Nous avons défini une image clé pour que les navigateurs l'appliquent lorsque l'animation d'un élément associé est à zéro pour cent (`0%`) de sa durée.
3. Nous avons défini une image clé pour que les navigateurs l'appliquent lorsque l'animation d'un élément associé est à cent pour cent (`100%`) de sa durée.

**Note :**

* Vous pouvez nommer vos `@keyframes` comme vous le souhaitez.
* `0%` est équivalent au mot-clé `from`. Et `100%` est le même que le mot-clé `to`. En d'autres termes, l'extrait ci-dessus est égal à ce qui suit :

```css
@keyframes change-color {
  /* La première image clé */
  from {background-color: purple;} 
  /* La dernière image clé */
  to {background-color: yellow;} 
}
```

* Les états de début et de fin d'une animation (`from` et `to`) sont optionnels.
* Supposons que vous omettiez l'état de début (`0%`) ou de fin (`100%`) d'un `@keyframes`. Dans ce cas, les navigateurs utiliseront par défaut les styles existants de l'élément pour chaque état.
* La règle importante (`!important`) ne fonctionne pas dans les images clés. Les navigateurs ignoreront toute déclaration d'image clé avec une règle `!important`.

Regardons un autre exemple.

#### Comment définir les images clés de `shape-image`

```css
@keyframes shape-image {
  0% { width: 40%; border: 5px solid blue;}
  40% { width: 70%; border: 1px solid red; border-radius: 50%;}
  75% { width: 50%; border: 30px solid green;}
  100% { width: 100%; border: 7px solid purple;}
}
```

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons créé le [ruleset](https://codesweetly.com/css-ruleset) `@keyframes` nommé `shape-image`.
2. Nous avons défini quatre images clés pour que les navigateurs les appliquent lorsque l'animation d'un élément associé est aux moments clés spécifiés.

**Astuce :** Utilisez l'interface [CSSKeyframesRule](https://developer.mozilla.org/en-US/docs/Web/API/CSSKeyframesRule) en JavaScript pour accéder aux règles CSS `@keyframes`.

Donc, maintenant que nous connaissons le ruleset CSS @keyframes, nous pouvons discuter de l'autre composant des animations CSS—_les propriétés d'animation_.

## Quelles sont les propriétés d'animation CSS ?

Les **propriétés d'animation CSS** informent les navigateurs de l'animation que vous souhaitez appliquer à un élément spécifique.

En d'autres termes, les propriétés d'animation CSS décrivent les attributs de l'animation, tels que son nom, sa durée, sa direction et son itération.

Les neuf (9) types de propriétés d'animation CSS sont :

* `animation-name`
* `animation-duration`
* `animation-timing-function`
* `animation-delay`
* `animation-iteration-count`
* `animation-direction`
* `animation-play-state`
* `animation-fill-mode`
* `animation`

Discutons de chacune maintenant.

### Qu'est-ce que la propriété CSS `animation-name` ?

La propriété CSS `animation-name` définit le nom des règles @keyframes contenant les styles que vous souhaitez appliquer à un élément spécifique.

**Voici un exemple :**

```css
div {
  width: 150px;
  height: 150px;
  animation-name: change-color;
}

@keyframes change-color {
  from {background-color: purple;}
  to {background-color: yellow;}
}
```

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. Nous avons créé le ruleset `@keyframes` de `change-color`.
3. Nous avons défini deux images clés pour que les navigateurs les utilisent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

**Astuce :** Vous pouvez utiliser le mot-clé `none` pour désactiver une animation.

### Qu'est-ce que la propriété CSS `animation-duration` ?

La propriété CSS `animation-duration` définit le temps nécessaire pour compléter un cycle d'animation.

**Notez ce qui suit :**

* La propriété `animation-duration` doit être en unités de millisecondes (ms) ou de secondes (s).
* La valeur de `animation-duration` doit être zéro ou positive. Sinon, les navigateurs ignoreront la déclaration de durée.
* Zéro seconde (`0s`) est la valeur par défaut de `animation-duration`.
* Supposons que `0s` soit la valeur de `animation-duration`. Dans ce cas, les navigateurs exécuteront toujours l'animation en déclenchant les événements [`animationStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event) et [`animationEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event). Mais la valeur de [`animation-fill-mode`](https://codesweetly.com/css-animations-explained#what-is-an-animation-fill-mode-property-in-css) déterminera si l'animation est visible. Par exemple, si vous définissez le `animation-fill-mode` sur `none`, l'animation sera invisible.

Regardons quelques exemples de la propriété `animation-duration`.

#### Comment animer le changement de couleur d'un élément en trois secondes

```css
div {
  width: 150px;
  height: 150px;
  animation-name: change-color;
  animation-duration: 3s;
}

@keyframes change-color {
  from {background-color: purple;}
  to {background-color: yellow;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-h6mb4k)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à trois secondes (`3s`).
3. Nous avons créé le [ruleset](https://codesweetly.com/css-ruleset) @keyframes de `change-color`.
4. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Par conséquent, les navigateurs créeront une animation fluide de trois secondes de la première image clé de `change-color` à sa dernière.

#### Comment animer les changements de bordure et de largeur d'une image en sept secondes

```css
img {
  animation-name: shape-image;
  animation-duration: 7s;
}

@keyframes shape-image {
  0% { width: 40%; border: 5px solid blue;}
  40% { width: 70%; border: 1px solid red; border-radius: 50%;}
  75% { width: 50%; border: 30px solid green;}
  100% { width: 100%; border: 7px solid purple;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-prumgo)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `img`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à sept secondes (`7s`).
3. Nous avons créé le ruleset @keyframes de `shape-image`.
4. Nous avons défini quatre images clés pour que les navigateurs les appliquent lorsque l'animation de l'image est aux moments clés spécifiés.

Par conséquent, les navigateurs créeront une animation fluide de sept secondes de la première image clé de `shape-image` à sa dernière.

### Qu'est-ce que la propriété CSS `animation-timing-function` ?

La propriété CSS `animation-timing-function` définit le timing d'implémentation (vitesse) d'une animation tout au long de sa durée.

En d'autres termes, la propriété `animation-timing-function` spécifie la vitesse pour implémenter l'animation à divers intervalles de sa durée.

Les valeurs que la propriété `animation-timing-function` accepte sont :

* `ease` : Commence l'animation lentement. Puis accélère et la termine lentement. `ease` est la valeur par défaut de la propriété `animation-timing-function`. Elle est équivalente à `cubic-bezier(0.25, 0.1, 0.25, 1)`.
* `ease-in` : Commence l'animation lentement avec une augmentation progressive de la vitesse. Elle est équivalente à `cubic-bezier(0.42, 0, 1, 1)`.
* `ease-out` : Commence rapidement et termine l'animation lentement. Elle est équivalente à `cubic-bezier(0, 0, 0.58, 1)`.
* `ease-in-out` : Commence et termine l'animation lentement. Elle est équivalente à `cubic-bezier(0.42, 0, 0.58, 1)`.
* `linear` : Commence et termine l'animation en utilisant une vitesse constante tout au long de la durée de l'animation. Elle est équivalente à `cubic-bezier(0, 0, 1, 1)`.
* `cubic-bezier(p1, p2, p3, p4)` : Vous permet de définir les valeurs de la [courbe de Bézier cubique](https://www.cssportal.com/css-cubic-bezier-generator/).

Regardons quelques exemples de la propriété `animation-timing-function`.

#### Comment animer le changement de largeur d'un élément en utilisant une vitesse linéaire

```css
div {
  width: 150px;
  height: 150px;
  background-color: purple;
  animation-name: change-width;
  animation-duration: 7s;
  animation-timing-function: linear;
}

@keyframes change-width {
  from {width: 50px;}
  to {width: 100%;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-tzwrdc)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à sept secondes (`7s`).
3. La fonction de timing `linear` a appliqué une vitesse constante à l'animation du `div`.
4. Nous avons créé le ruleset @keyframes de `change-width`.
5. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation du `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Par conséquent, les navigateurs créeront une animation fluide de sept secondes de la première image clé de `change-width` à sa dernière.

Regardons un autre exemple.

#### Comment animer le changement de largeur d'un élément en utilisant une vitesse ease-in-out et une vitesse linéaire

```css
div {
  width: 150px;
  height: 150px;
  color: white;
  animation-name: change-width;
  animation-duration: 7s;
}

.first-div {
  background-color: purple;
  animation-timing-function: ease-in-out;
}

.second-div {
  background-color: orange;
  animation-timing-function: linear;
}

@keyframes change-width {
  from {width: 50px;}
  to {width: 100%;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-janmqa)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à sept secondes (`7s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `first-div`.
4. La fonction de timing `linear` a appliqué une vitesse constante à l'animation du `second-div`.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque les animations des éléments `div` sont à zéro pour cent (`0%`) et cent pour cent (`100%`) de leur durée.

Par conséquent, les navigateurs créeront une animation fluide de sept secondes de la première image clé de `change-width` à sa dernière.

### Qu'est-ce que la propriété CSS `animation-delay` ?

La propriété CSS `animation-delay` définit combien de temps les navigateurs doivent attendre avant de commencer une animation.

En d'autres termes, utilisez `animation-delay` pour spécifier si l'animation doit commencer immédiatement dès le début, immédiatement à partir d'un temps spécifique, ou plus tard (après un certain retard).

**Notez ce qui suit :**

* La propriété `animation-delay` doit être en unités de millisecondes (ms) ou de secondes (s).
* `0s` est la valeur par défaut de `animation-delay`. Elle fait que l'animation commence une fois que les navigateurs l'appliquent à un élément HTML.
* Une valeur négative fait que l'animation commence immédiatement à partir du temps spécifié. Par exemple, supposons qu'un élément a une valeur `animation-delay` de `-3s`. Dans ce cas, l'animation commencerait immédiatement à 3 secondes.
* Une valeur positive fait que l'animation commence après que le temps de retard spécifié se soit écoulé. Par exemple, supposons qu'un élément a une valeur `animation-delay` de `3s`. Dans ce cas, l'animation commencerait après un retard de 3 secondes.

Regardons quelques exemples de la propriété `animation-delay`.

#### Comment animer le changement de largeur d'un élément avec un retard de quatre secondes

```css
div {
  width: 150px;
  height: 150px;
  color: white;
  animation-name: change-width;
  animation-duration: 7s;
}

.first-div {
  background-color: purple;
  animation-timing-function: ease-in-out;
}

.second-div {
  background-color: orange;
  animation-timing-function: linear;
  animation-delay: 4s;
}

@keyframes change-width {
  from {width: 50px;}
  to {width: 100%;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-iidpmk)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer aux éléments `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à sept secondes (`7s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `first-div`.
4. La fonction de timing `linear` a appliqué une vitesse constante à l'animation du `second-div`.
5. La propriété `animation-delay` a appliqué un retard de quatre secondes (`4s`) au temps de démarrage de l'animation du `second-div`.
6. Nous avons créé le ruleset @keyframes de `change-width`.
7. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque les animations des éléments `div` sont à zéro pour cent (`0%`) et cent pour cent (`100%`) de leur durée.

Par conséquent, les navigateurs retarderont l'animation du `second-div` de quatre secondes tout en commençant l'animation du `first-div` immédiatement.

Voici un autre exemple de la propriété `animation-delay`.

#### Comment animer le changement de largeur d'un élément à partir de la quatrième seconde de la séquence d'animation

```css
div {
  width: 150px;
  height: 150px;
  color: white;
  animation-name: change-width;
  animation-duration: 7s;
}

.first-div {
  background-color: purple;
  animation-timing-function: ease-in-out;
}

.second-div {
  background-color: orange;
  animation-timing-function: linear;
  animation-delay: -4s;
}

@keyframes change-width {
  from {width: 50px;}
  to {width: 100%;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-6xga4t)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer aux éléments `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à sept secondes (`7s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `first-div`.
4. La fonction de timing `linear` a appliqué une vitesse constante à l'animation du `second-div`.
5. La propriété `animation-delay` fait que l'animation du `second-div` commence à partir de la quatrième seconde de la séquence d'animation.
6. Nous avons créé le ruleset @keyframes de `change-width`.
7. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque les animations des éléments `div` sont à zéro pour cent (`0%`) et cent pour cent (`100%`) de leur durée.

Par conséquent, les navigateurs commenceront l'animation du `second-div` immédiatement à la quatrième seconde.

### Qu'est-ce que la propriété CSS `animation-iteration-count` ?

La propriété CSS `animation-iteration-count` définit le nombre de fois que les navigateurs doivent répéter une animation.

**Notez ce qui suit :**

* `1` est la valeur par défaut de `animation-iteration-count`.
* La propriété `animation-iteration-count` accepte des valeurs non entières—for exemple, `0.5` indique aux navigateurs de jouer la moitié d'un seul cycle d'animation.
* `animation-iteration-count` n'accepte _pas_ les valeurs négatives.
* Une valeur `infinite` signifie que les navigateurs doivent répéter l'animation indéfiniment.

Voici quelques exemples.

#### Comment animer le changement de largeur d'un élément avec une itération de deux cycles

```css
div {
  width: 70px;
  height: 50px;
  background-color: purple;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: 2;
}

@keyframes change-width {
  from {width: 70px;}
  to {width: 100%;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-vbcswe)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-iteration-count` indique aux navigateurs d'exécuter l'animation deux fois.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Par conséquent, les navigateurs exécuteront l'animation du `div` en deux cycles.

Voici un autre exemple de la propriété `animation-iteration-count`.

#### Comment animer le changement de largeur d'un élément avec une itération infinie

```css
div {
  width: 70px;
  height: 50px;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-p1zwk5)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-iteration-count` indique aux navigateurs d'exécuter l'animation indéfiniment.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Par conséquent, les navigateurs exécuteront l'animation du `div` indéfiniment.

### Qu'est-ce que la propriété CSS `animation-direction` ?

La propriété CSS `animation-direction` spécifie si la première itération de l'animation doit être exécutée en avant ou en arrière. Elle définit également si les navigateurs doivent alterner la direction des itérations suivantes.

Les valeurs que `animation-direction` accepte sont :

* `normal` : Joue l'animation dans le sens normal (c'est-à-dire en avant). `normal` est la valeur par défaut de `animation-direction`.
* `reverse` : Joue l'animation dans le sens inverse (en arrière).
* `alternate` : Joue le premier cycle d'animation dans le sens normal. Ensuite, alterne les itérations suivantes entre les directions arrière et avant.
* `alternate-reverse` : Joue le premier cycle d'animation dans le sens inverse. Ensuite, alterne les itérations suivantes entre les directions avant et arrière.

Voici quelques exemples.

#### Comment animer le changement de largeur d'un élément en commençant chaque cycle d'animation en arrière

```css
div {
  width: 70px;
  height: 50px;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  animation-direction: reverse;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-d2n3zt)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-iteration-count` indique aux navigateurs d'exécuter l'animation indéfiniment.
5. La propriété `animation-direction` commence chaque cycle d'animation en sens inverse (en arrière).
6. Nous avons créé le ruleset @keyframes de `change-width`.
7. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Voici un autre exemple de la propriété `animation-direction`.

#### Comment animer le changement de largeur d'un élément en alternant la direction de l'animation

```css
div {
  width: 70px;
  height: 50px;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-ld9kms)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-iteration-count` indique aux navigateurs d'exécuter l'animation indéfiniment.
5. La propriété `animation-direction` alterne la direction de l'animation de chaque cycle.
6. Nous avons créé le ruleset @keyframes de `change-width`.
7. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

### Qu'est-ce que la propriété CSS `animation-play-state` ?

La propriété CSS `animation-play-state` spécifie si le navigateur exécute ou a mis en pause une animation spécifique.

Les valeurs que la propriété `animation-play-state` accepte sont :

* `running` : Spécifie que le navigateur exécute l'animation. `running` est la valeur par défaut de `animation-play-state`.
* `paused` : Spécifie que le navigateur a mis en pause l'animation.

**Voici un exemple :**

```css
div {
  width: 70px;
  height: 50px;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}

div:hover {
  animation-play-state: paused;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-kbommn)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-iteration-count` indique aux navigateurs d'exécuter l'animation indéfiniment.
5. La propriété `animation-direction` alterne la direction de l'animation de chaque cycle.
6. Nous avons utilisé la propriété `animation-play-state` sur la [pseudo-classe](https://codesweetly.com/css-pseudo-selectors) `hover` du `div` pour mettre en pause l'animation chaque fois que les utilisateurs déplacent leur souris sur l'élément `div`.
7. Nous avons créé le ruleset @keyframes de `change-width`.
8. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

### Qu'est-ce que la propriété CSS `animation-fill-mode` ?

La propriété CSS `animation-fill-mode` définit les styles que les navigateurs doivent appliquer à un élément avant (ou après) que son animation ne s'exécute.

Les valeurs que la propriété `animation-fill-mode` accepte sont :

* `none` : Les navigateurs n'appliqueront _aucun_ style à l'élément avant ou après l'exécution de l'animation. `none` est la valeur par défaut de `animation-fill-mode`.
* `forwards` : L'élément conservera les déclarations de style de la dernière image clé lorsque l'animation se terminera. (Note : Les propriétés `animation-direction` et `animation-iteration-count` déterminent la dernière image clé.)
* `backwards` : L'élément conservera les déclarations de style de la première image clé pendant la période `animation-delay`. (Note : La propriété `animation-direction` détermine la première image clé.)
* `both` : Les navigateurs appliqueront à la fois les règles forwards et backwards. Par conséquent, les propriétés d'animation s'étendront dans les deux directions.

Voici quelques exemples.

#### Comment styliser un élément après la fin de son animation

```css
div {
  width: 70px;
  height: 50px;
  background-color: green;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-fill-mode: forwards;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-lkc7mw)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-fill-mode` indique aux navigateurs de conserver les déclarations de style de la dernière image clé lorsque l'animation se termine.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Voici un autre exemple de la propriété `animation-fill-mode`.

#### Comment styliser un élément pendant sa période de retard d'animation

```css
div {
  width: 70px;
  height: 50px;
  background-color: green;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-delay: 3s;
  animation-fill-mode: backwards;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-nfmq3r)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-fill-mode` indique aux navigateurs de conserver les déclarations de style de la première image clé pendant la période `animation-delay`.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les appliquent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

Regardons un troisième exemple de la propriété `animation-fill-mode`.

#### Comment styliser un élément pendant son retard d'animation et après l'animation

```css
div {
  width: 70px;
  height: 50px;
  background-color: green;
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-delay: 3s;
  animation-fill-mode: both;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-gbypmt)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. La propriété `animation-name` spécifie les `@keyframes` que nous souhaitons appliquer à l'élément `div`.
2. La propriété `animation-duration` définit le temps d'exécution de l'animation pour un cycle à cinq secondes (`5s`).
3. Nous avons utilisé la fonction de timing `ease-in-out` pour appliquer une vitesse de début lente et une vitesse de fin lente à l'animation du `div`.
4. La propriété `animation-fill-mode` indique aux navigateurs d'appliquer à la fois les règles forwards et backwards.
5. Nous avons créé le ruleset @keyframes de `change-width`.
6. Nous avons défini deux images clés pour que les navigateurs les utilisent lorsque l'animation de l'élément `div` est à zéro pour cent (`0%`) et cent pour cent (`100%`) de sa durée.

## Qu'est-ce que la propriété CSS `animation` ?

Nous utilisons la propriété `animation` comme raccourci pour :

* `animation-name`
* `animation-duration`
* `animation-timing-function`
* `animation-delay`
* `animation-iteration-count`
* `animation-direction`
* `animation-play-state`
* `animation-fill-mode`

En d'autres termes, au lieu d'écrire :

```css
div {
  animation-name: change-width;
  animation-duration: 5s;
  animation-timing-function: ease-in-out;
  animation-delay: 2s;
  animation-iteration-count: 3;
  animation-direction: alternate;
  animation-play-state: running;
  animation-fill-mode: both;
}
```

Vous pouvez alternativement utiliser la propriété `animation` pour raccourcir votre code comme suit :

```css
div {
  animation: 5s ease-in-out 2s 3 alternate both running change-width;
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-37ccew)

Voici la syntaxe de la propriété `animation` :

```css
animation: animation-duration animation-timing-function animation-delay animation-iteration-count animation-direction animation-fill-mode animation-play-state animation-name;
```

**Note :**

* La manière dont vous arrangez les valeurs de temps est essentielle. Les navigateurs lisent la première valeur de temps comme `animation-duration`. Et ils assignent la deuxième à `animation-delay`.
* Il est préférable de lister `animation-name` en dernier. Sinon, les navigateurs peuvent assigner la valeur de `animation-name` à d'autres propriétés.
* Vous pouvez appliquer plusieurs règles @keyframes à un élément en utilisant la propriété `animation`. Voici un exemple :

```css
div {
  width: 70px;
  height: 70px;
  background-color: green;
  animation: 
    5s ease-in-out 3s 3 alternate both change-width, 
    5s 3s infinite alternate both change-shape, 
    5s 3s infinite rotate-hue;
}

@keyframes change-width {
  from {width: 70px; background-color: purple;}
  to {width: 100%; background-color: orange;}
}

@keyframes change-shape {
  from {border-radius: 0%; border: 1px solid blue;}
  to {border-radius: 50%; border: 7px solid green;}
}

@keyframes rotate-hue {
  from {filter: hue-rotate(0deg);}
  to {filter: hue-rotate(360deg);}
}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/css-animations/js-4lyg4d)

L'extrait ci-dessus a appliqué trois règles @keyframes à l'élément `div` en utilisant des virgules (`,`) pour séparer chaque configuration de `@keyframes`.

**Note :** Nous avons utilisé la fonction [`hue-rotate()`](https://www.quackit.com/css/functions/css_hue-rotate_function.cfm) pour faire tourner les couleurs du `div`.

## Choses importantes à savoir sur les transitions et animations CSS

1. Vous ne pouvez pas animer toutes les propriétés CSS. Consultez l'article de MDN sur les [propriétés CSS animables](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties) pour voir celles que vous pouvez animer.
2. Les transitions et animations CSS sont des [opérations coûteuses](https://codesweetly.com/web-tech-terms-e#expensive-operation-computing) pour la plupart des propriétés CSS—sauf pour `opacity` et `transform`. En d'autres termes, appliquer des transitions (ou des animations) à toute propriété du modèle de boîte CSS est intrinsèquement une tâche [intensive en CPU](https://codesweetly.com/web-tech-terms-c#cpu-intensive). Par conséquent, n'animez que les propriétés `opacity` et `transform` si vous êtes préoccupé par les performances de votre page.
3. Soyez conscient des problèmes de [repeinture de mise en page](https://dzhavat.github.io/2021/02/18/debugging-layout-repaint-issues-triggered-by-css-transition.html) que les transitions CSS peuvent causer à travers l'ordre d'empilement de vos éléments.

## Conclusion

Dans cet article, nous avons discuté des différences entre les transitions et animations CSS. Nous avons également utilisé des exemples pour discuter de leur utilisation.

Merci d'avoir lu.

### Et voici une ressource utile sur React TypeScript :

J'ai écrit un livre sur la [Création de paquets NPM](https://amzn.to/3Pa4bI4) !

C'est un livre convivial pour les débutants qui vous guide de zéro à la création, au test et à la publication de paquets NPM comme un pro.

[![Livre sur la création de paquets NPM maintenant disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2023/09/creating-npm-package-banner-codesweetly.png)](https://amzn.to/3Pa4bI4)