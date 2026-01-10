---
title: Tutoriel Serveur Linux – Comment se connecter, communiquer et transférer des
  fichiers
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-02-28T23:55:22.000Z'
originalURL: https://freecodecamp.org/news/linux-server-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Server-Commands
seo_title: Tutoriel Serveur Linux – Comment se connecter, communiquer et transférer
  des fichiers
---

Brief-2.png
tags:
- name: Linux
  slug: linux
- name: serveurs
  slug: servers
seo_title: null
seo_desc: "Saviez-vous que 96 % des 1 million de meilleurs serveurs web fonctionnent sous Linux ?\
  \ \nOui. Vous avez bien entendu. Savoir travailler avec des serveurs Linux est donc une excellente\
  \ compétence à avoir.\nDans cet article, vous apprendrez à vous connecter à un serveur Linux\
  \ en utilisant SSH, comment ..."
---

Saviez-vous que [96 % des 1 million de meilleurs serveurs web](https://www.zdnet.com/home-and-office/networking/can-the-internet-exist-without-linux/) fonctionnent sous Linux ? 

Oui. Vous avez bien entendu. Savoir travailler avec des serveurs Linux est donc une excellente compétence à avoir.

Dans cet article, vous apprendrez à vous connecter à un serveur Linux en utilisant SSH, comment communiquer avec d'autres utilisateurs sur le serveur, et vous verrez un mécanisme pratique de transfert de fichiers. 

Une petite note avant de plonger dans le vif du sujet : l'adresse IP que j'ai donnée dans les exemples de commandes et celle des captures d'écran varieront. La raison est que je n'ai pas de serveur pour démontrer tout cela, alors j'ai transformé mon ordinateur portable en serveur. Ainsi, toutes mes captures d'écran d'exemple afficheront mes adresses IP locales commençant par `192.168...`.

## Comment se connecter à un serveur sous Linux

J'adore développer des logiciels, mais je n'aime vraiment pas DevOps et les déploiements. Quand j'ai un travail lié à DevOps, je le confie au spécialiste de mon équipe et je reste à l'écart. 

La raison est mon manque d'expérience dans la gestion des serveurs. Mais parfois, lorsque mes collègues ne sont pas disponibles, je suis obligé de faire des déploiements. 

Ainsi, la première étape pour un déploiement (manuel) est de se connecter au serveur. Pour se connecter, vous devez connaître l'adresse IP et le mot de passe du serveur.

Par-dessus tout, vous devez avoir le client SSH installé sur votre machine. Celui-ci est préinstallé sur presque toutes les distributions Linux.

Si vous ne l'avez pas installé, vous pouvez l'installer en exécutant la commande suivante dans le terminal :

```bash
sudo apt install openssh-client
```

Pour accéder au serveur via SSH, le serveur doit avoir `SSH Server` installé et le service en cours d'exécution. Cela sera préinstallé sur presque tous les serveurs Linux.

Connectons-nous au serveur maintenant.

Vous avez besoin des éléments suivants pour vous connecter au serveur :

1. Adresse IP de la machine serveur
2. Nom d'utilisateur du serveur
3. Le mot de passe de l'utilisateur

```bash
ssh user@<ipaddress>
```

Voici un exemple de commande :

```
ssh ubuntu@45.244.96.73
```

La commande ci-dessus demandera le mot de passe. Si vous entrez le mot de passe, elle se connectera au serveur.

![Image](https://lh3.googleusercontent.com/HgByhOjGdN5KCqnk-0RXRAqvrHXdttXbpxjatpEOm6f7k7_1VAEUZKu7xVZ6CrLqpeG6vAu2Lj3zj7sSFpUPF-7TEFRJ3FIeMOXAQyMyPXK2DWYSf2zPRM9onI1U-ieT9zRNee8blRaysH4LgE3ctFc)
_Exemple de sortie de connexion à un serveur Linux à l'aide de la commande SSH._

Alternativement, vous pouvez vous connecter sans invitation en ajoutant l'option `-p` avec la commande `sshpass` préfixée à la commande `ssh`. Vous devez avoir `sshpass` installé pour essayer cette méthode. 

La syntaxe ressemble à ceci :

```bash
sshpass -p <password> ssh user@<ipadrress>
```

Et voici un exemple rapide :

```bash
sshpass -p password ssh user@45.244.96.73
```

Ce n'est pas la méthode recommandée. Les arguments de la ligne de commande sont visibles par tous les utilisateurs (par exemple, `ps -ef | grep sshpass`). `sshpass` tente de masquer l'argument, mais il reste une fenêtre pendant laquelle **tous les utilisateurs** peuvent voir votre mot de passe passé en argument. 

Il existe également une commande sous Linux appelée `history` qui affiche vos commandes passées. Tout utilisateur ayant accès à votre machine peut exécuter la commande `history` et trouver vos identifiants de connexion au serveur. Mais si vous avez entré le mot de passe dans une invite, il ne sera pas affiché aux utilisateurs dans la commande `history`. 

Voici la sortie de la commande `history` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-265.png)
_La commande `history` affiche les commandes passées_

## Comment se connecter à un utilisateur particulier dans le terminal Linux

Sous Linux, nous pouvons nous connecter à différents utilisateurs en utilisant deux approches différentes :

1. ssh
2. login

### Comment se connecter avec SSH

Comme déjà discuté avec la commande SSH, nous pouvons nous connecter à un autre utilisateur en utilisant la même syntaxe.

```bash
ssh <user>@<ipaddress>
ssh root@45.244.96.73
```

### Comment se connecter avec la commande `login`

Vous pouvez utiliser la commande `login` pour changer d'utilisateur à l'intérieur du serveur.

Supposons que vous vous êtes connecté en tant qu'utilisateur `ubuntu` sur le serveur `45.244.96.73`. Plus tard, vous avez trouvé que vous souhaitez passer à l'utilisateur `ak` pour effectuer certaines opérations d'administration. Dans un tel cas, vous pouvez rapidement changer d'utilisateur en utilisant la commande `login`.

La syntaxe de la commande `login` est :

```bash
sudo login <username>
```

Et voici un exemple pour passer à l'utilisateur root :

```
sudo login ak
```

La commande ci-dessus demandera le mot de passe, similaire à la connexion via SSH.

![Image](https://lh6.googleusercontent.com/NdnozHMxq8yjUemRfgXbLseAJJOtdjFuogF80P3sXiHA9WsH-kaM7pfsqq7u9tMrCgB1kIU8up5_stEPbov2w7SEI8Tx-0jWfSDwGn4xMX0U0CZr_cG3GymiYQTQ3FIZNLGCRZDLzOwvyrvy1cWGq9I)
_Exemple de sortie pour se connecter avec un utilisateur local_

Hourra, nous nous sommes connectés avec succès à un autre utilisateur. Maintenant, explorons comment communiquer avec ces sessions.

Une petite note avant de passer à la section communication. Si vous souhaitez vous déconnecter de l'utilisateur connecté, vous pouvez simplement exécuter la commande `logout`.

## Comment communiquer entre les sessions sous Linux

Saviez-vous que vous pouvez utiliser votre terminal Linux comme une interface de chat ?

Eh bien, oui – vous pouvez. Si vous et vos collègues êtes connectés en tant qu'utilisateurs à part entière au même serveur en utilisant SSH, alors vous pouvez tous communiquer via le terminal.

Comme pour toutes ces fonctionnalités, il y a quelques prérequis à respecter.

Tout d'abord, assurez-vous que l'accès aux messages est activé dans le système du destinataire. Pour vérifier cela, tapez la commande suivante dans le terminal :

```bash
mesg
```

![Image](https://lh3.googleusercontent.com/GhfC5V8FTtbZMrFpMef_tdVanRwDZv7qksWLAtSp2Oi6LixFWOLUme82szxja60ho6h04jHi5cUjkFTAgKepTKw3KsRjr7Yx1yt1bJ_rvCWr1CFDqX9L-rfASEuSHWD4Emx7BdBKAyLqGcl3omuRsYg)
_Commande terminal pour vérifier si l'accès aux messages est activé_

La réponse sera soit oui, soit non.

`is y` – Accès aux messages activé

`is n` – Accès aux messages désactivé

Pour activer ou désactiver cette fonctionnalité, vous devez passer le symbole avec la commande `mesg`.

```bash
mesg y      # Activer l'accès aux messages
mesg n      # Désactiver l'accès aux messages
```

Essayons de communiquer avec les autres.

Il existe deux commandes disponibles pour communiquer :

1. `write`
2. `wall`

Les commandes `write` et `wall` utilisent un mécanisme assez simple. Les deux commandes prennent un message d'une session et le livrent à une ou plusieurs autres sessions.

### Comment utiliser la commande `write`

Vous pouvez utiliser la commande `write` pour envoyer un message à un seul utilisateur (Message Direct).

```bash
write <username>
```

```
write ak
```

Après avoir entré cette commande, elle invite à saisir le message à envoyer. Nous pouvons envoyer n'importe quel nombre de messages en utilisant la commande `write`.

Voici un exemple montrant la communication entre les utilisateurs `ak` et `gogosoon` :

![Image](https://lh5.googleusercontent.com/j5imQ3k0CpoU80sgoesN-0-C2YE94Q130NeWqCaWx9jU42jEhKKR31Izy1H5k6WSb5TRd5pVUfa4CPg0GUeY_qnIzcoapWEK8D6W42JqMIVrFe7vlBqVWRvbmqcTvYIKvRw4nUUTG59zlZ_MRcP3s7o)
_Exemple de sortie de l'envoi d'un message à l'utilisateur_

![Image](https://lh6.googleusercontent.com/DXtSsy3TbbeHr8oX3bB8mSxPxkXy6zsVjJ9WwlI8HfXJJVi6RL8BgTHaSUivl1rZzVpD9aEq6LPn9Gfq8_8FHTzwXE2FGtUz4TTO46b5GU8NXYCu-8gY-l4k0V328Sj0CHe6OMuay7SxdGlkf5LTLdg)
_Exemple de sortie du message reçu en utilisant la commande write_

Désactivons la messagerie pour l'utilisateur `ak` et essayons d'envoyer un message depuis l'utilisateur `gogosoon`.

```bash
mesg n
```

![Image](https://lh3.googleusercontent.com/Nyt9Ror-xWpTtnGd77lkjXM_cb7hUcj1fE3fbJEk-kEc-EPsUxQCwhpuo_br1ba44XEdnGa9WzDQkE2OcY4lZW9R7LFCob4kNVYBPmm65GNhpfK-UQ198i73dWynZ4pfeX4kzOB3oWwE0-HzLeNA9Ss)
_Désactiver la messagerie pour l'utilisateur `ak`_

![Image](https://lh4.googleusercontent.com/QY3yKIRAMJpxHOlaY3jJfyuQI5zLDyB8iecBIkAIzeuAHobYU1q6IiWDyN9sVu1Xikl5psyLMtpy7TFYAxohNbxINlQFS-5zE7Y18TSbYlVR6EhvCDWCBfWR3XYVL2CheGvny3CsTLCkiq3_f9F8hjY)
_Essayer d'envoyer un message à l'utilisateur `ak` depuis l'utilisateur `gogosoon`_

### Comment utiliser la commande `wall`

Vous pouvez utiliser la commande `wall` pour écrire des messages à tous les utilisateurs connectés. Cette commande affichera le message ou le contenu d'un fichier à tous les utilisateurs connectés. En gros, elle diffusera le message à toutes les sessions.

```bash
wall <message>
```

![Image](https://lh3.googleusercontent.com/9emd9tiz1MkQHQDYaCs_2Y8Cc87T1Yt3GLKsYPGZ9IYEZGecDE95zaLZJdpNik5szyKB1_Y-d60WsOIlZPVGy1YrNWmfb2tbCQltO3e6fxxXX1npqGnmaVnuQvqOsaz18h3b8Q25GUpHnzVtaBiWQwI)
_Commande exemple pour envoyer un message à tous les utilisateurs connectés_

![Image](https://lh5.googleusercontent.com/ey4zUh9Rv_OEZcn3LUn4ksRg_eMekUUNyOvvny7_E0PGvbODYjkYGcZ7fsBoZ7W3DwZQOshbCJlhm7AQ6_ty5rCItysHSAU_ceGvLmuUFimchZe8DQRtx8R9MK_CDfmOz1an14Qd6ScB3YHcYVrMY5Q)
_Exemple de sortie du message reçu de l'utilisateur `gogosoon`_

Ici, nous pouvons voir le message dans l'utilisateur `ak`. De même, il affiche le message à chaque utilisateur connecté.

## Comment transférer des fichiers vers/depuis le serveur en utilisant le terminal Linux

Je crois que la plupart des gens recommanderaient d'utiliser FTP pour transférer des fichiers vers et depuis le serveur. FTP offre plus de contrôle sur les fichiers, comme la possibilité de renommer, supprimer, déplacer et modifier des fichiers depuis l'ordinateur distant. 

Mais FTP n'offre pas de protection contre quiconque pourrait essayer de voir vos identifiants réseau. 

Nous pouvons faire cela en utilisant un terminal Linux – et croyez-moi, c'est super simple.

Vous pouvez transférer des fichiers en utilisant la commande `scp`. 

**SCP** signifie Secure Copy Protocol. Cette commande permet à l'utilisateur de partager des fichiers de manière sécurisée. Contrairement à FTP, SCP est très sécurisé. Il utilise un shell sécurisé pour chiffrer à la fois vos données et vos identifiants. SCP ne fournit pas de facilités pour contrôler les fichiers. 

Puisque cette commande suit le protocole de chiffrement de bout en bout, elle utilise le chiffrement sur une **connexion SSH**. Cela protégera les fichiers contre les attaques suspectes. 

Le transfert de fichiers via SCP sera lent par rapport à FTP. Mais c'est une meilleure alternative à FTP si vous avez besoin d'un mouvement ponctuel de fichiers. 

La syntaxe de la commande SCP ressemble à ceci :

```bash
scp [OPTIONS] <user>@<src_host>:<file_src_path> <user>@<dest_host>:<file_dest_path>
```

En utilisant la commande SCP, nous pouvons effectuer les opérations suivantes :

1. Copier le fichier de notre machine vers la machine serveur
2. Copier le fichier de la machine serveur vers notre machine
3. Copier le fichier d'un serveur à un autre serveur

Examinons chacune de ces opérations plus en détail maintenant.

### Comment copier le fichier de la machine cliente vers la machine serveur

Lors de la copie de fichiers de la machine locale vers la machine serveur, vous devez activer SSH sur le serveur. Cela est dû au fait que SCP utilise SSH pour établir la connexion entre les machines cliente et serveur.

```
scp <filepath> user@hostname:<filepath>
```

```bash
scp sample.txt ak@45.244.96.73:/home/ak/
```

![Image](https://lh6.googleusercontent.com/xRevVCaYkcjReW_KL5z3AR4URLrtfj7ddjb5syy9XYAM77ndXOwPsq5aqGpEY3Y6Py3ro2kYaklDYOjqSkf4t_eFDwsTvlHn7-EyI8GW1UXKSMtb17kThqdrgDZTLpjIrr2Q9b82EJqJbADsm5IAmRY)
_Exemple de sortie pour transférer des fichiers de la machine locale vers le serveur_

![Image](https://lh5.googleusercontent.com/R1Seq1__aIY64McpCrOxq2EHDzIUbkH9Yp_hjaGdTBjMx_Ig1Dl4JImNmeUJ83rKQnXbgaMOeqkgNwG7NAFEF7uHFPFzsmmGcrxXeAKYEbZSptDmPY5DI-YN7shaLmESQNwan8rwaVXI--TffliTR-M)
_Statut du téléchargement du fichier_

![Image](https://lh5.googleusercontent.com/Qn41hy9eTLlH8qHHdBNDHDP-svOKwuyEJI_1xcpQd3dMBepILQA6hu_yEA-fj-Yaguq6hoqYOqR5GunCfmnsAosKGosovwjKdXAFuLODjUXV4GwtLPUDQy9a69oLP4pIUkcoKnj2doetcfDQUwBiNDg)
_`Sample.txt` a été transféré vers le serveur_

Les captures d'écran ci-dessus montrent que le fichier a été copié vers le serveur.

### Comment copier le fichier de la machine serveur vers la machine cliente

Voyons comment transférer le fichier du serveur vers notre machine locale :

```bash
scp server_username@<server_host>:<filepath> <local_path>
```

Cette commande copiera le fichier `server_file.txt` de la machine serveur vers la machine locale dans le répertoire de test.

```bash
scp ak@45.244.96.73:/home/ak/server_file.txt /home/gogosoon/test
```

Si vous laissez le local_path vide, le fichier sera copié dans le répertoire personnel.

![Image](https://lh3.googleusercontent.com/oDuUIGXLgFnUYwZY1qrym9lsy8rvLI-cktIOMA-0eVASMw3c1NofUApRERSH8jAEt8Jqv8KTML7xHT_oQihD6cECczYyeTI0MyVlrixpR0CJhl6oMbmWqGuvuyMa9yXV2esY0XovawvN47Y5xV9_iG4)
_Créer un fichier sur le serveur à transférer_

![Image](https://lh4.googleusercontent.com/8UQdbKsHlapYP3pIKrlYM5_qAdVGBxN5I_cr_u3ugIyiHuzTXjHSjWsGMKESFascLc8KvqH_aAglXfB2qSiW2-90t3ceWVOQ-PYs-tkym20dakTq7cilKHe0_CabuBr8ufueVqmam1CnfTEQKL7dSDo)
_Exemple de sortie du transfert de fichier du serveur vers la machine locale_

### Comment copier le fichier d'un serveur à un autre serveur

Supposons que vous prenez une sauvegarde d'un fichier depuis un serveur. Vous ne voulez pas que ce fichier soit stocké sur votre machine pour des raisons de sécurité. Mais vous voulez transférer ce fichier vers un autre serveur.

Copier des fichiers d'un serveur à un autre serveur est également possible avec la commande `scp` :

```bash
scp <src_user>@<src_host>:<src_path> <dest_user>@<dest_host>.com:/<dest_path>
```

```bash
scp ak@45.244.96.73:/home/ak/script.sh gogosoon@45.244.196.173:/home/gogosoon/
```

## Conclusion

Très bien, nous sommes arrivés à la fin de ce tutoriel. J'espère que vous avez tous apprécié apprendre ces commandes utiles. 

Si vous êtes ingénieur DevOps, développeur Linux ou si vous apprenez Linux, ces commandes seront très utiles. Si vous avez apprécié ce guide, veuillez le partager avec vos collègues/amis qui travaillent davantage sur les serveurs. 

Pour en savoir plus sur Linux, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_server_guide) et suivez-moi sur les réseaux sociaux.