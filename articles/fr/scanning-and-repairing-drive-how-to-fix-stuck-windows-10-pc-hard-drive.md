---
title: Analyse et réparation du disque – Comment réparer un disque dur de PC Windows
  10 bloqué
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-22T17:10:42.000Z'
originalURL: https://freecodecamp.org/news/scanning-and-repairing-drive-how-to-fix-stuck-windows-10-pc-hard-drive
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/hard-drive-ga71e91ab5_1280.jpg
tags:
- name: error
  slug: error
- name: how-to
  slug: how-to
- name: Windows 10
  slug: windows-10
seo_title: Analyse et réparation du disque – Comment réparer un disque dur de PC Windows
  10 bloqué
seo_desc: 'If you have a Windows 10 PC, you might occasionally see the notorious "scanning
  and repairing drive" message. This error can happen to the C drive, hard drive,
  and any other external drive.

  This scanning and repairing can take several hours, or even ...'
---

Si vous avez un PC Windows 10, vous pouvez parfois voir le message notoire "analyse et réparation du disque". Cette erreur peut survenir sur le disque C, le disque dur et tout autre disque externe.

Cette analyse et réparation peuvent prendre plusieurs heures, voire vous coûter une journée entière de travail (comme je peux en témoigner moi-même). Elle est généralement causée par un arrêt incorrect – arrêt forcé, panne de courant, retrait soudain de la batterie, pilotes mal configurés, logiciels malveillants ou autres attaques de virus.

Dans ce guide, je vais vous montrer 3 façons de réparer un disque qui reste bloqué en analyse et réparation sur Windows 10. La première solution fonctionne en mode normal – si vous êtes en mesure de démarrer votre ordinateur – tandis que la deuxième et la troisième nécessitent de démarrer votre ordinateur en mode sans échec.

## Comment réparer un disque bloqué en analyse et réparation à l'aide de l'outil de vérification des erreurs Windows

**Étape 1** : Lancez l'Explorateur de fichiers Windows 10 et cliquez sur "Ce PC".
![ss-1-11](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-11.jpg)

**Étape 2** : Faites un clic droit sur le disque dur que Windows analyse et répare, puis sélectionnez Propriétés. Le disque dur peut être disponible en tant que F, E, ou toute autre lettre de lecteur que vous avez définie.
![ss-2-9](https://www.freecodecamp.org/news/content/images/2021/11/ss-2-9.jpg)

**Étape 3** : Cliquez sur l'onglet Outils et sélectionnez "Vérifier" sous "Vérification des erreurs".
![ss-3-10](https://www.freecodecamp.org/news/content/images/2021/11/ss-3-10.jpg)

**Étape 4** : Si une erreur est détectée sur le disque dur, vous serez invité à réparer le disque.

Si aucune erreur n'est détectée sur le disque dur, vous pouvez choisir de ne pas l'analyser.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-1.png)

## Comment réparer un disque bloqué en analyse et réparation avec Windows PowerShell

Pour utiliser cette solution, vous devez démarrer votre ordinateur Windows 10 en mode sans échec.

**Suivez les étapes ci-dessous pour démarrer votre ordinateur en mode sans échec** :

**Étape 1** : Sur l'écran de connexion de votre ordinateur, appuyez et maintenez `SHIFT`, sélectionnez Alimentation, puis Redémarrer.

**Étape 2** : Sélectionnez "Dépannage" dans l'écran "Choisir une option".
![85d63652-68b6-9a70-60e4-c63825eaca59](https://www.freecodecamp.org/news/content/images/2021/11/85d63652-68b6-9a70-60e4-c63825eaca59.png)

**Étape 3** : Sélectionnez "Options avancées".
![f4fde1b8-7b3d-ac4e-6d6c-5339925fb04c](https://www.freecodecamp.org/news/content/images/2021/11/f4fde1b8-7b3d-ac4e-6d6c-5339925fb04c.png)

**Étape 4** : Sélectionnez "Paramètres de démarrage".
![b6f591d9-227c-8ef1-80bc-5139e82b62ac](https://www.freecodecamp.org/news/content/images/2021/11/b6f591d9-227c-8ef1-80bc-5139e82b62ac.png)

**Étape 5** : Cliquez sur "Redémarrer".
![91786ae5-8514-50ac-fb43-9d13c005bc22](https://www.freecodecamp.org/news/content/images/2021/11/91786ae5-8514-50ac-fb43-9d13c005bc22.png)

**Étape 6** : Lorsque votre ordinateur redémarre, appuyez sur `4` ou `F4` pour enfin démarrer votre ordinateur en mode sans échec.

Pour réparer un disque bloqué en analyse et réparation avec PowerShell, suivez les étapes ci-dessous :

**Étape 1** : Cliquez sur Démarrer et recherchez "powershell".

**Étape 2** : Vous devez exécuter PowerShell en tant qu'administrateur, alors sélectionnez "Exécuter en tant qu'administrateur" à droite.
![ss-5-9](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-9.jpg)

**Étape 3** : Tapez la commande `repair-volume -driveletter x` et appuyez sur `ENTRÉE` sur votre clavier. Assurez-vous de remplacer "x" par la lettre de votre disque dur.
![ss-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-6.png)

**Étape 4** : Redémarrez votre PC.

## Comment réparer un disque bloqué en analyse et réparation avec l'invite de commandes

**Étape 1** : Démarrez votre ordinateur en mode sans échec. Reportez-vous à la dernière solution ci-dessus pour savoir comment faire.

**Étape 2** : Cliquez sur Démarrer et recherchez "cmd", puis appuyez sur `ENTRÉE`.
![ss-7-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-6.jpg)

**Étape 3** : Tapez la commande `chkdsk x: /f` et appuyez sur `ENTRÉE`. Remplacez x par la lettre de votre disque dur.
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-8-2.png)

**Étape 4** : Redémarrez votre PC.

## Conclusion

Dans ce guide détaillé, vous avez appris comment réparer un disque dur bloqué en analyse et réparation.

Les solutions discutées dans cet article s'appliquent également à tout autre disque – y compris le disque C.

En dernier recours pour résoudre ce problème, vous pouvez sauvegarder vos données et restaurer votre ordinateur.

Merci d'avoir lu.