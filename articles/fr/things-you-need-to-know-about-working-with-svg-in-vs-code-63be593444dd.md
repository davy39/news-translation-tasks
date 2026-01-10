---
title: Ce que vous devez savoir sur le travail avec SVG dans VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-19T15:42:22.000Z'
originalURL: https://freecodecamp.org/news/things-you-need-to-know-about-working-with-svg-in-vs-code-63be593444dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LkyIv0Kk298yNUu2nHhSgg.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: SVG
  slug: svg
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Ce que vous devez savoir sur le travail avec SVG dans VS Code
seo_desc: 'By Burke Holland

  Check out this VS Code release highlights video from Brian Clark. Towards the end,
  he shows how you can now zoom in on image previews in VS Code.

  https://youtu.be/MWz8y1D3PMQ

  I thought that was an interesting feature. I mean, let’s f...'
---

Par Burke Holland

Consultez cette [vidéo des points forts de la version de VS Code](https://code.visualstudio.com/updates/v1_20?WT.mc_id=vscoderelease-medium-buhollan) de [Brian Clark](https://twitter.com/_clarkio). Vers la fin, il montre comment vous pouvez maintenant zoomer sur les aperçus d'images dans VS Code.

%[https://youtu.be/MWz8y1D3PMQ]

J'ai trouvé cette fonctionnalité intéressante. Je veux dire, soyons réalistes — il n'y a que deux types de personnes dans le monde : celles qui aiment zoomer sur les images et celles qui ne veulent pas l'admettre. J'ai donc ouvert un projet pour l'essayer et, effectivement, cela fonctionne comme annoncé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cClUCHBbOIxPq5X5vHOPEg.png)

Ma prochaine pensée a été de voir si cela fonctionnait avec les images SVG. Parce que j'aime zoomer sur les SVG et les regarder ne pas se dégrader. À ce stade de ma vie, c'est une activité agréable et épanouissante.

Il s'avère que VS Code ne fournit pas d'aperçu visuel pour les fichiers SVG depuis l'éditeur. Ce qui est logique. SVG est du balisage et VS Code traite les fichiers SVG comme du XML, qui n'est que du texte. Vous auriez besoin de [XSLT](https://en.wikipedia.org/wiki/XSLT) pour le rendre en quelque chose que vous pourriez _voir_. Je viens de déclencher un tas de réactions, et pour cela, je m'excuse.

Voici une excellente blague sur XML pour apaiser votre anxiété :

> « XML est comme la violence : si cela ne fonctionne pas, c'est que vous n'en utilisez pas assez. »

> - Inconnu

Cela m'a fait me demander, si VS Code traite SVG comme XML, quelles extensions sont disponibles pour m'aider à travailler avec SVG dans VS Code ? Il s'avère qu'il y en a plusieurs, et certaines fonctionnent mieux que d'autres. Voici quelques-unes de mes extensions préférées pour travailler avec SVG dans VS Code.

### SVG

La première extension s'appelle simplement [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg&WT.mc_id=vscoderelease-medium-buhollan).

C'est exact. Cette personne a été la première à s'y mettre et a obtenu le nom convoité SVG rien que pour elle. Comme la personne qui a enregistré le nom Twitter « Burke ». Mais qu'est-ce que c'est que ça, Sam ! Tu n'as pas tweeté depuis... TU N'AS JAMAIS TWEETÉ !

![Image](https://cdn-media-1.freecodecamp.org/images/1*le6FD4mNmlHMu7jTMlb2kA.png)
_Sam, si tu lis ceci — tweete-moi et parlons. Sérieusement. Tu ne veux même pas de ce compte !_

Comme vous pouvez le voir dans ce GIF, Visual Studio Code a un support limité pour SVG dès la sortie de la boîte, car nous savons qu'il le traite comme du XML. Il sait comment mettre en évidence le balisage de manière appropriée, mais c'est à peu près tout. Remarquez qu'il n'a littéralement aucune suggestion pour moi ici lorsque j'essaie de créer ce rectangle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XXkYkF9VkrjPjhopsqIw_Q.gif)

La principale chose que fait l'extension « SVG » est d'ajouter la prise en charge de la langue pour SVG à Visual Studio Code. Ainsi, lorsque je commence à taper `rect`, il me donne des options pour les éléments que je peux vouloir sélectionner et une description de ce qu'ils sont.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_782ezwZaplm7oTTT6TAQ.png)

Une fois qu'il a l'élément, il connaît maintenant tous les attributs possibles également.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n2coQIEQfmPGGGw31yWhGg.png)

Et il connaît même les valeurs pour certains de ces attributs s'ils sont des énumérations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NCML04UHivsnY5J0NhalWw.png)

#### Aperçu

Cette extension fournit également une fonction « Aperçu » qui montre un aperçu côte à côte avec le balisage et l'image rendue. Cela est disponible depuis la Palette de Commandes (Ctrl/Cmd + Shift + P).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Y0488W57gQZhmTtaYcmOw.png)

Le côté cool de cela est que l'aperçu se met à jour en direct au fur et à mesure que vous tapez votre SVG. Cela fait un bac à sable assez sympa pour construire des images SVG à la main si c'est votre truc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-YsmT0Fp2pfuTjjrAVZumA.gif)

#### Minifier

Cette extension inclut également une commande de minification qui minifiera votre SVG en utilisant SVGO. Prenez cette belle image d'une colline créée avec Sketch. Oui, je l'ai faite tout seul.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U2XGkBcryp-WNyzjbemn0g.png)

Cette image est déjà assez petite. Elle fait environ 9 ko sur le disque. L'extension SVG fournit une commande « Minifier » dans la Palette de Commandes (Ctrl/Cmd + Shift + P). En utilisant cette commande, la taille de l'image est réduite à 5 ko. C'est presque la moitié. Plutôt impressionnant.

Si nous utilisons les différentiels Git intégrés dans VS Code, nous pouvons voir une partie de ce que SVGO fait. Il supprime des choses dont nous n'avons pas besoin comme « id » ou un paramètre de 0 où la valeur par défaut est déjà 0. Il a également converti mon `rect` en `path`. Je n'ai aucune idée pourquoi, mais c'est super intéressant ! Peu importe, SVGO. Je te fais confiance. Fais ton truc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2FIKY-LKJ4yF0DfFteHwdQ.png)

C'est la plupart de ce que fait SVG pour VS Code. Mais il y a une autre extension SVG qui est également pertinente ici — **SVG Viewer**.

### SVG Viewer

[**SVG Viewer - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan)
[_Extension pour Visual Studio Code - SVG Viewer pour Visual Studio Code._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan)

[SVG Viewer](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan) fournit le même aperçu d'image côte à côte que l'extension SVG. Cependant, celle-ci a deux avantages principaux. Premièrement, vous pouvez ouvrir automatiquement l'aperçu chaque fois que vous cliquez sur un fichier `svg` en ajoutant la ligne suivante à votre fichier de préférences utilisateur.

```
"svgviewer.enableautopreview": true,
```

ET, il réduit l'image pour qu'elle s'adapte à la fenêtre. Je ne sais pas encore si j'aime cela, mais je pense que oui. Je pense que je préfère cela à une image géante dont je ne peux pas voir l'intégralité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhmcEToLx4stYr0P4tDtTA.png)

#### Convertir en PNG

Cette extension ajoute également une commande de conversion, afin que vous puissiez convertir en ligne votre SVG en PNG. Prenez cette image de camion. Je l'ai exportée en SVG, mais ce n'est qu'un URI de données enveloppé dans une balise svg. Cela n'a aucun sens. Je pourrais aussi bien la ramener à une image statique. Avec cette extension, je n'ai pas besoin de retourner à Sketch pour le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A07GtiA0XJ4holgAzKYG7A.gif)

Cette extension vous permet également de copier le schéma d'URI de données de n'importe quel SVG. Je suppose que c'est bien, mais ce n'est pas quelque chose que je fais jamais. Je suis sûr que j'en aurai besoin maintenant que je l'ai dit.

La dernière extension à noter est [SVG Editor](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan).

### SVG Editor

[**SVG Editor - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan)
[_Extension pour Visual Studio Code - Éditeur SVG visuel et littéral pour VSCode._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan)

L'extension [SVG Editor](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan) est super agressive. Elle tente de créer une surface d'édition SVG complète à l'intérieur de VS Code, avec des outils de dessin et tout le toutim.

Il est important de noter que cette extension ne fonctionne pas du tout pour moi. Elle est là, mais elle ne fait rien, autant que je puisse en juger. Ou peut-être que je me trompe. Il y a une forte probabilité de cela. Mon approche de test complète consistait à « cliquer un peu partout et voir ce qui se passe ». Rien ne s'est jamais passé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cvxmnb8Zp_w98wK5Vc-BEA.gif)

Oui — cela ne fonctionne pas. Mais un coup de chapeau pour avoir tenté de construire un éditeur graphique dans Visual Studio Code. Ce n'est pas une tâche facile, et le fait que quelqu'un ait même tenté de le faire est très impressionnant pour moi.

### Profitez de votre SVG

Avec des extensions, VS Code a un support assez solide pour SVG. Les deux grandes choses pour moi sont la complétion de code et l'aperçu. Bien que je doive noter que vous ne pouvez pas zoomer sur aucun des aperçus, donc je ne peux toujours pas satisfaire mon étrange envie de regarder les graphiques vectoriels s'adapter à l'échelle.

Vous pouvez obtenir [la dernière version de VS Code aujourd'hui](https://code.visualstudio.com/?WT.mc_id=vscoderelease-medium-buhollan) et installer ces extensions SVG à votre guise.