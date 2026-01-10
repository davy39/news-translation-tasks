---
title: Comment héberger un dépôt Git sur un sous-domaine avec Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-23T15:15:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-a-git-repository-on-a-subdomain-with-netlify-b8afb5fca96e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yd8PzBwBVOc98lXb
tags:
- name: Netlify
  slug: netlify
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Hosting
  slug: web-hosting
seo_title: Comment héberger un dépôt Git sur un sous-domaine avec Netlify
seo_desc: 'By Glyn Lewington

  Let’s say you have your portfolio, like [www.glynlewington.com](http://www.glynlewington.com),
  hosted on Netlify and want to add your projects onto the same domain. They are all
  separate git repositories and Netlify is made for host...'
---

Par Glyn Lewington

Disons que vous avez votre portfolio, comme `[www.glynlewington.com](http://www.glynlewington.com)`, hébergé sur Netlify et que vous souhaitez ajouter vos projets sur le même domaine. Ce sont tous des dépôts git séparés et Netlify est conçu pour héberger à partir d'un seul dépôt... mais ne craignez rien ! Nous pouvons les héberger sur des sous-domaines comme `project.glynlewington.com` avec un peu de travail.

Netlify rend super facile l'hébergement de vos sites statiques avec eux gratuitement. J'ai récemment transféré mon portfolio d'un VPS vers eux, et c'est génial qu'ils mettent automatiquement à jour votre site à chaque fois que vous poussez vers votre dépôt git.

Dans le passé, j'avais tous mes projets personnels hébergés dans des sous-répertoires, par exemple `www.glynlewington.com/project`. Cela est soit difficile, soit impossible avec Netlify. Netlify est principalement configuré pour que vous hébergiez tout sur un seul site à partir d'un seul dépôt git.

Le compromis auquel je suis parvenu est de les héberger sur des sous-domaines à la place, comme `project.glynlewington.com`. Cela n'est pas non plus très bien documenté, mais c'est possible.

* Allez sur [www.netlify.com](http://www.netlify.com,) et connectez-vous ou inscrivez-vous.
* Sélectionnez "Nouveau site depuis git".
* Choisissez votre fournisseur (par exemple, GitHub) — Vous devrez peut-être vous authentifier ici.
* Sélectionnez le dépôt git à partir duquel vous souhaitez créer un site.
* Sélectionnez la branche à partir de laquelle vous souhaitez déployer.
* Choisissez les commandes à exécuter. — *Si c'est une application React, vous devrez exécuter une commande de build.*
* Choisissez le répertoire à partir duquel vous allez publier. Il contiendra des fichiers tels que index.html. — *Si c'est une application React, il s'agira probablement du dossier build.*
* Sélectionnez "Build Site".

À ce stade, vous devriez avoir une application fonctionnelle hébergée sur un domaine gratuit de Netlify tel que `https://hungry-bose-fb0e6d.netlfiy.com`. Si cela ne fonctionne pas, vérifiez qu'il n'y a pas d'erreurs dans le processus de build et corrigez-les si nécessaire.

Maintenant, pour configurer un domaine personnalisé.

* Allez dans l'aperçu de votre application sur Netlify.
* Il indiquera que votre site est déployé avec succès et que vous pouvez configurer un domaine personnalisé.
* Cliquez sur configurer un domaine personnalisé, saisissez le domaine que vous souhaitez, y compris le sous-domaine, et cliquez sur vérifier. Par exemple, `project.glynlewington.com`.

Ensuite, connectez-vous à votre fournisseur d'hébergement de domaine. J'utilise Cloudflare, mais cela sera similaire avec d'autres.

* Allez dans les paramètres DNS.
* Sélectionnez un nouvel enregistrement CNAME.
* Saisissez un "Nom" — il s'agit du sous-domaine, il doit être le même que celui que vous avez sélectionné précédemment sur Netlify. Par exemple, `project`
* Sous "Adresse IPv4", saisissez le domaine gratuit de votre site Netlify. Par exemple, `hungry-bose-fb0e6d.netlify.com`.
* Si vous utilisez également Cloudflare, désactivez le routage du trafic via Cloudflare. Cela perturbe Netlify.
* Ajoutez l'enregistrement.

Terminé ! Une fois que vous avez fait cela, vous pouvez accéder à votre site sur le sous-domaine.

Netlify ajoutera également automatiquement la sécurité https à votre site, pas besoin de vous en soucier.