---
title: Comment utiliser les Container Queries – Responsive Design au-delà de la viewport
subtitle: ''
author: Felix Favour Chinemerem
co_authors: []
series: null
date: '2023-05-22T16:24:14.000Z'
originalURL: https://freecodecamp.org/news/container-queries-responsive-design-beyond-the-viewport
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/container-queries-1.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: responsive design
  slug: responsive-design
seo_title: Comment utiliser les Container Queries – Responsive Design au-delà de la
  viewport
seo_desc: "Before now, making your website responsive was limited to resizing HTML\
  \ elements with media queries. This was, and still is, a brilliant innovation for\
  \ web development in general. \nBut web development has evolved with the advent\
  \ of JavaScript framewo..."
---

Avant maintenant, rendre votre site web responsive était limité à redimensionner les éléments HTML avec des media queries. Cela était, et reste, une innovation brillante pour le développement web en général. 

Mais le développement web a évolué avec l'avènement des frameworks JavaScript—particulièrement avec l'utilisation de composants comme blocs de construction dans le développement des interfaces utilisateur.

Dans le monde axé sur les composants dans lequel nous vivons, nous pouvons voir les avantages des container queries dans le Responsive Web Design. En fait, dans certains cas, nous pouvons obtenir une page web entièrement responsive sans utiliser de media queries.

Dans cet article, nous allons explorer le design responsive au-delà de la viewport avec les Container Queries et analyser un exemple de site entièrement responsive utilisant uniquement des container queries.

## Alors, que sont les Container Queries ?

Les container queries vous permettent de styliser les éléments HTML en fonction de la taille de leurs conteneurs. C'est similaire en exécution aux media queries, sauf que les éléments sont stylisés en fonction de la taille d'une viewport avec les media queries.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/container-queries-explanation.png)
_Image illustrant les Container Queries en CSS_

## Comment utiliser les Container Queries

### Le contexte de conteneur

Pour utiliser les container queries, vous devez indiquer au navigateur quel élément HTML vous souhaitez utiliser comme conteneur. Nous faisons cela en déclarant un "contexte de conteneur". 

Un contexte de conteneur instructe le navigateur à commencer à prêter attention à la taille d'un conteneur (ou d'un élément). Ainsi, le navigateur sait quand appliquer les styles spécifiés dans votre container query.

Pour déclarer un contexte de conteneur, nous utilisons la propriété `container-type` avec une valeur de `size`, `inline-size`, ou `normal`. Voir la référence de l'API [container-type](https://developer.mozilla.org/en-US/docs/Web/CSS/container-type) pour comprendre ce que chacune de ces valeurs signifie.

Considérons l'exemple suivant d'un composant de carte de boisson gazeuse ci-dessous :

```html
<div class="drink-card-container">
  <div class="drink-card">
    <img src="images/coke.png" alt="" />
    <div class="info">. . .</div>
   </div>
 </div>

```

Nous pouvons ensuite ajouter un contexte de conteneur au conteneur :

```css
.drink-card-container {
  container-type: inline-size; 
}

```

Et maintenant, le navigateur prête attention à la taille de `.drink-card-container`. Bien que, nous devons toujours appliquer des styles spécifiques en fonction de cette taille de conteneur, donc nous avons besoin de la règle `@container`.

### La règle `@container`

La règle `@container` vous permet de styliser les éléments en fonction de la taille de leur conteneur. La condition du conteneur est évaluée lorsque le conteneur change de taille. De plus, la règle `@container` est ce qui définit principalement une container query. Elle prend cette forme :

```css
@container <container-condition> {
  <stylesheet>
}

```

Elle a une syntaxe similaire à la règle `@media` dans les media queries.

Rappelons notre exemple de carte de boisson gazeuse. Nous pouvons maintenant ajouter une règle `@container` qui modifie la `flex-direction` de notre `.drink-card` lorsque la taille du conteneur est inférieure ou égale à `450px`.

```css
@container (max-width: 450px) {
  .drink-card-container .drink-card {
    flex-direction: column;
  }
}

```

Et c'est tout ! C'est tout ce que vous devez savoir pour commencer à utiliser les container queries.

### La propriété container-name

Maintenant que vous savez comment fonctionnent les container queries, réfléchissons à grande échelle—que se passe-t-il lorsque nous avons plusieurs conteneurs ou contextes de conteneur à gérer ? 

Cela introduit le besoin de spécificité lors de l'écriture de container queries, c'est pourquoi la propriété `container-name` existe.

Reconsidérons l'exemple de notre composant de carte de boisson gazeuse.

```html
<div class="drink-card-container">
  <div class="drink-card">
    . . .
    <div class="info">
		  <h3>Coke</h3>
      <p>Le 8 mai 1886, le premier verre de Coke a été vendu.</p>
      <h5>
6 150 <sup>prix de vente estimé</sup></h5>
      <a href="<https://www.coca-cola.com/>">Voir le site officiel</a>
		</div>
   </div>
 </div>

```

Nous pouvons ensuite ajouter un contexte de conteneur à l'élément `.info` en lui donnant une propriété `container-type`, comme nous l'avons fait précédemment. Mais cette fois, nous incluons une propriété `container-name` pour donner au conteneur une identité spécifique.

```css
.info {
  container-type: inline-size;
  container-name: drink-info;
}

```

Notre container query prendra alors cette forme :

```css
@container drink-info (max-width: 200px) {
  .info p {
    display: none;
  }
}

```

Le code ci-dessus suit la taille du conteneur `.info` (nommé `drink-info`) et masque l'élément paragraphe lorsque la taille du conteneur est inférieure ou égale à `200px`.

## Code source pour un site responsive utilisant uniquement des Container Queries

Pour accéder au code source complet d'où tous les extraits de cet article ont été extraits, vous pouvez visiter ce [dépôt GitHub](https://github.com/felixfavour/container-queries).

### Aperçu en direct

Vous pouvez voir un aperçu en direct du code GitHub [ici](https://felixfavour.github.io/container-queries/). Pour voir la réactivité en action, redimensionnez la fenêtre du navigateur. Alternativement, vous pouvez interagir avec le codepen ci-dessous.

%[https://codepen.io/felixfavour/pen/ZEqqRyr]

## Compatibilité des navigateurs pour les Container Queries

Les container queries sont disponibles sur tous les principaux moteurs de navigateurs et sont stables dans tous les navigateurs modernes. Cela signifie que vous pouvez les utiliser dès aujourd'hui pour des projets personnels et professionnels.

J'espère que cet article vous a aidé à apprendre les bases des container queries. Maintenant, vous ne serez plus limité à n'utiliser que les media queries—les container queries sont également un moyen valable de rendre vos sites web responsives.

J'espère que vous avez trouvé cet article utile. Si c'est le cas, n'hésitez pas à me contacter sur LinkedIn et à consulter [favourfelix.com](http://favourfelix.com/) pour voir ce que j'écris et ce que je fais d'autre.