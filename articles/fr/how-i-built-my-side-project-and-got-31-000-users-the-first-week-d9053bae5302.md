---
title: Comment j'ai construit mon projet secondaire et obtenu 31 000 utilisateurs
  la première semaine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-27T15:44:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-side-project-and-got-31-000-users-the-first-week-d9053bae5302
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pmZbtGBrql8SS3sCqccktQ.jpeg
tags:
- name: Design
  slug: design
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit mon projet secondaire et obtenu 31 000 utilisateurs
  la première semaine
seo_desc: 'By Jurn W

  I love building side-projects. Seeing your own ideas come to life is amazing.

  Side-projects provide a creative outlet and are a great way to learn and experiment
  with new things.

  If your side-project takes off, it might even turn into a sta...'
---

Par Jurn W

J'adore construire des projets secondaires. Voir ses propres idées prendre vie est incroyable.

Les projets secondaires offrent une sortie créative et sont un excellent moyen d'apprendre et d'expérimenter de nouvelles choses.

Si votre projet secondaire décolle, il pourrait même se transformer en une startup. De nombreuses entreprises bien connues ont commencé comme des projets secondaires — Twitter, Slack, GitHub et Instagram, pour n'en nommer que quelques-unes.

Récemment, j'ai lancé un nouveau projet secondaire et j'ai réussi à obtenir 31 000 utilisateurs dans les 7 premiers jours après le lancement.

