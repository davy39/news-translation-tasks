---
title: Network File System – Comment confirmer que votre application utilise NFS
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2023-09-18T06:54:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-confirm-your-application-is-using-nfs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725458376947/86a9c2e5-a07d-4802-82e4-dd8c28aebbc5.jpeg
tags:
- name: computer networking
  slug: computer-networking
seo_title: Network File System – Comment confirmer que votre application utilise NFS
seo_desc: 'I was tasked recently to find which of our processes was accessing an NFS
  share. During this process, I found that some tools are better adapted than others
  for the task.

  In this article, I want to share with you my findings. The whole process was fu...'
---

J'ai récemment été chargé de trouver quel processus accédait à un partage NFS. Lors de cette tâche, j'ai découvert que certains outils sont mieux adaptés que d'autres pour cette mission.

Dans cet article, je souhaite partager avec vous mes découvertes. L'ensemble du processus a été amusant et m'a donné des idées sur la façon d'utiliser ces outils pour résoudre des problèmes similaires à l'avenir.

## Qu'est-ce que NFS ?

Network File System (NFS) est un protocole de système de fichiers distribué qui permet à un utilisateur d'accéder à des fichiers via un réseau informatique.

Veuillez noter que ceci n'est pas un tutoriel complet sur NFS. Pour cela, veuillez consulter le [tutoriel](https://www.redhat.com/sysadmin/getting-started-nfs).

Dans cet article, nous nous concentrerons uniquement sur la détection de l'accès à un lecteur partagé en utilisant plusieurs techniques ainsi que sur la configuration de deux serveurs et d'un client.

De plus, j'utilise un système d'exploitation différent pour configurer à la fois le serveur et le client, donc les instructions pour effectuer la tâche changent un peu.

## Comment configurer un serveur et un client NFS

Mon environnement de laboratoire comprend un serveur NFS et deux clients :

