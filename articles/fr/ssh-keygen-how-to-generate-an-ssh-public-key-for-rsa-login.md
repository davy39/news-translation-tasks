---
title: Tutoriel SSH Keygen – Comment générer une clé publique SSH pour la connexion
  RSA
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2022-08-30T15:51:22.000Z'
originalURL: https://freecodecamp.org/news/ssh-keygen-how-to-generate-an-ssh-public-key-for-rsa-login
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/article-banner.jpg
tags:
- name: Cryptography
  slug: cryptography
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: ssh
  slug: ssh
seo_title: Tutoriel SSH Keygen – Comment générer une clé publique SSH pour la connexion
  RSA
seo_desc: 'Cryptography uses encryption and decryption to conceal messages. This introduces
  secrecy in information security.

  The purpose of cryptography is to ensure secure communication between two people
  or devices who are connecting through insecure channels...'
---

La cryptographie utilise le chiffrement et le déchiffrement pour dissimuler des messages. Cela introduit la confidentialité dans la sécurité de l'information.

Le but de la cryptographie est d'assurer une communication sécurisée entre deux personnes ou appareils qui se connectent via des canaux non sécurisés.

L'expéditeur utilise souvent une clé de chiffrement pour verrouiller le message, tandis que le destinataire utilise une clé de déchiffrement pour déverrouiller le message.

En général, la cryptographie emploie deux stratégies :

1. **Cryptographie à clé symétrique (clé privée) :** Avec cette technique, les clés de chiffrement et de déchiffrement sont connues à la fois de l'expéditeur et du destinataire. Certains exemples d'algorithmes utilisant cette technique incluent le chiffrement One Time Pad, le chiffrement Vernam, Playfair, le chiffrement Row column, et le Standard de Chiffrement des Données (DES).

2. **Cryptographie à clé asymétrique (clé publique) :** Avec cette technique, chaque personne possède deux clés : la clé Privée (secrète et accessible uniquement au créateur) et les clés Publiques (librement disponibles pour quiconque). L'expéditeur et le destinataire utilisent des clés différentes pour le chiffrement et le déchiffrement. Certains exemples d'algorithmes utilisant cette technique incluent l'algorithme Rivest–Shamir–Adleman (RSA), l'échange de clés Diffie-Hellman (DHE), et l'algorithme de signature numérique (DSA).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Cryptography--2-.png align="left")

*Le modèle de chiffrement pour la transmission sécurisée de données*

Les ingénieurs logiciels doivent généralement s'authentifier auprès de serveurs ou d'autres services comme GitHub pour le contrôle de version.

Au lieu d'utiliser l'authentification par mot de passe, ils peuvent utiliser l'authentification par clé publique pour générer et stocker une paire de clés cryptographiques sur leur ordinateur. Ensuite, ils peuvent configurer le serveur fonctionnant sur un autre ordinateur pour reconnaître et accepter ces clés.

C'est le flux de la technique de cryptographie à clé asymétrique dont nous avons discuté précédemment et c'est un processus d'authentification plus sécurisé.

Dans ce tutoriel, vous apprendrez comment tout cela fonctionne, ce que signifie SSH, et comment générer des clés SSH avec un algorithme RSA en utilisant SSH keygen.

## Prérequis

* Un ordinateur fonctionnel sous n'importe quel système d'exploitation.

* Des connaissances de base pour naviguer dans la ligne de commande.

* Un sourire sur votre visage :)

## Brève introduction à SSH (**S**ecure **Sh**ell Protocol)

L'authentification par clé publique utilisant SSH est une approche plus sécurisée pour se connecter aux services que les mots de passe. Comprendre SSH est plus facile une fois que vous comprenez comment fonctionne la cryptographie à partir de l'introduction ci-dessus.

Voici une définition de base utile :

