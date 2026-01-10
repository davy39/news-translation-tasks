---
title: Comment écrire des tests unitaires pour les contrats intelligents ERC-20 Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T14:22:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-erc-20-ethereum-smart-contracts-abfa2c482aea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b8-UrpS2ct361i2QWAVeRw.jpeg
tags: []
seo_title: Comment écrire des tests unitaires pour les contrats intelligents ERC-20
  Ethereum
seo_desc: 'By Il Kadyrov

  It’s very important to write unit tests for your smart contracts, same as for any
  development project. However, unit testing in blockchain-based solutions is often
  underestimated and overlooked.

  Last year I performed more than 200 audit...'
---

Par Il Kadyrov

Il est très important d'écrire des tests unitaires pour vos contrats intelligents, comme pour tout projet de développement. Cependant, les tests unitaires dans les solutions basées sur la blockchain sont souvent sous-estimés et négligés.

L'année dernière, j'ai effectué plus de 200 audits de contrats intelligents écrits principalement pour Ethereum, ainsi que pour les blockchains Neo, Eos, Tron et Bitcoin.

D'après ce que j'ai observé, près de la moitié de ces projets n'avaient pas écrit de tests unitaires. Une telle négligence a souvent entraîné de mauvaises performances des contrats et divers problèmes de sécurité identifiés lors de l'audit.

#### Tests indispensables

![Image](https://cdn-media-1.freecodecamp.org/images/1*8fQ1Akp_3eABKt_w9t_emQ.png)

Chaque contrat intelligent comporte des parties communes telles que

* un constructeur
* l'offre totale
* des fonctions de transfert vers et depuis
* des fonctions d'approbation
* et parfois une fonction pour brûler les jetons excédentaires

Il est donc important de vérifier que votre contrat intelligent initialise correctement tous les paramètres, et qu'il génère des erreurs en cas de dépassement ou de sous-dépassement de l'offre totale ou d'autres valeurs _uint_. Vous devez également vérifier les modificateurs et l'utilisation correcte des droits.

Dans cet article, je me concentrerai spécifiquement sur les contrats intelligents Ethereum, mais cela s'applique également à d'autres plateformes, car les contrats ont la même structure dans d'autres cryptomonnaies. Tout d'abord, testons l'initialisation correcte du jeton et son transfert correct vers une adresse.

#### Vérification de l'initialisation

Les tests pour une initialisation correcte sont simples. Vous devez simplement créer un contrat d'exemple et vérifier la correction de toutes les valeurs qui doivent être initialisées.

#### Vérification des transferts

Vérifier la fonction **_transfer_** est très important, car il peut y avoir des problèmes qui entraîneraient des transferts incorrects. Vous devez vous assurer que les soldes du destinataire et de l'expéditeur changent lors du transfert, et essayer d'obtenir des erreurs si la fonction reçoit de mauvais paramètres.

Par exemple,

* lorsque le montant envoyé dépasse le solde de l'expéditeur
* lorsque l'adresse du contrat ou une adresse invalide est envoyée au lieu de l'adresse du destinataire, etc.

Et enfin, vous devez vérifier que l'événement _transfer_ est **journalisé**.

La fonction **_transferFrom_** est très similaire à transfer, mais ici vous devez également tester que le dépensier a suffisamment de solde approuvé pour envoyer.

Voici les tests lorsque le dépensier n'a pas suffisamment de fonds nécessaires pour un transfert.

#### Vérification des approbations

La fonction **approve** est la fonction la plus simple de la norme ERC20. Il n'est pas nécessaire de vérifier l'adresse zéro. Il suffit de vérifier que le tableau d'autorisation est correctement rempli. De plus, si vous n'avez pas de fonctions increaseApproval ou decreaseApproval, approve écrasera toutes les valeurs précédentes.

Il est donc recommandé d'utiliser ces fonctions pour se protéger contre les écrasements inutiles. Et bien sûr, il est important de vérifier que vous obtenez les bons journaux de l'événement Approval.

#### Brûler les jetons non vendus

La plupart des contrats intelligents incluent une fonction pour **brûler** les jetons restants après la vente principale. Beaucoup d'entre eux ont un compte spécial de détenteur de jetons, parfois c'est le compte du propriétaire. La meilleure solution pour brûler les jetons non vendus est la suivante :

* obtenir le montant des jetons sur l'adresse du détenteur
* puis soustraire ce montant de l'offre totale
* et mettre à zéro le montant des jetons sur l'adresse du détenteur.

Cela garantira que vous ne brûlez pas tous les jetons, il est donc important de décrire votre stratégie de brûlage de jetons dans votre livre blanc.

#### Conclusion

Il est très important de tester votre contrat intelligent avant de le déployer sur le réseau principal afin de prévenir les problèmes à l'avenir. Lorsque vous avez écrit des tests unitaires, ils garantiront qu'il n'y aura aucune divergence entre votre livre blanc et votre contrat intelligent, et que votre contrat intelligent ne sera pas piraté en appelant des fonctions qui _devraient_ avoir les droits corrects mais qui _ne les ont pas_.

Ce n'est pas seulement une question de contrats intelligents : vous avez besoin de tests unitaires pour toutes vos applications et votre code, car cela vous montre toutes les façons dont votre application aurait pu échouer.