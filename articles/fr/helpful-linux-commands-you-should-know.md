---
title: Commandes Linux utiles que vous devriez connaître
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-07-03T20:36:49.000Z'
originalURL: https://freecodecamp.org/news/helpful-linux-commands-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/gabriel-heinzer-4Mw7nkQDByk-unsplash.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Commandes Linux utiles que vous devriez connaître
seo_desc: 'Ever feel like you’ve mastered the basics of Linux and are ready to level
  up your skills? Well, good news – there are many powerful commands that you might
  not know about.

  In this article, I''ll introduce you to some lesser-known Linux commands that w...'
---

Vous avez déjà l'impression d'avoir maîtrisé les bases de Linux et d'être prêt à passer au niveau supérieur ? Eh bien, bonne nouvelle – il existe de nombreuses commandes puissantes que vous ne connaissez peut-être pas encore.

Dans cet article, je vais vous présenter quelques commandes Linux moins connues qui vous aideront à devenir un développeur plus productif et efficace.

Que vous cherchiez à booster votre productivité, à renforcer la sécurité de votre système, ou simplement à impressionner vos collègues développeurs avec vos compétences Linux, ces commandes vous couvrent.

## Chroot : Exécuter des commandes avec un répertoire racine différent

Vous avez déjà voulu exécuter des commandes dans un répertoire racine différent ? La commande chroot vous permet de faire exactement cela.

Chroot, abréviation de « change root », vous permet d'exécuter des commandes avec un répertoire racine différent. Ainsi, si vous souhaitez tester un logiciel dans un environnement contenu ou construire un système Linux minimal, chroot est votre ami.

Pour utiliser chroot, vous devez d'abord configurer un répertoire pour qu'il agisse comme la nouvelle racine. Ensuite, vous exécutez la commande chroot, en lui passant le chemin de ce répertoire. Par exemple, pour chroot dans **/home/testdir**, vous exécuteriez :

```bash
chroot /home/testdir
```

Après cela, toutes les commandes que vous exécutez seront relatives à / dans le répertoire `/home/testdir`. Vous pourrez donc installer des paquets, exécuter des scripts shell, compiler des programmes, et ainsi de suite. Lorsque vous avez terminé, il suffit de quitter le chroot avec `exit`.

Chroot crée un environnement isolé, donc toutes les modifications que vous apportez n'affecteront pas le reste de votre système. C'est un outil pratique pour les tests et le développement ou pour la récupération d'urgence. Une fois que vous vous familiarisez avec chroot, vous trouverez toutes sortes d'utilisations pour celui-ci.

## Crontab : Planifier des tâches pour qu'elles s'exécutent automatiquement

Crontab est une commande Linux pratique qui vous permet de planifier des tâches pour qu'elles s'exécutent automatiquement à des heures spécifiques. Vous vous demanderez comment vous avez pu vivre sans elle !

