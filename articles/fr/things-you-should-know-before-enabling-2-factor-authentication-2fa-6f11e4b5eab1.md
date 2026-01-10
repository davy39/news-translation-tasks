---
title: Ce que vous devez savoir avant d'activer l'authentification à deux facteurs
  (2FA)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-17T17:13:46.000Z'
originalURL: https://freecodecamp.org/news/things-you-should-know-before-enabling-2-factor-authentication-2fa-6f11e4b5eab1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2blNOZ7xEYZbq7px1K1lOg.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: passwords
  slug: passwords
- name: Security
  slug: security
- name: technology
  slug: technology
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: Ce que vous devez savoir avant d'activer l'authentification à deux facteurs
  (2FA)
seo_desc: 'By Nitin Sharma

  With Cybersecurity becoming a big concern, two-factor authentication (2FA) is a
  topic that is becoming hotter with each passing day.

  After all, who doesn’t want to keep their private data safe? Two-factor authentication
  may not be a b...'
---

Par Nitin Sharma

Avec la cybersécurité devenant une préoccupation majeure, l'authentification à deux facteurs (2FA) est un sujet qui devient de plus en plus populaire chaque jour.

Après tout, qui ne veut pas garder ses données privées en sécurité ? L'authentification à deux facteurs peut ne pas être une solution infaillible, mais c'est l'une des méthodes les plus faciles et les meilleures pour renforcer votre sécurité virtuelle.

**Considérez l'authentification à deux facteurs comme un complément aux mots de passe forts, et non comme un remplacement.**

L'authentification à deux facteurs ajoute une couche de sécurité supplémentaire au processus de connexion, réduisant ainsi les risques de piratage de votre compte. Connaître et entrer votre mot de passe ne suffit pas, car il y a une deuxième couche, généralement sensible au temps. Cela rend le processus beaucoup plus sécurisé.

Voici quelques faits que vous voudrez connaître avant d'activer l'authentification à deux facteurs :

#### Quatre violations de données sur cinq pourraient être évitées en utilisant le 2FA

Les menaces cybernétiques sont en hausse et l'authentification à deux facteurs aide réellement à les contrer.

La majorité des violations liées au piratage se produisent en raison de mots de passe faibles ou volés. Comme de nombreux utilisateurs tendent à utiliser le même mot de passe partout, le risque est décuplé. Clairement, quelque chose de plus que des mots de passe est nécessaire.

Selon un [rapport de Verizon sur les violations de données](http://www.verizonenterprise.com/resources/reports/rp_data-breach-investigations-report-2013_en_xg.pdf), 80 % des violations de données pourraient être éliminées par l'utilisation de l'authentification à deux facteurs.

Le 2FA garantit que même si votre mot de passe est compromis, le pirate doit craquer une autre couche de sécurité avant de pouvoir accéder à votre compte. Et comme la plupart des méthodes 2FA sont dépendantes du temps, cela rend le travail du pirate beaucoup plus difficile.

Il n'est donc pas surprenant que tous les grands sites web et banques proposent une option pour activer la sécurité à deux facteurs.

#### L'authentification à deux facteurs n'est pas un remplacement pour les mots de passe forts

Les mots de passe faibles et répétés sont un fléau pour la cybersécurité. Peu importe le compte ou le service que vous utilisez, il est toujours préférable de définir un mot de passe complexe et unique.

L'utilisation de mots de passe répétés sur tout l'Internet nous rend vulnérables à des impacts massifs même si la sécurité d'un seul site est compromise. Dans un tel cas, tous nos comptes peuvent être à la disposition de l'attaquant.

Même si vous activez l'authentification à deux facteurs, des mots de passe forts sont indispensables. Comme mentionné précédemment, traitez le 2FA comme un complément aux mots de passe forts, et non comme un remplacement.

Utilisez toujours une combinaison complexe de lettres, de chiffres et de symboles spéciaux pour générer un mot de passe fort et unique pour chaque service que vous utilisez. Vous pouvez également utiliser un service comme [LastPass](https://www.lastpass.com/) pour gérer facilement vos mots de passe.

![Image](https://cdn-media-1.freecodecamp.org/images/MgQT70g6WFU4xfJ6Ce5-OuuTvLDXmOckpiLD)
_Facebook est l'une des principales entreprises soutenant l'authentification à deux facteurs._

#### Il existe deux façons d'obtenir les codes d'accès

Vous pouvez générer les codes d'accès pour le 2FA de plusieurs manières. Les codes peuvent être générés sur le serveur puis envoyés par e-mail, SMS ou appel téléphonique. Cela nécessite généralement une connectivité réseau pour votre mobile et peut ainsi vous rendre vulnérable à des comptes inaccessibles dans des zones reculées.

L'autre option consiste à générer le code d'accès hors ligne sur votre téléphone ou un appareil matériel. Vous pouvez facilement générer des codes d'accès 2FA sur votre téléphone via des applications comme Google Authenticator, Authy ou TOTP Authenticator. Il existe également des appareils matériels comme YubiKey disponibles sur le marché pour configurer l'authentification à deux facteurs.

Cette méthode est plus robuste car aucune connectivité de données n'est requise, vous rendant ainsi moins vulnérable au phishing réseau.

Dans certains cas, la deuxième étape peut également être une vérification biométrique ou l'entrée d'un code PIN que vous avez défini vous-même précédemment.

#### Faites toujours des sauvegardes. Vous ne voulez pas être bloqué hors de votre compte

Le 2FA fonctionne sur le principe que vous avez toujours accès au code d'accès secondaire. Mais si vous utilisez une application d'authentification à deux facteurs et que vous perdez votre téléphone ou que vos données sont effacées, vous pouvez être bloqué hors de votre compte.

Pour éviter un tel scénario, certains sites web fournissent des codes de sauvegarde que vous devez enregistrer en toute sécurité et que vous pouvez utiliser dans de telles situations. Alternativement, vous pouvez utiliser une application d'authentification qui offre la possibilité de sauvegarder votre clé de sécurité et les données associées.

Nous avons développé l'application TOTP Authentication pour iOS et Android en gardant cela à l'esprit. L'application vous permet de sauvegarder votre clé de sécurité et les informations associées soit sur votre appareil, soit sur des options de stockage en ligne telles que Google Drive de manière simple. Le fichier de sauvegarde chiffré peut être configuré sur un autre appareil en quelques clics. Vous pouvez télécharger l'application depuis l'iTunes Store [ici](https://itunes.apple.com/us/app/totp-authenticator/id1404230533?mt=8), et depuis le Google Play Store [ici](https://play.google.com/store/apps/details?id=com.authenticator.authservice2).

#### Conclusion

L'authentification à deux facteurs devient lentement une norme dans le monde numérique. La plupart des banques, des services de stockage en nuage et des sites web de médias sociaux proposent déjà cette option. Vous devriez activer le 2FA partout où c'est possible. Comme on dit, mieux vaut prévenir que guérir.

Vous avez des questions sur l'authentification 2FA ? Posez-les dans les commentaires !

Pour en savoir plus sur l'authentification à deux facteurs, vous pouvez également consulter [cet article](https://hackernoon.com/what-is-2-factor-authentication-and-why-you-should-care-e8af5808d499).