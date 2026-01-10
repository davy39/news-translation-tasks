---
title: Comment utiliser LocalStorage en JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-02-20T21:37:46.000Z'
originalURL: https://freecodecamp.org/news/use-local-storage-in-modern-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/JavaScript-localStorage-freeCodeCamp-Benjamin-Semah.png
tags:
- name: JavaScript
  slug: javascript
- name: localstorage
  slug: localstorage
- name: storage
  slug: storage
- name: Web Development
  slug: web-development
seo_title: Comment utiliser LocalStorage en JavaScript
seo_desc: 'In modern web development, having a way to persist data helps developers
  improve performance and create a better user experience. And using local storage
  is an effective way of persisting data in an application.

  In this article, you will learn what l...'
---

Dans le développement web moderne, disposer d'un moyen de persister les données aide les développeurs à améliorer les performances et à créer une meilleure expérience utilisateur. Et l'utilisation du stockage local est un moyen efficace de persister les données dans une application.

Dans cet article, vous apprendrez ce qu'est le stockage local et comment l'utiliser dans les applications web modernes. Vous apprendrez également les avantages de l'utilisation du stockage local, ainsi que certaines de ses limitations.

## Table des matières

* [Qu'est-ce que le stockage local ?](#quest-ce-que-le-stockage-local)
    
* [Différences entre le stockage local et le stockage de session](#differences-entre-le-stockage-local-et-le-stockage-de-session)
    
* [Comment utiliser le stockage local](#comment-utiliser-le-stockage-local)
    
* [Un exemple pratique](#un-exemple-pratique)
    
* [Comment afficher le stockage local dans DevTools](#comment-afficher-le-stockage-local-dans-devtools)
    
* [Avantages de l'utilisation du stockage local](#avantages-de-lutilisation-du-stockage-local)
    
* [Limitations du stockage local](#limitations-du-stockage-local)
    
* [Conclusion](#conclusion)
    

## Qu'est-ce que le stockage local ?

Le stockage local est une fonctionnalité des navigateurs web qui permet aux développeurs de sauvegarder des données dans le navigateur de l'utilisateur. Il fait partie de l'API de stockage web, avec le stockage de session.

Le stockage local fonctionne en acceptant des données sous forme de paires clé-valeur. Il conserve les données même lorsque l'utilisateur actualise la page ou ferme l'onglet ou le navigateur.

## Différences entre le stockage local et le stockage de session

Comme je l'ai mentionné précédemment, l'API de stockage web dans les navigateurs modernes fournit deux fonctionnalités principales pour le stockage des données. Il s'agit du stockage local et du stockage de session.

Les différences clés entre les deux sont la durée de vie des données stockées et leur portée.

Les données dans le stockage local restent disponibles même lorsque l'onglet/le navigateur est fermé. Mais la fermeture de l'onglet/du navigateur efface toutes les données stockées dans le stockage de session.

De plus, les données dans le stockage local sont accessibles dans plusieurs onglets et fenêtres du navigateur. En revanche, les données dans le stockage de session ne sont accessibles que dans des onglets spécifiques du navigateur et ne sont pas partagées.

## Comment utiliser le stockage local

L'objet de stockage local fournit différentes méthodes que vous pouvez utiliser pour interagir avec lui. Avec ces méthodes, vous pouvez ajouter, lire et supprimer des données du stockage local.

### Comment stocker des données dans le stockage local

Pour stocker des données dans le stockage local, vous utilisez la méthode `setItem()`. Cette méthode prend deux arguments, une clé et une valeur.

```javascript
localStorage.setItem(key, value)
```

Si la clé n'existe pas dans le stockage local, la méthode `setItem()` créera une nouvelle clé et lui assignera la valeur donnée. Mais si une clé avec le même nom existe dans le stockage local, elle mettra à jour la valeur de la clé avec la valeur fournie.

### Comment lire des données depuis le stockage local

Pour récupérer et utiliser des données depuis le stockage local, vous utilisez la méthode `getItem()`. Cette méthode prend une clé comme argument.

```javascript
localStorage.getItem(key)
```

Si la clé donnée existe dans le stockage local, la méthode retourne la valeur de cette clé. Si elle n'existe pas, la méthode retourne `null`.

### Comment stocker et lire des valeurs de données complexes dans le stockage local

Le stockage local ne peut stocker que des chaînes de caractères. Cela signifie que si vous devez stocker des valeurs comme des objets ou des tableaux, vous devez d'abord obtenir une représentation sous forme de chaîne de la valeur. Vous faites cela en utilisant la méthode `JSON.stringify()`.

Exemple :

```javascript
const userObj = {
  username = "Maria",
  email: "maria@mail.com"
}

localStorage.setItem('user', JSON.stringify(userObj))
```

La méthode `JSON.stringify()` convertit l'objet `userObj` en une représentation sous forme de chaîne avant de l'envoyer au stockage local.

Maintenant, lorsque vous voulez récupérer les données depuis le stockage local, vous devez également les convertir de leur représentation sous forme de chaîne à leur forme originale. Et vous faites cela en utilisant la méthode `JSON.parse()`.

Exemple :

```javascript
const storedUserData = localStorage.getItem('user')

if (storedUserData) {
  const userData = JSON.parse(storedUserData)
  // Vous pouvez utiliser userData ici...
} else {
  console.log('Données utilisateur non trouvées dans le stockage local')
}
```

Dans l'exemple ci-dessus, nous vérifions d'abord s'il y a des données pour 'user' dans le stockage local avant d'utiliser la méthode `JSON.parse()`. Cela est important car si elle n'existe pas dans le stockage local, `JSON.parse()` sera appliqué à une valeur `null` (ce qui entraînera une erreur).

### Comment supprimer des données du stockage local

Il existe deux méthodes disponibles pour supprimer des données du stockage local. L'une est la méthode `removeItem()` et l'autre est la méthode `clear()`.

Vous utilisez la méthode `removeItem()` lorsque vous voulez supprimer un seul élément du stockage local. La méthode prend une clé comme argument et supprime la paire clé-valeur correspondante du stockage local.

```javascript
localStorage.removeItem(key)
```

Mais que faire si, au lieu de supprimer une seule paire clé-valeur, vous voulez effacer toutes les données du stockage local ? Eh bien, le stockage local a une méthode pour cela - la méthode `clear()`.

```javascript
localStorage.clear()
```

La méthode `clear()` supprime toutes les paires clé-valeur dans le stockage local pour le domaine actuel.

### Comment obtenir le nom d'une clé dans le stockage local

Si vous voulez obtenir le nom d'une clé à un index particulier dans le stockage local, vous pouvez utiliser la méthode `key()`. Elle prend un nombre comme argument et retourne le nom de la clé à cet index spécifié.

Exemple :

```javascript
localStorage.key(0)
```

L'exemple ci-dessus retournera le nom de la clé à l'index 0. Si il n'y a pas de clé à l'index spécifié, la méthode retournera null.

## Un exemple pratique

Ce qui suit montre une démonstration pratique de la différence entre le stockage local et le stockage de session.

Dans cet exemple, nous allons sauvegarder le nom de l'utilisateur dans le stockage local et sauvegarder l'âge dans le stockage de session.

```html
<!-- HTML --> 
<body>

  <h1 class="userName"></h1>
  <h2 class="userAge"></h2>

  <input type="text" class="name" placeholder="Entrez le nom ici"/>
  <button class="saveNameBtn">Sauvegarder le nom</button>
  
  <br />

  <input type="text" class="age" placeholder="Entrez l'âge ici"/>
  <button class="saveAgeBtn">Sauvegarder l'âge</button>
  
</body>
```

Le balisage inclut deux éléments d'en-tête. Un pour `userName` et l'autre pour `userAge`. Il inclut également deux éléments d'entrée pour le nom et l'âge. Chaque entrée a un bouton associé que nous utiliserons pour sauvegarder les données.

Maintenant, utilisons la méthode `querySelector` pour sélectionner les différents éléments.

```javascript
const userNameText = document.querySelector(".userName")
const userAgeText = document.querySelector(".userAge")

const saveNameButton = document.querySelector(".saveNameBtn")
const saveAgeButton = document.querySelector(".saveAgeBtn")
```

### Exemple de code pour le stockage local

```javascript
saveNameButton.addEventListener("click", () => {
  const userName = document.querySelector(".name").value
  userNameText.textContent = userName
  localStorage.setItem("name", userName)
})
```

Tout d'abord, nous obtenons la valeur de l'entrée du nom, nous la définissons comme le `textContent` de `userNameText`. Ensuite, nous utilisons le `setItem()` du stockage local pour sauvegarder la valeur `userName` dans le stockage local.

Ensuite, voyons comment nous pouvons obtenir la valeur du nom depuis le stockage local lorsque nous en avons besoin.

```javascript
function displayUserName () {
  const nameFromLocalStorage = localStorage.getItem("name")

  if (nameFromLocalStorage) {
    userNameText.textContent = nameFromLocalStorage
  } else {
    userNameText.textContent = "Aucune donnée de nom dans le stockage local"
  }
}

displayUserName()
```

La fonction `displayUserName` obtient `nameFromLocalStorage` en utilisant la méthode `getItem()`. Si la valeur existe dans le stockage local, nous la définissons comme le `textContent` de l'élément `userNameText`. Si elle est `null` ou n'existe pas, alors nous définissons `textContent` sur la chaîne *"Aucune donnée de nom dans le stockage local"*.

### Exemple de code pour le stockage de session

Maintenant, faisons la même chose pour la valeur `age`. La seule différence ici sera l'utilisation du stockage de session au lieu du stockage local.

```javascript

saveAgeButton.addEventListener("click", () => {
  const userAge = document.querySelector(".age").value
  userAgeText.textContent = userAge
  sessionStorage.setItem("age", userAge)
})

function displayUserAge () {
  const ageFromSessionStorage = sessionStorage.getItem("age")

  if (ageFromSessionStorage) {
    userAgeText.textContent = ageFromSessionStorage
  } else {
    userAgeText.textContent = "Aucune donnée d'âge dans le stockage de session"
  }
}

displayUserAge()
```

Les méthodes `setItem` et `getItem` fonctionnent également pour le stockage de session.

### Démo :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/demo.gif align="left")

*Démo du stockage local et du stockage de session.*

Comme vous pouvez le voir dans la démo ci-dessus, lorsque vous fermez et rouvrez la page, les données `name` du stockage local persistent. Mais les données `age` du stockage de session sont effacées une fois la page fermée.

[Essayez le code sur StackBlitz](https://stackblitz.com/edit/vitejs-vite-hb86sa?file=index.html,main.js&terminal=dev)

## Comment afficher le stockage local dans DevTools

Vous pouvez suivre les étapes ci-dessous pour inspecter le contenu du stockage local dans les outils de développement de votre navigateur.

Tout d'abord, ouvrez DevTools. Vous pouvez le faire en cliquant avec le bouton droit sur la page web et en sélectionnant "Inspecter".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-ONE.gif align="left")

*Démo de comment ouvrir les DevTools.*

Ensuite, sélectionnez l'onglet "Application" dans le panneau DevTools. Selon votre navigateur, ce panneau peut avoir un nom différent. Par exemple, il s'appelle "Stockage" dans Safari et Firefox.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-TWO.gif align="left")

*Démo de comment ouvrir le panneau "Application" dans DevTools.*

Localisez la section "Stockage" dans la barre latérale montrant une liste des diverses options de stockage web.

Cliquez sur "Stockage local" pour développer et afficher son contenu.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-THREE.gif align="left")

*Démo de comment ouvrir l'onglet de stockage local dans le panneau de stockage.*

Vous pouvez cliquer sur des éléments individuels pour afficher la paire clé-valeur correspondante.

## Avantages de l'utilisation du stockage local

Voici quelques-uns des avantages du stockage local par rapport à d'autres mécanismes de stockage dans le développement web moderne.

1. **Données persistantes :** Lorsque vous utilisez le stockage local, les données stockées restent même lorsque l'utilisateur ferme l'onglet ou le navigateur. Cela est utile pour sauvegarder les préférences de l'utilisateur, les paramètres et autres données pertinentes. Cela peut aider à créer une expérience utilisateur fluide.
    
2. **Accès hors ligne :** Vous pouvez utiliser le stockage local comme moyen de mettre en cache des données qui peuvent être accessibles même avec un accès internet limité ou inexistant. Cela en fait une fonctionnalité utile pour les applications qui dépendent de la mise en cache des données pour une utilisation hors ligne comme les lecteurs de nouvelles, les applications de productivité, etc.
    
3. **Capacité de stockage plus importante :** Comparé à d'autres moyens de stockage, le stockage local a une capacité relativement élevée. Par exemple, les cookies sont limités à 4 kilo-octets par domaine. Mais le stockage local peut stocker jusqu'à 5 méga-octets de données par domaine.
    

## Limitations de l'utilisation du stockage local

1. **Stocke uniquement des chaînes de caractères :** Comme vous l'avez appris précédemment, le stockage local ne peut stocker que des valeurs de type chaîne. Vous pouvez utiliser les méthodes JSON `stringify` et `parse` pour contourner cela. Mais certains développeurs web peuvent ne pas le préférer car cela peut conduire à écrire un code complexe qui est difficile à déboguer.
    
2. **Problèmes de sécurité :** Les données dans le stockage local peuvent être vulnérables à des attaques comme le cross-site scripting (XSS). Par conséquent, vous devez être prudent lorsque vous travaillez avec des informations sensibles. Il est conseillé d'évaluer les implications de sécurité et de considérer d'autres alternatives lorsque cela est nécessaire.
    
3. **Non accessible aux web workers :** Le stockage local fait partie de l'objet Window. Par conséquent, il est lié au thread d'exécution principal de la page web. Cela signifie qu'il n'est pas accessible aux web workers. Donc, si vous exécutez des processus en arrière-plan, vous ne pouvez pas utiliser le stockage local dans les scripts des web workers.
    

## Conclusion

Le stockage local est une fonctionnalité des navigateurs web modernes qui facilite le stockage et la persistance des données entre les sessions du navigateur pour les développeurs web.

Comparé aux cookies traditionnels, il offre des capacités de stockage plus importantes. De plus, contrairement aux cookies, il ne dépend pas des processus côté serveur. Cela réduit le besoin de requêtes fréquentes au serveur et aide à améliorer les performances.

Dans cet article, vous avez appris comment utiliser le stockage local. Nous avons couvert la sauvegarde, la récupération et la suppression de données du stockage local. Vous avez également appris certains des avantages de l'utilisation du stockage local dans votre projet, ainsi que certaines de ses limitations.

Merci d'avoir lu. Et bon codage ! Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).