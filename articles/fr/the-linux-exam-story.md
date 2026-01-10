---
title: Comment j'ai réussi l'examen CompTIA Linux+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T10:01:32.000Z'
originalURL: https://freecodecamp.org/news/the-linux-exam-story
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screen-Shot-2020-04-29-at-10.33.10-PM.png
tags:
- name: comptia
  slug: comptia
- name: 'exam '
  slug: exam
- name: learning
  slug: learning
- name: Linux
  slug: linux
seo_title: Comment j'ai réussi l'examen CompTIA Linux+
seo_desc: 'By Clark Jason Ngo

  Summary of this article:


  The backstory: why CompTIA Linux+ exam.

  Review of learning resources: what is good and what is not good.

  Retrospective on studying: what worked and did not work.

  My experience during the exam: how the test...'
---

Par Clark Jason Ngo

### Résumé de cet article :

* Le contexte : pourquoi l'examen CompTIA Linux+.
* Revue des ressources d'apprentissage : ce qui est bon et ce qui ne l'est pas.
* Rétrospective sur l'étude : ce qui a fonctionné et ce qui n'a pas fonctionné.
* Mon expérience pendant l'examen : comment le test s'est déroulé et comment je me sentais.
* Mon approche pendant l'examen : quelles stratégies utiliser et quel état d'esprit avoir.
* Obtenir un badge génial : à quoi il ressemble et qu'est-ce que cela m'apporte ?
* Bonus : comme la plupart de mes matériaux sont sponsorisés par l'école, j'ai cherché du contenu gratuit pour vous aider à étudier pour l'examen, comme la [hiérarchie du système de fichiers](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard), les [commandes Linux de base](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html#binEssentialUserCommandBinaries), l'utilisation d'[AWS EC2 Ubuntu](https://aws.amazon.com/mp/linux/) comme environnement Linux. J'ai également créé une fiche de révision dans Trello, disponible [ici](https://trello.com/b/viGl7wam/linux-prep). Avertissement : le contenu gratuit pourrait ne pas être suffisant. 
* Objectifs de l'examen : [Objectifs officiels de l'examen CompTIA Linux+](https://www.comptia.jp/pdf/comptia-linux-xk0-004-exam-objectives.pdf). 

### Conseils pour l'examen en bref (je n'avais aucune expérience professionnelle avec Linux) :

* Concentrez-vous sur la section Activité du Guide d'étude CompTIA et suivez avec votre propre environnement Linux.
* Pratiquez les Questions Basées sur la Performance (PBQ). Elles montrent environ 10 choix qui semblent tous corrects.
* Jouez avec les combinaisons de commandes Linux en utilisant le piping (|)
* Configurez les tables IP, le pare-feu et le dépannage.
* Apprenez les étapes de configuration, le processus de démarrage et la sauvegarde des fichiers.
* Scripting bash de base et expressions régulières.

_Lisez jusqu'à la fin pour des conseils sur la façon d'avoir le bon état d'esprit et des stratégies pour répondre aux questions difficiles. De plus, une vidéo de moi résumant cet article lors d'une réunion de club à notre école est disponible à la fin de l'article. N'oubliez pas de regarder la vidéo car elle contient une section de questions-réponses à la fin._

Je voudrais commencer par un grand merci à l'[École de Technologie et d'Informatique](https://ciae.cityu.edu/programs/) de l'[Université de la Ville de Seattle](https://www.cityu.edu/) (CityU). Ils m'ont fourni un emploi, une croissance de carrière, et ont sponsorisé mes matériaux d'apprentissage CompTIA et mon bon d'examen. 

En tant que titulaire d'un visa d'étudiant F-1 avec des opportunités d'emploi limitées, cela m'a permis de gagner un revenu supplémentaire, dont je [fais don](https://www.freecodecamp.org/donate/) d'une partie à freeCodeCamp sur une base mensuelle. 

Ceci est une suite libre de mon histoire : _[Pourquoi j'ai abandonné mon MBA pour obtenir un master en Informatique](https://www.freecodecamp.org/news/cjn-why-i-abandoned-my-mba-to-get-a-masters-in-computer-science/)_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*cSvQ_M7qvgXFrIrA.jpg)
_Campus de l'Université de la Ville de Seattle_

## Pourquoi CompTIA Linux+ ?

En juillet 2019, notre école, avec l'aide de notre directeur des relations externes, a obtenu un contrat avec Amazon Web Services (AWS) et la Washington Technology Industry Association (WTIA), appelé le Programme d'Apprentissage AWS (AAP). 

Nous avons eu l'opportunité de former 23 vétérans militaires et conjoints de vétérans. Leur exigence était de passer l'examen CompTIA Linux+ et le Programme de Développeur Système Full Stack de CityU, qui inclut la préparation à l'examen CompTIA Linux+. Une fois qu'ils ont satisfait aux deux critères, ils pourraient passer à la formation en situation de travail avec AWS. 

Mon rôle à l'époque était celui d'Assistant d'Enseignement Principal (TA) et j'ai été chargé d'aider à construire la proposition de programme du Doyen. J'ai coordonné avec 6 autres TA pour construire les cours, qui comprenaient les éléments suivants : Linux I, Linux II, Réseautage, Développement Web, JavaScript/TypeScript, Full Stack - MEAN Stack, Python, et Full Stack - Django.

Comme c'était notre premier contrat, nous construisions l'avion tout en essayant de le faire voler.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-295.png)
_L'image semble amusante ! Mais pas dans la vraie vie lol !_

### Nous avons utilisé les ressources suivantes pour notre cours sur le système d'exploitation Linux :

* Manuel : Pro Bash Programming: Scripting the GNU/Linux Shell, Second Edition, par Chris F. A. Johnson, Jayant Varma 
* Environnement Linux de l'étudiant : Instance AWS EC2 avec Ubuntu
* Laboratoire virtuel : InfoSec Learning

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-296.png)

### Ce que j'ai appris

* Beaucoup d'exercices de scripting bash et de défis de codage
* Comment se connecter en SSH à un serveur distant (Instance EC2)
* Diverses commandes Linux et configurations liées à CompTIA Linux+

Après quelques semaines dans le programme, nous avons fait plus de recherches et écouté les retours des étudiants. Il s'avère que nous faisions trop de scripting bash et manquions de préparation pour l'examen CompTIA Linux+.

> Les étudiants étaient en enfer pendant les premières semaines de scripting bash

Nous avons immédiatement partenariat avec CompTIA pour obtenir des matériaux d'étude pour l'examen CompTIA Linux+ à prix réduit. Nous avons pivoté et changé des parties de notre programme pour intégrer les nouveaux matériaux d'étude.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-299.png)
_Badge cool_

> Heureusement que notre département pratiquait la méthodologie Agile et cela nous a rendu très agiles.

### Les nouvelles ressources sont les suivantes :

* CertMaster Learn - inclut un eBook, des Questions Basées sur la Performance (PBQ), et des vidéos CompTIA (Note : C'était l'année dernière. Si vous achetez cette année, vous n'aurez pas les PBQ, mais vous obtenez une nouvelle interface, et un test pratique supplémentaire).
* CertMaster Practice - des questions à choix multiples sur stéroïdes. Une fois que vous avez accumulé un bon nombre de mauvaises réponses, vous recevez des commentaires sur pourquoi vos réponses sont fausses et cela explique les autres choix également. Ensuite, cela recule votre barre de progression.
* CertMaster Labs - des activités de laboratoire plus courtes comparées aux InfoSec Labs.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-298.png)
_Le bundle d'apprentissage CompTIA Linux+_

### Mes pensées sur les nouvelles ressources

J'ai lu l'eBook de haut en bas et cela a été utile pour obtenir un aperçu. Cependant, je n'ai pas été en mesure de retenir des connaissances en le lisant. J'ai parcouru à la fois CertMaster Practice et CertMaster Labs et je n'ai rien gagné non plus. 

> Qu'est-ce qui ne va pas chez moi ? Hmm..

En raison d'une opportunité d'enseigner le cours JavaScript/TypeScript dans le programme AAP et de l'événement malheureux du décès de mon père, ma route vers l'examen Linux+ a finalement été déraillée et oubliée.

> Man.... Quelle déception...

## Avance rapide jusqu'à la fin du Programme d'Apprentissage AWS

En novembre 2019, nous avons réussi à transitionner tous les 23 étudiants ! Un 100 % ! Nous étions la seule école partenaire à avoir fait cela.

La plupart du crédit revient au Doyen de l'École de Technologie et d'Informatique pour ses citations répétées de "ne laisser aucun homme derrière" - similaire au cred des soldats : "Je ne laisserai jamais un camarade tombé derrière", et "nous restons ensemble, nous survivons" (du film Gladiator).

Le succès du programme a été largement attribué aux TA, qui ont soutenu les étudiants depuis le premier jour.

Nous avons demandé des retours à nos étudiants sur ce qui a fonctionné et ce qui n'a pas fonctionné en ce qui concerne les matériaux CompTIA Linux+. Nous avons obtenu les éléments suivants :

* Se concentrer sur la section Activité du Guide d'étude
* Faire les laboratoires virtuels à plusieurs reprises
* Passer l'examen pratique n'est pas efficace
* Regarder les vidéos ITPro.tv (que nous n'avons pas pu fournir à l'époque)

Je n'ai pas étudié pour l'examen Linux+ pendant plusieurs mois car je me suis concentré sur l'apprentissage de la MEAN Stack (en particulier le framework front-end Angular). J'ai régulièrement abordé les défis de codage leetcode pour me préparer aux entretiens d'embauche pour les postes de développeur logiciel. 

J'ai également terminé mon projet de fin d'études : [_Documentation Logicielle et Analyse Architecturale du Développement Full Stack_](https://www.freecodecamp.org/news/cjn-understanding-mean-stack-through-diagrams/), et j'enseignais deux classes : Systèmes d'Information, et Communications et Réseautage de Gestion des Données.

> Pas de temps... pas de temps du tout... ou était-ce juste des excuses ?

Lorsque j'approchais de la fin de mon dernier trimestre, je me suis senti coupable et j'ai recommencé à étudier pour l'examen Linux+.

> Cette fois, un nouveau plan d'attaque.

J'ai recommencé à lire l'eBook de haut en bas. Ce qui était différent la deuxième fois, c'est que pour chaque théorie, définition, commande, option, sous-commandes, etc. que je rencontrais, je créais une fiche de révision dans Trello (disponible [ici](https://trello.com/b/viGl7wam/linux-prep)). Je l'ai utilisé pour m'entraîner avec des amis à faire un quiz pop et exécuter des commandes dans le terminal Linux également. 

De mon côté, j'avais mon propre environnement Linux en suivant la section Activité de l'eBook. Cela m'a vraiment aidé à retenir mes connaissances sur les commandes et configurations Linux. J'ai également incorporé l'utilisation des commandes Linux dans mon ordinateur portable personnel avec MacBook Pro, car MacOS a un terminal de type Unix.

J'ai utilisé à nouveau l'examen pratique CertMaster. Et cette fois, j'avais un ami pour passer en revue et discuter pourquoi chaque choix était correct ou incorrect, en utilisant le processus d'élimination.

> Il semble que faire des activités pratiques et avoir une discussion avec un ami vous aide vraiment à maîtriser un sujet.

Je n'ai vraiment pas aimé les CertMaster Labs et ne les ai pas utilisés pendant mon étude.

### J'ai hésité à étudier les éléments suivants : 

* scripting bash - Je suis un développeur logiciel et je sais déjà coder. J'ai construit des scripts bash pour augmenter ma productivité, des notes de cours aux applications web.
* contrôle de version - J'ai utilisé git et GitHub dans mes cours et projets personnels.
* conteneurs et orchestration - J'ai une bonne base car j'ai lu des livres sur DevOps.

## Les vidéos ITPro.tv à regarder en rafale

> Je les ai découvertes par accident. C'était opportun et efficace.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-304.png)
_où vous pouvez regarder des vidéos IT en rafale_

Au début d'avril 2020, nous avons reçu des nouvelles de l'arrivée de nouveaux étudiants AAP. Le Doyen m'a demandé de vérifier à nouveau le magasin CompTIA pour les matériaux, et de découvrir ce que ces vidéos ITPro.tv étaient. 

Au début, j'étais réticent à acheter les vidéos car je me souvenais que le Guide d'étude CompTIA avait le logo ITPro.tv au début de leurs vidéos. J'ai commencé à calculer le nombre total d'heures des vidéos du Guide d'étude CompTIA. La durée totale était seulement de 22 minutes. 

C'était une grande différence par rapport aux vidéos ITPro.tv autonomes avec 16 heures de contenu. Je suis allé de l'avant et je les ai achetées (avec remboursement bien sûr).

Et je ne l'ai pas regretté. Ces vidéos étaient fantastiques. Elles plongeaient plus profondément dans les sujets et expliquaient les commandes en détail avec l'aide d'un co-animateur pour demander pourquoi nous devions utiliser ces commandes. 

La durée moyenne d'une vidéo est d'environ 15 minutes. Un grand contraste par rapport à l'autre ressource, qui avait une moyenne d'environ 2 minutes par vidéo.

J'ai commencé à choisir des vidéos à regarder en fonction des sujets que je savais que je ne pouvais pas expliquer à quiconque. J'ai combiné cette stratégie avec le CertMaster Practice à choix multiples sur stéroïdes pour combler mes lacunes de connaissances.

Au milieu d'avril 2020, j'ai planifié mon examen CompTIA Linux+ en ligne. Ils ont créé l'environnement de test en ligne en raison de la pandémie. Comme la date prévue approchait, j'ai relâché mes schémas d'étude et je me suis limité à regarder les vidéos ITPro.tv.

## Procédures d'examen

L'examen en ligne vous oblige à respecter les procédures suivantes :

* avoir une connexion internet
* avoir une webcam externe ou une webcam d'ordinateur portable
* avoir un microphone externe ou un microphone d'ordinateur portable
* avoir une photo d'une pièce d'identité valide
* avoir des photos de l'avant, de l'arrière, de la gauche et de la droite de votre propre environnement de test
* Pas de casque, et les smartphones et appareils électroniques doivent être hors de portée

Voir les détails complets [ici](https://www.comptia.org/testing/testing-options/take-online-exam).

## Heure de l'examen

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-308.png)
_publication Instagram de mon partenaire toujours soutien_

> J'apprécie vraiment le soutien !

### Mon expérience avec l'application de test en ligne

* L'examen était prévu à 12h15 minuit. C'était mon intention pour éviter tout bruit dans la maison. 
* Le surveillant peut vous voir à travers la webcam, et vous ne pouvez pas le voir.
* L'application de test en ligne a ralenti et planté plusieurs fois. Le surveillant a dit que c'était dû au grand nombre de candidats.

### Ce que j'ai ressenti pendant l'examen

Les premières questions que j'ai eues à l'examen étaient des Questions Basées sur la Performance. C'était extrêmement difficile. Je ne pouvais vraiment pas répondre avec 100% de confiance. J'ai rencontré un problème en utilisant les commandes Linux _grep_ et _awk_ avec le piping vers une autre commande. 

Un autre problème concernait l'investigation d'une violation de politique SELinux, ce qui nécessite d'inspecter chaque commande et leurs sorties respectives pour identifier quel fichier ou répertoire nécessitait une configuration supplémentaire.

> Si seulement j'avais cette expérience professionnelle, cela aurait été beaucoup plus facile.

Alors que je continuais à répondre à plus de questions, je me sentais vraiment stupide et j'ai perdu confiance. Je ne savais pas comment répondre aux questions sur les configurations réseau, système ou utilisateur. Dans la partie scripting bash, je savais que je n'étais pas vraiment bon en RegEx (expressions régulières). 

> Il me restait 30 minutes dans mon examen et je me sentais comme si j'allais échouer...

Mes pensées sur le plan B revenaient - je passerais simplement l'examen à nouveau. Cela était en partie dû à ma propre perspective sur la vie. Je dis toujours aux gens que je suis habitué à l'échec et que cela ne me dérange pas d'échouer tant que je peux être persévérant jusqu'à atteindre mon objectif. 

Vers la marque des 28 minutes, j'allais abandonner, quand j'ai entendu une autre voix dans mon cerveau (je ne suis pas fou, je vous le dis. C'est le tour de l'esprit Jedi, lisez _[Comment se réapprendre à apprendre](https://www.freecodecamp.org/news/cjn-how-to-teach-yourself-to-learn-again/)_). 

> La voix a dit : "ne pense pas à l'échec maintenant, utilise les minutes restantes et fais de ton mieux !"

J'ai donc utilisé le temps restant pour sauter d'une question à l'autre jusqu'à ce que je les aie toutes couvertes. Cette fois avec plus de concentration. J'ai changé presque 80% de mes réponses et j'ai commencé à utiliser les stratégies suivantes pour augmenter mes chances d'obtenir la bonne réponse :

* Processus d'élimination - J'ai éliminé les choix que je savais être totalement faux.
* Je me suis en tenu à ce que je savais - Je n'ai pas choisi une réponse si je ne savais pas ce qu'elle signifiait.
* Concentration plus profonde - J'ai lu mot par mot et j'ai essayé d'utiliser à la fois la compréhension et la pensée logique.
* Yeux fermés, esprit ouvert - Je me suis convaincu que j'avais étudié très dur pour cet examen, donc cela devait être stocké quelque part dans mon cerveau. Avec cela en tête, j'ai essayé de récupérer ces souvenirs pour atteindre 100% de confiance dans certaines questions où j'avais environ 70% de confiance en répondant.

J'ai continué à répéter ces stratégies jusqu'à la dernière minute. 

## Résultats de l'examen

L'examen s'est terminé et j'ai réussi - 739 sur 1000 ! Une note de passage est de 720. Après 30 minutes, j'ai reçu un email de CompTIA.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-312.png)
_ma publication Instagram cool célébrant mon accomplissement_

Je resterai humble et je dirai aux gens que j'ai eu de la chance. Mais pour moi-même, je ne dirai pas que j'ai eu de la chance car j'ai changé la plupart de mes réponses en utilisant un meilleur état d'esprit et des stratégies plus efficaces.

## Leçons apprises

* Je devrais vraiment arrêter de passer ces examens quand je n'ai pas encore d'expérience professionnelle. Pourquoi ? J'ai rencontré le même genre de difficulté et j'ai échoué à mon examen de certification AWS Developer avant (voici l'article : _[J'ai échoué à mon examen AWS Developer. Et maintenant ?](https://www.freecodecamp.org/news/cjn-i-failed-my-aws-developer-exam/)_). 
* En étudiant, j'aurais dû faire plus d'évaluations tôt pour me concentrer sur mes lacunes de connaissances au lieu de parcourir tous les matériaux à toute vitesse.
* Pendant l'examen, j'avais besoin de me rappeler que c'est ma réalité maintenant. Que puis-je faire pour être génial dans cette situation ? Cet état d'esprit est quelque chose que je peux appliquer à mon travail actuel également.
* N'oubliez pas d'avoir des sessions d'étude avec des amis ou des collègues, car vous aurez l'occasion de faire croître vos connaissances de manière exponentielle.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-284.png)
_citation du film Gladiator (2000)_

## Et maintenant, Clark ?

J'ai réintégré CityU à temps plein avec un poste de Program Manager pour le Programme d'Apprentissage AWS (Développeur Système Web Full Stack) le 20 avril 2019.

Avec la certification Linux+ sous ma ceinture, j'ai acquis une expérience supplémentaire, en plus de mon expérience précédente en tant que TA Lead avec le même programme. Cela m'a permis de mieux diriger, enseigner et mentor les nouvelles cohortes. Cela inclut mon équipe qui comprend de nouveaux TA que je sais seront plus réussis que je ne l'ai été.

Je ferai de mon mieux pour continuer à enseigner et mentor les étudiants tout en perfectionnant mes compétences en développement logiciel, car je suis toujours en chemin pour trouver un emploi de développeur logiciel dans l'industrie technologique. Je sais que c'est difficile de venir d'un milieu non technologique pour transitionner, mais nous y arriverons tous avec le temps.

À mes lecteurs, merci d'avoir lu mon article. Je veux vraiment me concentrer davantage sur les articles techniques mais je ne pouvais pas laisser une bonne histoire s'échapper. =)

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-322.png)
_Je n'arrivais pas à me décider sur mon titre LinkedIn lol_

**Résumé vidéo de l'article et Q&A**

%[https://youtu.be/5evBAfJi4l0]