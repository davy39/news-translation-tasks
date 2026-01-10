---
title: 'Comment améliorer vos ventilateurs Arduino : Introduction aux RTS et SCS pour
  les conceptions de ventilateurs COVID-19 de fortune'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T08:10:52.000Z'
originalURL: https://freecodecamp.org/news/programming-the-electronics-for-covid-19-ventilators
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bd5740569d1a4ca2e2b.jpg
tags:
- name: arduino
  slug: arduino
seo_title: 'Comment améliorer vos ventilateurs Arduino : Introduction aux RTS et SCS
  pour les conceptions de ventilateurs COVID-19 de fortune'
seo_desc: 'By Armstrong Subero

  The world as we know it was recently taken by storm. That storm was the outbreak
  of the COVID-19 pandemic. This has in turn created a shortage of ventilators world
  wide which has led many people to foray into the world of ventilat...'
---

Par Armstrong Subero

Le monde tel que nous le connaissons a récemment été pris d'assaut. Cette tempête était l'épidémie de la pandémie de COVID-19. Cela a à son tour créé une pénurie de ventilateurs dans le monde entier, ce qui a conduit de nombreuses personnes à s'aventurer dans le monde de la conception de ventilateurs. 

**Il y a juste un problème : beaucoup de gens basent leurs conceptions autour de la plateforme Arduino**. Bien que cela puisse être bon pour une preuve de concept, vous ne voulez pas l'utiliser pour un soutien vital réel sauf en cas de nécessité absolue.

C'est parce que des plateformes comme l'Arduino ont été conçues comme une plateforme à utiliser dans un environnement d'apprentissage. Elles n'ont pas été conçues pour la conception en temps réel et critique pour la sécurité requise pour construire des ventilateurs. 

Cependant, il existe quelques solutions de contournement que vous pouvez employer pour adapter la plateforme à une utilisation dans un ventilateur d'urgence de fortune si aucun n'est disponible. 

Dans cet article, nous discuterons des systèmes en temps réel et des systèmes critiques pour la sécurité. Espérons que vous pourrez utiliser certains de ces principes dans vos propres conceptions de systèmes de contrôle de ventilateurs pour améliorer leur sécurité et leur fiabilité. 

Puisque le public cible est principalement des développeurs web qui essaient de se lancer dans la conception embarquée, je vais essayer de rendre cet article aussi autonome que possible. Rejoignez-moi alors que nous plongeons du navigateur dans le domaine de la conception de systèmes embarqués et nous rapprochons du matériel pour concevoir nos ventilateurs. 

## **Systèmes embarqués**

Pour toute son utilité, un ventilateur est simplement un système embarqué. Un système embarqué est un système conçu pour accomplir une fonction et la réaliser efficacement, avec une grande fiabilité et une intervention minimale de l'utilisateur.

Pour y parvenir, un système embarqué se compose de deux éléments : un système matériel ainsi qu'un composant logiciel pour exécuter la configuration matérielle.

Un système embarqué classique est généralement alimenté par un dispositif de contrôle qui intègre généralement de la RAM, de la ROM, ainsi qu'une série de périphériques embarqués sur la carte pour permettre au système d'accomplir sa tâche. 

Les systèmes embarqués modernes peuvent parfois être basés sur un processeur d'applications, qui peut intégrer un GPU, plusieurs cœurs CPU, des codecs multimédias et d'autres dispositifs. Bien que les processeurs d'applications puissent être utilisés dans des systèmes embarqués, ils sont principalement utilisés dans des systèmes informatiques à usage général tels qu'un smartphone. 

Le logiciel qui s'exécute sur un système embarqué est appelé firmware. Il est appelé firmware parce qu'une fois écrit dans la ROM, il n'est pas censé changer fréquemment. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image.png)
_Composants d'un système embarqué_

Pensez à un ventilateur. Son objectif principal est de fournir une ventilation mécanique pour maintenir les patients en vie. Il effectue une fonction et le fait avec un haut degré de fiabilité, à tel point qu'il peut être utilisé comme système de maintien en vie. Très rarement, vous trouvez quelqu'un qui change le firmware d'un tel dispositif une fois déployé.  

## Le composant matériel

Comme mentionné précédemment, le système embarqué possède un composant matériel qui intègre la RAM, la ROM et d'autres dispositifs dans un seul package. Ce dispositif est appelé microcontrôleur. 

