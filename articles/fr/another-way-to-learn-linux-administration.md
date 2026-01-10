---
title: Une autre façon d'apprendre l'administration Linux
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-21T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/another-way-to-learn-linux-administration
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0b7740569d1a4ca4a58.jpg
tags:
- name: Linux
  slug: linux
- name: servers
  slug: servers
- name: System administration
  slug: system-administration
seo_title: Une autre façon d'apprendre l'administration Linux
seo_desc: "Looking to learn to administer Linux computers? Excellent choice. While\
  \ it can hold its own in the consumer desktop space, where Linux absolutely dominates\
  \ is the world of servers, especially virtual and cloud servers. \nBecause most\
  \ serious server ad..."
---

Vous souhaitez apprendre à administrer des ordinateurs Linux ? Excellent choix. Bien qu'il puisse se défendre dans l'espace des postes de travail grand public, Linux domine absolument le monde des serveurs, en particulier les serveurs virtuels et cloud. 

Étant donné que la plupart des administrations de serveurs sérieuses de nos jours se font à distance, travailler à travers une interface GUI d'un type ou d'un autre ajoute simplement une surcharge inutile. 

Si vous souhaitez gérer les serveurs et les architectures réseau qui attirent actuellement toute l'attention, vous devrez apprendre à vous débrouiller avec la ligne de commande Linux.

La bonne nouvelle est que l'ensemble de base des commandes Linux fonctionnera pour vous à travers les lignes géographiques et corporatives, presque partout où les ordinateurs et les entreprises se croisent. La meilleure nouvelle est que, relativement parlant, les compétences Linux ont une longue durée de vie.

Parce que c'est un système d'exploitation si mature et stable, la plupart des outils utilisés il y a un quart de siècle sont toujours aussi efficaces qu'avant, et la plupart des outils utilisés aujourd'hui seront probablement encore activement utilisés après un autre quart de siècle. Apprendre Linux, en d'autres termes, est un investissement pour la vie.

#### Comment fonctionne Linux en Action

Mais vous êtes occupé et vous avez des délais. Eh bien, je ne peux pas vous promettre que maîtriser Linux sera aussi simple que d'apprendre à lacer vos chaussures. Mais je peux vous aider à vous concentrer comme un laser afin que vous puissiez laisser tout ce dont vous n'avez pas besoin sur l'autoroute, étouffant dans vos fumées d'échappement (en supposant que vous ne conduisez pas une Tesla, bien sûr).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-146.png)
_Linux en Action de Manning_

Comment vais-je réussir cela ? Mon [livre Linux en Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) tourne la formation technologique de côté. C'est-à-dire que, tandis que d'autres livres, cours et ressources en ligne organisent leur contenu autour de catégories (« Allez les enfants, sortez vos règles à calcul et vos crayons à charbon. Aujourd'hui, nous allons apprendre les systèmes de fichiers Linux. »), j'utilise des projets du monde réel pour enseigner.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-147.png)
_Les compétences et les sujets associés couverts par [Linux en Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&amp;a_bid=4ca15fc9)_

Ainsi, par exemple, j'aurais pu construire un chapitre entier (ou deux) sur les systèmes de fichiers Linux. Mais au lieu de cela, vous apprendrez à construire des serveurs de fichiers d'entreprise, des disques de récupération système et des scripts pour répliquer des archives de données critiques. Dans le processus, vous acquerrez les connaissances sur les systèmes de fichiers en bonus gratuit.

Ne pensez pas que je vais couvrir chaque outil d'administration Linux. C'est impossible : il en existe littéralement des milliers. Mais ne vous inquiétez pas. Les compétences et fonctionnalités de base nécessaires au cours des premières années d'une carrière en administration Linux seront couvertes, et bien couvertes, mais seulement lorsqu'elles seront nécessaires pour un projet pratique et critique. Une fois terminé, vous aurez appris au moins autant que ce que vous auriez appris d'une source traditionnelle, mais vous saurez également comment compléter plus d'une douzaine de projets administratifs majeurs, et serez à l'aise pour aborder des dizaines d'autres.

Vous êtes partant ? Je le pensais.

## Qui devrait lire ce livre

Ce livre est conçu pour vous aider à acquérir une solide gamme de compétences en administration Linux. Peut-être êtes-vous un développeur qui souhaite travailler plus directement avec l'environnement serveur dans lequel vos applications vivront. Ou peut-être êtes-vous prêt à faire votre entrée dans le monde de l'administration serveur ou DevOps. Dans les deux cas, vous êtes au bon endroit.

Que devriez-vous déjà savoir ? Au minimum, vous devriez être à l'aise avec les fichiers, les réseaux et les ressources de base d'un système d'exploitation moderne. Une expérience en administration système, en gestion de réseau et en langages de programmation ne sera certainement pas un handicap, mais n'est pas requise. Par-dessus tout, vous devriez ne pas avoir peur d'explorer de nouveaux environnements et être enthousiaste à l'idée d'expérimenter avec de nouveaux outils.

Une dernière chose : vous êtes censé savoir comment effectuer une installation simple et directe d'un système d'exploitation Linux.

Juste quelques mots sur la façon dont le livre est construit. Chaque chapitre de Linux en Action couvre un ou deux projets pratiques — sauf le chapitre 1. Le chapitre 1, parce qu'il est conçu pour combler les lacunes très basiques qui pourraient exister dans vos connaissances Linux, sera différent de tous les autres. Vous n'avez pas besoin des bases ? Je suis absolument sûr que vous trouverez beaucoup de nouveaux jouets amusants avec lesquels jouer dans le chapitre 2.

En plus des projets du livre, je vous présenterai également les compétences et outils individuels dont vous aurez besoin. De plus, les projets de chaque chapitre s'appuient généralement sur les compétences que vous avez apprises précédemment dans le livre. Juste pour vous montrer que je suis sérieux, voici une liste assez complète des principaux projets (sous l'en-tête Chapitre), des domaines de compétences et des outils que vous rencontrerez tout au long du livre :

Il existe actuellement des dizaines de distributions Linux activement maintenues. Même si la plupart des bases de Linux sont communes à toutes les distributions, il y aura toujours de petites choses qui fonctionneront « ici » mais pas « là ». Pour des raisons pratiques, je vais me concentrer principalement sur deux distributions : Ubuntu et CentOS. Pourquoi ces deux-là ? Parce que chacune représente une famille entière de distributions. Ubuntu partage ses racines avec Debian, Mint, Kali Linux et d'autres, tandis que CentOS profite de la compagnie de Red Hat Enterprise Linux (RHEL) et Fedora.

Ce n'est pas pour dire que je ne valorise pas d'autres distributions comme Arch Linux, SUSE et Gentoo, ou que ce que vous apprendrez dans ce livre ne vous aidera pas à travailler avec ces environnements. Mais couvrir pleinement les familles Ubuntu et CentOS signifie saisir la plus grande part du gâteau Linux que je pouvais atteindre en utilisant seulement deux distributions.

_Cet article a été adapté de l'introduction à mon livre_ [_Linux en Action_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. En plus du livre, vous pouvez également travailler avec_ [_Linux en Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) — _un cours hybride composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux en Action._