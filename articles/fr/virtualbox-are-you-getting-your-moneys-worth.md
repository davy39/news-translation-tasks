---
title: 'VirtualBox : En avez-vous pour votre argent ?'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-25T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/virtualbox-are-you-getting-your-moneys-worth
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca13c740569d1a4ca4d76.jpg
tags:
- name: Linux
  slug: linux
- name: 'VirtualBox '
  slug: virtualbox
seo_title: 'VirtualBox : En avez-vous pour votre argent ?'
seo_desc: 'NOTE: As of November 7, 2018, there’s an unpatched zero-day vulnerability
  in VirtualBox that could allow a user on the guest full access to the host machine.
  Until further notice, do NOT use VirtualBox with the default network settings. Details
  are a...'
---

**NOTE** : À partir du 7 novembre 2018, il existe une [vulnérabilité zero-day non corrigée dans VirtualBox](https://github.com/MorteNoir1/virtualbox_e1000_0day) qui pourrait permettre à un utilisateur de la machine invitée d'avoir un accès complet à la machine hôte. Jusqu'à nouvel ordre, n'utilisez PAS VirtualBox avec les paramètres réseau par défaut. [Les détails sont disponibles ici](https://github.com/MorteNoir1/virtualbox_e1000_0day).

Bien sûr que vous en avez pour votre argent. VirtualBox est gratuit, n'est-ce pas ? D'accord, alors pourquoi ne pas doubler le retour sur votre investissement ? Pourquoi ne pas découvrir comment accomplir encore plus en tant qu'utilisateur avancé de VirtualBox ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*UAt3fRypjCK9quhYXf6w1g.png)

VirtualBox d'Oracle est facile à installer, facile à utiliser, et vous donne la possibilité d'exécuter des versions virtuelles de presque tous les systèmes d'exploitation modernes à partir de n'importe quel autre système d'exploitation moderne. Windows 10 sur Ubuntu Linux ? Je l'ai fait moi-même. FreeBSD sur CentOS Linux ? Pourquoi pas ?

Vous pouvez, bien sûr, faire des choses similaires avec l'outil gratuit VMware Player et, sur Windows 8 et versions ultérieures, avec Hyper-V. Mais cet article concerne VirtualBox.

J'utilisais VirtualBox depuis des années, mais ce n'est que lorsque j'ai eu besoin de rassembler plusieurs machines physiques qui traînaient dans la maison pour les utiliser comme nœuds dans un réseau [Docker swarm mode](https://hackernoon.com/too-many-choices-how-to-pick-the-right-tool-to-manage-your-docker-clusters-b5b3061b84b7) que les choses se sont compliquées. Après tout, créer et lancer manuellement des VM nécessiterait de passer du temps sérieux devant chaque PC, à surveiller les installations et configurations des systèmes d'exploitation. Et cela signifierait monter les escaliers et s'asseoir sur les chaises vraiment horribles dans les chambres de mes enfants. Ne leur dites pas que j'ai dit cela, mais je ne comprends pas pourquoi ils les supportent.

Il s'avère que la connectivité SSH entre mes PC (Linux) et une connaissance très basique de l'interface en ligne de commande _vboxmanage_ étaient tout ce dont j'avais besoin pour retrouver mon bonheur de sysadmin paresseux. C'était libérateur, et vous pourriez probablement utiliser un peu de libération vous-même.

Mais avant d'en arriver là, je vais parler un peu du fonctionnement de VirtualBox et des types de choses que vous pouvez faire avec lui. N'hésitez pas à passer à la section suivante si cela ne vous semble pas intéressant.

Quel est mon angle dans tout cela ? Tout en faisant des recherches pour mes divers [livres](https://bootstrap-it.com/index.php/books/) et [cours vidéo Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton), je construis souvent des environnements de test qui incluent des machines exécutant des combinaisons étranges de systèmes d'exploitation. Pour certains objectifs — surtout lorsque je dois travailler au niveau du noyau du système d'exploitation — VirtualBox s'est répété comme étant l'outil le plus rapide et le plus efficace que j'ai. Je ne suis pas sûr de vouloir utiliser une machine virtuelle VirtualBox gourmande en ressources pour exécuter des services permanents, mais pour les cas liés aux tests et au développement, c'est absolument le roi de la colline.

C'est moi. Mais mon expérience est-elle utile pour les utilisateurs normaux ? Dans le sens où, de temps en temps au moins, tout le monde a besoin de vérifier de nouvelles technologies, alors absolument. Mais je suppose que je suis un peu inhabituel en ce sens que je passe très rarement en production. Je teste toujours.

## Travailler avec VirtualBox

En plus de vous permettre d'essayer des systèmes d'exploitation entièrement nouveaux sans avoir à fouiller dans le garage pour des composants matériels inutilisés (mais utilisables), VirtualBox est également un bac à sable fantastique. Donc, même si vous ne vous souciez pas vraiment du système d'exploitation que vous exécutez, mais que vous n'êtes pas trop enthousiaste à l'idée de risquer la santé et le bien-être de votre station de travail principale sur une configuration logicielle expérimentale, VirtualBox peut aider.

Cela fonctionnera également si la configuration logicielle expérimentale est la vôtre. Ce qui signifie que VirtualBox peut être utilisé comme un outil pour tester en toute sécurité la manière dont vos propres projets de développement se comportent dans plusieurs environnements de système d'exploitation.

Et n'oubliez pas que VirtualBox est très largement utilisé comme fournisseur pour le système d'automatisation de configuration Vagrant.

Comme je l'ai brièvement écrit dans mon [article sur la virtualisation des serveurs Linux](https://hackernoon.com/linux-server-virtualization-the-basics-32079b0e7d6e), VirtualBox est un hyperviseur de type 2. Et c'est le cas. Mais c'est un hyperviseur avec une empreinte si légère que, fonctionnalité pour fonctionnalité, il peut parfois rivaliser avec des technologies de conteneurs comme Docker et LXC/LXD. Cela ouvre VirtualBox à une assez large gamme d'utilisations. Mais comme le chevauchement peut devenir compliqué, voici (parce que vous ne pouvez jamais avoir trop de tableaux) une comparaison visuelle des technologies :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wjZKFpRlCBCluCN3mijABA.png)
_Une matrice non scientifique des fonctionnalités/cas d'utilisation pour les technologies de virtualisation_

## Faire des choses

Assez parlé. Mettons-nous au travail.

L'interface graphique de VirtualBox est très belle, mais elle vous ralentira vraiment lorsque vous lancerez des VM sur plusieurs hôtes réseau. Voici donc quelques outils qui feront que les choses se passeront — à la fois localement ou via une connexion à distance — à partir de la ligne de commande.

Installez VirtualBox. Voici comment cela se fait sur Ubuntu ou Debian, en tout cas :

```
sudo apt install virtualbox
```

Il est maintenant possible de créer à distance une nouvelle VM à partir de zéro en utilisant des commandes comme celles-ci :

```
vboxmanage list ostypes
vboxmanage createhd --filename Ubuntu64.vdi --size 16384
VBoxManage createvm --name Ubuntu64 --ostype "Ubuntu_64" --register
```

…Mais afficher l'interface d'installation réelle sur un écran distant peut parfois être plus ennuyeux que cela n'en vaut la peine. Au lieu de cela, supposons que vous avez déjà une VM VirtualBox « golden-image » sur votre station de travail locale. Vous voudrez utiliser _vboxmanage list vms_ pour voir ce qui s'y trouve.

Voici à quoi cela ressemblait sur ma station de travail :

```
vboxmanage list vms
"Ubuntu-16.04-template" {c00d3b2b-6c77–4919–85e2–6f6f28c63d56}
"Ubuntu14-template" {43e2f9d4–8aa1–4db4-aa59–33b202df32ed}
"centos-7-template" {e2613f6d-1d0d-489c-8d9f-21a36b2ed6e7}
"Kali-Linux-template" {b7a3aea2–0cfb-4763–9ca9–096f587b2b20}
"Kali-Linux-openvas" {1ec41fdd-bf14–4025–9e9e-ee7272acf87f}
"docker-project" {2387a5ab-a65e-4a1d-8e2c-25ee81bc7203}
"Ubuntu-16-lxd" {62bb89f8–7b45–4df6-a8ea-3d4265dfcc2f}
```

Notez, au passage, comment je garde des copies « template » propres des systèmes d'exploitation individuels et que je crée des copies clonées chaque fois que j'ai besoin de faire un travail réel. Croyez-moi, cela peut vraiment accélérer votre temps de lancement par rapport au fait de devoir passer par toute la routine d'installation à chaque fois. Vous pouvez créer des clones à partir de l'interface graphique, ou en utilisant _clonevm_ comme ceci (où « Kali-Linux-template » est le nom d'une VM existante et « newkali » est le nom que nous aimerions donner au clone) :

```
vboxmanage clonevm Kali-Linux-template --name newkali
```

Consultez les détails de l'argument _clonevm_ sur la [page de documentation de VirtualBox ici](https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm).

Ici, cependant, je vais vous montrer comment exporter une VM existante vers un fichier .OVA que vous pouvez simplement copier sur vos machines distantes et ensuite importer dans leurs instances de VirtualBox. L'opération d'exportation ne pourrait pas être plus simple : vous entrez le nom de la VM que vous souhaitez exporter (docker-project, dans mon cas), _-o_ pour spécifier un nom de fichier de sortie, et le nom de fichier lui-même avec l'extension de fichier appropriée.

```
vboxmanage export docker-project -o docker.ova
0%…10%…20%…30%…40%…50%…60%…70%…80%…90%…100%
Successfully exported 1 machine(s).
```

Le fichier sera enregistré dans votre répertoire actuel. Vous pouvez afficher les détails du fichier que vous venez de créer :

```
ls -lh | grep docker-rw — — — — 
1 root root 2.1G Jun 4 17:01 docker.ova
```

D'une manière ou d'une autre, vous devrez copier le fichier .OVA sur vos autres PC. Voici comment le transfert de fichier pourrait fonctionner entre des machines Linux/MAC OS en utilisant scp :

```
scp docker.ova username@192.168.0.34:/home/username
```

Naturellement, vous devrez vous assurer que vous avez suffisamment d'espace disque libre pour sauvegarder le fichier .OVA lui-même (qui peut être assez grand) _et_ créer la nouvelle VM.

Maintenant, connectez-vous à votre machine distante et, à partir du répertoire contenant le fichier que vous venez de transférer, importez-le dans VirtualBox :

```
vboxmanage import docker.ova
0%…10%…20%…30%…40%…50%…60%…70%…80%…90%…100%
Interpreting /home/dad/docker.ova…
OK.
Disks: 
vmdisk2 36945920000 -1 http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized docker-disk1.vmdk
-1–1Virtual system 0:
0: Suggested OS type: "Ubuntu_64"
    (change with "--vsys 0 --ostype <type>"; use "list ostypes" to list all possible values)
 1: Suggested VM name "docker-project"
    (change with "--vsys 0 --vmname <name>")
 2: Number of CPUs: 1
    (change with "--vsys 0 --cpus <n>")
 3: Guest memory: 2048 MB
    (change with "--vsys 0 --memory <MB>")
 4: Sound card (appliance expects "", can change on import)
    (disable with "--vsys 0 --unit 4 --ignore")
 5: USB controller
    (disable with "--vsys 0 --unit 5 --ignore")
 6: Network adapter: orig Bridged, config 3, extra slot=0;type=Bridged
 7: CD-ROM
    (disable with "--vsys 0 --unit 7 --ignore")
 8: IDE controller, type PIIX4
    (disable with "--vsys 0 --unit 8 --ignore")
 9: IDE controller, type PIIX4
    (disable with "--vsys 0 --unit 9 --ignore")
10: SATA controller, type AHCI
    (disable with "--vsys 0 --unit 10 --ignore")
11: Hard disk image: source image=docker-disk1.vmdk, target path=/home/dad/VirtualBox VMs/docker-project/docker-disk1.vmdk, controller=10;channel=0
    (change target path with "--vsys 0 --unit 11 --disk path";
    disable with "--vsys 0 --unit 11 --ignore")
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Successfully imported the appliance.
```

Vous voudrez confirmer que tout a fonctionné en exécutant _list vms_ :

```
vboxmanage list vms
"docker-project" {30ec7f7d-912b-40a9–8cc1-f9283f4edc61}
```

Vous pouvez connecter votre VM à un réseau en utilisant _vboxmanage modifyvm_. Mais, avant de pouvoir faire cela, vous devrez savoir comment votre machine hôte fait référence à l'interface réseau appropriée. Sur une machine Linux, vous pouvez obtenir cela en utilisant _ip addr_. Dans ce cas, la deuxième interface qui est affichée ("eth0" — c'est "eth" suivi d'un zéro… pas la lettre o) est la NIC à travers laquelle cette machine obtient son accès internet, donc c'est la connexion que nous recherchons.

```
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state 
UNKNOWN group default qlen 1
 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
 inet 127.0.0.1/8 scope host lo
 valid_lft forever preferred_lft forever
 inet6 ::1/128 scope host
 valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc
 pfifo_fast state UP group default qlen 1000
 link/ether 94:de:80:c5:1e:2d brd ff:ff:ff:ff:ff:ff
 inet 192.168.1.13/24 brd 192.168.1.255 scope global dynamic eth0
 valid_lft 59857sec preferred_lft 59857sec
 inet6 fe80::e1c3:f8a2:9f8d:4375/64 scope link
  valid_lft forever preferred_lft forever
```

Une façon de déplacer la carte réseau (virtuelle) de votre VM sur l'interface eth0 via un adaptateur bridge est d'utiliser la commande `modifyvm`. Dans ce cas, "docker-project" pointe vers le nom de la VM, et eth0 est la cible du nouveau bridge, connectant l'interface réseau interne de votre VM avec l'eth0 de l'hôte.

```
vboxmanage modifyvm "docker-project" --bridgeadapter1 eth0
```

Maintenant, vous êtes prêt à lancer la VM. L'argument "type headless" indique à VirtualBox d'exécuter la VM en tant que serveur sans interface graphique.

```
vboxmanage startvm "docker-project" --type headless
Waiting for VM "docker-project" to power on…
VM "docker-project" has been successfully started.
```

Curieux de savoir ce qui se passe avec votre nouvelle VM ? Essayez _showvminfo_ :

```
vboxmanage showvminfo docker-project
```

Vous devrez peut-être exécuter un programme de recherche réseau comme nmap pour obtenir l'adresse IP de votre VM. Avec cette information, vous serez prêt à vous mettre au travail. Connectez-vous à votre nouvelle VM en utilisant les mêmes identifiants que ceux utilisés sur la VM source à partir de laquelle elle a été copiée. L'arrêt d'une VM une fois que vous avez terminé avec elle est aussi simple que l'exécution de la commande _poweroff_ :

```
VBoxManage controlvm "docker-project" poweroff 
0%…10%…20%…30%…40%…50%…60%…70%…80%…90%…100%
```

Bonne virtualisation !

_David Clinton est l'auteur de [cours sur Linux, AWS, Docker et la sécurité](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) sur Pluralsight, et de [livres et contenu technologique](https://bootstrap-it.com)._