Il existe plusieurs microcontrôleurs populaires aujourd'hui. Les PIC et AVR de Microchip Technology et le STM32 de STMicroelectronics sont les plus populaires. L'Arduino classique utilise un microcontrôleur AVR à son cœur. 

Quelle que soit la marque, le microcontrôleur comprendra un cœur de processeur, de la mémoire et un moyen de fournir des entrées et des sorties, également connu sous le nom d'E/S. 

Les microcontrôleurs comprennent également de la mémoire qui est divisée en deux catégories : la mémoire de données et la mémoire de programme. 

La mémoire de données est la mémoire utilisée pour stocker les données qui seront utilisées par le microcontrôleur pendant l'exécution. Elle est généralement de quelques dizaines à quelques centaines de kilo-octets de SRAM. La mémoire de données est volatile et est perdue lorsque l'alimentation est coupée du dispositif.

La mémoire de programme, en revanche, stocke effectivement la mémoire qui sera utilisée par le microcontrôleur. Elle se compose de Flash (pensez à la mémoire de votre clé USB) ou de FRAM (RAM ferroélectrique) et n'est pas volatile. La taille de la mémoire de programme varie généralement de quelques octets à quelques mégaoctets sur les systèmes modernes. 

Les broches d'entrée et de sortie (E/S) sur le microcontrôleur sont ce qui permet au dispositif de communiquer avec des dispositifs externes tels que des capteurs et d'autres puces qui effectuent diverses fonctions telles que l'extension de mémoire et même l'ajout d'E/S supplémentaires au dispositif. 

Un microcontrôleur intégrera également des périphériques pour effectuer des conversions analogique-numérique (A/N) et numérique-analogique (N/A). 

C'est parce que notre monde est de nature analogique et que la conversion analogique-numérique (CAN) convertira les données du monde réel dans un format que notre microcontrôleur peut traiter. Si vous avez un enregistreur vocal, un capteur de microphone ainsi qu'un microcontrôleur convertiront votre voix en un format numérique et le stockeront. 

Le microcontrôleur peut également avoir des moyens de effectuer une conversion numérique-analogique (CNA) par laquelle les données numériques peuvent être converties en un format analogique que nous pouvons utiliser dans le monde réel. 

Dans notre exemple d'enregistreur vocal, cela serait applicable lorsque vous devez lire votre voix enregistrée. Les informations numériques stockées sont converties en son que nous pouvons détecter dans notre monde analogique. 

Lorsque nous combinons tout cela, nous obtenons un diagramme de bloc du matériel typique d'un microcontrôleur. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-1.png)
_Diagramme de bloc crude d'un microcontrôleur_

Maintenant que nous avons une compréhension de base du matériel, examinons le composant logiciel. 

## Le composant logiciel

Aussi bon que soit votre matériel, sans le logiciel pour le contrôler, il est aussi utile qu'un presse-papiers. Le logiciel dans les systèmes embarqués se divise généralement en trois catégories de base : 

* les systèmes d'exécution cyclique, 
* les systèmes basés sur des machines à états finis, et 
* les systèmes construits à l'aide d'un système d'exploitation en temps réel. 

La différence entre ces trois types de systèmes logiciels est basée sur la manière dont ils gèrent les tâches. Lorsque nous parlons de tâches, ce dont nous parlons est la plus petite unité d'exécution dans votre firmware. 

### Systèmes d'exécution cyclique

Un système d'exécution cyclique fonctionne en ayant toutes les tâches du programme contenues dans une boucle infinie. Ces systèmes ont un point d'entrée principal du programme, puis le système cycle à travers une liste de tâches. Il s'agit du type de conception de firmware le plus simple et il est utilisé pour les systèmes de base. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-2.png)
_Système d'exécution cyclique_

Ce système aura un point d'entrée de programme qui configurerait généralement le matériel et mettra en place les horloges du système et les tâches de base de démarrage. Une fois que le programme entre dans la boucle infinie, il exécutera la Tâche un, puis la Tâche deux et enfin la Tâche trois.

### Machine à états finis

Bien que le système d'exécution basé sur le cycle soit simple et efficace pour la plupart des tâches, parfois vous avez besoin d'un peu plus de contrôle sur le flux du programme. Lorsqu'un concepteur peut utiliser ce que l'on appelle un système de Machine à États Finis (FSM).

