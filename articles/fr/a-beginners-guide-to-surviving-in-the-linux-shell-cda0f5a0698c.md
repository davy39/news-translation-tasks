---
title: Un guide du débutant pour survivre dans le shell Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T15:30:23.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-surviving-in-the-linux-shell-cda0f5a0698c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sviUxGylSOenBQTLmAtGnA.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
seo_title: Un guide du débutant pour survivre dans le shell Linux
seo_desc: 'By Puranjay Mohan

  In this article, you''ll learn how to kill your fear of the Linux shell by learning
  the ten most useful Linux commands.


  All the best people in life seem to like LINUX - Steve Wozniak


  The Linux Shell/Command-Line

  A black screen with...'
---

Par Puranjay Mohan

Dans cet article, vous apprendrez à vaincre votre peur du shell Linux en apprenant les dix commandes Linux les plus utiles.

> **Toutes les meilleures personnes dans la vie semblent aimer LINUX -** Steve Wozniak

### Le shell Linux/Ligne de commande

Un écran noir avec du texte blanc et sans graphiques, oui ! Le shell Linux peut sembler intimidant au premier abord, mais il est beaucoup plus puissant que tout outil graphique. 

Linux alimente 70 % des serveurs et 90 % des supercalculateurs dans le monde. La courbe d'apprentissage pour Linux est raide et pour l'apprendre, vous devez vivre dedans pendant un certain temps. Une fois que vous maîtrisez la ligne de commande, vous acquérez une compétence qui vous distingue de la foule.

Cet article présente et explique les 10 commandes Linux les plus utiles nécessaires pour survivre dans l'environnement du shell Linux. Après avoir lu cet article, vous devriez être capable d'effectuer toutes les tâches de base comme créer et supprimer des répertoires, éditer des fichiers texte, et ainsi de suite en utilisant la ligne de commande.

![Image](https://cdn-media-1.freecodecamp.org/images/98wBtN9xnRdYspAeLkK5MDYo5ibGqQI7nIM-)

### Pourquoi devrait-on apprendre la ligne de commande Linux ?

#### Avantages d'être bon à utiliser la ligne de commande.

* **Vous en apprenez beaucoup plus sur votre système d'exploitation.**  
Le shell vous expose au système de fichiers plus directement que le navigateur de fichiers graphique, il vous fait comprendre la hiérarchie et la structure du système d'exploitation. Vous pouvez également manipuler directement les fichiers de configuration et cela vous donne le pouvoir de contrôler votre système d'exploitation plus efficacement.
* **Vous pouvez contrôler des ordinateurs et des serveurs à distance.**  
Les protocoles réseau comme **SSH** et **Telnet** vous permettent de vous connecter à distance aux ordinateurs sur un réseau, mais ils ne vous fournissent que le shell et non l'interface graphique. Par conséquent, vous pouvez utiliser ces protocoles uniquement si vous êtes familiarisé avec le shell.
* **Vous pouvez installer Arch Linux sans l'aide de personne**  
Arch Linux est une distribution Linux qui effraie de nombreux débutants en raison de sa méthode d'installation. Pour installer Arch Linux, vous devez effectuer toutes les étapes manuellement, de la partition du disque à la création de l'utilisateur, en utilisant le shell. Vous devez être très bon dans le shell Linux pour installer Arch Linux.
* **Vous pouvez être payé pour configurer et administrer des serveurs Linux.**  
La plupart des entreprises ont une offre d'emploi intitulée « Administrateur système Linux ». Le rôle de la personne à ce poste est de maintenir les ordinateurs Linux et d'y apporter des modifications et des configurations selon les besoins. La personne à ce poste doit être très bonne dans le shell Linux et doit connaître toutes les commandes nécessaires pour configurer un système Linux.

### L'invite de commande Linux

Lorsque vous ouvrez l'application de terminal dans votre distribution Linux, vous verrez un écran noir avec votre nom et d'autres informations imprimées. Après quoi, vous verrez un curseur prêt à recevoir des commandes. Les informations affichées par l'invite sont configurables mais cela dépasse le cadre de ce tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/zzllZ1dcG-XhRNdpyGEmSghbZmhQdYXQB4JB)
_[nom_utilisateur@nom_hôte répertoire_courant]$_

L'invite fournit des informations sur le nom d'utilisateur, le nom d'hôte (le nom de votre ordinateur tel qu'il apparaît sur le réseau), le répertoire de travail actuel et un « $ », qui signifie que vous êtes un utilisateur normal et non l'utilisateur root (l'utilisateur root a tous les privilèges et droits dans Linux).