![](https://github.com/josevnz/tutorials/blob/main/docs/SpyOnNfs/NfsLayout.png?raw=true align="left")

Dans ma configuration, j'aurai trois ordinateurs communiquant entre eux. L'un d'eux sera le serveur NFS et les deux autres seront des clients.

| Machine | OS | Matériel | Mode |
| --- | --- | --- | --- |
| OrangePi5 | Ubuntu Armbian 23.8.1 jammy | Orange Pi 5 | Serveur:/data |
| RaspberriPi | Debian 20.04.4 LTS (Focal Fossa) | Raspberry Pi 4 Model B Rev 1.4 | Serveur:/var/log/suricata |
| Dmaf5 | Fedora 37 (Workstation Edition) | AMD Ryzen 5 3550H avec Radeon Vega Mobile Gfx | Client |

### Comment configurer le serveur

Je vais préparer ma machine OrangePI pour qu'elle soit le serveur NFS. Pour cela, je vais entrer les commandes suivantes :

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nfs-kernel-server -y
sudo systemctl enable nfs-kernel-server.service --now
```

L'étape suivante consiste à indiquer au [serveur ce que nous voulons partager](https://ubuntu.com/server/docs/service-nfs).

Pour cela, nous allons éditer le fichier [/etc/exports](https://www.man7.org/linux/man-pages/man5/exports.5.html) (`sudo vi /etc/exports history`) :

```text
/data *(ro,all_squash,async,no_subtree_check)
```

Veuillez consulter la page man pour comprendre ce que signifient ces options.

En résumé, l'exportation de /data :

* Est en lecture seule

* Mappe les ID à un ID anonyme

* Cette option permet au serveur NFS de violer le protocole NFS et de répondre aux requêtes avant que les modifications apportées par cette requête n'aient été validées dans un stockage stable

* Cette option désactive la vérification des sous-arborescences. C'est le comportement par défaut.

Il est maintenant temps d'activer nos répertoires partagés :

```shell
root@orangepi5:~# sudo exportfs -a
root@orangepi5:~# sudo showmount -e
Export list for orangepi5:
/data (everyone)
```

J'ai fait quelque chose de similaire sur l'autre hôte, raspberrypi :

```shell
root@raspberrypi:~# cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#		to NFS clients.  See exports(5).
#
/var/log/suricata *(ro,all_squash,async,no_subtree_check)
root@raspberrypi:~# showmount -e
Export list for raspberrypi:
/var/log/suricata *
```

### Comment configurer le client

La première chose à faire est de confirmer que nous pouvons effectivement voir les points de montage partagés depuis notre serveur :

```shell
(tutorials) [josevnz@dmaf5 SpyOnNfs]$ sudo showmount -e orangepi5
Export list for orangepi5:
/data raspberrypi,dmaf5
```

Les données sont partagées avec deux machines – exactement ce à quoi nous nous attendions.

Il existe plusieurs façons de monter ce lecteur. L'une d'elles est manuelle, une autre au démarrage, et la dernière, ma préférée, est à la demande.

#### Comment configurer le client AutoMount sur Fedora Linux

Tout d'abord, nous [configurons le service](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/system_administration_guide/mounting_nfs_file_systems-mounting_nfs_file_systems_using_autofs) :

```shell
sudo dnf install -y autofs
sudo systemct enable autofs.service --now
```

Ensuite, nous configurons cela pour terminer le montage du `/data` distant dans le `/misc/data` local. Pour cela, ajoutez la ligne suivante à votre `/etc/auto.master` :

```shell
[root@dmaf5 ~]# vi /etc/auto.misc
# Après avoir édité le fichier, ajout de notre entrée à la dernière ligne du fichier ...
[root@dmaf5 ~]# cat /etc/auto.misc
#
# This is an automounter map and it has the following format
# key [ -mount-options-separated-by-comma ] location
# Details may be found in the autofs(5) manpage

cd              -fstype=iso9660,ro,nosuid,nodev :/dev/cdrom

data            -ro,soft,rsize=16384,wsize=16384 orangepi5:/data
suricata        -ro,soft,rsize=16384,wsize=16384 raspberrypi:/var/log/suricata
```

Redémarrez le service une fois de plus :

```shell
[root@dmaf5 ~]# systemctl enable autofs.service --now
```

Et le test de fumée :

```shell
[root@dmaf5 ~]# ls -l /misc/data
total 0
drwxrwxr-x. 1 root 1001 48 Apr  7 17:57 nexus
[root@dmaf5 ~]# ls /misc/suricata
certs       eve.json.7  files            http.log    stats.log.1     suricata.log.2        suricata-start.log.3  tls.log.4
core        fast.log    http-data.log    http.log.1  stats.log.2     suricata.log.3        suricata-start.log.4  tls.log.5
eve.json    fast.log.1  http-data.log.1  http.log.2  stats.log.3     suricata.log.4        suricata-start.log.5  tls.log.6
eve.json.1  fast.log.2  http-data.log.2  http.log.3  stats.log.4     suricata.log.5        suricata-start.log.6  tls.log.7
eve.json.2  fast.log.3  http-data.log.3  http.log.4  stats.log.5     suricata.log.6        suricata-start.log.7
eve.json.3  fast.log.4  http-data.log.4  http.log.5  stats.log.6     suricata.log.7        tls.log
eve.json.4  fast.log.5  http-data.log.5  http.log.6  stats.log.7     suricata-start.log    tls.log.1
eve.json.5  fast.log.6  http-data.log.6  http.log.7  suricata.log    suricata-start.log.1  tls.log.2
eve.json.6  fast.log.7  http-data.log.7  stats.log   suricata.log.1  suricata-start.log.2  tls.log.3
```

Nous sommes maintenant prêts à utiliser notre service.

## Comment créer un programme Python qui lit des fichiers dans le serveur NFS

Pour notre exemple, nous voulons déterminer si une application Python lit des données depuis ce répertoire. Ce script a deux fonctionnalités :

* Effectue une lecture ponctuelle d'un fichier. Cela nous apprendra à capturer ce type de scénarios, lorsqu'un fichier n'est pas ouvert en permanence.

* Et le script suit également les mises à jour d'un fichier périodiquement.

Voici à quoi ressemble notre script de test en action :

```shell
./scripts/test_script.py \
--quick_read /misc/data/nexus/log/jvm.log \
--follow /misc/suricata/eve.json \
--verbose
...
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,889 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,890 <dependency_failed type='leaf_type' ctxk='java/io/FileOutputStream' witness='java/net/SocketOutputStream' stamp='66511.794'/>
2023-09-10 14:48:22,890 <dependency_failed type='unique_concrete_method' ctxk='java/io/ByteArrayOutputStream' x='java/io/ByteArrayOutputStream write ([BII)V' witness='sun/security/ssl/HandshakeOutStream' stamp='66511.855'/>
2023-09-10 14:48:22,890 <dependency_failed type='unique_concrete_method' ctxk='java/io/ByteArrayOutputStream' x='java/io/ByteArrayOutputStream write ([BII)V' witness='sun/security/ssl/HandshakeOutStream' stamp='66511.855'/>
...
# Ctrl-C pour quitter
```

Le code, écrit en Python, est assez simple :

```python
#!/usr/bin/env python
"""
Script simple pour simuler une activité légère sur les lecteurs NFS
Auteur Jose Vicente Nunez (kodegeek.com@protonmail.com)
"""
import concurrent
import os
import time
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED
from pathlib import Path
from argparse import ArgumentParser
import logging

logging.basicConfig(format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)


def forever_read(the_file: Path, verbose: bool = False):
    for line in continuous_read(the_file=the_file):
        if verbose:
            logging.warning(line.strip())


def continuous_read(the_file: Path):
    """
    Lit continuellement le contenu du fichier
    :param the_file:
    :return:
    """
    with open(the_file, 'r') as file_data:
        file_data.seek(0, os.SEEK_END)
        while True:
            line = file_data.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


def quick_read(the_file: Path, verbose: bool = False):
    """
    Lit le fichier entier et le ferme une fois terminé
    :param verbose:
    :param the_file:
    :return:
    """
    with open(the_file, 'r') as file_data:
        for line in file_data:
            if verbose:
                logging.warning(line.strip())


if __name__ == "__main__":
    PARSER = ArgumentParser(description=__doc__)
    PARSER.add_argument(
        '--verbose',
        action='store_true',
        default=False,
        help='Activer le mode verbeux'
    )
    PARSER.add_argument(
        '--quick_read',
        type=Path,
        required=True,
        help='Lire un fichier une fois'
    )
    PARSER.add_argument(
        '--follow',
        type=Path,
        required=True,
        help='Lire un fichier en continu'
    )
    OPTIONS = PARSER.parse_args()
    try:
        with ThreadPoolExecutor(max_workers=3) as tpe:
            futures = [
                tpe.submit(forever_read, OPTIONS.follow, OPTIONS.verbose),
                tpe.submit(quick_read, OPTIONS.quick_read, OPTIONS.verbose)
            ]
            concurrent.futures.wait(futures, return_when=ALL_COMPLETED)
    except KeyboardInterrupt:
        pass
```

Maintenant, voyons comment nous pouvons voir si notre script accède effectivement à une partition NFS.

### Étapes communes

Tout d'abord, nous devons apprendre où chercher. Donc sur la machine, vérifiez NFS dans `/etc/fstab` (pour les points de montage disponibles depuis le redémarrage de la machine) :

```shell
[root@dmaf5 ~]# rg -e 'rsize=' /etc/fstab
```

Ensuite, dans les fichiers AutoMount :

```shell
[root@dmaf5 ~]# rg -e 'rsize=' /etc/auto*
/etc/auto.misc
17:data            -ro,soft,rsize=16384,wsize=16384 orangepi5:/data
18:suricata        -ro,soft,rsize=16384,wsize=16384 raspberrypi:/var/log/suricata
```

Les expressions régulières ne sont pas une science exacte, mais vous avez une idée de ce qu'il faut chercher ensuite.

### Comment utiliser les outils

Nous devons confirmer s'il y a eu accès à l'une des partitions suivantes montées via NFS :

* `/misc/data`

* `/misc/suricata`

Ensuite, je vais vous montrer un ensemble d'outils qui faciliteront la tâche, chacun avec ses propres forces et limitations.

Commençons par [lsof](https://www.redhat.com/sysadmin/analyze-processes-lsof) et [ripgrep](https://github.com/BurntSushi/ripgrep) combinés.

### Comment utiliser Lsof et rg pour capturer et filtrer

```shell
[josevnz@dmaf5 docs]$ lsof -w -b| rg -e '/misc/data|/misc/suricata'
python    36509                 josevnz    3   unknown                           /misc/suricata/eve.json
python    36509 36510 python    josevnz    3   unknown                           /misc/suricata/eve.json
python    36509 36511 python    josevnz    3   unknown                           /misc/suricata/eve.json
```

J'ai passé l'option `-b` à lsof pour éviter qu'il ne se bloque, au cas où le [handle NFS serait obsolète](https://access.redhat.com/solutions/2674).

Quelques points sur lsof :

* Si vous utilisez Autofs, vous devez savoir que les points de montage sont éventuellement démontés pour économiser la bande passante. Cela peut poser problème lorsque vous essayez de capturer l'accès à un fichier qui n'est ouvert qu'une seule fois.

* La lecture de courte durée n'est pas apparue car le handle de fichier a été fermé après que nous avons inspecté le processus.

* Si vous souhaitez surveiller TOUS les processus sur cette machine, vous devrez peut-être exécuter en tant que root. Vous ne pouvez inspecter que vos propres processus sans privilèges spéciaux.

Néanmoins, lsof est un excellent outil d'investigation.

La stratégie suivante consiste à surveiller dès le début, pour capturer la lecture courte et insaisissable. Nous utiliserons [strace](https://strace.io/).

### Comment utiliser strace

```shell
sudo dnf install -y strace
(tutorials) [josevnz@dmaf5 SpyOnNfs]$ strace -f ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json 2>&1| rg -e '/misc/data|/misc/suricata'
execve("./scripts/test_script.py", ["./scripts/test_script.py", "--quick_read", "/misc/data/nexus/log/jvm.log", "--follow", "/misc/suricata/eve.json"], 0x7ffd9ae29738 /* 46 vars */) = 0
execve("/home/josevnz/virtualenv/tutorials/bin/python", ["python", "./scripts/test_script.py", "--quick_read", "/misc/data/nexus/log/jvm.log", "--follow", "/misc/suricata/eve.json"], 0x7ffe269dbf88 /* 46 vars */) = 0
[pid 38241] openat(AT_FDCWD, "/misc/suricata/eve.json", O_RDONLY|O_CLOEXEC <unfinished ...>
[pid 38242] openat(AT_FDCWD, "/misc/data/nexus/log/jvm.log", O_RDONLY|O_CLOEXEC <unfinished ...>
```

Les entrées `openat(AT_FDCWD)` révèlent les deux fichiers que notre script lit depuis NFS. Mais comme vous pouvez le constater, cette approche présente quelques inconvénients :

* Nous filtrons la sortie. Il est préférable d'enregistrer la sortie dans un fichier avec 'tee' et de rechercher ensuite

* Il nécessite de démarrer le processus avec strace dès le début. Oui, vous pourriez faire un 'strace -p $PID' pour vous attacher plus tard au processus, mais vous risquez de manquer les lectures de courte durée

Y a-t-il une autre façon ? Passons à l'outil suivant, [tshark](https://www.wireshark.org/docs/man-pages/tshark.html) et voyons comment utiliser une capture réseau pour confirmer l'accès au partage.

### Comment utiliser tshark

Nous pouvons également capturer le trafic réseau et filtrer uniquement NFS. [Ce n'est pas parfait](https://ask.wireshark.org/question/3582/how-to-capture-filename-path-for-nfsv4-traffic-using-tshark/), mais cela peut suffire.

Tout d'abord, découvrez quelle interface réseau est utilisée pour communiquer avec le serveur NFS. Dans mon cas, c'est facile – ils sont tous connectés en utilisant un réseau privé filaire :

```shell
[josevnz@dmaf5 docs]$ ip --oneline address|rg -e 'eno|wlp'
3: eno1    inet 192.168.68.70/22 brd 192.168.71.255 scope global dynamic noprefixroute eno1\       valid_lft 4568sec preferred_lft 4568sec
4: wlp4s0    inet 192.168.1.95/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp4s0\       valid_lft 3423sec preferred_lft 3423sec
4: wlp4s0    inet6 fe80::ac40:5365:7f09:a5d2/64 scope link noprefixroute \       valid_lft forever preferred_lft forever
```

Pour cet exemple, il s'agit de eno1 avec l'adresse IP '192.168.68.70'. Ensuite, capturez le trafic, et avec un peu de chance, nous obtiendrons le chemin du fichier :

```shell
[root@dmaf5 ~]# tshark -i eno1 -Y "nfs"
Running as user "root" and group "root". This could be dangerous.
Capturing on 'eno1'
 ** (tshark:42326) 16:02:47.417145 [Main MESSAGE] -- Capture started.
 ** (tshark:42326) 16:02:47.417286 [Main MESSAGE] -- File: "/var/tmp/wireshark_eno1rEGxiu.pcapng"
   13 1.601197994 192.168.68.70 → 192.168.68.60 NFS 450 V4 Call GETATTR FH: 0x90ba4ee1  ; V4 Call GETATTR FH: 0x90ba4ee1
   14 1.601374466 192.168.68.70 → 192.168.68.60 NFS 258 V4 Call GETATTR FH: 0x90ba4ee1
   15 1.601395155 192.168.68.70 → 192.168.68.60 NFS 258 V4 Call GETATTR FH: 0x90ba4ee1
   16 1.602155254 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 13) GETATTR
   17 1.602368826 192.168.68.60 → 192.168.68.70 NFS 554 V4 Reply (Call In 13) GETATTR  ; V4 Reply (Call In 14) GETATTR
   19 1.602515091 192.168.68.70 → 192.168.68.60 NFS 274 V4 Call READ StateID: 0xa902 Offset: 57552896 Len: 12288
   20 1.602557170 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 15) GETATTR
   22 1.603156327 192.168.68.60 → 192.168.68.70 NFS 1730 V4 Reply (Call In 19) READ
   66 4.611124808 192.168.68.70 → 192.168.68.60 NFS 642 V4 Call GETATTR FH: 0x90ba4ee1  ; V4 Call GETATTR FH: 0x90ba4ee1  ; V4 Call GETATTR FH: 0x90ba4ee1
   67 4.611301059 192.168.68.70 → 192.168.68.60 NFS 258 V4 Call GETATTR FH: 0x90ba4ee1
   68 4.611809385 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 66) GETATTR
   69 4.611887552 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 66) GETATTR
   71 4.611976479 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 66) GETATTR
   72 4.620685968 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 67) GETATTR
   74 5.017200005 192.168.68.70 → 192.168.68.60 NFS 250 V4 Call GETATTR FH: 0x9419c00c
   75 5.017804843 192.168.68.70 → 192.168.68.59 NFS 242 V4 Call GETATTR FH: 0x314e720f
   76 5.017838787 192.168.68.60 → 192.168.68.70 NFS 310 V4 Reply (Call In 74) GETATTR
   77 5.018131217 192.168.68.70 → 192.168.68.60 NFS 326 V4 Call OPEN DH: 0x90ba4ee1/
   78 5.018711408 192.168.68.60 → 192.168.68.70 NFS 386 V4 Reply (Call In 77) OPEN StateID: 0x9984
   79 5.018855699 192.168.68.59 → 192.168.68.70 NFS 310 V4 Reply (Call In 75) GETATTR
   81 5.018980434 192.168.68.70 → 192.168.68.59 NFS 262 V4 Call GETATTR FH: 0xecd332cc
   82 5.019934959 192.168.68.59 → 192.168.68.70 NFS 310 V4 Reply (Call In 81) GETATTR
   83 5.020032853 192.168.68.70 → 192.168.68.59 NFS 262 V4 Call GETATTR FH: 0x261d4440
   84 5.020734032 192.168.68.59 → 192.168.68.70 NFS 310 V4 Reply (Call In 83) GETATTR
   85 5.020874175 192.168.68.70 → 192.168.68.59 NFS 330 V4 Call OPEN DH: 0xc9b4831b/
