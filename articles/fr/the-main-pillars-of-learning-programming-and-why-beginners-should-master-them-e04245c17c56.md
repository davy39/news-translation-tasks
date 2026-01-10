---
title: Les piliers principaux de l'apprentissage de la programmation — et pourquoi
  les débutants devraient les maîtriser.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-19T18:14:05.000Z'
originalURL: https://freecodecamp.org/news/the-main-pillars-of-learning-programming-and-why-beginners-should-master-them-e04245c17c56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*guxwNxNHQB4mCLowb6V0mA.png
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Les piliers principaux de l'apprentissage de la programmation — et pourquoi
  les débutants devraient les maîtriser.
seo_desc: 'By Rainer Hahnekamp

  I have been programming for more than 20 years. During that time, I’ve had the pleasure
  to work with many people, from whom I learned a lot. I’ve also worked with many
  students, coming fresh from university, with whom I had to tak...'
---

Par Rainer Hahnekamp

Je programme depuis plus de 20 ans. Pendant cette période, j'ai eu le plaisir de travailler avec de nombreuses personnes, dont j'ai beaucoup appris. J'ai également travaillé avec de nombreux étudiants, fraîchement sortis de l'université, avec qui j'ai dû endosser le rôle d'enseignant ou de mentor.

Récemment, j'ai été impliqué en tant que formateur dans un programme qui enseigne la programmation à des débutants absolus.

Apprendre à programmer est difficile. Je trouve souvent que les cours universitaires et les bootcamps négligent des aspects importants de la programmation et adoptent de mauvaises approches pour enseigner aux débutants.

Je souhaite partager les cinq piliers de base sur lesquels, selon moi, un cours de programmation réussi devrait s'appuyer. Comme toujours, je m'adresse au contexte des applications web grand public.

L'objectif d'un débutant est de maîtriser les fondamentaux de la programmation et de comprendre l'importance des bibliothèques et des frameworks.

Les sujets avancés tels que le cloud, les opérations en général, ou les outils de build ne devraient pas faire partie du programme. Je suis également sceptique quant aux Design Patterns. Ils supposent une expérience que les débutants n'ont jamais.

Alors, voyons par où les nouveaux programmeurs devraient commencer.

### Développement piloté par les tests (TDD)

