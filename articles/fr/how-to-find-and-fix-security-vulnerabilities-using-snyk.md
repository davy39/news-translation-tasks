---
title: Comment trouver et corriger les vulnérabilités de sécurité en utilisant Snyk
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-05-20T18:08:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-and-fix-security-vulnerabilities-using-snyk
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/snyk-1.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: vulnerabilities
  slug: vulnerabilities
seo_title: Comment trouver et corriger les vulnérabilités de sécurité en utilisant
  Snyk
seo_desc: "In this article, we will be covering an important topic, Security in Python.\
  \ \nWe often download and install packages from PyPi but we're not sure about the\
  \ vulnerabilities that might come with them. \nSo, in this tutorial, we will learn\
  \ about an aweso..."
---

Dans cet article, nous allons aborder un sujet important, **la sécurité en Python**. 

Nous téléchargeons et installons souvent des packages depuis PyPi, mais nous ne sommes pas sûrs des vulnérabilités qui pourraient les accompagner. 

Dans ce tutoriel, nous allons donc apprendre à utiliser un outil génial appelé Snyk qui nous aide à trouver les vulnérabilités dans notre code et à les corriger. Alors, commençons !

## Qu'est-ce que Snyk ?

Snyk (prononcé _sneak_) est une plateforme de sécurité pour les développeurs permettant de sécuriser le code, les dépendances, les conteneurs et l'infrastructure en tant que code. Il analyse votre code, le lit et vous indique si vous avez des vulnérabilités dans votre code. 

Maintenant, il ne vérifie pas seulement votre code – il peut également vérifier les dépendances installées, votre conteneur Docker, votre Infrastructure as Code, et quelques autres choses aussi. 

Snyk est compatible avec de nombreux langages et dispose de plugins pris en charge par différents IDE. Donc, c'est essentiellement le Grammarly pour votre code.

## Comment commencer avec Snyk

Pour commencer, vous devez créer un compte sur Snyk. Rendez-vous sur [https://snyk.io/](https://snyk.io/) et inscrivez-vous pour un compte gratuit. Je vous recommande de vous connecter via GitHub. 

Une fois inscrit, vous pouvez vous connecter à votre compte. Après vous être connecté, vous pourrez voir un tableau de bord similaire :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-180046_rsvwrs)

Maintenant, vous pouvez vous rendre sur [ce lien](https://docs.snyk.io/snyk-cli/install-the-snyk-cli) et suivre les instructions pour télécharger le CLI de Snyk. Il existe diverses méthodes pour télécharger le CLI de Snyk. Vous pouvez choisir l'une d'entre elles.

Si vous êtes ici, je suppose que vous avez déjà installé le CLI de Snyk en utilisant l'une des méthodes disponibles. Maintenant, ce que nous devons faire est de nous authentifier avec le CLI de Snyk. 

Pour ce faire, exécutez la commande suivante dans le terminal :

```bash
snyk auth
```

Lorsque vous exécutez la commande, une page d'authentification s'ouvrira dans votre navigateur par défaut comme ci-dessous :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-180741_oz9lqe)

Il vous suffit de cliquer sur le bouton **Authentifier** et d'attendre que la page affiche un message de succès. Une fois que vous voyez le message, vous pouvez retourner à votre terminal où vous trouverez une sortie similaire à celle ci-dessous :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-181139_bte2bh)

Maintenant, le CLI Synk a été connecté à votre compte.

## Comment trouver des vulnérabilités dans une application de démonstration

À des fins de démonstration, nous allons utiliser une application web appelée PyGoat écrite en Django. J'ai ajouté beaucoup de vulnérabilités à l'application intentionnellement, afin que nous puissions avoir une bonne démonstration de Snyk en l'utilisant.

Voici le lien vers le dépôt GitHub : [https://github.com/purpledobie/pygoat](https://github.com/purpledobie/pygoat). Ouvrez le lien du dépôt, cliquez sur Fork, puis clonez le dépôt forké sur votre machine locale. 

Lorsque vous parcourez le dépôt, vous trouverez un Dockerfile, un fichier Infrastructure as Code, ainsi que des fichiers Python standard. Nous passerons en revue les fichiers plus tard. Vous pouvez installer les dépendances Python à partir du fichier **requirements.txt**. 

```bash
pip install -r requirements.txt
```

### Plugins Snyk

Snyk dispose de plugins disponibles pour différents IDE tels qu'Eclipse, VS Code et Jetbrains (PyCharm, IntelliJ, etc.). Comme je suis sur VS Code, j'ai installé l'extension Snyk sur mon IDE. Vous pouvez faire de même pour votre IDE.

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-182549_uco2bj)

Une fois que vous avez installé l'extension, vous devrez peut-être vous authentifier à nouveau. Une fois authentifié, le plugin commencera à analyser le code automatiquement. Après quelques secondes, il affichera les résultats similaires à ceux ci-dessous :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-183208_yixnwm)

Vous pouvez voir qu'il y a 18 vulnérabilités de sécurité du code et 2 problèmes de qualité du code dans le code. 

Chaque problème ou vulnérabilité a une icône à côté. Il peut s'agir de **C**, **H**, **M** et **L** signifiant respectivement **Critique**, **Élevé**, **Moyen** et **Faible**. Vous pouvez cliquer sur l'un d'eux pour en savoir plus et il suggérera même des corrections pour le problème ou la vulnérabilité.

### Commandes CLI de Snyk

Nous avons déjà exécuté une commande CLI Synk – **`snyk auth`** – pour nous authentifier avec Snyk. Maintenant, regardons quelques autres commandes importantes.

