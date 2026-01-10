---
title: Menu déroulant HTML – Comment ajouter une liste déroulante avec l'élément Select
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-26T14:25:06.000Z'
originalURL: https://freecodecamp.org/news/html-drop-down-menu-how-to-add-a-drop-down-list-with-the-select-element
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--9-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Menu déroulant HTML – Comment ajouter une liste déroulante avec l'élément
  Select
seo_desc: 'Many websites, applications, and web pages use drop-down menus to help
  display a list of information. You can use them to create navigation menus, options
  for forms, and more.

  If you''re looking at some of these menus or lists, you might imagine how c...'
---

De nombreux sites web, applications et pages web utilisent des menus déroulants pour faciliter l'affichage d'une liste d'informations. Vous pouvez les utiliser pour créer des menus de navigation, des options pour les formulaires, et bien plus encore.

Si vous regardez certains de ces menus ou listes, vous pourriez imaginer à quel point leur création peut être complexe. Et oui – dans certains cas, cela devient un peu complexe.

Un menu déroulant est une liste d'options qui se révèle verticalement lorsqu'un utilisateur interagit avec le menu, soit en cliquant dessus, soit en le survolant avec son curseur.

Ce menu disparaît également lorsque l'utilisateur cesse d'interagir avec lui en cliquant à nouveau ou en éloignant le curseur du menu.

Dans cet article, vous apprendrez comment ajouter une liste déroulante à l'élément `select` sur votre page web. Vous découvrirez également les différentes options disponibles et comment créer une liste ou un menu déroulant au survol.

## Comment créer une liste déroulante HTML

En HTML, par défaut, vous pouvez toujours créer une liste déroulante avec la balise `select` accompagnée de la balise `option`. Elle est principalement utilisée dans les formulaires pour sélectionner une valeur parmi une liste de nombreuses options.

La balise `select` possède deux attributs principaux : les attributs `name` et `id`.

```html
// Syntaxe
<select name="" id="">
  <option value="">...</option>
  // ...
</select>
```

Vous utilisez l'attribut `name` pour identifier le menu déroulant lorsqu'une sélection est soumise dans un formulaire. Vous pouvez connecter l'attribut `id` à un `label` qui possède des valeurs similaires à son attribut `for`.

```html
// Syntaxe
<label for="languages">Liste de langues :</label>
<select name="" id="languages">
  <option value="">...</option>
  // ...
</select>
```

La balise `select` possède également certains attributs booléens facultatifs comme `disabled` (qui désactive les champs de sélection), `required` (qui rend le champ obligatoire dans un formulaire), et bien d'autres encore.

```html
<select name="" id="languages" required>
  // ...
</select>

// Ou

<select name="" id="languages" disabled>
  // ...
</select>
```

À l'intérieur de la balise `select`, vous pouvez ajouter de nombreuses options dans chaque balise `option` individuelle. La balise `option` possède un attribut `value` qui spécifie une valeur soumise par le formulaire lorsqu'une option est sélectionnée.

```html
<select name="language" id="language">
  <option value="javascript">JavaScript</option>
  <option value="python">Python</option>
  <option value="c++">C++</option>
  <option value="java">Java</option>
</select>
```

Il existe d'autres attributs booléens comme `disabled` (qui désactive l'option dans le menu) et `selected` (que vous utilisez pour définir une option particulière comme l'option sélectionnée par défaut lors du chargement de la page, plutôt que la première option).

```html
<select name="language" id="language">
  <option value="javascript" disabled>JavaScript</option>
  <option value="python">Python</option>
  <option value="c++">C++</option>
  <option value="java" selected>Java</option>
</select>
```

Dans le code ci-dessus, la première option a un attribut `disabled`, ce qui signifie que vous ne pourrez pas sélectionner cette option. La quatrième option a un attribut `selected`, ce qui signifie qu'au lieu d'avoir JavaScript comme valeur sélectionnée par défaut, Java sera sélectionné.

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/YzaNgmw?default-tab=html%2Cresult">
  Voir le Pen <a href="https://codepen.io/olawanlejoel/pen/YzaNgmw">
  Dropdown List</a> par Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  sur <a href="https://codepen.io">CodePen</a>.
</iframe>

## Comment créer un menu déroulant au survol

Lorsque vous parcourez ou visitez de nombreuses pages web avancées et modernes, vous remarquerez qu'elles comportent des menus déroulants.

Ces menus sont utilisés pour la navigation afin d'aider à regrouper des liens similaires. La plupart du temps, lorsque vous survolez le menu parent, la liste déroulante apparaît.

![](https://paper-attachments.dropbox.com/s_B4C6D2ADDF91C398F7D0077C06A79A5494062ED47759B85768844AD11A4B757E_1664053790313_image.png align="left")

Vous pouvez créer ces types de menus de différentes manières, car il n'existe pas de syntaxe directe pour en construire un.

Vous pouvez créer cela en utilisant le style CSS pour afficher et masquer la liste déroulante lorsque l'utilisateur survole le menu. Une très bonne approche consiste à créer une `div` qui contient le menu et la liste déroulante.

```html
<div class="dropdown">
  <button>Profil</button>
  <div class="dropdown-options">
    <a href="#">Tableau de bord</a>
    <a href="#">Paramètres</a>
    <a href="#">Déconnexion</a>
  </div>
</div>
```

Cette `div` sert de conteneur et vous pouvez la styliser avec une `position` `relative` et un `display` `inline-block`, afin que les options déroulantes apparaissent sous le menu.

```css
.dropdown {
  display: inline-block;
  position: relative;
}
```

Vous pouvez styliser votre bouton et les `dropdown-options` comme vous le souhaitez. Mais le style principal qui contrôle l'effet de survol, par défaut, définit `dropdown-options` sur `display: none`. Ensuite, lorsqu'une souris survole le menu, l'affichage passe à `block`, de sorte que les options deviennent visibles. Vous définissez également la `position` sur `absolute`, pour que les options apparaissent sous le menu, et `overflow` sur `auto` pour permettre le défilement sur les petits écrans.

```css
.dropdown-options {
  display: none;
  position: absolute;
  overflow: auto;
}

.dropdown:hover .dropdown-options {
  display: block;
}
```

Dans la démo ci-dessous, nous ajoutons plus de styles pour rendre le menu déroulant plus attrayant et agréable :

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/ZExZGdK?default-tab=html%2Cresult">
  Voir le Pen <a href="https://codepen.io/olawanlejoel/pen/ZExZGdK">
  Hoverable dropdown menu</a> par Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  sur <a href="https://codepen.io">CodePen</a>.
</iframe>

## Conclusion

Dans cet article, vous avez appris comment créer une liste déroulante avec la balise `select`. Vous avez également appris comment créer le menu déroulant au survol avec CSS pour gérer l'effet de survol.

Vous pouvez en savoir plus sur la balise `select` dans [cet article sur **la balise HTML Select – Comment créer un menu déroulant ou une liste combinée**](https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/) par [Kolade](https://www.freecodecamp.org/news/author/kolade/).