Pour commencer, ouvrez le fichier crontab avec `crontab -e`. Cela ouvrira votre éditeur de texte par défaut où vous pourrez créer des entrées de planification, appelées [tâches cron](https://www.freecodecamp.org/news/cron-jobs-in-linux/). Chaque entrée a cinq champs de temps – minute, heure, jour du mois, mois, jour de la semaine, suivis de la commande à exécuter.

Par exemple, `0 0 * * * /home/user/daily_script.sh` exécuterait le script **daily_script.sh** à minuit chaque jour. Vous pouvez également faire `30 8 * * 1-5 /home/user/work_script.sh` pour exécuter **work_script.sh** à 8h30 chaque jour de la semaine.

Crontab permet une grande flexibilité. Vous pouvez planifier des tâches pour qu'elles s'exécutent :

* Toutes les minutes, toutes les heures, tous les jours, toutes les semaines, tous les mois ou toutes les années
* À une minute/heure spécifique
* Certains jours de la semaine/mois
* Avec des caractères génériques pour exécuter, par exemple, toutes les 3 heures ou tous les lundis et jeudis

Les possibilités sont infinies ! Vous pouvez planifier des scripts de sauvegarde, la maintenance du système, des rapports par e-mail et bien plus encore.

## Df : Vérifier l'utilisation de l'espace disque

Vous êtes déjà tombé à court d'espace disque et vous vous demandez où il est passé ? La commande `df` est là pour vous aider. df signifie « disk free » et vous montre exactement combien d'espace est utilisé et disponible sur votre système Linux.

### Vérifier l'utilisation pour tous les systèmes de fichiers montés

Pour voir un aperçu de l'utilisation de l'espace disque pour tous les lecteurs et partitions montés, il suffit d'exécuter :

```bash
df -h
```

L'option `-h` formate la sortie dans un format lisible par l'homme, affichant les tailles en Go et Mo au lieu d'octets. La sortie affichera :

* Système de fichiers : Le nom du lecteur ou de la partition
* Taille : Espace total
* Utilisé : Espace actuellement utilisé
* Disponible : Espace libre encore disponible
* Util% : Pourcentage d'espace utilisé

Cela vous donne un aperçu rapide de l'endroit où vous avez de l'espace et où il est en train de manquer.

### Vérifier l'utilisation pour un système de fichiers spécifique

Pour vérifier l'espace sur un lecteur ou une partition spécifique, passez son point de montage à df :

`df -h /home`

Cela affichera les statistiques d'utilisation uniquement pour votre partition /home.

Surveiller l'utilisation du disque avec df et les outils associés est important pour tout administrateur système Linux. Personne ne veut manquer d'espace de manière inattendue.

## Dmesg : Voir les messages du noyau

Vous vous êtes déjà demandé ce qui se passe en coulisses dans votre système Linux ? La commande **dmesg** vous permet de jeter un coup d'œil sous le capot et de voir les messages du noyau, le cœur de votre système d'exploitation.

Lorsque votre système Linux démarre, le noyau initialise le matériel, charge les pilotes, démarre les services et effectue d'autres tâches de démarrage. La commande **dmesg** affiche les messages qui sont enregistrés pendant ce processus afin que vous puissiez voir ce qui se passe.

Pour voir les messages du noyau, ouvrez simplement votre terminal et exécutez la commande dmesg. Vous verrez des pages et des pages de mises à jour de statut, de diagnostics, d'erreurs, et plus encore alors que votre système prend vie. Parcourez-les pour vérifier s'il y a des problèmes, ou recherchez des mots-clés spécifiques comme le nom de votre adaptateur Wi-Fi ou d'autres composants matériels.

La sortie de **dmesg** peut également fournir des indices pour résoudre les problèmes que vous rencontrez. Par exemple, si votre réseau ne fonctionne pas, **vérifiez dmesg pour les messages d'erreur liés à votre carte Ethernet ou sans fil**. Vous pourriez repérer quelque chose comme « erreur d'initialisation du périphérique réseau eth0 » qui pointe vers un problème de pilote.

La commande `dmesg` est un outil de diagnostic pratique pour tout administrateur système Linux ou utilisateur avancé. Elle offre un aperçu de votre système Linux et peut aider à découvrir la source de dysfonctionnements majeurs et de petites nuisances. Ps : vous pouvez vous sentir comme un hacker.

## Grep : Rechercher des motifs dans les fichiers

La commande grep vous permet de rechercher des motifs dans des fichiers et du texte. Elle est idéale lorsque vous devez trouver quelque chose de spécifique dans une mer de données.

Supposons que vous avez un fichier journal massif rempli d'informations, mais que vous ne souhaitez voir que les lignes contenant le mot « erreur ». Il suffit d'exécuter :

```bash
grep error log.txt
```

Cela imprimera uniquement les lignes dans log.txt qui contiennent le mot « erreur ».

Vous pouvez également utiliser grep pour rechercher des motifs plutôt que simplement des mots. Par exemple, pour trouver toutes les lignes dans un fichier qui commencent par « A » suivi d'un nombre, utilisez :

```bash
grep ^A[0-9] log.txt
```

Le `^A` ancre la correspondance au début de la ligne, et [0-9] correspond à n'importe quel chiffre.

Grep dispose de nombreuses autres fonctionnalités avancées. Vous pouvez utiliser :

* Des motifs regex pour des recherches complexes
* `-i` pour ignorer la casse
* `-v` pour inverser la recherche et afficher les lignes qui ne correspondent pas
* `-c` pour obtenir simplement un compte des correspondances
* `-r` pour rechercher récursivement tous les fichiers dans un répertoire

La prochaine fois que vous devrez rechercher dans des fichiers, ne le faites pas manuellement—laissez grep faire le travail pour vous.

## Head/Tail : Voir la première/dernière partie d'un fichier

Avez-vous déjà eu besoin de vérifier rapidement les premières ou dernières lignes d'un long fichier ? Les commandes head et tail sont parfaites pour cela.

La commande `head` vous montre les 10 premières lignes d'un fichier par défaut. Vous pouvez spécifier le nombre de lignes que vous souhaitez voir en utilisant l'option `-n`, comme `head -n 5 filename` pour afficher les 5 premières lignes.

La commande `tail` vous montre les 10 dernières lignes d'un fichier par défaut. Encore une fois, utilisez l'option `-n` pour spécifier le nombre de lignes que vous souhaitez voir, comme `tail -n 20 filename` pour afficher les 20 dernières lignes.

Les commandes `head` et `tail` sont utiles lorsque vous souhaitez faire une vérification rapide du début ou de la fin d'un long fichier sans avoir à faire défiler tout le contenu. Voici quelques autres utilisations de ces commandes :

* Vérification des fichiers journaux pour les erreurs ou avertissements récents
* Visualisation des en-têtes de courrier électronique
* Prévisualisation des fichiers de configuration
* Et plus encore !

Essayez `head` et `tail` – vous serez surpris de voir à quel point ils simplifient les tâches que vous effectuez tout le temps.

## Ps : Lister les processus en cours d'exécution

La commande Ps vous permet de voir des informations sur les processus en cours d'exécution sur votre système. Cela inclut les programmes, commandes et démons qui sont actuellement actifs. Utiliser Ps est un moyen rapide d'obtenir un aperçu de ce que votre système Linux fait à un moment donné et des ressources système que chaque processus utilise.

Pour voir une liste de base des processus en cours d'exécution, entrez :

```bash
ps aux
```

Cela vous montrera :

* A : Tous les processus
* U : Utilisateur
* X : Processus sans terminaux

La sortie contiendra des informations comme :

* **USER** : Le propriétaire du processus
* **PID** : L'identifiant du processus
* **%CPU** : L'utilisation du CPU
* **%MEM** : L'utilisation de la mémoire
* **VSZ** : L'utilisation de la mémoire virtuelle
* **TTY** : Le terminal associé au processus
* **STAT** : L'état du processus (En cours d'exécution, En sommeil, Zombie, etc.)
* **START** : L'heure de démarrage du processus
* **TIME** : Le temps CPU utilisé
* **COMMAND** : La commande qui a démarré le processus

