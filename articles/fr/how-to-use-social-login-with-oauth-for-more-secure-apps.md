---
title: Comment utiliser la connexion sociale avec OAuth pour rendre vos applications
  plus sécurisées
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-10-29T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-social-login-with-oauth-for-more-secure-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/MzBKTcnJA.jpeg
tags:
- name: Application Security
  slug: application-security
- name: oauth
  slug: oauth
- name: Security
  slug: security
seo_title: Comment utiliser la connexion sociale avec OAuth pour rendre vos applications
  plus sécurisées
seo_desc: 'Many developers have written a demo login application at some point in
  time. We all start with the simple user defined ID and password. We then try to
  implement something like a social login with, say, Google or Twitter.

  There is, of course, a more c...'
---

De nombreux développeurs ont écrit une application de démonstration de connexion à un moment donné. Nous commençons tous avec un simple identifiant et mot de passe définis par l'utilisateur. Nous essayons ensuite d'implémenter quelque chose comme une connexion sociale avec, par exemple, Google ou Twitter.

Il y a, bien sûr, un processus plus complexe impliqué dans la configuration de la connexion sociale, mais pour un utilisateur, c'est aussi simple que de cliquer sur un bouton pour se connecter.

La facilité de ne pas avoir à se souvenir d'un identifiant/mot de passe et de pouvoir simplement s'inscrire/se connecter en cliquant sur un bouton est extrêmement bénéfique pour l'utilisateur.

## Et si je vous disais que c'était bien plus sécurisé ? 😉

Les connexions sociales nous aident vraiment à accomplir quelques choses :

* Support pour plusieurs appareils
* Connexion unique (Single Sign On)
* Simple à implémenter
* La capacité de partager des données pour les utilisateurs sans avoir à divulguer des informations personnelles
* Capacité de révoquer une session active, c'est-à-dire ne pas permettre à un tiers d'accéder à la connexion et aux données
* Il n'y a pas d'identifiants de longue durée échangés

## Alors, quelle technologie alimente la connexion sociale ? 🤔

Le protocole sous-jacent utilisé est quelque chose appelé [OAuth](https://oauth.net/). Il est défini comme :

> Un protocole ouvert pour permettre une autorisation sécurisée de manière simple et standardisée à partir d'applications web, mobiles et de bureau.

Maintenant, avec une compréhension de base de la connexion sociale et la définition ci-dessus, vous avez probablement une idée de la manière dont cela fonctionne – mais laissez-moi utiliser un exemple simple pour expliquer comment utiliser OAuth.

Je me souviens de mon ami [Sumedh](https://twitter.com/lunatic_monk) le décrivant comme une interaction entre une Mère, un Père et leur Fils. Imaginez que la mère veut des courses du marché et qu'elle veut que le fils les achète pour elle.

Avant d'entrer dans la conversation, laissez-moi établir un contexte.

> **Mère** : L'utilisateur de l'application

> **Fils** : Le client tiers ou, en termes techniques, le Client OAuth

> **Père** : Le Compte Social ou, en termes techniques, le Fournisseur OAuth

La conversation pourrait se dérouler comme suit :

> **Mère** : Hé fils, va au marché et rapporte-moi de la poudre de café. Prends l'argent nécessaire auprès de ton père.

> **Fils** : D'accord.

> *Le fils (client OAuth) va voir le père (fournisseur OAuth)*

> **Fils** : Hé papa, maman m'a dit de prendre de l'argent auprès de toi puisqu'elle veut des choses du marché.

> *Le père (fournisseur OAuth) demande à la mère (utilisateur) l'autorisation de donner de l'argent à leur fils (client OAuth)*

> **Père** : Hé, dois-je lui donner l'argent et combien ?

> *L'autorisation de votre application a lieu ici.*

> **Mère** : Oui, s'il te plaît, donne-le-lui.

> *Autorisation accordée par la mère (utilisateur)*

> *Le fils (client OAuth) obtient les choses nécessaires du marché et les rapporte à la mère (utilisateur). Ici, rapporter les choses à la mère (utilisateur) peut être considéré comme rediriger l'utilisateur (ou le connecter) vers le site tiers.*

Pour une compréhension plus technique de la manière dont cela fonctionne en code, [Richard Schneeman](https://twitter.com/schneems) a cette vidéo incroyable ci-dessous :

%[https://youtu.be/tFYrq3d54Dc]

## Maintenant, mettons tout cela en contexte

Prenons comme exemple [la communauté DEV](https://dev.to/). Si vous vouliez créer un compte sur la communauté DEV en utilisant Twitter, que se passerait-il ?

En gros, si le bouton "S'inscrire avec Twitter" existe, alors la configuration initiale entre le Client OAuth (Dev.to) et le Fournisseur OAuth (Twitter) est déjà faite.

Le Client déclenche une page d'octroi de permission pour le Fournisseur OAuth en fonction des informations d'identification qu'il reçoit de la configuration initiale. Cela ressemble à quelque chose comme ci-dessous :

![Page d'octroi de permission](https://cdn.hashnode.com/res/hashnode/image/upload/v1622980489496/IrLawupb6.png)

Une fois que vous vous connectez et accordez la permission, le Fournisseur OAuth vous redirige vers le client et le client obtient un jeton pour accéder à vos informations auprès du Fournisseur OAuth. Ce jeton d'accès permet au client d'obtenir des données spécifiques auprès du fournisseur.

Sur la base de ces données, le client crée ensuite un compte et vous connecte.

### Que se passe-t-il lors des connexions successives ?

C'est une bonne question. Maintenant, OAuth a plusieurs types d'octroi, et en fonction de cela, nous avons différentes manières d'obtenir un jeton d'accès auprès du Fournisseur OAuth.

Pour toutes les connexions ultérieures, le Client OAuth contactera le fournisseur et générera un nouveau jeton d'accès pour obtenir l'accès aux données et effectuer la connexion.

Ainsi, cela nous permet de réaliser la Connexion Unique, la capacité de partager des données pour les utilisateurs sans avoir à divulguer des informations personnelles, la capacité de révoquer l'accès et la capacité de ne pas échanger d'identifiants de longue durée.

Tout cela conduit à une expérience plus sécurisée.

## Conclusion

J'espère que ce court article de blog vous aide à comprendre pourquoi les connexions sociales sont plus sécurisées que l'option traditionnelle de nom d'utilisateur/mot de passe. Je vais écrire sur les différents types d'octroi OAuth à l'avenir et je fournirai également des exemples de code.

Merci d'avoir lu ! J'espère vraiment que vous trouvez cet article utile. Je suis toujours intéressé à connaître vos pensées et heureux de répondre à toutes les questions que vous pourriez avoir en tête. Si vous pensez que cet article était utile, veuillez le partager pour aider à promouvoir cet article auprès des autres.

Merci d'avoir lu ! :)

P.S. N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/rohitjmathew) ou [Twitter](https://twitter.com/iamrohitjmathew)