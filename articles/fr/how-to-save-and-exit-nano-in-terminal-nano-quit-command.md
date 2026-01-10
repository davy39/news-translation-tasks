---
title: Comment sauvegarder et quitter Nano dans le terminal – Commande pour quitter
  Nano
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-26T16:57:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-and-exit-nano-in-terminal-nano-quit-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/nano.png
tags:
- name: editor
  slug: editor
- name: Linux
  slug: linux
- name: nano
  slug: nano
seo_title: Comment sauvegarder et quitter Nano dans le terminal – Commande pour quitter
  Nano
seo_desc: "Nano is a command line-based code editor known for its simplicity compared\
  \ to other editors like Vim and Emacs.\nBut if you are new to Nano, performing basic\
  \ operations like creating files, saving the file, and exiting the editor might\
  \ be confusing. \n..."
---

Nano est un éditeur de code basé sur la ligne de commande, connu pour sa simplicité par rapport à d'autres éditeurs comme Vim et Emacs.

Mais si vous êtes nouveau dans Nano, effectuer des opérations de base comme créer des fichiers, sauvegarder le fichier et quitter l'éditeur peut être déroutant.

Alors, dans cet article, je veux vous montrer comment sauvegarder votre code dans Nano et le quitter également.

J'utiliserai le sous-système Windows pour Linux (WSL) dans cet article. Mais ce n'est pas grave si vous êtes sous Linux lui-même. Les commandes sont les mêmes.

## Ce que nous allons couvrir
- [Comment sauvegarder un fichier dans Nano](#heading-comment-sauvegarder-un-fichier-dans-nano)
- [Comment quitter Nano](#heading-comment-quitter-nano)
- [Conclusion](#heading-conclusion)


## Comment sauvegarder un fichier dans Nano
**Étape 1** : Ouvrez WSL, tapez « nano » et appuyez sur `ENTRÉE` pour accéder à l'éditeur de code Nano
![ss1-4](https://www.freecodecamp.org/news/content/images/2022/07/ss1-4.png)

**Étape 2** : Écrivez votre code dans n'importe quel langage. Dans la capture d'écran ci-dessous, j'ai écrit du PHP.
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/07/ss2-5.png)

**NB** : Si vous n'obtenez pas de coloration syntaxique, activez-la en appuyant sur `ALT` + `4`. Si vous n'obtenez toujours pas de coloration syntaxique, vous devez sauvegarder le fichier.

**Étape 3** : Appuyez sur `CTRL` + `O` pour sauvegarder le fichier, tapez le nom du fichier et appuyez sur `ENTRÉE`.
![ss3-4](https://www.freecodecamp.org/news/content/images/2022/07/ss3-4.png)

Maintenant, la coloration syntaxique est activée :
![ss4-4](https://www.freecodecamp.org/news/content/images/2022/07/ss4-4.png)

Si vous avez déjà ouvert le fichier en tapant `nano nom_du_fichier` dans WSL...

Lorsque vous avez terminé vos modifications, appuyez sur `CTRL + O` et appuyez sur `ENTRÉE` pour sauvegarder les modifications.
![save-exit-nano](https://www.freecodecamp.org/news/content/images/2022/07/save-exit-nano.gif)

## Comment quitter Nano
Pour quitter Nano, il vous suffit d'appuyer sur `CTRL` + `X`.
![ss5-5](https://www.freecodecamp.org/news/content/images/2022/07/ss5-5.png)

Si vous avez des modifications non sauvegardées, vous serez invité à sauvegarder les modifications avant de quitter l'éditeur.
![save-nano](https://www.freecodecamp.org/news/content/images/2022/07/save-nano.gif)

## Conclusion
J'espère que cet article vous a aidé à apprendre comment sauvegarder un fichier dans Nano et quitter l'éditeur quand vous le souhaitez.

N'oubliez pas :
- Taper `nano` vous permet d'accéder à l'éditeur Nano dans WSL
- `CTRL` + `O` sauvegarde un fichier Nano
- `CTRL` + `X` quitte Nano

Merci d'avoir lu. Si vous trouvez l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.