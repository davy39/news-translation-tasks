---
title: Le menu Démarrer de Windows 10 ne fonctionne pas (Résolu)
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-06T17:07:32.000Z'
originalURL: https://freecodecamp.org/news/windows-10-start-menu-not-working-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa1226549c47664ed819287.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Le menu Démarrer de Windows 10 ne fonctionne pas (Résolu)
seo_desc: 'Windows 10 has come a long way since it was first launched in 2015. Each
  update brings a lot of new features, and Microsoft has embraced the open source
  community in a way that was once thought impossible.

  Still, like with any operating system, there...'
---

Windows 10 a parcouru un long chemin depuis son lancement initial en 2015. Chaque mise à jour apporte de nombreuses nouvelles fonctionnalités, et Microsoft a embrassé la communauté open source d'une manière autrefois jugée impossible.

Néanmoins, comme pour tout système d'exploitation, il existe des bugs. Et l'un des bugs les plus courants auxquels les utilisateurs de Windows 10 ont été confrontés est l'arrêt soudain du fonctionnement du menu Démarrer.

Parfois, le menu Démarrer ouvert se fige et devient inactif, et d'autres fois, il ne s'ouvre pas du tout lorsque vous cliquez sur le bouton du menu Démarrer.

Quel que soit le problème spécifique que vous rencontrez avec le menu Démarrer de Windows 10, nous allons passer en revue quelques solutions rapides et moins rapides dans cet article.

## Comment redémarrer l'Explorateur Windows

L'Explorateur Windows, maintenant appelé Explorateur de fichiers, est l'application que vous utilisez pour naviguer dans votre système de fichiers et ouvrir des programmes et des fichiers. Mais il contrôle également des éléments comme le menu Démarrer, la barre des tâches et d'autres applications.

Si vous avez un problème avec le menu Démarrer, la première chose que vous pouvez essayer est de redémarrer le processus "Explorateur Windows" dans le Gestionnaire des tâches.

Pour ouvrir le Gestionnaire des tâches, appuyez sur **Ctrl + Alt + Suppr**, puis cliquez sur le bouton "Gestionnaire des tâches".

Cliquez sur "Plus de détails" pour voir une liste complète des programmes ouverts et des processus en arrière-plan que vous exécutez :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/task-manager-more-details.jpg)

Faites défiler la liste jusqu'à ce que vous trouviez le processus "Explorateur Windows". Ensuite, faites un clic droit sur "Explorateur Windows" et sélectionnez "Redémarrer" :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/task-manager-restart-windows-explorer.jpg)

Il y aura un bref flash pendant que Windows redémarre l'Explorateur Windows, ainsi que la barre des tâches et le menu Démarrer.

Après cela, essayez d'ouvrir le menu Démarrer. S'il ne fonctionne toujours pas normalement, essayez une des autres solutions ci-dessous.

## Comment réparer les fichiers système Windows corrompus ou manquants

Parfois, une mise à jour se passe mal, ou vous avez accidentellement supprimé un fichier important en explorant le système de fichiers.

Si le menu Démarrer vous cause toujours des problèmes, ou si d'autres applications principales de Windows plantent, vous pouvez essayer de restaurer les fichiers système Windows manquants ou corrompus.

Pour ce faire, vous devrez [ouvrir l'invite de commandes Windows en tant qu'administrateur](https://www.freecodecamp.org/news/how-to-open-the-command-prompt-in-windows-10/#how-to-open-command-prompt-as-an-administrator) et exécuter le programme de vérification des fichiers système.

Une fois que vous avez ouvert l'invite de commandes en tant qu'administrateur, exécutez la commande `sfc /scannow` :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sfc-scannow.jpg)

Le vérificateur de fichiers système commencera à parcourir tous vos fichiers système et remplacera les fichiers corrompus ou manquants par une copie mise en cache.

Ce processus peut prendre un certain temps, alors n'hésitez pas à faire autre chose pendant 5 à 10 minutes. Faites simplement attention à ne pas fermer la fenêtre pendant que `sfc` fait son travail.

Une fois que le vérificateur de fichiers système a terminé, vous verrez soit un rapport de tous les fichiers qu'il a remplacés, soit, si tout était correct, vous verrez un message comme celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sfc-scan-complete.jpg)

Si le vérificateur de fichiers système a remplacé des fichiers système corrompus ou manquants, sauvegardez tout votre travail ouvert et redémarrez votre ordinateur. Une fois que vous êtes reconnecté, essayez d'ouvrir le menu Démarrer pour voir si cela a résolu vos problèmes.