Vous pouvez également filtrer la sortie de Ps par :

* Nom d'utilisateur : `ps aux | grep root`
* Nom du processus : `ps aux | grep cron`
* PID : `ps aux | grep 555`

La commande Ps vous permet de vérifier rapidement ce que fait votre système et de vous assurer qu'il n'y a pas de processus incontrôlés ou zombies qui monopolisent les ressources. Pour tout utilisateur Linux, `Ps` est un outil indispensable pour la surveillance et le dépannage du système.

## Rsync : Synchroniser des fichiers et dossiers

En tant qu'utilisateur Linux, vous avez probablement eu besoin de synchroniser des fichiers et dossiers entre différents emplacements. Peut-être avez-vous des fichiers sur votre bureau que vous devez transférer sur votre ordinateur portable, ou vous souhaitez sauvegarder vos dossiers les plus importants sur un disque externe. La commande rsync rend la synchronisation et la sauvegarde de vos fichiers très facile.

Rsync est un outil de copie de fichiers rapide et polyvalent. Il peut copier et synchroniser des fichiers et dossiers localement ou à distance via SSH. Il est assez intelligent pour ne transférer que les différences entre deux emplacements, économisant ainsi du temps et de la bande passante.

Pour utiliser rsync, ouvrez votre terminal et entrez la commande :

```bash
rsync [options] source destination
```

* La source est l'emplacement des fichiers que vous souhaitez copier. Cela pourrait être un dossier sur votre bureau ou un serveur distant.
* La destination est l'endroit où vous souhaitez copier les fichiers. Cela pourrait être un disque externe monté sur votre système ou un dossier sur un autre serveur.
* Les options vous permettent de spécifier des éléments comme :
* `-a` : Mode archive qui préserve les permissions, les timestamps, le groupe, le propriétaire et les liens symboliques
* `-v` : Sortie verbeuse pour que vous puissiez voir ce qui est copié
* `-z` : Compression pour accélérer les transferts sur les réseaux lents
* `-h` : Tailles lisibles par l'homme (par exemple, 1K, 234M, 2G)

Rsync est un outil indispensable pour tout utilisateur Linux. Une fois que vous l'aurez maîtrisé, vous synchroniserez et sauvegarderez vos fichiers en toute confiance. 

