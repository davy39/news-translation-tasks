---
title: Commandes en Ligne de Commande – Tutoriel CLI
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-09T15:28:14.000Z'
originalURL: https://freecodecamp.org/news/command-line-commands-cli-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cli.png
tags:
- name: command line
  slug: command-line
- name: Windows
  slug: windows
seo_title: Commandes en Ligne de Commande – Tutoriel CLI
seo_desc: 'The Windows command line is one of the most powerful utilities on a Windows
  PC. With it, you can interact with the OS directly and do a lot of things not available
  in the graphical user interface (GUI).

  In this article, I’ll show you 40 commands you ...'
---

L'invite de commande Windows est l'un des utilitaires les plus puissants sur un PC Windows. Avec celui-ci, vous pouvez interagir directement avec le système d'exploitation et faire beaucoup de choses non disponibles dans l'interface graphique (GUI).

Dans cet article, je vais vous montrer 40 commandes que vous pouvez utiliser sur l'invite de commande Windows qui peuvent renforcer votre confiance en tant qu'utilisateur Windows.

**N.B.** : Vous devez être prudent lors de l'utilisation des commandes que je vais vous montrer. Cela est dû au fait que certaines commandes peuvent avoir un effet négatif ou positif durable sur votre PC Windows jusqu'à ce que vous le réinitialisiez.

De plus, certaines de ces commandes nécessitent que vous ouvriez l'invite de commande en tant qu'administrateur.
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/08/ss5-1.png)


## Commandes de Ligne de Commande Windows

### ` powershell start cmd -v runAs` – Exécuter l'Invite de Commande en tant qu'Administrateur

Entrer cette commande ouvre une autre fenêtre d'invite de commande en tant qu'administrateur :
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/08/ss1-1.png)


### `driverquery` – Liste Tous les Pilotes Installés

Il est important d'avoir accès à tous les pilotes car ils causent souvent des problèmes. 

C'est ce que fait cette commande – elle vous montre même les pilotes que vous ne trouverez pas dans le gestionnaire de périphériques.
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/08/ss2-1.png)


### `chdir` ou `cd` – Change le Répertoire de Travail Actuel vers le Répertoire Spécifié
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/08/ss3-1.png)


### `systeminfo` – Affiche les Détails de Votre PC

Si vous voulez voir des informations plus détaillées sur votre système que vous ne verrez pas dans l'interface graphique, cette commande est faite pour vous.
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/08/ss4-1.png)


### `set` – Affiche les Variables d'Environnement de Votre PC

![ss5-2](https://www.freecodecamp.org/news/content/images/2022/08/ss5-2.png)


### `prompt` – Change le Texte par Défaut Affiché avant d'Entrez les Commandes

Par défaut, l'invite de commande montre le chemin du lecteur C vers votre compte utilisateur. 

Vous pouvez utiliser la commande `prompt` pour changer ce texte par défaut avec la syntaxe `prompt nom_de_l_invite $G` :
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/08/ss6-1.png)

**N.B** : Si vous n'ajoutez pas `$G` à la commande, vous n'aurez pas le symbole supérieur à devant le texte.


