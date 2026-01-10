---
title: 'Comment danser l''OAuth : une leçon étape par étape'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T19:08:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-dance-the-oauth-a-step-by-step-lesson-fd2364d89742
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eTlZtD7s7bWMGaa0P4anvA.jpeg
tags:
- name: data
  slug: data
- name: oauth
  slug: oauth
- name: Security
  slug: security
- name: technology
  slug: technology
- name: user experience
  slug: user-experience
seo_title: 'Comment danser l''OAuth : une leçon étape par étape'
seo_desc: 'By Anabella Spinelli

  Most of the times I try to learn something new and put it into practice, I quickly
  start to feel like I’m lost in a myriad of dance moves. I’m desperately trying to
  find the right way to do things, while not really understanding ...'
---

Par Anabella Spinelli

La plupart du temps, lorsque j'essaie d'apprendre quelque chose de nouveau et de le mettre en pratique, je me sens rapidement perdue dans une myriade de pas de danse. Je tente désespérément de trouver la bonne façon de faire les choses, sans vraiment comprendre ce qui se passe ou comment je me suis retrouvée du mauvais côté de la pièce...

J'essaie simplement des choses jusqu'à ce que quelque chose fonctionne.

Peut-être est-ce dû à ma façon d'apprendre, ou peut-être que les guides et tutoriels sont destinés à des personnes plus expérimentées ou techniques. Mais, après avoir compris le sujet, je me dis toujours qu'il devrait y avoir un guide simple pour comprendre les concepts clés **et** les appliquer plus facilement dans un projet.

Alors cette fois, j'ai décidé d'arrêter de souhaiter et de le faire moi-même, en utilisant la dernière chose que j'ai apprise.

Et cette chose était OAuth 2.0.

### Qu'est-ce que l'OAuth ?

Commençons par les bases : OAuth signifie **Open Authorization**. C'est un processus par lequel une application ou un site web peut accéder à des données privées d'un utilisateur depuis un autre site web.

Ce dernier site agit généralement comme un **fournisseur d'identité** de confiance. Il donne à l'application demandante certaines informations de base sur vous afin que l'application puisse créer un profil. Ainsi, vous n'avez pas à remplir un formulaire d'inscription ennuyeux et à gérer un autre mot de passe ?

Vous avez déjà utilisé cela au moins un milliard de fois, en fait, vous l'avez utilisé chaque fois que vous avez cliqué sur « Se connecter avec Facebook / Google / GitHub / ... ». Ensuite, vous avez vu un écran de consentement affichant les informations de votre profil (disons) Facebook que vous autorisez **ce-nouveau-site-super.com** à lire (et parfois, écrire). Après cela, comme **ce-nouveau-site-super.com** fait confiance à l'identité fournie par Facebook, ils peuvent créer un profil pour vous dans leur base de données en utilisant les données reçues.

La communication entre **ce-nouveau-site-super.com** et Facebook s'arrête généralement ici. C'est pourquoi votre photo de profil ne changera pas partout sur Internet si vous la modifiez sur Facebook. Ils ne retournent jamais sur Facebook pour demander des données mises à jour.

### Quand les rythmes de la marimba commencent à jouer...

Il y a une autre raison de construire ce type de mécanisme, avec beaucoup plus de potentiel : utiliser le fournisseur d'identité comme un **fournisseur de services** (de manière continue). Cela signifie communiquer avec lui régulièrement pour fournir des fonctionnalités améliorées à vos utilisateurs.

