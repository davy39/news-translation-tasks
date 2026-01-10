---
title: Formulaire HTML – Exemple de type d'entrée et de bouton de soumission
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-12T15:17:38.000Z'
originalURL: https://freecodecamp.org/news/html-form-input-type-and-submit-button-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/form-1.png
tags:
- name: CSS
  slug: css
- name: forms
  slug: forms
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Formulaire HTML – Exemple de type d'entrée et de bouton de soumission
seo_desc: 'Forms are one of the most important parts of the web. Without them, there
  wouldn''t be an easy way to collect data, search for resources, or sign up to receive
  valuable information.

  You can embed forms on websites with the HTML form element. Inside th...'
---

Les formulaires sont l'une des parties les plus importantes du web. Sans eux, il n'y aurait pas de moyen facile de collecter des données, de rechercher des ressources ou de s'inscrire pour recevoir des informations précieuses.

Vous pouvez intégrer des formulaires sur des sites web avec l'élément HTML `form`. À l'intérieur de l'élément de formulaire, plusieurs entrées sont imbriquées. Ces entrées sont également connues sous le nom de contrôles de formulaire.

Dans ce tutoriel, nous allons explorer l'élément de formulaire HTML, les différents types d'entrées qu'il accepte et comment créer un bouton de soumission avec lequel les données sont soumises.

À la fin, vous saurez comment fonctionnent les formulaires et vous serez en mesure de les créer en toute confiance.

## Syntaxe de base du formulaire HTML

```html
<form action="mywebsite.com" method="POST">
    <!--Les entrées de n'importe quel type et les zones de texte vont ici-->
</form>
```


## Types d'entrée de formulaire HTML

Vous utilisez la balise `<input>` pour créer divers contrôles de formulaire en HTML. C'est un élément en ligne et il prend des attributs tels que `type`, `name`, `minlength`, `maxlength`, `placeholder`, et ainsi de suite. Chacun de ces attributs a des valeurs spécifiques qu'ils prennent.

L'attribut `placeholder` est important car il aide l'utilisateur à comprendre le but du champ d'entrée avant qu'il ne tape quoi que ce soit.

Il existe 20 types d'entrée différents, et nous allons les examiner un par un.

### Type Texte

Ce type d'entrée prend une valeur de « text », il crée donc une seule ligne de saisie de texte.

```html
<input type="text" placeholder="Entrez le nom" />
```

