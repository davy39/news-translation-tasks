---
title: Qu'est-ce que WebAuthn ? Comment authentifier les utilisateurs sans mot de
  passe
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2022-04-20T23:45:39.000Z'
originalURL: https://freecodecamp.org/news/intro-to-webauthn
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/webauthn.jpeg
tags:
- name: authentication
  slug: authentication
- name: passwords
  slug: passwords
seo_title: Qu'est-ce que WebAuthn ? Comment authentifier les utilisateurs sans mot
  de passe
seo_desc: 'Most of us are used to logging into different accounts using a password.
  For years this has been the norm. But passwords face a number of security issues:


  They are extremely annoying when we don’t remember them and even harder to reset

  They can be q...'
---

La plupart d'entre nous sommes habitués à nous connecter à différents comptes en utilisant un mot de passe. Depuis des années, c'est la norme. Mais les mots de passe posent un certain nombre de problèmes de sécurité :

* Ils sont extrêmement ennuyeux lorsque nous ne nous en souvenons pas et encore plus difficiles à réinitialiser
* Ils peuvent être assez peu sécurisés, le mot de passe le plus courant étant `password` ou `123456`
* Les attaques de phishing sont monnaie courante à l'ère d'Internet aujourd'hui, et en utilisant cette technique, les pirates peuvent voler vos mots de passe

Ne serait-il pas plus simple de passer à une connexion sans mot de passe ? Un endroit où nous n'avons pas à nous souvenir ou à entrer des mots de passe pour accéder à nos comptes ? Une telle solution sans mot de passe est WebAuthn.

## Qu'est-ce que WebAuthn ? 😅

L'API Web Authentication (également connue sous le nom de WebAuthn) est une API qui permet une authentification forte avec la cryptographie à clé publique. Elle vous permet de mettre en œuvre une authentification sans mot de passe et/ou une authentification sécurisée à deux facteurs sans messages SMS.

Décomposons cela pour comprendre rapidement les parties :

* **Cryptographie à clé publique**
—
Nous utilisons donc une authentification basée sur des clés (clé publique et clé privée) pour nous connecter et non un mot de passe. Si vous n'êtes pas sûr de son fonctionnement, je vous suggère de regarder cette [vidéo](https://youtu.be/6-JjHa-qLPk?t=277).
* **Authentification sans mot de passe**
—
Dans ce type d'authentification, nous n'utiliserons pas de mot de passe pour nous connecter, mais nous utiliserons une forme d'interaction utilisateur pour vérifier et nous connecter. Cela utilise un authentificateur matériel comme un capteur d'empreintes digitales sur votre appareil ou une YubiKey.
* **Authentification sécurisée à deux facteurs sans messages SMS**
—
L'authentification à deux facteurs aujourd'hui est principalement basée sur les OTP par SMS, mais ceux-ci sont également sensibles au swap de SIM. Le swap de SIM consiste essentiellement à prendre le contrôle du numéro de téléphone de quelqu'un et à tromper un opérateur pour le transférer sur un nouveau téléphone. Un scénario d'authentification à deux facteurs basé sur un authentificateur matériel utilisant WebAuthn serait une solution plus sûre au problème ci-dessus.

WebAuthn est une spécification écrite par le [W3C](https://www.w3.org/) et [FIDO](https://fidoalliance.org/), avec la participation de Google, Mozilla, Microsoft, Yubico, et d'autres.

Web Authentication fonctionne main dans la main avec d'autres normes industrielles telles que [Credential Management Level 1](https://www.w3.org/TR/credential-management-1/) et [FIDO 2.0 Client to Authenticator Protocol 2](https://fidoalliance.org/specs/fido-v2.0-rd-20170927/fido-client-to-authenticator-protocol-v2.0-rd-20170927.html).

## Comment fonctionne WebAuthn ? 🤔

Comme pour toute autre situation de connexion :

* Un utilisateur serait invité à entrer un nom d'utilisateur pour s'identifier.
* Le navigateur inviterait alors l'utilisateur à utiliser son authentificateur matériel et à se vérifier.
* En cas d'authentification réussie, il serait connecté au système.

Ce que nous ne voyons pas souvent, c'est ce qui se passe en arrière-plan pour faciliter ce processus. Laissez-moi expliquer un peu plus.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/webauthn_flow_diagram.png)
_Flux WebAuthn générique_

### Flux d'inscription

Dans ce processus, un nouvel ensemble d'identifiants de clé est créé pour le nom d'utilisateur entré par l'utilisateur. Cet identifiant de clé est le point central du processus qui nous permet de nous assurer que cette authentification est sans mot de passe.

Il y a un processus simple en 8 étapes qui a lieu :

1. Un utilisateur clique sur le bouton d'inscription sur un site dans son navigateur (agent utilisateur).
2. Le serveur d'authentification (partie fiable) émet un défi (un ensemble aléatoire de données envoyé sous forme de tableau) au navigateur de l'utilisateur pour pouvoir activer la connexion WebAuthn.
3. Le navigateur envoie ce défi à l'appareil authentificateur.
4. L'appareil authentificateur invite alors l'utilisateur à s'authentifier. Cela serait différent en fonction de l'appareil, par exemple, Touch ID sur un Macbook ou toucher une YubiKey.
5. Une fois que l'utilisateur autorise l'appareil authentificateur, l'authentificateur crée alors une nouvelle paire de clés (une clé publique et une clé privée) et utilise ensuite la clé privée pour signer le défi.
6. L'appareil authentificateur renvoie ensuite le défi signé, la clé publique ainsi que les détails relatifs au processus, au serveur d'authentification.
7. Le serveur d'authentification confirme ensuite l'authenticité de la clé privée en utilisant la clé publique pour s'assurer que le défi a été signé par la clé privée.
8. Il enregistre ensuite les détails reçus pour le nom d'utilisateur pour une utilisation future et répond que l'utilisateur est inscrit.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Registration.png)
_Flux d'inscription_

