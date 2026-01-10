---
title: Comment vérifier les signatures de messages AS2 (SMIME) avec OpenSSL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T03:30:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-verify-as2-message-smime-signature-with-openssl-605c1affe3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E_4R13d5-VasRRr_JA9bxg.jpeg
tags:
- name: b2b
  slug: b2b
- name: openssl
  slug: openssl
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment vérifier les signatures de messages AS2 (SMIME) avec OpenSSL
seo_desc: 'By Rajind Ruparathna

  Error MDNs stating an error in the lines of “Signature verification failed” or “Decryption
  failed” are common for users who are just getting started with AS2 in any AS2 service.
  We have seen many such instances in our SaaS B2B AS...'
---

Par Rajind Ruparathna

Les MDN d'erreur indiquant une erreur du type **"La vérification de la signature a échoué"** ou "Le déchiffrement a échoué" sont courants pour les utilisateurs qui commencent à utiliser AS2 dans un service AS2. Nous avons vu de nombreux cas de ce type sur notre plateforme SaaS de messagerie B2B AS2, [AdroitLogic AS2Gateway](http://as2gateway.com/). Avec ce type d'erreurs, il est parfois important pour l'équipe de support et également pour l'utilisateur de pouvoir [essayer le déchiffrement](https://notebookbft.wordpress.com/2019/03/17/how-to-decrypt-an-as2-message-smime-with-openssl/) ou la vérification de la signature manuellement pour obtenir plus d'informations.

Dans cet article de blog, nous allons examiner ce qu'est la signature numérique dans le protocole AS2, comment vérifier la signature d'un message AS2, et quelques conseils pour déterminer la cause de certaines échecs de vérification de signature.

### Signature dans le protocole AS2

La signature AS2 est essentiellement une signature numérique qui fournit une authentification, une intégrité des données et une non-répudiation à la communication AS2.

* Authentification — Assure que le destinataire effectue une transaction avec l'expéditeur avec lequel il était censé effectuer une transaction (et non un imposteur)
* Intégrité des données — Détermine si le fichier ou les données reçues par le destinataire ont été altérés en cours de route
* Non-répudiation — Empêche l'expéditeur de nier que les messages qu'il a envoyés proviennent de lui

![Image](https://cdn-media-1.freecodecamp.org/images/QOy4kQEnq9wNekhfJZpPYQpiRLrz2H9dLynA)

Comme le montre la figure ci-dessus, la clé privée de l'expéditeur est utilisée lors de la génération de la signature, et ainsi pour la vérification, la clé publique de l'expéditeur est utilisée.

### Mettons-nous au travail !

À des fins de démonstration, nous allons utiliser un message AS2 entrant vers AS2Gateway. Puisque nous nous concentrons uniquement sur la vérification de la signature dans cet article de blog, le message AS2 entrant ne sera ni chiffré ni compressé. Si vous souhaitez essayer cela avec le chiffrement, veuillez consulter mon article précédent sur le [déchiffrement d'un message AS2 avec OpenSSL](https://notebookbft.wordpress.com/2019/03/17/how-to-decrypt-an-as2-message-smime-with-openssl/).

#### Téléchargement du message brut et des en-têtes de transport

Une fois que nous avons reçu un message AS2, nous pouvons voir le message reçu dans la **vue de la boîte de réception** dans AS2Gateway comme indiqué ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/7k7b4aSuzNZ8eN109UJUbmhT8bG4ec36uC-n)

Ensuite, nous pouvons cliquer sur le sujet du message (dans ce cas, il s'agit de "Message signé d'exemple") pour accéder à la **vue détaillée** du message reçu comme indiqué ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/WqWJsiJo0MDxa9ptSkvvPAxyyacdrRLnmeHt)

Maintenant, vous pouvez cliquer sur le bouton **"Message brut"** et le bouton **"Télécharger les en-têtes de transport"** pour télécharger la charge utile du message AS2 non traitée et les en-têtes de transport que nous avons reçus du partenaire respectivement. Le message brut sera téléchargé dans un fichier nommé _message.raw_ et les en-têtes de transport seront téléchargés dans un fichier nommé _headers.raw_.

#### Obtention de la clé publique de l'expéditeur

Maintenant que nous avons le message brut et les en-têtes de transport, ce dont nous avons besoin ensuite est la clé publique de l'expéditeur. Nous pouvons la télécharger directement en cliquant sur le bouton **PEM** (violet) à partir de la vue des certificats (affichée ci-dessous) dans AS2Gateway.

![Image](https://cdn-media-1.freecodecamp.org/images/uqKUE36b9ic7TzzfBY1YrZArVk5KZVVXcL8P)

Avant de passer aux étapes suivantes, assurons-nous que nous avons tout ce dont nous avons besoin.

* Message brut (message.raw)
* En-têtes de transport (headers.raw)
* Clé publique de l'expéditeur (cert.pem)

#### Analyse des en-têtes de transport HTTP

Examinons d'abord les en-têtes de transport avant de continuer.

Comme vous pouvez le voir, il y a un ensemble d'en-têtes. Concentrons-nous uniquement sur quelques-uns importants dans le contexte de la vérification de la signature du message AS2.

* L'en-tête **content-type** suggère que nous avons une charge utile **multi-partie signée** dans la couche la plus externe et indique également que la **limite multi-partie** est désignée par la chaîne "------=_Part_1_1702144111.1552838995900" pour ce message AS2.
* Nous avons également la **version mime** à 1.0

Si vous souhaitez connaître plus de détails approfondis, le meilleur endroit pour commencer serait le [RFC AS2 4130](https://www.ietf.org/rfc/rfc4130.txt).

#### Analyse du message brut

Maintenant, examinons le message brut (message.raw). Selon l'en-tête de transport du type de contenu, nous savons déjà que la charge utile est une charge utile multi-partie signée. Nous pouvons le voir ci-dessous. Il y a deux parties (séparées par la chaîne de limite multi-partie comme indiqué dans l'en-tête de transport du type de contenu). L'une avec la charge utile originale (nous voyons la charge utile en texte brut puisque nous n'avons pas chiffré ou compressé la charge utile pour cette démonstration). L'autre avec la signature (**application/pkcs7-signature**).

#### Ajout des en-têtes requis

Vous vous souvenez que nous avons parlé de quelques en-têtes de transport importants lorsque nous avons examiné les en-têtes de transport ? C'est maintenant le moment de les utiliser. Nous devons ajouter ces en-têtes à notre fichier message.raw afin que le résultat final soit le suivant. (Prenons le nouveau fichier comme **message_with_headers.raw**) Notez que l'espace blanc entre les en-têtes de transport HTTP et la charge utile multi-partie signée est intentionnel.

### Vérification de la signature...

Il est temps d'exécuter la commande de vérification. Ici, nous utilisons l'outil **'smime'** d'OpenSSL.

```
openssl smime -verify -noverify -in message_with_headers.raw -signer cert.pem -out verified_payload.txt
```

Une fois que vous avez exécuté la commande, vous devriez obtenir un message indiquant **"Vérification réussie"**. La charge utile vérifiée sera dans le fichier verified_payload.txt. Notez que dans ce cas, nous obtiendrons la partie mime de la charge utile comme sortie, ce qui ressemblera à quelque chose comme suit.

Pour être complet, laissez-moi ajouter une note sur une erreur que j'ai rencontrée en essayant cela. Pour moi, la cause de cette erreur était une incompatibilité dans la chaîne de limite multi-partie dans l'en-tête de type de contenu avec la chaîne de limite multi-partie réelle. Notez qu'il y a **deux tirets précédents '—'** lorsque la limite multi-partie est utilisée dans une charge utile SMIME multi-partie.

```
Error reading S/MIME message 4719224428:error:0DFFF0D2:asn1 encoding routines:CRYPTO_internal:no multipart body failure:/BuildRoot/Library/Caches/com.apple.xbs/Sources/libressl/libressl-22.240.1/libressl-2.6/crypto/asn1/asn_mime.c:464:
```

Notez également que nous avons utilisé le paramètre **'-noverify'** dans la commande de vérification de la signature. Cela est dû au fait que les certificats que nous avons utilisés dans cette démonstration sont des certificats auto-signés. Si le paramètre '-noverify' n'est pas utilisé, OpenSSL essaiera de vérifier le certificat en premier et échouera en donnant une erreur similaire à ce qui suit.

```
Verification failure 4567594604:error:21FFF075:PKCS7 routines:func(4095):certificate verify error:/BuildRoot/Library/Caches/com.apple.xbs/Sources/libressl/libressl-22.240.1/libressl-2.6/crypto/pkcs7/pk7_smime.c:340:Verify error:self signed certificate
```

Super. La vérification de la signature est terminée. Même si nous avons examiné la vérification de la signature entièrement en utilisant des outils en ligne de commande dans cet article, cela peut également être fait en utilisant quelques lignes de code Java. J'espère en parler dans un futur article.

### Bonus

Avant de conclure, je voudrais partager quelques détails bonus qui vous aideront à identifier la cause de certains scénarios d'échec de vérification de signature. Le premier concerne la manière de trouver l'algorithme de signature utilisé.

#### Trouver l'algorithme de signature utilisé

Pour trouver l'algorithme de signature utilisé, nous pouvons utiliser l'outil **asn1parse** d'OpenSSL. Tout d'abord, nous devons séparer la partie signature sans les en-têtes mime dans un fichier séparé comme suit. Appelons ce fichier **signature.raw**

Maintenant, nous pouvons exécuter la commande suivante pour obtenir la sortie asn1parse.

```
openssl asn1parse -i -in signature.raw
```

La sortie serait la suivante. Si vous pouvez voir ci-dessous, la partie la plus externe a le type **pkcs7-signedData**, et après quatre ou cinq lignes, nous voyons **sha1** qui est l'algorithme de signature utilisé.

#### Plus de détails à partir de la sortie asn1parse

Il y a quelques détails supplémentaires que nous pouvons voir et comprendre à partir de la sortie asn1parse. Optionnellement, lors de la signature, les certificats de signature sont joints à la signature elle-même. C'est ce que vous voyez à partir de la section **pkcs7-data**. Le **"INTEGER : 438EFDF3"** est le numéro de série du certificat de signature. Vous pouvez également voir la période de validité du certificat comme indiqué ci-dessous.

**258:d=7 hl=2 l= 13 prim: UTCTIME :051201134315Z**  
**273:d=7 hl=2 l= 13 prim: UTCTIME :190810134315Z**

> _Les agents d'envoi DOIVENT encoder l'heure de signature jusqu'à l'année 2049 en tant que UTCTime. Les heures de signature en 2050 ou ultérieures DOIVENT être encodées en tant que GeneralizedTime. Les agents DOIVENT interpréter le champ année (YY) comme suit : si YY est supérieur ou égal à 50, l'année est interprétée comme 19YY ; si YY est inférieur à 50, l'année est interprétée comme 20YY._

> _Concernant UTCTime du RFC 2311 — [https://tools.ietf.org/html/rfc2311](https://tools.ietf.org/html/rfc2311)_

Dans ce cas, la période pendant laquelle le certificat est valide est du 1er décembre 2005 à 13:43:15 UTC au 10 août 2019 à 13:43:15.

Nous avons également l'heure de signature à l'attribut **signingTime** à 190317161000Z qui est le 17 mars 2019 à 16:10:00 UTC. Notez que lors de la validation de la signature, en plus de la correspondance du hachage du contenu, une autre vérification sera effectuée pour voir si la signature était valide lorsque le certificat était en cours de validité. En gros, au moment de la signature, le certificat doit être valide.

Avec un peu plus de connaissances sur la structure ASN.1, nous devrions être en mesure d'obtenir beaucoup plus d'informations à partir de cela. Il est temps pour moi de conclure. Santé ! 🍻

### Appel à l'action

* **Applaudir.** Appréciez et permettez aux autres de trouver cet article.
* **Commenter.** Partagez vos opinions sur cet article.
* **Suivez-moi.** [Rajind Ruparathna](https://medium.com/@rajindruparathna) pour recevoir des mises à jour sur des articles comme celui-ci.
* **Restez en contact.** [LinkedIn](http://lk.linkedin.com/in/rajind), [Twitter](https://twitter.com/rajindrj)

_Publié à l'origine sur [notebookbft.wordpress.com](https://notebookbft.wordpress.com/2019/03/19/how-to-verify-as2-message-smime-signature-with-openssl/) le 19 mars 2019._