---
title: Comment déchiffrer un message AS2 (SMIME) avec OpenSSL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-17T08:33:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-decrypt-an-as2-message-smime-with-openssl-d47fda5fd7db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxwl0_gdFfhnpXeh8RozCA.jpeg
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
seo_title: Comment déchiffrer un message AS2 (SMIME) avec OpenSSL
seo_desc: 'By Rajind Ruparathna

  I have been involved in the AdroitLogic AS2Gateway, a SaaS B2B AS2 messaging platform
  for almost two years now. One of the common issues we see in the users who are getting
  started with AS2 is decryption failure. In this blog pos...'
---

Par Rajind Ruparathna

Je suis impliqué dans [AdroitLogic AS2Gateway](http://as2gateway.com/), une plateforme SaaS de messagerie B2B AS2 depuis presque deux ans maintenant. L'un des problèmes courants que nous rencontrons chez les utilisateurs qui commencent avec AS2 est l'échec du déchiffrement. Dans cet article de blog, nous allons examiner ce que sont le chiffrement et le déchiffrement dans le protocole AS2. Nous allons couvrir comment déchiffrer un message AS2 et quelques conseils pour identifier la cause de certains échecs de déchiffrement.

### Chiffrement dans le protocole AS2

Le protocole AS2 utilise principalement la **cryptographie à clé publique** ou **cryptographie asymétrique** pour le chiffrement. Là, la clé publique du destinataire est utilisée pour le chiffrement et la clé privée du destinataire est utilisée pour le déchiffrement comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ldcGxyCd6CjjIYhokAZHzg.png)

En supposant que la clé privée du destinataire n'a pas été compromise, le chiffrement des données et des messages offre les avantages de sécurité suivants.

* **Confidentialité** — Assure que seul le destinataire prévu peut déchiffrer et voir le contenu, c'est-à-dire que le contenu est chiffré avec la clé publique du destinataire. Par conséquent, il ne peut être déchiffré qu'avec la clé privée du destinataire.
* **Intégrité des données** — Détermine si le fichier ou les données reçus par le destinataire ont été altérés en cours de route. Une partie du processus de déchiffrement consiste à vérifier que le contenu du message chiffré original et le nouveau contenu déchiffré correspondent. Le moindre changement dans le contenu original entraînerait l'échec du processus de déchiffrement.

### Mettons-nous au travail !

À des fins de démonstration, nous utiliserons un message AS2 entrant vers AS2Gateway. Puisque nous nous concentrons uniquement sur le déchiffrement dans cet article de blog, le message AS2 entrant n'est ni signé ni compressé.

#### Téléchargement du message brut et des en-têtes de transport

Une fois que nous avons reçu un message AS2, nous pouvons voir le message reçu dans la **vue de la boîte de réception** dans AS2Gateway comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m_BskqHI_adR8UYuRgVmhA.png)

Ensuite, nous pouvons cliquer sur le sujet du message (dans ce cas, il s'agit de « Sample Encrypted Message ») pour accéder à la **vue détaillée** du message reçu comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NZL6lkKno6oIwoaCdI33QA.png)

Maintenant, vous pouvez cliquer sur le bouton **« Raw Message »** et le bouton **« Download Transport Headers »** pour télécharger respectivement la charge utile du message AS2 non traitée et les en-têtes de transport que nous avons reçus du partenaire. Le message brut sera téléchargé dans un fichier nommé message.raw. Les en-têtes de transport seront téléchargés dans un fichier nommé headers.raw.

#### Obtention de la clé publique et privée du destinataire

Maintenant que nous avons le message brut et les en-têtes de transport, nous avons besoin des clés publique et privée du destinataire. En ce qui concerne la clé publique, vous pouvez la télécharger directement en cliquant sur le bouton **PEM** (violet) à partir de la vue des certificats (affichée ci-dessous) dans AS2Gateway. Pour la clé privée, vous devrez d'abord télécharger le JKS (identity.jks). Vous faites cela en cliquant sur le bouton **JKS** (rouge) à partir de la vue des certificats et en extrayant la clé privée du JKS. Consultez mon [guide étape par étape](https://notebookbft.wordpress.com/2019/01/10/extracting-private-key-from-java-keystore-jks/) sur l'extraction de la clé privée du JKS pour plus de détails.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jlG2mJOTDZSqX11Wueixjg.png)