Dans une FSM, nous pouvons penser à chaque tâche comme un état dans lequel la machine peut se trouver. La FSM aura un état initial et après cela, chaque état s'exécutera en fonction d'une certaine instruction conditionnelle. Le tourniquet d'acceptation de pièces est généralement utilisé (comme le hello world des machines à états) pour expliquer le concept d'une machine à états. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-3.png)
_"FSM du tourniquet d'acceptation de pièces". (Source : Structures de données et algorithmes sans code par Armstrong Subero)._

Nous avons un point noir qui représente l'état initial ainsi que deux états, verrouillé et déverrouillé. Le tourniquet dans un état verrouillé se déverrouillera une fois que vous aurez inséré une pièce. Même si vous poussez sur la machine, elle ne se déverrouillera pas tant que vous n'aurez pas inséré une pièce. Une fois que vous avez inséré une pièce, la machine entre dans l'état déverrouillé et y restera tant qu'une pièce est présente.

Si vous poussez sur le tourniquet alors qu'il est dans l'état déverrouillé, cette condition fera passer la machine dans un état verrouillé dans lequel elle restera jusqu'à ce qu'une pièce soit à nouveau insérée.

Aussi simple que cela puisse paraître, cette méthode de modélisation des tâches du programme en tant qu'états qui se transforment en fonction des conditions est une méthode puissante de conception de firmware de systèmes embarqués. C'est la méthode que j'utilise le plus souvent lorsque je conçois mes propres systèmes.

## Les ventilateurs sont des systèmes en temps réel 

Les systèmes en temps réel (RTS) sont des systèmes qui doivent répondre à des exigences strictes en termes de temps de réponse. Dans un système en temps réel, il n'y a pas de place pour le compromis. 

De tels systèmes doivent garantir qu'ils effectueront une action dans un délai donné. L'échec de l'exécution d'une action dans un certain temps peut entraîner la perte de vies ou des dommages graves aux biens.

C'est la catégorie de systèmes dans laquelle un ventilateur entre. 

Lorsque qu'un patient a besoin d'un ventilateur, c'est parce qu'il ne peut pas respirer correctement et a besoin d'une assistance mécanique pour respirer, comme celle fournie par un ventilateur. Un ventilateur peut effectuer une ventilation mandataire continue (CMV), ce qui signifie que le patient devra recevoir un nombre minimum de respirations garanties par la machine. 

L'échec de fournir le nombre minimum de respirations requises entraînera la mort du patient. Cela signifie que l'électronique de contrôle doit être capable de fonctionner sans défaillance. 

Pour y parvenir, la plupart des systèmes en temps réel utiliseront ce que l'on appelle un système d'exploitation en temps réel (RTOS) pour garantir que les nombreuses tâches à effectuer par le dispositif peuvent toutes être exécutées sans échec.

Les RTOS utilisent un planificateur pour gérer les tâches et limiter la manière dont chaque tâche utilise les ressources. Le noyau gérerait la manière dont chaque tâche peut utiliser les ressources matérielles en fonction de leur priorité.

Pensez aux conceptions actuelles de ventilateurs de fortune qui existent. Les plus prometteuses sont construites à l'aide d'un resuscitateur à valve de sac qui utilise des moteurs pour actionner des bras mécaniques qui pressent sur le resuscitateur à valve de sac et effectuent les fonctions de ventilateur. 

Cependant, que se passera-t-il si le moteur tombe en panne ? Peut-être pouvons-nous ajouter un capteur infrarouge ou ultrasonique qui mesurera la distance du bras mécanique par rapport à un certain point et garantira qu'il atteint une distance particulière. Ces capteurs peuvent également garantir qu'il revient au point de départ. 

Cependant, le microcontrôleur principal qui lit ces capteurs a besoin de temps pour traiter les informations. Que se passe-t-il si un capteur tombe en panne ? Le microcontrôleur doit-il se bloquer en attendant les données du capteur ? Une défaillance du capteur empêchera-t-elle le moteur d'être actionné à temps ?

Pour garantir que chaque tâche se déroule à un certain moment, le planificateur n'allouera du temps de traitement à la tâche que comme désigné par le concepteur du système. 

Ainsi, si un capteur tombe en panne, une fois le temps alloué à la lecture de ce capteur écoulé, le microcontrôleur passera à l'autre tâche d'actionnement du moteur, ce qui maintiendra le système en fonctionnement. 

