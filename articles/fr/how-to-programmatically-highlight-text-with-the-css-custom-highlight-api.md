---
title: Comment surligner du texte de manière programmatique avec l'API CSS Custom
  Highlight
subtitle: ''
author: Joe Attardi
co_authors: []
series: null
date: '2025-01-15T15:37:04.767Z'
originalURL: https://freecodecamp.org/news/how-to-programmatically-highlight-text-with-the-css-custom-highlight-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736955360118/bd658ef5-734c-4e21-ad0e-be2dac0b7eee.png
tags:
- name: JavaScript
  slug: javascript
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Comment surligner du texte de manière programmatique avec l'API CSS Custom
  Highlight
seo_desc: 'You can highlight text in the browser by clicking and dragging through
  the desired text. And sometimes this works fine. But there are times when you’ll
  want to programmatically highlight some text in an HTML document.

  In this article, I’ll discuss a ...'
---

Vous pouvez surligner du texte dans le navigateur en cliquant et en faisant glisser sur le texte souhaité. Parfois, cela fonctionne bien. Mais il arrive que vous souhaitiez surligner du texte de manière programmatique dans un document HTML.

Dans cet article, je vais discuter de deux méthodes pour y parvenir. La première consiste à utiliser l'élément `<mark>`, et la seconde à utiliser l'API CSS Custom Highlight. Nous allons passer en revue des exemples, et j'expliquerai les problèmes liés à `<mark>`. Ensuite, vous apprendrez comment l'API Custom Highlight résout ces défis.

### Voici ce que nous allons couvrir :

