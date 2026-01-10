---
title: Comment Apple Pay fonctionne sous le capot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T06:29:56.000Z'
originalURL: https://freecodecamp.org/news/how-apple-pay-works-under-the-hood-8c3978238324
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zsr_ysZ5bNXXnzdC0LHY6w.jpeg
tags:
- name: Apple
  slug: apple
- name: iphone
  slug: iphone
- name: mobile
  slug: mobile
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment Apple Pay fonctionne sous le capot
seo_desc: 'By Dumindu Buddhika

  Do you use Apple Pay? Have you ever wondered how an Apple Pay transaction goes through?
  In this post, you will learn how Apple Pay works end to end.

  Mobile payments have become very popular due to the convenience and the security
  ...'
---

Par Dumindu Buddhika

Utilisez-vous Apple Pay ? Vous êtes-vous déjà demandé comment une transaction Apple Pay se déroule ? Dans cet article, vous apprendrez comment Apple Pay fonctionne de bout en bout.

Les paiements mobiles sont devenus très populaires en raison de la commodité et de la sécurité qu'ils offrent. Plus besoin de cartes en plastique à transporter, et vous n'avez pas à vous soucier de les perdre (quel soulagement !).

Dans cet article, je vais discuter de la manière dont Apple Pay fonctionne en général et comment il fonctionne lorsqu'il est utilisé à un terminal de point de vente physique, spécifiquement. Je parlerai également brièvement des avantages en matière de sécurité.

Avant de plonger dans le sujet, familiarisons-nous avec quelques termes de base.

#### Élément Sécurisé

Un élément sécurisé (SE) est quelque chose qui est mentionné lorsqu'on parle d'Apple Pay, nous devons donc comprendre ce que c'est.

Selon [Global Platform](https://www.globalplatform.org/mediaguideSE.asp) :

> Un Élément Sécurisé (SE) est une plateforme résistante aux manipulations (généralement un microcontrôleur sécurisé à une puce) capable d'héberger de manière sécurisée des applications et leurs données confidentielles et cryptographiques (par exemple, la gestion des clés) conformément aux règles et exigences de sécurité établies par un ensemble d'autorités de confiance bien identifiées.

Apple Pay utilise le SE pour stocker les informations secrètes associées aux cartes tokenisées (nous en parlerons plus tard).

Dans les iPhones après l'iPhone 6, et dans l'Apple Watch, un SE est intégré dans la puce de communication en champ proche (NFC) de l'appareil. Cela est utilisé aux terminaux de paiement pour effectuer des transactions via NFC. Le SE émule une carte de paiement lors d'une transaction Apple Pay.

#### Tokenisation

La tokenisation en tant que processus est de plus en plus adoptée dans l'industrie des paiements. Ici, nous allons essayer de comprendre les bases de la tokenisation.

Voici une description concise de Wikipedia sur la technologie de tokenisation :

> La **tokenisation**, lorsqu'elle est appliquée à la sécurité des données, est le processus de substitution d'un élément de données sensible par un équivalent non sensible, appelé jeton, qui n'a aucune signification ou valeur extrinsèque ou exploitable. Le jeton est une référence (c'est-à-dire un identifiant) qui mappe les données sensibles via un système de tokenisation. Le mappage des données originales à un jeton utilise des méthodes qui rendent les jetons impossibles à inverser en l'absence du système de tokenisation.

Dans le contexte des cartes de crédit et d'Apple Pay, la **tokenisation** est utilisée pour remplacer le numéro de compte principal (PAN, ou le numéro de carte de crédit) par un jeton. Un jeton ressemble à un numéro de carte de crédit normal, mais ce n'est pas le PAN original. La tokenisation empêche le numéro de carte original d'être utilisé lors des transactions.

Les jetons n'ont aucune signification par eux-mêmes et sont sans valeur pour les criminels si un jeton est volé. Il n'existe aucun algorithme pour déduire le numéro de compte principal si vous avez un jeton. Cela rend impossible pour les criminels de rétro-concevoir le numéro de compte principal à partir d'un jeton.