L'utilisation d'un système d'exploitation en temps réel dans votre conception garantira que votre dispositif pourra effectuer sa fonction dans le temps spécifié. 

## Les ventilateurs sont des systèmes critiques pour la sécurité

Dans la section précédente, nous avons discuté des systèmes d'exploitation en temps réel. Je pense que nous devrions élargir notre discussion et parler des systèmes en temps réel stricts par rapport aux systèmes en temps réel souples. 

Dans les systèmes en temps réel stricts, l'exigence d'opération est qu'elle DOIT se produire dans le temps spécifié à tout prix, et l'échec de respecter les délais n'est pas acceptable. Les systèmes de contrôle du trafic aérien et les systèmes de ventilateurs entrent dans cette catégorie. 

Les systèmes en temps réel stricts ne sont pas autorisés à manquer des délais.

Dans les systèmes en temps réel souples, il est préférable que les délais soient respectés. Mais si les délais ne sont pas toujours respectés, cela signifie que cela peut contrarier l'utilisateur final mais peut être acceptable. Pensez à une plateforme de jeu en ligne. Nous aimerions avoir une réponse en temps réel de nos jeux, mais si vous manquez quelques images, cela n'entraînera pas de perte de vie.

Les systèmes en temps réel souples sont autorisés à manquer des délais.

Maintenant, beaucoup de gens confondent un système en temps réel avec un système critique pour la sécurité. Tous les systèmes en temps réel ne sont pas des systèmes critiques pour la sécurité. Pensez à l'exemple ci-dessus avec le jeu en ligne ou la visioconférence – de tels systèmes nécessitent des performances en temps réel mais ils ne sont pas critiques pour la sécurité par nature.

Ce qui distingue un système critique pour la sécurité (SCS) d'un système en temps réel ordinaire, c'est que l'échec de respecter un délai dans un système critique pour la sécurité entraînera la mort ou une perte grave de biens.

Dans un système critique pour la sécurité, l'arrêt du système n'est PAS une option.

Par exemple, un système en temps réel à haute disponibilité peut être spécifié comme ayant un temps de fonctionnement d'environ 99 % sur une période de 24 heures. 

Pensez à un système de ventilateur. 

Quelle partie des 1 % de la journée est-il acceptable que le ventilateur ne soit pas opérationnel ? Puisque nous avons 1440 minutes dans une journée, quelles 14,4 minutes de la journée le patient ne devrait-il pas être autorisé à respirer ?

## La plateforme Arduino 

À ce stade de notre discussion, je pense qu'il est préférable de parler de la plateforme Arduino pour une utilisation dans les systèmes critiques pour la sécurité.

Dans notre discussion sur les systèmes embarqués, nous avons parlé du matériel et du logiciel, mais saviez-vous qu'il existe également un composant d'outils de développement dans le processus de conception ?

Vous voyez, afin de mettre le logiciel que vous avez écrit dans le dispositif microcontrôleur exécutant le matériel, vous devez utiliser des outils de développement tels qu'un IDE et une chaîne d'outils pour programmer le dispositif.

La configuration et l'utilisation d'une chaîne d'outils étaient un processus douloureux selon le dispositif que vous utilisiez. De nombreux fournisseurs de microcontrôleurs fournissaient des IDE encombrants que vous deviez être un concepteur embarqué expérimenté pour utiliser (bien que cela ait changé ces dernières années).

De plus, vous aviez également besoin de connaissances sur le matériel sous-jacent, et la configuration des registres et des horloges peut être intimidante même pour les concepteurs expérimentés. 

Même si vous surmontiez ces obstacles du côté logiciel, vous deviez avoir une carte de circuit imprimé (PCB) ou avoir de l'expérience dans l'utilisation d'une plaque d'essai pour faire fonctionner votre microcontrôleur. 

Si vous ne saviez pas comment connecter correctement votre matériel, même si votre programme était correct, le dispositif ne fonctionnerait pas et le dépannage du matériel nécessitait également une certaine expérience. 

Afin de résoudre le problème, la plateforme Arduino a été introduite comme un moyen de fournir une synergie entre le matériel, le logiciel et les outils de développement pour permettre aux étudiants de contrôler le matériel avec facilité. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-4.png)
_Les composants de la plateforme Arduino_

