---
title: 5 raccourcis React qui amélioreront instantanément votre productivité
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-19T14:55:08.000Z'
originalURL: https://freecodecamp.org/news/react-shortcuts-that-will-instantly-boost-your-productivity
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/5-react-shortcuts.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
seo_title: 5 raccourcis React qui amélioreront instantanément votre productivité
seo_desc: 'To become a better React developer, you don''t always have to learn an
  entirely new, challenging skill. You can instantly improve your React code in a
  few minutes by using the powerful features your development tools make available.

  Some of the bigges...'
---

Pour devenir un meilleur développeur React, vous n'avez pas toujours besoin d'apprendre une nouvelle compétence difficile. Vous pouvez améliorer instantanément votre code React en quelques minutes en utilisant les fonctionnalités puissantes que vos outils de développement mettent à votre disposition.

**Certaines des plus grandes améliorations dans votre travail en tant que développeur React prennent le moins de temps à apprendre.** Faites un effort aujourd'hui pour appliquer ces conseils et je vous garantis que vous économiserez de nombreuses heures de travail fastidieux dans votre codage quotidien, et vous apprécierez beaucoup plus le codage avec React.

Voici cinq raccourcis que vous pouvez utiliser dès maintenant pour devenir un codeur React plus productif.

> Ces conseils montrent principalement comment tirer le meilleur parti de votre éditeur de code. L'éditeur de code que j'utilise est Visual Studio Code, qui est très populaire parmi les développeurs React. Si vous souhaitez utiliser VSCode, vous pouvez le télécharger gratuitement sur [code.visualstudio.com](https://code.visualstudio.com). Notez que ces fonctionnalités sont disponibles dans pratiquement tous les éditeurs de code.

## 1. Fatigué d'écrire des balises de fermeture pour chaque élément JSX ? Utilisez Emmet.

En tant que développeur React, vous écrivez beaucoup d'éléments JSX, dont la plupart consistent en une balise d'ouverture et une balise de fermeture.

Si vous n'avez pas configuré Emmet avec React, vous devez écrire ces deux balises à la main pour chaque élément. Une approche bien meilleure consiste à utiliser un outil appelé **Emmet**, qui crée automatiquement la balise de fermeture chaque fois que vous créez la balise d'ouverture.

**Pour configurer Emmet avec React dans VSCode :**

1. Allez dans **Code** (en haut de votre écran), puis **Préférences**, puis **Paramètres** dans VSCode
2. Dans les options à gauche, sélectionnez **Extensions**, puis **Emmet**
3. Faites défiler jusqu'à la section **Include Languages**, ajoutez dans le champ de l'élément, _javascript_ et dans le champ de la valeur, _javascriptreact_, puis cliquez sur **Ajouter un élément**

_Et juste comme ça, Emmet a accéléré votre codage de 100% :_

![Démonstration Emmet](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/emmet.gif)

## 2. Fatigué de formater votre code à la main ? Utilisez Prettier.

Pouvez-vous compter le nombre de fois où votre code n'a pas été aligné correctement, alors vous avez essayé d'ajuster l'espacement vous-même ? Je ne veux même pas penser au temps que j'ai passé à formater mon propre code !

_Si vous essayez toujours de formater votre code manuellement, vous avez besoin de **Prettier**._

Prettier porte bien son nom : il transforme votre code mal aligné en une version beaucoup plus joli et formatée.

Prettier est disponible en tant que devDependency pour des projets JavaScript individuels ou vous pouvez l'utiliser dans tous vos projets avec l'extension Prettier VSCode. L'avantage d'utiliser l'extension VSCode est que vous pouvez formater automatiquement votre code JavaScript chaque fois que vous enregistrez.

**Voici comment configurer Prettier pour l'utiliser dans tous vos projets dans VSCode :**

1. Allez dans **Code**, puis **Préférences**, puis **Extensions**
2. Recherchez _prettier_ dans la barre de recherche et appuyez sur Entrée (il devrait être le premier à apparaître)
3. Sélectionnez l'extension, puis cliquez sur **Installer** (et éventuellement **Recharger** pour appliquer l'extension)
4. Allez dans **Code**, puis **Préférences**, puis **Paramètres**
5. Recherchez **Format on Save** et cochez la case à côté de l'option de formatage à l'enregistrement

