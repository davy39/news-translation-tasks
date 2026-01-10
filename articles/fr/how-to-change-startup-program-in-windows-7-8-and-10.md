---
title: Comment modifier les programmes de démarrage dans Windows 7, 8 et 10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T19:54:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-startup-program-in-windows-7-8-and-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d4b740569d1a4ca36f9.jpg
tags:
- name: how-to
  slug: how-to
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Comment modifier les programmes de démarrage dans Windows 7, 8 et 10
seo_desc: 'By Dillion Megida

  Startup programs are programs which run automatically when a system is booted. This
  is a good practice for programs which you use frequently. It saves you the stress
  of looking for those programs, or, in some cases, manually setting...'
---

Par Dillion Megida

Les programmes de démarrage sont des programmes qui s'exécutent automatiquement lorsque le système est démarré. C'est une bonne pratique pour les programmes que vous utilisez fréquemment. Cela vous évite le stress de rechercher ces programmes ou, dans certains cas, de les configurer manuellement.

Certains programmes ont également cette fonctionnalité par défaut lorsqu'ils sont nouvellement installés.

Mais si vous avez trop de programmes de démarrage, cela peut ralentir le processus de démarrage. Cela a un effet négatif, surtout sur les systèmes avec des capacités limitées ou une puissance de traitement réduite.

Dans cet article, nous allons apprendre comment ouvrir le panneau de configuration des applications de démarrage, comment activer et désactiver les applications de démarrage, et enfin comment ajouter nos programmes de démarrage souhaités dans Windows 7, 8 et 10.

Dans chacune de ces versions de Windows, il existe un Panneau de configuration pour les applications de démarrage qui affiche une liste d'applications pouvant être exécutées automatiquement au démarrage. Ces applications sont soit activées pour le démarrage, soit désactivées.

Alors, examinons le processus pour chaque version de Windows.

## Dans Windows 7

### Ouvrir le Panneau de configuration des applications de démarrage

Ouvrez le menu de démarrage de Windows, puis tapez "**MSCONFIG**". Lorsque vous appuyez sur Entrée, la console de configuration système s'ouvre. Cliquez ensuite sur l'onglet "**Démarrage**" qui affichera certains programmes pouvant être activés ou désactivés pour le démarrage.

### Désactiver/Activer une application de démarrage

Les cases à cocher à côté des applications indiquent leur statut. Si elle est cochée, l'application est activée pour le démarrage, sinon, elle est désactivée.

Pour désactiver une application activée, décochez simplement la case à cocher et cliquez sur Appliquer.

Pour activer une application désactivée, cochez la case à cocher et cliquez sur Appliquer.

Ces deux processus nécessitent que le système soit redémarré avant que les modifications ne soient appliquées aux applications.

### Ajouter une application de démarrage

Pour ajouter une application, vous devrez explorer le dossier de démarrage. Pour ce faire, essayez l'une des méthodes suivantes :

- Ouvrez le menu Démarrer et tapez "**Démarrage**" (pour le rechercher). Une fois trouvé, faites un clic droit et sélectionnez Explorer pour ouvrir le dossier.
- Ouvrez le menu Démarrer, sélectionnez "**Tous les programmes**" et faites défiler la liste jusqu'à trouver le dossier de démarrage. Une fois trouvé, explorez-le.

Créez un raccourci de votre programme souhaité, copiez-le et collez-le dans ce dossier. Après cela, le programme sera automatiquement ajouté au panneau avec un statut "**activé**".

## Dans Windows 8

### Ouvrir le Panneau de configuration des applications de démarrage

Pour ouvrir le panneau, essayez l'une des méthodes suivantes :

- Ouvrez le "**Gestionnaire des tâches**" et sélectionnez l'onglet "**Démarrage**"
- Ouvrez le menu de démarrage de Windows et tapez "**Démarrage**" pour rechercher le programme. Sélectionnez ensuite l'une des options fournies.

### Désactiver/Activer une application de démarrage

Pour désactiver une application de démarrage qui est activée, faites un clic droit sur l'application et sélectionnez "**Désactiver**".

Pour activer une application de démarrage qui est désactivée, faites un clic droit sur l'application et sélectionnez "**Activer**".

### Ajouter une application de démarrage

Appuyez sur la touche Windows et la touche R pour ouvrir la boîte de dialogue Exécuter. Ensuite, entrez **%AppData%**. Cela ouvrira un dossier roaming.

Accédez à **\Microsoft\Windows\Menu Démarrer\Programmes\Démarrage**. Dans ce dossier, collez le raccourci de votre application souhaitée. Cela en fera une application de démarrage avec un statut "activé".

## Dans Windows 10

### Ouvrir le Panneau de configuration des applications de démarrage

- Ouvrez le menu Démarrer, tapez "**Applications de démarrage**" (pour le rechercher) et cliquez sur l'un des résultats.
- Ouvrez le "**Gestionnaire des tâches**", puis sélectionnez l'onglet "**Démarrage**"

### Désactiver/Activer les applications de démarrage

Pour désactiver une application de démarrage, faites un clic droit sur une application dans la liste avec un statut "**activé**" et sélectionnez "**désactiver**".

Pour activer une application de démarrage dans la liste qui est désactivée, faites un clic droit sur l'application et sélectionnez "**activer**".

### Ajouter une application de démarrage

Maintenez la touche Windows et la touche R enfoncées sur le clavier. Dans la boîte de dialogue Exécuter, entrez "**shell:startup**".

Dans le dossier, vous pouvez ajouter n'importe quelle application de votre choix que vous souhaitez exécuter au démarrage. Elles seront ajoutées à la liste, donc lorsque vous accédez à vos applications de démarrage, vous pouvez les désactiver ou les activer.

## Conclusion

Si vous avez une application que vous exécutez toujours lorsque vous démarrez votre système, il est bon de la configurer comme programme de démarrage.

Lorsque votre système devient lent au démarrage, c'est probablement à cause des programmes de démarrage. Maintenant, vous savez comment les désactiver ou les réduire.