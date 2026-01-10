---
title: Comment créer et se connecter à une machine virtuelle Google Cloud avec SSH
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-02T16:45:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-connect-to-google-cloud-virtual-machine-with-ssh-81a68b8f74dd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uGmqUMo3h7NHNCkP.jpg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: ssh
  slug: ssh
- name: 'tech '
  slug: tech
- name: virtual machine
  slug: virtual-machine
seo_title: Comment créer et se connecter à une machine virtuelle Google Cloud avec
  SSH
seo_desc: 'By Nezar Assawiel

  Google Cloud offers many tools and services. One of these services is creating highly
  customizable virtual machines. If you are not familiar with what a virtual machine
  is, here is a definition from Microsoft:


  A virtual machine is ...'
---

Par Nezar Assawiel

Google Cloud offre de nombreux outils et services. L'un de ces services est la création de machines virtuelles hautement personnalisables. Si vous n'êtes pas familier avec ce qu'est une machine virtuelle, voici une définition de Microsoft :

> Une machine virtuelle est un fichier informatique, généralement appelé une image, qui se comporte comme un ordinateur réel. En d'autres termes, créer un ordinateur dans un ordinateur. Elle s'exécute dans une fenêtre, comme n'importe quel autre programme, offrant à l'utilisateur final la même expérience sur une machine virtuelle que sur le système d'exploitation hôte lui-même. La machine virtuelle est isolée du reste du système, ce qui signifie que le logiciel à l'intérieur d'une machine virtuelle ne peut pas s'échapper ou altérer l'ordinateur lui-même.

Les machines virtuelles sont nécessaires dans de nombreuses situations pour tester des applications sur d'autres systèmes d'exploitation, accéder à des données infectées par des virus ou expérimenter avec d'autres systèmes d'exploitation. Vous pouvez installer des machines virtuelles sur votre ordinateur. Vous pouvez également les créer dans le cloud et simplement vous y connecter.

Dans ce tutoriel, je vais vous guider à travers la création d'une machine virtuelle dans Google Cloud. Nous pouvons nous y connecter avec SSH depuis votre ordinateur.

1. Si vous n'en avez pas déjà un, créez un compte Google Cloud à partir d'[ici](https://cloud.google.com/).

Vous recevrez un crédit de 300 $ à utiliser pendant un an ! C'est plus que suffisant pour apprendre et explorer tout ce que Google Cloud offre.

2. Créez un nouveau projet ou utilisez un projet existant. Vous pouvez créer un nouveau projet appelé **project1**, par exemple, comme dans le gif suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/d8N926cdgrmskacPUiCBS-8j3E26n3wZKJMz)

3. Vous êtes maintenant prêt à créer une machine virtuelle. Allez dans le coin supérieur gauche de votre page d'accueil Google Cloud, cliquez sur l'icône à trois barres  et sélectionnez **Compute Engine -> VM insta_n_**ce et cli**quez sur Cré**er.

Entrez le nom que vous souhaitez dans le champ **Nom** comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qBdgjOVIiVQwafsecV7Gx0LmggEy2LkxHEec)

Gardez la région et la zone par défaut. N'importe quelle région/zone conviendra pour ce tutoriel. Si vous êtes curieux de savoir ce qu'elles signifient, vous pouvez lire la documentation de Google Cloud à leur sujet [ici](https://cloud.google.com/compute/docs/regions-zones/).

Vous pouvez garder le type de machine par défaut ou cliquer sur **Personnaliser** pour sélectionner le nombre de cœurs CPU, la mémoire et les GPU que vous souhaitez pour votre machine virtuelle. Vous verrez le coût changer sur le côté droit !

Pour vos premières expériences avec Google Cloud, vous pouvez être conservateur avec le crédit de 300 $ pour un travail réel. Dans un tel cas, vous pouvez choisir la configuration suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1dxebYaNuExfqZ8pfqh0xVbo2AM5mJVXWn9H)

Ensuite, choisissez un disque de démarrage. Par exemple, vous pouvez choisir **20 Go, SSD, Ubuntu 16.04 LTS** comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/yYCIobWt-a0d4u2CobgwkpqHuxKnrAfSb3Ur)

Ensuite, définissez le **Compte de service** sous **Identité et accès API** sur **Aucun compte de service** comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/GFhEp7kU2Q4w8vIAmGG8mVWsYf5EehrZ-qM4)

Enfin, allez dans l'onglet **Sécurité** sous **Pare-feu**. Vous verrez un champ **Clé SSH** comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/xgqwfK55ZoSZYLrKQ863EgDD42iW37KVo9mu)

C'est ici que vous allez connecter votre ordinateur à la machine virtuelle en utilisant votre clé SSH !

Si vous n'êtes pas familier avec SSH (Secure Shell) et pourquoi vous pourriez vouloir l'utiliser, c'est un protocole réseau qui fournit une communication de données chiffrées entre deux ordinateurs (votre ordinateur et les serveurs de Google, dans ce cas) qui sont connectés via un réseau non sécurisé (Internet ici).

Pour établir une connexion SSH, vous pourriez avoir besoin d'une application capable de le faire, selon votre système d'exploitation. **Suivez le reste de cet article en fonction de votre système d'exploitation (Windows ou Mac/Linux).**

#### **Windows**

Je recommande **PuTTY**. C'est un client SSH open-source et facile à utiliser. Vous pouvez télécharger PuTTY et l'installer à partir d'[ici](https://www.putty.org/).

Après avoir installé PuTTY, ouvrez **PuTTY Key Generator** et cliquez sur **create**. Il générera une clé aléatoire en **vous** déplaçant la souris sur la zone vide. Une fois terminé, vous obtiendrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/j6FJhRY3ijIeF2UOCU6rXR6hlxgXxDoJ-yJE)

