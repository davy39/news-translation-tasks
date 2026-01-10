---
title: Comment configurer VS Code pour le développement web en quelques étapes simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-20T22:12:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-vs-code-for-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/ep11-vscode-1.jpg
tags:
- name: editor
  slug: editor
- name: Visual Studio Code
  slug: vscode
- name: Web Development
  slug: web-development
seo_title: Comment configurer VS Code pour le développement web en quelques étapes
  simples
seo_desc: "By Thu Nghiem\nVisual Studio Code has become the most popular source code\
  \ editor out there. It is lightweight but powerful, and it is no doubt my favorite.\
  \ \nIn this article, I am going to walk you through how to get started and set up\
  \ VS Code for Web ..."
---

Par Thu Nghiem

Visual Studio Code est devenu l'éditeur de code source le plus populaire. Il est léger mais puissant, et c'est sans doute mon préféré. 

Dans cet article, je vais vous guider à travers les étapes pour commencer et configurer VS Code pour les développeurs web.  
  
Voici une vidéo que vous pouvez regarder si vous souhaitez compléter cet article :

%[https://youtu.be/uovNnCjjfx4]

## Introduction à VS Code

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.22.57.png)
_Télécharger Visual Studio Code_

Si vous n'avez pas encore VS Code installé sur votre ordinateur, rendez-vous sur [code.visualstudio.com](https://code.visualstudio.com/) pour le télécharger. Vous pouvez ouvrir le menu déroulant pour choisir les versions que vous souhaitez télécharger, mais généralement, le gros bouton devrait suffire.

## Onglet d'accueil de VS Code

Une fois installé et ouvert, la première chose que vous verrez est un onglet d'accueil. Ici, vous trouverez 5 sections :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.26.12.png)
_Onglet d'accueil_

**Démarrer** : Vous pouvez choisir de créer un nouveau fichier ou d'ouvrir un dossier.

**Récent** : Vous pouvez trouver les dossiers récemment ouverts.

**Aide** : Vous pouvez trouver des informations utiles. Par exemple, le cheat sheet imprimable du clavier ou une série de vidéos d'introduction.

**Personnaliser** : Vous pouvez voir que vous pouvez installer des paramètres et des raccourcis clavier d'autres éditeurs de code comme Vim ou Atom. Donc, si vous êtes habitué à utiliser ces éditeurs pour le moment, vous pouvez aller de l'avant et les vérifier.

Mais ce que nous voulons examiner, c'est le **thème de couleur**. Si vous le sélectionnez, vous pouvez voir qu'il y a une liste de thèmes parmi lesquels choisir. Vous pouvez également utiliser les touches fléchées haut et bas pour prévisualiser les thèmes. Mais mon thème préféré est celui par défaut, donc je vais rester avec celui-ci.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.59.13.png)
_Thème de couleur_

**Apprendre** : Ici, vous trouverez 3 sélections. La première sélection de la liste est **Trouver et exécuter toutes les commandes**. Avec cela, nous pouvons trouver et exécuter toutes les commandes disponibles. Nous allons utiliser cela souvent, donc je vous recommande de mémoriser le raccourci, qui est `Command/Control + Shift + P`.

La deuxième sélection est **Aperçu de l'interface**. Si nous la sélectionnons, nous pouvons voir les éléments les plus courants de l'interface utilisateur et nous pouvons également voir le raccourci pour basculer les éléments :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.30.16.png)
_Aperçu de l'interface_

La dernière sélection est **Interactive Editor Playground**. Ici, vous pouvez trouver les fonctionnalités mises en avant de VS Code avec des instructions et des exemples.

Sélectionnons **Emmet**, par exemple. Avec **Emmet**, nous pouvons écrire des raccourcis et les développer en un morceau de code.

Par exemple, si nous voulons créer un élément de liste non ordonnée avec 3 éléments à l'intérieur et chaque élément a un nom de classe "fruit", nous pouvons taper `ul>li.fruit*3` et appuyer sur `tab`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/emmet.gif)
_Emmet dans Interactive Editor Playground_

Vous pouvez également voir que dans l'exemple existant (`ul>li.item$*5`), ils ont essayé de créer un élément de liste non ordonnée et 5 éléments avec un nom de classe `item` à l'intérieur. Mais le nom de classe est également accompagné d'une _numérotation_ :

```html
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
</ul>
```

Dans cette section, vous pouvez également trouver un lien vers le [Emmet Cheat Sheet](https://docs.emmet.io/cheat-sheet/), qui est super utile.

D'accord, je vous recommande de vérifier toutes ces fonctionnalités. Il y en a beaucoup, et ce n'est pas grave si vous ne comprenez pas tout maintenant. Vous pouvez toujours revenir plus tard.

## Explorateur de fichiers de VS Code

Ensuite, allons à **Explorateur de fichiers** en sélectionnant le premier onglet de la navigation latérale ou `Command/Control + Shift + E`.

Ici, vous pouvez ouvrir un dossier existant, mais créons un nouveau dossier et un nouveau fichier. Au lieu d'ouvrir une nouvelle fenêtre, ouvrons le terminal dans VS Code. Vous pouvez sélectionner le bouton **erreur et avertissement** sur la barre d'état, puis sélectionner l'onglet `Terminal` ou utiliser le raccourci `Control + ``.

En ce moment, je suis dans mon répertoire personnel. Créons un nouveau dossier en tapant `mkdir vscode-tutoriels` et entrons dedans avec `cd vscode-tutoriels`. 

Maintenant, nous voulons ouvrir ce dossier, donc nous pouvons sélectionner le bouton `ouvrir le dossier` et naviguer jusqu'au répertoire du dossier – mais c'est beaucoup de travail. Donc, dans le terminal, nous pouvons dire `code .`. Maintenant, vous pourriez rencontrer une erreur : `bash: code: commande introuvable`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.52.42.png)
_Terminal dans VS Code_

Pour corriger cela, nous pouvons ouvrir la **Palette de commandes** et rechercher `Shell Command: Install code command in Path`, puis la sélectionner. Maintenant, si nous retournons au terminal et tapons `code .`, la nouvelle fenêtre VS Code s'ouvrira avec le dossier créé.

D'accord, ensuite, nous voulons créer un nouveau fichier. Dans la section du dossier, nous pouvons cliquer sur l'icône de nouveau fichier ou faire un clic droit et sélectionner `nouveau fichier`. Nommons le fichier `index.html`, et à l'intérieur, tapons le point d'exclamation (!) et appuyons sur tab ou entrer. Avec **Emmet**, il générera un modèle HTML.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.55.20.png)
_Génération de HTML avec Emmet dans VS Code_

Maintenant, ouvrons à nouveau la **Palette de commandes**, et recherchons **Format Document** et sélectionnons-le. Vous pouvez voir qu'il ajoute des espacements entre les différentes sections et nettoie notre code. 

C'est une fonctionnalité super utile de VS Code. Mais nous ne voulons pas rechercher **Format Document** tout le temps et nous voulons qu'il formate chaque fois que nous enregistrons le fichier.

Vous remarquez également ici que l'indentation est maintenant égale à **4 espaces**, ce qui, à mon avis, est un peu trop. Donc, changeons-la à 2. Et pour cela, nous pouvons aller dans les paramètres ou utiliser le raccourci `Command/Control + ,`. 

Dans l'onglet **Communément utilisé**, nous pouvons changer la taille de la tabulation à 2 et sous **Éditeur de texte/Mise en forme**, nous pouvons sélectionner **Formater à l'enregistrement**. Maintenant, chaque fois que nous enregistrons, les fichiers seront correctement formatés.

## Extensions de VS Code

La dernière chose que je veux vous montrer à utiliser est **Extensions**. Vous pouvez sélectionner l'onglet des extensions dans la navigation latérale ou avec le raccourci : `Command/Control + Shift + X`.

Ici, nous pouvons filtrer les extensions par, par exemple, **Les plus populaires** ou **Recommandées**. 

Il y a de nombreuses extensions parmi lesquelles choisir. Mais la première extension que nous devons installer est [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer). Avec cela, nous pouvons avoir un serveur local qui recharge les pages web statiques.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-20-at-17.56.38.png)
_Extension Live Server_

Par exemple, si nous allons dans notre `index.html` et ouvrons la Palette de commandes et recherchons **Live Server: Open with Live Server**, vous pouvez voir qu'un nouvel onglet dans le navigateur est ouvert. 

Et si nous créons un nouvel élément sur notre HTML, par exemple `<h1>Introduction à VScode<h1/>`, après avoir enregistré, la page sera automatiquement rechargée et nous pouvons voir les changements. Dans `index.html`, vous pouvez également ouvrir le serveur en direct avec le bouton **go live** sur la barre d'état.

## Conclusion

Il existe de nombreuses autres extensions utiles, mais je les couvrirai dans un autre article et une autre vidéo.

Pour l'instant, avec ce guide d'introduction et de configuration, je suis sûr que vous êtes prêt à commencer votre parcours en développement web.

Cela conclut l'article. Vous pouvez me suivre sur les réseaux sociaux pour les mises à jour futures. Sinon, restez heureux en codant et à bientôt dans les prochains articles.  
  
__________ 🐣 À propos de moi __________

* Je suis le fondateur de [DevChallenges](https://devchallenges.io/)
* Abonnez-vous à [ma Chaîne](https://www.youtube.com/c/thunghiem)
* Suivez-moi sur [Twitter](https://twitter.com/thunghiemdinh)
* Rejoignez [Discord](https://discord.com/invite/3R6vFeM)