---
title: Programmation pour Débutants - Comment Coder avec Python et C#
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-23T13:24:09.000Z'
originalURL: https://freecodecamp.org/news/programming-for-beginners-how-to-code-with-python-and-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/jabrils.png
tags:
- name: programing
  slug: programing
- name: youtube
  slug: youtube
seo_title: Programmation pour Débutants - Comment Coder avec Python et C#
seo_desc: "When it comes to learning how to write computer programs, it can be hard\
  \ to figure out where to start. \nWell, look no further.\nWe just released a full\
  \ course that teaches basic programming skills in both Python and C#. This course\
  \ is for absolute beg..."
---

Lorsque l'on apprend à écrire des programmes informatiques, il peut être difficile de savoir par où commencer.

Eh bien, ne cherchez plus.

Nous venons de publier un cours complet qui enseigne les compétences de base en programmation en Python et en C#. Ce cours est destiné aux débutants absolus.

L'une des meilleures choses à propos de ce cours est qu'il est enseigné par Jabrils. Il est l'un des YouTubeurs tech les plus divertissants. Il apporte ses solides compétences techniques et son style amusant à ce cours de programmation pour débutants.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/one-jabrils--1-.gif)

Voici les sujets que vous allez apprendre dans ce cours :

* Qu'est-ce qu'un IDE ?
* Installation de votre premier IDE (Windows)
* Les différences entre C# et Python
* Codez votre premier programme !
* Quels sont les types de données ?
* Qu'est-ce qu'un Bool ?
* Qu'est-ce qu'une chaîne de caractères ?
* Qu'est-ce qu'un caractère ?
* Qu'est-ce qu'un nombre à virgule flottante ?
* Qu'est-ce qu'un tableau ?
* Qu'est-ce qu'une variable ?
* Qu'est-ce qu'une instruction If ?
* Qu'est-ce qu'une instruction Else ?
* Qu'est-ce qu'une instruction Else If ?
* Qu'est-ce qu'une boucle For ?
* Qu'est-ce qu'une boucle While ?
* Qu'est-ce qu'une méthode ?
* Qu'est-ce qu'une fonction ?
* Comment commenter votre code !
* Vous pouvez coder tout ce que vous pouvez imaginer !

