---
title: Tableaux HTML – Tutoriel sur les tableaux avec exemple de code
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-09-07T21:17:18.000Z'
originalURL: https://freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/uide-to-writting-a-good-readme-file--7-.png
tags:
- name: data visualization
  slug: data-visualization
- name: HTML
  slug: html
seo_title: Tableaux HTML – Tutoriel sur les tableaux avec exemple de code
seo_desc: 'When you''re building a project that needs to represent data visually,
  you will need a good way to display the information so it''s easy to read and understand.

  Now, depending on the type of data, you can select between different representation
  methods...'
---

Lorsque vous construisez un projet qui nécessite de représenter des données visuellement, vous aurez besoin d'une bonne façon d'afficher les informations pour qu'elles soient faciles à lire et à comprendre.

Maintenant, selon le type de données, vous pouvez choisir entre différentes méthodes de représentation en utilisant des éléments HTML.

Dans la plupart des cas, les tableaux sont plus pratiques pour afficher de grandes quantités de données structurées de manière agréable. C'est pourquoi, dans cet article, nous allons apprendre comment utiliser les tableaux en HTML et ensuite comment les styliser.

### Voici un Scrim interactif sur les tableaux HTML

<iframe src="https://scrimba.com/scrim/coab640c695498ac58f9776ed?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

Mais d'abord, qu'est-ce qu'un tableau en HTML ?

## Qu'est-ce qu'un tableau en HTML ?
Un tableau est une représentation de données disposées en lignes et en colonnes. En réalité, c'est plus comme une feuille de calcul. En HTML, avec l'aide des tableaux, vous pouvez organiser des données comme des images, du texte, des liens, etc., en lignes et en colonnes de cellules.

L'utilisation des tableaux sur le web est devenue plus populaire récemment grâce aux incroyables balises de tableau HTML qui facilitent leur création et leur conception.

Pour créer un tableau en HTML, vous devrez utiliser des balises. La plus importante est la balise `<table>` qui est le conteneur principal du tableau. Elle montre où le tableau commence et où il se termine.

### Balises courantes des tableaux HTML

D'autres balises incluent :

* `<tr>` - représente les lignes
* `<td>` - utilisée pour créer des cellules de données
* `<th>` - utilisée pour ajouter des en-têtes de tableau
* `<caption>` - utilisée pour insérer des légendes
* `<thead>` - ajoute un en-tête séparé au tableau
* `<tbody>` - montre le corps principal du tableau
* `<tfoot>` - crée un pied de page séparé pour le tableau

## Syntaxe des tableaux HTML :
```html
<table>
  <tr>
    <td>Cellule 1</td>
    <td>Cellule 2</td>
    <td>Cellule 3</td>
  </tr>
  <tr>
    <td>Cellule 4</td>
    <td>Cellule 5</td>
    <td>Cellule 6</td>
  </tr>
</table>
```

<table class="default">

  <tr>

    <td>Cellule 1</td>

    <td>Cellule 2</td>

    <td>Cellule 3</td>

  </tr>

  <tr>

    <td>Cellule 4</td>

    <td>Cellule 5</td>

    <td>Cellule 6</td>

  </tr>

</table>

Maintenant que vous avez une compréhension de ce qu'est un tableau HTML et de la manière de le créer, passons à la suite et voyons comment nous pouvons utiliser ces balises pour créer des tableaux avec plus de fonctionnalités.

## Comment ajouter un en-tête de tableau en HTML
La balise `<th>` est utilisée pour ajouter des en-têtes aux tableaux. Dans les conceptions de base, l'en-tête du tableau prendra toujours la première ligne, ce qui signifie que nous aurons la balise `<th>` déclarée dans notre première ligne de tableau, suivie des données réelles du tableau. Par défaut, le texte passé dans l'en-tête est centré et en gras.

**Un exemple avec l'utilisation de `<th>`**
```html
<table>
  <tr>
    <th>Prénom</th>
    <th>Nom</th>
    <th>Adresse Email</th>
  </tr>
  <tr>
   <td>Hillary</td>
   <td>Nyakundi</td>
   <td>tables@mail.com</td>
  </tr>
  <tr>
    <td>Lary</td>
    <td>Mak</td>
    <td>developer@mail.com</td>
  </tr>
</table>
```

