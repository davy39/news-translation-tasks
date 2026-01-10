---
title: 'Guide d''installation d''ADB Android : pilotes et commandes'
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2021-02-18T16:48:06.000Z'
originalURL: https://freecodecamp.org/news/adb-android-install-guide-drivers-and-commands
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60297d780a2838549dcc57f3.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Android Studio
  slug: android-studio
- name: command line
  slug: command-line
seo_title: 'Guide d''installation d''ADB Android : pilotes et commandes'
seo_desc: 'In this article, we will explore how you can use the ADB to gain some fine-grained
  control when you''re installing, testing, diagnosing, and managing one or more devices
  and emulators.

  For my first few years as a software developer, primarily working ...'
---

Dans cet article, nous allons explorer comment utiliser l'ADB pour obtenir un contrôle fin lors de l'installation, des tests, du diagnostic et de la gestion d'un ou plusieurs appareils et émulateurs.

Lors de mes premières années en tant que développeur logiciel, travaillant principalement avec le SDK Android, je n'avais aucune idée de ce qu'était l'Android Debug Bridge (ADB/adb), de ce qu'il faisait, ou de quand l'utiliser.

De manière amusante, ce n'est pas un objectif professionnel qui m'a motivé à apprendre à son sujet initialement. C'était plutôt mon Nexus 6 en boucle de démarrage que je voulais désespérément ressusciter. Pour un problème comme celui-là, Android Studio et Gradle sont aussi utiles qu'un sachet de thé étanche.

Je tiens également à mentionner que cet article a été écrit en gardant à l'esprit **deux types d'individus** :

* Ceux qui sont familiers avec le CLI, le Shell, les Processus et le Modèle Client-Serveur

* Ceux qui ne sont pas familiers avec le CLI, le Shell, les Processus et le Modèle Client-Serveur

Pour ceux de la première catégorie, vous pouvez sauter la section intitulée : "**Comment travailler avec l'ADB**".

Pour ceux de la deuxième catégorie, je supposerai que vous étiez comme moi en tant que développeur junior et que vous savez très peu de choses sur les CLI, les Shells et l'ADB. La première section est une introduction douce et un glossaire pour certains termes et idées de base, expliqués de la manière la plus simple possible.

## Préliminaires

Ici, nous allons apprendre quelques sujets qui sont importants si vous voulez comprendre comment l'ADB fonctionne et est utilisé.

Certains d'entre vous ont peut-être été effrayés par l'apprentissage des outils en ligne de commande dans le passé par des enthousiastes de Vim ou des administrateurs système Unix juges. Comme vous le verrez, j'admets librement que le CLI n'est pas idéal pour le fonctionnement de mon cerveau, donc je pense que vous pourriez apprécier ma vision du sujet.

### Ligne de commande

