---
title: 'Kopernik : Une rétrospective sur un projet à but non lucratif'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-05-13T06:20:37.000Z'
originalURL: https://freecodecamp.org/news/kopernik-retrospective-68685371b00b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2lwlomgyQBSf47Ug.png
tags: []
seo_title: 'Kopernik : Une rétrospective sur un projet à but non lucratif'
seo_desc: 'By freeCodeCamp

  A few days ago, we marked our first nonprofit project at Free Code Camp as shipped.
  It was a big milestone (both for us and Free Code Camp as its first delivered project).
  I feel very happy for being able to deliver a working piece of...'
---

Par freeCodeCamp

Il y a quelques jours, nous avons marqué notre premier projet à but non lucratif chez Free Code Camp comme expédié. C'était une grande étape (à la fois pour nous et pour Free Code Camp en tant que premier projet livré). Je me sens très heureux d'avoir pu livrer un logiciel fonctionnel, mais aussi parce que l'expérience a été fantastique et une première pour ma carrière. Kopernik m'a ouvert les yeux sur la manière dont la technologie, même sous ses formes les plus simples, peut impacter la vie de milliers de personnes, et comment nous pouvons tous en faire partie.

### Free Code Camp

![Image](https://cdn-media-1.freecodecamp.org/images/0*2lwlomgyQBSf47Ug.png)

Tout d'abord, je vais résumer ce que fait Free Code Camp : Free Code Camp est une communauté de développeurs web aspirants. Il se concentre sur le JavaScript full stack, et son programme se divise en deux parties. La première consiste en différents cours gratuits trouvés partout sur le web (bientôt en interne), correspondant à environ 100 heures, et la deuxième partie consiste à réaliser des projets concrets pour des organisations à but non lucratif, ce qui représente également environ 900 heures. Ainsi, à la fois les participants et les organisations à but non lucratif bénéficient des projets, et il n'y a pas d'argent impliqué dans le processus. C'est un gain-gain pour tout le monde.

### L'initiative Wonder Women de Kopernik

![Image](https://cdn-media-1.freecodecamp.org/images/0*xxEBf3s-7cU_YP2t.png)

Après avoir terminé les défis (le programme de Free Code Camp), j'ai été assigné à un projet (hourra !) avec un autre participant, Alex. Notre projet était pour une organisation à but non lucratif appelée Kopernik, avec des opérations dans de nombreux pays d'Asie, mais dans ce cas, il s'agissait de la branche indonésienne. Ce que fait Kopernik, c'est d'apporter des technologies propres à des régions très pauvres et reculées de l'Indonésie orientale, aidant les femmes et leurs familles à améliorer leur vie et à les autonomiser avec une entreprise. Vous pouvez en savoir plus en regardant cette vidéo :

### Le problème

> "Pour que Kopernik mesure l'impact de ce projet et améliore sa méthodologie de projet, nous devons enregistrer les données de vente de nos agents ainsi que certaines données sur les utilisateurs finaux des technologies. Plus tard, nous interviewons les utilisateurs finaux pour déterminer dans quelle mesure la technologie a amélioré leur vie.

> "Cependant, nos agents de vente et nos coordonnateurs de zone travaillent dans des régions où l'accès à Internet est limité, peu fiable et lent. Les utilisateurs ont généralement peu d'expérience avec les ordinateurs et les appareils. Les données de vente sont recueillies auprès de nos agents à l'aide de reçus papier, mais la mise en forme de ces données pour que Kopernik puisse en créer des rapports significatifs est un processus compliqué."

Comme vous pouvez le voir, ce projet posait de nombreux défis, y compris des utilisateurs finaux peu expérimentés et des conditions défavorables pour une application web. En fin de compte, ce problème s'est traduit par une application de capture de données capable de fonctionner hors ligne avec un téléchargement automatique lorsqu'une connexion était disponible, car dans les régions décrites, elle peut être coupée pendant des semaines. Cela nous a fait faire des recherches pendant quelques jours avant de décider d'opter pour une extension Chrome, afin de pouvoir exploiter le stockage local de Chrome et avoir des services en arrière-plan en cours d'exécution. Nous l'avons également choisie parce qu'un navigateur web est une interface familière et nous a permis de faire des mises à jour automatiques via la boutique d'applications. Une fois cette décision prise, nous étions prêts à commencer à coder.

### Amber, notre partie prenante à but non lucratif et MVP

Notre plus grand avantage pendant la réalisation du projet était d'avoir Amber comme partie prenante. Pour commencer, elle était très enthousiaste à propos du projet et nous a offert toute l'aide dont nous avions besoin. Elle a été rapide pour nous fournir toutes les polices, les graphiques, les exigences, les traductions et les comptes nécessaires à mesure que nous faisions des progrès. De plus, elle a été très proactive dans la promotion du projet auprès de ses collègues, afin que nous puissions obtenir autant de retours que possible.

De plus, Amber est une développeuse web/logicielle avec de nombreuses années d'expérience, et elle a été très rapide à identifier les bugs et les problèmes d'utilisabilité. Cela nous a aidés à avancer et à livrer finalement une meilleure application. De plus, elle nous a toujours fait sentir comme faisant partie de Kopernik lui-même, et nous étions vraiment heureux de savoir que ce projet allait aider leur cause. Cela m'a vraiment fait espérer pouvoir travailler pour une organisation à but non lucratif comme celle-ci à temps plein à l'avenir.

### Défis et enseignements

Bien sûr, l'une des idées de la réalisation d'un projet réel est d'avoir l'opportunité d'apprendre et de mettre en pratique tout ce qui a été appris en réalisant les défis. Dans ce contexte, cela m'a beaucoup aidé à améliorer mes compétences en HTML et CSS, car le formulaire lui-même est très personnalisé dans son format. Obtenir le bon layout n'a pas été aussi facile que nous le pensions initialement. Cela m'a également beaucoup aidé à comprendre certains concepts de UX, car nous avons ajouté de nombreuses fonctionnalités visuelles et fait de nombreuses modifications à mesure que le projet progressait. Certaines soirées ont été passées à lire des documents, mais les récompenses en valent la peine.

Concernant les défis que nous avons rencontrés, je dirais que plus que des problèmes de code qui surviennent tout le temps dans chaque projet, le grand défi a été de synchroniser avec mon partenaire, car certaines tâches étaient interdépendantes et faire un git merge n'a pas toujours donné le résultat attendu. J'ai également manqué un peu plus de pairing pour être plus aligné sur ce que nous faisions. Mais je pense que cette expérience nous a également aidés à mieux définir les tâches qui étaient assignées et à segmenter le code pour qu'il soit plus facile de travailler en parallèle, un besoin réel dans chaque projet impliquant plus d'un développeur.

### Le projet

![Image](https://cdn-media-1.freecodecamp.org/images/0*wqvhw6IlIw38ectl.jpg)

Le projet se composait de deux sous-projets : une application frontale, sous la forme d'une extension Chrome, et une application back-end, qui expose un point de terminaison API pour recevoir les données envoyées par l'application de formulaire.

Côté front-end, il y a le formulaire, utilisant du **HTML** et **CSS** normaux (pas de préprocesseurs), un script pour gérer l'état du réseau et la transmission des données, un autre script pour gérer les fonctions de stockage en utilisant l'**API de stockage local Chrome** et un autre script pour gérer l'interactivité et la validation du formulaire. La seule dépendance utilisée était **jQuery** 2.1.3 pour gérer les sélecteurs, les retours visuels et **Ajax**.

Il y a également une étape de construction utilisant **Gulp** qui minifie les fichiers HTML, CSS et JavaScript, et optimise les images et les polices. La taille finale de l'extension une fois emballée était de 85KB incluant jQuery. Côté back-end, l'application utilise **Node.js** (0.12.1) avec **Express.js** pour le point de terminaison API. Les données reçues sont validées avec une clé API (pour la sécurité) et stockées dans une base de données **MongoDB** distante en utilisant **Mongoose**. Un processus récupère ensuite les données stockées et les convertit en un fichier .csv, qui est à son tour téléchargé sur un serveur **sFTP** distant. À l'avenir, il aura une intégration plus étroite avec un système CRM. L'application elle-même s'exécute sur **Heroku**, et le déploiement est géré par **Wercker**, qui ajoute des capacités de test (non utilisées pour l'instant) à la construction et découple le dépôt source avec le dépôt de l'application Heroku. Un outil supplémentaire utilisé était l'ajout de **New Relic** (niveau gratuit) pour le suivi des performances et des temps d'arrêt. Le code source sera disponible bientôt une fois que nous nous serons assurés qu'aucune référence aux serveurs de production n'est trouvée dans le code.

### Réflexions finales

![Image](https://cdn-media-1.freecodecamp.org/images/0*7mqB5LJZV_VRyEEx.jpg)

Cela me remplit vraiment de joie d'être arrivé aussi loin avec le projet et avec Free Code Camp. Travailler avec Kopernik a été l'une de mes meilleures expériences en matière de projet et j'espère vraiment que cela pourra aider la fondation à améliorer sa logistique et sa portée. Certainement, je veux continuer à améliorer l'application et à ajouter plus de fonctionnalités si nécessaire, bien que je sache que je ne suis pas tenu de le faire.

Je veux également remercier Michael et Quincy de nous avoir donné l'opportunité de réaliser des projets comme celui-ci et de rendre Free Code Camp meilleur chaque jour. Voici une vidéo qu'Amber chez Kopernik a créée pour remercier la communauté Free Code Camp :

Enfin, je pense que la réalisation de projets comme celui-ci aidera, sans aucun doute, toute personne poursuivant une carrière dans le développement web à améliorer ses chances de trouver un emploi à l'avenir, et m'a confirmé que je suis sur la bonne voie en faisant partie de ce bootcamp. Maintenant, passons au projet suivant.

Cristián Berríos est un développeur full stack JavaScript en devenir, basé à Mexico City. Vous devriez [le suivre sur Twitter ici](https://twitter.com/intent/user?screen_name=cbcodes).

_Initialement publié sur [blog.freecodecamp.com](http://blog.freecodecamp.com/2015/04/kopernik-retrospective-my-first-nonprofit-project-at-free-code-camp.html) le 1er avril 2015._