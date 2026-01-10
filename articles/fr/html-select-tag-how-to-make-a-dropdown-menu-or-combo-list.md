---
title: Balise HTML Select – Comment créer un menu déroulant ou une liste combinée
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-03T15:03:03.000Z'
originalURL: https://freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/HTML-select-tag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Balise HTML Select – Comment créer un menu déroulant ou une liste combinée
seo_desc: 'You use the HTML select tag to create drop-down menus so that users can
  select the value they want. It is an instrumental feature in collecting data to
  be sent to a server.

  The select tag normally goes within a form element, with the items to choose ...'
---

Vous utilisez la balise HTML select pour créer des menus déroulants afin que les utilisateurs puissent sélectionner la valeur qu'ils souhaitent. C'est une fonctionnalité très utile pour collecter des données à envoyer à un serveur.

La balise select est généralement placée dans un élément de formulaire, avec les éléments à choisir codés dans une autre balise, `<option>`. Elle peut également être un élément autonome, toujours associé à un formulaire avec l'un de ses attributs spéciaux, `form`.

Dans ce tutoriel, je vais vous guider à travers la création d'un menu déroulant avec la balise select afin que vous puissiez commencer à l'utiliser pour collecter des données dans vos projets de codage. Je vais également aborder comment styliser la balise select, car elle est notoirement difficile à styliser.

### Voici un Scrim interactif sur comment créer un menu déroulant ou une liste combinée en HTML

<iframe src="https://scrimba.com/scrim/co5b3416fb871e72f3c8e1e76?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## Attributs de la balise Select

Avant de plonger dans la création d'un menu déroulant avec la balise select, nous devons discuter des attributs que la balise select prend.

Voici ses attributs :

- name : Vous devez attacher le nom à chaque contrôle de formulaire car il est utilisé pour référencer les données après leur soumission au serveur.
- multiple : Cet attribut permet à l'utilisateur de sélectionner plusieurs options dans le menu déroulant.
- required : Cela est généralement utilisé pour la validation. Avec cela, le formulaire ne sera pas soumis à moins qu'un utilisateur ne sélectionne au moins une option dans le menu déroulant.
- disabled : Cet attribut empêche l'utilisateur d'interagir avec les options.
- size : Exprimé en nombres, l'attribut size est utilisé pour spécifier combien d'options seront visibles à la fois.
- autofocus : Cet attribut est utilisé sur toutes les entrées de formulaire, y compris select, pour spécifier que l'entrée doit être mise au point lorsque la page se charge.

## Comment créer un menu déroulant avec la balise Select

