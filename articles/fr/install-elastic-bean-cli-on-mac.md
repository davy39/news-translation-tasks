---
title: Comment installer l'interface de ligne de commande AWS Elastic Beanstalk sur
  un Mac
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2021-01-14T16:34:19.000Z'
originalURL: https://freecodecamp.org/news/install-elastic-bean-cli-on-mac
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ff9a7b475d5f706921cae6e.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: data
  slug: data
- name: deployment
  slug: deployment
seo_title: Comment installer l'interface de ligne de commande AWS Elastic Beanstalk
  sur un Mac
seo_desc: "Elastic Beanstalk is an orchestration service that allows users on the\
  \ AWS platform to deploy web applications easily. It caters to any setup you might\
  \ need to run an application in the cloud. \nOrchestration simply means that it\
  \ automates the workflo..."
---

Elastic Beanstalk est un service d'orchestration qui permet aux utilisateurs de la plateforme AWS de déployer facilement des applications web. Il répond à tous les besoins pour exécuter une application dans le cloud. 

L'orchestration signifie simplement qu'il automatise les processus de flux de travail qui se produisent afin de fournir des ressources en tant que service dans le cloud.

Dans ce tutoriel, nous allons passer en revue les étapes simples pour installer Elastic Beanstalk localement. L'installer localement signifie que nous pourrons interagir directement avec AWS depuis le terminal et pousser nos applications déployées vers le cloud via les commandes fournies par EB.

## Avantages d'Elastic Beanstalk

Elastic Beanstalk permet à vos données de persister après la terminaison de l'instance de calcul cloud élastique. Les données stockées sur le volume restent accessibles.

De plus, il vous aide à éviter les défaillances de composants en offrant une haute disponibilité et durabilité. 

## Comment installer l'interface de ligne de commande Elastic Beanstalk

L'interface de ligne de commande Elastic Beanstalk est une interface en ligne de commande qui permet aux utilisateurs de créer, configurer et gérer des processus sur Elastic Beanstalk.

Pour installer EB dans notre environnement local, nous devons consulter le projet open-source [aws-elastic-beanstalk-cli-setup](https://github.com/aws/aws-elastic-beanstalk-cli-setup). Nous y trouverons des guides d'installation pour nous aider dans le processus.

### Étape 1 :

Clonez le dépôt dans notre environnement local. Si vous n'avez pas de compte Github, vous pouvez vous inscrire [ici](https://www.freecodecamp.org/news/p/8ffef46d-0fe6-4768-8ccd-f8743b0008d1/github.com).

```github
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
```

### Étape 2 :

Dans cette section, nous devons télécharger zlib et le configurer. Zlib est une bibliothèque utilisée pour la compression et la décompression. EB utilise cette fonctionnalité lorsqu'il doit compresser et décompresser des données (chaînes de caractères, contenu structuré en mémoire ou fichiers).

```brew
brew install zlib openssl readline
CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib"
```

### Étape 3 :

Une fois l'installation terminée, nous allons exporter et configurer les chemins pour les variables d'environnement de zlib. Exécutez les commandes suivantes dans la ligne de commande :

```
$ export LDFLAGS=$LDFLAGS:-L/usr/local/opt/zlib/lib
$ export CPPFLAGS=$CPPFLAGS:-I/usr/local/opt/zlib/include
$ export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/usr/local/opt/zlib/lib/pkgconfig
```

Pour vérifier si les chemins ont été correctement définis, exécutez cette commande :

```
$ echo $LDFLAGS $CPPFLAGS $PKG_CONFIG_PATH
```

### Étape 4 :

De retour dans notre terminal où nous avons clonné le dépôt, nous devons exécuter l'installeur groupé avec le code ci-dessous :

```
$ ./aws-elastic-beanstalk-cli-setup/scripts/bundled_installer
```

Une fois le processus terminé, vous verrez une sortie qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.33.22.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.33.34.png)

### Étape 5 :

Pour compléter le processus d'installation, nous devons ajouter `eb` et `python` à notre chemin d'environnement. Nous pouvons faire cela en exécutant ce code dans le terminal :

```
$ echo 'export PATH="/Users/user/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
$ echo 'export PATH=/Users/user/.pyenv/versions/3.7.2/bin:$PATH' >> /Users/user/.bash_profile && source /Users/user/.bash_profile
```

Une fois que nous avons terminé l'ajout des chemins, nous pouvons maintenant essayer d'initialiser un Elastic Beanstalk et voir si nous obtenons une liste de régions sélectionnées. Exécutez ceci dans le terminal :

```
$ eb init
```

Et vous devriez voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.44.03.png)

Voilà ! Nous avons une liste de régions parmi lesquelles nous pouvons choisir et nous pouvons ajouter nos identifiants depuis un bucket S3 sur AWS. Nous pouvons également exécuter d'autres commandes EB telles que `eb create`, `eb deploy`, et bien plus encore.

### Références

* [Guide du développeur AWS Elastic Beanstalk](https://docs.amazonaws.cn/en_us/elasticbeanstalk/latest/dg/awseb-dg.pdf)
* [Compression avec zlib](https://www.zlib.net/)