<table>
      <tr>
    <th>Prénom</th>
    <th>Nom</th>
    <th>Adresse Email</th>
  </tr>
  <tr>
   <td>Hillary</td>
   <td>Nyakundi</td>
   <td>tables@mail.com</td>
  </tr>
  <tr>
    <td>Lary</td>
    <td>Mak</td>
    <td>developer@mail.com</td>
  </tr>
</table>

Dans l'exemple ci-dessus, nous sommes en mesure de dire quelle colonne contient quelle information. Cela est rendu possible grâce à l'utilisation de la balise `<th>`.

## Comment ajouter une légende à un tableau
L'utilisation principale de l'ajout d'une légende à un tableau est de fournir une description des données représentées dans le tableau. La légende peut être placée soit en haut du tableau, soit en bas, et par défaut, elle sera toujours centrée.

Pour insérer une légende dans un tableau, utilisez la balise `<caption>`.

### Syntaxe de la légende
```html
<table>
  <caption></caption>
  <tr> </tr>
</table>
```
**Un exemple avec l'utilisation de `<caption>`**
```html
<table>
  <caption>Ressources de codage gratuites</caption>
  <tr>
    <th>Sites</th>
    <th>Chaînes YouTube</th>
    <th>Applications mobiles</th>
  </tr>
  <tr>
    <td>Freecode Camp</td>
    <td>Freecode Camp</td>
    <td>Enki</td>
  </tr>
  <tr>
    <td>W3Schools</td>
    <td>Academind</td>
    <td>Programming Hero</td>
  </tr>
  <tr>
    <td>Khan Academy</td>
    <td>The Coding Train</td>
    <td>Solo learn</td>
  </tr>
</table>
```

<table>
  <caption>Ressources de codage gratuites</caption>
  <tr>
    <th>Sites</th>
    <th>Chaînes YouTube</th>
    <th>Applications mobiles</th>
  </tr>
  <tr>
    <td>Freecode Camp</td>
    <td>Freecode Camp</td>
    <td>Enki</td>
  </tr>
  <tr>
    <td>W3Schools</td>
    <td>Academind</td>
    <td>Programming Hero</td>
  </tr>
  <tr>
    <td>Khan Academy</td>
    <td>The Coding Train</td>
    <td>Solo learn</td>
  </tr>
</table>

## Comment utiliser l'attribut Scope dans les tableaux HTML
L'attribut scope est utilisé pour définir si un en-tête spécifique est destiné à une colonne, une ligne ou un groupe des deux. Je sais que la définition peut être difficile à comprendre, mais avec l'aide d'un exemple, vous la comprendrez mieux.

Le but principal de l'élément scope est de montrer les données cibles afin que l'utilisateur n'ait pas à se fier à des suppositions. L'attribut est déclaré dans la cellule d'en-tête `<th>`, et il prend les valeurs `col`, `row`, `colgroup` et `rowgroup`.

Les valeurs `col` et `row` indiquent que la cellule d'en-tête fournit des informations pour les lignes ou les colonnes, respectivement.

### Syntaxe de Scope
```html
<table>
 <tr>
   <th scope="value">
 </tr>
</table>
```

**Un exemple avec l'utilisation de `<scope>`**
```html
<table>
  <tr>
    <th></th>
    <th scope="col">Semestre</th>
    <th scope="col">Note</th>
  </tr>

  <tr>
    <td>1</td>
    <td>Janvier - Avril</td>
    <td>Crédit</td>
  </tr>

  <tr>
    <td>2</td>
    <td>Mai - Août</td>
    <td>Passable</td>
  </tr>
    
  <tr>
    <td>2</td>
    <td>Septembre - Décembre</td>
    <td>Distinction</td>
  </tr>
</table>
```

<table>
  <tr>
    <th></th>
    <th scope="col">Semestre</th>
    <th scope="col">Note</th>
  </tr>

  <tr>
    <td>1</td>
    <td>Janvier - Avril</td>
    <td>Crédit</td>
  </tr>

  <tr>
    <td>2</td>
    <td>Mai - Août</td>
    <td>Passable</td>
  </tr>
    
  <tr>
    <td>2</td>
    <td>Septembre - Décembre</td>
    <td>Distinction</td>
  </tr>