Le site web que j'ai construit s'appelle [Screely](https://www.screely.com/). Il vous permet de transformer instantanément une capture d'écran en une belle maquette de design, sans le tracas d'utiliser des modèles Photoshop ou Sketch.

Dans cet article, je vais vous dire comment j'ai eu l'idée, comment je l'ai construite et comment j'ai réussi à obtenir 31 000 utilisateurs dans les 7 premiers jours.

### Trouver une idée

L'idée de Screely est venue d'un chat de groupe de designers et de développeurs qui partagent et discutent de leurs projets. Souvent, ils partagent des captures d'écran pour demander des commentaires ou pour montrer un travail terminé.

Mais il y avait une personne dont les captures d'écran se distinguaient. Il partageait de belles images au lieu de simples captures d'écran comme tout le monde.

Elles ressemblaient davantage aux designs que l'on voit sur Dribbble ou Behance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pmZbtGBrql8SS3sCqccktQ.jpeg)
_Un exemple de capture d'écran_

Il s'est avéré qu'il avait fait un modèle personnalisé dans Sketch pour ajouter ces effets.

Je voulais que mes captures d'écran aient un aspect similaire. Mais je ne voulais pas concevoir mes propres modèles et devoir charger chaque nouvelle capture d'écran dans Sketch.

Je connaissais [Carbon](https://carbon.now.sh/?bg=rgba(171,%20184,%20195,%201)&t=seti&wt=none&l=auto&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=48px&ph=32px&ln=false&fm=Hack&fs=14px&si=false&es=2x&wm=false), un outil qui génère instantanément une belle image de votre **code**, mais je voulais quelque chose de similaire pour mes **captures d'écran**.

Je n'ai pas trouvé de site web qui faisait cela, alors j'ai décidé de le construire moi-même.

### Définir votre Produit Minimum Viable (MVP)

La première chose que je fais lorsque je commence à travailler sur un nouveau produit est de définir un MVP.

Il existe plusieurs définitions différentes de ce qu'est un MVP. Habituellement, il est décrit comme un produit avec le plus petit nombre de fonctionnalités qui résout toujours le problème.

Se limiter à construire uniquement un MVP est très important pour deux raisons.

Premièrement, vous vous empêchez de passer beaucoup de temps à construire un produit sans valider l'idée et savoir si c'est quelque chose que les autres veulent utiliser.

Deuxièmement, vous vous empêchez d'ajouter sans fin plus de fonctionnalités et de peaufiner votre produit.

Ce ne sont pas des mauvaises choses, bien sûr. Mais c'est un piège dangereux qui peut conduire à travailler sur votre produit pendant des mois ou des années avant de jamais le publier.

> _"En développement de produit, le produit minimum viable (MVP) est un produit avec juste assez de fonctionnalités pour satisfaire les premiers clients, et pour fournir des commentaires pour le développement futur" - [Wikipedia](https://en.wikipedia.org/wiki/Minimum_viable_product)_

Plus vous livrez rapidement votre MVP, plus vous pouvez valider rapidement votre idée et améliorer votre MVP avec les commentaires des utilisateurs.

Pour Screely, j'ai défini le MVP comme suit :

* Un utilisateur doit pouvoir choisir un fichier image local (jpg, png)
* Le système doit générer une image avec une fenêtre de maquette, une ombre de boîte et une couleur de fond
* Un utilisateur doit pouvoir changer la couleur de fond
* Un utilisateur doit pouvoir télécharger l'image générée

Bien sûr, il y avait beaucoup d'autres fonctionnalités que j'aurais aimé ajouter : glisser-déposer une image, des fonds dégradés, ou pouvoir tweeter l'image générée.

Mais aucune de ces fonctionnalités ne fait partie des fonctionnalités principales. Et comme je l'ai dit avant, il est important de se limiter pour le MVP, sinon vous commencez à vous lancer dans cette prolifération sans fin de fonctionnalités.

### Préparation

Avant de lancer mon éditeur de texte, j'ai exploré les solutions techniques potentielles et leurs avantages et inconvénients.

Après avoir fait quelques recherches, j'ai considéré 3 options différentes :

1. Utiliser un élément HTML canvas et JavaScript
2. Utiliser des éléments DOM réguliers et utiliser du HTML et CSS purs
3. Générer l'image côté serveur et retourner le résultat final

Chaque option avait ses avantages et ses inconvénients.

Par exemple, le rendu de l'image côté serveur éviterait les problèmes de compatibilité entre navigateurs. Mais en tant qu'utilisateur, je ne voudrais pas que mes captures d'écran soient envoyées à un serveur puisque je ne sais pas si elles sont sauvegardées ou utilisées de quelque manière que ce soit.

Cela nécessiterait également l'exécution d'un serveur, alors que je pourrais héberger une solution purement front-end gratuitement sur [Netlify](https://www.netlify.com/). Donc l'option trois était exclue.

Avec les deux premières options restantes. J'ai finalement décidé d'utiliser l'élément HTML `<canvas>` et de peindre sur le canvas avec du JavaScript simple. De plus, comme je n'avais pas utilisé l'élément HTML canvas auparavant, et que les projets secondaires sont un excellent moyen d'apprendre de nouvelles choses, j'étais enclin à suivre cette voie. 💡

### Commençons à construire

La partie la plus excitante de tout projet.

J'ai immédiatement commencé avec les fonctionnalités de base. Je n'ai pas passé de temps sur un nom/domaine, un design, un logo, ou la mise en place des réseaux sociaux. Vous pouvez faire cela plus tard.

1 heure après le début du projet, j'avais les bases les plus élémentaires qui fonctionnaient.

* Un nom de remplissage - sexy screenshots (c'est ce que nous appelions ces images dans le chat de groupe)
* Une entrée de fichier
* Un élément `<canvas>` généré avec l'image que je sélectionne avec un fond coloré et avec la fausse fenêtre ajoutée

![Image](https://cdn-media-1.freecodecamp.org/images/1*fhish_gZ0T2hHsC7CBHBDw.gif)
_Fonctionnalité de base de l'application_

J'ai codé en dur tout, et cela ne fonctionnait qu'avec une (spécifique) capture d'écran. Vous ne pouviez pas changer la couleur de fond, ou utiliser une capture d'écran avec des dimensions d'image différentes.

J'ai amélioré le produit à partir de là, en commençant par la capacité à gérer différentes tailles de captures d'écran.

J'ai également commencé à ajouter les autres fonctionnalités que j'avais définies pour le MVP, comme l'ajout d'un sélecteur de couleur pour changer la couleur de fond et un bouton de téléchargement pour l'image générée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wU0UwOKhg4ZKZmDyAlG2tA.gif)
_Démonstration du sélecteur de couleur_

Maintenant que toutes les exigences du MVP que j'avais fixées au début étaient satisfaites, il était temps de lancer (oui, déjà) !

### Préparation pour le lancement

À ce stade, mon MVP n'était rien de plus qu'un titre de remplissage, un bouton HTML et une petite liste de choses que je voulais ajouter après le lancement du MVP.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3VigELJUhmUPCnViE2U3ww.png)
_MVP, pas prêt à être lancé (encore)_

Après avoir choisi un nom (Screely), acheté le domaine .com et créé une page de destination, voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*up1fp28FspXTTdcVVPYuNA.png)

J'ai également ajouté une option d'inscription par e-mail et un lien vers un compte Twitter pour m'assurer de pouvoir rester en contact avec les utilisateurs après le lancement.

Une autre chose que j'ai ajoutée était un bouton de chat en bas à droite pour que les utilisateurs puissent facilement me parler. J'ai reçu des commentaires précieux sur le produit, des rapports de bugs et des suggestions de fonctionnalités là-bas.

Il existe de nombreuses options que vous pouvez utiliser pour intégrer un chat à votre produit. J'ai utilisé Drift mais vous pouvez également utiliser des alternatives telles que Intercom ou Olark.

#### Construire en public

Une rapide note sur le lancement de votre projet : **le lancement ne doit pas être un événement d'un jour où vous partagez votre projet et espérez le meilleur.**

Votre "lancement" commence le jour où vous commencez à travailler sur votre idée. Vous devriez commencer à promouvoir votre projet dès le premier jour.

Lorsque j'ai commencé à travailler sur Screely, j'ai tweeté sur ma progression juste une heure après avoir commencé. J'ai également tweeté des mises à jour régulières pendant que je construisais le MVP.

Cela aide à sensibiliser les gens à votre nouveau produit, suscite la curiosité et vous aide à obtenir des commentaires.

Ne soyez pas gêné de montrer un produit inachevé. Les gens adorent voir les autres construire des choses cool et comprennent qu'il faut du temps pour construire des projets cool.

### Lancement

J'ai publié Screely sur Product Hunt, Hacker News, Reddit, Designer News et quelques autres sites web.

Je ne vais pas entrer dans les détails sur où publier votre produit et les meilleures pratiques pour chaque plateforme, car c'est un sujet qui mérite un article à part entière.

L'essentiel est que vous atteigniez votre public cible. Pour Screely, il s'agissait principalement de designers, de développeurs et de rédacteurs techniques.

#### Product Hunt

Le lancement sur Product Hunt s'est extrêmement bien passé et a dépassé toutes mes attentes. Screely a fini par devenir le [produit n°1 du jour](https://www.producthunt.com/posts/screely) avec 1032 votes positifs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oKvwlrmVueEh3mQIyk0sOQ.jpeg)

Screely était le produit n°1 du jour, le produit n°1 de la semaine et le produit n°4 du mois. Cela signifiait qu'il apparaîtrait également dans la newsletter quotidienne et hebdomadaire de Product Hunt.

Au total, Product Hunt a apporté près de 11k visiteurs la première semaine !

#### Hacker News

Screely a commencé assez lentement mais après quelques heures, il a soudainement grimpé à la première page de Hacker News. Même si la position la plus élevée de Screely était "seulement" n°15, cela a tout de même entraîné beaucoup de trafic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iT9BB1q5pPgjDXrfGJ6TGA.png)

J'estime que 5 à 10k utilisateurs sont venus de Hacker News.

Il n'est pas clair exactement combien d'utilisateurs sont venus de HN car il n'ajoute pas de paramètre `?ref=` à l'URL. J'ai inclus un regard plus détaillé sur les sources de trafic plus tard dans cet article.

#### Designer News

La troisième plateforme la plus réussie (en termes de chiffres de trafic) était designernews.com.

Screely est arrivé à la 2ème place de la page d'accueil et cela a entraîné juste sous les 3k nouveaux utilisateurs.

#### Devenir viral

J'avais publié Screely sur de nombreux autres endroits, comme Reddit et Indie Hackers, mais les trois précédents étaient de loin les plus réussis.

Un effet secondaire intéressant de bien performer sur des plateformes comme Hacker News et Product Hunt est que votre produit apparaît sur de nombreux autres endroits — tweets, newsletters, blogs plus petits, agrégateurs et plus encore.

Par exemple, Screely a été mentionné par CSS tricks à leurs 360k abonnés.

Screely a également été inclus dans [Codrops Collective #416](https://tympanus.net/codrops/collective/collective-416/), une newsletter populaire parmi les designers.

Au total, Screely avait juste sous les 31 000 utilisateurs la toute première semaine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8o3Y-DGgGAYpRbyVF2A0yQ.png)
_Gauche : total des utilisateurs par jour, Droite : source du trafic. Source : Google Analytics_

### Améliorer avec les commentaires des utilisateurs

Étant donné le succès du lancement, je peux dire en toute confiance que l'idée a été validée. Maintenant, je sais qu'il vaut la peine de consacrer plus de temps à ce projet.

Vous vous souvenez de la fonction de chat que j'ai implémentée pour préparer le lancement de Screely ? Elle était remplie de demandes de fonctionnalités et de commentaires des utilisateurs de Screely.

Maintenant que vous savez exactement ce que vos utilisateurs veulent, il est facile de savoir quelles fonctionnalités travailler et quoi prioriser.

Par exemple, de nombreux utilisateurs voulaient pouvoir glisser-déposer leur image dans Screely, alors j'ai ajouté cette fonctionnalité en premier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XafYwAWmCGni0K5DDAMf7w.gif)
_Support Glisser-Déposer_

Une autre fonctionnalité souvent demandée était de faire correspondre automatiquement la couleur de fond avec l'image. Ainsi, vous avez immédiatement un fond qui convient à votre capture d'écran.

J'ai ajouté un script qui analyse l'image, génère une palette de couleurs et choisit la couleur la plus dominante pour le fond.

En plus d'ajouter de nouvelles fonctionnalités et de corriger des bugs, j'ai également passé du temps à peaufiner le design.

_Si vous voulez recevoir des mises à jour sur Screely. Suivez [@getScreely](https://twitter.com/getScreely) sur Twitter, ou inscrivez-vous à la mise à jour mensuelle du produit par e-mail sur [screely.com](https://www.screely.com/)._

### Conseils pour livrer vos projets secondaires (plus rapidement)

* **Gardez-le simple** : Gardez votre MVP aussi limité que possible. Utilisez des langages de programmation que vous maîtrisez au lieu du framework à la mode. Plus votre projet devient complexe, plus il prend de temps à livrer et à obtenir vos premiers utilisateurs.
* **Livrez tous les jours** : Maintenir l'élan dans vos projets secondaires est super important. Essayez de travailler sur votre projet tous les jours. Refactorisez une seule fonction ou corrigez un petit problème CSS. Peu importe la taille de la tâche que vous accomplissez, continuez à livrer ! Si vous sautez un jour (ça arrive), faites-en une priorité absolue de faire quelque chose, peu importe la taille, le lendemain.
* **Prenez des raccourcis** : Chaque fois que possible, essayez de trouver des raccourcis pour livrer votre produit plus rapidement. Si vous pouvez trouver une bonne solution open-source pour un problème, utilisez-la au lieu d'écrire la vôtre à partir de zéro. Utilisez des outils comme Netlify pour héberger et déployer au lieu de configurer votre propre serveur.
* **Lancez avant de penser que vous êtes prêt** : Ne vous laissez pas piéger par la perfection de votre produit. Vous pouvez vous en sortir avec beaucoup plus que vous ne le pensez.
* **La programmation est un outil pour faire connaître votre idée au monde** : Ne sur-ingéniez pas votre projet secondaire. Vos utilisateurs ne se soucient pas de votre stack technique, ce qui compte pour eux est le bénéfice qu'ils tirent de l'utilisation de votre produit. Ils ne se soucient pas si vous utilisez Docker ou React, ils se concentrent sur le problème que votre produit peut résoudre pour eux.
* **Vous en savez assez** : De nombreuses personnes qui apprennent à coder reportent le travail sur leurs propres projets. Ils pensent souvent qu'ils doivent suivre plus de tutoriels, acheter plus de cours et lire plus de livres. N'apprenez pas indéfiniment, commencez à construire ! Même les développeurs expérimentés cherchent encore des choses 'simples' comme comment supprimer un élément d'un tableau.

Bonne chance et amusez-vous !

Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements. ✨

Je suis un designer UI/UX freelance néerlandais et développeur front-end. Je gère également quelques sites web d'affiliation réussis et je construis des projets secondaires pour le plaisir et le profit.

Si vous voulez savoir sur quoi je travaille actuellement, [suivez-moi sur Twitter](https://twitter.com/jurn_w) ou consultez [mon blog](https://jurn.blog/).

N'hésitez pas à me tweeter avec toutes les questions que vous avez, je suis toujours heureux d'aider !