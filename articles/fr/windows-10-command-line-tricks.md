---
title: 14 astuces de ligne de commande Windows 10 qui vous donnent plus de contrôle
  sur votre PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-16T16:37:46.000Z'
originalURL: https://freecodecamp.org/news/windows-10-command-line-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/cmdtricks.png
tags:
- name: command line
  slug: command-line
- name: Windows 10
  slug: windows-10
seo_title: 14 astuces de ligne de commande Windows 10 qui vous donnent plus de contrôle
  sur votre PC
seo_desc: "Windows 10 has an incredible Graphics User Interface (GUI) that will often\
  \ be enough for you to get things done. \nBut if your inner Oliver Twist wants more,\
  \ then you should start learning about the Command Line. \nWith the command prompt,\
  \ you get acce..."
---

Windows 10 dispose d'une interface graphique (GUI) incroyable qui sera souvent suffisante pour accomplir vos tâches. 

Mais si votre Oliver Twist intérieur en veut plus, alors vous devriez commencer à apprendre la ligne de commande. 

Avec l'invite de commande, vous accédez à des fonctionnalités qui ne sont pas disponibles dans l'interface graphique et vous interagissez directement avec votre système d'exploitation Windows 10.

Dans cet article, je vais vous montrer 14 astuces et conseils de ligne de commande qui vous feront sentir comme un super-héros en utilisant votre ordinateur et qui impressionneront sûrement vos amis.

Soyez conscient que vous devez être très prudent lors de l'exécution de commandes dans l'invite de commande, car toute commande que vous exécutez peut avoir un effet durable sur votre ordinateur.

Assurez-vous de lire jusqu'à la fin car je vais vous montrer comment voir le mot de passe de chaque Wi-Fi qui a déjà été connecté à votre ordinateur.

## Table des matières

