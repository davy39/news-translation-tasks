---
title: La puissance de la communauté des développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T20:28:11.000Z'
originalURL: https://freecodecamp.org/news/the-power-of-the-developer-community-2b6e713fc9ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*39yXxTeKLonaag8vJfjg1Q.png
tags:
- name: Blogging
  slug: blogging
- name: community
  slug: community
- name: Devops
  slug: devops
- name: Inspiration
  slug: inspiration
- name: 'tech '
  slug: tech
seo_title: La puissance de la communauté des développeurs
seo_desc: 'By Joel Speed

  In the autumn of 2014, I started my adventure into the world of DevOps. Having just
  started my degree, I found a society at the university that was in desperate need
  of some IT love. My home for the next three years was at Warwick Stude...'
---

Par Joel Speed

À l'automne 2014, j'ai commencé mon aventure dans le monde de DevOps. Venant de commencer mon diplôme, j'ai trouvé une société à l'université qui avait désespérément besoin d'un peu d'amour informatique. Mon foyer pour les trois prochaines années était le [Warwick Student Cinema](https://warwick.film/).

![Image](https://cdn-media-1.freecodecamp.org/images/BufmiJ4tdnK0rolaro76iqb6Cq2n41YlrSBz)

Au cours de mon diplôme, j'ai démonté chaque partie de l'infrastructure du cinéma et l'ai reconstruite à partir de zéro (pas tout seul, bien sûr). Avec un budget serré, environ 30 £ par an, l'infrastructure du cinéma se composait de plusieurs machines de récupération dont l'université n'avait plus besoin et de quelques boîtiers Dell [1U](https://en.wikipedia.org/wiki/1U) qu'ils avaient achetés comme une dépense ponctuelle. Sur ces machines, ils hébergeaient leur site web public, ainsi que plusieurs sites internes cruciaux pour le fonctionnement du cinéma.

Le plus important de ces sites était connu sous le nom d'EPOS. C'était un monolithe PHP, entrelacé avec le site web public principal qui avait été écrit environ 10 ans plus tôt par une poignée d'étudiants enthousiastes et qui avait été transmis d'année en année au prochain responsable informatique.

Ce site EPOS était utilisé pour vendre des billets pour les projections du cinéma environ 7 fois par semaine. À chaque projection, sur une fenêtre de 30 minutes, nous pouvions vendre jusqu'à 300 billets. Mais, plus souvent qu'autrement, le site tombait en panne et nos responsables de service devaient recourir à l'utilisation de tickets de tombola pour compter nos participants. Malheureusement, les systèmes n'avaient aucune redondance, rien n'était mis à l'échelle horizontalement, et honnêtement, personne ne savait vraiment comment tout cela s'assemblait.

J'aimerais penser qu'au moment où j'ai transmis le chapeau de responsable informatique à mon successeur, l'infrastructure était dans un meilleur état. Toutes les charges de travail Linux avaient été migrées vers des conteneurs Docker, fonctionnant sur un [Swarm](https://docs.docker.com/engine/swarm/). Les Dockerfiles des conteneurs étaient sous contrôle de source, avec des builds et des déploiements automatisés utilisant Jenkins.

Nous comprenions maintenant le rôle de chaque partie de l'infrastructure, nous pouvions voir dans le code ce qui fonctionnait et où. Le monolithe pouvait maintenant être mis à l'échelle horizontalement et son temps de disponibilité avait considérablement augmenté. J'avais l'impression que moi et les quelques collègues qui m'avaient aidé pendant cette période avions vraiment fait une différence dans les systèmes que nous maintenions.

### Belle histoire Joel, mais quel est le rapport avec la communauté ?

Rien de ce que j'ai décrit ci-dessus, je n'aurais pu le faire seul. Je ne suis pas un génie. Je ne savais pas instantanément comment écrire un Dockerfile, ou comment configurer un Docker Swarm. Les pare-feux redondants que j'ai configurés avec un routage basé sur des politiques compliquées et [VRRP](https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol) sur leurs interfaces internes et externes, ce n'était pas du travail de devin. Je ne savais à peine ce qu'était Linux quand j'ai commencé l'université !

Tout ce que j'ai fait, tout ce que j'ai appris pendant cette période, venait d'Internet, de la communauté. J'ai passé d'innombrables heures sur Google — passant de tutoriels sur des sujets tels que comment générer un [CSR](https://en.wikipedia.org/wiki/Certificate_signing_request) à des questions StackOverflow qui correspondaient à la chaîne d'erreur que je venais de rencontrer. J'ai parcouru les forums de support de [pfSense](https://www.pfsense.org/) en essayant de comprendre comment faire du routage de trafic entre plusieurs [VLANs](https://en.wikipedia.org/wiki/Virtual_LAN). Et j'ai lu des articles sur les meilleures pratiques pour réduire les points de défaillance uniques. Toutes les réponses que j'ai trouvées, tout ce que j'ai lu, avait été contribué par des personnes pendant leur temps libre.

La communauté m'a inspiré. Il y avait tant de personnes prêtes à donner de leur temps, à partager leur expertise, à aider les gens en écrivant, en maintenant et en répondant aux problèmes sur des projets open source. J'ai l'impression d'avoir tant appris au cours de cette période de trois ans et je crois sincèrement que je ne serais pas dans mon rôle actuel sans tout cela. Je me sens redevable à la communauté de m'avoir aidé à arriver là où je suis aujourd'hui.

### Donc la communauté t'a amené là où tu es aujourd'hui ?

C'est exactement ce que je dis ! Sans le temps et les efforts que d'innombrables membres de la communauté ont consacrés à leurs blogs et tutoriels, je n'aurais pas réussi la plupart des projets que j'ai entrepris au cinéma, et je n'aurais pas tant appris !

Cela m'a fait réfléchir. Je voulais pouvoir redonner, prendre ce que j'avais appris et devenir un membre actif de la communauté. Si ces personnes m'aidaient tant, pourrais-je éventuellement les aider et leur rendre la pareille ?

Je suis arrivé à la conclusion que je faisais peut-être des choses intéressantes au cinéma. Peut-être avais-je passé assez de temps à apprendre des autres pour commencer à contribuer à la communauté. Je me suis acheté un [domaine personnel](https://joelspeed.co.uk/) et j'ai décidé que je commencerais à bloguer, dans l'espoir que, un jour, les gens pourraient trouver mes divagations utiles.

Cela ne s'est pas passé tout à fait comme prévu. Il m'a fallu trois ans complets, depuis l'achat de mon domaine, pour enfin mettre un blog en ligne. J'ai la chance que mon entreprise, [Pusher](https://pusher.com/), soutienne mon désir d'écrire et de redonner à la communauté. En mars de cette année, j'ai réussi à écrire mon premier article de blog et j'ai maintenant été publié sur [The New Stack](https://thenewstack.io/kubernetes-single-sign-one-less-identity/), et [InfoQ](https://www.infoq.com/articles/tips-running-scalable-workloads-kubernetes). J'ai parlé à 2 meetups et j'ai poussé à open-sourcer un tas de projets sur lesquels j'ai travaillé depuis que j'ai rejoint Pusher. Cinq ont été partagés jusqu'à présent !

Ce que j'ai réalisé au cours de l'année dernière, c'est qu'il n'est pas aussi difficile de contribuer à la communauté que je le pensais, et qu'en fait, j'ai travaillé sur des choses intéressantes. Plusieurs personnes m'ont contacté, m'ont parlé après des conférences, me posant des questions ou demandant plus de détails sur le travail que j'ai fait. À quelques reprises, des gens m'ont simplement dit qu'ils avaient lu mon travail et l'avaient utilisé comme guide pour leurs propres projets. Je suis heureux d'avoir pu aider ces personnes et commencer à aider les autres comme tant d'autres m'ont aidé.

### Pourquoi open-sourcer votre travail ?

Les projets que nous avons open-sourcés chez Pusher ne sont pas particulièrement grands et ils ne nous donnent aucun avantage concurrentiel sur nos concurrents. Ils sont liés à notre infrastructure Kubernetes. Là où nous n'avons pas trouvé de solution existante dans la communauté, nous avons écrit les outils dont nous avions besoin, et maintenant nous les partageons afin que d'autres personnes, essayant de résoudre les mêmes problèmes, n'aient pas à passer leur temps à écrire leur propre version.

Peut-être avez-vous travaillé sur quelque chose de similaire, est-ce open source ? Pourrait-il l'être ? J'aimerais vous encourager à le partager si vous le pouvez.

### Mon plaidoyer

Si vous êtes arrivé jusqu'ici, merci, j'ai une faveur à demander. Que vous soyez développeur ou comptable, que vous travailliez dans les relations publiques ou dans les ventes, vous savez quelque chose que quelqu'un d'autre ne sait pas. Vous serez un expert en quelque chose même si vous ne le savez pas. Réfléchissez à cela et puis prenez la plume (ou l'équivalent numérique).

Écrivez un article et partagez votre expérience. Écrivez un article et aidez quelqu'un à apprendre, et à se développer. Aidez-le à comprendre quelque chose qu'il essaie de comprendre depuis des jours. Écrivez un article et, comme tant l'ont fait pour moi, inspirez quelqu'un.