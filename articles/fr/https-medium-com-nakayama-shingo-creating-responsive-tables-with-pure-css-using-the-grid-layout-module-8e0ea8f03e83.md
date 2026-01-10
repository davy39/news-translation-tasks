---
title: Comment créer des tableaux réactifs avec du CSS pur en utilisant le module
  de mise en page Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T06:17:06.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-nakayama-shingo-creating-responsive-tables-with-pure-css-using-the-grid-layout-module-8e0ea8f03e83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CthvMCprY75MLB_q8BygXg.png
tags:
- name: css properties
  slug: css-properties
- name: Datatables
  slug: datatables
- name: flexbox
  slug: flexbox
- name: grid layout
  slug: grid-layout
- name: responsive design
  slug: responsive-design
seo_title: Comment créer des tableaux réactifs avec du CSS pur en utilisant le module
  de mise en page Grid
seo_desc: 'By Shingo Nakayama

  TL;DR

  The most popular way to display a collection of similar data is to use tables, but
  HTML tables have the drawback of being difficult to make responsive.

  In this article, I use CSS Grid Layout Module and CSS Properties (and no ...'
---

Par Shingo Nakayama

### TL;DR

La manière la plus populaire d'afficher une collection de données similaires est d'utiliser des tableaux, mais les tableaux HTML ont l'inconvénient d'être difficiles à rendre réactifs.

Dans cet article, j'utilise le module de mise en page CSS Grid et les propriétés CSS (et pas de JavaScript) pour disposer des tableaux qui enveloppent les colonnes en fonction de la largeur de l'écran, ce qui se transforme ensuite en une carte basée sur la mise en page pour les petits écrans.

Pour les impatients, regardez le pen suivant pour une implémentation prototypique.

%[https://codepen.io/ShingoNakayama/pen/LMLeRZ]

### Un peu d'histoire des tableaux HTML réactifs

Les tableaux réactifs ne sont pas un nouveau sujet, et de nombreuses solutions ont déjà été proposées. ["Responsive Table Data Roundup"](https://css-tricks.com/responsive-data-table-roundup/) publié pour la première fois en 2012 par Chris Coyier, résume très bien les choses (y compris une mise à jour de 2018).

["Really Responsive Tables using CSS3 Flexbox"](https://hashnode.com/post/really-responsive-tables-using-css3-flexbox-cijzbxd8n00pwvm53sl4l42cx) par Vasan Subramanian montre une idée d'enveloppement des colonnes, implémentée avec Flexbox.

Même si de nombreuses idées intéressantes ont été proposées, des bibliothèques comme [bootstrap](https://getbootstrap.com/docs/4.0/content/tables/#responsive-tables) optent pour le défilement horizontal pour les petits écrans.

Maintenant que nous avons CSS Grid, je pense que nous pourrions avoir une meilleure alternative commune au défilement horizontal.

### Tableaux HTML

En commençant par les bases, un tableau en HTML est un format de mise en page pour afficher des collections d'éléments à travers une matrice de lignes et de colonnes. Les éléments sont disposés en lignes, avec les mêmes attributs de données dans les mêmes colonnes, les lignes étant souvent triées avec un ou plusieurs attributs triables. Le format vous donne une vue d'ensemble pour saisir et examiner rapidement de grandes quantités de données.

Par exemple, voici un tableau hypothétique des détails des bons de commande, que vous pourriez voir dans une application d'achat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B78yFFUVc1X8uEp_gVLcNw.png)
_Tableau des détails des bons de commande_

Un élément, dans ce cas, est un détail de bon de commande, qui a des attributs tels que le numéro de pièce, la description de la pièce, etc.

Lors de l'utilisation de tableaux HTML, la mise en page des données est codée en dur en lignes et colonnes (par exemple, `<tr>` et `<td>`). Cela peut être suffisant pour une utilisation par un écran qui s'adapte à la largeur totale du tableau, mais en réalité, cela ne s'applique pas aux myriades d'appareils qui existent aujourd'hui. En termes de hacks, vous pouvez modifier la propriété d'affichage des tableaux et utiliser n'importe quelle mise en page que vous pouvez faire avec CSS en général, mais cela ne semble pas sémantiquement correct.

### Tableaux redéfinis (= Collection d'éléments)

Commençons par redéfinir comment les données de tableau doivent être exprimées en HTML.

Comme indiqué précédemment, puisque les données de tableau sont essentiellement une collection ordonnée d'éléments, il semble naturel d'utiliser des listes ordonnées. De plus, puisque les tableaux sont souvent utilisés pour compléter les descriptions textuelles, il semble naturel de les enfermer dans une section, mais cela dépendrait du contexte de la manière dont les données de tableau sont utilisées.

```html
<section>
 <ol>
  <!-- Le premier élément de la liste est l'en-tête du tableau -->
  <li>
   <div>#</div>
   <!-- Enfermer les attributs sémantiquement similaires comme une hiérarchie de div -->
   <div>
    <div>Numéro de pièce</div>
    <div>Description de la pièce</div>
   </div>
   ...
  </li>
  <!-- Le reste des éléments de la liste sont les données réelles -->
  <li>
   <div>1</div>
   <!-- Grouper les informations liées aux pièces-->
   <div>
    <div>100-10001</div>
    <div>Description de la pièce</div>
   </div>
  ...
  </li>
 ...
 </ol>
</section>
```

Des `<div>` vanilla sont utilisés pour exprimer les attributs des éléments puisque HTML5 ne définit pas de balise appropriée pour cela. Le point clé ici est d'exprimer les attributs sémantiquement similaires comme une hiérarchie de `<div>`. Cette structure sera utilisée lors de la définition de la manière dont les données doivent être disposées. Je reviendrai sur ce point dans la section suivante sur le sujet du style.

En ce qui concerne les données réelles à l'intérieur de l'élément `<div>`, le premier élément de la liste est l'en-tête, et le reste des éléments sont les données réelles.

Maintenant, il est temps de commencer à parler du style des éléments avec CSS Grid.

### Stylisation des collections d'éléments

L'idée de base ici est d'afficher tous les attributs de l'élément sous forme de tableau normal, si la largeur de l'affichage le permet. Cette mise en page a l'avantage de pouvoir voir autant d'éléments (lignes) que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6sZipUcqB3hru4Q5r0kORw.png)
_Tableau complet_

Lorsque la largeur de l'affichage devient plus étroite, certains attributs sont empilés verticalement, afin d'économiser de l'espace horizontal. Le choix des attributs à empiler doit être basé sur :

1. Les attributs ont-ils un sens lorsqu'ils sont empilés verticalement ? et,
2. Lorsqu'ils sont empilés verticalement, cela économise-t-il de l'espace horizontal ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*llLsnXzdnBBfMRPqoKNBmw.png)
_Tableau enveloppant 1. Commencez par envelopper les colonnes qui nécessitent peu de largeur, et donnez de l'espace aux autres colonnes_

![Image](https://cdn-media-1.freecodecamp.org/images/1*DdQ-n4VzeGU1EzhRKdHj8w.png)
_Tableau enveloppant 2. Enveloppez "Description de la pièce", pour pouvoir voir la description_

![Image](https://cdn-media-1.freecodecamp.org/images/1*ys0ukWXXtbWhVyXTD9E0Zw.png)
_Tableau enveloppant 3. Enveloppez davantage "Nom du fournisseur"_

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ik1zA0LDXzWib7Ux-4EpQ.png)
_Tableau enveloppant 4. Enveloppez les informations liées au fournisseur sous les informations liées à la pièce_

![Image](https://cdn-media-1.freecodecamp.org/images/1*sEvQQjZoux7PEii3JQpCRg.png)
_Tableau enveloppant 5. Complètement enveloppé_

Lorsque la largeur se réduit davantage à la taille d'un appareil mobile, chaque élément est affiché sous forme de carte. Cette mise en page a une redondance car les noms des attributs sont répétés sur chaque carte, et a la moindre lisibilité, mais ne compromet pas l'utilisabilité (par exemple, défilement horizontal, texte super petit, etc.).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jI0hhzrpYpjbO3-fGh8IWA.png)
_Mise en page de carte à deux colonnes_

![Image](https://cdn-media-1.freecodecamp.org/images/1*XCCcicUngRBcBaKyETC4vg.png)
_Mise en page de carte à une colonne_

Maintenant, plongeons dans les détails.

#### Étape de stylisation 1 : Tableau complet

Voici un résumé visuel de la manière dont les choses seront implémentées avec CSS Grid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uA9PfcQ9JCzY54mH7p_v-A.png)
_Conteneurs de grille_

Afin de faire envelopper les colonnes, plusieurs conteneurs de grille sont définis comme une hiérarchie. La boîte rouge est un conteneur de grille pour chaque ligne, et la boîte bleue est un conteneur pour chaque groupe de colonnes qui s'enveloppe.

Commençons par définir la liste comme un conteneur de grille en définissant une classe appelée `.item-container` et en l'appliquant au `<li>` (la boîte rouge).

```css
.item-container {
    display: grid;
    grid-template-columns: 2em 2em 10fr 2fr 2fr 2fr 2fr 5em 5em;
}
```

Le nombre de colonnes explicites spécifiées avec `grid-template-columns` est de neuf, ce qui est le nombre de `<div>` de premier niveau, directement sous `<li>`.

La largeur de la colonne est définie en longueur relative pour faire envelopper les colonnes. La fraction réelle doit être ajustée en fonction du contenu.

Les colonnes qui ne s'enveloppent pas sont définies en longueur absolue pour maximiser l'utilisation de la largeur pour les colonnes enveloppantes. Dans l'exemple des détails de bon de commande, la deuxième colonne est un identifiant à deux chiffres, donc j'ai défini la largeur à deux fois cette taille de 2 m.

Ensuite, nous définissons un autre conteneur de grille appelé `.attribute-container` et l'appliquons sur tous les `<div>` intermédiaires sous la liste (la boîte bleue).

```css
.attribute-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(var(--column-width-min), 1fr));
    }
```

La largeur minimale de la colonne pour tous les éléments de grille sous `.attribute-container` est spécifiée avec une variable CSS appelée `--column-width-min` (plus d'informations à ce sujet plus tard) en utilisant la fonction `minmax`, avec le maximum défini pour prendre le reste de l'espace (par exemple, une fraction). Puisque `grid-template-columns` sont `repeat`és, l'espace horizontal disponible sera divisé en le nombre maximum de colonnes qui pourraient prendre au moins `--column-width-min`, et le reste des colonnes passerait à la ligne suivante. La largeur de la colonne sera étirée s'il y a un excès d'espace horizontal car le `repeat` est `auto-fit`é.

#### Étape de stylisation 2 : Tableau enveloppant

Ensuite, `--column-width-min` doit être spécifié indépendamment pour chaque colonne afin de les envelopper. Juste pour être clair, les variables doivent être spécifiées pour que le tableau complet soit rendu correctement également. Pour ce faire, une classe est définie pour chaque `.attribute-container`, et un `--column-width-min` différent est spécifié pour chaque portée de classe.

Regardons le HTML où `.part-id` est appliqué,

```html
<div class="attribute-container part-id">
    <div>Numéro de pièce</div>
    <div>Description de la pièce</div>
</div>
```

et le CSS :

```css
.part-id {
    --column-width-min: 10em;
}
```

Ce conteneur de grille spécifique aura deux colonnes, tant que la largeur disponible est plus large que 10em pour chaque élément de grille (par exemple, le conteneur de grille est plus large que 20em). Une fois que la largeur du conteneur de grille devient plus étroite que 20em, le deuxième élément de grille passera à la ligne suivante.

Lorsque nous combinons les propriétés CSS de cette manière, nous n'avons besoin que d'un seul conteneur de grille `.attribute-container`, les détails changeant là où la classe est appliquée.

Nous pouvons imbriquer davantage les `.attribute-container`, pour avoir plusieurs niveaux d'enveloppement avec différentes largeurs, comme dans l'exemple suivant.

```html
<div class="attribute-container part-information">
    <div class="attribute-container part-id">
        <div class="attribute" data-name="Numéro de pièce">Numéro de pièce</div>
        <div class="attribute" data-name="Description de la pièce">Description de la pièce
    </div>
    </div>
    <div class="attribute-container vendor-information">
        <div class="attribute">Numéro de fournisseur</div>
        <div class="attribute">Nom du fournisseur</div>
    </div>
</div>
.part-information {
    --column-width-min: 10em;
}
.part-id {
    --column-width-min: 10em;
}
.vendor-information {
    --column-width-min: 8em;
}
```

Tout ce qui précède est enfermé dans la requête média suivante. Le point de rupture réel doit être sélectionné en fonction de la largeur nécessaire lorsque votre tableau est enveloppé à l'extrême.

```
@media screen and (min-width: 737px) {
...
}
```

#### Étape de stylisation trois : Mise en page de carte

La mise en page de la carte ressemblera à un formulaire typique avec les noms des attributs dans la première colonne et les valeurs des attributs dans la deuxième colonne.

Pour ce faire, une classe appelée `.attribute` est définie et appliquée à toutes les balises `<div>` feuilles sous le `<li>`.

```js
.attribute {
    display: grid;
    grid-template-columns: minmax(9em, 30%) 1fr;
}
```

Les noms des attributs sont pris à partir d'un attribut personnalisé de la feuille `<div>` appelé `data-name`, par exemple `<div class="attribute" data-name="Numéro de pièce">`, et un pseudo-élément est créé. Le pseudo-élément sera soumis à la mise en page du conteneur de grille.

```js
.attribute::before {
    content: attr(data-name);
}
```

Le premier élément de la liste est l'en-tête et n'a pas besoin d'être affiché.

```js
/* Ne pas afficher le premier élément, car il est utilisé pour afficher l'en-tête pour les mises en page tabulaires*/
.collection-container>li:first-child {
    display: none;
}
```

Et enfin, les cartes sont disposées en une colonne pour les appareils mobiles, mais en deux pour les écrans avec un peu plus de largeur, mais pas assez pour afficher un tableau.

```
/* Mise en page de carte à 2 colonnes */
@media screen and (max-width: 736px) {
    .collection-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 20px;
    }
...
}
/* Mise en page de carte à 1 colonne */
@media screen and (max-width:580px) {
    .collection-container {
        display: grid;
        grid-template-columns: 1fr;
    }
}
```

### Notes finales

L'accessibilité est un domaine qui n'a pas été du tout considéré et qui pourrait avoir de la place pour des améliorations.

Si vous avez des idées ou des réflexions, n'hésitez pas à commenter !

Et bien sûr, merci pour la lecture.