### Les 10 commandes de base

Ces 10 commandes vous permettront d'expérimenter le shell de manière à pouvoir effectuer toutes les tâches que vous avez faites dans l'environnement de l'interface graphique, comme créer et supprimer des répertoires, écrire, éditer et supprimer des fichiers, etc., dans le shell sans rencontrer de problèmes.

### 1. pwd

La commande print working directory (pwd) imprime le chemin complet vers le répertoire dans lequel vous travaillez. Lorsque vous ouvrez l'application de terminal, elle démarre généralement le shell dans votre dossier personnel, donc exécuter la commande `pwd` imprimera « /home/(votre-nom-utilisateur) ». « ~ » représente le répertoire personnel dans l'invite.

![Image](https://cdn-media-1.freecodecamp.org/images/q6g9sTGABPXyjHqygPu9WrAntYD36G3tbEC5)
_commande pwd dans le dossier personnel_

### 2. cd

La commande Change Directory (cd) change le répertoire de travail vers le répertoire dont le nom est donné après cd. Écrire `cd mon_dossier` changera le répertoire de travail vers « mon_dossier » et son nom apparaîtra dans l'invite, mais elle générera une erreur si « mon_dossier » n'existe pas dans le répertoire actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/0T5iCKOE7JlCPyhM0aU8TMik9-UN4862-AYN)
_cd vers mon_dossier puis exécuter pwd_

Exécuter la commande « pwd » après l'étape ci-dessus affichera le chemin vers le répertoire vers lequel nous sommes passés.

Exécuter la commande `cd ..` changera le répertoire de travail vers le répertoire précédent dans la hiérarchie. Dans ce cas, il reviendra au répertoire personnel.