> "Le **S**ecure **Sh**ell Protocol est un **protocole de réseau cryptographique** pour exploiter des services réseau de manière sécurisée **sur un réseau non sécurisé**." ([Source](https://en.wikipedia.org/wiki/Secure_Shell))

SSH est utilisé entre un client et un serveur, tous deux fonctionnant sur le protocole SSH, pour se connecter à distance au serveur et accéder à certaines ressources via la ligne de commande.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-197.png align="left")

*Source : SSH Academy*

Il existe une version open-source du protocole SSH (version 2) avec une suite d'outils appelée [OpenSSH](https://www.openssh.com) (également connue sous le nom de OpenBSD Secure Shell). Ce projet inclut les outils suivants :

* Opérations à distance : [ssh](https://man.openbsd.org/ssh.1), [scp](https://man.openbsd.org/scp.1), et [sftp](https://man.openbsd.org/sftp.1).

* Génération de clés : [ssh-add](https://man.openbsd.org/ssh-add.1), [ssh-keysign](https://man.openbsd.org/ssh-keysign.8), [ssh-keyscan](https://man.openbsd.org/ssh-keyscan.1), et [**ssh-keygen**](https://man.openbsd.org/ssh-keygen.1).

* Côté service : [sshd](https://man.openbsd.org/sshd.8), [sftp-server](https://man.openbsd.org/sftp-server.8), et [ssh-agent](https://man.openbsd.org/ssh-agent.1).

## Comment générer une clé publique SSH pour la connexion RSA

Notre objectif est d'utiliser ssh-keygen pour générer une clé publique SSH en utilisant l'algorithme RSA. Cela créera une paire de clés contenant une clé privée (enregistrée sur votre ordinateur local) et une clé publique (téléversée sur le service de votre choix).

Maintenant, pour continuer, suivez les étapes ci-dessous pour y parvenir :

1. Installez OpenSSH si vous ne l'avez pas déjà installé en utilisant la commande suivante :

```python
// pour mac

brew install openssh

// pour linux

sudo apt install openssh-client && sudo apt install openssh-server
```

2. Créez une paire de clés privée/publique avec un algorithme RSA (chiffrement 2046 bits par défaut), en utilisant la commande :

```python
ssh-keygen -t rsa
```

3. Ou, si vous voulez créer avec un algorithme RSA avec un chiffrement 4096 bits, utilisez la commande :

```python
ssh-keygen -t rsa -b 4096
```

4. Entrez un emplacement de fichier pour enregistrer la clé (par défaut, elle sera enregistrée dans le répertoire de votre utilisateur (par exemple, `(/Users/bolajiayodeji/.ssh/id_rsa)` ).

5. Entrez une phrase secrète pour une sécurité supplémentaire de votre clé privée. En général, une bonne phrase secrète doit comporter au moins 15 caractères (dont au moins une lettre majuscule, des lettres minuscules, des chiffres numériques et des caractères spéciaux) et doit être difficile à deviner. Vous pouvez utiliser l'un de ces générateurs de mots de passe en ligne ou utiliser hexdump pour générer une paraphrase facilement comme suit :

```python
hexdump -vn16 -e'4/4 "%08X" 1 "\n"' /dev/urandom
```

6. Une fois que vous avez créé votre mot de passe avec succès, votre clé privée sera enregistrée dans `/<votre_répertoire_choisi>/.ssh/id_rsa` et votre clé publique sera enregistrée dans `/<votre_répertoire_choisi>/.ssh/id_rsa.pub`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-1.18.15-PM.png align="left")

Maintenant, vous pouvez copier la clé créée dans le fichier authorized_keys du serveur auquel vous souhaitez vous connecter en utilisant ssh-copy-id (cet outil fait partie d'OpenSSH) comme suit :

```python
ssh-copy-id username@remote_host
```

Alternativement, vous pourriez vouloir ajouter votre clé privée SSH à l'agent ssh et stocker votre phrase secrète dans le trousseau. Vous pouvez ensuite ajouter la clé SHH au compte de votre serveur via une interface utilisateur de tableau de bord ou autre (par exemple, en utilisant des outils comme Git ou GitHub).

## Conclusion

Bien qu'un mot de passe fort aide à prévenir les attaques par force brute, l'authentification par clé publique offre un processus d'authentification beaucoup plus sécurisé en utilisant la cryptographie.

J'espère que vous avez trouvé cet article utile. De plus, vous pouvez consulter la [page manuelle de ssh-keygen](https://man.openbsd.org/ssh-keygen.1) et les ressources suivantes pour approfondir vos connaissances :

* [Se connecter à GitHub avec SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

* [Commencer avec OpenSSH pour Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

Santé ! 💙