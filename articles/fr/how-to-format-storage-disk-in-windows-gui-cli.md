---
title: Comment supprimer un disque ou un périphérique de stockage dans Windows en
  utilisant l'interface graphique et l'interface en ligne de commande
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-01-20T20:20:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-storage-disk-in-windows-gui-cli
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Artboard-1-2.jpg
tags:
- name: cli
  slug: cli
- name: Windows
  slug: windows
seo_title: Comment supprimer un disque ou un périphérique de stockage dans Windows
  en utilisant l'interface graphique et l'interface en ligne de commande
seo_desc: "Deleting or formatting a disk or storage device is a common task for most\
  \ computer users. \nIf you use the Windows operating system, you would normally\
  \ do that using the GUI Disk Management application which comes built-in with any\
  \ Windows operating s..."
---

Supprimer ou formater un disque ou un périphérique de stockage est une tâche courante pour la plupart des utilisateurs d'ordinateurs. 

Si vous utilisez le système d'exploitation Windows, vous le feriez normalement en utilisant l'application de gestion des disques GUI qui est intégrée à tout système d'exploitation Windows.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_18-50.png)
_Gestion des disques (GUI)_

Parfois, vous pourriez avoir des difficultés à supprimer un disque en utilisant l'application GUI, vous devrez donc le faire en utilisant l'interface en ligne de commande (CMD) à la place. 

Dans cet article, je vais vous présenter le processus de suppression d'un disque de tout type de périphérique de stockage en utilisant la méthode GUI et la méthode CLI directement à partir du système d'exploitation Windows lui-même. J'utiliserai une clé USB de 32 Go comme cobaye. 

**Note importante :** assurez-vous d'abord que vous avez copié toutes vos données sur un autre lecteur/stockage avant de supprimer un disque ou un périphérique de stockage.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/IMG_20220120_185541.jpg)
_Mon cobaye_

## Comment formater ou supprimer un disque en utilisant la méthode GUI (Interface Graphique)

Tout d'abord, ouvrez la Gestion des disques. Vous pouvez le faire de plusieurs manières, mais je vais vous montrer deux méthodes ici.

Cliquez sur l'icône de recherche dans la barre des tâches et tapez `Gestion des disques`. Cliquez sur `Créer et formater des partitions de disque dur`.  

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-07.png)
_Résultat de la recherche pour la Gestion des disques_

Alternativement, vous pouvez ouvrir le panneau de configuration et rechercher `Gestion des disques`. Vous obtiendrez `Créer et formater des partitions de disque dur` sous les `Outils Windows`. Cliquez dessus.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-36.png)
_Résultat de la recherche pour la Gestion des disques dans le Panneau de configuration_

L'outil `Gestion des disques` s'ouvrira et affichera tous les périphériques de stockage ainsi que leurs partitions. Ici, la 3ème option – **Disque 2** – est notre cobaye (clé USB de 32 Go).

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-33.png)
_Notre cobaye dans la Gestion des disques_

Supposons que vous souhaitiez supprimer la première partition du **Disque 2**. Vous devez alors suivre ces étapes :

Tout d'abord, faites un clic droit sur la partition que vous souhaitez supprimer. Cliquez ensuite sur `Supprimer le volume...`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot--81--1.png)
_Cliquez sur Supprimer le volume..._

Assurez-vous d'avoir copié tout le contenu du disque/stockage entier. Si vous l'avez déjà fait, cliquez simplement sur `Oui`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-43.png)
_Fenêtre de confirmation avant de supprimer une partition ou un stockage_

Une autre fenêtre de confirmation peut apparaître indiquant qu'il est actuellement utilisé. Assurez-vous qu'aucune autre tâche ou application n'utilise le lecteur/la partition. Cliquez ensuite simplement sur `Oui`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-47.png)
_Une autre confirmation_

Maintenant, vous verrez que la partition est devenue non allouée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-49.png)
_Après avoir supprimé une partition du Disque 2_

De cette manière, vous pouvez supprimer n'importe quelle partition. Plus tard, vous pouvez créer une nouvelle partition à partir de celle-ci ou étendre la partition avec d'autres partitions existantes. 

