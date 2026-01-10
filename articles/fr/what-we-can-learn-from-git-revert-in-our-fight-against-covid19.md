---
title: Leçons que nous pouvons tirer de Git Revert dans notre lutte contre le COVID-19
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-08T07:17:58.000Z'
originalURL: https://freecodecamp.org/news/what-we-can-learn-from-git-revert-in-our-fight-against-covid19
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bbb740569d1a4ca2d97.jpg
tags:
- name: Covid-19
  slug: covid-19
- name: development
  slug: development
- name: Life Lesson
  slug: life-lesson
- name: Spain
  slug: spain
seo_title: Leçons que nous pouvons tirer de Git Revert dans notre lutte contre le
  COVID-19
seo_desc: 'By Syk Houdeib

  In this article, I''ll discuss how a small tech team found itself in the middle
  of a national emergency in Spain. And what their use of git revert can teach us
  about dealing with COVID-19 in our personal lives.

  Intro

  It was late in the ...'
---

Par Syk Houdeib

Dans cet article, je vais discuter de la manière dont une petite équipe technique s'est retrouvée au cœur d'une urgence nationale en Espagne. Et ce que leur utilisation de git revert peut nous apprendre sur la gestion du COVID-19 dans nos vies personnelles.

## Introduction

C'était en fin d'après-midi, le mercredi 11 mars 2020. Il ne restait que quelques-uns d'entre nous dans le bureau au centre de Madrid lorsque nous avons été informés d'emporter nos ordinateurs portables chez nous aujourd'hui. À partir du lendemain, nous devions travailler à distance jusqu'à nouvel ordre. 

Deux jours plus tôt, le gouvernement avait fermé toutes les écoles et universités en raison de l'urgence du Coronavirus. Il y avait beaucoup d'incertitude, et les choses changeaient à un rythme rapide. Aucun de nous ne savait vraiment ce qui allait se passer ensuite.

L'ambiance est devenue sombre alors que nous faisions nos affaires. Nous avons commencé à faire des prédictions sombres sur la durée avant notre retour. Peu savions-nous que nous étions à quelques jours d'une déclaration de l'état d'urgence à l'échelle nationale. Et qu'au moment où j'écris ces lignes, nous sommes encore à des semaines de retourner dans ce bureau au centre de Madrid.

Je veux partager avec vous cet article en deux sections. La première, un rapide tour d'horizon de la manière dont mon équipe s'est retrouvée au centre de cette urgence nationale. Pour vous donner une idée de la manière dont nous avons réagi. 

Mais en essence, je partage cela avec vous parce que j'ai trouvé une leçon précieuse dans cette réponse pour ma vie personnelle. Et j'espère que vous aussi pourrez y trouver une certaine valeur alors que nous faisons tous face à cette crise du COVID-19 qui s'aggrave et au monde changeant autour de nous.

