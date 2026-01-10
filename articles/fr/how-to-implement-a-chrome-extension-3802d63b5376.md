---
title: Comment implémenter une extension Chrome
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-11-12T16:29:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-chrome-extension-3802d63b5376
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_IrKrGVmSj1DVh6kIsfqYyA.jpeg
tags:
- name: chrome extension
  slug: chrome-extension
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment implémenter une extension Chrome
seo_desc: 'We all like surfing the web. And we all like things to be at the touch
  of our fingertips. Why not create something that caters to these two absolute truths?

  In this article, I’ll explain the building blocks of a Chrome extension. Afterwards,
  you’ll j...'
---

Nous aimons tous surfer sur le web. Et nous aimons tous avoir les choses à portée de main. Pourquoi ne pas créer quelque chose qui répond à ces deux vérités absolues ?

Dans cet article, je vais expliquer les éléments constitutifs d'une extension Chrome. Ensuite, il vous suffira de trouver une bonne idée comme excuse pour en créer une.

### Pourquoi Chrome ?

Chrome est de loin le navigateur web le plus populaire. [Certaines estimations atteignent jusqu'à **59%**](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers). Donc, si vous voulez toucher autant de personnes que possible, développer une extension Chrome est la meilleure façon de procéder.

⚠️ Pour pouvoir publier une extension Chrome, vous devez avoir un compte développeur, ce qui implique des [$5 de frais d'inscription uniques](https://developer.chrome.com/webstore/publish).

Chaque extension Chrome doit comporter ces composants : le **fichier manifest**, **popup.html** et **popup.js**, ainsi qu'un script **background**. Examinons-les.

### Qu'est-ce qui compose une extension Chrome ?

#### Le fichier Manifest

Qu'est-ce qu'un fichier manifest ? Il s'agit d'un fichier texte au format JSON ([JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON)) qui contient certains détails sur l'extension que vous allez développer.

Google utilise ce fichier pour obtenir des détails sur votre extension lorsque vous la publierez. Il existe des champs **obligatoires**, **recommandés** et **optionnels**.

#### Obligatoires

```js
{
  "manifest_version": 2,
  "name": "Mon Extension Chrome",
  "version": "1.0",
  "default_locale": "en"
}
```

* `manifest_version` - Version du format du fichier manifest. À partir de Chrome 18, la version 1 est obsolète
* `name` - Peut comporter jusqu'à 45 caractères. Utilisé pour afficher le nom de votre extension dans les endroits suivants : boîte de dialogue d'installation, interface de gestion des extensions, Chrome Web Store
* `version` - Version de votre extension Chrome. Peut comporter jusqu'à quatre chiffres séparés par des points (par exemple, 1.0.0.0)
* `default_locale` - Ce dossier réside à l'intérieur du dossier `_locals` et contient les littéraux de chaîne par défaut. Le dossier `_locals` est utilisé pour l'internationalisation (permettant à votre extension de supporter plusieurs langues). Il s'agit d'un champ obligatoire si un dossier `_locals` existe, sinon, il ne doit pas être présent

Si vous souhaitez supporter plusieurs langues, lisez plus [ici](https://developer.chrome.com/extensions/i18n).

#### Recommandés

```js
  "description": "Une description en texte brut",
  "author": "Votre Nom Ici",
  "short_name": "nomCourt",
  "icons": {
      "128":"icon128.png",
       "48":"icon48.png",
       "16":"icon16.png"
    },
```

* `description` - Vous pouvez utiliser jusqu'à 132 caractères pour décrire l'extension
* `short_name` - Limité à 12 caractères, il est utilisé dans les cas où il n'y a pas assez d'espace pour afficher le nom complet de l'extension (Lanceur d'applications et Nouvelle page d'onglet)
* `icons` - Les icônes qui représentent l'extension. **Incluez toujours une icône 128X128** car elle est utilisée par le Chrome Web Store et lors de l'installation de votre extension

Les champs optionnels sont spécifiques à chaque cas, nous ne les aborderons donc pas dans cet article.

Après avoir couvert les données nécessaires pour le fichier manifest, nous pouvons maintenant passer à l'endroit où nous allons réellement écrire du code pour notre extension, **Popup et Background**.

#### Popup et Background

Le popup fait référence à la page principale que les utilisateurs voient lorsqu'ils utilisent votre extension. Il se compose de deux fichiers : **Popup.html** et un fichier JavaScript, **Popup.js**.

Popup.html est le fichier de mise en page pour l'apparence de votre extension. Selon ce que votre extension fera, le balisage de ce fichier changera.

Un script de fond est le seul qui peut interagir avec les événements qui se produisent et utiliser l'API Chrome. Pour utiliser des scripts de fond, vous devez ajouter ce qui suit à votre fichier manifest.json :

```js
{
  "manifest_version": 2,
  "name": "Mon Extension Chrome",
  "version": "1.0",
  "background":{
    	"scripts": ["yourScript.js"],
    	"persistent": false
    }
}
```

La clé `scripts` a une valeur de tableau de noms de scripts.

`persistent` est une clé avec une valeur booléenne qui indique l'utilisation de votre extension avec l'API chrome.webRequest pour bloquer ou modifier les requêtes réseau. L'API Chrome.webRequest ne fonctionne pas avec les pages de fond non persistantes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mFgdmSgmiXKQmhZ_)
_Panneau ouvert sur la porte par [Unsplash](https://unsplash.com/@belart84?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Artem Bali</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Comment votre extension s'ouvrira

Chaque extension Chrome ajoute une petite icône à la barre d'outils en haut de votre navigateur. Une fois que l'utilisateur clique sur cette icône, vous pouvez choisir comment vous voulez que votre extension s'ouvre dans le navigateur :

1. Elle peut remplacer un nouvel onglet, afin de ne pas perturber l'activité actuelle de l'utilisateur

2. Vous pouvez ouvrir une petite fenêtre dans l'onglet actuel de l'utilisateur, afin de garder l'utilisateur dans le même onglet

Chaque choix a ses conséquences et c'est à vous de décider quelle est la meilleure option pour vous.

Ci-dessous se trouve le code nécessaire pour réaliser chacune des options. Les deux utiliseront le même fichier popup.html décrit ci-dessous :

```html
<html>

	<head>
		
		<title>Exemple d'extension Chrome</title>
	</head>

	<body>

		<h1>Bonjour depuis l'extension</h1>

	</body>


</html>
```

### Mettre le tout ensemble

#### Remplacer le nouvel onglet

```js
//Dans manifest.json
{
    "name": "ChromeExampleNewTab",
    "version": "1.0",
    "manifest_version": 2,
    "chrome_url_overrides": {
    	"newtab": "popup.html"
    },
    "browser_action": {}, 
    "permissions":[        
    	"tabs"
    ],
    "background":{        
    	"scripts": ["background.js"],
    	"persistent": false
    }
}

//Dans background.js
chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.create({'url': chrome.extension.getURL('popup.html')}, function(tab) {
		// Onglet ouvert.
	});
});
```

#### Ouvrir dans l'onglet actuel

```js
//Dans manifest.js
{
    "name": "ChromeExample",
    "version": "1.0",
    "manifest_version": 2,
    "browser_action": {         
      "default_popup": "popup.html"
    }
}
```

Remarquez comment nous avons remplacé la clé `browser_action` dans les deux exemples.

Nous devons faire cela, car nous ne voulons pas que le navigateur ouvre un nouvel onglet de la manière habituelle.

De plus, si nous voulons ouvrir un nouvel onglet avec notre extension, nous devons ajouter une clé de permissions au manifest et spécifier la valeur des onglets. Cela permet au navigateur de savoir que nous avons besoin de la permission de l'utilisateur pour remplacer le comportement par défaut d'ouverture d'un nouvel onglet.

Il y a beaucoup plus à dire sur les extensions Chrome (messagerie, menus contextuels et stockage, pour n'en nommer que quelques-uns). J'espère vous avoir donné un aperçu des extensions Chrome. Peut-être juste assez pour vous intriguer et vous inciter à créer la vôtre !

Et pendant que vous y êtes, consultez celle que j'ai créée [ici](https://chrome.google.com/webstore/detail/gifted/jmhifaldhcbhfdgdbneekdaloednddco).