- [Comment ouvrir l'invite de commande dans n'importe quel dossier](#heading-1-comment-ouvrir-l-invite-de-commande-dans-n-importe-quel-dossier)
- [Comment créer un dossier sécurisé avec l'invite de commande](#heading-2-comment-creer-un-dossier-secure-avec-l-invite-de-commande)
- [Comment exécuter l'invite de commande en tant qu'administrateur](#heading-3-comment-executer-l-invite-de-commande-en-tant-qu-administrateur)
- [Comment chiffrer des fichiers avec l'invite de commande](#heading-4-comment-chiffrer-des-fichiers-avec-l-invite-de-commande)
- [Comment masquer un dossier avec l'invite de commande](#heading-5-comment-masquer-un-dossier-avec-l-invite-de-commande)
- [Comment changer la couleur de fond et la couleur de police de l'invite de commande](#heading-6-comment-changer-la-couleur-de-fond-et-la-couleur-de-police-de-l-invite-de-commande)
- [Comment changer le titre de la fenêtre de l'invite de commande](#heading-7-comment-changer-le-titre-de-la-fenetre-de-l-invite-de-commande)
- [Comment changer le texte de l'invite de l'invite de commande](#heading-8-comment-changer-le-texte-de-l-invite-de-l-invite-de-commande)
- [Comment changer la taille de police des textes de l'invite de commande](#heading-9-comment-changer-la-taille-de-police-des-textes-de-l-invite-de-commande)
- [Comment générer un rapport sur l'état de la batterie avec l'invite de commande](#heading-10-comment-generer-un-rapport-sur-l-etat-de-la-batterie-avec-l-invite-de-commande)
- [Comment se connecter à un site web depuis l'invite de commande](#heading-11-comment-se-connecter-a-un-site-web-depuis-l-invite-de-commande)
- [Comment vérifier l'adresse IP d'un site web avec l'invite de commande](#heading-12-comment-verifier-l-adresse-ip-d-un-site-web-avec-l-invite-de-commande)
- [Comment afficher tous les mots de passe Wi-Fi avec l'invite de commande](#heading-13-comment-afficher-tous-les-mots-de-passe-wi-fi-avec-l-invite-de-commande)
- [Comment éteindre votre ordinateur avec l'invite de commande](#heading-14-comment-eteindre-votre-ordinateur-avec-l-invite-de-commande)


## 1. Comment ouvrir l'invite de commande dans n'importe quel dossier

Tout le monde ne veut pas se donner la peine de naviguer entre les dossiers dans la ligne de commande.

Si vous êtes l'une de ces personnes comme moi, vous pouvez ouvrir le dossier directement dans l'invite de commande en tapant « cmd » dans la barre d'adresse du dossier et en appuyant sur `ENTRÉE`.
![open-cmd](https://www.freecodecamp.org/news/content/images/2021/12/open-cmd.gif)

Et voilà !

## 2. Comment créer un dossier sécurisé avec l'invite de commande

Pour des raisons de confidentialité, vous pourriez vouloir créer un dossier qui ne peut pas être édité, déplacé, copié ou supprimé par une personne aléatoire qui accède à votre ordinateur.

Pour ce faire, naviguez jusqu'au répertoire où vous souhaitez créer ce dossier ou ouvrez l'invite de commande directement dans celui-ci avec le premier conseil de cet article. Ensuite, exécutez la commande – `md aux\`.
![ss-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1.png)

Cela créera un dossier nommé « aux ». Il ne peut pas être supprimé, édité, déplacé ou copié. 

Si vous vérifiez et que vous ne trouvez pas le dossier, actualisez le répertoire dans lequel vous avez créé le dossier.
![ss-2-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2-2.png)

Alors, que faire si vous voulez supprimer ce dossier ? Vous ne pouvez pas le faire avec l'interface graphique, vous devez donc le faire dans la ligne de commande. Exécutez la commande – `rd aux\` – pour supprimer le dossier. Assurez-vous que les fichiers dans le dossier sont sauvegardés.

## 3. Comment exécuter l'invite de commande en tant qu'administrateur

Parfois, vous pourriez avoir besoin de privilèges administratifs lorsque vous n'avez pas accès à l'interface graphique. 

Pour obtenir ces privilèges, tapez `powershell "start cmd -v runAs` et appuyez sur `ENTRÉE`. Sélectionnez Oui dans la prochaine invite et cela ouvrira une nouvelle fenêtre de l'invite de commande avec des privilèges administratifs.
![ss-3-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-3-2.png)

## 4. Comment chiffrer des fichiers avec l'invite de commande

Si vous n'êtes pas le seul à utiliser votre ordinateur Windows 10 et que vous souhaitez que vos fichiers soient inaccessibles aux autres utilisateurs, vous pouvez chiffrer les fichiers en naviguant jusqu'au dossier où se trouvent les fichiers et en tapant `Cipher /E`.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-4-1.png)

Tout autre utilisateur à part vous ne pourra pas ouvrir les fichiers.

## 5. Comment masquer un dossier avec l'invite de commande

Alors, que faire si vous voulez masquer un dossier ? Vous pouvez le faire en tapant `attrib +h +s +r nom_du_dossier` puis en appuyant sur `ENTRÉE`.

Pour afficher à nouveau le dossier, exécutez la commande – `attrib -h -s -r nom_du_dossier`.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-3.png)

## 6. Comment changer la couleur de fond et la couleur de police de l'invite de commande

Si les couleurs noir et blanc old-school de la ligne de commande vous semblent ennuyeuses, vous pouvez les changer selon votre schéma de couleurs souhaité.

Pour ce faire, lancez l'invite de commande et exécutez `color -help`. Cela vous montrera les couleurs disponibles représentées par des nombres et des lettres. Vous pouvez changer les couleurs de fond et de police.
![ss-7](https://www.freecodecamp.org/news/content/images/2021/12/ss-7.png)

Pour changer les couleurs correctement, exécutez `color numéro_couleur_fond numéro_couleur_police`. Par exemple, `color 02` laisse la couleur de fond noire et change la couleur de la police en vert.

![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-3.png)

## 7. Comment changer le titre de la fenêtre de l'invite de commande

Le titre d'une fenêtre d'invite de commande ouverte n'a pas besoin de rester par défaut – vous pouvez le changer.

Pour ce faire, tapez `title nom_titre_fenêtre`.
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-8-2.jpg)

## 8. Comment changer le texte de l'invite de l'invite de commande

Le texte qui apparaît avant que vous ne tapiez vos commandes peut ne pas être assez attrayant pour vous. Pour moi, ce n'est pas le cas, alors je l'ai changé. 

Pour changer le texte de l'invite, tapez `prompt nom_invite $G` et appuyez sur `ENTRÉE`.
Le « $G » devant le nom de l'invite spécifié ajoutera le symbole supérieur à (>) pour vous, afin que vous sachiez où commence votre commande – une meilleure UX pour vous, par vous !
![ss-9](https://www.freecodecamp.org/news/content/images/2021/12/ss-9.jpg)

## 9. Comment changer la taille de police des textes de l'invite de commande

Si la taille de police par défaut de l'invite de commande est trop petite pour vos yeux, vous pouvez la changer. Vous n'avez même pas besoin d'exécuter une commande pour cela.

**Étape 1** : Faites un clic droit sur la fenêtre de l'invite de commande et sélectionnez « propriétés ».
![ss-10-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-10-1.jpg)

**Étape 2** : Passez à l'onglet police et sélectionnez la taille de police souhaitée, puis cliquez sur « Ok ».
![ss-11-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-11-2.jpg)

## 10. Comment générer un rapport sur l'état de la batterie avec l'invite de commande

Avec cela, vous connaissez l'état de la batterie de votre ordinateur portable et ce qu'il faut faire pour l'améliorer. En fait, c'est ma chose préférée que l'invite de commande me permet de faire. 

Pour générer un rapport sur l'état de la batterie, assurez-vous d'exécuter l'invite de commande en tant qu'administrateur. Ensuite, entrez la commande `powercfg/energy` et appuyez sur `ENTRÉE`.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.png)

Un fichier HTML que vous pouvez ouvrir avec le navigateur sera généré pour vous en 60 secondes. 
Vous pouvez localiser le fichier HTML dans `C:\Windows\system32\energy-report.html`.

## 11. Comment se connecter à un site web depuis l'invite de commande 

Vous pouvez ouvrir un site web depuis l'invite de commande en tapant `start www.nom_du_site.com` puis en appuyant sur `ENTRÉE`. Ensuite, le site web s'ouvrira dans votre navigateur par défaut.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/12/ss-13.png)

![ss-14-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-14-1.png)

Notez que vous devez ajouter « www » avant le nom de domaine, sinon cela ne fonctionne pas.

## 12. Comment vérifier l'adresse IP d'un site web avec l'invite de commande

Vous pouvez vérifier l'adresse IP de n'importe quel site web en tapant `ping www.nom_du_site.com` puis en appuyant sur `ENTRÉE`.
![ss-15](https://www.freecodecamp.org/news/content/images/2021/12/ss-15.png)

Notez que vous devez ajouter « www » avant le nom de domaine, sinon cela ne fonctionne pas.

## 13. Comment afficher tous les mots de passe Wi-Fi avec l'invite de commande

Vous pouvez vérifier le mot de passe de votre connexion Wi-Fi actuelle avec l'interface graphique. Mais l'invite de commande affiche également les mots de passe de chaque Wi-Fi qui a déjà été connecté à votre ordinateur.

Pour vérifier les mots de passe, exécutez la commande – `for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear` et appuyez sur `ENTRÉE`.

Vous pouvez trouver la clé juste devant « Contenu de la clé ».
![ss-16](https://www.freecodecamp.org/news/content/images/2021/12/ss-16.jpg)

J'ai flouté la clé, car certains de mes voisins lisent mes articles freeCodeCamp. :)

## 14. Comment éteindre votre ordinateur avec l'invite de commande

Maintenant que vous avez appris 11 commandes utiles qui vous feront sentir comme un patron, en voici une autre : éteindre ou redémarrer votre ordinateur avec l'invite de commande.

Pour éteindre votre ordinateur avec l'invite de commande, exécutez la commande `shutdown -s`. 
Pour redémarrer votre ordinateur, entrez `shutdown -r` et appuyez sur `ENTRÉE`.

Pour définir un compte à rebours pour l'extinction de votre ordinateur, entrez `shutdown /s /t temps_en_secondes` et appuyez sur `ENTRÉE`.
![ss-17](https://www.freecodecamp.org/news/content/images/2021/12/ss-17.png)

Pour définir un compte à rebours et un message d'alerte pour l'extinction de votre ordinateur, entrez `shutdown /s /t temps_en_secondes /c "message_d'alerte"` et appuyez sur `ENTRÉE`.
![ss-18](https://www.freecodecamp.org/news/content/images/2021/12/ss-18.png)

Merci d'avoir lu cet article. Si vous le trouvez utile, veuillez le partager avec vos amis et votre famille.