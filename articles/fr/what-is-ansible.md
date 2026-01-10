---
title: Qu'est-ce qu'Ansible ? Un outil pour automatiser des parties de votre travail
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-10-29T20:42:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-ansible
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/ansble.png
tags:
- name: ansible
  slug: ansible
- name: automation
  slug: automation
seo_title: Qu'est-ce qu'Ansible ? Un outil pour automatiser des parties de votre travail
seo_desc: 'Hello everyone, today we will talk about Ansible, a fantastic software
  tool that allows you to automate cross-platform computer support in a simple but
  effective way.

  Table of Contents


  What is Ansible?

  How Does Ansible Work?

  Ansible''s Architecture

  P...'
---

Bonjour à tous, aujourd'hui nous allons parler d'Ansible, un outil logiciel fantastique qui permet d'automatiser le support informatique multiplateforme de manière simple mais efficace.

## Table des matières

- Qu'est-ce qu'Ansible ?
- Comment fonctionne Ansible ?
- Architecture d'Ansible
  - Plugins
  - Modules
  - Inventaires
  - Playbook
- Avantages de l'utilisation d'Ansible
- Pourquoi Ansible est-il si important ?
- Comment installer et configurer Ansible sur Ubuntu
- Conclusion
- Références


## Qu'est-ce qu'Ansible ?

Ansible est un outil qui génère des instructions écrites pour automatiser le travail des professionnels de l'informatique dans l'ensemble de l'infrastructure système.

Il est particulièrement conçu pour les professionnels de l'informatique qui l'utilisent pour le déploiement d'applications, la gestion de la configuration, l'orchestration intra-service et pratiquement tout ce qu'un administrateur système fait sur une base hebdomadaire ou quotidienne. 

Ansible est simple à installer car il ne nécessite aucun logiciel agent ou une autre infrastructure de sécurité.

Bien qu'Ansible soit à la pointe de l'automatisation, de l'administration système et de DevOps, il est également précieux en tant qu'outil pour les développeurs à utiliser dans leur travail quotidien. 

Ansible permet de configurer non pas une seule machine, mais un réseau complet de machines en une seule fois, et il ne nécessite aucune connaissance en programmation.

## Comment fonctionne Ansible ?

Ansible se connecte aux nœuds d'un réseau (clients, serveurs, etc.) et envoie ensuite un petit programme appelé module Ansible à chaque nœud. 

Il exécute ensuite ces modules via SSH et les supprime une fois qu'ils sont terminés. 

Votre nœud de contrôle Ansible doit avoir un accès de connexion aux nœuds gérés pour que cette interaction fonctionne. 

La méthode d'authentification la plus fréquente est l'utilisation de clés SSH, mais d'autres méthodes sont également autorisées.

Si vous souhaitez voir comment installer et commencer à utiliser Ansible, nous allons couvrir cela ci-dessous.

## Architecture d'Ansible

Examinons maintenant l'architecture d'Ansible et comment il gère les opérations.

### Plugins Ansible

Les plugins sont des morceaux de code supplémentaires qui améliorent la fonctionnalité, et vous les avez probablement utilisés dans de nombreux autres outils et plateformes. Vous pouvez utiliser les plugins intégrés d'Ansible ou créer les vôtres. 

Exemples : 

- Action Plugins
- Become Plugins
- Cache Plugins
- Callback Plugins
- Cliconf Plugins
- Connection Plugins
- HTTP API Plugins
- Inventory Plugins
- Lookup Plugins
- Netconf Plugins
- Tests

### Modules Ansible

Les modules sont de petits programmes qu'Ansible distribue à tous les nœuds ou hôtes distants à partir d'une station de travail de contrôle centrale. Les modules contrôlent des éléments comme les services et les paquets et peuvent être exécutés via des playbooks. 

Ansible exécute tous les modules nécessaires pour installer des mises à jour ou compléter toute opération requise, puis les supprime une fois qu'ils sont terminés.


### Inventaires Ansible

Ansible utilise un fichier d'inventaire pour suivre les hôtes qui font partie de votre infrastructure, puis y accède pour effectuer des commandes et des playbooks.

Ansible fonctionne en parallèle avec divers systèmes de votre infrastructure. Il y parvient en sélectionnant les méthodes mentionnées dans le fichier d'inventaire d'Ansible, qui est enregistré dans l'emplacement de l'hôte par défaut.

