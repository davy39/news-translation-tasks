---
title: Comment utiliser Node Version Manager dans vos projets React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-21T13:51:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-nvm-in-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/React
seo_title: Comment utiliser Node Version Manager dans vos projets React
---

NVM.png
tags:
- name: node
  slug: node
- name: React
  slug: react
seo_title: null
seo_desc: Dans ce guide, vous apprendrez à gérer efficacement plusieurs versions de Node pour différents projets en utilisant Node Version Manager (NVM). Que vous développiez des applications React, Angular, Vue.js ou Node, vous pouvez toujours utiliser NVM pour configurer le projet et l'adapter à une version spécifique de Node.
---

Dans ce guide, vous apprendrez à gérer efficacement plusieurs versions de Node pour différents projets en utilisant Node Version Manager (NVM). Que vous développiez des applications React, Angular, Vue.js ou Node, vous pouvez toujours utiliser NVM pour configurer le projet et l'adapter à une version spécifique de Node.

## Prérequis

Avant de commencer, vous devez avoir quelques [connaissances de base de la ligne de commande](https://www.freecodecamp.org/news/command-line-commands-cli-tutorial/). Rien de sophistiqué, mais assurez-vous de l'avoir utilisée avant de lire cet article, sinon vous pourriez vous sentir un peu perdu.

## Qu'est-ce que NVM ?

Node Version Manager (NVM) est un utilitaire en ligne de commande qui vous permet de gérer plusieurs installations de Node.js et de basculer facilement entre elles.

Que vous ayez besoin de travailler sur des projets nécessitant différentes versions de Node.js ou que vous souhaitiez expérimenter les dernières versions sans affecter vos configurations existantes, NVM fournit un moyen facile de le faire.

## Pourquoi avez-vous besoin de plusieurs versions de Node ?

De nos jours, les entreprises construisent souvent leurs applications selon une architecture de microservices. Cela signifie que les applications tendent à être divisées en de nombreux services plus petits, où chaque service a son rôle dédié.

Cela peut sembler être une sur-ingénierie, mais il y a quelques avantages à cette approche. Dans certains cas, les entreprises décident de construire leurs applications en utilisant des microservices pour atteindre une haute disponibilité et permettre des déploiements sans temps d'arrêt. En fin de compte, elles peuvent déployer un service à la fois.

Cette approche a également des inconvénients liés à la complexité et à la gestion de plusieurs projets. Imaginez que votre application est divisée en de nombreux microservices, où le premier a été construit il y a plus de 5 ans.

Le service fonctionne probablement sur une version héritée de Node.js. Dans un monde idéal, vous devriez mettre à jour la version de Node vers la version la plus récente, mais ce n'est pas toujours possible. En fin de compte, la satisfaction des utilisateurs passe en premier, et si ils ont besoin de nouvelles fonctionnalités, leurs besoins doivent être satisfaits en premier.

Parfois, une nouvelle fonctionnalité peut vous obliger à introduire un nouveau microservice. Dans ce cas, vous devriez toujours essayer d'utiliser la version la plus récente de Node disponible. Je vais vous montrer comment installer plusieurs versions de Node sur votre machine.

## Mais je suis un développeur Front End

Vous aurez toujours besoin de NVM en tant que développeur front end.

De nos jours, chaque bibliothèque et framework JavaScript nécessite un environnement d'exécution Node, c'est pourquoi vous devriez gérer les versions de Node pour les projets front end également. Le projet exemple que nous utiliserons dans cet article est construit avec React 18 et Next.js.

Commençons.

## Comment installer NVM sur Linux et Mac

L'installation sur Linux et Mac est ultra simple.

Ouvrez simplement votre terminal et exécutez la commande suivante :

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Ce script configurera NVM sur votre machine et vous pourrez l'utiliser immédiatement. Rien d'autre n'est requis.

Essayez simplement d'exécuter la commande `nvm` dans votre terminal, et vous devriez voir la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-19-at-21.57.31.png)
_sortie de la commande nvm_

Si vous voyez quelque chose comme `nvm: command not found`, vous pouvez exécuter ces commandes :

```sh
source ~/.bashrc
source ~/.zshrc
```

Il est attendu qu'une des deux échoue. Ces commandes rechargeront votre profil bash/zsh et activeront NVM dans votre invite de commande.

## Comment installer NVM sur Windows

Vous pouvez facilement installer NVM sur Windows – il suffit d'[ouvrir le dépôt nvm-windows sur GitHub](https://github.com/coreybutler/nvm-windows/releases), de faire défiler jusqu'à la section **Assets** et de télécharger le fichier `nvm-setup.exe`.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-19-at-22.04.05.png)
_Dépôt NVM Windows_

Le fichier d'installation sera maintenant téléchargé. Une fois le téléchargement terminé, double-cliquez sur le fichier `nvm-setup.exe` et suivez les instructions :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/nvm-installer.jpg)
_Installeur NVM pour Windows par [Corey Butler](https://github.com/coreybutler)_

Après l'installation, ouvrez PowerShell et exécutez la commande `nvm`, vous devriez voir la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/nvm-1.1.8-screenshot.jpg)
_NVM dans PowerShell par [Corey Butler](https://github.com/coreybutler)_

Si la commande `nvm` retourne `command not found`, vous devriez redémarrer votre ordinateur pour actualiser vos paramètres utilisateur.

## Comment définir la version de Node pour votre projet

Maintenant, nous arrivons au cœur de ce guide – définir une version dédiée de Node pour votre projet.

Tout d'abord, créez un fichier **.nvmrc** dans le dossier racine de votre projet et spécifiez la version de Node attendue.

Dans mon cas, c'est `20.10.0` :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-19-at-22.24.11.png)
_Version de Node dans le fichier .nvmrc_

Ouvrez maintenant votre terminal, naviguez jusqu'à votre projet et exécutez la commande `nvm use`. NVM chargera automatiquement la version de Node attendue par votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-19-at-22.27.04.png)
_commande nvm use_

Si vous n'avez pas la version attendue sur votre machine, vous serez invité à l'installer :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-19-at-22.28.46.png)
_invitation à installer la version de Node_

Dans ce cas, vous devez installer la version requise de Node en exécutant `nvm install x.y.z`. Remplacez `x.y.z` par la version de Node attendue. Dans mon cas, c'était `20.10.0`.

## Conclusion

Travailler sur plusieurs projets peut être fastidieux, surtout lorsqu'ils nécessitent différentes versions de Node. Cependant, avec NVM, changer la version de Node est aussi rapide qu'un clin d'œil.

Vous devriez toujours l'utiliser, que vous travailliez seul sur votre projet personnel ou avec plusieurs collègues sur une grande application d'entreprise.

Si cet article vous a aidé, veuillez le partager sur vos réseaux sociaux ou me donner un [coup de pouce sur Twitter](https://twitter.com/msokola). Merci !

## **Apprendre React 18 et Next.js**

Cet article fait partie de mon cours React et Next.js sur Udemy. Je vous aiderai à démarrer avec React et Next.js en créant un jeu 2048 avec des animations géniales. Je crois que créer des jeux rend l'apprentissage plus amusant, et vous aurez quelque chose de cool à montrer à vos amis.

👍👍👍👍

### **🧑‍🏫** Inscrivez-vous à **mon [cours sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106)**