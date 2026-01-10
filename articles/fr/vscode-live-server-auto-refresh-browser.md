---
title: VS Code Live Server – Comment rafraîchir automatiquement votre navigateur avec
  cette extension simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-14T18:36:28.000Z'
originalURL: https://freecodecamp.org/news/vscode-live-server-auto-refresh-browser
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9837740569d1a4ca18cd.jpg
tags:
- name: automation
  slug: automation
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: vscode
seo_title: VS Code Live Server – Comment rafraîchir automatiquement votre navigateur
  avec cette extension simple
seo_desc: 'By Cem Eygi

  Visual Studio Code is one of the most popular code editors out there. It''s free,
  it has a clean interface, and it has countless extensions which make programming
  easier and more fun.

  I''m a frontend web developer and I use VS Code while I ...'
---

Par Cem Eygi

Visual Studio Code est l'un des éditeurs de code les plus populaires. Il est gratuit, possède une interface propre et compte d'innombrables extensions qui rendent la programmation plus facile et plus amusante.

Je suis développeur web frontend et j'utilise VS Code pour travailler et sur ma chaîne YouTube. Beaucoup de gens m'ont demandé comment le navigateur se rafraîchit automatiquement pendant que je code, sans cliquer sur le bouton de rechargement. 

Eh bien, cela est possible si vous configurez une extension utile dans VS Code appelée live-server. Dans cet article, je vais expliquer en détail comment cela fonctionne et comment installer et configurer un serveur live dans votre éditeur VS Code.

## Pourquoi devrais-je utiliser l'extension live-server ?

Normalement, lorsque vous apportez une modification à votre code ou écrivez quelque chose de nouveau, vous devez rafraîchir manuellement la page pour voir les changements. 

En d'autres termes, si vous apportez 100 modifications à votre code chaque jour, vous devez rafraîchir le navigateur 100 fois.

L'extension live-server, cependant, automatise cela pour vous. Après l'avoir installée, un localhost automatisé pourra s'exécuter dans votre navigateur, que vous pourrez démarrer avec un seul bouton.

Une fois que vous aurez apporté des modifications à votre code ou écrit quelque chose de nouveau, après l'avoir enregistré, le navigateur se rafraîchira automatiquement. Vous pourrez alors voir les changements rapidement et automatiquement.

Si vous préférez, vous pouvez également regarder la vidéo tutorielle ci-dessous :

%[https://youtu.be/jdWlGQdq1Q0]

## D'abord, installez VS Code

Vous pouvez sauter cette partie si vous avez déjà installé VS Code sur votre ordinateur. Sinon, vous pouvez le télécharger depuis [son site officiel](https://code.visualstudio.com/).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1-3.png)
_Site officiel de Visual Studio Code_

Après avoir téléchargé et installé VS Code, vous verrez l'écran de bienvenue :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2-3.png)

Sur le côté gauche, vous devriez voir quelques icônes. L'une d'entre elles (sous l'icône sans bugs) est le bouton des extensions :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2-4.png)

Une fois que vous cliquez dessus, une barre de recherche apparaîtra. Tapez simplement « live server ».

![Image](https://www.freecodecamp.org/news/content/images/2020/10/3-2.png)

Vous verrez plusieurs options, vous pouvez donc choisir celle qui fonctionne pour votre système. J'utilise Live Server par Ritwick Dey, alors continuons avec celui-ci dans cet exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/4-2.png)

Cliquez sur le bouton d'installation et l'extension sera installée.

## Créez une nouvelle page HTML

Pour démarrer le serveur live, assurez-vous d'avoir au moins une page HTML créée. Pour cela, cliquez sur le bouton de fichier tout en haut, puis choisissez le bouton de nouveau fichier et tapez index.html :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/6-2.png)
_Icône de nouveau fichier avec signe plus (2ème à partir de la gauche)_

### Problèmes de configuration

Maintenant, après avoir créé une page HTML et installé l'extension, vous devriez voir une icône « Go Live » juste en dessous dans le champ bleu :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/5-2.png)

Si vous ne la voyez pas, redémarrez simplement VS Code. Ensuite, tout devrait être en ordre.

Cliquez sur le bouton « Go Live » et le localhost (attribué à un numéro de port) devrait démarrer sur votre navigateur par défaut. Vous pouvez démarrer et arrêter votre serveur live à tout moment en cliquant sur le même bouton.

Si vous avez atteint cette étape, félicitations ! :) Maintenant, vous pouvez travailler avec le live-server. Sinon, si vous rencontrez toujours des problèmes, consultez [cet article pour plus d'informations](https://www.freecodecamp.org/news/visual-studio-code-live-server-not-working/).

## Conclusion

J'espère que cet article vous aide à installer et configurer l'extension live server dans VS Code. Si vous souhaitez en apprendre davantage sur le développement web, n'hésitez pas à visiter ma [chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q).

Merci d'avoir lu !