---
title: Utiliser Selenium pour Créer un Bot de Web Scraping
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-31T12:43:06.000Z'
originalURL: https://freecodecamp.org/news/use-selenium-to-create-a-web-scraping-bot
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/selenium.png
tags:
- name: selenium
  slug: selenium
- name: youtube
  slug: youtube
seo_title: Utiliser Selenium pour Créer un Bot de Web Scraping
seo_desc: 'Selenium is a powerful web automation tool that can be used for browser
  automation, to test front-end code, and create web scraping bots.

  We just released a full course on the freeCodeCamp.org website that will teach you
  Selenium while you build a we...'
---

Selenium est un puissant outil d'automatisation web qui peut être utilisé pour l'automatisation des navigateurs, pour tester le code front-end et créer des bots de web scraping.

Nous venons de publier un cours complet sur le site freeCodeCamp.org qui vous apprendra à utiliser Selenium tout en construisant un bot de web scraping.

Jim de JimShapedCoding a développé ce cours. Jim a créé de nombreux cours populaires à la fois sur notre chaîne et sur sa propre chaîne.

Voici les sections de ce cours :

* Commencer avec les bases
* Explicite vs Implicite
* Envoyer des touches & Sélecteur CSS
* Structurer un projet de bot
* Recherche de deals
* Filtrations de réservation
* Exécution à partir d'un CLI
* Rapport de deals

