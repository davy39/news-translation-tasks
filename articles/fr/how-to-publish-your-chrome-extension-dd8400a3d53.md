---
title: Comment publier votre extension Chrome
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-11-30T18:08:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-your-chrome-extension-dd8400a3d53
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6SBGxnrpx8yGjo5S
tags:
- name: chrome extension
  slug: chrome-extension
- name: coding
  slug: coding
- name: development
  slug: development
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment publier votre extension Chrome
seo_desc: 'In my previous article I wrote, I talked about the building blocks of a
  Chrome extension. Now, I would like to focus on the other part of building a Chrome
  extension: what to do when you are done building it. The process in itself is not
  long nor har...'
---

Dans mon [article](https://medium.freecodecamp.org/how-to-implement-a-chrome-extension-3802d63b5376) précédent, j'ai parlé des éléments constitutifs d'une extension Chrome. Maintenant, je souhaite me concentrer sur l'autre partie de la création d'une extension Chrome : **que faire lorsque vous avez terminé de la construire**. Le processus en lui-même n'est ni long ni difficile, mais il y a certaines choses auxquelles vous devez prêter attention.

Chaque extension Chrome est publiée sur le [Chrome Web Store](https://chrome.google.com/webstore/category/extensions). Considérez cela comme l'équivalent du Play Store de Google ou de l'App Store d'Apple, mais uniquement pour les extensions et thèmes Chrome.

### Étapes

Si vous n'en avez pas déjà créé un, vous devrez créer un compte Développeur. Dans celui-ci, vous aurez un Tableau de bord Développeur.

> Comme je l'ai mentionné dans l'article précédent, il y a des frais d'inscription uniques de 5 $ si vous souhaitez pouvoir publier des extensions Chrome. Cela vous donnera la possibilité de publier jusqu'à 20 extensions.

Une fois que vous êtes le fier propriétaire d'un compte Développeur, l'étape suivante consiste à télécharger votre extension Chrome sur votre compte. Pour ce faire, créez un fichier ZIP avec tous les fichiers associés à votre extension. **Le seul fichier que Google vous demande de télécharger est le fichier manifest.json**. Mais vous voudrez également ajouter les fichiers JavaScript que vous avez.

Après cela, l'étape suivante consiste à publier notre extension. Connectez-vous à votre compte développeur et accédez à votre Tableau de bord Développeur.

![Image](https://cdn-media-1.freecodecamp.org/images/u6LZm6jafoX5k2lVN-j1m64kWSJuCm658oBK)

Là, vous verrez un bouton **Ajouter un nouvel élément**.

![Image](https://cdn-media-1.freecodecamp.org/images/Y5aNZVWVXR4nIZFiLm8yblYJVnv5dGVBEZ95)
_Cliquez ici_

> **⚠️ Sachez que une fois que vous avez ajouté une extension à votre Tableau de bord Développeur, vous ne pouvez pas la supprimer. Tant qu'elle n'est pas publiée, elle ne comptera pas dans votre limite d'extensions.**

Cela vous dirigera vers une page où vous pourrez télécharger le fichier ZIP que nous avons créé précédemment :

![Image](https://cdn-media-1.freecodecamp.org/images/0kFfxuPAmDDtuVIZhzbxq29DXK9dUjvVmUbY)
_Cliquez sur choisir le fichier et appuyez sur télécharger_

En supposant que tout s'est bien passé, vous serez dirigé vers la page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/w6sFu56M9LcBHekEYrid8oSWKC3ZN6XyfE8o)
_Ici, vous pouvez fournir une description de votre extension_

> Si vous prévoyez d'apporter des modifications à votre extension, vous pouvez utiliser le bouton Télécharger le package mis à jour pour retélécharger votre fichier ZIP.

Sur cette page, vous pouvez ajouter une icône qui sera affichée sur la barre d'outils :

![Image](https://cdn-media-1.freecodecamp.org/images/TypgvFz8T8rYSBC5--KHPZm-7pzJSJnJn9hQ)

Ajoutez des captures d'écran de votre extension (elles seront utilisées lorsqu'un utilisateur regardera votre extension) :

![Image](https://cdn-media-1.freecodecamp.org/images/33NG7giJ5X3U2Jkzc-1tm1EGkbdJBEJl47Y1)

Et diverses autres fonctionnalités comme le choix d'une catégorie pour l'extension (par exemple, Divertissement), le choix des régions où votre extension sera disponible, le prix de votre extension, et d'autres catégories que je vous suggère de consulter.

Lorsque vous avez terminé de peaufiner les détails de votre extension, vous arriverez à la fin de la page et verrez les boutons suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/-T9LN7NxeYyk8gqb4nuFe2p0J-P9zH9TvkKq)

Les deux boutons de gauche vous permettent d'enregistrer le travail que vous avez effectué jusqu'à présent pour configurer votre extension (ou de l'annuler), et les deux boutons de droite sont pour lorsque vous êtes prêt à publier. Pour voir comment tout ce que vous avez configuré apparaîtra sur le Chrome Web Store, appuyez sur le bouton **Prévisualiser les modifications**. Lorsque vous êtes satisfait de ce que vous avez, cliquez sur **Publier les modifications**.

![Image](https://cdn-media-1.freecodecamp.org/images/i0xLibubdSwSbK0BDVOsPv3WTdfKFWSoGhrN)
_Photo par [Unsplash](https://unsplash.com/@adspedia?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Val Vesa</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Félicitations ! Vous venez de publier votre première extension Chrome !

Dans votre Tableau de bord Développeur, vous verrez maintenant ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/oBMLsvN4hlBDyUy0ZGwfVKOHFrJwi6Aa3Qso)

En cliquant sur le lien _Statistiques_, vous obtiendrez des analyses concernant votre extension (nombre d'impressions, d'installations et d'utilisateurs actifs). J'ai hâte de voir vos extensions Chrome publiées.