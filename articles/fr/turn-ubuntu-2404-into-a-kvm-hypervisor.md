---
title: Comment transformer Ubuntu 24.04 en un hyperviseur KVM – Installation rapide
  avec gestion Web
subtitle: ''
author: Shamsuddoha Ranju
co_authors: []
series: null
date: '2025-04-28T15:45:09.631Z'
originalURL: https://freecodecamp.org/news/turn-ubuntu-2404-into-a-kvm-hypervisor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745591647377/613d9a44-cc2b-45b7-b1d1-5fc3154b9623.png
tags:
- name: KVM
  slug: kvm
- name: hypervisor
  slug: hypervisor
- name: virtualization
  slug: virtualization
- name: virtual machine
  slug: virtual-machine
- name: vm
  slug: vm
seo_title: Comment transformer Ubuntu 24.04 en un hyperviseur KVM – Installation rapide
  avec gestion Web
seo_desc: 'Virtualization lets you run multiple operating systems on one machine.
  It’s perfect for testing apps, hosting servers, or learning DevOps.

  A hypervisor is the software that lets you run multiple virtual machines on a single
  physical machine, and the ...'
---

La virtualisation vous permet d'exécuter plusieurs systèmes d'exploitation sur une seule machine. Elle est parfaite pour tester des applications, héberger des serveurs ou apprendre le DevOps.

Un hyperviseur est le logiciel qui vous permet d'exécuter plusieurs machines virtuelles sur une seule machine physique, et la Machine Virtuelle basée sur le Noyau (KVM) est l'une des meilleures. Intégré à Linux, KVM est rapide (performances quasi natives), open-source (gratuit !) et flexible (supporte Windows, Linux, et plus). Il est utilisé par les fournisseurs de cloud et les homelabbers pour sa stabilité et sa faible surcharge.

