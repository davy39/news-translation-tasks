---
title: Qu'est-ce que dllhost.exe et COM Surrogate dans le Gestionnaire des tâches
  Windows ? (Résolu)
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2020-05-12T16:14:45.000Z'
originalURL: https://freecodecamp.org/news/what-is-dllhost-exe-and-com-surrogate-in-windows-task-manager-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b18740569d1a4ca29a4.jpg
tags:
- name: error handling
  slug: error-handling
- name: Windows
  slug: windows
seo_title: Qu'est-ce que dllhost.exe et COM Surrogate dans le Gestionnaire des tâches
  Windows ? (Résolu)
seo_desc: COM Surrogate processes, short for Component Object Model, are necessary
  components in Windows. They are used to run software extensions that other programs
  need to run. And if those extensions crash, it is the surrogate processes that are
  affected a...
---

Les processus COM Surrogate, abréviation de **Component Object Model**, sont des composants nécessaires dans Windows. Ils sont utilisés pour exécuter des extensions logicielles dont d'autres programmes ont besoin pour fonctionner. Et si ces extensions plantent, ce sont les processus surrogates qui sont affectés et non les programmes qui les exécutaient.

Il existe de nombreux cas d'utilisation de ces processus, par exemple la création de miniatures d'images et d'autres fichiers lorsqu'un dossier est ouvert. Le processus COM Surrogate héberge les fichiers .dll, donc son nom est dllhost.exe.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-172.png)
_Photo par [Unsplash](https://unsplash.com/@christinhumephoto?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Christin Hume</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## **COM Surrogate est-il un virus ?**

La réponse courte est non. Les processus COM Surrogate en eux-mêmes ne peuvent pas être des virus. Cependant, des virus et des logiciels malveillants peuvent se déguiser en processus COM Surrogate.

## Dois-je supprimer COM Surrogate ?

Puisqu'il s'agit d'une partie intégrée de Windows, je ne vous conseillerais pas de le supprimer. Ce processus conteneur permet à votre système d'exploitation d'exécuter des objets COM qui aident d'autres processus et programmes à fonctionner.

## Vérification de la légitimité de COM Surrogate

Puisque ces processus sont des composants authentiques de Windows, ils sont largement utilisés par les cybercriminels. Cela a des conséquences – comme une consommation élevée du CPU par COM Surrogate et la création de doublons dans le Gestionnaire des tâches.

Une méthode simple pour vérifier sa légitimité est :

1. Ouvrez le Gestionnaire des tâches Windows en **cliquant avec le bouton droit** sur la barre des tâches et en cliquant sur Gestionnaire des tâches.
2. Trouvez les processus COM Surrogate, puis cliquez avec le bouton droit pour **Ouvrir l'emplacement du fichier**.
3. Les processus sont légitimes s'ils sont situés dans **C:/Windows\System32** ou **C:/winnt/system32**.

## Erreurs courantes

1. **COM Surrogate utilise beaucoup de CPU, de disque**
2. **COM Surrogate ne répond pas, se fige**
3. **Virus COM Surrogate**
4. **COM Surrogate utilise de la mémoire**
5. **COM Surrogate est toujours en cours d'exécution**
6. **COM Surrogate a cessé de fonctionner**
7. **COM Surrogate continue de planter, de s'ouvrir**

Il existe de nombreuses raisons pour que ces erreurs se produisent. Les plus courantes sont :

1. Un programme tiers a incorrectement enregistré des objets COM ou ils n'ont pas fonctionné correctement (s'ils étaient incompatibles avec les versions actuelles de Windows, logiciels obsolètes).
2. Si le problème se produit lors de la génération de miniatures dans l'Explorateur, c'est à cause de codecs obsolètes ou fonctionnant incorrectement.
3. Peut être causé par des virus ou des logiciels malveillants, ainsi que par des dommages aux fichiers système Windows.

## Comment pouvez-vous corriger ces erreurs ?

Nous avons discuté de nombreuses erreurs ci-dessus, mais la plus courante d'entre elles est « **COM Surrogate a cessé de fonctionner** ». Voici les différentes méthodes pour la résoudre.

Et même si vous rencontrez l'une des autres erreurs listées ci-dessus, ces méthodes sont bonnes à suivre et devraient aider à les corriger également.

### 1. Mettre à jour les Codecs

Une méthode manuelle pour résoudre cette erreur consiste à mettre à jour tous les **Codecs** de Windows (7, 8 ou 10) vers leurs dernières versions mises à jour. Vous pouvez télécharger et installer votre dernier **Windows Codec Pack** depuis ici :