### Flux d'authentification WebAuthn

L'authentification est un processus similaire où les identifiants générés ci-dessus sont utilisés pour vérifier l'identité de l'utilisateur en passant par un processus de défi signé à nouveau.

Il y a un processus simple en 8 étapes qui a lieu :

1. Un utilisateur clique sur le bouton de connexion sur un site dans son navigateur (agent utilisateur) et entre son nom d'utilisateur.
2. Le serveur d'authentification (partie fiable) émet un défi (un ensemble aléatoire de données envoyé sous forme de tableau) au navigateur de l'utilisateur avec l'ID de la clé privée enregistrée avec le nom d'utilisateur.
3. Le navigateur envoie ce défi et l'ID de la clé privée à l'appareil authentificateur.
4. L'appareil authentificateur invite alors l'utilisateur à s'authentifier. Cela serait différent en fonction de l'appareil (à nouveau, Touch ID sur un Macbook ou toucher une YubiKey).
5. Une fois que l'utilisateur autorise l'appareil authentificateur, l'authentificateur récupère alors la paire de clés générée enregistrée sur celui-ci avec l'ID de la clé privée fourni. Il utilise ensuite la clé privée pour signer le défi.
6. L'appareil authentificateur renvoie ensuite le défi signé ainsi que les détails relatifs au processus au serveur d'authentification.
7. Le serveur d'authentification confirme ensuite l'authenticité de la clé privée en utilisant sa clé publique enregistrée pour s'assurer que le défi a été signé par la clé privée.
8. Il connecte ensuite l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Login.png)
_Flux d'authentification_

## Avantages de WebAuthn

Cela semble génial, n'est-ce pas ? 😮 Absolument. Voyons rapidement quelques-uns des avantages :

* **Authentification basée sur les clés privée/publique**
—
C'est une méthode plus sécurisée pour authentifier les utilisateurs par rapport à la norme actuelle de l'authentification basée sur les mots de passe, car elle utilise la cryptographie asymétrique par défaut.
* **Résistant au phishing**
—
WebAuthn est résistant aux attaques de phishing grâce au nom de domaine stocké sur l'authentificateur. Cela rend plus difficile pour les pirates de pouvoir usurper des sites Web et d'accéder aux identifiants.
* **Stocker les données publiques dans votre base de données**
—
Seules les données publiques sont stockées dans la base de données. Aucune donnée sensible telle que les mots de passe ne doit être stockée dans ce flux.
* **Contrôle granulaire**
—
Vous pouvez contrôler le type d'interaction utilisateur que vous souhaitez dans le cadre du flux, par exemple un appareil matériel spécifique.
* **Meilleure UX**
—
Un utilisateur n'aura pas besoin de se souvenir de mots de passe ou autres et devra uniquement utiliser un authentificateur matériel pour pouvoir se connecter à l'appareil.
* **Recommandation du W3C**
—
Cela signifie qu'il devrait être supporté par tous les principaux navigateurs sur tous les appareils.

et enfin **PLUS DE MOTS DE PASSE.**

### Inconvénients de WebAuthn

Tout cela étant dit, il présente quelques problèmes qui restent à résoudre :

* **Gestion des identifiants utilisateur**
—
L'expérience utilisateur en matière de gestion des identifiants est encore dans un état très primitif.
* **Identifiants multi-appareils**
—
Pouvoir transférer des identifiants d'un appareil à un autre n'est pas très facile, sauf si vous utilisez un authentificateur matériel itinérant comme une YubiKey.
* **Récupération de l'appareil authentificateur perdu/volé**
—
Au cas où vous n'auriez pas accès ou perdriez votre authentificateur matériel itinérant, le scénario de repli est généralement un mot de passe pour accéder à un compte, mais il faudrait le configurer explicitement.
* **WebAuthn pourrait remplacer les mots de passe**
—
WebAuthn est encore dans une phase très précoce et est lentement adopté et supporté. Il pourrait remplacer la connexion basée sur les mots de passe à l'avenir, mais cela pourrait prendre un certain temps avant que nous ne le voyions se produire.

Note
—
Cela ne remplace pas des choses comme les flux d'authentification basée sur les jetons comme OAuth ou OIDC ou les fournisseurs d'identité comme Auth0, Okta, Google, et autres.

## Conclusion

WebAuthn est un flux d'authentification beaucoup plus sécurisé que l'utilisation d'un simple mot de passe. Il est résistant au phishing et ne stocke que les données publiques dans une base de données, la plupart des données privées étant généralement stockées uniquement sur l'authentificateur matériel.

Il utilise la cryptographie asymétrique pour effectuer une vérification de l'utilisateur et offre une bien meilleure UX par rapport au flux de connexion existant.

Actuellement, WebAuthn est principalement utilisé comme authentification à deux facteurs ou flux de facteur universel secondaire. Mais il pourrait éventuellement remplacer la connexion basée sur les mots de passe à l'avenir.

J'espère que cet article vous aide à comprendre ce qu'est WebAuthn et comment il fonctionne.

Merci d'avoir lu ! J'espère vraiment que vous trouverez cet article utile. Je suis toujours intéressé à connaître vos pensées et heureux de répondre à toutes les questions que vous pourriez avoir en tête. Si vous pensez que cet article était utile, veuillez le partager pour que d'autres puissent le voir également.

N'hésitez pas non plus à me contacter sur [LinkedIn](https://www.linkedin.com/in/rohitjmathew) ou [Twitter](https://twitter.com/iamrohitjmathew).