```

C'est génial, il y a de l'activité contre deux serveurs NFS, 192.168.68.59 et 192.168.68.60. Mais, y a-t-il un moyen de voir le nom des fichiers ?

tshark a un moyen de fournir des informations par champ. Le problème est que NFS en a beaucoup :

```shell
[root@dmaf5 ~]# for field in $(tshark -G fields| cut -d'        ' -f3|rg -e '^nfs\.'); do echo "-e $field"; done|head -n 10
Running as user "root" and group "root". This could be dangerous.
-e nfs.unknown
-e nfs.svr4
-e nfs.knfsd_le
-e nfs.nfsd_le
-e nfs.knfsd_new
-e nfs.ontap_v3
-e nfs.ontap_v4
-e nfs.ontap_gx_v3
-e nfs.celerra_vnx
-e nfs.gluster
```

Alors, [capturons-les](https://www.wireshark.org/docs/dfref/n/nfs.html) dans une variable ([nous devons également activer certaines options](https://wiki.wireshark.org/NFS_Preferences)) :

```shell
[root@dmaf5 ~]# fields=$(for field in $(tshark -G fields| cut -d'       ' -f3|rg -e '^nfs\.'); do echo "-e $field"; done)
[root@dmaf5 ~]# tshark -i eno1 --enable-protocol nfs -o nfs.file_name_snooping:true -o nfs.file_full_name_snooping:true -T fields -E header=y -E separator=, -E quote=d $fields
Running as user "root" and group "root". This could be dangerous.
nfs.unknown,nfs.svr4,nfs.knfsd_le,nfs.nfsd_le,nfs.knfsd_new,nfs.ontap_v3,nfs.ontap_v4,nfs.ontap_gx_v3,n...
```

J'ai réussi à obtenir le nom de fichier une seule fois, puis après avoir interrompu et redémarré le programme, je n'ai plus eu de chance.

Et pourtant, aucun signe du nom de fichier. Le handle de fichier était dans le contenu, mais ce n'est pas très utile si vous voulez une façon rapide de voir ce qui a été accédé.

Y a-t-il un moyen plus facile de faire cela ? Sysdig peut offrir quelques réponses.

### Comment utiliser Sysdig

En essayant de trouver les points de montage insaisissables, je suis tombé sur [Sysdig](https://github.com/draios/sysdig) :

Sysdig instrument vos machines physiques et virtuelles au niveau du système d'exploitation en s'installant dans le noyau Linux et en capturant les appels système et autres événements du système d'exploitation. Sysdig utilise [DTrace](https://en.wikipedia.org/wiki/DTrace) pour accéder au noyau du système.

Sysdig permet également de créer des fichiers de trace pour l'activité du système, de manière similaire à ce que vous pouvez faire pour les réseaux avec des outils comme tcpdump et Wireshark.

J'ai décidé d'utiliser la dernière version ([0.33.1](https://github.com/draios/sysdig/releases/tag/0.33.1)) pour Fedora 37 où mon script est en cours d'exécution :

```shell
sudo dnf install -y https://github.com/draios/sysdig/releases/download/0.33.1/sysdig-0.33.1-x86_64.rpm
# Attendez un peu, car un module noyau doit être compilé et préparé...
Installed:
  bison-3.8.2-3.fc37.x86_64                    dkms-3.0.11-1.fc37.noarch          elfutils-libelf-devel-0.189-3.fc37.x86_64  flex-2.6.4-11.fc37.x86_64            kernel-devel-6.4.13-100.fc37.x86_64 
  kernel-devel-matched-6.4.13-100.fc37.x86_64  libzstd-devel-1.5.5-1.fc37.x86_64  m4-1.4.19-4.fc37.x86_64                    openssl-devel-1:3.0.9-1.fc37.x86_64  sysdig-0.33.1-1.x86_64              
  zlib-devel-1.2.12-5.fc37.x86_64