Simplement, une ligne de commande est une interface (manière d'envoyer/recevoir des informations) à un ordinateur qui **n'utilise que des lignes de texte**.

Il est important de comprendre qu'une interface en ligne de commande (CLI) n'est pas elle-même un programme, mais plutôt que certains programmes fourniront une CLI (et peut-être d'autres interfaces comme une GUI).

À un moment donné, vous avez peut-être tapé quelque chose dans l'invite de commande Windows (ou MS-DOS si vous êtes un enfant des années 90 comme moi), le Terminal Mac, ou quelque chose comme le Terminal GNOME courant sur de nombreuses distributions Linux. Tous ceux-ci sont principalement utilisés via une CLI.

Les avantages et les inconvénients de l'utilisation d'une CLI dépendent largement de l'individu qui l'utilise et du type de problème qu'il essaie de résoudre. **Personnellement, je n'aime pas utiliser une CLI sauf si c'est pour quelque chose que je fais presque tous les jours**.

Mon cerveau n'est tout simplement pas adapté pour mémoriser des commandes texte obscures (j'avais du mal à apprendre à lire enfant pour la même raison), donc je dois m'appuyer sur une grande quantité de mémoire implicite basée sur la répétition (mémoire musculaire) et des aides-mémoire.

Pour ceux qui sont prêts à investir du temps même si c'est une lutte (comme je le fais), ou ceux qui sont vraiment très bons pour se souvenir de telles choses, **vous apprendrez probablement à apprécier à quel point vous pouvez être plus efficace dans une CLI par rapport à une GUI**.

De nombreuses opérations peuvent être effectuées en une fraction du temps qu'il faut pour pointer et cliquer à travers divers menus et écrans. Il est également possible d'écrire des scripts, qui sont des fichiers contenant une série de commandes texte, ce qui peut augmenter encore votre efficacité.

### Comment utiliser le Shell ABD

Je dois supposer que vous êtes familier avec le terme Système d'exploitation (OS), qui inclut Android, iOS, Windows, Mac, Linux et tout autre système de type Unix.

Pourquoi ce terme est-il pertinent pour l'ADB ? Pour donner une explication qui privilégie la clarté à la précision, le système d'exploitation Android est basé sur Linux, et Linux est basé sur Unix.

En conséquence, nous pouvons utiliser l'ADB pour obtenir le Shell Unix de l'appareil ou de l'émulateur avec lequel nous travaillons. Cela nous permet une grande flexibilité, des capacités et un contrôle sur l'appareil ou l'émulateur en interagissant directement avec son shell.

Un shell est un terme général pour le programme que vous utilisez pour interagir avec un système d'exploitation. Tout comme une carapace de tortue fournit une protection et un accès à une tortue (et est la couche la plus externe), le shell d'un système d'exploitation protège et fournit un accès aux rouages internes du système d'exploitation. Personnellement, j'ai été assez surpris d'apprendre que "Shell" n'était pas un acronyme ésotérique.

Ne vous sentez pas obligé de trop réfléchir à ce terme. Si vous lisez ceci sur un ordinateur, vous avez utilisé un shell pour vous aider à arriver ici.

Un shell peut fournir soit une CLI, soit une GUI, soit les deux. Dans tous les cas, vous l'utiliserez pour créer/mettre à jour/supprimer/déplacer des fichiers, démarrer d'autres programmes et accéder aux divers services du système d'exploitation qui sont mis à disposition via le shell.

### Comment utiliser le Client ABD et le Serveur ABD

Commençons à nouveau par une explication légèrement imprécise qui, je l'espère, sera plus facile à comprendre. Je corrigerai cette définition sous peu, cependant.

Les Clients et les Serveurs sont tous deux des ordinateurs. La raison pour laquelle nous les différencions de cette manière est basée sur leur **rôle**. Par exemple, votre ordinateur (qu'il s'agisse d'un bureau, d'un portable, d'un téléphone ou autre) est un Client d'un Serveur freeCodeCamp, qui vous **sert** cette page HTML.

En général, un client est **quelque chose qui utilise autre chose**, tandis qu'un serveur est **ce qui est utilisé**. Ne réfléchissez pas trop à ce terme, car un modèle Client-Serveur peut décrire un très grand nombre de choses à la fois à l'intérieur et à l'extérieur de l'informatique.

Maintenant, lorsque j'ai dit que les Clients et les Serveurs sont tous deux des "ordinateurs", ce n'est pas vraiment vrai dans le contexte où nous utiliserons ces termes plus tard.

En tant que programmeurs et ingénieurs, nous devons généralement penser aux Clients et aux Serveurs comme étant des processus (**un processus est simplement un programme en cours d'exécution**).

Cela signifie que bien qu'un processus Client et un processus Serveur fonctionnent souvent sur des ordinateurs séparés, il est également possible qu'ils fonctionnent sur le même ordinateur.

Ils occuperont des emplacements distincts dans l'espace mémoire dudit ordinateur, donc effectivement la seule différence est qu'ils communiqueront en utilisant l'IPC (communication inter-processus) plutôt que d'envoyer des messages les uns aux autres via une connexion réseau.

Comme nous le verrons bientôt, l'ADB utilise un processus Serveur, qui permet à plusieurs développeurs (plusieurs clients) de gérer plusieurs appareils Android et/ou émulateurs.

Dans un environnement d'entreprise, ce processus Serveur serait probablement situé sur un ordinateur distant (communiqué via une connexion réseau), mais nous allons configurer un Serveur qui est local à notre Client. Faire cela sera beaucoup plus simple que vous ne le pensez probablement.

### Qu'est-ce qu'un Daemon ABD ?

Au cas où vous auriez sauté en avant, j'ai déjà expliqué qu'un processus est simplement un programme en cours d'exécution. Un Daemon est un processus qui s'exécute en arrière-plan, ce qui signifie que l'utilisateur n'interagit pas directement avec lui.

Par exemple, si vous ouvrez un navigateur web, il est probable que le travail réel de gestion des connexions réseau nécessaires pour se connecter à Internet sera effectué par quelque chose comme un Daemon NetworkManager (plutôt que par le processus du navigateur lui-même).

Chaque appareil Android (physique ou émulé), en supposant qu'il soit configuré correctement, aura un Daemon ADB (adbd) qui exécute les commandes qui lui sont données par un processus Serveur.

En bref, lorsque notre Client émet une commande au Serveur, le Serveur transmettra cette commande à l'ADBD, qui l'exécutera sur l'appareil.

## Comment utiliser ADB pour le développement Android

Pour le reste de cet article, nous allons explorer les sujets suivants :

* Pilotes et configuration nécessaires pour utiliser l'ADB sur votre système

* Utilisation de l'ADB avec des appareils physiques et des émulateurs

* Commandes de base utilisant le CLI de l'ADB

* Un aperçu de l'utilisation plus compliquée en utilisant le Shell d'un appareil Android via l'ADB

Avant de continuer, vous voudrez établir quel outil CLI vous allez utiliser pour interagir avec l'ADB. Sur Windows, je préfère utiliser PowerShell, mais l'invite de commande fonctionnerait aussi. Pour Linux et Mac, le Terminal par défaut devrait fonctionner.

N'hésitez pas à utiliser ce qui fonctionne pour vous.

Cet article contient une explication très détaillée de tout le processus, mais j'ai préparé un tutoriel vidéo qui le couvre succinctement ici :

%[https://youtu.be/g___gGA9jn8]

### Comment comprendre les exemples de CLI

Cet article contient de nombreuses commandes à entrer dans votre outil CLI préféré. Toute partie d'une commande donnée qui change selon la situation sera écrite entre crochets.

**Ne pas inclure les crochets dans la commande CLI que vous écrivez.**

Par exemple, si j'écrivais... :

`adb pair <ip-address>:<port>`

... vous remplaceriez les crochets et le nom par la valeur réelle, comme :

`adb pair 192.168.0.1:5554`

### Pilotes et configuration ABD

Tout d'abord, assurez-vous d'avoir la dernière version (ou au moins une version récente) des [Android SDK Platform-Tools](https://developer.android.com/studio/releases/platform-tools). Si pour une raison quelconque vous n'utilisez pas Android Studio (AS), cliquez sur ce lien et téléchargez le package autonome pour votre système d'exploitation respectif.

Si vous avez Android Studio, vous pouvez télécharger ou mettre à jour ce package en utilisant le SDK Manager.

Il y a généralement une icône de barre d'outils dans AS pour ouvrir le SDK Manager, mais ils aiment changer son apparence pratiquement à chaque correctif.

Si vous ne trouvez pas, allez dans **Fichier -> Paramètres** et dans la barre de recherche, tapez "SDK", et recherchez l'élément de menu "Android SDK".

![Image](https://www.freecodecamp.org/news/content/images/2021/02/as_sdk_manager.png align="left")

*Paramètre système montrant que les outils de plateforme Android SDK sont installés*

L'étape suivante change en fonction de plusieurs variables. Comme discuté dans la section **Préliminaires**, l'ADB utilise un modèle Client-Serveur qui permet une grande flexibilité dans la manière dont vous utilisez l'outil.

Pour être plus précis, vous pouvez avoir :

* Plusieurs Clients interagissant avec un Serveur distant

* Un Serveur qui est local (même ordinateur) à un Client

* Une variété d'appareils physiques et d'émulateurs connectés au même serveur

La configuration avancée avec plusieurs Clients et un nombre extrêmement élevé d'appareils est possible avec l'ADB, mais hors du cadre de cet article.

Un Serveur peut gérer jusqu'à 16 émulateurs et autant d'appareils physiques que vous le souhaitez (dans la raison), sans nécessiter de configuration avancée.

Pour le reste de cet article, le maximum avec lequel nous travaillerons est un appareil physique et un émulateur pour un seul processus de serveur ADB.

#### Comment configurer un émulateur ABD

Très probablement, vous n'avez pas besoin de faire d'autres configurations, mais il est possible que vous deviez activer les **Options pour les développeurs** sur votre émulateur. Vous saurez très bientôt si cela fonctionne correctement lorsque nous en viendrons à nos premières commandes ADB.

Si vous souhaitez activer cette fonctionnalité sur votre émulateur, vous devrez [rechercher](https://developer.android.com/studio/debug/dev-options) comment faire cela pour votre version particulière d'Android.

### Débogage USB – Comment configurer un appareil physique

Si vous ne prévoyez pas d'utiliser un appareil Android physique, vous pouvez sauter cette section. Cependant, il est bon de noter que vous devrez peut-être toujours activer les Options pour les développeurs.

Pour continuer, vous devrez configurer soit le Débogage USB, soit le Débogage WiFi sur votre appareil Android et votre machine de développement.

Dans les deux cas, commencez par activer les **Options pour les développeurs** sur votre appareil. Vous devrez [rechercher](https://developer.android.com/studio/debug/dev-options) comment faire cela pour votre version particulière d'Android.

#### Débogage USB

Assurez-vous d'avoir activé le Débogage USB sur l'appareil Android via les Options pour les développeurs. Le lien que j'ai partagé ci-dessus décrira ce processus, qui tend à changer quelque peu selon les différentes versions du système d'exploitation Android.

Avant de continuer, les utilisateurs de Windows devront [télécharger un pilote USB](https://developer.android.com/studio/run/oem-usb). Les utilisateurs d'Ubuntu [nécessitent également quelques étapes supplémentaires](https://developer.android.com/studio/run/device). Pour Mac et Chrome OS, vous devriez être prêt à partir.

Une fois le Débogage USB activé via les Options pour les développeurs, connectez votre appareil Android via un câble USB.

#### Débogage WiFi

Si vous avez plusieurs appareils physiques ou un manque de câbles USB, vous pouvez opter pour le Débogage WiFi.

Visitez à nouveau les Options pour les développeurs sur votre appareil Android et activez le débogage sans fil. Il devrait vous demander d'autoriser le débogage sur le réseau auquel l'appareil est actuellement connecté, ce que vous devriez autoriser (en supposant que ce soit le réseau approprié).

**Il est temps de commencer à travailler avec votre CLI**. Tout d'abord, vous devrez localiser le répertoire platform-tools (ou dossier – même chose) dans votre répertoire d'installation du SDK Android.

En supposant que vous avez Android Studio installé, un moyen rapide de le localiser via l'application est d'aller à nouveau dans Fichier -> Paramètres, puis de taper "SDK" dans la barre de recherche. Le menu "Android SDK" vous montrera où votre SDK est installé, ce qui sera le répertoire qui devrait contenir platform-tools.

Dans l'exemple ci-dessous, **j'ai copié le chemin vers mon répertoire Android SDK**, puis j'ai ouvert une instance de Windows PowerShell. J'ai ensuite tapé les commandes suivantes :

**Changer de répertoire :**

```pgsql
cd <chemin-vers-le-répertoire-SDK>
```

**Lister les fichiers et répertoires :**

```pgsql
ls
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/power_shell_cd_ls.png align="left")

Ensuite, j'ai tapé `cd platform-tools` pour naviguer vers ce répertoire. Notez que les étapes suivantes supposent que vous utilisez un appareil qui exécute Android OS 11 ou supérieur.

Si vous travaillez avec un appareil exécutant Android 10 ou inférieur, des instructions détaillées pour cette situation peuvent être [trouvées ici](https://developer.android.com/studio/command-line/adb#wireless).

Une fois que vous êtes dans le répertoire platform-tools, vous êtes prêt à apparier un appareil Android à une machine de développement en utilisant les étapes suivantes :

1. Dans le sous-menu de débogage sans fil dans Paramètres -> Système -> Options pour les développeurs, sélectionnez **Appareils avec code d'appairage**.

2. Dans votre outil CLI qui doit être défini sur le répertoire platform-tools, entrez la commande suivante :

`adb pair <adresse IP>:<port>`

où l'adresse IP et le port proviennent de la boîte de dialogue sur votre appareil Android qui est apparue après avoir sélectionné **Appareils avec code d'appairage** (ne pas inclure les crochets).

**Remarque : Vous devrez peut-être préfixer votre appel à adb avec d'autres symboles ou commandes selon l'outil CLI que vous utilisez, votre système d'exploitation et vos contrôles d'accès.** Par exemple, j'ai dû taper .\\adb pair : en utilisant PowerShell sur Windows.

3. En supposant que tout s'est bien passé avec votre CLI, vous serez invité à entrer le code d'appairage qui a été rendu visible dans la même boîte de dialogue sur l'appareil Android qui vous a donné l'adresse IP et le numéro de port.

4. Après avoir entré le code d'appairage, vous saurez que cette opération a réussi si vous recevez un message indiquant :

`Appairage réussi avec <adresse IP>:<port> [guid=<un GUID>]`

5. Si vous utilisez Windows ou Linux, vous devrez également exécuter la commande suivante en utilisant l'adresse IP et le port visibles dans le menu des préférences de débogage sans fil (et non la boîte de dialogue qui apparaît après avoir sélectionné Appareils avec code d'appairage) :

`adb connect <adresse IP>:<port>`

après quoi vous devriez recevoir une notification sur le téléphone pour indiquer que vous êtes connecté.

### Comment utiliser l'ADB : Commandes

En supposant que vous avez réussi à configurer correctement votre appareil Android et votre machine de développement, vous pouvez maintenant utiliser l'outil ADB.

Avant de continuer, naviguez jusqu'au répertoire qui contient adb en utilisant un outil CLI (sauf si vous venez de suivre les étapes de la section précédente pour configurer le débogage WiFi).

Sinon, faites-le maintenant, ou consultez cette section pour des instructions sur la façon de localiser ce dossier.

#### Comment voir quels appareils sont actuellement connectés au serveur

Vous pouvez maintenant démarrer un serveur adb en appelant presque n'importe quelle commande sur l'ADB sauf `adb kill-server`. Que votre processus serveur soit en cours d'exécution ou non, tapez la commande suivante :

`adb devices`

![Image](https://www.freecodecamp.org/news/content/images/2021/02/pwershell_devices-1.png align="left")

Dans la capture d'écran ci-dessus, j'ai d'abord appelé `adb devices` lorsque mon téléphone Android était connecté au serveur. Après avoir tué le serveur via la commande `adb kill-server`, j'ai de nouveau appelé devices qui a redémarré le serveur.

Encore une fois, si un serveur ADB n'est pas actuellement en cours d'exécution, **l'appel de presque n'importe quelle commande ADB démarrera le serveur** (sauf `adb kill-server`, bien sûr). Il existe une commande explicite `adb start-server`, mais en pratique, je n'ai jamais eu besoin de l'utiliser.

Puisque le serveur a été réinitialisé, devices n'a retourné aucun élément. Par conséquent, avant de passer à l'exemple suivant, j'ai dû utiliser à nouveau les commandes `adb pair` et `adb connect` (si sur Windows ou Linux) décrites dans la section précédente.

J'ai maintenant lancé un émulateur en utilisant PowerShell et le programme émulateur qui se trouve également dans un sous-répertoire de platform-tools appelé "emulator".

Vous pouvez bien sûr utiliser le gestionnaire AVD ou Android Studio pour démarrer un émulateur pour suivre l'exemple si vous le souhaitez.

Si vous avez de nombreux appareils connectés, une option utile pour la commande `adb devices` est `-l`, qui vous donne plus d'informations sur les appareils.

Ci-dessous, vous verrez plusieurs entrées qui font référence à mon appareil Android physique, ainsi qu'à un émulateur qui a été attaché à un port spécifique :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_devices_list-1.png align="left")

#### Comment envoyer des commandes à un appareil spécifique

Pour éviter de bricker accidentellement mon téléphone, je veux envoyer des commandes à l'émulateur à la place. Pour ce faire, je dois préfixer l'option `-s`, suivie du numéro de série de l'appareil cible, avant de taper la commande.

Le numéro de série est le premier ensemble de caractères qui décrit un appareil connecté après avoir utilisé la commande devices.

Par exemple, le numéro de série de l'émulateur dans ce cas est simplement le mot émulateur suivi du port auquel l'émulateur est actuellement attaché.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_devices_serial-1.png align="left")

L'autre flèche rouge pointe vers le numéro de série de mon téléphone (masqué pour des raisons évidentes).

Naturellement, si vous n'avez qu'un seul appareil connecté (quel qu'il soit), vous n'avez pas besoin d'utiliser l'option `-s`.

#### Installer un APK (App) sur un appareil

Je vais maintenant installer un APK de test sur l'émulateur en cours d'exécution en utilisant la commande `adb install`.

Cela équivaut essentiellement à avoir Android Studio et Gradle installer un APK de débogage. Comme vous le verrez, les APK de test nécessitent l'option `-t` après la commande d'installation :

`adb -s <numéro-de-série-de-l'appareil> install -t <chemin-vers-l'APK>`

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_install_test_apk.png align="left")

**Remarque : Le système d'exploitation Android exige que tout APK soit signé avant de pouvoir être installé** (même s'il s'agit simplement d'un APK de test/débogage).

Une solution consiste à construire et exécuter l'application à installer dans Android Studio, qui la signera avec un certificat de débogage généré. Il existe plusieurs autres façons de signer un tel APK que vous pouvez explorer en visitant ce [lien](https://developer.android.com/studio/publish/app-signing#debug-mode).

#### Que peut faire d'autre l'ADB ?

Avant de regarder quelques utilisations plus avancées de l'ADB, je vous encourage fortement à essayer la commande `adb --help`. Comme il est d'usage pour la plupart des programmes basés sur CLI, la commande d'aide imprimera une documentation qui décrit les diverses commandes et options de l'outil.

Je suis heureux de dire que la documentation pour l'ADB est assez lisible et utile, ce qui n'est pas toujours le cas dans les programmes CLI.

## Conseils d'utilisation avancée de l'ADB

Ce serait une perte de temps pour nous deux de couvrir chaque utilisation et commande de l'ADB dans cet article.

Au cas où il y aurait une confusion, utiliser l'ADB pour installer des APK et faire beaucoup de choses que Android Studio et Gradle font pour vous n'est pas quelque chose que je recommanderais (sauf si vous avez une bonne raison de le faire).

Cela dit, il y a beaucoup de choses que l'ADB peut faire qui sont soit difficiles, soit impossibles à faire sans lui.

Dans la section des préliminaires, j'ai mentionné que l'ADB peut être utilisé pour obtenir un accès au shell de l'appareil. Pour terminer cet article, nous allons voir comment utiliser les commandes shell et où trouver plus d'informations à leur sujet.

Si vous ne savez pas ce qu'est un shell, vous avez probablement sauté la section ci-dessus où je l'ai expliqué.

### Comment utiliser le Shell ABD

Envoyer une commande au shell de l'appareil en utilisant l'ADB est assez simple. N'oubliez pas que si vous avez plusieurs appareils connectés, suivez-la avec `-s <numéro-de-série-de-l'appareil>` pour diriger la commande vers un appareil spécifique.

Pour faire une seule commande shell, nous devons utiliser la commande `adb shell` (grosse surprise, hein ?), suivie de la commande réelle que nous voulons faire sur le shell de l'appareil :

`adb shell ls`

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_shell_ls.png align="left")

Comme mentionné précédemment, la commande `ls` affiche une liste de fichiers et de répertoires dans le répertoire actuel du CLI. Cela se trouve être le répertoire racine de l'appareil Android jusqu'à ce que nous passions à un autre.

Si vous prévoyez de faire de nombreuses commandes via le Shell, vous pouvez également démarrer une session Shell interactive. Cela peut être fait via la commande simple :

`adb shell`

Pendant une session Shell interactive, vous pouvez taper des commandes Shell directement sans utiliser davantage `adb shell <commande>`.

Notez que lorsque vous voulez quitter la session Shell interactive, vous pouvez le faire en tapant `exit` ou en appuyant sur Ctrl + D.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_start_interactive_shell.png align="left")

Il existe une variété de commandes et d'utilitaires différents avec lesquels vous pouvez travailler via le Shell. Le ActivityManager (`am`) d'un appareil Android peut être particulièrement utile pour tester différents composants (Activities, Services, BroadcastReceivers, pour en nommer quelques-uns) d'une application Android dans différentes circonstances.

Supposons que nous voulons lancer directement dans une Activity particulière, mais cette Activity n'est pas désignée comme l'Activity de lancement dans le manifest.

Vous devrez toujours ajouter l'attribut `android:exported="true"` à chaque entrée `<activity/>` dans le manifest que vous souhaitez lancer (en supposant qu'il ne s'agit pas déjà de l'Activity de lancement).

Après cela, vous pouvez utiliser la commande suivante pour y aller directement :

`am start -n <id-du-package-de-l'application>/<nom-de-l'activité>`

Notez que le `<nom-de-l'activité>` doit inclure les packages, relatifs à l'id du package, dans lesquels il se trouve. Voir la sortie ci-dessous pour un exemple de lancement d'une Activity qui se trouve dans plusieurs packages.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/powershell_shell_start.png align="left")

### Lectures complémentaires

Mon objectif dans cet article était de faire de mon mieux pour introduire, expliquer et vous guider à travers l'utilisation de l'ADB avec mes propres mots (dans la mesure du possible).

À ce stade, je devrais commencer à faire des exemples très artificiels ou simplement copier la documentation, ce qui n'est pas quelque chose qui m'intéresse.

Au lieu de cela, je vous encourage à visiter la [documentation](https://developer.android.com/studio/command-line/adb#shellcommands), et à jeter un bref coup d'œil à certaines des choses cool que vous pouvez faire en utilisant des outils comme le Activity Manager, le Package Manager, le Policy Manager, et d'autres.

#### **Vous pouvez me contacter sur les réseaux sociaux ici :**

[https://www.instagram.com/rkay301/](https://www.instagram.com/wiseassbrand/)
[https://www.facebook.com/wiseassblog/](https://www.facebook.com/wiseassblog/)
[https://twitter.com/wiseass301](https://twitter.com/wiseass301)
[http://wiseassblog.com/](http://wiseassblog.com/)