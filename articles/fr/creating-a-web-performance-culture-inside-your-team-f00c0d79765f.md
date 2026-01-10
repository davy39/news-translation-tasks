---
title: Comment créer une culture de la performance web au sein de votre équipe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T12:32:57.000Z'
originalURL: https://freecodecamp.org/news/creating-a-web-performance-culture-inside-your-team-f00c0d79765f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f-Ey0tW6O_vFHz_RPZWh_A.jpeg
tags:
- name: Culture
  slug: culture
- name: JavaScript
  slug: javascript
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une culture de la performance web au sein de votre équipe
seo_desc: 'By Alex Moldovan

  Those who work with me know that I’m always obsessing about performance. Words like:
  critical rendering path, bundle size and frames-per-second are a common thing around
  the office. But it’s all for a good reason.

  Performance should ...'
---

Par Alex Moldovan

Ceux qui travaillent avec moi savent que je suis toujours obsédé par la performance. Des mots comme : chemin de rendu critique, taille du bundle et images par seconde sont mon pain quotidien au bureau. Mais c'est pour une bonne raison.

La performance devrait être un **citoyen de première classe** en ingénierie logicielle.

Avoir une forte **culture de la performance** dans votre équipe peut garantir que vous atténuez — à l'avance — tout risque associé à une mauvaise performance.

Mais pourquoi est-ce si important ? Et quels sont ces risques ?

## Pourquoi la performance compte

Rappelez-vous qu'en tant que développeurs web, notre objectif est de créer la meilleure expérience possible pour nos utilisateurs.

### La performance est une question d'utilisabilité.

