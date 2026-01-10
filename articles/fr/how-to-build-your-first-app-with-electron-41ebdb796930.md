---
title: Comment créer votre première application de bureau avec JavaScript en utilisant
  Electron
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-06T16:34:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-app-with-electron-41ebdb796930
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aBsgPiEeOE5lLoippRm7BA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer votre première application de bureau avec JavaScript en utilisant
  Electron
seo_desc: 'By Carol-Theodor Pelu

  Have you ever wondered if you can build cross-platform desktop apps with HTML, CSS,
  and JavaScript?

  It is possible with Electron.

  This article will help you understand some core concepts of Electron.

  By the end of this post, you...'
---

Par Carol-Theodor Pelu

Avez-vous déjà pensé à créer des applications de bureau multiplateformes avec HTML, CSS et JavaScript ?

C'est possible avec Electron.

Cet article vous aidera à comprendre certains concepts fondamentaux d'Electron.

À la fin de cet article, vous connaîtrez le processus de création d'applications de bureau multiplateformes avec Electron, HTML et CSS.

Avant de commencer, vous pouvez consulter à l'avance l'application que nous allons créer dans ce tutoriel.

_Hear Me Type_ aura une fonctionnalité simple mais directe. Chaque touche pressée sur le clavier jouera un son spécifique. Donc, si j'appuie sur la touche "A", l'application jouera le son spécifique pour la lettre A.

Il existe deux versions disponibles pour le téléchargement. Le [code source de ce tutoriel](https://github.com/Tynael/Hear-Me-Type-Tutorial), et une [version avancée](https://github.com/Tynael/Hear-Me-Type) de l'application, recommandée pour les utilisateurs plus expérimentés d'Electron.

Le code changera car j'ajoute de nouvelles fonctionnalités et améliorations. Assurez-vous de revenir pour voir ce qui est nouveau.

Sans plus tarder, découvrons plus sur Electron et créons notre première application !

### Qu'est-ce qu'Electron ?

Electron est un framework pour les applications de bureau multiplateformes utilisant Chromium et Node.js.

Il est facile de créer des applications multiplateformes en utilisant HTML, CSS et JavaScript. Votre application sera compatible avec les systèmes d'exploitation Mac, Windows et Linux dès le départ.

D'autres fonctionnalités intégrées sont :

* **Mises à jour automatiques** — permettent aux applications de se mettre à jour automatiquement
* **Menus et notifications natifs** — créent des menus d'application natifs et des menus contextuels
* **Rapport de plantage d'application** — vous pouvez soumettre des rapports de plantage à un serveur distant
* **Débogage et profilage** — le module de contenu de Chromium trouve les goulots d'étranglement de performance et les opérations lentes. Vous pouvez également utiliser vos outils de développement Chrome préférés dans votre application.
* **Installeur Windows** — vous pouvez créer des packages d'installation. Rapide et simple.

Si vous êtes satisfait de ce qu'Electron offre, plongeons plus profondément et créons une simple application Electron.

Avant de nous mettre au travail, vous devrez installer [Node.js](https://nodejs.org/en/download/). Vous devriez également avoir un compte [GitHub](https://github.com/join?source=header) pour stocker et mettre à jour votre application. Bien qu'un compte ne soit pas nécessaire, il est fortement recommandé. GitHub est une norme industrielle et il est important de savoir comment l'utiliser.

Nous utiliserons GitHub dans ce tutoriel.

### Getting Started

Lorsque vous êtes prêt, ouvrez une fenêtre de terminal pour votre système d'exploitation.

Suivez les instructions ci-dessous pour [cloner](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) le dépôt Git Electron Quick Start sur votre ordinateur.

Nous allons construire notre logiciel sur la base d'Electron Quick Start.

```
# Clonez le dépôt Quick Start
git clone https://github.com/electron/electron-quick-start
# Allez dans le dépôt
cd electron-quick-start
# Installez les dépendances et exécutez
npm install && npm start
```

Lorsque les étapes listées ci-dessus sont terminées, vous devriez voir l'application s'ouvrir dans ce qui ressemble à une fenêtre de navigateur. Et c'est effectivement une fenêtre de navigateur !

Le style de la fenêtre change en fonction du système d'exploitation. J'ai choisi d'utiliser l'apparence classique de Windows. Groovy !

![Image](https://cdn-media-1.freecodecamp.org/images/6dk5Yfd3NSg8JaR2-34cyuIXZy3IllZnnDAc)
_La fenêtre principale de notre application Electron Quick-Start._

Comme je le disais plus tôt, vous pouvez utiliser les outils de développement de Chrome dans votre application. Ce que vous pouvez faire avec les outils de développement de votre navigateur, vous pouvez aussi le faire dans l'application. Extraordinaire !

### Architecture de l'application Electron

Examinons le code source et la structure des fichiers de notre application. Ouvrez le projet dans votre éditeur de texte ou IDE préféré. Je vais utiliser [Atom](https://atom.io/) qui est construit sur... vous l'avez deviné... Electron !

![Image](https://cdn-media-1.freecodecamp.org/images/PFmH2g6ZVQ14CQy0Df1oIJ8ANKnN7YMBXXaw)
_Structure des dossiers et fichiers de notre nouvelle application._

Nous avons une structure de fichiers de base :

`electron-quick-start`

`- index.html`  
 `- main.js`  
 `- package.json`  
 `- render.js`

La structure des fichiers est similaire à celle que nous utilisons lors de la création de pages web.

Nous avons :

* `index.html` qui est une page web HTML5 servant un grand but : notre toile
* `main.js` crée des fenêtres et gère les événements système
* `package.json` est le script de démarrage de notre application. Il s'exécutera dans le processus principal et contiendra des informations sur notre application
* `render.js` gère les processus de rendu de l'application

Vous pouvez avoir quelques questions sur les processus principal et de rendu. Qu'est-ce que c'est et comment puis-je m'en sortir avec eux ?

Content que vous ayez demandé. Accrochez-vous à votre chapeau car cela peut être un nouveau territoire si vous venez du monde JavaScript du navigateur !

### Qu'est-ce qu'un processus ?

Lorsque vous voyez "processus", pensez à un processus au niveau du système d'exploitation. C'est une instance d'un programme informatique qui s'exécute dans le système.

Si je démarre mon application Electron et que je vérifie le Gestionnaire des tâches de Windows ou le Moniteur d'activité pour macOS, je peux voir les processus associés à mon application.

![Image](https://cdn-media-1.freecodecamp.org/images/Lxo5EGNxaU2WSP9xyrV-2PL8VDZOyaBnNsER)

Chacun de ces processus s'exécute en parallèle. Mais la mémoire et les ressources allouées pour chaque processus sont isolées des autres.

Supposons que je veuille créer une boucle `for` qui incrémente quelque chose dans un processus de rendu.

```
var a = 1;
```

```
for ( a = 1; a < 10; a ++) { console.log('Ceci est une boucle for');}
```

Les incréments ne sont disponibles que dans le processus de rendu. Cela n'affecte pas du tout le processus principal. Le message `Ceci est une boucle for` n'apparaîtra que sur le module rendu.

### Processus principal

Le processus principal contrôle la vie de l'application. Il dispose de l'API Node.js complète intégrée et ouvre des dialogues, et crée des processus de rendu. Il gère également d'autres interactions avec le système d'exploitation et démarre et quitte l'application.

Par convention, ce processus se trouve dans un fichier nommé `main.js`. Mais il peut avoir n'importe quel nom que vous souhaitez.

Vous pouvez également changer le fichier du processus principal en le modifiant dans le fichier `package.json`.

À des fins de test, ouvrez `package.json` et changez :

`"main" : "main.js"`,

en

`"main" : "mainTest.js"`,

Démarrez votre application et voyez si elle fonctionne toujours.

Gardez à l'esprit qu'il ne peut y avoir qu'un seul processus principal.

### Processus de rendu

Le processus de rendu est une fenêtre de navigateur dans votre application. Contrairement au processus principal, il peut y avoir plusieurs processus de rendu et chacun est indépendant.

Parce que chaque processus de rendu est séparé, un plantage dans l'un n'affectera pas un autre. Cela est dû à l'architecture multi-processus de Chromium.

Ces fenêtres de navigateur peuvent également être masquées et personnalisées car elles sont comme des fichiers HTML.  
   
Mais dans Electron, nous avons également l'API Node.js complète. Cela signifie que nous pouvons ouvrir des dialogues et d'autres interactions avec le système d'exploitation.

Pensez à cela comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/Sr3uE0N9q-Uv5L0Dimh61ld0JJiR-nFAHo3O)
_[Source : Kristian [Poslek](https://medium.com/developers-writing/building-a-desktop-application-with-electron-204203eeb658" rel="noopener" target="_blank" title=")]_

Une question reste. Peuvent-ils être liés d'une manière ou d'une autre ?

Ces processus s'exécutent simultanément et indépendamment. Mais ils doivent encore communiquer d'une manière ou d'une autre. Surtout puisque ils sont responsables de différentes tâches.

Pour cela, il existe un système de communication inter-processus ou IPC. Vous pouvez utiliser IPC pour passer des messages entre les processus principal et de rendu. Pour une explication plus approfondie de ce système, lisez l'article de Christian Engvall sur [ipcMain et ipcRenderer](https://www.christianengvall.se/ipcmain-and-ipcrenderer/).

Ce sont les bases des processus pour développer une application Electron.

Maintenant, revenons à notre code !

### Personnalisez-le

Donnons à notre dossier d'application un nom approprié.

Changez le nom du dossier de `electron-quick-start` à `hear-me-type-tutorial`.

Rouvrez le dossier avec votre éditeur de texte ou IDE préféré. Personnalisons davantage l'identité de notre application en ouvrant le fichier `package.json`.

`package.json` contient des informations vitales sur notre application. C'est là que vous définissez le nom, la version, le fichier principal, l'auteur, la licence et bien plus encore.

Mettons un peu de fierté et mettez-vous comme auteur de l'application.

Trouvez le paramètre "author" et changez la valeur par votre nom. Cela devrait ressembler à ceci :

`"author" : "Carol Pelu"`,

Nous devons également changer le reste des paramètres. Trouvez le `name` et `description` ci-dessous et changez-les dans votre fichier package.json :

![Image](https://cdn-media-1.freecodecamp.org/images/iHnCji2q4KIc2DDsYKU7wKk-qL6XvRyxcCYc)

Super ! Maintenant notre application a un nouveau nom et une description courte mais directe.

N'oubliez pas, vous pouvez toujours exécuter `npm start` dans votre terminal pour exécuter l'application et voir les changements que vous avez apportés.

Passons à l'étape suivante et ajoutons la fonctionnalité attendue de notre application. Nous voulons jouer un son spécifique pour chaque touche du clavier que nous pressons.

### Oh, la Fonctionnalité !

Qu'est-ce qu'une application sans fonctionnalité ? Pas grand-chose...

Maintenant, nous devons nous en occuper et donner à notre application la fonctionnalité qu'elle désire.

Pour faire réagir l'application à notre entrée, nous devons d'abord définir un élément sur lequel nous allons nous accrocher, puis déclencher l'action souhaitée.

Pour cela, nous allons créer des éléments `audio` avec des `id` spécifiques pour les touches du clavier que nous voulons. Ensuite, nous allons créer une instruction `switch` pour découvrir quelle touche du clavier a été pressée. Ensuite, nous jouerons un son spécifique attribué à cette touche.

Si cela semble un peu complexe pour vous maintenant, n'ayez pas peur. Je vais vous guider à travers chaque étape.

Téléchargez cette [archive](https://neutrondev.com/wp-content/uploads/2017/05/sounds.zip?x77671) contenant tous les fichiers sonores que nous allons utiliser. Nous allons bientôt les utiliser !

Ouvrez le fichier `index.html` et créons les éléments `<audio>` pour intégrer le contenu sonore dans notre application.

À l'intérieur de l'élément `<body>`, créez un élément div avec la balise de classe `audio`.

À l'intérieur de l'élément `div` créé, créez un élément `<audio>` avec un id de "A", la balise source de "sounds/A.mp3" et avec un attribut preload de "auto".

Nous utiliserons `preload="auto"` pour indiquer à l'application qu'elle doit charger l'ensemble du fichier audio lorsque la page se charge. `index.html` est le fichier principal de l'application, et tous nos fichiers sonores se chargeront lorsque l'application s'exécutera.

Le code devrait ressembler à ceci :

```
<div class="audio">
```

```
<audio id="A" src="sounds/A.mp3" preload="auto"></audio>
```

```
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/sKvM9fyEk1Rg3mCRPXQvLvbdYx4CDF58s5so)
_Votre fichier index.html devrait ressembler à ceci._

Maintenant, l'élément `<audio>` pointe vers un fichier source inconnu. Créons un dossier appelé `sounds` et décompressons tous les fichiers sonores à l'intérieur du dossier.

Super ! La seule chose importante qui manque pour le moment est le code JavaScript.

Créez un nouveau fichier appelé `functions.js`. Incluons-le dans le fichier `index.html` afin que le code JS soit prêt à l'emploi lorsque l'application est en cours d'exécution.

En suivant l'exemple de `require(./renderer.js')`, ajoutez cette ligne de code juste en dessous :

`require('./functions.js')`

Votre projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BzXjPH3U6HOL49ZmopqfxKx4L7cxgRp6rwSr)

Extraordinaire ! Maintenant que nous avons tout cousu, il est temps pour le moment de vérité.

Ouvrez le fichier `functions.js` et ajoutez le code JavaScript suivant dans le fichier. Je vais expliquer comment il fonctionne dans un instant.

```
document.onkeydown = function(e) {    switch (e.keyCode) {        case 65:            document.getElementById('A').play();            break;        default:            console.log("La touche n'est pas trouvée !");    }};
```

Le code devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/o23bi2Ap-bMlD0uuS8V0JiU64kghy6wd2NPN)

Ouvrez votre bash ou votre fenêtre de terminal. Assurez-vous d'être dans le dossier de votre projet et tapez `npm start` pour exécuter l'application.

Augmentez le volume de vos haut-parleurs et appuyez sur la touche **A** de votre clavier.

#MindBlown

![Image](https://cdn-media-1.freecodecamp.org/images/oydgxWivKeKhYtwKBTI6mGVadHYrxS71LrpY)

Le code JS est assez simple et direct.

Nous utilisons l'événement `onkeydown` sur l'objet `document` pour découvrir quel élément HTML est en cours d'accès. N'oubliez pas, l'objet `document` est la fenêtre principale de notre application.

Dans la fonction anonyme, nous utilisons une instruction `switch`. Son but est d'identifier la valeur Unicode de la touche du clavier pressée.

Si la valeur Unicode de la touche du clavier pressée est correcte, le son est joué. Sinon, une erreur "non trouvée" est générée. Cherchez le message dans la console.

Quelle aventure !

Vous avez peut-être remarqué que nous avons des fichiers sonores pour couvrir les touches A-Z et 0-9. Utilisons-les également pour qu'ils ne ressentent pas l'amertume de la solitude.

Rendez-vous dans `index.html` et créez un élément `<audio>` pour chaque touche pour laquelle nous avons un fichier sonore.

Le code devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vcy2HIf0WKJqzceuZAuURqC2xOwJqTRs4JJn)

Oui, bien sûr, vous pouvez copier-coller :

```
<audio id="B" src="sounds/B.mp3" preload="auto"></audio><audio id="C" src="sounds/C.mp3" preload="auto"></audio><audio id="D" src="sounds/D.mp3" preload="auto"></audio><audio id="E" src="sounds/E.mp3" preload="auto"></audio><audio id="F" src="sounds/F.mp3" preload="auto"></audio><audio id="G" src="sounds/G.mp3" preload="auto"></audio><audio id="H" src="sounds/H.mp3" preload="auto"></audio><audio id="I" src="sounds/I.mp3" preload="auto"></audio><audio id="J" src="sounds/J.mp3" preload="auto"></audio><audio id="K" src="sounds/K.mp3" preload="auto"></audio><audio id="L" src="sounds/L.mp3" preload="auto"></audio><audio id="M" src="sounds/M.mp3" preload="auto"></audio><audio id="N" src="sounds/N.mp3" preload="auto"></audio><audio id="O" src="sounds/O.mp3" preload="auto"></audio><audio id="P" src="sounds/P.mp3" preload="auto"></audio><audio id="Q" src="sounds/Q.mp3" preload="auto"></audio><audio id="R" src="sounds/R.mp3" preload="auto"></audio><audio id="S" src="sounds/S.mp3" preload="auto"></audio><audio id="T" src="sounds/T.mp3" preload="auto"></audio><audio id="U" src="sounds/U.mp3" preload="auto"></audio><audio id="V" src="sounds/V.mp3" preload="auto"></audio><audio id="W" src="sounds/W.mp3" preload="auto"></audio><audio id="X" src="sounds/X.mp3" preload="auto"></audio><audio id="Y" src="sounds/Y.mp3" preload="auto"></audio><audio id="Z" src="sounds/Z.mp3" preload="auto"></audio><audio id="0" src="sounds/0.mp3" preload="auto"></audio><audio id="1" src="sounds/1.mp3" preload="auto"></audio><audio id="2" src="sounds/2.mp3" preload="auto"></audio><audio id="3" src="sounds/3.mp3" preload="auto"></audio><audio id="4" src="sounds/4.mp3" preload="auto"></audio><audio id="5" src="sounds/5.mp3" preload="auto"></audio><audio id="6" src="sounds/6.mp3" preload="auto"></audio><audio id="7" src="sounds/7.mp3" preload="auto"></audio><audio id="8" src="sounds/8.mp3" preload="auto"></audio><audio id="9" src="sounds/9.mp3" preload="auto"></audio>
```

Super ! Maintenant, faisons la même chose pour le code JS dans `functions.js`.

Vous pouvez trouver les codes de caractères (codes de touches) sur ce [site web](https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes).

Mais oui, vous pouvez aussi copier-coller ceci :

```
document.onkeydown = function(e) {    switch (e.keyCode) {        case 48:            document.getElementById('0').play();            break;        case 49:            document.getElementById('1').play();            break;        case 50:            document.getElementById('2').play();            break;        case 51:            document.getElementById('3').play();            break;        case 52:            document.getElementById('4').play();            break;        case 53:            document.getElementById('5').play();            break;        case 54:            document.getElementById('6').play();            break;        case 55:            document.getElementById('7').play();            break;        case 56:            document.getElementById('8').play();            break;        case 57:            document.getElementById('9').play();            break;        case 65:            document.getElementById('A').play();            break;        case 66:            document.getElementById('B').play();            break;        case 67:            document.getElementById('C').play();            break;        case 68:            document.getElementById('D').play();            break;        case 69:            document.getElementById('E').play();            break;        case 70:            document.getElementById('F').play();            break;        case 71:            document.getElementById('G').play();            break;        case 72:            document.getElementById('H').play();            break;        case 73:            document.getElementById('I').play();            break;        case 74:            document.getElementById('J').play();            break;        case 75:            document.getElementById('K').play();            break;        case 76:            document.getElementById('L').play();            break;        case 77:            document.getElementById('M').play();            break;        case 78:            document.getElementById('N').play();            break;        case 79:            document.getElementById('O').play();            break;        case 80:            document.getElementById('P').play();            break;        case 81:            document.getElementById('Q').play();            break;        case 82:            document.getElementById('R').play();            break;        case 83:            document.getElementById('S').play();            break;        case 84:            document.getElementById('T').play();            break;        case 85:            document.getElementById('U').play();            break;        case 86:            document.getElementById('V').play();            break;        case 87:            document.getElementById('W').play();            break;        case 88:            document.getElementById('X').play();            break;        case 89:            document.getElementById('Y').play();            break;        case 90:            document.getElementById('Z').play();            break;        default:            console.log("La touche n'est pas trouvée !");        }};
```

Notre application est maintenant complète ! Félicitations !

![Image](https://cdn-media-1.freecodecamp.org/images/tobZ6s1lbq0mCLO6q6JTb7mPn5qXhu4kbczt)

La fonctionnalité principale de l'application est terminée, mais il reste encore du travail à faire !

### Polska ja ! (Polissez-moi !)

Même si l'application est fonctionnelle, il lui manque encore quelques éléments ici et là.

Par exemple, dans le fichier `index.html`, vous pouvez changer le titre de l'application et le contenu de la fenêtre principale.

De plus, l'application n'a pas de design, pas de belles couleurs, et pas d'images de chats ou de chiens.

Libérez votre imagination et trouvez des moyens d'améliorer le design de l'application.

Le code n'est pas parfait non plus. Nous avons beaucoup de code identique qui peut être optimisé et amélioré. Cela entraînera moins de lignes de code et ce sera moins douloureux pour les yeux.

Le code dupliqué est une mauvaise pratique !

### Testez-le ! Testez-le simplement !

Un bon logiciel doit être soigneusement testé.

Je vous suggère de commencer par appuyer sur chaque touche du clavier pour voir ce qui se passe.

Le meilleur scénario est que vous entendrez l'audio pour chaque touche du clavier que vous avez spécifiée dans le code. Mais que se passera-t-il lorsque vous appuierez sur plusieurs touches à la suite aussi vite que possible ? Et les touches qui ne sont même pas censées être pressées comme les boutons Home et NumLock ?

Que se passe-t-il si vous minimisez l'application et essayez d'appuyer sur une touche ? Entendez-vous un son ? Et que se passe-t-il lorsque vous n'avez pas la fenêtre de l'application sélectionnée et que vous appuyez sur une touche du clavier, entendez-vous encore des sons ?

La réponse est malheureusement non.

Ce comportement est dû à l'architecture sur laquelle Electron a été construit. Il vous permet d'obtenir des touches globales comme vous pouvez le faire avec le langage C#, mais vous ne pouvez pas enregistrer de frappes de touches individuelles. Cela est en dehors du cadre des cas d'utilisation normaux pour une application Electron.

Parcourez le code ligne par ligne et essayez de le casser. Voyez ce qui se passe et quels types d'erreurs Electron génère. Cet exercice vous aidera à devenir meilleur en débogage. Si vous connaissez les défauts de votre application, vous savez alors comment les corriger et rendre l'application meilleure.

Dans le fichier `functions.js`, j'ai intentionnellement utilisé un événement JavaScript obsolète. Pouvez-vous le repérer ?

Une fois que vous l'avez trouvé, j'aimerais que vous réfléchissiez à la manière dont vous pouvez le remplacer sans changer la fonctionnalité de l'application.

L'utilisation de code obsolète est une mauvaise pratique et peut entraîner des bugs sérieux dont vous ne soupçonnez même pas l'existence. Restez à jour avec la documentation du langage pour voir ce qui a pu changer. Restez toujours à jour.

### Conclusion

Je voudrais remercier et féliciter vous pour être arrivé à ce point !

Vous avez maintenant les connaissances pour créer une simple application Electron multiplateforme.

Si vous souhaitez approfondir Electron et voir sur quoi je travaille, consultez [Hear Me Type](https://github.com/Tynael/Hear-Me-Type) et [mon profil](https://github.com/Tynael) sur GitHub.

N'hésitez pas à cloner, forker, étoiler et contribuer à l'un de mes projets publics.

Veuillez revenir et relire cet article de temps en temps. Je le modifierai pour rester à jour avec les mises à jour d'Electron.

Merci beaucoup d'avoir pris le temps de lire mon article.

Cet article a été initialement publié sur [NeutronDev.com](https://www.NeutronDev.com).

Si vous souhaitez plus d'articles/tutoriels détaillés sur Electron, cliquez sur le ? ci-dessous. N'hésitez pas à laisser un commentaire.