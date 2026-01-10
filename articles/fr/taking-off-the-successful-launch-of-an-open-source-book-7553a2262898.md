---
title: Comment lancer votre propre livre open source populaire et rentable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-03T20:29:18.000Z'
originalURL: https://freecodecamp.org/news/taking-off-the-successful-launch-of-an-open-source-book-7553a2262898
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i0W3owJAB1oR57Bu6v1_Hw.jpeg
tags:
- name: books
  slug: books
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: Comment lancer votre propre livre open source populaire et rentable
seo_desc: 'By Baptiste Pesquet

  I am the author of The JavaScript Way, a self-published open source book for learning
  to code. Despite the lack of any initial audience, it topped GitHub trending charts
  worldwide during its launch.

  This is the story of this unexp...'
---

Par Baptiste Pesquet

Je suis l'auteur de [The JavaScript Way](https://github.com/bpesquet/thejsway), un livre open source auto-édité pour apprendre à coder. Malgré l'absence de public initial, il a atteint les premières places des tendances GitHub dans le monde lors de son lancement.

Voici l'histoire de ce succès inattendu.

### Genèse du projet

Au début de ce projet, j'ai [expliqué](https://medium.com/@bpesquet/walk-this-javascript-way-e9c45ab5b696) pourquoi je l'ai commencé et j'ai passé en revue certains de mes choix initiaux. En bref :

