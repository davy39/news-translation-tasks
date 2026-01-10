---
title: Comment fonctionnent les méthodes reduce et reduceRight en JavaScript
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-05-13T16:10:35.000Z'
originalURL: https://freecodecamp.org/news/how-reduce-reduceright-works-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/reduce-cover-with-title-3.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionnent les méthodes reduce et reduceRight en JavaScript
seo_desc: "reduce and reduceRight are two built-in JavaScript array methods that have\
  \ a bit of a steep learning curve. \nBut the very essence of these methods are as\
  \ simple as the following arithmetic computations.\nSuppose we have an array of\
  \ numbers:\n[1, 2, 3, ..."
---

`reduce` et `reduceRight` sont deux méthodes intégrées de tableau JavaScript qui ont une courbe d'apprentissage un peu raide. 

Mais l'essence même de ces méthodes est aussi simple que les calculs arithmétiques suivants.

Supposons que nous avons un tableau de nombres :

```js
[1, 2, 3, 4]
```

Et nous voulons obtenir la somme de ceux-ci.

La manière `reduce` d'obtenir la somme est similaire à :

<p style="text-align: center; font-size: 1.2em">((((1) + 2) + 3) + 4)</p>

Alors que la manière `reduceRight` d'obtenir la somme est similaire à :

<p style="text-align: center; font-size: 1.2em">((((4) + 3) + 2) + 1)</p>

Avec `reduce` et `reduceRight`, vous pouvez définir votre propre +. Les éléments du tableau peuvent être n'importe quoi aussi. Cela semble excitant, n'est-ce pas ?

Considérez `reduce` et `reduceRight` comme rien de plus qu'une généralisation des motifs arithmétiques ci-dessus. Dans cet article, nous couvrirons tous les détails importants.

Cet article adopte une approche algorithmique facile à digérer pour vous montrer comment fonctionne la réduction en JavaScript. 

J'ai également créé une vidéo pour vous montrer comment ces méthodes fonctionnent. Consultez-la si vous voulez apprendre les concepts sous un angle plus visuel :

