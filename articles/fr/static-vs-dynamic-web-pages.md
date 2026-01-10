---
title: Pages Web Statiques vs Dynamiques – Quelle est la Différence ?
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-11T19:54:10.000Z'
originalURL: https://freecodecamp.org/news/static-vs-dynamic-web-pages
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/staticdynamic.png
tags:
- name: interview questions
  slug: interview-questions
- name: Web Development
  slug: web-development
- name: website development,
  slug: website-development
seo_title: Pages Web Statiques vs Dynamiques – Quelle est la Différence ?
seo_desc: 'Imagine that you''re interviewing for your dream job and the interviewer
  drops this question for you:

  “So can you distinguish between a static web page and a dynamic web page?”

  What would your reaction be?

  If you don’t know the answer to that question...'
---

Imaginez que vous passez un entretien pour le travail de vos rêves et que l'intervieweur vous pose cette question :

*"Alors, pouvez-vous distinguer une page web statique d'une page web dynamique ?"*

Quelle serait votre réaction ?

Si vous ne connaissez pas la réponse à cette question, ou si vous avez du mal à y penser, alors cet article est fait pour vous.

Si vous êtes un codeur débutant, vous avez peut-être entendu parler des termes "pages web statiques" et "pages web dynamiques" – mais vous ne savez peut-être pas ce qu'ils signifient.

Vous vous demandez peut-être ce qui rend une page web statique et ce qui rend une page web dynamique.

Dans cet article, je vais vous dire tout ce que vous devez savoir – et pourquoi c'est important. Et, comme d'habitude, je le ferai en anglais simple.

## Qu'est-ce qu'une Page Web ?

Tout d'abord, nous devons comprendre ce qu'est une page web et un site web et comment ils diffèrent. Pour cela, considérons une encyclopédie.

Une encyclopédie (comme Wikipedia, par exemple) se compose de nombreuses pages. Chaque page a son propre contenu : un en-tête, un paragraphe, des images, des diagrammes, des puces, des listes, et bien sûr, les définitions des termes que vous recherchez.

Il est très courant dans une encyclopédie de trouver des mots sur la page qui renvoient (ou lient) à une autre page pour des informations supplémentaires.

Cela est très similaire aux pages web et aux sites web.

Une page web est un document unique qui peut contenir du texte, des images, de l'hypertexte ou tout autre élément. Nous créons des pages web en utilisant un langage de balisage tel que le HyperText Markup Language – plus communément connu sous le nom de HTML.

L'hypertexte est tout document web qui contient des hyperliens. Un hyperlien est tout élément de la page web qui, lorsque vous cliquez dessus, vous lie à une autre page web.

Ces pages web interconnectées forment un réseau organisé de pages web, que nous appelons alors un **site web**.

Chaque page web accessible sur Internet doit avoir sa propre URL. Voici une URL typique d'une page web :

[`www.freecodecamp.org/news`](http://www.freeCodeCamp.com/news)

> N/B : Au cas où vous vous poseriez la question, la page que l'URL ci-dessus retourne est une page dynamique. Ne vous inquiétez pas, nous allons découvrir ce que cela signifie très bientôt.

**Maintenant, j'ai un simple test pour vous :**

Ouvrez votre navigateur web. Allez à la barre d'adresse et tapez (ou sélectionnez) une URL aléatoire mais valide que vous connaissez. Appuyez sur Entrée et attendez. Une page web sera rendue sur votre fenêtre de navigateur. Prenez une capture de l'état actuel de la page web et fermez-la.

Attendez un certain temps, puis visitez à nouveau cette URL. Ensuite, répondez aux questions suivantes :

* Si vous comparez l'état actuel de la page à son état précédent, y a-t-il des différences dans son contenu ?

* L'URL de la page se termine-t-elle par une extension de document (par exemple, `/.html`) ou se termine-t-elle par un point de terminaison ? (par exemple, `/profile`)

* En supposant que vous changiez les paramètres de votre navigateur (comme effacer les cookies, par exemple), le fait de taper la même URL retourne-t-il une page différente ?

* Êtes-vous invité à soumettre un formulaire avant que la page ne soit rendue sur votre navigateur ?

La manière dont vous répondez à ces questions (et à quelques autres que je poserai ci-dessous) déterminera si la page est statique ou dynamique.

## Qu'est-ce qu'une Page Statique ?

Une page statique a les caractéristiques suivantes :

* La page est déjà présente même avant qu'un utilisateur ne la demande. Une page statique doit être déjà physiquement présente et hydratée (c'est-à-dire avec du contenu) au moment où un utilisateur en fait la demande. Si elle n'est pas présente, alors elle n'est pas statique.