Notez que vous aurez besoin du mot de passe de la clé et du mot de passe du magasin de clés lors de l'extraction de la clé privée. Si vous ne vous en souvenez pas, vous pouvez consulter plus de détails sur le certificat en cliquant sur le **nom commun** (dans ce cas, le nom commun sur la station AS2 pertinente pour cette démonstration est « RJ_LOCAL »). À partir de là, vous devriez pouvoir trouver les mots de passe pertinents.

Avant de poursuivre avec les étapes suivantes, assurons-nous que nous avons tout ce dont nous avons besoin en place.

* Message brut (message.raw)
* En-têtes de transport (headers.raw)
* Clé privée du destinataire (private_key.pem)
* Clé publique du destinataire (cert.pem)

#### Analyse des en-têtes de transport HTTP

Examinons d'abord les en-têtes de transport avant de continuer.

Comme vous pouvez le voir, il y a un ensemble d'en-têtes et ainsi nous allons nous concentrer uniquement sur quelques-uns importants dans le contexte du déchiffrement du message AS2.

* L'en-tête **content-type** suggère que nous avons une charge utile chiffrée dans la couche la plus externe.
* L'en-tête **content-disposition** révèle le nom de fichier de la charge utile comme étant test_message.txt.
* Nous avons également la **version MIME** à 1.0

