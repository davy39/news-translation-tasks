---
title: 'La commande Tar sous Linux : Tar CVF et Tar XVF expliqués avec des exemples
  de commandes'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-08-14T21:34:05.000Z'
originalURL: https://freecodecamp.org/news/tar-command-linux-tar-cvf-tar-xvf
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9938740569d1a4ca1e84.jpg
tags:
- name: Linux
  slug: linux
seo_title: 'La commande Tar sous Linux : Tar CVF et Tar XVF expliqués avec des exemples
  de commandes'
seo_desc: "The name tar is, by most accounts, short for tape archive. The \"tapes\"\
  \ in question would be all those magnetic storage drives that were popular all the\
  \ way back in the 1950s. \nThat suggests that the tar tool might be a bit old and\
  \ past its prime. But..."
---

Le nom `tar` est, selon la plupart des sources, l'abréviation de _tape archive_. Les "bandes" en question seraient toutes ces unités de stockage magnétique qui étaient populaires dès les années 1950. 

Cela suggère que l'outil `tar` pourrait être un peu ancien et dépassé. Mais la vérité est que, au fil des années et à travers tous les changements sismiques du monde de l'IT, `tar` n'a perdu aucune de sa puissance et de sa valeur.

Dans cet article, basé sur le contenu de mon livre [Linux in Action](https://www.amazon.com/gp/product/1617294934/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1617294934&linkCode=as2&tag=projemun-20&linkId=1a460c0cd9a39e01821133b90632cba8), je vais vous montrer les bases de la création, de la compression et de la restauration des archives tar. Commençons par le début.

# Création d'archives

Cet exemple va prendre tous les fichiers et répertoires dans et sous le répertoire de travail actuel et construire un fichier d'archive que j'ai astucieusement nommé `archivename.tar`. 

Ici, j'utilise trois arguments après la commande tar : 

* le `c` indique à tar de créer une nouvelle archive,
* `v` définit la sortie de l'écran en mode verbeux afin que je reçoive des mises à jour, et 
* `f` pointe vers le nom de fichier que je souhaite donner à l'archive. 

Le `*` est ce qui indique à `tar` d'inclure tous les fichiers et répertoires locaux de manière récursive.

```
$ tar cvf archivename.tar *
file1
file2
file3
directory1
directory1/morestuff
directory1/morestuff/file100
directory1/morestuff/file101

```

La commande tar ne déplacera ni ne supprimera jamais aucun des répertoires et fichiers originaux que vous lui fournissez - elle ne crée que des copies archivées. 

Vous devriez également noter que l'utilisation d'un point (.) au lieu d'un astérisque (*) dans la commande précédente inclurait même les fichiers cachés (dont les noms de fichiers commencent par un point) dans l'archive.

Si vous suivez sur votre propre ordinateur (ce que vous devriez définitivement faire), alors vous verrez un nouveau fichier nommé archivename.tar. L'extension de nom de fichier .tar n'est pas nécessaire, mais c'est toujours une bonne idée de communiquer clairement le but d'un fichier de toutes les manières possibles.

Extraire votre archive afin de restaurer les fichiers est facile : il suffit d'utiliser `xvf` au lieu de `cvf`. Cela, dans l'exemple, sauvegardera de nouvelles copies des fichiers et répertoires originaux à l'emplacement actuel.

```
$ tar xvf archivename.tar
file1
file2
file3
directory1
directory1/morestuff
directory1/morestuff/file100
directory1/morestuff/file101

```

Bien sûr, vous pouvez également faire en sorte que tar envoie vos fichiers extraits à un autre endroit en utilisant l'argument `-C`, suivi de l'emplacement cible :

```
$ tar xvf archivename.tar -C /home/mydata/oldfiles/

```

Vous ne voudrez pas toujours inclure tous les fichiers d'une arborescence de répertoires dans votre archive. 

Supposons que vous avez produit des vidéos, mais qu'elles sont actuellement conservées dans des répertoires avec toutes sortes de fichiers graphiques, audio et texte (contenant vos notes). Les seuls fichiers que vous devez sauvegarder sont les clips vidéo finaux utilisant l'extension de nom de fichier .mp4. 

Voici comment faire :

```
$ tar cvf archivename.tar *.mp4

```

C'est bien. Mais ces fichiers vidéo sont énormes. Ne serait-il pas agréable de rendre cette archive un peu plus petite en utilisant la compression ? 

Ne dites plus rien ! Il suffit d'exécuter la commande précédente avec l'argument `z` (zip). Cela indiquera au programme gzip de compresser l'archive. 

Si vous souhaitez suivre la convention, vous pouvez également ajouter une extension `.gz` en plus du `.tar` qui est déjà là. Rappelez-vous : la clarté.

Voici comment cela se passerait :

```
$ tar czvf archivename.tar.gz *.mp4

```

Si vous essayez cela sur vos propres fichiers .mp4 et que vous exécutez ensuite ls -l sur le répertoire contenant les nouvelles archives, vous remarquerez peut-être que le fichier `.tar.gz` n'est pas beaucoup plus petit que le fichier `.tar`, peut-être 10 % ou moins. Qu'est-ce que c'est que ça ? 

Eh bien, le format de fichier `.mp4` est lui-même compressé, donc il y a beaucoup moins de place pour que gzip fasse son travail.

Comme tar est parfaitement conscient de son environnement Linux, vous pouvez l'utiliser pour sélectionner des fichiers et des répertoires qui se trouvent en dehors de votre répertoire de travail actuel. Cet exemple ajoute tous les fichiers `.mp4` dans le répertoire `/home/myuser/Videos/` :

```
$ tar czvf archivename.tar.gz /home/myuser/Videos/*.mp4

```

Parce que les fichiers d'archive peuvent devenir volumineux, il peut parfois être judicieux de les diviser en plusieurs fichiers plus petits, de les transférer vers leur nouvel emplacement, puis de recréer le fichier original à l'autre extrémité. L'outil split est fait à cet effet.

Dans cet exemple, `-b` indique à Linux de diviser le fichier archivename.tar.gz en parties de 1 Go. L'opération nomme ensuite chacune des parties—archivename.tar.gz.partaa, archivename.tar.gz.partab, archivename.tar.gz.partac, et ainsi de suite :

```
$ split -b 1G archivename.tar.gz "archivename.tar.gz.part"

```

De l'autre côté, vous recréez l'archive en lisant chacune des parties en séquence (cat archivename.tar.gz.part*), puis vous redirigez la sortie vers un nouveau fichier appelé archivename.tar.gz :

```
$ cat archivename.tar.gz.part* > archivename.tar.gz

```

# Archives de système de fichiers en streaming

Voici où commence le bon matériel. Je vais vous montrer comment créer une image d'archive d'une installation Linux fonctionnelle et la diffuser vers un emplacement de stockage distant — le tout en une seule commande. Voici la commande :

```
# tar czvf - --one-file-system / /usr /var \
  --exclude=/home/andy/ | ssh username@10.0.3.141 \
  "cat > /home/username/workstation-backup-Apr-10.tar.gz"

```

Plutôt que d'essayer d'expliquer tout cela tout de suite, je vais utiliser des exemples plus petits pour l'explorer pièce par pièce. 

Créons une archive du contenu d'un répertoire appelé importantstuff qui est rempli de, eh bien, des choses vraiment importantes :

```
$ tar czvf - importantstuff/ | ssh username@10.0.3.141 "cat > /home/username/myfiles.tar.gz"
importantstuff/filename1
importantstuff/filename2
[...]
username@10.0.3.141's password:

```

Permettez-moi d'expliquer cet exemple. Plutôt que de saisir le nom de l'archive juste après les arguments de la commande (comme vous l'avez fait jusqu'à présent), j'ai utilisé un tiret (czvf -). 

Le tiret envoie les données vers la sortie standard. Il vous permet de repousser les détails du nom de fichier de l'archive à la fin de la commande et indique à tar de s'attendre au contenu source de l'archive à la place. 

J'ai ensuite redirigé (|) l'archive compressée sans nom vers une connexion ssh sur un serveur distant où l'on m'a demandé mon mot de passe. 

La commande enfermée entre guillemets a ensuite exécuté cat contre le flux de données de l'archive, ce qui a écrit le contenu du flux dans un fichier appelé myfiles.tar.gz dans mon répertoire personnel sur l'hôte distant.

Un avantage de la génération d'archives de cette manière est que vous évitez le surcoût d'une étape intermédiaire. Il n'est même pas nécessaire de sauvegarder temporairement une copie de l'archive sur la machine locale. Imaginez sauvegarder une installation qui remplit 110 Go de ses 128 Go d'espace disponible. Où irait l'archive ?

Ce n'était qu'un répertoire de fichiers. Supposons que vous devez sauvegarder un système d'exploitation Linux actif sur une clé USB afin de pouvoir le déplacer vers une machine séparée et le déposer dans le lecteur principal de cette machine.

En supposant qu'il y a déjà une nouvelle installation de la même version de Linux sur la deuxième machine, l'opération de copier/coller suivante générera une réplique exacte de la première.

> NOTE : Cela ne fonctionnera pas sur un lecteur cible qui n'a pas déjà un système de fichiers Linux installé. Pour gérer cette situation, vous devrez utiliser `dd`.

L'exemple suivant crée une archive compressée sur la clé USB connue sous le nom de `/dev/sdc1`. 

L'argument `--one-file-system` exclut toutes les données de tout système de fichiers autre que le système actuel. Cela signifie que les pseudo-partitions comme `/sys/` et `/dev/` ne seront pas ajoutées à l'archive. Si vous avez d'autres partitions que vous souhaitez inclure (comme vous le ferez pour `/usr/` et `/var/` dans cet exemple), alors elles doivent être ajoutées explicitement. 

Enfin, vous pouvez exclure des données du système de fichiers actuel en utilisant l'argument `--exclude` :

```
# tar czvf /dev/sdc1/workstation-backup-Apr-10.tar.gz \
  --one-file-system \
  / /usr /var \
  --exclude=/home/andy/

```

Maintenant, revenons à cet exemple de commande complète. En utilisant ce que vous avez déjà appris, archivez tous les répertoires importants d'un système de fichiers et copiez le fichier d'archive sur une clé USB. Cela devrait maintenant avoir du sens pour vous :

```
# tar czvf - --one-file-system / /usr /var \
  --exclude=/home/andy/ | ssh username@10.0.3.141 \
  "cat > /home/username/workstation-backup-Apr-10.tar.gz"

```

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/)._