Un bon exemple de cela est [**Relive**](https://www.relive.cc/), un service qui se connecte à différentes applications de suivi sportif pour créer des vidéos de vos courses ou balades. Chaque fois que vous terminez une activité, Relive vous propose de créer une vidéo. Si vous acceptez, ils la traitent et vous avertissent lorsqu'elle est prête pour le partage sur les réseaux sociaux ?

Il n'y a vraiment aucune différence technique entre ces deux usages. C'est pourquoi **vous devriez être prudent** quant à l'endroit où vous vous connectez avec votre compte de réseau social ou Google/Gmail.

Cela peut sembler effrayant, mais il n'y a vraiment rien à craindre. Gardez simplement à l'esprit que vous autorisez **ce-nouveau-site-super.com** à accéder aux informations vous concernant, détaillées dans l'écran de consentement, potentiellement de manière récurrente. Soyez conscient des permissions que vous accordez et assurez-vous de savoir comment les désactiver lorsque vous ne faites plus confiance.

Par exemple, si vous utilisez votre compte Google pour accéder à **ce-nouveau-site-super.com** mais ne souhaitez plus l'autoriser, allez simplement dans les [paramètres de votre compte Google](https://myaccount.google.com/security#connectedapps) et désactivez leur accès.

Tous les principaux fournisseurs d'identité offrent un contrôle sur cela.

### Très bien, mais comment danse-t-on l'OAuth ?

Avant que vous arriviez sur **ce-nouveau-site-super.com** et même cliquiez sur « Se connecter avec `VotreFournisseurDIdentitePrefere` », quelqu'un — probablement un développeur — doit créer une application sur le site du fournisseur.

C'est une façon d'enregistrer **ce-nouveau-site-super.com** afin que, plus tard, le fournisseur sache qui demande des données privées.

À cette étape, le développeur configurera certaines informations sur l'application, comme le nom ou le site web de l'application et — surtout — **une URI de redirection**. Le fournisseur (comme Google ou Facebook) l'utilisera pour contacter l'application demandante et lui dire que l'utilisateur a dit _oui_ ?

![Image](https://cdn-media-1.freecodecamp.org/images/-ZNoydoRCuDXAntqiAdKG9MVmuTjLk7qpOtW)
_Je vous promets que vous n'aurez pas à l'écrire à la main, nous sommes fiers de notre absence de papier._

Une fois l'application enregistrée, le fournisseur donnera à **ce-nouveau-site-super.com** un **clientId** et un **clientSecret** qui seront utilisés dans les communications entre eux. Ils fonctionnent un peu comme un nom d'utilisateur et un mot de passe pour l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/Nc8EUZy8o8w-5QddAogfWj2SifjW9Qh5OZWh)
_Vous obtiendrez le clientID et le clientSecret juste après avoir cliqué sur Enregistrer l'application._

Il est très important de garder votre clientSecret dans un endroit sécurisé et de ne pas le partager avec des inconnus. Si quelqu'un y accède, il pourrait demander des données privées d'utilisateurs au fournisseur en votre nom, et les utiliser à des fins malveillantes !

Nous ne voulons pas cela.

#### Mains sur les hanches ou les épaules

En plus de configurer toutes ces choses, le développeur doit découvrir quel type de données le fournisseur donne accès et comment elles sont segmentées.

Ces « segments » sont connus sous le nom de **scopes** et ils définissent les droits d'accès, généralement séparés en catégories de lecture/écriture. Par exemple, **ce-nouveau-site-super.com** peut demander les scopes « **profile:read** » et « **contacts:read** ». Cela signifie qu'ils peuvent lire tout ce que le fournisseur assigne aux segments « profile » et « contacts ». D'autres choses ne seront pas accessibles, par exemple vos publications ou le contenu que vous aimez.

Pour simplifier, disons que **ce-nouveau-site-super.com** est un site web qui s'intègre avec [**Typeform**](https://www.typeform.com/), un service pour créer des formulaires intelligents et esthétiques, et aussi l'entreprise pour laquelle je travaille. Vous voulez absolument faire partie de la dernière tendance, alors sur leur site web, vous cliquez sur « Se connecter avec Typeform » pour passer directement à l'action. Qu'est-ce qui suit ?

Voici un diagramme fait maison, organique et sans cholestérol à utiliser comme carte pour tout cela. Cela peut sembler un peu compliqué, mais ne vous inquiétez pas, nous examinerons chaque étape ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/EieGAKMEfd4kumthtdBGcXE7rUq4xsvo8i15)
_Les notes colorées apportent de la joie à mon cœur._

### Autoriser : la première étape de la danse OAuth

Vous prenez l'initiative et cliquez sur « Se connecter avec Typeform ». Ici, ce-nouveau-site-super.com (_THNA_ à partir de maintenant, car je suis fatiguée d'écrire des mots séparés par des tirets) vous enverra à l'endpoint d'autorisation de Typeform (`/oauth/authorize`) et fournira :

* leur clientId (rappelez-vous, c'est le **nom d'utilisateur** de **THNA**)
* leurs scopes souhaités (ou droits d'accès)
* et leur URI de redirection à nouveau (Typeform la connaît déjà depuis la configuration initiale, mais nous l'envoyons à nouveau comme une couche de sécurité supplémentaire)

Cette URL ressemblera à quelque chose comme ceci :

```
https://api.typeform.com/oauth/authorize?client_id=yourClientId&scope=accounts:read+forms:read+results:read
```

Typeform utilisera ces informations pour générer un écran de consentement où vous pouvez vérifier les types de choses que vous autorisez **THNA** à voir et à faire.

![Image](https://cdn-media-1.freecodecamp.org/images/istIyX0juNBgdwBXW2-y-sAzMhnOgkF1sY0R)

Une fois que vous avez **lu attentivement ce à quoi vous consentez** et cliqué joyeusement sur « Autoriser », Typeform vous enverra à l'URI de redirection avec un code temporaire, comme ceci :

```
https://ce-nouveau-site-super.com/auth/redirect?code=xxxXXXxxxXXXxxx
```

### Token : il faut être deux pour danser le tangOAuth ?

Tous ces allers-retours donnent l'impression que quelqu'un vous fait tourner comme dans un tango, n'est-ce pas ?

La deuxième étape de la danse OAuth est lorsque **THNA** reçoit ce code et l'échange contre un **jeton OAuth**.

Ainsi, **THNA** prend ce code et le renvoie à Typeform, avec l'URI de redirection (oui, encore !), et le secret client (c'est le mot de passe de l'application !).

En récompense d'une danse bien exécutée, **THNA** recevra un jeton OAuth brillant ✨ qu'il pourra utiliser pour interagir avec Typeform au nom de l'utilisateur, c'est-à-dire... vous !

#### Restez avec moi, balancez-vous avec moi

Désormais, dans chaque requête que _THNA_ fait à Typeform en votre nom, ils devront inclure un en-tête **Authorization** avec ce jeton d'accès. Avec celui-ci, Typeform (ou tout autre fournisseur) peut identifier :

* qui demande les données (dans ce cas, **THNA**)
* à qui appartiennent les données (vous !)
* et également s'assurer qu'ils ont l'**autorisation** correcte pour accéder à ces données (uniquement ce à quoi vous avez consenti).

### Prêt pour la piste de danse ?

Maintenant que vous connaissez tous les pas et les tours de la technique de danse OAuth, vous devriez être prêt à créer vos propres chorégraphies, je veux dire, intégrations, et rendre Internet un endroit encore plus génial.

Dessins par moi-même, photo de couverture par [Gez Xavier Mansfield](https://unsplash.com/photos/I_mkJxsx8kA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).