![Image](https://cdn-media-1.freecodecamp.org/images/CjYtnXGLppUpsrd6vfQxjeO9L9XfVlthV1JG)
_exécuter « cd .. » pour changer vers le répertoire précédent puis exécuter pwd._

Vous pouvez également fournir le chemin absolu vers le répertoire vers lequel vous souhaitez passer. Les chemins absolus sont des chemins complets commençant par le répertoire racine. Par exemple, le chemin absolu vers « mon_dossier » sera « /home/puranjay/mon_dossier », qui est le même chemin montré par la commande pwd.

### 3. ls

La commande List (ls) imprime le contenu du répertoire de travail actuel, elle imprime les noms de tous les fichiers et répertoires présents dans le répertoire actuel. Exécuter `ls` dans le répertoire « mon_dossier » affichera son contenu, c'est-à-dire fichier1, fichier2, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/TaePljLT3fT2nJCjxvnPyvJKkdUn-DzEP0BF)
_commande ls en cours d'exécution dans le répertoire mon_dossier_

Vous pouvez également fournir le chemin absolu vers le répertoire dont vous souhaitez voir le contenu. Par exemple, si le répertoire de travail est le répertoire personnel et que `ls /boot` est exécuté, le shell imprimera le contenu du dossier « boot » présent dans le répertoire racine (/). Le répertoire de travail ne changera pas. De plus, « boot » et « /boot » n'impliquent pas la même signification pour le shell. « boot » signifie un répertoire ou un fichier dans le répertoire de travail actuel, mais « /boot » signifie un répertoire ou un fichier présent dans le répertoire racine (/). Exécuter `ls boot` imprimera un message d'erreur car il n'y a pas de fichier ou de dossier nommé « boot » dans le répertoire de travail actuel (répertoire personnel).

![Image](https://cdn-media-1.freecodecamp.org/images/48xdRf17CmuwqY1VPoU2UhdRD7uKDlaJZc5l)
_ls /boot montre le contenu du répertoire boot dans la racine, mais ls boot montre une erreur_

### 4. man

La commande man (manuel) ouvrira la page de manuel pour la commande donnée après man. Les pages de manuel contiennent de la documentation sur toutes les commandes disponibles dans Linux, elles fournissent des informations sur l'utilisation correcte de la commande et les différentes options disponibles pour la commande.

Pour quitter la page de manuel, appuyez sur « **q** ».

Par exemple, exécuter `man ls` ouvrira la page de manuel pour la commande ls.

![Image](https://cdn-media-1.freecodecamp.org/images/JCZU2ozbykb3h7XWxcNHjydpFhQbQ5l-fHLi)
_La page de manuel pour la commande ls_

### 5. mkdir

La commande Make-directory (mkdir) crée un nouveau répertoire du nom donné après la commande, dans le répertoire de travail actuel. Par exemple, exécuter `mkdir bonjour` créera un dossier nommé « bonjour » à l'intérieur du répertoire actuel. Après la création du répertoire, exécuter `cd bonjour` changera le répertoire actuel vers le nouveau répertoire « bonjour », « ~ » changera pour « bonjour ».

![Image](https://cdn-media-1.freecodecamp.org/images/hLfshSo4P6YvuXovTirK3orqrs7We64Yroa6)
_création d'un répertoire nommé « bonjour » puis passage à celui-ci._

### 6. rmdir

Remove directory (rmdir) supprime/efface le répertoire avec le nom donné après la commande. Exécuter `rmdir bonjour` supprimera le répertoire « bonjour » créé précédemment. Un répertoire ne peut pas être supprimé en exécutant rmdir à l'intérieur du même répertoire, qui doit être supprimé. La commande `cd ..` peut être utilisée pour sortir du répertoire et ensuite `rmdir bonjour` peut être exécutée pour le supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/CTZDh51AjPqZCIECZ3gioTMyMz5k25OE3Yz3)
_sortie du répertoire « bonjour » puis suppression de celui-ci._

Si un répertoire n'est pas vide et que `rmdir` est exécuté pour supprimer ce répertoire, il échouera avec une erreur indiquant que le répertoire supprimé n'est pas vide.

![Image](https://cdn-media-1.freecodecamp.org/images/LAtnIwDlG-0AiKkaW9WmQXSofw9qzZ7DrDed)
_« bonjour » contient un fichier nommé « fichier1 », donc rmdir échoue avec une erreur._

Pour surmonter cette erreur et supprimer des répertoires qui ne sont pas vides, le drapeau `--ignore-fail-on-non-empty` peut être passé à rmdir.

Par exemple, exécuter rmdir `--ignore-fail-on-non-empty bonjour` supprimera le répertoire bonjour bien qu'il ne soit pas vide.

![Image](https://cdn-media-1.freecodecamp.org/images/QILE4pb42NKSHyTcaMva1GqQV5Jc0LIUVD1d)
_suppression du dossier bonjour qui n'est pas vide_

### 7. clear

La commande Clear nettoie le shell et supprime toutes les sorties précédentes. Elle est utile lorsque vous souhaitez effacer l'encombrement dans le terminal.

### 8. nano

Nano est un éditeur de texte basé sur le terminal, qui peut être utilisé pour créer et éditer des fichiers texte et également éditer des fichiers de configuration. Il est similaire à tout autre éditeur de texte comme le bloc-notes, la seule différence étant qu'il fonctionne via le shell et n'a pas d'interface graphique. Il est préinstallé avec la plupart des distributions Linux.  
Exécuter `nano` dans le shell ouvre l'éditeur de texte nano et fournit une interface où le texte peut être tapé.

![Image](https://cdn-media-1.freecodecamp.org/images/zq8NxPxsqyD9POpd6kN4h9paPhYWdnwQ80rj)
_Nano en cours d'exécution dans le terminal Linux_

Pour quitter nano, appuyez sur `CTRL+X`, il vous demandera si vous souhaitez enregistrer le fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/h0-TOHFeaAS-YS4wbvHHGygujfasDRHtXxIP)
_Appuyer sur « Y » enregistrera le fichier._

Si vous appuyez sur « Y », il vous demandera d'entrer le nom pour le fichier et appuyer sur « ENTRÉE » après avoir tapé le nom fermera nano. Un fichier avec le nom que vous avez donné sera créé dans le répertoire actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/zFnHFjfM12jMK4exVqKDWuhAd7XT-3OS94Lp)
_enregistrement du fichier sous testfile.txt_

### **9. cat**

La commande Cat est utilisée pour imprimer le contenu d'un fichier sur la console du shell, elle est principalement utilisée lorsque vous souhaitez voir ce qui est présent à l'intérieur d'un fichier. Pour utiliser la commande cat, `cat nom_fichier` peut être exécutée dans le shell, elle affichera le contenu du fichier à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/TwM-2qx7s6pXkSKhI6fmQJGFBTfCspCsA5c4)
_exécution de la commande cat sur le fichier texte créé précédemment._

### 10. rm

La commande Remove (rm) est similaire à la commande `rmdir` mais elle supprime des fichiers au lieu de répertoires. Pour utiliser cette commande, `rm nom_fichier` peut être exécutée dans le shell. Elle supprimera le fichier s'il est présent dans le répertoire actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/8OHhC5Y-oTjhX16iw0xJtByyGtUHJZLlCDGD)
_suppression du fichier texte créé précédemment._

### **11. mv (Commande Bonus)**

La commande mv peut être utilisée pour déplacer ou renommer des fichiers. Le renommage est simplement le déplacement d'un fichier vers un autre nom. La commande mv a le format, `mv source destination`. Vous devez fournir le chemin complet vers la source et la destination si elle se trouve en dehors du répertoire de travail actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/2gb8qFl079Dpdp-evt5JxeiIta2JOmhSvEar)

### Notes et points à retenir :

* Le shell Linux est sensible à la casse, donc « bureau » et « Bureau » n'impliquent pas la même signification.
* Il faut faire attention lors de l'écriture des chemins dans Linux car « boot » et « /boot » sont deux dossiers différents.
* La seule façon de maîtriser le shell Linux est d'y passer du temps et de l'utiliser tous les jours. C'est un avantage supplémentaire si votre système d'exploitation principal est Linux.
* Tout ce que vous faites dans le système d'exploitation Linux, essayez de trouver un moyen de faire la même chose mais depuis le shell. [Stack Overflow](https://stackoverflow.com/) est un excellent endroit pour obtenir des réponses à vos questions sur Linux.
* Si vous voulez vraiment perfectionner vos compétences Linux et devenir un maître de Linux, alors vous pouvez lire la [Linux Bible](https://www.oreilly.com/library/view/linux-bible-9th/9781118999875/), qui est le guide Linux le plus approfondi jamais écrit.

### Conclusion :

Ma première rencontre avec le terminal Linux remonte à 5 ans et j'étais moi aussi très intimidé par celui-ci. Depuis ces cinq années, j'ai appris quelque chose de nouveau sur Linux chaque jour. L'énergie et le temps que vous passez à apprendre Linux en valent complètement la peine et ne seront jamais vains. Linux est le plus grand et le plus ancien projet Open-Source et l'apprendre est la première étape du processus de contribution à celui-ci.

N'hésitez pas à signaler les erreurs que vous trouvez, la critique constructive ne fait pas de mal.

Merci.