Regardez le cours complet ci-dessous ou sur la [chaîne YouTube de freeCodeCamp.org](https://youtu.be/j7VZsCCnptM) (3 heures de visionnage).

%[https://youtu.be/j7VZsCCnptM]

## Transcription

(générée automatiquement)

Selenium est un framework portable pour tester les applications web.

Jim de JimShapedCoding enseigne ce cours sur Selenium.

Il a créé de nombreux cours populaires à la fois sur la chaîne freeCodeCamp et sur sa propre chaîne.

Bonjour à tous, et bienvenue dans la série Python Selenium, où nous allons apprendre à créer une automatisation de l'interface utilisateur pour les sites web.

Selenium est largement utilisé.

Et il est très populaire pour une excellente raison.

Parce qu'il peut vous aider à créer des tests pour vos applications web.

Et il peut également vous aider à créer des bots en ligne, ce qui est très bien.

Dans cette série, nous allons apprendre à utiliser Selenium à partir des bases.

Et plus tard, nous apprendrons à créer un bot en ligne qui signalera les meilleures offres d'un site de réservation.

Et cette série va vraiment inclure de superbes épisodes, alors assurez-vous de cliquer sur le bouton s'abonner ainsi que sur la notification de la cloche.

Ainsi, vous ne manquerez jamais un épisode de cette série entière.

Alors prenez une tasse de café, et commençons.

Super.

Avant de vraiment commencer, nous devons comprendre qu'il y aura quelques prérequis.

Dans cette série, je vais supposer que vous avez Python installé.

Et aussi que vous avez un IDE comme Python qui est correctement configuré avec Python.

Maintenant, vous pouvez également utiliser un éditeur de texte aléatoire comme Sublime Text, mais assurez-vous simplement qu'il est correctement connecté à votre interpréteur système.

Et si vous n'avez rien de tout cela, alors vous pouvez visiter mon cours de cinq heures pour débutants et rattraper les installations.

D'accord, comme beaucoup de bibliothèques dans le langage de programmation Python, nous devons d'une manière ou d'une autre utiliser la bibliothèque de scillonian.

C'est pourquoi nous devons l'installer sur notre ordinateur.

Et nous pouvons le faire avec la commande PIP.

Maintenant, si vous avez Python installé, alors vous devriez également avoir le gestionnaire de paquets PIP installé avec lui.

Maintenant, je vais ouvrir notre terminal ici.

Et je vais dire pip install Selenium comme ça.

Maintenant, je fais cela dans l'interpréteur système, car je ne vais pas utiliser d'environnements virtuels tout au long de la série.

C'est pourquoi je peux me permettre de le faire à partir du terminal.

D'accord, donc si vous ne voyez pas de flèches, cela signifie que tout est bien.

Et nous pouvons revenir à un graphique à secteurs et importer cette bibliothèque et voir comment nous pouvons l'utiliser.

D'accord, donc ici, je vais importer de Selenium import WebDriver.

Donc j'importe quelque chose de très spécifique à l'intérieur de la bibliothèque Selenium.

Et il y a une excellente raison de le faire.

Maintenant, lorsqu'il s'agit d'effectuer une automatisation de l'interface utilisateur dans les navigateurs web, nous devons d'une manière ou d'une autre ouvrir ce navigateur web.

C'est pourquoi nous devons importer une bibliothèque dédiée qui va automatiser l'action d'ouvrir un navigateur web.

Maintenant, lorsque nous parlons d'effectuer des automatisations sur un navigateur web, nous devons comprendre que pour chaque navigateur web, il y aura une version qui sera dédiée à l'exécution de ces tâches automatisées.

Par exemple, si nous voulons effectuer ces tâches d'automatisation sur le navigateur Chrome, alors nous devons instancier la classe chrome driver pour effectuer ces actions automatisées.

C'est pourquoi nous devons importer cette bibliothèque.

D'accord, maintenant que nous avons importé cela, nous devons instancier la bibliothèque qui sera responsable de faire apparaître le navigateur Chrome.

C'est pourquoi je vais descendre.

Et je vais dire, par exemple, driver est égal à WebDriver dot Chrome, comme ça.

Et comme vous pouvez le voir ici, il y a en fait plus d'options que Chrome.

Donc si je supprime cela, et que j'appuie sur contrôle espace, alors vous pouvez voir que nous avons aussi Firefox.

Et je crois qu'il y a edge comme prévu.

Donc, comme vous pouvez le voir, vous pouvez effectuer ces actions automatisées dans différents navigateurs.

Mais en fait, tout au long de cette série, je vais utiliser le navigateur Chrome.

C'est pourquoi je vais dire Chrome, et nous allons instancier la classe comme ça.

Maintenant, nous pourrions continuer et essayer d'exécuter cela.

Mais nous allons recevoir quelques flèches et les flèches vont parler de quelque chose qui s'appelle chromedriver.

Qui n'existe pas sur mon ordinateur.

Et aussi qu'il n'est pas dans le tat.

Donc, décomposons cette erreur en deux étapes importantes que nous devons faire.

La première d'entre elles, nous devons télécharger le chrome driver.

Et en fait, chrome driver est un fichier exécutable séparé que Selenium WebDriver utilise pour effectuer ces actions automatisées dans un navigateur Chrome.

Cela signifie que nous devons télécharger ce fichier chromedriver dot e xe sur notre ordinateur.

C'est pourquoi je vais apporter ici ce site web.

Et je vais mettre le lien de celui-ci dans la description pour sûr.

Et comme vous pouvez le voir, voici la page où nous pouvons télécharger le chrome driver, et si nous faisons défiler vers le bas, alors vous pouvez voir qu'il y a beaucoup de versions de Chrome driver que vous pouvez télécharger.

Maintenant, vous pourriez vous demander comment je vais décider quelle version doit être installée sur mon ordinateur ? Eh bien, cela dépend de la version du navigateur Chrome que vous avez actuellement installée sur votre ordinateur.

Donc, si vous utilisez le navigateur Chrome par défaut, comme moi, alors ce que nous pouvons faire, c'est aller dans un onglet séparé, et nous pouvons cliquer ici, Chrome, deux points, deux barres obliques, et puis dire, version.

Et juste après cela, nous verrons une sortie comme celle-ci.

Et comme vous pouvez le voir d'ici, voici la version de google chrome que j'utilise.

Et comme vous pouvez le voir, nous avons la version majeure comme 89.

Donc pour vous, cela pourrait être 9091 92, ou même 84.

Mais vous devez vous assurer que cette version majeure va correspondre à la version que vous allez télécharger à partir de la page chromedriver.

Donc dans mon cas, je vais revenir maintenant à cette page.

Et je vais rechercher une version qui commence par 89.

Et c'est pourquoi je vais cliquer ici.

Et juste après cela, je vais rechercher l'archive spécifique dont j'ai besoin.

Et bien sûr, ce sera windows car c'est le système d'exploitation de ma machine.

Et je vais cliquer ici et cela devrait commencer à télécharger et juste après avoir téléchargé cela, nous devons l'extraire car il s'agit en fait d'une archive zip.

D'accord, donc comme vous le savez probablement, dans Windows, par défaut, les fichiers téléchargés vont être téléchargés dans la bibliothèque de téléchargement.

Et vous voulez déplacer cela vers un emplacement où vous souhaitez avoir votre chromedriver.

Pour moi, ce sera sous le lecteur C.

Et à l'intérieur du dossier que j'ai nommé salonu drivers, comme vous pouvez le voir sur le côté gauche de mon écran.

Donc je vais couper cela d'ici et le déplacer vers le dossier où je souhaite l'avoir.

Donc je vais faire cela.

Et juste après cela, allons-y et travaillons avec ce suivi maintenant.

Donc comme vous pouvez le voir, l'emplacement de cela sera C Selenium drivers comme cela.

Et vous pouvez à nouveau, le mettre dans n'importe quel emplacement que vous aimeriez inviter jusqu'à ce que je vais extraire les fichiers ici.

Et dès que j'ai fait cela, alors vous pouvez voir que nous avons obtenu le fichier exécutable situé dans ce répertoire.

Donc c'est un bon début pour résoudre nos problèmes que nous avons lorsque nous essayons d'exécuter ce fichier de combat.

Parfait.

Donc retour à Python.

Maintenant, si nous allons essayer d'exécuter ce fichier à nouveau, alors nous allons finir avec la même erreur.

Et c'est parce que nous n'avons pas effectué la deuxième étape dont j'ai parlé lorsque nous avons vu cette erreur.

Et nous devons maintenant mettre l'emplacement de notre chromedriver dans une variable d'environnement qui s'appelle un chemin.

Maintenant, la variable d'environnement PATH va être responsable des fichiers que votre système doit rechercher lorsque vous voulez les exécuter immédiatement à partir du terminal.

C'est pourquoi elle doit être à l'intérieur de la variable d'environnement PATH.

Maintenant, nous aurions pu faire cela au niveau du système.

Mais ce n'est en fait pas une bonne idée.

Si un jour vous souhaitez exécuter le projet Selenium sur un autre serveur.

C'est pourquoi configurer cette variable d'environnement au niveau du code et non au niveau du système est considéré comme une meilleure pratique.

C'est pourquoi je vais dire en haut ici, quelque chose comme import OAS.

Et je vais maintenant télécharger une valeur de plus à la variable d'environnement PATH déjà existante.

Donc je vais dire Oh, s dot n, v wrong comme cela.

Et puis je vais chercher la clé de cat et m'assurer que vous devriez le faire tout en majuscules comme je l'ai fait.

Et maintenant, nous aimerions utiliser plus égal car nous ajoutons une valeur de pet à un pad déjà existant, nous pourrions avoir plusieurs valeurs pour cette variable d'environnement.

Et juste ici, nous voulons spécifier l'emplacement de notre chrome driver.

Donc je peux commencer à taper ici C, deux points et Ford slash.

Donc je pointe vers le lecteur C de mon ordinateur.

Et je vais dire ici, selenium drivers comme cela, car c'est le nom du dossier où j'ai le chromedriver.

D'accord, donc juste après avoir fait cela, nous devrions ajouter ici la lettre r avant les guillemets doubles.

Et c'est en fait une convention pour un préfixe qui va le marquer comme une chaîne brute et cela va être utile lorsque vous spécifiez des chemins vers différents emplacements.

Donc maintenant, si nous devions essayer d'exécuter ce programme, alors nous devrions voir maintenant le chrome apparaître et c'est exactement ce qui se passe.

Donc cela signifie que maintenant nous sommes prêts à travailler et à commencer à essayer d'effectuer quelques automatisations sur un site web aléatoire.

D'accord, donc maintenant que nous avons compris comment configurer un environnement Selenium, essayons d'effectuer une automatisation sur un site web aléatoire.

Maintenant, dans cet épisode, spécifiquement, je vais commencer par un site web de test Selenium qui nous permettra de prendre des actions de base pour commencer avec lui.

Donc je vais utiliser ce site web Selenium ez.com.

Et je vais aller à cette URL ici, dont je vais mettre le lien dans la description.

Et je vais essayer de cliquer sur ce bouton de téléchargement, en le réalisant avec Selenium uniquement.

Et juste après avoir cliqué sur celui-ci, nous devrions d'une manière ou d'une autre identifier que la progression a été complétée.

Donc, en fait, ces types d'actions sont de bons candidats pour des actions que vous souhaitez effectuer avec Selenium sans vraiment être impliqué dans le clic manuel sur ces boutons.

Donc, allons-y et commençons.

Donc, premièrement, nous devrions comprendre comment nous allons identifier l'élément sur lequel nous voulons cliquer.

Et pour faire quelque chose comme cela, nous pouvons aller à l'élément que nous voulons.

Et nous pouvons cliquer sur Inspecter comme suit.

Maintenant, en fait, lorsqu'il s'agit de pages, chaque page aura son architecture HTML unique.

Et chaque élément HTML sera décrit par chaque type.

Et ainsi que par certains attributs supplémentaires.

Donc, voyons ce que j'ai dit en action.

Donc, je vais dire inspecter.

Et comme vous pouvez le voir, nous avons cette ligne en arrière-plan bleu.

Et comme je l'ai dit, le type de cet élément est un bouton car nous voyons qu'il est juste après les balises.

Donc, c'est pourquoi il est appelé un élément HTML de bouton.

Et comme vous pouvez le voir, il a différents attributs comme la classe, l'ID comme cela.

Donc, ce que nous pouvons faire à partir d'ici, c'est essayer d'identifier l'élément qui a l'ID de bouton de téléchargement, comme il est dit ici.

Donc, essayons de faire et voyons comment nous pouvons identifier cet élément spécifique, et essayer de cliquer dessus.

D'accord, donc retournons à pi charm.

Maintenant, avant de faire cela, laissez-moi copier le lien du site web, car nous allons l'utiliser dans une minute.

D'accord, donc maintenant si j'ouvre pi charm, et que je descends, et ici nous sommes prêts à écrire un code supplémentaire.

Maintenant, avant tout, nous devons spécifier à selenium quel est le site web que nous allons utiliser dans notre automatisation, donc cela devrait être fait avec la méthode get que le driver va avoir.

Donc, je vais dire driver dot get.

Et comme vous pouvez le voir, il attend une URL, donc je peux directement mettre le lien de l'URL sur laquelle nous voulons effectuer des actions automatiques.

Donc, comme vous pouvez le voir, c'est la manière dont le driver dot get devrait être exécuté.

D'accord, donc maintenant que nous avons fait cela, nous devons d'une manière ou d'une autre dire à Selenium que nous aimerions cliquer sur un élément dont l'ID est le bouton de téléchargement.

Donc, je vais dire ici, driver dot find underscore element, underscore by ID.

Et comme vous pouvez le voir, nous avons plusieurs méthodes pour trouver un élément par, nous avons le nom de la classe, le sélecteur CSS, et même plus comme le nom.

Et ce sont des méthodes que nous allons voir dans le futur tout au long de la série.

Mais commençons par l'ID.

Et je vais dire ici, bouton de téléchargement, comme suit.

Maintenant, puisque cette déclaration entière va nous retourner un objet avec lequel nous pouvons effectuer des actions supplémentaires, je devrais assigner cela à une variable.

Donc, je peux dire mon élément, quelque chose comme ça.

Et ensuite, en dessous, je peux dire mon élément qui clique comme ça.

Et nous devrions voir le pilote Selenium essayer de cliquer sur cet élément.

Donc, testons cela.

Donc, je vais exécuter cela tout de suite.

Et je ne vais rien toucher.

Donc, voyons cela en action.

D'accord, donc il nous amène ici.

Et comme vous pouvez le voir, il a immédiatement cliqué sur cet élément, car nous voyons la boîte de progression qui nous dit maintenant que le téléchargement a été complété.

Mais il y a en fait un gros problème avec cette approche.

Parce que parfois, dans la plupart des cas, le chargement d'un site web entier peut prendre un certain temps.

Donc, c'est pourquoi nous pouvons aller entre ces deux lignes, et essayer d'attendre avant d'essayer d'effectuer une action sur un élément.

Donc, c'est pourquoi, en allant entre ces lignes et en disant quelque chose comme driver that implicitly wait.

Et ici, nous devons spécifier la quantité de secondes que nous aimerions attendre pour que ce site web soit chargé avec succès.

Donc, nous pouvons dire que nous aimerions attendre par exemple trois secondes, donc c'est considéré comme une meilleure chose à faire, car maintenant nous sommes totalement en sécurité contre notre navigateur étant un peu lent parfois.

Ou peut-être pouvons-nous avoir certains cas où notre serveur pourrait être très lent.

Donc, c'est pourquoi attendre un peu ici et là pourrait être une meilleure idée.

Donc maintenant, si nous exécutons notre programme une fois de plus, voyons les résultats.

Donc, au début, la page est chargée.

Puis, comme vous pouvez le voir, elle essaie immédiatement de télécharger ce fichier.

Maintenant, encore une fois, ceci est juste une simulation, cela ne télécharge vraiment rien sur votre ordinateur.

D'accord, donc identifions ce qui s'est passé ici.

Tout d'abord, nous pouvons comprendre qu'il n'a vraiment pas attendu trois secondes.

Donc, ce que cela signifie, c'est que l'attente implicite fait quelque chose de spécial à notre objet driver, car nous n'avons pas vraiment attendu trois secondes, n'est-ce pas.

Donc, essayons de tester cela avec 30 secondes maintenant.

Donc, je vais exécuter cela une fois de plus.

Et comme vous pouvez le voir, en une seconde, cela semble le télécharger une fois de plus.

Donc, cela ne attend vraiment pas le temps spécifié dans cette ligne.

Donc, que se passe-t-il ici et pourquoi avons-nous vu les actions prises immédiatement.

Eh bien, nous aurions pu utiliser ici quelque chose comme time dot sleep, et spécifier la quantité de secondes à attendre.

Mais c'est quelque chose que nous n'aimons pas faire ici.

Parce que parfois, nous n'aimons pas attendre toute la durée du temps, au cas où l'élément serait trouvé avant la durée spécifiée, il doit passer à la ligne suivante de l'exécution du code.

Et donc, utiliser ici l'attente implicite est en fait très, très utile.

Parce que, encore une fois, nous ne ressentons pas le besoin d'attendre 30 secondes si l'élément est déjà là dans cette page web.

Maintenant, pour être honnête, il y a plus de choses dont je voudrais parler à propos de cette attente implicite, car elle a quelques fonctionnalités supplémentaires dont je parlerai dans le futur.

Et si vous avez des questions sur le comportement de cette méthode délicate, alors faites-le moi savoir dans la section des commentaires ci-dessous.

D'accord, donc avant d'aller de l'avant et de comparer ces types d'attentes, clarifions quelques points importants sur l'attente implicite.

Jusqu'à présent, nous savons que cela est beaucoup plus efficace, plutôt que de taper dans le temps dot sleep, car nous n'aimons pas toujours attendre 30 secondes, avant de trouver un élément par ID, par exemple.

Mais il y a une information que nous devons savoir sur l'attente implicite, elle va être configurée comme un délai d'attente dans tout votre projet scillonien.

Donc, ce que cela signifie, c'est que vous n'avez besoin d'appeler cette méthode d'attente implicite qu'une seule fois, et ensuite elle va configurer une durée d'attente implicite pour tous les éléments que vous allez essayer de trouver dans le futur.

Par exemple, je pourrais descendre ici et dire quelque chose comme my second element, et je peux le faire égal à driver dot find element by ID.

Et je vais mettre ici un élément qui n'existe même pas dans la page à gauche.

Donc je peux dire quelque chose comme, écrivons simplement quelque chose au hasard.

Et ensuite je peux essayer d'exécuter notre programme.

Et juste à des fins de test, laissez-moi diminuer cela à huit secondes.

Donc nous n'attendrons pas vraiment 30 secondes avant de voir ce programme s'écraser.

D'accord, donc si nous exécutons cela une fois de plus, alors voyons les résultats.

Donc comme vous pouvez le voir, nous n'avons aucun problème avec le premier élément.

Mais en une seconde ou deux, nous devrions recevoir une erreur indiquant que Selenium n'a pas pu identifier un élément avec cet ID ici.

Donc c'est en fait un point important à retenir.

Parce qu'une fois que nous avons dit l'attente implicite, elle va être appliquée à tous les éléments que nous allons essayer de trouver dans le futur.

D'accord, donc maintenant que nous avons complètement compris le comportement de l'attente implicite, allons de l'avant avec notre automatisation.

Donc maintenant, comme prochaine étape, il aurait été bien d'identifier si le téléchargement a été complété avec succès.

Et nous avons compris que pour indiquer quelque chose comme cela, nous devons comprendre quand ce texte ici va être exactement égal à complet avec un point d'exclamation.

Donc essayons d'écrire une automatisation comme celle-ci.

Donc je vais sélectionner tout ici et essayer de cliquer sur Inspecter.

Et laissez-moi faire cela une fois de plus car cela n'a pas vraiment pointé dessus.

D'accord, donc nous pouvons voir que ce complet avec un point d'exclamation provient de cet élément HTML, qui nous dit que son type est Dave, et qu'il a la classe de progress label.

Maintenant, jusqu'à ce point, nous n'avons pas vraiment identifié un élément HTML spécifique par son nom de classe.

Et il y a en fait une excellente façon de le faire en utilisant à nouveau une méthode avec le préfixe find element.

Donc voyons comment nous pouvons faire cela.

Donc laissez-moi supprimer cette ligne en fait, et je vais rester avec celle-ci.

Donc je peux dire quelque chose comme progress element est égal à driver dot find element, et puis je peux sélectionner une méthode qui s'appelle by class name.

Donc nous ne pouvons pas identifier un élément par son nom de classe.

Donc c'est une bonne idée de sélectionner cela.

Et je dois maintenant passer la valeur de la classe.

Donc ce sera progress dash label comme nous l'avons vu précédemment.

Maintenant, pour ceux qui sont confus sur ce que sont les classes dans le monde du web, c'est en fait une référence à une méthode de classement, contrairement à Python, qui fait référence aux classes que nous utilisons pour la programmation orientée objet.

Donc je voulais juste m'assurer que nous ne confondons pas les significations de la classe dans le web.

Et maintenant que j'ai cela, je peux aller à une nouvelle ligne.

Et je peux dire ici, quelque chose comme print, et je peux utiliser la chaîne formatée.

Et je peux essayer d'imprimer le texte de ces éléments.

Donc ce sera par les deux textes, et il a montré que l'affichage est le texte ici.

Donc si nous faisons cela, et que nous exécutons cela une fois de plus, testons le résultat de cela.

D'accord, donc nous avons une nouvelle page qui est apparue.

Et comme vous pouvez le voir, il a immédiatement montré le texte de cet élément, qui était en train de descendre maintenant en montrant le texte immédiatement n'est en fait pas une bonne idée, car nous aimerions probablement attendre un certain temps jusqu'à ce que nous voyions le complet.

Mais il n'y a en fait pas une belle façon de faire cela avec les approches que nous avons apprises jusqu'à ce point.

Donc nous devons utiliser un autre utilitaire.

Et pour cela, il y a quelque chose qui existe dans selenium, qui s'appelle explicit wait.

Maintenant, avec cela, nous pouvons en fait permettre à notre programme d'attendre une condition inattendue.

Et ensuite, nous pouvons attendre jusqu'à ce que cette condition retourne vrai.

Donc, ce que cela signifie, c'est que nous cherchons cette expression vraie ici.

Donc je peux dire ici, complété avec le point d'exclamation.

Et dans notre cas, si nous n'attendons pas de manière intelligente, alors nous allons toujours recevoir faux avec cela.

Donc nous devons trouver comment nous pouvons attendre jusqu'à ce que cette condition soit vraie.

Et allons-y et voyons comment nous pouvons faire cela.

D'accord, donc pour utiliser l'attente explicite, nous devons importer quelques bibliothèques secondaires qui se trouvent à l'intérieur de Selenium.

Donc nous allons dire en haut ici quelque chose comme from Selenium dot web driver, that common.by import by comme cela.

Et nous allons également importer deux autres choses ici.

Donc ce sera from Selenium dot web driver.support.ui.

Comme cela, nous devons importer la classe intégrée à l'intérieur de Selenium qui s'appelle web driver wait.

Et nous aimerions également importer une dernière chose, qui sera Selenium dot WebDriver dot support.

Import expected conditions as EC, les deux en majuscules comme cela.

Maintenant, je sais que c'était beaucoup d'informations que nous avons utilisées en entrée.

Mais il y a en fait une excellente raison à cela.

Et nous verrons pourquoi dans une minute.

Donc maintenant, je vais descendre ici et je vais commencer à écrire la condition que nous aimerions attendre.

Maintenant, pour commencer avec cela, je vais d'abord instancier la classe WebDriver weight.

Donc je vais dire web driver weight et je vais l'instancier sans l'assigner à une variable.

Et d'abord, nous devons passer l'objet driver.

Donc nous allons simplement dire ici, driver.

Et maintenant, nous aimerions spécifier la quantité de secondes que nous devrions attendre jusqu'à ce que la condition attendue soit vraie ou non.

Donc je vais dire ici quelque chose comme 30 secondes à nouveau, et cela devrait être suffisant.

Et ensuite, je vais lancer automatiquement la méthode until ici.

Maintenant, par convention, les informations écrites à l'intérieur de cette méthode until sont généralement sur une ligne séparée.

Donc je vais appuyer sur entrer ici.

Et ensuite, nous devons écrire la condition que nous voulons qu'elle soit vraie à un moment donné.

Et dans notre cas, c'est après 30 secondes environ.

Donc nous pouvons dire ici e c, qui signifie expected condition que nous avons utilisée comme import ici.

Et nous pouvons maintenant utiliser une méthode qui dit text to be present in element.

Donc, comme nous pouvons le comprendre, cette méthode est conçue pour attendre que le texte ait le texte attendu.

Et je vais lancer cette méthode ici et appuyer à nouveau sur entrer.

Donc, encore une fois, je vais simplement écrire les arguments sur une ligne séparée.

Maintenant, cette méthode attend deux arguments importants, le premier étant l'élément sur lequel nous aimerions vérifier la condition.

Et le second étant le texte que nous attendons après 30 secondes.

Donc je vais simplement commenter ici, ces downs So je vais dire ici, element filtration.

Et comme le second, nous allons dire le texte attendu comme cela.

D'accord, donc la manière dont nous allons identifier l'élément que nous aimerions vérifier est en utilisant le by class.

Maintenant, ce n'est qu'une autre approche pour trouver des éléments dans une page web.

Donc cela ne va pas sembler complexe.

Donc c'est aussi facile que de dire ici quelque chose comme je vais simplement créer un tuple ici, et puis je vais commencer ma filtration.

Donc nous aimerions trouver cela à nouveau, par le nom de la classe.

Et comme vous pouvez le voir, nous avons une complétion automatique pour cela.

Donc je peux simplement utiliser le nom de la classe comme cela.

Et la deuxième partie de l'information juste à côté devrait être la valeur du nom de la classe, donc ce sera progress dash label exactement comme avant.

Donc cette expression entière est juste une autre façon de trouver un élément dans une page web, contrairement à l'utilisation de la méthode find element by class name, meddled, et je viens de réaliser que je n'ai pas supprimé ces deux lignes dont nous n'avons pas besoin.

Donc allons-y et faisons cela.

Et ensuite dans la deuxième ligne, juste après avoir dit, virgule, nous allons écrire le texte attendu.

Donc ce sera complet avec un point d'exclamation.

Donc maintenant, si nous exécutons notre programme, alors nous ne devrions pas recevoir d'erreurs, car cette condition va probablement nous retourner vrai en moins de 30 secondes.

Donc si nous exécutons notre automatisation maintenant, et attendons les résultats, donc encore une fois, nous cliquons sur ce bouton de téléchargement.

Et voyons, juste en une seconde, ce qui va se passer.

D'accord, donc nous avons obtenu le texte de complet.

Et si nous retournons à notre programme, alors vous pouvez voir que le programme s'est terminé avec succès.

Donc, ce que cela signifie, c'est que nous avons pu écrire une belle automatisation, jusqu'à ce que nous ayons attendu, ce qui vérifie vraiment que le téléchargement d'un fichier a été complété avec succès.

Donc, c'est très bien de jouer entre ces méthodes d'attente, nous pouvons utiliser implicitement l'attente pour trouver des éléments dans toute notre page.

Et nous pouvons également utiliser l'attente explicite, qui est l'attente la plus personnalisée, donc cela signifie que nous devons l'utiliser si nous voulons que l'exécution attende un certain temps jusqu'à ce qu'une condition soit atteinte.

Maintenant, pour tous ceux qui sont intéressés à savoir quelles sont les conditions attendues que vous pouvez utiliser, vous pouvez le faire en voyant toutes les options ici.

Donc, si nous supprimons tout d'ici, et utilisons cela à nouveau, et vous pouvez voir que nous avons beaucoup d'options que nous pouvons utiliser pour la condition attendue.

Donc, vous pouvez voir que nous avons un élément à cliquer, des éléments à sélectionner et en fait attendre qu'une nouvelle fenêtre soit ouverte.

Donc, comme vous pouvez le voir, il y a des tonnes d'options que vous pouvez utiliser si vous souhaitez attendre qu'une condition attendue soit atteinte.

Donc, c'est une très belle fonctionnalité de Selenium que nous pouvons toujours utiliser pour écrire des bots plus dynamiques et ainsi que pour écrire des cas de test plus efficaces.

D'accord, donc la raison pour laquelle vous voulez apprendre à envoyer des touches ou à cliquer sur différents boutons juste après, c'est pour effectuer des actions comme la connexion et l'enregistrement de comptes.

Et c'est quelque chose de très utile lorsque vous voulez surmonter l'autorisation sur certains sites web pour effectuer des tests d'interface utilisateur ou créer un bot pour une raison quelconque.

Pour pratiquer cela, je vais ouvrir ce site web à nouveau depuis Selenium easy.com.

Donc, c'est en fait la page sur laquelle nous allons essayer d'envoyer les touches.

Comme vous pouvez le voir, ici, nous avons quelques formulaires HTML.

Et en fait, lorsque nous voulons envoyer les touches, généralement nous aimerions le faire dans des formulaires HTML où nous devons vraiment écrire des données, et ensuite nous devons cliquer sur un bouton pour soumettre nos données.

Donc, comme vous pouvez le voir, ici, nous avons un formulaire qui demande deux valeurs.

Et si nous devions cliquer sur Get total, alors vous pouvez voir qu'il nous montre 30 et si je change cela en un autre nombre, vous pouvez voir qu'il est mis à jour.

Donc, c'est ce que nous allons essayer d'automatiser maintenant avec Selenium.

Tout d'abord, laissez-moi prendre le site web de cette section ici et revenez à Python et dites ici rival dot get et le lien sera disponible dans la description pour sûr.

Donc vous pouvez directement copier et coller à partir de là, d'accord.

Donc maintenant, je vais coller cela.

Et juste après avoir fait cela, nous devons d'une manière ou d'une autre essayer d'identifier l'élément dans une méthode par ID, nom de classe ou quelle que soit la méthode.

Donc je vais revenir à notre site web ici et comme d'habitude, je vais dire inspecter, et vous pouvez voir que nous avons ici quelque chose qui s'appelle classe que nous pouvons à nouveau, trouver l'élément par classe.

Et ainsi que l'ID.

Maintenant, j'aime toujours filtrer par ID car je pense que c'est le champ le plus fort qui est toujours unique.

Donc je vais utiliser cet ID some one.

Et je crois que la deuxième boîte ici devrait être some tools.

Donc si je vérifie cela avec inspecter, alors vous pouvez voir que c'est juste comme prévu.

Donc nous devons tirer ces éléments et essayer d'envoyer des touches.

Donc je vais revenir à Python.

Et je vais dire ici, some one est égal à driver dot find element by ID.

Et je peux utiliser quelqu'un ici.

Et je peux faire exactement la même chose en copiant cela ici, et en le collant et en changeant les valeurs en nombre deux, comme cela.

Et ensuite, je peux essayer d'envoyer des touches.

Donc ce sera aussi facile que de tirer l'élément.

Parce que maintenant nous avons un accès complet à celui-ci, et nous lançons la méthode send keys comme cela.

Maintenant, vous pouvez mettre ici ce que vous voulez, comme vous pouvez le voir, cela attend une valeur.

Donc cela pourrait être n'importe quelle valeur que vous aimeriez passer ici, cela pourrait être une chaîne, ou cela pourrait être directement un nombre comme cela.

Donc, allons-y avec des nombres et disons 15, comme nous l'avons fait manuellement.

Et je vais faire la même chose avec some tools.

Donc je vais envoyer 15 aussi.

Et maintenant, nous pouvons tester cela et voir si cela fonctionne.

Mais pas avant d'aller de l'avant et de dire ici quelque chose comme rival that implicitly wait.

Et il est suffisant d'attendre cinq secondes ici pour chaque élément.

Et maintenant, nous pouvons tester cela.

Donc si je lance notre programme, alors voyons les résultats.

D'accord, donc la page a été chargée.

Et vous pouvez voir que nous avons reçu ce message.

Et nous allons le gérer dans une minute.

Mais vous pouvez voir en arrière-plan, que nous avons les valeurs.

Donc je sais que c'est un peu transparent ici, mais vous pouvez vraiment voir cela en arrière-plan.

D'accord, donc je pense que nous avons un nouveau défi ici comme nous voyons cette sortie.

Et nous devons d'une manière ou d'une autre effectuer une opération pour cliquer sur les boutons non pour continuer notre automatisation.

Donc c'est en fait un bon candidat pour gérer les choses en cours de route.

Donc maintenant, je peux aller à inspecter ici et voir ce qui doit être fait pour identifier ce bouton ici et cliquer dessus avant de continuer avec notre automatisation.

D'accord, donc vous pouvez voir que nous avons cet élément avec plusieurs classes.

Et si je jette un coup d'œil ici, alors vous pouvez voir que nous avons quelques classes ici qui sont séparées par des espaces.

Maintenant, si vous voyez des classes séparées par des espaces, comme je l'ai dit, alors cela signifie qu'elles font référence à une classe différente.

Donc je peux en fait essayer de filtrer cet élément par le nom de la classe at dash c m dash, no dash button, car ce sera probablement le nom de classe le plus unique que je puisse essayer de filtrer cet élément.

Donc je peux aller ici et utiliser, laissez-moi copier cela et le manipuler dans Python.

Avant de continuer avec tout ici, laissez-moi s'il vous plaît descendre ici et coller ce texte ici.

Et comme vous pouvez le voir, c'est le nom de la classe par lequel nous aimerions filtrer.

Donc je vais tout supprimer.

Et je vais couper cette chaîne d'ici.

Et je vais dire no button est égal à driver dot find element by class name.

Et je vais coller le nom de la classe par lequel nous aimerions filtrer.

Et maintenant que j'ai fait cela, je peux appliquer la méthode click.

Donc ce sera no button dot click comme cela.

Maintenant, une dernière chose qu'il est bon de faire ici est d'envelopper cela avec un bloc try except car nous ne trouverons pas toujours un élément par ce nom de classe car peut-être que la prochaine fois cette fenêtre contextuelle n'apparaîtra pas.

Donc c'est une bonne idée d'utiliser ici, try et de localiser ces deux lignes sous un bloc try.

Et ensuite, si Selenium ne trouve aucun élément avec ce nom de classe, alors il ne plantera pas notre programme.

Parce que dans le bloc except, nous pouvons simplement dire quelque chose comme print no element with this class name.

Donc je peux dire juste skipping comme cela.

D'accord, et en dessous, je peux continuer avec notre automatisation exactement comme cela.

D'accord, donc si nous exécutons notre programme ici, alors voyons ce qui va se passer cette fois.

Donc la page a été ouverte.

Et comme vous pouvez le voir, maintenant nous ne voyons pas la fenêtre contextuelle, et nous ne voyons aucun message du bloc except.

Donc ce que cela signifie, c'est que Selenium a identifié l'élément avec ce nom de classe et qu'il a cliqué sur ce bouton que nous voulions cliquer dès le premier stade.

Et ensuite, il a continué et exécuté le reste des lignes de code.

Et vous pouvez voir que les valeurs sont juste là.

Donc nous sommes très proches de compléter l'automatisation que nous voulions compléter.

Maintenant, il y a une dernière chose que j'aimerais vous montrer avant de continuer avec l'élément get total.

Et je parle du fait que nous pouvons envoyer les touches directement, pas seulement en spécifiant le texte que nous aimerions envoyer.

Donc ce que cela signifie, c'est que nous pouvons envoyer les touches comme Shift Alt, enter control et des choses comme ça.

Et la manière dont cela va fonctionner est en important la classe keys de Selenium.

Et c'est quelque chose d'utile ici et là que vous voudrez automatiser certaines actions qui nécessitent peut-être de copier du texte.

Donc vous devez automatiser Ctrl C.

Et encore une fois, c'est utile car parfois vous voudrez automatiser l'appui sur une touche directement plutôt que d'envoyer un texte aléatoire.

Donc je vais importer ici de Selenium dot WebDriver, dot common dot keys, import keys comme cela.

Et à l'intérieur de cette classe, vous avez toutes les options qui sont essentiellement les touches du clavier qui existent dans chaque clavier.

Donc pour vous montrer cela, je vais maintenant changer cela en quelque chose comme keys, dot.

Et comme vous pouvez le voir, dans le menu déroulant, nous avons toutes les options.

Donc nous avons même F 1234.

Et nous avons même les nums qui existent sur le côté droit de notre câble, qui est dans le pavé numérique.

Donc si nous voulons, nous pouvons envoyer les touches du pavé numérique, je sais que ce n'est pas très utile pour ce cas.

Mais encore une fois, envoyer des touches directement pourrait être très, très utile dans certains cas lorsque vous en avez besoin.

Donc comme vous pouvez le voir, vous avez toutes les options ici.

Et si un jour, vous voulez jeter un coup d'œil à toutes les options, alors vous pouvez toujours aller ici et utiliser Ctrl B dans Python ou F 12 dans visual code, et vous pouvez inspecter cette classe.

Et vous pouvez voir que toutes les options sont disponibles ici.

Et c'est très, très utile.

Maintenant, pour vous prouver que cela fonctionnera, je vais essayer cela avec le pavé numérique.

Donc dans le someone, je vais envoyer numpad.

Un, et je vais aussi envoyer attention que je peux séparer les valeurs par une virgule.

Et je peux dire ici keys that numpad five, et ensuite cela va envoyer le 15.

Donc cela va être assez équivalent à ce que nous avons fait.

Et pour vous montrer que cela fonctionne, je peux lancer notre programme à nouveau.

Et vous pouvez voir en bas que les résultats sont assez les mêmes.

Donc ce n'est qu'une autre approche pour envoyer des touches.

Et la beauté derrière le destin huit est le fait que vous pouvez envoyer toutes les touches du clavier qui existent.

D'accord, donc maintenant nous n'avons que le bouton gate total à filtrer.

Maintenant, nous n'aimons pas toujours filtrer les éléments HTML par leur ID ou leur nom de classe, nous pourrions avoir dans certains cas des paires clé-valeur d'attributs supplémentaires que nous pouvons essayer de filtrer les éléments.

Donc maintenant, je vais cliquer sur Inspect ici.

Et nous faisons cela à nouveau.

Et comme vous pouvez le voir, nous avons ici un attribut que nous n'avons pas vu auparavant, qui est on click.

Maintenant, disons que j'aimerais filtrer cet élément par onClick égal à cette valeur ici.

Et c'est quelque chose que nous n'avons pas appris à faire jusqu'à présent.

Et cela est possible avec quelque chose qui s'appelle un sélecteur CSS.

Et le sélecteur CSS est un motif pour filtrer un élément par son style.

Maintenant, contrairement aux méthodes de find element by ID ou class name.

avec les sélecteurs CSS, nous n'avons pas toujours besoin de filtrer un élément qui correspond à une chaîne exacte.

Par exemple, avec les sélecteurs CSS, il est possible d'identifier un élément en recherchant uniquement une sous-chaîne qu'il contient.

Cela est extrêmement utile car nous ne voulons pas toujours filtrer les éléments par correspondance exacte clé-valeur, car nous pourrions vouloir effectuer quelque chose avec des éléments ayant le même préfixe ou suffixe.

Donc voyons comment les sélecteurs CSS fonctionnent en action.

D'accord, donc nous sommes de retour à pi charm.

Et descendons et voyons comment nous pouvons utiliser le sélecteur CSS.

Donc je vais dire ici, button est égal à driver dot find element by CSS selector comme cela.

Et ici, nous devons passer notre expression de sélecteur CSS.

Et la manière dont nous allons faire cela est en utilisant un motif spécial qui existe.

Maintenant, pour sélectionner un élément par sélecteur CSS.

Vous avez plusieurs options mais nous allons utiliser le motif d'un type d'élément HTML, suivi d'une correspondance clé-valeur.

Maintenant, par exemple, nous pouvons revenir à notre bouton et voir comment nous allons le filtrer.

Et vous pouvez voir que c'est un type de bouton.

Et nous pouvons le voir à partir d'ici, et il a la paire clé-valeur de on click return total.

Donc cela signifie que nous pouvons essayer de filtrer tous les boutons qui ont l'attribut de onClick avec la valeur de return total comme cela.

Pour y parvenir, nous allons revenir ici et nous allons dire button, et ensuite nous devrons ouvrir des crochets.

Et nous devrons dire ici quelque chose comme on click equals et ensuite nous allons utiliser des guillemets doubles ici.

Maintenant, la raison pour laquelle j'utilise des guillemets doubles est parce que j'utilise des guillemets simples ici depuis le début.

Et nous ne voulons pas les confondre.

Et maintenant ici, je peux dire return total comme cela.

Et comme vous pouvez le voir, c'est une façon dont un sélecteur CSS pourrait fonctionner, vous pouvez spécifier l'élément HTML suivi de la correspondance clé-valeur, et vous assurer qu'il est à l'intérieur des crochets juste après.

Maintenant, je vais montrer plus tard toutes les options de cert ou CSS, car il y a des tonnes d'options que vous pouvez filtrer dans un élément par sélecteur CSS.

D'accord, donc je m'attends à ce que ce bouton ait l'élément HTML de ce bouton.

Et ensuite, je peux utiliser button dot click comme prévu.

Donc maintenant, nous pouvons tester si cela fonctionne.

Donc si nous exécutons notre automatisation, une fois de plus, voyons ce qui va se passer.

D'accord, donc en bas, vous pouvez voir que nous avons reçu le texte de total A plus B est 30.

Et c'est exactement le résultat que nous attendions.

Donc, ce que cela signifie, c'est que nous avons pu sélectionner un élément par sélecteurs CSS avec succès.

Et c'est parfait.

D'accord, donc j'ai dit plus tôt que je vais vous montrer la page où j'ai pris cette expression de motif de sélecteur CSS.

Et vous pouvez voir que maintenant, je veux dire une page qui a plusieurs exemples de la façon dont vous pouvez filtrer les éléments en utilisant le sélecteur CSS.

Donc vous pouvez voir que nous avons un tableau avec toutes les options de sélecteur.

Et ainsi que quelques exemples supplémentaires pour tous les motifs.

Donc vous pouvez voir que si nous faisons défiler vers le bas, alors j'ai en fait utilisé ces motifs.

Donc c'est un motif qui contient le type d'élément.

Et dans cet exemple, le type est a et cela signifie ancre.

Et vous pouvez voir que dans les crochets ici, il recherche une correspondance clé-valeur.

Mais dans ce cas, comme je l'ai dit plus tôt, vous pouvez non seulement rechercher un élément qui inclut une chaîne exacte, vous pouvez également rechercher un élément qui contient une chaîne.

Donc vous pouvez voir que dans la description, il est dit sélectionne chaque élément de balise a dont la valeur de l'attribut href commence par HTTP s.

Et il en va de même lorsque vous voulez sélectionner certains éléments qui se terminent par un texte.

Donc vous pouvez voir que nous avons beaucoup d'options ici.

Et c'est très utile.

Et je peux totalement confirmer que le sélecteur CSS est la méthode que j'utilise le plus, car il vous donne beaucoup plus de contrôle que les autres éléments.

Donc il vous aide vraiment à trouver les éléments que vous allez rechercher lorsque vous voulez effectuer une automatisation sur eux.

D'accord, donc la première chose que nous voulons faire est de dédier un fichier pour le projet.

Maintenant, avant de commencer l'enregistrement de cela, j'ai déjà créé ce dossier de bord.

Donc cela va inclure le code pour notre projet.

Et vous pouvez aller de l'avant et créer le dossier où vous voulez, assurez-vous simplement que vous connectez cela à Python.

Donc je vais cliquer OK.

Et nous allons commencer à partir d'ici.

Maintenant, vous pouvez faire attention au fait que par défaut, Python a créé pour nous le fichier main.py, donc nous pouvons simplement supprimer tout cela et continuer à travailler.

Donc si le fichier auto-généré ne vous convient pas, alors allez-y et créez un nouveau fichier par vous-même et nommez-le main comme cela.

D'accord, donc maintenant, je vais commencer à concevoir la structure du projet.

Et la manière dont je vais structurer ce projet va être comme je l'ai décrit dans ma vidéo de structure de projet sur ma chaîne.

Maintenant, si vous ne savez pas ce que je veux dire, alors j'ai une vidéo qui décrit comment un projet Python devrait être structuré, qu'il s'agisse d'un projet débutant ou d'un projet avancé.

Donc si vous voulez jeter un coup d'œil, vous pouvez cliquer sur le lien suggéré.

Donc maintenant, je vais créer un sous-répertoire qui s'appelle Woking comme cela.

Et je fais cela parce que je veux inclure tout le code pertinent au bot de réservation à l'intérieur de ce répertoire.

Et ensuite, ce fichier main.py va aller de l'avant et appeler les fichiers Python nécessaires à partir de ce répertoire.

Et laissez-moi aller de l'avant et changer cela pour run en fait, c'est juste plus confortable pour gagner.

Donc je vais aller de l'avant et faire cela.

D'accord, donc à l'intérieur de ce répertoire de réservation, nous allons commencer par créer trois fichiers.

Donc, allons-y et créons le premier d'entre eux.

Donc, le premier va s'appeler réservation comme cela.

Et ici, je vais avoir une classe qui va avoir quelques méthodes d'instance que nous allons appeler afin de faire en sorte que notre conseil effectue certaines actions.

Et le second va être des constantes.

Donc nous allons avoir beaucoup de valeurs que nous voulons vraiment changer au cours de l'exécution de notre projet.

Donc, c'est pourquoi séparer ces variables dans un autre fichier que nous pouvons nommer constantes est une excellente idée.

Donc je vais aller de l'avant et faire cela.

Et l'autre fichier que je vais créer pour l'instant va être appelé de la manière suivante.

Donc ce sera underscore deux fois en it underscore deux fois une fois de plus.

Et il y a en fait une excellente raison pour laquelle je nomme ce fichier de cette manière, c'est parce que c'est une convention lorsque vous voulez créer un package Python.

Maintenant, la raison pour laquelle vous voulez créer un package Python, c'est parce que nous voulons appeler le package à partir de ce fichier run.pi.

Maintenant, remarquez comment le fichier run.pi est en dehors du répertoire de travail.

Et c'est une raison de plus pour laquelle j'ai créé ce fichier double underscore, vous avez besoin d'un fichier double underscore, c'est juste une convention pour marquer ce répertoire comme un package Python.

Maintenant, je vais utiliser quelques secondes de plus pour expliquer quelque chose de très spécial à propos du fichier double underscore init ainsi.

Donc, disons que nous allons au fichier run.py, et que nous cherchons à importer quelque chose du fichier constants afin d'exécuter quelque chose avec succès.

Donc nous pourrions dire quelque chose comme from booking dot constants, import a par exemple, maintenant je sais que cette variable n'existe pas vraiment, donc nous pouvons la créer comme cela.

Et remarquez que maintenant je suis à l'intérieur des constantes.

Et si je retourne à run, alors nous sommes totalement bien.

Maintenant, avant de faire cela, laissez-moi aller au fichier double underscore init et dire, je vais d'abord imprimer.

Maintenant, ce que je veux dire ici, c'est le fait que peu importe quel sous-module vous importez depuis le répertoire de réservation, d'abord, le fichier double underscore init sera toujours exécuté.

Donc pour prouver cela, je vais exécuter le fichier run.py, qui importe simplement une variable du fichier constants.

Donc si je vais de l'avant et que je l'exécute, alors vous pouvez voir que nous avons reçu ce message.

Donc c'est un autre comportement important dont nous devons être conscients lorsqu'il s'agit de packages Python.

Et nous allons utiliser cet avantage dans notre projet également.

Mais je veux juste m'assurer que vous comprenez le comportement des packages Python.

Et maintenant nous sommes totalement prêts à aller de l'avant et à commencer à construire notre bot.

Maintenant, une sorte de mise en garde, avant de commencer, je ne recommande pas d'exécuter ce bot à l'état sauvage ou de l'exécuter toutes les quelques secondes, car cela pourrait conduire le côté serveur à désactiver automatiquement votre adresse IP publique.

Et ce n'est jamais agréable car alors vous devez contacter ce site web et expliquer que vous ne vouliez pas faire de mal.

Donc, c'est pourquoi, assurez-vous de donner suffisamment de marge lorsque vous testez votre bot sur ces grands sites web comme celui que nous allons utiliser, qui est booking.com.

D'accord, donc j'ai supprimé tout ce que je vous ai montré précédemment comme exemple.

Maintenant, nous sommes prêts à partir et à écrire notre classe.

Maintenant, je dis que nous allons rendre ce projet orienté objet.

Donc ce fichier que j'ai nommé booking.py va être responsable de la description des méthodes que nous allons appeler plus tard et ces méthodes vont prendre les actions que nous voulons que nos bots prennent.

Donc, commençons.

Maintenant, tout d'abord, nous voulons importer le WebDriver de la bibliothèque Selenium.

Donc nous pouvons créer une classe qui héritera de certaines utilités à l'intérieur de cette bibliothèque Selenium.

Donc nous allons commencer par dire from Selenium import web driver, et ensuite nous allons descendre les lignes.

Et nous allons dire class booking donc c'est en fait un bon nom pour notre classe.

Et maintenant cette classe va hériter de WebDriver dot Chrome.

Et la raison pour laquelle nous voulons faire cela, c'est parce que je veux que l'objet sale ait l'option d'utiliser à la fois les méthodes de WebDriver dot chrome et aussi les méthodes que je vais concevoir pour la classe booking elle-même.

Donc maintenant je peux aller à l'intérieur de notre classe et m'excuser pour ces barres obliques inverses et concevoir la méthode double underscore init.

Maintenant, c'est le constructeur de notre classe, donc cette méthode va être appelée immédiatement une fois que nous instaurons une instance de cette classe.

Donc nous allons dire def double underscore in it comme cela.

Et nous allons recevoir un paramètre que je peux nommer driver, Pat comme cela.

Et si vous vous souvenez, cela va stocker des informations sur l'emplacement de nos drivers.

Maintenant, juste pour nous faire gagner un peu de temps, je vais recevoir une valeur par défaut pour ce paramètre, qui va être exactement la valeur que j'ai utilisée tout au long des trois premiers épisodes de cette série de synonymes.

Donc ce sera all for rostering in I will open here, double quotes, et je vais dire C colon backslash, say lynnium.

Drivers comme cela, car c'est l'emplacement où j'ai le chrome driver.

D'accord, donc maintenant je peux descendre et dire self dot rival pad est égal à rival path.

Et plus que cela, je vais dire, super.

Et la raison pour laquelle j'utilise un super ici, c'est parce que je veux instancier la classe WebDriver dot chrome en cours de route.

Et la raison pour laquelle je veux faire cela, c'est parce que le constructeur va se plaindre de la manière dont la classe héritée n'est pas encore instanciée.

Donc c'est pourquoi je peux me permettre d'utiliser la méthode super pour le faire.

Maintenant, si vous ne m'avez jamais vu utiliser la méthode super, alors j'ai en fait une vidéo d'une série que j'ai créée il y a un an que vous pouvez regarder une vidéo qui est dédiée à l'héritage de classe.

Donc je vais mettre le lien dans la vidéo suggérée en haut.

D'accord, donc ce super va recevoir le nom de la classe actuelle comme argument, et ainsi que l'objet self.

Et maintenant je vais appeler la méthode double underscore init de la classe webdriver.com également.

Donc cette ligne va instancier avec succès une instance de la classe WebDriver dot chrome également.

Et pour le faire, allons-y et concevons un métal aléatoire.

Donc disons ici, quelque chose comme this land first page, et recevons self comme paramètre pour sûr, car c'est une méthode d'instance.

Et maintenant, si j'allais dire self dot get, alors vous pouvez voir que j'ai un accès complet aux méthodes de la classe WebDriver dot chrome.

Et vous pouvez voir que je peux également utiliser find element by quelque chose.

Et ainsi que l'utilisation de la méthode get.

Donc ces méthodes nous sont familières, car nous les avons vues au début de la série.

Donc c'est parfait.

Maintenant, j'ai une classe que je peux utiliser les méthodes Selenium pour jouer avec l'action que nous voulons prendre avec notre bar en ligne.

D'accord, donc je vais en fait utiliser cette méthode.

Et je vais pointer notre bot vers le premier emplacement où nous voulons le faire.

Et je vais utiliser ici la méthode get.

Et comme l'URL, je vais passer l'URL du site web sur lequel nous essayons de faire un bot en ligne.

Donc ce sera HTTPS, qui sera double w booking.com.

Maintenant, en fait, voici la raison exacte pour laquelle j'ai créé les constantes dot p y, ce que nous pouvons faire dans ce cas, cette valeur ici est probablement une valeur qui ne va pas changer.

Donc communément, parce que c'est le site web que nous allons toujours utiliser.

Donc c'est pourquoi déplacer cette valeur vers un fichier que j'ai déjà créé, comme constants.py est une idée parfaite.

Donc nous pouvons utiliser ce fichier en stockant quelques constantes.

Et par convention en programmation, lorsque nous avons des constantes, alors nous devons utiliser toutes les obligations.

Donc je vais dire base underscore URL est égal à l'URL exacte ici.

Et maintenant je peux revenir à notre booking.py.

Et je peux utiliser import booking dot constants comme cela as const, juste pour le rendre plus court et plus facile à lire.

Et je peux aller maintenant et dire const, dot base URL.

Et maintenant nous sommes prêts à continuer à partir d'ici.

Maintenant, en fait, avant de tester cela, si vous vous souvenez, avant d'avoir instancié la classe WebDriver chrome dans les trois premiers épisodes, alors nous devions faire quelque chose qui est assez obligatoire, sinon Selenium va se plaindre de ne pas avoir le chemin du pilote au niveau du système de la variable PATH.

Donc c'est pourquoi nous avons utilisé quelque chose qui ressemblait à toujours pensé à tort, si vous vous souvenez.

Donc faisons cela avant d'utiliser ce métal super, car sinon le cylindre va se plaindre de cette erreur.

Donc je vais monter ici, et je vais dire import always, et je vais descendre et je vais utiliser ici always dot envy Ron, et je vais accéder à la variable cat.

Et je vais utiliser plus égal.

Et puis je vais ajouter le self dot driver path comme cela.

Maintenant, si vous ne vous souvenez pas de ce que cela fait, envisagez définitivement de regarder le premier épisode peut-être pendant une minute ou deux.

Mais laissez-moi apporter le code du premier épisode.

Donc je suis à l'intérieur de mon dépôt sur GitHub que j'ai publié récemment, lorsque j'ai lancé la série.

Et si nous jetons un coup d'œil, alors vous verrez que j'ai utilisé au tout début, cette ligne qui ajoute ce chemin à la variable PATH.

Donc c'est pourquoi j'ai utilisé l'expression même à peu près à l'intérieur de notre classe.

D'accord, donc retournons à cinq messieurs et continuons.

Et maintenant, ce que nous pouvons faire, c'est aller à notre fichier run.py, et importer cette classe et créer une instance de celle-ci.

Donc nous pouvons vraiment utiliser ses méthodes comme land the first page.

Donc si nous allons au fichier run.py, et zoomons un peu, et disons, from booking, en fait, cela devrait être from booking dot booking, car nous voulons nous référer au nom du fichier également, nous voulons seulement importer la classe booking, que j'ai nommée ainsi.

Et maintenant je peux dire inst est égal à une instance de booking.

Et je ne vais rien passer car je veux utiliser la valeur par défaut de ce driver pad.

Et maintenant je peux vraiment essayer d'utiliser le premier métal que nous avons lancé.

Donc ce sera inst dot land first page.

Donc cette ligne va être responsable de faire en sorte que notre bot aille à la page d'accueil de booking.com.

Donc maintenant je peux exécuter le fichier run.py et tester si tout fonctionne.

Donc si je fais cela, alors voyons ce qui va se passer.

D'accord, donc vous pouvez voir que nous sommes à l'intérieur de la page que nous voulions être dès le début.

Et maintenant nous pouvons continuer à concevoir notre bot à partir d'ici.

Maintenant, il y aura des tonnes d'actions que nous voulons prendre pour remplir le formulaire de l'endroit où nous allons, ou la date à laquelle nous aimerions vérifier l'entrée et la sortie, ainsi que l'ajout de plus de personnes à nos vacances.

Donc la combinaison de toutes ces actions sera divisée en médailles d'instance.

Et le fait que nous fassions cela rendra notre code beaucoup plus lisible et maintenable.

Donc c'est pourquoi utiliser ici l'orienté objet est une idée parfaite, car il vous donne l'option d'étendre votre application, si vous voulez le faire plus tard.

D'accord, donc il y aura une autre chose très intéressante que nous voulons concevoir à ce stade.

Maintenant, vous auriez pu remarquer que bien que nous voulions seulement lancer la page d'index, nous avons toujours obtenu l'instance du pilote ouverte.

Donc ce que cela signifie, c'est que lors de notre prochain test, le navigateur Chrome sera toujours ouvert.

Et cela peut nous amener à avoir comme 10 ou même 20 navigateurs ouverts sur notre ordinateur.

Maintenant, parfois lorsque nous testons quelque chose, nous voulons immédiatement forcer la fermeture de notre navigateur une fois que le bot a terminé son travail.

Donc c'est pourquoi parfois nous voulons avoir le contrôle de savoir si nous voulons quitter l'application Chrome ou la laisser ouverte.

Donc c'est un bon candidat pour lequel nous aimons utiliser les gestionnaires de contexte, car l'utilisation des gestionnaires de contexte pourrait nous donner beaucoup plus de contrôle lorsque nous voulons démarrer quelque chose et lorsque nous voulons tout démolir.

Donc c'est pourquoi je vais utiliser les gestionnaires de contexte tout au long de ce projet.

Donc pour implémenter cela, je vais vous montrer ce qui doit être fait au niveau de la classe.

Et si vous n'avez pas encore entendu parler des gestionnaires de contexte, je vais donner ici une brève explication à ce sujet.

Mais en gros, si vous voulez en apprendre davantage, j'ai une vidéo qui est dédiée aux gestionnaires de contexte en Python.

Donc si vous voulez, envisagez définitivement de jeter un coup d'œil au lien suggéré.

Mais allons-y et couvrons cela.

Donc je vais aller au fichier booking.pi.

Et je vais utiliser deux méthodes magiques supplémentaires qui nous permettront de faire usage des gestionnaires de contexte.

Maintenant, la manière dont les gestionnaires de contexte sont utilisés au niveau de l'instance est en instanciant une instance d'une classe avec le mot-clé width et les outils similaires.

Ensuite, je vais diviser les volets maintenant, horizontalement, je crois, non, nous devrions faire cela, excusez-moi.

J'aimerais le faire verticalement.

D'accord, donc dans le volet de gauche, je vais avoir notre fichier booking.py et dans le volet de droite, je vais avoir le fichier rumbaut py.

Donc du côté droit, je vais maintenant tout supprimer et je vais dire Attendez, réservation comme cela en tant que conseil et ensuite je vais aller ici et je vais voir le conseil qui a atterri en premier.

Maintenant, la beauté d'utiliser quelque chose comme cela, c'est le fait que lorsque Python atteint la ligne à l'extérieur de l'indentation, il va exécuter certaines actions de démontage.

Et l'emplacement où nous aimerions définir ces actions de démontage sont par convention utilisés sous la méthode magique qui s'appelle level underscore exit.

Donc pour implémenter cela, je vais aller ici, et je vais dire là, double underscore exit.

Et je vais utiliser la suggestion de Python, car par défaut, elle reçoit quelques paramètres supplémentaires.

Et je ne veux pas tout gâcher.

Donc je vais simplement appuyer sur Entrée sur la suggestion de Python.

Donc maintenant je peux dire self dot quit.

Donc quit va être la méthode qui sera responsable de la fermeture du navigateur Chrome, une fois que nous avons terminé.

Maintenant, pour prouver cela, je vais exécuter cela.

Et je vais dire à l'intérieur de l'indentation, exiting, comme cela.

Et maintenant, essayons d'exécuter le fichier run.py une fois de plus, et voyons ce qui va se passer.

Donc je vais exécuter cela.

Et une fois que nous avons reçu la page, alors vous pouvez voir que nous avons exiting, et juste après, le navigateur Chrome s'est éteint.

Donc ce que cela signifie, c'est que lorsque Python sort de l'indentation de l'expression de poids, il exécute automatiquement la méthode double underscore exit, c'est ainsi que fonctionnent les gestionnaires de contexte.

Et avoir quelque chose comme cela, lorsque nous voulons tester plusieurs choses tout au long du développement de ce projet est parfait.

Maintenant, pour étendre l'option de savoir quand nous voulons le démolir.

Ou quand nous ne voulons pas le démolir, alors nous pouvons recevoir ici un paramètre supplémentaire.

Donc je suis maintenant dans le fichier de réservation, alors je peux dire tear down est égal à false par défaut.

Et je peux dire sous le modèle de sortie, quelque chose comme si teardown.

Donc cela fait référence à self dot teardown.

Et nous devons aller ici et dire self dot teardown equals to teardown et ensuite je peux utiliser ici une instruction if et dire self dot teardown.

Donc si cela est vrai, alors exécuter le self dot exit.

Mais si cela est faux, alors ne faites rien et laissez le navigateur ouvert.

Et maintenant, lorsque je veux démolir, alors je peux passer ici till now I'm equals to true, ou je ne peux pas le passer.

Et si je ne le passe pas, alors le navigateur restera ouvert.

Donc encore une fois, c'est un bon moyen d'avoir le contrôle de savoir si vous voulez fermer votre navigateur ou le laisser ouvert, allez peut-être parfois vous voulez tester autre chose, plutôt que de simplement tester le code Selenium.

Maintenant, laissez-moi aussi supprimer la ligne de sortie maintenant que nous avons compris cela.

Et je pense que ce sera tout sur le gestionnaire de contexte.

Donc j'espère que vous avez compris les concepts de fonctionnement des gestionnaires de contexte.

D'accord, donc à ce stade, nous avons quitté le tutoriel précédent, et nous avons compris dans l'épisode précédent, comment nous utilisons cette classe de réservation afin d'avoir plus de contrôle dans notre classe WebDriver chrome.

Et nous avons également conçu certaines méthodes qui pourraient être utiles, comme la méthode double underscore exit.

Donc nous pourrions avoir l'option d'utiliser des gestionnaires de contexte lorsque nous instaurons une instance de cette classe de réservation.

Et nous avons également conçu cette méthode ici, qui ressemble à poser la première page.

Et elle fait essentiellement atterrir le bot sur ces cons pensées base URL, qui est booking.com, qui se trouve dans le fichier constants.py.

D'accord, donc maintenant avant d'aller de l'avant et de comprendre quelles sont les prochaines étapes, laissez-moi faire deux actions supplémentaires qui vont être assez utiles pour avoir plus de contrôle.

Donc la première va être l'ajout de la méthode implicitement weight.

Et juste un rappel rapide, implicitement weight est le métal qui nous permettra d'attendre un certain temps jusqu'à ce que l'élément soit prêt sur le site web.

Donc si nous devions dire self dot implicitly Wait, et par exemple, passer ici 15 secondes, alors peu importe quelle méthode va être exécutée avec le préfixe de find element, alors elle va attendre environ 15 secondes.

Mais il pourrait aussi passer à la méthode find element suivante en moins de temps car nous n'aimons pas toujours attendre 15 secondes, et cette méthode va prendre la responsabilité de cela.

Et la deuxième ligne de code que j'aimerais ajouter ici va être self dot maximize window.

Et la raison pour laquelle je veux faire cela, c'est parce que je veux simplement avoir une apparence plus propre lorsque je teste le bot.

Donc maintenant, laissez-moi aller et exécuter notre fichier run.py.

Et maintenant vous pouvez voir que le navigateur web a été ouvert en fenêtre maximisée, donc c'est plus agréable.

Et vous pouvez également voir que nous sommes sur booking.com comme prévu.

D'accord.

Donc maintenant que nous avons fait cela, la prochaine étape ici sera probablement d'automatiser le clic sur Choisissez votre devise.

Maintenant, vous pourriez penser que nous devrions automatiser automatiquement Où allez-vous, ainsi que les dates de vérification de sortie, et la sélection du nombre de personnes que nous sommes, mais en fait, au début, il pourrait être une bonne idée de changer la devise.

Donc nous aurons une vue plus commune de toutes les offres qui vont résulter après que nous les ayons recherchées.

Donc maintenant, essayons de comprendre ce que nous devons automatiser.

Donc nous devons automatiser le clic sur cela.

Et juste après, nous devons automatiser le clic sur USD ou euro ou quelle que soit la devise que nous recherchons.

Maintenant, aux fins de ce tutoriel, je vais essayer d'automatiser le clic sur USD, car c'est en fait l'une des devises les plus populaires.

Donc c'est ce que nous devrions faire, nous devrions cliquer sur celui-ci.

Et juste après cela, nous devrions d'une manière ou d'une autre essayer de cliquer sur celui-ci.

Et ensuite vous pouvez voir que juste après avoir cliqué sur cela, la devise a été changée.

Et ensuite nous sommes prêts à essayer d'envoyer du texte dans la zone de texte Où allez-vous.

Donc maintenant, essayons de comprendre comment nous allons automatiser le clic sur cela.

Donc je vais cliquer avec le bouton droit et cliquer sur Inspecter.

Donc nous pouvons comprendre quel élément est responsable de l'affichage de ce bouton.

Maintenant, je ne suis pas sûr de pourquoi je dois le faire deux fois, toujours.

Mais je n'ai vraiment pas encore compris cela.

Mais si cela vous arrive aussi, alors peut-être essayez de le faire une fois de plus.

Et cela va colorier l'élément en arrière-plan bleu comme prévu.

Donc je vais le faire une fois de plus.

Et vous pouvez voir que ce bouton est en fait ce qui est responsable de l'affichage de cet élément de devise.

Donc maintenant, lorsque nous essayons d'identifier un élément avec selenium, nous devons toujours essayer d'être assez intelligents pour identifier cet élément dans l'expression la plus unique possible.

Maintenant, l'attribut de l'ID est en fait l'attribut le plus unique qu'un élément HTML puisse avoir, mais ce n'est pas toujours le cas, nous allons avoir un ID pour les éléments HTML.

Donc c'est pourquoi nous devons trouver d'autres approches pour trouver cet élément.

Et dans notre cas, peut-être que vous auriez pensé à trouver cet élément avec la classe est égale à be UI button.

Mais en fait, ce n'est peut-être pas la manière la plus intelligente de le faire.

Parce qu'il pourrait y avoir d'autres boutons avec cette classe, car les classes en HTML sont pour le style des éléments.

Donc plusieurs boutons pourraient avoir le même style.

Donc c'est pourquoi peut-être filtrer ce bouton avec le data tooltip text est égal à choose your currency est une expression plus unique que nous pouvons utiliser.

Donc maintenant, je vais copier cette expression d'ici.

Et je vais identifier cela avec la méthode CSS selector que nous avons apprise dans le troisième épisode.

Donc je vais revenir à pi charm.

Et en bas, je vais dire leur changement de devise.

Et je vais également recevoir la devise comme paramètre ici afin que nous puissions avoir l'option de changer pour une devise différente plutôt que le dollar américain.

Donc je vais dire devise.

Et en bas, je vais dire self dot find element by CSS selector.

Et je vais ouvrir et fermer et je vais appuyer sur entrer, car je ne veux pas rendre les lignes de code trop longues, donc c'est une bonne idée de les séparer de la manière suivante.

Et je vais maintenant ouvrir un code unique, et je vais utiliser le bouton et ouvrir et fermer les crochets.

Maintenant, si vous vous souvenez, c'est ainsi que nous avons l'habitude de travailler avec les sélecteurs CSS, nous avons d'abord écrit le type d'élément HTML.

Et ensuite, à l'intérieur, nous avons écrit l'expression que nous devrions filtrer ce bouton par, et cela va être data tooltip text est égal à choose your currency.

Et ensuite, c'est une bonne idée d'assigner cette expression entière à une variable.

Donc je vais dire currency, underscore element est égal à cela.

Et en bas, je peux dire currency underscore element dot click, donc cela automatisera le clic sur cela.

Maintenant, laissez-moi changer ce paramètre pour avoir une valeur par défaut.

Donc nous n'aurons pas vraiment à passer la valeur tout le temps.

Donc maintenant, je vais ouvrir le run dot p y sur le côté droit.

Donc laissez-moi diviser cela verticalement.

Et laissez-moi ouvrir cela ici comme cela, et ensuite laissez-moi appeler ces boutons.

Donc ce sera bought that change currency comme cela.

Et ensuite laissez-moi exécuter ce fichier run.py et tester les résultats.

Comme prévu, nous sommes sur la page d'accueil, et vous pouvez voir que nous avons automatisé le clic uniquement sur l'élément de changement de devise.

Donc c'est bien.

C'est une première étape pour atteindre notre objectif.

Maintenant, la prochaine chose que nous cherchons à automatiser est probablement le clic sur l'une des devises.

Et pour les besoins de ce tutoriel, laissez-moi d'abord montrer comment nous pourrions identifier l'USD.

Maintenant, à l'avenir, nous avons un paramètre qui reçoit le type de devise.

Donc peut-être pourrions-nous choisir à partir du fichier run.py, une devise différente que nous pouvons automatiser pour cliquer dessus.

Donc laissez-moi utiliser inspecter à nouveau.

Donc nous pourrions identifier cet élément.

Et maintenant, si je clique sur cet élément pour développer ses éléments innerHTML, alors vous pouvez voir que nous avons ce texte et ce texte également.

Mais en fait, le bouton entier provient de cette balise d'ancrage, car si je déplace ma souris ici, et que je la survole, alors vous pouvez voir que nous avons un fond vert entouré de notre devise.

Donc c'est pourquoi peut-être devrions-nous essayer de trouver cet élément a.

Et nous devrions utiliser quelque chose qui nous aidera à identifier cette balise a.

Maintenant, j'ai agrandi la vue de l'inspection ici pour que nous ayons une vue plus propre.

Et vous pouvez voir que nous avons ici quelques paires clé-valeur d'attributs à nouveau, maintenant je peux essayer de trouver le data model header async URL params, quelque chose comme cela, qui contient le texte qui ressemble à selected underscore currency est égal à USD.

Maintenant, je sais que nous n'avons pas appris à trouver des éléments qui contiennent certaines sous-chaînes.

Mais cela est en fait très facile avec la méthode du sélecteur CSS également.

Donc disons dans le diagramme circulaire comment nous pouvons faire cela, d'accord, donc en bas, je vais utiliser une nouvelle variable que nous pouvons nommer selected the currency element, et cela va être self dot find element by CSS selector.

Et ici, nous allons écrire l'expression à nouveau.

Donc ce sera des guillemets simples a, et ensuite nous utiliserons des crochets.

Et maintenant, nous allons utiliser cette longue expression qui va nous aider à identifier cet élément.

Donc ce sera data dash, modal dash, Heather dash, async dash, again, URL dash, Param, comme cela.

Je sais que c'est une longue expression.

Mais c'est en fait une excellente approche pour identifier cet élément.

Et cela va inclure une sous-chaîne.

Donc au lieu de faire égal à deux, nous devrions utiliser asterisk égal.

Maintenant, je sais que cela n'est pas quelque chose que j'ai couvert dans les trois premiers épisodes.

Mais maintenant nous savons comment nous pouvons essayer de trouver une expression qui contient une sous-chaîne.

Et c'est aussi facile que d'utiliser le signe asterisk près du signe égal.

Et ensuite, je vais utiliser ici des guillemets doubles.

Et je vais dire selected currency est égal à USD comme cela.

Maintenant, si vous vous souvenez, alors c'est en fait la valeur que cette clé longue avait dans cet élément que nous voulions automatiser.

Donc maintenant, nous pourrions dire selected currency dot click.

Et cela devrait être suffisant pour automatiser le clic sur la devise USD.

Maintenant, vous pourriez vous demander pourquoi vous avez codé en dur cet USD ici, au lieu d'utiliser le paramètre de devise.

Donc c'est un point merveilleux.

Et je vais juste le changer maintenant.

Donc je vais ajouter ici une chaîne formatée.

Et je vais me référer à la valeur de la devise comme cela.

Et ensuite, ce que je vais faire maintenant, c'est exécuter le fichier run.pi en divisant à nouveau les volets et en travaillant sur run.py et je vais passer en devise est égal à USD comme suit.

Et ensuite, cette ligne sera responsable de remplacer cette expression par la chaîne USD, et cela devrait être suffisant.

Donc testons cela.

Donc je vais exécuter notre programme.

D'accord, donc vous pouvez voir que la devise a été changée en USD.

Maintenant, nous pourrions également tester cela une fois de plus en essayant de cliquer sur une devise totalement différente.

Donc essayons de faire cela.

Donc ouvrons à nouveau le PI charm.

Et au lieu d'envoyer USD, envoyons GB P et exécutons notre programme à nouveau.

Et voyons maintenant ce qui va se passer.

D'accord, d'accord.

Donc encore une fois, parfait.

Donc comme vous pouvez le comprendre, nous avons identifié l'expression clé-valeur parfaite pour identifier l'élément de changement de devise et à partir d'ici, nous sommes prêts à avancer avec la prochaine étape que notre bot devrait faire afin de rechercher les meilleures offres.

D'accord, donc maintenant que nous avons terminé la méthode de changement de devise, concevons la prochaine méthode que nous devons faire maintenant.

Donc si vous vous souvenez, nous devons maintenant essayer d'identifier un élément pour envoyer du texte à l'élément de formulaire de texte de recherche.

Donc si nous exécutons notre automatisation, encore une fois, juste pour avoir le navigateur ouvert sur booking.com, et attendre que cette automatisation soit terminée, alors maintenant nous devons automatiser l'envoi de texte à cette zone.

Donc je vais inspecter à nouveau.

Et je vais essayer de trouver l'expression la plus intelligente possible pour envoyer le texte à ce champ de formulaire.

Maintenant, j'ai dit plus tôt dans ce tutoriel, que si nos éléments incluent l'attribut ID, alors c'est en fait l'attribut le plus fort que l'élément puisse avoir pour identifier son unicité.

Donc c'est pourquoi je vais identifier un élément par l'ID avec la valeur de s deux fois.

Donc maintenant je peux aller et dire dans une nouvelle méthode en Python, quelque chose comme ceci, select place to go quelque chose comme cela.

Et je peux recevoir un paramètre qui dira place to go.

Et maintenant je peux descendre et dire search field est égal à laissez-moi agrandir la police.

Donc excusez-moi si vous n'avez pas vu le texte très bien.

Donc je vais dire ici self dot find element by IE.

Et je vais trouver cela par s, deux fois comme cela.

Et au début, je vais faire quelque chose que nous n'avons vraiment pas vu avant, qui ressemble à search field dot clear.

Donc clear signifie nettoyer le texte existant.

Donc si un jour, nous voulons rechercher quelque chose deux fois, alors peut-être aurons-nous des restes.

Donc c'est pourquoi nettoyer tout le texte en premier lieu est une bonne idée avant d'écrire un nouveau texte frais.

Donc c'est pourquoi j'ai lancé la méthode clear.

Et ensuite, je vais utiliser search field dot send underscore keys.

Et je vais envoyer la place to go qui provient de ce paramètre.

Et ensuite, je vais aller à run the spy.

Et je vais dire bot dot select place to go.

Et utilisons ici New York comme premier lieu à visiter.

Et maintenant, voyons ce qui va se passer.

Maintenant, en passant, nous pourrions commenter le code de changement de devise, juste parce que nous ne voulons probablement pas l'exécuter à chaque fois que nous testons une nouvelle zone dans notre bot.

Donc je vais le faire dans une minute.

D'accord, donc vous pouvez voir que la minute où j'ai écrit du texte, nous avons reçu un menu déroulant.

Donc ce que cela signifie, c'est que nous devons maintenant aller et identifier le premier résultat de notre menu déroulant.

Et nous devons automatiser le clic sur celui-ci.

Donc c'est exactement ce que je vais faire.

Maintenant, je vais cliquer sur inspecter sur le menu déroulant.

Et je vais le faire une fois de plus.

Et vous pouvez voir que c'est la valeur que nous devons automatiser en cliquant dessus.

Donc c'est en fait un attribut avec la balise de API.

Maintenant, Li est en fait l'abréviation de list HTML field qui est généralement utilisé si nous voulons afficher une liste d'éléments.

Donc c'est pourquoi nous voyons cette balise avec le nom de Li.

Maintenant, nous devons à nouveau essayer de trouver comment nous allons cliquer sur ces Li.

Donc c'est cet élément, je crois Oui.

Et ensuite, si nous développons cela un peu plus, alors nous aurons une vue plus propre.

Maintenant, vous pouvez voir qu'à l'intérieur de chaque Li, nous avons un attribut qui dit data dash i est égal à une chaîne.

Maintenant, je sais que c'est difficile à voir.

Mais si vous regardez en bas à gauche, alors vous pouvez voir que lorsque je pointe sur cet élément, le premier résultat de notre menu déroulant est montré avec un fond vert.

Et si je déplaçais ma souris sur cet élément, alors vous pouvez voir qu'il pointe maintenant sur le deuxième résultat du menu déroulant.

Donc ce que cela signifie, c'est que la valeur data I est en fait comme un index de tous les résultats car le premier résultat a la valeur zéro et le deuxième a la valeur un et le troisième résultat a la valeur deux, et ainsi de suite.

Donc c'est pourquoi nous appelons l'élément d'identification avec l'expression de data dash i est égal à zéro.

Donc je vais ouvrir notre diagramme circulaire, et je vais dire juste sous select place to go quelque chose comme first result est égal à self dot find element by CSS selector.

Et notre expression va ressembler à l II et les crochets à nouveau, et ce sera data dash i est égal à zéro comme cela.

Et ensuite, après avoir fait cela, nous allons dire first resolved dot click comme cela.

Et ensuite, je vais laisser tout comme c'est, car ces lignes vont être responsables de cliquer sur le premier résultat.

Et c'est exactement ce que nous voulons faire.

Donc je vais exécuter run up UI, et tester les résultats une fois de plus.

Et j'ai oublié de décommenter cette section, donc excusez-moi pour cela.

Et maintenant vous pouvez voir que nous avons obtenu un résultat parfait, nous avons automatisé le clic sur le premier résultat du menu déroulant, et par conséquent, booking.com nous a automatiquement emmenés à la zone de vérification d'entrée et de sortie.

Donc voici l'endroit exact où nous pouvons déjà essayer d'automatiser la sélection des dates d'entrée et de sortie.

Donc c'est génial.

Et cela signifie que nous avons fait un travail merveilleux en identifiant comment nous appelons le clic sur cet élément spécifique.

D'accord, donc c'est l'étape à laquelle nous avons laissé le tutoriel précédent.

Maintenant, comme vous vous en souvenez, lorsque nous avons sélectionné l'emplacement où nous voulions aller, booking.com, par défaut, a fait apparaître la date de vérification d'entrée ou de sortie que l'utilisateur peut sélectionner.

Donc cela signifie que nous pouvons automatiquement essayer de sélectionner la date de vérification d'entrée, ainsi que la date de vérification de sortie.

Maintenant, le temps que j'enregistre, cette vidéo sera mai 2021.

Donc si pour vous-même, vous voyez un résultat totalement différent, cela signifie probablement que vous regardez cela à une autre date.

Donc les résultats vont être différents pour vous.

Mais je vais écrire une méthode qui sera suffisamment générique pour supporter n'importe quel type de date.

Donc, allons-y et commençons.

Donc nous devons d'une manière ou d'une autre cliquer sur deux dates, la première représentant l'entrée et la seconde représentant la sortie.

Donc je vais simplement cliquer sur cela, cliquer avec le bouton droit et dire inspecter, le faire une fois de plus.

Et ensuite je vais aller à la fenêtre d'inspection.

Et voyons comment nous allons automatiser le clic sur ces boutons.

Donc vous pouvez voir que c'est en fait celui-ci.

Et c'est un élément enfant de cet élément TD.

Maintenant, te D signifie table data.

Et ce que cela signifie probablement, c'est que cet élément fait partie d'une balise HTML plus grande appelée table, qui est conçue pour créer des tableaux HTML.

Et c'est aussi ainsi que cette page représente le calendrier.

Comme vous pouvez le voir, le tableau ici et lorsque je survole ma souris, vous pouvez voir qu'il est totalement coloré avec un fond bleu.

Donc maintenant, cela signifie que nous devons d'une manière ou d'une autre automatiser le clic sur celui-ci.

Et nous pouvons en fait utiliser un cercle à nouveau, en sélectionnant un élément avec data date égal à une certaine date.

Comme vous pouvez le voir, dans ce cas, c'est 2021 05 16.

Donc je vais copier cette déclaration, et je vais revenir à pi charm.

Et essayons d'automatiser cela.

Donc ici en bas dans booking.pi, juste où se trouve notre classe booking, je vais taper une autre méthode que nous pouvons appeler quelque chose comme select, shake.

Ou nous pouvons simplement l'appeler select date, quelque chose comme cela.

Et ensuite, nous allons recevoir deux paramètres comme check in date in the ainsi qu'une check out date.

Et nous pouvons descendre et nous pouvons dire check in element est égal à self dot find element by CSS selector.

Et cela va avoir comme argument, l'énoncé suivant.

Donc je vais ouvrir des guillemets simples, et je vais utiliser TD car c'est l'élément que nous voulons automatiser.

Et ensuite, nous allons ouvrir et fermer les crochets.

Et nous allons coller l'énoncé que nous voulons identifier par l'élément.

Donc maintenant vous pouvez voir que cette date est codée en dur ici.

Et je vais simplement utiliser une chaîne formatée et remplacer la valeur de codée en dur pour avoir la valeur de check in date, que nous recevons comme paramètre et cela a totalement du sens de descendre et de dire check in element dot click et ensuite nous allons faire exactement la même chose pour la date de check out car c'est ainsi que nous allons sélectionner une plage de dates pour décider des dates de nos vacances.

Donc je vais aller maintenant, je vais dire check elevate, element, excusez-moi.

Et cela sera égal à self dot find element by CSS selector une fois de plus.

Et je vais simplement utiliser la même déclaration comme nous l'avons fait avec check in.

Et je vais remplacer la date de check in par la date de check out.

Donc en bas, nous pouvons à nouveau utiliser l'élément de check out qui clique initialement assez pour décider de la date de check in et de check out.

Et la seule chose que nous devons faire maintenant est de revenir à notre run.pi et d'exécuter cette méthode en passant deux arguments.

Donc ce sera bought that select date, et nous allons passer check in date est égal à disons 2021 dash 05.

Pour mai, et puis ils ont le mois sera 16.

Et ensuite nous allons faire la même chose pour la date de check out.

Et nous allons passer 2021 05 23, par exemple.

D'accord, donc allons-y et testons notre programme.

Maintenant, nous comprenons que nous n'avons pas vraiment besoin de tester le changement de devise, car cela fonctionne.

Donc je peux me permettre de commenter cela juste pour l'instant.

D'accord, donc exécutons cela et voyons ce qui se passe.

D'accord, cela fonctionne très bien.

Et vous pouvez voir que nous avons les dates de check in et de check out.

Maintenant, laissez-moi dire quelque chose de très important ici.

En fait, disons que vous aimeriez automatiser la sélection de dates qui sont deux mois ou trois mois à partir d'aujourd'hui.

Donc c'est quelque chose que je ne vais pas montrer dans ce tutoriel, mais vous avez toutes les utilités pour l'atteindre par vous-même.

Donc disons que vous voulez sélectionner une date qui sera quatre mois à partir d'aujourd'hui.

Donc cela signifie que vous devez automatiser le clic sur ce bouton suivant trois fois.

Et ensuite vous aurez l'option de sélectionner une plage de dates, qui sera quatre mois à partir d'aujourd'hui, ce qui dans mon cas sera septembre 2021.

Je voulais juste mentionner que je sais que ce programme ne va pas supporter la sélection de vacances à des dates comme cinq mois ou six mois à partir d'aujourd'hui.

Mais encore une fois, vous avez tous les outils pour essayer d'automatiser cette action par vous-même.

D'accord, donc la prochaine chose que je vais montrer ici est comment nous pouvons sélectionner les adultes pour décider de nos vacances.

Et pour ce faire, nous devons d'abord simuler le clic sur cette zone.

Et ensuite, nous cherchons essentiellement à automatiser le clic sur ce signe moins, ou ce signe plus pour décider des adultes.

Maintenant, encore une fois, nous allons essayer d'écrire une méthode qui recevra essentiellement un paramètre avec adults count quelque chose comme cela.

Et ensuite, nous allons essayer de simuler la décision des adultes pour nos vacances.

Maintenant, je ne vais pas montrer pour les enfants ou les chambres, car cela va probablement être la même logique que nous devons répéter.

Mais encore une fois, vous avez l'option d'étendre votre robot de la manière que vous souhaitez.

D'accord, donc maintenant, premièrement, commençons par identifier cette zone entière ici.

Donc inspecter, et recharger à nouveau.

D'accord, donc nous cherchons l'élément qui va colorier toute la zone de ce bouton de sélection.

Donc je pense que ce sera ce label avec l'ID de XP, guests toggle.

Donc je sais que la police est un peu petite ici.

Mais c'est en fait ce qu'il dit ici.

Il nous dit HP guests toggle.

Donc je vais simplement copier cette valeur.

Et je vais aller à notre bot.

Et je vais descendre et écrire une autre méthode que nous pouvons à nouveau nommer quelque chose comme ceci, select adults comme cela.

Et ensuite, nous recevrons count comme paramètre.

Et nous verrons comment nous allons contrôler le nombre de nos adultes dans cette méthode.

Donc en bas, je vais dire selection element, quelque chose comme cela.

Et je vais utiliser self dot find element by ID, et je vais coller la valeur que j'ai copiée précédemment.

Donc vous pouvez voir que c'est XP double underscore guests double underscore toggle, et je vais simplement selection element dot click comme suit.

Maintenant, laissez-moi passer une valeur par défaut ici comme un.

Donc nous ne recevrons pas de flèches lorsque nous appellerons cela depuis run dot p y et ensuite je vais aller ici et je vais dire Bob dot select adults, quelque chose comme cela.

Et maintenant, voyons ce qui va se passer si nous exécutons notre programme.

Jusqu'à présent, nous devrions nous attendre à voir seulement cette page apparaître.

Je veux dire cette zone, pas la page et cela semble correct.

Cela semble fonctionner.

Donc nous pouvons continuer à voir comment nous allons contrôler les adultes pour nos vacances.

D'accord, donc maintenant nous devons d'une manière ou d'une autre contrôler comment nous allons sélectionner le nombre d'adultes.

Maintenant, cela pourrait être une action délicate à prendre, car disons que vous voulez partir avec trois adultes, alors cela signifie que dans ce cas, vous devez automatiser le clic sur le signe plus une fois car la valeur par défaut est deux.

Mais que se passe-t-il si un jour la valeur par défaut ne sera pas deux adultes sur booking.com, disons que la valeur par défaut va être changée en quelque chose comme quatre ou cinq, trois ou n'importe quel autre nombre.

Donc nous pouvons en fait être plus intelligents.

Plutôt que d'essayer d'automatiser le clic sur le signe plus, en fonction du nombre d'adultes que nous allons passer dans notre méthode.

Donc nous pouvons d'abord essayer de diminuer le nombre d'adultes à la valeur minimale.

Et ensuite nous pouvons avoir plus de contrôle sur le nombre de fois où nous devons vraiment cliquer sur le bouton d'augmentation.

Donc au début, nous pouvons écrire une logique pour diminuer le nombre d'adultes jusqu'à ce que la valeur atteigne un adulte, car c'est la valeur la plus basse d'adultes que nous pouvons avoir.

Et ensuite nous pouvons essayer de cliquer sur le signe plus, en fonction du nombre d'adultes qui est passé.

Donc c'est une manière plus générique de compléter ce type de tâche.

Et cela va être très intéressant à implémenter.

Donc je vais aller à notre PI Chairman, vous savez quoi, avant cela, nous devons comprendre comment nous allons cliquer sur le bouton quiz.

Donc faisons inspecter et voyons comment nous allons identifier l'élément de diminution.

Donc développons cela et voyons ce qui se passe ici.

Donc vous pouvez voir que lorsque je survole ma souris ici, alors ce bouton de diminution est coloré avec le fond vert.

Donc c'est le bouton que nous voulons automatiser le clic, et vous pouvez voir qu'il a une valeur unique de area label avec la valeur de decreased number of adults.

Et je crois que nous allons dire la même chose pour increased number of adults weight area label comme clé.

Donc je pense que ce devrait être celui-ci.

Donc si nous ouvrons cet élément, et voyons ses attributs, donc je vais juste me déplacer ici.

Et d'accord, le voilà.

Donc vous pouvez voir qu'il a area label increased number of adults.

Donc c'est l'approche que nous allons identifier ces boutons.

Et laissez-moi identifier cet élément par le sélecteur CSS.

D'accord, donc juste sous la méthode Select adults, nous allons utiliser quelque chose comme decrease.

Adults element est égal à self dot find element by CSS selector.

Et nous allons passer en bouton et ouvrir et fermer les crochets et identifier cet élément par l'énoncé clé-valeur que nous avons copié précédemment.

Et vous pouvez voir que c'est area label est égal à decrease number of adults.

Maintenant, nous devons d'une manière ou d'une autre simuler le clic sur ce bouton jusqu'à ce que le nombre d'adultes atteigne un, car comme nous l'avons dit, cela nous permettra d'avoir plus de contrôle pour décider du nombre d'adultes.

Donc pour cela, je vais utiliser while true, et ensuite à l'intérieur de cette règle while, nous allons écrire une instruction if qui va chercher la valeur du nombre d'adultes.

Et une fois qu'il atteint la valeur de un, alors nous allons sortir de notre boucle while.

Donc je vais dire ici while through.

Et je vais aller ici et corriger les indentations.

Et ensuite, je vais descendre et je vais dire decrease adults element thought click.

Maintenant, si je laisse le code tel quel, il va toujours essayer de cliquer sur le bouton de diminution, ce qui n'est évidemment pas ce que nous voulons.

Mais nous voulons une logique pour identifier si la valeur atteint le nombre de un.

Et si c'est le cas, nous aimerions sortir de la boucle while true.

Donc ce sera quelque chose comme si la valeur des adultes atteint un, alors nous devrions sortir de la boucle while.

Donc voyons comment nous allons identifier cela.

Donc je vais revenir à notre navigateur, et je vais chercher l'élément qui affiche la valeur.

Donc ce devrait être celui-ci où ma souris pointe, zoomez un peu pour que vous puissiez voir plus clairement.

Et vous pouvez voir que je pointe exactement ici.

Donc allons inspecter et vous pouvez voir qu'il dépend en fait de cet élément span.

Et vous pouvez voir qu'il a le texte de un.

Donc ce que cela signifie, c'est que nous pouvons essayer de trouver cet élément et voir quelle est sa valeur.

Maintenant, si j'ajoute ici plus, alors vous pouvez voir qu'il a été mis à jour.

Donc cela signifie que c'est l'élément exact dont nous avons besoin.

Maintenant, je peux en fait voir dans cette page d'inspection que nous avons plus d'éléments qui sont mis à jour avec le nombre d'adultes.

Et vous pouvez voir en haut dans l'entrée ici que je vais zoomer.

Donc vous pouvez voir que cet élément est en fait mis à jour en continu également.

Et la raison pour laquelle je veux sélectionner cet élément est en fait parce qu'il a un ID.

Et si vous vous souvenez, j'ai dit que l'ID est l'attribut le plus fort que l'élément HTML puisse avoir pour identifier son unicité.

Donc si je clique sur plus ici, et ensuite vous pouvez voir qu'il est mis à jour.

Donc je vais simplement trouver cet élément par l'ID de group adults.

Et je vais revenir à Python et voir ce que nous pouvons faire avec cet élément.

Donc je vais aller ici et dire, adults value element est égal à self dot find element by ID, et il devrait être la valeur de group adults.

D'accord, donc maintenant que nous avons le contrôle de l'élément qui affiche la valeur du nombre d'adultes, nous devons d'une manière ou d'une autre recevoir le défi des adultes.

Maintenant, c'est quelque chose que nous n'avons pas appris à faire, car nous n'avons appris que des actions comme cliquer ou envoyer des touches.

Mais nous n'avons pas appris à recevoir une valeur d'une clé dans les éléments HTML.

Donc cela va être en utilisant l'adults value element que nous avons identifié ici.

Et ensuite, cela va être en lançant une méthode appelée get attribute.

Maintenant, get attribute est en fait une méthode qui reçoit un nom de clé, et ensuite elle essaie de vous donner la valeur de l'attribut quelle qu'il soit.

Donc si nous retournons à notre navigateur, vous pouvez voir que nous devons travailler avec cette clé qui s'appelle value, car c'est ce qui affiche le nombre d'adultes, n'est-ce pas ? Donc nous avons besoin de cette clé.

Donc je vais aller ici et revenir à un diagramme circulaire et passer en valeur.

Et cette déclaration entière devrait donner le nombre d'adultes devrait donner le nombre d'adultes.

Donc je vais simplement commenter cela car le code commence à être plus complexe, donc nous pouvons nous souvenir de ce à quoi chaque ligne est responsable.

Donc en bas, je vais taper une conditionnelle et il sera beaucoup mieux si nous assignons cette déclaration entière à une variable séparée.

Donc je peux dire quelque chose comme adults' value est égal à cette déclaration entière.

Et laissez-moi juste écrire ici quelques lignes de séparation car nous voulons avoir un code plus organisé.

D'accord, donc en bas, je peux dire quelque chose comme si adults' value est égal à un comme cela, maintenant, je sais déjà que cette déclaration va nous donner une erreur, car par défaut, le get attribute retourne la valeur sous forme de chaînes.

Et nous ne pouvons pas écrire des conditionnelles si en comparant des chaînes à des entiers.

Donc nous allons convertir ces adults value en entier exactement ici.

Et ensuite nous allons vérifier si cela est égal à un.

Maintenant, une fois qu'il est égal à un, alors nous pouvons rompre la boucle while true.

Donc voyons si cette logique fonctionne.

Donc nous devrions aller de l'avant et tester le fichier run.py en l'exécutant.

Et nous devrions voir le nombre d'adultes être configuré à un adulte.

Donc maintenant, je vais tester cela.

Et d'accord, donc nous pouvons voir que cela fonctionne parfaitement, le nombre d'adultes a été changé à un.

Et la seule chose que nous devons faire maintenant est d'identifier ce bouton plus et de dire que nous aimerions avoir 10 adultes, alors nous aimerions lancer une boucle for qui va cliquer sur ce bouton neuf fois.

Donc retournons à pi charm et implémentons cela maintenant pour vraiment tester si cela fonctionne correctement, alors vraiment nous allons supposer que nous avons 10 adultes dans nos vacances.

Donc je vais simplement passer cet argument lorsque nous appelons cette méthode.

Donc maintenant, allons à notre méthode et minimisons cette règle while car nous avons fini de travailler avec elle.

Et nous pouvons dire increase button element est égal à self dot find element by CSS selector une fois de plus.

Et si vous vous souvenez, c'était un bouton avec la paire clé-valeur de area labeled est égal à et je vais ouvrir ces guillemets doubles et dire increase avec une majuscule.

I Number of adults avec une majuscule A, et ensuite je vais descendre.

Et je vais lancer une boucle for, en appliquant la fonction de construction de plage, afin que nous puissions vraiment avoir le contrôle du nombre de fois que cette boucle for va s'exécuter.

Donc je vais dire for i in range, et nous allons utiliser la plage de count, moins un, car si vous vous souvenez, j'ai dit que nous devrions diminuer cela de un pour vraiment atteindre le compte exact qui est passé ici.

Donc nous allons dire increase button element dot click.

Et c'est tout.

Maintenant, je ne suis pas sûr si vous le savez ou non.

Mais en fait, si vous n'allez pas vous référer à la variable qui est utilisée ici, alors par convention, vous n'avez pas vraiment besoin de passer un nom de variable comme I ou a ou quelque chose comme cela, vous pouvez simplement utiliser underscore comme cela et le laisser tel quel.

Et ce n'est qu'une convention en Python qui dit que nous n'allons pas utiliser la valeur de la variable.

Donc maintenant nous sommes prêts à tester l'ensemble du programme.

Donc je vais lancer notre fichier run.pi, et nous montrerons le C, le nombre d'adultes étant fixé à 10.

Donc si nous exécutons notre bot, et attendons une minute, d'accord, donc vous pouvez voir que cela fonctionne vraiment parfaitement. Au début, nous avons utilisé cette logique de sécurité pour configurer les adultes à un et ensuite nous avons le contrôle total du nombre d'adultes que nous aimerions configurer.

Maintenant, cela est vraiment générique et fonctionne parfaitement, car même si nous allons passer en count equals to one à partir de notre méthode, alors ce qui va finir par se passer, c'est qu'il va aller ici, et il va essayer d'appliquer une boucle for dans la plage de zéro, et il ne va jamais s'exécuter car si vous avez une boucle for avec une plage sur zéro, alors vous n'itérer sur rien.

Donc le nombre d'adultes va rester un.

Et c'est parfait.

Donc cette logique fonctionne vraiment.

Et nous sommes essentiellement prêts à aller de l'avant et à cliquer sur le bouton de recherche pour vraiment tester si nous allons recevoir des résultats.

Donc ce sera très facile, car par convention, chaque bouton de recherche sur n'importe quel site est principalement une paire clé-valeur qui dit type equals to submit quelque chose à ce moment-là.

Donc nous allons cliquer sur Inspect et voir si c'est la même chose pour ce site web.

Donc si nous développons cela, et allons ici et cherchons ce bouton, et vous pouvez voir qu'il a type equals to submit.

Donc encore une fois, nous pouvons automatiquement essayer de trouver un élément avec le sélecteur CSS avec le type HTML de bouton qui a cette paire clé-valeur.

Donc si nous retournons à Python, nous pouvons facilement créer une autre méthode que nous pouvons appeler click Search.

Et nous pouvons recevoir rien dans cette méthode car il n'y aura aucun argument que nous aimerions passer.

Et nous allons dire directement self dot find element by CSS selector.

Et nous devons trouver un bouton avec cette paire clé-valeur, et assigner cela à une variable comme search button.

Et ensuite, nous aimerions cliquer dessus.

D'accord, donc ici, je vais simplement appeler ce board dot click search, et voir si tout fonctionne correctement.

Maintenant, pour vraiment tester toute la logique, laissez-moi décommenter le changement de devise et changer cela en USD pour vraiment voir si tout fonctionne.

Et laissez-moi défier ce programme un peu et passer une autre date.

Donc nous pouvons peut-être dire ici 19, et passer ici 25.

Et vraiment tester si tout fonctionne et fonctionne correctement, même si j'ai personnalisé la valeur un peu.

Donc si nous exécutons notre programme, et ne faisons essentiellement rien, donc je ne vais pas toucher ma souris du tout, et voir si tout fonctionne.

D'accord, donc la devise, la date, les adultes, la recherche, parfait, juste parfait.

Tout fonctionne vraiment bien.

Et nous voyons quelques résultats sur différents hôtels de ce site web booking.com.

Et c'est juste excitant car nous avons vraiment des résultats qui arrivent ici.

Et dans les prochains épisodes, nous allons plonger dans des choses plus complexes car nous devons seulement identifier les meilleures offres et en disant meilleures offres, nous devons d'une manière ou d'une autre automatiser l'application de la filtration à ce résultat.

D'accord, donc ici vous pouvez voir que nous avons quelques résultats sur ce que nous pouvons vraiment réserver.

Mais comme nous pouvons le comprendre à partir de cette page, nous avons vraiment plusieurs options pour ce que nous pouvons filtrer pour améliorer les résultats que nous avons reçus.

Donc, dans le but d'appliquer certaines filtrations, nous allons devoir écrire certaines méthodes qui seront responsables de l'application de ces filtrations.

Mais le fait de les inclure dans cette classe de réservation pourrait nous amener à une situation où nous allons avoir trop de méthodes dans une seule classe.

Donc, c'est pourquoi nous allons essentiellement créer un nouveau fichier Python qui inclura certaines méthodes sur les filtrations, une fois que notre bot aura atteint la page des résultats, donc si nous retournons à notre Python maintenant, alors nous pouvons en fait concevoir notre projet de la manière suivante.

Donc laissez-moi ouvrir booking.pi.

Et nous pouvons descendre ici, et nous pouvons dire quelque chose comme, apply filtrations.

Et cette filtration devrait être filtrations.

Et celle-ci ira en fait de l'avant et instanciera une instance d'une autre classe qui pourrait être nommée quelque chose comme booking filtration, quelque chose comme cela.

Et ensuite dans cette classe, nous pourrions inclure certaines méthodes qui seront responsables d'aller de l'avant et d'appliquer ces filtrations avec le scillonien.

Driver.

Donc, allons-y et commençons à travailler sur une telle conception.

Donc je peux aller ici, et je peux dire, nouveau fichier, et je peux nommer cela booking underscore filtration.

Et ensuite à l'intérieur de cela, je peux écrire un commentaire, quel est le but de ces pages.

Donc ce sera ce fichier qui inclura une classe avec des méthodes d'instance qui seront responsables de l'interaction avec notre site web.

Après avoir obtenu certains résultats, pour appliquer des filtrations, afin que nous puissions vraiment comprendre de quoi parle cette page.

Et juste après cela, nous pouvons descendre et nous pouvons dire class booking filtration.

Et cette classe n'héritera de rien.

Donc nous pouvons aller directement à l'intérieur du constructeur.

Et en fait, le constructeur doit recevoir un paramètre.

Et ce paramètre va être en fait le driver que nous allons passer en argument car nous voulons également que cette classe travaille avec le WebDriver.

Donc si je vais à booking.pi, alors nous pouvons en fait voir que tout au long du processus d'écriture des méthodes, nous le faisons sur l'objet self.

Donc nous devons d'une manière ou d'une autre passer l'objet self à l'instance instanciée de cette booking filtration.

Donc cela va ressembler à quelque chose comme rival equals to self dans le futur.

Donc c'est pourquoi nous devons aller à notre booking dot filtration, et recevoir ici driver comme paramètre.

Donc avant de continuer à travailler sur celui-ci, laissez-moi rapidement corriger les flèches dans l'autre fichier.

Donc je vais écrire ici et passer à ignorer les flèches.

Et je vais aller à booking.pi.

Et je vais essentiellement monter en haut de ce fichier.

Et je vais dire from booking, dot booking filtration, import looking filtration comme cela.

Et je vais sauter ici, une ligne de plus.

Et je vais descendre ici.

Et je vais dire, filtration, quelque chose comme cela.

Et je vais instancier la classe booking filtration.

Et je vois que j'ai manqué le t ici aussi.

Donc désolé pour cela.

Et ensuite, nous pouvons décider de quel type de filtrations nous voulons appliquer dans cette méthode.

Donc c'est en fait une bonne façon de concevoir notre programme.

Parce que lorsque nous avons trop de méthodes dans notre classe, alors nous pourrions avoir du mal à maintenir notre code à long terme.

Donc c'est pourquoi concevoir les filtrations de la manière suivante pourrait être une excellente idée.

D'accord, donc maintenant que nous avons compris comment nous pourrions structurer les filtrations de réservation, voyons quelques bons candidats pour ce que nous pouvons filtrer par les résultats.

Et vous pouvez voir que nous pouvons appliquer une certaine notation par étoiles pour les résultats.

Donc ce sera la première méthode que nous allons écrire dans le fichier de filtration de réservation.

Maintenant, nous pouvons voir que nous avons cette boîte entière ici qui est responsable de nous donner toutes ces cases à cocher.

Donc j'aimerais d'abord travailler avec cet élément, car vous pouvez voir que nous avons quelques cases à cocher supplémentaires sur cette page.

Et je ne veux pas confondre ces cinq étoiles, par exemple, avec celle-ci, car cette même case à cocher apparaît également dans les filtres populaires.

Donc c'est pourquoi c'est une meilleure idée de prendre d'abord notre bot et d'identifier l'élément qui est responsable de l'affichage de toute cette zone.

Donc je vais essayer de cliquer sur Inspecter ici.

Et nous allons le faire deux fois.

Et vous pouvez voir que nous avons ce titre de catégorie de filtre.

Donc l'élément parent de celui-ci est probablement ce qui est responsable de l'affichage de toutes ces cases à cocher.

Et si nous prenons notre souris sur l'élément parent ici, alors vous pouvez voir que c'est exactement la boîte car elle dit aussi filter box dans son nom de classe et elle a aussi un ID qui dit filter on this coral class.

Donc c'est parfait, car nous pouvons essayer d'utiliser notre bot pour sélectionner cet élément avec cet ID.

Et ensuite, nous allons faire quelque chose de très spécial qui sera responsable de l'affichage de tous les éléments enfants de cet élément div.

Donc, allons-y et travaillons sur cela.

Donc je vais copier cette déclaration ici.

Et je vais revenir à notre PI charm.

Et vous pouvez voir que je suis à l'intérieur du fichier de filtration de réservation.

Donc, tout d'abord, nous devons assigner le driver à l'objet self de cette classe de filtration de réservation.

Donc ce sera self dot driver est égal à driver.

Et si vous vous souvenez, cela va toujours recevoir le driver original de la classe de réservation elle-même.

Donc c'est pourquoi je fais ce petit tour ici.

Et je peux lancer une méthode comme a fly star rating ici.

Et cela recevra self comme paramètre.

Et maintenant je peux utiliser quelque chose comme self dot driver, dot find element by ID.

Et l'ID devrait être filter underscore class, car c'est l'ID de l'élément que nous aimerions filtrer maintenant, remarquez comment nous n'avions pas de complétion automatique.

Et c'est très ennuyeux, car dans les bibliothèques qui sont très grandes, comme selenium, nous aimerions probablement toujours avoir une complétion automatique pour les différentes méthodes afin de rendre nos vies plus faciles.

Et la raison pour laquelle la complétion automatique ne fonctionne pas, c'est parce que ce paramètre n'a pas de type spécifique.

Maintenant, il y a en fait quelque chose en Python qui s'appelle typing.

Donc nous pouvons vraiment décider du type de paramètre pour travailler avec les complétions automatiques.

Maintenant, pour vous montrer un exemple de la façon dont les choses de typage fonctionnent, je vais utiliser, je veux dire, expliquer cela avec un type de variable plus familier que nous utilisons couramment et qui s'appelle une liste.

Donc disons que cette classe reçoit en fait une liste comme ma liste, et nous aimerions toujours passer ici une liste.

Mais si nous allons ici, et disons ma liste, alors nous n'aurons pas de complétion automatique pour des méthodes comme append, remove, et des trucs très liés aux listes.

Et encore une fois, c'est parce que ce paramètre ne connaît pas son typage.

Donc nous pourrions en fait faire quelque chose comme from typing import list.

Et nous pourrions aller ici, et nous pourrions dire que celui-ci va être list.

Et maintenant, si j'allais dire, dot, alors vous pouvez voir que j'ai une complétion automatique pour les méthodes de liste.

Dans la même approche, cela s'applique aux instances de driver de selenium, nous pourrions importer une bibliothèque pour décider de ce type de driver.

Et cela va être aussi facile que d'aller ici et de dire from Selenium dot WebDriver dot remote dot web driver import web driver comme cela.

Et laissez-moi supprimer les exemples car nous n'allons vraiment pas recevoir de liste comme paramètre.

C'était juste un exemple.

Et ensuite, je vais dire ici, call on web driver.

Et une fois que nous avons défini le type de ce paramètre driver, alors nous allons toujours avoir self dot rival dot et vous pouvez voir que nous avons ces complétions automatiques comme prévu, car maintenant l'objet self dot driver connaît son type.

Donc c'est pourquoi c'est très utile.

Et maintenant nous pouvons aller de l'avant et assigner cela à une variable afin que nous puissions la nommer quelque chose comme Star filtration box.

Et ensuite nous pourrions utiliser cela.

Et maintenant, la prochaine étape devrait être comment identifier les éléments enfants d'un élément que nous avons sélectionné.

Et c'est quelque chose que nous pouvons réaliser en utilisant les sélecteurs CSS.

Donc laissez-moi vous montrer comment cela pourrait être fait.

Donc star child elements, c'est mon nom de variable.

Et je vais maintenant utiliser self dot driver.

Et je vais utiliser find elements et non elements.

Donc je sais que c'est la première fois que nous utilisons plus d'un élément comme méthode.

Mais en fait, il y a aussi l'option de trouver plus d'un élément dans un site web.

Donc je vais utiliser find elements by CSS selector.

Et en fait, il y a une convention pour trouver tous les éléments enfants d'un élément donné et cela sera en utilisant le signe astérisque à l'intérieur d'une chaîne.

Maintenant, je veux que vous regardiez et réfléchissiez à ce qui ne va pas avec cette déclaration.

Donc nous allons de l'avant et disons self that rival et nous lançons.

Par-dessus cela, ces find the limits of ICS cert or method.

Donc cela finira par nous donner tous les éléments de cette page web entière.

Et c'est faux car nous ne voulons que les éléments de star filtration box element, je veux dire tous les éléments enfants.

Donc ce que nous pouvons faire, c'est supprimer ce self dot driver, et nous pouvons remplacer cela par Star filtration box.

Et ensuite cette ligne sera responsable de nous donner tous les éléments qui appartiennent à cet élément star filtration box.

Donc maintenant, nous pourrions aller de l'avant et utiliser quelque chose comme print when star child elements pour vraiment voir que nous avons des éléments stockés dans cette variable.

Et nous pouvons aller à booking dot p y.

Et nous pouvons également utiliser ici quelque chose comme filtration dot apply star rating.

Et si vous vous souvenez, nous n'avons pas utilisé cette méthode dans notre fichier principal, qui était run.pi.

Donc je vais aller ici, et je vais toujours exécuter what dot apply filtrations.

Et nous voulons laisser ici, cette méthode toujours en cours d'exécution.

Et ensuite, nous personnaliserons les méthodes que nous voulons exécuter dans cette méthode apply filtrations à l'intérieur du fichier booking.py.

Donc maintenant, exécutons notre projet entier.

Donc je vais exécuter run that pie et voir ce qui se passe.

Et dans une minute, je vais également vous montrer les résultats dans notre console, car nous imprimons quelque chose.

Donc attendons cela.

D'accord, donc si nous revenons ici, alors vous pouvez voir que nous recevons comme résultat pour la fin.

Maintenant, à l'intérieur de ces éléments, nous cherchons les cinq cases à cocher dont nous avons besoin.

Maintenant, si nous revenons au navigateur Chrome, encore une fois, j'ai en fait configuré quels sont les éléments exacts dont nous avons besoin.

Donc nous pouvons voir que j'ai développé ici, cet élément de filtre de classe.

Et si nous regardons un peu plus bas, donc si nous allons dans cette zone, alors ici, vous pouvez voir que c'est plus axé sur les cases à cocher.

Et à l'intérieur de cela, nous avons toutes ces balises huit.

Et ces balises huit sont ce que nous devons vraiment cliquer.

Et vous pouvez voir que chacune de ces balises huit a quelques classes enfants supplémentaires, je sais que cela a une structure très longue.

Et vous pouvez voir qu'à la fin, le innerHTML de l'un des éléments enfants est une étoile.

Donc ce que nous pouvons faire, nous pouvons essayer d'itérer sur ces éléments et chercher ceux qui ont la sous-chaîne de un, deux, ou trois, ou quatre ou cinq.

Et c'est la même structure pour toutes les autres étoiles.

Donc si nous allons et développons l'élément deux étoiles, nous pouvons en fait voir qu'il a à la fin innerHTML avec la valeur de deux étoiles.

Donc ce sont les éléments sur lesquels nous voulons cliquer.

Donc c'est pourquoi nous pouvons aller ici.

Et nous pouvons ouvrir le fichier de filtration de réservation.

Et nous pouvons travailler sur ces éléments enfants d'étoile en itérant sur chacun d'eux.

Donc nous pouvons dire quatre éléments d'étoile dans les éléments enfants d'étoile.

Et nous pourrions utiliser quelque chose qui ressemblerait à si star underscore element dot get underscore attribute.

Et nous devons recevoir l'attribut qui est vraiment responsable de l'affichage du texte interne.

Donc ce devrait être inner HTML comme cela.

Donc c'est une convention pour trouver les valeurs de ce qui se trouve à l'intérieur de ces balises HTML.

Par exemple, si nous devions avoir une balise qui ressemble à cela, et que nous avons une valeur comme gym, alors si nous voulons recevoir la valeur gym uniquement, alors vous devez lancer la méthode obligate attribute medal.

Et donc c'est pourquoi nous utilisons cette expression ici.

Et nous voulons voir si cette expression entière ici est égale à quelque chose comme une étoile, n'est-ce pas, c'est ce que nous cherchons.

Et bien sûr, je ne vais pas coder cela en dur.

Et en plus, nous allons recevoir utiliser quelque chose comme Star value.

Et nous voulons transformer cela en une chaîne formatée.

Et nous voulons changer cette valeur de l'outil comme cela.

Et si cette expression entière est vraie, alors nous voulons faire quelque chose.

Maintenant, avant d'aller de l'avant à l'intérieur de cette instruction if.

Laissez-moi écrire ici vite.

Tout d'abord, nous voulons convertir cette expression entière en une chaîne juste pour être plus en sécurité.

Donc je vais simplement faire cela et envelopper toute cette expression avec la méthode str.

Et je vais également lancer une méthode que vous avez peut-être vue auparavant et qui s'appelle strip.

Maintenant, cette méthode strip sera responsable de nettoyer tous les espaces blancs, car nous pourrions avoir des espaces blancs lorsque nous voulons voir les valeurs des fichiers innerHTML.

Et cela sera essentiellement responsable de nettoyer tous ceux-ci.

D'accord, donc maintenant je peux aller à l'intérieur de notre conditionnelle if et je peux dire star element, dot click.

Et la raison pour laquelle je peux faire cela maintenant, c'est parce que nous allons itérer sur les éléments.

Et si nous avons un élément dont le innerHTML est en fait star value stars, alors nous voulons probablement cliquer dessus.

Donc testons cela en action.

Donc je vais maintenant exécuter notre run bot p y.

Mais avant de le faire, nous devons aller à booking dot p y, car c'est là que nous utilisons l'application star rating.

Et nous devons passer une valeur star.

Donc, allons-y et essayons de cliquer sur cinq étoiles.

Donc je vais passer ici, et faisons ces mots-clés pour que nous puissions vraiment comprendre de quoi il s'agit.

Et maintenant, nous pouvons lancer notre bot à nouveau.

Donc, allons-y et faisons cela.

Et voyons ce qui va se passer.

Donc nous recherchons quelques résultats comme d'habitude.

Et ensuite, il devrait aller de l'avant et essayer de cliquer sur cinq étoiles.

Et si nous allons en fait en bas, alors vous pouvez voir qu'il clique ici.

Donc c'est parfait.

Et vous pouvez voir que celui-ci a également été activé.

Et c'est génial car nous avons vraiment pu atteindre notre objectif.

D'accord, donc maintenant que nous avons compris cela, il y aura une autre chose dans le futur que nous aimerions ajouter à cette méthode.

Parce que parfois, il est réaliste de rechercher des résultats qui sont du genre comme quatre étoiles ou plus, ou trois étoiles ou plus ou quelque chose de ce genre.

Donc c'est pourquoi nous devons d'une manière ou d'une autre recevoir comme paramètre, pas seulement une valeur de magasin, mais peut-être recevoir plus d'une valeur de magasin.

Et la manière dont nous pouvons y parvenir est en transformant la valeur de magasin en argument arbitraire.

Et c'est une manière de passer plusieurs arguments à un argument, en le faisant avec l'ajout d'un signe astérisque avant le nom du paramètre.

Maintenant, si vous ne savez pas profondément ce que cela fait ici, alors j'ai une vidéo qui explique quelle est la différence entre ajouter un signe astérisque près d'un paramètre et ajouter un double signe astérisque.

Et cela est couramment vu avec les orgs.

Ou peut-être avez-vous vu précédemment des clés w arms à double astérisque.

Et si vous ne savez pas ce que sont ceux-ci, alors j'ai une vidéo qui explique les différences entre ceux-ci dans la vidéo suggérée.

Donc, envisagez définitivement de jeter un coup d'œil à celle-ci.

D'accord.

Donc maintenant que j'ai changé cela pour être un argument arbitraire, laissez-moi changer cela en store values car ce sera un nom plus convivial pour ce type de variable.

Et je peux descendre et utiliser une déclaration comme for store value in store values.

Et je peux prendre tout mon code dans cette zone et l'insérer dans une nouvelle boucle for.

Donc ce sera quelque chose comme cela.

Et maintenant que nous avons fait cela, testons cela avec plusieurs valeurs de style.

Et la manière dont nous allons faire cela est aussi facile que d'aller à booking.py.

Et au lieu de passer une seule valeur, essayons de passer trois, quatre, et aussi cinq.

Donc nous devrions voir les résultats dont la note est de trois étoiles ou plus.

Donc si nous exécutons notre programme maintenant et attendons quelques secondes, alors voyons ce qui va se passer.

Comme d'habitude, nous voyons les comportements réguliers dans les résultats de recherche.

D'accord, donc si nous jetons un coup d'œil ici, alors vous pouvez voir que nous avons activé ces notes.

Et si nous regardons dans votre boîte de filtres, là, vous pouvez également voir qu'elle a été activée avec succès.

Donc nous avons fait un travail vraiment formidable en implémentant la notation par étoiles sur ce site web booking.com.

Et nous pouvons continuer à partir d'ici.

D'accord, donc vous pouvez définitivement comprendre qu'il n'y a pas de limite pour les filtrations que vous pouvez appliquer une fois que vous êtes dans la page des résultats.

Donc je vais ajouter une autre méthode pour les besoins de ce tutoriel, que je pense personnellement être très utile.

Et je pense que si nous avions l'option de faire en sorte que notre bot clique sur l'option de tri du prix le plus bas au plus élevé, alors ce serait très, très utile.

Donc si nous regardons la page des résultats, alors vous pouvez en fait voir qu'en haut nous avons quelques filtres supplémentaires ou en fait juste quelques utilitaires qui peuvent nous aider à personnaliser nos résultats, que vous pouvez voir que nous avons l'option de cliquer sur le prix le plus bas en premier.

Donc nous aimerions automatiser le clic sur cela.

Et je vais cliquer sur Inspecter.

Et vous pouvez voir que ce n'est qu'un bouton avec seulement cet attribut ici que nous devons trouver pour probablement cliquer dessus.

Et cela va être ce data ID est égal à price.

Donc nous pouvons prendre cette paire clé-valeur et trouver cette façon, le sélecteur CSS et essayer de cliquer sur celui-ci.

Donc nous pouvons revenir à notre diagramme circulaire, et en fait à notre fichier de filtration de réservation.

Et nous pouvons concevoir ici une autre méthode, et nous pourrions nommer cela sold price lowers first.

Et cela va simplement essayer de trouver un élément.

Donc nous pouvons le nommer simplement element.

Et cela sera égal à self dot driver, dot find element by CSS selector, et cela sera celui-ci.

Et cela va simplement recevoir Li car c'était l'élément pipe.

Et nous allons ouvrir nos crochets.

Et nous allons dire data ID est égal à, en fait, j'ai copié cette déclaration.

Donc excusez-moi pour cela.

Et je peux simplement coller data ID est égal à price, assurez-vous d'utiliser des guillemets doubles pour price.

Et ensuite en bas, je peux dire element thought click et ce sera tout.

Maintenant, si vous vous souvenez, ce n'est que la page où nous écrivons nos méthodes, mais nous ne les appelons pas vraiment à l'endroit où nous les appelons est à l'intérieur du fichier spoking dot p y dans la méthode apply filtrations.

Donc juste après avoir appliqué une chose de stockage, nous pourrions également vendre nos résultats.

Donc nous pourrions dire filtration, mais sold price lowest first et cela ne recevra rien comme paramètres.

Donc nous ne allons pas passer d'arguments.

Et maintenant, testons ce programme entier maintenant en action.

Et laissez-moi en fait tester notre programme et attendre et n'utiliser que quatre à cinq étoiles.

D'accord, donc si nous exécutons cela, alors et attendons un peu, voyons ce qui va se passer.

D'accord, donc vous pouvez voir que nous avons également activé le bouton price lowest first, comme vous pouvez vraiment voir que nous avons des résultats moins chers maintenant dans la première page.

Et si nous regardons dans notre filtration, alors vous pouvez voir que nous avons obtenu quatre étoiles et cinq étoiles.

Donc je pense que cela sera assez suffisant pour les filtrations que vous pouvez appliquer.

Si vous voulez voir des résultats utiles.

Bien sûr, il y a plus de choses que vous pouvez appliquer pour recevoir de meilleurs résultats.

Et comme vous pouvez le voir, la technique est assez similaire à la recherche des éléments avec les différentes méthodes que vous pouvez utiliser dans la bibliothèque Selenium.

D'accord, donc l'une des premières choses que nous allons faire dans cet épisode est de supporter l'exécution de ce projet, pas toujours à partir d'un ID, car dans certains cas, vous voulez seulement exécuter le bot pour qu'il effectue ses actions et reçoive certains résultats.

Et pour faire une telle action, vous ne voulez peut-être pas toujours l'ouvrir dans un IV spécifique.

De plus, parfois, exécuter des bots à partir de la ligne de commande est simplement plus confortable que d'aller dans pi charm et de pointer essentiellement vers votre projet.

Et ensuite, utiliser le raccourci shift fn pour exécuter votre projet, parfois le seul moyen de le faire à partir d'un terminal en exécutant Python, et ensuite en vous référant au fichier, dans notre cas, c'est run.pi.

Maintenant, je ne vais pas vous mentir, mais notre projet ne supporte actuellement pas un tel comportement.

Parce que nous avons cette ligne délicate à l'intérieur du fichier booking.py, qui va ajouter l'emplacement de notre chemin de pilote à la variable d'environnement PATH du système.

Maintenant, exécuter une telle ligne à partir de Python fonctionnera car Python sait comment prendre cette ligne et l'attacher à un processus Python et ajouter vraiment cet emplacement à la variable de chemin du système.

Mais lorsqu'il s'agit d'autres processus à partir desquels nous voulons exécuter le projet, par exemple, une interface de ligne de commande sous Windows, alors nous allons avoir quelques problèmes car nous devons ajouter l'emplacement de nos pilotes Selenium avant d'exécuter le projet.

Donc cela va être délicat à gérer au niveau du terminal.

Et je vais en fait vous prouver que notre projet ne s'exécutera pas avec succès si nous essayons d'exécuter le fichier run.py à partir d'un terminal.

Donc si vous vous souvenez, dans ce répertoire, nous avons ce fichier, que nous voulons exécuter.

Et si j'allais dire Python, run dot p y, alors vous pouvez voir qu'il se plaint de la manière dont le chromedriver exécutable doit être dans le chemin.

Donc je vais corriger cela.

Donc vous aurez la possibilité d'exécuter ce projet à partir de votre terminal.

Peu importe si vous travaillez dans un environnement Linux ou si vous travaillez dans un environnement Windows.

D'accord, donc la manière dont nous allons corriger cela est en utilisant des blocs try et accept.

Et nous pouvons en fait essayer d'exécuter ces lignes de code.

Et si nous avons des erreurs, alors nous pourrions toujours amener à nos utilisateurs que l'utilisateur doit exécuter une ligne à partir d'une interface de ligne de commande qui ajoutera ce dossier C Selenium rivals au système de variable de chemin.

Donc, allons-y et essayons de concevoir cela.

Donc je vais prendre toutes ces lignes de code ici, et je vais les indenter toutes.

Et je vais les envelopper avec le bloc try.

Maintenant, juste après cela, nous pouvons descendre ici, et nous pourrions dire, accepter toute exception.

Et nous pourrions prendre l'exception à l'intérieur d'une variable, quelque chose comme E, peut-être.

Et comme un démarreur, nous pourrions dire quelque chose comme print, il y a un problème ou l'exécution de ce programme à partir de l'interface de ligne de commande.

Donc c'est juste un bon début pour gérer les choses à l'intérieur du bloc except, bien sûr, il y aura quelques ajouts supplémentaires à l'avenir.

Donc je vais revenir à notre terminal, et je vais juste exécuter la même commande.

Donc ce sera python run.pi.

Et vous pouvez voir que maintenant nous voyons automatiquement ce message, il y a un problème d'exécution de ce programme à partir de l'interface de ligne de commande, car nous avons pu atteindre le bloc except, car nous avons vraiment des exceptions.

Mais dans certains autres cas, nous pourrions aussi avoir des problèmes directement dans notre bot.

Maintenant, toutes les exceptions du monde ne concernent pas le fait que le chromedriver n'est pas à l'intérieur du chemin.

Donc c'est pourquoi il est assez dangereux de sortir quelque chose comme cela pour toutes les exceptions qui vont se produire dans notre programme.

Donc c'est pourquoi nous devons vérifier que nous avons vraiment atteint ce message qui dit chromedriver executable needs to be in path.

Donc c'est pourquoi nous pourrions revenir à Python.

Et nous pourrions vérifier que le message est vraiment à propos de la manière dont il n'y a pas de dossier à l'intérieur du chemin du système.

Donc nous pourrions dire si str E.

Donc c'est une manière de mettre en cache le message d'exception.

Et nous pourrions revenir au terminal et vérifier les sous-chaînes de cette exception spécifique.

Donc si nous devions vérifier si ce in path est une sous-chaîne dans le message d'exception, alors cela signifie vraiment que le problème est à propos de la manière dont le chromedriver executable doit être impair.

Donc je vais revenir à pi charm.

Et je vais dire si impair à l'intérieur d'une chaîne comme cela, dans le message d'exception, alors nous pourrions descendre et nous pourrions imprimer ce message.

Mais si nous avons d'autres problèmes, disons que nous avons un problème avec selenium, disons que nous avons un problème de syntaxe, alors nous aimerions soulever le problème original.

Et cela est réalisable en disant simplement else.

Et en utilisant le mot-clé ou la phrase comme cela.

Maintenant, la minute où vous faites quelque chose comme cela, alors une fois que nous ne rencontrons pas ce problème spécifique, alors nous soulevons vraiment les exceptions originales.

Donc c'est une excellente façon de gérer les exceptions.

Donc maintenant nous pourrions vérifier que cela fonctionne.

Donc nous pourrions revenir à notre terminal.

Et nous pourrions nettoyer l'écran pendant une minute.

Et nous pourrions dire à nouveau, python run.pi.

Et vous pouvez voir que nous avons à nouveau reçu ce message.

Donc cela signifie que notre conditionnelle if fonctionne parfaitement.

Maintenant, pour être honnête, je vais changer ce message pour qu'il soit plus convivial.

Donc l'utilisateur pourrait comprendre quelle commande doit être exécutée pour ajouter l'emplacement de nos pilotes Selenium à la variable d'environnement de chemin du système.

Donc je vais prendre un extrait de code que j'ai préparé comme un message d'impression.

Et je vais simplement coller le même ici.

Et évidemment, vous pouvez prendre cela à partir de mon site web dans le huitième épisode de notre série entière.

Donc vous pouvez voir que ici j'ai un joli message d'erreur qui dit que vous essayez d'exécuter le bot à partir de la ligne de commande.

Et le backslash n est juste un caractère d'échappement pour sauter à la ligne suivante.

Donc dans la ligne suivante, nous disons s'il vous plaît ajouter le towpath vos pilotes Selenium et pour Windows utiliser cette commande.

Maintenant, je sais que cela semble un peu complexe.

Mais c'est en fait une commande Windows intégrée que nous pouvons exécuter pour ajouter plus d'emplacements à notre variable de système de chemin déjà existante.

Maintenant, comme je l'ai dit dans le premier épisode, notre variable d'environnement de chemin a déjà environ 50 ou même 100 emplacements que nous avons comme valeur.

Donc c'est pourquoi nous utilisons set path et nous ajoutons les chemins originaux.

Et en plus, c'est pourquoi nous avons un point-virgule, nous ajoutons notre chemin, qui sera C Selenium drivers ou n'importe quel dossier où vous avez configuré le chromedriver window et si vous utilisez Linux, alors vous devez exécuter cette ligne qui ressemble à peu près à la même.

Seul Windows inclut la commande set.

D'accord, donc maintenant nous pourrions exécuter cette commande et maintenant vous pouvez voir que nous avons un message très convivial.

Donc la seule chose que je dois faire maintenant est de prendre cela et de le coller et maintenant vraiment personnaliser le chemin que nous devons avoir.

Ajoutez ici.

Donc ce sera Selenium rivals, une fois de plus.

Et je ne suis pas toujours sûr s'il doit être ajouté avec une barre oblique à la fin ou non.

Donc je vais essayer les deux.

Et je recommande pour vous d'essayer les deux aussi.

Donc essayons cela et ensuite essayons d'exécuter Python run.pi.

Et vous pouvez voir que j'ai à nouveau reçu ce message.

Donc laissez-moi nettoyer l'écran et exécuter la même commande avec une barre oblique à la fin.

Et exécuter à nouveau python run.pi.

Et maintenant vous pouvez voir que notre bot fonctionne.

Et vous pouvez voir que tout fonctionne à peu près comme prévu, vous verrez que nous avons pu rechercher les résultats, vous pouvez voir que nous avons pu filtrer et aussi appliquer le tri.

Donc cela signifie que cela fonctionne parfaitement.

Et si nous regardons notre terminal, alors vous pouvez voir que nous avons en fait reçu quelques avertissements que nous allons vraiment corriger bientôt.

Mais dans l'ensemble, notre bot fonctionne parfaitement même si nous l'exécutons à partir d'un terminal.

D'accord, donc maintenant vous pourriez remarquer quelques avertissements étranges sur les retraits, écoutant notre localhost avec un port, etc.

Donc c'est en fait quelque chose que nous n'avons pas vu avant.

Mais en fait, lorsque nous travaillons avec des navigateurs comme Chrome, qui est dans notre cas, Chrome driver, alors chrome vient maintenant avec certains outils de développement.

C'est un ensemble d'outils de développement web intégrés directement dans le navigateur Google Chrome.

Et je pense que lorsqu'il reconnaît que nous exécutons un navigateur Chrome automatisé pour exécuter des cas de test, ou automatiser des sites web, alors il exécute déjà cet utilitaire.

Maintenant, dans ce tutoriel, je ne vais pas couvrir trop de choses sur leurs outils.

Donc c'est pourquoi nous pouvons nous permettre d'ignorer ces types d'erreurs.

Et pour ignorer ces types d'erreurs à ce stade, nous devons revenir à notre fichier booking.py, et ajouter quelques configurations supplémentaires à notre instance WebDriver.

Donc ce sera aussi facile que de revenir à pi charm et d'ajouter quelques lignes dans ce fichier ici.

Et si vous vous souvenez, nous avons une ligne qui dit super, qui est vraiment responsable de l'instanciation d'une instance de la classe héritée et ainsi que de la classe que nous écrivons juste à ce moment-là.

Donc c'est pourquoi nous devons personnaliser cette ligne, car nous devons passer quelques options supplémentaires à cette classe dont nous héritons.

Donc ce sera quelque chose comme cela.

Donc nous allons dire options est égal à web driver dot chrome options.

Et vous pouvez voir que c'est juste une classe intégrée que j'instancie.

Et ensuite je peux dire quelque chose comme options, dot add experimental option.

Et je vais écrire ici quelques chaînes qui seront responsables d'ignorer ces types d'erreurs.

Et je ne vais pas mentir, j'ai beaucoup cherché sur ces outils de développement.

Et pourquoi nous voyons ces avertissements.

Donc j'ai fini par prendre ce code à partir d'un sondage Stack Overflow, que je vais ajouter dans la description.

Donc vous pouvez jeter un coup d'œil plus approfondi à la discussion qui s'y déroule.

D'accord, donc ce sera exclude switches comme cela, faites attention que les switches est avec un S majuscule.

Et ensuite il y aura une valeur supplémentaire que je vais passer ici, qui sera acceptée à l'intérieur de la liste avec un élément et ce sera enable dash logging, comme cela.

Et une fois que j'ai fait cela, alors nous devons prendre les options, qui est égal à une instance de Chrome options.

Et nous devons passer cela dans la ligne d'initialisation.

Donc ce sera options est égal à options comme cela.

Et ensuite, une fois que j'ai fait cela, alors testons si nous voyons toujours ces logs.

Donc je vais ouvrir notre terminal.

Et je vais dire à nouveau, python run.pi.

Et je vais laisser notre bot tourner en arrière-plan.

Voyons ce qui se passe avec le terminal.

Et vous pouvez voir que maintenant, puisque nous ignorons ces types de logs, alors nous ne voyons vraiment rien.

Et vous pouvez voir que notre bot a terminé son travail.

Et c'est parfait, comme nous pouvons voir les résultats dans cette page du navigateur Chrome.

Donc c'est une façon dont nous pouvons ignorer ces types d'erreurs.

Et nous pouvons continuer à partir d'ici.

D'accord, donc maintenant que nous avons pu comprendre cela, alors il y aura une autre chose que nous aimerions tester à ce stade.

Maintenant, nous aimerions tester si nous allons vraiment voir l'exception originale, même si nous avons une exception qui ne concerne pas le fait que le chromedriver soit dans le chemin.

Donc c'est pourquoi faisons quelque chose de mal dans notre projet à dessein.

Donc je vais aller à notre PI charm et je vais dire ici a est égal à deux divisé par zéro comme cela.

Et nous devrions recevoir essentiellement une erreur de division par zéro avant même que notre bot ne commence.

Donc c'est pourquoi nous devons maintenant revenir à notre table.

Et nettoyons l'écran et essayons d'exécuter notre bot une fois de plus et voyons les résultats.

D'accord, donc nous pouvons voir que nous voyons maintenant l'exception originale, qui nous dit zéro division error, car nous avons vraiment essayé de diviser un nombre par zéro.

Donc nous allons avoir quelques flèches et vous pouvez voir comment notre récompense n'a même pas commencé à exécuter les lignes de code, car nous avions une exception précoce.

Donc c'est parfait.

Et c'est une excellente préparation pour l'avenir de ce projet de bot.

Et nous pouvons maintenant continuer à étendre notre application autant que nous le voulons, et même la tester avec un terminal.

Maintenant, la principale raison pour laquelle je voulais vraiment la possibilité d'exécuter ce projet à partir d'un terminal, c'est parce que si vous vous souvenez de l'aperçu du bot, alors nous aimerions visualiser les résultats des offres de manière agréable.

Donc l'utilisateur peut vraiment avoir une vue gravable sur les résultats des meilleures offres.

Et nous voulons probablement éviter de le faire avec le PI charm.

Et nous voulons probablement le visualiser bien avec le terminal.

Donc c'est pourquoi je veux la possibilité d'exécuter ce bot à partir de n'importe quel terminal, même si c'est un environnement Windows, ou même si c'est un environnement Linux.

D'accord, donc regardons le prochain élément que nous devons identifier afin de commencer à signaler les résultats à l'utilisateur qui utilise ce bot.

Comme prévu, je vais exécuter ce projet maintenant à partir du terminal.

Et je vais utiliser cette recommandation que nous avons générée dans la ligne d'impression.

Donc nous pouvons vraiment avoir le dossier des pilotes sous la variable d'environnement de chemin du système.

Donc je vais exécuter ces lignes.

Et comme vous pouvez le remarquer, j'ai remplacé ce chemin par mon chemin original.

Donc je vais exécuter cela.

Et juste après cela, je vais dire Python run.pi exactement comme l'épisode précédent.

Maintenant, juste un rappel, si vous vous souvenez, j'ai montré une exception à dessein à la fin du dernier tutoriel, et je l'ai supprimée, et c'était une erreur de division par zéro.

Donc assurez-vous de l'avoir supprimée.

Et ensuite, je peux revenir à notre navigateur.

Et vous pouvez voir que nous avons les résultats comme prévu et les filtrations et le tri sont assez bien.

D'accord, donc maintenant nous devons examiner cet élément important qui est responsable de l'affichage de tous les résultats.

Maintenant, je vais être honnête avec vous, je ne vais pas montrer comment vous pouvez voir tous les 170 résultats.

Mais nous allons juste chercher la première page pour les besoins de ce tutoriel.

Donc cela signifie que nous devons identifier un élément qui a 25 éléments enfants qui sont responsables de l'affichage de toutes ces boîtes qui affichent le prix des offres, le nom des hôtels et la note par étoiles et autres.

D'accord, donc commençons.

Maintenant, encore une fois, notre objectif va être de trouver d'abord cet élément parent qui est responsable de l'affichage de toutes ces 25 boîtes, chacune de ces boîtes étant responsable, comme vous le verrez, de l'affichage du nom de l'hôtel et de la note par étoiles et autres.

Donc, tout d'abord, laissez-moi essayer de trouver l'élément qui couvre à peu près toute la boîte.

Donc j'ai fait défiler jusqu'au premier résultat.

Et cliquons ici sur Inspecter.

Et je vais le faire deux fois.

Excusez-moi pour cela.

Et comme vous pouvez le voir, c'est par exemple le titre de la première boîte.

Et si je fais défiler un peu vers le haut, et ici, par exemple, nous ne voyons que la partie sans l'image, ce qui n'est à nouveau pas ce que nous voulons, nous voulons toute la boîte.

Et comme vous pouvez le voir, c'est celui-ci qui est responsable de l'affichage de toute la boîte.

Et si je minimise cet élément, et vous pouvez voir que maintenant si je déplace ma souris sur le second, alors vous pouvez voir que la seconde boîte a été couverte avec un fond bleu.

Donc cela signifie que ces balises div qui ont peut-être le data score, ou data or tail ID sont ce qui est responsable de l'affichage de chacune des boîtes.

Et vous pouvez également voir que l'élément parent de tous ceux-ci est une balise div avec l'ID de alternate list Enter.

Maintenant, avant d'aller de l'avant et de commencer à écrire cela dans le côté Python, laissez-moi vous montrer quelques astuces que vous auriez pu faire dans le côté JavaScript des pages web.

Maintenant, ne craignez pas JavaScript, je sais que c'est un langage de programmation que vous n'avez probablement pas pratiqué.

Mais je vais simplement faire une courte promenade à travers comment j'ai identifié lorsque j'ai développé ce projet, toutes ces 25 boîtes.

Donc allons à la console. D'accord, donc la console est en fait une zone où vous pouvez exécuter du code JavaScript pur qui sera responsable d'identifier chacun des éléments que nous cherchons.

Donc si nous allons à la console et Way, ignorons ce qui se passe ici.

Et laissez-moi zoomer un peu.

Donc vous pouvez tout voir.

Et je vais d'abord tout nettoyer ici.

Donc ce sera clair.

Et ensuite, c'est une méthode que nous devons exécuter.

Donc, comme cela, et ensuite vous avez une console propre.

Maintenant, pour récupérer tous les éléments qui sont responsables de l'affichage de cette page, alors nous pouvons utiliser l'énoncé document intégré.

Maintenant, cela vient à nouveau de JavaScript.

Donc ne le confondez pas avec Python.

Mais je veux juste faire une courte promenade à travers comment j'ai identifié les éléments dont j'ai besoin.

Donc vous pouvez exécuter une méthode qui est assez similaire à celle de selenium, et maintenant elle s'appelle get element by ID.

Maintenant, faites attention que E, B et le AI sont en majuscules.

Et ensuite, je vais dire ici, or fail list underscore inner.

Et si vous vous souvenez, c'était l'ID qui est responsable de l'affichage de tous les résultats.

Et je vais assigner cette expression entière à une variable, nous pouvons la nommer comme hotel list, et cela sera égal à cette expression.

Et vous pouvez voir que lorsque je clique sur Entrée, alors vous pouvez voir qu'il me retourne l'élément qui est responsable de l'affichage de toutes ces boîtes.

Maintenant, je vais à nouveau nettoyer l'écran et travailler avec la bibliothèque hotel list.

Et je veux dire la variable.

Et ensuite, par-dessus cela, je vais exécuter get elements by class name.

Donc II, B, C, et n sont en majuscules.

Et je vais trouver ici le nom de la classe qui est assez unique pour chaque boîte.

Donc j'ai en fait trouvé cette ASR underscore property, walk string comme unique par boîte.

Maintenant, vous pouvez voir que même avant que je ne l'exécute, cela va être responsable de me donner 25 éléments.

Donc ce que cela signifie, c'est que maintenant nous avons le contrôle de tous ces 25 éléments avec lesquels nous pouvons travailler.

Donc si j'appuie sur Entrée, alors vous pouvez voir que nous avons un résultat avec 25 éléments.

Donc encore une fois, c'est ce que nous devons faire du côté Selenium, nous devons d'abord trouver cet élément parent avec l'ID alternate list, inner.

Et ensuite, par-dessus cela, nous devons aller de l'avant et exécuter, find elements by class name, et nous devons passer cette valeur.

Donc traduisons ce que nous avons fait ici en Python.

Et je pense que le fait que je vous ai montré cela du côté JavaScript est juste une autre utilité qui pourrait être utile pour vous.

D'accord, donc nous sommes à l'intérieur de pi charm à l'intérieur du fichier booking.pi.

Et je vais simplement descendre ici et taper une autre méthode que nous pouvons appeler report results.

Et ensuite, à l'intérieur de cette méthode, nous allons dire self dot find element by ID, et il va recevoir hotel list on the score, Enter.

Et ensuite, par-dessus cela, nous allons exécuter dot find elements by class name.

Et en fait, divisons la ligne pour que nous ayons une vue plus propre.

Donc je vais faire cela ici.

Et ce by class name va recevoir comme argument ASR underscore property underscore block.

Et j'ai besoin d'assigner cette expression entière à quelques variables.

Donc nous pouvons la nommer artell underscore boxes, cela va être égal à celle-ci.

Et en fait, testons d'abord si cela fonctionne.

Donc je vais simplement dire return ortel boxes, et je vais aller à notre run.pi.

Et je vais dire print la longueur de bot dot report results.

Parce que si vous vous souvenez, cela retourne une liste.

Et nous voulons seulement voir la longueur de cette liste.

Et bien sûr, cela devrait nous retourner 25.

Et si c'est le cas, alors cela signifie que nous sommes prêts à continuer les actions ultérieures.

Donc je vais simplement aller à notre terminal.

Et je vais à nouveau exécuter Python run dot p y.

Et attendons les résultats de cela.

D'accord, donc les filtrations ont été appliquées.

Maintenant, si je vais au terminal, là, vous pouvez voir que nous recevons 25 en retour.

Donc cela signifie que nous avons fait un excellent travail en recevant toutes ces boîtes qui sont responsables de l'affichage des données sur les offres.

D'accord, donc maintenant que nous avons le contrôle de chacune des boîtes, nous devons d'une manière ou d'une autre essayer de récupérer les données spécifiques dont nous avons besoin.

Et évidemment, nous aimerions commencer par les détails du nom.

Donc nous devons trouver un motif pour obtenir le titre de toutes les 25 offres.

Donc essayons de les trouver.

Donc je vais ouvrir notre dernier navigateur et voir ce qui se passe ici.

Donc allons à notre première boîte et essayons de cliquer sur Inspecter. Et si vous vous souvenez, cela est sous les éléments que nous avons trouvés.

Donc cela signifie que nous pouvons itérer sur chacun des 25 boîtes.

Et nous pouvons essayer de trouver un élément par un nom de classe qui est égal à ASR dash hotel, underscore underscore name.

Donc je vais m'en souvenir et commencer à travailler sur celui-ci.

Maintenant, je veux commencer à travailler sur un nouveau fichier maintenant, car nous voulons avoir le rapport dans un fichier Python séparé pour avoir un projet plus organisé.

Donc je vais aller dans le répertoire de réservation.

Et je vais créer un fichier que nous pouvons nommer booking underscore report.

Et documentons d'abord ce que ce fichier concerne.

Donc ce fichier va inclure des méthodes qui analyseront les données spécifiques dont nous avons besoin à partir de chacune des boîtes de veau.

Donc cette explication est assez logique.

D'accord.

Donc en bas, nous allons avoir une classe qui sera responsable d'avoir quelques méthodes qui commenceront à afficher les données dont nous avons besoin dans un beau tableau.

Donc je vais commencer par dire class booking report.

Et ensuite, cela n'héritera de rien.

Donc nous sommes prêts à recevoir directement quelque chose à l'intérieur de notre constructeur.

Maintenant, ce qui a le plus de sens est probablement de recevoir comme paramètre, l'élément parent qui est responsable de l'affichage de toutes ces boîtes de deal.

Donc je vais recevoir comme paramètre quelque chose comme boxes section element.

Et ensuite, je vais dire ici, self dot voxels section element est égal à celui-ci.

Et ensuite, nous allons instancier une instance de celui-ci, et nous allons passer l'élément avec l'ID de a pill list, enter.

Donc, travaillons sur cela.

Donc je vais aller ici, et je vais utiliser from booking dot booking report, import booking report.

Et je vais descendre, et je vais dire report est égal à booking report et je vais passer les hotel boxes.

Excusez-moi pour avoir instancié cela avant celui-ci, c'est faux.

Donc je vais simplement corriger cela.

Et je vais simplement le déplacer et en fait remplacer cela par le return car nous ne voulons vraiment pas que cela retourne quoi que ce soit pour l'instant.

Donc je vais simplement l'instancier ici.

Et ensuite, je vais passer les hotel boxes comme cela.

Maintenant, j'aimerais en fait exécuter ces find elements by class name sur le côté booking report.

Donc je vais simplement couper cela d'ici, et ne passer que l'élément avec cet ID spécifique.

Et maintenant, laissez-moi supprimer cette ligne vide d'ici.

Et je pense que ce sera tout.

Donc plus tard, nous pouvons exécuter certaines méthodes de la classe booking report, comme je ne sais pas, display table, des trucs comme ça, je sais que cette méthode n'existe pas, mais je suppose simplement l'avenir de notre projet.

Donc laissez-moi supprimer cela.

Et en fait, il devrait y avoir une autre zone dont nous devons tout supprimer.

Et cela devrait être celle-ci.

Donc, supprimons également l'exécution d'ici et continuons à concevoir cela.

D'accord, donc maintenant je suis dans le fichier booking.py.

Et je vais simplement laisser tout ici tel quel.

Et je vais simplement continuer à travailler sur le rapport de réservation.

D'accord, donc maintenant que nous avons des éléments HTML à l'intérieur de cet élément de section de boîte, nous devons aller et exécuter find elements by class name par-dessus.

Donc nous aurons tous ces 25 éléments en retour.

Donc je vais simplement taper une méthode qui dira pull deal boxes, et cela recevra self comme paramètre.

Et je vais dire self, excusez-moi, cela devrait être self dot boxes, section element, dot find element by class name, et cela aura l'argument as ASR property block.

Et encore une fois, cela va simplement tirer tous ces 25 éléments.

Et ce que je veux faire maintenant, c'est instancier une autre liste à l'intérieur de notre méthode init.

Et je vais simplement dire ici, retourner à l'expression entière ici, et je vais dire dans la méthode init, self dot deal boxes est égal à pull self dot pull the boxes et ensuite nous aurons le contrôle de tous les éléments sous ce nom, ce qui est beaucoup plus logique.

Et je suis désolé d'avoir manqué le s juste après find the elements.

Donc, évidemment, ils devraient être find elements by class name, car nous aimerions tirer tous les éléments qui correspondent à ce nom de classe.

D'accord.

Donc maintenant que nous avons fait cela, alors encore une fois, vous avez peut-être remarqué que nous n'avions aucune complétion automatique à propos de find elements by class name.

Et c'est parce que nous n'avions pas de typage pour l'élément de la section des boîtes.

Et nous sommes déjà familiers avec ceux-ci depuis le septième épisode.

Donc maintenant, cela va être une action très similaire à ce que nous avons vu précédemment tout au long de la série et cela va être importer le typage pour la classe web element, et ensuite utiliser ce typage spécifique.

Donc je vais dire ici, from Selenium dot WebDriver dot remote, that web element, import web element comme cela.

Et ensuite, je vais dire que ces boîtes section element vont être de type web element comme cela.

Et ensuite, nous commencerons à avoir des complétions automatiques comme prévu.

D'accord, donc maintenant que nous avons fait cela, commençons à tirer les données dont nous avons vraiment besoin de chacune des boîtes.

Et comme un excellent début, nous aimerions d'abord tirer le nom de l'hôtel pour chacune des boîtes.

Et si vous vous souvenez, j'ai dit que nous avons une balise span spécifique avec ce nom de classe unique qui dit s our hotel underscore underscore name.

Donc je vais trouver tous les éléments avec ce nom de classe.

Donc ce sera en revenant à pi charm et en disant quelque chose comme leur full titles.

Donc encore une fois, recevez self ici comme paramètre.

Et ensuite, je vais itérer sur chacune des boîtes.

Donc ce sera pour deal box dans self dot deal boxes.

Et je vais dire deal box dot find element by class name, et nous allons coller la valeur ou la classe que nous cherchons, qui est ASR dash ortel, underscore underscore name.

Et ensuite, ce que nous aimerions faire avec cet élément, c'est tirer son inner HTML, car si vous avez remarqué ici, cet élément a le nom de l'hôtel à l'intérieur de son inner HTML, que vous pouvez vraiment voir à partir d'ici.

Donc ce sera aussi facile que de dire à cette expression, quelque chose comme cela.

Donc laissez-moi d'abord diviser cela en plusieurs lignes.

Et ensuite, je peux dire par-dessus cela dot get attribute.

Et nous aimerions recevoir le inner HTML de cet élément.

Et si vous vous souvenez, lorsque j'utilise le get attribute innerHTML, j'ai également exécuté une méthode qui sera responsable de supprimer tous les espaces blancs.

Et si vous vous souvenez, c'était dot strip, comme cela.

Et cela sera tout, cette expression entière devrait vraiment afficher les noms des hôtels.

Donc laissez-moi d'abord assigner cette expression entière à une variable comme hotel name, ou deal name, cela n'a pas vraiment d'importance.

Et ensuite, nous pouvons essayer d'utiliser ici, print hotel name et voir si cela fonctionne.

Maintenant, si vous vous souvenez, pull titles n'est appelé nulle part.

Donc je vais simplement aller à working dot p y.

Et je vais lancer les méthodes dont nous avons besoin pour signaler les résultats dans cette méthode report results.

Donc ce sera report dot full titles.

Et maintenant, voyons ce qui se passe dans le fichier run.py.

Et si vous vous souvenez, nous avons supprimé la section report results.

Donc dans ce cas, ce sera what that report results.

Et je vais laisser tout ici tel quel.

Et maintenant, notre Ward devrait être responsable de l'affichage de tous les noms des hôtels.

Donc si nous allons à notre terminal, et disons, à nouveau, Python run.pi, alors voyons les résultats.

Et comme prévu, nous changeons la devise, nous ajoutons new york et un adulte, et nous appliquons les filtrations.

Et nous avons vu les prix.

Et maintenant, voyons ce que nous avons dans le terminal.

Et vous pouvez voir que nous avons vraiment tous les noms des hôtels, nous avons vraiment tout ce dont nous avons besoin.

Donc nous avons ici 25 hôtels, et voyons en fait si le tri correspond à notre convention.

Donc le premier hôtel devrait être ici à New York City Times Square.

Et si nous allons ici, vous pouvez voir que cela ne correspond pas tout à fait.

Et je connais la raison pour cela car parfois vous devez probablement actualiser après avoir reçu ces types de résultats.

Et nous ne voulons probablement pas exécuter le polling de chacun des titres trop rapidement.

Et ils se souviennent que c'était un contournement.

Que j'ai appliqué lorsque j'ai développé ce projet avant de vous le présenter maintenant.

Donc ce que je vais faire avant de tirer les résultats, je vais simplement déclencher un rafraîchissement de cette page.

Donc le bot aura une seconde ou deux pour tirer les données correctement.

Donc je vais simplement dire ici, bot dot refresh.

Et ce contournement devrait faire l'affaire.

Donc je vais simplement dire ici, un travail pour plate our bot to grab the data properly.

Maintenant, laissez-moi essayer d'exécuter notre bot une fois de plus et voir maintenant si cela va fonctionner comme prévu.

Maintenant, je pense que la raison pour laquelle cela se produit, c'est parce que nous essayons de tirer les données.

Et ce holding n'a pas terminé son travail.

Donc il est logique de tout rafraîchir avant de vraiment essayer de tirer tous les titres.

Donc, nettoyons simplement l'écran et disons python run.pi.

Et attendons encore quelques secondes.

D'accord, donc maintenant le premier hôtel est appeal Edison Times Square.

Et si nous allons à notre terminal, alors vous pouvez voir que le premier hôtel est hotel Edison Times Square.

Et le second devrait être Holiday Inn.

Et le troisième devrait être Paul Times Square.

Donc vérifions cela.

D'accord, donc je pense que maintenant les résultats sont affichés comme prévu, ce rafraîchissement donne vraiment à notre bot une seconde pour respirer, et pour tirer les données dans l'ordre que nous voulons.

Maintenant, je veux faire quelque chose d'important avant de continuer avec ce tutoriel.

Et cela sera de changer la quantité de la date de check-in et de la date de check-out.

Et c'est parce qu'il s'est écoulé une semaine ou deux semaines depuis que j'ai enregistré le dernier épisode de cette série.

Donc je veux juste m'assurer que les dates vont correspondre à la date d'aujourd'hui.

Donc c'est pourquoi je vais simplement sauter la date d'un mois seulement en changeant ces 206 à la place de 05.

D'accord, donc maintenant nous sommes prêts à continuer à personnaliser les données dont nous avons besoin.

Maintenant, nous avons dit que nous aimerions personnaliser les données dans un beau tableau, où nous allons afficher le nom de l'hôtel et le prix et aussi stocker le score de l'hôtel, ce qui signifie que la note pourrait être une excellente idée.

Donc si vous vous souvenez, nous avons terminé par personnaliser à l'intérieur du fichier de rapport de réservation, cette méthode pull titles et celle-ci est en fait en train de passer sur chacune des boîtes de deal et essaie de tirer certains attributs qui vont être utiles pour nous.

Donc nous pourrions tirer parti du fait que nous itérons sur chacune des boîtes de deal.

Et nous pourrions en fait essayer de tirer le prix et le score en cours de route.

Donc c'est pourquoi je vais supprimer la ligne d'impression d'ici.

Et je vais simplement commenter ce que je fais à chaque étape d'itération.

Donc je vais commenter ici, suivant le nom de l'ortel.

Et ensuite, plus tard, je vais également changer le pole titles en une fonction plus générique comme pull deal box attributes quelque chose de ce genre.

Et maintenant, je vais passer et commencer à tirer les prix.

Maintenant, pour gagner du temps, je vais simplement montrer ici, quelle était l'approche pour trouver le prix sur chaque boîte de deal.

Et ainsi que comment j'ai trouvé le score de chaque hôtel.

Donc c'est pourquoi je vais dire ici hotel underscore price.

Et cela sera égal à do underscore box dot find element by class name.

Et ensuite, la valeur ici sera donc ouvrons des chaînes.

Et ensuite, je vais dire V UI dash price dash display, underscore underscore value.

Et donc si j'ai une classe avec cette valeur, alors cela signifie que cela va nous donner le prix.

Donc c'est pourquoi je peux me permettre de faire cela.

Maintenant, je vais utiliser la même approche pour obtenir l'attribut innerHTML.

Et la seule chose que l'espace blanc est et si nous nous souvenons, nous avons fait cela dans le nom de l'hôtel également.

Donc je vais copier cela et le coller ici et cette ligne, je veux dire ces trois lignes seront responsables de tirer le prix de l'hôtel.

Et ensuite, si nous descendons en bas, et nous disons aussi ici hotel score, et cela sera par deal box, dot get attribute et il y a une excellente raison pour laquelle j'utilise ici get attribute et non me dot wait find element by quelque chose.

Et c'est parce que cet élément a déjà un attribut HTML qui ressemble à data dash score.

Et donc ce que cela signifie, c'est que si nous devions tirer seulement la valeur de cet attribut ici, alors cela signifie que nous allons recevoir le score de l'hôtel sur une échelle de 10.

Et donc le score de l'hôtel pourrait être 8.5 9.1 9.5, et ainsi de suite.

Et donc maintenant que j'ai fait cela, alors encore une fois, j'aimerais nettoyer les espaces blancs.

Donc juste pour la sécurité, je vais lancer votre dot strip, comme nous l'avons fait précédemment avec le prix et les noms des hôtels.

D'accord, donc maintenant que nous avons un nom, un prix et un score pour chacune des boîtes de deal, alors testons d'abord notre problème.

Maintenant, je vais faire quelque chose qui pourrait vous sembler étrange.

Mais je vais expliquer dans une minute pourquoi je fais cela.

Donc pour tester cela, je vais monter ici, et je vais utiliser une liste que je veux nommer quelque chose comme collection.

Et cela sera égal à une liste vide.

Et ensuite, à mesure que nous continuons à itérer sur le nom, le prix et le score, je vais avoir besoin d'ajouter ces attributs à cette collection.

Donc nous pourrions avoir des données organisées et structurées.

Et je vais utiliser des listes imbriquées ici où la collection sera la liste.

Et cela inclura plusieurs listes.

Et chaque liste qu'elle aura va inclure les trois éléments et l'un d'eux sera le nom, l'autre le prix.

Et le troisième sera le score.

Donc je vais utiliser ici quelque chose comme collection, dot append, et ensuite je vais ajouter à cela une autre liste.

Et ensuite, je vais dire hotel name, alltel price, et l'autre devrait être hotel score.

Et maintenant que j'ai fait cela, alors je veux vraiment tester si j'ai toutes les données que je voulais tirer depuis le début.

Donc je vais utiliser ici return collection.

Et je vais aller à notre fichier booking.py.

Et je vais chercher la méthode où nous signalons les résultats.

Et je pense que cela devrait être ici.

Et ensuite, je vais lancer ici la méthode que nous venons de finir de concevoir.

Et cela va être pull deal box attitudes.

Maintenant, si vous vous souvenez, nous utilisons des déclarations de retour.

Donc lorsque nous exécutons cette ligne, directement, alors nous ne allons pas voir quoi que ce soit.

Donc nous allons devoir envelopper cela avec l'instruction print intégrée afin que nous puissions voir les données.

D'accord, donc maintenant que nous avons fait cela, alors ouvrons notre terminal et testons les résultats.

Donc je vais amener notre terminal ici.

Et je vais dire Python run dot p y, et voyons si tout va fonctionner correctement.

Maintenant, laissez-moi déplacer le navigateur web vers l'écran.

Et voyons ce qui va se passer.

D'accord, donc le bot est en cours d'exécution.

Et maintenant, nous devrions voir dans la console de notre terminal le résultat.

Donc je vais l'ouvrir.

Et zoomons un peu pour que nous puissions comprendre ce qui se passe ici.

D'accord, donc vous pouvez voir que nous avons une sortie un peu étrange.

Mais laissez-moi décomposer ce qui se passe ici.

Donc vous pouvez voir que les premiers et derniers caractères sont en fait des crochets, car c'est la collection de données que nous avons maintenant.

Et vous pouvez voir que cela inclut la liste de tout d'abord, et ensuite le deuxième hôtel et ensuite le troisième hôtel et ainsi de suite.

Maintenant, je ne suis pas sûr de pourquoi nous voyons ici une chaîne vide.

Et c'est probablement parce que ce Webster square Tony, ils n'ont pas de score.

Donc c'est pourquoi c'est une liste vide.

Et vous pouvez voir qu'à mesure que je continue, nous avons des listes à l'intérieur d'une liste plus grande, chaque liste représentant une collection de données sur le nom de l'hôtel, le prix de l'hôtel, et aussi le score de l'hôtel.

Et c'est un bon début pour visualiser nos données avec la bibliothèque pretty table dont j'ai parlé au tout début de la série.

Et encore une fois, cette bibliothèque va nous aider à visualiser les données dans un beau tableau divisé en colonnes et en lignes.

Et maintenant, voyons ce que nous devons faire pour pouvoir visualiser nos données plus joliment.

D'accord, donc allons-y et voyons comment visualiser nos données maintenant.

Donc je vais nettoyer l'écran, et je vais installer une bibliothèque qui s'appelle pretty table.

Donc ce sera pip install pretty table comme cela.

Maintenant, pour ceux qui demandent pourquoi je n'utilise pas l'environnement visuel ici, maintenant, parce que j'installe une bibliothèque sur l'interpréteur système, vous pouvez aller de l'avant et le faire.

Parce que cela vous aidera à avoir un environnement organisé pour ce projet spécifique.

Je ne me sens pas comme passer par quelque chose en quelques secondes, au moins si je n'ai pas un tutoriel complet sur cela sur ma chaîne.

Donc c'est pourquoi je vais installer directement ces packages dans l'interpréteur système et je vais m'appuyer sur cela pour ce projet.

Mais si vous vous sentez à l'aise avec les environnements virtuels, alors je vous accueille vraiment à le faire car c'est une manière plus agréable d'organiser vos projets sur votre machine.

D'accord, donc maintenant je vais utiliser cette ligne.

Et vous pouvez voir que j'ai installé cela, donc cela signifie que nous pouvons travailler avec cette bibliothèque.

Donc maintenant je vais revenir à notre PI charm et voir comment nous pouvons travailler avec cela.

D'accord, donc maintenant que nous avons la collection de données ici, alors nous allons écrire ici quelques lignes de plus pour afficher cela dans un tableau.

Donc je vais faire défiler vers le haut.

Et je vais importer la bibliothèque pretty table.

Mais je vais importer seulement une classe de cette bibliothèque.

Donc ce sera from 3d with the table, import free t table comme suit.

Et ensuite, nous devons instancier cette classe.

Et donc ce sera ici.

Donc je vais dire ici quelque chose comme cela.

Donc je vais utiliser ici table est égal à 50 table, et celui-ci va recevoir quelques arguments.

Et le premier est très important, qui est les noms de champ.

Maintenant, j'ai dit que dans le tableau, nous allons avoir des colonnes.

Donc dans notre cas, nous voulons probablement déclarer ici, trois colonnes.

Et la première sera le nom et ensuite le prix et ensuite le score.

Donc je vais passer ici directement une liste qui va ressembler à ce qui suit.

Donc je vais utiliser ici, alltel name, et ensuite je vais utiliser hotel price.

Et ensuite je vais utiliser hotel score comme cela.

Et encore une fois, ceux-ci vont être utilisés comme les colonnes.

Donc laissez-moi utiliser en fait un paramètre de mot-clé ici afin que nous puissions comprendre.

D'accord, donc maintenant que j'ai passé cet argument, alors nous devons aller de l'avant et créer quelques lignes dans notre tableau.

Donc ce sera aussi facile que d'utiliser la méthode Add rows.

Et ensuite, nous sommes autorisés à passer une collection de données.

Et devinez ce que nous allons passer dans la liste imbriquée que j'ai créée il y a quelques minutes.

Donc c'est pourquoi ici, j'utilise une liste imbriquée.

Donc cela rendra nos vies très faciles.

Donc maintenant, la seule chose que nous devons faire dans ce fichier booking.py sera table dot add underscore rows.

Et ensuite, nous pouvons passer ce que cela retourne ici.

Donc ce sera simplement copier et coller cela juste là.

Et ensuite, je vais le laisser tel quel.

Et en fait, nous devons imprimer le tableau lui-même.

Donc excusez-moi d'avoir supprimé la ligne d'impression avant.

Maintenant, nous devons imprimer le tableau lui-même pour vraiment voir le vrai tableau avec des colonnes et des lignes.

D'accord, donc maintenant que nous sommes prêts, allons maintenant à notre terminal et nettoyons l'écran et exécutons notre mot.

Donc ce sera Python run.pi à nouveau, et voyons ce que seront les résultats.

Donc je vais afficher les résultats ici.

Et nous verrons en arrière-plan dans quelques secondes, le tableau que nous attendons.

Donc maintenant, vous pouvez voir que nous avons ce beau tableau organisé qui est vraiment responsable de l'affichage de tout ce dont vous avez besoin sur les offres que vous lisez sur le site de réservation.

Et vous pouvez voir que c'est très, très organisé.

Et vous pouvez voir que c'est avec le tri du plus bas au plus haut car nous avons appliqué cette filtration tout au long de la série.

Et vous pouvez voir que c'est juste plus facile de lire les données de cette manière.

Et vous pouvez également utiliser cette bibliothèque pretty table pour différents projets également.

J'aime vraiment cette bibliothèque pour visualiser les données lorsque j'ai besoin de faire certaines tâches.

Et je travaille généralement avec cette bibliothèque car elle affiche vraiment les données plus joliment, et c'est juste plus confortable à regarder.

D'accord, donc maintenant que nous avons terminé cela, il aurait été plus agréable de contrôler chaque fois comment nous voulons exécuter notre bot.

Donc nous pourrions vouloir voir les résultats pour différents endroits à l'avenir.

Et bien sûr, nous aimerions aussi changer notre date de check-in et notre date de check-out, en fonction de ce qui est le moment exact où nous voulons nous préparer pour un endroit.

Donc c'est pourquoi maintenir ces types d'informations dans le code lui-même pourrait ne pas être une bonne idée.

Donc c'est pourquoi ce que nous pouvons faire exactement comme je l'ai montré au tout début de la série, comment le projet est développé depuis le début, c'est de transformer ces chaînes codées en dur en entrées obéissantes.

Et ensuite, nous aurons la possibilité de demander à l'utilisateur ces types de morceaux d'informations.

Donc nous pourrions avoir ici quelque chose comme input et ensuite nous pourrions demander ici où vous voulez aller.

Et ensuite, ce qui finira par se passer, c'est que la chaîne que je vais passer ici comme input sera automatiquement passée à l'intérieur de cette méthode bot dot select place to go.

Et donc ce sera utile car maintenant nous n'aurons pas à changer le code, chaque fois que nous voulons chercher un endroit différent pour préparer nos vacances.

Donc c'est pourquoi je vais faire cette approche pour la date de check-in et la date de check-out ainsi que le nombre d'adultes.

Et je vais laisser la devise telle quelle car il sera probablement plus agréable de voir les prix en dollars américains, vous pouvez la changer en n'importe quelle devise que vous voulez.

Mais laissons-la simplement codée en dur ici et ne changeons que celles-ci.

D'accord, donc je vais vous demander au lieu de coder en dur la date de check-in, quelque chose comme ceci.

Donc je vais demander, quelle est la date de check-in ? Et maintenant je vais aussi copier cette déclaration et la coller ici.

Et ensuite je vais demander, quelle est la date de check-out ? Et je vais aussi vous demander quelque chose comme, combien de personnes quelque chose comme cela, et ensuite nous sommes prêts à partir.

D'accord, donc maintenant je vais me permettre d'exécuter à nouveau, Python, run dot p y.

Et voyons ce qui va se passer.

Donc au début, nous voyons notre programme, et vous pouvez voir que rien ne se passera seulement après avoir sélectionné notre devise, car notre programme attend une entrée de notre part.

Donc ce sera maintenant répondre à chaque étape à la fois.

Donc ce sera quelque chose comme, disons que nous voulons aller à Los Angeles maintenant.

Donc je vais mettre cela et vous pouvez voir que maintenant il me demande, quelle est la date de check-in.

Donc maintenant, si j'ouvre le navigateur, alors nous pouvons voir qu'il a déjà sélectionné Los Angeles.

Donc c'est parfait, cela signifie que cela fonctionne vraiment.

Et nous devrions voir le résultat exact, lorsque nous fournissons la date de check-in et de check-out.

Maintenant, nous devons être prudents ici car nous voulons donner le bon format.

Donc ce sera année dash Mont et seulement le jour de la demande juste après cela.

Donc je vais utiliser cela.

Et ensuite je vais dire check out date quelque chose comme ce qui suit.

Donc disons que nous voulons partir pour cinq jours.

Et ensuite vous verrez qu'il a demandé combien de personnes.

Et entre-temps, je peux vérifier si cela fonctionne.

Et vous pouvez voir qu'il remplit les informations correctes.

Et maintenant, je vais fournir quatre personnes, par exemple.

Et vous pouvez voir que nous recevons une erreur.

Et je crois que c'est parce que nous n'avons pas converti le nombre d'adultes en un entretien.

Maintenant par défaut.

Donc c'est une grande erreur que nous avions ici.

Et corrigeons cela rapidement.

Donc, prenons notre programme et expliquons ce qui se passe ici.

Donc vous pouvez voir que dans select adults, si nous utilisons ici Ctrl V, vous pouvez voir que ici nous effectuons certaines actions qui nécessitent que ce count soit un entretien.

Et vous pouvez voir que exactement à partir de cette ligne où nous utilisons moins un.

Donc il se plaint de la manière dont une chaîne pourrait ne pas utiliser la soustraction ici.

Donc c'est pourquoi nous devons aller de l'avant et convertir automatiquement cela en un entier.

Donc je vais utiliser une fonction int intégrée ici et me permettre d'exécuter ce programme une fois de plus.

Donc, nettoyons l'écran.

Et encore une fois, utilisons Python run dot p y.

Et minimisons cela et ensuite fournissons les informations.

Donc ce sera Los Angeles.

Et ensuite ce sera à nouveau cette date et ensuite cette date de check-out et ensuite nous pouvons dire quatre et vous pouvez voir que maintenant nous ne recevons aucune flèche.

Donc je crois que dans quelques secondes, nous devrions voir les résultats dans un beau tableau.

Et vous pouvez voir que exactement, c'est ce qui se passe ici.

Et nous avons en fait un appel avec 10 scores.

Donc c'est une excellente nouvelle à propos de ce Grand Park la told the the states et d'accord, donc vous pouvez vraiment voir que les résultats sont parfaits et que tout fonctionne bien.

Et le fait que nous utilisions le code d'entrée aide vraiment à exécuter ce programme.

Chaque fois que nous voulons tester les résultats pour différents endroits et ainsi que pour différentes dates.

Donc nous pouvons sélectionner le mois prochain ou les trois prochaines semaines ou même demain.

Donc nous aurons cette option dynamique pour simplement fournir les informations une fois que nous exécutons le programme et nous n'avons pas vraiment besoin de changer le code à chaque fois.

D'accord, donc je pense que ce sera tout sur la conception de ce projet Selenium.

Maintenant, bien sûr, il y a toujours de la place pour l'amélioration et aussi pour ajouter quelques fonctionnalités ici et là.

Mais je pense que j'ai couvert tout ce que je voulais accomplir depuis le début.

Et c'est le fait que nous affichons les résultats dans une console de manière agréable en fonction des informations qui ont été fournies sur l'endroit où nous voulons aller et la date de check-in et de check-out et combien de personnes, donc si vous avez aimé cette série, alors assurez-vous de cliquer sur le bouton like et de laisser un commentaire.

Donc nous pouvons vraiment diffuser cette vidéo à plus de personnes sur YouTube.

Et je vous verrai dans mes futures vidéos.

Donc encore une fois, cliquez sur le bouton pouce vers le haut et abonnez-vous à ma chaîne et à bientôt.