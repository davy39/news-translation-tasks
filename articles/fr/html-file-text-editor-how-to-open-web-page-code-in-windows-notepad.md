---
title: Éditeur de texte de fichiers HTML – Comment ouvrir le code d'une page web dans
  le Bloc-notes Windows
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-16T15:08:00.000Z'
originalURL: https://freecodecamp.org/news/html-file-text-editor-how-to-open-web-page-code-in-windows-notepad
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/notepad.png
tags:
- name: editor
  slug: editor
- name: HTML
  slug: html
- name: Windows
  slug: windows
seo_title: Éditeur de texte de fichiers HTML – Comment ouvrir le code d'une page web
  dans le Bloc-notes Windows
seo_desc: 'Notepad is a built-in text editor that comes pre-installed on Windows machines
  of all versions – XP, Windows 7, Windows 8, Windows 10, and so on.

  It is the default Windows text editor. You can think of Notepad as your VS Code
  or favorite text editor ...'
---

Le Bloc-notes est un éditeur de texte intégré qui est préinstallé sur les machines Windows de toutes les versions – XP, Windows 7, Windows 8, Windows 10, et ainsi de suite.

C'est l'éditeur de texte Windows par défaut. Vous pouvez considérer le Bloc-notes comme votre VS Code ou votre éditeur de texte préféré avec moins de fonctionnalités. 

Coder avec le Bloc-notes est idéal pour les débutants, car vous n'avez pas accès à la coloration syntaxique, à la mise en forme et à d'autres fonctionnalités automatisées de ce type. 

Sans ces aides, vous apprendrez l'attention aux détails, la persévérance, la résilience et comment formater votre code vous-même, avant de commencer à coder avec d'autres éditeurs de texte comme VS Code, Sublime Text ou Atom.

Ainsi, dans cet article, je vais vous guider à travers l'utilisation du Bloc-notes Windows et comment ouvrir le code de n'importe quelle page web avec celui-ci en créant un site web simple avec HTML, un peu de CSS et de JavaScript.

## Comment coder un site web simple dans le Bloc-notes

Vous pouvez utiliser le Bloc-notes pour coder de deux manières : lancer le Bloc-notes directement depuis votre machine Windows et commencer à coder puis sauvegarder le code plus tard, ou créer le fichier et l'ouvrir avec le Bloc-notes.

Dans ce tutoriel, je vais me concentrer sur la deuxième méthode, donc je vais d'abord créer les fichiers, puis les ouvrir avec le Bloc-notes.

**Étape** 1 : Créez un dossier n'importe où sur votre ordinateur 
**Étape 2** : Dans la section du menu principal du dossier, cliquez sur l'onglet "Affichage" et assurez-vous que "extensions de nom de fichier" est coché. Cela vous donnera accès à la création d'un fichier et à la spécification de l'extension également.

![file-extension_LI](https://www.freecodecamp.org/news/content/images/2021/09/file-extension_LI.jpg)

**Étape 3** : À l'intérieur du dossier, créez un fichier HTML appelé `index.html`, un fichier CSS appelé `styles.css`, et un fichier JavaScript appelé `app.js`.

![file-creation](https://www.freecodecamp.org/news/content/images/2021/09/file-creation.png)

Ces noms sont dus à la convention. Vous pouvez nommer les fichiers comme vous le souhaitez si vous ne voulez pas suivre les conventions.

**Étape 4** : Faites un clic droit sur `index.html` et survolez l'option "ouvrir avec". Cela affichera les applications avec lesquelles vous pouvez ouvrir le fichier. Choisissez Bloc-notes.

![file-openinig](https://www.freecodecamp.org/news/content/images/2021/09/file-openinig.jpg)

Par défaut, le fichier index.html sera ouvert par votre navigateur par défaut, alors assurez-vous de ne pas double-cliquer sur le fichier.

Si le Bloc-notes n'est pas affiché dans les options, cliquez sur "Choisir une autre application", sélectionnez "Plus d'applications" dans la fenêtre contextuelle suivante, et vous verrez le Bloc-notes parmi les applications listées.

![file-opening-alternative](https://www.freecodecamp.org/news/content/images/2021/09/file-opening-alternative.jpg)

Maintenant, vous devriez avoir ouvert le fichier HTML avec le Bloc-notes. Vous verrez quelque chose comme ceci (si vous avez tout fait correctement) :

![blank-notepad](https://www.freecodecamp.org/news/content/images/2021/09/blank-notepad.png)

**Étape 5** : Collez le code HTML suivant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Site web Bloc-notes</title>
  </head>
  <body>
    <h1 class="page-heading"></h1>

    <h1>Ceci est un titre 1</h1>
    <h2>Ceci est un titre 2</h2>
    <h3>Ceci est un titre 3</h3>
    <h4>Ceci est un titre 4</h4>
    <h5>Ceci est un titre 5</h5>
    <h6>Ceci est un titre 6</h6>

    <p>
      Ceci est un paragraphe avec quelques textes de remplissage : Lorem ipsum dolor sit
      amet, consectetur adipisicing elit. Beatae, mollitia quo quasi voluptatum
      quam soluta debitis praesentium molestias nam magnam aperiam deserunt eos
      modi odit incidunt ut vitae cum maiores.
    </p>

    <strong>Ceci est une phrase en gras</strong> <br>

    <em>Ceci est un texte en italique</em>

    <p>
      Ceci est un lien vers <a href="https://freecodecamp.org">freeCodeCamp</a>, une
      plateforme où vous pouvez apprendre à coder gratuitement
    </p>

    <p>Ci-dessous se trouve le logo de freeCodeCamp :</p>

    <img
      src="https://popsql.com/static/external-logos/freecodecamp.png"
      alt="logo-freecodecamp"
    />
  </body>
</html>
```

Votre application Bloc-notes devrait maintenant être remplie de code :
![html-notepad-1](https://www.freecodecamp.org/news/content/images/2021/09/html-notepad-1.png)

Enregistrez le fichier en appuyant sur Ctrl + S, ou allez dans Fichier et cliquez sur "Enregistrer".

Si votre code n'est pas indenté comme le mien, ne vous inquiétez pas. Le Bloc-notes ne le fait pas automatiquement pour vous, donc vous devez le faire manuellement.

**Étape 6** : Maintenant, le fichier HTML est prêt. Retournez dans le dossier dans lequel vous avez créé les fichiers HTML, CSS et JavaScript à l'**Étape 3**. Double-cliquez sur le fichier HTML pour l'ouvrir dans votre navigateur par défaut.

Le site web devrait maintenant ressembler à ceci :
![html-page-1](https://www.freecodecamp.org/news/content/images/2021/09/html-page-1.png)

Ouvrez le fichier CSS que vous avez créé à l'**Étape 3** et collez le code suivant : 

```css
.page-heading {
  color: #2ecc71;
}
```

Si vous rechargez la page, vous ne verrez aucun changement. Ne vous inquiétez pas du tout. Cela est dû au fait que la balise `h1` avec la classe `page-heading` dans le fichier HTML est vide.

Maintenant, vous pouvez insérer du texte dans cette balise `h1` dynamiquement avec JavaScript.

Ouvrez le fichier JavaScript créé à l'**Étape 3** et collez le code suivant : 

```js
const pageHeadingText = "Ceci est un site web simple codé avec le Bloc-notes Windows";
const pageHeading = document.querySelector(".page-heading");

pageHeading.innerHTML = pageHeadingText;
```

Que fait le code JavaScript ci-dessus ?

J'ai déclaré une variable appelée `pageHeadingText` et je l'ai définie sur une chaîne, "Ceci est un site web simple codé avec le Bloc-notes Windows".

J'ai déclaré une autre variable appelée `pageHeading` pour sélectionner la balise h1 vide dans le HTML. Je l'ai fait avec la méthode DOM (Document Object Model) `querySelector`.

Dans la troisième ligne du code JavaScript, j'ai utilisé la méthode `innerHTML` du DOM pour définir le contenu textuel de la balise `h1` sur la valeur de la variable `pageHeadingText`, que j'ai définie sur "Ceci est un site web simple codé avec le Bloc-notes Windows".

Maintenant, retournez sur le site web et rechargez-le. Il n'y a toujours pas de différence. Ne vous inquiétez pas une fois de plus. Cela est dû au fait que vous devez lier les fichiers CSS et JavaScript. 

Pour lier le fichier CSS, collez le code suivant dans la section head du HTML : 

```html
<link rel="stylesheet" href="styles.css" />
```

Pour lier le fichier JavaScript, collez le code ci-dessous juste avant la balise de fermeture body dans le HTML : 

```html
<script src="app.js"></script>
```

Le fichier HTML devrait maintenant avoir les fichiers CSS et JavaScript liés comme ceci : 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Site web Bloc-notes</title>

    <!-- Lien CSS -->
    <link rel="stylesheet" href="styles.css" />

  </head>
  <body>
    <h1 class="page-heading"></h1>

    <h1>Ceci est un titre 1</h1>
    <h2>Ceci est un titre 2</h2>
    <h3>Ceci est un titre 3</h3>
    <h4>Ceci est un titre 4</h4>
    <h5>Ceci est un titre 5</h5>
    <h6>Ceci est un titre 6</h6>

    <p>
      Ceci est un paragraphe avec quelques textes de remplissage : Lorem ipsum dolor sit
      amet, consectetur adipisicing elit. Beatae, mollitia quo quasi voluptatum
      quam soluta debitis praesentium molestias nam magnam aperiam deserunt eos
      modi odit incidunt ut vitae cum maiores.
    </p>

    <strong>Ceci est une phrase en gras</strong>

    <em>Ceci est un texte en italique</em>

    <p>
      Ceci est un lien vers <a href="https://freecodecamp.org">freeCodeCamp</a>, une
      plateforme où vous pouvez apprendre à coder gratuitement
    </p>

    <p>Ci-dessous se trouve le logo de freeCodeCamp :</p>

    <img
      src="https://popsql.com/static/external-logos/freecodecamp.png"
      alt="logo-freecodecamp"
    />

    <!-- Lien JavaScript -->
    <script src="app.js"></script>

  </body>
</html>
```

Si vous rechargez maintenant la page, vous devriez voir une différence :

![html-page-2](https://www.freecodecamp.org/news/content/images/2021/09/html-page-2.png)

Le code dans les fichiers CSS et JavaScript fonctionne maintenant.

## Conclusion

Le Bloc-notes Windows est un éditeur de texte comme VS Code, Atom, Sublime Text, et d'autres. Il n'a simplement pas les fonctionnalités d'autres éditeurs de texte plus avancés comme la coloration syntaxique, la mise en forme du texte, le terminal intégré, et ainsi de suite. Mais il remplit toujours toutes les fonctions d'un éditeur de texte car vous pouvez coder dans n'importe quel langage de programmation avec celui-ci.

Pour être plus à l'aise avec le codage, vous pouvez télécharger et installer un éditeur de texte plus riche en fonctionnalités comme VS Code (il est gratuit !). Il vous offre la coloration syntaxique, la mise en forme du texte et pratiquement toutes les fonctionnalités que vous souhaitez grâce à une riche bibliothèque d'extensions disponibles dans le marché VS Code. 

Outre VS Code, d'autres éditeurs de texte que vous pouvez utiliser sont Atom, Sublime Text, Vim et Notepad++, une version hybride du Bloc-notes Windows.

Merci d'avoir lu cet article. Si vous le trouvez utile, partagez-le avec vos amis et votre famille.