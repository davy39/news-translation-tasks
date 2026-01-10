---
title: Comment décrocher l'emploi de vos rêves en logiciel embarqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T16:39:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-landing-your-embedded-software-dream-job-4ff9674bf1c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*doISq7nDJgKnuvp9UjlALA.jpeg
tags:
- name: careers
  slug: careers
- name: Computer Science
  slug: computer-science
- name: embedded systems
  slug: embedded-systems
- name: interview
  slug: interview
- name: General Programming
  slug: programming
seo_title: Comment décrocher l'emploi de vos rêves en logiciel embarqué
seo_desc: 'By Rohan Dasika

  Guides on preparing for software interviews are aplenty. Embedded software interviews
  are somewhat similar, but it’s still a different game you have to play.

  There is some helpful material on the Internet and some content for software...'
---

Par Rohan Dasika

Les guides sur la préparation aux entretiens pour les postes en logiciel sont nombreux. Les entretiens pour les postes en logiciel embarqué sont quelque peu similaires, mais c'est toujours un jeu différent auquel vous devez jouer.

Il existe du matériel utile sur Internet et certains contenus pour la préparation aux entretiens en logiciel peuvent être réutilisés. Mais en général, je n'ai pas été en mesure de trouver un guide complet pour me lancer.

Le recrutement et la préparation aux entretiens pour les postes en logiciel embarqué au cours des quatre derniers mois m'ont appris beaucoup sur la façon d'aborder le processus. J'ai récemment reçu des offres de quelques grandes entreprises technologiques. Dans cet article, je vais partager quelques insights que j'ai acquis en cours de route.

Je vais diviser cet article en plusieurs sections, alors n'hésitez pas à naviguer ! Il existe déjà des tonnes de contenus sur les façons intelligentes de recruter, donc je ne vais pas aborder ici comment obtenir des entretiens.

* Contenu à préparer et à réviser
* L'entretien lui-même !

### Choisir un langage

En règle générale, le développement de logiciels embarqués est principalement effectué en C, bien que le C++ devienne de plus en plus populaire récemment. Si vous avez suivi des cours d'architecture informatique ou de systèmes embarqués, vous avez probablement utilisé l'un ou l'autre. Assurez-vous de savoir quel langage l'entreprise avec laquelle vous passez l'entretien utilise. Si vous êtes plus familier avec le C++ mais qu'ils utilisent le C, soyez franc à ce sujet — si vous en connaissez un, vous pourrez passer de l'un à l'autre assez facilement.

Puisque je suis le plus familier avec le C++, les entreprises m'ont permis d'écrire du code en C++. Si nécessaire, elles m'ont aidé à convertir ce code en C. Pour la plupart, cela ne fait pas vraiment de différence. À moins que vous ne travailliez avec certaines fonctions et conteneurs spécifiques de la bibliothèque standard C++.

Le Verilog est principalement utilisé pour le développement FPGA. Python est utilisé dans une certaine mesure pour communiquer entre l'utilisateur et le système embarqué sur lequel ils travaillent. Il est peu probable que vous soyez interrogé sur ces sujets.

Il en va de même pour le langage d'assemblage (heureusement !! ?).

### Les bases restent les bases

J'ai commencé ce parcours de manière similaire à la plupart des étudiants en informatique — en révisant mes structures de données et mes algorithmes. Mais bientôt, j'ai réalisé que le contenu pour les logiciels embarqués diverge à un certain point. Il est _beaucoup_ plus axé sur l'architecture informatique, les systèmes d'exploitation et certains fondamentaux matériels que sur des structures de données de haut niveau comme les arbres ou les algorithmes de tri.

Vous traitez avec du code de bas niveau et du matériel dans les rôles de logiciel embarqué. Mais d'un point de vue programmation, vos structures de données et algorithmes sont toujours _hautement_ pertinents. Similaire aux entretiens pour les logiciels, il existe des tonnes de ressources pour vous aider à préparer les bases ! Faire quelques problèmes de chaque section dans [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X) était un bon point de départ.

