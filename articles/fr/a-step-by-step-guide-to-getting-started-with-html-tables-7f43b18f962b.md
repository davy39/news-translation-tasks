---
title: Un guide étape par étape pour commencer avec les tableaux HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:06:12.000Z'
originalURL: https://freecodecamp.org/news/a-step-by-step-guide-to-getting-started-with-html-tables-7f43b18f962b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NmvyJ4xEENdOUXBvmbHgpg.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Un guide étape par étape pour commencer avec les tableaux HTML
seo_desc: 'By Abhishek Jakhar

  Overview

  The web is filled with information like football scores, cricket scores, lists of
  employee names and email addresses. HTML tables enable you to display information
  in what is commonly known as tabular data.


  NOTE: I have a...'
---

Par Abhishek Jakhar

#### Aperçu

Le web est rempli d'informations comme les scores de football, les scores de cricket, les listes de noms d'employés et d'adresses e-mail. Les tableaux HTML vous permettent d'afficher des informations sous forme de **données tabulaires**. 

> **NOTE :** J'ai déjà ajouté le style en utilisant CSS, donc mes éléments auront une apparence différente. Mais ils fonctionneront exactement de la même manière.  
> Si vous voulez que vos éléments ressemblent aux miens, vous pouvez trouver mon fichier CSS dans les liens donnés ci-dessous :  
> **CSS :** [https://gist.github.com/abhishekjakhar/2ea51dfc0dcf6f6ed0d44ac0e72f9c54](https://gist.github.com/abhishekjakhar/2ea51dfc0dcf6f6ed0d44ac0e72f9c54)

#### Tableau de base

Nous pouvons créer un tableau HTML en utilisant l'élément table. Il a une balise d'ouverture et de fermeture, et il enveloppe toutes les **lignes de tableau** et **cellules de tableau** à l'intérieur. 

```
<table></table>
```

Maintenant, tapons une ligne de tableau. Les tableaux sont composés de lignes d'informations qui traversent la page. Un élément **<tr>** est utilisé pour créer une ligne de tableau. 

Cependant, il n'y a pas d'élément pour la colonne de tableau. Les **colonnes de tableau** dépendent du nombre de **cellules de tableau** qui se trouvent **à l'intérieur de chaque ligne**. Un élément **<td>** est utilisé pour créer une cellule de tableau. Donc, en gros, le nombre d'éléments <td> que vous allez ajouter à l'intérieur de l'élément <tr> est exactement le même nombre de colonnes que vous allez obtenir à l'intérieur de votre ligne de tableau. 

Pour récapituler :

* **<table>** : L'élément de tableau représente des données sous forme de séries de lignes et de colonnes. Les tableaux ne doivent être utilisés que pour afficher des données tabulaires, et jamais pour la mise en page. 
* **<tr>** : L'élément de ligne de tableau définit une ligne de cellules dans un tableau. Les lignes de tableau peuvent être remplies avec des cellules de tableau et des cellules d'en-tête de tableau. 
* **<td>** : L'élément de cellule de tableau contient des données et représente une seule cellule de tableau. Chaque cellule de tableau doit être à l'intérieur d'une ligne de tableau. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*yOyJaEaHDXFPhiYsCAa_Pg.png)
_**ligne de tableau (&lt;tr&gt;) et cellule de tableau (&lt;td&gt;) ensemble pour former un tableau**_

> **Note :** Les éléments <table> n'ont pas d'attributs. Si vous avez déjà travaillé avec des tableaux, vous avez peut-être utilisé certains attributs par le passé. Cependant, ils sont tous désormais obsolètes. 

#### Élément d'en-tête de tableau

Nous avons créé un tableau de base, mais il n'est pas clair que notre première ligne dans le tableau est en fait une tentative de labelliser chacune de nos colonnes. Pour l'instant, la première ligne ressemble simplement à une autre ligne dans notre tableau. 

Nous pouvons utiliser un **élément d'en-tête de tableau** sur chacune de ces trois colonnes pour indiquer au navigateur, aux robots des moteurs de recherche et aux lecteurs d'écran que ce sont en fait des en-têtes et non pas simplement des données régulières. 

Maintenant, nous allons changer les cellules de tableau de la première ligne en cellules d'en-tête de tableau. Pour ce faire, nous allons remplacer **<td>** par **<th>**. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*w9jJlM8jiASJryGjS0Exaw.png)
_**Le texte de la première ligne est plus gras que les autres lignes grâce à l'élément &lt;th&gt; utilisé à l'intérieur du premier &lt;tr&gt;**_

#### En-tête et corps du tableau

De manière similaire à la structure de notre document HTML, où nous avons un en-tête et un corps, nous pouvons également ajouter un en-tête et un corps à notre tableau. Nous n'utiliserons certainement pas les mêmes éléments HTML car alors la syntaxe deviendrait invalide. Pour le tableau, nous avons **<thead>** pour l'en-tête et **<tbody>** pour le corps. 

* **<thead>** — L'élément d'en-tête de tableau (à ne pas confondre avec l'élément de cellule d'en-tête de tableau) définit un ensemble de lignes qui composent l'en-tête d'un tableau. 
* **<tbody>** — L'élément de corps de tableau définit une ou plusieurs lignes qui composent le contenu principal (ou « corps ») d'un tableau. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*j8s-VYH2HgcKHC7F5Ir4xA.png)
_**en-tête de tableau (&lt;thead&gt;) et corps de tableau (&lt;tbody&gt;) éléments**_

#### Élément de pied de tableau

Nous avons un **en-tête de tableau** et un **corps de tableau**. Donc, bien sûr, il y a aussi un **pied de tableau**. Mais la question est, quel est l'intérêt de l'élément de pied de tableau alors que nous avons déjà les en-têtes de tableau qui étiquetent les colonnes ? 

En général, un élément de pied de tableau doit **contenir un résumé du tableau**. Cela peut être quelques cellules finales contenant des sommes, des totaux et des moyennes pour chaque colonne. Il peut également contenir des méta-informations comme des informations de copyright ou la source des données dans un tableau. 

Maintenant, vous pourriez penser que le pied de tableau devrait aller en bas du tableau. Cependant, il devrait en fait aller **juste après** l'élément **en-tête de tableau** et **juste avant** l'élément **corps de tableau**. 

* **<tfoot>** — L'élément de pied de tableau définit un ensemble de lignes résumant les colonnes du tableau. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*gAmY0_Zv-Lo4LCeKLbgmgg.png)
_**pied de tableau (&lt;tfoot&gt;) élément**_

#### Élément de légende

Cet élément est essentiellement un titre pour le tableau, et il doit venir immédiatement après la balise d'ouverture du tableau. C'est bien à ajouter car il résume rapidement ce que peut contenir un tableau. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*uDdPUgPmOUt_nm1_XgUs0w.png)

Nous avons maintenant couvert les éléments essentiels des tableaux en HTML. 

Vous pouvez en apprendre plus sur les **tableaux** dans les **liens** donnés ci-dessous. 

[**Les bases des tableaux HTML**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)  
[_Cela résume à peu près les bases des tableaux HTML._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)[**Tableaux HTML avancés**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)   
[_Il y a quelques autres choses que vous pourriez apprendre sur les tableaux HTML._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)

J'espère que vous avez trouvé cet article informatif et utile. J'adorerais avoir votre retour ! 

**Merci d'avoir lu !**