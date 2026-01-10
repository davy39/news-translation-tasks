---
title: Comment télécharger un ou plusieurs fichiers facilement avec FormData
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-21T20:53:42.000Z'
originalURL: https://freecodecamp.org/news/formdata-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca151740569d1a4ca4deb.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment télécharger un ou plusieurs fichiers facilement avec FormData
seo_desc: 'By Ahmed Bouchefra

  In this post, we''ll learn about the FormData interface available in modern web
  browsers as a part of the HTML5 spec.

  We''ll see examples of using FormData with Ajax, Angular 7, Ionic and React.

  What''s FormData

  FormData is simply a d...'
---

Par Ahmed Bouchefra

Dans cet article, nous allons apprendre à utiliser l'interface FormData disponible dans les [navigateurs web modernes](http://caniuse.com/#feat=xhr2) dans le cadre de la spécification HTML5.

Nous verrons des exemples d'utilisation de FormData avec Ajax, Angular 7, Ionic et React.

## Qu'est-ce que FormData

FormData est simplement une structure de données qui peut être utilisée pour stocker des paires clé-valeur. Comme son nom l'indique, elle est conçue pour contenir des données de formulaires, c'est-à-dire que vous pouvez l'utiliser avec JavaScript pour créer un objet qui correspond à un formulaire HTML. Elle est surtout utile lorsque vous devez envoyer des données de formulaire à des points de terminaison d'API RESTful, par exemple pour télécharger un ou plusieurs fichiers en utilisant l'interface `XMLHttpRequest`, l'API `fetch()` ou Axios.

Vous pouvez créer un objet FormData en instanciant l'interface FormData à l'aide de l'opérateur `new` comme suit :

```js
const formData = new FormData()

```

La référence `formData` fait référence à une instance de FormData. Vous pouvez appeler de nombreuses méthodes sur l'objet pour ajouter et travailler avec des paires de données. Chaque paire a une clé et une valeur.

Voici les méthodes disponibles sur les objets FormData :

* `append()` : utilisée pour ajouter une paire clé-valeur à l'objet. Si la clé existe déjà, la valeur est ajoutée à la valeur d'origine pour cette clé,
* `delete()` : utilisée pour supprimer une paire clé-valeur,
* `entries()` : retourne un objet Iterator que vous pouvez utiliser pour parcourir la liste des paires clé-valeur dans l'objet,
* `get()` : utilisée pour retourner la valeur d'une clé. Si plusieurs valeurs sont ajoutées, elle retourne la première valeur,
* `getAll()` : utilisée pour retourner toutes les valeurs pour une clé spécifiée,
* `has()` : utilisée pour vérifier s'il y a une clé,
* `keys()` : retourne un objet Iterator que vous pouvez utiliser pour lister les clés disponibles dans l'objet,
* `set()` : utilisée pour ajouter une valeur à l'objet, avec la clé spécifiée. Cela va remplacer la valeur si une clé existe déjà,
* `values()` : retourne un objet Iterator pour les valeurs de l'objet FormData.

## Exemple de téléchargement de fichier avec JavaScript Vanilla

Voyons maintenant un exemple simple de téléchargement de fichier en utilisant JavaScript Vanilla, `XMLHttpRequest` et `FormData`.

Accédez à votre dossier de travail et créez un fichier `index.html` avec le contenu suivant :

```html
<!DOCTYPE html>
<html>

<head>
	<title>Parcel Sandbox</title>
	<meta charset="UTF-8" />
</head>

<body>
	<div id="app"></div>

	<script src="index.js">
	</script>
</body>

</html>

```

Nous créons simplement un document HTML avec une `<div>` identifiée par l'ID `app`. Ensuite, nous incluons le fichier `index.js` en utilisant une balise `<script>`.

Ensuite, créez le fichier `index.js` et ajoutez le code suivant :