%[https://youtu.be/o43livPsWn4]

## Table des matières

<ul
  style="
    padding-left: 0px;
    padding-block: 0.5rem;
    list-style-type: none;
    margin: 0px;
  "
>
  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >1</span
    ><a href="#quest-ce-qui-est-reduit-en-quoi">Qu'est-ce qui est réduit en quoi ? </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >2</span
    ><a href="#parametres-de-reduce-reduceright"
      >Paramètres de <code>reduce</code>/<code>reduceRight</code>
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >3</span
    ><a href="#comprendre-reduce-reduceright-avec-un-diagramme"
      >Comprendre <code>reduce</code>/<code>reduceRight</code> avec un diagramme
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >4</span
    ><a href="#lalgorithme-de-reduce-reduceright"
      >L'algorithme de <code>reduce</code>/<code>reduceRight</code>
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >5</span
    ><a href="#exercices">Exercices </a>

    <ul style="padding-left: 1.3em; list-style-type: none">
      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.1</span
        ><a href="#aplatir-un-tableau-imbrique">Aplatir un tableau imbriqué </a>
      </li>

      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.2</span
        ><a href="#supprimer-les-elements-dupliques-dun-tableau"
          >Supprimer les éléments dupliqués d'un tableau
        </a>
      </li>

      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.3</span
        ><a href="#inverser-un-tableau-sans-le-muter"
          >Inverser un tableau sans le muter
        </a>
      </li>
    </ul>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >6</span
    ><a href="#conclusion">Conclusion </a>
  </li>
</ul>


<h2 id="quest-ce-qui-est-reduit-en-quoi"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>Qu'est-ce qui est réduit en quoi ?
<a href="#quest-ce-qui-est-reduit-en-quoi" aria-label="Anchor link for: &quot;Qu'est-ce qui est réduit en quoi ?
&quot;" style="text-decoration: none;">
7</a></h2>

Vous vous demandez peut-être, "Quel type de réduction se produit lors de l'utilisation de `reduce` ou `reduceRight` ?"

Ici, la réduction reflète une manière particulière de transformer (que nous verrons en détail) les éléments d'un tableau en une seule valeur similaire aux calculs arithmétiques que nous avons vus ci-dessus. 

Mais notez que la valeur de sortie peut être n'importe quoi. Donc, elle peut être une valeur qui semble plus grande que le tableau original sur lequel la méthode est appelée.

Dans les langages de _programmation fonctionnelle_, l'idée de réduire a de nombreux [autres noms](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) tels que **fold**, **accumulate**, **aggregate**, **compress** et même **inject**.

<h2 id="parametres-de-reduce-reduceright"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>Paramètres de <code>reduce</code>/<code>reduceRight</code>
<a href="#parametres-de-reduce-reduceright" aria-label="Anchor link for: &quot;Paramètres de reduce/reduceRight
&quot;" style="text-decoration: none;">
7</a></h2>

Ces méthodes ont toutes deux les mêmes règles pour les appeler. Il est donc facile de les apprendre ensemble. Voyons comment elles peuvent être appelées :

```js
let myArray      = [/* un tableau */];
let callbackfn   = /* Une valeur de fonction */ ;
let initialvalue = /* n'importe quelle valeur */ ;

myArray.reduce(callbackfn)
myArray.reduce(callbackfn, initialValue)

myArray.reduceRight(callbackfn)
myArray.reduceRight(callbackfn, initialValue)

```

Ici, l'utilisation des paramètres de `reduce`/`reduceRight` est expliquée à travers les variables `callbackfn` et `initialValue` :

**`callbackfn`** : Il doit s'agir d'une fonction. Lors de l'itération sur le tableau, pour chaque élément, `reduce`/`reduceRight` appelle `callbackfn` avec 4 arguments. Supposons que les variables `previousValue`, `currentElement`, `index` et `array` contiennent les valeurs de ces arguments, respectivement. Ainsi, l'appel interne à `callbackfn` ressemble à ceci :

```js
callbackfn(previousValue, currentElement, index, array)

```

Maintenant, voyons la signification de ces valeurs :

1. `previousValue` : Cela est également connu sous le nom d'_accumulateur_. En bref, cette valeur représente le "travail en cours" de la valeur de retour de la méthode. Ce que cette valeur représente deviendra complètement clair lorsque vous étudierez l'algorithme présenté plus tard dans cet article.
2. `currentElement` : L'élément actuel.
3. `index` : L'index de l'élément actuel.
4. `array` : `myArray`.

**Valeur de retour de `callbackfn`** : Pour le dernier appel à `callbackfn`, sa valeur de retour devient la valeur de retour de `reduce`/`reduceRight`. Sinon, sa valeur de retour sera donnée comme `previousValue` pour l'appel suivant à `callbackfn`.

Et enfin, **`initialValue`** : Il s'agit d'une valeur initiale facultative pour `previousValue` (l'accumulateur). Si elle est donnée, et que `myArray` contient des éléments, le premier appel à `callbackfn` recevra cette valeur comme son `previousValue`.

**Note** : La `callbackfn` est généralement appelée une **fonction de réduction** (ou simplement **réducteur** en abrégé).

<h2 id="comprendre-reduce-reduceright-avec-un-diagramme"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>Comprendre <code>reduce</code>/<code>reduceRight</code> avec un diagramme
<a href="#comprendre-reduce-reduceright-avec-un-diagramme" aria-label="Anchor link for: &quot;Comprendre reduce/reduceRight avec un diagramme
&quot;" style="text-decoration: none;">
7</a></h2>

La seule différence entre `reduce` et `reduceRight` est la direction de l'itération. `reduce` itère sur les éléments du tableau de gauche à droite. Et `reduceRight` itère sur les éléments de droite à gauche.

Voyons comment vous pouvez utiliser `reduce`/`reduceRight` pour joindre un tableau de chaînes. Notez comment le résultat final est atteint en joignant les éléments du tableau étape par étape dans les deux directions :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/reduce-diagram1-1.png)
_Un diagramme montrant les différences entre `reduce` et `reduceRight`_

Ici, notez que :

* `acc` est utilisé pour accéder à `previousValue`.
* `curVal` est utilisé pour accéder à `currentElement`.
* L'entrée en forme circulaire à _**`r`**_ représente `curVal`.
* L'entrée en forme rectangulaire à _**`r`**_ représente `acc` ou l'accumulateur.
* Les valeurs initiales sont en formes rectangulaires, car elles sont reçues par _**`r`**_ comme `acc`s.

<h2 id="lalgorithme-de-reduce-reduceright"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>L'algorithme de <code>reduce</code>/<code>reduceRight</code>
<a href="#lalgorithme-de-reduce-reduceright" aria-label="Anchor link for: &quot;L'algorithme de reduce/reduceRight
&quot;" style="text-decoration: none;">
7</a></h2>

L'algorithme de 29 lignes ci-dessous peut sembler intimidant à première vue. Mais vous le trouverez probablement beaucoup plus facile à comprendre que de digérer des globs de longues phrases expliquant les détails complexes de ces méthodes.

**Note** : L'algorithme décrit ici a le contexte de la section "[Paramètres de reduce/reduceRight](https://www.freecodecamp.org/news/how-reduce-reduceright-works-javascript/#parameters-of-reduce-reduceright)". (C'est-à-dire que les variables `myArray`, `callbackfn` et `initialValue` proviennent de cette section.)