[https://www.microsoft.com/en-in/download/details.aspx?id=507](https://www.microsoft.com/en-in/download/details.aspx?id=507)

**Windows 7 Codec Pack :** [https://www.windows7codecs.com/](https://www.windows7codecs.com/)

**Windows 8 & 10 Codec Pack :** [http://www.windows8codecs.com/](https://www.windows8codecs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-68.png)
_Installation des Codecs_

### **2. Réinitialiser Internet Explorer**

Le problème peut également être causé par des fichiers cache corrompus. Dans ce cas, il est préférable de réinitialiser IE.

1. Maintenez la **touche Windows** enfoncée et appuyez sur **R**. Dans la boîte de dialogue Exécuter, tapez **inetcpl.cpl** et cliquez sur **OK**. Allez dans l'onglet Avancé et choisissez Réinitialiser.
2. Sélectionnez **Supprimer les paramètres personnels** et cliquez à nouveau sur le bouton Réinitialiser. Une fois que vous avez tout fait, redémarrez votre PC et testez-le.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-69.png)
_Réinitialisation d'Internet Explorer_

### 3. Vérifier le disque pour les erreurs

Si cette erreur se produit lors de l'ouverture de fichiers enregistrés dans un **LECTEUR** autre que C:\, vous devez vérifier ce lecteur pour les erreurs. Si vous n'avez pas de lecteurs supplémentaires, vérifiez simplement le lecteur C:\.

1. Maintenez la **touche Windows** enfoncée et appuyez sur **E**. Sur **Windows 7/Vista**, vous verrez les lecteurs listés.
2. Sur Windows 8/10, choisissez **Ce PC** dans le volet de gauche pour voir les lecteurs. **Cliquez avec le bouton droit** sur le **disque dur** sélectionné que vous souhaitez vérifier, puis sélectionnez « **Propriétés** ».

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-67.png)
_Vérification du disque pour les erreurs_

3. Cliquez sur l'onglet **Outils** en haut, puis cliquez sur **Vérifier maintenant** sous **Vérification des erreurs**. Cochez les deux **Options**, puis cliquez sur **Démarrer**.

### 4. Réenregistrer les DLL

1. Exécutez les commandes suivantes dans une invite de commande élevée. Cliquez sur Démarrer, tapez **cmd**, puis cliquez avec le bouton droit sur le programme « **cmd** » dans les résultats de recherche. Sélectionnez ensuite **Exécuter en tant qu'administrateur**.

![cmd-run-as-administrator](https://cdn.appuals.com/wp-content/uploads/2014/11/cmd-run-as-administrator.png)
_Exécution de cmd en tant qu'administrateur_

2. Dans la fenêtre **Invite de commande**, tapez les commandes suivantes et appuyez sur la **touche Entrée** une par une :

```
regsvr32 vbscript.dll
regsvr32 jscript.dll
```

![2015-12-03_002655](https://cdn.appuals.com/wp-content/uploads/2015/12/2015-12-03_002655.png)
_Réenregistrement des DLL_

### 5. Revenir à la version précédente du pilote de l'adaptateur d'affichage

1. Pour ce faire, maintenez la **touche Windows** enfoncée et appuyez sur **R**. Dans la boîte de dialogue Exécuter, tapez **hdwwiz.cpl** et cliquez sur **OK**.
2. Faites défiler jusqu'à la section **Adaptateurs d'affichage** dans le Gestionnaire de périphériques. Cliquez avec le bouton droit dessus et sélectionnez Propriétés.
3. Cliquez sur **Revenir au pilote précédent** et suivez les instructions à l'écran.

Dans certains cas, cette option est grisée. Si c'est le cas, essayez les méthodes ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-72.png)
_Adaptateur d'affichage_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-71.png)
_Revenir au pilote précédent_

### **6. Ajouter dllhost.exe à l'exception DEP (Data Execution Prevention)**

Allez dans Démarrer > Panneau de configuration > Système > Paramètres système avancés > Paramètres de performance > Prévention de l'exécution des données.

1. Sélectionnez **« Activer la DEP pour tous les programmes et services sauf ceux que je sélectionne : »**
2. Cliquez sur **« Ajouter »** et accédez à **C:\Windows\System32\dllhost.exe sur une machine 32 bits** et sur une **machine 64 bits, ajoutez **C:\Windows\SysWOW64\dllhost.exe**
3. Après avoir ajouté **dllhost.exe** à la liste d'exceptions, **Appliquez les modifications** ou cliquez sur **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-73.png)
_Prévention de l'exécution des données_

### 7. Passer à la vue Liste ou Détails / désactiver les miniatures

Nous avons déjà discuté du fait que **COM Surrogate** est responsable de vos miniatures. Pour éviter les problèmes avec lui, vous pouvez désactiver les miniatures.

De plus, vous pouvez passer à la vue **Liste** ou **Détails** en procédant comme suit :

1. Ouvrez l'**Explorateur de fichiers**.
2. Cliquez sur l'onglet **Affichage** et choisissez l'option **Liste** ou **Détails**.

### 8. Mettre à jour votre antivirus

Il a été signalé que certains logiciels antivirus, comme Kaspersky antivirus, peuvent parfois causer des problèmes avec le processus **COM Surrogate**.

Pour corriger ces problèmes, vous devez installer la dernière version de votre logiciel antivirus actuel.

---

_Merci d'avoir lu cet article. J'espère qu'il vous aidera à corriger vos erreurs COM Surrogate._