Si vous souhaitez transformer votre système Ubuntu 24.04 ou Kubuntu 24.04 (Kubuntu est une variante d'Ubuntu avec le bureau KDE Plasma) en un hyperviseur puissant sans la complexité de **Proxmox**, ce guide est fait pour vous. Avec KVM, vous créerez des machines virtuelles (VM) en quelques minutes, et avec le gestionnaire basé sur le web de Cockpit, vous les contrôlerez depuis votre navigateur.

Dans ce tutoriel, vous transformerez un Ubuntu 24.04 ou Kubuntu 24.04 Desktop ou Server – neuf ou existant – en un hyperviseur KVM. Vous configurerez le backend (KVM, QEMU, libvirt), ajouterez Cockpit pour la gestion des VM basée sur le web, et créerez une VM invitée pour tout tester. Que vous soyez un codeur, un homelabber ou un passionné d'IT, ce guide est adapté aux débutants.

## Table des matières

* [Avant de commencer : Ce que vous devez savoir](#heading-avant-de-commencer-ce-que-vous-devez-savoir)
    
* [Ce dont vous aurez besoin](#heading-ce-dont-vous-aurez-besoin)
    
* [Pourquoi KVM sur Ubuntu/Kubuntu 24.04 ?](#heading-pourquoi-kvm-sur-ubuntukubuntu-2404)
    
* [Étape 1 : Vérifier la prise en charge de la virtualisation](#heading-etape-1-verifier-la-prise-en-charge-de-la-virtualisation)
    
* [Étape 2 : Installer KVM et les outils backend](#heading-etape-2-installer-kvm-et-les-outils-backend)
    
* [Étape 3 : Configurer un pont réseau](#heading-etape-3-configurer-un-pont-reseau)
    
* [Étape 4 : Installer Cockpit pour la gestion Web](#heading-etape-4-installer-cockpit-pour-la-gestion-web)
    
* [Étape 5 : Créer une VM invitée](#heading-etape-5-creer-une-vm-invitee)
    
* [Étape 6 : Exécuter et tester votre VM invitée](#heading-etape-6-executer-et-tester-votre-vm-invitee)
    
* [Continuez à explorer votre hyperviseur](#heading-continuez-a-explorer-votre-hyperviseur)
    
* [Conclusion](#heading-conclusion)
    

## Avant de commencer : Ce que vous devez savoir

Ce guide est conçu pour les débutants en virtualisation, mais vous aurez besoin de quelques compétences de base :

* Exécuter des commandes terminal comme `sudo apt install` ou `nano`, etc.
    
* Navigation de base sous Linux (par exemple, éditer des fichiers dans `/etc`).
    
* Connaissances de base en réseau, comme la compréhension des interfaces réseau (par exemple, `enp4s0` ou `wlp3s0`), des adresses IP, et des concepts comme le pontage ou le NAT. Vous utiliserez des outils comme `ip link` ou `nmcli` pour configurer un pont réseau à l'étape 3.
    
* Optionnel : L'expérience avec les VM aide mais n'est pas requise – je vais tout expliquer.
    

Pas de soucis si des termes comme « libvirt » vous sont nouveaux. Je les expliquerai au fur et à mesure.

## Ce dont vous aurez besoin

* **Un ordinateur** : Exécutant Ubuntu 24.04 ou Kubuntu 24.04 Desktop ou Server (neuf ou existant). Minimum : 4 Go de RAM, 20 Go de stockage, CPU avec prise en charge de la virtualisation (Intel VT-x ou AMD-V). Plus de RAM/stockage pour plusieurs VM.
    
* **Accès Internet** : Pour télécharger des paquets et des ISO de VM.
    
* **Un navigateur web** : Firefox (par défaut sur Ubuntu) ou Chrome pour accéder à Cockpit.
    
* **Une image ISO** : Une image ISO pour votre VM invitée (par exemple, ISO Ubuntu 24.04 Desktop depuis ubuntu.com ou ISO Windows si vous l'avez déjà).
    
* **30–45 minutes** : Selon la vitesse de votre configuration.
    

## Pourquoi KVM sur Ubuntu/Kubuntu 24.04 ?

KVM transforme votre noyau Linux en un hyperviseur, vous permettant d'exécuter des VM avec une vitesse quasi native. Associé à QEMU (pour l'émulation matérielle) et libvirt (pour la gestion), c'est une alternative légère à **Proxmox** ou **VMware**. Ses points forts incluent :

* **Performance** : Exécute les VM efficacement, idéal pour les homelabs ou les environnements de développement.
    
* **Gratuit et Open-Source** : Pas de licences, comme Ubuntu/Kubuntu, etc.
    
* **Flexibilité** : Supporte divers systèmes d'exploitation invités (Linux, Windows, BSD).
    
* **Intégration** : L'interface web de Cockpit rend la gestion des VM facile, sans CLI requise.
    

Voici ce que fait chaque outil :

* **KVM** : Un module du noyau Linux qui transforme votre système en un hyperviseur, permettant aux VM de s'exécuter avec des performances quasi natives en utilisant les fonctionnalités de virtualisation du CPU (par exemple, Intel VT-x).
    
* **QEMU** : Un émulateur puissant qui fournit le matériel virtuel (par exemple, CPU, disque, réseau) pour vos VM, travaillant avec KVM pour une exécution rapide.
    
* **libvirt** : Une couche de gestion qui simplifie la création de VM, le réseau et le stockage, offrant des outils comme `virsh` et des API pour l'automatisation.
    
* **Cockpit** : Une interface basée sur le web pour gérer les VM, les ressources système et les réseaux, parfaite pour les débutants qui veulent un tableau de bord visuel.
    

Ubuntu 24.04 (« Noble Numbat ») apporte le dernier noyau et outils, assurant une compatibilité KVM de premier ordre. Construisons votre hyperviseur !

## Étape 1 : Vérifier la prise en charge de la virtualisation

Tout d'abord, vous voulez confirmer que votre CPU prend en charge la virtualisation (la plupart des CPU modernes le font). Pour cela, ouvrez un terminal (comme Konsole sur Kubuntu) et exécutez :

```bash
lscpu | grep Virtualization
```

Recherchez « VT-x » (Intel) ou « AMD-V » (AMD). Si présent, vous êtes bon !

Si rien ne s'affiche, vérifiez votre BIOS/UEFI :

* Redémarrez, entrez dans le BIOS (généralement `F2`, `Del`, ou `Esc`).
    
* Activez « Intel VT-x » ou « AMD-V » sous les paramètres du CPU.
    
* Sauvegardez et redémarrez.
    

![Terminal Konsole sur Kubuntu affichant la sortie de 'lscpu | grep Virtualization' confirmant la prise en charge de VT-x pour KVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745226012162/337e2324-50b3-4bd9-b040-01c2ac919e7c.png align="center")

## Étape 2 : Installer KVM et les outils backend

Installons KVM, QEMU et libvirt. Ceux-ci formeront l'épine dorsale de votre hyperviseur :

Commencez par mettre à jour votre système (vous devrez peut-être redémarrer votre ordinateur après la mise à jour) :

```bash
sudo apt update && sudo apt upgrade -y
```

Ensuite, installez les paquets de virtualisation :

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
```

* `qemu-kvm` : Émule le matériel pour les VM.
    
* `libvirt-daemon-system` : Gère les VM.
    
* `libvirt-clients` : Outils CLI comme `virsh` pour la gestion de l'hyperviseur.
    
* `bridge-utils` : Pour le pontage réseau.
    

Ensuite, vérifiez que KVM est chargé :

```bash
lsmod | grep kvm
```

Vous verrez « kvm_intel » ou « kvm_amd » si c'est réussi.

![Terminal Konsole sur Kubuntu affichant la sortie de 'lsmod | grep kvm' montrant le module kvm_intel chargé pour KVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745226199517/a146d89d-2894-4bbc-b241-11a8ed385758.png align="center")

Enfin, ajoutez votre utilisateur (actuel) au groupe `libvirt` pour les permissions :

```bash
sudo usermod -aG libvirt $USER
```

Déconnectez-vous et reconnectez-vous pour appliquer ces changements.

## Étape 3 : Configurer un pont réseau

Les VM ont besoin d'un accès réseau, vous allez donc créer un pont (`br0`) pour les connecter à votre réseau physique. Cela permet aux VM d'agir comme des appareils sur votre réseau (réseau en pont).

Ubuntu 24.04 et Kubuntu 24.04 Desktop utilisent généralement NetworkManager, tandis qu'Ubuntu Server peut utiliser Netplan. Nous privilégierons l'approche NetworkManager, avec Netplan comme alternative.

**Note** : L'installation de libvirt (Étape 2) crée un pont par défaut appelé `virbr0` pour le réseau basé sur NAT, qui isole les VM du réseau physique (IP comme `192.168.122.x`). Pour un accès réseau direct (IP comme `192.168.0.x`), utilisez `br0` comme décrit ci-dessous, et sélectionnez-le dans la configuration de la VM de l'Étape 5.

Vous pouvez vérifier si votre système utilise NetworkManager ou Netplan. Ouvrez une console et exécutez `systemctl status NetworkManager`. Si vous voyez le statut actif et en cours d'exécution, utilisez NetworkManager.

![Terminal Konsole sur Kubuntu affichant la sortie de 'systemctl status NetworkManager' confirmant le statut de NetworkManager.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745305149513/0926f09c-1748-484f-af4c-37dcb82d06a5.png align="center")

### Option 1 : NetworkManager (Recommandé pour Kubuntu/Ubuntu desktop)

Vérifiez votre interface réseau :

```bash
ip link
```

Exemple : `enp4s0`. Remplacez `enp4s0` ci-dessous si le vôtre est différent.

Tout d'abord, trouvez le nom de votre connexion Ethernet :

```bash
nmcli connection show
```

Recherchez la colonne **NAME** où **DEVICE** est `enp4s0` (par exemple, « Connexion filaire 1 » ou « Connexion Ethernet »). Notez ce nom. Ignorez `virbr0`, qui est le pont NAT par défaut de libvirt.

Ensuite, créez un pont nommé `br0` :

```bash
sudo nmcli connection add type bridge ifname br0 con-name bridge-br0
```

Associez votre interface au pont :

```bash
sudo nmcli connection add type ethernet ifname enp4s0 master br0 con-name bridge-slave-enp4s0
```

Désactivez l'ancienne connexion (remplacez par le nom de votre connexion identifié précédemment) :

```bash
sudo nmcli connection down "Connexion filaire 1"
sudo nmcli connection delete "Connexion filaire 1"
```

Activez le DHCP sur le pont :

```bash
sudo nmcli connection modify bridge-br0 ipv4.method auto
```

Activez le pont :

```bash
sudo nmcli connection up bridge-br0
```

Vérifiez :

```bash
ip addr show br0
nmcli connection show
```

Maintenant, vous voulez vous assurer que `br0` est actif, `enp4s0` est associé, et `virbr0` est séparé. Tout d'abord, testez l'internet avec `ping 8.8.8.8`.

Ensuite, vous devez définir `br0` dans libvirt (pour qu'il apparaisse dans le menu déroulant du réseau VM de Cockpit). Pour cela, créez `br0.xml` dans votre répertoire personnel :

```bash
nano ~/br0.xml
```

Ensuite, ajoutez ce qui suit :

```xml
<network>
  <name>br0</name>
  <forward mode='bridge'/>
  <bridge name='br0'/>
</network>
```

Enregistrez et quittez (`Ctrl+O`, `Entrée`, `Ctrl+X`).

Maintenant, définissez et démarrez ce qui suit :

```bash
sudo virsh net-define ~/br0.xml
sudo virsh net-start br0
sudo virsh net-autostart br0
```

Vérifiez comme suit :

```bash
virsh net-list --all
```

Vous pouvez maintenant supprimer `~/br0.xml` après la définition, car libvirt le stocke dans `/etc/libvirt/qemu/networks/`.

```bash
rm ~/br0.xml
```

### Option 2 : Netplan (Pour Ubuntu Server ou si préféré)

Si vous voyez `renderer: networkd` dans `/etc/netplan/???.yaml` ou préférez Netplan, suivez ces étapes.

Tout d'abord, vérifiez votre interface :

```bash
ip link
```

Exemple : `enp4s0`.

Ensuite, éditez la configuration Netplan comme suit :

```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

Utilisez ce qui suit :

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp4s0:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp4s0]
      dhcp4: yes
```

Enregistrez et quittez (`Ctrl+O`, `Entrée`, `Ctrl+X`).

Maintenant, définissez des permissions strictes pour éviter les erreurs :

```bash
sudo chmod 600 /etc/netplan/01-netcfg.yaml
```

Et appliquez :

```bash
sudo netplan apply
```

Maintenant, vérifiez :

```bash
ip addr show br0
```

Testez l'internet avec `ping 8.8.8.8` (depuis la console).

![Terminal Konsole sur Kubuntu affichant la sortie de 'nmcli connection show' avec bridge-br0 actif, enp4s0 associé, et virbr0 présent pour le réseau KVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745227201229/35988335-5ff1-49bc-9809-e9c08d6798c4.png align="center")

**Dépannage** :

* **Erreur de permissions** : Si Netplan se plaint des permissions « trop ouvertes », revérifiez `sudo chmod 600 /etc/netplan/01-netcfg.yaml`.
    
* **Conflit NetworkManager** : Si vous utilisez Netplan, assurez-vous que `/etc/netplan/01-network-manager-all.yaml` est sauvegardé ou supprimé (`sudo mv /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak`).
    
* **Pas d'internet** : Redémarrez NetworkManager (`sudo systemctl restart NetworkManager`) ou redémarrez.
    
* **Mauvais pont** : Si une VM utilise `virbr0` (NAT, `192.168.122.x`), revérifiez le paramètre réseau de l'Étape 5 et sélectionnez `br0`.
    
* **br0 manquant dans Cockpit** : Définissez `br0` dans libvirt (étape 9 ci-dessus) ou assurez-vous que `br0` est actif (`ip addr show br0`).
    

## Étape 4 : Installer Cockpit pour la gestion Web

Cockpit fournit une interface web élégante pour gérer les VM. Installons-la.

Tout d'abord, vous devez installer Cockpit et son plugin VM :

```bash
sudo apt install cockpit cockpit-machines -y
```

Ensuite, vous pouvez démarrer et activer Cockpit :

```bash
sudo systemctl enable --now cockpit.socket
systemctl status cockpit.socket
```

Maintenant, ouvrez votre navigateur (par exemple, Firefox sur Ubuntu) et visitez :

```plaintext
https://localhost:9090
```

Ou utilisez l'IP de votre serveur KVM (par exemple, `https://192.168.0.100:9090`) si vous êtes à distance. Connectez-vous avec votre nom d'utilisateur et mot de passe. Ignorez l'avertissement de certificat auto-signé.

Autorisez le port de Cockpit si vous utilisez un pare-feu :

```bash
sudo ufw allow 9090
```

Vous verrez le tableau de bord de Cockpit. Activez l'accès administratif en cliquant sur « **Activer l'accès administratif** ». Ensuite, cliquez sur « **Machines virtuelles** » pour gérer les VM.

![Firefox sur Kubuntu affichant la page de connexion de Cockpit à https://localhost:9090 pour la gestion des VM basée sur le web.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745227293385/96291774-d4cf-4de2-9392-3947ade4bb8b.png align="center")

## Étape 5 : Créer une VM invitée

Créons une VM invitée en utilisant Cockpit. Nous utiliserons une ISO Ubuntu 24.04 Desktop comme exemple :

Pour commencer, téléchargez l'ISO Ubuntu 24.04 Desktop depuis ubuntu.com et enregistrez-la (par exemple, `/home/ranju/Downloads/ubuntu-24.04.1-desktop-amd64.iso`).

Dans Cockpit, allez dans « Machines virtuelles » et cliquez sur « Créer une VM ». Voici les spécifications :

* **Nom** : TestVM
    
* **Type d'installation** : Support d'installation local (ou votre type d'installation souhaité)
    
* **Source d'installation** : Parcourez jusqu'à votre ISO (par exemple, `/home/ranju/Downloads/ubuntu-24.04.1-desktop-amd64.iso`).
    
* **OS** : Sélectionnez « Ubuntu 24.04 » (généralement Cockpit le détecte automatiquement).
    
* **Stockage** : Créer un nouveau volume qcow2 (préféré). *Note : le disque est créé dans* `/var/lib/libvirt/images/`*.*
    
* **Limite de stockage** : 20 Go (ajustez si nécessaire).
    
* **Mémoire** : 4 Go (ajustez si nécessaire).
    

Cliquez sur « Créer et Éditer ». Cockpit ouvre une boîte de dialogue avancée où il y a des options de personnalisation (par exemple, CPU, Interfaces réseau et ordre de démarrage, etc.). Assurez-vous que `br0` a été sélectionné comme source d'interface. Enfin, cliquez sur « **Installer** ».

![Interface web de Cockpit dans Firefox sur Kubuntu montrant la boîte de dialogue Créer une VM avec les paramètres de TestVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745228999671/4d80faf7-d8f8-4395-985e-298b4add426c.png align="center")

Dans la console VM de Cockpit, suivez l'installateur pour configurer le système d'exploitation invité (nom d'utilisateur, mot de passe, etc.).

**Dépannage** :

* **Erreur de permissions** : Si vous avez une erreur de permissions pour l'ISO, copiez l'ISO dans le dossier temporaire par défaut (`/tmp/`) et localisez l'ISO depuis là.
    
    ```bash
    cp /home/ranju/Downloads/ubuntu-24.04.1.iso /tmp/
    ```
    

## Étape 6 : Exécuter et tester votre VM invitée

Votre VM est en cours d'exécution ! Testons-la :

1. Dans Cockpit, sous « Machines virtuelles », cliquez sur TestVM. Vous verrez sa console (une vue en direct de l'écran de la VM).
    
2. Connectez-vous à l'Ubuntu invité en utilisant les identifiants que vous avez définis.
    
3. Testez le réseau :
    
    * Ouvrez un terminal dans la VM (via la console de Cockpit).
        
    * Exécutez `ip addr` dans la console pour confirmer une IP de réseau physique (par exemple, `192.168.0.x` avec `br0`, pas `192.168.122.x` avec `virbr0`).
        
    * Exécutez `ping 8.8.8.8` pour confirmer l'accès à Internet.
        
4. Expérimentez : Ouvrez un navigateur dans la VM, visitez un site web ou installez des applications pour simuler une utilisation réelle.
    

Si la VM démarre et se connecte à votre réseau, votre hyperviseur KVM est au top ! Vous pouvez l'arrêter, la redémarrer ou la supprimer depuis Cockpit.

![Interface web de Cockpit dans Firefox sur Kubuntu affichant la console TestVM avec le bureau Ubuntu 24.04.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745307664700/ed54d452-4979-4468-a7fe-1dd538844e25.png align="center")

## Continuez à explorer votre hyperviseur

Vous avez transformé votre Ubuntu 24.04 en un hyperviseur KVM – félicitations ! Essayez ces prochaines étapes :

* **Ajoutez plus de VM** : Créez des VM Windows ou d'autres Linux en utilisant différentes ISO.
    
* **Utilisez virt-manager** : Installez virt-manager pour une alternative basée sur le bureau à Cockpit (`sudo apt install virt-manager`).
    
* **Sauvegardez les VM** : Exportez les disques VM avec `virsh` pour la sécurité.
    
* **Passez à l'échelle** : Ajoutez du stockage ou de la RAM pour des charges de travail plus lourdes, comme dans mon guide de cluster Proxmox.
    

Vérifiez vos VM à tout moment via CLI :

```bash
virsh list --all
```

## Conclusion

Vous avez construit un hyperviseur KVM rapide et gratuit sur Ubuntu 24.04, complet avec l'interface web de Cockpit et une VM invitée en cours d'exécution. C'est un terrain de jeu parfait pour le codage, les tests ou le plaisir du homelab.

Partagez vos idées ou commentaires avec moi – j'adorerais les entendre !