* Il y avait un besoin pour un livre enseignant le JavaScript moderne aux débutants.
* J'ai décidé d'auto-éditer ce livre et de l'écrire en open source sur [GitHub](https://github.com). En faisant cela, j'espérais atteindre autant de personnes que possible. De plus, tirer parti du grand [modèle collaboratif](https://en.wikipedia.org/wiki/Open-source_model) qui est au cœur de l'open source.
* Le livre aurait une licence Creative Commons [BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/). Elle permet à quiconque de partager ou de s'appuyer sur mon travail tant que certaines règles sont respectées. En particulier, aucun usage commercial en dehors du mien n'est autorisé.

De plus, certains facteurs clés dans la décision étaient :

* Le texte est toujours un excellent moyen de transmettre des connaissances. Donc, le choix d'un livre plutôt que du matériel basé sur des vidéos.
* J'avais déjà écrit deux cours en ligne sur le même sujet ([ici](https://openclassrooms.com/courses/learn-the-basics-of-javascript) et [là](https://openclassrooms.com/courses/use-javascript-on-the-web)). Les retours sur ceux-ci ont été très positifs, donc je savais que j'avais un contenu assez solide à portée de main.
* Je voulais perfectionner mes compétences en JavaScript, et je savais par expérience que enseigner quelque chose est un excellent moyen de le maîtriser.

Ce qui me manquait, c'était un public initial, souvent considéré comme un atout critique pour ce type de projet. Comme quelqu'un doit bien commencer quelque part, je me suis lancé quand même.

### Choix d'un modèle économique

Chaque créateur est confronté au même dilemme. Comment partager votre travail avec le monde de manière à avoir un impact et à être rentable ? Il n'y a pas de réponse définitive à cette question séculaire.

La révolution numérique a bouleversé les choses pour les auteurs. Elle a réduit les coûts de distribution et de partage à zéro. Dans notre "économie de la réputation", les créateurs de contenu doivent se battre pour attirer l'attention des consommateurs. En tant que nouveau venu dans ce domaine, rencontrer le succès sera très difficile si tout votre contenu est derrière un paywall. Une partie de celui-ci doit être disponible gratuitement.

Pour les auteurs, la tactique marketing la plus courante est désormais de diviser votre travail en plusieurs parties. La première, gratuite, donne aux clients potentiels un aperçu de votre contenu et de votre style. Dans l'espoir que les clients accrochés achèteront les autres parties.

Le choix alternatif de Kyle Simpson pour sa série de livres [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS) assez réussie m'a plu. Comme lui, j'ai décidé de donner tout le contenu du livre gratuitement, mais de laisser les utilisateurs payer pour une meilleure expérience de lecture via la version ebook.

En m'inspirant d'un [autre best-seller auto-édité](https://leanpub.com/rprogramming), j'ai choisi d'inclure des exercices de codage et des projets directement dans le livre, mais de vendre leurs solutions en supplément.

Ce modèle économique "hybride" semblait être un équilibre raisonnable entre ouverture et profit potentiel.

### Construire un public (ou non)

Un autre conseil marketing courant est de construire un public via une liste de diffusion, en utilisant du contenu existant (par exemple, votre propre blog) comme aimant.

Je n'aime pas beaucoup cette approche et je ne voulais pas ennuyer mes lecteurs avec un quelconque abonnement.

J'ai également envisagé de lancer une campagne de crowdfunding. Sans aucun public initial, cela me semblait être beaucoup de travail pour un résultat très incertain, donc je m'en suis éloigné. Peut-être la prochaine fois !

### Outils et processus

Le meilleur format de fichier pour écrire un livre (pas seulement technique) est le **texte brut**. Pas besoin d'un éditeur dédié. Pas de problème d'interopérabilité. La possibilité d'utiliser un système de [contrôle de version](https://en.wikipedia.org/wiki/Version_control) comme [Git](https://git-scm.com/) pour suivre les changements.

Parmi les divers langages de balisage basés sur du texte disponibles, j'ai choisi [Markdown](https://en.wikipedia.org/wiki/Markdown) parce que je connaissais déjà et aimais sa syntaxe. Markdown est également un citoyen de première classe sur GitHub, ce qui était essentiel pour ce projet.

Un auteur auto-édité a besoin d'une chaîne d'outils pour transformer les fichiers de manuscrit brut en divers formats d'ebook (PDF, EPUB, MOBI). Pour moi, la plateforme [Leanpub](https://leanpub.com) cochait toutes les cases : support Markdown, intégration avec GitHub et une structure de royalties équitable (90% moins 50 cents par vente).

J'ai utilisé l'éditeur de texte gratuit [Visual Studio Code](https://code.visualstudio.com/) pour écrire les fichiers du livre sur mon ordinateur. Il a un excellent support Markdown dès la sortie de la boîte et un aperçu de fichier côte à côte très pratique (voir l'image ci-dessous). Des extensions comme [Markdown Shortcuts](https://marketplace.visualstudio.com/items?itemName=mdickin.markdown-shortcuts) et [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) peuvent être installées pour devenir encore plus productif.

![Image](https://cdn-media-1.freecodecamp.org/images/Y5eTbqW4dc3WfElzvEWI2vEcnVTc3UfilwkK)

Après que tous les outils ont été choisis, j'ai rédigé le plan du livre (une première étape très importante) en utilisant mes cours précédents comme base. Ensuite, je me suis plongé dans le processus d'écriture.

### Publication précoce

Le slogan de Leanpub est "Publiez tôt, publiez souvent". La plateforme vous permet de publier des brouillons précoces de votre travail. Recevez des commentaires et créez de l'élan, permettant une approche de type [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product) pour l'écriture de livres.

C'est une excellente idée sur le papier... Qui, malheureusement, n'a pas du tout fonctionné pour moi. Un mois après le début du processus d'écriture, j'ai rendu le livre public sur Leanpub. À cette époque, le prix de l'ebook était de 0$, donc n'importe qui pouvait l'obtenir gratuitement.

J'en ai parlé à mon réseau personnel, j'en ai [tweeté](https://twitter.com/bpesquet/status/836354787616641024), je l'ai soumis à [Reddit](https://www.reddit.com/r/javascript/comments/5wmw8q/the_javascript_way_a_new_book_for_learning_modern/) et [Hacker News](https://news.ycombinator.com/item?id=13749641). J'ai également contacté d'autres auteurs de livres ou des personnalités éminentes. J'ai également contacté Kyle Simpson, [Robin Wieruch](https://www.robinwieruch.de/) et [Quincy Larson](https://twitter.com/ossia) de freeCodeCamp, à la recherche de conseils et de soutien.

Le résultat a été mitigé. Quelques étoiles GitHub, une poignée de messages sur Twitter et Reddit. Un fil HN qui est sorti du sujet et a été enterré. L'exécution a été médiocre, le manque de public initial était un désavantage trop important.

La majorité des commentaires étaient du type "Contactez-moi quand ce sera terminé". Les gens ne veulent peut-être pas investir du temps à lire des livres en cours, ce qui est compréhensible après tout.

Mais, les réponses individuelles de Kyle, Robin et Quincy ont été chaleureuses. Ils ont joué un grand rôle pour me garder motivé. Je leur suis très reconnaissant.

### La phase d'écriture

Même après ce lancement précoce décevant, j'étais toujours convaincu que mon livre valait quelque chose. Je ne voulais pas abandonner après avoir déjà passé des dizaines d'heures dessus. En utilisant un plan de livre inchangé, j'ai opté pour une route sans feedback et j'ai continué à écrire tout seul jusqu'à ce que le livre soit terminé.

C'était la partie la plus difficile. Passer d'innombrables heures, jour après jour, pour voir les choses prendre forme très lentement. Inévitablement, des doutes surgissent : comment cela pourrait-il réussir ? Est-ce une perte de temps géante ? Pourquoi est-ce que je m'inflige cela ?

La clé pour surmonter ces obstacles est de **se mettre la bonne quantité de pression**. Si votre engagement en temps est trop rare, vous perdrez la motivation et abandonnerez. Mais, essayer d'avancer trop vite, en négligeant d'autres aspects importants de votre vie en cours de route, est risqué à bien des égards.

Après tout, ce n'était qu'un projet secondaire. Faible risque, faible pression ! L'auto-édition signifie que je n'avais pas de délais à respecter, ce qui peut être à la fois une bénédiction et une malédiction. J'ai essayé d'utiliser cela à mon avantage : j'étais libre d'investir du temps dans quelque chose en quoi je croyais, mais à mon propre rythme.

J'ai trouvé un équilibre raisonnable (environ 10 à 15 heures par semaine) entre le travail, la vie personnelle et le processus d'écriture. J'ai limité les longues et dangereuses pauses. Cet [article sur les projets secondaires](https://open.buffer.com/side-projects-creative-hobbies/) donne des conseils utiles pour garder les choses en marche pendant cette phase.

![Image](https://cdn-media-1.freecodecamp.org/images/vHUYXRM9s9XVXig3ZhqCoCA3nP2Br7Sinym7)
_Mes statistiques de commit sur GitHub pendant la phase d'écriture_

Heureusement, j'avais du matériel existant sur lequel m'appuyer. Une certaine expérience dans l'écriture de contenu de mon propre chef... Et aussi un conjoint très compréhensif ;)

### Jour du lancement

Après huit mois de travail régulier et quelques dernières heures passées fiévreusement à corriger des choses ici et là, mon livre était enfin prêt !

L'avantage d'écrire dans le vide comme je l'ai fait est que le lancement de votre livre devient un événement assez important. Après un tel investissement en temps, c'est une grande satisfaction (et aussi un énorme soulagement) de montrer votre création terminée au monde.

Par manque de mieux, j'ai réutilisé ma stratégie de lancement précédente. [Twitter](https://twitter.com/bpesquet/status/890564975596630017), [Reddit](https://www.reddit.com/r/javascript/comments/6poszc/the_javascript_way_a_new_book_for_learning_modern/) et [Hacker News](https://news.ycombinator.com/item?id=14865043) ([soumission du timing](https://www.quora.com/When-is-the-best-time-to-post-on-Hacker-News-to-get-and-stay-long-on-the-front-page) pour une visibilité maximale). De plus, les mêmes personnes sympathiques qui m'ont gardé motivé après le lancement précoce.

À ma grande surprise, le résultat a été cette fois-ci écrasant de positivité. Kyle Simpson et Quincy Larson ont gentiment tweeté à propos du livre à leurs dizaines de milliers de followers.

Heure après heure, j'ai regardé avec incrédulité les commentaires élogieux et les retweets s'accumuler dans ma boîte de réception. J'ai enfin su que mon livre aurait un impact.

Le lancement est également le moment béni où la magie de l'open source se produit. Les gens peuvent lire et partager votre livre gratuitement. Créer de l'élan sans aucun effort marketing. Mais ils peuvent aussi améliorer sa qualité grâce à des contributions utilisant les [issues](https://guides.github.com/features/issues/) et les [pull requests](https://help.github.com/articles/about-pull-requests/) de GitHub.

Comme je ne suis pas un natif anglais et que je n'avais pas d'éditeur à mes côtés pour vérifier le contenu, je savais que mon livre contenait de nombreuses fautes de frappe et erreurs au lancement. J'espérais que les gens aideraient à les repérer et à les corriger, et je n'ai pas été déçu.

Voici quelques chiffres recueillis deux jours après le lancement :

* Le dépôt du livre sur GitHub avait plus de **51k vues** de **17k visiteurs uniques**. La majeure partie de ce trafic provenait de Hacker News, suivi par Reddit.
* Il a gagné plus de **2,400 étoiles**, et est devenu le **dépôt #1 en tendance** dans le monde pendant une journée.
* L'histoire de Hacker News a grimpé à la **5ème place** sur la page d'accueil, générant plus d'une centaine de commentaires.
* Les lecteurs ont soumis **30 pull requests**, corrigeant beaucoup des erreurs initiales du livre. Principalement de petites fautes de frappe, mais aussi des améliorations grammaticales et même quelques erreurs de codage.
* J'ai déjà reçu **deux demandes de traduction**, en espagnol et en chinois.

Dans l'ensemble, bien plus que ce que je pouvais rêver.

### Résultat financier

Un livre open source peut-il être rentable après tout ? Bien sûr, il est trop tôt pour le dire. Deux jours après le lancement, il est devenu le livre le plus vendu de la semaine sur Leanpub, avec plus de **1,000 $** de royalties.

![Image](https://cdn-media-1.freecodecamp.org/images/7fU7sEq2J2tPqUKuOqKBIP7Z9nEBHlbpbwf8)
_Tableau de bord des royalties Leanpub deux jours après le lancement_

La rentabilité n'était pas la raison pour laquelle ce projet a été lancé en premier lieu. Pourtant, le modèle de tarification hybride, avec des sources gratuites et un ebook/corrections payant, contribuera finalement à la réputation du livre tout en générant un revenu passif bienvenu.

Plus tard, je pourrais créer une version papier du livre (peut-être [Amazon CreateSpace](https://www.createspace.com/)) s'il y a une demande pour cela. Un cours en ligne interactif offrant une expérience utilisateur plus riche est déjà en cours.

Plus important encore, j'ai la profonde satisfaction d'avoir contribué à quelque chose de significatif pour la communauté. Des milliers de personnes dans le monde utiliseront mon livre pour apprendre à coder, améliorer leur JavaScript et cela pourrait changer leur vie pour le mieux.

Et cela n'a pas de prix.

### Conclusion

Ce n'était pas tout rose, mais auto-éditer un livre open source réussi sans aucun public préalable est définitivement possible.

J'espère que cette petite histoire vous a diverti. J'espère aussi qu'elle pourrait vous inspirer à commencer un projet créatif par vous-même, qu'il s'agisse d'un livre ou de quelque chose de complètement différent.

J'ai hâte de voir ce que vous allez accomplir !