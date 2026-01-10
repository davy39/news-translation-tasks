---
title: Qu'est-ce que le RTLO dans le piratage ? Comment utiliser le remplacement de
  droite à gauche et se défendre contre celui-ci
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2023-02-28T00:36:36.000Z'
originalURL: https://freecodecamp.org/news/rtlo-in-hacking
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/image-249-1.png
tags:
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Qu'est-ce que le RTLO dans le piratage ? Comment utiliser le remplacement
  de droite à gauche et se défendre contre celui-ci
seo_desc: 'Let’s play a lovely game of hide your malware in plain sight. 🐴

  Malicious hackers look for all kinds of underhanded tricks to make everyday users
  victims as a result of common mistakes. They might get someone to click the wrong
  link, open the wrong ...'
---

Jouons à un jeu charmant de cache-cache avec votre malware en pleine vue. 🐵

Les pirates malveillants recherchent toutes sortes de trucs malhonnêtes pour faire des utilisateurs quotidiens des victimes à la suite d'erreurs courantes. Ils peuvent amener quelqu'un à cliquer sur le mauvais lien, ouvrir le mauvais site web ou exécuter le mauvais programme.

La plupart du temps, il est facile d'identifier un fichier suspect par les éléments suivants :

1. L'icône ne correspond pas au nom
2. L'extension semble incorrecte
3. Le fichier est sensiblement plus grand ou plus petit que son type de fichier proposé (Imaginez une image de 50 Mo 🤯)

Mais seriez-vous suspicieux face à un fichier comme celui-ci ?