Une entrée avec le type de texte ressemble à la capture d'écran ci-dessous :
![textInput](https://www.freecodecamp.org/news/content/images/2021/08/textInput.png)

### Type Mot de passe

Comme son nom l'indique, une entrée avec un type de mot de passe crée un mot de passe. Il est automatiquement invisible pour l'utilisateur, sauf s'il est manipulé par JavaScript.

```html
<input type="password" placeholder="Entrez votre mot de passe" />
```

![passwordInput](https://www.freecodecamp.org/news/content/images/2021/08/passwordInput.png)

### Type Email

Toute entrée avec le type email définit un champ pour saisir une adresse email.

```html
<input type="email" placeholder="Entrez votre email" />
```

![typeEmail](https://www.freecodecamp.org/news/content/images/2021/08/typeEmail.png)

### Type Nombre

Ce type d'entrée permet à l'utilisateur d'insérer uniquement des nombres.

```html
<input type="number" placeholder="Entrez un nombre" />
```

![numberInput](https://www.freecodecamp.org/news/content/images/2021/08/numberInput.png)

### Type Radio

Parfois, les utilisateurs devront choisir une option parmi de nombreuses. Un champ d'entrée avec ses attributs de type définis sur « radio » vous permet de faire cela.

```html
<input type="radio" />
```

![typeRadio](https://www.freecodecamp.org/news/content/images/2021/08/typeRadio.png)

### Type Case à cocher

Ainsi, avec un type d'entrée radio, les utilisateurs pourront choisir une option parmi de nombreuses. Que faire si vous voulez qu'ils choisissent autant d'options que possible ? C'est ce que fait une entrée avec un attribut de type défini sur `checkbox`.

```html
<input type="checkbox" />
```

![typeCheckbox](https://www.freecodecamp.org/news/content/images/2021/08/typeCheckbox.png)

### Type Soumettre

Vous utilisez ce type pour ajouter un bouton de soumission aux formulaires. Lorsque l'utilisateur clique dessus, il soumet automatiquement le formulaire. Il prend un attribut de valeur, qui définit le texte qui apparaît à l'intérieur du bouton.

```html
<input type="submit" value="Entrez pour gagner" />
```

![typeSubmit](https://www.freecodecamp.org/news/content/images/2021/08/typeSubmit.png)

### Type Bouton

Une entrée avec un type défini sur bouton crée un bouton, qui peut être manipulé par le type d'écouteur d'événements onClick de JavaScript. Il crée un bouton tout comme un type d'entrée de soumission, mais avec l'exception que la valeur est vide par défaut, donc elle doit être spécifiée.

```html
<input type="button" value="Soumettre" />
```

![typeButton](https://www.freecodecamp.org/news/content/images/2021/08/typeButton.png)

### Type Fichier

Cela définit un champ pour la soumission de fichiers. Lorsque l'utilisateur clique dessus, il est invité à insérer le type de fichier souhaité, qui peut être une image, un PDF, un fichier document, etc.

```html
<input type="file" />
```

Le résultat d'un type d'entrée de fichier ressemble à ceci :

![fileInput](https://www.freecodecamp.org/news/content/images/2021/08/fileInput.png)

### Type Couleur

C'est un type d'entrée fantaisiste introduit par HTML5. Avec lui, l'utilisateur peut soumettre sa couleur préférée par exemple. Le noir (#000000) est la valeur par défaut, mais peut être remplacé en définissant la valeur sur une couleur souhaitée.

De nombreux développeurs l'ont utilisé comme une astuce pour sélectionner différentes nuances de couleurs disponibles en RGB, HSL et formats alphanumériques.

```html
<input type="color" />
```

Voici le résultat d'un type d'entrée de couleur :

![colorInput](https://www.freecodecamp.org/news/content/images/2021/08/colorInput.png)

### Type Recherche

L'entrée avec le type de recherche définit un champ de texte tout comme un type d'entrée de texte. Mais cette fois, il a pour seul but de rechercher des informations. Il est différent du type texte en ce sens qu'un bouton d'annulation apparaît une fois que l'utilisateur commence à taper.

```html
<input type="search" />
```

![typeSearch](https://www.freecodecamp.org/news/content/images/2021/08/typeSearch.png)

### Type URL

Lorsque l'attribut de type d'une balise d'entrée est défini sur URL, il affiche un champ où les utilisateurs peuvent entrer une URL.

```html
<input type="url" />
```

![typeURL](https://www.freecodecamp.org/news/content/images/2021/08/typeURL.png)

### Type Tel

Un type d'entrée tel vous permet de collecter des numéros de téléphone auprès des utilisateurs.

```html
<input type="tel" />
```

![typeTel](https://www.freecodecamp.org/news/content/images/2021/08/typeTel.png)

### Type Date

Vous avez peut-être enregistré sur un site web où vous avez demandé la date d'un certain événement. Le site a probablement utilisé une entrée avec la valeur de type définie sur date pour y parvenir.

```html
<input type="date" />
```

Voici à quoi ressemble une entrée avec le type date :

![dateInput](https://www.freecodecamp.org/news/content/images/2021/08/dateInput.png)

### Type Datetime-local

Cela fonctionne comme le type d'entrée date, mais il permet également à l'utilisateur de choisir une date avec une heure particulière.

```html
<input type="datetime-local" />
```

![datelocalInput](https://www.freecodecamp.org/news/content/images/2021/08/datelocalInput.png)

### Type Semaine

Le type d'entrée de semaine permet à un utilisateur de sélectionner une semaine spécifique.

```html
<input type="week" />
```

![weekInput](https://www.freecodecamp.org/news/content/images/2021/08/weekInput.png)

### Type Mois

L'entrée avec le type de mois remplit les mois pour que l'utilisateur puisse choisir parmi eux lorsqu'il clique.

```html
<input type="month" />
```

![monthInput](https://www.freecodecamp.org/news/content/images/2021/08/monthInput.png)

### Textarea

Il arrive que l'utilisateur doive remplir plusieurs lignes de texte qui ne seraient pas adaptées à un type d'entrée de texte (car il spécifie un champ de texte d'une seule ligne).

`textarea` permet à l'utilisateur de le faire car il définit plusieurs lignes de saisie de texte. Il prend ses propres attributs tels que `cols` – pour le nombre de colonnes, et `rows` pour le nombre de lignes.

```html
<textarea cols="50" rows="20"></textarea>
```

![textarea](https://www.freecodecamp.org/news/content/images/2021/08/textarea.png)

### Boîte de sélection multiple

Cela ressemble à un bouton radio et à une case à cocher en un seul package. Il est intégré dans la page avec deux éléments – un élément `select` et une `option`, qui est toujours imbriquée à l'intérieur de `select`.

Par défaut, l'utilisateur ne peut choisir qu'une seule des options. Mais avec les attributs multiples, vous pouvez permettre à l'utilisateur de sélectionner plus d'une des options.

```html
<select>
      <option value="HTML">Sélectionnez une langue</option>
      <option value="HTML">HTML</option>
      <option value="CSS">CSS</option>
      <option value="JavaScript">JavaScript</option>
      <option value="React">React</option>
</select>
```

![selectDemo](https://www.freecodecamp.org/news/content/images/2021/08/selectDemo.gif)

## Comment étiqueter les entrées HTML

Attribuer des étiquettes aux contrôles de formulaire est important. Lorsqu'elles sont correctement connectées au champ d'entrée via leur attribut `for` et l'attribut `id` de l'entrée, il est plus facile pour l'utilisateur de les utiliser car il peut simplement cliquer sur l'étiquette elle-même pour accéder à l'entrée.

```html
<label for="name">Nom</label>
<input type="text" id="name" /> <br />
<label for="check">Accepter les termes</label>
<input type="checkbox" id="check" />
```

![labelDemo](https://www.freecodecamp.org/news/content/images/2021/08/labelDemo.gif)

## Comment fonctionnent les formulaires HTML

Lorsque l'utilisateur remplit un formulaire et le soumet avec le bouton de soumission, les données des contrôles de formulaire sont envoyées au serveur via les méthodes de requête HTTP `GET` ou `POST`.

Alors, comment le serveur est-il indiqué ? L'élément de formulaire prend un attribut d'action, dont la valeur doit être spécifiée à l'URL du serveur. Il prend également un attribut de méthode, où la méthode HTTP qu'il utilise pour transmettre les valeurs au serveur est spécifiée.

Cette méthode pourrait être `GET` ou `POST`. Avec la méthode `GET`, les valeurs saisies par l'utilisateur sont visibles dans l'URL lorsque les données sont soumises. Mais avec `POST`, les valeurs sont envoyées dans les en-têtes HTTP, donc ces valeurs ne sont pas visibles dans l'URL.

Si un attribut de méthode n'est pas utilisé dans le formulaire, il est automatiquement supposé que l'utilisateur souhaite utiliser la méthode GET, car c'est la méthode par défaut.

Alors, quand devez-vous utiliser la méthode `GET` ou `POST` ? Utilisez la méthode `GET` pour soumettre des données non sensibles ou récupérer des données d'un serveur (par exemple, lors de recherches). Utilisez la requête `POST` lors de la soumission de fichiers ou de données sensibles.

## Mini Projet : Construire un formulaire de contact de base

Prenons ce que nous avons appris sur les formulaires et utilisons-le pour créer un simple formulaire de contact. Je vais également introduire quelques nouveaux concepts au fur et à mesure pour compléter le tout.

### Voici le HTML :

```html
<form action="example-server.com">
      <fieldset>
        <legend>Contactez-moi</legend>
        <div class="form-control">
          <label for="name">Nom</label>
          <input type="name" id="name" placeholder="Entrez votre nom" required />
        </div>

        <div class="form-control">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            placeholder="Entrez votre email"
            required
          />
        </div>

        <div class="form-control">
          <label for="message">Message</label>
          <textarea
            id="message"
            cols="30"
            rows="10"
            placeholder="Entrez votre message"
            required
          ></textarea>
        </div>
        <input type="submit" value="Envoyer" class="submit-btn" />
      </fieldset>
</form>
```

#### Que se passe-t-il dans ce code HTML ?

Tout d'abord, un élément `form` enveloppe tous les autres éléments. Il a une action définie sur « example-server.com », un serveur factice où les données du formulaire seront reçues.

Après l'élément de formulaire, tous les autres éléments sont également entourés par un élément `fieldset` avec une balise `legend` juste en dessous.

Nous utilisons l'élément `fieldset` pour regrouper les entrées connexes, et la balise `legend` contient une légende indiquant de quoi parle le formulaire.

Les entrées `name`, `email` et `textarea` sont toutes dans une `div` avec une classe de form-control. Ainsi, ils se comportent comme un élément de bloc, afin de faciliter le style avec CSS.

Ils sont également validés avec l'attribut `required`, donc le formulaire échoue à la soumission lorsque ces champs sont vides ou lorsque l'utilisateur ne tape pas les valeurs dans le format approprié.

Après tout cela, nous aurons le résultat dans la capture d'écran ci-dessous :
![unstyledForm](https://www.freecodecamp.org/news/content/images/2021/08/unstyledForm.png)

Comme c'est moche ! Nous devons appliquer un peu de style !

### Voici le CSS :

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-family: cursive;
  }

 input,
    textarea {
    width: 100%;
    padding: 5px;
    outline: none;
  }

  label {
    line-height: 1.9rem;
  }

  input[type="submit"] {
   transform: translate(2.2%);
   padding: 3px;
   margin-top: 0.6rem;
   font-family: cursive;
   font-weight: bold;
  }

 fieldset {
   padding: 20px 40px;
 }
```

#### Que fait le code CSS ici ?

Nous centrons tout dans le corps horizontalement avec Flexbox, et verticalement avec une hauteur de viewport de 100 %. Nous avons utilisé une famille de polices cursive.

Nous avons donné aux entrées et à `textarea` une largeur de 100 % pour qu'ils aillent jusqu'au bout. Les étiquettes ont obtenu une hauteur de ligne minimale de 1,9rem (30,4px), pour qu'elles ne restent pas trop proches de leurs entrées respectives.

Nous avons spécifiquement stylisé le bouton (type de bouton d'entrée) avec la propriété transform pour le pousser au centre car il était un peu décentré. Nous lui avons donné un remplissage de 3px pour plus d'espacement autour. Nous avons ensuite sélectionné une famille de polices cursive pour lui avec un poids en gras.

Parce que le bouton était trop proche de la `textarea`, nous avons défini une marge supérieure de 0,6rem pour le pousser un peu vers le bas.

Nous avons donné à notre élément fieldset un remplissage de 20px en haut et en bas, avec 40px à gauche et à droite pour éloigner la bordure qu'il crée autour des éléments `form` qu'il enveloppe.

À la fin de tout cela, nous avons le beau formulaire ci-dessous :
![styledForm](https://www.freecodecamp.org/news/content/images/2021/08/styledForm.png)

## Conclusion

J'espère que ce tutoriel vous a aidé à comprendre comment fonctionnent les formulaires. Maintenant, vous devriez avoir les connaissances nécessaires pour intégrer des formulaires dans vos sites web afin de commencer à collecter des données.

Merci d'avoir lu, et continuez à coder.