1. [Ce que nous voulons faire](#heading-ce-que-nous-voulons-faire)

2. [Raisons de surligner du texte](#heading-raisons-de-surligner-du-texte)

3. [Comment surligner du texte en utilisant l'élément Mark](#heading-comment-surligner-du-texte-en-utilisant-lelement-mark)

4. [Présentation de l'API CSS Custom Highlight](#heading-presentation-de-lapi-css-custom-highlight)

5. [Comment appliquer un surlignage personnalisé](#heading-comment-appliquer-un-surlignage-personnalise)

6. [Comment modifier une plage surlignée](#heading-comment-modifier-une-plage-surlignee)

7. [Comment surligner plusieurs plages](#heading-comment-surligner-plusieurs-plages)

8. [Comment supprimer les surlignages](#heading-comment-supprimer-les-surlignages)

9. [Support des navigateurs](#heading-support-des-navigateurs)

10. [Conclusion](#heading-conclusion)

## Ce que nous voulons faire

Nous voulons appliquer des effets de surlignage à du texte dans un document, sans avoir besoin de le sélectionner manuellement. Typiquement, nous le ferions en donnant au texte une couleur de fond qui attire l'attention sur le texte surligné. Vous pouvez voir à quoi cela ressemble dans la capture d'écran suivante.

![Démonstration de texte surligné](https://cdn.hashnode.com/res/hashnode/image/upload/v1736729603375/cb0e081b-a848-4079-8b8e-67815d56711d.png align="center")

## Raisons de surligner du texte

Il existe plusieurs cas d'utilisation pour surligner du texte de manière programmatique. Avant de parler de *comment* surligner, parlons de *pourquoi* nous pourrions vouloir surligner.

* **Surligner les résultats de recherche ou les correspondances** : Si l'utilisateur atteint cette page par le biais d'une recherche, il peut être utile de mettre en évidence le texte correspondant à la recherche en appliquant un surlignage.

* **Mettre en emphasis des informations** : Nous pourrions vouloir mettre en évidence un texte important sur la page.

* **Surlignage défini par l'utilisateur** : Un exemple serait une application de lecture électronique comme l'application Amazon Kindle. Ici, les utilisateurs peuvent sélectionner et enregistrer des régions surlignées d'un livre. Plus tard, lorsqu'ils reviennent à une page, les surlignages précédents de l'utilisateur sont affichés.

## Comment surligner du texte en utilisant l'élément `<mark>`

Une façon de surligner du texte est d'utiliser l'élément [HTML `<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark). Cela a l'avantage d'être un élément sémantique HTML.

Pour surligner du texte en utilisant `<mark>`, vous pouvez envelopper le texte à surligner dans un élément `<mark>`. Le navigateur appliquera un style de surlignage à tout texte à l'intérieur d'un élément `<mark>`.

Considérez le code HTML suivant contenant un élément `<mark>` qui entoure le texte que vous souhaitez surligner.

```html
Voici un <mark>texte à surligner</mark>.
```

`<mark>` peut être stylisé avec CSS comme tout autre élément HTML, vous pouvez donc personnaliser la couleur et le style du texte surligné.

L'utilisation de l'élément `<mark>` présente cependant quelques inconvénients. Vous devez modifier le DOM et insérer des nœuds chaque fois que vous souhaitez ajouter un surlignage. Cela peut entraîner des effets secondaires tels qu'un recalcul de la mise en page qui peut affecter les performances de la page.

Il est également plus difficile de surligner du texte qui pourrait s'étendre sur plusieurs éléments HTML. Puisque `<mark>` est un élément HTML, vous devez l'utiliser de manière à produire un HTML valide.

Pour le reste de cet article, nous utiliserons un exemple de balisage HTML dont nous voulons surligner certaines parties. Considérez ce balisage HTML contenant un paragraphe d'introduction et quelques éléments de liste. Nous voulons appliquer un surlignage à une partie du contenu, mais montrons d'abord le HTML de base.

```html
<p>Un texte d'introduction.</p>

<ul>
  <li>Élément un</li>
  <li>Élément deux</li>
</ul>
```

Maintenant, supposons que nous voulons surligner "Un texte d'introduction." *et* "Élément un" ensemble. Nous ne pouvons pas utiliser un seul élément `<mark>`, car cela serait un HTML invalide.

La balise de fermeture serait imbriquée à l'intérieur d'un élément `<li>`, ce qui n'est pas un HTML valide. Le code suivant montre à quoi cela pourrait ressembler :

```html
<p><mark>Un texte d'introduction.</p>

<ul>
  <li>Élément un</mark></li>
  <li>Élément deux</li>
</ul>
```

Au lieu de cela, pour obtenir l'effet souhaité, nous devrions insérer plusieurs éléments `<mark>` comme le montre le code suivant. Notez qu'il y a deux éléments `<mark>` : un dans l'introduction et un dans le premier élément de la liste. Si vous vouliez surligner plusieurs éléments de la liste, vous devriez ajouter encore plus d'éléments `<mark>`.

Voici un exemple de code avec plusieurs éléments `<mark>` :

```html
<p><mark>Un texte d'introduction.</mark></p>

<ul>
  <li><mark>Élément un</mark></li>
  <li>Élément deux</li>
</ul>
```

Cela fonctionne, mais c'est fastidieux et ne donne pas un surlignage continu.

## Présentation de l'API CSS Custom Highlight

La solution à notre problème est l'[API CSS Custom Highlight](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API), une API plus récente qui vous permet de créer des régions de surlignage et de les styliser avec CSS. Les surlignages sont liés à des *plages*, qui peuvent s'étendre sur plusieurs éléments HTML et n'ajoutent aucun balisage ou élément au document.

Il y a plusieurs concepts que vous devez connaître lors de l'utilisation de cette API :

* [`Range`](https://developer.mozilla.org/en-US/docs/Web/API/Range) : Un `Range` est un objet représentant une partie d'un document entre deux nœuds. Ceux-ci peuvent être des nœuds d'élément ou des nœuds de texte.

* [`Highlight`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight) : Un `Highlight` est un objet qui définit un surlignage personnalisé autour d'un ou plusieurs objets `Range`. Ces objets sont enregistrés avec le moteur CSS sous un nom unique.

* [Registre de surlignage CSS](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry) : Un objet global où les objets `Highlight` sont enregistrés sous des noms uniques.

* [Le pseudo-élément `::highlight`](https://developer.mozilla.org/en-US/docs/Web/CSS/::highlight) : Celui-ci est utilisé dans une feuille de style CSS pour définir le style de surlignage. Chaque pseudo-élément `::highlight` référence un nom d'objet `Highlight` qui a été enregistré avec le registre de surlignage CSS.

## Comment appliquer un surlignage personnalisé

Revenons à l'exemple précédent de surlignage et utilisons l'API CSS Custom Highlight pour surligner le texte d'introduction et le premier élément de la liste.

Tout d'abord, ajoutons quelques ID pour pouvoir sélectionner les éléments pertinents plus facilement. Considérez ce code mis à jour où nous avons ajouté des ID à certains des éléments.

```html
<p id="intro">Texte d'introduction.</p>

<ul>
  <li id="item1">Élément un</li>
  <li id="item2">Élément deux</li>
</ul>
```

Passons en revue les étapes pour créer le surlignage.

### Créer le `Range`

Tout d'abord, nous allons créer un objet `Range` qui couvre les éléments souhaités. Cela représentera une plage d'éléments qui couvre l'introduction et le premier élément de la liste sans avoir à modifier le DOM.

```javascript
const range = new Range();
range.setStartBefore(document.getElementById('intro'));
range.setEndAfter(document.getElementById('item1'));
```

Cet objet `Range` commencerà au début de l'élément `<p>` et se terminera à la fin de l'élément `<li>` avec l'ID `item1`.

### Créer et enregistrer l'objet `Highlight`

Maintenant que nous avons un `Range`, nous pouvons créer un `Highlight` pour ce `Range`. Nous le faisons en appelant le [constructeur `Highlight`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight/Highlight), en passant l'objet `Range` comme argument.

```javascript
const highlight = new Highlight(range);
```

Cela crée l'objet `Highlight`, mais nous ne pouvons encore rien faire avec. Tout d'abord, nous devons l'enregistrer avec le registre de surlignage CSS avec la méthode [`CSS.highlights.set`](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry/set).

Le code suivant montre comment vous pouvez utiliser `CSS.highlights.set` pour enregistrer un objet `Highlight` sous le nom `my-custom-highlight`. Nous référencerons ce nom dans le CSS lorsque nous appliquerons le style dans l'étape suivante.

```javascript
CSS.highlights.set('my-custom-highlight', highlight);
```

### Styliser le surlignage

Nous avons créé et enregistré le `Highlight` autour d'un `Range` donné, mais à ce stade, nous ne verrons toujours rien dans le document. Nous devons utiliser une règle CSS pour définir le style de surlignage.

Pour ce faire, nous utiliserons le pseudo-élément `::highlight`. Nous passons le nom du surlignage personnalisé utilisé dans l'étape précédente à ce pseudo-élément. Cela nous permet de définir des styles CSS qui sont appliqués au texte dans la plage surlignée.

```css
::highlight(my-custom-highlight) {
  background-color: yellow;
}
```

Maintenant, le texte d'introduction et le premier élément de la liste seront surlignés en jaune, comme le montre cette capture d'écran.

![Capture d'écran montrant l'état initial du surlignage](https://cdn.hashnode.com/res/hashnode/image/upload/v1736729896575/97b15f77-e8fc-449e-8a89-ad5658e13605.png align="center")

## Comment modifier une plage surlignée

Lorsque nous créons un objet `Highlight` autour d'un objet `Range`, le `Highlight` sera dynamiquement mis à jour avec toute modification apportée au `Range`. Dans notre exemple, supposons que nous voulons maintenant étendre le surlignage au deuxième élément de la liste.

Nous n'avons pas besoin de créer un nouveau `Highlight` ou `Range` – plutôt, nous pouvons simplement définir la position de fin du `Range` sur le nouvel élément.

```javascript
range.setEndAfter(document.getElementById('item2'));
```

Dès que le `Range` est modifié, le nouveau texte sera surligné comme le montre cette capture d'écran.

![Le deuxième élément de la liste est maintenant surligné](https://cdn.hashnode.com/res/hashnode/image/upload/v1736729961827/8633c59b-485d-4ba6-a716-7dcb084fddae.png align="center")

## Comment surligner plusieurs `Range`s

Pour encore plus de flexibilité, un seul `Highlight` peut couvrir plusieurs `Range`s. Mettons à jour notre exemple HTML pour inclure quatre éléments de liste.

```html
<p id="intro">Texte d'introduction.</p>

<ul>
  <li id="item1">Élément un</li>
  <li id="item2">Élément deux</li>
  <li id="item3">Élément trois</li>
  <li id="item4">Élément quatre</li>
</ul>
```

Jusqu'à présent, nous surlignons le texte d'introduction et les deux premiers éléments de la liste. Supposons que nous voulons maintenant également surligner le quatrième élément de la liste. Nous ne pouvons pas faire cela avec notre objet `Range` existant, car il ne représenterait pas une plage contiguë de nœuds. Nous devons créer un deuxième `Range`. Ce nouveau `Range` couvre le quatrième élément de la liste.

```javascript
const item4 = document.getElementById('item4');
const range2 = new Range();
range2.setStartBefore(item4);
range2.setEndAfter(item4);
```

Maintenant, nous pouvons ajouter ce nouveau `Range` à notre objet `Highlight` existant en appelant sa méthode [`add`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight/add). Cela nous permettra d'appliquer un surlignage au deuxième `Range`.

```javascript
highlight.add(range2);
```

Une fois que nous avons fait cela, le quatrième élément de la liste sera également surligné, comme le montre cette capture d'écran.

![Le quatrième élément est maintenant également surligné](https://cdn.hashnode.com/res/hashnode/image/upload/v1736730028688/6710e901-6027-46c5-af8e-2d2c3bc7563f.png align="center")

## Comment supprimer les surlignages

Il existe deux façons de supprimer les surlignages du document.

Tout d'abord, supposons que nous voulons supprimer le surlignage du texte d'introduction et des deux premiers éléments de la liste, mais garder le dernier élément de la liste surligné. Nous pouvons utiliser la méthode [`delete`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight/delete) de l'objet `Highlight` pour supprimer le premier `Range` de l'objet `Highlight`.

```javascript
highlight.delete(range);
```

Après avoir supprimé ce `Range`, seul le dernier élément de la liste restera surligné, comme le montre cette capture d'écran.

![Seul le dernier élément de la liste est maintenant surligné](https://cdn.hashnode.com/res/hashnode/image/upload/v1736730070050/626121b3-60a3-4491-b9d8-11940d4d34f2.png align="center")

L'autre façon de supprimer les surlignages est de désenregistrer un objet `Highlight` du registre de surlignage CSS en appelant [`CSS.highlights.delete`](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry/delete) avec le nom unique que nous avons donné au `Highlight`. Cela supprime l'objet `Highlight` que nous avons enregistré précédemment.

```javascript
CSS.highlights.delete('my-custom-highlight');
```

Maintenant, rien ne restera surligné, comme le montre cette capture d'écran.

![Rien n'est surligné](https://cdn.hashnode.com/res/hashnode/image/upload/v1736730106386/593b7b46-027d-442a-b633-04ac0aecdb4a.png align="center")

## Support des navigateurs

En janvier 2025, au moment de la rédaction, l'API CSS Custom Highlight est supportée dans Chrome, Edge et Safari. Le support de Firefox commence à apparaître dans les versions nocturnes, vous pouvez donc vous attendre à ce que Firefox ait un support amélioré bientôt. Pour les dernières données de compatibilité, voir [https://caniuse.com/mdn-api\_highlight](https://caniuse.com/mdn-api_highlight).

Pour tester si le navigateur supporte le surlignage CSS personnalisé, vous pouvez vérifier l'existence de la propriété `highlights` de l'objet [`CSS`](https://developer.mozilla.org/en-US/docs/Web/API/CSS) :

```javascript
if (!('highlights' in CSS)) {
  // L'API de surlignage n'est pas supportée
}
```

## Conclusion

L'API CSS Custom Highlight vous permet de surligner de manière programmatique des régions de texte dans un document HTML sans avoir à modifier le DOM ou à vous soucier d'insérer un balisage HTML invalide. Sa nature flexible et dynamique vous permet d'ajouter, de modifier et de supprimer des surlignages à l'exécution.

### Lectures complémentaires

* [`Range` (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Range) : Documentation de l'API pour l'interface `Range`.

* [API CSS Custom Highlight (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API) : Plus de détails sur l'API CSS Custom Highlight.