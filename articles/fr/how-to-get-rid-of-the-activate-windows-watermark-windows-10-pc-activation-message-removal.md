---
title: Comment supprimer le filigrane "Activer Windows" [Suppression du message d'activation
  de Windows 10 PC]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-06T16:00:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-rid-of-the-activate-windows-watermark-windows-10-pc-activation-message-removal
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/activate.png
tags:
- name: how-to
  slug: how-to
- name: Windows
  slug: windows
seo_title: Comment supprimer le filigrane "Activer Windows" [Suppression du message
  d'activation de Windows 10 PC]
seo_desc: 'If you''re a Windows user, you might have seen the "Activate Windows" message
  that displays over every other thing – including your cursor. I guess they gave
  it a z-index of infinity.

  This message gets displayed when you use a Windows OS that has an i...'
---

Si vous êtes un utilisateur de Windows, vous avez peut-être vu le message "Activer Windows" qui s'affiche par-dessus tout le reste – y compris votre curseur. Je suppose qu'ils lui ont donné un z-index infini.

Ce message s'affiche lorsque vous utilisez un système d'exploitation Windows dont la licence est invalide ou expirée. Cela vous empêche de personnaliser votre bureau ou de recevoir des mises à jour pour Windows Defender – maintenant Windows Security. Vous ne pourrez également pas installer Microsoft Office.

Si c'est le cas, vous pouvez supprimer le filigrane car il pourrait avoir un effet négatif sur la hiérarchie visuelle et pourrait être embarrassant si vous prenez des captures d'écran ou enregistrez votre bureau. 

Cela m'est arrivé lorsque j'utilisais freeCodeCamp pour ma première série de 100DaysOfCode.
![day49](https://www.freecodecamp.org/news/content/images/2021/12/day49.jpg)

Dans cet article, je vais vous montrer 4 façons de supprimer le filigrane "Activer Windows" sur votre PC Windows 10. 

Certaines des astuces ne suppriment que le message mais pas les problèmes sous-jacents, vous devriez donc prêter attention à la dernière, qui supprimera le message et activera également votre Windows.

## Table des matières
- [Comment supprimer le filigrane "Activer Windows" avec PowerShell](#heading-comment-supprimer-le-filigrane-activier-windows-avec-powershell)
- [Comment supprimer le filigrane "Activer Windows" avec le Bloc-notes](#heading-comment-supprimer-le-filigrane-activier-windows-avec-le-bloc-notes)
- [Comment supprimer le filigrane "Activer Windows" en utilisant le Registre](#heading-comment-supprimer-le-filigrane-activier-windows-en-utilisant-le-registre)
- [Comment supprimer le filigrane "Activer Windows" avec une clé de produit](#heading-comment-supprimer-le-filigrane-activier-windows-avec-une-cle-de-produit)
- [Conclusion](#heading-conclusion)


## Comment supprimer le filigrane "Activer Windows" avec PowerShell

PowerShell vous permet d'interagir directement avec votre système d'exploitation Windows avec des scripts. 

Il existe un script PowerShell que vous pouvez exécuter pour vous débarrasser du message "Activer Windows". 

**Pour exécuter le script, suivez les étapes ci-dessous.**

**Étape 1** : Appuyez sur `WIN` (touche du logo Windows) + `S` sur votre clavier.

**Étape 2** : Recherchez "powershell". Vous devez exécuter le script en tant qu'administrateur, alors cliquez sur "Exécuter en tant qu'administrateur" à droite.
![ss-1-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-1.jpg)

**Étape 3** : Tapez "slmgr /renew" (sans les guillemets) et appuyez sur `ENTRÉE`.
![ss-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2.png)

**Étape 4** : Redémarrez votre PC.

Si vous avez effectué plusieurs modifications avec des applications tierces pour activer Windows, cette solution pourrait ne pas fonctionner pour vous. Si cela ne fonctionne pas, essayez la suivante.

## Comment supprimer le filigrane "Activer Windows" avec le Bloc-notes

Aussi simple que le Bloc-notes semble pour tout le monde, vous pouvez l'utiliser pour supprimer le filigrane "Activer Windows". En fait, cette méthode est l'une des plus populaires pour se débarrasser du message.
	
Vous pouvez utiliser le Bloc-notes pour supprimer le message avec les étapes simples ci-dessous.

**Étape 1** : Appuyez sur le bouton `WIN` de votre clavier et recherchez le Bloc-notes. Cliquez sur Ouvrir à droite ou sur le résultat de recherche du Bloc-notes pour lancer l'application.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-3-1.jpg)

**Étape 2** : Assurez-vous de travailler avec un nouveau fichier non enregistré. Collez le script ci-dessous :

```
@echo off
taskkill /F /IM explorer.exe
explorer.exe
exit
```

**Étape 3** : Cliquez sur Fichier dans le menu et sélectionnez "Enregistrer sous".
![ss-4-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-4-1.jpg)

**Étape 4** : Nommez le fichier "Activation.bat" et sélectionnez "Tous les fichiers" comme format. Ensuite, enregistrez le fichier à l'emplacement de votre choix.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/12/ss-5.jpg)

**Étape 5** : Localisez le fichier, faites un clic droit dessus, puis sélectionnez "Exécuter en tant qu'administrateur". 
![ss-6-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-1.png)

Le script sera exécuté rapidement et rafraîchira votre ordinateur.

**Étape 6** : Redémarrez votre PC.

## Comment supprimer le filigrane "Activer Windows" en utilisant le Registre

Le registre Windows 10 vous permet d'effectuer des modifications plus profondes qui ont des effets significatifs sur votre ordinateur.

Vous pouvez supprimer le filigrane "Activer Windows" en effectuant une modification moins compliquée dans le Registre, comme indiqué ci-dessous.

**Étape 1** : Faites un clic droit sur Démarrer et sélectionnez Exécuter.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-7-1.jpg)

**Étape 2** : Tapez "regedit" (sans les guillemets) dans la boîte de dialogue Exécuter et appuyez sur `ENTRÉE`.
![ss-8](https://www.freecodecamp.org/news/content/images/2021/12/ss-8.png)

**Étape 3** : Développez HKEY_CURRENT_USER, Panneau de configuration, puis cliquez sur Bureau.
![ss-9-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-9-1.png)

**Étape 4** : Localisez PaintDesktopVersion et double-cliquez dessus.

**Étape 5** : Changez la valeur de 1 à 0 et cliquez sur Ok.
![ss-10](https://www.freecodecamp.org/news/content/images/2021/12/ss-10.jpg)

**Étape 6** : Redémarrez votre ordinateur.

## Comment supprimer le filigrane "Activer Windows" avec une clé de produit

La meilleure façon de supprimer le filigrane "Activer Windows" est de faire ce que le message dit - activer Windows. 

Vous pouvez activer Windows avec une clé de produit que vous devez acheter auprès de Microsoft.

Les étapes ci-dessous vous aideront à utiliser votre clé de produit pour activer Windows :

**Étape 1** : Cliquez sur Démarrer et sélectionnez Paramètres.
![ss-11-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-11-1.jpg)

**Étape 2** : Choisissez Mise à jour et sécurité parmi les vignettes du menu.
![ss-12-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-12-1.jpg)

**Étape 3** : Passez à l'onglet Activation à gauche et cliquez sur Changer la clé de produit.
![ss-13-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-13-1.jpg)

**Étape 4** : Entrez votre clé de produit alphanumérique de 24 caractères et cliquez sur Suivant. 
![ss-14](https://www.freecodecamp.org/news/content/images/2021/12/ss-14.png)

Windows sera activé tant que la clé de produit est correcte.

## Conclusion
J'espère que ces méthodes pour supprimer le filigrane "Activer Windows" vous seront utiles. 

Si vous trouvez cet article utile, n'oubliez pas de le partager avec vos amis et votre famille.

Merci d'avoir lu.