Pour supprimer un stockage/disque complètement, vous devez supprimer toutes les partitions qu'il contient manuellement, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-55_1.png)
_Après avoir supprimé toutes les partitions du Disque 2_

Après cela, vous verrez que l'ensemble du stockage/disque est devenu non alloué. Si vous souhaitez créer une nouvelle partition, faites simplement un clic droit sur la boîte **Non alloué** et cliquez sur `Nouveau volume simple...`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot--85-.png)
_Création d'un nouveau volume_

Cliquez sur `Suivant` dans l'assistant.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-58.png)

Sélectionnez la taille du volume que vous souhaitez et cliquez sur `Suivant`. Si vous souhaitez la taille totale du volume, conservez simplement la boîte telle quelle.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-59.png)
_Taille du volume_

Sélectionnez la lettre de lecteur que vous souhaitez et cliquez à nouveau sur le bouton `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_21-00.png)
_Sélection de la lettre de lecteur_

Sélectionnez le système de fichiers et l'étiquette du volume. Si vous ne souhaitez pas modifier quoi que ce soit ici, conservez la taille de l'unité d'allocation comme `Par défaut`. De plus, si vous souhaitez un formatage rapide, conservez la case à côté de `Effectuer un formatage rapide` cochée. Cliquez sur le bouton `Suivant`.

**Quelques informations supplémentaires concernant le système de fichiers** : Si vous souhaitez travailler sur Windows, Linux et Mac simultanément, sélectionnez FAT32. Gardez simplement à l'esprit que FAT32 ne supporte pas plus de 4 Go dans un seul fichier. 

Pour travailler sur Windows et Linux simultanément tout en évitant la limite de 4 Go par fichier, NTFS est un bon choix.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_21-02.png)

Cliquez sur `Terminer` et c'est fait.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_21-03.png)
_Terminer la tâche_

Maintenant, vous avez vu comment supprimer un disque/stockage via l'interface graphique. Maintenant, je vais discuter de la partie la plus excitante – la méthode **CLI** !

## Comment supprimer un disque/stockage en utilisant la méthode CLI (Interface en Ligne de Commande)

Tout d'abord, ouvrez l'invite de commande ou le **CMD**. Vous pouvez le faire en recherchant le nom comme dans l'image ci-dessous. **Assurez-vous de cliquer sur `Exécuter en tant qu'administrateur`.**

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-55.png)
_Ouvrir le CMD_

Alternativement, vous pouvez ouvrir le CMD en utilisant la fenêtre Exécuter. Appuyez simplement sur les touches `Win` + `R`. Tapez `cmd` et appuyez sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-57.png)
_Ouvrir le CMD en utilisant Exécuter_

Après avoir ouvert le CMD, nous devons ouvrir DiskPart. Selon Google, voici une définition de Diskpart :

> L'interpréteur de commandes diskpart vous aide à gérer les lecteurs de votre ordinateur (disques, partitions, volumes ou disques durs virtuels).

Pour ouvrir DiskPart, tapez la commande `diskpart` et appuyez sur Entrée sur votre clavier.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_19-59.png)
_Ouvrir DiskPart_

Maintenant, nous devons vérifier les disques disponibles. Pour cela, tapez la commande `list disk`. Cela affichera tous les lecteurs que nous avons dans notre ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-03.png)
_liste des disques_

Vous pouvez voir que j'ai 3 disques ou périphériques de stockage dans ma station de travail en ce moment. Ceux-ci sont classés comme `Disque 0`, `Disque 1` et `Disque 2`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-05.png)
_État du disque_

Vous pouvez également voir les autres statistiques comme l'**État** des disques, la **Taille** des disques, combien d'espace **libre** ils ont, si le disque est devenu **Dynamique** ou non, et la table de partition (dans mon cas, il s'agit de GPT ou GUID Partition Table, indiqué comme `Gpt`). 

Gardez à l'esprit que si votre disque est en MBR, vous ne rencontrerez aucun problème dans le processus suivant. Si votre disque est en GPT comme le mien, vous obtiendrez une erreur – mais ne craignez rien ! Je vais montrer comment vous pouvez résoudre l'erreur et terminer le reste de la tâche également. 

Ici, comme je travaille toujours avec ma clé USB de 32 Go comme cobaye, `Disque 2` est mon disque cible.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-09.png)
_Disque cible_