Cliquez [ici](https://en.wikipedia.org/wiki/Tokenization) pour l'article Wikipedia sur la tokenisation si vous souhaitez en savoir plus.

Le diagramme suivant décrit le flux de transaction d'Apple Pay. Nous allons discuter de ces étapes une par une dans les sections suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/Tvs9gM2jDlgnFkUqWnw7f7bE1YG4DsYEsJah)
_ymedialabs.com_

### Ajout d'une Carte à Apple Pay

![Image](https://cdn-media-1.freecodecamp.org/images/C4FQQR5WKo8KpyiLxfG3tvmsLRwiaOv6h5ny)
_[http://www.iphoneincanada.ca](http://www.iphoneincanada.ca" rel="noopener" target="_blank" title=")_

Une carte peut être ajoutée à Apple Pay soit en scannant la carte, soit en soumettant les informations de la carte. Ces informations sont ensuite envoyées aux serveurs d'Apple.

Apple envoie les informations de la carte reçues au réseau de cartes concerné (Visa, MasterCard, AmericanExpress, Discover, etc.). Le réseau de cartes valide ensuite les informations de la carte avec la banque émettrice.

Après la validation, le réseau de cartes, agissant en tant que [TSP](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269) (Token Service Provider), crée un jeton (appelé DAN ou Device Account Number dans le contexte d'Apple Pay) et une clé de jeton. Ce DAN est généré en utilisant la tokenisation et n'est pas le numéro de carte réel.

Ensuite, ces informations sont renvoyées aux serveurs d'Apple. Une fois que l'appareil reçoit ces informations des serveurs d'Apple, elles sont enregistrées dans l'élément sécurisé (SE) de l'appareil.

### Initiation d'une Transaction avec Apple Pay

![Image](https://cdn-media-1.freecodecamp.org/images/fzP2zrOr4FBQoNSAervf20OXqrWoeIHJhZHi)
_support.apple.com_

Lorsque vous utilisez votre appareil Apple à un terminal de point de vente pour effectuer un paiement, l'appareil communique avec le terminal pour initier une transaction. Apple Pay utilise la spécification [sans contact](https://www.emvco.com/emv-technologies/contactless/) d'EMVCO pour communiquer avec le terminal. Si le terminal ne prend pas en charge le sans contact EMV, Apple Pay revient en mode sans contact MSD (magnetic stripe data).

#### Mode sans contact EMV

Lorsque le mode sans contact EMV est utilisé, l'appareil Apple communique avec le terminal selon la spécification [sans contact](https://www.emvco.com/emv-technologies/contactless/) d'EMV. L'élément sécurisé de l'appareil génère un **cryptogramme dynamique** pour chaque transaction en utilisant le jeton, la clé de jeton, le montant et d'autres informations liées à la transaction. Ce cryptogramme dynamique est ensuite envoyé au processeur de paiement avec le jeton (DAN), le montant de la transaction et d'autres informations requises pour traiter la transaction.

#### Mode sans contact MSD

Le mode sans contact MSD existe pour supporter les terminaux qui ne sont pas encore capables de traiter en mode sans contact EMV. La plupart des terminaux fonctionnent encore en mode sans contact MSD. Examinons de plus près comment une transaction se déroule en utilisant le mode sans contact MSD.

MSD, ou Magnetic Stripe Data, est la manière dont les anciennes cartes stockent les détails de la carte. Les données sont stockées sous forme de **pistes** dans les cartes à bande magnétique. Les cartes à bande magnétique peuvent avoir jusqu'à 3 pistes, et chaque piste (piste1, piste2, piste3) a un format différent. Veuillez cliquer [ici](https://en.wikipedia.org/wiki/ISO/IEC_7813) pour plus d'informations sur les données de piste.

En mode sans contact MSD d'Apple Pay, le format de données de piste2 est utilisé pour transférer les données de la carte au processeur de paiement qui communique ensuite avec le réseau de cartes.

Examinons quelques exemples de données de piste envoyées d'un terminal au processeur pour une transaction Apple Pay.

370295292756481=220672716078290600047

![Image](https://cdn-media-1.freecodecamp.org/images/06Uue0GUDG01OBeKpoIeOHee0WRnfRdPm-mP)

Ci-dessus, un exemple de données de piste reçues d'un terminal qui a été capturé à une passerelle de paiement.

Comprenons ces données segment par segment,

* Surligné en jaune - Il s'agit du Device Account Number ou DAN (Le DAN de l'exemple ici provient d'une carte AmericanExpress. Vous pouvez valider le numéro d'identification bancaire (BIN), ou les 6 premiers chiffres du numéro de carte de crédit, [ici](https://www.bincodes.com/bin-checker/) ).
* Surligné en bleu - Il s'agit de l'année et du mois d'expiration de la carte de crédit (aa/mm)
* Surligné en rose - Il s'agit du code de service. Cliquez [ici](https://atlassian.idtechproducts.com/confluence/display/KB/Credit+Card+Service+Code+Chart++) pour en savoir plus à ce sujet.
* Surligné en violet - Cette partie des données est à la discrétion du réseau de cartes. Dans le cas d'Apple Pay, cela est utilisé comme une **valeur de vérification de carte dynamique (CVV).**

Nous avons appris que dans le mode EMV, un **cryptogramme dynamique** est généré. Ici, le **CVV dynamique** joue le rôle du cryptogramme. Cela est généré en utilisant la clé de jeton et d'autres données liées à la transaction (similaire à la génération d'un **cryptogramme dynamique**).

Les données de piste montrées ci-dessus sont envoyées à l'[acquéreur](https://en.wikipedia.org/wiki/Acquiring_bank) avec le montant de la transaction. L'acquéreur transmet ces informations au réseau de cartes concerné (Visa, MasterCard, etc.) en fonction du [BIN](https://www.investopedia.com/terms/b/bank-identification-number.asp).

### Achèvement d'une Transaction Apple Pay

Lorsque le réseau de cartes reçoit la demande de transaction, il identifie s'il s'agit d'un numéro de carte réel ou d'un numéro de carte tokenisé. Si c'est tokenisé (ce qui est le cas pour les transactions Apple Pay), le réseau de cartes valide le cryptogramme (ou CVV dynamique) en utilisant leur copie de la **clé de jeton** (le réseau de cartes agit en tant que [TSP](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269) ici).

Après quelques validations supplémentaires, le réseau de cartes détokenise le DAN et obtient le PAN original (numéro de compte principal).

Cette demande de transaction est envoyée à l'[émetteur](https://www.thebalance.com/credit-card-issuer-959984) (la banque ou l'institution financière qui a émis la carte de crédit) avec le PAN original. L'émetteur autorise la transaction et envoie la réponse qui atteint finalement le terminal de point de vente.

Hourra ! Transaction terminée !

![Image](https://cdn-media-1.freecodecamp.org/images/QLw4aphNtbO5blklWMB-m9S2UsU5XWY7d63z)
_support.apple.com_

### Rejeu des Demandes de Transaction

L'un des plus grands problèmes avec les transactions par carte traditionnelles est la capacité de rejouer les demandes de transaction passées ([attaque par rejeu](https://en.wikipedia.org/wiki/Replay_attack)). Si vous renvoyez la même demande de transaction, une autre transaction serait effectuée avec les mêmes données.

Avec Apple Pay, cela ne se produit pas (également lorsque vous utilisez des cartes EMV directement sur le terminal). Chaque demande de transaction ne peut être utilisée qu'une seule fois. Le cryptogramme dynamique (CVV dynamique en mode MSD) garantit cela. Pour chaque transaction, un nouveau cryptogramme est généré qui ne peut être utilisé qu'une seule fois (et n'est valable que pour une certaine période de temps).

### Conclusion

Dans cet article, nous avons passé en revue le flux de transaction d'Apple Pay. Je discuterai de Google Pay dans un prochain article.

#### Références

* [http://www.gmarwaha.com/blog/2015/01/03/apple-pay-an-attempt-to-demystify-take-2/](http://www.gmarwaha.com/blog/2015/01/03/apple-pay-an-attempt-to-demystify-take-2/)
* [https://www.emvco.com/emv-technologies/contactless/](https://www.emvco.com/emv-technologies/contactless/)
* [http://msrtron.com/blog-headlines/blog-card-data](http://msrtron.com/blog-headlines/blog-card-data)
* [https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269)

#### Avant de partir !

Si vous avez apprécié cet article, les applaudissements sont les bienvenus !