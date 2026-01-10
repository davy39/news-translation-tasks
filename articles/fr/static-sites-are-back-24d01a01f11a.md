---
title: Les meilleurs générateurs de sites web statiques, et quand les choisir plutôt
  qu'un CMS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-21T08:39:26.000Z'
originalURL: https://freecodecamp.org/news/static-sites-are-back-24d01a01f11a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xbivs4c7SBkMAHnNFIUHuA.png
tags:
- name: Design
  slug: design
- name: Entrepreneurship
  slug: entrepreneurship
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Les meilleurs générateurs de sites web statiques, et quand les choisir
  plutôt qu'un CMS
seo_desc: 'By Stefanos Vardalos

  Back in the day, web pages were static sites, with only HTML and CSS (and later
  some JavaScript). Try to remember what that actually means.

  There was no server code or database. Your browser downloaded and displayed an HTML
  file ...'
---

Par Stefanos Vardalos

À l'époque, les pages web étaient des sites statiques, avec seulement du HTML et du CSS (et plus tard un peu de JavaScript). Essayez de vous rappeler ce que cela signifie réellement.

Il n'y avait pas de code serveur ni de base de données. Votre navigateur téléchargeait et affichait un fichier HTML hébergé quelque part. Le développement était fait directement dans les fichiers texte, ou via des programmes comme Dreamweaver.

Le développement web a finalement pris de l'essor et, jusqu'à aujourd'hui, il n'a pas cessé de s'accélérer. À un moment donné, la notion de Système de Gestion de Contenu (CMS) a émergé. Ensuite, de nouvelles façons de développer des portails, des blogs et des sites marketing ont vu le jour et prospéré. Ils le font toujours, avec WordPress étant le choix de CMS leader actuellement.

Un CMS peut résoudre de nombreux problèmes, tant du point de vue du développeur que de l'administrateur. Mais il y a des raisons de _ne pas_ en utiliser un et de revenir à un vieux, très vieux ami.

Sélectionner un CMS pour un projet spécifique nécessitera des spécifications et des dépendances strictes. Une installation typique de WordPress nécessitera un serveur web comme Apache, PHP avec diverses extensions et une base de données MySQL. Tout cela doit être mis à jour et maintenu. Mais, dans certaines situations, ces procédures peuvent même causer plus de problèmes.

L'un des facteurs les plus importants pour le développement web aujourd'hui est la sécurité. Cela, malheureusement, est l'un des principaux inconvénients des CMS. Utiliser un CMS, c'est comme se rendre vulnérable aux cyberattaques. Le nombre de vulnérabilités auxquelles vous vous exposez augmente avec les plugins que vous installez et utilisez. (Les plugins étant la vraie raison d'utiliser un CMS en premier lieu.)

Outre la sécurité, un autre facteur important d'un projet moderne est la performance. Un CMS génère la page demandée par l'utilisateur à partir de zéro ou utilise un plugin intégré ou installable. Le système de cache assure la réutilisation d'une page pré-générée chaque fois que possible. Utiliser un type de système de cache peut aider beaucoup, mais cela peut ajouter un certain overhead.

![Image](https://cdn-media-1.freecodecamp.org/images/4ikaZcRhrPAhgic7wBlZDZO9NoY0oSO7JvYf)
_Une capture d'écran de la belle interface graphique utilisateur que les outils CMS offrent aux utilisateurs non techniques._

Ainsi, en créant un site statique, ces problèmes deviennent obsolètes. Un site statique se compose uniquement, comme son nom l'indique, de fichiers statiques. Comme certains fichiers HTML et CSS, et un peu de JavaScript.

Il n'y a pas d'exigences spécifiques pour le type de machine qui hébergera la page, pas de restriction de langage back-end et pas besoin de base de données. Comme les fichiers statiques servis au navigateur, il n'y a pas de vulnérabilités réelles.

Les pages réelles sont déjà générées et peut-être minifiées. Du point de vue de la performance, elles semblent être bien meilleures que toute solution CMS en cache.

De plus, les générateurs de sites statiques modernes lisent généralement des fichiers de type plat, comme Markdown. Le contenu de l'article réside dans des fichiers, au lieu d'une base de données, vous pouvez donc les mettre sous votre flux de travail Git.

Mais les sites statiques ont aussi quelques inconvénients. Vous abandonnez essentiellement le back-end du web. Plus important encore, vous perdez l'interactivité avec l'utilisateur — des choses comme les profils utilisateurs, les favoris et les lectures suggérées. Il existe des moyens d'ajouter quelques-unes de ces fonctionnalités — comme les commentaires via la plateforme Disqus — mais celles-ci ne sont pas optimales.

La plus grande fonctionnalité manquante de ces générateurs est l'absence d'une interface utilisateur administrative. (Bien qu'il soit raisonnable de supposer qu'il y aura une solution pour cela à un moment donné.) Certaines personnes plus techniques pourraient ne pas trouver difficile de créer de nouveaux fichiers dans des dossiers appropriés et de lier des actifs comme des images. Mais pour la plupart, les créateurs de contenu non techniques pourraient trouver l'absence d'une interface utilisateur administrative être un vrai calvaire.

Ceci est principalement une décision de planification de projet basée sur ses exigences. Pour de nombreux sites web, un CMS est définitivement excessif.

En tenant compte des points ci-dessus, vous devriez être en mesure de répondre si un site web statique est suffisant pour un projet spécifique. Mais un autre problème serait le grand nombre de choix requis et le temps de configuration initial qui l'accompagne.

Dans le monde des CMS, il y a d'innombrables options, mais aussi un gagnant. WordPress, en tant que choix, fera le travail pour n'importe quel projet. Dans le monde des générateurs de sites statiques, il y a trop d'options — [459](https://staticsitegenerators.net/) pour être précis.

Mais il n'y a pas de gagnant clair ou de moyen de les différencier. Il semble que cela pourrait changer à partir de maintenant, mais cela reste à voir. Certains d'entre eux ont gagné une grande popularité et valent la peine d'être notés.

![Image](https://cdn-media-1.freecodecamp.org/images/xdSxTp8MpsZooz1Lb22SeRUwYvwtFqEGdMCS)
_Statistiques via [StackShare](https://stackshare.io/stackups/gatsby-vs-wintersmith-vs-hugo-vs-hexo-vs-jekyll" rel="noopener" target="_blank" title=")_

[**Jekyll**](https://jekyllrb.com/) est de loin le plus populaire de ces générateurs. Il est construit avec Ruby et intégré à GitHub Pages. Donc, il est assez populaire pour les projets personnels et/ou la documentation. Il a une grande base d'utilisateurs et un grand répertoire de plugins.

[**Hugo**](https://gohugo.io/) est assez similaire à Jekyll. Il est construit sur Go et son principal argument contre Jekyll est sa vitesse fulgurante. Jekyll peut être assez lent lorsque le site est généré, surtout lorsque le nombre de posts/pages augmente.   
Mais Hugo génère le site en quelques secondes. Il y a d'autres abstractions qui rendent Hugo plus convivial et plus facile à démarrer. Il ne nécessite pas autant de configuration pour créer quelque chose à partir de zéro.

[**Hexo**](https://hexo.io/) est une nouvelle addition et créée avec NodeJS. Publicisé et principalement utilisé comme plateforme de blog, il combine l'extensibilité de Jekyll avec la vitesse de Hugo. (en fait plus rapide que Hugo)

[**Wintersmith**](http://wintersmith.io/) est un autre construit sur NodeJS. Celui-ci est différent car il est assez minimaliste. Il est essentiellement une plateforme que vous pouvez personnaliser via des plugins selon vos besoins. Il nécessite définitivement quelques ajustements pour le faire fonctionner, mais laisse plus d'espace pour la personnalisation.

La dernière option est la plus récente et la plus intéressante.

[**Gatsby**](https://www.gatsbyjs.org/) est le framework qui amène les pages statiques aux stacks de nos jours. Il utilise React.js et Webpack pour créer une SPA (Single Page Application) avec votre contenu. Il promet de supprimer une grande partie de la configuration nécessaire pour une telle application. En faisant cela, il fournit au développeur une solution facile à utiliser qui produira, en fin de compte, une application moderne et haut de gamme.   
La vérité est que Gatsby peut être utilisé pour bien d'autres choses qu'un simple blog. Sa vraie limite n'a pas encore été trouvée. (Puisqu'il n'a atteint sa première version stable que plus tôt ce mois-ci.)

Le fait qu'il utilise React aide beaucoup, car de plus en plus de développeurs utilisent React en ce moment ou prévoient de le faire bientôt.

### Résumé

![Image](https://cdn-media-1.freecodecamp.org/images/7N7Ui-fytY1esR7HEknVxj3quonolO0jtu6o)
_Téléchargements au cours des 6 derniers mois_

En regardant les téléchargements des six derniers mois, nous pouvons voir que Gatsby pourrait être un gagnant en devenir. Ces chiffres ne sont peut-être pas 100% vrais.   
Gatsby peut également être utilisé pour des choses plus complexes que la conversion de markdown en HTML. Mais, alors que sa base d'utilisateurs s'étend rapidement, nous avons peut-être trouvé le WordPress pour les générateurs de sites statiques.