L'Arduino fournit une carte physique avec la puce qui est dans une configuration connue pour fonctionner ainsi qu'un IDE simple avec des tonnes de bibliothèques. Cette intégration transparente rend l'aventure moins intimidante pour les débutants qui cherchent à entrer dans le domaine de la conception matérielle. 

## Le problème de l'utilisation d'Arduino dans les systèmes critiques pour la sécurité

Il y a un problème : puisque l'Arduino est si facile à utiliser, cela a conduit de nombreuses personnes à utiliser l'Arduino bien au-delà de ce pour quoi la plateforme était initialement prévue, y compris l'utilisation dans des systèmes en temps réel.

Il n'est pas recommandé d'utiliser l'Arduino pour les systèmes en temps réel. Pourquoi ? Certaines personnes peuvent soutenir que vous pouvez utiliser un système d'exploitation tel qu'Amazon FreeRTOS sur l'Arduino et le rendre en temps réel. C'est vrai. Mais bien que la plateforme devienne en temps réel et qu'elle soit très fiable, elle ne la rendra pas critique pour la sécurité. 

Qu'est-ce qui rend l'Arduino inadapté à une utilisation dans les systèmes critiques pour la sécurité ? La réponse réside dans l'abstraction et sa relation avec la capacité de test et de débogage de la plateforme.

L'Arduino est une bonne plateforme pour l'apprentissage, et à ce titre, il ajoute beaucoup d'abstraction logicielle pour faciliter les choses. 

L'abstraction en soi n'est pas nécessairement une mauvaise chose. L'abstraction permet la réutilisation du code et peut aider à éliminer les bugs si elle est utilisée correctement. Un code correctement testé qui abstrait une grande partie du matériel peut être un outil puissant entre de bonnes mains.

Cependant, l'abstraction n'élimine PAS les bugs et c'est là le problème. Même si le code est abstrait, s'il avait une logique défectueuse dès le départ, alors l'abstraction ne vous sauvera pas. 

Si vous trouvez un bug, généralement vous compteriez sur un débogueur et des tests logiciels pour vous aider à trouver la source et améliorer la fiabilité du système. 

Là réside le problème. La plateforme Arduino n'a pas de capacité de débogage. 

Ne pas avoir de débogage rend les bugs difficiles à suivre. Avoir un logiciel sans bug est crucial dans une conception critique pour la sécurité. De plus, l'exécution de tests sur votre code n'est pas facile car l'IDE est trop simple pour le débogage et les tests puissants nécessaires à la conception de systèmes critiques pour la sécurité. 

Si vous n'avez pas le choix, vous pouvez utiliser l'Arduino pour la conception d'un système de ventilateur. Mais le manque de débogage rend difficile de le faire et augmente la probabilité de bugs dans votre firmware, et augmente le risque de défaillance dans le système. 

## Comment puis-je concevoir un bon système de fortune ?

Si vous devez concevoir un système de ventilateur, il y a deux choses spécifiques que vous pouvez faire pour améliorer votre conception basée sur l'Arduino : vous pouvez améliorer la conception logicielle et améliorer la conception matérielle.

### Améliorer la conception du côté logiciel

Tout espoir n'est pas perdu. Pour vous assurer que votre système dispose d'un logiciel fiable, envisagez de faire ce qui suit :

1. Envisagez d'utiliser un autre IDE - Atmel Studio est un excellent IDE qui offre l'option de débogage si vous utilisez un débogueur externe tel que le débogueur Atmel ICE ou ICD 4. De plus, MPLAB X peut être utilisé. Ces IDE vous aideront avec le débogage.
2. Respectez une norme de codage C/C++ - L'utilisation d'une norme de codage peut améliorer la fiabilité de votre système et rendre votre conception de système plus efficace. Envisagez de réécrire les bibliothèques que vous utilisez pour respecter MISRA, JSF++ ou même la norme de codage C embarqué du Barr Group.
3. Utilisez un RTOS - De nombreuses conceptions de ventilateurs basées sur l'Arduino utilisent la plateforme telle quelle avec un système d'exécution cyclique en place. Envisagez d'utiliser Amazon FreeRTOS pour rendre votre système en temps réel. Cela éviterait le blocage du système et rendrait votre système plus fiable.
4. Envisagez d'utiliser une plateforme avec des bibliothèques qui répondent aux exigences de sécurité - Bien que ce ne soit pas idéal pour les concepteurs inexpérimentés, l'utilisation d'un dispositif qui possède des bibliothèques répondant déjà aux exigences de sécurité existantes aidera à rendre votre conception plus robuste. 
Par exemple, même si notre dispositif est un dispositif médical de fortune, l'utilisation des exigences IEC 60730 pour la sécurité de classe B peut aider à rendre votre conception plus robuste. Microchip Technology (la société qui fabrique la puce qui alimente l'Arduino) dispose d'autres dispositifs qui ont des bibliothèques répondant aux exigences de sécurité de classe B et qui aideraient à améliorer la sécurité des dispositifs. 
5. Mettez en œuvre la redondance analytique des données des capteurs - Lors de la conception de votre dispositif, envisagez d'utiliser des capteurs pour garantir que le dispositif est toujours opérationnel et, lorsque vous le faites, envisagez d'utiliser des méthodes de redondance analytique pour aider à obtenir des données de capteurs plus précises. 
6. Envisagez d'utiliser SAFERTOS - Bien que cela puisse nécessiter de changer de système, SAFERTOS est pré-certifié pour une utilisation dans les systèmes médicaux et offrira un niveau de sécurité plus élevé que le logiciel de la plateforme Arduino. 

