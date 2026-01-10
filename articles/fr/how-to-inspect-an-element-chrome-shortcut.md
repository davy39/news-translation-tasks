---
title: Comment inspecter un élément – Raccourci Chrome
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-15T01:40:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-inspect-an-element-chrome-shortcut
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/inspect-element.png
tags:
- name: Google Chrome
  slug: chrome
- name: Developer Tools
  slug: developer-tools
- name: Web Development
  slug: web-development
seo_title: Comment inspecter un élément – Raccourci Chrome
seo_desc: 'The Inspect Element feature of the Google Chrome browser is a powerful
  yet easy-to-use tool.

  It’s an important part of Chrome Developer Tools that you can use to check the source
  code of any website.

  But it doesn’t end there. You can take things furt...'
---

La fonction Inspecter l'élément du navigateur Google Chrome est un outil puissant et facile à utiliser.

C'est une partie importante des Chrome Developer Tools que vous pouvez utiliser pour vérifier le code source de n'importe quel site web.

Mais ce n'est pas tout. Vous pouvez aller plus loin en modifiant les éléments et les styles qui composent le site web – c'est-à-dire le code HTML, CSS et JavaScript du site. C'est pourquoi de nombreux développeurs utilisent l'outil Inspecter pour le débogage.

Si vous êtes débutant en développement web, l'outil Inspecter est une fonctionnalité utile dont vous pouvez tirer parti pour apprendre comment les sites web sont construits, les polices, icônes et plugins utilisés, et même qui a créé le site.

La bonne nouvelle est que vous n'avez pas besoin d'être le développeur du site pour utiliser cet outil puissant, car il est également disponible pour les utilisateurs. Vous n'avez même pas besoin d'être développeur pour l'utiliser.

Dans cet article, vous apprendrez comment ouvrir les Chrome Developer Tools pour accéder à la fonction Inspecter, et comment inspecter des éléments spécifiques sur un site web. Je vous montrerai également comment manipuler les éléments d'un site en modifiant les textes et les styles.

J'utiliserai freeCodeCamp.org pour vous montrer comment fonctionne l'outil Inspecter.

## Comment ouvrir les Chrome Developer Tools
Pour ouvrir les Chrome Developer Tools, cliquez sur les trois points verticaux en haut à droite de votre navigateur :
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/04/ss1-3.png)

Puis survolez « Plus d'outils » et sélectionnez « Outils de développement » :
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/04/ss2-5.png)

Vous aurez alors accès aux onglets des outils de développement tels que Elements (le HTML et CSS qui composent le site), Console avec laquelle vous pouvez exécuter du JavaScript, Sources, et bien plus encore.

Vous pouvez faire glisser ces onglets et les placer où vous le souhaitez :
![drag](https://www.freecodecamp.org/news/content/images/2022/04/drag.gif)

## Comment ouvrir l'outil Inspecter un élément dans Chrome avec le clavier ?
Vous pouvez ouvrir l'outil Inspecter un élément sur Linux en appuyant sur `CTRL` + `SHIFT` + `C` ou `F12` sur Windows.

Si vous êtes sur Mac, appuyez sur `Command` + `SHIFT` + `C`.

## Comment inspecter des éléments spécifiques sur un site web
Pour inspecter n'importe quel élément que vous voyez sur un site web, qu'il s'agisse de texte, d'un bouton, d'une vidéo ou d'une image, faites un clic droit sur l'élément et cliquez sur « Inspecter ».

Dans ce cas, je vais faire un clic droit sur le texte « Learn to code – for free » de la page d'accueil de freeCodeCamp.org.
![ss3-3](https://www.freecodecamp.org/news/content/images/2022/04/ss3-3.png)

Le code source s'ouvrira et l'élément sera mis en surbrillance pour vous, comme ceci :
![ss4-2](https://www.freecodecamp.org/news/content/images/2022/04/ss4-2.png)

Vous pouvez voir que le texte est un élément `h1`.

## Comment manipuler les éléments d'un site web avec l'outil Inspecter
Vous pouvez modifier le contenu textuel d'un site web avec l'outil Inspecter.

Par exemple, je vais changer le texte « Build projects » sur la page d'accueil de freeCodeCamp.org en « Build real-world projects ».

Pour ce faire, faites un clic droit sur l'élément que vous souhaitez modifier et cliquez sur « Inspecter ». Dans ce cas, il s'agit du texte « Build projects » :
![ss5-2](https://www.freecodecamp.org/news/content/images/2022/04/ss5-2.png)

Double-cliquez sur le texte « Build projects » :
![ss6-2](https://www.freecodecamp.org/news/content/images/2022/04/ss6-2.png)

Tapez « Build real-world projects » et appuyez sur `ENTRÉE` :
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/04/ss7-1.png)

![ss8-1](https://www.freecodecamp.org/news/content/images/2022/04/ss8-1.png)
Vous pouvez voir que le texte a été changé en « Build real-world projects ».

## Comment changer les styles avec l'outil Inspecter
Changeons l'arrière-plan du bouton « Get started (it's free) » en ma couleur préférée – #2ecc71.

Faites un clic droit sur le bouton et sélectionnez « Inspecter » :
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/04/ss9-1.png)

Double-cliquez sur la valeur de la propriété « background-image » à droite, c'est-à-dire `linear-gradient(#fecc4c,#ffac33)`.

Changez les couleurs en `#2ecc71,#2ecc72` et appuyez sur `ENTRÉE` :
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/04/ss10-1.png)
Vous pouvez voir que l'arrière-plan du bouton a changé.

Nous avons maintenant apporté 2 modifications à la page d'accueil de freeCodeCamp.org – nous avons changé le texte « Build projects » en « Build real-world projects » et nous avons changé l'arrière-plan du bouton « Get Started (it's free) » :
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/04/ss11-1.png)

## Les modifications que vous apportez avec l'outil Inspecter sont-elles permanentes ?
Non. Toute modification que vous apportez avec l'outil Inspecter n'est pas permanente. Une fois que vous rechargez la page, les modifications disparaissent.

C'est parce que le site web a été déployé sur un serveur. Donc, lorsque vous faites une nouvelle requête à ce serveur en rechargeant la page, le contenu du serveur est chargé par votre navigateur.

Ne vous inquiétez donc pas - jouer avec l'outil Inspecter de cette manière ne changera pas un site web de manière permanente. Cela vous aide simplement à en apprendre davantage et à pratiquer votre codage :)

## Conclusion
Cet article vous a montré comment accéder aux outils de développement de Google Chrome, comment utiliser sa fonction Inspecter pour voir le code source d'un site web, et comment modifier les éléments et les styles d'un site web avec celle-ci.

Si vous venez de commencer à apprendre à coder en HTML, CSS et JavaScript, la fonction Inspecter des outils de développement Chrome est un outil puissant que vous pouvez utiliser pour voir le code source de n'importe quel site web afin d'apprendre comment ils sont construits.

Merci d'avoir lu.