Alors détendez-vous, profitez des étapes, et n'oubliez pas d'expérimenter dans la console :

<div style="position: relative; margin-left: 40px; margin-bottom: 20px;"><ul style="padding: 0px; margin-block: 0px;"><div style="border-left: 1px solid lightgray; position: absolute; height: 100%;"></div><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">1</div>Si <code>initialValue</code> est présent,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">2</div>Si <code>myArray</code> n'a pas d'éléments, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">3</div>Retourner <code>initialValue</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">4</div>Sinon <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">5</div>Soit <code>accumulator</code> égal à <code>initialValue</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">6</div>Si la méthode est <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">7</div>Soit <code>startIndex</code> l'index de l'élément le plus à gauche de <code>myArray</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">8</div>Si la méthode est <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">9</div>Soit <code>startIndex</code> l'index de l'élément le plus à droite de <code>myArray</code>.</li></ul></li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">10</div>Sinon<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">11</div>Si <code>myArray</code> n'a pas d'éléments, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">12</div>Lancer <code>TypeError</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">13</div>Sinon si <code>myArray</code> n'a qu'un seul élément, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">14</div>Retourner cet élément.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">15</div>Sinon<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">16</div>Si la méthode est <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">17</div>Soit <code>accumulator</code> l'élément le plus à gauche de <code>myArray</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">18</div>Soit <code>startIndex</code> l'index de l'élément qui vient juste après l'élément le plus à gauche de <code>myArray</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">19</div>Si la méthode est <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">20</div>Soit <code>accumulator</code> l'élément le plus à droite de <code>myArray</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">21</div>Soit <code>startIndex</code> l'index de l'élément qui vient juste avant l'élément le plus à droite de <code>myArray</code>.</li></ul></li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">22</div>&nbsp;</li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">23</div>Si la méthode est <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">24</div>Dans l'ordre de gauche à droite, pour chaque élément de <code>myArray</code> tel que son index <code>i</code> 
2265 <code>startingIndex</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">25</div>Définir <code>accumulator</code> sur <code>callbackfn(accumulator, myArray[i], i, myArray)</code>. </li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">26</div>Si la méthode est <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">27</div>Dans l'ordre de droite à gauche, pour chaque élément de <code>myArray</code> tel que son index <code>i</code> 
2264 <code>startingIndex</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">28</div>Définir <code>accumulator</code> sur <code>callbackfn(accumulator, myArray[i], i, myArray)</code>. </li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">29</div>Retourner <code>accumulator</code>.<div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div></li></ul></div>

**Note** : Un tableau peut avoir une longueur supérieure à `0` mais aucun élément. Ces emplacements vides dans le tableau sont généralement appelés _trous_ dans le tableau. Par exemple :

```js
let arr = [,,,,];
console.log(arr.length);
// 4

// notez que la virgule finale n'augmente pas la longueur.
// Cette fonctionnalité nous permet d'ajouter un nouvel élément rapidement.

```

Ces méthodes n'appellent `callbackfn` que pour les éléments de `myArray` qui existent réellement. Par exemple, si vous avez un tableau comme `[1,,3,,5]`, elles ne tiendront pas compte des éléments non existants aux indices `1` et `3`. Essayez de deviner ce qui sera journalisé après avoir exécuté ce qui suit :

```js
[,,,3,,,4].reduce((_, cv, i) => {
  console.log(i);
});
```

Si vous avez dit `6`, vous avez raison !


26a0
fe0f **Avertissement** : Il n'est pas recommandé de modifier `myArray` à l'intérieur de `callbackfn` car cela complique la logique de votre code et augmente ainsi la possibilité de bugs.

