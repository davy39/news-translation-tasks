---
title: Comment corriger l'erreur "Élément introuvable" sous Windows lors de la suppression
  d'un fichier ou d'un dossier
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-04-15T18:32:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-item-not-found-windows-error-deleting-file-folder
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Email_woman1.jpg
tags:
- name: command line
  slug: command-line
- name: error
  slug: error
- name: Windows
  slug: windows
seo_title: Comment corriger l'erreur "Élément introuvable" sous Windows lors de la
  suppression d'un fichier ou d'un dossier
seo_desc: "If you use a Windows operating system, then you might have gotten this\
  \ error before when trying to delete a file or folder. \nIt happens when, even though\
  \ the file or folder is there, Windows says that it is failing to delete it because\
  \ it can't find ..."
---

Si vous utilisez un système d'exploitation Windows, vous avez peut-être déjà rencontré cette erreur lorsque vous essayez de supprimer un fichier ou un dossier. 

Cela se produit lorsque, même si le fichier ou le dossier est présent, Windows indique qu'il ne peut pas le supprimer car il ne trouve pas ce fichier/dossier dans ce répertoire.

Cela m'est également arrivé. En fait, j'ai été confronté à ce problème assez souvent. Et ce soir n'a pas été différent. 

J'essayais de supprimer un dossier, mais je n'y arrivais pas. Chaque fois que j'essayais de supprimer le dossier, Windows m'affichait un message disant "**Ceci n'est plus situé dans [emplacement]. Vérifiez l'emplacement de l'élément et réessayez.**" 

J'ai essayé toutes les méthodes que j'ai pu trouver pour résoudre le problème, mais rien n'a fonctionné. 

Enfin, j'ai réussi et j'ai résolu le problème. Alors, je me suis dit pourquoi ne pas partager l'astuce que j'ai découverte avec les autres ? Alors, voici ! 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-225801.png)
_[Source de l'image : D Studios Media](https://www.youtube.com/watch?v=u4IQCZ5dKMw)_

Si vous avez lu [mes autres articles sur freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/), alors vous devriez savoir que j'utilise toujours des images de mon propre ordinateur. Donc, si vous vous demandez pourquoi je partage une image d'une autre source, ne vous inquiétez pas – vous allez obtenir la réponse tout de suite !

Alors que j'essayais de résoudre le problème pour pouvoir supprimer en toute sécurité le dossier que je voulais supprimer, j'ai essayé diverses méthodes. Enfin, j'ai résolu le problème, et je pense que vous pouvez deviner ce que je veux dire ici : le dossier a été supprimé avec succès ! 

Comme le dossier avait été supprimé, je n'ai pas pu prendre de captures d'écran. J'ai donc échoué à collecter la capture d'écran avant de supprimer le dossier.

C'est pourquoi j'ai utilisé une image d'une autre source ci-dessus. 😅

## Comment corriger l'erreur "Élément introuvable" sous Windows

Maintenant, laissez-moi vous montrer comment vous pouvez également résoudre ce problème sur votre système d'exploitation Windows. Ne vous inquiétez pas, car je vais vous montrer chaque étape depuis mon propre ordinateur.

Supposons que j'ai un dossier comme celui ci-dessous qui ne se supprime pas, peu importe mes tentatives.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-230359.png)

Alors, j'utiliserai une astuce spéciale où j'utiliserai le terminal pour supprimer ce dossier en toute sécurité.

Ouvrez l'invite de commandes en tant qu'administrateur. Pour cela, cliquez simplement sur le bouton Windows et recherchez **CMD**. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-230529.png)

Maintenant, faites un clic droit sur **Invite de commandes**, et cliquez sur **Exécuter en tant qu'administrateur**. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-230710-1.png)

L'invite de commandes s'ouvrira avec les privilèges d'un administrateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-232004.png)

Maintenant, nous devons utiliser la commande `rd /s "\\?\chemin`. Dans le chemin, vous devez entrer l'adresse du dossier. 

Vous pouvez obtenir l'adresse du dossier ou du répertoire de diverses manières. Je vais vous montrer deux méthodes ci-dessous.

**Première méthode :** Faites un clic droit sur le dossier/fichier, et cliquez sur propriétés.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-231044.png)

Ici, vous obtiendrez l'adresse du répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-231156.png)

Vous devez ajouter le nom du dossier après cela. Par exemple, ici mon répertoire est : `C:\Users\FBA\Desktop` et le nom du dossier que je veux supprimer est `Ce dossier ne se supprime pas`. Donc, l'adresse complète du répertoire que je dois utiliser dans le terminal sera : `C:\Users\FBA\Desktop\Ce dossier ne se supprime pas`. 

**Deuxième méthode :** Allez dans le dossier où vous voulez supprimer le dossier/fichier, et vous obtiendrez l'adresse du répertoire là.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-231450.png)

Cliquez simplement sur l'adresse et copiez toute l'adresse. Vous pouvez également utiliser `Ctrl` + `C` comme raccourci.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-231537.png)

Quoi qu'il en soit, après cela, j'ai l'adresse du répertoire. Maintenant, je dois utiliser la commande complète, `**rd /s "\?\C:\Users\FBA\Desktop\Ce dossier ne se supprime pas**` dans le terminal et je dois appuyer sur la touche Entrée après cela.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-233359.png)

Maintenant, je dois taper Y et appuyer sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-14-233408.png)

Et voilà ! Le dossier a maintenant disparu. 😊

Vous pouvez en apprendre davantage sur cette commande rd depuis [la documentation officielle de Microsoft](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/rd).

De cette manière, vous pouvez supprimer en toute sécurité n'importe quel dossier/fichier qui ne se supprime pas en utilisant la méthode régulière.

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !