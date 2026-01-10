---
title: Comment créer et gérer des machines virtuelles avec l'outil en ligne de commande
  Vagrant
subtitle: ''
author: Eti Ijeoma
co_authors: []
series: null
date: '2023-04-03T20:15:11.000Z'
originalURL: https://freecodecamp.org/news/create-and-manage-virtual-machines-with-vagrant
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-01-at-23.42.01-1.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: virtual machine
  slug: virtual-machine
seo_title: Comment créer et gérer des machines virtuelles avec l'outil en ligne de
  commande Vagrant
seo_desc: 'Creating and managing virtual machines used to be a tedious and time-consuming
  process. Replicating the VM on a different server can also be challenging, and it
  gets harder if you have to replicate multiple VMs.

  But then Vagrant came along, a command...'
---

Créer et gérer des machines virtuelles était autrefois un processus fastidieux et chronophage. Répliquer la machine virtuelle sur un serveur différent peut également être un défi, et cela devient plus difficile si vous devez répliquer plusieurs machines virtuelles.

Mais ensuite, Vagrant est arrivé, un outil en ligne de commande ou shell qui fonctionne généralement avec des [hyperviseurs de type 2](https://en.wikipedia.org/wiki/Hypervisor#:~:text=Type%2D2%20or%20hosted%20hypervisors). Vous l'utilisez pour créer et gérer des machines virtuelles. C'est un outil puissant qui peut aider à simplifier la configuration et la gestion de votre environnement de développement.

Vagrant peut être vraiment utile si vous travaillez en équipe ou avec plusieurs personnes. Cela est dû au fait qu'il garantit la cohérence de votre environnement de développement en assurant que tout le monde utilise le même environnement, évitant ainsi les problèmes de compatibilité.

Ce tutoriel vous guidera à travers le processus de configuration d'une seule machine virtuelle Ubuntu Linux avec Vagrant et la configuration d'un serveur web à l'intérieur.

### Prérequis pour ce tutoriel :

* Un ordinateur avec au moins 8 Go de RAM

* Connaissance de base du système d'exploitation Linux

### Outils requis et installation

* **Oracle VirtualBox :** Rendez-vous sur le site [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads), trouvez la version de VirtualBox compatible avec votre système d'exploitation et suivez les instructions pour la télécharger et l'installer. Virtual Box fournira l'environnement virtuel, tandis que Vagrant le configurera et le gérera.

* **Vagrant :** Visitez le site [Vagrant](https://www.vagrantup.com/) et suivez les instructions pour télécharger et installer le binaire adapté à votre système d'exploitation. Dans ce tutoriel, nous utiliserons le binaire open-source de Vagrant.

Pour vérifier si l'installation a réussi, lancez votre outil de ligne de commande préféré et entrez la commande suivante pour afficher le numéro de version installé :

```bash
$ vagrant --version
```

## Comment créer un environnement de développement avec Vagrant

Pour créer un projet Vagrant, commencez par créer un nouveau répertoire de projet à l'emplacement de votre choix pour la configuration Vagrant et les fichiers associés.

```bash
$ mkdir vagrant-project && cd vagrant-project
```

Dans ce répertoire, créez un nouveau Vagrantfile. Vagrant utilise la configuration dans le Vagrantfile pour construire la machine virtuelle. Par défaut, Vagrant synchronise le répertoire du projet où le Vagrantfile est initialisé vers /vagrant. Cela élimine le besoin de s'inquiéter des volumes pour la persistance des données.

Vagrant utilise le concept de boxes. Les boxes sont des images de base complètes d'un système d'exploitation. Le dépôt public de [vagrant box](https://app.vagrantup.com/boxes/search) contient une liste de boxes possibles. Il est bon de choisir une box qui correspond au système d'exploitation utilisé dans votre environnement de production.

Une box Vagrant porte le nom de l'utilisateur ou de l'organisation qui l'a créée et le nom de la box `user/boxname`. Pour initialiser le fichier de configuration Vagrant avec une box Ubuntu, exécutez la commande :

```bash
$ vagrant init ubuntu/trusty64
```

Cela génère un Vagrantfile avec une box Ubuntu/trusty64 dans le répertoire courant. Le Vagrantfile, écrit en Ruby, contient le type de machine virtuelle à utiliser et diverses options commentées supplémentaires telles que le réseau, le transfert de port, la capacité du disque, etc., pour aider à configurer l'environnement de développement.

Vous pouvez ajouter le flag `--minimal` à la commande d'initialisation du Vagrantfile pour générer un Vagrantfile sans aucun paramètre supplémentaire.

Ouvrez le Vagrantfile avec l'éditeur de votre choix. J'utiliserai l'éditeur Vim dans ce tutoriel.

```bash
 $ vim Vagrantfile
```

En supprimant les commentaires informatifs et certaines configurations avancées, le fichier ressemblera à ceci :

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.provider "virtualbox" do |vb| vb.memory = "1024"
 end
  config.vm.provision :shell, path: "simple-node-project.sh", privileged: false
end
```

Le fichier `simple-node-project.sh` est un script bash qui installe Node.js et Git, clone un projet qui crée un serveur web simple Node.js, et démarre le serveur.

```bash
#!/bin/bash

 sudo apt-get update -y

 ## Git ##
 echo '###Installation de Git..'
 sudo apt-get install git -y

 git clone https://github.com/Aijeyomah/simple-node-app.git

# Installation de la dernière version de Node et npm
 sudo apt-get install -y curl software-properties-common

# Ajout du PPA Node.js
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# Installation de Node.js et npm
sudo apt-get install -y nodejs

# Vérification de l'installation
node -v
npm -v

echo "Node.js a été installé avec succès."

# navigation vers le répertoire de l'application et démarrage de l'application
cd simple-node-app
node index.js &
```

Cette configuration Vagrant met en place les éléments suivants :

* `ubuntu/trusty64` est spécifié comme image de base de la box virtuelle

* Transfère le port 8000 de la machine virtuelle vers le port 8000 de la machine hôte.

* Alloue 1 Go de mémoire à la machine virtuelle

* Exécute `simple-node-project` pour provisionner la machine virtuelle

* Pour que le provisionneur shell exécute le script en tant qu'utilisateur non-root dans un shell de connexion, `privileged` est défini sur `false`

Enregistrez le `Vagrantfile` et démarrez la machine virtuelle en exécutant la commande suivante :

```bash
$ vagrant up
```

La première fois que cette commande est exécutée, elle téléchargera la dernière version de la box spécifiée, et elle configurera et démarrera la machine virtuelle. Ce processus peut prendre un certain temps, mais lorsque la box Ubuntu existe dans la machine locale, la machine virtuelle démarrera immédiatement.

Une fois la machine virtuelle en cours d'exécution, vous pouvez accéder à la page web en ouvrant un navigateur web et en naviguant vers [`http://localhost:8000`](http://localhost:8080). Vous devriez voir la page de message `Hello World` si tout a été configuré correctement.

## Comment gérer Vagrant

Vous pouvez utiliser Vagrant pour gérer la machine virtuelle en cours d'exécution. Voici quelques commandes Vagrant utiles :

`vagrant up` : Lance la machine virtuelle et la provisionne selon les paramètres du Vagrantfile. Cette commande se connectera simplement à la machine virtuelle si elle est déjà en cours d'exécution.

`vagrant halt` : Arrête la machine virtuelle en envoyant un signal d'arrêt au système d'exploitation invité. Cette commande est similaire à l'arrêt d'un ordinateur réel.

`vagrant reload` : Redémarre la machine virtuelle et la re-provisionne en fonction des modifications du Vagrantfile.

`vagrant ssh` : Se connecte à la machine virtuelle via SSH. Cette commande est utile pour accéder à l'interface de ligne de commande de la machine virtuelle.

`vagrant status` : Affiche l'état actuel de la machine virtuelle, y compris si elle est en cours d'exécution, arrêtée ou suspendue.

`vagrant destroy` : Supprime la machine virtuelle et toutes les ressources associées. Cette commande est utile pour nettoyer votre environnement de développement.

## Conclusion

Dans cet article, nous avons appris comment utiliser Vagrant pour configurer un environnement de développement reproductible et cohérent.

L'utilisation de Vagrant peut vous aider à configurer un environnement de développement virtuel qui imite de près votre environnement de production. Cela vous permet de tester et de développer votre code dans un environnement cohérent et isolé.