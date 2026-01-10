---
title: Discord ne s'ouvre pas sur mon PC [Résolu sous Windows 10]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-09T14:57:04.000Z'
originalURL: https://freecodecamp.org/news/discord-wont-open-on-my-pc-solved-in-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Discord.png
tags:
- name: Chat
  slug: chat
- name: discord
  slug: discord
- name: how-to
  slug: how-to
- name: Problem Solving
  slug: problem-solving
seo_title: Discord ne s'ouvre pas sur mon PC [Résolu sous Windows 10]
seo_desc: "Discord is an instant messaging app you can use to communicate through\
  \ text messages, voice calls, and video calls. You can also use it to share files.\
  \ \nDiscord was originally created for gamers, but many other people now use it\
  \ these days. It has be..."
---

Discord est une application de messagerie instantanée que vous pouvez utiliser pour communiquer via des messages texte, des appels vocaux et des appels vidéo. Vous pouvez également l'utiliser pour partager des fichiers. 

Discord a été initialement créé pour les joueurs, mais de nombreuses autres personnes l'utilisent aujourd'hui. Il est devenu une alternative à Slack pour de nombreux utilisateurs – surtout pour ceux qui souhaitent avoir une communauté en ligne.

Mais parfois, Discord peut ne pas s'ouvrir lorsque vous le lancez. Cela peut être dû à des mises à jour en attente, à des jeux en cours d'exécution et à d'autres causes.
 
Dans cet article, je vais vous montrer 5 façons rapides de faire en sorte que Discord s'ouvre à nouveau sur un ordinateur Windows 10.

## Table des matières
- [Comment réparer Discord qui ne s'ouvre pas dans l'invite de commande](#heading-comment-reparer-discord-qui-ne-souvre-pas-dans-linvite-de-commande)
- [Comment réparer Discord qui ne s'ouvre pas en effaçant AppData](#heading-comment-reparer-discord-qui-ne-souvre-pas-en-effacant-appdata)
- [Comment réparer Discord qui ne s'ouvre pas en effaçant LocalAppData](#heading-comment-reparer-discord-qui-ne-souvre-pas-en-effacant-localappdata)
- [Comment réparer Discord qui ne s'ouvre pas en fermant les applications en arrière-plan](#heading-comment-reparer-discord-qui-ne-souvre-pas-en-fermant-les-applications-en-arriere-plan)
- [Comment réparer Discord qui ne s'ouvre pas avec le Gestionnaire des tâches](#heading-comment-reparer-discord-qui-ne-souvre-pas-avec-le-gestionnaire-des-taches)
- [Conclusion](#heading-conclusion)

## Comment réparer Discord qui ne s'ouvre pas dans l'invite de commande

La première solution que je recommande pour faire en sorte que Discord s'ouvre à nouveau est de terminer la tâche Discord avec l'invite de commande.

Voici comment faire :

**Étape 1** : Cliquez sur Démarrer ou appuyez sur `WIN` (touche Windows) de votre clavier, puis recherchez "cmd".

**Étape 2** : Appuyez sur `ENTRÉE` ou sélectionnez le premier résultat de recherche pour ouvrir l'invite de commande.

![ss-1-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-5.jpg)

**Étape** : Tapez `taskkill /F /IM discord.exe` et appuyez sur `ENTRÉE`.

Vous devriez recevoir un message indiquant que le processus Discord a été terminé.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-2-1.png)


## Comment réparer Discord qui ne s'ouvre pas en effaçant AppData

Lorsque vous effacez les AppData d'une application, tous les fichiers cache sont effacés – ce qui peut résoudre certains problèmes, y compris le chargement.

Suivez les étapes suivantes pour effacer les AppData de Discord :

**Étape 1** : Appuyez sur `WIN` (touche Windows) + R pour ouvrir la boîte de dialogue Exécuter.

**Étape 2** : Tapez "%appdata%" (sans les guillemets) et appuyez sur `ENTRÉE` de votre clavier. Cela ouvrira le dossier AppData.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-3-1.png)

**Étape 3** : Localisez le dossier Discord et supprimez-le. Supprimez-le également de votre Corbeille.
![ss-4-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-6.jpg)

## Comment réparer Discord qui ne s'ouvre pas en effaçant LocalAppData

Effacer les LocalAppData de Discord peut le faire s'ouvrir à nouveau. Cela peut également résoudre l'erreur JavaScript courante associée à Discord.

Pour effacer LocalAppData, suivez ces étapes :

**Étape 1** : Appuyez sur `WIN` (touche Windows) + R pour ouvrir la boîte de dialogue Exécuter.

**Étape 2** : Tapez "%localappdata%" (sans les guillemets) et appuyez sur `ENTRÉE` de votre clavier. Cela ouvrira le dossier LocalAppData.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-5.png)

**Étape 3** : Recherchez le dossier Discord et supprimez-le. Allez dans votre Corbeille et supprimez-le également.
![ss-6-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-5.jpg)

Notez que vous devrez peut-être réinstaller Discord pour le faire fonctionner à nouveau après avoir effacé ses LocalAppData. Je peux attester que cela résout le problème, car j'ai récemment dû le faire.

## Comment réparer Discord qui ne s'ouvre pas en fermant les applications en arrière-plan

Beaucoup de jeux s'exécutent en arrière-plan et cela peut avoir un effet négatif sur votre application Discord.

Utilisez les étapes ci-dessous pour résoudre le problème uniquement si vous n'avez pas d'applications utiles en cours d'exécution en arrière-plan.

**Étape 1** : Cliquez sur Démarrer ou appuyez sur `WIN` (touche Windows) de votre clavier et sélectionnez Paramètres.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-1.jpg)

**Étape 2** : Sélectionnez "Confidentialité".
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-8-2.jpg)

**Étape 3** : Cliquez sur Applications en arrière-plan à gauche, puis désactivez le bouton sous "Autoriser les applications à s'exécuter en arrière-plan".
![ss-9-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-9-1.jpg)

## Comment réparer Discord qui ne s'ouvre pas avec le Gestionnaire des tâches

Arrêter le processus Discord avec le Gestionnaire des tâches peut faire en sorte que Discord s'ouvre à nouveau, car cela rafraîchit l'application.

**Étape 1** : Appuyez sur `CTRL` + `SHIFT` + `ÉCHAP` pour ouvrir le Gestionnaire des tâches.

**Étape 2** : Assurez-vous d'être sous l'onglet `Processus`. Faites un clic droit sur Discord et sélectionnez "Fin de tâche". 
![ss-10-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-10-2.jpg)

## Conclusion

Dans cet article, vous avez appris comment réparer Discord lorsqu'il ne s'ouvre pas de plusieurs manières différentes.

En plus des méthodes discutées dans ce guide, vous pouvez également résoudre le problème en désinstallant et en réinstallant Discord. 

Notez que vous pouvez également résoudre un autre problème courant avec Discord – l'erreur JavaScript – en utilisant l'une des solutions suggérées dans cet article – effacer LocalAppData. J'ai dû le faire moi-même.

Merci beaucoup d'avoir lu. Si vous trouvez cet article utile, envisagez de le partager avec vos amis. Cela est grandement apprécié.