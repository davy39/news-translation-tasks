---
title: Comment les Multi-User Dungeons m'ont appris à programmer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-31T22:20:03.000Z'
originalURL: https://freecodecamp.org/news/how-i-learned-to-program-f196a5a8bfd3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DeiKjabeUsFcTYtUfH-SlQ.jpeg
tags:
- name: Game Development
  slug: game-development
- name: Games
  slug: games
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment les Multi-User Dungeons m'ont appris à programmer
seo_desc: 'By Carl Tashian

  “Mom, what do you want me to write? Just tell me and I’ll write a program for you.”
  That was me at 9, urgently tugging at my mom’s pant leg.

  I don’t remember what, if anything, I ended up writing in BASIC on our Timex Sinclair
  compute...'
---

Par Carl Tashian

« Maman, quoi veux-tu que j'écrive ? Dis-le-moi et j'écrirai un programme pour toi. » C'était moi à 9 ans, tirant urgemment sur la jambe du pantalon de ma mère.

Je ne me souviens pas de ce que j'ai écrit, si j'ai écrit quelque chose, en BASIC sur notre ordinateur Timex Sinclair, mais je me souviens d'avoir voulu être pris au sérieux — vouloir créer quelque chose qui serait utile à quelqu'un. Je pense que mon père a acheté cet ordinateur sur un coup de tête dans un catalogue de vente par correspondance, ce qui était surprenant car il n'est pas vraiment un amateur de gadgets. Nous l'avons branché à un vieux téléviseur portable noir et blanc de 8" que nous avions. Ma mère a écrit un programme qui affichait mon nom à l'écran en boucle infinie.