Une fois l'inventaire enregistré, vous pouvez utiliser un simple fichier texte pour assigner des variables à n'importe quel hôte, et vous pouvez récupérer l'inventaire à partir de diverses sources. 


### Playbook Ansible

Les professionnels de l'informatique peuvent utiliser les playbooks Ansible pour programmer des applications, des services, des nœuds serveurs et d'autres appareils sans partir de zéro. Les playbooks Ansible, ainsi que les conditions, les variables et les tâches qu'ils contiennent, peuvent être stockés, partagés et réutilisés indéfiniment.

Les playbooks Ansible fonctionnent de manière similaire à des manuels de tâches. Ce sont des fichiers [YAML](https://en.wikipedia.org/wiki/YAML) simples, un langage de sérialisation de données lisible par l'homme. 

Les playbooks sont au cœur de ce qui rend Ansible si populaire. Ils spécifient des activités qui peuvent être complétées rapidement sans que l'utilisateur ait besoin de connaître ou de se souvenir d'une syntaxe spécifique.


## Avantages de l'utilisation d'Ansible

- Ansible est rapide et facile à utiliser, car il exécute toutes ses opérations via SSH et ne nécessite pas l'installation d'agents.
- Ansible est un outil gratuit et open-source, et il est simple à installer et à utiliser : les playbooks d'Ansible ne nécessitent aucune connaissance particulière en codage.
- Ansible peut être utilisé pour effectuer des tâches simples telles que s'assurer qu'un service fonctionne ou redémarrer à partir de la ligne de commande sans avoir besoin de fichiers de configuration.

Dans un système plus étendu ou plus uniforme, Ansible peut être mieux adapté. Il fournit également un ensemble de modules pour gérer diverses méthodes et infrastructures cloud.

## Pourquoi Ansible est-il si important ?

La modernisation et la transformation numérique nécessitent une automatisation à la fois nécessaire et intentionnelle. Nous avons besoin d'une nouvelle solution de gestion dans les contextes dynamiques d'aujourd'hui pour augmenter la vitesse, l'échelle et la stabilité dans toute l'infrastructure IT.

La technologie est notre instrument le plus puissant pour l'amélioration des produits. Auparavant, accomplir cela nécessitait une quantité significative de travail manuel et une coordination complexe. Mais aujourd'hui, Ansible - un moteur d'automatisation IT simple mais puissant utilisé par des milliers d'entreprises pour simplifier leurs configurations et accélérer les opérations DevOps - est disponible.

## Comment installer Ansible sur Ubuntu

Exécutez les commandes suivantes pour configurer le PPA sur votre machine et installer Ansible :

Mettre à jour le dépôt :

```
sudo apt-get update
```

Installer les propriétés logicielles :

```
sudo apt-get install software-properties-common
```

Puis installer Ansible comme ceci :

```
sudo apt-add-repository --yes --update ppa:ansible/ansible
```

Ensuite, exécutez ceci :

```
sudo apt-get install ansible
```

Vous devriez obtenir quelque chose de similaire à ce qui est montré ci-dessous :

![ansible_installation](https://www.freecodecamp.org/news/content/images/2021/10/ansible_installation.png)

Maintenant que vous avez installé Ansible avec succès, testons s'il fonctionne en utilisant la commande ci-dessous :

```
ansible --version
```

![ansible_check](https://www.freecodecamp.org/news/content/images/2021/10/ansible_check.png)


Nous allons utiliser la commande ci-dessous pour instruire Ansible de cibler tous les systèmes pour l'hôte d'inventaire localhost, et nous allons exécuter le module ping depuis votre console locale (plutôt que ssh).

```
ansible all -i localhost, --connection=local -m ping
```

Vous devriez obtenir une réponse similaire à ce que vous pouvez voir ci-dessous :

![ansible_ping](https://www.freecodecamp.org/news/content/images/2021/10/ansible_ping.png)

### Comment modifier les hôtes ciblés par Ansible

Nous allons apporter des modifications au fichier des hôtes dans `/etc/ansible/hosts`. C'est le fichier par défaut où Ansible recherche les hôtes (et groupes) définis où les commandes données doivent être exécutées à distance.

```
sudo nano /etc/ansible/hosts
```

Ajoutez les lignes ci-dessous au fichier et sauvegardez les modifications :

```
[local]
localhost
```

Exécutez cette commande avec votre fichier d'inventaire ajusté :

```
ansible all --connection=local -m ping
```

La réponse devrait ressembler à ce que nous avons ci-dessous :

![ansible_pong](https://www.freecodecamp.org/news/content/images/2021/10/ansible_pong.png)

### Comment configurer un serveur distant

Nous déployons notre programme de test Ansible sur notre serveur distant en utilisant une droplet Digital Ocean.

Utilisez la commande ci-dessous pour vous connecter en ssh au serveur :

```
ssh username@IP_Address
```

> Note : nous avons déjà configuré une clé ssh dans notre profil, qui a été sélectionnée lors de la création de la droplet.

![ansible_server](https://www.freecodecamp.org/news/content/images/2021/10/ansible_server.png)

### Comment configurer Ansible pour un serveur distant

Nous allons éditer notre fichier hosts dans /etc/ansible/hosts en utilisant la commande ci-dessous :

```
sudo nano /etc/ansible/hosts
```

Ajoutez les lignes ci-dessous au fichier et sauvegardez les modifications :

```
[remote]
remote_test

[remote:vars]
ansible_host=IP_ADDRESS_OF_VIRTUAL_MACHINE
ansible_user=USERNAME
```

Pour voir si Ansible peut se connecter à votre instance de calcul distante via SSH, tapons la commande suivante :

```
ansible remote -m ping
```

![asnible_result](https://www.freecodecamp.org/news/content/images/2021/10/asnible_result.png)

Nous allons créer un playbook Ansible en utilisant la commande ci-dessous, qui est la manière typique d'indiquer à Ansible quelles commandes exécuter sur le serveur distant et dans quel ordre. Le playbook est écrit en .yml et suit un format strict. 

Dans la documentation officielle [Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html), vous pouvez en apprendre davantage sur les playbooks.

```
nano my-playbook.yml
```

Ajoutez le code suivant, qui indique à Ansible d'installer Docker en plusieurs étapes :

```
---
- name: install docker
hosts: remote
become_method: sudo
become_user: root
vars: #variables locales
docker_packages:
- apt-transport-https
- ca-certificates
- curl
- software-properties-common

tasks:
- name: Mettre à jour les paquets apt
become: true #assurez-vous d'exécuter la tâche avec les privilèges sudo
apt: #utiliser le module apt
update_cache: yes #équivalent de apt-get update

- name: Installer les paquets nécessaires pour Docker
become: true
apt:
name: "{{ docker_packages }}" #utilise notre variable déclarée docker_packages
state: present #indique l'état souhaité du paquet
force_apt_get: yes #force l'utilisation de apt-get

- name: Ajouter la clé GPG officielle de Docker
shell: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

- name: Enregistrer la version actuelle de la release Ubuntu dans une variable
shell: lsb_release -cs
register: ubuntu_version #La sortie est stockée dans cette variable

- name: Définir le bon répertoire Docker
become: true
shell: add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ubuntu_version.stdout }} stable"

- name: Mettre à jour les paquets apt
become: true
apt:
update_cache: yes

- name: Installer Docker
become: true
apt:
name: docker-ce
state: present
force_apt_get: yes

- name: Tester Docker avec l'exemple hello world
become: true
shell: docker run hello-world
register: hello_world_output

- name: Afficher la sortie de l'exemple hello world
debug: #utiliser le module debug
msg: "Sortie du conteneur : {{hello_world_output.stdout}}"
```

Nous pouvons maintenant l'exécuter avec la commande ci-dessous :

```
ansible-playbook my-playbook.yml -l remote
```

Après cela, nous verrons un peu de magie se produire (cela peut prendre un certain temps), et quelque part dans le dernier message de débogage dans notre terminal, nous devrions voir "Hello from Docker !"

## Conclusion

Dans cet article, nous avons examiné en détail Ansible, ses avantages, son fonctionnement et ce qu'il peut faire, son architecture, ses plugins, ses playbooks, son inventaire, et comment configurer et déployer Docker avec Ansible sur un serveur distant.

Merci d'avoir lu !


## Ressources

[Documentation Ansible](https://docs.ansible.com/)
[Configuration des inventaires Ansible](https://www.digitalocean.com/community/tutorials/how-to-set-up-ansible-inventories)
[Installation d'Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)


J'aimerais me connecter avec vous sur [Twitter](https://twitter.com/olanetsoft) | [LinkedIn](https://www.linkedin.com/in/olubisi-idris-ayinde-05727b17a/) | [GitHub](https://github.com/Olanetsoft)