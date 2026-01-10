---
title: Ce que j'ai appris en disséquant The Web Developer Roadmap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T15:42:45.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-dissecting-the-web-developer-roadmap-1ccd0ecb5ae9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aZyrIIxkDtxWIQlUO9fPpA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Ce que j'ai appris en disséquant The Web Developer Roadmap
seo_desc: 'By Nicole Archambault

  The benefits of learning with the goal of teaching others


  Hey freeCodeCampers and others!

  I’m Nicole, one of your fellow newbie web developers.

  I’m active in the freeCodeCamp community as organizer of the MetroWest MA freeCodeC...'
---

Par Nicole Archambault

#### Les avantages d'apprendre avec l'objectif d'enseigner aux autres

![Image](https://cdn-media-1.freecodecamp.org/images/1*aZyrIIxkDtxWIQlUO9fPpA.jpeg)

#### **Salut les freeCodeCampers et autres !**

Je m'appelle Nicole, l'une de vos collègues développeuses web débutantes.

Je suis active dans la communauté freeCodeCamp en tant qu'organisatrice du [MetroWest MA freeCodeCamp Meetup](https://www.facebook.com/groups/free.code.camp.metrowest.ma/), et animatrice du [La Vie en Code Podcast](http://www.lavieencode.net/podcast). J'ai récemment été récompensée par le statut de Top Contributor 2018 par Quincy, ce qui a littéralement fait toute mon année. ?

J'adore rendre la pareille et partager tout ce que je peux... ce qui est en fait le sujet de cet article !

### Un peu de mon histoire

Comme je l'ai dit plus haut, je suis une développeuse web autodidacte comme vous peut-être. Je ne suis même pas fantastique en programmation ou quoi que ce soit. Je l'assume totalement. Je serai probablement une débutante pour toujours, et c'est tout à fait normal.

Nous sommes tous nuls lorsque nous essayons quelque chose pour la première fois. Nous pourrions aussi bien profiter du processus d'apprentissage de la programmation, car le stress ne le rend pas plus facile — et ce n'est pas comme si vous vous blessiez ou quoi que ce soit, n'est-ce pas ?

J'ai définitivement eu des fous rires en larmes lorsque j'attends une chose et que j'obtiens une sortie inutile qui ne m'aide pas du tout, ou que tout explose.

Cela fait partie du processus, et c'est _amusant_. Ou du moins, je pense que cela devrait l'être !

Donc, je m'amuse dans l'industrie depuis 2015, lorsque j'ai décidé de changer de carrière, passant du service client à l'apprentissage de la construction pour le web. J'avais commencé en tant que majeure en informatique à l'université, mais j'ai finalement changé de majeure après avoir été découragée de continuer en raison de mauvaises performances — peut-être involontairement, mais le mal était fait.

Lorsque j'ai commencé à apprendre à coder en 2015, j'ai également lancé un blog appelé [La Vie en Code](http://blog.lavieencode.net). J'y écrivais un peu de tout, ce que j'apprenais, et des pensées aléatoires sur le développement web que je pensais pouvoir aider les autres.

J'ai commencé à coder à Portland, dans l'Oregon, puis j'ai traversé le pays début 2016 pour être plus proche de ma famille. Pendant ce temps, j'ai obtenu mon premier emploi de développeuse web dans une petite boutique à Cape Cod, MA, dont je parle dans un [épisode entier de podcast](http://www.lavieencode.net/podcast/004-my-first-dev-job-used-coldfusion-or-why-im-a-freelancer) parce que c'était... unique. ?

Aujourd'hui, je vis toujours dans le Massachusetts, et j'ai traversé un emploi, le freelance, et je commence actuellement à développer mes propres cours. Cela a été une aventure folle, car j'ai dû grandir beaucoup dans le processus de devenir un nom dans l'industrie, et je n'y suis pas encore.

J'ai en fait amené la marque "La Vie en Code" à de nouveaux sommets, bien que ce soit vraiment juste moi. J'ai lancé le [La Vie en Code Podcast](http://www.lavieencode.net/podcast) en 2016, dédié aux étudiants en développement web autodidactes.

Mes intérêts sont profondément enracinés dans cette intersection de la technologie, de la psychologie, de l'éducation et du gaming. Je parle de divers sujets, notamment :

* L'expérience d'apprentissage de la programmation
* La science de l'apprentissage — et spécifiquement, comment apprendre efficacement les informations que vous rencontrez
* Les jeux et la gamification
* Les théories de la technologie éducative
* Comment démarrer votre propre blog
* Les plateformes d'e-Learning comme [Treehouse](http://www.teamtreehouse.com) et [freeCodeCamp](https://www.freecodecamp.org/)
* Des interviews avec d'autres étudiants en développement web autodidactes
* La maladie mentale et la santé
* (J'ai en fait une histoire assez inspirante là-dessus, pour être honnête)
* Certains concepts simplifiés, comme [JavaScript et le DOM](http://www.lavieencode.net/podcast/009-intro-to-js-document-object-model)

Ce podcast est mon cœur et mon âme. J'ai eu du mal à sortir des épisodes de manière régulière en raison de problèmes de santé — mais je reviens toujours à cela, parce que je l'adore. Vous pouvez même vous identifier à ce sentiment lorsqu'il s'agit de développement web.

Alors, parlons de ce défi que je me suis lancé en avril.

### Quel est ce "défis" dont je parle ?

**En bref :** Je me suis lancé le défi de construire un projet qui s'appuie sur des informations existantes pour les développeurs web autodidactes. En d'autres termes, je prendrais une ressource, je la "disséquerais", et je construirais à partir de chaque partie pour aider les étudiants à mieux comprendre le contenu lui-même.

Travailler de cette manière a enlevé la pression de créer quelque chose de entièrement nouveau, et d'apprendre dans le processus. Le projet serait un guide audio d'une ressource que je pensais pouvoir être expliquée à un niveau plus "simplifié".

Pouvoir communiquer des idées que j'ai apprises est important pour moi. Je compte sur les autres pour pouvoir communiquer des idées, et j'ai des différences dans mon apprentissage.

(Ceci est principalement parce que — rebondissement ! — je suis également sur le [spectre de l'autisme](https://taniaannmarshall.wordpress.com/2013/03/26/moving-towards-a-female-profile-the-unique-characteristics-abilities-and-talents-of-asperwomen-adult-women-with-asperger-syndrome/). L'apprentissage a été un enfer pour moi, alors je suis déterminée à aider à le rendre plus facile pour les autres. Je n'avais pas encore été diagnostiquée lorsque j'ai enregistré mon deuxième épisode, [Comment j'ai appris comment j'apprends](http://www.lavieencode.net/podcast/002-how-i-learn), et j'ai appris _tellement_ plus sur moi-même même depuis.)

En gros, c'était autant un exercice d'apprentissage et de compréhension que de développement web. Et je le savais en y entrant. Cela m'a donné encore plus envie de le faire.

Alors, sur quoi allais-je m'appuyer ? En tant que ressource, j'ai choisi un organigramme créé par le développeur [Kamran Ahmed](http://www.twitter.com/kamranahmedse). La ressource s'appelait [The Web Developer Roadmap](http://www.lavieencode.net/devroadmap)... et c'était absolument parfait pour mon projet. Je m'y étais référée plusieurs fois au cours de mon éducation.

### **Qu'est-ce que le Web Developer Roadmap ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*BCr-k47OjhPDxEI-bGr5CA.jpeg)

Kamran Ahmed a essentiellement créé cet organigramme en imaginant un chemin "idéal" à suivre pour apprendre le développement web.

Il comprend :

* **Les bases / "Requis pour tout chemin"** : Les concepts que vous devez connaître, quel que soit l'endroit où vous vous retrouvez dans le développement web
* **Front-end** : Les concepts et technologies nécessaires pour construire le Front-End (côté client)
* **Back-end** : Les concepts et technologies nécessaires pour construire le Back-End (côté serveur)
* Et **Dev Ops**, que j'ai décidé de me donner une passe pour essayer de couvrir moi-même — c'est pour un futur épisode invité, si quelqu'un veut venir sur le podcast et nous enseigner ! Il suffit de [me contacter sur Twitter](http://www.twitter.com/lavie_encode).

(À la place de Dev Ops, j'ai complété la série avec un 4ème épisode sur les **outils de construction** : les exécuteurs de tâches, les gestionnaires de paquets et les chargeurs de modules. Je vais expliquer ce qu'ils font, et comment ils peuvent faciliter notre vie de développeur !)

#### Quels sont les sujets spécifiques sur la Roadmap ?

Il y a beaucoup de sujets dans les sections Bases / "Requis pour tout chemin", Front-end et Back-end. Donc, j'étais vraiment fière de moi lorsque j'ai réussi à réduire chaque section à seulement une heure !

Voici les sujets, détaillés par chemin :

### **Les bases / Requis pour tout chemin**

* Contrôle de version : Git & GitHub
* SSH (Secure Shell)
* HTTP/HTTPS (et les protocoles en général)
* APIs
* Utilisation de base du terminal
* Apprendre à rechercher
* (**Critique** pour les étudiants autodidactes)
* Structures de données et algorithmes
* Encodages de caractères
* Modèles de conception
* Tests
* Outils de construction

#### **Front-end**

* Bases de HTML
* Bases de CSS
* Bases de JavaScript
* jQuery
* Réactivité mobile
* Gestionnaires de paquets et dépendances
* Préprocesseurs/Frameworks/Architecture CSS
* Applications Web Progressives
* Vérificateurs de type
* Rendu côté serveur

#### **Back-end**

* Langages côté serveur
* Bases de données relationnelles
* Bases de données non relationnelles (NoSQL)
* Bases de données graphiques
* Mise en cache
* APIs RESTful
* Méthodologies d'authentification et d'autorisation
* Courtiers de messages
* Moteurs de recherche
* Conteneurs/Docker
* Serveurs Web
* Websockets
* GraphQL

C'était beaucoup de choses. J'ai dû faire beaucoup de recherches, comme je m'y attendais. Mais j'ai aussi été surprise de voir à quel point je savais, honnêtement.

J'ai inclus les ressources que j'ai utilisées dans les notes de l'émission. Certaines des vidéos que j'ai utilisées avaient moins de 5 000 vues sur YouTube, mais je pensais vraiment qu'elles expliquaient bien le concept.

### Qu'ai-je appris de cette expérience ?

#### **Beaucoup de choses !**

Je recommande vivement à tout le monde de se lancer le défi d'expliquer des sujets aux autres aussi simplement que possible. C'est beaucoup plus difficile que cela n'en a l'air !

![Image](https://cdn-media-1.freecodecamp.org/images/1*hUIthykOh-sYE_pkXDtldw.png)
_J'ai tweeté un défi pour que quelqu'un explique les fermetures de la manière la plus simple possible. C'est plus difficile que cela n'en a l'air._

Il y a une leçon particulièrement importante ici :

Je n'étais **pas** sûre à 100 %, ou même proche de cela, que j'expliquerais ces concepts correctement. Ils seraient tous filtrés à travers ma propre perception, et la perception de chacun est différente. J'ai **bien** fait rebondir beaucoup de mes explications et contextualisations sur des amis développeurs sur Twitter et j'ai obtenu un pouce levé majoritaire avant d'enregistrer.

Mais au-delà de cela, je devais simplement **faire confiance** que je savais assez grâce à mes recherches pour pouvoir parler du sujet et aider les autres.

J'avais déjà fait un sujet technique sur le podcast : [JavaScript et le DOM](http://www.lavieencode.net/podcast/009-intro-to-js-document-object-model). Mais cela n'était rien comparé à couvrir une "roadmap" entière de sujets de développement web.

J'ai dû mettre mes grandes culottes, être ouverte à la critique et aux critiques, et sortir tout ce que je pouvais pour relever mon propre défi.

Et c'était une grosse affaire pour moi, car je n'ai jamais eu l'impression de "savoir assez" tout au long de mes études. Comme je l'ai dit, j'ai dû faire beaucoup de croissance pour devenir une entrepreneure émotionnellement intelligente ! ?

Spécifique aux sections, voici ce que j'ai appris :

#### Les bases / Requis pour tout chemin

Je n'ai pas vraiment été surprise de constater que certaines de ces "bases" n'étaient pas si basiques pour moi. Je suis contente d'être entrée avec cette attente, donc je n'ai pas été découragée. J'avais déjà travaillé avec tous ces sujets dans une certaine mesure, donc je me sentais assez confiante pour faire des recherches et en parler.

J'ai essayé de me concentrer sur quelques détails et anecdotes, comme [MacOS Roman](https://en.wikipedia.org/wiki/Mac_OS_Roman) lors de la discussion sur **l'encodage des caractères**. J'apprends mieux lorsqu'il y a de petits détails à retenir et à associer au sujet.

J'étais si heureuse de voir que Kamran Ahmed avait inclus **Apprendre à rechercher** sur la Roadmap. C'est une compétence absolument critique qui fait ou défait les nouveaux développeurs web — nous devons savoir comment apprendre en toute confiance et efficacement à partir des ressources, et les uns des autres. Je pourrais parler de ce sujet toute la journée.

Probablement la chose la plus surprenante que j'ai apprise dans cette partie de la Roadmap est que les **modèles de conception** — et à plus grande échelle, les **normes et meilleures pratiques** — jouent vraiment un rôle _majeur_ dans le code que nous écrivons.

Nous trébuchons au début, en essayant simplement de faire fonctionner les choses. Mais je n'avais jamais vraiment réalisé à quel point le travail de devinette est éliminé de la résolution de problèmes lorsque vous suivez simplement ces modèles de conception dès que possible.

Vous commencez à penser en termes de modèles, et les modèles sont comme de la drogue pour moi. Les modèles sont la colle de l'univers.

#### Le Front-end

Je suis une développeuse Front-end, mais ne pensez pas une seconde que c'était une promenade de santé. J'ai été totalement transparente sur le fait que je n'ai pas construit autant de projets que je l'aurais souhaité au cours de ma propre éducation.

À la lumière de cela : il est devenu **très** évident **très** rapidement où je n'avais pas encore contextualisé ces sujets et outils que je n'avais pas encore utilisés.

Dans les parties Front-end et Back-end, la Roadmap commence à décomposer chaque concept en une "étape", que j'ai passée une par une. Je le vois comme une sorte de voyage. Cela m'a été très utile de voir le flux d'apprentissage suggéré, car chaque sujet avait vraiment l'opportunité de s'appuyer sur le précédent.

Peut-être la meilleure partie de la configuration de la Roadmap est l'espacement du temps de projet, ou "pratiques", avec lesquelles j'ai toujours eu du mal.

Quand construisez-vous des projets ? Combien devez-vous savoir sur un sujet avant d'essayer de construire quelque chose avec ? En regardant en arrière (et en avant) dans ma propre éducation, je vois où ces pratiques m'auraient aidée à utiliser les compétences que j'apprenais bien plus tôt que je ne le croyais.

C'est un thème commun dans mon auto-éducation : j'ai toujours supposé que je devais en savoir plus que je ne le faisais. Cela m'a beaucoup retenue. Ne faites pas cela.

Mais à la fin de cette section, j'ai vraiment eu l'impression d'avoir une nouvelle appréciation pour le Front-end. Je pouvais voir son importance une fois de plus, et j'étais fière de connaître des concepts comme **HTML sémantique** et **CSS modulaire**.

Le Front-end est vraiment beau. ❤️

#### Le Back-end

Je pense que j'ai transpiré en enregistrant cela (LOL). Non, ce n'était pas si mal, et j'ai appris BEAUCOUP... mais c'était définitivement un exercice d'auto-éducation !

J'ai appris PHP et un peu de NodeJS, surtout par nécessité. J'adore WordPress et je fais tourner le [site web La Vie en Code](http://www.lavieencode.net) dessus, donc je suis devenue involontairement une développeuse PHP novice. Dites ce que vous voulez, je pense que PHP est un excellent langage de script.

Ce que vous finissez par réaliser, c'est que **chaque** langage a ses lourdeurs. Vous ne pouvez vraiment pas l'éviter. Tant que la technologie est constamment améliorée, je préfère me concentrer sur ce qu'elle fait bien, et utiliser un langage pour ces types de projets.

J'adore voir **les tests** dans les parties Front-end et Back-end de la Roadmap, car les principes des tests s'appliquent vraiment partout. Nous devons savoir à chaque étape que nos applications fonctionnent comme prévu — côté client **et** côté serveur. Je pense que beaucoup de nouveaux développeurs web pensent que les tests sont uniquement pour le développement Back-end, et j'espère leur enseigner le contraire.

Pour moi, les **bases de données** étaient la partie la plus amusante de cette section de la Roadmap à disséquer. J'ai seulement utilisé des **bases de données relationnelles**, et je connaissais vaguement les différences entre les bases de données relationnelles et non relationnelles (NoSQL). Je ne savais pas que les bases de données graphiques existaient, donc si j'ai l'air de le savoir, c'est parce que je l'ai appris pour pouvoir vous l'enseigner. ?

### D'accord, allez-vous partager ce projet ou quoi ?

Oui ! Le contexte est important, et je pense que comprendre l'histoire derrière cela améliorera votre expérience d'écoute du podcast.

Vous pouvez écouter les épisodes dans l'ordre [ici](http://www.lavieencode.net/wdrm-series) :

[**Série LVEC "Disséquer la Web Developer Roadmap" | Podcast La Vie en Code**](http://www.lavieencode.net/wdrm-series)

[_La Web Developer Roadmap 2018 de Kamran Ahmed est une ressource précieuse pour les nouveaux développeurs web. Dans cette série, je dissèque..._www.lavieencode.net](http://www.lavieencode.net/wdrm-series)

J'ai créé cette page de destination pour les épisodes de podcast, afin qu'ils soient faciles à parcourir dans l'ordre. Ne vous souciez pas de sa simplicité — c'est juste un foyer pour les épisodes.

Vous pouvez également vous abonner au podcast La Vie en Code sur [iTunes](http://www.lavieencode.net/itunes), [Google Play](http://www.lavieencode.net/googleplay), [SoundCloud](http://www.lavieencode.net/soundcloud), et [Stitcher](http://www.lavieencode.net/stitcher). Et j'ai une newsletter hebdomadaire géniale, [Life in Code](https://mailchi.mp/3380e75dea0d/3), si vous êtes intéressé par des ressources utiles, des nouvelles et des blagues de devs ringards :

#### J'espère que cela aide !

J'adorerais avoir vos retours sur [Twitter](https://twitter.com/lavie_encode) ! Si cela vous a aidé, si j'ai manqué quelque chose sur un sujet, si vous avez des pensées supplémentaires... Je veux les entendre.