</table>

Ce que l'attribut `scope` a fait, c'est qu'il montre si une cellule d'en-tête appartient à une colonne, une ligne ou un groupe des deux.

Dans ce cas, les en-têtes appartiennent à la colonne car c'est ce que nous avons défini dans le code. Vous pouvez jouer en changeant l'attribut pour voir les différents comportements.

## Comment utiliser la fusion de cellules dans un tableau HTML
Peut-être avez-vous rencontré des cellules qui s'étendent sur deux ou plusieurs colonnes ou lignes dans un tableau. Cela s'appelle la fusion de cellules.

Si vous avez travaillé avec des programmes comme MS Office ou Excel, vous avez probablement utilisé la fonction en surlignant les cellules et en cliquant sur la commande, et voilà ! Vous l'avez.

Les mêmes fonctionnalités peuvent être appliquées dans un tableau HTML en utilisant deux attributs de cellule, `colspan` pour la fusion horizontale et `rowspan` pour la fusion verticale. Les deux attributs sont assignés à des nombres supérieurs à zéro qui montrent le nombre de cellules que vous souhaitez fusionner.

**Un exemple avec l'utilisation de `span`**
```html
<table>
  <tr>
    <th>Nom</th>
    <th>Matière</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td rowspan = "2">Hillary</td>
    <td>Web Avancé</td>
    <td>75</td>
  </tr>
  <tr>
    <td>Système d'exploitation</td>
    <td>60</td>
  </tr>
      <tr>
    <td rowspan = "2">Lary</td>
    <td>Web Avancé</td>
    <td>80</td>
  </tr>
  <tr>
    <td>Système d'exploitation</td>
    <td>75</td>
  </tr>
  <tr>
    <td colspan="3">Moyenne totale : 72,5</td>
  </tr>
</table>
```

<table>
  <tr>
    <th>Nom</th>
    <th>Matière</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td rowspan = "2">Hillary</td>
    <td>Web Avancé</td>
    <td>75</td>
  </tr>
  <tr>
    <td>Système d'exploitation</td>
    <td>60</td>
  </tr>
      <tr>
    <td rowspan = "2">Lary</td>
    <td>Web Avancé</td>
    <td>80</td>
  </tr>
  <tr>
    <td>Système d'exploitation</td>
    <td>75</td>
  </tr>
  <tr>
     <td></td>
    <td colspan="3">Moyenne totale : 72,5</td>
  </tr>
</table>

Dans l'exemple ci-dessus, nous avons une cellule qui s'étend sur 2 cellules dans les lignes et 3 cellules dans la colonne comme indiqué. Nous avons réussi à appliquer la fusion à la fois verticalement et horizontalement.

> *Lorsque vous utilisez les attributs `colspan` et `rowspan`, assurez-vous de déclarer correctement les valeurs assignées pour éviter le chevauchement des cellules.*

## Comment ajouter un en-tête, un corps et un pied de page à un tableau HTML
Tout comme un site web ou tout autre document a trois sections principales – l'en-tête, le corps et le pied de page – il en va de même pour un tableau.

Dans un tableau, ils sont divisés en utilisant des attributs notamment :
* `<thead>` - fournit un en-tête séparé pour le tableau
* `<tbody>` - contient le contenu principal du tableau
* `<tfoot>` - crée un pied de page séparé pour le tableau

**Un exemple avec l'utilisation de `<thead>`, `<tbody>` & `<tfoot>`**
```html
<table>
  <thead>
    <tr>
      <th colspan="2">Octobre</th>
      <th colspan="2">Novembre</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Ventes</td>
      <td>Profit</td>
      <td>Ventes</td>
      <td>Profit</td>
    </tr>
    <tr>
      <td>$200,00</td>
      <td>$50,00</td>
      <td>$300,000</td>
      <td>$70,000</td>
    </tr>
  </tbody>
    
  <tfoot>
    <tr>
      <th colspan= "4">Novembre a été plus productif</th>
    </tr>
  </tfoot>
</table>
```

