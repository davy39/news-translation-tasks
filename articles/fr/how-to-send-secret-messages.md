---
title: Comment envoyer des messages secrets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T21:04:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-secret-messages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca196740569d1a4ca4f7c.jpg
tags:
- name: Cryptography
  slug: cryptography
- name: technology
  slug: technology
seo_title: Comment envoyer des messages secrets
seo_desc: 'By Megan Kaczanowski

  Cryptography is the science of using codes and ciphers to protect messages, at its
  most basic level. Encryption is encoding messages with the intent of only allowing
  the intended recipient to understand the meaning of the message...'
---

Par Megan Kaczanowski

La cryptographie est la science de l'utilisation de codes et de chiffres pour protéger les messages, à son niveau le plus basique. Le chiffrement consiste à coder des messages dans le but de permettre uniquement au destinataire prévu de comprendre le sens du message. Il s'agit d'une fonction à double sens (vous devez pouvoir annuler tout brouillage que vous avez fait au message). Cela est conçu pour protéger les données en transit. 

L'un des premiers chiffres impliquait un simple décalage. Par exemple, si vous décalez simplement toutes les lettres de l'alphabet de quelques positions, l'alphabet pourrait ressembler à ce qui suit :

ABCDEFGHIJKLMNOPQRSTUVWXYZ

NOPQRSTUVWXYZABCDEFGHIJKLM

Ensuite, chaque lettre de l'alphabet correspond à une lettre différente, mais il est difficile de déterminer laquelle, si vous ne le savez pas déjà. En utilisant ce chiffre, le message « Hello » se traduit par « Uryyb ».

Malheureusement, les avancées dans l'analyse, en particulier l'analyse de motifs alimentée par des ordinateurs très puissants, ont rendu ces types de chiffres très faciles à casser. 

En réponse à cela, nous avons développé des algorithmes très forts et complexes. Ceux-ci peuvent être divisés en deux types de base de chiffrement : les algorithmes symétriques et les algorithmes asymétriques. 

Les algorithmes symétriques sont également connus sous le nom d'algorithmes à « clé secrète », et les algorithmes asymétriques sont connus sous le nom d'algorithmes à « clé publique ». La différence clé entre les deux est que les algorithmes symétriques utilisent la même clé pour coder et décoder (voir la première figure ci-dessous), tandis que les algorithmes asymétriques utilisent des clés différentes pour le chiffrement et le déchiffrement (voir la deuxième figure ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.56.58-PM.png)

Comme vous pouvez le voir dans la figure ci-dessus, avec le chiffrement symétrique, si Bob et Midge veulent communiquer, Bob chiffrera d'abord son message avec la clé secrète (le message chiffré est appelé texte chiffré). Ensuite, il l'envoie à Midge. Midge déchiffre alors le message avec la même clé secrète et peut lire le message. Pour envoyer un message en retour, le processus est inversé. 

Ce processus est rapide, évolutif et très sécurisé. Le problème est qu'il nécessite que les deux parties possèdent déjà la même clé secrète. Si ce n'est pas le cas, elles doivent la transmettre via des canaux non sécurisés, ce qui supprime essentiellement la sécurité du chiffrement.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.57.02-PM.png)

Avec le chiffrement asymétrique, comme dans la figure ci-dessus, si Bob et Midge veulent communiquer, Bob chiffrera son message avec la clé publique de Midge et le lui enverra. Elle déchiffrera alors le message avec sa clé privée pour le lire. Pour envoyer un message en retour, le processus est inversé. 

De cette manière, n'importe qui peut envoyer un message à Midge, car elle peut rendre sa clé publique disponible à tous, mais seule elle peut déchiffrer un message (car elle garde sa clé privée secrète). Cela résout également le besoin de transmettre une clé secrète via des canaux non sécurisés, car il n'est pas nécessaire de transmettre un secret du tout. L'inconvénient est qu'il nécessite que chaque personne souhaitant communiquer possède deux clés différentes (peu évolutif), et il est relativement lent.

En général, lorsque l'on parle de chiffrement, les considérations les plus importantes sont :

* Authentification/Non-répudiation — Puis-je prouver d'où proviennent les messages (Suis-je sûr de qui a envoyé ce message ?).
* Réutilisation — Puis-je continuer à utiliser cette clé ou devra-t-elle être régénérée pour chaque nouvelle communication ?
* Efficacité — À quelle vitesse puis-je transférer de grandes quantités de données ?
* Évolutivité — Est-ce réalisable pour de grands groupes ?
* Distribution — Comment distribuez-vous les clés aux personnes avec lesquelles vous communiquez, sans divulguer le secret à quiconque ?

C'est là que des différences significatives commencent à apparaître entre le chiffrement symétrique et asymétrique, résumées ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.57.55-PM.png)

Afin d'utiliser le meilleur des deux mondes, de nombreux protocoles de chiffrement modernes utiliseront le chiffrement asymétrique pour établir une connexion et créer un secret partagé. Ensuite, ils passeront au chiffrement symétrique pour bénéficier de la différence de vitesse. 

%[https://twitter.com/preinheimer/status/841273046317060105]