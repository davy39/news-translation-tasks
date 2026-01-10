---
title: Les outils de développement du navigateur expliqués en formant pour devenir
  chef
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-21T04:11:43.000Z'
originalURL: https://freecodecamp.org/news/browser-developer-tools-explained-by-training-to-become-a-chef-edfaa82b740c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zdQasZBj8_S3hYF4CAgbHw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les outils de développement du navigateur expliqués en formant pour devenir
  chef
seo_desc: 'By Kevin Kononenko

  If you have ever visited a restaurant, this guide will help you understand how dev
  tools like Chrome Dev Tools and text editors like Sublime Text work.

  When you are building your first website with HTML and CSS, you can easily get ...'
---

Par Kevin Kononenko

Si vous êtes déjà allé dans un restaurant, ce guide vous aidera à comprendre comment fonctionnent les outils de développement comme Chrome Dev Tools et les éditeurs de texte comme Sublime Text.

Lorsque vous construisez votre premier site web avec HTML et CSS, vous pouvez facilement être submergé par toutes les nouvelles technologies nécessaires pour déployer même un site de base.

Services d'hébergement ?

Éditeurs de texte ?

[Répertoires de fichiers](https://blog.codeanalogies.com/2018/06/24/file-directories-explained-by-getting-dressed-in-the-morning/) ?

Toutes ces technologies vont bien au-delà des tutoriels que vous avez peut-être essayés sur des sites comme [freeCodeCamp](http://freecodecamp.com/) et [Codecademy](http://codecademy.com/) !

Alors, j'ai pensé qu'un rapide tutoriel sur l'utilisation des éditeurs de texte et des outils de développement éliminerait une partie confuse du processus.

En fait, tout cela ressemble étroitement à la manière dont un chef de restaurant pourrait créer de nouveaux plats à servir aux clients. Pensez au concept de recette. Une recette est un ensemble spécifique d'instructions et d'ingrédients qui produira le même repas à chaque fois. Comme vous allez le voir, le processus de développement d'une nouvelle recette est un peu comme la construction d'un site web avec HTML et CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/0*F-EL1qZ_NXoH7-Cd)

Pour comprendre ce tutoriel, vous devez simplement connaître les bases de HTML et CSS. Commençons.

#### Comparaison d'une recette et du code Front-End

Pensons à l'objectif fondamental d'être chef. Votre objectif est de traduire des recettes en délicieux plats pour les clients. Bien sûr, cela devient difficile lorsque vous devez gérer tous les facteurs en même temps : commandes entrantes, différents temps de préparation, etc. Mais oublions cela pour un moment.

Voici à quoi pourrait ressembler un système de restaurant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B0f0CXgRdEfzZUBO)

1. Un chef développe une recette qui sera utilisée chaque soir au restaurant. Elle peut être reproduite encore et encore par le personnel de cuisine, et transformée en le même repas chaque soir.
2. Le personnel de cuisine suit les instructions de la recette
3. Le produit final est le repas (qui ressemble à des pâtes et des boulettes de viande dans ce cas, quel genre de chef est-ce ?)

De même, lorsque vous construisez un site web, vous devez écrire du code qui peut être interprété par un navigateur afin que le même site web puisse être servi aux visiteurs du monde entier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5FogkHgSQE8DdXMW)

1. Vous écrivez du code en utilisant HTML, CSS et JavaScript qui produira une page web complète
2. Un navigateur interprète ce code et le transforme en une interface graphique (GUI)
3. Un visiteur du site web expérimente le site (par exemple, Google.com)

Chaque fois que vous visitez un site web particulier, cela s'appelle une "**session**". Chaque fois que vous ouvrez une page sur un nouveau **domaine** (comme Google.com ou Facebook.com), une nouvelle session commence et dure jusqu'à ce que vous quittiez le domaine. Ainsi, une personne peut visiter plusieurs pages au sein d'une session. La session est un peu comme la visite d'un restaurant.

#### Que sont les outils de développement, alors ?

Les outils de développement vous permettent d'inspecter le code sous-jacent d'un site web et de jouer avec. Si vous utilisez le navigateur Chrome, vous pouvez utiliser [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/), par exemple. Il suffit de faire un clic droit n'importe où sur la page et de sélectionner "Inspecter", la dernière option du menu.

Les outils de développement vous permettent de manipuler le style, la structure et le JavaScript de la page au sein d'une session individuelle. Cependant, ces modifications ne dureront pas si vous actualisez la page et commencez une nouvelle session.

