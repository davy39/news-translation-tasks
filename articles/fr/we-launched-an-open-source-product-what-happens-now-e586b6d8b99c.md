---
title: Nous venons de lancer un produit open source. Alors, que se passe-t-il ensuite
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-09T15:17:05.000Z'
originalURL: https://freecodecamp.org/news/we-launched-an-open-source-product-what-happens-now-e586b6d8b99c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-m9PuNCzweMOUaJb.png
tags:
- name: Design
  slug: design
- name: Entrepreneurship
  slug: entrepreneurship
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Nous venons de lancer un produit open source. Alors, que se passe-t-il
  ensuite ?
seo_desc: 'By Victor F. Santos

  Last month me and the ninja god Pedro launched GitShowcase, a plug-and-play portfolio
  for developers. Open source and free.

  It’s quite simple what the product does. It fetches GitHub user info and projects
  to craft an one-page lay...'
---

Par Victor F. Santos

Le mois dernier, Pedro et moi avons lancé [GitShowcase](http://www.gitshowcase.com/), un portfolio clé en main pour les développeurs. Open source et gratuit.

Ce que fait le produit est assez simple. Il récupère les informations de l'utilisateur GitHub et les projets pour créer une mise en page d'une seule page, [comme ceci](https://www.gitshowcase.com/showcasecat).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SOYAm8dehW0aP7qNZ95O3Q.png)
_Rencontrez Ludmilla, le super chat de présentation._

Dans cet article, je vais parler de la façon dont nous avons obtenu plus de 25 000 projets présentés par des utilisateurs de 80 pays différents en un seul mois, et de la manière dont nous prévoyons d'en tirer des revenus. Nous espérons que cela sera utile aux passionnés de produits. Allons-y pour l'open source ! :)

### Pourquoi nous avons créé GitShowcase

Les développeurs sont des artisans incroyables. Personne ne le nierait. Mais lorsqu'ils postulent à de nouveaux emplois, la plupart d'entre eux ont du mal à trouver un bon moyen de présenter leur travail. Habituellement, ils cherchent des modèles pré-faits ou des outils CMS (Content Management System) personnalisés pour développer leurs sites web personnels.

Nous avons simplifié les choses pour les développeurs pressés. Pas d'inscriptions compliquées, pas de formulaires à remplir, pas de code. Juste un bouton pour se connecter avec un compte GitHub. Après une connexion en un clic, toutes les informations pertinentes et les projets sont affichés dans une mise en page personnalisable d'une seule page.

J'étais responsable du design et Pedro de l'ingénierie. Ironiquement, GitShowcase était censé être seulement un projet secondaire à mettre dans nos portfolios et c'est tout, mais la communauté nous a poussés dans une autre direction...

### L'embrassement de la communauté

Nous avons publié GitShowcase dans quelques groupes de développement brésiliens sur Facebook pour recueillir des commentaires. Nous avons été submergés par beaucoup de gens formidables qui interagissaient avec les publications et les recommandaient à leurs amis.

En seulement quelques heures, nous avions déjà plus de 4 000 projets présentés sur la plateforme. La partie la plus surprenante était que beaucoup d'entre eux ne venaient pas du Brésil.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4uQU1568PJ_2gGTo.png)

### Notre stratégie de croissance

Nous étions un peu effrayés par les chiffres. Comment allions-nous maintenir ce rythme de croissance ? Nous n'avions pas de budget pour faire de la publicité, ni pour promouvoir le site web d'une autre manière que de façon organique.

Nous avons concentré nos efforts sur trois piliers pour voir comment cela se performerait :

1. **Les réseaux sociaux** – La source qui nous a rendus visibles dans le monde. Nous avons continué à publier GitShowcase dans d'autres groupes via Facebook, LinkedIn, et à contacter des influenceurs technologiques sur Twitter pour faire tester GitShowcase. Nous avons également rendu les boutons de partage plus visibles et actionnables sur les pages.
2. **Le marketing de contenu** – Pedro aime écrire sur la vie technologique. Il a donc commencé à écrire sur GitShowcase, comme notre stack technique, notre processus, notre livraison, etc., et à les publier sur [Hackernoon](http://hackernoon.com/) et d'autres blogs. Consultez son [Medium](http://medium.com/@pedsmoreira/) si vous êtes intéressé par la livraison d'applications.
3. **SEO** – Il s'agit d'une stratégie plus à long terme. Nous avons réfléchi aux mots-clés pour lesquels nous voulons être bien classés : « portfolio de développeur », « portfolio github », « site web de développeur », afin que les utilisateurs puissent nous trouver organiquement via la recherche Google. Pour les profils, nous avons préparé des mots-clés dynamiques : « gitshowcase + nom d'utilisateur », « portfolio de développeur + nom d'utilisateur », pour obtenir des recherches spécifiques d'utilisateurs liées à notre site web également. Nous avons également diffusé le lien GitShowcase sous les commentaires de célèbres articles de blog pour travailler sur notre netlinking (et pour attirer certains lecteurs curieux qui font défiler les pages pour nous rencontrer également).

### Alors, comment la stratégie a-t-elle performé ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*3vk-4iIiQeYyY8kj.png)

Les données ci-dessus représentent :

* À gauche : **sessions par source**. Nous identifierons laquelle des initiatives a apporté le plus de visiteurs sur le site web.
* À droite : **infographie sur le trafic par pays**. Nous verrons comment les personnes de différents pays ont visité le site web, combien se sont inscrites, quels sont les 10 premiers pays avec le plus d'inscriptions et quels sont les 10 premiers pays avec les meilleurs taux de conversion.

Avant de plonger, il est important de préciser que « _(direct) / none_ » et « _Github.com / referral_ » sont assez trompeurs. Nous ne les inclurons pas dans l'analyse car c'est confus même pour nous, voici pourquoi :

* **(direct) / none** – Cette source devrait représenter les personnes qui tapent directement gitshowcase.com dans leur navigateur et appuient sur entrer, mais Google Analytics a un bug depuis toujours et prend le crédit du trafic d'autres sources en raison d'une défaillance de suivi. Vous pouvez en lire plus à ce sujet [ici](http://blog.analytics-toolkit.com/2015/google-analytics-direct-none-source/).
* **Github.com / referral** – Nous utilisons l'API GitHub pour authentifier l'utilisateur, donc elle prend le crédit de la source de trafic lorsqu'elle renvoie à GitShowcase.

Nous allons maintenant supprimer les données trompeuses afin que vous puissiez voir des points de données plus précis.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3MtcR_35NR8YewwY.png)

### Cela semble mieux.

Voici comment les trois piliers ont contribué à la génération de trafic :

**Réseaux sociaux :** 2 429 sessions (50 % du trafic) ;

**Marketing de contenu :** 1 084 sessions (22,3 % du trafic) ;

**SEO :** 235 sessions (4,8 % du trafic).

### Oh, attendez. Que dire des autres 22,9 % ?

Ce sont notre **trafic de marketing par e-mail (3,6 %) et** **les références (19,3 %)**. Les références sont d'autres sites web avec des liens vers le nôtre. C'est quelque chose que nous n'avions pas cartographié au début lors de l'élaboration de la stratégie, d'autres personnes liant GitShowcase à leurs pages et newsletters.

Cela nous a surpris positivement car nous avons été présentés sur des sites vraiment cool, comme [Product Hunt](http://www.producthunt.com/posts/gitshowcase). Nous avons été chassés par un gentil gars israélien nommé Raz. Merci, mec ! [Voir GitShowcase sur Product Hunt.](http://www.producthunt.com/posts/gitshowcase)

Quelque chose qui est maintenant sur notre radar sont les références, qui deviennent notre 4e pilier — faire en sorte que d'autres sites web parlent de nous et nous recommandent.

Les réseaux sociaux ont été la meilleure source pour générer du trafic, comme nous nous y attendions. C'est là que les utilisateurs partagent leurs profils et discutent de l'outil, le tweetent, le recommandent, et d'autres peuvent nous rencontrer.

Le marketing de contenu a également été assez expressif. Les gens prêtent attention au contenu de bonne qualité et le récompensent avec leur temps.

Le SEO est encore un bébé, car nous construisons notre notoriété de marque et notre réputation avec les moteurs de recherche. Nous pensons qu'il deviendra plus efficace au cours des 3 prochains mois.

### D'accord, nous avons obtenu des inscriptions de personnes formidables dans le monde entier et certains sites web parlent de nous. Maintenant, comment en tirer de l'argent ?

C'est là où nous en sommes à ce moment-là. À mesure que la base grandit, les utilisateurs commencent à faire beaucoup de suggestions et à demander plus de fonctionnalités. Nous itérons le produit quotidiennement lorsque nous sommes chez nous après nos emplois à temps plein. Cela nous rend un peu sans sommeil. Nous nous sommes donc dit : « Serait-ce, disons, peut-être... le bon moment pour monétiser GitShowcase ? »

![Image](https://cdn-media-1.freecodecamp.org/images/0*6_WCjPSgxnNcb8F6.jpg)

Nous avons quelques idées sur la manière de faire de GitShowcase un produit freemium. En d'autres termes, les gens pourraient utiliser le plan de base gratuitement, et obtenir certaines fonctionnalités exclusives via des plans payants. Notre plan de base serait le même qu'aujourd'hui — un portfolio complet et automatisé. Les plans payants auraient la même chose, ainsi que quelques extras :

* **Un domaine personnalisé** — [www.username.com](http://www.username.com) au lieu de [https://www.gitshowcase.com/username](https://www.gitshowcase.com/username)
* **Accès à des modèles premium** — Des modèles artisanaux pour différents focus. Aujourd'hui, nous n'avons qu'un seul modèle, qui est principalement axé sur les projets.
* **Avantages de la zone de recrutement** — Les développeurs ont besoin de portfolios principalement pour les candidatures à des emplois, ou pour être chassés, donc la création d'une zone de recrutement semble être une évidence. Les recruteurs pourraient rechercher dans notre base de données pour trouver des développeurs avec des connaissances spécifiques, et ceux qui sont sur des plans payants apparaîtraient plus haut dans les résultats que ceux qui sont sur le plan de base.

### Temps pour une enquête

Avant de passer du temps à développer les fonctionnalités, nous avons réalisé une enquête auprès de nos utilisateurs pour comprendre si ces idées résonneraient avec leurs intérêts. Nous avons utilisé [Mailchimp](http://mailchimp.com/) pour envoyer l'e-mail et [Typeform](http://www.typeform.com/) pour l'activer.

### « Qu'est-ce qui manque aujourd'hui ? »

![Image](https://cdn-media-1.freecodecamp.org/images/0*rF4mprGs9Wvzc-tG.jpg)

Wow, des analyses et du contenu interne générique ? Nous avons juste mis ces options là pour remplir l'espace, mais apparemment, c'est ce que la plupart des gens veulent.

C'est pourquoi il est important d'écouter les utilisateurs. Nous sommes très biaisés par ce que nous pensons être une priorité.

### « Paieriez-vous pour cela ? »

![Image](https://cdn-media-1.freecodecamp.org/images/0*PoyhjMsCpuzAVx3L.jpg)

Je dois avouer que nous nous attendions à plus d'enthousiasme ici, même si nous savons qu'il est difficile de demander aux gens d'abstraire et d'imaginer qu'ils paient pour quelque chose qu'ils ne peuvent pas encore voir ou avec lequel ils ne peuvent pas interagir.

Eh bien, peut-être que ce n'est pas si mal... N'est-ce pas ? *retenant les larmes*

J'ai entendu dire une fois que les entreprises devraient écouter davantage les utilisateurs extrêmes des deux extrémités — les haters et les lovers. C'est là que vous pouvez voir des erreurs graves, et vous pouvez voir comment vous ajoutez une réelle valeur à la vie des gens. Les neutres ne se donneront pas la peine de vous dire grand-chose, car ils ne vous détestent ni ne vous aiment, donc cela vous maintient surtout au même endroit. Cela a du sens, je suppose...

### « Quel pourrait être un service qui vaut la peine d'être payé ? »

C'était la dernière question de l'enquête. Elle était ouverte, plus abstraite que les autres et non obligatoire, donc beaucoup de gens l'ont simplement laissée vide. **29 % ont exprimé leur avis**. Je vais essayer de condenser les réponses en trois personas :

**Hater :** Je me suis peut-être inscrit, mais n'essaie même pas de facturer quelque chose, je peux développer mon propre portfolio si je veux, vous capitalistes odieux !!!!

**Neutral :** C'est bon de facturer quelque chose, mais qu'en est-il d'un dollar symbolique par an juste pour avoir accès à GitShowcase ? C'est juste pour vous aider à payer les factures.

**Lover side :** J'aime l'idée du domaine personnalisé et je paierais pour cela. Le portfolio est vraiment cool. Mais les gars, avez-vous pensé à nous rapprocher des recruteurs ? Mec, c'est quelque chose qui me ferait tatouer le logo GitShowcase sur ma jambe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NOCOPxZxESW5WdQ5.jpg)

Cela était bien plus révélateur que les autres questions fermées. Nous ne ferons pas beaucoup de progrès sur de petites choses spécifiques que les développeurs peuvent coder eux-mêmes. Les domaines personnalisés sont toujours une chose car certaines personnes aimeraient que leur profil GitShowcase soit leur site web officiel.

Ce qui nous a vraiment fait réfléchir, c'est que nous avions prévu une zone de recrutement pour l'avenir, mais nous ne l'avons pas mise dans l'enquête car nous pensions que c'était une étape vraiment éloignée. Mais certains utilisateurs s'attendent déjà à ce que cela se produise. AUJOURD'HUI. Et ils sont en feu.

### Les recruteurs s'intéressent-ils à GitShowcase ?

Je me penche sur cette question. J'ai spammé quelques recruteurs technologiques de haut niveau dans mon réseau avec quelques questions pour voir quels outils ils utilisent actuellement, comment ils recherchent les candidats avant de les approcher, et s'ils sont intéressés par un endroit pour chasser les développeurs par connaissances spécifiques, localisation et projets.

Trois ont répondu. Tous avaient des retours positifs sur les perspectives d'utilisation de notre plateforme.

Connaissez-vous un recruteur technologique ? Taggez-le/la dans les commentaires s'il vous plaît. Nous sommes très ouverts à compter sur eux pour nous aider à façonner GitShowcase.

### Que allons-nous faire ensuite ?

Eh bien, il semble que nous ayons maintenant un plan. Et des tonnes de devoirs. Nous avons décidé de prioriser les tâches en équilibrant la pertinence et la facilité de mise en œuvre. Donc, voici ce que nous allons faire au cours des trois prochains mois :

* Fonctionnalité de domaine personnalisé
* Modèles modulaires pour enrichir le contenu du profil
* Une zone de recrutement de talents

### Pourquoi viens-je de vous raconter tous mes plans ?

Nous embrassons la culture open source. Même lorsque le bon sens pourrait dire le contraire, nous croyons que la transparence construit la confiance, tandis que le secret la repousse. Les gens ne devraient pas avoir peur de partager des connaissances et de parler ouvertement de leurs plans.

![Image](https://cdn-media-1.freecodecamp.org/images/0*sDjGc7KNViMU4ePY.jpg)

### Les leçons que nous avons apprises jusqu'à présent :

1. L'open source, c'est l'amour. L'open source, c'est la vie.
2. Les gens ne voleront pas le code parce qu'il est open source. En fait, les gens aident à construire le produit. [Forkez notre projet sur GitHub et aidez-nous aussi](https://github.com/gitshowcase/gitshowcase).
3. Le marketing de contenu fonctionne bien si le contenu est pertinent et publié aux bons endroits.
4. Si vous n'êtes pas sûr de quelque chose, demandez simplement. N'essaiez pas de falsifier quoi que ce soit dont vos utilisateurs dépendent.
5. Si votre produit ne résout pas un problème réel, aucune stratégie ne peut le sauver. Construisez un bon produit, et faites un peu de marketing pour faire connaître votre produit.

### Aimez l'article ? Aidez-nous en taggant un développeur ou un recruteur technologique dans les commentaires :)

Nous sommes un duo sans budget qui essaie de faire avancer les choses, donc tout le soutien est le bienvenu. Vous pouvez soit :

1. **Tagguer un développeur** dans les commentaires pour rencontrer [GitShowcase](http://www.gitshowcase.com/)
2. **Tagguer un recruteur technologique** pour qu'il jette un coup d'œil à ce que nous faisons ici. Nous ouvrirons bientôt le tableau de bord de recrutement de talents en version bêta.
3. **Aimer, commenter et partager** cet article pour l'aider à atteindre plus de personnes intéressantes comme vous.

Si vous lisez toujours ceci, vous êtes les meilleurs. Merci pour votre temps.

Suivez GitShowcase sur [Facebook](http://www.facebook.com/gitshowcase/), [Twitter](http://twitter.com/Gitshowcase) et [GitHub](http://github.com/gitshowcase/gitshowcase).