---
title: Pourquoi les projets open source (malheureusement) favorisent les nouveaux
  utilisateurs, et ce que vous pouvez faire à ce sujet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-19T16:18:15.000Z'
originalURL: https://freecodecamp.org/news/why-open-source-projects-sadly-favor-new-users-and-what-you-can-do-about-it-ba586038949e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m13n-rBdC5GtBhHN9nLqRQ.jpeg
tags:
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Pourquoi les projets open source (malheureusement) favorisent les nouveaux
  utilisateurs, et ce que vous pouvez faire à ce sujet
seo_desc: 'By Filip Hracek

  Every now and then, all developer products (SDKs, frameworks, APIs) will have to
  choose between favoring their existing users or new ones. Make the initial app “just
  work” for beginners with some default magic? You hurt the debuggabil...'
---

Par Filip Hracek

De temps en temps, tous les produits pour développeurs (SDK, frameworks, API) doivent choisir entre favoriser leurs utilisateurs existants ou les nouveaux. Faire en sorte que l'application initiale "fonctionne simplement" pour les débutants avec un peu de magie par défaut ? Vous nuisez à la débogabilité des grandes applications. Introduire une fonctionnalité pour vos utilisateurs avancés ? Les nouveaux venus devront gérer une courbe d'apprentissage plus raide.

En avril, j'ai écrit sur le ["Hello World" fallacy](https://medium.com/@filiph/the-hello-world-fallacy-ef4f43ca8b7e). Il s'agit de l'hypothèse inconsciente que si une technologie A est plus facile à prendre en main qu'une technologie B, alors A est meilleure que B.

C'est mauvais, car la plupart des développeurs, la plupart du temps, n'écrivent pas des applications "hello world". Ils tombent amoureux de la facilité à construire une démo. Puis, des mois plus tard, ils luttent en essayant de construire un produit réel.

Mais c'est pire.

Ce n'est pas seulement une question de perception. Favoriser le scénario "Hello World" **paie réellement à long terme** si vous construisez une bibliothèque ou un framework open source. Malheureusement, vous avez tout intérêt à sacrifier la productivité de vos utilisateurs à long terme pour faciliter les choses pour vos nouveaux utilisateurs.

Cela est dû à la dynamique de l'adoption technologique :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Diagramme simplifié de l'adoption des technologies par les développeurs. Dans le diagramme ci-dessus, nous avons deux technologies concurrentes, A et B. Leur adoption est proportionnelle au buzz (articles de blog, conférences, dépôts Github) autour d'elles, et à leur valeur perçue telle que rapportée par les utilisateurs actuels._

Il y a une **boucle de rétroaction renforçante** ici. Plus les gens essaient la technologie, plus le buzz est généré autour d'elle, donc plus les gens l'essaient, et ainsi de suite.

Après un certain temps, les développeurs cessent d'utiliser la technologie et passent à autre chose. Ce **taux de désabonnement** est proportionnel à leur insatisfaction envers la technologie et à son âge.

Le problème réside dans les **délais**. La boucle de rétroaction renforçante des nouveaux utilisateurs est presque immédiate. Les premiers articles de blog commencent à apparaître après quelques semaines. Mais le taux de désabonnement et les articles plus informés apparaissent beaucoup plus tard, après plusieurs mois. Il faut du temps pour construire quelque chose de réel. Vous devez construire quelque chose de réel avant de pouvoir parler de la technologie sous-jacente de manière informée.

Supposons que la technologie A soit optimisée pour la facilité d'utilisation initiale ("hello world" et petites applications). La technologie B est optimisée pour les utilisateurs à long terme (applications réelles). **Si la technologie A obtient deux fois plus de buzz initial de la part des nouveaux utilisateurs que la technologie B, et que la technologie B obtient deux fois plus de buzz informé que la technologie A, alors la technologie A gagne toujours — et de loin.** Cela est dû, dans notre petit modèle, au fait que le buzz informé suit le buzz initial avec un retard moyen de 12 semaines. C'est tout ce qu'il faut. La technologie A attirera de nouveaux utilisateurs à un rythme beaucoup plus rapide. Elle perdra également des utilisateurs plus rapidement que la technologie B. Mais ce taux de désabonnement se produit beaucoup plus tard et, en général, plus lentement que dans la phase d'adoption.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Résultat d'une simple simulation._

Au moment où la technologie A perd son avantage, c'est déjà terminé. Les deux technologies sont sur leur lent déclin. La technologie A aura été utilisée par presque deux fois plus de développeurs à ce moment-là. **Malgré le fait qu'elle soit pire pour construire des applications réelles.**

Supposons que la technologie B aille jusqu'au bout. Elle optimise à l'extrême l'expérience utilisateur à long terme et dé-priorise complètement le scénario "hello world". Le résultat est encore plus triste :

