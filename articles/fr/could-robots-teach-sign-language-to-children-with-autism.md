---
title: J'ai aidé à construire un robot qui enseigne la langue des signes aux enfants
  atteints d'autisme. Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-16T15:16:40.000Z'
originalURL: https://freecodecamp.org/news/could-robots-teach-sign-language-to-children-with-autism
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/back-1.png
tags:
- name: Autism
  slug: autism
- name: education
  slug: education
- name: educational technology
  slug: educational-technology
- name: robotics
  slug: robotics
seo_title: J'ai aidé à construire un robot qui enseigne la langue des signes aux enfants
  atteints d'autisme. Voici ce que j'ai appris.
seo_desc: "By Minja Axelsson\nIn Spring 2018, I conducted a pilot study of a robot\
  \ teaching sign language to children with autism. This blog post reflects on the\
  \ results of the study, and our team’s process of designing the robot. \nRobotics,\
  \ Sign Language, and C..."
---

Par Minja Axelsson

Au printemps 2018, j'ai mené une étude pilote sur un robot enseignant la langue des signes à des enfants atteints d'autisme. Cet article de blog reflète les résultats de l'étude et le processus de notre équipe pour concevoir le robot. 

### Robotique, Langue des Signes et Enfants atteints d'Autisme

Pour commencer, répondons à la première grande question : **Pourquoi utiliser un robot dans la thérapie de l'autisme ?** [Les personnes atteintes d'autisme ont une préférence d'attention pour les objets plutôt que pour les personnes](http://ekirjasto.kirjastot.fi/ekirjat/autismin-kirjo-ja-kuntoutus), et [les enfants atteints d'autisme ont montré plus d'intérêt pour la thérapie lorsqu'elle implique des composants technologiques ou robotiques](https://www.researchgate.net/profile/Janek_Dubowski/publication/228364332_Does_appearance_matter_in_the_interaction_of_children_with_autism_with_a_humanoid_robot_Interact_Stud/links/54b7a0970cf2bd04be33b122/Does-appearance-matter-in-the-interaction-of-children-with-autism-with-a-humanoid-robot-Interact-Stud.pdf). De plus, [le fonctionnement d'un robot peut être strictement contrôlé, ce qui peut rendre la thérapie moins accablante pour les personnes autistes](https://ri.cmu.edu/pub_files/2009/1/fulltext.pdf).

Ensuite, la deuxième grande question : **Pourquoi enseigner la langue des signes aux enfants atteints d'autisme ?** Les personnes atteintes de troubles du spectre autistique (TSA) rencontrent des problèmes de communication : [40 à 50 % des personnes atteintes de TSA sont fonctionnellement muettes à l'âge adulte](https://books.google.fi/books?hl=en&lr=&id=0Smd-xouZjYC&oi=fnd&pg=PA3&dq=Bogdashina,+O.+(2004).+Communication+issues+in+autism+and+Asperger+syndrome:+Do+we+speak+the+same+language%3F.+Jessica+Kingsley+Publishers&ots=FBSfAPlA_z&sig=uyC0Dms-31cQRue-wilVK5SUQ-w&redir_esc=y#v=onepage&q=Bogdashina%2C%20O.%20(2004).%20Communication%20issues%20in%20autism%20and%20Asperger%20syndrome%3A%20Do%20we%20speak%20the%20same%20language%3F.%20Jessica%20Kingsley%20Publishers&f=false). Pour atténuer cela, ils utilisent des méthodes de Communication Améliorative et Alternative (CAA). [La langue des signes assistée, une forme simplifiée de la langue des signes, est la forme la plus courante de CAA](https://www.worldcat.org/title/introduction-to-augmentative-and-alternative-communication-sign-teaching-and-the-use-of-communication-aids-for-children-adolescents-and-adults-with-developmental-disorders/oclc/44603909). D'autres formes courantes de CAA sont les images symboliques et les photographies.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/symbolic.png)
_Un exemple de système de communication par images symboliques utilisé par les enfants atteints d'autisme : « Nous faisons des exercices. »_

L'idée de combiner ces deux domaines, la robotique pour les enfants atteints de TSA et la langue des signes pour les enfants atteints de TSA, est venue à l'origine du [district de santé de Satakunta](https://www.satasairaala.fi/). Satakunta est une petite région du sud-ouest de la Finlande, avec une population de 225 000 habitants. Le responsable qualité du district avait lu un article sur [un robot utilisé pour enseigner la langue des signes à des enfants neurotypiques](https://link.springer.com/article/10.1007/s12369-015-0307-x), et voulait étudier la même méthode avec des enfants autistes.

Satakunta a découvert que l'entreprise pour laquelle je travaille ([Futurice](https://www.futurice.com/)) avait construit un robot humanoïde. Ils ont pris contact, et nous avons assemblé une équipe pluridisciplinaire qui redessinerait et modifierait le robot humanoïde de Futurice pour répondre à cet objectif. Notre équipe comptait trois roboticien·ne·s de Futurice et trois expert·e·s en traitement de l'autisme de Satakunta : une neuropsychologue, une orthophoniste et le responsable qualité.

### Comment Devons-Nous Concevoir le Robot ?

Le robot humanoïde construit par Futurice était un robot InMoov. [L'InMoov est conçu par le sculpteur français Gaël Langevin](http://inmoov.fr/). Il a rendu les schémas et le logiciel du robot open source et disponibles en ligne pour tout le monde. 

En utilisant ces ressources, Futurice a construit son propre InMoov. Satakunta voulait utiliser l'InMoov en raison de ses mains agiles qui lui permettent de signer. Son apparence humanoïde était également un avantage : l'une des neuropsychologues de Satakunta pensait qu'un robot ressemblant à un humain serait le meilleur pour cette solution.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/inmoov.jpeg)
_La forme originale du robot humanoïde open source InMoov, conçu par Gaël Langevin. Image Wikimedia Commons._

Cependant, l'InMoov n'était pas prêt tel quel. Pour rendre le robot adapté aux enfants atteints d'autisme, nous devions modifier sa forme, son comportement, ses interactions et son environnement. 

Mon travail était de concevoir ces quatre dimensions du robot. Je devais également concevoir l'étude d'interaction humain-robot où les enfants rencontreraient et signeraient avec le robot. Heureusement, la nature open source du logiciel et du matériel du robot rendrait relativement facile la réalisation des modifications nécessaires.

Nous voulions prendre en compte les caractéristiques du TSA lors de la conception du robot. Le TSA est caractérisé par des problèmes de communication et de langage, des problèmes de comportement social, une inflexibilité des routines et des problèmes de formation d'une perception holistique de l'environnement. Cependant, l'autisme est un spectre, donc ces caractéristiques se présentent différemment chez différentes personnes. En raison de ces différentes présentations, nous savions que nous ne pouvions pas concevoir un robot qui bénéficierait à tout le monde. Néanmoins, nous voulions trouver la meilleure solution qui servirait le plus d'enfants atteints de TSA.

Au cours du projet, l'équipe a créé cinq directives de conception pour le robot, qui adapteraient sa conception aux enfants autistes. Par exemple, la préoccupation qu'un enfant pourrait se distraire pendant l'expérience a été soulevée par les spécialistes de l'autisme. L'équipe a convenu que pour éviter de confondre l'enfant, le comportement du robot devait être cohérent et structuré. Cela a été défini comme la directive : « comportement cohérent, structuré et simple ». Pour suivre cette directive, l'orthophoniste et moi avons créé un script strict des interactions entre le robot et l'enfant. Les cinq directives ont été formulées de manière similaire lors de discussions de co-conception.

#### Directives de conception pour un robot destiné à être utilisé avec des enfants autistes :

1. Forme simple
2. Comportement cohérent, structuré et simple
3. Expérience et environnement positifs, encourageants et récompensants
4. Complexité modulaire
5. Modularité spécifique aux préférences de l'enfant

Les directives de conception ont aidé l'équipe à maintenir une conception logique et uniforme pour le robot et ont formé une base pour toutes les décisions prises lors du processus de conception.

### Éthique Intégrée

Alors que l'équipe discutait de la conception du robot et des expériences, plusieurs considérations éthiques ont été soulevées. Ces considérations éthiques ont été intégrées dans le robot finalisé.

**Sécurité physique** — Les utilisateurs peuvent potentiellement être pincés ou écrasés par un robot. Pour atténuer cette préoccupation, nous avons décidé d'empêcher les enfants de toucher le robot pendant les interactions. Pour y parvenir, nous avons décidé que l'orthophoniste serait dans la pièce avec l'enfant pour l'empêcher de s'approcher du robot, si nécessaire.

**Sécurité des données** — Il est primordial que les données de l'utilisateur restent sécurisées, surtout dans les applications de santé. Ici, nous avons décidé de garder toutes les données des enfants participant à l'étude cryptées. Nous n'avons également enregistré aucune donnée inutile.

**Renforcement du comportement approprié** — Les personnes peuvent apprendre de mauvaises manières des robots. Par exemple, [les enfants ont oublié d'utiliser un langage poli tel que « s'il vous plaît » et « merci » après avoir interagi avec l'agent vocal Alexa](https://thriveglobal.com/stories/artificial-intelligence-alexa-impact-children-expert-opinion-tips/). Alexa ne demande pas explicitement un langage poli, ce qui amène les personnes à se comporter mal envers elle. Dans ce cas, nous ne voulions pas que les enfants apprennent à mal traiter le robot et potentiellement généraliser ce mauvais comportement aux personnes. Nous avons décidé que le thérapeute interviendrait dans tous les mauvais comportements envers le robot.

**Égalité entre les utilisateurs** — Les algorithmes d'intelligence artificielle se sont révélés racistes ou sexistes par le passé (par exemple, [COMPAS, un algorithme de prédiction du taux de récidive utilisé aux États-Unis, était biaisé envers les Afro-Américains](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)). Si un robot utilise des algorithmes pour fonctionner, les concepteurs de l'algorithme doivent être prudents. Une autre chose à considérer est la forme du robot. Les conceptions de robots ont été montrées pour renforcer les stéréotypes de genre, avec des robots « géniaux » souvent étiquetés comme masculins, et des robots « de service » comme féminins. Dans notre cas, nous voulions concevoir un robot qui soit neutre en termes de genre, afin que chaque enfant participant à l'étude puisse se sentir bienvenu. Pour ce faire, le robot n'a reçu aucun signe distinctif de genre.

**Transparence** — Si l'utilisateur comprend comment le robot fonctionne et prend des décisions, il peut calibrer son niveau de confiance en lui. Dans notre cas, nous avons décidé d'informer les enfants et leurs accompagnateurs de la nature téléopérée du robot à la fin de l'étude. Ainsi, ils pourraient éviter de former de fausses hypothèses sur l'état de la robotique aujourd'hui et sur la manière dont elle peut être appliquée à la thérapie de l'autisme.

**Considération émotionnelle** — La recherche a montré que les humains traitent les robots comme s'ils étaient vivants, même lorsqu'ils ne le sont clairement pas. Les personnes forment des liens émotionnels avec les robots. Cela doit être pris en compte dans la conception : quelle force de lien est souhaitable pour ce cas d'utilisation ? Dans ce cas, nous ne voulions pas que l'enfant ou ses accompagnateurs pensent que le robot remplaçait le lien entre l'enfant et le thérapeute. Pour garantir cela, l'orthophoniste resterait dans la pièce avec l'enfant tout le temps.

### Un Acte d'Équilibriste

Construire une technologie complexe (robotique) pour un domaine complexe (thérapie de l'autisme) est difficile. L'espace problématique était peu intuitif pour les deux côtés de l'équipe : les spécialistes de l'autisme n'étaient pas familiers avec les limitations techniques, et les roboticien·ne·s n'avaient aucune connaissance du groupe d'utilisateurs. 

La conception était un acte d'équilibriste : une petite modification en apparence dans la conception pouvait entraîner une grande quantité de travail technique. Et vice versa, certaines modifications qui étaient significatives en termes de conception pouvaient être faciles à mettre en œuvre techniquement. 

C'est là que j'ai passé la plupart de mon temps, à harmoniser les différents points de vue de l'équipe en une bonne conception qui serait réaliste à exécuter dans notre délai de 6 mois. Ensemble, nous avons pris une série de décisions équilibrant l'expérience utilisateur et la complexité technique.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/robo.png)
_L'InMoov final avec modifications : nouvelles mains Ada, lumières attachées à sa main droite et un écran sur sa poitrine._

Lors de la conception d'un robot social, il y a beaucoup de pièces mobiles (littéralement et figurativement). Les caractéristiques du robot affectent toutes les autres. Le contexte d'opération du robot affecte son comportement, ce qui affecte la manière dont il interagit avec l'utilisateur, ce qui affecte sa forme. Séparer ces considérations de conception et les cristalliser en tâches techniques distinctes et réalisables était un défi.

La modification du robot depuis sa forme originale a pris 4,5 mois (la construction originale avait été assemblée en 9 mois). Toutes nos modifications suivaient les directives de conception : par exemple, nous avons changé la voix humanoïde du robot en une voix robotique, pour lui donner une « forme simple » (directive 1).

Pour faire de l'InMoov un meilleur professeur de langue des signes, nous avons apporté quelques grands ajustements. Nous lui avons donné de nouvelles [mains Ada, conçues par Open Bionics](https://openbionicslabs.com/obtutorials/ada-v1-assembly), et construites par [l'Université des Sciences Appliquées Metropolia](https://www.metropolia.fi/en/). Nous avons également intégré un écran dans sa poitrine et des lumières sur ses bras. L'écran a été ajouté pour fournir un autre mode de communication (les photographies sont souvent utilisées en CAA), et les lumières ont été ajoutées pour capter l'attention de l'enfant.

### 10 Enfants et un Robot

10 enfants ont participé aux expériences. Certains sont venus avec leurs parents, d'autres avec d'autres personnes de soutien. Deux roboticien·ne·s (dont moi) étaient dans la pièce adjacente à la salle d'expérience, opérant le robot et observant l'expérience via un flux vidéo. Un·e troisième roboticien·ne était présent·e pour résoudre tout problème qui pourrait survenir. L'orthophoniste était dans la salle d'expérience avec chaque enfant, facilitant l'interaction entre l'enfant et le robot, et intervenant si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/signs.png)
_Les 9 mots que le robot a signés, et les images correspondantes sur son écran._

Le robot a effectué 9 signes. Avec ⅓ des signes, il a également fait clignoter les lumières sur son bras. Avec un autre ⅓ des signes, il a affiché une image correspondant au signe sur son écran. Ces 3 conditions de conception différentes ont été examinées pour voir laquelle était la plus efficace.

J'ai été surprise par la manière dont chaque enfant interagissait différemment avec le robot. Quelques enfants ont signé avec une précision quasi parfaite tout au long de l'expérience, imitant tous les signes du robot en seulement 6 minutes. Certains ont pris jusqu'à 28 minutes, luttant avec chaque signe. Un enfant en particulier, qui n'était pas très enthousiaste à l'idée de signer, ne pouvait pas arrêter de rire du robot. L'enfant a continué à essayer soit d'embrasser soit de se jeter sur le robot tout au long de l'expérience, avec l'orthophoniste et la neuropsychologue se précipitant après lui pour l'arrêter à temps.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/front.png)
_Un enfant signe avec le robot (photo avec permission)._

![Image](https://www.freecodecamp.org/news/content/images/2019/08/back.png)
_L'orthophoniste signale aux opérateurs du robot que l'enfant a signé correctement (photo avec permission)._

### Les Enfants Imitent et Portent Attention au Robot

J'ai mesuré la précision des signes des enfants et leur focus d'attention. Les enfants et leurs accompagnateurs ont également rempli des enquêtes où ils ont donné leur opinion sur le robot.

#### Ce que nous avons appris :

**1. Les enfants pouvaient imiter le robot et lui portaient attention**

7 enfants sur 10 ont réussi à imiter le robot au moins une fois. 70 % du temps, ils ont gardé leur regard sur le robot, indiquant un focus d'attention. 8 accompagnateurs sur 8 qui ont rempli l'enquête ont également noté que les enfants avaient une connexion avec le robot.

**2. L'image sur l'écran du robot était bonne**

Le robot affichait une image sur son écran simultanément à la signature ⅓ du temps. Les accompagnateurs des enfants ont trouvé les images utiles et ont pensé qu'elles pourraient aider les enfants à apprendre.

**3. Le robot était perçu comme bon, mais un peu effrayant**

Les enfants et leurs accompagnateurs ont évalué les expériences des enfants avec le robot comme bonnes. Cependant, certains enfants et leurs accompagnateurs ont noté que les enfants trouvaient le robot effrayant. Les facteurs qui créent cette peur doivent être identifiés et réduits dans les conceptions futures.

**4. La performance des signes doit être meilleure**

L'orthophoniste et les accompagnateurs des enfants ont noté que le robot ne signait pas tous les mots correctement, ce qui pourrait affecter la compréhension des enfants.

#### Choses encore à apprendre :

**1. Les enfants comprennent-ils les signes ?**

Pour cette expérience, je n'ai mesuré que si les enfants imitaient les signes. Des expériences futures sont nécessaires pour vérifier si les enfants les comprennent.

**2. Qui bénéficie le mieux du robot ?**

Tous les enfants n'ont pas réagi de la même manière au robot. Il est peu probable que ce type de thérapie de langue des signes basée sur un robot soit utile à tous les enfants atteints d'autisme. Les expériences futures devraient examiner à qui cette thérapie est adaptée. Cette variation de bénéfice est soutenue par les résultats de l'enquête des accompagnateurs : 6 sur 8 pensaient que le robot pourrait potentiellement être bénéfique en tant que tuteur de langue des signes.

**3. Comment entrer les commandes de l'orthophoniste ?**

Pour utiliser le robot à l'avenir, le thérapeute doit pouvoir contrôler indépendamment le robot. Pour les futures implémentations, une télécommande ou une interface utilisateur pour programmer le comportement et les interactions du robot pourrait être utile.

**4. Comment les directives 4 et 5 affecteront-elles la conception ?**

Pour cette expérience, j'ai utilisé une conception statique du robot. Seules ses interactions ont changé (utilisation de son écran et de ses lumières à différents moments). Des recherches futures sont nécessaires pour examiner les directives de conception « modularité de la complexité » (directive 4) et « modularité spécifique aux préférences des enfants » (directive 5). Celles-ci pourraient aider à adapter le robot à différents utilisateurs.

### L'Avenir des Tuteurs Robotiques de Langue des Signes

Les personnes interagissant de près avec des robots peuvent induire des critiques. La préoccupation la plus importante est que les robots remplacent les humains. Dans ce cas, le robot n'est pas destiné à remplacer les soins humains, mais plutôt à les augmenter et à les soutenir.

Les séances de thérapie sont exigeantes pour les thérapeutes. Ils doivent planifier et mener la séance, tout en traitant avec un·e participant·e potentiellement peu coopératif·ve. À l'avenir, des outils technologiques pourraient être utilisés pour réduire la charge cognitive du thérapeute. Le robot pourrait effectuer les signes, tandis que le thérapeute pourrait se concentrer sur l'encouragement, le tutoriel et la gestion de l'enfant. Avec une charge cognitive réduite, les séances pourraient être plus longues et donc plus approfondies. 

Le même effet pourrait potentiellement être atteint si le robot était situé dans la maison de l'enfant : l'enfant aurait un outil cohérent pour pratiquer les signes, et le robot ne serait pas ennuyé ou frustré par la pratique répétitive.

À ma connaissance, il s'agissait de la première instance d'utilisation d'un robot pour enseigner la langue des signes à des enfants atteints d'autisme. J'espère que cette recherche sera poursuivie. J'espère que notre pilote peut éclairer sur la manière de développer cette application à l'avenir.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/science.png)
_La science, surtout les études pilotes, nécessite parfois de l'improvisation : les lumières du dos du robot étaient réfléchies sur une fenêtre derrière lui, ce qui aurait pu distraire les enfants. Nous avons fabriqué un bloqueur de réflexion de lumière pour le dos du robot, à partir d'une serviette volée dans notre hôtel (nous l'avons payée)._

---

%[https://www.youtube.com/watch?v=JKWnwpTl774]

L'étude complète est disponible sous forme :

Axelsson, M., Racca, M., Weir, D., Kyrki, V. (2019). A Participatory Design Process of a Robotic Tutor of Assistive Sign Language for Children with Autism. In _2019 28th IEEE International Symposium on Robot and Human Interactive Communication (RO-MAN)_. IEEE. **Accepté.**

L'étude est basée sur mon mémoire de master à l'Université Aalto, [disponible ici](https://aaltodoc.aalto.fi/handle/123456789/34183).

Le projet a été financé par Robocoast de Prizztech et le fonds FEDER, et Futurice.