```js
document.getElementById("app").innerHTML = `
<h1>Exemple de téléchargement de fichier & FormData</h1>
<div>
<input type="file" id="fileInput" />
</div>
`;

const fileInput = document.querySelector("#fileInput");

const uploadFile = file => {
  console.log("Téléchargement du fichier...");
  const API_ENDPOINT = "https://file.io";
  const request = new XMLHttpRequest();
  const formData = new FormData();

  request.open("POST", API_ENDPOINT, true);
  request.onreadystatechange = () => {
    if (request.readyState === 4 && request.status === 200) {
      console.log(request.responseText);
    }
  };
  formData.append("file", file);
  request.send(formData);
};

fileInput.addEventListener("change", event => {
  const files = event.target.files;
  uploadFile(files[0]);
});

```

Nous insérons d'abord un élément `<input type="file" id="fileInput" />` dans notre page HTML. Cela sera utilisé pour sélectionner le fichier que nous allons télécharger.

Ensuite, nous interrogeons l'élément d'entrée de fichier en utilisant la méthode `querySelector()`.

Ensuite, nous définissons la méthode `uploadFile()` dans laquelle nous déclarons d'abord une variable `API_ENDPOINT` qui contient l'adresse de notre point de terminaison de téléchargement de fichier. Ensuite, nous créons une requête `XMLHttpRequest` et un objet `FormData` vide.

Nous utilisons la méthode append de FormData pour ajouter le fichier, passé en paramètre à la méthode `uploadFile()`, à la clé `file`. Cela créera une paire clé-valeur avec `file` comme clé et le contenu du fichier passé comme valeur.

Ensuite, nous envoyons la requête en utilisant la méthode `send()` de `XMLHttpRequest` et nous passons l'objet `FormData` comme argument.

Après avoir défini la méthode `uploadFile()`, nous écoutons l'événement de changement sur l'élément `<input>` et nous appelons la méthode `uploadFile()` avec le fichier sélectionné comme argument. Le fichier est accessible à partir du tableau `event.target.files`.

Vous pouvez expérimenter avec cet exemple à partir de ce bac à sable de code :

## Téléchargement de plusieurs fichiers

Vous pouvez facilement modifier le code ci-dessus pour prendre en charge le téléchargement de plusieurs fichiers.

Tout d'abord, vous devez ajouter la propriété `multiple` à l'élément `<input>` :

```html
<input type="file" id="fileInput" multiple />

```

Maintenant, vous pourrez sélectionner plusieurs fichiers depuis votre disque.

Ensuite, modifiez la méthode `uploadFile()` pour accepter un tableau de fichiers comme argument et parcourez simplement le tableau et ajoutez les fichiers à l'objet `FormData` :

```js
const uploadFile = (files) => {
  console.log("Téléchargement du fichier...");
  const API_ENDPOINT = "https://file.io";
  const request = new XMLHttpRequest();
  const formData = new FormData();

  request.open("POST", API_ENDPOINT, true);
  request.onreadystatechange = () => {
    if (request.readyState === 4 && request.status === 200) {
      console.log(request.responseText);
    }
  };
  
  for (let i = 0; i < files.length; i++) {
    formData.append(files[i].name, files[i])
  }
  request.send(formData);
};

```

Enfin, appelez la méthode avec un tableau de fichiers comme argument :

```js
fileInput.addEventListener("change", event => {
  const files = event.target.files;
  uploadFile(files);
});

```

Ensuite, vous pouvez consulter ces tutoriels avancés pour savoir comment utiliser `FormData` avec Angular, Ionic et React :

* [Comment publier FormData avec Angular 7](https://www.techiediaries.com/angular-formdata/)
* [React & Axios FormData](https://www.techiediaries.com/react-formdata-file-upload-multipart-form-tutorial/)
* [Téléchargement de plusieurs fichiers avec Ionic 4 & FormData](https://www.techiediaries.com/ionic-formdata-multiple-file-upload-tutorial/)