Si vous êtes intéressé à connaître des détails plus approfondis, le meilleur endroit pour commencer serait le [AS2 RFC 4130](https://www.ietf.org/rfc/rfc4130.txt).

Maintenant, nous savons que la charge utile est chiffrée (ce qui devrait être le cas puisque c'est le type que nous avons sélectionné pour cette démonstration). Nous savons que le nom de fichier est test_message.txt. Super. Maintenant, nous avons presque tout ce dont nous avons besoin pour effectuer le déchiffrement. Encore quelques étapes à suivre.

#### Encodage du message brut en Base64

Puisque nous travaillons avec un message brut chiffré ici, il est toujours préférable de le convertir en base64 afin que nous puissions le manipuler en toute sécurité à l'aide d'éditeurs de texte. Bien sûr, on peut et devrait être en mesure de procéder sans le convertir en base64 également. Je préfère convertir le message brut en base64 pour plus de commodité dans les étapes suivantes. Exécutons la commande suivante (ici nous utilisons l'outil de ligne de commande **'base64'**) pour convertir le message brut en base64. Notez qu'il est très important d'avoir le paramètre '--break=64' qui divise la sortie base64 en lignes de 64 caractères, sinon vous pourriez rencontrer une erreur lors du déchiffrement.

```
base64 message.raw --break=64 > base64_message.raw
```

À partir de maintenant, nous travaillerons sur le fichier base64_message.raw.

#### Ajout des en-têtes requis

Vous vous souvenez que nous avons parlé de quelques en-têtes de transport importants lorsque nous avons examiné les en-têtes de transport ? C'est le moment de les utiliser. Nous devons ajouter ces en-têtes à notre fichier base64_message.raw afin que la sortie finale soit comme suit. (Prenons le nouveau fichier comme **base64_message_with_headers.raw**). Notez que l'espace blanc entre les en-têtes et la charge utile encodée en base64 est intentionnel. Vous pourriez remarquer qu'en plus des en-têtes dont nous avons parlé précédemment, nous avons ajouté **'content-transfer-encoding: base64'** pour indiquer que le contenu est en base64.

### Déchiffrement...

Il est temps d'exécuter la commande de déchiffrement. Ici, nous utilisons l'outil **'smime'** d'OpenSSL.

```
openssl smime -decrypt -in base64_message_with_headers.raw -recip cert.pem -inkey private_key.pem >> test_message.txt
```

Une fois que vous avez exécuté la commande, vous devriez avoir la sortie dans le fichier test_message.txt. Notez que dans ce cas, nous obtiendrons la sortie en texte brut puisque nous avons utilisé une charge utile sans compression ni signature.

```
This is a test message for the demonstration of AS2 decryption by OpenSSL.
```

Comme je l'ai mentionné précédemment, si la sortie base64 n'est pas divisée en lignes de 64 caractères, vous pourriez obtenir une erreur similaire à celle qui suit. J'ai pensé à l'ajouter pour être complet afin que quiconque rencontre ce problème puisse trouver la solution ici.

Cela conclut les étapes de déchiffrement de la charge utile. Même si nous avons examiné le déchiffrement entièrement à l'aide d'outils de ligne de commande dans cet article, cela peut également être fait avec quelques lignes de code Java. J'espère en parler dans un futur article.

### Bonus

Avant de conclure, je voudrais partager quelques détails bonus qui vous aideront à identifier la cause de certains scénarios d'échec de déchiffrement. Le premier concerne la façon de trouver l'algorithme de chiffrement utilisé.

#### Trouver l'algorithme de chiffrement utilisé

Afin de trouver l'algorithme de chiffrement utilisé, nous pouvons utiliser l'outil **asn1parse** d'OpenSSL. Exécutons la commande suivante pour obtenir la sortie asn1parse. (Notez que si vous exécutez la commande sans le paramètre 'inform der', vous pourriez obtenir une erreur comme 'Error: offset too large')

```
openssl asn1parse -inform der -in message.raw
```

La sortie serait comme suit. Si vous pouvez voir ci-dessous, il y a environ deux parties principales affichées ici en [notation ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One) comme partie **pkcs7-envelopedData** et partie **pkcs7-data**. Dans la partie pkcs7-data, nous avons **'des-ede3-cbc'** qui est l'algorithme de chiffrement utilisé.

#### Trouver la clé publique utilisée pour le chiffrement

Le pack bonus n'est pas encore terminé ;-). Parfois, il est important de déterminer le certificat utilisé dans le chiffrement pour s'assurer que l'expéditeur a utilisé la bonne clé publique du destinataire. Si vous regardez la **sortie asn1parse** ci-dessus, vous devriez voir que nous avons **commonName**, **organizationName**, etc. dans la section **pkcs7-envelopedData**. Ce sont les détails du certificat utilisé pour chiffrer la charge utile AS2.

Maintenant, après l'entrée **countryName**, vous pourriez voir une ligne comme suit.

**122:d=9 hl=2 l= 4 prim: PRINTABLESTRING :None**  
**128:d=6 hl=2 l= 6 prim: INTEGER :01627AE13D2D**

Ceci est le numéro de série du certificat en hexadécimal et avec cela, vous pouvez vérifier si la bonne clé publique a été utilisée lors du chiffrement.

Cela conclut le pack bonus. Puissent tous vos échecs de déchiffrement AS2 disparaître. 😊

### Appel à l'action

* **Applaudissez.** Appréciez et permettez aux autres de trouver cet article.
* **Commentez.** Partagez vos opinions sur cet article.
* **Suivez-moi.** [Rajind Ruparathna](https://medium.com/@rajindruparathna) pour recevoir des mises à jour sur des articles comme celui-ci.
* **Restez en contact.** [LinkedIn](http://lk.linkedin.com/in/rajind), [Twitter](https://twitter.com/rajindrj)

_Publié à l'origine sur [notebookbft.wordpress.com](https://notebookbft.wordpress.com/2019/03/17/how-to-decrypt-an-as2-message-smime-with-openssl/) le 17 mars 2019._