Au cœur de tout cela se trouve une petite case à cocher intitulée "Revert".

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-176.png)
_Photo par [Unsplash](https://unsplash.com/@martinsanchez?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Martin Sanchez</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Dans l'œil du cyclone

Je suis développeur front-end chez Lola Market. C'est une startup espagnole basée à Madrid. Notre activité consiste à offrir une plateforme pour les courses en ligne. Les utilisateurs peuvent faire leurs courses en ligne parmi une large sélection de marchés et de supermarchés. Leurs commandes sont ensuite envoyées à des acheteurs qui peuvent les livrer à leur domicile en moins d'une heure.

Cela est soudainement devenu un service essentiel en ce moment. Si vous lisez ceci et que vous faites partie des millions de personnes actuellement confinées en raison du coronavirus, je n'ai pas besoin de vous expliquer pourquoi. Mais pour la postérité, je le ferai. Croyez-le ou non, tout cela passera bientôt, et il viendra un moment où ce ne sera pas aussi évident qu'aujourd'hui.

Une fois que le gouvernement espagnol a déclaré l'état d'urgence, tout le pays est entré en confinement. Les gens n'étaient plus autorisés à quitter leur domicile sauf pour les essentiels. 

Certains groupes étaient en quarantaine totale, ce qui ne leur permettait pas de quitter la maison du tout. Cela inclut les personnes présentant des symptômes de COVID-19. Ceux qui ont été en contact avec une personne testée positive. Ou les personnes appartenant à des groupes à haut risque.

Compte tenu de tout cela, faire ses courses en ligne et se les faire livrer à domicile n'était plus une commodité. C'était désormais une nécessité pour de nombreuses personnes.

Lola Market, à la veille de la déclaration de l'état d'urgence, était encore une petite startup. J'y suis depuis près de deux ans, période pendant laquelle nous avons connu une croissance régulière et impressionnante. 

Nous avions changé de bureaux il y a un an et avions presque doublé notre effectif. Mais nous n'étions toujours que 40 personnes au total. L'équipe technique est composée de 11 personnes, dont 8 développeurs. Notre équipe de service client est encore plus petite.

Le PDG, quelques semaines plus tôt, parlait de se préparer au moment de croissance exponentielle vers lequel nous travaillions. Mais nous n'avions aucune idée qu'une pandémie mondiale allait nous propulser là-bas si tôt à cette vitesse vertigineuse. 

## L'inondation

Une fois l'état d'urgence déclaré, nous avons instantanément commencé à battre tous les records. Nous avons regardé le nombre de commandes exploser.

Au début, tout s'est bien passé. Mais les chiffres ont continué à augmenter. À la deuxième semaine de confinement, la demande avait dépassé tout ce qui pouvait être géré. 

Le service client était submergé par des milliers d'e-mails et d'appels. Les opérations étaient en difficulté car les supermarchés souffraient de graves pénuries, de longues files d'attente, de fermetures précoces et de nombreuses restrictions. Ainsi que du manque d'acheteurs pour répondre à la demande.

Et notre infrastructure technique a commencé à souffrir sous une pression qui ne venait pas seulement d'une énorme augmentation du trafic. Mais aussi parce que les outils que nous avions étaient utilisés de manière atypique qui ne suivait pas ce à quoi nous étions habitués avec notre utilisateur habituel avant l'urgence. Tout le pays était stressé et sous pression. Tout le monde devait couvrir ses besoins essentiels.

Il faut compter ses bénédictions. Personnellement, j'étais reconnaissant d'être dans cette situation. Tout autour de moi, des gens perdaient leur emploi en un clin d'œil. 

Et ce n'était pas seulement que nous avions un emploi, c'était que notre travail nous donnait la sensation de contribuer au soulagement dans un état d'urgence. Même si c'était de la manière la plus petite possible. Cela nous donnait un but et rendait ce que nous faisions utile. Et c'est plus que ce que l'on pourrait demander dans une situation aussi difficile.

## Le changement

Dès le début, nous avons eu une réunion et notre CTO nous a expliqué comment nous devions changer nos priorités et répondre au changement soudain.

Nous étions au milieu d'un sprint important, en train de finaliser les derniers projets du trimestre. Mais la plupart de ces projets n'étaient plus une priorité. Le sprint devait être suspendu alors que nous commencions à traiter les questions plus urgentes qui se posaient.

La première semaine, nous devions trouver des moyens d'aider le reste de l'équipe dans d'autres départements à faire face au grand volume auquel ils étaient confrontés.

Même quelque chose d'aussi simple que déplacer un menu dans un outil interne pour le rendre facilement accessible pouvait faire gagner des heures de travail lorsque vous êtes confronté à une demande aussi soudaine. Mais à la deuxième semaine, nous avions des problèmes encore plus sérieux à résoudre pour pouvoir absorber et contrôler la hausse de la demande sur notre infrastructure.

## Les changements

Au cours de ces dernières semaines, nous avons dû mettre en œuvre de nombreux changements à la volée pour faire face à cette situation en constante évolution. Certaines des choses confiées à l'équipe technique pour résoudre incluaient : 

* Afficher des informations dynamiques et plus claires à nos utilisateurs sur la situation et sur l'état de leurs commandes.
* Simplifier et automatiser certaines parties du processus d'intégration de nouveaux acheteurs pour accélérer le processus et aider à répondre à la demande.
* Essayer de montrer une disponibilité plus réaliste des créneaux de livraison.
* Grandes améliorations et optimisations de l'infrastructure, des performances, des outils de service client, des outils d'exploitation et de l'application des acheteurs.
* Automatisation de nombreuses tâches internes, en particulier celles qui sont devenues répétitives.
* Alléger la charge de l'API.

_Avertissement : Il s'agit d'un article personnel et non d'une déclaration officielle de l'entreprise. Au moment de l'écriture, nous sommes encore au cœur de l'action. Certains changements sont déjà déployés. D'autres sont encore en cours de mise en œuvre. Et la situation évolue constamment._

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-177.png)
_Photo par [Unsplash](https://unsplash.com/@glenncarstenspeters?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Glenn Carstens-Peters</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## La liste d'urgence

Vous pouvez imaginer que travailler dans de telles circonstances est un défi pour toute équipe, et encore plus pour une équipe de cette taille. Cela a été stressant et exaltant à parts égales. 

Mais j'ai de la chance de travailler avec une équipe aussi positive. Surtout l'équipe backend de 4 personnes qui a fait face stoïquement à des moments de crise totale et a trouvé des solutions à une vitesse étonnante.

Cela m'amène à l'élément qui relie les deux sections de cet article : la liste d'urgence.

Pour gérer toutes ces tâches et les changements constants, nous avons créé une liste d'urgence. Il s'agit d'une simple liste de tâches dans un tableau Notion. Au fur et à mesure que la situation évoluait, la liste n'a cessé de croître et les tâches ont continué à changer de priorité.

La partie la plus importante de cette liste pour notre histoire ici est la colonne intitulée "Revert". La colonne contient une case à cocher à côté de chaque tâche. C'est cette petite case à cocher qui a résonné en moi et m'a donné une idée sur la manière dont je devrais gérer cette crise sur un plan personnel également. 

## Revert 

Nous utilisons la case à cocher "Revert" pour indiquer clairement si une tâche doit être annulée une fois que tout cela sera terminé ou non.

Si la case à cocher "Revert" est cochée, cela signifie qu'il s'agit d'une tâche que nous effectuons maintenant pour résoudre un problème spécifique qui, une fois la crise terminée et que nous serons revenus à la normale, devra être annulée. 

C'est quelque chose qui n'a de valeur que dans cette urgence et son contexte. Cela sert un but maintenant, mais ne sera plus nécessaire plus tard. Beaucoup de ces changements seront, en fait, carrément nuisibles une fois l'urgence passée.

Si cette case à cocher n'est pas cochée, cela signifie que tout ce que nous changeons reste après la crise. C'est quelque chose que nous savions depuis longtemps que nous devions faire mais que nous n'avions pas encore fait. Mais à cause de cette situation, cela est devenu une priorité. 

Ou c'est quelque chose que nous n'avions pas vu et qui est devenu évident maintenant. Ce sont des choses pour nous aider à mieux évoluer et à améliorer notre service en général. Ce sont des choses qui règlent une dette technique qui est devenue vitale à payer. Ce sont des améliorations de notre base de code, de notre infrastructure ou de nos processus qui sont bénéfiques à long terme et pas seulement pour maintenant.

Ce que nous faisons, c'est que nous pensons à l'avenir, à ce qui se passe une fois que tout cela est passé. Parce que cela arrivera. Et la vie reprendra son cours naturel. Nous serons changés, et le monde autour de nous aussi. Mais la vie continuera.

Une pandémie à laquelle la plupart d'entre nous n'étaient pas préparés a semé le chaos dans nos vies et nos entreprises. Mais nous ne pouvons pas permettre à cette crise de créer un chaos total dans nos vies par la suite. Nous devons être préparés pour le moment où tout cela passera.

## Appliquer le revert à nos vies personnelles

Alors, comment tout cela se rapporte-t-il à nos vies alors que nous faisons face à ce monde du COVID-19 dans lequel nous vivons et à ses conséquences ?

Simplement, nous avons tous besoin d'une case à cocher "Revert". Nous en avons besoin à côté des nombreux changements que nous appliquons à nos vies. Des changements que nous appliquons pour faire face au virus, à nos emplois, à nos familles et au monde en général alors que nous naviguons dans cette situation sans précédent.

Pour ma part, je tiens une liste similaire pour ma vie personnelle. Nous pouvons tous avoir une liste comme celle-ci. Documentez-la de la manière que vous connaissez le mieux. Qu'il s'agisse d'une liste écrite, d'une liste mentale ou de tout autre type de documentation que vous utilisez habituellement. Cela n'a pas d'importance. Ce qui compte, c'est d'avoir cette case à cocher "Revert".

Alors que nous luttons tous contre cette situation extraordinaire et toute la peur, les difficultés, l'incertitude et même la tragédie qu'elle apporte avec elle. Nous avons tous une liste de choses que nous faisons nées de cette urgence.

Nous devons garder clair ce qui doit être annulé plus tard et ce qui doit rester. Nous formons très rapidement des habitudes. Beaucoup d'entre nous ont déjà passé un mois à l'intérieur. Beaucoup d'autres suivront bientôt alors que cette situation continue de se propager. Nous ne pouvons même pas dire combien de temps nous allons être dans cette situation.

Nous devons donc garder cette case à cocher "Revert" aussi proéminente que possible.

Nous devons examiner la liste des changements que nous appliquons à notre nouvelle réalité.

Si c'est quelque chose qui nous améliore, nous et nos vies, gardez cette case à cocher claire. Peut-être avez-vous réalisé que vous devriez appeler votre mère plus souvent. Ou cultiver vos vieilles amitiés. Ou passer plus de temps avec vos enfants. Ou ne jamais tenir pour acquis les câlins que vous pouvez donner à vos grands-parents. 

Peut-être est-ce quelque chose d'aussi simple que d'être reconnaissant de pouvoir boire une bière avec vos amis. Ou écouter un musicien de rue dans un coin de rue animé sur le chemin du retour du travail.

Marquez ceux-ci comme des habitudes à garder. Des choses à continuer à travailler et à améliorer après que cela soit passé.

Mais pour tout le reste, toutes ces choses qui ne seront pas utiles après. Nous devons cocher la case "Revert".

Toutes les choses qui nous aident à survivre à une épreuve, à faire face à cela, à y faire face. Toutes les peurs qui sont importantes pour nous tenir sur nos gardes et rester en sécurité. Toutes les précautions supplémentaires. La distanciation. Les petites choses que nous nous permettons. Les indulgences. Les excès. Toutes ces choses qui deviendront rapidement nuisibles pour nous dans une vie après le COVID-19.

Pour celles-ci, assurez-vous de cocher la case "Revert" avec un gros marqueur vert. ✅

Une fois que tout cela sera terminé, il sera temps de revenir en arrière. Temps de défaire tout cela et d'avancer.

## Conclusion

Merci d'avoir lu. J'espère que vous et vos proches restez en sécurité et que la vie revient à la normale pour nous tous très bientôt.  


Et bonne chance avec vos cases à cocher "Revert".