```

À quel point est-il facile de sonder le script pour confirmer qu'il accède effectivement aux répertoires montés NFS ? Imprimons trois champs d'intérêt et le nom du fichier accédé :

```shell
# `sysdig -l` affichera chaque champ que vous pouvez capturer
[root@dmaf5 ~]# sysdig -p"%proc.cmdline,%fd.name" proc.name contains python and fd.name contains /misc
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
...
```

Et si vous souhaitez capturer toutes les données et filtrer plus tard ? Une façon de faire est de capturer dans un fichier :

```shell
# Capture pendant une minute...
[root@dmaf5 ~]# timeout --preserve-status 1m sysdig -w /tmp/sysdig.dump
[root@dmaf5 ~]# ls -lh /tmp/sysdig.dump
-rw-r--r--. 1 root root 32M Sep 10 19:03 /tmp/sysdig.dump
```

Puis relisez le contenu, avec filtrage (la relecture ne nécessite pas de privilèges élevés) :

```shell
[root@dmaf5 ~]# sysdig -r /tmp/sysdig.dump -p"%proc.cmdline,%fd.name" proc.name contains python and fd.name contains /misc|sort -u
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/data/nexus/log/jvm.log
python ./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose,/misc/suricata/eve.json
```

Sysdig prend en charge le scripting, en utilisant le [langage LUA](https://www.lua.org/). Par exemple, il dispose d'une version très pratique de lsof :

```shell
[root@dmaf5 ~]# sysdig -cl|rg lsof
lsof            List (and optionally filter) the open file descriptors.
```

Alors utilisons-le :

```shell
[root@dmaf5 ~]# sysdig -c lsof|rg misc
automount           52410   52410   root    8       directory   /misc
automount           52410   52413   root    8       directory   /misc
automount           52410   52414   root    8       directory   /misc
automount           52410   52415   root    8       directory   /misc
automount           52410   52418   root    8       directory   /misc
automount           52410   52421   root    8       directory   /misc
python              75840   75840   josevnz 3       file        /misc/suricata/eve.json
python              75840   75841   josevnz 3       file        /misc/suricata/eve.json
python              75840   75842   josevnz 3       file        /misc/suricata/eve.json
```

Ce que j'ai aimé dans cet outil :

* Peut fonctionner avec des noyaux plus anciens (comme 4.xx)

* Dispose d'un langage d'expression puissant pour le filtrage

* Facile à apprendre et bien documenté

* Vous pouvez écrire vos propres scripts si vous connaissez LUA

Avant de terminer, regardons un autre outil, BPF.

### Comment utiliser la sonde BPF

À l'origine Berkeley Packet Filter, est un schéma d'observabilité du noyau et de l'espace utilisateur pour Linux.

Le BPF est un [outil très puissant](https://www.linuxjournal.com/content/bpf-observability-getting-started-quickly), et cet article court ne fera même pas effleurer la surface.

Oui, c'est énorme. Je l'apprends moi-même.

J'ai trouvé que le [dépôt bcc](https://github.com/iovisor/bcc) contient de nombreux scripts prêts à l'emploi que nous pourrions utiliser pour suivre notre accès NFS, et même vérifier les performances (vous pouvez trouver plus d'exemples [ici](https://github.com/iovisor/bpftrace), et sur le [dépôt BPF Performance Book](https://github.com/brendangregg/bpf-perf-tools-book/tree/master)).

Mais il est plus intéressant d'écrire des outils vous-même qui surveillent à peu près tout ce que vous voulez. Pour ce tutoriel, j'utiliserai certains programmes prêts à l'emploi qui utilisent les traces pour capturer des informations utiles.

En premier lieu, nous devrons installer un interpréteur de haut niveau pour nos scripts. Encore une fois, sur ma machine Fedora Linux :

```shell
[josevnz@dmaf5 ~]$ sudo dnf install -y bpftrace.x86_64 bcc-tools.x86_64
# Et vérifiez si le noyau a btf activé
[josevnz@dmaf5 ~]$ ls -la /sys/kernel/btf/vmlinux
-r--r--r--. 1 root root 5635179 Sep 12 04:21 /sys/kernel/btf/vmlinux
```

Dans un terminal séparé, relancez le script de test NFS :

```shell
. ~/virtualenv/tutorials/bin/activate
cd SpyOnNfs/
./scripts/test_script.py --quick_read /misc/data/nexus/log/jvm.log --follow /misc/suricata/eve.json --verbose
```

Vous pouvez tracer tous les fichiers ouverts par un programme, comme top :

```shell
18:59:20 loadavg: 1.20 1.00 0.74 1/1175 28520

