---
title: La Meilleure Façon d'Apprendre le Développement Web Backend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-12T14:38:22.000Z'
originalURL: https://freecodecamp.org/news/learn-backend-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bab740569d1a4ca2d39.jpg
tags:
- name: Backend Development
  slug: backend-development
- name: Web Development
  slug: web-development
seo_title: La Meilleure Façon d'Apprendre le Développement Web Backend
seo_desc: 'By Mehul Mohan

  My previous article described how you can get into frontend development. It also
  discussed how the front end can be a place filled with landmines – step in the wrong
  place and you''ll be overwhelmed by the many frameworks of the JavaScr...'
---

Par Mehul Mohan

Mon article précédent décrivait [comment se lancer dans le développement frontend](https://www.freecodecamp.org/news/learn-frontend-web-development/). Il y était également question de la manière dont le frontend peut être un terrain miné – un faux pas et vous serez submergé par les nombreux frameworks de l'écosystème JavaScript. 

Dans cet article de blog, voyons comment se lancer dans le développement backend. En cours de route, je répondrai à certaines des questions les plus courantes que les gens me posent à ce sujet.

## Qu'est-ce que le Développement Backend ?

Le développement frontend concerne ce qu'un utilisateur voit à l'écran lorsqu'il ouvre une URL spécifique que vous possédez. Même dans un environnement complètement statique (avec uniquement HTML/CSS), lorsqu'une personne ouvre un site web, un serveur quelque part sur la planète doit vous répondre avec ces fichiers HTML et CSS. 

Ce serveur n'est qu'un ordinateur, comme celui que vous utilisez pour naviguer sur Internet. Mais il a été optimisé pour la performance et n'a pas de composants inutiles comme une souris ou un clavier. Et il se trouve avec des tonnes d'autres ordinateurs, probablement dans un entrepôt de données. 

Programmer ces ordinateurs de manière spéciale s'appelle le **développement backend**.

Vous pourriez penser que le développement backend est appelé ainsi parce qu'il fonctionne en arrière-plan de l'utilisateur. Un visiteur de votre site web n'accède jamais vraiment complètement au backend. Il communique simplement avec votre serveur, soit directement via des ports pour un accès très limité (comme le transfert de fichiers HTML/CSS), soit même pas cela – profondément enfoui sous des CDN ou des pare-feu (comme Cloudflare).

Maintenant que nous avons une compréhension brute de ce que signifie le développement backend, passons à quelques **vraies** questions.

## La connaissance de la programmation frontend est-elle nécessaire pour le backend ?

**TLDR ;** Non.

Le développement backend, comme mentionné ci-dessus, implique la programmation d'un ordinateur situé probablement de l'autre côté de la planète, responsable de la réponse aux requêtes des utilisateurs depuis leurs propres ordinateurs. 

Si vous êtes un développeur backend à temps plein, vous n'avez pas vraiment besoin de vous soucier de ce qui se passe à l'intérieur de ces fichiers HTML, CSS et JavaScript que vous envoyez au navigateur de l'utilisateur. Au lieu de cela, vous devez vous concentrer davantage sur la performance du serveur, le code du serveur et le débit.

## Qu'est-ce qui entre dans le développement backend ?

Eh bien, selon les livres, vous pourriez dire qu'une personne qui code une application capable de répondre aux requêtes HTTP est un développeur backend. 

Mais en réalité, parfois les développeurs backend sont capables de faire bien plus que simplement écrire des scripts serveur. Ils ont les connaissances pour configurer des serveurs proxy inversés (NGiNX/HAProxy), activer la compression et d'autres moyens pour accélérer le site, et configurer un environnement docker de production.

Pour être qualifié en tant que développeur backend, je dirais que les compétences minimales dont vous avez besoin sont :

1. Bonne connaissance d'un langage de programmation dans lequel vous pouvez écrire des serveurs HTTP. Exemples : C#, Java, Node, PHP, Python, etc. (il y en a beaucoup !)
2. Savoir héberger en utilisant cPanel (traditionnel) ou en utilisant le terminal bash (hébergement cloud/traditionnel)
3. Travailler avec des systèmes de contrôle de version (VCS) comme git pour gérer et déployer des builds

Tout comme chaque jeu vient avec des spécifications minimales et recommandées, pour les développeurs backend, mes spécifications recommandées seraient (y compris les compétences minimales) :

1. NGiNX pour les actifs de fichiers statiques et la gestion du serveur
2. Compétences en gestion de bases de données (SQL/NoSQL)
3. Sécurité du backend (Écrire du code sûr et robuste, exécuter des applications dans des conteneurs docker avec des privilèges limités, protection contre les attaques DoS)
4. Autoscaling/Équilibrage de charge

D'accord, assez parlé de ce qui entre dans le développement backend. Mais comment devenir un développeur backend ?

## Commencez avec les exigences minimales

Comme je l'ai dit, pour le backend, tout comme les jeux, nous avons un ensemble d'exigences minimales et recommandées. Les exigences minimales consistent en 3 choses :

### Apprendre un langage de programmation backend

Lorsque les gens apprennent par eux-mêmes, ils n'ont généralement pas d'équipe ou quelqu'un qui peut faire du développement frontend. Ils sont seuls. Vous devrez donc souvent créer des pages web et des serveurs tout seul, au moins au début. 

Bien qu'il y ait beaucoup de choix pour les langages de programmation backend, et je ne peux pas penser à un langage système populaire qui ne supporte pas les serveurs HTTP dès la sortie de la boîte. L'avantage de choisir Node est que vos compétences en JavaScript frontend sont transférables au backend.

Néanmoins, vous pouvez choisir parmi une variété de langages comme Java, C++, C#, Python, PHP, etc.

Comment en choisir un, pourriez-vous demander. La réponse est la même que dans l'article sur le développement frontend : vous devez tout essayer au début et voir lequel vous convient le mieux. 

Node est facile car vous avez peut-être déjà fait de la programmation JS pour le frontend. Mais si vous êtes un développeur Python ou Java, vous pourriez trouver ces langages faciles à apprendre. Cela dépend entièrement de votre profession et de vos goûts.

### Apprendre à gérer l'hébergement

Les jours où vous deviez acheter manuellement des serveurs et les installer chez vous, les connecter à votre FAI, faire tout cela vous-même, sont révolus. Nous sommes à l'ère de l'informatique en nuage. Maintenant, lorsque vous hébergez votre site web, vous avez principalement 2 options :

1. Opter pour des serveurs d'hébergement gérés comme HostGator ou GoDaddy.
2. Opter pour des fournisseurs d'hébergement cloud comme GCP, AWS ou DigitalOcean.

Quelle est la différence entre les deux ? Dans les deux cas, les serveurs sont détenus et exploités par les entreprises respectives. Mais la principale différence est que l'hébergement géré est plus convivial avec une interface graphique, dispose d'un ensemble riche d'outils pour voir le système de fichiers, surveiller l'utilisation, gérer vos emails de domaine officiels, télécharger/télécharger des fichiers depuis votre serveur, et ainsi de suite. C'est essentiellement une configuration pour les personnes ayant moins de compétences techniques. 

Pour cette raison, je ne recommande pas les sites gérés comme HostGator ou GoDaddy pour les développeurs expérimentés. Cependant, cela peut être une bonne plateforme pour faire des erreurs et apprendre, principalement parce que vous avez généralement des plans prépayés pour eux. Vous aurez également une belle interface utilisateur pour gérer les choses, ce qui ne vous permet pas de faire exploser accidentellement vos factures.

Mais lorsque vous commencez à prendre de la vitesse, je vous recommande de passer à un fournisseur de cloud. Cela supprime tous les outils sympas de cPanel que vous utilisiez pour gérer les fichiers et dossiers sur les serveurs. Mais en même temps, cela vous mettra au défi de monter en compétences. 

Aujourd'hui, de nombreux fournisseurs de cloud offrent également un essai gratuit décent, afin que vous puissiez réellement essayer leur plateforme avant de vous engager pleinement. J'héberge mon site web pour développeurs - codedamn - sur DigitalOcean et le trouve à un bon équilibre entre la complexité du site et les fonctionnalités. 

Vous pouvez utiliser [ce lien pour vous inscrire](https://m.do.co/c/2c4c3ec5405a) sur DigitalOcean et obtenir **100 $ de crédits gratuits**. Les instances DigitalOcean coûtent aussi peu que 5 $ par mois, vous avez donc une marge de manœuvre d'environ 20 mois sur cette instance, une bonne affaire, n'est-ce pas ?

Quoi qu'il en soit, vous pouvez choisir n'importe quel fournisseur de cloud. Ensuite, il est important d'apprendre à gérer le serveur en utilisant uniquement la ligne de commande en vous connectant via ssh.

### Apprendre les Systèmes de Contrôle de Version

Il existe d'autres solutions en plus de Git pour les VCS. Mais Git est le plus utilisé et le plus simple à comprendre. 

En tant qu'individu, vous ne l'apprécierez peut-être pas tout de suite. Mais vous comprendrez pourquoi c'est si important dès que vous commencerez à travailler soit en équipe, soit sur plusieurs fonctionnalités simultanément dans votre projet. 

Git vous permet de gérer votre flux de travail en utilisant des commits et des branches. Les commits sont comme des **points de contrôle** dans votre base de code - ceux auxquels vous pouvez toujours revenir si vous faites une erreur. 

Les branches sont comme des **réalités alternatives** de votre projet, où quelque chose de complètement différent pourrait se produire. Ces réalités alternatives peuvent être créées à partir de n'importe quel point dans le temps et peuvent être fusionnées à nouveau à n'importe quel moment. 

Si ces réalités peuvent être fusionnées ensemble avec compatibilité, alors c'est bien. Mais s'il y a un conflit (comme si vous êtes vivant dans une réalité et mort dans une autre), alors vous devez faire un choix manuellement. Les autres changements peuvent être fusionnés automatiquement.

Git est super intéressant, et une fois que vous l'aurez compris, vous voudrez l'utiliser dans tous vos projets. Vous pouvez garder un historique de votre travail de manière efficace (il compresse et stocke uniquement la différence entre les commits). 

Il vous permet également de créer des dépôts git en ligne sur des sites comme GitHub, qui agit comme une source centrale de vérité pour votre site web. Des sites comme GitHub peuvent être configurés avec des webhooks spéciaux qui peuvent réellement mettre à jour votre site web chaque fois que vous ajoutez un nouveau point de contrôle (un nouveau commit) sans que vous ayez jamais besoin de vous rendre manuellement sur le serveur et de le mettre à jour vous-même.

## Optez pour les compétences recommandées

Je suis un grand croyant de l'apprentissage par la pratique. Et la meilleure façon de faire quelque chose vient de la nécessité ou de l'intérêt. Une fois que vous vous considérez assez bon avec les exigences minimales, il est temps d'acquérir les compétences recommandées. Cela inclut tous les outils comme Docker et NGiNX mentionnés ci-dessus. 

**DevOps** est également quelque chose qui s'intègre super bien avec les développeurs backend. Vous pourriez essayer et explorer **TravisCI** ou **CircleCI** pour les déploiements de builds automatisés. L'Intégration et le Déploiement Continus (CI/CD) est un sujet qui pourrait faire l'objet d'un autre article de blog complet, je ne vais donc pas entrer dans les détails. En fait, une fois qu'il est correctement configuré, il vous fera économiser une quantité ridicule de temps de développement !

Ensuite, viennent les bases de données, que j'ai placées dans les compétences recommandées. Mais vous aurez besoin de bases de données pour presque toutes les applications qui impliquent une certaine forme de persistance des données générées par l'utilisateur. 

Les bases de données sont généralement faciles à commencer à utiliser, mais plus difficiles à maintenir et à ajuster correctement. La meilleure façon de commencer à travailler sur une stack technologique backend est d'avoir tout ensemble sur un seul serveur - le code de votre application, les serveurs proxy inversés, la base de données, etc. Ensuite, à mesure que vous devenez plus compétent dans chaque domaine, vous pouvez le découpler de la logique métier existante. 

En faisant cela, vous activez une architecture qui peut être hautement scalable. Une application intensive en opérations de base de données pourrait avoir une solution optimisée pour les bases de données. Et un site lié à un trafic important devrait avoir un bon mécanisme CDN pour décharger les actifs statiques, et ainsi de suite.

## Conclusion

Il y a tant de choses à apprendre, mais tout est réalisable si vous ne abandonnez pas. Faites-moi savoir ce que vous pensez de cet article via mes comptes [**twitter**](https://twitter.com/mehulmpt) et [**Instagram**](https://instagram.com/mehulmpt). Cela signifierait beaucoup pour moi si nous nous connectons là-bas ! 

De plus, si vous êtes intéressé, consultez [**codedamn**](https://codedamn.com) - une plateforme axée sur les développeurs pour apprendre des technologies comme le développement backend ! J'ai même publié une [vidéo YT sur la création de votre propre serveur de site web simple en 2 minutes](https://www.youtube.com/watch?v=IOTL7RqUZEU)! Consultez cela et faites-moi savoir ce que vous en pensez!

Paix !