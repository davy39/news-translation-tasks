---
title: Comment installer cPanel/WHM sur un VPS Digital Ocean
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T21:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-cpanel-whm-on-a-digital-ocean-vps-8146eb83f70a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*11DoUz1iZt4Fs6R_5SB_NA.jpeg
tags:
- name: deployment
  slug: deployment
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment installer cPanel/WHM sur un VPS Digital Ocean
seo_desc: 'By Michael Umanah

  Introduction

  In this article, I will be taking us through a step by step process of installing
  a cpanel/whm on a digital ocean VPS. Note that these steps can be used to install
  a cpanel/whm on any VPS, but for this post, I will be u...'
---

Par Michael Umanah

#### **Introduction**

Dans cet article, je vais vous guider à travers le processus d'installation de cPanel/WHM sur un VPS Digital Ocean. Notez que ces étapes peuvent être utilisées pour installer cPanel/WHM sur n'importe quel VPS, mais pour cet article, j'utiliserai un VPS Digital Ocean.

Choisir une plateforme d'hébergement fiable pour héberger vos projets peut être une tâche ardue. J'ai effectivement passé beaucoup de temps à lire des avis et à comparer des fonctionnalités avant de finalement opter pour Digital Ocean.

#### Pourquoi Digital Ocean

* Ils ont l'un des meilleurs prix pour leurs VPS — à partir de 5 $ par mois.
* Interface d'administration agréable
* Support très réactif
* Serveurs haute performance.

#### Pourquoi installer cPanel/WHM

