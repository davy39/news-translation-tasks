---
title: L'avenir des systèmes de paiement numérique — Google Tez et Audio Quick Response
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-25T02:36:15.000Z'
originalURL: https://freecodecamp.org/news/google-tez-and-audio-quick-response-the-future-of-digital-payment-systems-9ae3485c7128
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SRMpLrweLP-mrzjgEl4FYg.jpeg
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: Google
  slug: google
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: L'avenir des systèmes de paiement numérique — Google Tez et Audio Quick
  Response
seo_desc: 'By Vaidic Joshi

  Google recently marked its entry into the Indian digital payments market by introducing
  the payment app Tez (Hindi for fast). Since the demonetization of the Indian currency
  last year, India has seen a tremendous increase in the numbe...'
---

Par Vaidic Joshi

Google a récemment marqué son entrée sur le marché indien des paiements numériques en introduisant l'application de paiement [**Tez**](https://en.wikipedia.org/wiki/Google_Tez) (rapide en hindi). Depuis la démonétisation de la monnaie indienne l'année dernière, l'Inde a connu une augmentation considérable du nombre d'applications et de solutions de paiement numérique.

Presque toutes les banques, les entreprises de commerce électronique et les principaux fournisseurs de télécommunications disposent d'une ou plusieurs applications prenant en charge les paiements numériques et les portefeuilles électroniques.

Alors, qu'est-ce qui rend [Google Tez](https://en.wikipedia.org/wiki/Google_Tez) différent ?

C'est là que la solution basée sur **AQR** de Google Tez semble prometteuse. Les utilisateurs peuvent échanger des informations de compte de manière sécurisée en utilisant l'audio pour initier une transaction. Et la transaction **peut être effectuée avec un appareil qui dispose simplement d'un microphone et d'un haut-parleur.**

![Image](https://cdn-media-1.freecodecamp.org/images/DNazKRax5sqHwgrXWbsYBOtdTmtFo5eoOI1c)

Les systèmes de paiement numérique existants utilisent une ou plusieurs des technologies suivantes pour échanger des informations de compte lors de transactions.

* **QR** (**Q**uick **R**esponse) codes
* **UPI** ( [**U**nified **P**ayments **I**nterface](http://www.npci.org.in/UPI_Background.aspx) )
* **NFC** ( **N**ear **F**ield **C**ommunication )

C'est là que Google Tez utilise une nouvelle alternative, les codes QR basés sur l'audio (**AQR**).

Pour comprendre cela, examinons les limitations de ces solutions de paiement numérique.

Les solutions basées sur **NFC** **nécessitent un matériel spécial** qui prend en charge les communications en champ proche. Ainsi, les utilisateurs avec un téléphone basique ne peuvent pas l'utiliser.

Les solutions basées sur **UPI** sont un succès. Cependant, le point de douleur réside dans le processus de configuration long. De plus, l'UPI est **étroitement lié à la banque sous-jacente** qui détient votre compte, donc vous pourriez vous retrouver avec une adresse UPI par compte. En outre, les utilisateurs doivent taper leur UPI à chaque fois qu'une transaction est effectuée (ce qui, pour des personnes comme moi, est trop fastidieux à faire ?).

Les solutions basées sur **QR** sont les plus populaires et semblent être le moyen le plus facile d'initier une transaction. Tout ce que l'on a à faire est de scanner un code QR. Cependant, encore une fois, les solutions basées sur les codes QR nécessitent **des appareils avec des caméras** et sont vulnérables aux attaques de **attagging**.

?C'est là que l'**AQR** de Google Tez semble prometteur. L'audio est utilisé pour démarrer la transaction. Son meilleur argument de vente est que les transactions peuvent être complétées avec un simple appareil qui dispose simplement d'un microphone et d'un haut-parleur — et n'est-ce pas ce à quoi ressemblaient les téléphones il y a une décennie ?

Oui et non. Il existe des applications et des solutions d'échange de données basées sur l'audio. En voici deux :

* [Chirp](https://www.chirp.io/), qui fournit des données via des solutions sonores
* L'application [Shuttl](https://vimeo.com/181485272), qui fournit des cartes d'embarquement audio et est basée sur Chirp

En fait, nous avons une solution de paiement basée sur l'audio par [ToneTag](http://tonetag.com/). [Infosys](https://www.infosys.com/) a récemment annoncé son partenariat avec ToneTag pour des solutions numériques basées sur l'audio. (Une autre raison de croire que les solutions de paiement basées sur l'audio sont l'avenir. ?)

L'utilisation de l'audio pour générer des codes QR semble être nouvelle. (Je n'ai pas encore rencontré de solution existante. Veuillez me corriger si je me trompe.?)

![Image](https://cdn-media-1.freecodecamp.org/images/JFMV133KrxJta5RMqWBhmviavBprPxLjol0i)
_Appariement d'appareils basé sur AQR_

**AQR** permet à deux appareils proches de s'apparier en utilisant le son. Google Tez utilise AQR pour les transferts de paiement en mode cash.

L'application utilise l'audio **ultrasons** pour apparier les appareils. Un audio aléatoire est enregistré, mélangé, chiffré, puis transmis en courtes rafales en utilisant les haut-parleurs de l'appareil. L'autre appareil capture ces rafales audio en utilisant son microphone, puis déchiffre l'audio pour obtenir les données nécessaires à l'appariement.

AQR est censé être plus sécurisé que les codes QR. De plus, Google utilise son réseau pour détecter les activités frauduleuses.

Au moment de la rédaction de cet article, il n'existe aucune documentation officielle sur la manière dont les AQR sont créés, chiffrés et déchiffrés. Examinons comment ToneTag utilise l'audio pour effectuer des transactions de paiement sécurisées. La solution de paiement basée sur l'audio de ToneTag utilise les méthodes suivantes pour garantir des paiements audio sécurisés :

L'appareil échange d'abord des données audio dynamiques pour effectuer une poignée de main basée sur l'audio. Cela s'appelle la **tokenization**. Une fois la poignée de main réussie, les données sont encodées en ondes sonores, qui peuvent ensuite être transférées via les haut-parleurs d'un téléphone. Les données sont chiffrées et disposent d'un mécanisme de détection d'erreurs intégré. Ces données chiffrées sont ensuite échangées et permettent aux appareils de s'apparier les uns avec les autres. Pour compléter la transaction, un [mot de passe à usage unique](https://en.wikipedia.org/wiki/One-time_password) (OTP) et une authentification basée sur un code PIN sont nécessaires.

Avec Google Tez et Infosys s'associant à ToneTag, il semble que nous soyons entrés dans une nouvelle ère de paiements numériques basés sur l'audio.

Puisque l'application Google Tez utilise la fréquence des ultrasons pour AQR, l'application pourrait ne pas fonctionner avec les téléphones qui ne disposent pas de haut-parleurs ou de microphones à ultrasons. L'application affirme prendre en charge tous les smartphones.

**Publié à l'origine sur [vedify.in](https://vedify.in/is-audio-the-future-of-digital-payment-systems-google-tez-and-aqr-audio-qr-63cf3c0aaaa7) le 25 septembre 2017.**