Maintenant, tout le code que vous écrivez sera parfaitement formaté, chaque fois que vous enregistrez :

![Prettier pour React Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/prettier.gif)

## 3. Écrivez-vous chaque composant que vous créez ? Utilisez des extraits React.

Créer de nombreuses choses dans React et dans les projets JavaScript en général nécessite beaucoup de code boilerplate. Chaque fois que vous écrivez un composant, vous devez taper chaque partie de celui-ci – importer React, créer une fonction et l'exporter depuis votre fichier.

_En avez-vous assez de devoir faire cela ?_ Nous en avons tous assez. C'est pourquoi les extraits pour React existent.

Pour éviter tout le travail supplémentaire d'écrire le même code encore et encore, utilisez des **extraits React**. Les extraits vous permettent d'utiliser des raccourcis clavier pour écrire instantanément chaque partie de votre code React au lieu de devoir tout taper manuellement.

Par exemple, au lieu d'écrire `import React from 'react'`, vous pouvez simplement écrire `imr` et appuyer sur la touche Tab pour créer instantanément la même chose. Les extraits sont un gain de temps énorme.

**Voici comment utiliser les extraits React dans VSCode :**

1. Allez dans **Code**, puis **Paramètres**, puis **Extensions**
2. Recherchez _React Snippets_. Il existe de nombreuses bonnes extensions d'extraits parmi lesquelles choisir.
3. Lorsque vous avez une extension d'extraits installée, jetez un coup d'œil aux raccourcis disponibles et notez les meilleurs.
4. Lorsque vous tapez un raccourci, attendez que la suggestion apparaisse dans votre éditeur de code, puis appuyez sur **Tab** (vous pouvez parcourir la liste avec les flèches si vous voulez une autre option)

Vous serez surpris de la rapidité avec laquelle vous pouvez créer vos composants maintenant :

![Extraits React pour VSCode Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/react-snippets.gif)

## 4. Importez-vous tous vos composants manuellement ? Utilisez l'importation automatique à la place.

L'une des choses les plus fastidieuses à faire dans la création d'applications React est d'importer des packages et des composants depuis d'autres fichiers.

C'est très répétitif et peut prendre une quantité significative d'énergie pour importer chaque chose manuellement (sans compter les corrections lorsque vous faites une faute de frappe).

Au lieu de devoir vous souvenir, trouver et importer manuellement vos composants et packages, laissez votre éditeur de code le faire pour vous. Vous pouvez **importer automatiquement** ce que vous voulez en sélectionnant ce que vous souhaitez importer en appuyant sur la touche Tab.

**Voici comment importer automatiquement des packages et des composants dans VSCode :**

1. Allez dans **Code**, puis **Préférences**, puis **Paramètres**
2. Recherchez _auto import_ et assurez-vous que la case **Enable Auto Import** est cochée
3. Retournez dans votre projet, écrivez le nom de ce que vous voulez importer, parcourez les options suggérées par l'éditeur et appuyez sur **Tab** pour créer instantanément une instruction d'importation pour cela.

Lorsque vous utilisez l'importation automatique, cela facilite le travail avec des projets de toute taille, car vous ne passez plus la moitié de votre temps à écrire des instructions d'importation.

![Importation automatique pour React Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/auto-import.gif)

## 5. Supprimez-vous manuellement vos imports inutilisés ? Utilisez le raccourci organiser les imports.

En plus d'avoir Prettier pour tout le code que nous écrivons, VSCode nous donne un raccourci appelé **organiser les imports** qui fait exactement cela. En fait, il fait deux choses :

1. Il organise alphabétiquement nos instructions d'importation
2. Il supprime les instructions d'importation inutilisées (corrige instantanément les avertissements de linting concernant les imports inutilisés)

Et surtout, ce raccourci ne nécessite aucune configuration. **Voici comment l'utiliser :**

1. Allez dans **Affichage**, puis **Palette de commandes**.
2. Recherchez _organize imports_ et sélectionnez-le.
3. Vos imports devraient maintenant être organisés et tous les imports inutilisés supprimés.

Notez que vous pouvez également utiliser le raccourci clavier `command/control + shift + o`.

![Démonstration organiser les imports](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/organize-imports.gif)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*