![image-248](https://www.freecodecamp.org/news/content/images/2023/02/image-248.png)
_Un fichier totalement non suspect | Crédit : Mercury_

Rien d'extraordinaire, n'est-ce pas ? Cela ressemble à votre document Word moyen. Examinons de plus près.

![image-250](https://www.freecodecamp.org/news/content/images/2023/02/image-250.png)
_Propriétés du fichier | Crédit : Mercury_

Dans ce tutoriel, vous apprendrez :

1. Ce qu'est le remplacement de droite à gauche (Right-To-Left Override)
2. Comment l'utiliser pour masquer les extensions de fichiers
3. Comment détecter si elle a été utilisée sur un fichier
4. Les mesures d'atténuation

**Avertissement amical** : Ceci est uniquement à des fins éducatives et est écrit uniquement pour protéger les individus, les entreprises et les organisations contre les acteurs de menaces. Si vous souhaitez toujours l'utiliser d'une autre manière, c'est votre choix... mais préparez-vous pour un joli voyage en prison... pendant très longtemps. 🤴

Et avec cette introduction, plongeons-nous dans le sujet 🤓

## **Qu'est-ce que le remplacement de droite à gauche (Right-To-Left Override) ?**

![image-252](https://www.freecodecamp.org/news/content/images/2023/02/image-252.png)
_Quand rien ne va à droite, allez à gauche | Crédit : [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Le remplacement de droite à gauche (RTO ou RTLO) est un caractère Unicode non imprimable utilisé pour écrire des langues lues de droite à gauche. Il prend l'entrée et inverse littéralement le texte dans l'autre sens. De telles langues incluent l'hébreu, l'arabe, l'araméen et l'ourdou.

Vous pouvez trouver le caractère dans la table des caractères sous Windows et Linux en utilisant le code [202E].

![image-253](https://www.freecodecamp.org/news/content/images/2023/02/image-253.png)
_Table des caractères | Crédit : Mercury_

Voici une démonstration de son utilisation :

![image-254](https://www.freecodecamp.org/news/content/images/2023/02/4.2---RTLO-demonstration.gif)
_Démonstration du RTLO | Crédit : Mercury_

Comme vous pouvez le voir, les deux déclarations tapées sont exactement la même chose, sauf que celle du bas est écrite à l'envers parce que le caractère RTLO a été inséré avant de la taper.

## **Comment le RTLO peut être un outil malveillant**

Peut-être qu'à première vue, ce caractère semble inoffensif. Quel est le mal à inverser du texte de toute façon ? La réponse : les extensions de fichiers.

![image-255](https://www.freecodecamp.org/news/content/images/2023/02/image-255.png)
_Un installeur Chrome en tant qu'installeur et document Word | Crédit : Mercury_

Voici quelques piratages réalisés dans le passé en utilisant cette technique :

1. **Telegram** : En 2018, Kaspersky a rapporté dans [un article de blog sur Securelist](https://securelist.com/zero-day-vulnerability-in-telegram/83800/) que des cybercriminels russes exploitaient des failles RTLO dans la nature sur les clients Windows de Telegram. Comme démontré dans l'article, cela permettait aux criminels d'installer des cryptomineurs ou des RATs lorsqu'un utilisateur ouvrait ce qui semblait être un fichier inoffensif ⛔.
2. **Scarlet Mimic** : En 2016, Unit 42 de Palo Alto Networks a publié un rapport sur les tactiques d'un groupe de menace connu sous le nom de Scarlet Mimic. Le groupe est communément connu pour cibler des activistes minoritaires. Selon [le rapport](https://unit42.paloaltonetworks.com/scarlet-mimic-years-long-espionage-targets-minority-activists/), l'une des tactiques courantes du groupe comprenait l'utilisation de caractères RTLO pour masquer les extensions de fichiers réelles des archives auto-extractibles (SFX/SEA)🏭.
3. **Applications de messagerie célèbres** : En 2022, Bleeping Computer a publié un [article de presse](https://www.bleepingcomputer.com/news/security/url-rendering-trick-enabled-whatsapp-signal-imessage-phishing/) sur les techniques de phishing sur les plateformes de messagerie et de courrier électronique utilisant le RTLO. Des plateformes telles que iMessage, WhatsApp, Signal et Facebook Messenger (je me demande qui utilise la dernière 😨) étaient vulnérables à de telles tactiques. Cela permettait à un attaquant d'injecter un caractère RTLO entre deux liens. À gauche se trouvait un domaine légitime tel que ([google.com](http://google.com/)) et à droite un domaine malveillant. Cela faisait apparaître un seul lien et si un utilisateur cliquait sur le côté gauche, il était en sécurité. Cependant, s'il cliquait sur le côté droit, il ne l'était pas.
4. **PLEAD** : En 2017, Trend Micro a publié [un article](https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html) sur trois campagnes menées par un groupe de menace connu sous le nom de BlackTech. L'une de ces campagnes s'appelait PLEAD, qui se concentrait sur le vol d'informations et ciblait le gouvernement et les organisations taïwanais. Selon l'article, des e-mails de harponnage étaient utilisés pour livrer et installer une porte dérobée. La partie notable de cette attaque était que les installeurs étaient déguisés en documents utilisant des caractères RTLO et des documents leurres étaient également ajoutés pour tromper les utilisateurs 📄.
5. **OS X d'Apple** : Malgré sa fréquence sous Windows, cette technique pourrait être utilisée pour cibler les utilisateurs de Mac. En 2013, [un article de blog](https://archive.f-secure.com/weblog/archives/00002576.html) de F-Secure Labs a révélé que le RTLO était utilisé pour déguiser un malware Mac relativement bénin dans la nature. Cependant, le malware crie « Je suis un virus ! » en raison du fait que OS X montre l'extension de fichier réelle et lorsque le fichier est exécuté, la notification de quarantaine du fichier est écrite à l'envers (Belle trouvaille Apple 😉🍎).

## **Comment masquer un fichier potentiellement malveillant**

![image-256](https://www.freecodecamp.org/news/content/images/2023/02/image-256.png)
_Un masque de Guy Fawkes | Crédit : [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Le RTLO peut être utilisé dans toute attaque qui exploite la tromperie de l'utilisateur concernant le texte écrit. Comme nous l'avons vu dans les piratages ci-dessus, les liens, les pièces jointes des e-mails et les scripts et fichiers exécutables sont les vecteurs d'attaque les plus courants.

Mais ce tutoriel se concentrera sur les fichiers hébergés localement car cela donne l'idée de base et ses variations peuvent être utilisées pour mener d'autres attaques.

Il y a deux étapes dans le processus :

1. Insérer le caractère RTLO dans le nom du fichier
2. Changer l'icône du fichier

L'icône du fichier doit être changée pour imiter la fausse extension afin de faciliter la tromperie de l'utilisateur.

Voici les prérequis pour la procédure :

1. Un exécutable ou un script – La charge utile
2. Une icône de fichier – Partie de l'appât
3. Resource Hacker – Pour changer l'icône du fichier

L'icône du fichier peut être au format .exe, .dll, .res ou .ico. Vous pouvez en télécharger certaines [ici](https://icon-icons.com/). Et maintenant, que le chaos commence ⚠.

### **Étape 1 – Insérer le caractère RTLO**

Choisissez un fichier de votre choix et ouvrez-le dans l'Explorateur Windows. Ouvrez l'application Carte des caractères sur Windows et cochez la case « Vue avancée ». Dans l'option « Aller à Unicode », tapez 202E. Cliquez respectivement sur les boutons « Sélectionner » et « Copier » et allez au fichier que vous souhaitez modifier.

![image-257](https://www.freecodecamp.org/news/content/images/2023/02/6---RTLO-demonstration.gif)
_Sélection du caractère de remplacement de droite à gauche | Crédit : Mercury_

Voici la partie délicate 🎃. Lorsque vous tapez avec le caractère RTLO, il tape de droite à gauche. Cela peut être déroutant lorsque vous essayez de renommer le fichier. Si vous souhaitez renommer un fichier après avoir injecté le caractère, épellez-le à l'envers.

Par exemple, si vous souhaitez écrire l'extension « .pdf », vous devez la taper comme « fdp. ». Cela prend un peu de temps pour s'y habituer, mais c'est facile après quelques essais.

![image-258](https://www.freecodecamp.org/news/content/images/2023/02/7---RTLO-demonstration.gif)
_Démonstration de renommage courte | Crédit : Mercury_

Dans l'Explorateur de fichiers, cochez l'option pour afficher les extensions de fichiers. Allez au fichier, faites un clic droit et cliquez sur renommer. Changez le nom en ce que vous voulez, mais assurez-vous de ne jamais éditer l'extension elle-même pour que le fichier fonctionne comme prévu❗.

Placez le curseur juste avant le nom de l'extension. Collez le caractère RTLO. Vous observerez qu'il semble que rien ne se soit passé, mais c'est ainsi que cela est censé apparaître. Ensuite, tapez « xcod » pour obtenir « docx » et appuyez sur Entrée.

![image-259](https://www.freecodecamp.org/news/content/images/2023/02/8---Gif-of-renaming.gif)
_Renommage du fichier cible | Crédit : Mercury_

### **Étape 2 – Changer l'icône**

Maintenant, pour la partie finale de notre astuce incroyable – changer l'icône 🤖. Téléchargez et installez un logiciel appelé Resource Hacker. Ouvrez-le et appuyez sur Ctrl + O. Ensuite, sélectionnez votre programme cible. Il y a beaucoup d'informations ici que nous pouvons éditer, mais nous voulons simplement nous concentrer sur l'icône.

![image-260](https://www.freecodecamp.org/news/content/images/2023/02/image-260.png)
_Resource Hacker | Crédit : Mercury_

Appuyez sur Ctrl+R pour ouvrir la fenêtre de remplacement et cliquez sur le bouton « Ouvrir le fichier avec la nouvelle icône ».

Dans l'Explorateur, sélectionnez l'icône de fichier que vous souhaitez remplacer sur le programme et cliquez sur le bouton « Remplacer ».

Enfin, appuyez sur Ctrl+S pour enregistrer le fichier. Si vous avez un antivirus, vous voudrez peut-être le désactiver temporairement avant d'enregistrer le fichier.

![image-261](https://www.freecodecamp.org/news/content/images/2023/02/Untitled.gif)
_Utilisation de Resource Hacker pour changer l'icône | Crédit : Mercury_

![image-262](https://www.freecodecamp.org/news/content/images/2023/02/image-262.png)
_Un fichier totalement non suspect | Crédit : Mercury_

Propre, n'est-ce pas ? Regardons comment éviter de tomber dans ce piège.

## **Mesures d'atténuation**

![image-263](https://www.freecodecamp.org/news/content/images/2023/02/image-263.png)
_Sécurité en ligne | Crédit : [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Puisqu'il abuse des fonctionnalités du système, presque n'importe quel utilisateur régulier ou geek technologique tomberait dans ce piège. Alors, comment pouvez-vous l'éviter ? Voici quelques conseils :

### **Ne jamais ouvrir un fichier ou un lien d'origine inconnue**

Ne sous-estimez jamais le pouvoir de l'hygiène cybernétique de base. Ne cliquez pas sur des liens aléatoires ou n'ouvrez pas de fichiers dont vous ne savez pas d'où ils viennent ou qui les a envoyés.

### **Afficher les extensions de fichiers**

Un nom de fichier qui masque son extension est beaucoup plus facilement remarqué comme étant suspect lorsque les extensions de fichiers sont affichées.

Soyez prudent si vous remarquez que juste avant l'extension, le fichier se termine par des extensions de fichiers courantes écrites à l'envers. Par exemple, « infoexe.pdf » sera évident. Cependant, certains sont moins évidents comme « infosbv.png » qui pourrait être un script Visual Basic (.vbs). Un fichier nommé « Samsung_Galaxy_tab.png » pourrait être un fichier batch (.bat).

### **Installer et maintenir à jour un logiciel antivirus**

Au cas où vous seriez tombé dans un tel piège, cela pourrait être votre dernière ligne de défense. Un antivirus approprié prendra note si un script ou un fichier exécutable avec des actions malveillantes a été exécuté et le mettra en quarantaine ou le supprimera.

Je veux dire, un abonnement annuel de 20 $ semble mieux que plus de 200 $ jetés par les égouts pour rien 💰.

### **Appliquer les meilleures pratiques**

Pour les personnes informatiques plus sophistiquées dans les organisations, la mise en œuvre des meilleures pratiques telles que l'analyse du trafic réseau, les pare-feu, l'utilisation de systèmes de détection et de prévention des intrusions et la segmentation du réseau sont votre meilleur atout.

## **Conclusion**

Faisons un résumé de ce que vous avez appris :

1. Comment utiliser les caractères RTLO pour manipuler du texte
2. Comment changer les icônes d'application en utilisant Resource Hacker
3. Comment identifier le texte manipulé avec des caractères RTLO

Au début, il est difficile d'identifier les fichiers modifiés de cette manière. Je vous encourage à jouer avec différents noms et extensions de fichiers et à voir ce que vous obtenez. Cela vous entraînera également à identifier les fichiers qui ne sont pas ce qu'ils semblent être.

Rappelez-vous, **ceci est strictement à des fins éducatives**. Et avec cela, nous sommes arrivés à la fin de cet article. Comme je le dis toujours, Bon Piratage ! 🤓

## **Ressources**

1. [Autres façons de changer une icône d'application](https://www.wikihow.com/Change-the-Icon-for-an-Exe-File)
2. [Plus de façons d'utiliser le RTLO](http://blog.sevagas.com/?Bypass-Defender-and-other-thoughts-on-Unicode-RTLO-attacks)

## **Remerciements**

Merci à [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o?t=4Cv6VR2c2_wK5HLXwbvXCQ&s=09), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisées pour mettre cet article ensemble. Vous m'inspirez tous quotidiennement.

Crédit de l'image de couverture : The Kelpies | Jamie McInall