Pour une lecture approfondie, veuillez consulter [RSync Examples – Rsync Options and How to Copy Files Over SSH](https://www.freecodecamp.org/news/rsync-examples-rsync-options-and-how-to-copy-files-over-ssh/).

## Le puissant visualiseur de pipe (pv)

Vous avez déjà voulu voir la progression des données à travers un pipe ? La commande `pv` vous permet de faire exactement cela. C'est un visualiseur de pipe qui vous montre la progression des données à travers un pipeline.

Supposons que vous avez un gros fichier que vous souhaitez compresser, comme une vidéo ou un fichier de sauvegarde. Au lieu de fixer un curseur clignotant pendant que gzip fait son travail, vous pouvez voir la progression avec pv. Il suffit de faire passer les données à travers pv, puis à gzip :

```bash
cat mylargefile.mp4 | pv | gzip > mylargefile.mp4.gz
```

`pv` affichera le débit et le temps estimé restant pendant que vos données sont compressées. C'est un moyen simple d'obtenir un retour sur les commandes de longue durée.

Vous pouvez également utiliser `pv` pour voir le [débit](https://www.techtarget.com/searchnetworking/definition/throughput#:~:text=Throughput%20is%20a%20measure%20of,and%20network%20systems%20to%20organizations.) et les taux de transfert des données sur le réseau. Par exemple, lors de la copie d'un fichier avec `scp` ou `rsync`, ajoutez `pv` au pipeline :

```bash
rsync -avz myfiles user@host:/backup | pv
```

Maintenant, vous verrez la progression de vos fichiers copiés sur le réseau. pv vous donne des informations comme :

* Octets transférés
* Taux de transfert
* Temps restant estimé
* Progression
* Et plus encore

C'est un outil pratique pour vous donner plus d'informations sur ce qui se passe dans ces commandes de terminal de longue durée.

## mtr : Diagnostics réseau

Vous avez déjà eu besoin de diagnostiquer des problèmes réseau mais vous n'aviez pas accès à des outils coûteux ? mtr est un outil de diagnostic réseau simple mais puissant pour Linux. Il combine la fonctionnalité des programmes « traceroute » et « ping » en un seul outil de diagnostic réseau.

`mtr` envoie des requêtes d'écho [ICMP](https://www.freecodecamp.org/news/traceroute-and-ping/) pour tester la connectivité réseau entre l'hôte sur lequel `mtr` s'exécute et un hôte de destination spécifié par l'utilisateur. Il imprime les temps de réponse et les statistiques de perte de paquets pour chaque routeur le long du chemin. Cela vous permet de localiser rapidement les problèmes réseau.

Pour utiliser mtr, ouvrez un terminal et entrez :

```bash
mtr [nom de domaine ou adresse IP]
```

Par exemple, pour tracer la route vers google.com, entrez :

```bash
mtr google.com
```

mtr commencera à tracer la route et imprimera les résultats qui se mettent à jour en temps réel. Il affichera :

* L'adresse IP et le nom d'hôte de chaque routeur le long du chemin
* Le pourcentage de perte de paquets pour chaque routeur
* Les temps de réponse en millisecondes pour chaque routeur

La sortie continuera à se mettre à jour jusqu'à ce que vous appuyiez sur Ctrl+C pour arrêter le trace.

mtr est un outil simple mais utile pour tout administrateur réseau Linux. Il peut vous faire gagner des heures de temps de dépannage lorsque le réseau tombe en panne en vous aidant à identifier la source de la latence ou de la perte de paquets.

## jq : Analyser JSON

Vous êtes déjà tombé sur un fichier JSON désordonné et vous avez souhaité avoir un moyen facile de le parser ? Rencontrez jq, un outil en ligne de commande qui vous permet de filtrer et d'analyser les données JSON avec facilité.

jq fonctionne comme un filtre. Vous lui passez des données JSON sur stdin, et il passe les données filtrées/transformées à stdout. 

Par exemple, supposons que vous avez un fichier JSON appelé `data.json` avec un tableau d'objets. Vous pouvez le filtrer pour ne montrer que les objets où `name` est égal à `John` comme ceci :

```bash
cat data.json | jq '.[] | select(.name == "John")'
```

Cela imprimera uniquement les objets John sur la console.

jq supporte beaucoup plus de filtres que juste `select()`, en voici quelques autres utiles :

* `.key` : Accéder à une clé des objets
* `.[10:]` : Montrer les éléments à partir de l'index 10
* `.[10:15]` : Montrer les éléments de l'index 10 à 15
* `length` : Imprimer la longueur d'un tableau
* `map(.)` : Appliquer un filtre à chaque élément d'un tableau
* `group_by(.key)` : Grouper les objets par une clé

Avec jq, vous pouvez manipuler les données JSON de presque n'importe quelle manière directement depuis la ligne de commande. `jq` peut sembler niche, mais JSON est utilisé partout sur le web, donc être capable de l'analyser et de le transformer efficacement est une compétence utile.

## tac : Voir les fichiers de configuration à l'envers

Avez-vous déjà fait une erreur en éditant un fichier de configuration et enregistré les changements, pour réaliser que vous préfériez la version précédente ? La commande `tac` vous permet de voir rapidement les fichiers de configuration à l'envers, afin que vous puissiez voir à quoi ressemblait le fichier avant vos modifications.

Tac imprime simplement les fichiers dans l'ordre inverse, ligne par ligne. Pour voir un fichier appelé `config.txt` à l'envers, exécutez :

```bash
tac config.txt
```

Cela imprimera la dernière ligne du fichier en premier, puis l'avant-dernière ligne, et ainsi de suite jusqu'à ce qu'il atteigne la première ligne.

* Utilisez tac lorsque vous souhaitez **voir rapidement un fichier journal à l'envers** pour voir les dernières entrées en premier.
* Tac peut également être utile lorsque vous **éditez des fichiers de configuration via la ligne de commande**. Si vous faites une erreur, exécutez tac pour voir à quoi ressemblait le fichier avant afin de pouvoir revenir en arrière.

Tac est un utilitaire simple mais utile à avoir dans votre boîte à outils Linux.

## perf : Analyser les performances du CPU

Si vous vous êtes déjà demandé pourquoi votre système Linux semble plus lent avec le temps, la commande perf peut vous aider à le découvrir. Perf est un outil de profilage dans Linux qui peut analyser les performances de votre CPU pour vous aider à identifier les goulots d'étranglement.

Pour commencer, exécutez la commande de base `perf list` pour voir une liste des événements que vous pouvez surveiller. Il y en a des centaines ! Certains des plus utiles pour profiler les performances du CPU sont :

* `cpu-clock` : Mesurer les cycles d'horloge du CPU
* `task-clock` : Mesurer le temps passé sur l'exécution des tâches
* `cache-misses` : Compter le nombre de défauts de cache
* `branch-misses` : Compter le nombre d'erreurs de prédiction de branche

Choisissez un événement que vous souhaitez surveiller, puis exécutez une commande comme :

```bash
perf stat -e cpu-clock sleep 5
```

Cela exécutera la commande `sleep 5` et mesurera l'événement `cpu-clock` pendant son exécution. Perf vous donnera ensuite un résumé des statistiques pour cet événement.

Pour obtenir des informations de profilage plus détaillées, utilisez la commande `perf record`. Par exemple, pour profiler un script appelé `script.sh`, exécutez :

```bash
perf record script.sh
```

Cela exécutera le script et enregistrera les données de profilage. Vous pourrez ensuite voir les résultats avec :

```bash
perf report
```

Cela vous donne un rapport interactif pour analyser les résultats. Vous verrez des choses comme :

* Le pourcentage de temps passé dans chaque fonction
* Le temps réel passé dans chaque fonction
* Le nombre d'appels à chaque fonction

En utilisant perf, vous avez un outil puissant pour optimiser les performances de votre système Linux. Perf est vraiment un outil incroyable (bien que sous-utilisé).

## Conclusion

Voilà, quelques commandes Linux utiles qui vous feront sentir comme un utilisateur avancé en un rien de temps. 

Avec ces astuces en poche, vous navigerez dans Linux comme un pro. La prochaine fois que vous serez bloqué ou frustré, essayez l'une de ces commandes. Vous pourriez bien vous surprendre par ce que vous pouvez accomplir.

Linux est un système d'exploitation incroyablement puissant si vous savez parler son langage. Considérez ceci comme votre guide de démarrage pour devenir fluent.

Je suis [Rahul](https://rahul.biz/), 19 ans, Hustler. Je construis [Fueler.io](https://fueler.io/register?referral_token=94329340-3e14-4e1e-83fa-bd5e1992) une plateforme pour les généralistes afin de créer un profil de preuve de travail et de décrocher des opportunités. Connectons-nous sur [Twitter](https://twitter.com/rahul_wip).