Changez le champ **key comment** en quelque chose de reconnaissable et facile à taper, car cela deviendra un nom d'utilisateur plus tard !

Ensuite, sauvegardez les clés publique et privée en cliquant sur les icônes correspondantes montrées dans l'image ci-dessus.

Surlignez tout le champ **Key** du PuTTY Key Generator, et copiez et collez-le dans le champ **key data** dans Google Cloud :

![Image](https://cdn-media-1.freecodecamp.org/images/Wl6IzBYOc7UgC7MtV-A6wbPe1x5aHKeuN38l)

![Image](https://cdn-media-1.freecodecamp.org/images/S9zZ0zEE-wcbiUTyA-NQh5onxHushq3ENrFF)

Cliquez sur **create** et attendez que l'instance de machine virtuelle soit créée.

En attendant, vous pouvez aller dans PuTTY. Allez dans **SSH ->A**uth et parcourez pour trouver le fichier de clé privée que vous avez sauvegardé.

![Image](https://cdn-media-1.freecodecamp.org/images/7MbOpAr9WTaSj-hqcIjvv1xihat-FRPryrUv)

Ensuite, allez dans Google Cloud et copiez l'IP externe de l'instance de machine virtuelle que vous venez de créer comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/OSZMJ8Lqd1SyxuVYZFZcNTef3-ChxBFUSF6y)

Et collez-la dans le champ Host sous **Sessions** dans PuTTY et appuyez sur **Enter** :

![Image](https://cdn-media-1.freecodecamp.org/images/7rKBTabUWQ4bwJPEXMPhhjNxSEAJuEZ0iq4F)

Note : vous pourriez obtenir un message d'erreur. Ignorez-le et cliquez sur **yes**. (Il dit simplement que la clé n'est pas déjà dans le registre. Êtes-vous sûr de vouloir vous connecter ?)

Ensuite, entrez le nom d'utilisateur que vous avez créé lors de la génération de la clé (**key comment** ci-dessus). Boom ! vous êtes dans la machine virtuelle que vous venez de créer.

Vous pouvez installer Python et les API Google sur celle-ci, par exemple, pour commencer à faire de la magie ! N'oubliez pas de l'éteindre dans Google Cloud après avoir terminé pour économiser votre crédit :)

#### **Mac/Linux**

Mac et Linux supportent nativement la connexion SSH. Vous avez juste besoin de générer une paire de clés SSH (clé publique/clé privée) pour vous connecter en toute sécurité à la machine virtuelle.

La clé privée est équivalente à un mot de passe. Ainsi, elle est gardée privée, résidant sur votre ordinateur, et ne doit pas être partagée avec une quelconque entité. La clé publique est partagée avec l'ordinateur ou le serveur auquel vous souhaitez établir la connexion. Pour générer la paire de clés SSH afin de vous connecter en toute sécurité à la machine virtuelle, suivez ces étapes :

Entrez la commande suivante dans le Terminal : `ssh-keygen -t rsa`. Cela lancera le processus de génération de la clé. Vous serez invité à choisir l'emplacement pour stocker la paire de clés SSH. Appuyez sur ENTER pour accepter l'emplacement par défaut comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/R3w3esMPp0ClobIdopPztKXJKS9VBB3tmEmo)

Ensuite, choisissez un mot de passe pour votre connexion à la machine virtuelle ou appuyez sur ENTER si vous ne souhaitez pas utiliser de mot de passe. La clé privée (c'est-à-dire l'identification) et la clé publique seront générées comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/b8KjgTG8JFeY38Lvdp3jdytUxcCQ71UnVo7K)

Maintenant, exécutez la commande suivante : `cat ~/.ssh/id_rsa.pub`. Elle affichera la clé publique dans le terminal comme montré ci-dessous. Surlignez et copiez cette clé :

![Image](https://cdn-media-1.freecodecamp.org/images/fsKg95sN2WmbA7zWAkOc23K3xWxmKuqnOyL2)

et collez-la dans le champ de clé SSH dans Google Cloud et cliquez sur **Créer** :

![Image](https://cdn-media-1.freecodecamp.org/images/REYZEUmTlmkyKvRdSNb6TYjGXp2LEdbhSPoN)

Maintenant, vous pouvez utiliser l'**IP externe** de la machine virtuelle que vous venez de créer :

![Image](https://cdn-media-1.freecodecamp.org/images/FwkOZXHdOi8xv9XMeE9V4J4vo2BjVHgmzO2k)

pour vous y connecter en _ssh_ comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/fN1tFu7LE0uQOrNrSPJCILOjiysC4xyc7U4i)

Vous recevrez un avertissement "The authenticity of hostetc." comme montré dans l'image ci-dessous. C'est normal. Chaque fois que SSH se connecte à un système qu'il n'a jamais vu auparavant, il générera un avertissement comme celui-ci. Répondez **yes** pour vous connecter, et bingo ! Vous êtes dans la machine virtuelle, comme vous pouvez le voir à partir du nom d'hôte **instance-3.** Pour quitter la machine virtuelle, tapez simplement **exit.**

![Image](https://cdn-media-1.freecodecamp.org/images/60u5MB5wOQP9RAsG-KhrQgoJ5NB36YZKBYbG)

N'oubliez pas d'éteindre la machine virtuelle dans Google Cloud après avoir terminé pour économiser ce crédit de 300 $ !

_Publié à l'origine sur [assawiel.com/blog](http://www.assawiel.com/blog) le 23 décembre 2017. Mis à jour : 10 octobre 2018_