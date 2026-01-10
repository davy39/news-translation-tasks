---
title: Comment permettre aux utilisateurs de DApp de récupérer une clé privée perdue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-07T07:15:47.000Z'
originalURL: https://freecodecamp.org/news/solutions-for-private-key-management-in-decentralized-apps-d20b25c7474a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3GggWGvVHs4_tZ-8FyCPnA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment permettre aux utilisateurs de DApp de récupérer une clé privée
  perdue
seo_desc: 'By Pierre-Marie Riviere

  On Ethereum, private keys are used to access accounts, sign messages, etc. Once
  you lose access to your private key, you lose access to all funds stored with that
  account.

  How is that different from losing a credit card pin co...'
---

Par Pierre-Marie Riviere

Sur Ethereum, les clés privées sont utilisées pour accéder aux comptes, signer des messages, etc. Une fois que vous perdez l'accès à votre clé privée, vous perdez l'accès à tous les fonds stockés avec ce compte.

En quoi cela diffère-t-il de la perte d'un code PIN de carte de crédit ? Vous ne pouvez pas demander à la banque de vous donner un nouveau code, car la banque n'existe pas sur Ethereum. Vos fonds sont toujours crédités à votre adresse sur la blockchain, mais il n'y a aucun moyen pour vous de les retirer.

Les comptes et les services [DApp-] sur la blockchain Ethereum visent à être décentralisés, et personne ne conserve les codes d'accès en votre nom.

Un service stockant votre clé privée dans sa base de données pourrait accéder à vos fonds à tout moment — tout comme une banque — et cela va précisément à l'encontre de ce que la communauté Ethereum essaie d'accomplir.

**Alors, comment concilier l'appel d'Ethereum à la décentralisation et le besoin d'un utilisateur pour des services de support ?**

Pour les fournisseurs de services décentralisés, être des gardiens financiers a également de fortes implications légales. Un regard sur notre propre cas : The DApact construit une plateforme de Crédit-en-tant-que-Service au-dessus des agents de prêt existants dans les pays à faible revenu. Nous nous définissons comme une société de logiciels — une plateforme technologique plug-and-play pour les prêteurs locaux légalement enregistrés.

Avoir accès aux fonds des utilisateurs nous transformerait en fournisseur de services financiers plutôt qu'en société de logiciels, et cela impliquerait un examen par les régulateurs financiers locaux. Cela se traduirait éventuellement par l'obligation d'avoir une sorte de licence bancaire et un dépôt de capital dans chaque pays où The DApact est disponible.

Dans les services DApps purs, il n'y a absolument aucun moyen de récupérer l'accès à vos fonds une fois que vous avez perdu votre clé privée. Les utilisateurs doivent prendre soin de sauvegarder leur phrase de récupération dans un endroit sûr eux-mêmes. La méthode la plus efficace est de littéralement écrire la phrase de passe trois fois et de garder les copies papier dans différents endroits.

