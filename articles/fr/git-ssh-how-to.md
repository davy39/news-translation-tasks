---
title: Comment obtenir et configurer vos clés SSH Git et GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T17:46:00.000Z'
originalURL: https://freecodecamp.org/news/git-ssh-how-to
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e49740569d1a4ca3c4e.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: ssh
  slug: ssh
- name: toothbrush
  slug: toothbrush
seo_title: Comment obtenir et configurer vos clés SSH Git et GitHub
seo_desc: 'If you use GitHub without setting up an SSH key, you''re really missing
  out. Just think–all of that time you spent entering your email address and password
  into the console every time you push a commit could have been spent coding.

  Well no more. Here''...'
---

Si vous utilisez GitHub sans configurer de clé SSH, vous passez à côté de quelque chose. Imaginez tout ce temps passé à entrer votre adresse e-mail et votre mot de passe dans la console à chaque fois que vous poussez un commit, temps qui aurait pu être consacré au codage.

Eh bien, c'est terminé. Voici un guide rapide pour générer et configurer une clé SSH avec GitHub afin de ne plus jamais avoir à vous authentifier à l'ancienne.

### Vérifier l'existence d'une clé SSH

Tout d'abord, vérifiez si vous avez déjà généré des clés SSH pour votre machine. Ouvrez un terminal et entrez la commande suivante :

```shell
ls -al ~/.ssh
```

Si vous avez déjà généré des clés SSH, vous devriez voir une sortie similaire à celle-ci :

```sh
-rw-------  1 user_name user_name  1766 Jul  7  2018 id_rsa
-rw-r--r--  1 user_name user_name   414 Jul  7  2018 id_rsa.pub
-rw-------  1 user_name user_name 12892 Feb  5 18:39 known_hosts
```

Si vos clés existent déjà, passez directement à la section **Copier votre clé SSH publique** ci-dessous.

Si vous ne voyez aucune sortie ou si ce répertoire n'existe pas (vous obtenez un message `No such file or directory`), alors exécutez :

```shell
mkdir $HOME/.ssh
```

Puis générez un nouvel ensemble de clés avec :

```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```

Vérifiez maintenant que vos clés existent avec la commande `ls -al ~/.ssh` et assurez-vous que la sortie est similaire à celle listée ci-dessus.

**Note :** Les clés SSH sont toujours générées par paires : une clé publique (`id_rsa.pub`) et une clé privée (`id_rsa`). Il est extrêmement important de **ne jamais révéler votre clé privée** et de **n'utiliser que votre clé publique** pour des choses comme l'authentification GitHub. Vous pouvez en savoir plus sur le fonctionnement des paires de clés SSH/RSA [ici](https://www.freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e/).

### Ajouter votre clé SSH à ssh-agent

`ssh-agent` est un programme qui démarre lorsque vous vous connectez et stocke vos clés privées. Pour qu'il fonctionne correctement, il doit être en cours d'exécution et disposer d'une copie de votre clé privée.

Tout d'abord, assurez-vous que `ssh-agent` est en cours d'exécution avec :

```shell
eval "$(ssh-agent -s)" # pour Mac et Linux
```

ou :

```shell
eval `ssh-agent -s`
ssh-agent -s # pour Windows
```

Ensuite, ajoutez votre clé privée à `ssh-agent` avec :

```shell
ssh-add ~/.ssh/id_rsa
```

### Copier votre clé SSH publique

Ensuite, vous devez copier votre clé SSH publique dans le presse-papiers.

Pour Linux ou Mac, affichez le contenu de votre clé publique dans la console avec :

```shell
cat ~/.ssh/id_rsa.pub # Linux
```

Puis surlignez et copiez la sortie.

Ou pour Windows, exécutez simplement :

```shell
clip < ~/.ssh/id_rsa.pub # Windows
```

### Ajouter votre clé SSH publique à GitHub

Allez sur votre page [paramètres](https://github.com/settings/keys) GitHub et cliquez sur le bouton "New SSH key" :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-14.png)

Donnez ensuite à votre clé un titre reconnaissable et collez votre clé publique (`id_rsa.pub`) :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-15.png)

Enfin, testez votre authentification avec :

```shell
ssh -T git@github.com
```

Si vous avez suivi toutes ces étapes correctement, vous devriez voir ce message :

```sh
Hi your_user_name! You've successfully authenticated, but GitHub does not provide shell access.
```

### Plus d'informations sur SSH :

* [Guide ultime de SSH](https://www.freecodecamp.org/news/the-ultimate-guide-to-ssh-setting-up-ssh-keys/)
* [Une introduction de haut niveau à SSH](https://www.freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e/)