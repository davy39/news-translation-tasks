---
title: Voici comment j'aurais pu rouler gratuitement avec Uber
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-26T10:43:53.000Z'
originalURL: https://freecodecamp.org/news/how-anyone-could-have-used-uber-to-ride-for-free-36cdee5ea854
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cK-cejMVQq51oIX9C7M60A.jpeg
tags:
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: uber
  slug: uber
- name: Web App Security
  slug: web-app-security
seo_title: Voici comment j'aurais pu rouler gratuitement avec Uber
seo_desc: 'By AppSecure

  Summary

  This post is about a critical bug on Uber which could have been used by hackers
  to get unlimited free Uber rides anywhere in the world. This post also explains
  few best practices while integrating payment gateways.

  Description

  Ub...'
---

Par AppSecure

### Résumé

Cet article traite d'un bug critique sur Uber qui aurait pu être utilisé par des pirates pour obtenir des trajets Uber gratuits illimités partout dans le monde. Cet article explique également quelques bonnes pratiques lors de l'intégration des passerelles de paiement.

### Description

Uber Technologies Inc. est une entreprise de réseau de transport en ligne, basée à San Francisco, en Californie, avec des opérations dans 528 villes à travers le monde. Les utilisateurs peuvent créer leur compte sur Uber.com et réserver un trajet. Lorsque le trajet est terminé, un utilisateur peut soit payer en espèces, soit le charger sur sa carte de crédit/débit.

Mais, en spécifiant un mode de paiement invalide (par exemple, abc, xyz, etc.), j'ai pu rouler gratuitement avec Uber.

Pour démontrer le bug, j'ai obtenu la permission de l'équipe Uber et j'ai pris un trajet gratuit en Inde. Je n'ai pas été facturé pour aucun de mes trajets, en utilisant le mode de paiement invalide.

### Requête vulnérable:

> POST /api/dial/v2/requests HTTP/1.1 Host: dial.uber.com {"start_latitude":12.925151699999999,"start_longitude":77.6657536,
>  "product_id":"db6779d6-d8da-479f-8ac7–8068f4dade6f","payment_method_id":"xyz"}

### Étapes pour reproduire:

1. Rejouer la requête ci-dessus avec des caractères aléatoires comme payment_method_id.
2. Le trajet était gratuit.

#### Vidéo POC:

Merci à l'équipe de sécurité d'Uber pour avoir corrigé cela rapidement.

### Chronologie

22 août 2016 : Rapport de vulnérabilité à Uber.

26 août 2016 : Uber a demandé plus d'informations sur le bug.

26 août 2016 : J'ai pris un trajet gratuit et j'ai répondu avec les détails du trajet

27 août 2016 : Vulnérabilité corrigée par Uber.

10 septembre 2016 : Récompensé avec une prime de 5000 $ par Uber.

### Leçons à retenir

En tant que développeur, vous devez toujours prendre en compte les cas de test suivants lors de l'intégration des paiements :

a) Vérifiez si le paiement a réussi ou échoué en effectuant une requête serveur à serveur vers la passerelle de paiement ou en vérifiant la somme de contrôle avec le fournisseur de la passerelle de paiement.

b) Validez toujours le montant de l'article avec le montant payé par l'utilisateur à la passerelle de paiement.

c) Validez la devise dans les appels d'API de paiement. Par exemple, l'attaquant peut payer 50 IDR pour un article de 50 USD.

d) Si vous stockez des informations de cartes de crédit/débit, vérifiez toujours l'autorisation si un identifiant est passé dans l'une des requêtes API.

> [**AppSecure**](https://appsecure.in) est une entreprise spécialisée en cybersécurité avec des années de compétences acquises et une expertise méticuleuse. Nous sommes là pour protéger votre entreprise et vos données critiques contre les menaces ou vulnérabilités en ligne et hors ligne.

> Contactez-nous : **hello@appsecure.in**