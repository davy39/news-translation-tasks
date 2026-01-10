---
title: Comment copier du texte dans le presse-papiers avec JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-14T21:18:48.000Z'
originalURL: https://freecodecamp.org/news/copy-text-to-clipboard-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--14-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment copier du texte dans le presse-papiers avec JavaScript
seo_desc: When you're building advanced web pages and applications, you'll sometimes
  want to add the copy feature. This lets your users simply click a button or icon
  to copy text rather than highlighting the text and clicking a couple of buttons
  on the keyboar...
---

Lorsque vous construisez des pages web et des applications avancées, vous voudrez parfois ajouter la fonctionnalité de copie. Cela permet à vos utilisateurs de simplement cliquer sur un bouton ou une icône pour copier du texte plutôt que de surligner le texte et de cliquer sur quelques boutons du clavier.

Cette fonctionnalité est principalement utilisée lorsqu'une personne doit copier un code d'activation, une clé de récupération, un extrait de code, etc. Vous pouvez également ajouter des fonctionnalités comme une alerte ou un texte à l'écran (qui pourrait être une modale) pour informer l'utilisateur que le texte a été copié dans son presse-papiers.

Auparavant, vous auriez géré cela avec la commande `document.execCommand()`, mais celle-ci est obsolète (plus recommandée). Vous pouvez maintenant utiliser l'API Clipboard, qui vous permet de répondre aux commandes du presse-papiers (couper, copier et coller) et de lire de manière asynchrone et **d'écrire dans** le presse-papiers du système.

Dans cet article, vous apprendrez comment écrire (copier) du texte et des images dans le presse-papiers avec l'API Clipboard.

Au cas où vous seriez pressé, voici le code :

```js
<p id="myText">Hello World</p>
<button class="btn" onclick="copyContent()">Copier !</button>

<script>
  let text = document.getElementById('myText').innerHTML;
  const copyContent = async () => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Contenu copié dans le presse-papiers');
    } catch (err) {
      console.error('Échec de la copie : ', err);
    }
  }
</script>
```

Si vous n'êtes pas pressé, comprenons mieux l'API Clipboard et voyons comment cela fonctionne avec un projet de démonstration.

## Comment vérifier les permissions du navigateur

Il est important de savoir que l'API Clipboard n'est prise en charge que pour les pages servies via HTTPS. Vous devez également vérifier les permissions du navigateur avant de tenter d'écrire dans le presse-papiers pour vérifier si vous avez l'accès en écriture. Vous pouvez le faire avec la requête `navigator.permissions` :

```js
navigator.permissions.query({ name: "write-on-clipboard" }).then((result) => {
  if (result.state == "granted" || result.state == "prompt") {
    alert("Accès en écriture accordé !");
  }
});
```

## Comment copier du texte dans le presse-papiers

Pour copier du texte avec la nouvelle *API Clipboard*, vous utiliserez la méthode asynchrone `writeText()`. Cette méthode n'accepte qu'un seul paramètre - le texte à copier dans votre presse-papiers. Cela peut être une chaîne de caractères, un littéral de modèle contenant des variables et d'autres chaînes, ou une variable utilisée pour contenir une chaîne.

Étant donné que cette méthode est asynchrone, elle retourne une promesse. Cette promesse est résolue si le presse-papiers a été mis à jour avec succès, et est rejetée sinon :

```js
navigator.clipboard.writeText("Ceci est le texte à copier").then(() => {
  console.log('Contenu copié dans le presse-papiers');
  /* Résolu - texte copié dans le presse-papiers avec succès */
},() => {
  console.error('Échec de la copie');
  /* Rejeté - texte n'a pas pu être copié dans le presse-papiers */
});
```

Vous pouvez également utiliser async/await avec try/catch :

```js
async function copyContent() {
  try {
    await navigator.clipboard.writeText('Ceci est le texte à copier');
    console.log('Contenu copié dans le presse-papiers');
    /* Résolu - texte copié dans le presse-papiers avec succès */
  } catch (err) {
    console.error('Échec de la copie : ', err);
    /* Rejeté - texte n'a pas pu être copié dans le presse-papiers */
  }
}
```

### Exemple de copie de texte dans le presse-papiers

Voici une démonstration montrant comment cela fonctionne en utilisant un exemple concret. Dans cet exemple, nous récupérons des citations d'une API publique de citations. Ensuite, lorsque vous cliquez sur l'icône de copie, la citation et son auteur sont copiés, montrant que vous pouvez ajuster ce que vous copiez dans la méthode `writeText()`.

Voir le Pen [copy text JS](https://codepen.io/olawanlejoel/pen/MWGLXyX) par Olawanle Joel ([@olawanlejoel](https://codepen.io/olawanlejoel)) sur [CodePen](https://codepen.io).

## Conclusion

Dans cet article, vous avez appris comment copier du texte dans le presse-papiers avec JavaScript en utilisant l'API Clipboard sans avoir à penser hors des sentiers battus ou à installer une bibliothèque JavaScript.

Amusez-vous bien à coder !

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.