<table>
  <thead>
    <tr>
      <th colspan="2">Octobre</th>
      <th colspan="2">Novembre</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Ventes</td>
      <td>Profit</td>
      <td>Ventes</td>
      <td>Profit</td>
    </tr>
    <tr>
      <td>$200,00</td>
      <td>$50,00</td>
      <td>$300,000</td>
      <td>$70,000</td>
    </tr>
  </tbody>
    
  <tfoot>
    <tr>
      <th colspan= "4">Novembre a été plus productif</th>
    </tr>
  </tfoot>
</table>

Dans l'exemple ci-dessus, l'en-tête est représenté par le nom des mois, la partie avec les chiffres des ventes et des profits représente le corps du tableau, et enfin la partie avec la déclaration représente le pied de page de notre tableau.

Une autre chose importante à noter est qu'un tableau peut avoir plus d'une partie de corps. Dans un scénario comme celui-ci, chaque corps groupe les lignes qui sont liées ensemble.

## Comment styliser les tableaux HTML en utilisant CSS
Bien que les tableaux soient largement utilisés aujourd'hui, il est très rare d'en trouver un qui n'a pas été stylisé. La plupart d'entre eux utilisent différentes formes de styles, qu'il s'agisse de couleurs, de polices, de mise en évidence de valeurs importantes, etc.

Le style aide à rendre les tableaux professionnels et attrayants pour les yeux. Après tout, vous ne voudriez pas que votre lecteur fixe des données divisées par une seule ligne.

Contrairement au style avec d'autres langages ou outils, en HTML, vous devrez obtenir un fichier supplémentaire avec une extension `.css` où vous ajouterez vos styles et le lierez à votre fichier HTML.

Ci-dessous, un bac à sable de code avec un exemple de tableau stylisé est joint. N'hésitez pas à jouer avec pour voir comment différents styles affecteront l'affichage.

%[https://codepen.io/larymak/pen/BaZQGYj]

Dans le bac à sable de code ci-dessus, nous avons créé un tableau et l'avons stylisé en utilisant certaines des attributs que nous avons couverts dans l'article.

Nous l'avons stylisé en utilisant un fichier CSS, où nous avons ajouté la couleur et la bordure à notre tableau pour le rendre plus lisible et beau. Le tableau a également un en-tête fixe afin que vous puissiez faire défiler la grande quantité de données et toujours voir l'en-tête d'une colonne particulière.

Nous avons donc vu ce qu'est un tableau, nous en avons créé quelques-uns, et nous sommes même allés plus loin en appliquant un style.

Mais avoir les connaissances et ne pas savoir comment les appliquer ne sera d'aucune aide. Cela étant dit, où ou quand devez-vous utiliser des tableaux dans votre conception ?

## Quand utiliser un tableau
Il existe de nombreuses situations où les tableaux peuvent être utiles lors du développement de vos projets :
* Vous pouvez utiliser des tableaux lorsque vous souhaitez comparer et contraster des données avec des caractéristiques partagées comme les différences entre A et B ou les scores de l'équipe X par rapport à ceux de Y.
* Vous pouvez également en utiliser un si vous souhaitez donner un aperçu des données numériques. Un bon exemple de cela est lorsque vous essayez de représenter les notes des étudiants ou même les scores des équipes comme le tableau de l'EPL.
* Et un tableau peut aider les lecteurs à trouver rapidement des informations spécifiques présentées de manière claire. Par exemple, si vous parcourez une longue liste de noms, un tableau peut être utilisé pour sous-diviser la liste, ce qui la rend facile à lire.

## Conclusion
Les tableaux sont un excellent moyen de représenter des données tabulaires, et vous pouvez les créer en utilisant des éléments HTML de base comme `<table>`, `<tr>`, `<td>`.

Et vous pouvez également ajouter un peu de style pour les rendre attrayants et présenter les données clairement avec l'aide d'un fichier CSS.

Avant de conclure, faisons une dernière tâche :

Créez un tableau en utilisant ce que nous avons appris pour résumer ce que nous avons couvert dans l'article aujourd'hui. Après cela, comparez votre conception avec mon bac à sable de code épinglé ci-dessous :

%[https://codepen.io/larymak/pen/PojbMGW]