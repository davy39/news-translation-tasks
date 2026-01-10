---
title: Hébergez votre site web statique sur votre propre domaine via GitHub Pages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-10-22T19:23:28.000Z'
originalURL: https://freecodecamp.org/news/hosting-custom-domain-on-github-pages-8c598248d2bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FFYtzf28XKPFBdknfXf-jg.jpeg
tags:
- name: coding
  slug: coding
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
seo_title: Hébergez votre site web statique sur votre propre domaine via GitHub Pages
seo_desc: 'By Taurus Omejia

  Did you know that Github will allow anyone to host their static webpages for free?
  The best part is that you can even use your own custom domain. Let’s do this!

  Step 1: Create your website

  If you already have a website, than you can ...'
---

Par Taurus Omejia

Saviez-vous que GitHub permet à quiconque d'héberger ses pages web statiques gratuitement ? Le meilleur dans tout cela, c'est que vous pouvez même utiliser votre propre domaine personnalisé. Faisons cela !

#### Étape 1 : Créez votre site web

Si vous avez déjà un site web, vous pouvez passer à l'étape 2.

Sinon, aujourd'hui est un bon jour pour commencer.

Je suggère de commencer un blog. Un blog est un excellent moyen d'établir une présence plus significative en ligne. Vous pouvez l'utiliser pour construire votre propre [marque personnelle en ligne](http://www.forbes.com/sites/shamahyder/2014/08/18/7-things-you-can-do-to-build-an-awesome-personal-brand/).

Vous ne savez pas par où commencer ? Je vous couvre. John Sommez de [Simpleprogrammer.com](http://simpleprogrammer.com/?__s=e9nxoo3daippuegoyzyj&utm_campaign=lesson-5-do-you-know-how-to-get-traffic-for-your-blog&utm_medium=email&utm_source=how-to-create-a-blog-that-boosts-your-career-course) propose un excellent cours par email intitulé : [Comment créer un blog qui boostera votre carrière](http://t.dripemail2.net/c/eyJhY2NvdW50X2lkIjoiOTUyNDk2NiIsImRlbGl2ZXJ5X2lkIjoiMjQ3MzM4MTciLCJ1cmwiOiJodHRwOi8vZGV2Y2FyZWVyYm9vc3QuY29tL2Jsb2ctY291cnNlLz9fX3M9ZTlueG9vM2RhaXBwdWVnb3l6eWpcdTAwMjZ1dG1fY2FtcGFpZ249bGVzc29uLTUtZG8teW91LWtub3ctaG93LXRvLWdldC10cmFmZmljLWZvci15b3VyLWJsb2dcdTAwMjZ1dG1fbWVkaXVtPWVtYWlsXHUwMDI2dXRtX3NvdXJjZT1ob3ctdG8tY3JlYXRlLWEtYmxvZy10aGF0LWJvb3N0cy15b3VyLWNhcmVlci1jb3Vyc2UifQ). C'est un excellent cours qui vous guide tout au long du processus.

Vous avez donc décidé de créer un blog. Maintenant quoi ? Il existe de nombreuses façons de procéder, comme Wordpress, Tumblr, ou même Blogger.

Mais cela irait à l'encontre du but de cet article. Nous voulons utiliser GitHub Pages pour héberger une page statique gratuitement. Je recommande donc d'utiliser un générateur de blog statique.

J'utilise personnellement [Jekyll](http://jekyllrb.com/) pour mon blog. Mais il en existe beaucoup d'autres. Voici une liste de certains des plus populaires : [Générateurs de blogs statiques](http://www.sitepoint.com/6-static-blog-generators-arent-jekyll/). Choisissez-en un, lisez les instructions et configurez votre blog !

#### Étape 2 : Ajoutez votre site au contrôle de version Git

Super, vous êtes arrivé à l'étape 2. Maintenant que votre blog est prêt, mettons-le sous contrôle de version en utilisant [Git](http://git-scm.com/). Cet article suppose que vous avez [Git installé](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git), que vous avez un compte GitHub et que vous pouvez [y pousser](http://guides.railsgirls.com/github/).

* Cette étape est très importante : créez un simple fichier .txt et nommez-le « CNAME ». Ouvrez le fichier et tapez votre nom de domaine personnalisé dedans. Enregistrez-le.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ooJqWG_qyn-Qlmr-.png)
_Créez un simple fichier .txt et nommez-le CNAME_

OK ! Lancez votre terminal et naviguez jusqu'au répertoire où se trouve votre site. Il est temps d'initialiser le contrôle de version en entrant la commande.

```
$ git init
```

Maintenant, ajoutez l'ensemble du projet sous le suivi git. Entrez :

```
$ git add .
```

Faisons un commit :

```
$ git commit -m "first commit"
```

Votre site est maintenant sous contrôle de version. Maintenant, le plaisir commence.

#### Étape 3 : Poussez votre site vers GitHub

Nous sommes enfin prêts à pousser vers GitHub et à voir notre site automatiquement en ligne gratuitement !

1. Lancez [github.com](https://github.com/) et connectez-vous.
2. Sur votre page d'accueil, cliquez sur le grand bouton vert qui dit « + New repository ».
3. Pour que votre page soit automatiquement hébergée, vous devez suivre une convention de nommage spécifique. Nommez votre dépôt « [votre-nom-dutilisateur].github.io », laissez tout le reste tel quel, et appuyez sur « Create Repository ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*1RJpGhJ1eFNwlCAy.png)
_Nommez votre dépôt, ne faites rien d'autre, cliquez sur 'Create Repository'_

Suivez maintenant les instructions de GitHub pour pousser votre blog vers votre nouveau dépôt.

C'est tout ! Votre nouvelle page devrait être disponible à l'adresse http://votre-nom-dutilisateur.github.io.

Si vous ne la voyez pas tout de suite, attendez quelques minutes, dix au maximum.

C'est tout ! Pour la plupart des gens, c'est tout ce que vous avez à faire. Cependant, pour ceux qui souhaitent utiliser leur propre domaine personnalisé, passez à l'étape finale.

#### Étape 4 : Associez votre domaine personnalisé à votre nouveau site web GitHub Pages

Cela variera en fonction de l'endroit où vous avez enregistré votre domaine. J'ai GoDaddy, donc ces instructions sont spécifiques à cela. Mais les étapes devraient être similaires avec d'autres fournisseurs de domaines. Voici comment je l'ai fait :

1. Je me suis connecté à mon compte GoDaddy et j'ai sélectionné « gérer les domaines ». J'ai sélectionné le domaine que je voulais utiliser et j'ai cliqué sur « Manage Connection ».
2. Sur la page « Domain Details », j'ai cliqué sur l'onglet « DNS ZONE FILE ».
3. Modifiez « A-Host » et pointez-le vers 192.30.252.153
4. Maintenant, modifiez la partie www de « CName (Alias) » et pointez-la vers [votre-nom-dutilisateur].github.io.
5. Assurez-vous d'enregistrer tout. Une fois que vous avez enregistré cela, cela peut prendre jusqu'à une heure pour se mettre à jour complètement.
6. Maintenant, « [votre-domaine-personnalisé].com » devrait pointer vers [votre-nom-dutilisateur].github.io. Mais que se passe-t-il si votre utilisateur tape « www.[votre-domaine-personnalisé].com » à la place ? Corrigons cela pour que le sous-domaine www pointe également vers [votre-nom-dutilisateur].github.io.
7. Sélectionnez votre domaine et appuyez sur « Manage Connections », puis sélectionnez l'onglet « Settings ».
8. Sous Forwarding -> Domain, cliquez sur « manage ».
9. Cliquez sur « Update Forwarding ».
10. Dans « Forward to: », tapez www.[votre-domaine-personnalisé].com
11. Assurez-vous que 301 (Permanent) est sélectionné, puis enregistrez votre travail.
12. C'est tout. Laissez environ 1 heure pour que tout se mette à jour.

Laissez-moi être le premier à vous féliciter. Vous avez un site web en ligne, sous contrôle de version, avec votre propre nom de domaine — le tout hébergé gratuitement !

_Publié à l'origine sur [www.tauruso.com](http://www.tauruso.com/guide,/beginner,/tutorial/2015/04/17/Github-pages/). Pour voir cet article dans toute sa gloire et plus de [Taurus Omejia](https://www.freecodecamp.org/news/hosting-custom-domain-on-github-pages-8c598248d2bc/undefined), allez [ICI !](http://www.tauruso.com)_