![Image](https://cdn-media-1.freecodecamp.org/images/FUMfOXgXiLpnrh5wnZA2IU2CzU85iECs5kZb)

L'ordinateur m'appelait. Mon frère et moi avons écrit quelques choses en BASIC sur cet ordinateur, et nous avons même pu charger et sauvegarder nos programmes en utilisant un lecteur de cassettes branché à la prise audio de l'ordinateur. Nous avons essayé de jouer la cassette logicielle sur un lecteur de cassettes normal et cela ressemblait à des cigales stridentes.

Ce n'est que plus tard, à 14 ans, que je me suis vraiment passionné pour la programmation. Je suis devenu accro à un jeu d'aventure en ligne — un Multi-User Dungeon (MUD) gratuit appelé HexOnyx. Hex était un monde virtuel populaire avec au moins une centaine de personnes jouant à tout moment. Bien que les MMPORG d'aujourd'hui accueillent des millions de joueurs à la fois, à l'époque, quelques centaines de personnes dans un seul espace virtuel semblaient nombreuses. J'y ai fait de grands amis, et chaque nuit nous combattions ensemble des wargs vicieux et des Démons de Décadence dans les donjons et les forêts sombres. Le jeu était entièrement basé sur du texte, donc l'imagination était obligatoire. Près de 20 ans plus tard, j'ai encore des images dans ma tête de certains des vieux terrains de jeu.

Chaque jour après l'école était une nouvelle aventure dans le MUD, jusqu'à ce que la cloche du dîner familial me ramène dans le monde physique. « J'arrive tout de suite ! » criais-je, pour finalement me glisser dans la salle à manger beaucoup plus tard, en plein milieu du repas. Il n'y a jamais de point d'arrêt facile lorsque vous faites face à une bête lamia à quatre pattes qui veut votre tête pour son prochain repas.

Pendant des mois, mes amis en ligne et moi avons combattu ces créatures générées par ordinateur de manière obsessionnelle. J'ai finalement fait progresser mon personnage jusqu'au point d'immortalité, ce qui est le point final effectif du jeu.* Les immortels ne peuvent plus combattre — leur rôle était d'aider les nouveaux joueurs, de résoudre les disputes, de signaler les bugs, et ainsi de suite.

En me liant d'amitié avec les administrateurs et les développeurs de Hex, j'ai commencé à examiner la conception du MUD, essayant de comprendre comment il pouvait déclencher une expérience aussi profondément immersive, et me demandant comment nous pourrions l'améliorer encore.

Il y avait des centaines de MUDs à l'époque, et chacun essayait de se différencier. Pour différencier Hex, les développeurs avaient créé un constructeur de monde personnalisé, intégré au jeu. Là où d'autres MUDs devaient éditer un fichier texte plat avec un format propriétaire confus, le constructeur intégré rendait l'écriture de mondes agréable et permettait aux joueurs de s'impliquer facilement. Yaz, le gardien de Hex, avait ceci à dire :

> « L'objectif du jeu de notre point de vue à l'époque était de créer un environnement qui pouvait être maintenu depuis l'intérieur du monde. c'est-à-dire : personne n'aurait vraiment besoin de faire fonctionner le jeu depuis l'extérieur. Nous nous en sommes approchés avec le constructeur de monde. »

Avec le constructeur de monde, vous pouviez écrire une nouvelle porte et une nouvelle pièce dans le jeu, puis traverser la porte dans la pièce et voir comment cela se sentait. Cela a déclenché un boom de développement, avec de nombreux nouveaux mondes en construction, attendant d'être terminés et connectés à la carte principale du jeu. Ces mondes inachevés étaient des endroits étranges accessibles uniquement aux administrateurs et remplis de monstres assoiffés de sang qui erraient seuls jour et nuit.

Je n'avais aucun intérêt à construire des mondes ; même avec le constructeur de monde, cela semblait être trop de travail. Au lieu de cela, je voulais comprendre les mécanismes du logiciel et apporter des changements structurels.

Contrairement aux MMPORG modernes, la plupart des MUDs, y compris HexOnyx, étaient effectivement open source. J'ai téléchargé l'ancêtre de HexOnyx, [CircleMUD](http://www.circlemud.org/), écrit par Jeremy Elson, et je l'ai exécuté sur mon ordinateur personnel. J'avais programmé quelques choses en BASIC auparavant, mais CircleMUD était écrit en C — un tout nouveau monde pour moi. Juste le faire compiler était un projet. Mais progressivement, j'ai compris comment apporter de petites modifications, et c'était passionnant de `make` le MUD et de voir l'impact de mes changements localement.

Typiquement, les concepts de CS sont enseignés dans des scénarios d'affaires artificiels et ennuyeux : Clients, Commandes, Produits, Enseignants, Cours, etc. Mais CircleMUD était un logiciel réel, fonctionnel et assez complexe qui vivait dans le contexte d'un grand monde mythique. J'apprenais les fondamentaux de l'informatique par l'exemple, en modifiant des fonctions comme celle-ci :

```
/* * Fonction : find_guard * * Retourne le pointeur vers un garde en service. * Utilisé par Peter, le Capitaine de la Garde Royale */struct char_data *find_guard(struct char_data *chAtChar){  struct char_data *ch;  for (ch = world[IN_ROOM(chAtChar)].people; ch; ch = ch->next_in_room)    if (!FIGHTING(ch) && member_of_royal_guard(ch))      return (ch);  return (NULL);}
```

Dans une seule fonction courte, nous avons des boucles, des conditionnelles, des pointeurs, une liste chaînée, un tableau, des macros de préprocesseur et des structs. Et nous avons Peter, le Capitaine de la Garde Royale.

Selon les normes d'aujourd'hui, certaines parties du code de Circle seraient jugées malodorantes et inelegantes. Il n'avait pas de tests, car les tests logiciels orientés prévention n'avaient pas encore pris leur essor. Mais pour moi, Circle était assez beau. C'était un exemple de quelque chose de plus grand que ce que j'avais jamais écrit ou même conçu d'écrire auparavant. Lui-même un fork du projet MUD DikuMUD, écrit en 1990 par quelques personnes à l'Université de Copenhague, Circle avait l'attrait rugueux d'un grand programme C : il interagissait intimement avec les appels système de l'OS, il était hautement optimisé et piloté par événements, et il faisait beaucoup de travail lourd qui est aujourd'hui caché dans des bibliothèques. Il gérait ses propres sockets TCP et ses propres tampons d'E/S à partir de zéro, définissait ses propres formats de fichiers de jeu, et ainsi de suite.

Ce qui serait considéré comme du bare metal aujourd'hui était, à l'époque, le sommet de la pile. Les créateurs de Circle ne se plaignaient pas du manque de typage dynamique ou d'autres luxes de haut niveau — ils se réjouissaient des commodités de voler au-dessus du langage d'assemblage et de s'appuyer sur le système d'exploitation pour toutes sortes de tâches importantes.

En conséquence, Circle est un bourreau de travail, et en production, Hex pouvait fonctionner en douceur avec 200+ utilisateurs simultanés en moins de 20 Mo de RAM sur un 486. Le jeu fonctionne dans une grande boucle d'événements de 100 ms qui ne bloque jamais ; il sert simplement tous les utilisateurs actuellement connectés, fait avancer le monde d'un tick, puis dort pour le reste du cycle. Je me souviens avoir fait quelque chose de long dans cette boucle et avoir appris à mes dépens que cela arrête le jeu pour tout le monde. Une leçon précoce en optimisation.

Après des semaines à étudier le code, et après beaucoup d'essais et d'erreurs, j'ai été ravi d'envoyer un petit patch qui changeait le style de l'invite de commande dans le jeu. Dans une demande de tirage de style milieu des années 90, j'ai envoyé un e-mail aux administrateurs de Hex avec mon patch et j'ai attendu avec impatience une réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/XfauirSYQh7enzRERxIzqK14oGRE7ppRHbWB)
_L'art ASCII d'introduction pour HexOnyx_

Ils ont accepté mon patch. Ils l'ont appliqué. Et ce fut magique de voir mon petit changement incorporé dans un jeu que tant de gens jouaient chaque jour. Les développeurs — pour la plupart des étudiants en informatique d'âge universitaire — m'ont donné des commentaires sur mon patch, tout comme les joueurs.

J'ai continué à travailler et j'ai envoyé plus de petits patches. Finalement, Yaz s'est lassé de jouer l'intermédiaire et a dit : « Pourquoi ne fais-tu pas des modifications directement dans notre code ? » et il a créé un compte sur le serveur pour moi.

Le statut d'implémenteur sur Hex était de loin la responsabilité la plus personnelle que j'avais jamais ressentie. J'ai commencé à publier de nouveaux changements presque toutes les nuits, recevant des commentaires immédiats d'autres joueurs. Non seulement je concevais et construisais des fonctionnalités que je voulais voir dans le jeu en tant que joueur vétéran — plus important encore, j'itérais à l'intérieur d'une boucle de commentaires serrée avec d'autres utilisateurs.

La boucle de commentaires a motivé mon travail. Elle m'a maintenu en mouvement, à travers des bugs qui semblaient impossibles à corriger et des problèmes qui semblaient insurmontables. Il n'y avait pas de calendrier — juste de petites étapes sans fin chaque jour vers un meilleur jeu. J'étais accro à la profonde satisfaction qui venait avec l'amélioration de quelque chose que les gens aimaient utiliser, et j'avais atteint un état de flux incroyable.

Je pense que c'est une excellente façon d'apprendre la programmation : plutôt que de dire « Je veux apprendre à programmer », commencez par un désir d'améliorer quelque chose qui existe déjà. Quelque chose que les gens utilisent. Attendez-vous à rencontrer des obstacles et des défis, et laissez les commentaires des utilisateurs et des collaborateurs être votre encouragement à persévérer à travers ceux-ci. De nombreux projets open source offrent cette opportunité, mais je pense qu'il y a quelque chose de spécial dans l'environnement de jeu.

Au cours des mois suivants, j'ai appris les structures de données et l'allocation de mémoire. J'ai appris des façons saines de structurer le logiciel procédural. J'ai appris les sockets, la sérialisation des données (avant que JSON ou même XML n'existent), les temporisateurs et les interruptions. Je ne connaissais pas le vocabulaire pour ces choses au-delà de ce que je pouvais lire dans les commentaires du code et dans les pages de manuel pour les appels système. Mais j'étais accro. Coder pour le MUD était tout ce à quoi je pensais à l'école chaque jour, et tout ce que je faisais à la maison chaque nuit.

J'ai ajouté une multitude de nouvelles fonctionnalités au cours de l'année ou des deux années suivantes. J'ai étendu l'économie interne des MUDs, construisant un système de logement (en fait des casiers de stockage virtuels) et un marché immobilier pour ceux-ci. J'ai introduit la rareté des biens dans l'économie du jeu, écrivant un algorithme qui limitait le taux auquel le meilleur équipement serait introduit dans le monde. J'ai agi en tant que main invisible, rendant le jeu plus amusant et plus stimulant pour les gens, et c'était génial.

Le plaisir d'être un développeur m'a poussé à en apprendre davantage et à m'efforcer de construire plus de choses que les gens voulaient. Je suis ingénieur aujourd'hui grâce à cette expérience. Je suis reconnaissant que CircleMUD était un code open source malléable, et que Yaz ait fait un saut de foi en me confiant les clés à seulement 14 ans.

J'aime un médium où vous pouvez vous approcher en tant que consommateur et passer en douceur à un producteur. Aujourd'hui, Minecraft permet certaines modifications dans un environnement simple et contraint et pourrait être une bonne porte d'entrée pour les programmeurs en herbe. Mais l'art de la programmation a encore un long chemin à parcourir avant de pouvoir être universellement accessible. Les jeux multijoueurs les plus populaires d'aujourd'hui sont largement immuables pour les joueurs. Parce que les jeux populaires comme WoW ne sont pas open source, il semble plus difficile de devenir un contributeur principal sur un système réel, vivant et respirant.

J'aimerais que la prochaine génération de programmeurs s'amuse autant à apprendre à programmer que moi. Changer le jeu est beaucoup plus intéressant que de le jouer.

_Publié à l'origine sur mon site web personnel. Merci à Siobhán K Cronin pour la relecture._

#### Si vous êtes arrivé jusqu'ici, vous devriez [rejoindre ma liste de diffusion](http://tashian.com/superstack) sur la technologie et l'humanité.