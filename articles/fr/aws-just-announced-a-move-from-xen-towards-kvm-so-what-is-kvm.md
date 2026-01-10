---
title: AWS annonce un passage de Xen vers KVM. Alors, qu'est-ce que KVM ?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-31T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-just-announced-a-move-from-xen-towards-kvm-so-what-is-kvm
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/xen-kvm.png
tags:
- name: Linux
  slug: linux
- name: virtualization
  slug: virtualization
seo_title: AWS annonce un passage de Xen vers KVM. Alors, qu'est-ce que KVM ?
seo_desc: Tied up in a AWS announcement about a new EC2 high-end instance type (the
  C5) is a strong suggestion that Amazon’s cloud computing giant has begun to shift
  its hundreds of thousands of physical servers away from the open source Xen hypervisor
  that’s ...
---

Dans une annonce d'AWS concernant un nouveau type d'instance EC2 haut de gamme (le C5), il y a [une forte suggestion](https://www.theregister.co.uk/2017/11/07/aws_writes_new_kvm_based_hypervisor_to_make_its_cloud_go_faster/) que le géant du cloud computing d'Amazon a commencé à migrer ses centaines de milliers de serveurs physiques de l'hyperviseur open source Xen qui les a fait fonctionner jusqu'à présent, vers l'alternative open source, KVM.

Que vous ayez votre carrière et/ou votre prêt immobilier profondément investis dans l'avenir de Xen ou que vous ne saviez même pas qu'il existait, vous pourriez être intéressé à en apprendre davantage sur KVM. Voici donc une introduction générale adaptée de mon livre, [Teach Yourself](https://www.amazon.com/gp/product/B06XTZ4YWQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06XTZ4YWQ&linkCode=as2&tag=projemun-20&linkId=fa7577d96ed91ffe111b08665bcb53f9) [Linux Virtualization and High Availability: prepare for the LPIC-3 304 certification exam](https://bootstrap-it.com/index.php/books/).

> _Besoin de plus de bases sur les serveurs Linux ou AWS ? Mes livres [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) et [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27) de Manning pourraient aider, ainsi que mes [cours d'administration de serveurs Linux sur Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton). Il y a aussi un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action._

## KVM

Comme Xen, KVM (Kernel-based Virtual Machine) est une technologie d'hyperviseur open source pour la virtualisation de l'infrastructure de calcul fonctionnant sur du matériel compatible x86. Tout comme Xen, KVM dispose à la fois d'une communauté d'utilisateurs active et de déploiements significatifs en entreprise.

Un hôte KVM fonctionne en réalité sur le noyau Linux avec deux modules noyau KVM (le module kvm.ko et soit kvm-intel.ko soit kvm-amd.ko). Grâce à son intégration étroite avec le noyau — y compris la connectivité I/O avec les pilotes de bloc et de réseau du noyau fournis par Virtio — KVM peut offrir à ses invités un accès plus transparent à tous les profils matériels et réseau complexes qu'ils pourraient rencontrer.

Les extensions de virtualisation matérielle intégrées dans les conceptions de CPU modernes et requises pour les déploiements KVM signifient que, dès la sortie de la boîte, les invités KVM peuvent accéder en toute sécurité uniquement aux ressources matérielles dont ils ont besoin sans avoir à se soucier des fuites vers le système plus large.

Où exactement QEMU s'intègre-t-il dans tout cela ? En plus de pouvoir agir comme un hyperviseur, la force de QEMU réside dans son rôle d'émulateur. KVM, dans son rôle de virtualisation d'hyperviseur, peut utiliser les capacités d'émulation de QEMU pour compléter ses propres fonctionnalités d'accélération matérielle, présentant à ses invités un jeu de puces et un bus PCI émulés. Le tout, comme on dit, peut être plus grand que la somme de ses parties.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-56.png)
_Un hyperviseur KVM situé entre le système d'exploitation hôte Linux et ses machines virtuelles invitées_

Une grande partie des fonctionnalités de gestion pour KVM est souvent fournie par Libvirt. Par conséquent, vous pourriez parfois vouloir vous référer aux informations détaillées sur les fonctionnalités liées à KVM comme le réseau, le stockage et les dispositions du système de fichiers que l'on trouve dans le cinquième chapitre du livre [Teach Yourself Linux Virtualization and High Availability](https://www.amazon.com/gp/product/B06XTZ4YWQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06XTZ4YWQ&linkCode=as2&tag=projemun-20&linkId=fa7577d96ed91ffe111b08665bcb53f9) ("Libvirt et outils associés").

## Installation

Avant toute chose, vous devrez vous assurer que la machine physique que vous prévoyez d'utiliser comme hôte KVM supporte la virtualisation matérielle. En plus du paramètre BIOS et du contenu de /proc/cpuinfo (dont nous avons discuté dans le chapitre un), vous pouvez également vérifier cela rapidement à partir d'un système Linux en cours d'exécution en utilisant kvm-ok :

$ kvm-ok

Il est également judicieux de vérifier l'architecture matérielle — 64 ou 32 bits — avec laquelle vous travaillez :

$ uname -m

Mais même si votre profil matériel est à la hauteur de la tâche, vous devrez informer le noyau Linux de vos plans. Si elles ne sont pas déjà présentes, vous devriez ajouter les modules noyau kvm et soit kvm-intel soit kvm-amd.

# modprobe kvm-intel

Si ces modules échouent à se charger (et qu'il n'y a pas de périphérique /dev/kvm dans le système de fichiers), alors il y a de fortes chances que votre CPU ne soit tout simplement pas à la hauteur de la tâche que vous aimeriez lui confier. Cependant, si tout cela a fonctionné, vous êtes prêt à installer le paquet qemu-kvm (et, si nécessaire, libvirt, virt-install et bridge-utils également).

## Travailler avec les outils de gestion KVM

Il n'est un secret pour personne que les plateformes de virtualisation ont une réputation bien méritée d'être compliquées. Mais il y a deux choses qui peuvent rendre le démarrage avec KVM un peu plus difficile que certaines autres :

* Il existe plusieurs kits d'outils de gestion disponibles, chacun offrant des fonctionnalités similaires — mais pas identiques.
* Ils ont la mauvaise habitude de changer les noms utilisés pour les binaires clés en fonction de la distribution et de la version que vous utilisez.

Je vous présenterai les outils Libvirt et vmbuilder dans le chapitre cinq, mais ici, nous discuterons du kit d'outils KVM.

La construction de nouveaux invités en utilisant ce que nous appellerons la méthode « KVM » est un processus en deux étapes. Tout d'abord, vous utiliserez qemu-img pour créer une nouvelle image — ou modifier ou convertir une ancienne. Ensuite, vous utiliserez qemu-kvm pour configurer une machine virtuelle qui démarrera l'installation.

> _Ai-je dit « vous utiliserez qemu-kvm… » ? Quelle étourderie. qemu-kvm a été fusionné dans qemu il y a longtemps et a été remplacé par qemu-system-x86_64. En attendant, certains systèmes vous offrent kvm comme un wrapper qui exécute qemu-system-x86_64 -enable-kvm — bien que vous ne devriez pas confondre le wrapper kvm avec l'ancien binaire kvm qui utilisait une syntaxe quelque peu différente._

Voyons donc comment ces deux étapes fonctionnent. Vous créez une image de disque avec qemu-img (qui, soit dit en passant, peut être utilisé très efficacement pour d'autres hyperviseurs également), où « my-disk » est le nom de l'image que vous souhaitez créer, la taille maximale de l'image sera de 6 Go, et qcow2 est le format de fichier. qcow, soit dit en passant, signifie « QEMU Copy On Write ».

```
qemu-img create -f qcow2 /home/username/myimages/my-disk.img 6G \
 Formatting /home/username/myimages/my-disk.img, \
 fmt=qcow2 size=6442450944 \
 encryption=off \
 cluster_size=65536 \
 lazy_refcounts=off \
 refcount_bits=16
```

Le choix d'un format de fichier dépendra de vos besoins spécifiques. Si vous avez besoin d'une plus grande compatibilité et flexibilité — y compris la capacité à générer des instantanés sophistiqués — alors qcow2 est probablement votre meilleur choix.

Le format d'image de disque qcow permet à l'allocation d'espace disque de croître uniquement selon les besoins, ce qui signifie que l'utilisation de l'espace est toujours aussi efficace que possible. Les modifications apportées à une image qcow en lecture seule peuvent être enregistrées dans un fichier séparé, qui fait référence en interne à l'image originale. qcow2 a ajouté la capacité de créer plusieurs instantanés d'image.

Nous sommes maintenant prêts pour la deuxième étape. Voici comment nous allons construire notre machine virtuelle :

```
kvm -name my-VM \
 -hda /home/username/myimages/my-disk.img \
 -cdrom /home/username/Downloads/ubuntu-16.04-server-amd64.iso \
 -boot d -m 1024
```

Une nouvelle fenêtre SDL s'ouvrira souvent (bien que pas nécessairement pour toutes les distributions) où vous pourrez compléter le processus d'installation du système d'exploitation. Pour récupérer le contrôle de votre souris depuis le terminal Qemu, il faut appuyer sur CTRL+ALT.

Pour expliquer : en utilisant « kvm » (bien que la commande précise dont vous aurez besoin pour votre version puisse différer), nous appellerons notre nouvel invité « my-VM », désignerons le fichier my-disk.img comme hda (« disque dur a »), pointerons vers l'emplacement de l'ISO du système d'exploitation (Ubuntu 16.04 serveur, dans ce cas), et définirons 1024 Mo comme la mémoire maximale allouée à la machine virtuelle.

Par défaut, KVM configurera votre invité pour le réseau au niveau utilisateur (comme si les paramètres -netdev user,id=user.0 -device e1000,netdev=user.0 étaient spécifiés). Cela fournira à l'invité une adresse IP via le service DHCP propre à KVM et un accès à votre hôte, à Internet et aux ressources basées sur le LAN. Bien que la configuration par défaut soit simple, elle peut être trop restrictive pour certains scénarios, car il existe souvent des limitations de performance et de fonctionnalités.

En plus de celles-ci, vous pouvez utiliser des indicateurs de ligne de commande pour contrôler divers paramètres de configuration de la machine virtuelle, y compris :

* -smp 2 fournit deux processeurs (« smp » = multiprocessing symétrique).
* L'argument -net (exemple : -net nic,model=virtio,macaddr =52:54:00:05:11:11) établit une connexion réseau pour votre invité.
* Vous pouvez provisionner un pont réseau en utilisant quelque chose comme -net bridge,vlan=0,br=br0 — bien que cela nécessitera une définition -net correspondante sur l'hôte. Les deux sont connectés via un paramètre spécial « vlan ».
* -balloon virtio me permettra d'augmenter ou de réduire la taille de la mémoire d'un invité sans avoir à le redémarrer.
* Vous pouvez également utiliser l'indicateur -drive file= pour définir des dispositifs de stockage par blocs supplémentaires. Ajout d'une valeur pour format= (qcow2, par exemple).

L'indicateur -M assignera une émulation de type de machine matérielle spécifique. pc. Par exemple, fournira un profil PC standard. Pour une liste complète des types de machines disponibles, vous pouvez exécuter kvm -M ? :

```
kvm -M ?
Supported machines are:
ubuntu Ubuntu 15.04 PC (i440FX + PIIX, 1996) (alias of pc-i440fx-wily)
pc-i440fx-wily Ubuntu 15.04 PC (i440FX + PIIX, 1996) (default)
ubuntu Ubuntu 15.04 PC (i440FX + PIIX, 1996) (alias of pc-i440fx-vivid)
pc-i440fx-vivid Ubuntu 15.04 PC (i440FX + PIIX, 1996) (default)
pc-i440fx-utopic Ubuntu 14.10 PC (i440FX + PIIX, 1996)
pc-i440fx-trusty Ubuntu 14.04 PC (i440FX + PIIX, 1996)
pc Standard PC (i440FX + PIIX, 1996) (alias of pc-i440fx-2.5)
pc-i440fx-2.5 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-2.4 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-2.3 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-2.2 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-2.1 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-2.0 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-1.7 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-1.6 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-1.5 Standard PC (i440FX + PIIX, 1996)
pc-i440fx-1.4 Standard PC (i440FX + PIIX, 1996)
pc-1.3 Standard PC (i440FX + PIIX, 1996)
pc-1.2 Standard PC (i440FX + PIIX, 1996)
pc-1.1 Standard PC (i440FX + PIIX, 1996)
pc-1.0 Standard PC (i440FX + PIIX, 1996)
pc-0.15 Standard PC (i440FX + PIIX, 1996)
pc-0.14 Standard PC (i440FX + PIIX, 1996)
pc-0.13 Standard PC (i440FX + PIIX, 1996)
pc-0.12 Standard PC (i440FX + PIIX, 1996)
pc-0.11 Standard PC (i440FX + PIIX, 1996)
pc-0.10 Standard PC (i440FX + PIIX, 1996)
q35 Standard PC (Q35 + ICH9, 2009) (alias of pc-q35–2.5)
pc-q35–2.5 Standard PC (Q35 + ICH9, 2009)
pc-q35–2.4 Standard PC (Q35 + ICH9, 2009)
pc-q35–2.3 Standard PC (Q35 + ICH9, 2009)
pc-q35–2.2 Standard PC (Q35 + ICH9, 2009)
pc-q35–2.1 Standard PC (Q35 + ICH9, 2009)
pc-q35–2.0 Standard PC (Q35 + ICH9, 2009)
pc-q35–1.7 Standard PC (Q35 + ICH9, 2009)
pc-q35–1.6 Standard PC (Q35 + ICH9, 2009)
pc-q35–1.5 Standard PC (Q35 + ICH9, 2009)
pc-q35–1.4 Standard PC (Q35 + ICH9, 2009)
isapc ISA-only PC
none empty machine
xenfv Xen Fully-virtualized PC
xenpv Xen Para-virtualized PC
```

## Moniteur KVM

En travaillant avec QEMU, vous pouvez ouvrir une console de moniteur et interagir avec vos clients de manières qui pourraient être difficiles ou même impossibles en utilisant un serveur sans tête régulier. Vous pouvez lancer le moniteur KVM en appuyant sur CTRL+ALT, puis SHIFT+2, et une nouvelle console s'ouvrira sur votre bureau. SHIFT+1 fermera la console. Vous pouvez également accéder à la console à partir de la ligne de commande en utilisant quelque chose comme :

```
kvm -monitor stdio
```

Vous ne pourrez probablement PAS lancer le moniteur en tant que root (c'est-à-dire via sudo). Naturellement, votre version peut nécessiter « qemu-system-x86_64 » plutôt que kvm. Cette approche vous permet d'ajouter des arguments de ligne de commande (comme ce -monitor qui spécifie une cible de console). Consultez man qemu-system-x86_64 pour plus de détails sur les types d'opérations que le moniteur permet.

Cet exemple (emprunté à en.wikibooks.org/wiki/QEMU/Monitor) listera tous les dispositifs de bloc actuellement disponibles pour votre système, puis pointera l'un d'eux vers un fichier ISO que vous souhaitez utiliser :

```
(qemu) info block
ide0-hd0: type=hd removable=0 file=/path/to/winxp.img
ide0-hd1: type=hd removable=0 file=/path/to/pagefile.raw
ide1-hd1: type=hd removable=0 file=/path/to/testing_data.img
ide1-cd0: type=cdrom removable=1 locked=0 file=/dev/sr0 ro=1 drv=host_device
floppy0: type=floppy removable=1 locked=0 [not inserted]
sd0: type=floppy removable=1 locked=0 [not inserted]
(qemu) change ide1-cd0 /home/images/my.iso
```

## Réseautage

Par défaut, un invité KVM recevra une adresse IP dans le sous-réseau 10.0.2.0/24, et aura un accès sortant (y compris l'accès SSH) à la fois à son hôte et au réseau plus large au-delà. Par ce même défaut, cependant, il ne pourra pas héberger de services pour les clients du réseau. Si vous devez ouvrir la connectivité réseau entrante, vous voudrez probablement créer un pont réseau sur votre hôte similaire à celui que nous avons utilisé pour Xen dans le chapitre précédent. Comme avant, vous installerez bridge-utils sur l'hôte et, en supposant que vous exécutez un système basé sur Debian et que vous souhaitez que votre hôte reçoive son IP d'un serveur DHCP réseau, modifiez le fichier /etc/network/interfaces pour qu'il ressemble à ceci (sur les machines CentOS, modifiez les fichiers dans le répertoire /etc/sysconfig/network-scripts/) :

```
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet manual
auto br0
iface br0 inet dhcp
 bridge_ports eth0
 bridge_stp off
 bridge_fd 0
 bridge_maxwait 0
```

Sur CentOS, vous devrez créer un fichier ifcfg-br0 dans le répertoire /etc/sysconfig/network-scripts/ pour qu'il ressemble à ceci :

```
DEVICE=br0
TYPE=Bridge
BOOTPROTO=static
DNS1=192.168.0.1
GATEWAY=192.168.0.1
IPADDR=192.168.0.100
NETMASK=255.255.255.0
ONBOOT=yes
SEARCH="example.com"
```

…Et puis ajoutez une ligne lisant BRIDGE=br0 au fichier de votre interface réseau principale (qui sera souvent : /etc/sysconfig/network-scripts/ifcfg-eth0).

Vous devrez ensuite arrêter et redémarrer vos services réseau (ou redémarrer).

_Cherchez une introduction solide à l'administration Linux ou AWS ? Consultez mes livres [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) et [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27) ainsi que le cours hybride texte-vidéo [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) de Manning. Préférez-vous apprendre la technologie en vidéo ? J'ai des [cours d'administration Linux sur Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) qui n'attendent que d'être regardés._