Si vous avez lu et compris jusqu'ici, félicitations ! Vous devriez maintenant avoir une compréhension solide de comment `reduce`/`reduceRight` fonctionne. 

C'est un excellent moment pour résoudre quelques problèmes afin de vous habituer à `reduce`/`reduceRight`. Avant de voir les solutions, résolvez-les vous-même ou passez au moins un peu de temps à y réfléchir.

<h2 id="exercices"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5</span>Exercices
<a href="#exercices" aria-label="Anchor link for: &quot;Exercices
&quot;" style="text-decoration: none;">
7</a></h2>

<h3 id="aplatir-un-tableau-imbrique"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.1</span>Aplatir un tableau imbriqué
<a href="#aplatir-un-tableau-imbrique" aria-label="Anchor link for: &quot;Aplatir un tableau imbriqué
&quot;" style="text-decoration: none;">
7</a></h3>

Écrivez une fonction `flatten` qui peut aplatir un tableau imbriqué.

```js
let arr = [1, [2, [3], [[4], 5], 6]];
console.log(flatten(arr));
// [1, 2, 3, 4, 5, 6]

```

<details  style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
const flatten = (arr) => 
  arr.reduce((acc, curVal) =>
    acc.concat(Array.isArray(curVal) ? flatten(curVal) : curVal), []);
    </code>
  </pre>
</details>


<h3 id="supprimer-les-elements-dupliques-dun-tableau"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.2</span>Supprimer les éléments dupliqués d'un tableau
<a href="#supprimer-les-elements-dupliques-dun-tableau" aria-label="Anchor link for: &quot;Supprimer les éléments dupliqués d'un tableau
&quot;" style="text-decoration: none;">
7</a></h3>

Écrivez une fonction `rmDuplicates` qui supprime les éléments dupliqués comme ci-dessous :

```js
console.log(rmDuplicates([1, 2, 2, 3, 4, 4, 4]));
// [1, 2, 3, 4]
```

<details style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
const rmDuplicates = arr => 
  arr.reduce((p, c) => p.includes(c) ? p : p.concat(c), []);
    </code>
  </pre>
</details>


<h3 id="inverser-un-tableau-sans-le-muter"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.3</span>Inverser un tableau sans le muter
<a href="#inverser-un-tableau-sans-le-muter" aria-label="Anchor link for: &quot;Inverser un tableau sans le muter
&quot;" style="text-decoration: none;">
7</a></h3>

Il existe une méthode de tableau intégrée `reverse` pour inverser les tableaux. Mais elle mute le tableau original. Utilisez `reduceRight` pour inverser un tableau sans le muter.

<details style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
let arr = [1, 2, 3];

let reversedArr = arr.reduceRight((acc, curVal) => [...acc, curVal], []);

console.log(arr);
// [1, 2, 3]

console.log(reversedArr);
// [3, 2, 1]
    </code>
  </pre>
  <p>
    Notez qu'en inversant le tableau de cette manière, vous perdrez tous les trous dans le
    tableau.
  </p>
</details>


<h2 id="conclusion"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">6</span>Conclusion
<a href="#conclusion" aria-label="Anchor link for: &quot;Conclusion
&quot;" style="text-decoration: none;">
7</a></h2>

Lorsque `reduce`/`reduceRight` appelle `callbackfn` en interne, nous pouvons appeler ces motifs d'appel "comportements normaux" et nous pouvons traiter les autres scénarios comme des cas limites. Ceux-ci peuvent être résumés dans le tableau ci-dessous :

Valeur initiale | Nombre d'éléments | Sortie
--- | --- | --- 
Présente | 0 | **Cas limite** : Valeur initiale
Présente | Supérieur à 0 | **Comportement normal** 
Absente | 0 | **Cas limite** : TypeError
Absente | 1 | **Cas limite** : Cet élément
Absente | Supérieur à 1 | **Comportement normal** 

Apprendre `reduce`/`reduceRight` est un peu plus impliqué que les autres méthodes de tableau d'ordre supérieur. Mais cela vaut la peine de bien l'apprendre. 

Merci d'avoir lu ! J'espère que cet article a été utile. Si vous le souhaitez, vous pouvez consulter mon [site web](https://www.ashutoshbiswas.dev/) et me suivre sur [Twitter](https://twitter.com/ashutoshbw) et [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/).

Bonne réduction 
d83d
de03