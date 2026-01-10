---
title: Le guide absolument pas sarcastique pour concevoir pour le Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-26T15:56:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-for-the-web-in-2019
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1-HG5PTqPptU4IKFhrLu2j9w-1.jpeg
tags:
- name: satire
  slug: satire
- name: Web Design
  slug: web-design
seo_title: Le guide absolument pas sarcastique pour concevoir pour le Web
seo_desc: 'By Casper Beyer

  I’ve written about how to design for the modern web before, way back in 2018. But
  the web moves forward quickly so those guidelines are already obsolete and outdated,
  as more modern conventions have become mainstream.

  Let''s break down...'
---

Par Casper Beyer

J'ai déjà écrit sur la manière de concevoir pour le web moderne, en 2018. Mais le web évolue rapidement, si bien que ces directives sont déjà obsolètes et dépassées, car des conventions plus modernes sont devenues mainstream.

Décortiquons et passons en revue les principes de conception les plus importants pour concevoir pour le **web moderne en 2019**.

### Informez les utilisateurs que vous avez une application mobile

Celui-ci reste le principe le plus important et ce n'est pas sans raison. Des groupes de discussion bien rémunérés ont montré que la première chose qu'un utilisateur veut faire en visitant votre site web dans son navigateur est d'installer une application mobile.

La meilleure façon d'y parvenir est d'afficher une boîte de dialogue modale qui les invite à l'installer.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-N52LD7f0iAMB9-iPo496zA.png align="left")

En option, vous pouvez ajouter un bouton ou un hyperlien pour fermer ladite boîte de dialogue. Mais il est important d'utiliser un texte cryptique, de préférence formulé pour faire honte à l'utilisateur afin qu'il se conforme.

**Astuce** : Si vous n'avez pas d'application mobile réelle, vous pouvez simplement faire en sorte qu'un stagiaire emballe votre site web dans une webview avec la sécurité désactivée et livrer cela !

### Mettre en place une politique de non-suivi

De nombreux navigateurs modernes supportent aujourd'hui un en-tête HTTP appelé DNT, qui signifie Do Not Track. Cet en-tête est destiné à signaler qu'un utilisateur ne souhaite pas être suivi. Malheureusement, cela est activé par défaut dans certains navigateurs comme [Brave (Un navigateur open source bloquant les publicités créé par le créateur de JavaScript Brendan Eich)](https://brave.com/cas860).

Cependant, ne vous inquiétez pas, tout n'est pas perdu ! Nous avons constaté que la plupart des utilisateurs supprimeront cet en-tête lorsqu'on leur demandera de le faire. Afin de gérer cela, nous recommandons de servir un guide sur la manière de le désactiver lorsque l'en-tête est présent.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-Gfb0mEijJO5D263uDCZlRA.png align="left")

**Astuce** : Ne servez pas l'invite pour désactiver **DNT** sur le guide qui montre aux utilisateurs comment le désactiver, car le taux de conversion finit par être plutôt faible.

### Mettre en place une politique de cookies

Le consentement aux cookies est déroutant. Bien qu'il ne soit pas requis dans la plupart des cas, avec une utilisation raisonnable des cookies, il est préférable de demander le consentement de l'utilisateur afin que nous puissions tout suivre sans crainte de représailles.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-nje_74QVARVpyYXWjEqBkg.png align="left")

**Astuce** : Ne servez pas de pages sans cookies activés même lorsque nous n'en avons pas besoin. Cela signifie que nous pouvons suivre moins d'informations personnelles, ainsi nous avons moins d'informations utilisateur à vendre.

### Bloquer les bloqueurs de publicités

Les bloqueurs de publicités sont partout et peuvent vraiment nuire à vos marges, donc la précaution évidente à prendre est de bloquer les bloqueurs de publicités.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-Xzcqh2F2hYOnmu85f8lUSA.png align="left")

Chrome se dirige vers le blocage des bloqueurs de publicités, donc si l'utilisateur utilise un navigateur comme Brave, nous pourrons simplement prétendre que le navigateur de l'utilisateur n'est pas assez moderne.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-YdD82em4kZRVeYsMvHRQxg.png align="left")

**Astuce** : Ne parlez à personne de [Brave, le navigateur open source basé sur Chromium avec blocage des publicités intégré](https://brave.com/cas860).

### Bloquer les pays et appareils non américains

Entre les nations Cupcake, le GDPR, les taxes sur les liens et l'interdiction de Huwaei que nous n'avons pas réussi à comprendre du tout, la meilleure approche est de simplement les bloquer tous pour éviter toute responsabilité.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-kUODMQZJ7hSwkgviUdRGrA.png align="left")

**Astuce** : Vous pouvez...

### Maximiser votre mise en page

Les jours des mises en page de 800 pixels de large sont révolus. Les écrans modernes tendent à être larges, alors assurez-vous de tirer parti de toute la largeur dans la mise en page.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-gOOfNDipsZ7CWWfsIpi16A.png align="left")

**Astuce** : Des recherches ont montré que les boîtes de dialogue modales qui ne peuvent pas être fermées performant mieux.

### Utiliser les notifications

Les navigateurs modernes supportent les notifications, donc les activer est une nécessité. Mais en tant que solution de repli, abonnez également automatiquement l'utilisateur à une newsletter, des notifications SMS et/ou des notifications par email.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-gOOfNDipsZ7CWWfsIpi16A-1.png align="left")

**Astuce** : Utilisez ces notifications pour informer les utilisateurs lorsqu'une nouvelle version de l'application mobile est disponible.

### Invitez l'utilisateur

Parfois, les utilisateurs oublient qu'ils peuvent s'inscrire. Assurez-vous de les inviter régulièrement et mettez en avant un lien ou un bouton d'inscription bien visible.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-mzhgQidc4ThapURdDfRGyQ.png align="left")

**Astuce** : Invitez également l'utilisateur lorsqu'il est sur le point de quitter le site web ou lorsque son curseur quitte le site web.

### Permettre à l'utilisateur de se désinscrire

Il est très important que nous soyons conviviaux et que nous ne soyons pas intrusifs. Cela signifie que nous devons permettre aux utilisateurs de se désinscrire de nos invites constantes et de nos boîtes de dialogue modales.

La meilleure pratique ici est de placer les paramètres de désinscription à un endroit où l'utilisateur pourra facilement les repérer — généralement, cela se trouve dans l'une des pages de "préférences de compte".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-hUVWFANCpA4LXjJW4hx3Uw.png align="left")

### Utiliser JavaScript

C'est un fait connu, tous les sites web nécessitent JavaScript.

Bien que vous puissiez penser, "Oh, ce n'est que du texte brut et quelques modales." Mais dans le futur ? À ce moment-là, il y aura beaucoup plus de modales, et je vous le promets dès maintenant.

Lorsque cela se produira, vous regretterez de ne pas avoir fait de votre site web une application isomorphique utilisant le dernier framework fonctionnant sur un cloud serverless.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-Cmno6gxTMAdMXGqE1EksLA.png align="left")

**Astuce** : Ne rendez pas cette page avec JavaScript.

---

Pas encore développeur web ? Ne vous en faites pas - vous êtes déjà qualifié après avoir lu cet article.

Déjà un [développeur web ? Achetez le livre sur le langage de programmation C ici et **sortez tant que vous le pouvez encore** !](https://amzn.to/2OKhVsg)