---
title: Comprendre Hello World dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-27T10:08:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-understanding-hello-world-in-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-26-at-3.14.04-PM.png
tags:
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
seo_title: Comprendre Hello World dans Node.js
seo_desc: "By Clark Jason Ngo\nHow I wish there was a documentation that shows me\
  \ a detailed explanation of what's happening in a Hello World example. \nWell. Instead\
  \ of wishing, I started to craft a nice visual for my own and I hope this would\
  \ help others as wel..."
---

Par Clark Jason Ngo

Comme je souhaite qu'il existe une documentation qui montre une explication détaillée de ce qui se passe dans un exemple Hello World. 

Bien. Au lieu de souhaiter, j'ai commencé à créer une belle visualisation pour moi-même et j'espère que cela aidera les autres également.

**Quelques explications de base :**

**Qu'est-ce que Node.js ?**

* Un environnement serveur open source.
* Il vous permet d'exécuter JavaScript sur le serveur.

**Node.js utilise la programmation asynchrone**

* générer du contenu de page dynamique
* créer, ouvrir, lire, écrire, supprimer et fermer des fichiers sur le serveur
* collecter des données de formulaire
* ajouter, supprimer et modifier des données dans votre base de données

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-150.png)
_Serveur HTTP_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-151.png)
_fonction et paramètres req et res_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-152.png)
_Code d'état_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-153.png)
_Content-Type_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-154.png)
_Finalisation de la requête_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-155.png)
_Écoute du port_

---

Ce dont vous avez besoin pour exécuter cela sur votre machine :

1. Installer VSCode : [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Installer Node.js : [https://nodejs.org/en/](https://nodejs.org/en/).
3. Créer un fichier nommé `app.js`.
4. Copier le code ci-dessous.
5. Dans votre terminal, exécutez `node app.js`. 
6. Dans votre navigateur, tapez [http://localhost:8080/](http://localhost:8080/) et appuyez sur Entrée.

```js
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
}).listen(8080);
```

%[https://youtu.be/sTB3oP_5UXU]

**Références :**

[https://www.w3schools.com/nodejs/default.asp](https://www.w3schools.com/nodejs/default.asp)

[https://nodejs.org/api/http.html](https://nodejs.org/api/http.html)