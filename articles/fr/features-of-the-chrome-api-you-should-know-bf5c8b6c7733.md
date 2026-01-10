---
title: Fonctionnalités de l'API Chrome que vous devriez connaître
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-12-28T17:27:17.000Z'
originalURL: https://freecodecamp.org/news/features-of-the-chrome-api-you-should-know-bf5c8b6c7733
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Got1zk0gpNuHC0V1
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
seo_title: Fonctionnalités de l'API Chrome que vous devriez connaître
seo_desc: So you think you know your way around building a Chrome extension? Well,
  that’s all fine and dandy, but have you heard about context menus? Messaging between
  scripts? Adding a badge to your extension’s icon? If all this sounds fascinating,
  you’re in ...
---

Vous pensez maîtriser la création d'une extension Chrome ? C'est très bien, mais avez-vous entendu parler des menus contextuels ? Des messages entre scripts ? De l'ajout d'un badge à l'icône de votre extension ? Si tout cela vous semble fascinant, vous avez de la chance. Nous allons passer en revue certaines fonctionnalités intéressantes que l'API Chrome nous offre.

Si vous êtes intéressé par la lecture sur la façon de créer une extension Chrome, vous pouvez lire mon article précédent [ici](https://medium.freecodecamp.org/how-to-implement-a-chrome-extension-3802d63b5376). Si vous voulez savoir comment en publier une, vous pouvez tout lire à ce sujet [ici](https://medium.freecodecamp.org/chrome-extension-how-to-publish-dd8400a3d53)

### [Menu contextuel](https://developer.chrome.com/extensions/contextMenus)

Pour faire simple, le menu contextuel est le menu qui apparaît lorsque vous faites un clic droit n'importe où dans le navigateur. Vous pouvez ajouter votre extension Chrome à ce menu avec quelques étapes simples :

1. Ajoutez **context-menus** à la clé **permissions** dans le manifest
2. Ajoutez une icône de 16x16 (car elle sera utilisée dans le menu contextuel)
3. Ajoutez le code suivant à votre script d'arrière-plan :

### [Stockage](https://developer.chrome.com/extensions/storage)

Similaire à [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API#localStorage), l'API Chrome permet d'enregistrer des données sous forme d'objets, qui persistent même lorsque le navigateur est fermé et rouvert. Voici les étapes nécessaires pour permettre l'utilisation du stockage dans votre extension :

1. Ajoutez **storage** à la clé **permissions** dans le manifest
2. Pour mettre des données dans le stockage, vous utilisez :

3. Pour récupérer des données du stockage, vous utilisez :

> ⚠️ Ne mettez PAS de données sensibles de l'utilisateur dans le stockage, car elles ne sont pas cryptées

### [Messagerie](https://developer.chrome.com/extensions/messaging#simple)

Chrome possède une autre fonctionnalité ingénieuse qui vous permet de transmettre des messages entre scripts. Par exemple, dans votre extension, vous avez votre fichier popup.js qui gère les éléments liés à la fenêtre contextuelle et vous avez un script d'arrière-plan. Si vous souhaitez que ces deux scripts communiquent entre eux, vous pouvez utiliser les méthodes suivantes :

**SendMessage**

**Écouter les messages entrants**

### Badges

Vous les connaissez, vous les aimez, et vous pouvez les ajouter à l'icône de votre extension. Assurez-vous d'être conscient que, en raison de sa petite taille, le texte que vous souhaitez afficher est limité à **_quatre caractères_**.

Pour définir la couleur de fond du badge, vous utilisez :

Pour définir le texte du badge, vous utilisez :

Dans les deux méthodes, le rappel est un paramètre facultatif que vous pouvez utiliser après que la méthode ait terminé son action.

Avez-vous d'autres API Chrome dont vous souhaitez savoir plus ? Vous voulez poser une question ? N'hésitez pas à demander.

*Si vous avez aimé cet article, applaudissez pour que les autres puissent en profiter aussi ! 👏*