![Image](https://cdn-media-1.freecodecamp.org/images/0*55kT4xY-Ei77yv8s)

Dans ce cas, j'ai changé la couleur de fond de l'élément **input** en bleu. Assez ennuyeux. Vous pouvez aller sur n'importe quel autre site web et faire la même chose. Bien sûr, les changements ne dureront jamais au-delà de votre session individuelle.

Cela ressemble un peu à être cette personne dans le restaurant qui prend un délicieux repas... et y met de la sauce piquante. Parce que vous êtes ce genre de personne qui adore la sauce piquante sur tout. ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*AC9vkIwvCUgtmLoY)

Votre amour pour la sauce piquante n'aura aucun impact sur la recette elle-même. Cela n'aura aucun impact sur les autres repas similaires qui seront servis ce soir-là. Et, si vous allez dans un autre restaurant, vous devrez redemander de la sauce piquante.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UhPaUxJpiboe_T27)

De la même manière, vous pouvez utiliser les outils de développement pour jouer avec le code sur un autre domaine, mais cela n'aura aucun impact au-delà de cette session particulière sur ce domaine.

#### Utilisation des outils de développement lors de la construction de votre premier site web

En tant que chef, c'est votre travail de créer des recettes qui mèneront à des plats que les clients adorent. Mais, vous **ne voulez probablement** pas découvrir cela en inventant une recette, en la donnant au personnel de cuisine, et en apprenant plus tard si les clients l'ont aimée ou non.

Au lieu de cela, vous voulez probablement tester un tas de recettes dans votre propre cuisine, puis publier celle qui semble avoir le meilleur goût.

Cela élimine toute la complexité de travailler avec un personnel de cuisine et de produire un grand volume de nourriture. Vous agissez à la fois comme le chef et le client en même temps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BglqPJucNuE0AOzL)

Remarquez que dans ce cas, vous avez le contrôle à la fois de la recette et du produit final. Donc, au lieu de pousser un repas vers les clients, vous pouvez faire une partie d'une recette, puis combiner les ingrédients de différentes manières. Ensuite, vous pouvez ajuster la recette au fur et à mesure pour refléter les combinaisons qui fonctionnent.

Lorsque vous construisez votre premier site web, vous devriez également utiliser le code original ainsi que les outils de développement pour ajuster votre site web sur votre ordinateur portable ou de bureau.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8CxZHcH6Lljbk4KV)

L'éditeur de texte (comme Sublime Text, Vim ou Emacs) est l'outil qui vous permet de changer la recette originale — les fichiers HTML, CSS et JavaScript.

Cependant, lorsque vous ajustez votre navigateur en temps réel, vous ne voudrez probablement pas changer la "recette", enregistrer le fichier et recharger la page à chaque fois. C'est épuisant !

Au lieu de cela, vous pouvez raccourcir ce cycle de feedback en apportant des modifications à l'aide des outils de développement, puis en ajustant la "recette" après avoir créé quelque chose qui vaut la peine d'être enregistré dans le navigateur lui-même.

Rappelez-vous, si vous construisez quelque chose de précieux en utilisant les outils de développement, mais que vous actualisez ensuite la page, vos modifications seront perdues. Même si le fichier est hébergé localement sur votre ordinateur.

#### Les outils de développement ne fonctionnent que pour le Front-End

Bien sûr, un restaurant a de nombreux processus en cours en même temps qui soutiennent le chef. Il y a la personne qui vous accueille à la porte, les serveurs, l'équipe de nettoyage, le barman, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vcuFkRYKEKX3vyhy)

Ce sont les personnes qui ne sont pas impliquées dans la traduction des recettes en nourriture, mais qui aident toujours à faire fonctionner les opérations du restaurant.

Cela ressemble un peu au code côté serveur, ou le **back-end**. Bien que vous écriviez du code côté serveur avec un éditeur de texte également, vous ne pouvez pas apporter de modifications via les outils de développement.

Pourquoi en est-il ainsi ? Eh bien, pouvez-vous imaginer si les clients individuels étaient autorisés à changer les règles du restaurant comme ils peuvent changer leur nourriture ? Ce serait la folie ! Les clients ne peuvent pas changer la façon dont le restaurant fonctionne, peu importe à quel point ils le souhaitent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7jJULiF0FDXjRoZ8)

Les outils de développement vous permettent uniquement d'ajuster HTML, CSS et JavaScript. Ils ne révèlent pas le code côté serveur, car cela permettrait à quiconque d'identifier toute vulnérabilité de sécurité présente dans l'application web. Mais, le code côté serveur est également écrit dans un éditeur de texte.

Si vous souhaitez en savoir plus sur la configuration du code côté serveur pour la première fois, consultez mon [guide sur le concept d'un localhost](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

#### Obtenez les derniers tutoriels

Avez-vous apprécié ce tutoriel ? Donnez-lui un "clap" ? ou inscrivez-vous ici pour obtenir le dernier tutoriel visuel sur les sujets de développement web.