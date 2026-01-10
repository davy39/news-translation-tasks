---
title: Comment télécharger des applications rapidement en utilisant des miroirs sur
  Manjaro Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-11-09T18:57:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-application-fast-on-manjaro-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/1631592932_Manjaro-Linux-211-with-fresh-desktop-environments.png
tags:
- name: Linux
  slug: linux
- name: performance
  slug: performance
- name: servers
  slug: servers
seo_title: Comment télécharger des applications rapidement en utilisant des miroirs
  sur Manjaro Linux
seo_desc: 'If you are running Linux OS, you''ve likely already heard about mirror
  repositories. According to Quora,


  In Linux, a mirror is a copy of programs available for download. If you are close
  (in networking terms, maybe or maybe not geographically) to one...'
---

Si vous utilisez un système d'exploitation Linux, vous avez probablement déjà entendu parler des dépôts miroirs. Selon Quora,

> Dans Linux, un miroir est une copie des programmes disponibles pour le téléchargement. Si vous êtes proche (en termes de réseau, peut-être ou peut-être pas géographiquement) de l'un des sites miroirs listés, vous pourriez choisir le site miroir comme votre principale source de téléchargements pour obtenir de meilleurs temps de réponse.


Différents systèmes d'exploitation basés sur Linux ont différentes méthodes pour vous aider à choisir les miroirs les plus rapides. Mais la plupart des solutions de contournement sont à peu près les mêmes.

J'ai utilisé [Manjaro](https://manjaro.org/) pendant assez longtemps, et c'est l'un des systèmes d'exploitation basés sur Linux les plus populaires. J'ai donc décidé d'écrire cet article à ce sujet.

Comme beaucoup d'entre nous aiment utiliser le CLI (Command Line Interface) pour télécharger les applications et les paquets nécessaires dans les systèmes d'exploitation basés sur Linux, avoir une vitesse internet décente est très utile. Les dépôts/serveurs miroirs nous aident avec cela.

## Pourquoi les serveurs miroirs sont utiles

Alors que Linux devient de plus en plus populaire, de nombreux serveurs sont créés dans divers pays qui conservent les mêmes données que celles présentes sur les serveurs officiels.

Nous appelons ces serveurs miroirs car ils ne font que miroir (copier) les données originales des sources originales et conservent ces données sur leurs serveurs. Cela aide les utilisateurs proches d'eux à obtenir les données à une vitesse décente.

De plus, ces serveurs/dépôts miroirs réduisent la pression sur les serveurs internationaux mondiaux.

Mais gardez à l'esprit que tous les serveurs miroirs n'ont peut-être pas une réputation décente pour contenir des logiciels malveillants/des données non mises à jour, etc. La meilleure pratique avant d'ajouter un serveur miroir est de rechercher sur Google/Reddit. 

Je préfère toujours la communauté officielle sur Reddit car je peux obtenir des informations légitimes de leur grande base d'utilisateurs.

Si vous recherchez simplement sur Reddit, vous obtiendrez d'innombrables subreddits pour les utilisateurs de Linux. Les forums officiels et les documents sont également vraiment utiles pour ces informations.

Par défaut, les systèmes d'exploitation Linux viennent avec des serveurs/dépôts mondiaux pour télécharger des applications et des paquets, car ils ont des clients du monde entier. Mais si vous souhaitez passer à un serveur spécifique d'où vous pouvez télécharger les paquets nécessaires à une vitesse décente, vous pouvez le faire manuellement.

### Cas d'utilisation du serveur miroir

Si vous n'êtes pas super familier avec ces serveurs/dépôts miroirs, laissez-moi également vous fournir un scénario de cas réel.

Supposons que vous souhaitez télécharger un fichier, et que ce fichier est hébergé sur plusieurs serveurs situés dans différents pays.

Disons que vous êtes au Bangladesh, et que vous souhaitez télécharger une application. Lorsque vous commencez à télécharger le fichier de l'application, il commence à télécharger depuis le serveur international mondial situé aux États-Unis. Naturellement, cela prendra plus de temps à télécharger depuis ce serveur étant donné la longue distance, n'est-ce pas ?

Mais il est également possible que le même fichier d'application soit également hébergé en Inde, un pays proche de votre pays. Si vous téléchargez le fichier de l'application depuis le serveur indien à la place, alors cela prendra définitivement moins de temps.

C'est parce que ce serveur est plus proche que l'autre aux États-Unis – donc la distance que les données doivent parcourir est plus petite. Ainsi, vous pouvez télécharger et obtenir votre fichier d'application plus rapidement.

Maintenant, voyons comment activer un serveur miroir.

## Comment activer le miroir le plus rapide sur Manjaro Linux

Commencez simplement par ouvrir votre terminal. Ensuite, appliquez la commande suivante :

```bash
sudo pacman-mirrors --country all --api --protocols all --set-branch stable && sudo pacman -Syyu
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034726.png)

Entrez le mot de passe et appuyez sur la touche `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034736.png)

Cela prendra un certain temps en fonction de votre vitesse internet. Ensuite, il sélectionnera automatiquement le miroir le plus rapide qu'il peut trouver pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034748.png)

Après cela, je vous suggère de redémarrer votre PC / de vous déconnecter et de vous reconnecter à la session.

C'est tout ! Si vous voulez en savoir plus, alors le [wiki officiel](https://wiki.manjaro.org/index.php/Pacman-mirrors) est également disponible pour vous ici.

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez entrer en contact avec moi, vous pouvez le faire en utilisant [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA).

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec beaucoup d'exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !

_L'image de couverture a été prise depuis [ici](https://marketresearchtelecast.com/manjaro-linux-21-1-with-fresh-desktop-environments/155191/).