#### **1. Commande `snyk test`**

Cette commande analysera le code et vous montrera les vulnérabilités. Exécutons cela et voyons ce que nous obtenons :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-185708_rhnx7f)

Vous pouvez voir qu'il a terminé l'analyse et a trouvé les mêmes vulnérabilités. Les vulnérabilités sont à nouveau marquées comme Faible, Moyen, Élevé et Critique. 

En plus de cela, il nous fournit également des suggestions pour corriger les problèmes. Par exemple, si vous regardez l'image ci-dessus, il suggère que nous devrions mettre à niveau Django de la version 3.1.12 à 3.2.13 pour résoudre de nombreux problèmes. 

Mettons à niveau Django et réanalysons l'application pour voir si ces vulnérabilités ont été corrigées ou non.

Nous allons d'abord mettre à niveau la version de Django à 3.2.13 en utilisant la commande :

```bash
pip install django==3.2.13
```

Vous obtiendrez une sortie similaire :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-190535_o8xsbe)

Maintenant, réanalysons le code en utilisant la commande **`snyk test`**.

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-190749_xadhap)

Maintenant, si vous remarquez, nous n'avons plus ces vulnérabilités telles que l'injection SQL.

#### **2. Commande `snyk monitor`**

Cette commande analyse le code et télécharge une capture instantanée sur l'interface utilisateur de Snyk ou la plateforme Snyk. Exécutons d'abord la commande :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-191230_sfugwx)

La commande a pris une capture instantanée du projet et l'a téléchargée sur la plateforme Snyk. Elle nous donne ensuite une URL où nous pouvons voir beaucoup d'autres informations concernant le projet. Si vous ouvrez l'URL, vous verrez une page similaire :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-191445_w8iqii)

Il est maintenant plus facile de voir les vulnérabilités dans l'application. Vous pouvez également retester l'application en cliquant sur le lien **Retest Now**. Vous pouvez également voir les **Fixes** et **Dependencies** de l'application.

### 3. Analyser l'Infrastructure as Code

Si vous regardez le projet, vous trouverez un dossier appelé **infrastructure**. Dans celui-ci, nous avons le **dossier application-load-balancer**. Donc, ce projet peut être déployé sur un équilibreur de charge AWS. 

Il y a un fichier Python `**app.py**` qui génère en réalité un modèle pour la configuration de l'équilibreur de charge sur AWS. Ensuite, dans le dossier **cdk.out**, vous pouvez trouver un fichier **LoadBalancerStack.template.json** généré à partir du code Python.

Pour analyser les éventuelles mauvaises configurations avant le déploiement, nous pouvons en fait tester ce fichier en utilisant Snyk. La commande pour cela est :

```bash
snyk iac test <template-file-path>
```

Exécutons et voyons la sortie :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-193031_vfjhco)

Il montre tous les problèmes et vulnérabilités dans le fichier de modèle.

### 4. Analyser le Dockerfile et les images Docker

Dans le projet, nous avons un Dockerfile. Vous pouvez construire l'image Docker à partir du Dockerfile en utilisant la commande :

```bash
docker build -t pygoat .
```

Vous pouvez voir l'image en cours de création ci-dessous :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-194028_hwvwcl)

Une fois l'image construite, vous pouvez analyser les vulnérabilités en utilisant la commande :

```bash
docker scan pygoat
```

L'intégration de Snyk avec Docker rend l'analyse incroyablement simple.

Vous obtiendrez la sortie suivante :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-194240_qmn7uc)

La sortie est très grande et il n'est pas possible de montrer tout ce qu'il y a. Mais nous pouvons voir les vulnérabilités dans l'image.

## Comment intégrer Snyk avec GitHub

Snyk peut automatiquement corriger les problèmes pour vous. Lorsque vous liez un dépôt GitHub à Snyk, il analysera l'ensemble du projet et s'il a une correction pour une vulnérabilité, il créera une Pull Request avec la correction. N'est-ce pas génial ?

Puisque nous nous sommes déjà connectés en utilisant GitHub, Snyk a déjà accès à nos dépôts. Nous devons simplement sélectionner le dépôt que nous souhaitons analyser.

Cliquez sur le bouton Add project, puis cliquez sur GitHub et sélectionnez votre dépôt.

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-194818_lep7yp)

Une fois que vous avez ajouté le projet, vous pouvez le trouver sur le tableau de bord. Snyk analysera automatiquement le projet. 

Une fois que vous voyez les problèmes, vous verrez un bouton **Corriger cette vulnérabilité** (pour chaque vulnérabilité) ou **Corriger ces vulnérabilités** (pour corriger toutes les vulnérabilités).

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-203739_wmekyo)

Lorsque vous cliquez dessus, vous verrez cette page :

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-204131_fmt2uc)

Vous pouvez sélectionner les cases à cocher pour corriger les vulnérabilités que vous souhaitez corriger, puis cliquer sur le bouton **Ouvrir une PR de correction**. Une fois que vous cliquez dessus, une PR est créée sur votre dépôt avec la correction.

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2022/05/20/screenshot-2022-05-20-204526_xbzqfo)

Maintenant, vous êtes libre de fusionner ou de rejeter la pull request.

## Conclusion

Dans cet article, nous avons appris à connaître Snyk, un outil qui peut nous aider à trouver des vulnérabilités et à les corriger. Ce n'était qu'un aperçu de base. Il y a beaucoup plus à apprendre à ce sujet.

Merci d'avoir lu !

Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris) ou consulter [mon blog](https://ireadblog.com).