Regardez le cours complet ci-dessous ou sur la [chaîne YouTube de freeCodeCamp.org](https://youtu.be/__izua1kKeI) (5 heures de visionnage).

%[https://www.youtube.com/watch?v=__izua1kKeI&rel=0]

## Transcription

(autogénérée)

Si vous connaissez Jabrils, vous savez qu'il est l'un des créateurs tech les plus divertissants.

YouTube, l'entreprise, lui a demandé de créer un cours de programmation complet.

Et nous sommes fiers de pouvoir publier l'intégralité du cours en une seule vidéo sur la chaîne freeCodeCamp.

Yo les gars, toute ma vie, on m'a dit que la programmation était difficile.

C'est seulement pour les intellos.

Cela demande tellement de maths, vos notes ne sont pas assez bonnes.

Mais après avoir programmé pendant 13 ans, je peux confirmer que toutes ces hypothèses sont fausses.

Et c'est pourquoi, lorsque YouTube m'a récemment approché avec l'opportunité de créer un cours de programmation de niveau débutant, j'ai su que c'était mon opportunité d'essayer de corriger certaines idées fausses qui, je suis sûr, empêchent encore des gens ordinaires comme vous de plonger dans le monde merveilleux de la programmation.

Mais d'abord, nous devons en finir avec ce champ médical à haut salaire.

Alors, vous voulez apprendre à coder.

Je veux dire, je ne vous en blâme pas, l'informatique est la deuxième majeure la plus précieuse à apprendre.

Maintenant, bien sûr, vous pourriez simplement aller à votre école et apprendre à programmer ou vous pourriez simplement apprendre à programmer auprès d'un idiot comme moi qui n'a pas de formation scolaire traditionnelle.

Jouer.

Attendez, attendez avant de cliquer hors de cette vidéo et de vous inscrire à un cours à votre université locale.

Laissez-moi au moins essayer de gagner votre cœur avec une petite histoire rapide.

Tout a commencé quand j'avais environ neuf ans, mon ami m'a invité à jouer à ce nouveau jeu dont je n'avais jamais entendu parler.

Oui, mec.

C'est fou.

Vous pouvez jouer à Donkey Kong si vous voulez et combattre contre Link Mario Pikachu.

Et en effet, il parlait de l'original sur le Nintendo 64.

Et comme, j'avais toujours joué à des jeux vidéo.

Mais il y avait quelque chose dans ce jeu qui, à partir de ce jour, m'a rendu obsédé par les jeux vidéo.

Je me souviens quand ma famille a déménagé de Virginie en Californie en 2000, tout le trajet à travers les États-Unis, je concevais mes propres niveaux de Smash Bros en utilisant un peu de Paint dans Notepad, et quand Noël est arrivé, j'ai demandé à ma mère une Nintendo 64 avec Super Smash Brothers et j'ai joué à ce jeu pendant d'innombrables heures, absolument captivé par le concept de tout cela, j'ai rassemblé des mascottes internes toutes ensemble pour qu'elles s'affrontent dans un jeu vidéo en trois dimensions.

Comment quelque chose comme cela est-il même possible ? Cette expérience entière est ce qui m'a intéressé à vouloir comprendre comment fonctionnent les jeux vidéo, non, pas pour apprendre à programmer parce que j'étais encore à cet âge où j'apprenais encore à lire, écrire et faire des maths de base.

Encore une fois, cela m'a intéressé à vouloir apprendre comment fonctionnent les jeux.

Et souvenez-vous de cela, car cela deviendra important plus tard.

Ce n'est pas longtemps après cela que j'ai découvert un petit site web appelé newgrounds.com.

Un endroit où des gens comme moi faisaient des jeux simples à petit budget et des films interactifs.

Et je crois vraiment que c'est l'expérience qui a planté la graine dans ma tête que faire des jeux vidéo comme ceux que j'aime jouer était en fait possible pour quelqu'un comme moi.

Alors un peu plus tard dans la vie, quand j'ai découvert quelque chose appelé Game Maker, qui se présente comme vous pouvez commencer à faire des jeux aujourd'hui, aucun code requis.

Et après des semaines de suppliques à ma mère pour qu'elle l'achète pour moi, elle l'a finalement fait.

Et mec, c'était un moment si amusant dans ma vie.

Je n'avais absolument aucune idée de ce que je faisais.

Mais simplement faire de mon mieux pour créer des déclarations logiques qui feront faire à un ordinateur ce que je veux faire était suffisant pour m'accrocher.

Ressentir cette sensation d'être vraiment fatigué pour la première fois.

Parce que je suis resté éveillé toute la nuit en essayant de comprendre comment créer un système d'inventaire est quelque chose que je n'oublierai jamais.

À partir de ce jour.

Je continue à apprendre autant que je peux, demandant de l'aide à tous ceux qui sont prêts à m'aider, apprenant de plus en plus non pas sur la programmation, mais sur le fonctionnement des jeux.

Parce que vous voyez, comprendre comment fonctionnent les jeux est ce qui m'a initialement attiré vers la programmation.

Et sans même le savoir.

C'est ce à quoi je revenais toujours lorsque les temps devenaient difficiles pendant mes aventures de codage.

Et donc la morale de l'histoire est, je sais ce que c'est que d'avoir une envie extrême d'apprendre ces trucs tout en n'étant pas exactement sûr de par où commencer.

Donc je sais exactement ce qui vous manque et comment vous amener de ce côté de la clôture.

Et heureusement, j'ai appris à faire toutes ces choses sans scolarité traditionnelle, ce qui signifie que vous et moi, nous parlons la même langue.

Maintenant, si cette histoire n'a pas gagné votre cœur, vous n'en avez probablement pas.

Non, je plaisante.

Je plaisante.

Mais je suis sûr que cela le fera.

Voici mon ami Zargar, un programmeur hautement intelligent qui, sans blague, a programmé des systèmes stellaires entiers en solo en utilisant uniquement une calculatrice TI 80.

Et quand j'ai dit à Zargar que j'allais créer votre cours de programmation, il n'a pas arrêté de parler de vouloir l'enseigner pour moi.

Maintenant, Zargar est un quintillion de fois plus intelligent que moi.

Mais pourquoi ne voulez-vous pas que Zoglair enseigne ce cours ? Eh bien, regardez cela, Zargar, qu'est-ce qu'un tableau ? Eh bien, vous voyez, nous avons besoin d'un peu de contexte, car traditionnellement, la mémoire ne peut stocker des informations qu'à un débit de 32 bits, ce qui signifie que la profondeur de récursion appelée le pull up sur la loi de Moore a pris de l'ampleur en 1996, nous avons non seulement obtenu plus de puissance et de mémoires, d'accord, désolé, vous avez prouvé mon point.

Ce public n'a rien compris de ce doctorat en programmation qui me ralentit, il est temps de partir.

Et la prochaine fois, souvenez-vous, respirez.

Oh, mec.

Alors bienvenue dans mon cours.

Dans cette série, vous repartirez avec tout ce dont vous avez besoin pour commencer à programmer.

Oui, vous avez lu le titre, n'est-ce pas ? Ce n'est pas du clickbait.

En fait, à la fin de ce cours, vous écrivrez votre toute première application en utilisant tout ce que nous avons appris.

Mais si vous devez retenir quelque chose de ce cours, laissez-moi vous dire ceci.

Demandez-vous, pourquoi êtes-vous ici ? Qu'est-ce qui vous a poussé à vouloir apprendre tout ce dont vous avez besoin pour commencer à programmer ? Pour moi, c'était de comprendre comment fonctionnent les jeux, quelle que soit votre raison, je vous encourage à écrire cette raison dans la section des commentaires maintenant.

Et si à un moment donné tout au long de ce cours ou même n'importe où dans vos aventures de programmation, les choses deviennent difficiles, je veux que vous retourniez à ce commentaire et que vous soyez rappelé de la raison pour laquelle vous avez commencé.

Faites-moi confiance, vous avez ce qu'il faut, je vous promets, c'est beaucoup plus facile que vous ne le pensez.

Et je vais faire de mon mieux pour faciliter les choses pour vous dans ce cours.

Je vous verrai dans la prochaine partie.

Oui, c'est si serré de voir que vous avez cliqué sur cette vidéo et que vous êtes intéressé à apprendre quelques principes de programmation.

Eh bien, je vous dirai une chose, si vous voulez devenir programmeur, vous n'irez pas très loin sans cette chose.

Cela s'appelle un IDE.

Il existe de nombreux, nombreux, nombreux types d'IDE différents, certains provenant de grandes organisations que vous avez définitivement entendues comme Visual Studio de Microsoft, Xcode d'Apple et Android Studio de Google.

Mais il existe également des IDE provenant de diverses autres organisations.

Pie chart de JetBrains, Eclipse de Eclipse, sublime de quelques gars, Adam de GitHub, pour n'en nommer que quelques-uns.

Et comme vous l'avez probablement deviné, la leçon d'aujourd'hui est entièrement consacrée à l'IDE.

Hey, que signifie-t-il ? Duh, bien sûr, comment ai-je pu oublier de couvrir cela ? IDE signifie environnement de développement intégré.

Et comme le suggère le nom, c'est un environnement numérique utilisé pour développer des jeux, des logiciels, du matériel, à peu près tout ce qui concerne le code, qui offre une intégration ou un contrôle sur de nombreux aspects du développement, du débogage, ce qui signifie ajouter, supprimer ou modifier du code qui empêche votre programme de s'exécuter comme prévu, jusqu'à la compilation, ce qui signifie grossièrement prendre votre code et le transformer en quelque chose que les ordinateurs peuvent comprendre.

Certains IDE ne supportent qu'un seul langage, par exemple, IDL, qui est un IDE fourni avec le langage Python lorsque vous le téléchargez, et il ne supporte que Python, mais des IDE comme Xcode d'Apple supportent une multitude de langages différents comme C, c++, Java, Python, la liste est longue.

Mais comme vous le voyez, mon propos ici est qu'il existe de nombreuses options différentes lorsqu'il s'agit de choisir votre IDE.

Et honnêtement, cela peut être un peu intimidant.

Mais encore une fois, si vous voulez commencer à programmer, vous en avez besoin, plus tard, lorsque vous aurez plus d'expérience, vous pourrez utiliser Microsoft Word pour écrire vos programmes, si vous le souhaitez vraiment, mais je ne recommanderais pas cela, peu importe l'expérience que vous avez, vous allez perdre beaucoup de temps.

Et c'est ce qu'il est, un environnement numérique qui est une partie centrale de la programmation.

Où voulez-vous coder, des jeux, des logiciels, du matériel, vous l'appelez, et c'est votre meilleur ami pour vous aider à assurer votre succès.

Il est maintenant temps d'installer votre premier IDE.

Êtes-vous prêt ? Faisons-le.

Et attention.

Il existe de nombreux IDE différents.

Mais au lieu de vous guider à travers chaque IDE, ce qui serait une conférence très ennuyeuse à suivre, vous allez plutôt obtenir mon avis et je vais vous montrer comment installer mes deux IDE préférés : Microsoft Visual Studio, qui devrait vous intéresser si vous voulez vous lancer dans le développement Windows ou si vous voulez créer des jeux en utilisant un moteur populaire appelé Unity.

Et nous allons également installer Microsoft Visual Studio Code, qui devrait vous intéresser si vous êtes intéressé par la programmation générale ou la science des données, ainsi qu'une multitude d'autres tâches.

Et oui, ils ont tous les deux Microsoft Visual Studio dans leur nom.

Et oui, ce sont deux IDE séparés.

Maintenant, commençons.

D'accord, donc la première chose que vous allez vouloir faire est d'ouvrir votre navigateur.

Je vais utiliser Google Chrome comme navigateur.

Vous pouvez choisir ce que vous voulez, mais vous voulez rechercher Visual Studio dans la barre de recherche et ensuite cliquer sur téléchargements, vous verrez visual studio.microsoft.com, cliquez sur téléchargements et cela vous amènera directement à la page que vous voulez.

Donc, comme vous le voyez, nous avons ici Visual Studio 2019, l'édition communautaire, cliquons sur téléchargement gratuit.

Et puis vous avez également votre Visual Studio Code, attendez une seconde, vous verrez qu'il apparaît ici, vous informant qu'il est en cours de téléchargement.

Et puis je vais revenir en arrière et ensuite je vais cliquer sur Visual Studio Code, téléchargement gratuit, c'est le deuxième IDE dont nous avons besoin.

Et il apparaîtra ici, vous informant qu'il est en cours de téléchargement.

Et attendez simplement que cela se télécharge.

D'accord, une fois ceux-ci téléchargés, vous pouvez soit cliquer dessus depuis ici dans Google Chrome, si c'est ce que vous utilisez, et ils commenceront à s'installer.

Mais si vous n'avez pas Google Chrome, alors vous allez vouloir trouver votre dossier de téléchargements par défaut, dans la plupart des cas, il devrait s'agir de téléchargements dans Windows CE téléchargements.

Mais si ce n'est pas le cas, vous allez vouloir trouver cela afin de pouvoir installer les IDE.

Donc, d'abord, installons Visual Studio Code.

Je vais simplement double-cliquer dessus.

Et vous verrez que nous obtenons une fenêtre ici qui dit Bienvenue dans l'assistant de configuration de Windows Studio, assistant de configuration.

Et cette partie est vraiment facile.

C'est comme toute autre installation que vous avez déjà faite, vous cliquez simplement sur suivant et vous acceptez, lisez si vous voulez.

Cliquez sur suivant.

Et puis ici, vous voulez laisser cela à l'emplacement par défaut, qui est comme voir, quelque part quelque part Program Files, probablement.

Mais parce que je l'ai déjà installé sur mon système, je vais l'installer dans un emplacement très spécial, afin qu'il ne perturbe pas nos préréglages.

Donc oui, laissez cela comme cela, cliquez sur suivant, et puis cliquez simplement sur suivant.

Et ici, je vous recommande de cocher ouvrir avec le code et sur les deux.

Et assurez-vous également que ajouter le chemin est coché.

Et ce que ces deux options font ici, c'est qu'elles vous permettent, par exemple, si vous avez des scripts Python, et au lieu d'avoir à ouvrir d'abord Visual Studio Code, puis à cliquer sur fichier et ensuite sur ouvrir et à rechercher, vous pouvez simplement aller, par exemple, l'un de ceux-ci est un script Python, vous pouvez simplement faire un clic droit dessus.

Et ensuite vous aurez cela disponible ici où il est ouvert avec le code.

Donc il ouvrira simplement ce fichier directement dans Visual Studio Code, c'est très pratique.

Vous pouvez également faire cela avec des répertoires au cas où vous avez un fichier, désolé, vous avez un dossier avec beaucoup de scripts Python, vous pouvez simplement faire un clic droit quelque part dans le dossier, cliquer sur ouvrir avec le code.

Très, très utile, je recommande vraiment de cocher ces deux options, puis de cliquer simplement sur suivant.

Maintenant, je vais revenir en arrière et supprimer ceux-ci car encore une fois, je ne veux pas perturber mes préréglages.

Mais c'est ainsi que vos années devraient ressembler avec, bien sûr, cette destination suivante étant C C program files, peu importe.

Et puis après cela, cliquez simplement sur installer, installer, et puis vous pouvez voir qu'il va s'installer.

Donc je vais prendre quelques secondes, je vais prendre terriblement longtemps, et bada boom, le voilà, Visual Studio Code a officiellement été installé.

Nous allons cliquer sur terminer et lancer vinje Visual Studio Code.

Je vais amener cela Oups, mauvaise fenêtre.

Aller amener Visual Studio Code ici.

Voici à quoi cela ressemble.

Maintenant, avant de commencer, il y a quelques choses que vous voulez faire, vous voulez définitivement ajouter Python ici.

Donc cliquez sur Installer.

En fait, je vais vous montrer comment le faire traditionnellement, recherchez simplement Python et installez-le.

Cela vous permet d'utiliser Python avec Visual Studio Code.

Et il y a quelques options pour le faire.

Mais celle-ci provient directement de Microsoft.

Donc installez simplement la première qui s'appelle Python.

Et une autre extension dont nous aurons besoin s'appelle code runner, recherchez simplement code runner, ouvrez les extensions et téléchargez la première, cela nous permettra d'exécuter nos scripts Python dans Visual Studio Code sans avoir à quitter l'IDE.

C'est très bien.

D'accord, et le voilà, Visual Studio Code est installé.

Si vous voulez faire un nouveau fichier, allez simplement dans Fichier, nouveau fichier et bada boom.

Si vous voulez enregistrer une extension, utilisez simplement enregistrer le fichier n'importe où, nous allons simplement faire des documents, par exemple, et simplement faire comme mon fichier, je ne sais pas.et.pi vous obtiendrez un script Python, cliquez sur enregistrer.

Et maintenant, il est reconnu comme un script Python.

Et si vous obtenez cette fenêtre contextuelle ici qui nous dit que Python est installé.

Visual Studio Code est souvent très bon pour vous faire savoir ce dont vous avez besoin et ce dont vous n'avez pas besoin, mais vraiment Google vous le fera savoir.

Donc, cliquons sur télécharger ici dans une fenêtre contextuelle, nous allons vouloir télécharger python 3.7.

Et puis je vais simplement cliquer sur exécuter les probabilités, c'est enregistrer ouvrir le dossier ici.

Et je vais simplement double-cliquer dessus pour l'exécuter.

Ensuite, tout ce que vous avez à faire est de cliquer sur Ajouter Python 3.7 au chemin et puis simplement cliquer sur installer maintenant.

Et il va simplement s'installer maintenant.

Donnez un peu de temps et Python devrait être installé.

Et juste comme cela, la configuration a réussi.

Donc, de retour dans notre dossier de téléchargements.

Je vais simplement double-cliquer sur l'installateur de Visual Studio.

Et je ne suis pas sûr de ce que vous voyez en ce moment, mais il me demande de taper mon mot de passe.

Donc je vais faire cela.

Voyons voir, attendez.

Non, c'est un ancien code PIN, désolé.

D'accord, désolé, un noir là pendant une seconde.

Et puis nous avons l'installateur de Visual Studio, cliquez simplement sur Continuer.

Et il va commencer à télécharger et à installer des trucs, cela ne devrait pas prendre trop longtemps, puis vous devriez voir quelque chose comme cela apparaître.

Et ils vont vous donner quelques options, vous pouvez ignorer la plupart d'entre elles, peut-être revenir à elles plus tard lorsque vous aurez un peu plus d'expérience.

Mais tout ce dont vous avez vraiment besoin est celui-ci.

Développement de bureau .net, car ce que nous cherchons, ce sont les applications de console utilisant C sharp, donc cliquez simplement sur celui-ci.

Et puis vous cliquez simplement sur installer, et voyez installer sur les lecteurs système recommandés.

Encore une fois, je l'ai déjà installé.

Donc je vais placer cela dans un emplacement très spécial, mais placez définitivement cette installation sur votre lecteur système où il est recommandé.

Donc je vais cliquer sur OK.

Et vous obtenez cela qui apparaît, merci pour l'installation, prenez un sondage maintenant.

Et cela va commencer à s'installer, cela va probablement prendre un peu de temps.

Mais une fois que c'est fait, vous n'aurez pas grand-chose à craindre.

D'accord, et une fois qu'il est à 100%, donnez-lui une seconde.

Il va probablement démarrer automatiquement, car nous avions cela coché.

Et bada boom, maintenant vous avez bienvenue connectez tous vos services de développeur, services de développeur.

Cliquez simplement sur pas maintenant, peut-être plus tard, à un moment donné pour vous forcer à créer un compte de toute façon.

Donc pour l'instant, nous allons faire pas maintenant, démarrer Microsoft Visual Studio, préparer votre première utilisation.

Et nous y voilà.

Maintenant, si vous voulez créer un nouveau projet, vous cliquez simplement sur créer un nouveau projet.

Et puis il vous demandera quel type de projets vous voulez faire.

Nous allons simplement faire un simple projet de console en C sharp ici, et puis cliquer sur suivant.

Et vous pouvez le nommer, laissons-le simplement comme il est, concert projet un est bien.

Et créer une application de console, désolé.

Je ne sais pas comment lire.

Donnez-lui une seconde, et bada bing, il va démarrer et maintenant vous êtes officiellement dedans.

Et c'est à peu près tout ce que vous avez à faire pour C sharp.

Donc si vous êtes sur un programme en C sharp et/ou Python, il est important de comprendre leur syntaxe.

Mais d'abord, qu'est-ce que la syntaxe ? Eh bien, la syntaxe en relation avec la programmation, c'est à peu près un ensemble de règles qui doivent être suivies dans l'ordre d'opération que votre code doit respecter, un processus qui doit être respecté si vous voulez que votre programme s'exécute.

Et donc aujourd'hui, nous allons examiner la syntaxe de deux langages différents et voir les différences entre eux, car je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Et donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous faites du développement Windows ou si vous voulez créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Donc la première chose que nous examinons aujourd'hui est comment les deux langages utilisent les types de données.

Maintenant, les types de données en eux-mêmes sont inutiles, vous devez assigner un type de données à une variable.

Maintenant, pour commencer en C sharp à gauche, je vais simplement me débarrasser de ces deux lignes car je n'en ai plus besoin, elles viennent de série avec chaque nouveau projet.

Et puis nous allons utiliser un Booléen comme exemple aujourd'hui.

Maintenant, un Booléen est un type de données qui ne peut être que l'un des deux types.

C'est soit vrai, soit faux.

Donc initialisons un Booléen en C sharp.

Appelons-le do it.

Et puis nous allons lui assigner vrai.

Donc do it est égal à vrai.

Maintenant, c'est bien et tout, do it est un Booléen que nous avons assigné à être vrai.

Cependant, C sharp ne le reconnaîtra pas comme un Booléen à moins que vous ne définissiez son type de données.

Et en C sharp, vous définissez simplement le type de données en allant avant la variable, qui à nouveau, une variable doit faire do it avant, il suffit de taper le type de données.

Donc c'est bool, qui est l'abréviation de Booléen, bool do it est égal à vrai, donc votre erreur disparaît et tout est correct.

Et cette syntaxe très précise s'applique à chaque variable.

Par exemple, si vous voulez initialiser une variable de chaîne, vous devez la définir.

Donc je vais dire que c'est une chaîne.

Je vais l'appeler str, abréviation de chaîne, et puis je vais lui assigner bonjour.

Par exemple, vous devez faire cela pour chaque variable.

Cependant, il y a un petit piège.

Donc je vais simplement me débarrasser de cette ligne car je n'en ai plus besoin.

Vous n'avez à initialiser vos variables qu'à leur première utilisation.

Donc, par exemple, si je voulais changer la variable booléenne do it, je dois simplement venir ici.

Et je dois faire do it est égal à faux, par exemple, et c'est parce que nous sommes sur cette ligne ici.

Le programme sait quel est le type de données pour la variable do it, il sait que c'est un bool.

Donc je n'ai pas à le faire à nouveau.

En fait, si j'essaie de le faire à nouveau, vous verrez que j'obtiens une erreur, cette erreur me dit simplement que je ne peux pas créer la même variable deux fois, essentiellement.

Donc rappelez-vous, vous n'avez à initialiser qu'à la première utilisation.

Et cette convention s'applique à chaque type de données.

Donc c'est Booléen, chaînes, entiers, flottants, chaque type.

Maintenant, en Python, les choses sont beaucoup différentes.

Donc disons que nous voulons faire le même exemple, nous voulons toujours initialiser une variable booléenne ? Eh bien, en Python, tout ce que vous avez à faire est simplement écrire le nom d'une variable et ensuite assigner la valeur que vous voulez.

Donc dans ce cas, nous allons assigner vrai.

Et voilà, nous venons d'initialiser une variable booléenne.

C'est exact.

En Python, vous n'avez pas à définir vos variables, vous n'avez pas à définir le type de données que vous voulez que votre variable soit, comme vous le faites en C sharp.

Et cet avantage vient du fait que Python est ce qu'on appelle un langage interprété.

Et ce que cela signifie, c'est que tout ce que vous avez à faire est de créer une variable et ensuite lui assigner une valeur.

Et selon la valeur que vous assignez à votre variable, Python interprétera le type de données que cette variable devrait avoir.

Et avec cette syntaxe, elle permet beaucoup de flexibilité avec le langage Python.

C'est l'une des raisons pour lesquelles tant de gens aiment Python, car c'est un peu comme un bol d'air frais, en ce qui concerne les langages informatiques.

Et c'est l'une des raisons pour lesquelles beaucoup de développeurs qui s'intéressent à la science des données utilisent Python, car comme vous pouvez le voir, vous pouvez gagner beaucoup de temps en n'ayant pas à taper le type de données encore et encore pour vos variables.

Cependant, la flexibilité ne s'arrête pas là.

Je vais simplement imprimer ce que fait do it, comme ça, l'enregistrer, appuyer sur le bouton de lecture, et vous verrez que do it est égal à vrai, évidemment, c'est ce que vous attendiez.

Mais regardez ça.

Si nous voulons le réassigner à être faux.

Par exemple, nous venons ici et disons do it est égal à faux, enregistrer, appuyer sur le bouton de lecture, et nous avons une valeur fausse.

Mais c'est là que cela devient vraiment cool.

Actuellement, comme vous le comprenez, do it est une variable booléenne.

Mais nous pouvons faire do it est égal à 13037, par exemple.

Donc d'abord nous assignons vrai et ensuite nous changeons d'avis pour faux et ensuite nous changeons d'avis à nouveau, et nous l'assignons à 1337.

Quand j'appuie sur lecture, aucune erreur, il imprime simplement que c'est 1337.

La dernière chose que nous avons assignée, ce qui est une flexibilité folle par rapport à C sharp, nous ne pouvons tout simplement pas faire cela si nous voulons changer do it pour qu'il soit comme un entier, par exemple, nous allons simplement obtenir une erreur disant que vous ne pouvez pas convertir un entier en bool.

Une fois qu'une variable a son type de données, il ne peut pas être changé.

Et c'est probablement l'une des plus grandes différences entre C sharp et Python, le fait de savoir comment ils définissent leurs types de données.

Ensuite, je veux parler des terminaisons de commandes et des différences entre C sharp et Python.

Tout d'abord, qu'est-ce qu'une commande ? Eh bien, par exemple, ce bout de code ici est une commande.

Et ce qu'il dit, c'est prendre notre variable dude et lui assigner une valeur fausse.

De même ici, prendre notre variable dude, lui assigner une valeur vraie, et aussi la définir comme un Booléen.

Ce sont des exemples de commandes.

Donc, à un niveau très bas, la façon dont un ordinateur fonctionne, c'est qu'il doit savoir quand ces commandes commencent et se terminent pour savoir ce qu'il doit traiter.

Et c'est là que la terminaison de commande entre en jeu.

Nous avons besoin de quelque chose pour pouvoir séparer toutes ces différentes commandes.

Et en C sharp, la terminaison de commande est un point-virgule.

Ces points-virgules ici sont ce que vous devez ajouter à la fin de chaque commande pour pouvoir dire à l'ordinateur que cette commande est terminée, vous pouvez la traiter avant de traiter la suivante.

Je simplifie grossièrement, mais c'est ainsi que cela fonctionne à un niveau supérieur.

Et donc avec cela en C sharp, tant que vous avez un point-virgule séparant votre commande précédente de la suivante, vous pouvez placer vos commandes où vous voulez.

Par exemple, je peux déplacer cette commande ici pour qu'elle soit juste après la commande précédente.

Aucune erreur, aucun problème, je peux la remettre à la ligne suivante et appuyer sur Tab plusieurs fois, aucun problème, aucune erreur.

Vous avez beaucoup de flexibilité en utilisant le point-virgule comme terminaison de commande, C sharp a beaucoup de flexibilité à cet égard en utilisant le point-virgule comme terminaison de commande.

Maintenant, en Python, ils diffèrent beaucoup ici aussi.

Donc vous pourriez regarder C sharp et voir que le point-virgule a du sens comme terminaison de commande avec Python.

Comment font-ils cela ? Eh bien, la réponse est en fait assez simple, au lieu d'utiliser des points-virgules, ils utilisent simplement un saut de ligne.

Donc si vous voulez séparer deux commandes, vous les mettez simplement sur une nouvelle ligne.

Aussi simple que cela, en fait, pour démontrer, nous ne pouvons pas faire ce que nous avons fait ici en C sharp.

Si nous devions les mettre côte à côte, puis l'enregistrer, vous verrez que dans l'onglet problèmes, il dit que nous avons une syntaxe invalide car vous ne pouvez pas, il ne sait pas ce qui se passe ici.

Pourquoi y a-t-il une valeur et une variable l'après-midi, il ne comprend tout simplement pas comment Python a pensé à toutes les arrêts, vous pouvez simplement ajouter un point-virgule et Wallah, il agira maintenant comme une terminaison de commande.

En fait, juste pour prouver qu'il fait ce que je dis qu'il fait, je vais les mettre tous sur la même ligne avec deux terminaisons de commande.

Et puis je vais appuyer sur lecture et vous montrer qu'il s'exécute, il imprime 1337.

Donc oui, à cet égard, cela rend Python vraiment très flexible.

Parce que vous pouvez utiliser des points-virgules si vous voulez.

Cependant, vous trouverez que la plupart des développeurs ne le font pas, car il est souvent beaucoup plus rapide d'utiliser simplement la terminaison de commande de nouvelle ligne au lieu des points-virgules.

Et permettez-moi de vous le démontrer.

Donc je vais simplement restaurer les deux scripts à leur état initial, c'est une nouvelle ligne.

C'est une nouvelle ligne.

Cela faire cela.

D'accord, donc maintenant ils sont revenus à leur état initial.

Donc la raison pour laquelle vous pouvez gagner beaucoup de temps est que si vous regardez les deux scripts différents, ils utilisent tous les deux une nouvelle ligne de terminaison de toute façon, même si vous deviez regarder des scripts C sharp plus complexes, souvent vous trouverez que plus de 90% d'un script C sharp va utiliser comme une nouvelle ligne comme terminaison de commande de toute façon.

Donc vous gagnez en fait beaucoup de temps sans avoir à taper, vous savez, point-virgule, point-virgule, point-virgule, et vous verrez qu'il devient rouge dans ce contexte, car il vous fait savoir qu'il est pratiquement inutile.

Comme nous savons que vous voulez terminer cette commande en allant à la nouvelle ligne.

Et puis si nous devions appuyer sur la touche de retour arrière, elle devient blanche, car comme, d'accord, maintenant elle est en cours d'utilisation, nous comprenons ce que vous essayez de faire ici.

Mais sachez que c'est une fonctionnalité qui vient avec l'IDE Visual Studio Code.

Donc prenez les informations comme vous le souhaitez, mais sachez que la plupart des développeurs Python vous regarderont de travers s'ils voient des points-virgules dans votre code.

Donc oui, il y a quelques différences de syntaxe là.

Ensuite, je veux parler de la façon dont ils diffèrent dans le blocage de code.

Donc première question, qu'est-ce que le blocage de code ? Eh bien, je vais venir ici en C sharp et vous donner un exemple rapide.

Tout d'abord, la façon dont vous indiquez un bloc de code est d'utiliser ces accolades.

Tout ce qui va à l'intérieur de ces accolades est un bloc de code.

Donc la syntaxe générale, vous n'avez pas à la suivre, mais la plupart des développeurs mettront un bloc de code, une ligne au milieu est tout le code qui sera exécuté dans ce bloc de code, et puis une accolade à la fin.

Et donc ici, nous pouvons, par exemple, déplacer notre do it equals false dans ce bloc.

Et bien sûr, supprimer celui-ci car nous n'en avons pas besoin.

Et voilà, nous avons un bloc de code en C sharp, cependant, un bloc de code comme celui-ci est assez inutile à ajouter car il sera exécuté quoi qu'il arrive.

Cependant, ce que le blocage de code vous permet de faire est que vous pouvez ajouter des choses comme, par exemple, une instruction if.

Donc nous pouvons dire si do it, alors définir duals equals false.

Et ce bloc de code ne s'exécutera que si do it equals true.

Et je veux vous le prouver.

Donc je vais venir ici, et je vais écrire console, dot write line, cela va imprimer tout ce que nous voulons dans la console.

Et je vais dire vérifier.

Et puis je vais descendre ici et faire la même chose.

Je vais dire console dot write, ou attendez, qu'est-ce que c'est ? console, dot write line, nous y voilà.

Euh, d'accord, défini sur false.

D'accord.

Et puis à la fin, nous avons besoin d'une console dot read key.

Cela fait simplement en sorte que le terminal ne se ferme pas lorsque nous appuyons sur le bouton de démarrage, qui est ici et je vais appuyer sur boom, le terminal est hors écran, je le ramène, et voilà.

Vous voyez qu'il va vérifier, et puis il le définit sur false.

Mais vous n'êtes pas convaincu parce que nous avons bloqué ce code et il s'est quand même exécuté.

Donc je vais changer do a T equals false et regarder ce qui se passe lorsque j'appuie sur le bouton de démarrage et que je ramène le terminal ici.

Il dit simplement vérifier parce que, encore une fois, do it equals false et nous avons dit si do it, ce qui est une autre façon de dire si do it equals true, alors exécutez ce bloc de code.

Et au fait que do it equals false, ce bloc de code n'a jamais été exécuté.

Et c'est le blocage de code, vous trouverez que le blocage de code est très important et très utile pour toutes les choses de programmation.

Mais c'est ainsi que vous le faites en C sharp.

Maintenant, en Python, c'est encore une fois très différent, je vais me débarrasser de ces deux lignes juste pour que ce soit beaucoup moins confus.

Et donc tout ce qui est sous la condition et indenté sera compté comme ce bloc de code.

D'accord, et je vais exécuter cela, et vous verrez que nous obtenons vérifier défini sur false.

Et puis nous avions aussi une impression supplémentaire ici, que nous avons déplacée la prochaine fois, mais cela imprime aussi false.

Et encore une fois, vous n'êtes pas convaincu parce que ce bloc de code est exécuté de toute façon.

Donc nous allons définir cette valeur sur false.

Et puis je vais aussi supprimer cela pour que ce ne soit pas confus lorsqu'il imprime, puis enregistrer, appuyer sur lecture et seulement vérifier.

Et donc c'est ainsi que vous faites le blocage de code en Python.

Et donc comme vous pouvez le voir, le blocage de code est une autre syntaxe que C sharp et Python ont beaucoup de différences entre eux.

Mais il est très important de savoir comment faire du code walk dans les deux langages, car vous l'utiliserez assez souvent pour les boucles for, pour les instructions if, pour les méthodes, les fonctions, toutes sortes de choses.

Et la toute dernière chose que je veux aborder aujourd'hui s'appelle la portée des variables.

Donc qu'est-ce que la portée des variables ? Eh bien, avec l'introduction au blocage de code, c'est ceci, un bloc de code.

Souvenez-vous, c'est aussi un bloc de code, bien, plus ici, c'est un bloc de code.

Mais avec l'introduction de ces blocs de code, vous devez maintenant vous soucier de la portée de vos variables.

Donc laissez-moi vous donner un exemple rapide.

Donc disons que dans ce bloc de code, ici, nous voulons initialiser une nouvelle variable.

Initialisons simplement pour faire un entier, nous l'appellerons a juste pour un exemple.

Et puis nous lui assignerons une valeur zéro, n'est-ce pas ? Eh bien, parce que nous initialisons cette variable entière dans ce bloc de code, elle ne peut pas être utilisée en dehors de ce bloc de code.

Et pour le démontrer, je vais venir ici, et je vais faire en dehors du bloc de code, console dot write line, oops, bright line.

A, par exemple.

Et vous pouvez voir ce qui se passe, il dit que cette variable n'existe pas.

Que voulez-vous dire, elle n'existe pas, donc nous l'avons initialisée ici ? Eh bien, encore une fois, comme je l'ai dit, cette variable, parce que nous l'avons initialisée dans ce bloc de code ne peut pas quitter ce bloc de code.

Si nous voulions quitter ce bloc de code, nous devons le faire comme ceci, nous sortons ici, oops, nous sortons ici et nous initialisons int a est égal à dire, cinq, par exemple.

Et puis à l'intérieur de ce bloc de code, nous changeons simplement, nous le réassignons à zéro.

Donc parce qu'il est initialisé dans ce bloc de code, qui est notre fonction principale, nous pouvons l'utiliser en dehors de ce bloc de code.

Et c'est la portée des variables.

En résumé, en C sharp, cette syntaxe n'est pas différente.

Donc si nous devions venir dans ce bloc de code et initialiser un A, assigner un zéro à cela, et puis venir en dehors de ce bloc de code et essayer d'imprimer cette variable a, vous verrez que lorsque nous enregistrons et appuyons sur le bouton de lecture, nous obtenons une erreur de syntaxe disant que cette variable a n'est pas définie.

Et encore une fois, si nous voulons contourner cela, nous devons changer la portée d'une variable.

Donc sortons de l'indentation régulière, et faisons simplement a est égal à cinq, par exemple.

Et puis lorsque nous entrons dans cette portée, nous allons simplement la réassigner, la changer en zéro, et puis nous pourrons l'imprimer et prouver que j'ai appuyé sur enregistrer, et puis j'ai appuyé sur lecture.

Et voilà, vérifier cinq.

Et encore une fois, je veux juste m'assurer de couvrir toutes les bases.

La raison pour laquelle cela imprime vérifier cinq est parce que nous avons dit do it est égal à faux.

Et si do it est vrai, alors ce bytecode sera exécuté, mais parce que do it est faux, ce bytecode n'est pas exécuté.

Donc il saute simplement tout cela.

Et il imprime simplement cinq, ce que nous avons assigné à.

Et c'est à peu près tout.

C'est tout ce dont vous avez besoin pour remarquer notre programmation en ce qui concerne la syntaxe.

Et donc en conclusion, même si C sharp et Python ont des différences dans leur syntaxe, comme vous pouvez le voir, les différences sont suffisamment petites pour pouvoir retenir l'essentiel, vous devez définir les types de données en C sharp Python, vous ne le faites pas en C sharp, vous devez utiliser des points-virgules pour terminer les commandes.

Python utilise des sauts de ligne, et C sharp utilise des accolades pour le blocage de code tandis que Python utilise l'indentation.

Bien sûr, il y a plus de différences dans leur syntaxe.

Mais ce sont les principales différences qui confondent souvent les développeurs.

D'accord.

D'accord.

D'accord.

C'est le moment de coder votre premier programme.

Êtes-vous prêt à faire cela ? Prêt, partons.

Donc nous allons faire une simple application MATLAB.

Dans la console, car c'est simple, ne nécessite pas d'installer un million de choses et est quelque chose que vous pouvez montrer à vos amis et à votre famille.

Maintenant, avant de nous lancer dans ce premier projet, le code de ce projet est dans la description.

De plus, je pense qu'il est important de vous faire savoir que cette leçon agit un peu comme un test de classement.

Si vous commencez tout juste à programmer, vous pourriez avoir du mal à comprendre ce qui se passe dans le code.

Et si c'est vous, eh bien, ce n'est pas grave.

Parce que j'ai structuré cette leçon pour être un peu difficile à suivre.

Une fois capable de coder un projet comme celui-ci par vous-même, alors, je ne pense pas qu'il y ait beaucoup de choses que ce cours puisse vous enseigner à ce moment-là.

Mais je vous encourage à regarder le tout et à suivre.

De toute façon.

Encore une fois, le code est dans la description.

Donc vous pouvez simplement vous y référer et me suivre.

Parce que si vous faites ce qui suit, vous obtiendrez la plus grande inspiration pour devenir programmeur.

Après avoir lutté, je vous encourage à parcourir le reste de mon cours LinkedIn description, ou simplement à consulter les leçons sur les choses qui n'étaient pas faciles à suivre.

J'ai plus de 20 vidéos qui vous enseignent comment coder et ces vidéos approfondissent leurs sujets respectifs.

Ensuite, lorsque vous vous sentez à l'aise, revenez à cette leçon et voyez comment vous vous en sortez une deuxième ou troisième fois en codant votre premier projet.

Et faites-moi confiance, lorsque vous regardez combien de choses que vous ne compreniez pas par rapport à la prochaine fois où vous essayez de coder votre premier projet, vous ne voudrez pas arrêter de programmer, ayant programmé pendant 15 ans, je peux vous dire que ce sentiment résume très bien la programmation, cela peut devenir assez addictif à poursuivre, mais une addiction de la meilleure façon possible.

Cependant, si c'est votre deuxième ou troisième fois ou plus que vous codez votre premier projet, je vous encourage à ne pas copier le code mot à mot.

Mais peut-être créer votre propre histoire ou ajouter des instructions et des fonctions à ce jeu de mad libs, qui sait, votre expérimentation pourrait commencer une toute nouvelle tendance en programmation.

Enfin, si vous voulez partager votre projet avec moi, n'hésitez pas à me le tweeter et je serai heureux de vous répondre.

Mais maintenant, avec tout cela hors du chemin, commençons à coder votre premier programme.

Et nous allons faire cette application en deux langages différents car je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows, ou si vous voulez créer des jeux en utilisant l'un des moteurs de jeu les plus populaires appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, commençons à écrire notre programme Mad Libs.

Maintenant, avant d'écrire un projet ou un programme ou un prototype, que vous ayez, j'aime généralement commencer par ce que j'aime appeler un squelette et ce qu'est un squelette, c'est à peu près comme un processus étape par étape dans lequel vous pouvez vous attendre à devoir faire pour compléter le projet réel.

Et parce que c'est un programme plus petit et plus simple, nous pouvons simplement le faire en écrivant quelques commentaires.

Donc d'abord, je vais commenter l'initialisation des variables, et cela signifie simplement initialiser est plus court que le liège à droite, puis après cela, obtenir simplement l'entrée de l'utilisateur.

Donc nous allons initialiser les variables.

Et puis nous allons demander à l'utilisateur de remplir les données pour ces variables.

Et puis après cela, nous devons initialiser, oops, et tricoter l'histoire.

Et puis après avoir initialisé notre histoire, alors nous devons simplement imprimer notre histoire.

Et pour les parties, notre programme sera terminé.

Simple, facile et direct.

Et maintenant, faisons simplement la même chose en Python, faisons un commentaire, puis un net variables et puis obtenons, oops, obtenons l'entrée de l'utilisateur.

Et puis après cela, nous allons mettre fin à notre histoire.

Et puis après cela, nous devons imprimer l'histoire.

Facile comme cela.

La prochaine chose que je vais faire rapidement est simplement embellir notre script.

Je vais simplement ajouter des espaces entre tous les commentaires, cela m'aide à le lire et à comprendre les différents processus qui doivent avoir lieu.

Parfait.

D'accord, continuons.

Maintenant, avant de pouvoir faire quoi que ce soit ici, C sharp à gauche, nous avons besoin de notre histoire car tout dépend de notre histoire, vraiment.

Donc je vais coller une citation de la matrice.

Je vais simplement surligner tout cela rapidement et appuyer sur Tab quelques fois pour l'embellir, le rendre plus facile à lire.

Mais vous êtes les bienvenus pour inventer votre propre histoire.

Vous êtes les bienvenus pour prendre n'importe quoi sur Internet.

Ce que vous voulez utiliser comme votre histoire Mad Libs est complètement bien.

J'ai même mis l'histoire dans la description si vous voulez l'utiliser aussi.

Mais la voici.

C'est l'histoire que nous voulons utiliser pour C sharp.

Et maintenant je vais faire la même chose pour Python.

Je vais simplement coller cette chaîne d'histoire, la même chose exactement, juste dans un format Python.

La prochaine chose que je vais faire est simplement imprimer l'histoire.

Et en C sharp, vous allez vouloir faire console dot write line.

Et puis ad lib story, Mad Libs story, boom, point-virgule, terminé.

Et en Python, nous allons vouloir attendre, je vais changer cela pour dire Madlib story juste pour que ce soit la même mère histoire parfaite.

Et en Python, c'est vraiment simple.

Vous tapez simplement prints, et puis Madlib story, boom.

Donc ensuite, ce que nous voulons faire est obtenir l'entrée de l'utilisateur.

Mais nous ne pouvons pas vraiment obtenir d'entrée de l'utilisateur car nous n'avons pas de variables à passer à l'utilisateur pour collecter des données.

Et donc ce que notre prochaine étape réelle est, nous devons initialiser nos variables afin de pouvoir les passer à l'utilisateur.

Et pour initialiser nos variables.

Eh bien, nous devons transformer notre histoire Mad Libs en un tas de variables.

Et nous pouvons le faire assez simplement, si vous êtes familier avec le jeu Mad Libs, vous savez que tout le plaisir du jeu est que vous avez une histoire ou un texte ou quelque chose de ce genre.

Et vous remplacez tous les verbes, les noms, les adjectifs, etc., par des mots de contexte similaire, espérons-le, mais pas exactement.

Et cela crée des histoires vraiment drôles et intéressantes.

Et donc ce que nous voulons faire est de faire défiler notre texte et essentiellement remplacer les verbes, les noms, les adjectifs, par des variables, et le premier que je vais faire est la matrice, je vais simplement mettre des accolades autour de cela, oh, oui, je dois en faire une chaîne interpolée.

Je vais faire cela pour toutes ces chaînes.

Et cela doit être une variable, qui est un mot, la matrice boom.

Et donc je vais simplement venir à de nouvelles variables, je vais initialiser le type de données de chaîne, et mettre la matrice là.

Et maintenant la matrice est une variable que nous pouvons demander à l'utilisateur, et ils peuvent la changer en ce qu'ils veulent.

Et je l'ai fait un peu à l'avance, je suis passé dans le texte et j'ai choisi beaucoup de verbes, de noms, d'adjectifs que je pensais intéressants à changer.

Donc je vais simplement passer et faire cela, par exemple, le système est un autre, je vais changer le système en variables, je peux l'ajouter à cette liste.

Et je vais simplement faire cela pour tout le texte.

Je vais le sauter cependant, car ce n'est pas très amusant à regarder.

D'accord, donc je suis passé dans mon histoire et j'ai remplacé tous les verbes, noms, adjectifs intéressants, etc., par des variables afin que nous puissions les passer à l'utilisateur, et ils peuvent mettre les mots qu'ils veulent là.

Mais maintenant je veux vous montrer votre premier truc d'optimisation.

Si vous regardez cette ligne ici, la phrase en tant qu'hommes d'affaires, enseignants, avocats, charpentiers, ce sont tous des professions, c'est ce qu'ils ont tous en commun.

Et au fait qu'ils vont de l'avant à l'arrière, nous pouvons faire un truc vraiment cool.

Eh bien, nous allons initialiser un tableau de chaînes, et nous les appellerons profession.

Et puis revenir à l'initialisation est égal à un nouveau tableau de chaînes de combien y en a-t-il 1234, un quatre.

Et donc maintenant nous pouvons faire ce truc vraiment cool où nous venons ici, et faisons simplement de cela une chaîne interpolée.

Et surchargeons le cas qui est juste pour une bonne pratique, hommes d'affaires, et Oops, désolé, ce n'est pas ce que je veux faire, je veux faire profession, zéro, parce que nous allons faire une boucle for, ce que je vais aborder dans une seconde.

Je vais copier cela, parce que je suis paresseux.

Et je vais coller cela ici, et l'incrémenter, et puis nous allons coller cela ici.

Et puis je vais l'incrémenter à deux.

Et puis la dernière profession, incrémente cela à trois, déjà commence à zéro, simple dans le point.

Et donc maintenant ce que nous pouvons faire est lorsque nous obtenons l'entrée de l'utilisateur, puisque il y a quatre professions, elles sont toutes dos à dos, nous pouvons simplement écrire une simple boucle for et demander à l'utilisateur quatre professions différentes, l'une après l'autre.

Et je vous montrerai comment faire cela dans un peu.

Mais il y a aussi deux adjectifs ici qui font cela avec donc je vais simplement initialiser un nouveau tableau de chaînes, appeler cela additif AJ, DJ sharp additif est égal à un nouveau tableau de chaînes de deux, il n'y en a que deux là.

Et donc ici, transformons cela en un flux interpolé, ce sera un D j, zéro.

Et je vais copier cela parce que je suis paresseux et c'est le deuxième adjectif.

Je vais simplement incrémenter.

Et voilà, nous avons maintenant nos deux tableaux de chaînes.

Et dernière note, si vous regardez ici, vous verrez une série d'erreurs pour les variables locales non assignées.

Et c'est seulement parce que nous n'avons pas encore assigné ces variables à quoi que ce soit.

Je crois qu'elles ne sont pas là pour le moment, ce que votre programme n'aime pas, mais nous allons assigner les variables lorsque nous obtiendrons l'entrée de l'utilisateur.

Et en Python à droite, c'est beaucoup la même chose.

D'abord, transformons toutes nos chaînes en chaînes interpolées.

Et c'est comme en C sharp, sauf que c'est un F au lieu d'un signe $1.

Donc je vais simplement ajouter un F à toutes les chaînes.

Parfait.

Et sortons cette variable ici, la matrice, ou plutôt, transformons cela en une variable appelée la matrice.

Et puis initialisons-la ici et faisons la matrice égale à une chaîne vide.

D'accord, et puis faisons le système suivant, la chaîne interpolée système.

Et puis le système comme ceci, collons-le égal à une chaîne vide.

Et je vais passer et faire cela pour tous les verbes, adjectifs et noms intéressants de ce texte.

D'accord, donc j'ai extrait tous les mots intéressants et les ai transformés en variables.

Et maintenant je vais vous montrer comment faire ce truc d'optimisation en Python.

Donc encore une fois, nous avons ces quatre professions, et nous voulons transformer cela en un tableau de chaînes.

Et pour faire cela en Python, nous allons faire profession égale aux crochets, et donc les pièces seront des chaînes vides, des chaînes vides, des chaînes vides, des chaînes vides pour des chaînes vides.

Et nous avons un tableau avec quatre chaînes dedans, que nous pouvons passer à l'utilisateur et puis ils peuvent changer la bière ou ce qu'ils veulent.

Et c'est la même chose qu'en C sharp, n'utilise pas de chaîne interpolée, professions zéro, je suis paresseux, je copie cela et le colle ici, l'incrémente, le colle ici, l'incrémente, collé ici, l'incrémente, oops, oui, c'est trois.

Et puis nous voulons aussi notre tableau d'adjectifs, qui n'en a que deux.

Donc je vais faire des crochets, une chaîne vide, et puis une autre chaîne vide, deux chaînes vides.

Et puis cela va ici, qui est un bord, zéro, je vais copier cela parce que je suis paresseux, et puis le coller sur dépendant, et puis l'incrémenter, et bada boom, maintenant les scripts sont dans le même état exact.

Pour tout bien, la dernière ligne droite, obtenons cette entrée de l'utilisateur.

Donc tout d'abord, il y a deux fonctions que nous devons nous familiariser.

L'une que nous avons déjà vue, et c'est console dot write line.

C'est là que nous allons l'utiliser pour imprimer quelque chose à la console.

Et la seconde est console dot read line.

C'est là que nous allons l'utiliser, eh bien, il n'y a pas de paramètres d'entrée.

Mais cela va nous retourner une chaîne que nous pouvons définir pour nos variables de chaîne.

Et cela vient de ce que l'utilisateur tape dans la console et appuie sur entrée.

C'est ce qui va être retourné avec console dot read line.

Par exemple, nous pouvons faire la matrice égale à console dot readline.

Facile comme cela.

Donc commençons.

J'ai un peu préparé à l'avance une petite histoire intéressante que l'utilisateur peut avoir avec le terminal juste pour m'assurer que je ne trébuche pas sur cette partie.

Mais commençons par console dot write line.

Faisons comme, bienvenue.

utilisateur, bienvenue utilisateur.

Et puis nous pouvons passer à un autre, console dot write line.

Et puis disons, jouons à un jeu de Mad Libs.

Et puis après cela, nous pouvons obtenir leur nom.

Donc nous pouvons dire, faisons un autre console dot write line.

Et puis s'il vous plaît partagez avec moi votre nom.

Et puis ici, le terminal va s'arrêter et leur permettre de mettre une entrée.

donc ici nous pouvons faire Neo, puisque c'est le nom du personnage dans le texte, est égal et nous pouvons faire console dot read line.

Et ce qu'ils ont retourné ici est ce que la variable Neo va être définie.

Et juste au cas où vous ne me croyez pas, essayons réellement d'exécuter ce programme et voyons cela imprimé à l'écran.

La première chose que nous devons faire, cependant, avec toutes ces erreurs, il ne nous permettra pas d'exécuter réellement le programme.

Donc commentons simplement cela et Fatigué, oops, attendez une seconde, je dois faire cela et commenter cela, venir avec celui-ci tout le long de la ligne.

Donc cela ne se compile pas.

Et puis remplaçons cela pour l'instant par, avec Neil.

Donc quel que soit le nom que nous passons au terminal, il va simplement le recracher.

Et cela va vous prouver que nous sommes capables de définir des variables de cette manière.

Donc je vais venir ici en haut et appuyer sur start.

Et ma fenêtre sort en fait du cadre.

Je vais la ramener à l'écran.

Donc comme nous l'avons mis Bonjour, bienvenue utilisateur, jouons à un jeu de Mad Libs, partagez avec moi votre nom, et je vais mettre mon nom pour ramener cela.

Bien sûr, il va quitter parce que nous n'avons même pas dit de pause.

Donc faisons Um, je pense que nous devons annuler cela, attendre cela, faisons une autre lecture de clé, concept de lecture de clé qui va attendre une pression de touche et puis il va quitter le terminal.

Donc exécutez-le à nouveau.

Ramenez-le à l'écran.

Bienvenue utilisateur.

Jouons à un jeu de Mad Libs, s'il vous plaît partagez avec nous votre nom, je vais mettre bros et ils impriment directement à nous le même variable que nous avons mis, ce qui vous fait savoir qu'il fonctionne réellement.

Donc maintenant je vais simplement revenir à son état initial.

Et nous pouvons faire z Ctrl, z Ctrl Z Ctrl, z Ctrl Z.

Donc plusieurs fois, et nous sommes réveillés à un point-virgule, et nous sommes de retour à notre état initial.

Et si vous n'avez pas de contrôle Z, je pense que sur Apple, c'est Apple z, je crois.

Mais si vous n'avez pas ces boutons, vous pouvez venir en haut à éditer et puis cliquer sur annuler ici.

Et cela fera la même chose que j'ai fait avec mon raccourci sur le clavier.

Aussi, rapidement, ajoutons à la toute fin de notre processus, ajoutons console, console dot read key.

Cela s'assurera qu'il met en pause l'application avant de quitter.

D'accord, donc maintenant en Python, commençons à obtenir des entrées des utilisateurs.

Donc ce que nous voulons faire ici, au lieu d'écrire console dot write line, encore une fois, c'est aussi simple que prints.

Et nous pouvons faire print, welcome, user, descendre à un autre print.

Jouons à un jeu de Mad Libs, et puis un autre print et disons, s'il vous plaît, s'il vous plaît partagez avec moi votre nom.

Et puis nous pouvons simplement faire Neo equals inputs.

Eh bien, techniquement, techniquement, nous pouvons ajouter cette chaîne dans input, et ce sera la même chose exacte.

Donc nous pouvons faire cela, et il imprimera et puis quelle que soit la ligne suivante, il obtiendra cette entrée.

Cependant, nous devons ajouter une pause ici.

Sinon, il va vous permettre de taper juste après le point d'interrogation, nous voulons aller à une nouvelle ligne, juste pour le rendre un peu plus propre.

Et donc maintenant, la chose cool est que maintenant que nous avons notre nom réel défini dans la variable, Neo, nous pouvons l'utiliser avec notre fonction d'impression.

Donc si nous faisons console dot write line, par exemple.

Interpolons la chaîne et disons Bonjour.

Et puis nous pouvons faire ici, Neo.

Et puis un point d'exclamation.

Et puis disons quelque chose comme, êtes-vous prêt ? Êtes-vous prêt ? Et puis qu'est-ce que quelque chose que vous voulez savoir plus ce qui manque d'espace ? Donc je vais passer à la ligne suivante pour en savoir plus sur.

Il a appris à épeler plus sur.

Et puis la ligne suivante, quand ils répondent ce qu'ils veulent savoir plus, nous pouvons mettre cela dans la matrice.

Donc j'ai oublié mon point-virgule.

Donc nous pouvons faire la matrice égale à console dot read line.

Facile comme cela.

Et en Python, c'est à peu près la même chose.

Nous allons faire print.

Qu'est-ce que c'est quand interpoler la chaîne avec F ? Bonjour.

Et puis ce sera Neil.

Oops, Neil.

Et puis êtes-vous prêt ? Êtes-vous prêt ? Et puis en fait, je vais casser cela.

Oops, je vais casser cela en un autre print.

En fait, je veux en faire une entrée.

entrée.

Et puis c'est ce qui est quelque chose que vous voulez savoir, oops, pour en savoir plus sur.

Et bien sûr, nous devons faire la variable matrice égale à ce qu'ils veulent savoir plus.

Donc juste pour m'assurer que vous êtes toujours avec moi, rappelez-vous simplement que la seule chose sur laquelle nous travaillons actuellement est obtenir l'entrée de l'utilisateur.

C'est cette section ici, tout le reste nous ne nous concentrons pas dessus.

Et dans cette section, il n'y a que deux fonctions que nous utilisons.

La première s'appelle lire la ligne, qui est simplement l'impression d'une chaîne à l'utilisateur.

Et une seconde est console dot read line, qui nous retournera ce que l'utilisateur a entré dans sa console, que nous pouvons ensuite assigner à une variable.

C'est tout.

Rien de plus complexe que cela.

Donc en continuant avec notre petite histoire, nous pouvons nous amuser beaucoup.

Et faire console dot write line, et puis interpoler une chaîne, et faire quelque chose comme, oh, et puis nous pouvons mettre vous voulez en savoir plus sur, et puis la matrice Ha.

Vous savez, juste vous amuser avec.

Et puis nous pouvons faire une autre ligne console, dot write line, interpoler une chaîne.

Voyons voir.

Ensuite, nous voulons obtenir la variable système.

Et donc nous devons leur donner un peu de contexte.

Donc nous pouvons faire quelque chose comme, d'abord, voyons voir d'abord.

D'accord, s'il vous plaît, soyez patient avec moi.

D'accord, eh bien, d'abord, dites-moi ce que vous savez déjà sur la matrice.

Et puis faisons une dernière, qui leur donne un peu d'instruction, car c'est madlibs.

Après tout, nous allons faire voyons voir maintenant, comment catégoriseriez-vous la matrice comme, et puis nous pouvons ajouter comme un petit point-virgule ici.

Et puis enfin, enfin, nous pouvons faire système égal à console dot readline.

Et oui, assez simple.

Encore une fois, j'essaie simplement de m'amuser avec ce Mad Libs pendant que nous obtenons les données, les informations, l'entrée de l'utilisateur.

Et donc, vous savez, tout cela est des indices de madlibs pour le moment.

Mais vous voulez aussi donner, vous savez, c'est tous des indices de madlibs pour le moment.

Mais vous voulez aussi donner à l'utilisateur comme une sorte d'indice sur le mot qu'ils remplacent.

Donc j'ai simplement demandé quel nom catégoriseriez-vous la matrice comme, et il essaie simplement de s'amuser avec cela en Python, pas grand-chose ne change vraiment, nous imprimons simplement les mêmes chaînes exactes.

Donc oh, oh, vous voulez en savoir plus sur cela ? Je veux dire, vous mettez la matrice et puis imprimez une autre ligne.

Et cela va dire, D'accord, eh bien d'abord, dites-moi, oops, dites-moi ce que vous savez déjà sur la matrice pour une autre ligne.

Nous sommes en df et puis qu'est-ce que maintenant ? Catégoriseriez-vous la matrice ?

En fait, j'oublie que c'est Python.

Donc nous pouvons en fait faire de cette entrée notre entrée, et puis faire système égal à cette entrée.

Et juste pour vous prouver que nous essayons simplement de créer l'histoire ici, rien de plus complexe que cela.

Je vais initialiser toutes ces variables restantes comme des chaînes vides juste pour que cette erreur disparaisse.

Parce que la chaîne vide est égale à la chaîne vide, est égale à la chaîne vide, est égale à la chaîne vide.

Et maintenant nous pouvons réellement imprimer cette histoire.

Même si la plupart des mots, la plupart des rôles très probablement vont être, oops, est égal à la chaîne vide, vont être des chaînes vides.

Nous pouvons imprimer cela.

Ma console va à gauche.

Donc quel est mon nom pour les brillants ? Et puis, comme nous l'avons écrit, hello jimbros nous a donné son nom.

Êtes-vous prêt ? Qu'est-ce que quelque chose que vous voulez savoir plus sur ? Il y a une faute de frappe là.

Nous pouvons corriger cela.

Je veux en savoir plus sur la pizza, par exemple.

Oh, vous voulez en savoir plus sur la pizza ? Ha.

D'accord, eh bien d'abord, dites-moi ce que vous savez déjà sur la pizza.

Qu'est-ce que maintenant ? Catégoriseriez-vous la pizza comme je dirais que la pizza est une tarte.

Et puis c'est aussi loin que nous en sommes dans notre code.

Donc maintenant cela fait les Mad Libs, il remplace les variables dans l'histoire réelle des Madlib.

Et ils obtiennent, nous leur donne cette pizza est une tarte deux Bros.

Cette tarte est notre et puis c'est toutes des chaînes vides à partir de là.

Mais comme vous le voyez, c'est tout ce que nous faisons en ce moment, c'est cette partie du script du terminal, nous créons simplement cette histoire.

C'est tout ce qu'il y a à faire.

Espérons qu'à ce stade, je vous ai convaincu que nous ne faisons rien de complexe.

Avec cette étape, nous imprimons simplement une histoire à la console et demandons des variables.

C'est tout.

Donc terminons simplement notre histoire en continuant.

Donc la prochaine chose que je veux faire ici est bien sûr, nous allons faire console dot write line.

Et nous allons interpoler une chaîne.

Et ce que je veux mettre ensuite est, voyons voir.

Donnez-moi un nom imposant, imposant maintenant, au système, oui, parce que le prochain mot que nous allons obtenir est ennemi, nous allons essayer de remplacer ennemi encore une fois, nous essayons simplement de leur donner un indice pour un bon nom à remplacer.

Donc cela devrait fonctionner.

Donc ensuite, nous allons faire ennemi égal à console.

dot read line.

D'accord, donc espérons que cette chaîne que je suis en train d'imprimer, que je suis en train d'imprimer à la console, est suffisante pour leur donner un indice.

Sur un bon mot, remplacer ennemi avec continuer, nous allons faire un autre console dot write line.

Et qu'obtenons-nous ensuite ? Ensuite, nous allons obtenir le mot inside.

Donc voyons voir.

Quel indice puis-je donner pour inside, je ne sais pas, relaxant.

Maintenant, disons maintenant donnez-moi un relaxant.

Maintenant, bien sûr, cela doit être au présent, au présent.

Et puis nous pouvons faire inside égal à console dot read line à nouveau.

Et nous continuons ainsi, nous ne nous mettons pas à jour en Python.

Donc la dernière fois que nous avons laissé était le système.

Donc nous devons imprimer, voyons voir, interpoler une chaîne.

Faisons ce qui est, donnez-moi un nom imposant maintenant au système.

J'oublie toujours que c'est Python, donc nous n'avons pas à imprimer et puis faire une lecture de ligne.

Nous pouvons simplement faire input.

Voyons voir, quelles sont les variables ennemi, oui ? Oui, ennemi égal à input.

Cool.

Et puis nous pouvons faire la même chose avec inside égal à input.

Et puis je vais interpoler la chaîne.

Et puis faisons maintenant.

Maintenant donnez-moi un relaxant.

Maintenant, présent.

D'accord, oops, non, point-virgule, non Python.

Cool.

Et nous sommes tous à jour.

Maintenant, cette partie est la partie intéressante que nous avons un peu mise en place plus tôt dans la vidéo.

Maintenant, nous devons utiliser notre boucle for pour nos tableaux de chaînes.

Et donc nous pouvons nous y prendre de manière très simple, il suffit de créer une boucle for pour int i égal à zéro.

i est inférieur à profession, point longueur, point-virgule i plus plus, et puis descendre ici, sorte de crochets.

Et donc cette boucle for va simplement passer par les professions qui est la prochaine dans l'invite de texte, et nous pouvons simplement demander.

Voyons voir.

Je suppose qu'avant cela, nous devons alerter l'utilisateur, disons console dot write line et disons D'accord.

Maintenant, j'ai besoin de professions, professions, professions relatives à ce que cela relaie au système et interpoler la chaîne ici, boom.

Donc nous laissons alerter l'utilisateur de ce qui est sur le point de se passer, j'ai besoin de professionnels pour construire des systèmes.

Et puis ici, nous pouvons faire console dot write line.

Et nous allons faire une course interpolée ici.

Et faisons profession.

Si j'ai des fautes de frappe, je m'excuse, profession, pluriel.

Parce que, encore une fois, nous faisons des hommes d'affaires, je ne me souviens pas d'eux à l'origine, des hommes d'affaires mckellan, quelque chose comme ça.

Mais ils sont un employé rural.

Et puis nous pouvons simplement leur faire savoir où ils en sont, en faisant i plus un, parce que cela va commencer à zéro.

Donc nous pouvons faire cela plus un pour le faire commencer à un.

Et puis simplement profession dot longueur.

Bien, donc ce que cela fait, laissez-moi simplement vous guider à travers cela, c'est un peu vague.

Donc ce que cela fait, simplement, comme nous passons par notre boucle for, il y a quatre professions différentes, cela va écrire à la console, donnez-moi une profession, pluriel, et cela va imprimer quel numéro de profession ils remplissent actuellement.

C'est tout ce que c'est.

Et puis il est divisé par la longueur est combien de professions nous avons besoin.

Et je vous montrerai cet exemple un peu plus tard.

Mais une fois que nous avons fait cela, alors après chaque fois que nous imprimons cela à la console, nous voulons lire la ligne et assigner profession de AI à cela, et cela remplira pratiquement tout notre tableau de chaînes de profession.

D'accord, et pour rattraper Python, ce n'est pas trop difficile, bien sûr, nous devons écrire notre print.

Et nous alertons actuellement le joueur qu'une boucle for est sur le point de se produire pour la plupart.

Donc d'accord, maintenant j'ai besoin de quatre pro fish ones relatives au système.

Bien.

Et puis nous devons faire notre boucle for.

Et les boucles for en Python sont un peu différentes.

Donc nous allons faire pour i dans la plage, la longueur de la profession.

Et puis nous ferons notre deux-points et la ligne suivante fera profession de AI égale à inputs.

Et puis ici, que mettons-nous, nous mettons profession, qui est définitivement une faute de frappe dans le C sharp profession.

Et puis pluriel.

Et puis ici, nous allons faire i plus un, espérons que ce n'est pas une chaîne interpolée, et ajouter un F pour faire une chaîne interpolée, divisée par la longueur, oops, allez, allez.

La voici, la longueur de la profession.

Et les voilà.

Ils sont maintenant actuellement à jour.

Maintenant, à ce stade, je suis presque sûr que vous pourriez terminer ce programme par vous-même, car nous faisons essentiellement la même chose que nous avons fait.

Et une fois que vous avez rempli le reste, qu'est-ce que c'est, trois ou quatre variables, l'application est terminée.

Cependant, je veux prendre une seconde pour faire une pause, car je n'ai souvent pas fait cela sans laisser de commentaires.

C'est toujours bien de laisser des commentaires pour soi-même dans le futur.

Ou si vous allez envoyer cela à un ami, ou si vous allez le télécharger sur GitHub pour que d'autres développeurs essaient de le décomposer et d'apprendre de lui, c'est toujours bien et agréable de laisser des commentaires.

Donc faisons cela.

Juste pour expliquer ce qui se passe ici.

Je vais simplement dire que nous obtenons la variable matrice, une variable de l'utilisateur, il y en aura beaucoup de ces commentaires pour obtenir la variable système, la variable de l'utilisateur, pour obtenir la variable ennemi de l'utilisateur où je n'ai même pas ajouté le système, la variable système de l'utilisateur, désolé, pour obtenir cette variable intérieure ? variable de l'utilisateur.

Et puis ce sont des bras et dire commencer.

Non, commencer.

Maintenant, je vais dire que je vais dire obtenir obtenir toutes les professions.

De l'utilisateur.

Aussi, je sais que j'ai une faute de frappe ici.

Donc je vais corriger cela, profession.

Oui.

Cool.

Je vais en fait combiner ceux-ci, pas pas.

Et oui, cela m'aide vraiment personnellement.

Souvent, lorsque je lis du code, je regarde souvent le vert, ou comme, où sont les commentaires, quelle que soit la couleur des commentaires, dans le langage, je regarde souvent ceux-ci comme des marqueurs.

Donc je peux remplir le code et savoir exactement ce qui se passe où.

Donc c'est toujours une bonne pratique de laisser des commentaires en Python et de faire exactement la même chose.

Et laisser un commentaire ici, obtenir la variable matrice.

De l'utilisateur.

Je m'excuse si j'ai des fautes de frappe, je ne suis pas terriblement préoccupé par cela, obtenir obtenir la variable système de l'utilisateur, et puis cela va être obtenir la variable ennemi de l'utilisateur.

Et cela obtient la variable intérieure de l'utilisateur.

Et cela obtient toutes les professions.

variable de l'utilisateur, allait changer son profession.

Je suppose que cela n'a pas vraiment d'importance.

Cool, un peu redondant, mais cela aide toujours.

D'accord, donc je suis allé et je vous ai fait une faveur et j'ai pratiquement écrit le reste de la logique pour le reste des variables, car cela aurait probablement été un peu trop monotone si je l'avais enregistré à l'écran, mais nous pouvons le parcourir quand même.

Donc juste après la boucle for des professions, nous obtenons essentiellement la même variable.

Et nous faisons cela en écrivant à la console, donnez-moi un verbe héroïque lié au présent.

Encore une fois, ce n'est qu'un indice pour l'utilisateur.

Donc ils ont une idée de ce qu'ils remplacent.

Et puis nous allons enregistrer la valeur de chaîne qu'ils nous ont retournée dans la variable Save.

Et puis nous obtenons la variable unplugged, que nous faisons en écrivant à la console.

Maintenant, donnez-moi un verbe qui vous fait penser au soulagement au passé.

Encore un autre indice, vous pouvez voir à quel point cela aurait été monotone.

Et puis la valeur de chaîne qu'ils nous ont retournée avec le conseiller reline, nous allons l'enregistrer dans la variable unplugged.

Et puis après cela, nous devons obtenir nos adjectifs, il y en a deux.

Donc nous alertons d'abord l'utilisateur, disons, enfin, j'ai besoin de deux adjectifs dystopiques.

Et puis nous faisons une boucle for.

Et simplement, nous allons leur dire qu'ils remplissent actuellement un adjectif.

Et nous allons leur faire savoir quel numéro ils sont sur le nombre total.

Et puis nous allons enregistrer cela dans leurs variables d'adjectifs respectives, quelle que soit la chaîne qu'ils nous ont retournée.

Et puis enfin, nous devons simplement obtenir la variable fight.

Et nous disons simplement, hey, nous avons besoin d'un verbe sur la console.

Et puis la chaîne qu'ils nous ont retournée, nous allons l'enregistrer dans la variable fight.

Et c'est à peu près tout du côté Python des choses, c'est exactement la même chose, juste dans la syntaxe Python, vous savez, obtenir la même variable, obtenir la variable unplugged, obtenir les deux adjectifs à une boucle for, et puis obtenir la variable fight.

Et nous avons terminé.

Super travail les gars, notre application madlibs est à peu près terminée.

Je veux dire, il ne reste rien à faire.

Sauf qu'il y a une chose que je veux faire en Python.

Donc la fonction d'entrée est un peu différente de la fonction console dot read line, la fonction console read line va toujours à une nouvelle ligne, l'entrée ne le fait pas.

Donc avec cela, mettons cela un peu en forme.

Je vais faire avec toutes les entrées, point-virgule, et puis un espace.

Donc quelle que soit la question que nous leur avons posée, ils peuvent entrer cela juste après notre question.

Donc je vais faire cela à nouveau.

Je vais en fait supprimer le point d'interrogation car cela pourrait être un peu confus avec cette syntaxe.

Donc il y a un espace supplémentaire là.

Et puis entrée ici, je vais faire deux-points espace.

Ici, je vais faire deux-points espace.

Où ailleurs ici, je vais faire deux-points espace.

Et c'est l'espace d'entrée ici, il y a l'espace d'entrée.

Ici, espace entrée ici, espace, et boom.

D'accord, et cela va simplement avoir l'air beaucoup plus propre lorsque nous jouerons réellement au jeu dans le terminal.

Donc il ne reste plus qu'à le jouer et à le jouer.

Je vais exécuter C sharp en premier.

Je vais amener cela ici et il dit bienvenue utilisateur.

Jouons à un jeu de madlibs.

S'il vous plaît, partagez avec moi votre nom.

Mon nom est jabril Hello, jabril.

Êtes-vous prêt ? Qu'est-ce que quelque chose que vous voulez savoir plus sur ? Je veux en savoir plus sur la pizza.

Oh, vous voulez en savoir plus sur la pizza ? Ha.

D'accord, eh bien d'abord, dites-moi ce que vous savez déjà sur la pizza.

Qu'est-ce que maintenant ? Catégoriseriez-vous la pizza comme je dirais que la pizza est une tarte.

Donnez-moi un nom imposant à la tarte.

Hmm, peut-être un gâteau.

Maintenant, donnez-nous un nom relaxant.

Présent.

Je suppose que dormir est un nom relaxant et au présent.

D'accord, maintenant j'ai besoin de quatre professions relatives à la tarte.

Ooh, je ne sais pas.

Boulanger.

Cuisinier.

Chef.

Je ne sais pas.

Je ne sais pas.

Quel est le dernier ? Je vais simplement dire boucher.

Je ne sais pas.

Donnez-moi un héros.

Verbe lié au présent.

Voici un verbe lié au présent.

Voyons voir.

Sauver.

C'est tout ce à quoi je peux penser.

Je sais que c'est le mot réel, mais c'est tout ce à quoi je peux penser.

Maintenant, donnez-moi un verbe qui vous fait penser au soulagement.

Massage.

Massage au passé, massage.

Oui.

Est-ce un verbe ? Quelque chose à faire ? Je suppose que je ne sais pas.

Enfin, j'ai besoin de deux adjectifs dystopiques.

Je ne sais pas, des oiseaux, je suppose.

Et quel est un autre ? Je suis sale.

Et le verbe, un verbe est ce que vous faites, disons, euh, ce que vous faites, kick.

Voyons ce que nous avons ici.

La pizza est une tarte deux rangées.

Cette tarte est notre gâteau.

Mais quand vous dormez, vous regardez autour.

Que voyez-vous ? Boulanger, cuisinier, Chef, boucher, oops, je n'ai pas écouté les instructions, socialement pluriel, très esprits des gens que nous essayons de sauver.

Mais jusqu'à ce que nous le fassions, ces gens font encore partie de cette tarte.

Et cela en fait notre gâteau très profond.

Vous devez comprendre, la plupart de ces gens ne sont pas prêts à être massés.

Et beaucoup d'entre eux sont si brûlés, si désespérément sales sur la tarte qu'ils vont kick pour la protéger.

Art, art absolu.

Et maintenant jouons en Python.

Rapidement.

Je ne suis pas sûr comment j'ai manqué cela.

Mais nous devons mettre input en bas pour que la console reste ouverte.

Mais c'est un peu différent de jouer avec Python.

Allez en haut ici où se trouve le nom de votre fichier de projet, cliquez avec le bouton droit et puis faites révéler dans l'explorateur.

Et puis où que votre faute, votre fichier est simplement double-cliquez dessus et une console devrait apparaître.

Cela devrait avoir l'air à peu près exactement pareil, juste avec une légère différence de syntaxe Python que nous avons faite.

Et donc s'il vous plaît partagez avec moi votre nom ? Mon nom est quoi vais-je dire ? Mon nom est fajita.

Je suis cool cette fois.

Bonjour Vegito, êtes-vous prêt ? Qu'est-ce que quelque chose que vous voulez savoir plus sur ? Je veux en savoir plus sur Um, voyons voir.

Pas de pizza.

Oh, non plus sur les Skittles.

Skittles, hein ? D'accord, eh bien d'abord, dites-moi ce que vous savez sur les compétences ? Qu'est-ce que maintenant ? Une fois que vous avez catégorisé les Skittles, comme je dirais que c'est des bonbons.

Donnez-moi un nom imposant à bonbons.

Ooh, des légumes.

Maintenant, donnez-moi un nom relaxant au présent, un nom relaxant.

Personne, lieu ou chose ? C'est probablement incorrect, mais je comprends ce qu'il demande.

Relaxant maintenant.

Je ne sais pas.

Relaxant lui-même.

D'accord, donc maintenant j'ai besoin de quatre professionnels en rapport avec les bonbons.

Voyons voir.

Boulanger.

Maman.

Clerk.

Je ne sais pas.

Supposé être pluriel.

Je continue à oublier associé pluriel clerks.

Boulanger.

Je ne sais pas comment vous appelez cela, fabricant de bonbons, fabricants de bonbons.

Fabriquer ici, les propriétaires de l'usine de chocolat.

Voyons voir, donnez-moi un héros lié au verbe au présent.

Que font les héros ? Ils sauvent.

Ils combattent le crime.

Le verbe Combattre, combattre le crime.

combattre le crime.

Je ne sais pas.

Maintenant, donnez-moi un verbe qui vous fait penser au soulagement.

codage.

C'est ce que vous faites au passé, codé.

Enfin, j'ai besoin de deux adjectifs dystopiques.

Faisons dystopique, faisons vide, je suppose.

Et faisons sombre et un verbe, un verbe.

Glisser.

Voyons ce que nous avons ici.

Skittles est un bonbon fajita ? Ce bonbon est nos légumes.

Mais quand vous êtes en train de vous détendre, vous regardez autour de vous quand vous voyez des boulangers, des commis, des fabricants de bonbons, des propriétaires d'usines de chocolat, les esprits mêmes des gens que nous essayons de combattre le crime.

Mais jusqu'à ce que nous le fassions, ces gens font encore partie de ce bonbon.

Et cela en fait plus de légumes très profonds.

C'est si profond.

Vous devez comprendre, la plupart de ces gens ne sont pas prêts à être codés.

Et beaucoup d'entre eux sont si vides.

Si désespérément sombres sur le bonbon qu'ils vont glisser pour le protéger.

Wow.

Wow.

Donc c'est de la poésie.

Et voilà, les gars, félicitations pour la création de votre tout premier programme.

Vous l'avez fait.

Félicitations à tous.

Croyez-le ou non, vous venez d'écrire un programme réel et utilisable, vous pouvez aller maintenant et jouer à cela avec vos amis et vos proches et les impressionner avec vos nouvelles compétences.

Mais si vous êtes encore perdu, vous devriez vous sentir vraiment chanceux.

Parce que cette vidéo fait partie d'un cours de programmation que j'ai mis en place pour vous enseigner tout ce que vous devez savoir pour commencer à programmer.

Et je vous promets qu'à la fin de celui-ci, cette application sera très facile à comprendre même sans mon aide.

J'envie toutes les connaissances que vous allez apprendre.

Donc peut-être qu'il y a certaines choses que vous avez comprises et d'autres qui vous ont confus.

Eh bien, j'ai conçu ce cours pour que vous n'ayez à prendre que les leçons que vous voulez prendre, aucun cours précédent n'est requis pour créer votre propre programme.

Alors, qu'attendez-vous ? Maintenant, si vous voulez être un bon programmeur, il est très important que vous ayez une solide compréhension des types de données.

Alors parlons un peu d'eux et familiarisons-vous avec les bases.

Au niveau le plus fondamental, disons que vous avez des données qui sont stockées dans une variable.

Eh bien, ces données ont un certain type qui leur est associé.

Il existe un bon nombre de types de données différents, et ils ont tous des instructions et des règles différentes.

Et c'est ainsi que l'ordinateur sait ce qu'il peut et ne peut pas faire avec la variable.

Maintenant, il y a six types de données principaux qui sont partagés par la plupart des langages.

bool, qui signifie Booléen, nommé d'après le mathématicien du 19ème siècle George Boole dont le travail l'a popularisé, char, qui signifie caractère, string, qui signifie chaîne de caractères, int, qui signifie entier, float, qui signifie valeur à virgule flottante, et array, qui n'est pas réellement un type de données.

C'est une structure de données.

Mais par définition, c'est une série ordonnée ou un arrangement de types de données similaires.

Et non, il existe plus de types de données qui existent.

Mais si vous voulez en savoir plus sur ceux-ci en particulier, j'ai une leçon sur chacun d'eux, vérifiez le lien dans la description, car cette leçon, nous allons simplement les survoler brièvement.

Maintenant, encore une fois, chacun de ceux-ci a son propre ensemble unique de règles et d'instructions.

Par exemple, prenons le type de données entier, qui est un type de données pour les nombres entiers.

Disons que vous avez un entier qui est égal à 11.

Et vous voulez soustraire un de celui-ci, eh bien, vous écriviez cette opération, vous l'envoyez à l'ordinateur pour qu'il l'exécute.

Et devinez quoi, votre ordinateur va regarder cette opération, puis il va vérifier s'il a les instructions pour faire cette opération, puis il va dire, oui, je sais comment soustraire un entier d'un entier, l'ordinateur va alors soustraire un de 11 et puis vous renvoyer un 10.

tout est bien.

tout est correct.

Mais maintenant, regardons un type de données chaîne, qui est à nouveau une chaîne de caractères.

Si vous aviez la chaîne 11, et vous voulez soustraire l'entier un de la chaîne 11.

Eh bien, vous envoyez cette opération à votre ordinateur, votre ordinateur regarderait son opération, puis vérifierait s'il a des instructions sur la façon de faire cela ou non, puis il réaliserait que ce que vous lui avez envoyé n'a absolument aucun sens.

Il n'a aucune instruction sur la façon de soustraire des entiers de chaînes.

Ce n'est pas différent de dire à votre ordinateur de soustraire un de le mot bonjour.

Comment faites-vous cela ? Votre ordinateur va simplement vous renvoyer une erreur vous faisant savoir que l'opération que vous essayez de faire n'a aucun sens.

Ce qui est spécifiquement dans ce cas est une erreur de type.

Maintenant, faisons la même opération, mais au lieu de cela, faisons en sorte que les deux soient des chaînes.

Que pensez-vous qu'il va se passer ? Eh bien, nous obtenons un entier, mais comme une chaîne, peut-être obtiendrons-nous une autre erreur.

Eh bien, si vous avez à nouveau la chaîne 11, et vous envoyez l'opération à votre ordinateur pour soustraire la chaîne un de la chaîne 11, votre ordinateur regardera son opération, puis réalisera à nouveau qu'il n'a aucune instruction sur la façon de faire cela, renvoyant ainsi une erreur.

Mais vous trouverez cette partie suivante assez intéressante.

Si vous dites plutôt à votre ordinateur de prendre la chaîne 11 et d'ajouter la chaîne un à celle-ci, il regardera cette opération, puis vérifiera s'il a des instructions sur la façon de faire cela ou non.

Et puis dira, oui, en fait, je peux faire cela pour vous, puis il vous renverra une chaîne de 111 simplement parce que puisque la chaîne un et la chaîne 11 sont toutes deux des chaînes, tout ce qu'il a à faire est d'ajouter un un supplémentaire à la chaîne 11, juste pour exemple.

Et voilà pour les types de données.

C'est pourquoi comprendre les types de données est vraiment important, vous aurez beaucoup de mal à essayer d'écrire des programmes sans connaître la différence entre un nombre en tant qu'int, float ou string.

Consultez les leçons liées dans la description pour en savoir plus sur chaque type de données individuellement.

Mais en conclusion, rappelez-vous simplement que les types de données sont différents types de données avec différentes règles et instructions.

Et selon le type de données de votre variable, il y a certaines opérations que vous pouvez et ne pouvez pas faire avec elle, ce qui deviendra très important à saisir et à comprendre lorsque vous commencerez à les utiliser.

Alors parlons des booléens. Bool est l'abréviation de Booléen.

Si vous entendez bool ou Booléen, ils signifient la même chose.

Et il a été introduit par George Boole dans son livre L'analyse mathématique de la logique en 1847.

Mais qu'est-ce qu'un Booléen en termes de programmation ? Eh bien, un Booléen est un type de données qui ne peut être assigné qu'à l'une des deux valeurs différentes, soit une valeur vraie, soit une valeur fausse.

Et c'est tout, cela ne devient pas plus complexe que cela.

Et ce qui pourrait vous surprendre, c'est que les booléens sont le bloc de construction le plus fondamental pour la programmation, la plupart de votre code se contentera simplement de vérifier si quelque chose est vrai ou non.

Et la complexité est ajoutée en combinant un tas de volumes.

Mais nous y viendrons dans un instant.

Mais pour l'instant, plongeons dans le vif du sujet sur la manière d'utiliser les volumes.

Et nous allons le faire en utilisant deux langages différents.

Parce que je pense que cela peut être vraiment utile pour vous d'apprendre comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows, ou si vous voulez créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console en C sharp ou en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc la première chose que je veux aborder aujourd'hui est simplement la syntaxe de base des booléens.

Donc la première chose que je vais faire est simplement supprimer ces deux lignes, je n'en ai pas besoin, elles viennent de série avec chaque nouveau projet C sharp.

Et puis je vais définir un type de données booléen, bool, et puis je vais créer une variable appelée pizza time et lui assigner vrai.

Maintenant, la première chose que vous devez savoir sur les booléens est qu'ils n'ont que deux états, ils peuvent être vrais, ou ils peuvent être faux.

C'est à peu près la seule flexibilité qu'un booléen a lorsqu'il s'agit de l'assigner.

Mais en Python, les booléens ont juste un peu plus de flexibilité.

Donc je vais créer une nouvelle variable, et nous l'appellerons pizza time, bien sûr, je vais lui assigner une valeur vraie.

Et maintenant il sait que c'est un booléen, mais je peux aussi lui assigner une valeur fausse.

Ou je peux aussi dire, assigner une valeur de un à cela, ce qui est égal à vrai.

Et enfin, je peux assigner une valeur de zéro à cela, et cela est égal à faux.

Et juste pour vous le prouver, je vais vous montrer tous les différents cas.

Donc nous allons faire vrai ici.

Et puis pour le vérifier, nous avons besoin d'une instruction if.

Donc je vais dire si pizza time, alors nous devons imprimer pizza, ou une chaîne pizza.

Comme cela, je vais appuyer sur le bouton de lecture et vous verrez qu'il imprime pizza.

Ensuite, je vais changer la valeur fausse, et il devrait imprimer rien.

Si nous appuyons sur le bouton de lecture.

Vous ne voyez rien imprimé, comme nous l'avions prévu.

Et maintenant je vais changer cela pour qu'il ait une valeur de un et appuyer sur le bouton de lecture.

Vous verrez que nous obtenons à nouveau pizza, c'est assez bien.

Et enfin, je vais simplement dire pizza time est égal à zéro, l'enregistrer, appuyer sur le bouton de lecture et vous voyez qu'il n'imprime rien.

Donc qu'est-ce qui se passe ici parce que clairement la variable pizza time est un entier.

Et nous disons si zéro, alors imprimer pizza time.

Cela n'a aucun sens, n'est-ce pas.

Et c'est l'un des avantages de Python étant un langage interprété, il vous permet de passer des entiers dans une instruction conditionnelle.

Et si c'est zéro, alors il va convertir cela en une valeur fausse.

Mais si c'est un, il va convertir cela en une valeur vraie.

En fait, toute valeur numérique qui n'est pas zéro, et qui est utilisée comme instruction conditionnelle, retournera une valeur vraie.

Donc Pete's time est égal à neuf, enregistrer, appuyer sur lecture, vous verrez qu'il imprime pizza, pizza time est égal à moins trois, appuyer sur enregistrer, appuyer sur lecture, imprime toujours pizza, et ceci n'est pas seulement limité aux entiers, vous pouvez aussi utiliser des flottants.

Donc si nous disons pizza time est égal à point 0000001, appuyer sur enregistrer, vous voyez ici pizza time est maintenant un flottant, nous appuyons sur lecture, et il imprimera toujours pizza.

Et ceci est unique à Python, nous ne pouvons même pas penser à faire cela en C sharp, si nous essayions même, nous obtenons toutes sortes d'erreurs.

Donc c'est juste une flexibilité supplémentaire que vous avez en utilisant le langage Python.

Donc maintenant je veux parler des nombreux, nombreux, nombreux opérateurs que les booléens ont, ce qui est juste un témoignage de la puissance de ces choses.

Mais commençons par l'opérateur d'égalité.

Maintenant, disons que vous voulez créer un système de connexion utilisateur, n'est-ce pas.

Donc je vais simplement créer quelques chaînes ici.

Je vais dire string, password type some su p T signifie password typed, je vais dire equals ABC 123.

Et puis faisons une autre chaîne de point-virgule, bien sûr, et puis faisons une autre chaîne.

Et ceci va être P A pour password actual.

Et nous allons dire equals, encore, ABC 123.

D'accord, donc disons que ceci est le mot de passe réel de l'utilisateur PA, ABC 123.

Et ce qu'ils ont tapé est ABC 123.

Donc comment pouvons-nous vérifier s'ils correspondent ? Eh bien, nous devons utiliser quelque chose qui s'appelle l'opérateur d'égalité égal.

Et l'opérateur d'égalité égal ressemble à ceci.

pt, equals PA.

Et c'est tout ce qu'il y a à faire.

Maintenant, je sais ce que vous pensez, cela semble vraiment confus.

Et je programme depuis environ 13 ans maintenant.

Et je suis d'accord avec vous.

Donc une chose que j'aime généralement faire avec mes booléens est, premièrement, j'aime mettre des parenthèses autour de ce qui est comme le booléen que je vérifie, cela le rend beaucoup plus facile à lire lorsque je scanne des lignes de code.

Mais pour vous expliquer ce qui se passe ici, encore une fois, equals equals, c'est deux equals dos à dos, c'est ce que nous appelons l'opérateur d'égalité égal, ne vous confondez pas avec un égal, un égal est simplement l'opérateur d'assignation, cela signifie que vous voulez assigner quelque chose à une variable, deux equals, encore une fois, vérifie si deux choses sont égales.

Donc si nous devions lire cette ligne complète, nous initialisons simplement une variable booléenne appelée pizza time.

Et nous assignons la valeur true ou false à celle-ci avec cette opération booléenne ici.

Et ce que cette opération booléenne fait simplement, c'est qu'elle vérifie si p t est égal à PA.

Si c'est le cas, alors pizza time sera égal à true.

Mais si ce n'est pas le cas, il va retourner un false et pizza time sera égal à false.

Je veux dire, assez simple, n'est-ce pas ? Nous avons simplement demandé si deux choses sont égales.

Si c'est le cas, alors donnez-nous un true, si ce n'est pas le cas, donnez-nous un false.

Et aussi simple que cela soit, si vous vous êtes déjà connecté à quelque chose auparavant, c'est à peu près tout ce qu'ils font avec peut-être quelques vérifications supplémentaires par-dessus.

D'accord, je pense que j'ai assez battu ce cheval.

Mais je continue à marteler cela car c'est vraiment important que vous compreniez cette étape.

Si vous comprenez ce qui se passe ici, alors je pense que beaucoup de programmation va être vraiment facile à comprendre pour vous, car c'est comme l'un des piliers de la programmation.

Continuons.

Juste pour vous prouver que cela fonctionne comme je le dis, nous allons descendre ici et faire un console dot write line, juste pour imprimer cela à la console, pizza time.

Et puis nous avons aussi besoin d'un console dot read key.

Cela fait simplement en sorte que le terminal ne se ferme pas immédiatement lorsque nous l'exécutons, appuyez sur le bouton de démarrage ici.

Et puis je vais amener le terminal à l'écran.

Et comme vous pouvez le voir, il retourne une valeur vraie.

Mais si nous en faisons un légèrement différent, si je transforme cela en un deux quatre, et que nous appuyons sur le bouton de démarrage, vous pouvez voir que ce qu'il retourne est une valeur fausse.

Donc ce n'est pas le moment de la pizza car ils ne correspondent pas, ils ne sont pas égaux.

Et maintenant en Python, je vais simplement recréer rapidement le même scénario.

C'est le temps égal, eh bien, nous avons besoin de quelque chose pour cela, nous avons besoin de p t égal à A b, c 123 p p A égal égal à une chaîne, ABC 123.

Et puis pizza time égal à P t égal à P oops, p a, comme cela, allez-y, ajoutez le prince, faisons imprimer pizza time ici.

Et puis je vais appuyer sur le bouton de lecture et retourner à la valeur True, parfait.

Et bien sûr, je peux en faire un légèrement différent, puis appuyer sur le bouton de lecture et retourner à une valeur fausse.

Maintenant, j'espère vraiment que tout cela avait du sens, car si c'était le cas, tout à partir de ce point va être vraiment facile à comprendre.

Mais ensuite, passons à notre prochain opérateur, qui est l'opérateur d'inégalité.

Et comment fonctionne l'opérateur d'inégalité, disons que vous voulez vérifier un mot grossier, par exemple ? Donc nous allons changer pa pour être un mot grossier, n'est-ce pas.

Et donc au lieu de vérifier s'ils sont les mêmes, vous allez vérifier s'ils ne sont pas les mêmes, et non est indiqué par un point d'exclamation.

Maintenant, ce que cela dit, c'est que s'ils ne sont pas égaux, alors je veux que vous retourniez une valeur vraie.

Cependant, s'ils sont égaux, alors je veux que vous retourniez une valeur fausse, cela inverse essentiellement l'opération booléenne, ce qui est à nouveau ce que nous voulons dans ce scénario, car nous essayons de filtrer le mot grossier, si ce que vous avez tapé est un mot grossier, alors ce n'est pas le moment de la pizza.

Et juste pour vous prouver que cela retournera vrai parce qu'ils ne sont pas égaux, je vais simplement appuyer sur le bouton de lecture ici, et puis amener la fenêtre de la console à l'écran, vous pouvez voir qu'elle retourne une valeur vraie.

Donc c'est à peu près tout ce que vous devez savoir sur les opérateurs d'égalité.

Ensuite, passons à l'opérateur relationnel, en commençant par l'opérateur supérieur à.

Donc imaginez que vous avez un système de connexion, et vous voulez limiter le nombre de fois qu'un utilisateur peut se connecter, eh bien, une chose que vous pouvez faire est d'utiliser l'un des opérateurs relationnels, commençons simplement par un supérieur à.

Donc premièrement, ignorons ces deux variables pour l'instant et créons-en de nouvelles, nous allons faire un entier, je vais l'appeler a log attempts, equals, disons qu'il est trois.

Et puis faisons un autre entier et appelons-le log max equals cinq, par exemple, n'est-ce pas, ce que nous pouvons faire est de descendre à notre booléen pizza time, et nous pouvons remplacer cela par log Max est supérieur à log attempts.

Et ce que cela fait, c'est qu'il vérifie essentiellement si log Max est supérieur à log attempt.

Et comme log Max est cinq et log 10 plus trois, cela va retourner une valeur vraie pour notre variable booléenne pizza time.

Et juste pour vous prouver que cela est correct, je vais appuyer sur le bouton de démarrage, amener la console où vous pouvez voir que nous avons une valeur vraie.

Donc c'est l'opérateur supérieur à, nous pourrions aussi utiliser l'opérateur inférieur à, qui va vérifier si log Max est inférieur à log attempts, retourner une valeur vraie si c'est vrai ou une valeur fausse si c'est faux.

Mais il y a aussi un opérateur supérieur ou égal à, qui vérifie simplement si c'est supérieur ou égal à log attempts.

Et enfin, bien sûr, il y a l'opérateur inférieur ou égal à qui vérifiera si log Max est inférieur ou égal à log attempt.

Et en Python, ces opérateurs ne changent pas du tout, je vais simplement me mettre à jour, je vais faire log attempt equals trois et log max equals cinq et puis descendre à notre pizza time et faire log Max est supérieur à log attempt.

Et puis je vais l'exécuter juste pour prouver que cela fonctionne de la même manière.

Et voilà.

Et les derniers opérateurs que je veux aborder sont les opérateurs and et or.

Donc ici, vous pouvez vraiment voir la puissance des booléens être démontrée.

D'accord, donc ramenons notre ancien scénario.

Donc nous allons changer cela en ABC 1234, passé réel, et puis notre passé tapé est aussi ABC 123.

Et remplaçons cette opération booléenne par P t equals equals, c'est notre opérateur d'égalité égal, equals P a.

Donc que se passe-t-il si vous voulez vérifier si le mot de passe correspond et qu'ils sont en dessous d'un certain nombre de tentatives de connexion ? Eh bien, nous pouvons utiliser notre opérateur and et en C sharp, cela se fait comme ceci, vous tapez simplement l'esperluette, et puis une autre esperluette.

Et c'est l'opérateur and.

Et puis après cela, vous pouvez faire, vous pouvez écrire une autre opération booléenne.

Donc nous allons écrire log attempt est inférieur à log max.

Et donc ce que ce booléen complet demande, c'est simplement de savoir si notre mot de passe tapé et notre mot de passe réel se correspondent, et les deux esperluettes.

Et sommes-nous en dessous, est-ce que nos tentatives de connexion sont inférieures à notre log max.

Si vrai, si les deux sont vrais, alors retourner une valeur vraie pour un temps de pizza.

Mais si l'un d'eux est faux, peu importe lequel, alors retourner une valeur fausse pour notre temps de pizza.

Et juste pour vous prouver que c'est ainsi que cette opération est faite, je vais appuyer sur le bouton de démarrage en haut et amener la fenêtre de la console et l'ouvrir, vous pouvez voir que nous avons une valeur vraie ici.

Et il suffit qu'un de ceux-ci soit faux.

Et je vais simplement changer cela pour être passé, ou ABC 124.

Et puis nous appuyons sur enregistrer, et puis je vais appuyer sur le bouton de démarrage et amener la fenêtre de la console ici.

Et vous pouvez voir que nous avons un faux, même si l'un est vrai, nous demandons un n.

Et cela signifie qu'ils doivent tous les deux être vrais pour que le temps de pizza soit vrai.

Et juste une petite note rapide, j'aime généralement utiliser beaucoup de parenthèses, autant que possible.

Lorsque cela concerne les opérations booléennes comme celle-ci, j'aime le segment car cela rend beaucoup plus facile à lire lorsque je parcourt les lignes de code, les parenthèses comme moi savent, d'accord, cette opération booléenne ici, je vois cela et je sais qu'il y en a une autre, cela rend beaucoup plus facile pour moi, parfois je vais même faire comme une parenthèse globale sur toute l'opération booléenne.

Cela m'aide simplement à la lire beaucoup plus facilement.

Je ne sais pas si cela vous aide ou non.

Mais c'est un conseil que vous pourriez utiliser.

Et en Python, la syntaxe est juste un peu différente.

Donc je vais simplement me mettre à jour, je vais changer cela pour être passé 123 ou juste pas passé, est-ce que c'est ABC 123.

Désolé, ABC 123.

Et puis nous allons changer cela pour être P t equals equals p a, ou ne m'a pas dit depuis pour moi, et la façon dont nous faisons and en Python est que vous tapez littéralement le mot and, et log attempt est inférieur à log Max, boy, cela est devenu une fenêtre vraiment petite, peut-être devrais-je l'envoyer un peu.

Cool.

Donc maintenant je vais simplement prouver cela en appuyant sur le bouton de lecture.

Et vous pouvez voir que nous avons une valeur vraie.

Mais encore une fois, il suffit qu'une de ces opérations booléennes soit fausse.

Et ils, toute la chose devient fausse.

Et je vais prouver cela, je vais changer cela en quatre, appuyer sur le bouton de lecture, et nous avons une valeur fausse qui nous est retournée.

Mais que se passe-t-il si vous voulez être un développeur de médias sociaux miséricordieux, n'est-ce pas, où vous ne vous souciez pas s'ils se trompent sur l'un ou l'autre, tant que vous vous trompez sur l'un d'eux.

Tout d'abord, ne faites jamais cela.

Mais si vous voulez le faire, vous changeriez simplement l'opérateur AND en opérateur OR, et en C sharp, cela se fait en remplaçant les deux esperluettes.

Par deux barres verticales.

Je ne suis pas sûr de comment s'appellent ces caractères.

Mais vous les remplacez par deux barres verticales, c'est sur la même touche que la touche de la barre oblique inverse, regardez-la, je suppose qu'elle s'appelle le caractère de la barre verticale, je ne l'ai jamais su, mais peu importe, cela va maintenant vérifier si l'un d'eux est vrai, ce que nous savons, l'un d'eux est faux, parce que p t n'est pas égal à PA.

Mais le second est vrai parce que les tentatives de connexion sont inférieures au log max.

Et pour prouver que cela retournera vrai parce que l'un d'eux est vrai, je vais appuyer sur le bouton de démarrage et puis amener la fenêtre ici, vous pouvez voir que nous avons une valeur vraie qui nous est retournée.

Et en Python, l'opérateur OR est juste un peu différent, tout comme vous écrivez and pour l'opérateur and en Python, vous devez écrire or pour l'opérateur OR en Python.

Et maintenant en Python, l'opérateur OR est juste un peu différent, tout comme vous avez dû écrire and pour l'opérateur and, vous devez écrire or pour l'opérateur OR en Python.

Et bien sûr, juste pour prouver que cela fonctionne, je vais appuyer sur le bouton de lecture ici.

Et vous verrez que nous obtenons une valeur vraie qui nous est retournée.

Donc j'espère que vous pouvez voir ce qui rend les booléens si puissants dans le monde de la programmation.

Juste à partir de cet exemple simple, nous avons déjà un booléen qui vérifie les tentatives de connexion par rapport au mot de passe réel tapé.

Et puis nous pouvons prendre ce booléen et l'intégrer dans un autre booléen et continuer à ajouter de la complexité et de la complexité.

Les booléens sont incroyablement puissants et ils sont vraiment importants à comprendre.

Et oui, vous l'avez, les gars.

C'est à peu près tout ce dont vous avez besoin.

Pour commencer à programmer en ce qui concerne les booléens.

Donc les chaînes, les chaînes sont l'un des ingrédients les plus importants de presque tous les programmes que vous ferez jamais.

Pourquoi ? Eh bien, il est probable qu'à un moment donné dans le déploiement ou même pendant le développement, un humain devra interagir avec votre application.

Et avec cela, votre programme doit communiquer avec eux d'une manière ou d'une autre.

Et il est très probable que l'utilisation de chaînes sera la manière dont vous allez procéder, les chaînes au niveau le plus basique sont une série de caractères ensemble, d'où le nom chaîne, vous pouvez écrire n'importe quel mot dans n'importe quelle langue, vous pouvez écrire n'importe quel nombre, ou même n'importe quel code, argot clé, vous le nommez, rendant les chaînes incroyablement puissantes.

Et c'est à peu près tout ce que sont les chaînes, elles sont vraiment faciles à comprendre.

Et il y a quelques choses qui sont vraiment bonnes à savoir en les utilisant.

Donc regardons quelques exemples.

Maintenant, nous allons faire ces exemples en utilisant deux langages différents, car je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous allez faire du développement Windows, ou si vous voulez créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc la première chose que je veux aborder est la syntaxe de base des chaînes.

Donc premièrement, je vais supprimer ces lignes, elles viennent de série avec votre tout nouveau projet C sharp.

Et puis je vais initialiser une chaîne, nous l'appellerons a juste pour exemple.

Et puis si vous voulez assigner une valeur à une chaîne, vous devez utiliser des guillemets doubles.

Et puis vous pouvez taper n'importe quelle chaîne que vous voulez, et puis un point-virgule à la fin.

Et en ce qui concerne la syntaxe des chaînes en C sharp, c'est tout ce dont vous devez vous soucier, juste les guillemets doubles, assurez-vous qu'ils sont des guillemets doubles.

Maintenant en Python, nous avons juste un peu plus de liberté.

Donc je vais initialiser une chaîne ici.

Et puis je vais lui assigner bonjour.

Et comme vous pouvez le voir, j'utilise des guillemets doubles comme nous l'avons fait en C sharp, mais vous pouvez aussi initialiser une chaîne et assigner Bonjour, avec des guillemets simples aussi, les deux seront comptés comme une chaîne dans Python.

Et juste pour vous le prouver, je vais faire print a et puis B.

Nous y voilà.

Et voilà, bonjour, et Bonjour, les deux sont comptés comme des chaînes.

En fait, aujourd'hui, vous trouverez que cette liberté ici, les guillemets doubles et simples peuvent être assignés à une chaîne est assez agréable, Yossi.

Et donc la prochaine chose dont je veux parler est le fait que les chaînes sont des tableaux de caractères.

Et pour le démontrer en C sharp ici à gauche, nous allons simplement faire un console dot write line.

Et puis je vais faire un a et je vais utiliser les crochets et simplement mettre un zéro entre eux.

Cela, c'est un élément dans le tableau A.

Encore une fois, les chaînes sont un tableau de caractères.

Donc je demande simplement le zéroième élément du tableau de chaînes A, celui-ci est zéro, celui-ci est un, celui-ci est 234.

Les tableaux commencent toujours à zéro dans presque tous les langages de programmation.

Et donc maintenant juste pour le prouver, je vais appuyer sur le bouton de démarrage ici pour l'exécuter, j'oublie toujours de faire console dot read key, cela fait simplement en sorte que le terminal reste ouvert jusqu'à ce que nous appuyions sur une touche et appuyons sur start.

Et puis amenez cela ici et vous voyez que nous avons le zéroième élément dans le tableau A qui est à nouveau une chaîne de caractères, qui est H.

Et c'est assez flexible, nous pouvons mettre n'importe quel que nous voulons ici comme l'exercice.

Donc si nous voulons obtenir zéro, nous pouvons encore compter cela est zéro, et puis il est 1234.

Donc si nous mettons quatre ici, alors lorsque nous appuyons sur le bouton de démarrage, vous verrez qu'il imprime Oh, en fait, cette technique est celle que beaucoup de développeurs de jeux utilisent lorsqu'ils essaient de créer un système de chat qui apparaît un caractère à la fois, ils vont à peu près écrire tout le dialogue ici comme Bonjour, bienvenue.

Bienvenue dans ma boutique.

Et puis ils vont écrire une fonction qui va prendre une chaîne et puis va attraper chaque caractère et puis va en imprimer un avec une pause près comme une pause d'une seconde probablement beaucoup moins que cela, comme une pause d'un dixième de seconde, puis imprimer le suivant un dixième de seconde pause, imprimer le suivant, et ainsi de suite.

Juste un petit ajout ici, et en Python, je vais me débarrasser du B, nous allons simplement garder la convention des guillemets doubles pour correspondre avec C sharp, donné le B ici, et puis je vais en fait simplement faire un print.

Faisons zéro d'abord, appuyez sur le bouton de lecture, vous verrez que nous obtenons un H.

Et encore une fois, nous allons faire un quatre.

Donc nous pouvons obtenir le O, appuyez sur le bouton de lecture, et O, j'ai oublié de l'enregistrer, puis appuyez sur le bouton de lecture.

Et puis nous avons O, juste là, à peu près la même chose dans les deux langages.

Encore une fois, rappelez-vous simplement que toutes les chaînes sont juste un tableau de caractères.

La prochaine chose dont je veux parler est l'utilisation de l'opérateur d'addition avec les chaînes.

Et pour le démontrer ici à gauche, lorsque C sharp est en train de supprimer ce Bechtel, nous l'avions, supprimer cela de la droite, et je vais simplement descendre ici et faire un plus égal à oops, plus égal, c'est l'opérateur d'addition, ces deux ici, lorsque vous voyez plus égal, c'est un opérateur d'addition, plus égal et puis ajouter un caractère point d'exclamation à cela.

Et puis je vais l'imprimer, et vous verrez simplement qu'il va être Bonjour, et puis je vais simplement ajouter un petit point d'exclamation à la fin.

Démarrez cela, amenez-le ici, et voilà.

Maintenant, une chose cool à propos de ce processus est que parce que le fait que la chaîne a est juste un tableau de caractères, l'utilisation de l'opérateur d'addition prend simplement cette chaîne de caractères et ajoute ce caractère à la fin.

Cependant, la chose cool est que vous n'êtes pas limité à ajouter uniquement des caractères.

Encore une fois, les guillemets simples désignent un caractère, les guillemets doubles, et cela désigne une chaîne.

Donc nous pourrions ajouter à la fin de ce monde, par exemple.

Maintenant, bien sûr, nous devons changer ces guillemets simples ou doubles pour faire savoir à C sharp que ceci est maintenant une chaîne.

Et ce que cela va faire, c'est qu'il va maintenant ajouter chaque caractère dans ce tableau de caractères, ou cette chaîne va ajouter chaque caractère à cette chaîne.

Et juste pour le prouver, je vais appuyer sur start, et puis nous allons amener cela ici et voilà, bonjour le monde.

D'accord, maintenant en Python, je vais simplement restaurer cela à son état initial, puis faire un plus égal à un point d'exclamation.

Maintenant, bien sûr, cela va simplement prendre la chaîne Hello, la chaîne A, ajouter un point d'exclamation à celle-ci, et cela va l'imprimer avec le bouton de lecture pour confirmer, descendre.

Et c'est exactement ce que nous avons obtenu.

Maintenant, je veux à nouveau souligner que Python ne se soucie pas si vous utilisez des guillemets doubles ou simples pour les caractères ou les chaînes.

Donc contrairement à C sharp, nous pourrions simplement mettre world entre deux guillemets simples, et il va nous l'imprimer sans nous donner d'erreurs ou de problèmes.

C'est juste l'un des avantages d'utiliser un langage interprété.

Si vous voulez utiliser des guillemets simples ou doubles, c'est à peu près à vous de décider.

Mais juste pour garder tout cohérent, nous allons utiliser des guillemets doubles pour les chaînes aussi, pour cette leçon, pas avant de continuer, vous vous demandez peut-être, oh, eh bien, si nous pouvons faire l'opérateur d'addition, que se passe-t-il si nous utilisons comme un opérateur de multiplication ou de soustraction, un opérateur de division ? Eh bien, malheureusement, l'opérateur d'addition est le seul opérateur arithmétique que vous pouvez utiliser sur les chaînes.

Donc ne soyez pas trop heureux.

Maintenant, les caractères d'échappement sont des caractères réels, donc je ne vais pas trop m'attarder sur eux pour cette leçon.

Mais ils sont assez importants pour le chant des chaînes, car les chaînes sont un tableau de caractères.

Mais regardons-en quelques-uns rapidement.

Donc je vais simplement en ajouter quelques-uns ici.

Je vais faire une barre oblique inverse en.

Et puis je vais faire une barre oblique inverse T, je vais faire une barre oblique inverse, une apostrophe, une barre oblique inverse, des guillemets, et puis une barre oblique inverse, une barre oblique inverse.

Maintenant, ce sont, qu'est-ce que cela, cinq sont les caractères d'échappement les plus populaires.

Le premier, c'est une nouvelle ligne, c'est une tabulation.

C'est une apostrophe, ce sont des guillemets, et c'est une barre oblique inverse.

Et je vais simplement imprimer cela pour vous montrer ce qu'ils font, appuyer sur le bouton de démarrage, et puis amener cela ici.

Et donc vous avez une nouvelle ligne, qui est la barre oblique inverse, N, et puis une tabulation, qui est la barre oblique inverse, T.

Et puis vous avez l'apostrophe, qui est la barre oblique inverse, l'apostrophe, les guillemets, qui est la barre oblique inverse, les guillemets, puis vous avez la barre oblique inverse, qui est la barre oblique inverse, la barre oblique inverse.

Et ces gars sont pratiques car ils vous aident à faire certaines choses qui ne sont probablement pas intuitives lorsque vous commencez à coder, par exemple, comme comment appuyez-vous sur Entrée lorsque vous avez juste des chaînes ou comment utilisez-vous des guillemets si les chaînes nécessitent des guillemets pour s'initialiser, donc par exemple, je vais simplement me débarrasser de tout cela.

Juste vous donner un exemple rapide.

Je vais utiliser le caractère d'échappement, les guillemets à la fin et cela a l'air bien.

Tuer le caractère d'échappement, les guillemets au début.

Et cela va ressembler à bonjour entre guillemets, je vais appuyer sur le bouton de démarrage, et puis l'amener ici.

Et voilà, vous avez échappé à la syntaxe des chaînes en utilisant le caractère d'échappement.

Encore une fois, j'ai passé cela assez brièvement dans cette leçon.

Mais si vous voulez en savoir plus à ce sujet, consultez la leçon que j'ai faite sur les caractères, et j'y vais un peu plus en profondeur.

Donc je vais simplement restaurer cela à son état initial avant de passer à Python.

Maintenant en Python, la syntaxe pour les caractères d'échappement est exactement la même, je vais simplement me débarrasser de cette ligne.

Et puis simplement les ajouter comme nous l'avons fait en C sharp, barre oblique t barre oblique, apostrophe, barre oblique, guillemets, et puis barre oblique, barre oblique.

Assurez-vous d'ajouter ce guillemet.

Et oui, les voilà.

Une chose cool à propos de cela est en fait une addition de Visual Studio Code, il va changer la couleur des caractères d'échappement dans votre chaîne.

Donc c'est assez pratique.

Je vais simplement l'imprimer, nous devrions obtenir des résultats similaires.

Et les voilà.

D'accord, donc la prochaine chose que je veux aborder est les chaînes interpolées.

Maintenant, il n'y a aucune raison pour qu'un homme ait tant d'amour pour une syntaxe, mais j'adore les chaînes interpolées.

Et ici, vous les aimerez aussi.

Voici ce qui se passe.

D'accord, donc disons que nous voulions livrer un message, n'est-ce pas ? Je vais me débarrasser de tout cela et faire comme Bonjour, nom.

Comment allez-vous ? Bien.

Maintenant, disons que vous ne voulez pas avoir un nom réel ici.

Vous voulez avoir comme une entrée utilisateur, n'est-ce pas ? Donc créons une nouvelle chaîne pour ce nom.

Initialisons la chaîne, faisons nom égal à job Brill's.

Bien.

Donc comment vous feriez cela normalement, vous segmenteriez cette chaîne, vous feriez cela et vous supprimeriez cela ici et vous feriez plus, plus nom, et puis plus la chaîne à nouveau, bien, donc vous avez trois chaînes différentes, mais vous devez la casser pour mettre la variable de chaîne ici, et puis vous la recousez en ajoutant la dernière moitié de la chaîne.

Je veux dire, écoutez, cela fonctionne, cela fera le travail.

Mais quand vous devez écrire beaucoup de chaînes comme celle-ci, avec le temps, cela devient vraiment fatigant et facile à frustrer.

Mais c'est là que les chaînes interpolées entrent en jeu.

Tout d'abord, juste pour vous prouver que cela fonctionne, je vais simplement appuyer sur le bouton de démarrage.

Et puis nous allons amener l'écran ici et bada boom, cela fonctionne bien.

Mais avec les chaînes interpolées, nous n'avons plus à segmenter les chaînes, nous pouvons ramener cela ensemble comme une seule chaîne, et puis simplement venir au début de notre chaîne et ajouter le signe dollar.

Ce signe dollar indique que la chaîne est maintenant interpolée.

Et ce que cela vous permet de faire, c'est d'ajouter des crochets au milieu des chaînes, et à l'intérieur de ces crochets, vous pouvez ajouter des variables.

Et donc maintenant lorsque je l'imprime, regardez cela.

C'est si excitant.

Maintenant vous avez la même chose exacte, c'est juste que vous n'avez pas eu à casser votre chaîne, j'adore les chaînes interpolées.

Donc vous pouvez imaginer si vous avez comme un texte très long ou quelque chose comme cela, et vous avez beaucoup de variables que vous devez injecter dans ce texte, vous pouvez simplement transformer une chaîne en une chaîne interpolée, et simplement, vous savez, ajouter les crochets et vos variables partout.

Et cela fait gagner beaucoup de temps.

Et c'est juste magnifique.

J'adore cela.

Non, exécutez Python, c'est à peu près la même chose.

Je vais simplement configurer cela et dire bonjour nom.

Comment allez-vous ? Et la seule différence en Python, c'est qu'au lieu de $1 signe, vous allez utiliser un F pour les chaînes interpolées.

Et donc maintenant nous avons le créateur initialisateur de la variable nom.

Cela va être jabril Rose.

Et donc maintenant nous pouvons faire la même chose, utiliser les crochets et bada boom, appuyer sur lecture juste pour vous le prouver, et bonjour à Brill's Comment allez-vous, si beau, j'adore cela.

Et donc la dernière chose que je veux aborder est simplement quelques fonctions pratiques qui viennent avec le type de données chaîne.

Et pour démontrer ces fonctions pratiques, je vais me débarrasser de cette ligne, elle n'est plus nécessaire.

Et la première que je vais vous montrer est une fonction de mise en minuscules.

Donc nous pouvons simplement faire nom égal à nom dots to lower end C sharp to lowers la méthode et utiliser appeler cela ajouter le point-virgule.

Ensuite, nous descendons ici et nous imprimons simplement le nom.

Et ce qui va se passer, c'est qu'il va prendre le nom et ensuite il va le mettre en minuscules chaque caractère dans le nom.

Cela commence à prouver que nous amenons la fenêtre ici et vous voyez qu'il a transformé cela en toutes les lettres minuscules.

Cela peut être assez pratique lorsque, par exemple, vous créez une base de données d'utilisateurs ou quelque chose de ce genre et que vous ne voulez pas de doublons, alors peu importe le nom qu'ils passent dans votre base de données, vous le mettrez en minuscules à chaque fois et puis vous ferez simplement une correspondance contre ceux-ci.

C'est l'un des cas d'utilisation les plus courants pour cette fonction.

Mais c'est toujours bon à savoir au cas où vous en auriez besoin.

Ensuite, je veux vous montrer l'inverse, qui est une fonction de mise en majuscules.

Et au lieu de recommencer complètement, je vais simplement ajouter à notre journalisation de la console.

Donc sous le premier write line, je vais simplement faire réinitialiser le nom à égal à Brill's.

Et puis nous allons faire nom égal à nom.to to upper est la fonction en C sharp.

Et puis je vais copier cela Ctrl C Ctrl V.

Et maintenant il va d'abord imprimer à la console et tout en minuscules, et puis tout en majuscules et prouver cela, je vais appuyer sur le bouton de démarrage, et l'amener ici.

Et voilà.

Ensuite, une fonction vraiment, vraiment, vraiment utile qui vient avec le type de données chaîne est la fonction split.

Donc je vais réinitialiser le nom, je vais dire nom égal à je vais faire un peu différent cette fois-ci.

jabril est ce que la virgule au milieu parce que nous allons utiliser cela comme notre caractère que nous allons utiliser pour diviser la chaîne.

Donc avec cela, nous parce que nous divisons la chaîne en deux, nous devons avoir un tableau à la place.

Donc je vais dire, chaîne, et puis ajouter les crochets, laisser une note, laisser le C sharp savoir que c'est un tableau, et nous l'appellerons name deux égal à, et puis cela nous allons nommer point split, et puis nous allons passer dans le caractère, nous voulons utiliser le split comme va être la virgule.

Et puis nous pouvons simplement descendre ici et faire console dot write line, et name deux.

Et puis nous voulons faire le premier élément de ce tableau, qui est zéro.

Et c'est la copie et le collage.

Et puis nous allons imprimer le deuxième élément de tableau de ce tableau, qui est un, et prouver qu'il va diviser ce que je vais appuyer sur start ici.

Et puis je vais amener la fenêtre ici et vous voyez qu'il divise le nom en fonction de la virgule, jab, reals, magnifique.

Et la dernière fonction pratique que je veux vous montrer est la fonction contains.

Donc je vais simplement faire name égal à, j'aime le vaisseau spatial.

Je ne sais pas, j'aime le vaisseau spatial.

Et puis nous avons besoin d'un Booléen car contains retourne un Booléen.

Donc Boolean, nous allons simplement dire does, et cela est égal à name, dot contains, et puis nous devons passer une chaîne ici.

Et puis nous allons dire does this contain le mot the in it et puis simplement nous faisons console dot write line does.

Et puis juste pour prouver que cela retourne une valeur vraie, si elle retourne, si elle a le mot the, dans la chaîne, je vais appuyer sur start, et puis amener le vent ici.

Et vous voyez le dernier ici, il a retourné un vrai et oui, contains est juste une autre fonction vraiment puissante qui vient avec le type de données chaîne.

Très bon cas d'utilisation pour cela, et toujours bon à savoir.

Et en Python, c'est juste un peu différent de la façon dont ils le font en C sharp.

Donc nous avons jamais nommé ici, nous allons faire name égal à whoops, égal à name, dots.

Lower.

Huh.

Et nous allons faire print name ici.

Nous allons l'imprimer, appuyer sur le bouton de lecture, vous montrer qu'il met en minuscules le nom, comme nous l'attendons.

Et puis le suivant, je vais faire name encore égal à Brill's, et name égal à name dot upper fonction, et puis print name encore.

Je vais l'imprimer.

Et vous verrez que nous avons tout en minuscules et puis tout en majuscules.

Et maintenant cette prochaine fonction de chaîne va vraiment démontrer comment Python a un peu d'avance sur C sharp à cet égard.

Donc nous allons faire name égal à la même jab et puis rails.

Et puis ici, tout ce que nous avons à faire est name égal à name, dot split, nous le réassignons simplement et il va instantanément transformer cela en un tableau.

Si facile, le réassigner et puis tout ce que nous avons à faire est simplement d'imprimer name et de le prouver et d'appuyer sur le bouton de lecture.

Et voilà jab rails.

Oui, personnellement, c'est l'une de mes raisons préférées d'utiliser Python, c'est à cause de la facilité de faire des trucs.

Comme cela par rapport à C sharp où nous devions avoir notre chaîne name, nous devions initialiser un nouveau tableau de chaînes pour contenir le nouveau tableau de chaînes que nous allions faire et puis les imprimer un par un.

C'est juste comme trois lignes de code.

Facile, simple.

L'un des avantages que j'aime utiliser Python, et le dernier est la fonction contains.

Donc il ne fait pas name égal à j'aime le vaisseau spatial.

Et puis venir ici, et puis faire does initialiser un Booléen appelé does.

Et puis nous allons faire name dots.

Contains, je vais expliquer pourquoi cela a l'air bizarre dans la seconde, et puis le, et puis nous pouvons imprimer does, d'accord, et juste pour prouver que cela fonctionne, je peux appuyer sur play, et cela ne fonctionne pas.

Et c'est parce que, bien sûr, j'ai oublié de l'enregistrer.

Donc enregistrez-le et puis appuyez sur play, allez, en bas, et voilà, une valeur vraie, je veux vraiment m'arrêter une seconde ici et souligner que Python ne se soucie vraiment pas si vous utilisez des guillemets doubles ou simples.

Comme vous le voyez, nous utilisons des guillemets doubles ici pour le nom et des guillemets simples pour la chaîne qu'il contient.

Et cela retourne toujours vrai, il interprète simplement.

Maintenant, la raison pour laquelle cette partie a l'air si laide, c'est parce que c'est ce qu'on appelle une méthode wrapper, ou plutôt une méthode wrapper, et ce n'est pas important pour vous de comprendre ce terme pour le moment, dans vos premiers jours de programmation, mais essentiellement ce que c'est, Python ne veut pas que vous l'utilisiez de cette manière.

Comment ils préfèrent que vous l'utilisiez est si vous étiez à aller si et puis le dans name.

Donc si la chaîne le est un nom, alors nous allons faire imprimer does.

Python se targue vraiment de vous savoir, être un langage qui est assez proche de la façon dont nous utilisons réellement le langage en tant qu'êtres humains.

Donc c'est ainsi que je préfère que vous utilisiez cette méthode plutôt.

Et juste pour prouver cela, nous allons appuyer sur play, nous allons nous assurer qu'il est enregistré et appuyer sur play, et nous devrions voir deux vrais, ce que nous faisons et cela ne fait pas les gars, c'est à peu près tout ce dont vous avez besoin pour commencer avec la programmation en termes de chaînes.

Les types de données char sont assez faciles à comprendre.

Char est l'abréviation de caractère.

Et si vous savez lire et écrire dans n'importe quelle langue, alors vous savez ce qu'est un caractère.

La première lettre de votre nom, un caractère, une lettre que vous avez obtenue en cours de maths, un caractère, ce symbole de hashtag que vous surutilisez sur les réseaux sociaux, un caractère, un répertoire, tout chiffre unique, tout signe ou symbole, même certains glyphe comme le signe yin et yang ou un caractère unique.

Mais cela dépasse un peu le cadre de ce cours, gardez cela à l'esprit pour quand vous voudrez en savoir plus sur eux.

Mais pour l'instant, sachez simplement que les caractères sont très importants dans le monde de la programmation cette année, il y a beaucoup de chevauchement avec un type de données de chaîne, car une chaîne de caractères est ce qui constitue une chaîne.

En fait, dans les premiers jours des langages de programmation, les chaînes n'existaient même pas en tant que type de données, vous deviez plutôt créer un tableau de caractères, mais des chaînes comme le bureau téléchargements c colon barre oblique programme fichiers où toutes vos applications sont installées sont toutes une série de caractères que les ordinateurs utilisent quotidiennement pour rendre votre expérience informatique aussi fluide que possible.

Les caractères jouent un rôle essentiel pour que les ordinateurs puissent communiquer et relayer des informations à nous.

Et c'est à peu près tout ce qu'il y a à dire.

Maintenant, à partir de là, il n'y a pas vraiment grand-chose à couvrir.

Mais jetons un rapide coup d'œil à la façon dont nous utilisons les caractères dans deux langages différents.

Parce que je pense que cela peut être vraiment utile de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, c'est un langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows ou créer des jeux en utilisant un moteur populaire appelé Unity.

Et à droite, c'est le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

Donc premièrement, regardons un peu la syntaxe de base des caractères.

Donc ici à gauche en C sharp, je vais supprimer ces deux lignes car je n'en ai pas besoin.

Elles viennent de série avec votre projet de console vide.

Et maintenant regardons les cinq principaux types de données.

Tout d'abord, nous avons les booléens.

Et vous pouvez initialiser un booléen comme ceci, tapez simplement le mot bool.

Et puis n'importe quel nom pour votre variable.

Dans ce cas, nous allons simplement faire un a.

Et maintenant regardons le type de données suivant, qui est un char.

Donc vous faites cela en tapant le type de données, qui est à nouveau char, et le nom de votre variable.

Gardons l'ordre alphabétique ici, et je vais simplement l'appeler B.

Et maintenant le char a été initialisé, regardons le type de données suivant, qui est une chaîne.

Et nous faisons cela en tapant le type de données qui est une chaîne, et puis en gardant l'ordre alphabétique, nous allons simplement l'appeler un C, je pense que vous pouvez obtenir le motif à ce stade, nous allons initialiser le type de données suivant, qui est un int, tapez simplement le type de données et puis nommez la variable, nous allons garder, nous allons l'appeler un D garder la convention d'ordre.

Maintenant, le dernier type de données est un float, que nous appellerons un E.

Et voilà, l'initialisation de vos variables en C sharp est assez simple.

Vous tapez simplement le type de données que vous voulez initialiser, et puis vous nommez cette variable.

Et c'est pour tous les types de données.

Cependant, ce n'est pas la seule façon d'initialiser les variables, vous pouvez également assigner quelque chose à ces variables lorsque vous les initialisez.

Et pour assigner quelque chose aux variables, vous devez utiliser ce qu'on appelle l'opérateur d'assignation, qui ne doit pas vous effrayer, car c'est aussi simple que de taper égal, égal ici, ce signe est ce qu'on appelle l'opérateur d'assignation, il vous permet d'assigner quelque chose à une variable.

Et pour ce booléen, assignons-lui simplement vrai.

Donc passons en revue et assignons quelque chose à toutes nos variables.

Donc pour notre variable char, assignons la lettre J.

Et puis pour notre chaîne, assignons la chaîne bonbon à notre entier, assignons le nombre 13.

Et puis pour notre float, assignons un 7.77.

f, c'est un bon nombre.

Et voilà, c'est une autre façon d'initialiser une variable.

Mais attention, il est toujours de bonne pratique d'initialiser vos variables avec une assignation comme vrai j, par exemple, ce sont des assignations.

Et la raison en est que, comme dans l'exemple précédent, si vous les initialisez sans assignations, parfois elles peuvent retourner No.

Et si vous utilisez cette variable, vous pourriez rencontrer des cas limites étranges, et vous obtiendrez des erreurs.

Donc il est toujours de bonne pratique de simplement assigner une valeur à vos variables chaque fois que vous les initialisez.

Maintenant, pour initialiser les variables en Python, c'est beaucoup plus simple avec un léger bémol.

Donc Python se passe de l'idée de devoir définir vos variables.

Donc comme ici, en C sharp, nous devons définir que notre variable a est un type de données bool, définir que notre variable B est un type de données char, taper le type de données à côté est ce qu'on appelle le typage.

Et en Python, vous n'avez pas à faire cela, tout ce que nous devons faire à la place est simplement taper le nom de notre variable et lui assigner quelque chose.

Donc si nous voulons faire un booléen, nous assignons simplement une valeur vraie.

Le langage Python est un type de langage classé comme langage interprété.

Et ce que cela signifie, c'est que Python interprète le type de données de vos variables en fonction de ce que vous leur avez assigné.

Donc au fait que nous avons assigné une valeur vraie à la variable a, lorsque vous allez exécuter votre script Python, Python saura que la variable a a un type de données booléen, car nous avons assigné une valeur booléenne.

Et cela s'applique à toutes les variables.

Par exemple, si nous copions simplement ce que nous avons fait en C sharp, b equals j, et C equals candy, et puis d equals 13, et puis equals 7.77, Python interprétera toutes ces variables dans leur type de données approprié.

Et il y a des avantages à cela.

Et pour examiner cela, revenons à C sharp un instant.

Maintenant, au fait que vous devez explicitement définir le type de données de votre variable en C sharp, dès que vous initialisez cette variable, elle est bloquée avec ce type de données.

Par exemple, si je voulais descendre ici, et disons, je ne veux pas que b soit un char, en fait, je veux que ce soit un bool.

Eh bien, je ne pourrais pas faire bool b equals true.

Par exemple, il nous dira que cette variable a déjà été définie.

Donc nous ne pouvons pas recaster les types de données des variables.

Eh bien, pouvons-nous simplement réassigner la tab à un type de données différent ? Et la réponse est non, il vous dira que vous ne pouvez pas le convertir de son type de données d'origine au nouveau type de données, il dit simplement que cette variable a déjà un type de données.

Cependant, en Python, parce que c'est un langage interprété, nous pouvons faire ce que nous voulons avec nos variables.

Par exemple, nous pouvons descendre ici et dire, comme, je veux B égal à true et il ne vous donnera aucune erreur.

quoi que ce soit.

Et pour prouver cela, je vais simplement écrire une fonction print ici, print a, whoops, A, B, C, D, E, et vous verrez que nous obtiendrons deux vrais pour a et b.

Enregistrons et appuyons sur le bouton de lecture.

Et voilà.

Maintenant, bien que cette syntaxe sans type de données semble assez cool et tout, et ne vous méprenez pas, elle est vraiment cool.

C'est beaucoup de flexibilité, surtout si vous savez comment l'utiliser correctement.

Mais cela peut aussi causer quelques problèmes si vous n'êtes pas prudent.

Beaucoup des problèmes courants que je rencontrais dans les premiers jours de l'apprentissage de Python avec cette syntaxe sans type de données était que je n'étais jamais vraiment sûr du type de données de certaines variables.

Et j'essayais de les utiliser dans certains contextes, et cela me causait vraiment des problèmes.

Un autre problème est qu'il n'y a rien qui vous empêche de réassigner facilement une variable lorsque vous ne le vouliez pas, en C sharp, par exemple, ils vous diront si vous avez déjà une variable avec ce nom dans votre script.

Et il vous dira aussi que vous essayez de changer le type de données de cette variable, ce qui agit tous les deux comme une sorte de sécurité, si vous voulez, mais dans tous les cas, les deux ont leurs propres avantages et inconvénients, c'est à vous de décider lequel est le meilleur pour vous, en continuant, une chose que je pense être vraiment importante à aborder est l'assignation de vos variables après l'initialisation.

Donc en C sharp, vous n'avez à définir le type de données de votre variable qu'une seule fois.

En fait, vous ne pouvez définir le type de données de votre variable qu'une seule fois, pour le démontrer, je vais simplement me débarrasser de cette ligne car je n'en ai pas besoin.

Et essayons de réinitialiser notre variable a en tant que bool avec une valeur fausse.

Donc je vais définir notre type de données, je vais faire bool, et puis a equals false.

Et vous pouvez voir ici qu'il nous dit que cette variable a déjà été initialisée.

Essentiellement, c'est ce qu'il dit.

Et bien sûr, ce que vous assigner à cette variable doit être une valeur qui est acceptée par ce type de données.

Par exemple, Boolean n'accepte que vrai ou faux, par exemple, et bien sûr, en Python, parce que c'est un langage interprété, ce n'est pas un problème, nous pouvons simplement faire a equals false.

Et nous pourrions aussi faire b equals false si nous le voulions, C equals false.

Et pourquoi s'arrêter là, nous pouvons faire d equals false aussi.

Et nous pouvons même faire c equals false.

Parce que cela sera interprété lorsque nous exécuterons notre script, ce qui est maintenant j'ai appuyé sur le bouton de lecture en haut et vous verrez que nous avons tous faux et un 777.

Parce que je n'ai pas fait II ici, désolé, equals false, enregistrer, appuyer sur le bouton de lecture.

Et voilà, tous faux, cela a été interprété dès que vous exécutez le script.

Et donc c'est l'essentiel des variables, elles sont vraiment faciles à comprendre, il suffit de se rappeler que ce sont à peu près des conteneurs qui ont une sorte de données avec un type de données spécifique.

Donc enfin, je vais vous laisser avec un exemple simple.

Donc que vous puissiez avoir une meilleure idée de la façon dont les variables sont appliquées et comment elles sont utiles.

Donc imaginez que vous créez un jeu avec une bataille de boss.

Et ce boss ne peut prendre des dégâts que lorsqu'il est soit blessé, clignotant ou étourdi.

Il doit être dans un certain état.

Donc je vais simplement créer le scénario.

Supprimer toutes ces lignes, je n'en ai pas besoin, recommencer.

Tout d'abord, initialiser un int, je vais l'appeler enemy hp.

Par exemple, qui est égal à 50.

Et puis obtenir un Booléen, je vais l'appeler hurt.

Et disons qu'il est déjà blessé.

Donc hurt equals true.

Obtenir un autre Booléen, nous l'appellerons flashing, flashing equals true.

Et puis faisons ball.

dizzy, disons dizzy.

Et disons que ce n'est pas étourdi.

Ce n'est pas vraiment important.

Je vais simplement utiliser des instructions if pour créer ces états.

Si blessé, alors nous allons faire enemy HP moins equals quatre, par exemple.

Et puis si je sors de l'écran ici, si je suis quoi d'autre, flashing ? Oops.

Si c'est flashing, alors enemy HP moins equals quatre.

Et enfin, désolé, voir si quoi dizzy.

Alors aussi enemy HP moins equals quatre.

D'accord, donc juste pour expliquer ce qui se passe ici.

C'est juste comme je l'ai dit, nous avons, disons que vous créez un jeu avec une bataille de boss.

Et la seule façon que le boss puisse prendre des dégâts est s'il est soit blessé, clignotant ou étourdi.

Maintenant, rien de tout cela n'est vraiment important pour l'exemple que je voulais créer.

Mais cela donne au moins une idée d'un scénario.

Donc maintenant imaginez que vous avez fait quelques tests sur votre jeu et que vous avez découvert que quatre n'est pas assez de dégâts pour rendre le jeu amusant.

Vous avez besoin que ces dégâts soient plus élevés.

Eh bien, vous devriez revenir dans votre script et changer enemy HP moins equals, vous savez, disons sept enemy HP moins equals sept encore enemy HP moins equals sept.

Et disons que vous aviez cette référence de dégâts comme partout dans vos scripts, vous devez faire cela autant de fois que vous faites cette référence.

Et c'est un cas d'utilisation où les variables sont très utiles.

Donc au lieu d'avoir à faire cela, autant de fois que vous faites la référence dans votre script, vous pourriez simplement venir ici en haut de vos variables et simplement initialiser, disons, un nouvel entier, appelez-le dégâts et mettez-le à sept.

Et puis tout ce que vous avez à faire est de parcourir votre script, et simplement ajouter une référence à cet entier que vous venez d'initialiser.

Donc mon état stat, whoops, dégâts, dégâts et dégâts.

Donc maintenant disons que vous avez retesté votre jeu à nouveau, et vous êtes comme, Oh, attendez, sur une seconde pensée, sept est un peu trop élevé, j'ai besoin de le baisser un peu.

Eh bien, au lieu d'avoir à parcourir tous vos scripts, et de changer partout où vous faites une référence à HP moins dégâts, tout ce que vous avez à faire maintenant est de changer une variable à, vous savez, un nombre plus bas, disons six.

Et maintenant toutes ces références sont mises à jour.

Et donc maintenant que votre valeur de dégâts est une variable, vous avez maintenant beaucoup plus de pouvoir avec elle, vous pouvez descendre, par exemple, donc votre état étourdi et dire comme, juste pour exemple, s'il est étourdi, alors ce que je veux faire est dégâts égal à trois, par exemple, je veux le rendre beaucoup plus faible s'il est étourdi, et cela sera mis à jour chaque fois qu'il est en train de clignoter, et vous faites cette ligne, ou vous faites cette ligne.

Et bien sûr, je vais rapidement faire cet exemple en Python, c'est aller se débarrasser de tout, je n'en ai pas besoin.

Je vais faire enemy, HP enemy HP equals 50.

Et puis hertz equals true et flashing equals false et puis dizzy.

equals false.

J'ai fait cela à l'envers, c'est en fait vrai.

Et puis nous avons à faire si hertz, alors enemy, HP moins equals dégâts, je suppose que nous avons besoin de dégâts, allons-y pour l'exemple réel moins equals six.

Et puis si, si quoi est-ce que c'est flashing, alors enemy HP moins equals dégâts.

Et si dizzy, whoops, dizzy, alors dégâts equals trois.

Et pourquoi pas juste pour le plaisir, nous pouvons exécuter cela, je vais faire à la fin de tout cela print et PHP, juste voir ce que nous obtenons.

Je n'ai pas pré-calculé cela, nous obtenons 38.

Très bien.

Et puis si nous imprimons cela en C sharp, nous devrions obtenir le même résultat.

Je vais console dot write line.

Et puis qu'est-ce que c'est enemy hp.

Et puis oops, similar icon puis nous avons aussi besoin d'une console dot read line.

Donc la console ne se ferme pas sur nous lorsque nous l'exécutons.

Je vais appuyer sur le bouton de démarrage ici et puis amener la console ici et vous voyez que nous avons à nouveau 38 Très bien.

Et voilà.

Encore une fois, les variables sont assez faciles à comprendre conceptuellement, mais elles deviennent beaucoup plus puissantes et un peu plus complexes lorsque vous commencez à utiliser différentes structures de données comme les tableaux et autres.

Mais c'est à peu près tout ce dont vous avez besoin pour commencer avec la programmation en ce qui concerne les variables.

D'accord, donc une instruction if est un type d'instruction conditionnelle en programmation, ce qui signifie qu'elle vérifie si une certaine condition est remplie, une instruction if dans les termes les plus simples est si ceci alors cela, en fait, les instructions if en programmation sont en fait une abréviation pour les instructions If This Then That, l'une des plus grandes leçons de fait que la plupart des gens ne réalisent même pas avec les instructions if est que les instructions if sont essentiellement juste des booléens, elles s'activent si quelque chose est vrai, et ne s'activent pas si quelque chose est faux.

Maintenant, rappelez-vous cela car comprendre ce fait peut vous éviter beaucoup de maux de tête lorsque vous essayez de déboguer vos instructions if, vous devez simplement regarder votre instruction if et demander si cela retourne une valeur vraie ou fausse ? Et honnêtement, cela ne devient pas plus complexe que cela.

Si vous avez déjà posé une question IF, vous comprenez les instructions if, maintenant regardons comment écrire une instruction if avec du code.

Et nous allons le faire en utilisant deux langages différents car je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows ou créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc le labo d'aujourd'hui va être vraiment simple et vraiment facile, car une fois que je vous aurai montré le secret booléen avec les instructions if, vous allez le comprendre tout de suite, et vous n'aurez aucun problème avec les instructions if à l'avenir.

Donc comme je l'ai mentionné, le secret que la plupart des gens ne réalisent même pas avec les instructions if est qu'elles sont vraiment juste des booléens qui exécuteront un bloc de code si leur valeur est vraie.

Mais avant de nous plonger dans cela, regardons d'abord quelques différences de syntaxe entre C sharp et Python.

D'accord, en commençant par C sharp ici à gauche, je vais simplement me débarrasser de ces deux lignes, car je n'en ai pas besoin, elles viennent de série avec tout nouveau projet de console.

Et je vais écrire une instruction if.

Et pour faire cela en C sharp, la première chose que vous devez faire est simplement écrire le mot if, et puis vous voulez ajouter des parenthèses, et puis à l'intérieur de ces parenthèses, c'est là que vous voulez mettre votre booléen, donc je vais mettre true en C sharp, la valeur true est en minuscules.

Et puis en dessous, je vais simplement écrire une accolade de début.

Et puis dans l'accolade, c'est le bloc de code qui s'exécutera si notre instruction if est vraie.

Et voilà.

C'est ainsi que vous écrivez une instruction if en C sharp. À partir de là, vous pouvez écrire n'importe quelle commande que vous voulez ici.

Donc vous pouvez faire comme, je ne sais pas, console dot write line si vous voulez.

Et puis nous pouvons mettre Hi, par exemple, vous pouvez mettre ce que vous voulez.

Et tant que cela retourne vrai, ce booléen dans l'instruction if entre parenthèses est vrai, alors ce bloc de code sera exécuté.

Maintenant, avant de passer à Python, je veux simplement mentionner une chose vraiment importante.

Les instructions if en C sharp, elles doivent avoir les parenthèses, et le booléen doit aller à l'intérieur des parenthèses.

Si vous deviez supprimer cela, vous pouvez voir que nous obtiendrions une erreur de syntaxe car les instructions if en C sharp doivent englober la valeur booléenne dans des parenthèses.

Maintenant en Python, la façon dont l'instruction if fonctionne est exactement la même, cependant, la syntaxe est un peu différente.

Pour écrire une instruction if en Python, nous voulons d'abord écrire le mot if, et puis simplement mettre true.

Et la valeur true en Python est en majuscules.

Donc ne l'oubliez pas.

Et puis à la fin, nous devons la terminer avec le point-virgule, je veux simplement m'arrêter ici et faire cette distinction.

Bien que oui, Python n'utilise pas de parenthèses, il utilise à la place un deux-points.

Et ce deux-points est ce qui indique à Python que le booléen de votre instruction if a été complété.

Et donc en continuant pour faire le bloc de code de votre instruction if en Python, c'est un peu différent de la façon dont C sharp le fait, encore une fois, la façon dont nous indiquons un bloc de code en C sharp est que nous utilisons les deux accolades de début et nous mettons toutes nos commandes au milieu de ces deux accolades, toutes celles qui sont sous l'instruction if.

Mais en Python, au lieu de cela, nous devons aller à la nouvelle ligne.

Et nous utilisons des indentations au lieu d'accolades.

Donc prenons un exemple.

et ici nous pouvons simplement faire comme print.

Et puis Hi.

Et voilà.

Et donc la prochaine question naturelle à poser est, eh bien, comment ajouter plus de commandes à mon instruction if ? Eh bien, la réponse est assez facile.

En fait, tout ce qui est sous l'instruction if et est indenté sera compté dans le bloc de code de cette instruction if.

Donc par exemple, je vais simplement faire Ctrl C Ctrl V, juste pour vous donner un exemple.

Donc voici quatre fonctions print différentes qui sont toutes dans le bloc de code de cette instruction if, car elles sont toutes indentées et elles sont toutes sous cette instruction if.

Et donc la prochaine question naturelle à poser est probablement quelque chose comme, eh bien, comment sortir de ce bloc de code ? Je veux dire, je ne veux pas que tout mon programme dépende de cette instruction if.

Et la réponse est en Python, l'indentation prime sur tout.

Donc par exemple, si vous voulez sortir de ce bloc de code, tout ce que vous auriez à faire est simplement descendre et puis revenir à l'indentation régulière, et simplement faire print them out.

Par exemple.

Et juste pour vous prouver que cela fonctionne comme je le dis, je vais appuyer sur le bouton de lecture ici.

Et vous verrez que nous obtenons high high high amount.

Et puis je vais simplement définir cela sur false pour vous laisser voir que nous définissons cela sur false, ce bloc de code ne s'exécutera pas, vous n'avez pas été imprimé, j'appuie sur le bouton de lecture.

Et là, tout ce que nous avons, c'est I'm out.

Et une autre question que vous pourriez avoir est, eh bien, qu'en est-il des instructions if dans les instructions if comme l'imbrication des instructions if, je pense qu'en C sharp, il est assez évident comment vous faites cela, vous écriviez simplement un autre if dans un F et vous faisiez un autre bloc de code et vous pourriez faire un autre if si vous le voulez.

Et cela peut continuer ainsi jusqu'à ce que vous soyez fatigué.

Mais en Python, ce n'est probablement pas aussi évident, donc je vais vous montrer, vous faites simplement dans ce bloc de code qui est à nouveau indenté d'une indentation, vous faites simplement une autre instruction if.

True, par exemple, deux-points, et puis juste une autre indentation.

Et vous continuez simplement ce format, aussi longtemps que vous en avez besoin.

Et ici, nous allons faire une autre instruction if.

Hmm.

Print another high.

Et c'est tout ce qu'il y a à faire.

Et voici la toute dernière chose que je vais vous laisser.

Donc en C sharp, je vais simplement me débarrasser de tout cela pour que ce soit beaucoup moins confus.

En C sharp, lorsqu'un bloc de code est vide, vous pouvez le laisser vide si vous le souhaitez, vous n'avez pas d'erreurs, pas de problèmes.

C sharp ne se plaindra pas, vous serez bien.

Mais en Python, vous ne pouvez pas faire cela.

Donc si je supprime toutes ces lignes, et que nous avons simplement notre instruction if, et puis nous allons revenir à l'indentation après l'instruction.

Vous pouvez voir si nous allons à nos problèmes ici, vous voyez que nous avons une erreur pour cela.

Ce n'est pas autorisé, vous devez mettre au moins quelque chose là.

Donc vous savez, si vous voulez simplement écrire une instruction if, juste pour la remplir plus tard.

Par exemple, vous pouvez simplement mettre un if vous voulez, ce qui ne fait absolument rien.

Et oui, les voilà, les gars, ce sont les instructions if pour vous.

Je veux simplement que vous vous souveniez de notre petit secret, la condition que les instructions if vérifient, elles ne sont qu'un booléen, et encore une fois, le bloc de code s'exécutera si le booléen retourne vrai, et il ne s'exécutera pas si le booléen retourne faux.

Et donc avec cela, vous pouvez créer des booléens assez complexes et complexes et puis simplement mettre ce booléen ici dans la condition if, du programme le plus simple au programme le plus complexe.

C'est à peu près ainsi que fonctionne chaque programme sous le capot.

Si vous voulez apprendre à mieux utiliser les instructions if, je vous suggère fortement de consulter la leçon sur les booléens que j'ai faite, dans cette leçon, je vais plus en détail sur la façon d'utiliser les booléens dans certaines situations réelles et puis une fois que vous avez créé ce booléen, vous pouvez simplement l'intégrer dans une instruction if comme celle-ci.

Et oui, c'est à peu près tout ce que vous devez savoir pour commencer à programmer en ce qui concerne les instructions if.

Donc au fait que vous regardez une vidéo sur les instructions else, je vais supposer que vous savez ce qu'est une instruction if, ou en d'autres termes, une instruction If This Then That déguisée, mais les instructions if seules sont très limitées, par exemple, disons que vous construisez un robot pour aller chercher votre déjeuner, et vous lui dites si ils ont des spicy jackasses, Delia's donnez-moi en un, votre robot va chercher le déjeuner, ils n'ont pas de spicy jack case à deal us.

Et donc il retourne sans vous donner quoi que ce soit.

Maintenant, vous ne pouvez pas vous fâcher contre votre robot car il a fait exactement ce que vous lui avez ordonné de faire.

Très littéralement, les ordinateurs sont très littéraux, mais c'est là que l'instruction else, partenaire en crime de l'instruction if, entre en jeu.

Commençons par ce qu'est une instruction else ? Eh bien, dans la définition la plus simple possible, une instruction else est une instruction conditionnelle qui s'exécutera si la condition initiale n'est pas remplie, et elles sont très importantes en programmation.

En revenant à notre exemple, une instruction else serait l'équivalent de dire à votre robot si ils sont spicy jack case, et Delia's barmy one else give me anything, votre robot va encore chercher le déjeuner, ils n'ont pas de spicy jack case et dalias, cette condition initiale n'est pas remplie.

Et donc il vous obtient n'importe quoi.

Et honnêtement, les instructions else ne deviennent pas plus complexes que cela.

Elles sont des concepts assez simples à comprendre.

Maintenant, regardons comment utiliser correctement l'instruction else avec du code.

Et nous allons le faire en utilisant deux langages différents car je pense que cela peut être vraiment utile de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows ou créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc comme le labo de l'instruction if, ce labo else va être assez rapide et facile car il n'y a pas grand-chose à faire.

Donc comment utilisons-nous une instruction else ? Eh bien, la première chose importante à savoir est que les instructions else sont complètement inutiles sans une instruction if.

Elles sont 100% dépendantes d'une instruction if.

Pour démontrer cela à gauche en C sharp, je vais simplement me débarrasser de ces deux lignes car je n'en ai pas besoin.

Elles viennent de série avec chaque nouveau projet de console.

Et puis je vais simplement écrire else et puis nos blocs de code.

Mais vous pouvez voir que nous avons une erreur, mais syntaxiquement nous avons tout fait correctement en ce qui concerne la syntaxe.

Donc qu'avons-nous fait de mal ? Eh bien, encore une fois, les instructions else par elles-mêmes sont complètement inutiles.

Elles ont besoin d'une instruction if pour dépendre.

Donc pour corriger cela, je vais simplement venir au-dessus de l'instruction else et écrire if et puis faisons en fait false et puis nos blocs de code.

Et puis voilà, c'est corrigé.

Comme vous pouvez le voir, nous n'avons pas d'erreurs, nous n'avons pas de problèmes, tout est bien.

Donc laissez-moi vous expliquer cette relation que nous avons ici.

Donc vous avez votre instruction if ici, et ce bloc de code ne sera exécuté que si le booléen à l'intérieur des parenthèses est vrai, mais au fait qu'il est nous l'avons défini sur false, il va descendre et faire cette instruction else.

Donc en d'autres termes, si cette instruction est vraie, cela signifie que tout ce qui est à l'intérieur de ces parenthèses, si cela retourne vrai, alors exécutez ce bloc de code, sinon, exécutez ce bloc de code.

Aussi simple que cela.

Et pour démontrer cela, je vais écrire à la console.

Donc je veux utiliser console dot write line.

Et puis ici, je vais mettre un plan A, et puis je vais descendre ici dans les L OS, et puis écrire console dot write line.

Et je vais faire Plan B.

Et puis bien sûr, j'ai besoin d'ajouter une console dot read key, juste pour que le terminal ne se ferme pas sur nous jusqu'à ce que nous appuyions sur une touche.

Hmm.

Et puis juste à des fins de démonstration, je vais changer cela pour qu'il ait une valeur vraie, puis j'appuie sur le bouton de démarrage ici, et j'amène la fenêtre ici.

Et vous pouvez voir qu'il imprime un plan A, et encore une fois, très intuitif.

La raison en est que nous avons dit If true, ce qui signifie que tout ce qui est à l'intérieur des parenthèses est vrai, ce que nous avons dit est vrai, alors il va imprimer cela, et au fait que c'est vrai, il ignore tout ce qui suit.

Maintenant, disons que notre instruction if, le booléen retourne une valeur fausse à la place, eh bien, rappelez-vous la logique, cela vérifie si ce qui est dans ces parenthèses retourne vrai, alors exécutez ce code, sinon.

Si ce n'est pas le cas, alors exécutez ce code.

Et vous pouvez voir que Visual Studio, l'IDE nous donne un petit coup de pouce que cela ne sera pas atteignable, car il a un peu mis l'alpha, il est un peu plus sombre que le reste du code, ce qui est un joli petit coup de pouce de l'IDE et juste démontrer que cela fonctionne.

Laissez-moi appuyer sur le bouton de démarrage et amener la fenêtre de la console ici.

Et vous pouvez voir qu'il imprime le plan B, comme nous l'attendions.

Et maintenant en Python, l'instruction else fonctionne exactement de la même manière, cependant, bien sûr, la syntaxe est un peu différente.

Et tout comme l'instruction else en C sharp, nous ne pouvons pas simplement écrire une instruction else par elle-même en Python non plus.

Donc juste pour exemple, je vais mettre un zéro et puis appuyer sur le bouton de lecture.

Et vous pouvez voir qu'il retourne une erreur de syntaxe.

Et encore une fois, la raison en est que les instructions else ont besoin de dépendre d'une instruction if.

Et donc je vais simplement venir au-dessus de l'instruction O et puis écrire une instruction if, je vais dire si false.

Et puis je vais imprimer un, je vais simplement faire un oui.

Et puis vous pouvez voir que j'ai utilisé le mauvais false, c'est le false de C sharp, en Python, et true en Python sont tous deux en majuscules, cela me trompe tout le temps.

Mais nous avons corrigé notre erreur d'instruction else.

Et juste pour faire en sorte que cela ressemble exactement au programme que nous avons fait en C sharp, je vais écrire Plan A ici.

Et puis je vais écrire Plan B là.

Et encore une fois, vous pouvez utiliser des guillemets simples ou doubles pour Python, et cela n'a pas vraiment d'importance.

Mais pour le rendre plus propre, je vais utiliser des guillemets doubles pour les deux.

Et bien sûr, si je change cela en une valeur vraie, alors cela va nous donner le plan A, lorsque je clique sur play, Oh, j'ai oublié de faire print.

Plan A, et puis j'appuie sur play.

Et vous voyez que nous avons le Plan A et pas le Plan B.

Et bien sûr, si nous changeons cela en false, et puis nous enregistrons, et puis nous appuyons sur le bouton de lecture, vous verrez que nous avons le Plan B à la place.

Parce qu'encore une fois, il vérifie si cette instruction est vraie.

Faites ce bloc de code.

Sinon, faites ce bloc de code.

Simple comme cela.

Et la dernière chose que je veux vous laisser est que vous ne pouvez avoir qu'une seule instruction else par instruction if.

Par exemple, si vous descendez ici en C sharp et faites si cette instruction, exécutez ce bloc de code, sinon exécutez ce bloc de code, et puis nous avons enchaîné à une autre else.

Vous pouvez voir instantanément que nous avons une erreur de syntaxe.

Parce que même si vous pensez à la logique, cela n'a absolument aucun sens.

Vous dites si c'est vrai, alors exécutez ce code.

Ou sinon, exécutez simplement ce code et puis ou sinon exécutez ce code, cela n'a tout simplement aucun sens logique.

Donc c'est pourquoi vous ne pouvez pas le faire.

Et bien sûr en Python, nous ne pouvons pas faire deux instructions else dos à dos non plus, j'allais taper l's et puis print plan.

gosh dang it, Plan C, enregistrer, appuyer sur exécuter, voir que nous avons une erreur de syntaxe ici parce que cela n'a absolument aucun sens.

Et voilà.

Les instructions else sont assez pratiques lorsqu'elles sont associées à des instructions if et bien sûr vos instructions if sont juste des instructions if régulières avec des booléens dedans et font des opérations logiques vraiment puissantes.

Et il y a tout ce dont vous avez besoin pour commencer à programmer en ce qui concerne les instructions else.

D'accord, donc vous avez des instructions if et vous avez des instructions elif, mais vous avez aussi des instructions else if.

Donc en commençant par la première question évidente, qu'est-ce qu'une instruction else if, donc vous construisez un robot pour aller chercher votre déjeuner, et vous lui dites si ils ont des spicy jackasses do is give me one else give me anything, votre robot va chercher votre déjeuner, ils n'ont pas de spicy jack case, Delia's et sort de retourner avec vous obtenir un cheeseburger, mais vous réalisez que le restaurant ne sert pas de frites et maintenant vous souhaitez que vous aviez quelque chose de différent parce que qu'est-ce qu'un cheeseburger sans frites et soda ? Correct quelque chose comme cela.

Vous pouvez amener les instructions if autres partenaires dans le crime l'instruction else if.

Donc comment cela fonctionne-t-il ? En revenant à notre exemple, en utilisant l'instruction elif, vous pouvez dire à votre robot si ils sont spicy jackasses do is give me one else, si ils servent des frites, donnez-moi un cheeseburger, else give me anything.

Et avec ce programme, vous pouvez envoyer votre robot dans n'importe quel restaurant et être sûr qu'il vous obtiendra ce que vous voulez si les conditions sont réunies, car les instructions if sont à peu près juste des booléens, elles sont essentiellement comme des instructions if de secours.

Et c'est à peu près tout ce qu'il y a à une instruction else if.

Maintenant, regardons comment utiliser correctement les instructions elif avec du code.

Et nous allons le faire en utilisant deux langages différents.

Parce que je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous êtes dans le développement Windows ou si vous voulez créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code qui vous intéresse si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc comme le labo de l'instruction else, le labo de l'instruction elif va être assez rapide et facile.

Parce que encore une fois, il n'y a pas vraiment trop de choses à cela.

Donc comment utilisons-nous une instruction else if ? Eh bien, tout comme une instruction else, une instruction elif est complètement dépendante d'une instruction if sans une instruction if, une instruction elif est juste complètement inutile.

Et pour démontrer cela ici à gauche en C sharp, je vais simplement supprimer ces deux lignes car je n'en ai pas besoin, elles viennent de série avec tout nouveau projet de console.

Et je vais simplement écrire else.

Et puis if et puis true, et puis mon bloc de code.

Et comme vous pouvez le voir, nous avons une erreur car c'est une syntaxe invalide, encore une fois, les instructions elif sont complètement inutiles sans une instruction if.

Et en Python, c'est exactement la même chose, sauf que la syntaxe pour les instructions elif est un peu différente.

Donc au lieu d'écrire else if explicitement, vous écrivez simplement e L, i f, else if, c'est raccourci, et puis vous pouvez simplement mettre true ici, et puis votre deux-points et puis votre logique.

Mais même si j'avais mis une logique ici, disons que je vais mettre zéro, vous pouvez voir que nous avons une erreur, je vais appuyer sur play.

Et il nous dit que c'est une syntaxe invalide.

Encore une fois, l'instruction elif par elle-même est complètement inutile.

Et donc pour corriger cela, je vais simplement venir juste au-dessus de notre instruction elif et ajouter une instruction if à cela.

Donc si true, alors nous allons faire console dot write line.

Et puis nous allons dire Plan A, et puis je vais descendre ici et faire la même chose console dot write line, et puis plan spell Plan B, point-virgule, qui va faire la même chose en Python pour qu'ils soient au même endroit.

Voyons voir true, alors nous voulons faire print planning.

N'oubliez pas, l'indentation est vraiment importante.

Donc nous allons revenir ici.

Et alors si c'est vrai, ils veulent imprimer Plan B.

Et donc qu'est-ce que tout cela signifie ? Eh bien, cela dit si cette instruction est vraie, alors exécutez ce bloc de code.

Sinon.

Si cette instruction n'est pas vraie, mais si cette instruction est vraie, alors exécutez ce bloc de code.

Et en Python, cela fonctionne exactement de la même manière.

Donc nous avons si cette instruction est vraie, alors exécutez ce bloc de code ici.

Sinon si cette instruction n'est pas vraie, mais si cette instruction est vraie, alors exécutez ce bloc de code, une différence sur un point de sortie pour l'instruction elif, c'est une différence minimale.

Mais Python se targue d'être optimisé de toutes les manières possibles.

Et cela inclut le nombre de caractères que vous devez taper pour elif.

Cela n'en fait que quatre contre en C sharp, vous devez en taper sept, y compris l'espace.

Encore une fois, c'est minimal, mais les différences sont des différences.

Maintenant, voici où la vraie puissance des instructions elif entre en jeu.

Ce qui rend les instructions elif si utiles, c'est que vous pouvez ajouter autant d'instructions else if que vous le souhaitez, il n'y a pas de limites.

Donc si je viens ici, et que je prends cela, et que j'appuie sur copier, et puis coller et puis coller, et puis coller, vous pouvez voir que nous n'avons pas d'erreurs, il n'y a pas de problèmes, pas de questions, vous pouvez faire cela autant de fois que vous le souhaitez.

En Python, il n'y a pas de différence, vous pouvez prendre cela, copier et coller par exemple.

Et oops, et faire cela autant de fois que vous le souhaitez.

Ils vont faire attention à votre indentation, assurez-vous que votre indentation est toujours correcte.

Et avec cela, je pense qu'il est important de parler de l'ordre des opérations et de son importance.

Donc avec n'importe quel arbre d'instructions if, il vérifiera toujours le premier, si le premier n'est pas vrai, alors il passera au suivant.

Si le suivant n'est pas vrai, alors il passera au suivant, il continuera ainsi jusqu'à ce qu'il en trouve un qui est vrai.

Donc disons, par exemple, que celui-ci est vrai, alors il va exécuter ce bloc de code, et il va sortir, il ne touchera jamais à cette instruction elif là.

Et je peux vous le démontrer.

Je vais simplement changer cela en plan C, changer en plan D, changer en plan E.

Et disons que la vérification booléenne ici retourne un faux.

Et puis disons que celui-ci retourne aussi un faux, et celui-ci aussi ? Eh bien, ce que nous devrions attendre, c'est qu'il va vérifier celui-ci, obtenir un faux elif, vérifier cela, obtenir un faux L.

Donc vérifier cela, obtenir un faux, Elsa, vérifier cela et obtenir un vrai, et puis nous allons exécuter ce bloc de code et devrions imprimer le plan D.

Et juste pour vous le prouver, je vais appuyer sur le bouton de démarrage.

Et puis je vais amener oops, nous avons oublié d'ajouter une console.

Console dot read key pour que le terminal ne se ferme pas jusqu'à ce que nous appuyions sur un bouton.

Et puis je vais appuyer sur start et puis amener le terminal ici.

Et voilà, nous avons le plan D comme nous l'attendions.

Maintenant, bien sûr, cela fonctionne aussi en Python, et je peux vous le prouver, je vais simplement changer cela en C, D, E, ai-je fait une erreur, B, C, D, E est m a un sur ici, de toute façon, e f, et puis nous pouvons définir celui-ci sur false.

Et puis nous pouvons définir celui-ci sur false.

Et puis nous pouvons définir celui-ci sur false.

Et nous devrions nous attendre à nouveau à obtenir l'impression du plan D, appuyer sur le bouton de lecture et nous voyons un plan D.

Et la dernière information que je pense sera utile pour vous de savoir est comment incorporer l'instruction else réelle.

Donc disons que vous avez une sorte de variable, n'est-ce pas, vous avez comme une variable d'argent.

Et vous avez ces premières instructions comme si j'ai plus, je ne sais pas 1000 $, alors faites ce bloc de code.

Sinon.

Si j'ai plus, disons 750 $, alors exécutez ce bloc de code.

Si j'ai plus de 500, exécutez celui-ci, si j'ai plus de 250 par exemple, exécutez celui-ci.

Si j'ai plus de 100 alors exécutez celui-ci.

Et disons que vous avez à imprimer à la console quelque chose, n'est-ce pas ? Eh bien, si vous faites toutes ces vérifications, et que vous avez 0 $ et que vous n'imprimez jamais rien, mais c'est là que l'instruction else revient en jeu.

Tout ce que vous avez à faire à la toute fin de votre arbre d'instructions if est simplement ajouter else.

Je veux faire un console dot write line.

plan qu'est-ce que f Plan F et c'est tout ce que vous avez à faire.

Maintenant, notez que votre instruction else doit être à la fin de votre arbre d'instructions if.

Elle ne peut pas être ailleurs.

Mais à la toute fin.

Je veux dire, même si vous y réfléchissez logiquement, c'est la seule chose qui a du sens.

Et c'est à peu près tout ce qu'il y a à faire avec les instructions else if.

La dernière chose à noter est que les instructions else if ne sont pas différentes des instructions if comme celle-ci et celle-ci sont exactement la même chose.

La seule différence est qu'une instruction else if est dépendante d'une instruction if.

Vous vous souvenez de cette règle simple et vous n'aurez aucun problème à utiliser les instructions elif et c'est tout ce dont vous avez besoin pour commencer à programmer en ce qui concerne les instructions else if.

Les boucles for, il est temps d'apprendre tout sur les boucles for.

Maintenant, ce sont des choses très essentielles pour tout programmeur à connaître.

Donc qu'est-ce qu'une boucle for ? Eh bien, simplement dit, une boucle for est un raccourci pour exécuter un bloc de code un certain nombre de fois.

Donc disons que vous avez quatre numéros de téléphone, par exemple, et vous voulez ajouter un indicatif régional à chacun d'eux.

Eh bien, au lieu de coder cela quatre fois numéro de téléphone un plus égal indicatif régional, numéro de téléphone deux plus égal indicatif régional, numéro de téléphone trois plus égal indicatif régional, etc, etc, vous pouvez simplement utiliser une boucle for et écrire la logique une fois pour faire le même travail en moins de lignes de code.

Et les boucles for sont très puissantes à cet égard, car elles s'adaptent assez bien.

Donc pour les numéros de téléphone, ce n'est pas si mal, vous pouvez écrire numéro de téléphone 1234567, jusqu'à 4000 plus égal indicatif régional 4000 fois.

Donc regardons comment nous pouvons utiliser les boucles for pour faire des choses incroyables comme celle-ci.

Et nous allons le faire en utilisant deux langages différents car je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous êtes intéressé par le développement Windows ou si vous voulez créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc les boucles for, les boucles for sont des outils extrêmement utiles en programmation.

Donc plongeons-nous dans la syntaxe.

Maintenant, la syntaxe des boucles for en C sharp peut être un peu difficile à retenir.

Mais ce n'est pas terriblement difficile, vous n'avez à retenir que ces trois choses.

Mais d'abord, je vais supprimer ces deux lignes car je n'en ai pas besoin, elles viennent de série avec chaque nouveau projet de console en C sharp, donc nous pouvons simplement nous en débarrasser.

Et c'est ce que vous devez retenir, je vais l'écrire dans un commentaire pour que ce soit plus facile à retenir.

Donc un couple de barres obliques pour cela.

Et donc d'abord vous écrivez le mot for, et puis des parenthèses.

Et maintenant dans ces parenthèses, cette boucle for se fait en trois étapes.

Donc segmentons-la en ajoutant deux points-virgules.

Et cela, la première chose que vous devez mémoriser est d'initialiser votre variable.

Je vais simplement l'abréger en initialiser car nous allons rapidement manquer de place.

Et puis la deuxième chose que vous devez vous souvenir de faire est de définir votre condition.

Et la dernière chose que vous devez faire est de donner une commande.

Tant que vous vous souvenez de ces trois choses, les boucles for seront vraiment faciles à retenir.

Donc maintenant, passons par un exemple sur la façon d'initialiser une boucle for pour de vrai, je vais simplement descendre ici à la ligne suivante, et je vais écrire le mot for.

Et puis la première chose que je dois faire est d'initialiser une variable.

Maintenant, la variable la plus commune que la plupart des gens initialisent à cette étape est en fait une variable entière appelée I.

Et vous lui assignerez généralement zéro.

Mais vous pouvez lui assigner ce que vous voulez.

En fait, vous pouvez initialiser n'importe quelle variable de n'importe quel type de données que vous voulez ici, mais nous y reviendrons dans un instant.

Et donc la prochaine chose que nous devons ajouter ici est la condition, qui demande simplement, combien de fois voulons-nous que cette boucle for s'exécute.

Et cette condition ici dans cet espace attend en fait un booléen.

Et donc écrivons un booléen ici.

Disons que nous voulons l'exécuter tant que i est inférieur à 10.

Cela semble assez bien pour nous.

Et puis la dernière chose que nous devons ajouter est la commande et ce que la commande, nous instruisons simplement notre ordinateur de faire quelque chose.

Donc si nous initialisons un entier nommé I et que nous lui assignons zéro, et que nous disons que nous voulons que cette boucle for s'exécute tant que i est inférieur à 10.

Alors ici, nous pouvons dire, nous voulons i pour chaque fois que la boucle se termine, simplement ajouter un, en utilisant l'opérateur d'incrémentation, il ajoute simplement un à la variable à laquelle nous avons ajouté l'opérateur d'incrémentation.

Et puis enfin, nous descendons ici et ajoutons notre bloc de code pour la boucle for.

Et maintenant, chaque fois que cette boucle passe, elle va exécuter tout ce qui est dans les blocs de code, qui est à nouveau tout ce que nous ajoutons dans ces deux accolades, et puis à la fin, elle va simplement revenir en haut et puis quand elle revient en haut, elle va simplement vérifier notre condition ici, elle va demander si i est inférieur à 10 ? Si vrai, alors elle va sortir ici.

Elle ne va plus exécuter cette boucle et aller à la ligne qui est juste après la boucle for, mais si faux, alors elle va faire notre commande ici.

Et puis elle va à nouveau exécuter ce bloc de code et continuer ainsi jusqu'à ce que quand elle vérifie ici, et ceci est faux, alors à nouveau, elle va sortir et exécuter la ligne qui vient après la boucle for.

Et donc maintenant pour faire une boucle for en Python, c'est en fait très différent.

Python n'a pas cette syntaxe où vous initialisez une variable, et puis vous définissez une condition et puis vous donnez une commande.

C'est en fait, en fait, probablement beaucoup plus simple.

Mais la syntaxe pour cela est la suivante.

D'abord, vous voulez taper le mot for, et puis vous voulez taper I, pour i dans et puis vous devez définir une plage.

Et disons 10, nous allons utiliser le même 10.

Et puis vous écrivez votre deux-points ici pour commencer votre bloc de code.

Et puis ici, vous pouvez mettre les commandes que vous voulez.

Maintenant, c'est ainsi que vous initialisez une boucle for en C sharp et en Python.

Cependant, je veux revenir à l'initialisation C sharp rapidement et souligner quelque chose de vraiment intéressant.

Maintenant, je pense que dans la plupart des cas, pour les boucles for avec cette syntaxe, vous trouverez que la plupart des développeurs initialiseront d'abord un int appelé I, et puis l'assigneront à zéro et puis feront comme, si et si i est inférieur à un certain nombre, alors nous allons simplement utiliser l'opérateur d'incrémentation dessus.

Mais je veux libérer votre esprit tôt dans le développement, car ceci est en fait les règles pour une boucle for.

Mais pour comprendre où je vais, je pense que je dois d'abord vous montrer ce qui se passe avec les boucles for traditionnelles.

Donc je vais faire console dot write line ici.

Et je vais simplement imprimer la valeur de i.

Et puis bien sûr, ici, j'ai besoin d'écrire une console dot read key, pour que le terminal ne se ferme pas sur nous.

Dès que nous l'exécutons, j'ai oublié de faire console dot read key, cela fait simplement en sorte que le terminal reste ouvert jusqu'à ce que nous appuyions sur une touche et appuyons sur start.

Et puis amenez cela ici et vous voyez ce qui se passe.

Donc comme vous le voyez, I est initialisé et assigné à zéro, et puis nous incrémentons jusqu'à ce que I ne soit plus inférieur à 10.

Et puis nous sortons de la boucle for.

Assez simple.

Mais encore une fois, ici, il est dit initialiser.

Donc nous pouvons initialiser ce que nous voulons.

En fait, cela n'a pas besoin d'être un int, nous pouvons initialiser un float si vous voulez l'exécuter à nouveau.

Et vous pouvez voir que nous avons le même résultat exact.

Mais pourquoi s'arrêter là, au lieu d'utiliser l'opérateur d'incrémentation, nous pouvons faire plus égal à point cinq, nous voulons appuyer sur start juste pour montrer ce résultat et vous voyez que nous avons zéro puis nous incrémentons plus cinq et puis un autre plus cinq jusqu'à 9.5.

Et bien sûr, ce n'est pas tout, nous pouvons initialiser une chaîne si nous le voulons et l'assigner à être une chaîne vide pour l'instant.

Et maintenant nous avons à remplacer toutes les références de variable au tableau de noms dans le temp, car c'est ce qui rend cette fonction dépendante de la variable.

Donc je vais changer cela ici en temp.

Et puis je vais changer celui-ci aussi en temp.

Et puis je vais changer cela ici en temp.

Et en fait, parce que nous avons besoin d'une entrée avec le nom d'origine, nous n'avons pas vraiment besoin d'initialiser cela ici.

Donc je vais me débarrasser de cette ligne.

Et nous pouvons maintenant changer notre variable entière d'entrée en une variable de chaîne d'entrée et l'appeler temp.

Et donc la toute dernière chose que nous devons faire ici est que nous devons changer le type de données de notre fonction d'un void à une chaîne.

Et puis vous verrez que nous avons une erreur disant qu'elle ne retourne pas de valeur.

Lorsque vous définissez le type de données de vos fonctions, elles doivent retourner le même type de données dans le retour.

Donc nous allons descendre ici et ajouter, retourner et temp est une chaîne.

Donc nous allons simplement retourner le temp qui a été modifié avec sir au début.

Et donc maintenant parce que nous avons changé l'entrée en surnom de type de données entier à chaîne, vous pouvez voir que nous avons trois erreurs ici.

Pour les fois où nous l'avons appelé, ceux-ci sont actuellement des entiers, ils doivent être des chaînes, ce qui n'est pas un problème, nous pouvons simplement entrer le nom réel que nous voulons changer ici.

Donc bien sûr, le premier est le nom de l'élément zéro, et je suis paresseux.

Donc je vais copier et coller cela, coller et coller et changer cela en un et deux, qui correspond à nouveau ici.

Et si je sauvegarde simplement, et puis appuie sur le bouton de démarrage ici, et puis amène la console, vous pouvez voir qu'absolument rien n'a changé, la fonction fonctionne exactement de la même manière.

Cependant, la toute dernière chose que nous devons faire pour la rendre complètement fonctionnelle est, encore une fois, ici, elle imprime le temp, donc c'est seulement temporaire, nous obtenons une référence à cela, et puis nous le changeons et puis nous le retournons.

Mais vous pouvez voir ici que ce n'est pas assigné à quoi que ce soit.

Donc c'est la dernière chose que nous devons faire ici.

Mais avant de le faire, pour illustrer davantage mon propos, je vais simplement descendre ici et faire un console dot write line.

Et puis nous allons imprimer le nom zéro, et puis je vais copier coller quelques fois parce que je suis paresseux, changé en un et deux.

Et donc si je viens ici et appuie sur le bouton de démarrage et amène la console ici, vous pouvez voir que oui les noms de certains sont ajoutés pour les trois premiers qui est ce qui est à l'intérieur de la fonction de surnom réelle.

Mais les trois derniers qui ont été imprimés qui est à l'extérieur de la fonction de surnom est la vérité de base à nos noms de zéro élément nom de un élément et nom de deux éléments sont toujours les mêmes que nous l'avons initialisé.

Et donc pour corriger cela, nous devons simplement l'assigner à ce qui est retourné ici.

Donc nom de zéro égal surnom avec les entrées et nom de un égal surnom avec les entrées et nom de deux égal surnom avec les entrées, venez ici appuyez sur le bouton de démarrage, amenez la fenêtre ici et vous pouvez voir qu'ils ont été assignés.

Et juste pour vous guider à travers ce qui se passe ici.

Sur ces trois ici, nous allons assigner que le nom de l'élément zéro, le nom de l'élément un, le nom de l'élément deux sera égal au surnom avec certaines entrées.

Et donc nous entrons dans la fonction et nous passons les entrées.

temp, qui est le nom réel pour le moment et puis le surnom est un nom que nous voulons ajouter au début du nom et donc nous allons assigner le surnom au début du nom et puis nous allons l'imprimer et puis nous allons retourner temp.

Et donc parce que cette fonction entière ici, est retournée avec la valeur ce que temp est qui est à nouveau calculé ici, nous allons assigner cette valeur de retour au nom de l'élément zéro, nom de la valeur un et nom de l'élément deux.

Et maintenant enfin pour boucler la boucle.

Maintenant que nous avons cette fonction de surnom flexible indépendante de la variable, nous pouvons initialiser notre chaîne de boss ici, qui est égale à Helen, et simplement la réassigner en allant boss égale à surnom.

Et puis nous allons passer boss ici.

Et nous allons passer Mrs.

Et aussi simple que cela.

Et juste pour vous le prouver, je vais me débarrasser de ces trois lignes, le rendre un peu moins confus, appuyer sur le bouton de démarrage et amener la fenêtre ici.

Et comme vous pouvez le voir, nous avons Mr.

Johnny, Mrs.

Carla, Mr.

Zack, et à la toute fin, Mrs.

Helen.

Maintenant, c'est ainsi que vous écrivez du bon code.

Et donc nous sommes en Python, nous pouvons faire ce changement vraiment facilement aussi, nous pouvons simplement changer cela pour dire temp, et puis changer cela aussi pour dire temp, et puis changer celui-ci aussi pour dire temp.

Et bien sûr, nous voulons changer notre entrée pour être temp, oops, et puis descendre ici.

Et puis nous voulons assigner cela pour être le nom de zéro, et puis celui-ci pour être le nom de un.

Et puis celui-ci pour être le nom de deux.

Bien sûr, et puis nous devons assigner cela ici, le nom de zéro est égal au surnom avec ces entrées, et puis le nom de un est égal au surnom avec ces entrées, et puis je suis paresseux.

Donc je vais copier et coller le dernier, changer cela pour que le nom soit égal au surnom avec le dernier de ces entrées.

Et bien sûr, j'ai une erreur ici.

Il dit assigné à une fonction qui ne retourne pas, j'ai oublié de retourner ici.

Donc nous allons simplement faire retourner le bout.

Et puis bien sûr, nous ne pouvons pas oublier notre boss, Helen.

Donc nous pouvons l'initialiser en disant boss est égal au surnom.

Et parce que nous initialisons cela, nous passons simplement Helen.

Comme ça.

Et puis Mrs.

peut venir ici, appuyer sur le bouton de lecture.

Et voilà, Mr.

Johnny, Mrs.

Carla, Mr.

Zack et Mrs.

Helen, les fonctions sont simplement absolument incroyables.

J'adore ces choses.

Nous avons à peine effleuré la surface de ce qui est possible avec les fonctions ici.

Mais j'espère que vos jus créatifs coulent et que vous pensez à différentes façons dont vous pourriez appliquer une fonction.

Je l'ai dit avant.

Et je vais dire que, encore une fois, les fonctions sont probablement l'outil le plus puissant lorsqu'il s'agit de programmation.

En fait, si vous êtes familier avec toutes les recherches révolutionnaires qui se font dans le domaine de l'apprentissage automatique, eh bien, tout est alimenté par des fonctions.

Donc j'espère avoir été utile pour vous enthousiasmer à propos de certaines fonctions.

Mais c'est tout ce que vous devez savoir pour commencer à programmer en ce qui concerne les fonctions.

Maintenant, commenter peut être un facteur décisif pour votre succès en codage, surtout si vous travaillez en équipe sur un projet open source ou sur un projet que vous prévoyez de travailler à long terme, les commentaires, comme vous vous y attendez, sont un moyen de laisser des commentaires dans votre code dans un format lisible par l'homme, afin que vous sachiez ce qui se passe dans différentes parties de votre code.

À tout moment, parfois vous allez écrire un code extrêmement compliqué qui a du sens sur le moment.

Mais lorsque vous revenez à ce code des mois plus tard, ou que vous le donnez à quelqu'un d'autre pour qu'il puisse l'ajouter, il peut être vraiment difficile ou une perte de temps à essayer de comprendre le code.

Donc regardons comment utiliser les commentaires dans deux langages différents.

Parce que je pense que cela peut être vraiment utile pour vous de voir comment ils se comparent et contrastent.

Et en plus, vous apprendrez à peu près deux langages à la fois.

Donc à gauche, nous avons le langage C sharp utilisant l'IDE Visual Studio, qui devrait vous intéresser si vous voulez faire du développement Windows ou créer des jeux en utilisant un moteur de jeu populaire appelé Unity.

Et à droite, nous avons le langage Python trois utilisant l'IDE Visual Studio Code, qui devrait vous intéresser si vous voulez vous lancer dans la programmation générale ou la science des données.

D'accord, donc ici j'ai deux nouveaux projets de console.

Et si vous ne savez pas comment créer un nouveau projet de console, ni en C sharp ni en Python, ou les deux, assurez-vous de consulter la vidéo dans la description.

Elle s'appelle Comment installer un IDE.

Et à la fin de cette vidéo, je vous montrerai comment faire cela.

D'accord, donc la première chose que je veux aborder est le commentaire de ligne.

Donc en C sharp à gauche, je vais simplement supprimer ces deux lignes qui viennent de série avec chaque nouveau projet C sharp.

Et je vais commencer à créer un petit faux projet.

Donc je vais initialiser quelques flottants.

Nous allons appeler cela location x va faire un 2.345 F et puis nous allons faire un autre float location y et nous allons faire 123 point 456 D'accord.

Oh f Désolé.

D'accord, donc ces variables vont simplement agir comme des coordonnées de fate et lo exemple.

Donc je vais créer un booléen plus impliqué, je vais dire bool oops, in position, disons in pause equals, et faisons location x est supérieur à, je ne sais pas, disons 12.

Bien.

Et puis nous allons aussi vérifier si, si location, y est inférieur à 30, par exemple.

Mais alors en dehors de cela, nous allons aussi vérifier, ou si je suis sur le point de sortir de l'écran ici, je vais me déplacer, ou si location, x est supérieur à location, y, et puis nous allons mettre un point-virgule.

Et maintenant nous avons un booléen plus impliqué.

D'accord, donc ici, nous avons peut-être l'un des plus grands exemples de la façon dont le commentaire de ligne est assez utile, ou il peut être assez utile.

Plutôt, je vais aller au-dessus de notre booléen ici, et je vais simplement faire une barre oblique avant, une barre oblique avant, et cela, c'est le début de notre commentaire, et nous pouvons écrire ce que nous voulons.

Donc je vais faire de mon mieux pour expliquer ce que fait ce booléen.

Donc si location, x est supérieur, est supérieur à 12, et 12.

Et location y y est supérieur, non inférieur, inférieur à 30.

Ou si location x, x est supérieur à location, y, y, alors nous sommes en position.

Désolé, c'est un peu long, et cela ne correspond pas exactement au reste du code.

Mais c'est ainsi que vous écrivez un commentaire de ligne.

Et la façon dont cela fonctionne est que lorsque votre code est compilé, chaque fois que le compilateur voit une double barre oblique, il sait ignorer tout ce qui suit.

Donc il va simplement passer à la ligne suivante.

Et en Python, c'est beaucoup la même chose, je vais simplement faire loq oops, loq x equals one 2.345.

Et loq, y equals one 2.412 3.456.

Et puis je vais faire in pause equals, voyons voir loq x est supérieur à 12.

Et qu'est-ce que le loq ? Pourquoi est inférieur à 30 ? Hmm.

Ou nous avons loq déjà oublié x est supérieur à x est supérieur à loq Pourquoi ? Boy, c'était brutal.

Et pour ajouter notre commentaire, je vais simplement venir ici au-dessus de notre variable in position.

Et au lieu de faire une barre oblique avant, une barre oblique avant, cette forme de devise n'est pas acceptée en Python, je vais appuyer sur le signe de la livre ou le hashtag, peu importe comment vous l'appelez, et puis je vais écrire notre message.

Donc je ne vais pas l'écrire car cela va prendre une éternité encore, je vais le copier d'ici et puis le coller.

Et le voilà.

Commentaires, et commentaire.

Désolé, je viens de réaliser que la police Python devrait probablement être un peu plus grande.

Donc je vais simplement la rendre un peu plus grande.

Oui.

Donc c'est un cas d'utilisation pour le commentaire de ligne probablement l'un des cas d'utilisation les plus utiles pour le commentaire de ligne, cependant, vous pouvez faire autre chose aussi.

Donc disons que, vous savez, nous essayons ce booléen et il ne fonctionne tout simplement pas bien pour une raison quelconque, eh bien, nous pouvons faire un commentaire de ligne sur tout ce qui suit l'opérateur d'assignation, et puis simplement mettre, par exemple, égal à un, juste pour être sûr que ce booléen fonctionne, juste pour exemple, et puis en Python, c'est la même chose, utilisez le hashtag, tout ce qui suit est ignoré, et vous mettez simplement vrai oops, vrai.

Oops, non point-virgule.

Et oui, c'est un autre cas d'utilisation, qui peut être assez pratique aussi lors du débogage de votre code.

Et donc le dernier cas d'utilisation que je veux vous montrer avec le commentaire de ligne est disons que nous allons retourner ceux-ci à cette affectation.

Et disons que nous descendons ici.

Et puis nous ajoutons une instruction if.

Donc si in position, bien, nous voulons que quelque chose se passe.

Cependant, nous ne savons pas exactement ce que nous voulons qu'il se passe encore.

Nous avons une idée peut-être que nous ne savons pas comment le faire.

Peut-être que vous voulez que quelqu'un d'autre le fasse.

Eh bien, ce que nous pouvons faire ici est simplement ajouter un commentaire.

sur comme, ici, je veux afficher quelque chose, vous savez, une notification, je ne sais pas, je veux simplement afficher quelque chose ici.

Et vous pouvez laisser ce commentaire ici, peut-être revenir plus tard, peut-être le donner à un ami, peut-être faire des recherches et puis vous savez, apprendre comment le faire et puis l'implémenter.

Ce commentaire est juste un moyen facile pour vous de, vous savez, savoir quelle était votre intention en mettant cette instruction if là.

Et en Python, c'est vraiment similaire, mais un peu différent.

Donc disons que nous faisons notre instruction if, si in position, nous allons descendre ici, nous pouvons écrire notre commentaire, qui était, encore une fois, copier et coller, copier, coller.

Cependant, nous ne pouvons pas le laisser comme cela, vous voyez, si nous avions enregistré, nous aurions un problème, qui est, nous avons une erreur d'analyse, une erreur de syntaxe, plutôt.

Et la raison est, parce que si vous faites une instruction if, et puis vous indent, ce que vous devez faire, il n'y a rien quand il exécute une instruction if, il n'exécutera rien.

Et c'est une erreur de syntaxe en Python.

Donc nous pouvons simplement mettre, comme print, vous savez, zéro, par exemple, juste pour effacer cette erreur de syntaxe.

Et techniquement parlant, vous n'avez même pas à faire un print, par exemple, vous pouvez simplement faire comme des guillemets vides, oops, vous pouvez faire comme des guillemets vides.

Et cela fonctionnera de la même manière, mais il doit exécuter quelque chose dans l'indentation.

Parce que, encore une fois, cette ligne est ignorée.

D'accord, donc c'était le commentaire de ligne.

Ensuite, je veux parler du commentaire de bloc.

Donc pour démontrer, je vais me débarrasser de tout ce code que nous venons de faire.

Et puis oops, oui.

Et puis je vais, disons que vous créez une sorte d'algorithme complexe que vous comprenez à peu près, mais que vous ne comprenez pas vraiment.

Donc je vais simplement créer quelque chose, c'était juste une représentation pour un algorithme avancé, utilisez simplement votre imagination.

Faisons loq y, divisé par égal à quatre, bien ? Et puis nous devons le retourner ou quelque chose comme ça.

Donc nous allons faire loq new égal à loq y divisé par loq x.

Par exemple, oh, je dois l'initialiser, ce n'est pas Python floats.

Et puis enfin, retournons-le.

Faisons.

Faisons cela console.

Oops, console dot write line.

Bien ? ligne, location, new.

D'accord.

Donc disons que c'est un algorithme avancé, et vous venez de l'implémenter dans votre programme.

Mais tout à coup, comme tout est cassé, rien ne fonctionne plus.

Vous êtes comme, qu'est-ce qui se passe ? Ce n'est pas le comportement que j'attends, je sais que cela fonctionne, bien.

C'est évidemment, vous savez, très simple.

Mais peut-être que cette partie de l'algorithme ne fonctionne pas bien.

Maintenant, vous pourriez, vous savez, aller par et faire comme, vous savez, barre oblique avant, barre oblique avant, barre oblique avant quatre barre oblique.

Et si vous en avez un tas, faites cela ligne par ligne.

Mais une façon vraiment pratique est d'utiliser le commentaire de bloc, qui en C sharp est juste une barre oblique avant, et puis un astérisque.

Et l'après avoir fini en faisant l'inverse, donc un astérisque et puis une barre oblique avant, et c'est une façon que vous pouvez rapidement commenter un bloc entier de code.

Maintenant, une chose vraiment importante à noter sur le commentaire de bloc est que vous devez avoir un début, et vous devez avoir une fin.

Parce que si vous n'avez pas de fin, ce qui se passe ici, c'est qu'il commente tout ce qui suit, y compris les crochets.

Et si le crochet a un début, mais n'a pas de fin, vous allez avoir un tas d'erreurs.

Donc ils doivent tous avoir un début, et ils doivent tous avoir une fin et maintenant en Python, je vais simplement répliquer notre super algorithme avancé ici, je vais faire loq x fois égal à deux et puis loq y divisé par égal à quatre.

Et puis nous allons faire loq nu égal à loq y divisé par loq.

x, puis nous allons simplement l'imprimer parce que pourquoi pas loq new.

Et pour ajouter le commentaire de bloc en Python, c'est similaire, mais aussi très différent.

Et ce que je veux dire par là, c'est que vous voulez venir au-dessus ou si vous voulez faire votre bloc, commentaire et simplement faire trois guillemets simples.

Et encore une fois, il a besoin d'un début et il a besoin d'une fin.

Si vous n'avez pas de fin, vous allez avoir une erreur de syntaxe, parce qu'il a besoin d'un début et d'une fin pour la chaîne littérale à triple guillemet, alias le commentaire de bloc.

Maintenant, le tout dernier type de commentaire que je veux aborder est le commentaire de résumé.

Donc pour démontrer, je vais simplement me débarrasser de tout ce code, ce n'est plus nécessaire.

Et puis je vais simplement initialiser une variable float, l'appeler loq equals zéro, par exemple.

Ensuite, créons une petite fonction rapide, je vais sortir de notre fonction principale et puis faire static float.

Appelons-le ret, one.

Et puis, passons un float, et puis nous appellerons notre float a sum, pour le rendre facile.

Et puis ce que nous allons faire, c'est que nous allons retourner un, voyons voir un plus un.

C'est ce que nous allons retourner.

Et puis utilisons-le rapidement.

Donc nous allons faire loq equals rat one, et puis nous allons simplement passer lui-même.

Donc il va plus un à lui-même.

Et juste pour le prouver, nous allons faire console dot write line, même si ce n'est pas pour prouver cela, c'est vraiment à propos des commentaires, mais nous allons simplement le faire quand même.

Console dot read key.

Et puis je vais appuyer sur le bouton de lecture.

Et boom, nous y voilà.

Zéro plus un est égal à un.

Donc notre fonction fonctionne.

Mais disons que vous savez, c'est plus tard dans votre projet, et vous revenez au script pour mettre à niveau ou corriger quelque chose, vous voyez que Loki va à droite, qu'est-ce que cela fait, et vous descendez à la fonction read one.

Et disons que c'est beaucoup plus complexe, vous ne comprenez pas vraiment ce qui se passe.

Eh bien, vous pourriez perdre beaucoup de temps à essayer de comprendre ce que fait cette fonction.

Mais ce que SOT ce qui peut résoudre cela est en ajoutant un commentaire de résumé.

Donc ajouter des commentaires de résumé en C sharp est en fait très facile.

Tout ce que vous avez à faire est d'aller juste au-dessus de la fonction à laquelle vous voulez ajouter un résumé ou une méthode et de taper barre oblique, barre oblique, barre oblique, cela se complétera automatiquement si vous êtes dans Visual Studio, ce qui signifie simplement remplir ce que votre résumé est.

Donc je vais faire plus un à l'entrée.

Maintenant, si je passe sur le read one, vous verrez que maintenant il y a une petite description là.

Et il me dit exactement où cela ajoute un à l'entrée.

L'entrée est Loki.

Donc cela va être Loki plus un est ce qu'il va retourner.

Simple, facile, et au point.

Et ils ont aussi quelques autres variables que vous pouvez remplir, vous pouvez remplir comme ce que le paramètre A est, vous pouvez mettre ce que cela est pour, vous pouvez mettre ce que les retours, et dans le bon contexte, cela affichera ces informations pour vous aussi.

Et en Python, je vais simplement me débarrasser de tout et configurer notre scénario rapidement.

Donc loq equals zéro en faisant un do def read one, et puis nous avons besoin de notre entrée a.

Et puis voyons voir return, whoops, return a plus one.

Et puis nous faisons simplement loq equals qu'est-ce que le read one, et puis pass in Loki.

Et puis nous pouvons l'imprimer, et puis nous n'avons pas besoin d'une entrée.

Et juste pour prouver que cela fonctionne, je vais appuyer sur play ici et vous voyez que nous avons un.

Maintenant pour ajouter des commentaires de résumé aux méthodes et fonctions Python, tout ce que vous avez à faire est d'aller juste en dessous de la méthode ou de la fonction en Python, et puis de taper trois caractères de guillemet simple, et puis un autre.

Donc vous faites à peu près un commentaire de bloc.

Et puis vous tapez simplement ce que fait la fonction.

Je vais simplement pop copier cela parce que je suis paresseux.

Et puis je vais le coller ici.

Et donc maintenant si nous passons ici, il vous montre ce qu'il fait définition read one, il ajoute un à l'utilisateur, je suis désolé, à l'entrée.

Et puis nous pouvons ajouter plus si vous voulez comme a equals, vous savez, float, par exemple, juste plus d'informations pour l'utilisateur.

Et c'est à peu près tout ce qu'il y a à faire.

Et les voilà, les gars, c'est à peu près tout ce dont vous avez besoin pour commencer avec la programmation en termes de comédie.

Eh bien, toutes nos félicitations, vous avez complètement réussi le cours.

Maintenant, comment pensez-vous que vous vous en êtes sorti ? Si vous n'êtes vraiment pas sûr, vous devriez revenir à la section de votre premier programme, leçon quatre et le réessayer sur une difficulté différente.

Si vous êtes capable de compléter votre premier programme sur sa difficulté la plus élevée, alors vous savez, vous êtes officiellement prêt à aller dans le monde pour trouver vos propres problèmes à résoudre et coder vos propres idées avec votre nouvelle compétence.

Mais avant de vous laisser partir complètement, je veux simplement vous inspirer avec certaines des possibilités cool que vous pouvez prendre avec cette compétence à partir d'aujourd'hui avec plus de pratique, bien sûr, mais je veux simplement que vous pensiez à tout ce que vous faites ces jours-ci.

Pensez simplement au fait que presque tout ce avec quoi vous interagissez dans ce nouvel âge numérique est d'une certaine manière déterminé par le code, la banque en ligne, la banque hors ligne, l'envoi de SMS, le tweeting, le visionnage de cette vidéo YouTube même la conduite de votre voiture intelligente maintenant ou l'utilisation de votre brosse à dents intelligente.

Verrouillez votre maison avec votre Smart Lock ou même utilisez votre thermomètre intelligent, la liste est longue et continue.

Et bien sûr, à partir de ce jour, cette liste ne fera que s'allonger.

Notre monde devient de plus en plus dépendant des programmes pour diriger le spectacle, ce qui est une toute autre conversation.

Mais encore une fois, félicitations car vous avez au moins maintenant ce qu'il faut pour mieux comprendre et contribuer à ce paysage.

Je vous souhaite, à vous et à vos aventures de codage, le meilleur.

Et la dernière chose que je veux vous laisser est ce conseil.

Vous êtes garanti de faire des choses incroyables avec le code tant que vous suivez cette règle finale.

N'oubliez pas de toujours nourrir votre curiosité.


<script>
var iframe = document.getElementsByTagName("iframe")[0];
var elmnt = iframe.contentWindow.document.getElementsByClassName("ytp-pause-overlay")[0];
elmnt.style.display = "none";
</script>