### `clip` – Copie un Élément dans le Presse-papiers
Par exemple, `dir | clip` copie tout le contenu du répertoire de travail actuel dans le presse-papiers.
![ss7](https://www.freecodecamp.org/news/content/images/2022/08/ss7.png)

Vous pouvez taper `clip /?` et appuyer sur `ENTRÉE` pour voir comment l'utiliser.


### `assoc` – Liste les Programmes et les Extensions qui Leur sont Associées
![ss8](https://www.freecodecamp.org/news/content/images/2022/08/ss8.png)


### `title` – Change le Titre de la Fenêtre de l'Invite de Commande en Utilisant le Format `title nom-de-la-fenêtre`

![ss9](https://www.freecodecamp.org/news/content/images/2022/08/ss9.png)


### `fc` – Compare Deux Fichiers Similaires 

Si vous êtes un programmeur ou un écrivain et que vous voulez voir rapidement ce qui diffère entre deux fichiers, vous pouvez entrer cette commande puis le chemin complet vers les deux fichiers. Par exemple `fc "chemin-fichier-1" "chemin-fichier-2"`.
![ss10](https://www.freecodecamp.org/news/content/images/2022/08/ss10.png)

### `cipher` – Efface l'Espace Libre et Chiffre les Données

Sur un PC, les fichiers supprimés restent accessibles à vous et à d'autres utilisateurs. Donc, techniquement, ils ne sont pas supprimés sous le capot. 

Vous pouvez utiliser la commande cipher pour nettoyer le lecteur et chiffrer ces fichiers.
![ss11](https://www.freecodecamp.org/news/content/images/2022/08/ss11.png)


### `netstat -an` – Affiche les Ports Ouverts, leurs Adresses IP et États
![ss12](https://www.freecodecamp.org/news/content/images/2022/08/ss12.png)


### `ping` – Affiche l'Adresse IP d'un Site Web, Vous Indique Combien de Temps il Faut pour Transmettre des Données et Obtenir une Réponse  
![ss13](https://www.freecodecamp.org/news/content/images/2022/08/ss13.png)


### `color` – Change la Couleur du Texte de l'Invite de Commande
Entrez `color attr` pour voir les couleurs que vous pouvez changer :
![ss14](https://www.freecodecamp.org/news/content/images/2022/08/ss14.png)

Entrer `color 2` change la couleur du terminal en vert :
![ss15](https://www.freecodecamp.org/news/content/images/2022/08/ss15.png) 


### `for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear` – Affiche Tous les Mots de Passe Wi-Fi

![ss16](https://www.freecodecamp.org/news/content/images/2022/08/ss16.png) 


### `ipconfig` – Affiche des Informations sur les Adresses IP et les Connexions du PC

![ss17](https://www.freecodecamp.org/news/content/images/2022/08/ss17.png) 

Cette commande a également des extensions telles que `ipconfig /release`, `ipconfig /renew`, et `ipconfig /flushdns` que vous pouvez utiliser pour résoudre les problèmes de connexions internet.

### `sfc` – Vérificateur des Fichiers Système
Cette commande analyse votre ordinateur pour trouver des fichiers corrompus et les répare. L'extension de la commande que vous pouvez utiliser pour exécuter une analyse est `/scannow`.
![ss18](https://www.freecodecamp.org/news/content/images/2022/08/ss18.png) 


### `powercfg` – Contrôle les Paramètres de Puissance Configurables
Vous pouvez utiliser cette commande avec ses plusieurs extensions pour afficher des informations sur l'état de la puissance de votre PC. 

Vous pouvez entrer `powercfg help` pour afficher ces extensions.
![ss19](https://www.freecodecamp.org/news/content/images/2022/08/ss19.png) 

Par exemple, vous pouvez utiliser `powercfg /energy` pour générer un rapport sur l'état de la batterie.
![ss20](https://www.freecodecamp.org/news/content/images/2022/08/ss20.png) 

La commande `powercfg /energy` générera un fichier HTML contenant le rapport. Vous pouvez trouver le fichier HTML dans `C:\Windows\system32\energy-report.html`.


### `dir` – Liste les Éléments dans un Répertoire
![ss21](https://www.freecodecamp.org/news/content/images/2022/08/ss21.png)


### `del` – Supprime un Fichier 
![ss22](https://www.freecodecamp.org/news/content/images/2022/08/ss22.png)


### ` attrib +h +s +r nom_du_dossier ` – Masque un Dossier 

Vous pouvez masquer un dossier directement depuis la ligne de commande en tapant `attrib +h +s +r nom_du_dossier` puis en appuyant sur `ENTRÉE`.

Pour afficher à nouveau le dossier, exécutez la commande `- attrib -h -s -r nom_du_dossier`.
![ss23](https://www.freecodecamp.org/news/content/images/2022/08/ss23.png)


### `start adresse-du-site` – Se Connecte à un Site Web depuis la Ligne de Commande
![ss24](https://www.freecodecamp.org/news/content/images/2022/08/ss24.png)
![ss25](https://www.freecodecamp.org/news/content/images/2022/08/ss25.png) 


### `tree` – Affiche l'Arborescence du Répertoire Actuel ou du Lecteur Spécifié
![ss26](https://www.freecodecamp.org/news/content/images/2022/08/ss26.png) 


### `ver` – Affiche la Version du Système d'Exploitation
![ss27](https://www.freecodecamp.org/news/content/images/2022/08/ss27.png)


### `tasklist` – Affiche les Programmes Ouverts

Vous pouvez faire la même chose que vous faites avec le gestionnaire des tâches avec cette commande :
![ss28](https://www.freecodecamp.org/news/content/images/2022/08/ss28.png)
La commande suivante vous montre comment fermer une tâche ouverte.


### `taskkill` – Termine une Tâche en Cours

Pour terminer une tâche, exécutez `taskkill /IM "tache.exe" /F`. Par exemple, `taskkill /IM "chrome.exe" /F` :
![ss29](https://www.freecodecamp.org/news/content/images/2022/08/ss29.png) 


### `date` – Affiche et Change la Date Actuelle
![ss30](https://www.freecodecamp.org/news/content/images/2022/08/ss30.png)


### `time` – Affiche et Change l'Heure Actuelle
![ss31](https://www.freecodecamp.org/news/content/images/2022/08/ss31.png)


### `vol` – Affiche le Numéro de Série et les Informations d'Étiquette du Lecteur Actuel
![ss32](https://www.freecodecamp.org/news/content/images/2022/08/ss32.png) 


### `dism` – Exécute l'Outil de Gestion des Images de Déploiement
![ss33](https://www.freecodecamp.org/news/content/images/2022/08/ss33.png) 


### `CTRL + C` – Arrête l'Exécution d'une Commande 

### `-help` – Fournit un Guide pour d'Autres Commandes

Par exemple, `powercfg -help` montre comment utiliser la commande `powercfg`
![ss34](https://www.freecodecamp.org/news/content/images/2022/08/ss34.png) 


### `echo` – Affiche des Messages Personnalisés ou des Messages depuis un Script ou un Fichier
![ss35](https://www.freecodecamp.org/news/content/images/2022/08/ss35.png) 

Vous pouvez également utiliser la commande `echo` pour créer un fichier avec cette syntaxe `echo contenu-du-fichier > nomfichier.extension`.
![ss36](https://www.freecodecamp.org/news/content/images/2022/08/ss36.png) 


### `mkdir` – Crée un Dossier
![ss37](https://www.freecodecamp.org/news/content/images/2022/08/ss37.png)


### `rmdir` – Supprime un Dossier
![ss38](https://www.freecodecamp.org/news/content/images/2022/08/ss38.png)

**N.B.** : Le dossier doit être vide pour que cette commande fonctionne.


### `more` – Affiche Plus d'Informations ou le Contenu d'un Fichier
![ss39](https://www.freecodecamp.org/news/content/images/2022/08/ss39.png) 


### `move` – Déplace un Fichier ou un Dossier vers un Dossier Spécifié
![ss40](https://www.freecodecamp.org/news/content/images/2022/08/ss40.png)


### `ren` – Renomme un Fichier avec la Syntaxe `ren nomfichier.extension nouveau-nom.extension`
![ss41-1](https://www.freecodecamp.org/news/content/images/2022/08/ss41-1.png)


### `cls` – Efface la Ligne de Commande 

Au cas où vous entrez plusieurs commandes et que la ligne de commande devient encombrée, vous pouvez utiliser `cls` pour effacer toutes les entrées et leurs sorties.
![cls](https://www.freecodecamp.org/news/content/images/2022/08/cls.gif)


### `exit` – Ferme la Ligne de Commande 


### `shutdown` – Éteint, Redémarre, Met en Veille ou en Veille Prolongée l'Ordinateur

Vous pouvez éteindre, redémarrer, mettre en veille ou en veille prolongée votre PC depuis la ligne de commande. 

Entrez `shutdown` dans la ligne de commande pour voir les extensions que vous pouvez utiliser pour effectuer les actions. Par exemple, shutdown /r redémarrera votre ordinateur.
![ss42](https://www.freecodecamp.org/news/content/images/2022/08/ss42.png)


## Conclusion

Cet article vous a montré plusieurs commandes "inconnues de beaucoup" que vous pouvez utiliser pour accéder à des fonctionnalités cachées sur votre PC Windows.

Encore une fois, vous devez être prudent lors de l'utilisation de ces commandes car elles peuvent avoir un effet durable sur votre système d'exploitation.

Si vous trouvez les commandes utiles, partagez l'article avec vos amis et votre famille.

Au cas où vous connaissez une autre commande utile que je n'ai pas listée, [parlez-moi en sur Twitter](https://twitter.com/Ksound22). Je l'ajouterai et vous mentionnerai comme source.