**Note :** Vous pourriez également utiliser PowerShell pour exécuter la commande `sfc /scannow`, mais n'oubliez pas que vous devrez ouvrir un terminal PowerShell élevé.

## Comment réinitialiser le menu Démarrer avec les applications Windows 10 par défaut

La prochaine chose que vous pouvez essayer est de réinitialiser complètement le menu Démarrer, ainsi que toutes les applications Windows 10 préinstallées ou installées depuis le Microsoft Store.

Pour ce faire, vous devrez ouvrir PowerShell en tant qu'administrateur – l'invite de commandes ne fonctionnera pas pour la commande que vous allez exécuter.

Il existe de nombreuses façons d'ouvrir PowerShell, mais l'une des plus rapides est d'utiliser le programme Exécuter.

Utilisez le raccourci **Windows + R** pour ouvrir le programme Exécuter, entrez "powershell", puis maintenez "Ctrl + Maj" enfoncées et cliquez sur le bouton "OK" :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/run-cmd-powershell.jpg)

Cela devrait ouvrir un terminal PowerShell avec des privilèges administratifs.

Dans le terminal PowerShell, exécutez la commande suivante :

```
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

La commande `Get-AppXPackage` tentera de réinstaller toutes les applications Windows par défaut, y compris le menu Démarrer et la barre de recherche.

Elle enregistrera également un fichier manifeste pour chaque programme qu'elle réinstalle. Vous n'avez pas à vous soucier des fichiers manifeste, cependant – c'est juste quelque chose dont Windows a besoin pour exécuter chaque programme.

Donnez-lui 5 à 10 minutes, et assurez-vous de ne pas fermer la fenêtre PowerShell jusqu'à ce qu'elle ait terminé.

**Note :** Vous pourriez voir des erreurs effrayantes apparaître pendant l'exécution de la commande `Get-AppXPackage`. Ne vous en souciez pas – la plupart ne sont que des avertissements sur les raisons pour lesquelles un programme ne peut pas être réinstallé :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/powershell-get-appxpackage.jpg)

Lorsque la commande `Get-AppXPackage` est terminée, redémarrez votre ordinateur, connectez-vous et essayez d'ouvrir le menu Démarrer.

## Comment réinitialiser votre installation de Windows 10

Si aucune des méthodes ci-dessus n'a corrigé le menu Démarrer, la dernière chose que vous pouvez essayer est de faire une réinitialisation d'usine de votre installation de Windows 10. Mais gardez à l'esprit que c'est une méthode "presque de la terre brûlée", et ne devrait être utilisée qu'en dernier recours.

La réinitialisation de votre installation de Windows 10 devrait conserver tous vos fichiers personnels intacts (documents, images, vidéos, etc.), mais désinstallera tous les autres pilotes et programmes que vous avez installés. En gros, cela réinitialise votre ordinateur à l'état dans lequel il était lorsque vous l'avez allumé pour la première fois.

Avant d'aller plus loin, faites des sauvegardes de tous vos fichiers importants en utilisant une clé USB, un disque dur externe/SSD, et/ou un hébergeur de fichiers en ligne comme Google Drive ou Dropbox.

En fait, faites deux sauvegardes. Vous n'en aurez probablement pas besoin, mais cela ne fait pas de mal.

Lorsque vous avez terminé de sauvegarder tous vos fichiers, ouvrez un terminal PowerShell – utilisez le raccourci **Windows + R**, entrez "powershell", puis cliquez sur le bouton "OK".

Dans le terminal PowerShell, exécutez la commande `systemreset` pour lancer l'assistant de réinitialisation de Windows.

Ensuite, cliquez sur le bouton "Conserver mes fichiers" :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/system-reset-keep-my-files.jpg)

Attendez un moment pendant que l'assistant analyse votre système. Ensuite, vous verrez une liste de tous les programmes qui seront supprimés :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/system-reset-programs-to-be-removed.jpg)

Cliquez sur le bouton "Suivant", et suivez les instructions pour réinitialiser votre installation de Windows 10.

Une fois que vous avez terminé de réinitialiser Windows et de créer un nouvel utilisateur, le menu Démarrer devrait fonctionner à nouveau.

## "Cortana, ouvre le menu Démarrer"

Voici donc toutes les façons de corriger le menu Démarrer de Windows 10, classées du plus facile au plus difficile.

L'une de ces méthodes a-t-elle fonctionné pour vous ? Y a-t-il une autre façon d'ouvrir le menu Démarrer que j'ai manquée ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).