Il existe de nombreuses études ([[1]](https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/), [[2]](https://wp-rocket.me/blog/speed-up-your-website-make-the-first-few-seconds-count/), [[3]](https://www.fastcompany.com/1825005/how-one-second-could-cost-amazon-16-billion-sales)) qui montrent une corrélation directe entre les objectifs commerciaux et l'utilisabilité sur le web.

Un site web rapide et réactif peut faire la différence entre le succès et l'échec en ce qui concerne la relation avec vos utilisateurs.

Votre framework UI sophistiqué et votre architecture n'auront aucune importance si votre site web est perçu comme lent et laggy. Sans parler du scénario dans lequel les utilisateurs quittent parce qu'ils attendent derrière un spinner ou un écran blanc.

[53 % des utilisateurs fermeront votre site web en moins de 3 secondes](https://developer.akamai.com/blog/2016/09/14/mobile-load-time-user-abandonment) si vous n'affichez aucun contenu.

De plus, la performance est également une métrique dans le classement des pages mobiles, [selon Google](https://webmasters.googleblog.com/2018/01/using-page-speed-in-mobile-search.html).

### La performance est une question d'accessibilité.

Parlons du marché mondial. Les budgets de performance sont également importants en ce qui concerne le coût des données. Combien un utilisateur paie-t-il pour visiter votre site web ?

Vous pouvez le découvrir en utilisant [ce site web](https://whatdoesmysitecost.com/#usdCost). Ensuite, vous pouvez vous demander : « Suis-je prêt à payer x cents pour visiter mon site web ? » Vous pourriez être surpris par votre propre réponse.

De plus, il existe des pays où la majorité du [temps passé sur internet l'est via mobile](https://www.smartinsights.com/mobile-marketing/mobile-marketing-analytics/mobile-marketing-statistics/). Vous devez donc adopter une approche mobile-first pour optimiser la performance.

En omettant cela, vous rendez votre produit inaccessible pour beaucoup de gens !

### La performance est une question d'empathie

Nous avons tendance à voir notre travail strictement à travers nos propres yeux. Cela est dangereux, car cela conduit à une compréhension superficielle des besoins de nos utilisateurs.

Sans parler de notre besoin constant de travailler sur des choses cool (nouvelles technologies, frameworks à la pointe de l'art, etc.) et d'ignorer les tâches ennuyeuses et fastidieuses.

La performance compte, et vous devez travailler à son optimisation avec **empathie** et **abnégation** à l'esprit. Mais ces qualités, malheureusement, ne viennent pas par défaut dans tous les environnements de travail.

## Prévoyez le pire

Un collègue m'a montré un scénario intéressant il y a quelques semaines. Il y a un site web de décoration intérieure qui utilise un système CMS en arrière-plan pour gérer les données. Quelqu'un a téléchargé cette image :

![Image](https://cdn-media-1.freecodecamp.org/images/4u0XBu8dfPbS9KEEuq0Uc1ad5g9cMbqoJb3g)
_capture d'écran des outils de développement Chrome_

C'est **9,3 mégaoctets** de données qui prennent environ **7 secondes** à charger sur une connexion Wi-Fi ultra-rapide et sur un MacBook Pro. Pouvez-vous imaginer combien de temps cela prendrait sur un appareil mobile ? La réponse est **l'infini** ! Parce que le navigateur mobile devient non réactif lorsque vous ouvrez le site web.

[Voici le site web](http://www.homemade-modern.com/ep106-media-console/) si vous êtes curieux, mais veuillez procéder avec prudence car il pourrait potentiellement bloquer votre navigateur !

Nous ne devrions pas blâmer l'utilisateur. Ils voulaient afficher une image très détaillée d'un assemblage.

Revenant à l'idée de **comprendre** nos utilisateurs, nous devrions toujours nous préparer aux pires scénarios en ce qui concerne le contenu créé par les utilisateurs.

En tant que développeur, vous êtes **totalement responsable** de la manière dont vos utilisateurs interagissent avec votre logiciel.

## Quand optimiser

Il existe deux approches pour les optimisations de performance. [Ben Schwarz](https://twitter.com/benschwarz?s=17) résume les deux approches dans son deck, [The Critical Request](https://speakerdeck.com/benschwarz/the-critical-request).

![Image](https://cdn-media-1.freecodecamp.org/images/LQhLZLaEKGlTWi5btGkboK0W2JOjNv6QRxKF)

![Image](https://cdn-media-1.freecodecamp.org/images/fulD0TWIdNZHkuxffOBGWBmxvWBZftfMwpZc)
_**Approche réactive** (en haut) vs **approche proactive** (en bas) pour optimiser la performance_

D'un côté, nous avons l'approche traditionnelle : « Houston, nous avons un problème ! ». C'est une manière hautement **réactive** de traiter les problèmes de performance. J'aime aussi l'appeler le problème : « Oh zut ! Appelez le consultant ! ».

Non seulement cela est coûteux pour votre entreprise, mais cela peut également être un grand démotivateur pour l'équipe. Cela peut même conduire à des conflits lorsque les personnes ne sont pas connectées aux objectifs d'optimisation de la performance.

De l'autre côté, nous avons l'approche **proactive**. Vous intégrez l'optimisation de la performance dans votre processus de développement logiciel.

Si vous devez convaincre le côté commercial d'essayer l'approche proactive, consultez [WPO stats](https://wpostats.com/). C'est une excellente ressource avec des études de cas qui montrent les avantages des optimisations de performance.

Une fois l'approche en place, c'est l'équipe et la culture qui résolvent les problèmes à l'avance, plutôt que le consultant qui vient sauver la journée. Et bien fait, cela peut être un grand motivateur pour l'équipe.

Mais la sensibilisation à la performance ne se fait pas du jour au lendemain. Vous devez créer le bon contexte pour que les gens soient conscients de l'impact de ce qu'ils font.

## Mesurer et agir

Savez-vous combien d'utilisateurs arrivent sur votre site depuis des appareils mobiles ? À quelle fréquence testez-vous dans des conditions de réseau médiocres ? À quelle fréquence sortez-vous un appareil de milieu de gamme, comme un [Moto G4](https://www.gsmarena.com/motorola_moto_g4-8103.php), et commencez à jouer avec votre application ?

Ce sont tous des scénarios pertinents que vos utilisateurs pourraient rencontrer chaque jour !

Connaissez votre base d'utilisateurs, et connaissez les usages de vos appareils et navigateurs. De bonnes et pertinentes **métriques** sont essentielles si vous voulez implémenter une culture de la performance.

Une fois que vous avez les métriques, il est temps d'établir les **budgets de performance**.

Enfin, il est temps d'agir ! Voici quelques outils et pratiques que vous pouvez introduire dans votre environnement de travail régulier :

### Étape 1 : Mesurer les indicateurs de performance

* [Lighthouse](https://developers.google.com/web/tools/lighthouse/) est un projet incroyable et est disponible dans les outils de développement Chrome. Il vous donnera de grandes informations sur les améliorations de performance potentielles. Il vous donnera également quelques suggestions pour le SEO, l'accessibilité et les meilleures pratiques.
* [Webpagetest](https://webpagetest.org/) est idéal pour suivre les métriques et comparer les graphiques en cascade avant et après les déploiements. Je peux également recommander [gtmetrix](https://gtmetrix.com/), un outil moins connu, avec une interface très facile à utiliser.

### Étape 2 : Automatiser

* Ajoutez des étapes de construction liées à la performance dans votre CI. [bundlesize](https://github.com/siddharthkp/bundlesize) est un excellent package si vous souhaitez définir des limites strictes pour vos bundles.
* Créez des tests automatisés qui échoueront si les temps de chargement ou d'autres métriques pertinentes dépassent certains seuils. [Puppeteer](https://github.com/GoogleChrome/puppeteer) a un accès direct à l'API Chrome, vous pouvez donc l'utiliser dans vos tests.

### Étape 3 : Rendre visible

* Tout le monde dans l'équipe doit être conscient de l'impact du code qu'il écrit. [Webpack bundle analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) est un excellent moyen de visualiser ce qui se trouve dans les bundles de sortie. Les gens pourraient réfléchir à deux fois avant d'utiliser une bibliothèque qui augmente la taille globale de 10 %.
* [import cost](https://github.com/wix/import-cost) pour VSCode vous montrera combien de code vous ajoutez au projet en utilisant certaines dépendances. Encore une fois, il s'agit de s'assurer que tout le monde est pleinement conscient de l'impact de ce qu'il fait.

### Étape 4 : Faire respecter et autonomiser

* Vous devez être prêt à faire respecter des règles strictes au sein de l'organisation. Dans notre cas, nous avons créé une [checklist de performance](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/checklist.md) à suivre sur chaque projet.
* Assurez-vous que **tout le monde** dans l'équipe travaille sur les tâches d'optimisation de la performance. Vous ne voulez pas avoir une seule personne qui le fait, car vous retombez dans le scénario du consultant. En répartissant les tâches, tout le monde se familiarise avec le contexte et les différentes façons de prévenir les problèmes.

La construction d'une culture orientée **performance** est un processus étape par étape. Et c'est un processus de **compréhension** des problèmes et d'**action** sur ceux-ci.

Une constante dans tout le processus est le besoin d'**éduquer** les gens.

Les techniques d'optimisation de la performance ne sont pas compliquées. Mais elles nécessitent un certain bagage technique et une bonne compréhension du fonctionnement du web.

Construire sur une base solide peut aider votre équipe à maîtriser même les techniques les plus avancées pour accélérer votre application.

Dans notre cas, nous nous assurons que la performance web fait partie du parcours d'apprentissage de tous les ingénieurs. Nous ne nous contentons pas de faire respecter une checklist. Nous nous assurons que les gens disposent d'un bon environnement pour apprendre les raisons derrière les techniques.

![Image](https://cdn-media-1.freecodecamp.org/images/hkpZovJ1oITO9WFs3xjZzrDaUKIPzwyZ2Ig6)
_[Affiche de la checklist de performance](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/performance-cheatsheet.png" rel="noopener" target="_blank" title=") dans notre bureau chez Fortech_

## La performance comme partie de la qualité logicielle

En fin de compte, travailler sur la performance revient à travailler sur l'UX, la sécurité ou l'accessibilité. Cela fait partie de la **qualité logicielle** que vous offrez.

Parfois, cela peut sembler être un effort supplémentaire pour quelque chose qui ne vous est pas demandé. La performance ne fait peut-être pas partie de vos exigences non fonctionnelles, après tout.

Mais en revenant à l'idée de responsabilité, c'est notre devoir de fournir la meilleure qualité possible. Et la performance est l'un des piliers de la qualité logicielle.

Si je devais résumer le chemin vers une culture de la performance, voici les points clés à retenir :

* Sensibiliser et construire avec empathie pour l'utilisateur
* Privilégier l'approche proactive et traiter les problèmes à l'avance
* Mesurer et agir en boucle continue
* Diffuser les connaissances et impliquer toute l'équipe dans le processus
* En faire partie de votre qualité logicielle comme objectif final

## Références

Puisque beaucoup de gens demandent des matériaux sur la performance web, voici quelques endroits où vous pouvez commencer :

* Le [portail Google Developers](https://developers.google.com/web/fundamentals/performance/why-performance-matters/) propose de grands articles sur les techniques d'optimisation de la performance
* [perf-tooling.today](https://www.perf-tooling.today/) offre de nombreuses ressources sur la performance web
* La [publication de l'équipe Chrome Dev](https://medium.com/dev-channel) explore de nombreuses idées et études de cas sur l'amélioration de la performance des sites web populaires.
* Consultez notre [checklist de performance sur github](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/checklist.md) et contribuez avec des idées !
* Jetez également un coup d'œil à la checklist de performance front-end 2018 de Smashing Magazine [front-end performance checklist](https://www.smashingmagazine.com/2018/01/front-end-performance-checklist-2018-pdf-pages/), elle est vraiment impressionnante !

Je suis super curieux d'entendre vos réflexions à ce sujet. Votre équipe adopte-t-elle une culture de la performance ? Qu'est-ce qui fonctionne pour vous ? Qu'est-ce qui ne fonctionne pas ? Laissez un commentaire et partagez si vous avez aimé cet article !