Cpanel est un panneau de contrôle serveur basé sur le web qui rend la gestion de site un jeu d'enfant. Il inclut de nombreuses fonctionnalités telles que la création de comptes email, la sécurité du serveur, la gestion de domaines, les bases de données, et bien plus, qui simplifient le travail d'un DevOps. Vous pouvez voir une démonstration de son fonctionnement en suivant ce [lien](https://cpanel.com/demo/).

![Image](https://cdn-media-1.freecodecamp.org/images/Wg3kjVeNdAuPt3MQhhJ86fa7tBSjPoLggUku)
_tableau de bord cpanel_

#### Créer un compte avec Digital Ocean

Tout d'abord, vous devez ouvrir un compte avec Digital Ocean. En vous inscrivant avec ce lien, [https://bit.ly/2JvuZ2V](https://bit.ly/2JvuZ2V), vous recevrez un crédit de 10 $ sur votre compte à utiliser, et cela me donnera également un crédit de parrainage. Ce n'est vraiment pas grand-chose, mais c'est mieux que rien.

Si vous êtes étudiant ou connaissez quelqu'un qui l'est, inscrivez-vous au Student Pack de Github, et vous recevrez 50 $ supplémentaires à utiliser sur votre compte Digital Ocean.

![Image](https://cdn-media-1.freecodecamp.org/images/26S1HH2w-YjRYezgyUpWgdQ9snatGo4iEi0i)
_formulaire d'inscription digital ocean_

#### Créer un droplet

Une fois connecté à votre tableau de bord, allez dans le coin supérieur droit et cliquez sur le bouton créer dans le menu déroulant, puis sélectionnez droplets.

![Image](https://cdn-media-1.freecodecamp.org/images/-aYXUw-XzCMYqqE-SxppXNCMMDiLv3q92k56)
_tableau de bord digital ocean_

Droplet est le nom donné aux serveurs Digital Ocean, que vous utiliserez pour installer et configurer cPanel.

Vous serez alors redirigé vers un écran pour choisir une image. Cliquez sur centOS. Nous choisissons celui-ci car WHM/cPanel fonctionne sur un serveur CentOS.

![Image](https://cdn-media-1.freecodecamp.org/images/bPI5Y0v98EGFTQwonHxv9Z3bYmifXporepU0)

En faisant défiler vers le bas, vous pouvez choisir la taille du droplet que vous souhaitez. Vous pouvez choisir n'importe quelle configuration qui vous convient, mais gardez à l'esprit que la configuration minimale pour installer cPanel, comme indiqué sur le site web de cPanel, est de 1 Go de RAM et 20 Go d'espace disque.

![Image](https://cdn-media-1.freecodecamp.org/images/BxVgNSyBj2kcHNDEoXJS96Y-oyA03LhkDP5N)

Vous pouvez également choisir un stockage par blocs pour vos sauvegardes de données.

![Image](https://cdn-media-1.freecodecamp.org/images/GmkzZBXYAcvwKY9KvTSzXItS5utwbmIUKbcU)

En faisant défiler vers le bas, vous serez invité à choisir une région de centre de données. Si vous ciblez un pays spécifique avec la plupart de vos sites web, il est utile d'avoir un serveur local proche de l'endroit où la plupart de vos utilisateurs accéderont à vos sites web.

![Image](https://cdn-media-1.freecodecamp.org/images/4O2v6xt6WRBMLmeQLFn3IPegQaVcHQv0AlA2)

Plus bas, vous pouvez sélectionner des options supplémentaires. Ici, je choisis généralement Private Networking, IPv6 et Monitoring.

![Image](https://cdn-media-1.freecodecamp.org/images/mkUwhy1jkkl9kGeOvkQt3JOKz9le-YG24gEq)

Assurez-vous que votre nom d'hôte est HOSTNAME.YOURDOMAIN.COM

![Image](https://cdn-media-1.freecodecamp.org/images/NpervttWN0lB6-0c7wk5tU69gSBZ2wLXjAFQ)

Une fois que vous avez finalisé, Digital Ocean commencera à créer votre droplet et vous enverra les clés SSH par email, vous donnant un accès root à votre serveur.

#### Installer Cpanel sur votre droplet.

Une fois que vous recevez l'email, cela signifie que votre serveur est prêt et que vous pouvez commencer à installer cPanel/WHM dessus. Vous devez noter les éléments suivants dans l'email :

* Nom du Droplet
* Adresse IP du Droplet
* Nom d'utilisateur du Droplet (qui sera root)
* Mot de passe du Droplet (que vous devrez changer lors de la première connexion)

Nous devons pouvoir accéder à notre serveur à distance pour exécuter quelques commandes.

Pour les utilisateurs de Mac, vous pouvez le faire facilement en utilisant le terminal. Ouvrez le terminal sur votre Mac et tapez la commande suivante.

```
ssh root@162.345.323.09
```

Le numéro ci-dessus doit être l'adresse IP du droplet qui vous a été envoyée par email.

Il vous demandera alors le mot de passe que vous pouvez copier et coller, puis cliquez sur entrer.

Notez que lors de la saisie ou du collage du mot de passe, le champ ne s'affichera pas — cliquez simplement sur entrer après l'avoir collé.

Pour les utilisateurs de Windows, je recommande d'utiliser PuTTY (que vous pouvez télécharger [ici](https://www.putty.org/)). C'est un logiciel gratuit que vous pouvez utiliser pour obtenir un accès shell à un serveur.

Après avoir installé PuTTY et l'avoir ouvert, voici ce que vous verrez.

![Image](https://cdn-media-1.freecodecamp.org/images/ulAvPqtMbowO7GwzJ-lWeOBE6rM9ZKlB6IC1)

Tout ce que vous avez à ajouter ici est votre Nom d'hôte (ou adresse IP du Droplet) et cliquez sur Ouvrir.

Vous allez vous connecter en tant que "root", puis copier et coller le mot de passe que vous avez noté précédemment.

Note : Pour copier et coller sur Windows, cliquez simplement avec le bouton droit de la souris et appuyez sur entrer. PuTTY n'affiche pas votre mot de passe pour des raisons de sécurité, mais il est là.

Par défaut, Digital Ocean va vous demander de réinitialiser votre mot de passe. Entrez simplement votre mot de passe actuel, puis votre nouveau mot de passe souhaité, et appuyez sur entrer.

#### Installer cPanel

L'installation de cPanel est assez simple, nous allons simplement exécuter quelques commandes sur notre serveur. Nous commençons par préparer notre serveur pour l'installation de cPanel en exécutant la commande suivante pour installer perl.

```
sudo yum install perl
```

Après avoir installé perl, nous devons effectuer une étape préliminaire supplémentaire. cPanel est très exigeant quant à la vérification que le serveur sur lequel il est installé possède un Nom de Domaine Complètement Qualifié. À cet effet, nous devons lui fournir un nom d'hôte valide. Vous pouvez en entrer un temporaire et le corriger une fois cPanel installé.

```
hostname  host.example.com
```

**Note : la dernière commande doit être votre propre nom d'hôte.**

Nous avons maintenant terminé la pré-installation, nous allons donc commencer l'installation réelle de cPanel. Nous commençons par installer screen et wget.

```
sudo yum install screen wget
```

Une fois screen et wget installés, nous pouvons démarrer une nouvelle session screen en tapant ceci.

```
screen
```

Après avoir ouvert screen, nous pouvons alors commencer à installer cPanel en utilisant cette commande.

```
wget -N http://httpupdate.cPanel.net/latest
```

Une fois cela fait, nous pouvons démarrer le script en tapant la commande.

```
sh latest
```

Le script peut prendre de 1 à 3 heures pour s'exécuter, vous devez donc être patient jusqu'à ce qu'il soit terminé.

#### Configurer votre nouveau compte cPanel.

Wow, nous avons enfin installé cPanel sur le serveur. La prochaine étape est de configurer les paramètres de base.

#### Accéder à votre serveur

Pour accéder à votre serveur, allez sur [https://ADRESSE_IP_DU_DROPLET:2087](https://ADRESSEIPDUDROPLET:2087) dans votre navigateur et entrez votre nom d'utilisateur et votre mot de passe root.

```
exemple : https://162.345.323.09:2087
```

![Image](https://cdn-media-1.freecodecamp.org/images/iYx-vDaqjOVLFWR0qvz5WDg0QOSU0bmmkQhq)

Une fois connecté, nous devons maintenant ajouter les fonctionnalités de base à WHM et accepter leurs conditions de licence.

![Image](https://cdn-media-1.freecodecamp.org/images/VeZ9ewLKTOPCNuMo6CnaLWPX6hxmnUAzXCB5)

Ensuite, entrez votre email de contact et passez à l'étape suivante. Vous n'avez pas besoin de changer les autres paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/73gDsVSuVq9ubJNlGfurBVYhg9DQaeXT2oh9)

Passez l'étape suivante.

Assurez-vous que votre Configuration de Serveur de Noms est définie sur BIND, et faites défiler vers le bas pour sélectionner vos serveurs de noms.

![Image](https://cdn-media-1.freecodecamp.org/images/iSlAPTsuF87L0TmsCaQf7kzQxwHaircXsSws)

Laissez les paramètres de votre Serveur FTP définis sur Pure-FTPD — c'est le paramètre par défaut sur tous les systèmes cPanel. Une fois terminé, passez à l'étape suivante.

Sélectionnez Utiliser les quotas de système de fichiers et cliquez sur Terminer.

![Image](https://cdn-media-1.freecodecamp.org/images/fHrlNyeDk-wwNBIZguYKijcdkXM6GlZaBazm)

Et vous avez terminé ! WHM est maintenant installé. Prêt pour que vous commenciez à créer des comptes et à ajouter vos domaines.

#### Licence cPanel/WHM

Pour utiliser cPanel/WHM sur votre serveur, vous devrez payer pour une licence. Mais comme vous installez cPanel sur un nouveau serveur avec une nouvelle adresse IP, vous aurez un essai gratuit de 15 jours. Après cela, vous devrez ajouter une licence, sinon vous serez bloqué hors de WHM.

L'achat d'une licence VPS WHM/cPanel auprès de cPanel vous coûtera 20 $ par mois. Mais si vous souhaitez économiser, vous pouvez suivre [ce lien](https://www.buycpanel.com/) pour acheter la même licence pour seulement 15 dollars par mois auprès de "buy cpanel", qui est un revendeur agréé pour cPanel.

![Image](https://cdn-media-1.freecodecamp.org/images/dm4vk7s3kVYmFDOTdkzcZuX5TyoFE3XHljIR)
_page d'accueil de buycpanel_

Après avoir cliqué sur le lien, n'oubliez pas de sélectionner la licence VPS WHM/cPanel, puis vous pouvez ajouter les addons que vous souhaitez. Ensuite, procédez au paiement.

C'est vraiment aussi simple. Si vous rencontrez des problèmes ou avez des suggestions lors de l'installation, vous pouvez simplement ajouter un commentaire et je vous répondrai certainement.