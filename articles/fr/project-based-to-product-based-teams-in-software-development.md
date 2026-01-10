---
title: Équipes basées sur les projets VS Équipes basées sur les produits – Quelle
  est la meilleure pour développer des logiciels ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T18:09:02.000Z'
originalURL: https://freecodecamp.org/news/project-based-to-product-based-teams-in-software-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99ed740569d1a4ca2275.jpg
tags:
- name: 'Junior developer '
  slug: junior-developer
- name: product development
  slug: product-development
- name: software development
  slug: software-development
seo_title: Équipes basées sur les projets VS Équipes basées sur les produits – Quelle
  est la meilleure pour développer des logiciels ?
seo_desc: "By Enrico Piccinin\nSuppose you have to add a new major feature to an app.\
  \ \nIs it easier to add this major feature to a relatively small app, still under\
  \ construction and not yet in production? Or is it easier on a big app that has\
  \ grown over time, wh..."
---

Par Enrico Piccinin

Supposons que vous deviez ajouter une **nouvelle fonctionnalité majeure** à une application. 

Est-il plus facile d'ajouter cette fonctionnalité majeure à une **application relativement petite**, encore en construction et pas encore en production ? Ou est-il plus facile de le faire sur une **grande application** qui a évolué avec le temps, dont la qualité globale est douteuse, et qui est déjà en production servant plusieurs clients ?

Eh bien, il n'y a aucun doute. La seconde option est une tâche bien plus difficile. 

Alors pourquoi trouvons-nous habituellement les développeurs les plus expérimentés, les architectes – les "cool kids" – principalement impliqués dans le travail sur ces petites applications, tandis que le reste de l'équipe est souvent enterré dans les grands projets ?

## Mon histoire

Il y a de nombreuses années, j'ai rejoint l'équipe de développement responsable de l'un des systèmes centraux d'une grande entreprise. Le premier poste qui m'a été attribué était dans l'équipe de Maintenance Applicative (AM) responsable des parties héritées de l'application. 

Les raisons étaient simples et m'ont été partagées : j'étais nouveau dans l'entreprise, et les nouveaux projets avançaient rapidement. Ils utilisaient des technologies de pointe pour lesquelles il n'y avait pas beaucoup d'expérience. Ainsi, l'AM était le bon endroit pour moi pour grandir sans trop de pression. 

Ils m'ont dit que dès que j'aurais acquis suffisamment de connaissances et d'expérience, je rejoindrais l'équipe Projet. C'était l'équipe qui développait de nouvelles fonctionnalités avec de nouvelles technologies, l'équipe des développeurs expérimentés. 

Après un an environ, cela s'est effectivement produit, mais je n'oublierai jamais cette période supposément peu stressante de l'AM.

## L'équipe Projet et l'équipe AM

Tout cela remonte à de nombreuses années, mais depuis, j'ai vu ce même schéma se répéter à maintes reprises, souvent sous des formes bien plus extrêmes. 

Lorsque vous avez une nouvelle initiative, vous commencez avec l'équipe Projet. L'équipe Projet développe l'architecture et les fonctionnalités. L'équipe Projet accumule des retards par rapport à un plan initial très optimiste, puis ils commencent à travailler des heures supplémentaires, en prenant des raccourcis en cours de route. 

La qualité est souvent sacrifiée sur l'autel du Plan, les tests sont oubliés, et des correctifs sont ajoutés par-dessus d'autres correctifs. Les développeurs commencent à ajouter des commentaires « À refactoriser dès que nous aurons un peu de temps ». La dette technique est déjà là et elle ne fera que grandir. 

Finalement, le projet est mis en production et ensuite, immédiatement après son lancement, l'équipe Projet commence la transition vers l'équipe AM. 

Après une période de chevauchement, l'équipe AM se retrouve à naviguer seule. L'équipe AM est généralement plus jeune, moins expérimentée, et considérée comme moins forte que l'équipe Projet. 

Mais la partie difficile est terminée, le projet est maintenant en production. Maintenant, c'est l'heure de l'AM – c'est plus facile, cela doit coûter moins cher, et l'entreprise peut se permettre une nouvelle équipe junior.

## Un an après le lancement

Avance rapide, et cela fait un an de travail intense. Les bugs ont été corrigés, de petites choses ont été changées, et de petites choses ont été ajoutées. 

Le système a finalement été rendu prêt à supporter une charge de production réelle et la base de code a grandi. À ce stade, l'équipe AM reçoit une demande pour ajouter une nouvelle grande fonctionnalité. 

Et nous revenons à la question initiale. Est-il plus facile d'ajouter la nouvelle fonctionnalité maintenant ou était-il plus facile d'ajouter une nouvelle fonctionnalité lorsque nous étions en mode projet ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-leZpJJQ4qsyleIHMzG7Tdg.png)

La réponse est claire : la tâche pour l'équipe AM est beaucoup plus difficile. Il est vrai que l'équipe AM s'appuie sur son expérience développée au fil du temps. Mais en même temps, l'équipe AM doit gérer une base de code peu stable, éviter d'introduire des régressions sans avoir un filet de sécurité de tests décents, et concevoir un moyen de déployer une nouvelle version majeure sans créer de perturbations.