TID     COMM             READS  WRITES R_Kb    W_Kb    T FILE
28520   clear            2      0      60      0       R xterm-256color
28203   python           7      0      56      0       R eve.json
28347   filetop          2      0      15      0       R loadavg
824     systemd-oomd     2      0      8       0       R memory.swap.current
824     systemd-oomd     2      0      8       0       R memory.low
...
```

Mais il n'imprime pas le chemin complet. Il est plus utile de demander un espion NFS et de voir si l'un de nos fichiers apparaît :

```shell
[josevnz@dmaf5 SuricataLog]$ sudo /usr/share/bcc/tools/nfsslower 1
# Commented out some warnings ...
Tracing NFS operations that are slower than 1 ms... Ctrl-C to quit
TIME     COMM           PID    T BYTES   OFF_KB   LAT(ms) FILENAME
19:02:25 python         28202  R 1460    62150       1.96 eve.json
19:02:28 python         28202  R 2446    62151       2.09 eve.json
19:02:31 python         28202  R 970     62154       1.99 eve.json
19:02:34 python         28202  R 3335    62155       2.43 eve.json
19:02:37 python         28202  R 4564    62158       1.84 eve.json
19:02:40 python         28202  R 5876    62162       1.89 eve.json
19:02:43 python         28202  R 4504    62168       1.61 eve.json
19:02:46 python         28202  R 3131    62173       1.92 eve.json
```

C'est beaucoup mieux. De plus, nous pouvons voir que la latence est presque de deux millisecondes.

Nous pouvons également surveiller les opérations de montage/démontage :

```shell
[josevnz@dmaf5 SuricataLog]$ sudo /usr/share/bcc/tools/mountsnoop 
# Commented out some warnings ...
2 warnings generated.
COMM             PID     TID     MNT_NS      CALL
mount.nfs        29012   29012   4026531841  mount("orangepi5:/data", "/misc/data", "nfs", MS_RDONLY, "sloppy,soft,rsize=16384,wsize=16384,vers=4.2,addr=192.168.68.59,clientaddr=192.168.68.68") = 0
```

C'est bien aussi, nous pouvons voir l'activité sur NFS que nous voulions confirmer.

## Prochaines étapes

Vous avez appris plusieurs outils et, comme vous l'avez peut-être deviné, vous pouvez les utiliser pour espionner plus que simplement les fichiers ouverts sur NFS.

Il est toujours utile de connaître plus d'un outil. Sysdig mérite une mention spéciale pour être très polyvalent, puissant et pourtant facile à utiliser. De plus, il peut être étendu avec des scripts écrits en langage LUA.

BPF est une autre alternative et vous donnera un accès incroyable aux appels du noyau. Préparez-vous à passer du temps à lire et à apprendre comment utiliser les outils.

Le code des scripts utilisés dans ce tutoriel peut être obtenu depuis mon [dépôt GitHub : SpyOnNfs](https://github.com/josevnz/tutorials/tree/main/docs/SpyOnNfs).