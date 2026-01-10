---
title: Comment créer un espace de travail IT virtuel
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2018-03-09T18:57:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-virtual-it-workspace-16927c0f3535
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2p-yQIIofCUjFNfQ3KII1A.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un espace de travail IT virtuel
seo_desc: '_This article is based on a chapter from my free online book, Solving for
  Technology: how to quickly learn valuable new skills in a madly changing technology
  world. There’s lots more where that came from at my Bootstrap IT site, including
  links to my...'
---

_Cet article est basé sur un chapitre de mon livre en ligne gratuit, [Résoudre pour la technologie : comment apprendre rapidement de nouvelles compétences précieuses dans un monde technologique en constante évolution](https://learntech.bootstrap-it.com/). Il y a beaucoup plus à découvrir sur mon site Bootstrap IT, y compris des liens vers mon livre, [Linux en Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9), et un cours hybride appelé [Linux en Mouvement](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui comprend plus de deux heures de vidéo et environ 40 % du texte de Linux en Action._

Avez-vous déjà complètement endommagé votre poste de travail ou votre ordinateur portable principal en testant une nouvelle technologie ? Ou avez-vous tellement de paquets et leurs dépendances installés que vous n'avez plus aucune idée de ce qui fait que vos expériences réussissent ou échouent ?

La virtualisation peut vous fournir un environnement propre, rapide et léger où vous pouvez tester à votre guise. Vous n'êtes même pas limité au système d'exploitation qui s'exécute sur votre machine hôte, donc c'est aussi un excellent moyen de voir comment les choses fonctionnent sur plusieurs plateformes.

Lorsque vous avez terminé — ou si tout s'effondre dans un échec glorieux — vous pouvez simplement supprimer votre environnement et en lancer un nouveau pour le remplacer. Aucun dommage n'est fait.

Dans cet article, j'explorerai VirtualBox et les conteneurs Linux (LXC) comme outils pour fournir des environnements de système d'exploitation virtuel facilement répliqués et partageables. Je terminerai avec quelques réflexions sur l'écriture de code et la construction de piles logicielles directement dans des environnements virtuels.

### VirtualBox

Dites donc « bonjour » au produit hyperviseur multiplateforme gratuit VirtualBox d'Oracle et, en particulier, à quelques astuces avancées pour tirer plus de valeur de votre investissement (sans coût). VirtualBox est quelque chose que vous pouvez utiliser sur n'importe quel système d'exploitation pour créer des ordinateurs virtualisés exécutant à peu près n'importe quelle version de Windows ou de Linux.

> Vous devez toujours obtenir une licence pour toute image Windows que vous décidez d'exécuter, bien que vous soyez généralement libre d'installer et d'utiliser des copies sans activer la licence pendant un mois ou deux.

Si vous avez déjà lu mon livre [Linux en Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9&chan=freeCodeCamp1) et que certains de ces éléments vous semblent familiers, c'est parce que ce chapitre est une version réduite du chapitre 2 de Linux en Action. Le contenu a été rendu disponible grâce à l'aimable autorisation de Manning Publications.

#### Démarrer avec VirtualBox

VirtualBox fournit un environnement dans lequel vous pouvez lancer autant d'ordinateurs virtuels que les ressources de votre système physique peuvent gérer. Et, bien sûr, c'est un outil particulièrement utile pour tester et apprendre en toute sécurité de nouvelles compétences d'administration — ce qui est notre objectif principal pour l'instant.

**Installation de VirtualBox**

Vous voulez essayer tout cela depuis un PC Windows ? Rendez-vous sur le [site web de VirtualBox](https://www.virtualbox.org/wiki/Downloads) et téléchargez l'archive exécutable. Cliquez sur le fichier que vous avez téléchargé, puis suivez quelques étapes d'installation (les valeurs par défaut devraient toutes fonctionner). Enfin, on vous demandera si vous êtes d'accord avec une éventuelle réinitialisation de vos interfaces réseau, puis si vous souhaitez installer VirtualBox. Bien sûr, vous êtes d'accord et vous le faites.

L'installation de VirtualBox sur une machine Ubuntu Linux est encore plus simple. Juste deux commandes :

```
sudo apt updatesudo apt install virtualbox
```

#### Définir une machine virtuelle

Je ne suis pas sûr que vous ayez déjà assemblé un ordinateur physique à partir de composants, mais cela peut devenir compliqué. Définir une nouvelle machine virtuelle dans VirtualBox fonctionne à peu près de la même manière. La seule différence significative est que, plutôt que de devoir vous mettre à genoux avec une lampe de poche serrée entre les dents pour ajouter manuellement de la RAM et un disque de stockage à votre boîte, VirtualBox vous permet de définir les spécifications « matérielles » de votre VM en cliquant avec votre souris.

Après avoir cliqué sur Nouveau dans l'interface de VirtualBox, vous donnerez à la VM que vous êtes sur le point de créer un nom descriptif et, comme vous pouvez le voir dans la figure, le logiciel devrait pouvoir remplir correctement les champs Type et Version automatiquement. Le Type et la Version que vous sélectionnez ici n'installeront pas un système d'exploitation réel, mais sont simplement utilisés pour appliquer des paramètres d'émulation matérielle appropriés.

![Image](https://cdn-media-1.freecodecamp.org/images/Y67phsA74KpA38pRcmB4ZmYV5rG8ORzyVOdV)
_La boîte de dialogue Créer une machine virtuelle : VirtualBox essaiera de deviner votre système d'exploitation et sa version pour offrir des choix par défaut intelligents plus tard_

Sur l'écran suivant, vous allouerez de la RAM à votre VM. À moins que vous ne prévoyez quelque chose de particulièrement exigeant — comme héberger un essaim de conteneurs ou exécuter un serveur web occupé — la quantité par défaut (768 Mo) devrait être suffisante. Vous pouvez certainement lui donner plus de RAM si nécessaire, mais n'oubliez pas de laisser suffisamment de mémoire pour votre machine hôte et toute autre VM qui pourrait déjà y résider. Donc, si votre hôte n'a que 4 Go de RAM physique, vous ne voudrez probablement pas en donner la moitié à votre VM.

Gardez ces limites à l'esprit si vous décidez éventuellement d'exécuter plusieurs VM en même temps — quelque chose qui sera utile pour tester des projets d'infrastructure plus complexes. Même si chaque VM n'utilise que la quantité de mémoire par défaut, deux ou trois d'entre elles peuvent commencer à grignoter la RAM nécessaire aux opérations normales de l'hôte.

#### Définir votre disque dur virtuel

Qu'est-ce qu'un ordinateur sans disque dur ? Le processus de configuration de VirtualBox vous demandera maintenant si vous souhaitez créer un nouveau disque virtuel pour votre VM ou utiliser un disque existant. Il peut y avoir des moments où vous souhaitez partager un seul disque entre deux VM, mais pour cet exercice, je suppose que vous voudrez partir de zéro. Sélectionnez donc « Créer un disque dur virtuel maintenant ».

L'écran suivant vous permet de choisir un format de fichier de disque dur pour le disque que vous êtes sur le point de créer. À moins que vous ne prévoyez d'exporter éventuellement le disque pour l'utiliser dans un autre environnement de virtualisation, le format d'image de disque VirtualBox (VDI) par défaut fonctionnera bien.

Je n'ai jamais regretté d'avoir choisi l'option par défaut « Alloué dynamiquement » pour déterminer comment le lecteur virtuel consommera de l'espace sur l'hôte. Par « dynamique », ils entendent que l'espace sur le disque de stockage de l'hôte sera alloué à la VM uniquement au besoin. Si l'utilisation du disque de la VM reste faible, moins d'espace hôte sera alloué.

Un disque de taille fixe, en revanche, se verra attribuer sa quantité maximale d'espace immédiatement, quelle que soit la quantité qu'il utilise réellement. Le seul avantage de la « taille fixe » est la performance de l'application, mais comme j'utilise généralement les VM VirtualBox pour des tests et des expériences, je préfère éviter ce compromis.

Lorsque VirtualBox sait que vous recherchez Linux — et parce que Linux utilise si efficacement l'espace de stockage — VirtualBox vous proposera probablement seulement 8 Go de taille de disque totale sur l'écran suivant (montré ci-dessous). À moins que vous n'ayez des plans inhabituellement grands pour la VM (par exemple, vous allez travailler avec des opérations de base de données sérieuses), cela devrait être suffisant. D'un autre côté, si vous aviez choisi Windows comme système d'exploitation, le choix par défaut aurait été de 25 Go, et pour une bonne raison : Windows n'est pas timide pour demander beaucoup de ressources. C'est une excellente illustration de la manière dont Linux est si bien adapté aux environnements virtuels.

![Image](https://cdn-media-1.freecodecamp.org/images/z6wb3cAfhqTF54YDwohdCl7lOXTFmL4Jaird)
_Si nécessaire, votre disque virtuel peut être aussi grand que 2 To — ou l'espace libre maximum sur le périphérique hôte_

Vous pouvez également modifier le nom et l'emplacement que VirtualBox utilisera pour votre disque sur cet écran.

Lorsque vous avez terminé, cliquez sur Créer et la nouvelle VM apparaîtra dans la liste des VM sur le côté gauche du gestionnaire VirtualBox. Profitez du goût du succès, mais vous n'avez pas terminé : ce n'était que la machine. Maintenant, vous aurez besoin d'un système d'exploitation pour la faire vivre.

#### Télécharger un système d'exploitation

Maintenant que vous avez défini le profil matériel virtuel de votre nouvelle VM, voici ce qui reste à faire :

* Télécharger un fichier (au format ISO) contenant l'image du système d'exploitation que vous souhaitez utiliser.
* Démarrer la nouvelle VM en utilisant un lecteur DVD virtuel contenant l'ISO que vous avez téléchargé
* Suivre le processus d'installation standard du système d'exploitation
* Démarrer la VM et lancer le système d'exploitation que vous venez d'installer

Vous devrez télécharger un fichier .ISO contenant les fichiers du système d'exploitation et le programme d'installation. Trouver le bon fichier est généralement une question de recherche sur Internet du nom de la distribution et du mot « télécharger ». Dans le cas d'Ubuntu, vous pourriez également aller sur la page [ubuntu.com](https://ubuntu.com) et cliquer sur l'onglet Téléchargements comme vous le voyez dans la figure. Remarquez les différentes versions d'Ubuntu qui sont disponibles. Si vous allez utiliser cette VM pour des tâches d'administration, alors la version Server, petite et rapide, est probablement un meilleur choix que Desktop.

![Image](https://cdn-media-1.freecodecamp.org/images/MKs0xzalhjCBE3UjEMnxTYoVttmSerE1HM2Q)
_Le menu déroulant Téléchargements sur la page d'accueil d'Ubuntu.com. Notez la gamme de versions qu'Ubuntu propose_

**Valider l'archive ISO que vous avez téléchargée**

Les grands fichiers peuvent parfois être corrompus pendant le processus de téléchargement. Si même un seul octet dans votre .ISO a été changé, il y a une chance que l'installation ne fonctionne tout simplement pas. Parce que vous ne voulez pas investir du temps et de l'énergie pour découvrir qu'il y avait un problème avec le téléchargement, il est toujours bon de calculer immédiatement la somme de contrôle (ou hash) pour le .ISO que vous avez téléchargé pour confirmer que tout est comme il était.

Pour cela, vous devrez obtenir la somme de contrôle SHA ou MD5 appropriée — qui est une longue chaîne ressemblant à ceci :

`4375b73e3a1aa305a36320ffd7484682922262b3`

Dans le cas d'Ubuntu, obtenir cela signifiera aller sur la page web à [releases.ubuntu.com](http://releases.ubuntu.com/), cliquer sur le répertoire correspondant à la version que vous avez téléchargée, puis cliquer sur l'un des liens vers une somme de contrôle (comme, par exemple, SHA1SUMS).

Vous devez comparer la chaîne appropriée de cette page avec les résultats d'une commande exécutée depuis le même répertoire que votre .ISO téléchargé, qui pourrait ressembler à ceci :

`$ shasum ubuntu-16.04.2-server-amd64.iso`

Si elles correspondent, vous êtes en affaires. Si elles ne correspondent pas — et que vous avez vérifié deux fois pour vous assurer que vous regardez la bonne version — alors vous devrez peut-être télécharger le .ISO une deuxième fois.

#### Installer un système d'exploitation

Une fois votre fichier .ISO en place, retournez à VirtualBox. Avec la VM que vous venez de créer mise en surbrillance dans le panneau de gauche, cliquez sur le bouton vert Démarrer en haut de l'application. On vous demandera de sélectionner un fichier .ISO de votre système de fichiers à utiliser comme lecteur DVD virtuel. Naturellement, vous choisirez celui que vous venez de télécharger. La nouvelle VM lira ce DVD et lancera une installation du système d'exploitation.

> La plupart du temps, le processus d'installation se déroulera bien. Cependant, décrire des solutions à chacune des nombreuses petites choses qui pourraient mal tourner nécessiterait une série d'articles. Donc, si vous avez des problèmes, vous pouvez consulter la documentation et les guides disponibles pour votre système d'exploitation ou partager votre question avec la communauté en ligne.

Lorsque tout est bien installé, il peut encore y avoir quelques choses à faire avant de pouvoir démarrer avec succès dans votre VM. Avec l'entrée de votre VM mise en surbrillance, cliquez sur l'icône jaune Paramètres. C'est ici que vous pouvez jouer avec les paramètres de l'environnement et du matériel de votre VM.

En cliquant sur Réseau, par exemple, vous pouvez définir la connectivité réseau. Si vous voulez que votre VM ait un accès Internet complet via l'interface réseau de la machine hôte, alors, comme montré ci-dessous, vous pouvez sélectionner « Adaptateur en pont » dans le menu déroulant Attaché, puis le nom de l'adaptateur de votre hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/NlcUwM8Y9793b9wAvqsDZb4aFK73Z2JoeCWH)
_L'onglet réseau de l'écran Paramètres. Vous pouvez déterminer quel type d'interface réseau — ou interfaces — utiliser pour votre VM_

> L'utilisation d'un adaptateur en pont n'est peut-être pas toujours votre premier choix, et elle peut parfois présenter un risque pour la sécurité. En fait, choisir « Réseau NAT » est un moyen plus courant de fournir à une VM un accès Internet. Cependant, un réseau en pont est le moyen le plus simple d'obtenir une connectivité réseau complète, donc, pour les tests au moins, c'est une approche utile.

Les sections suivantes sont un peu bonus, mais qui n'aime pas les choses gratuites ? Je vais vous parler de deux astuces connexes : comment organiser vos VM VirtualBox pour rendre le démarrage de nouvelles aussi rapide que possible, et comment utiliser la ligne de commande pour partager des VM sur un réseau.

#### Cloner des VM pour des démarrages rapides

L'un des avantages les plus évidents de travailler avec des VM est la capacité à accéder rapidement à un environnement de système d'exploitation frais et propre. Mais si l'accès à cet environnement nécessite de passer par le processus d'installation complet, alors je ne vois pas beaucoup de « rapidement ».

Jusqu'à ce que vous ajoutiez le clonage au mélange. Pourquoi ne pas garder votre VM originale dans son état propre post-installation, et simplement créer un clone identique chaque fois que vous voulez faire un peu de travail réel ?

C'est facile. Jetez un autre coup d'œil à l'application VirtualBox. Sélectionnez la VM (arrêtée) que vous souhaitez utiliser comme copie principale, cliquez sur le lien de menu Machine, puis Clone. Vous confirmerez le nom que vous souhaitez donner à votre clone et puis, après avoir cliqué sur Suivant, si vous souhaitez créer un clone complet (ce qui signifie que de nouvelles copies de fichiers seront entièrement créées pour la nouvelle VM) ou un clone lié (ce qui signifie que la nouvelle VM partagera tous les fichiers de base avec son maître, tout en maintenant votre nouveau travail séparément).

Sélectionner l'option Liée sera beaucoup plus rapide et prendra beaucoup moins de place sur votre disque dur. Le seul inconvénient est que vous ne pourrez pas déplacer ce clone particulier vers un autre ordinateur plus tard. C'est votre choix.

Maintenant, cliquez sur Clone, et une nouvelle VM apparaîtra dans le panneau VM. Démarrez-la de la manière habituelle, puis connectez-vous en utilisant les mêmes identifiants que vous avez définis sur le maître.

#### Gérer les VM depuis la ligne de commande

VirtualBox est livré avec son propre shell de ligne de commande qui est invoqué en utilisant `vboxmanage`. Pourquoi se donner la peine de la ligne de commande ? Parce que, parmi d'autres avantages, cela vous permettra de travailler sur des serveurs distants — ce qui peut considérablement augmenter la portée des projets possibles. Pour voir comment fonctionne `vboxmanage`, utilisez `list vms` pour lister toutes les VM actuellement disponibles sur votre système. Voici à quoi cela ressemble sur ma machine :

```
$ vboxmanage list vms
"Ubuntu-16.04-template" {c00d3b2b-6c77–4919–85e2–6f6f28c63d56}
"centos-7-template" {e2613f6d-1d0d-489c-8d9f-21a36b2ed6e7}
"Kali-Linux-template" {b7a3aea2–0cfb-4763–9ca9–096f587b2b20}
"website-project" {2387a5ab-a65e-4a1d-8e2c-25ee81bc7203}
"Ubuntu-16-lxd" {62bb89f8–7b45–4df6-a8ea-3d4265dfcc2f}
```

`vboxmanage clonevm` effectuera le même type d'action de clonage que j'ai décrit ci-dessus en utilisant l'interface graphique. Ici, je crée un clone de la VM Kali-Linux-template, en nommant la copie "newkali" :

```
$ vboxmanage clonevm Kali-Linux-template --name newkali
```

Cela fonctionnera bien tant que je n'ai besoin d'utiliser la nouvelle VM que sur mon ordinateur local. Mais supposons que je veux que d'autres membres de mon équipe aient une copie exacte de cette VM — peut-être pour qu'ils puissent tester quelque chose sur lequel j'ai travaillé. Pour cela, je devrai convertir la VM dans un format de fichier standardisé. Voici comment je pourrais exporter une VM locale dans un fichier en utilisant le format Open Virtualization Format (.OVA) :

```
$ vboxmanage export website-project -o website.ova
0%…10%…20%…30%…40%…50%…60%…70%…80%…90%…100%
Successfully exported 1 machine(s).
```

Ensuite, vous devrez copier le fichier .OVA sur l'ordinateur de votre collègue. Gardez à l'esprit que le fichier ne sera, selon aucune norme, considéré comme petit et délicat. Si vous n'avez pas de bande passante réseau à revendre pour un transfert de plusieurs Go, envisagez de le déplacer via un périphérique USB.

Une fois le transfert terminé, il ne reste plus qu'à importer la VM dans le VirtualBox de cette machine depuis l'ordinateur distant. La commande est simple :

```
$ vboxmanage import docker.ova
```

Confirmez que l'opération d'importation a fonctionné en utilisant `list vms` et essayez de lancer la VM depuis le bureau.

```
$ vboxmanage list vms"docker-project" {30ec7f7d-912b-40a9–8cc1-f9283f4edc61}
```

Si vous n'avez pas besoin d'un accès distant sophistiqué, vous pouvez également partager une VM depuis l'interface graphique. Avec la machine que vous souhaitez partager mise en surbrillance, cliquez sur le menu Fichier, puis sur Exporter l'appliance.

À venir : le monde merveilleux et mystérieux des LXC.

VirtualBox est idéal pour exécuter des opérations nécessitant un accès au noyau, pour lorsque vous avez besoin de sessions de bureau GUI, ou pour tester des systèmes d'exploitation de niche. Mais si vous êtes sur une machine Linux et que vous avez simplement besoin d'un accès rapide à un environnement Linux propre et que vous ne recherchez aucune version spéciale, alors vous seriez bien en peine de battre les conteneurs Linux.

À quelle vitesse sont les conteneurs LXC ? Vous le verrez par vous-même assez tôt. Mais, parce qu'ils partagent habilement de nombreuses ressources système avec à la fois l'hôte et d'autres conteneurs, ils fonctionnent comme des serveurs autonomes à plein régime tout en utilisant uniquement un espace de stockage et une mémoire minimaux.

> NOTE : Nous allons discuter du LXC classique, mais vous devez être conscient qu'il existe un environnement similaire des mêmes développeurs appelé LXD. LXD est essentiellement une nouvelle implémentation de l'interface LXC. Il utilise toujours LXC sous le capot, mais fournit un ensemble différent de commandes qui étendent la fonctionnalité à l'administration de réseau à distance.

### Démarrer avec LXC

Installer LXC sur votre poste de travail Ubuntu ? Un jeu d'enfant :

```
sudo apt updatesudo apt install lxc
```

C'est tout. Nous sommes prêts à nous mettre au travail. L'ensemble des compétences de base de LXC est en fait assez simple. Je vais vous montrer les trois ou quatre commandes dont vous aurez besoin pour faire fonctionner le tout, puis un conseil d'initiés qui, une fois que vous comprendrez comment LXC s'organise, vous laissera sans voix.

#### Lancer votre premier conteneur

Pourquoi ne pas plonger directement et créer votre premier conteneur ? La valeur donnée à `-n` définit le nom que je veux utiliser pour le conteneur, et `-t` indique à LXC de construire le conteneur à partir du modèle Ubuntu.

```
$ sudo lxc-create -n mycont -t ubuntu
```

Si vous avez décidé de créer, par exemple, un conteneur CentOS, alors vous devriez noter les dernières lignes de la sortie, car elles contiennent des informations sur le mot de passe que vous devez utiliser pour vous connecter :

```
$ sudo lxc-create -n centos_lxc -t centos 
[...]
Le mot de passe root temporaire est stocké dans :
        '/var/lib/lxc/centos_lxc/tmp_root_pass'
```

Vous vous connecterez en utilisant le nom d'utilisateur « root » et le mot de passe contenu dans ce fichier. Si, en revanche, votre conteneur a utilisé le modèle Ubuntu, alors vous utiliserez « ubuntu » pour votre nom d'utilisateur et votre mot de passe. Naturellement, si vous prévoyez d'utiliser ce conteneur pour quelque chose de sérieux, vous voudrez changer ce mot de passe immédiatement.

Utilisez `lxc-ls --fancy` pour vérifier l'état de votre conteneur :

```
$ sudo lxc-ls --fancy
NOM     ÉTAT    AUTOSTART GROUPES IPV4    IPV6 
mycont  ARRÊTÉ  0         -      -       -
```

Eh bien, il existe, mais apparemment il doit être démarré. Comme avant, `-n` spécifie par nom le conteneur que vous voulez démarrer. `-d` signifie « détacher » — ce qui signifie que vous ne voulez pas être automatiquement placé dans une session interactive lorsque le conteneur démarre.

```
$ sudo lxc-start -d -n mycont
```

La liste de vos conteneurs devrait maintenant afficher quelque chose comme ceci :

```
$ sudo lxc-ls --fancy
NOM     ÉTAT    AUTOSTART GROUPES IPV4        IPV6
mycont  EN COURS 0         -      10.0.3.142  -
```

Cette fois, le conteneur est en cours d'exécution et s'est vu attribuer une adresse IP. Vous pourriez utiliser cette adresse pour vous connecter en utilisant une session shell sécurisée.

```
$ ssh ubuntu@10.0.3.142
```

Alternativement, vous pouvez lancer une session shell root dans un conteneur en cours d'exécution en utilisant `lxc-attach`.

```
$ sudo lxc-attach -n mycontroot@mycont:/#
```

Lorsque vous avez terminé de jouer avec votre nouveau conteneur, vous pouvez soit exécuter `exit` pour vous déconnecter en laissant le conteneur en cours d'exécution :

```
root@mycont:/# exitexit
```

…ou éteindre le conteneur en utilisant `shutdown -h now`.

Mais avant de faire cela, découvrons à quelle vitesse les conteneurs LXC sont vraiment rapides. Le drapeau `-h` que j'ai ajouté à `shutdown` juste avant signifie « halt ». Si j'utilisais `r` à la place, plutôt que de s'éteindre définitivement, le conteneur redémarrerait. Donc, exécutons reboot et essayons de nous connecter à nouveau immédiatement pour voir combien de temps il faut au conteneur pour se remettre sur pied.

```
root@mycont:/# shutdown -r nowsudo lxc-attach -n mycont
```

Comment cela s'est-il passé ? Je parie que, au moment où vous avez réussi à retaper la commande `lxc-attach`, mycont était réveillé et prêt à l'action. Mais saviez-vous qu'en appuyant sur la touche flèche vers le haut dans Bash, la ligne de commande se remplira avec la commande précédente. Utiliser cela rendrait encore plus rapide la demande de connexion. Dans mon cas, il n'y a eu aucun délai perceptible. Le conteneur s'est éteint et a redémarré complètement en moins de 2 secondes !

> Les conteneurs Linux sont également très légers en ressources système. Contrairement à mon expérience avec les VM VirtualBox — où l'exécution de trois simultanément commence déjà à sérieusement impacter les performances de ma station de travail hôte de 8 Go — je peux lancer toutes sortes de conteneurs LXC sans subir aucun ralentissement.

#### Réparer un conteneur LXC froid

Maintenant, que dire de ce conseil d'initiés que je vous ai promis ? Eh bien, de retour dans un terminal sur la machine hôte (par opposition au conteneur), vous devrez ouvrir un shell administrateur en utilisant `sudo su`. À partir de maintenant — jusqu'à ce que vous tapiez `exit` — vous serez `sudo` à temps plein.

```
$ sudo su[sudo] password for username:#
```

Maintenant, changez de répertoire pour `/var/lib/lxc/` et listez le contenu. Vous devriez voir un répertoire avec le nom de votre conteneur. Si vous avez d'autres conteneurs sur le système, ils auront leurs propres répertoires également.

```
# cd /var/lib/lxc
# ls
mycont
```

Déplacez-vous dans votre répertoire de conteneur et listez son contenu. Il y aura un fichier appelé « config » et un répertoire appelé « rootfs ». Le « fs » signifie « file system ».

```
# cd mycont
# ls
config rootfs
```

C'est le répertoire rootfs que je veux vraiment que vous voyiez maintenant :

```
# cd rootfs
# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

Tous ces sous-répertoires qui remplissent rootfs… vous semblent-ils familiers ? Bien sûr ! Ils font tous partie de la norme de hiérarchie du système de fichiers Linux. Il s'agit essentiellement du répertoire racine (/) du conteneur… mais dans le système de fichiers de l'hôte. Tant que vous avez des permissions d'administrateur sur l'hôte, vous pourrez parcourir ces répertoires et éditer n'importe quel fichier que vous voulez — même lorsque le conteneur ne s'exécute pas.

Il y a toutes sortes de choses que vous pourrez faire avec cet accès, mais en voici une qui pourrait bien vous sauver la vie (professionnelle) un jour. Supposons que vous fassiez quelque chose de stupide sur un conteneur et que vous vous bloquiez, il n'y a maintenant rien qui vous empêche de naviguer dans le système de fichiers, de corriger le fichier de configuration que vous avez endommagé, et de retourner au travail. Allez-y : dites-moi que ce n'est pas cool.

Besoin de monter un seul processus sur un conteneur arrêté ? Utilisez simplement [chroot de la manière que je décris dans cet article](https://hackernoon.com/chroot-the-magical-healing-powers-of-the-original-linux-virtualization-tool-9aa4c3928711).

Mais cela devient encore mieux. Il est vrai que l'écosystème [Docker](https://hackernoon.com/too-many-choices-how-to-pick-the-right-tool-to-manage-your-docker-clusters-b5b3061b84b7) a gagné de nombreuses couches de fonctionnalités et de sophistication depuis que la technologie est sortie de l'ombre de LXC il y a quelques années. Sous le capot, cependant, il est toujours construit sur un paradigme structurel de base qui sera instantanément reconnaissable pour quiconque est familier avec LXC.

Ce qui signifie que, si vous êtes enclin à essayer la technologie de virtualisation à la croissance la plus rapide de la décennie, vous avez déjà une longueur d'avance.

### Écrire du code sur un serveur distant

Maintenant que vous avez compris ces environnements virtuels, que pouvez-vous en faire ? Eh bien, il est évident que de telles configurations sont parfaites pour jouer avec des outils et des architectures système.

Supposons que vous ne soyez pas intéressé par les trucs système, mais que vous aimeriez un endroit sûr pour construire des applications. Que veux-je dire par « sûr » ? Je parle d'un environnement où vous pouvez librement installer des bibliothèques et des paquets de dépendances sans avoir à vous soucier de déstabiliser votre ordinateur de travail personnel.

Mais il y a des limites à ce que cela peut vous apporter. Il se passe beaucoup de choses sous la surface des IDE comme Eclipse ou Visual Studio, et les gens deviennent très attachés à leur commodité. Mais s'attendre à pouvoir exécuter facilement toutes ces couches de complexité via une connexion distante — et surtout sur un serveur distant sans tête — est peut-être un peu ambitieux.

Mais quand même, ne serait-ce pas bien de travailler sur l'IDE de votre ordinateur portable et d'avoir le code sauvegardé, compilé et exécuté à distance… disons, sur une VM hébergée ou une instance cloud ? De cette façon, vous pourriez construire vos applications sur les serveurs où elles seront réellement exécutées sans avoir à risquer la stabilité de votre propre poste de travail.

C'est possible. Généralement, l'astuce consiste à faire en sorte que votre IDE fonctionne sur une session Secure Shell (SSH). Pour plus de détails, recherchez sur Internet quelque chose comme « eclipse edit java code on remote server ».

_Cet article est basé sur un chapitre de mon livre en ligne gratuit, [Résoudre pour la technologie : comment apprendre rapidement de nouvelles compétences précieuses dans un monde technologique en constante évolution](https://learntech.bootstrap-it.com/). Il y a beaucoup plus à découvrir sur mon site Bootstrap IT, y compris des liens vers mon livre, [Linux en Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9), et un cours hybride appelé [Linux en Mouvement](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui comprend plus de deux heures de vidéo et environ 40 % du texte de Linux en Action._