Disons-le. L'équipe AM est souvent confrontée à une tâche bien plus difficile que l'équipe Projet. Alors pourquoi, si la tâche de l'équipe AM est plus difficile, tous les développeurs expérimentés travaillent-ils dans l'équipe Projet (et sont maintenant ailleurs, probablement en train de faire autre chose de cool) ?

## Une réponse possible : l'équipe Projet doit poser les bonnes bases

Une raison d'avoir les personnes les plus expérimentées pour démarrer un Projet est que, au début, nous devons poser les bases de ce qui va suivre. Nous devons définir l'architecture et prendre certaines décisions fondamentales concernant la conception de la solution, donc l'expérience appropriée est requise.

En même temps, au début d'un Projet, nous avons généralement une connaissance limitée du problème que nous sommes appelés à résoudre. 

Au début de tout Projet significatif, il y a beaucoup d'inconnues connues et aussi beaucoup d'inconnues inconnues. Pour cette raison, l'Architecture du système doit toujours être considérée comme évolutive. Nous devons être conscients que de nombreuses décisions cruciales ne peuvent pas être prises au début mais doivent être prises lorsque les inconnues commencent à se révéler.

Les décisions architecturales peuvent rarement être prises une fois pour toutes au début d'un projet. Des questions architecturales critiques peuvent surgir à tout moment dans la vie du système logiciel. Et ces décisions critiques prises au début du projet peuvent devoir être révisées plus tard – peut-être à cause de nouvelles exigences, peut-être à cause de nouvelles technologies comme le Cloud, peut-être parce qu'elles étaient simplement les mauvaises pour le problème à résoudre.

Donc oui, c'est vrai, l'équipe Projet doit prendre des décisions architecturales. Mais l'équipe AM doit aussi prendre des décisions architecturales, et elle doit les prendre dans un environnement beaucoup plus complexe.

### Vous ne pouvez tout simplement pas faire l'inverse

Alors que le modèle classique d'une équipe Projet forte suivie d'une équipe AM plus junior n'est pas le plus efficace à moyen terme, l'inverse n'est pas non plus une solution. 

La plupart des entreprises ne peuvent pas imaginer avoir une équipe junior démarrant un projet puis le transmettant à une équipe plus senior pour la maintenance. Ce n'est tout simplement pas une option.

## Un cas pour l'inconscient

Peut-être qu'une raison profonde pour laquelle les personnes plus expérimentées commencent de nouveaux Projets avec des technologies cool est qu'elles aiment commencer de nouvelles choses et jouer avec de nouvelles technologies. Mais ensuite, avec le temps, lorsque le travail semble devenir plus répétitif, elles veulent simplement passer à d'autres défis.

C'est bon pour leur curiosité technologique et c'est bon pour leur CV. Mais ce n'est probablement pas bon pour la santé à long terme du système logiciel qu'elles construisent.

## De l'équipe Projet à l'équipe Produit

En 2006, Werner Vogels, CTO chez Amazon, a inventé la célèbre devise ["you build it, you run it"](https://queue.acm.org/detail.cfm?id=1142065). Elle véhiculait l'idée qu'une équipe responsable d'un Produit doit en prendre soin depuis sa conception jusqu'à sa phase d'exploitation (où l'exploitation couvre à la fois les aspects Ops et les aspects d'évolution). 

Pour faire simple, la même équipe est responsable de toutes les phases nécessaires pour qu'un Produit soit réussi : conception, construction, exécution, évolution. 

C'est le modèle adopté par les géants du numérique qui ont émergé au cours de la dernière décennie, d'Amazon à Facebook en passant par AirB&B. Leur succès incontesté est la preuve que le modèle est le bon à l'ère du numérique.

De nos jours, un nombre croissant de personnes soulignent la nécessité de passer d'une organisation du travail orientée projet à un modèle plus orienté produit. 

Il s'agit d'une transformation complexe qui implique de nombreux aspects d'une organisation. Mais pour le sujet que nous débattons ici, cela signifie définitivement que nous devons abandonner l'idée d'équipes Projet et AM séparées et créer des équipes Produit plus stables. 

Les équipes Produit doivent avoir le bon mélange de personnes expérimentées et de personnes plus juniors qui ont besoin de grandir. En travaillant ensemble avec les développeurs expérimentés, les juniors deviennent progressivement expérimentés eux-mêmes. Une rotation contrôlée est alors possible sans compromettre la qualité de l'équipe.

## Conclusion

À l'ère dans laquelle nous vivons, l'ère du numérique, nous devons être suspicieux lorsque nous entendons quelque chose comme _"et lorsque le Projet se termine, nous passerons à l'AM"_. 

Cela ne signifie pas qu'il n'y a plus de place pour l'AM. Il existe encore d'anciens systèmes hérités, servant généralement le back-office, qui accomplissent égrégieusement leur travail, qui sont très stables, et qui ont simplement besoin d'un peu de maintenance. 

Mais lorsqu'il s'agit de développer de nouvelles capacités numériques différenciantes, nous devons nous éloigner du modèle Projet/AM et adopter un modèle orienté Produit. 

Dans ce modèle, les équipes sont conçues pour être responsables de la construction non seulement de la première version du Produit, mais aussi de son exécution. Et elles apprennent de son exécution tout en l'améliorant au fil du temps pour s'assurer qu'il reste pertinent pour ses utilisateurs finaux.