Rapidement après cela, j'ai préféré utiliser [LeetCode](https://leetcode.com/) en raison de la capacité à exécuter et tester instantanément. LeetCode est une plateforme incroyable avec une grande communauté. À mon avis, elle propose des questions _les plus similaires_ à celles que vous rencontrerez lors des entretiens. Elle sauvegarde toutes vos solutions soumises et calcule également les temps d'exécution. Faites la plupart des questions "Faciles" et une bonne partie des questions "Moyennes" et vous devriez être bien :)

De plus, [Geeks For Geeks](http://www.geeksforgeeks.org/) est une excellente ressource avec des explications très détaillées pour des centaines de problèmes.

#### Points communs avec les entretiens pour les logiciels

Les quelques sujets suivants sont très similaires aux concepts des entretiens pour les logiciels, et ils sont fortement testés, alors assurez-vous de bien les connaître !

* Complexité algorithmique (temps et mémoire)
* Pointeurs
* Tableaux
* Listes chaînées
* Chaînes de caractères (et C-strings)
* Piles et files d'attente

Les sujets suivants ne sont pas vraiment testés, mais soyez familier avec eux conceptuellement. Sachez comment ils fonctionnent, leurs complexités et comment les résoudre à un niveau basique.

* Récursivité
* Arbres
* Tas
* Hachage
* Tri

### Au-delà du logiciel

C'est ici que commence le vrai travail sur les systèmes embarqués !

![Image](https://cdn-media-1.freecodecamp.org/images/H-cg252SKkDHBoTxRqvVExi2Re4dWEbJFJQz)

#### Manipulation de bits !!

Connaissez cela comme le fond de votre poche.

C'est probablement le **sujet le plus important** de vos entretiens. Sur ce sujet spécifique, faites _toutes_ les questions sur LeetCode.

* Sachez comment les nombres négatifs sont représentés en binaire
* Connaissez les différences entre les compléments à un et à deux
* Soyez capable de convertir entre binaire, décimal et hexadécimal
* L'opération XOR est _puissante_. Sachez tout ce qu'elle peut faire.

[Voici une excellente ressource](https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently) que j'ai utilisée pour des conseils et astuces utiles.

### Architecture informatique

Un proche second de la manipulation de bits.

Vous ne serez probablement pas invité à implémenter l'un de ces sujets, mais vous serez définitivement interrogé sur le fonctionnement des choses sous le capot. Certains sujets à étudier incluent...

* Registres importants et leur fonctionnement
* Différence entre caller-save et callee-save
* Fonctionnement des interruptions
* Une compréhension de base des pipelines d'instructions
* Caches, TLBs et comment la mémoire virtuelle est implémentée
* Divers types de mémoire (ROM vs RAM, DDR, EEPROM, Flash, etc)
* Remplissage de mémoire (instructions et classes)
* Ce qui se passe lorsque vous démarrez un système

#### Systèmes d'exploitation

Selon l'entreprise et le rôle, les systèmes d'exploitation peuvent être un sujet _très_ important. Vous ne serez pas invité à implémenter l'un de ces sujets, mais sachez comment les choses fonctionnent à un niveau conceptuel !

* Processus vs. Thread
* Fonctionnement du multithreading
* Systèmes d'exploitation en temps réel vs systèmes d'exploitation traditionnels
* Planification des tâches (FIFO, Round Robin, basé sur la priorité)
* Comment les sémaphores et les mutex protègent les données
* Inversion de priorité, héritage de priorité, spinlocks et interblocages
* Qu'est-ce qui rend une fonction 'réentrante' ?
* Sections critiques
* Niveaux de priorité dans les microcontrôleurs (EL0 — EL3)

#### Protocoles de communication

Connaissez les avantages et les compromis de l'utilisation des protocoles suivants :

* UART
* SPI
* I2C

En fonction de vos expériences précédentes, du rôle pour lequel vous postulez et de l'entreprise, vous pourriez être interrogé sur d'autres protocoles également. Typiquement, les entreprises ne s'attendent pas à ce que vous connaissiez ces protocoles spécifiques et vous formeront sur le tas. Mais avoir une compréhension de base peut toujours aider à impressionner l'intervieweur !

* **Automobile** : CAN, LIN
* **Sans fil** : 3G, 4G LTE, bases du 5G, 802.11 (Wifi), Bluetooth
* **Réseau** : HTTP, TCP/UDP, IP, 802.11 (Wifi), Ethernet

#### Fondamentaux du matériel

Le matériel n'est pas beaucoup testé pour les logiciels embarqués, mais selon le rôle, votre niveau d'interaction peut varier. Consultez les descriptions de poste et parlez aux personnes qui y travaillent pour avoir une meilleure idée !

* Minuteries de surveillance (Watchdog timers)
* Minuteries en général
* Détails sur _tous_ les périphériques que vous avez pu utiliser dans vos projets (accéléromètres, capteurs, LiDAR, moteurs, etc)

### Pratique

**La pratique est essentielle** — il n'y a vraiment pas moyen d'y échapper. Assurez-vous de consacrer _au moins_ 2 heures par jour à la préparation des entretiens, sans compter la candidature aux emplois et la prise de contact avec les recruteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/GT7z8aGsV2fxl4P2D8Vqa7vVGBWppn5wCXMQ)

Lors de la pratique sur LeetCode, commentez votre code. Expliquez votre algorithme et les complexités d'exécution. Chaque jour avant de commencer à coder, révisez les problèmes sur lesquels vous avez travaillé la veille. À la fin de la semaine, révisez chaque problème sur lequel vous avez travaillé cette semaine-là. Cela vous aidera à mieux vous souvenir des algorithmes et, petit à petit, vous deviendrez un pro de la reconnaissance de motifs.

Les entretiens pour les systèmes embarqués tendent à être plus conceptuels que les entretiens typiques pour les logiciels, en raison de la nature de certains des sujets testés. Pour ces domaines, j'ai maintenu un document Google de toutes les questions qui pourraient m'être posées, mais aussi de toutes leurs réponses. J'ai également inclus un lien vers un endroit où je peux lire plus d'informations pour être utile. Cela m'a aidé à rester organisé et à réviser plus rapidement.

> Beaucoup de gens m'ont demandé le lien vers le document Google, alors le voici : [Questions d'entretien pour les systèmes embarqués](https://docs.google.com/document/d/18HMyd-lFu1hWiixFLS2Pc7-SgyzDDqitzXbfAnUVeBE/edit?usp=sharing)

### À l'entretien

Vous y êtes arrivé — excellent travail !

Prenez une profonde inspiration. Il est temps de mettre tout votre travail acharné à bon escient. Habituellement, vous et l'intervieweur passerez en revue quelques questions conceptuelles. Vous discuterez également de vos expériences et projets précédents. Assurez-vous de pouvoir répondre aux questions sur vos contributions et aux divers défis que vous avez rencontrés en détail.

Si cet entretien se déroule à distance, il vous sera probablement demandé de coder dans un document partagé. Ayez du papier à portée de main pour noter les points importants et les diagrammes. Si cela vous aide, vous pouvez également avoir quelques notes que vous pouvez consulter pendant l'entretien. Je garde toujours une feuille des complexités algorithmiques de base à portée de main.

Vérifiez les fuseaux horaires. Vérifiez-les à nouveau. N'oubliez pas d'utiliser un casque. Soyez dans un environnement calme pour éviter les perturbations. Les problèmes de communication ne feront que rendre l'entretien plus difficile.

![Image](https://cdn-media-1.freecodecamp.org/images/tz9ML84FNkxqAsD8TFCW47fa9z72LsPIAVqm)

#### Lorsque vous obtenez la question

Ne commencez jamais à coder tout de suite. Aussi important que d'arriver à la bonne solution, l'intervieweur regarde vraiment votre approche.

Prenez un instant et répétez la question à l'intervieweur, juste pour vous assurer que vous êtes sur la même longueur d'onde. Et s'il y a des malentendus, l'intervieweur peut toujours répéter et clarifier tout doute.

Ensuite, comprenez la portée du problème

* Quelle est la taille de l'entrée ?
* Est-elle triée ?
* Y a-t-il une certaine complexité de temps ou de mémoire que vous devez respecter ?
* Y a-t-il des doublons ? Des valeurs négatives ? Des valeurs vides ?
* Devez-vous effectuer une vérification des erreurs ?

Ensuite, parcourez votre algorithme. Commencez par l'approche la plus basique, brute-force. Elle peut être super inefficace et mentionnez que vous l'utilisez comme point de départ. Expliquez les complexités de temps et de mémoire et pourquoi c'est une mauvaise solution.

À partir de là, il est temps d'optimiser. Recherchez généralement les endroits où vous stockez des quantités inutiles de données ou répétez des sections de code. Pour les applications embarquées, la mémoire est importante ! Au lieu d'utiliser un tableau ou un vecteur, envisagez d'utiliser un bitset. Si vous ne traitez que des valeurs entre 0 et 31, basculez les bits dans un entier ! C'est ici que la manipulation de bits est utile.

Il est important de réfléchir à voix haute pendant que vous réfléchissez. Si vous êtes bloqué ou que vous allez dans la mauvaise direction, l'intervieweur peut vous aider à revenir sur la bonne voie. Une fois que vous êtes tous les deux d'accord sur une solution, il est enfin temps de commencer à coder.

#### Écrire du code

Lire le code des autres n'est pas toujours la chose la plus agréable. Facilitez un peu la tâche de votre intervieweur en utilisant un bon style. Cela ne signifie pas que vous devez mettre _chaque_ point-virgule ou accolade, mais indentiez bien et utilisez des noms de variables significatifs. Essayez d'écrire proprement et utilisez bien l'espace du tableau blanc.

Pendant que vous écrivez du code, continuez à vérifier par rapport à l'algorithme que vous avez conçu. Similaire à la phase de brainstorming, _réfléchissez à voix haute_. Fournissez des commentaires verbaux à votre code. À chaque étape, expliquez ce que vous vérifiez, ce que vous espérez atteindre et les décisions de conception que vous prenez.

Une fois que vous avez terminé d'écrire du code, ne dites pas que vous avez terminé. Prenez du recul et analysez votre code d'un point de vue de haut niveau. Vérifiez les entrées, les sorties et votre logique pour détecter les bugs. Assurez-vous de repérer les erreurs de décalage d'un ! Ensuite, parcourez le code avec quelques cas de test. S'il y a des problèmes que vous voyez, révisez et retravaillez votre code si nécessaire.

Selon l'entretien, vous pourriez avoir une grande question ou quelques petites. Mais une fois que l'intervieweur a accepté votre solution, il y a une chance qu'il ou elle l'étende avec différents paramètres. Vous n'aurez probablement pas à retravailler le code, mais vous pourriez avoir à discuter de la façon de changer des parties de votre approche. Comme je l'ai mentionné auparavant, la mémoire est importante dans les applications embarquées. Donc une question de suivi courante est généralement sur l'optimisation supplémentaire de la mémoire.

### Réflexions finales

La nature des entretiens pour les logiciels embarqués dépend fortement de l'entreprise et du travail qu'elles priorisent. Les entreprises travaillant sur un protocole de communication spécifique rechercheront des choses différentes qu'une entreprise développant un système d'exploitation en temps réel ou une entreprise travaillant sur un produit IoT.

Je voulais utiliser cet article comme un endroit pour partager quelques thèmes communs dans les entretiens que j'ai eus, mais cela n'est en aucun cas exhaustif. Cela est destiné à être utilisé comme un point de départ. Mais n'hésitez pas à contacter les employés actuels et à consulter [Glassdoor](https://www.glassdoor.com/index.htm) pour des conseils d'entretien spécifiques à l'entreprise.

Les entretiens sont difficiles, mais bien se préparer et travailler dur maintenant peut vous aider à décrocher un emploi que vous aimez :)

J'espère que cet article vous a aidé et je vous souhaite bonne chance !

Si vous avez aimé cet article, n'oubliez pas de laisser un ?. Vous pouvez également me suivre sur T[witter](https://twitter.com/rohandasika) ou Q[uora](https://www.quora.com/profile/Rohan-Dasika))