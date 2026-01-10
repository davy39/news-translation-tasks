---
title: Comment enregistrer une chaîne Base64 en tant que fichier PDF côté client en
  JavaScript
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2023-02-27T18:20:44.000Z'
originalURL: https://freecodecamp.org/news/save-a-base64-string-as-pdf-on-client-side-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/How-to-check-if-a-String-is-URL-in-Javascript.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment enregistrer une chaîne Base64 en tant que fichier PDF côté client
  en JavaScript
seo_desc: 'Base64 strings represent binary objects in textual format. They are designed
  to transmit binary data between channels that only support a textual format.

  Sometimes, you might receive PDF files from various services as a Base64 string,
  and you may nee...'
---

Les chaînes Base64 représentent des objets binaires au format texte. Elles sont conçues pour transmettre des données binaires entre des canaux qui ne supportent que le format texte.

Parfois, vous pouvez recevoir des fichiers PDF de divers services sous forme de chaîne Base64, et vous devrez peut-être les convertir en fichier PDF côté client après avoir reçu la réponse.

Ce tutoriel vous apprend à enregistrer une chaîne Base64 en tant que PDF côté client en JavaScript.

## Format de la chaîne Base64

Les [chaînes Base64](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) sont au format texte et comportent un préfixe de métadonnées.

**Voici la syntaxe :**

```
data:[<mediatype>][;base64],<data>

```

Où,

* `data` est un préfixe commun
* `Mediatype` est une chaîne [Mimetype](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) qui représente le type de fichier
* `Base64` indique que la chaîne est une chaîne Base64

Examinons un exemple :

```
data:application/pdf;base64,<Base64 String>

```

La chaîne ci-dessus représente une chaîne Base64 d'un fichier PDF.

Les chaînes Base64 sont également connues sous le nom de [DataURLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs). Les Data URLs sont des URLs préfixées par le schéma `data:` pour permettre aux utilisateurs d'intégrer des fichiers en ligne dans le document `HTML`.

Pour convertir un fichier PDF en chaîne Base64, vous pouvez utiliser l'outil [online Base64 Encoder tool](https://www.base64encode.pro/). Vous pouvez télécharger le fichier et cliquer sur _Encode_. Il retournera un fichier texte contenant la chaîne équivalente en base64 du fichier PDF.

Maintenant, utilisons la chaîne de sortie et [convertissons la chaîne Base64 en fichier PDF](https://www.base64decode.pro/blog/how-to-convert-a-base64-string-to-a-file-in-java-with-examples/) côté client en utilisant JavaScript.

## Comment créer une interface utilisateur avec HTML

Pour cette démonstration, créons une interface utilisateur simple en HTML. Notre interface utilisateur comportera :

* Une `zone de texte` qui accepte une chaîne Base64 dans la boîte de texte
* Un `bouton`, avec un événement de clic, qui convertit la chaîne Base64 disponible dans la zone de texte en format PDF et la télécharge automatiquement.

Voici le code pour le faire :

```
<label for="Base64StringTxtBox">Chaîne Base64</label>

<textarea id="Base64StringTxtBox" name="Base64Text" rows="4" cols="50">

</textarea>

<button type="Convert" onclick="downloadAsPDF()">Convertir en PDF</button>

```

## Comment utiliser la balise d'ancrage

Pour convertir la chaîne Base64 en fichier PDF, vous devrez faire ce qui suit :

* Obtenir la chaîne Base64 de la zone de texte
* Créer un élément [Anchor](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) dans l'élément HTML
* Assigner la chaîne Base64 à l'attribut `href` de l'élément d'ancrage
* Assigner un nom de fichier à l'attribut `download`. Le [download](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attr-download) indique au navigateur de traiter l'URL liée comme une option de téléchargement. Lorsque le lien d'ancrage est cliqué, la cible spécifiée dans l'attribut `href` est téléchargée avec le nom de fichier.

Examinons un exemple :

Le code JavaScript suivant télécharge la chaîne Base64 en tant que fichier PDF :

```
function downloadAsPDF(pdf) {

  var base64String = document.getElementById("Base64StringTxtBox").value;
  
  const downloadLink = document.createElement("a");
  
  downloadLink.href = base64String;
  
  downloadLink.download = "convertedPDFFile.pdf";
  
  downloadLink.click();
}

```

## Comment gérer les chaînes Base64 sans métadonnées

Dans certains cas, une chaîne base64 peut ne pas avoir de préfixe de métadonnées. L'utilisateur peut recevoir uniquement les données Base64 en réponse.

Chaque type de fichier a un préfixe commun dans la chaîne Base64. Par exemple,

* Une chaîne Base64 de fichier JPG commence par `/9j`
* Une chaîne Base64 de fichier PDF commence par `JVB`
* Une chaîne Base64 de fichier PNG commence par `iVB`

La réponse Stackoverflow [ici](https://stackoverflow.com/a/58158656/8510024) explique plus en détail comment trouver le type Mime à partir de la chaîne Base64 sans métadonnées.

Maintenant, apprenons à télécharger une chaîne Base64 sans métadonnées en tant que fichier PDF.

* Vérifiez si la Base64 commence par `JVB`, ajoutez les métadonnées `data:application/pdf;base64,` à la chaîne Base64 existante et téléchargez-la en utilisant la balise d'ancrage.
* Vérifiez si la chaîne Base64 commence par le préfixe `Data:`. Si oui, téléchargez directement le fichier en utilisant la balise d'ancrage.
* Si la chaîne n'a pas le préfixe `data:` ou `JVB`, alors ce n'est pas une chaîne Base64 de fichier PDF valide. Avertissez l'utilisateur avec un message d'erreur approprié.

Examinons un exemple.

Le code suivant montre comment valider la chaîne Base64 avant de la télécharger en tant que fichier PDF.

```
function downloadAsPDF(pdf) {

  var base64String = document.getElementById("Base64StringTxtBox").value;

  if (base64String.startsWith("JVB")) {
    base64String = "data:application/pdf;base64," + base64String;
    downloadFileObject(base64String);
  } else if (base64String.startsWith("data:application/pdf;base64")) {
    downloadFileObject(base64String);
  } else {
    alert("Ce n'est pas une chaîne Base64 PDF valide. Veuillez vérifier");
  }

}

function downloadFileObject(base64String) {
  const linkSource = base64String;
  const downloadLink = document.createElement("a");
  const fileName = "convertedPDFFile.pdf";
  downloadLink.href = linkSource;
  downloadLink.download = fileName;
  downloadLink.click();
}

```

## Comment utiliser l'outil de décodage Base64 en ligne

Vous pouvez également utiliser l'outil [Online Base64 Decode tool](https://www.base64decode.pro/) pour convertir la chaîne Base64 en fichier PDF. Vous pouvez ajouter la chaîne Base64 dans un fichier texte et le télécharger vers l'outil en ligne. Il convertira le fichier et le téléchargera.

### Lien JSfiddle

Les deux tutoriels ci-dessus sont disponibles dans les liens JSfiddle suivants :

* Exemple 1 – [Télécharger la chaîne Base64 avec le préfixe de métadonnées](https://jsfiddle.net/jsowl/yxbts6ap/4/)
* Exemple 2 – [Télécharger la chaîne Base64 sans le préfixe de métadonnées](https://jsfiddle.net/jsowl/vmu5t80b/9/)

## Conclusion

Pour résumer, dans ce tutoriel, vous avez appris ce que sont les chaînes Base64, comment convertir une chaîne Base64 en fichier, puis la télécharger côté client en utilisant JavaScript.

Vous avez également appris les préfixes de métadonnées des chaînes Base64.