Je vais simplement sélectionner le disque cible (le disque que je veux supprimer).

Pour sélectionner le disque, vous devez taper la commande `select disk 2`. Appuyez ensuite simplement sur la touche Entrée. 

Ici, vous devez taper le numéro de disque que vous souhaitez supprimer. Par exemple, si votre disque cible est `3`, vous devez utiliser la commande `select disk 3`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-11.png)
_Sélection du disque cible_

Le disque cible a été sélectionné !

Maintenant, vous devez supprimer l'ensemble du disque. Pour cela, tapez simplement la commande `clean`. Cela supprimera toutes les partitions que le disque cible possède.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot--82-.png)
_Nettoyage du disque_

Vous recevrez la confirmation que DiskPart a nettoyé avec succès le disque cible.

Rappelez-vous que nous ne pouvons pas encore utiliser le lecteur. 

Pour créer une partition principale, tapez la commande `create partition primary` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-23.png)
_Création d'une partition principale_

Nous recevrons une confirmation qu'il a réussi à créer la partition spécifiée.

Maintenant, nous devons rendre la partition active. Tout d'abord, nous devons sélectionner la partition. Comme nous n'avons créé qu'une seule partition, nous n'avons que `Partition 1`. Je vais donc sélectionner la première partition en utilisant la commande `select partition 1` et appuyer sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-27.png)
_Sélection de la partition_

Maintenant, nous devons rendre la partition active. Pour cela, tapez la commande `active` et appuyez sur Entrée. Vous recevrez l'erreur marquée uniquement si votre disque est également sur une table de partition GPT comme moi.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-31.png)

Cela se produit parce que la commande `active` n'est pas applicable pour les disques GPT. Nous pouvons simplement convertir l'ensemble du disque en MBR, puis appliquer la commande `active`.

Si votre disque est en MBR, vous ne recevrez pas le message d'erreur. Vous pouvez sauter les quelques étapes suivantes si vous ne recevez pas le message d'erreur à cette étape.

Pour convertir le disque en MBR, vous devez d'abord nettoyer (supprimer toutes les partitions) le disque. Tapez donc `clean` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-33.png)
_Commande de nettoyage_

Maintenant, pour convertir la table de partition de GPT en MBR, tapez `convert MBR` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-36.png)
_Conversion en MBR_

Pour créer une partition principale, entrez la commande et appuyez sur Entrée `create partition primary`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-38.png)
_Création d'une partition principale_

Maintenant, sélectionnez la partition en entrant la commande `select partition 1` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-39.png)
_Sélection de la partition_

Maintenant, vous devez rendre la partition active. Tapez simplement `active` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-41.png)
_Rendre la partition active_

D'accord, **c'est ici que vous reprenez** si vous n'avez pas obtenu l'erreur.

Maintenant, nous devons formater la partition. Supposons que je veux le système de fichiers **NTFS** pour formater le disque. Je peux également ajouter une étiquette ici.

Tapez la commande `format fs=NTFS label=my_guinea_pig quick` et appuyez sur Entrée. Ici, `fs` indique le système de fichiers, et `quick` indique que je veux un formatage rapide ici. 

Vous pouvez ajouter n'importe quelle étiquette que vous souhaitez, mais assurez-vous de ne pas laisser d'espace entre plusieurs mots dans le nom de l'étiquette (vous pouvez utiliser le trait de soulignement si vous le souhaitez). 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot--83-.png)
_Formatage rapide du disque_

Maintenant, nous avons terminé et nous pouvons également fermer le **CMD**. Tapez simplement `exit` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot--84-.png)
_Quitter le CMD_

Maintenant, si je vérifie le lecteur USB en utilisant mon explorateur de fichiers, je verrai que mon lecteur est formaté exactement comme je le souhaitais.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-46.png)
_La tâche a été terminée_

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2022-01-20_20-47.png)
_Propriétés du disque_

Maintenant, vous savez comment supprimer et reformater un disque/stockage via l'interface en ligne de commande. 

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez entrer en contact avec moi, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !