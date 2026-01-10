---
title: Comment installer Node.js et npm sur Windows
subtitle: ''
author: Daniel Rosa
co_authors: []
series: null
date: '2022-03-02T00:18:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-digital-buggu-171198--1-.jpg
tags:
- name: node
  slug: node
- name: npm
  slug: npm
- name: Windows
  slug: windows
seo_title: Comment installer Node.js et npm sur Windows
seo_desc: 'In this article, you''ll learn how to work with JavaScript in the backend
  using Node on Windows.

  When you start working with JavaScript and discover that you can not only work with
  it in the frontend but also in the backend, a new world of possibiliti...'
---

Dans cet article, vous apprendrez à travailler avec JavaScript dans le backend en utilisant Node sur Windows.

Lorsque vous commencez à travailler avec JavaScript et que vous découvrez que vous pouvez non seulement l'utiliser dans le frontend mais aussi dans le backend, un nouveau monde de possibilités semble s'ouvrir devant vous.

Pour commencer, vous réalisez que vous n'avez pas besoin d'apprendre un autre langage pour avoir le backend de vos applications opérationnel. Ensuite, Node.js est simple à installer et fonctionne sur toutes les plateformes de développement auxquelles nous sommes habitués : Mac, Linux et Windows.

Dans cet article, je vais vous montrer comment installer Node sur Windows avec un guide étape par étape pour que vous soyez prêt à l'utiliser.

Vous serez également heureux de savoir que la gestion des packages est encore plus facile, car npm (le Node Package Manager) est inclus avec l'installation de Node.

Avec npm, vous aurez accès à un nombre presque illimité de dépendances créées par la communauté. Vous pouvez simplement les installer dans votre application pour ne pas avoir à réinventer la roue encore et encore.

Alors, installons Node sur Windows et commençons à l'utiliser un peu.

## Comment installer Node sur Windows

La première chose à faire est d'accéder au [site officiel de Node](https://nodejs.org/).

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_site.PNG)
_Page d'accueil du site de Node_

Le site est suffisamment intelligent pour détecter le système que vous utilisez, donc si vous êtes sur Windows, vous obtiendrez probablement une page comme celle ci-dessus. Au milieu de celle-ci, deux boutons vous montrent les possibilités de téléchargement les plus courantes, ainsi que les plus récentes.

Si vous êtes curieux de connaître toutes les fonctionnalités les plus récentes que Node a à offrir, choisissez le bouton de droite. Cependant, pour la plupart des gens, le site lui-même recommande d'utiliser la version Long-Term Support, ce qui vous conduit au bouton de gauche.

Au moment de la rédaction de cet article, la version LTS est la version 16.14.0.

Lorsque vous cliquez sur l'un d'eux, un fichier .msi est téléchargé sur votre ordinateur. L'étape suivante consiste à cliquer dessus et l'installation commence. L'assistant s'ouvre et la fenêtre suivante apparaît :

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_install1.PNG)
_Page initiale de l'assistant d'installation de Node_

Cliquez sur Suivant. Dans la fenêtre suivante, vous lirez (vous le lisez, n'est-ce pas ?) le CLUF de Node, acceptez ses termes et cliquez à nouveau sur Suivant. La fenêtre suivante est celle où vous sélectionnez le dossier de destination pour Node.

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_install2.PNG)

Windows recommande généralement que les programmes soient installés dans le dossier Program Files, dans un dossier qui leur est propre (dans notre cas, nous installons Node.js, donc le dossier nodejs est notre destination).

Pour simplifier, suivons les suggestions de l'assistant et utilisons `C:\Program Files\nodejs\` comme dossier de destination.

La fenêtre suivante est celle où vous pouvez personnaliser votre installation. À moins d'avoir des problèmes d'espace disque ou une idée claire de ce que vous faites, je recommande de garder les options telles quelles et de simplement appuyer à nouveau sur Suivant.

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_install3.PNG)

Une chose que je voudrais souligner sur cette fenêtre est la troisième option que vous voyez. C'est l'option qui vous permet d'avoir npm installé en même temps que Node sur votre ordinateur. Ainsi, si vous avez encore l'intention de modifier la configuration de cette page d'une manière ou d'une autre, gardez cette option telle quelle et npm sera installé pour vous à la fin du processus.

La fenêtre suivante traite de l'installation automatique des "Outils pour Modules Natifs". À moins d'être sûr d'en avoir besoin, je recommande de laisser cette case décochée et de simplement appuyer à nouveau sur Suivant.

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_install4.PNG)

Nous avons atteint la dernière fenêtre de pré-installation. Comme il est indiqué, à partir de là, vous devez simplement cliquer sur Installer pour commencer l'installation, alors faisons-le.

Remarquez le bouclier à côté du mot Installer ? Cela signifie que Windows vous demandera de confirmer si vous souhaitez vraiment poursuivre le processus d'installation dès que vous cliquez sur ce bouton. En supposant que c'est la raison pour laquelle vous lisez cet article, cliquez simplement sur Oui et laissez l'installateur faire son travail.

![Image](https://www.freecodecamp.org/portuguese/news/content/images/2022/03/node_install5.PNG)

Nous avons enfin atteint la fenêtre que nous espérions, nous indiquant que Node a été installé avec succès sur notre ordinateur Windows. Cliquez sur Terminer et vérifions si tout est en ordre.

## Comment vérifier votre installation de Node

Pour vérifier si Node (et npm) ont été correctement installés sur votre ordinateur, vous pouvez choisir d'ouvrir soit Windows Powershell soit l'Invite de commandes.

Nous allons utiliser le premier. Cliquez sur la barre de recherche à côté du bouton du menu Démarrer et tapez `powershell`. Appuyez sur Entrée et Windows Powershell s'ouvrira dans une fenêtre pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/node_install10.PNG)

Dans n'importe quel dossier (comme `C:\Users`, par exemple), vous pouvez taper `node -v` pour vérifier la version de Node que vous utilisez. Comme je l'ai mentionné ci-dessus, la dernière version au moment de la rédaction de cet article est la version 16.14.0 et c'est exactement ce que nous voyons sur Powershell ci-dessus.

En passant, vous vous demandez peut-être pourquoi nous pouvons vérifier cela dans n'importe quel dossier. L'une des options dans la configuration personnalisée (que nous avons laissée telle quelle) était d'ajouter Node au PATH. En faisant cela, nous pouvons y accéder de n'importe où tout en naviguant à travers les dossiers.

Il est également possible de vérifier la version de npm. Pour ce faire, tapez `npm -v` et appuyez sur Entrée. Dans notre cas, la dernière version est la version 8.3.1, donc nous pouvons dire que nous sommes à jour.

## Comment utiliser npm

D'accord, mais vous n'avez pas lu tout ce chemin pour finir ici après avoir installé Node et npm, n'est-ce pas ? Vous voulez voir les deux en action. Alors, faisons-le.

Pour apprendre à démarrer un projet avec Node et installer des packages avec npm, nous allons utiliser Visual Studio Code.

Nous allons créer un dossier nommé Node_Test, où nous allons mettre Node et npm au travail un peu.

Commençons simplement. À l'intérieur du dossier Node_Test, faites un clic droit à l'intérieur du dossier et cliquez sur Ouvrir avec Visual Studio Code. Cela fera ouvrir VS Code dans ce dossier vide automatiquement.

À l'intérieur de VS Code, si vous ne l'avez pas encore fait, ouvrez un nouveau terminal en appuyant sur `Ctrl+Shift+'` (guillemet simple).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/node_install11.PNG)

Cliquez sur le terminal et, sur la ligne de commande, tapez `npm init -y`. Cela démarrera un projet Node automatiquement pour nous sans que nous ayons à nous soucier de la configuration initiale (le drapeau `-y` le fera à notre place). Cela crée un fichier package.json dans le dossier Node_Test.

Ensuite, installons Express comme dépendance. Vous pouvez le trouver ainsi qu'une liste d'autres dépendances possibles de npm sur [https://www.npmjs.com/](https://www.npmjs.com/).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/node_install12.PNG)

Une autre note : chaque fois que vous ouvrez le site web de npm, en haut à gauche, vous verrez ce qui semble être une combinaison sans signification de trois mots. Si vous regardez les initiales, cependant, vous verrez qu'il s'agit d'une toute nouvelle séquence avec l'acronyme npm.

Bien, maintenant installons Express avec ce Manticore Ronronnant Nifty. Retournez sur VS Code et le terminal, tapez `npm i express` et appuyez sur Entrée. Express sera installé. Vous pouvez faire de même avec n'importe quelle autre dépendance à laquelle vous pensez.

Pour vous assurer qu'Express est installé, ouvrez package.json. Faites défiler vers le haut jusqu'à la liste des dépendances et vous verrez Express là.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/node_install13.PNG)

## Conclusion

C'est à peu près tout. Dans cet article, vous avez vu comment installer Node et npm sur Windows.

J'espère que cela vous a été utile. Pour plus de tutoriels comme celui-ci, consultez [freecodecamp.org/news](https://freecodecamp.org/news) et parcourez les sujets que vous aimeriez apprendre.

Bon codage ! 😊