Pour créer un menu déroulant avec la balise select, vous avez d'abord besoin d'un élément de formulaire. Cela est dû au fait que vous aurez également un bouton de soumission dans celui-ci (l'élément de formulaire) afin de soumettre les données au serveur.

```html
<form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang">
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```

J'ai ajouté un peu de CSS pour centrer le menu déroulant et le bouton, et donner au corps un fond gris clair :

```css
body {
     display: flex;
     align-items: center;
     justify-content: center;
     margin: 0 auto;
     height: 100vh;
     background-color: #f1f1f1;
   }

input {
     display: flex;
     align-items: center;
     justify-content: center;
     margin: 0 auto;
   }
```

Pour le rendre plus élaboré et accessible, vous pouvez également attacher la boîte de sélection à un élément de label, afin qu'elle soit mise au point lorsque le texte du label est cliqué. Vous pouvez faire cela avec ce code :

```html
<form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang">
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```
J'ai mis un symbole de numéro (#) comme valeur de l'attribut action afin que vous n'obteniez pas une erreur 404 lorsque vous cliquez sur le bouton de soumission.

Mais maintenant, nous devons apporter une petite modification au CSS :

```css
 body {
     display: flex;
     align-items: center;
     justify-content: center;
     margin: 0 auto;
     height: 100vh; 
     background-color: #f1f1f1;
   }

input {
     display: flex;
     align-items: center;
     justify-content: center;
     margin: 0 auto;
   }

label {
     display: flex;
     align-items: center;
     justify-content: center;
     margin: 0 auto;
   }

select {
     margin-bottom: 10px;
     margin-top: 10px;
   }
```

En fin de compte, voici le résultat :

![select-one](https://www.freecodecamp.org/news/content/images/2021/09/select-one.gif)

Ce n'est pas tout. L'un des éléments du menu déroulant apparaît par défaut et sera sélectionné si l'utilisateur clique sur le bouton de soumission immédiatement lorsqu'il arrive sur la page.

Mais ce n'est pas une bonne expérience utilisateur. Vous pouvez vous en débarrasser en codant « sélectionnez un langage » comme premier élément du menu déroulant.

```html 
 <form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang">
        <option value="select">Sélectionnez un langage</option>
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```

Lorsque l'utilisateur clique sur la boîte de sélection pour sélectionner un élément, le menu déroulant couvre également le bouton de soumission – une autre chose qui affecte négativement la bonne expérience utilisateur.

Vous pouvez changer cela avec l'attribut `size`, qui affichera un certain nombre d'éléments par défaut et affichera un défilement pour les autres éléments dans le menu déroulant.

Cela vous permet également de vous débarrasser du premier élément factice, car certains des éléments seront visibles pour l'utilisateur automatiquement.

```html
 <form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang" size="4">
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```

![select-two](https://www.freecodecamp.org/news/content/images/2021/09/select-two.gif)

Avec l'attribut `multiple`, vous pouvez permettre à l'utilisateur de sélectionner plusieurs éléments dans le menu déroulant.

```html 
 <form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang" multiple>
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```

Cela rend 4 éléments visibles par défaut. Pour sélectionner plusieurs éléments, l'utilisateur doit maintenir la touche shift ou ctrl enfoncée, puis sélectionner avec la souris.

![select-three](https://www.freecodecamp.org/news/content/images/2021/09/select-three.gif)

Ce n'est pas tout ce que vous pouvez faire avec les balises select et `<option>`. Vous pouvez également créer une boîte de sélection à plusieurs niveaux avec l'élément `<optgroup>` à l'intérieur d'une balise `<select>`.

Vous pouvez convertir le menu déroulant déjà créé en une boîte de sélection à plusieurs niveaux comme ceci :

```html
<form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang">
        <optgroup label="first-choice">
          <option value="select">Sélectionnez un langage</option>
          <option value="javascript">JavaScript</option>
          <option value="php">PHP</option>
          <option value="java">Java</option>
          <option value="golang">Golang</option>
        </optgroup>
        <optgroup label="second-choice">
          <option value="python">Python</option>
          <option value="c#">C#</option>
          <option value="C++">C++</option>
          <option value="erlang">Erlang</option>
        </optgroup>
      </select>
      <input type="submit" value="Submit" />
</form>
```

![multi-select](https://www.freecodecamp.org/news/content/images/2021/09/multi-select.png)

## Comment styliser l'élément Select

Styliser l'élément select est souvent confus et se rend de manière incohérente dans les navigateurs. Mais vous pouvez toujours essayer ce qui suit :

```html
 <form action="#">
      <label for="lang">Langage</label>
      <select name="languages" id="lang">
        <option value="select">Sélectionnez un langage</option>
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
```

```css
 select {
        margin-bottom: 10px;
        margin-top: 10px;
        font-family: cursive, sans-serif;
        outline: 0;
        background: #2ecc71;
        color: #fff;
        border: 1px solid crimson;
        padding: 4px;
        border-radius: 9px;
      }
```


Dans l'extrait de code CSS ci-dessus, j'ai donné au texte dans la boîte de sélection l'apparence suivante :

* une famille de polices cursive et une couleur blanche,
* un contour de 0 pour supprimer le contour disgracieux lorsqu'il est mis au point,
* un fond verdâtre,
* une bordure de 1 pixel de couleur cramoisie,
* un rayon de bordure de 4 pixels pour obtenir une bordure légèrement arrondie sur tous les côtés,
* et un remplissage de 4 pixels pour espacer un peu les choses.

La boîte de sélection a maintenant meilleure apparence :
![select-styled](https://www.freecodecamp.org/news/content/images/2021/09/select-styled.gif)

## Conclusion

La balise select est très utile lorsque vous créez des menus déroulants et des listes combinées en HTML. C'est comme un bouton radio et une case à cocher en un seul package.

Rappelez-vous qu'avec les boutons radio, vous ne pouvez sélectionner qu'un seul élément dans une liste – mais avec une case à cocher, vous pouvez sélectionner plusieurs éléments. Select est plus flexible, car vous pouvez le configurer pour accepter un seul élément ou plusieurs éléments.

Un problème avec la balise select est qu'elle est très difficile à styliser. Une solution raisonnable est d'utiliser une bibliothèque CSS qui offre de grandes classes utilitaires pour styliser un formulaire ainsi que l'élément select.

J'espère que ce tutoriel vous a rendu plus familier avec la balise select afin que vous puissiez commencer à l'utiliser dans vos projets.

Merci d'avoir lu et continuez à coder.