### Améliorer la conception du côté matériel

Pour améliorer votre conception du côté matériel :

1. Envisagez d'utiliser un Watch Dog Timer - Si vous n'avez pas le temps d'utiliser un RTOS, un moyen simple de garantir que votre dispositif continue de fonctionner est d'utiliser un watchdog timer dans votre conception. Le watchdog timer garantit que le dispositif se réinitialise si un problème survient lors de l'exécution de votre code. 
2. Utilisez un dispositif matériel avec des certifications de sécurité préexistantes et des bibliothèques - Certains dispositifs sont mieux adaptés à la tâche de conception d'un ventilateur. Plutôt que de confier une conception critique pour la sécurité à un Arduino, envisagez d'utiliser un dispositif de contrôle qui peut utiliser un logiciel déjà certifié pour une utilisation dans les dispositifs médicaux ou qui fournit des bibliothèques de sécurité. 
La plateforme prise en charge par SAFERTOS est un bon point de départ. La page web de Microchip Technology sur les logiciels de sécurité de classe B est également un bon point de départ. 
3. Ajoutez des systèmes de feedback - Il ne suffit pas que votre dispositif soit en marche et fonctionne. Vous avez également besoin de systèmes de feedback pour garantir que les dispositifs fonctionnent comme ils le devraient. Intégrez des capteurs pour fournir un feedback sur les pièces mécaniques sujettes à la défaillance. 
4. Envisagez un contrôle matériel distribué - Bien que de nombreuses personnes basent leurs conceptions sur une seule puce, envisagez d'utiliser plusieurs microcontrôleurs dans votre conception. Envisagez d'avoir un dispositif pour le contrôle et un autre pour notifier l'utilisateur final si un composant est en train de tomber en panne. 
5. Mettez en œuvre la redondance du système - Avoir un système d'arrêt approprié avec un système de transfert approprié est crucial pour de telles conceptions. Mettez en œuvre une procédure d'arrêt appropriée en cas de défaillance du système ainsi qu'un mécanisme de basculement approprié pour garantir un temps de fonctionnement de 100 % sur votre système. 

## Conclusion

Dans cet article, nous avons examiné les systèmes embarqués, brièvement parlé de leurs composants matériels et logiciels, et abordé les paradigmes de conception de firmware. Nous avons également parlé des systèmes en temps réel et des systèmes critiques pour la sécurité en relation avec la conception de ventilateurs. 

Enfin, nous avons parlé de la manière d'améliorer la sécurité et la fiabilité de vos conceptions de ventilateurs basées sur Arduino en améliorant la conception matérielle et logicielle. 

À la fin de cet article, vous devriez avoir une certaine compréhension de la manière d'améliorer votre système de ventilateur Arduino de fortune. 

Si vous souhaitez en savoir plus sur les microcontrôleurs, procurez-vous mon livre "Programming PIC Microcontrollers with XC8" où vous apprendrez à connaître le microcontrôleur PIC et à le programmer. Ce microcontrôleur peut également être utilisé pour concevoir vos ventilateurs et vous donnera un plus grand degré de contrôle et de capacité de débogage que la plateforme Arduino.

Lisez le livre ici :

[https://www.apress.com/gp/book/9781484232729](https://www.apress.com/gp/book/9781484232729)