![Image](https://cdn-media-1.freecodecamp.org/images/BUkKnp4j0Vf98G-ent7nW9MaWNHrxSFgi0s6)

Peu importe comment vous jouez avec les chiffres, la technologie B perd toujours. La boucle de rétroaction renforçante et le délai de désabonnement seront toujours présents.

Examinons exactement ce que j'entends par "optimiser pour les nouveaux utilisateurs" versus "optimiser pour les utilisateurs à long terme".

#### Ce qui est important pour les nouveaux utilisateurs (premières semaines ou mois) :

* Longueur et facilité de la première installation
* Défauts et automagie (capacité à "fonctionner simplement" pour les scénarios initiaux les plus courants)
* Taille des petites applications
* Performance des petites applications
* Liberté ("utilisez ce à quoi vous êtes habitué")

#### Ce qui est important pour les utilisateurs à long terme (une fois qu'ils ont construit une grande application) :

* Facilité de refactorisation
* Explicité (le principe "ne surprenez pas le programmeur")
* Personnalisation
* Taille des grandes applications
* Performance des grandes applications
* Standardisation

### Pourquoi est-ce un problème open source ?

Une des grandes choses à propos de l'open source est qu'il est gratuit. Dans ce cas, c'est aussi une partie du problème.

Les SDK et frameworks payants ne verront jamais le taux d'adoption de l'open source. Mais ils sont aussi le business de quelqu'un. Les entreprises tendent à préférer les clients à long terme aux nouvelles pistes incertaines. Si la technologie A était une entreprise, elle ne s'en sortirait pas bien.

Veuillez noter : Je ne dis _pas_ que nous devrions tous commencer à payer pour les frameworks maintenant. Je cherche simplement à expliquer pourquoi l'open source est particulièrement vulnérable à ce problème.

Je crois que c'est l'une des raisons de la "[JavaScript fatigue](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f)" dans le monde du web, d'ailleurs. Cet écosystème sélectionne naturellement les technologies qui sont faciles à prendre en main. Cela crée une course aux armements : les nouvelles générations de bibliothèques et de frameworks sont de plus en plus faciles pour les nouveaux venus, mais plus difficiles à mettre à l'échelle.

Les technologies qui _n'_optimisent _pas_ pour le "hello world" sont condamnées à l'obscurité. Vous vous retrouvez avec une succession rapide de technologies qui sont innovantes mais pas idéales pour construire de grands projets logiciels.

![Image](https://cdn-media-1.freecodecamp.org/images/A8msxeLS903u5vJe9wO1kbOjvsrdkq9Klhvz)
_Comparaison de la durée de vie de .NET avec celle de knockout.js._

Ce n'est pas seulement l'écosystème JavaScript, bien sûr. Le monde entier des produits pour développeurs voit des rotations plus rapides. Le framework .NET a 15 ans cette année, et il est toujours utilisé. C'est un vestige d'une ancienne époque. Aujourd'hui, même en dehors de l'écosystème web, nous voyons des frameworks qui "règnent" pendant 18 mois puis meurent.

### Que pouvons-nous faire à ce sujet ?

J'espère avoir montré que cela ne concerne pas les propriétaires de frameworks et de bibliothèques étant malhonnêtes, myopes ou stupides. Le problème est inhérent à l'écosystème. Il découle des retards de feedback — quelque chose que personne ne peut vraiment faire (sauf s'ils possèdent une machine à remonter le temps).

En tant que propriétaire de bibliothèque, si vous "choisissez de ne pas jouer", vous nuirez considérablement aux chances de succès de votre projet. Vous deviendrez la technologie B.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Cela étant dit, les propriétaires de frameworks _peuvent_ être conscients de cela. Ils peuvent éduquer sur la scalabilité des logiciels. Ils peuvent rechercher leurs plus grands "clients" et travailler étroitement avec eux. Ils peuvent mettre l'accent de manière consciente et transparente sur les grandes applications plutôt que sur les démonstrations technologiques. Mon espoir est que l'industrie commence à le faire dans son ensemble. C'est dans l'intérêt de tous.

Pour les consommateurs de ces frameworks (et SDK, bibliothèques, API), le conseil est assez simple :

**N'écoutez jamais quelqu'un qui n'a pas construit une très grande* application avec la technologie dont il parle.**

(* La taille de l'application dépend de ce que _vous_ voulez construire.)

Le problème avec ce conseil est probablement clair. Si vous vivez selon lui, vous allez manquer chaque nouvelle technologie cool qui existe. Au moment où quelqu'un construit quelque chose de suffisamment grand, et est donc compétent pour en parler, vous pourriez très bien être trop en retard pour la fête.

J'ai donc quelques conseils moins glorieux mais plus pratiques pour vous :

* **Prenez note des personnes sur le projet et de leur historique.** Le comportement passé est le meilleur prédicteur du comportement futur.
* **Ignorez l'expérience "hello world".** Sachez que 99,99 % de votre temps avec la technologie ne sera _pas_ "hello world".
* **Méfiez-vous de la "magie" implicite.** Cela ne se mélange presque jamais bien avec les applications réelles.
* **Réduisez les recommandations des personnes qui ne construisent que de petites applications ou des preuves de concept.**
* **Si vous voulez être sophistiqué, construisez des "générateurs d'applications" qui produisent automatiquement de très grandes bases de code dans les technologies que vous évaluez.** Avec cela, vous pouvez produire une approximation d'une énorme application de 100KLOC en un seul après-midi. Voyez comment l'application générée de grande taille performe et comment l'outil tient à cette échelle. (C'est ce que l'équipe AngularDart chez Google fait pour évaluer la position de son propre framework parmi les autres.)

Si vous avez d'autres idées, n'hésitez pas à les partager dans les commentaires. Je les ajouterai volontiers ci-dessus.