![Image](https://cdn-media-1.freecodecamp.org/images/r0uu3i4euj5dIIHpOKxnsgpUunuqgk3mva2U)

Le TDD apporte de nombreux [avantages](https://www.rainerhahnekamp.com/en/why-we-test-do-things-faster-with-test-driven-development/). Malheureusement, c'est un sujet avancé pour lequel les débutants ne sont pas entièrement prêts.

Les débutants ne devraient pas écrire de tests. Cela serait trop pour leur niveau de compétences de base. Au lieu de cela, ils devraient apprendre à utiliser et à travailler avec des tests.

Chaque cours de programmation devrait être centré sur des exercices. J'étend mes exercices avec des tests unitaires et je fournis aux étudiants un environnement déjà configuré pour exécuter ces tests.

Tout ce que les étudiants ont à faire est d'écrire leur code et puis de regarder les lumières du testrunner passer du rouge au vert. La gamification qui en résulte est un bel effet secondaire.

Par exemple : Si la technologie sélectionnée est Spring, je fournis les exercices et les tests dans un projet Spring. Les étudiants n'ont pas besoin de connaître quoi que ce soit sur Spring. Tout ce qu'ils doivent savoir est l'emplacement des exercices et le bouton pour déclencher les tests.

De plus, les étudiants doivent savoir comment utiliser un débogueur et avoir un Read-Eval-Print Loop (REPL) à portée de main. La capacité à analyser le code pendant l'exécution et à avoir un terrain de jeu pour de petites expériences est essentielle en TDD.

Le point principal est de s'assurer que les étudiants n'ont pas à apprendre les comportements de base du TDD après avoir acquis des compétences de base en programmation. Changer les habitudes plus tard dans la carrière des étudiants sera beaucoup plus difficile que d'apprendre ces habitudes maintenant. C'est pourquoi ils devraient vivre et respirer les tests unitaires dès le début.

Plus tard dans leur vie professionnelle, ils devraient avoir une antipathie pour les projets sans tests unitaires. Ils devraient intuitivement voir l'absence de tests unitaires comme un anti-pattern.

### Les fondamentaux d'abord

![Image](https://cdn-media-1.freecodecamp.org/images/ItdR01O9Fye8a-YtpGWDAQz0k2iU7rXNwZR8)

J'entends très souvent que les débutants devraient immédiatement commencer avec un framework. C'est comme apprendre aux gens à conduire en les plaçant dans une voiture de rallye et en leur demandant d'éviter le survirage. Cela ignore simplement le fait qu'ils confondent encore la pédale de frein avec celle de l'accélérateur.

Il en va de même lorsque nous commençons les étudiants avec un framework comme Angular. Les débutants doivent d'abord comprendre les fondamentaux de la programmation. Ils doivent être familiers avec les éléments de base et savoir ce que signifie écrire du code avant de pouvoir utiliser celui de quelqu'un d'autre.

Le concept de fonction, de variable, de condition et de boucle sont complètement étrangers aux novices. Ces quatre éléments constituent les fondations de la programmation. Tout ce dont un programme est fait repose sur eux.

Les étudiants entendent ces concepts pour la toute première fois, mais il est de la plus haute importance que les étudiants deviennent compétents avec eux. Si les étudiants ne maîtrisent pas les fondamentaux, tout ce qui suit semble être de la magie et conduit à la confusion et à la frustration.

Les enseignants **devraient** passer plus de temps sur ces fondamentaux. Mais, malheureusement, beaucoup passent à autre chose trop rapidement. Le problème est que certains enseignants ont du mal à se mettre à la place d'un étudiant. Ils programment depuis des années et ont oublié quels types de problèmes un débutant doit affronter. C'est assez similaire à un pilote de rallye professionnel. Il ne peut pas imaginer que quelqu'un doive réfléchir avant de freiner. Il le fait simplement automatiquement.

Je conçois mes exercices de manière à ce qu'ils soient stimulants mais résolubles en un temps raisonnable en utilisant une combinaison des quatre éléments principaux.

Un bon exemple est un convertisseur pour les chiffres romains et arabes. Ce défi demande de la patience aux étudiants. Une fois qu'ils appliquent avec succès les quatre éléments pour résoudre le défi, ils reçoivent également un grand coup de motivation.

Les fondamentaux sont importants. Ne passez pas à autre chose tant qu'ils ne sont pas maîtrisés.

### Bibliothèques et Frameworks

![Image](https://cdn-media-1.freecodecamp.org/images/lr7vOKfzzdX85fkOoW4u8INUBxuCCNyu5xfM)

Après avoir passé beaucoup de temps à coder, les étudiants doivent apprendre que la plupart du code existe déjà sous forme de bibliothèque ou de framework. Cela relève plus d'un état d'esprit que d'un modèle.

Comme je l'ai écrit [auparavant](https://www.rainerhahnekamp.com/en/modern-software-development/) : Les développeurs modernes connaissent et choisissent la bonne bibliothèque. Ils ne passent pas des heures à écrire une version boguée par eux-mêmes.

Pour que cette transition d'état d'esprit soit un succès, les exemples de la phase « fondamentaux » devraient être résolubles en utilisant des bibliothèques bien connues comme Moment.js, Jackson, Lodash ou Apache Commons.

De cette manière, les étudiants comprendront immédiatement la valeur des bibliothèques. Ils se sont creusé la tête autour de ces problèmes compliqués. Maintenant, ils découvrent qu'une bibliothèque résout l'exercice en un rien de temps.

De manière similaire au TDD, les étudiants devraient devenir suspicieux lorsque des collègues se vantent de leur bibliothèque de gestion d'état maison qui rend Redux inutile.

En ce qui concerne les frameworks, les étudiants n'auront aucun problème à comprendre l'importance une fois qu'ils auront compris l'utilité des bibliothèques.

Selon le calendrier du cours, il peut être difficile de consacrer du temps aux frameworks. Mais comme je l'ai déjà souligné, l'aspect le plus important est de faire évoluer l'état d'esprit de l'étudiant, passant de tout programmer à partir de zéro à explorer et utiliser des bibliothèques.

Je n'ai pas ajouté d'outils à ce pilier, car ils ne sont utiles qu'aux développeurs expérimentés. À ce stade précoce, les étudiants n'ont pas besoin d'apprendre à intégrer et configurer des outils.

### Maître et Apprenti

![Image](https://cdn-media-1.freecodecamp.org/images/Qarg7eqV5gyX7psyf7frI1dz4oZjICxiFXP6)

Dans mes débuts, à 20 ans, je voulais apprendre à jouer du piano. Je ne voulais pas de professeur et pensais pouvoir l'apprendre par moi-même. Cinq ans plus tard, j'ai consulté un tuteur professionnel. Eh bien, que puis-je dire ? J'ai appris plus en 1 mois qu'au cours des cinq années précédentes.

Mon professeur de piano a pointé des erreurs dans mon jeu que je ne pouvais pas entendre et m'a fait prendre conscience de choses interprétatives que je n'aurais jamais imaginées. Après tout, elle m'a inculqué l'état d'esprit pour la musique et l'art, deux choses qui étaient hors de ma portée en tant que personne technique.

C'est la même chose en programmation. Si quelqu'un n'a aucune expérience en programmation, alors l'auto-apprentissage peut être une mauvaise idée. Bien qu'il y ait de nombreuses histoires de succès, je remets en question l'efficacité de le faire seul.

Au lieu de cela, il devrait y avoir une relation de type « maître et apprenti ». Au début, le maître donne des règles que l'apprenti doit suivre — aveuglément ! Le maître peut expliquer les règles, mais généralement le raisonnement dépasse la compréhension de l'apprenti.

Ces règles intériorisées forment une sorte de filet de sécurité. Si l'on se perd, on a toujours un terrain sûr où revenir.

L'enseignement ne devrait pas être un monologue. Le maître doit traiter chaque étudiant individuellement. Il devrait vérifier comment les étudiants travaillent, donner des conseils et adapter la vitesse du cours à leur progression.

Une fois que les apprentis atteignent un certain niveau de maîtrise, ils devraient être encouragés à explorer de nouveaux territoires. Le maître évolue en un mentor qui partage la « sagesse » et est ouvert aux discussions.

### Défi et Motivation

![Image](https://cdn-media-1.freecodecamp.org/images/MwvSLxKLBGo0m-FuB8CK9wGJoDg6MdPKpGBk)

« Créons un clone de Facebook ! » Cela ne vient pas d'un PDG soutenu par une horde de développeurs logiciels seniors et un budget de plusieurs millions d'euros. C'est un exercice d'un cours d'introduction pour programmeurs. Une telle entreprise est virtuellement impossible. Pire encore, les étudiants sont plongés au pays des merveilles et persuadés qu'ils ont des compétences qui sont vraiment hors de leur portée.

Sans doute l'enseignant en est conscient, mais crée de tels exercices pour des raisons de motivation.

Le but principal d'un exercice n'est pas de divertir. Il devrait être créé autour d'une technique particulière et devrait aider les étudiants à comprendre cette technique.

La motivation est bonne, mais pas au sacrifice du contenu. La programmation n'est pas facile. Si les étudiants n'ont pas une motivation intrinsèque, la programmation n'est peut-être pas la voie à suivre.

Les débutants devraient vivre ce que signifie être un développeur professionnel. Ils devraient savoir ce qui les attend avant d'investir de nombreuses heures.

Par exemple, de nombreuses applications métiers sont centrées autour de formulaires et de grilles complexes. Créer ceux-ci est une compétence importante que les exercices peuvent transmettre. Construire une application similaire à Facebook n'est peut-être pas la meilleure leçon pour les étudiants à apprendre immédiatement.

De même, un non-programmeur pourrait être surpris du peu de lignes de code qu'un développeur écrit par jour. Il arrive même que nous supprimions du code ou que nous n'accomplissions rien.

Pourquoi ? Parce que les choses tournent mal tout le temps. Nous passons des heures sans fin à corriger des bugs extrêmement étranges qui se révèlent être une simple faute de frappe. Un outil peut ne pas fonctionner simplement parce qu'une bibliothèque a reçu une mise à jour mineure de version. Ou le système plante parce que quelqu'un a oublié d'ajouter un fichier à git. La liste peut continuer ainsi.

Les étudiants devraient apprécier ces expériences. Un exercice ciblant une bibliothèque inconnue sous pression de temps pourrait être exactement la bonne chose. ;)

Le soleil ne brille pas toujours dans la vie réelle. Les débutants devraient être bien préparés à la réalité de la programmation.

### Conseils finaux

Dernier point, mais non des moindres : On ne devient pas un programmeur professionnel en deux semaines, deux mois ou même un an. Cela prend du temps et de la patience.

Les formateurs ne devraient pas se précipiter ou faire de fausses promesses. Ils devraient se concentrer sur le fait que les étudiants comprennent les concepts et ne pas avancer trop vite.

_Publié à l'origine sur [www.rainerhahnekamp.com](https://www.rainerhahnekamp.com/en/5-pillars-of-learning-programming/) le 10 juin 2018._