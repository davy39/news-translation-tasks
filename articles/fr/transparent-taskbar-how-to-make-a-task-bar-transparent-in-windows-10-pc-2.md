---
title: Barre des tâches transparente – Comment rendre la barre des tâches transparente
  dans Windows 10 PC
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-26T00:11:44.000Z'
originalURL: https://freecodecamp.org/news/transparent-taskbar-how-to-make-a-task-bar-transparent-in-windows-10-pc-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/task-bar.png
tags:
- name: how-to
  slug: how-to
- name: Windows 10
  slug: windows-10
seo_title: Barre des tâches transparente – Comment rendre la barre des tâches transparente
  dans Windows 10 PC
seo_desc: 'Making your Windows taskbar transparent is a pretty cool thing to do. It
  looks great, and it''s one of the few ways you can personalize your taskbar.

  Some resources about this topic require you to install different software to accomplish
  it. But in th...'
---

Rendre votre barre des tâches Windows transparente est une chose assez cool à faire. Cela a l'air génial, et c'est l'une des rares façons de personnaliser votre barre des tâches.

Certaines ressources sur ce sujet vous demandent d'installer différents logiciels pour y parvenir. Mais dans ce tutoriel, nous verrons comment rendre la barre des tâches complètement transparente sans aucune installation.

## Comment rendre votre barre des tâches Windows transparente

### Étape 1 - Utiliser la commande Exécuter pour ouvrir le programme Éditeur du Registre

La commande Exécuter vous permet d'ouvrir divers programmes sur votre PC en tapant leur nom. Le programme que nous allons utiliser s'appelle Éditeur du Registre.

Pour utiliser la commande Exécuter, vous pouvez utiliser le raccourci **Win + R** (bouton Windows + R) ou vous pouvez **cliquer avec le bouton droit** sur l'icône Windows et cliquer sur "Exécuter".

![Image](https://www.freecodecamp.org/news/content/images/2022/01/run-command.png)

### **Étape 2 - Taper regedit**

Après avoir cliqué sur Exécuter, une fenêtre devrait s'ouvrir où vous pouvez taper le nom d'un programme que vous souhaitez ouvrir. Tapez "regedit" et appuyez sur OK. Cela ouvrira l'Éditeur du Registre.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/regedit.png)

Après avoir cliqué sur OK, la fenêtre suivante devrait s'ouvrir :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/registry.png)

### **Étape 3 - Naviguer à travers les dossiers**

Le premier dossier à développer est le dossier `HKEY_CURRENT_USER`. Faites défiler vers le bas et développez le dossier `SOFTWARE`.

Après cela, localisez le dossier `Microsoft` et développez-le également. Ensuite, faites défiler jusqu'en bas et développez le dossier `Windows`.

Dans le dossier `Windows`, développez le dossier `CurrentVersion` suivi du dossier `Explorer`. Enfin, cliquez sur le dossier `Advanced`.

Si vous avez trouvé les étapes ci-dessus confuses, vous pouvez utiliser ce chemin comme guide :

```
Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
```

Coller le chemin ci-dessus et appuyer sur Entrée devrait vous amener automatiquement à notre emplacement actuel.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/paths.png)

### **Étape 4 - Créer un nouveau fichier**

Cliquez avec le bouton droit et survolez l'option "Nouveau".

Puis cliquez sur **Valeur DWORD (32 bits)** :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/new.png)

Après avoir cliqué sur **Valeur DWORD (32 bits)**, vous verrez un espace où vous devez taper le nom du nouveau fichier. Nommez le fichier `TaskbarAcrylicOpacity`. Après avoir créé le fichier, double-cliquez dessus et définissez la **valeur des données** sur 0 (zéro) et cliquez sur OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/value-data.png)

### **Étape 5 - Activer les effets de transparence**

Allez sur le bureau et cliquez avec le bouton droit. Cliquez sur Personnaliser.

Cliquez sur l'onglet "Couleurs", et activez les effets de transparence sur **`On`** :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/personalize.png)

Après cela, vous devriez avoir une barre des tâches transparente.

Si la dernière étape ne fonctionne pas pour vous, passez aux étapes suivantes.

### **Étape 6 - Redémarrer l'Explorateur Windows à l'aide du Gestionnaire des tâches**

Avant d'ouvrir le gestionnaire des tâches, assurez-vous que votre Explorateur de fichiers est déjà en cours d'exécution. Puis suivez ces étapes :

* Cliquez avec le bouton droit sur la barre des tâches.
* Cliquez sur Gestionnaire des tâches.
* Cliquez avec le bouton droit sur Explorateur de fichiers sous Apps.
* Cliquez sur Redémarrer

![Image](https://www.freecodecamp.org/news/content/images/2022/01/restart.png)

Après avoir terminé la dernière étape, vous devriez avoir une barre des tâches complètement transparente.

## Conclusion

Dans ce tutoriel, nous avons rendu notre barre des tâches transparente sans installer de logiciel dans Windows 10. J'espère que cela fonctionne pour vous.

Merci d'avoir lu !