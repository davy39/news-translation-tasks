---
title: Comment écrire votre propre extension de navigateur [Projet d'exemple inclus]
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-11-02T15:57:40.000Z'
originalURL: https://freecodecamp.org/news/write-your-own-browser-extensions
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/browsers.png
tags:
- name: Browsers
  slug: browsers
- name: chrome extension
  slug: chrome-extension
- name: Productivity
  slug: productivity
seo_title: Comment écrire votre propre extension de navigateur [Projet d'exemple inclus]
seo_desc: 'In this article we will talk about Browser extensions – what they are,
  how they work, and how you can build your own.

  We will finish by actually writing our own extension (Super Fun!) which allows us
  to copy any code snippet to our clipboard with a c...'
---

Dans cet article, nous allons parler des extensions de navigateur – ce qu'elles sont, comment elles fonctionnent et comment vous pouvez créer la vôtre.

Nous terminerons en écrivant réellement notre propre extension (Super Amusant !) qui nous permet de copier n'importe quel extrait de code dans notre presse-papiers avec un clic sur un seul bouton.

Pour continuer avec cet article :

* Vous devez avoir une compréhension de base de JavaScript.
  
* Vous avez besoin du navigateur Firefox (ou tout autre navigateur fonctionnera également)
  

## Qu'est-ce qu'une extension de navigateur ?

Une extension de navigateur est quelque chose que vous ajoutez à votre navigateur pour améliorer votre expérience de navigation en étendant les capacités de votre navigateur.

Par exemple, pensez à un bloqueur de publicités que vous avez peut-être installé sur votre appareil. Cela améliore votre expérience de navigation en bloquant les publicités lorsque vous surfez sur le web.

## Comment écrire votre propre extension de navigateur basique

Maintenant, commençons par écrire une extension très basique.

Pour commencer, nous allons créer un dossier à l'intérieur duquel nous créerons un fichier nommé `manifest.json`.

### Qu'est-ce qu'un fichier manifest ?

Un fichier manifest est un fichier indispensable dans toute extension de navigateur. Ce fichier contient des données de base sur notre extension comme le nom, la version, etc.

Maintenant, à l'intérieur du fichier `manifest.json`, copiez le code suivant :

```json
{
  "manifest_version": 2,
  "version": "1.0",
  "name": "Test",
}
```

[**Mise à jour 2025** : Chrome [ne prend actuellement en charge que la version 3](https://developer.chrome.com/docs/extensions/reference/manifest) pour manifest.json]

### Comment charger le fichier d'extension

Pour les utilisateurs de Firefox, suivez ces étapes :

Dans la barre d'adresse, recherchez ceci :

```javascript
about:debugging#/runtime/this-firefox
```

Vous verrez une option pour *Charger un module complémentaire temporaire*. Cliquez sur cette option et choisissez le fichier `manifest.json` dans le répertoire.

Pour les utilisateurs de Chrome :

Dans la barre d'adresse, recherchez ceci :

```javascript
chrome://extensions
```

* Activez le Mode Développeur et basculez dessus.
  
* Cliquez sur le bouton Charger l'extension décompressée et sélectionnez le répertoire de l'extension.
  

Hourra ! Vous avez installé l'extension avec succès. Mais l'extension ne fait actuellement rien. Maintenant, ajoutons quelques fonctionnalités à notre extension. Pour cela, nous allons modifier notre fichier `manifest.json` comme ceci :

```json
{
  "manifest_version": 2,
  "version": "1.0",
  "name": "Test",
  "content_scripts": [
    {
     "matches": ["<all_urls>"],
     "js": ["main.js"]
    }
  ]
}
```

Dans le code ci-dessus, nous avons ajouté un script de contenu à `manifest.json`. Les scripts de contenu peuvent manipuler le Document Object Model de la page web. Nous pouvons injecter du JS (et du CSS) dans une page web en utilisant un script de contenu.

`"matches"` contient la liste des domaines et sous-domaines où le script de contenu doit être ajouté et `js` est un tableau des fichiers JS à charger.

Maintenant, dans le même répertoire, créez un fichier `main.js` et ajoutez le code suivant :

```js
alert("L'extension de test est opérationnelle")
```

Maintenant, rechargez l'extension et lorsque vous visitez n'importe quelle `URL`, vous verrez un message d'alerte.

**N'oubliez pas de recharger l'extension chaque fois que vous modifiez le code.**

## Comment personnaliser votre extension de navigateur

Maintenant, amusons-nous un peu plus avec notre extension.

Ce que nous allons faire maintenant, c'est créer une extension web qui change toutes les images d'une page web que nous visitons par une image que nous choisissons.

Pour cela, ajoutez simplement une image au répertoire actuel et changez le fichier `main.js` en :

```js
console.log("L'extension est opérationnelle");

var images = document.getElementsByTagName('img')

for (elt of images){
   elt.src = `${browser.runtime.getURL("pp.jpg")}`
   elt.alt = 'un texte alternatif'
}
```

Voyons ce qui se passe ici :

```js
var images = document.getElementsByTagName('img')
```

Cette ligne de code sélectionne tous les éléments de la page web avec la balise `img`.

Ensuite, nous parcourons le tableau d'images en utilisant une boucle for où nous changeons l'attribut `src` de tous les éléments `img` en une URL avec l'aide de la fonction `runtime.getURL`.

Ici, `pp.jpg` est le nom du fichier image dans le répertoire actuel de mon appareil.

Nous devons informer notre script de contenu du fichier `pp.jpg` en modifiant le fichier `manifest.json` comme suit :

```js
{
  "manifest_version": 2,
  "version": "1.0",
  "name": "Test",
  "content_scripts": [
   {
    "matches": ["<all_urls>"],
    "js": ["main.js"]
   }
  ],
  "web_accessible_resources": [
        "pp.jpg"
  ]
}
```

Ensuite, rechargez simplement l'extension et visitez n'importe quelle URL que vous souhaitez. Maintenant, vous devriez voir toutes les images changées en l'image qui se trouve dans votre répertoire de travail actuel.

### Comment ajouter des icônes à votre extension

Ajoutez le code suivant dans le fichier `manifest.json` :

```json
"icons": {
  "48": "icon-48.png",
  "96": "icon-96.png"
}
```

### Comment ajouter un bouton de barre d'outils à votre extension

Maintenant, nous allons ajouter un bouton situé dans la barre d'outils de votre navigateur. Les utilisateurs peuvent interagir avec l'extension en utilisant ce bouton.

Pour ajouter un bouton de barre d'outils, ajoutez les lignes suivantes au fichier `manifest.json` :

```json
"browser_action": {
   "default_icon": {
     "19": "icon-19.png",
     "38": "icon-38.png"
   }
  }
```

Tous les fichiers image doivent être présents dans votre répertoire actuel.

Maintenant, si nous rechargeons l'extension, nous devrions voir une icône pour notre extension dans la barre d'outils de notre navigateur.

### Comment ajouter des événements d'écoute pour le bouton de la barre d'outils

Peut-être voulons-nous faire quelque chose lorsque l'utilisateur clique sur le bouton – disons que nous voulons ouvrir un nouvel onglet chaque fois que le bouton est cliqué.

Pour cela, nous allons à nouveau ajouter ce qui suit au fichier `manifest.json` :

```json
"background": {
        "scripts": ["background.js"]
  },
  "permissions": [
      "tabs"
  ]
```

Ensuite, nous allons créer un nouveau fichier nommé `background.js` dans le répertoire de travail actuel et ajouter les lignes suivantes dans le fichier :

```js
function openTab() {
    
    var newTab = browser.tabs.create({
        url: 'https://twitter.com/abhilekh_gautam',
        active: true
    })
}

browser.browserAction.onClicked.addListener(openTab)
```

Maintenant, rechargez l'extension !

Chaque fois que quelqu'un clique sur le bouton, il appelle la fonction `openTab` qui ouvre un nouvel onglet avec l'URL qui mène à mon profil Twitter. De plus, la clé active, lorsqu'elle est définie sur true, fait de l'onglet nouvellement créé l'onglet actuel.

Notez que vous pouvez utiliser les API fournies par les navigateurs dans le script d'arrière-plan. Pour plus d'informations sur les API, consultez l'article suivant : [APIs Javacript](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API).

Maintenant que nous avons appris quelques bases des extensions de navigateur, créons une extension que nous, en tant que développeurs, pouvons utiliser dans notre vie quotidienne.

## Projet final

D'accord, maintenant nous allons écrire quelque chose qui nous sera utile dans la vie quotidienne. Nous allons créer une extension qui permet de copier des extraits de code de StackOverflow avec un seul clic. Ainsi, notre extension ajoutera un bouton `Copier` à la page web qui copie le code dans notre presse-papiers.

### Démo

![Image](https://www.freecodecamp.org/news/content/images/2021/10/demo.png align="left")

Tout d'abord, nous allons créer un nouveau dossier/répertoire, à l'intérieur duquel nous ajouterons un fichier `manifest.json`.

Ajoutez le code suivant au fichier :

```json
{
  "manifest_version": 2,
  "version": "1.0",
  "name": "copier le code",
  "content_scripts": [
    {
     "matches": ["*://*.stackoverflow.com/*"],
     "js": ["main.js"]
    }
  ]
}
```

Regardez les `matches` à l'intérieur du `content script` – l'extension ne fonctionnera que pour le domaine et les sous-domaines de StackOverflow.

Maintenant, créez un autre fichier JavaScript appelé `main.js` dans le même répertoire et ajoutez les lignes de code suivantes :

```js
var arr = document.getElementsByClassName("s-code-block")

for(let i = 0 ; i < arr.length ; i++) {
 var btn = document.createElement("button")
 btn.classList.add("copy_code_button")
 btn.appendChild(document.createTextNode("Copier"))
 arr[i].appendChild(btn)
 // stylisation du bouton
 btn.style.position = "relative"
 
 if(arr[i].scrollWidth === arr[i].offsetWidth && arr[i].scrollHeight === arr[i].offsetHeight)
  btn.style.left = `${arr[i].offsetWidth - 70}px`

  else if(arr[i].scrollWidth != arr[i].offsetWidth && arr[i].scrollHeight === arr[i].offsetWidth)
   btn.style.left = `${arr[i].offsetWidth - 200}px`
 else 
   btn.style.left = `${arr[i].offsetWidth - 150}px`
  
 if(arr[i].scrollHeight === arr[i].offsetHeight)
   btn.style.bottom = `${arr[i].offsetHeight - 50}px`
   
 else
   btn.style.bottom = `${arr[i].scrollHeight - 50}px`
 // fin de la stylisation du bouton
   
   console.log("Ajouté")
}
```

Tout d'abord, j'ai sélectionné tous les éléments avec le nom de classe `s-code-block` – mais pourquoi ? C'est parce que lorsque j'ai inspecté le site de StackOverflow, j'ai trouvé que tous les extraits de code étaient conservés dans une classe avec ce nom.

Et ensuite, nous parcourons tous ces éléments et ajoutons un bouton dans ces éléments. Enfin, nous positionnons et stylisons simplement le bouton correctement (le style n'est pas encore parfait – ce n'est qu'un début).

Lorsque nous chargeons l'extension en utilisant le processus que nous avons suivi ci-dessus et que nous visitons StackOverflow, nous devrions voir un bouton de copie.

### Comment ajouter une fonctionnalité au bouton

Maintenant, lorsque le bouton est cliqué, nous voulons que l'ensemble de l'extrait soit copié dans notre presse-papiers. Pour cela, ajoutez la ligne de code suivante au fichier `main.js` :

```js
var button = document.querySelectorAll(".copy_code_button")
 button.forEach((elm) => {
  elm.addEventListener('click', (e) => {
    navigator.clipboard.writeText(elm.parentNode.childNodes[0].innerText)
    alert("Copié dans le presse-papiers")
  })
 })
```

Tout d'abord, nous sélectionnons tous les boutons que nous avons ajoutés au site en utilisant `querySelectorAll`. Ensuite, nous écoutons l'événement de clic chaque fois que le bouton est cliqué.

```js
navigator.clipboard.writeText(elm.parentNode.childNodes[0].innerText)
```

La ligne de code ci-dessus copie le code dans notre presse-papiers. Chaque fois qu'un extrait est copié, nous alertons l'utilisateur avec le message `Copié dans le presse-papiers` et nous avons terminé.

## Mots de la fin

Les extensions web peuvent être utiles de diverses manières et j'espère qu'avec l'aide de cet article, vous serez en mesure d'écrire vos propres extensions.

Tout le code peut être trouvé dans [ce dépôt GitHub](https://github.com/Abhilekhgautam/Copy-Code). N'oubliez pas de faire une demande de tirage chaque fois que vous proposez un bon style ou une nouvelle fonctionnalité comme l'historique du presse-papiers et autres.

**Bon codage !**