![Image](https://cdn-media-1.freecodecamp.org/images/8o69I8L-ItDZY4A5KNT4Bw3YBlsLRLma83A2)
_Pas une blague_

Certains utilisateurs tendent à perdre cette phrase de passe ou à ne pas la sauvegarder du tout dès le départ. Cela pose un problème significatif pour tous les développeurs de DApps, et spécifiquement pour The DApact, car nous traitons avec des populations qui n'ont souvent pas autant de connaissances en technologie. Par conséquent, des solutions de récupération doivent être disponibles pour nos utilisateurs.

Les utilisateurs doivent se voir proposer des solutions de récupération de clé privée adaptées à leur compréhension des systèmes décentralisés.

De telles solutions de récupération doivent respecter les trois critères suivants :

* **Externe** : Les fournisseurs de services décentralisés ne peuvent pas avoir accès à la clé privée.
* **Personnalisable** : Les utilisateurs doivent pouvoir comprendre et configurer les options de récupération même en cas de perte des clés privées.
* **Sécurisé** : Il ne doit pas y avoir de moyen facile de détourner le compte d'une autre personne via les options de récupération. Seule la personne possédant réellement le compte doit pouvoir le récupérer.

### Solutions existantes

Voici un aperçu des solutions mises en œuvre, renforcées ou explorées par les designers UX dans la communauté Ethereum, en commençant par les plus déployées.

#### Plusieurs propriétaires

Les portefeuilles MultiSig permettent de définir un nombre de propriétaires _n_. Si moins de _n_ propriétaires sont requis, les propriétaires restants pourraient remplacer un propriétaire en cas de perte d'accès. Cette solution, cependant, nécessite au moins 3 propriétaires ou appareils propriétaires (2 confirmations requises pour les transactions) et un fort degré de confiance entre les propriétaires.

#### Mnemonic

Un mnemonic (également appelé phrase de départ ou phrase de passe) est une série de mots qui peuvent dériver cryptographiquement une clé privée. Les utilisateurs doivent sauvegarder leur mnemonic de récupération eux-mêmes et s'assurer de le garder en sécurité afin de pouvoir régénérer leur clé privée en cas de perte.

Cette option de récupération est la norme pour les adresses et portefeuilles Ethereum actuellement. Les mnemonics sont devenus un mécanisme bien compris parmi les utilisateurs avancés de DApps, cependant, un utilisateur moins connaisseur devrait avoir différentes options. Les mnemonics sont aussi sécurisés que l'endroit où ils sont conservés. Écrite sur un morceau de papier, ils sont exposés au feu et aux inondations, au vol et à la détérioration.

#### Données biométriques

Une solution de choix pour l'industrie serait les données biométriques comme l'empreinte digitale, la reconnaissance de l'iris ou l'identification faciale. Les données biométriques ne peuvent pas être "perdues" comme les mots de passe sur un morceau de papier. Si Apple et Samsung investissent autant dans la biométrie, cela doit être une excellente solution, n'est-ce pas ?

Le problème avec cette option est que, une fois les données biométriques d'une personne exposées au public, il n'y a aucun moyen de sécuriser un compte avec celles-ci, car vous ne pouvez pas vraiment changer votre empreinte digitale comme vous pouvez changer un mot de passe ou un compte. Cette éventualité devient de plus en plus plausible alors que la reconnaissance faciale se généralise et qu'il existe même un [dépôt basé sur OpenCV disponible sur Github](https://github.com/ageitgey/face_recognition).

Un autre inconvénient de la biométrie est que différents capteurs d'empreintes digitales peuvent devenir assez flous et ne pas correspondre exactement — par exemple, si un utilisateur se coupe, il pourrait y avoir des problèmes.

#### Récupération sociale

Les utilisateurs pourraient déterminer un groupe d'amis qui sont autorisés à récupérer l'accès à leur compte en leur nom (c'est-à-dire que chacun d'eux détient une partie de la signature qui, combinée, donnerait accès au compte). Ce n'est que lorsque tous les amis sont d'accord que le propriétaire du compte est remplacé.

Le plus gros problème avec cette solution est que le groupe d'amis pourrait travailler ensemble et voler l'accès au compte du propriétaire même si le propriétaire ne leur a pas demandé. C'est pourquoi, idéalement, les membres du groupe ne devraient pas savoir qui d'autre fait partie du groupe.

Une sorte de solution de récupération sociale a été mise en œuvre avec succès par WeChat pour permettre la récupération de mot de passe : lorsque un utilisateur perd son mot de passe, WeChat lui demande de sélectionner des personnes dans sa liste de contacts parmi une grande liste de noms. Sachant que WeChat contient des informations bancaires sensibles, c'est définitivement une bonne piste pour les DApps.

#### Procédures KYC standard

De manière similaire à la façon dont les banques modernes effectuent des procédures KYC sur les nouveaux clients, les utilisateurs pourraient s'identifier auprès des fournisseurs KYC afin de retrouver l'accès à leurs fonds. Les utilisateurs devraient cependant effectuer la procédure une première fois pour la configurer afin que les fournisseurs connaissent l'identité derrière une adresse.

Cette solution a été utilisée pour les opérations de swap de tokens (par exemple, Nimiq). La vérification KYC est généralement gérée par des fournisseurs tiers comme IDnow, ce qui est coûteux et quelque peu contraire aux principes de la blockchain.

#### Preuve de paralysie

Ce nouveau concept est également connu sous le nom de _récupération par verrouillage temporel_ et _récupération de dernier recours_. En cas de perte d'accès à un compte, celui-ci peut être marqué comme tel. De plus, la personne qui le marque comme perdu peut y mettre un dépôt. Une période de temps commence après laquelle le compte est remplacé. Pendant cette période, le véritable propriétaire du compte pourrait prouver que le compte n'est pas réellement perdu en effectuant une transaction. Si c'est le cas, l'attaquant perd le dépôt qui est transféré au compte.

Alors que de plus en plus de designers entrent dans l'espace blockchain, il y a de l'espoir qu'un grand esprit trouvera le UX révolutionnaire pour la gestion des clés cryptographiques. Ou qui sait, peut-être que ce sera un historien du Moyen Âge qui apportera une vieille astuce de chevalier pour sécuriser l'or...

![Image](https://cdn-media-1.freecodecamp.org/images/SbW9ifyUTjchPGPL1Cc8tnK-wBbTtfby88pA)

Pour l'instant, un certain nombre de solutions (ou une combinaison de celles-ci) montrent un bon potentiel selon nos 3 critères (externalité, personnalisation, sécurité). Une fois que la communauté sera d'accord sur des solutions de récupération acceptables, un langage de conception commun et des meilleures pratiques standardisées devront être adoptés de manière cohérente dans tout l'écosystème afin que les utilisateurs de DApps s'habituent aux modèles de récupération.

[_The DApact_](https://www.dapact.org) _est un framework blockchain pour les opérations de microfinance._

_Vous pouvez nous suivre [sur Twitter](https://twitter.com/TheDapact) ou rejoindre [le Telegram](https://t.me/thedapact)_