* La page conserve généralement le même contenu chaque fois que l'utilisateur la demande. Si le fait de taper la même URL retourne un contenu différent, alors cette page n'est pas du tout statique. Cela ne signifie pas que les pages statiques ne peuvent pas être modifiées. Mais la seule façon de changer une page statique est que le créateur modifie manuellement le contenu (comme un document HTML).

Voici un exemple de page statique :

`www.example.com/about.html`

## Qu'est-ce qu'une Page Dynamique ?

Une page dynamique a les caractéristiques suivantes :

* La page n'est pas physiquement présente sur le serveur lorsque l'utilisateur en fait la demande.

* Au lieu de cela, lorsqu'un utilisateur fait une demande, un script ou un programme s'exécute et finit par créer une page web. Il le fait en interagissant avec une base de données pour récupérer des données qu'il emballe et envoie en tant que page.

* À chaque demande, chaque nouvelle page créée peut être différente de la précédente.

Cela est dû au fait que la page créée dépend des informations de l'utilisateur et du programme. Le créateur n'a pas à modifier manuellement le contenu, comme avec les Pages Web Statiques.

Ainsi, par exemple, si un utilisateur différent demande la même page, un contenu différent est retourné.

Ou peut-être lorsque l'utilisateur change un paramètre, une nouvelle page est retournée.

Ou peut-être lorsque l'heure change, un contenu différent est retourné.

Pour illustrer cela de manière plus intuitive, examinons deux scénarios dans un restaurant :

*Vous avez faim, alors vous décidez d'aller dans un restaurant pour manger. Vous commandez une assiette de riz Jollof (un plat nigérian). À travers la vitre transparente de la cuisine, vous pouvez voir que la nourriture est déjà cuite. Tout ce que le serveur a à faire est d'aller là-bas, de prendre le repas et de vous l'apporter.*

*Maintenant, disons que vous commandez une assiette de suya (viande nigériane). Typiquement, la viande n'est pas déjà disponible et doit être préparée pour vous sur place. Avec les informations que vous fournissez au serveur (votre budget, combien d'oignons vous voulez, etc.), le cuisinier prépare votre portion pour vous.*

Le premier scénario illustre comment une page statique est rendue. Le second scénario illustre comment une page dynamique est rendue.

Voici un exemple de page dynamique :

`www.example.com/courses`

L'URL /course n'est pas une extension de document, mais plutôt un **point de terminaison**.

Faire des requêtes à ce point de terminaison déclenchera un programme qui utilisera les données fournies par l'utilisateur (comme le nom d'utilisateur et le mot de passe) et probablement quelques variables externes (comme l'heure et la date) pour interagir avec la base de données et finalement créer et retourner une nouvelle page web.

C'est aussi pourquoi j'ai dit plus tôt que la page d'actualités de freeCodeCamp est dynamique – parce que le contenu change à mesure que de nouveaux articles sont publiés.

Cette page n'a jamais existé en tant que fichier sur le serveur. Au lieu de cela, elle a été créée par le script qui s'est exécuté lorsque l'utilisateur l'a demandée.

## Conclusion

Une page web est un document unique qui contient du texte, des images, de l'hypertexte et d'autres éléments.

Un hypertexte est un document web qui contient des hyperliens. Un hyperlien relie une page web à une autre.

Un réseau de pages web organisées qui se lient les unes aux autres est appelé un site web.

Pour qu'un site web soit considéré comme statique, chaque appel à la même URL retourne la même page web.

D'un autre côté, si le contenu change souvent, alors cette page web est dynamique. Une page dynamique se termine également par un point de terminaison, et non par un chemin de fichier.

Donc, c'est tout. Espérons que maintenant vous pouvez distinguer une page web statique d'une page web dynamique. J'espère vraiment que vous avez tiré quelque chose d'utile de cet article.

Si vous voulez plus, j'ai récemment commencé une **série de défis de codage hebdomadaires** visant à enseigner aux débutants comment programmer en JavaScript. Consultez-la sur [mon blog](https://ubahthebuilder.tech/day-1-who-likes-it).

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).