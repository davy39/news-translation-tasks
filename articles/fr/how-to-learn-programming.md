---
title: Comment apprendre la programmation – Le guide que j'aurais aimé avoir quand
  j'ai commencé à coder
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2021-10-06T15:17:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/The-Programming-Guide-I-Wish-I-Had-When-I-Started-1.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
seo_title: Comment apprendre la programmation – Le guide que j'aurais aimé avoir quand
  j'ai commencé à coder
seo_desc: 'Just the thought of learning to code can be very intimidating. The word
  code is mysterious by definition. It implies a technical form of communication that
  computers, and not humans, are meant to understand.

  One way many people start learning to code...'
---

Le simple fait de penser à apprendre à coder peut être très intimidant. Le mot **code** est mystérieux par définition. Il implique une forme technique de communication que les ordinateurs, et non les humains, sont censés comprendre.

Une façon dont beaucoup de gens commencent à apprendre à coder est de choisir un langage de programmation populaire et de se lancer tête baissée sans direction. Cela peut prendre la forme d'un cours de codage en ligne, d'un projet de tutoriel, ou d'un achat aléatoire d'un livre sur un sujet spécifique.

Rarement les développeurs en herbe commencent avec une feuille de route – une vue d'ensemble du monde du codage qui décrit un ensemble de concepts, de langages et d'outils de programmation pertinents que presque 100 % des développeurs utilisent tous les jours.

Dans cet article, je propose une telle feuille de route. Je le fais en décrivant 14 étapes – chacune discutant d'un concept, d'un langage ou d'un outil essentiel – que les développeurs professionnels utilisent pour écrire du code, collaborer et créer des projets professionnels.

J'ai soigneusement choisi ces 14 étapes en fonction de mon propre parcours personnel d'apprentissage du codage, qui s'étend sur près de 20 ans.

Une partie de la raison pour laquelle il m'a fallu si longtemps pour me sentir à l'aise en tant que développeur est que j'apprenais des sujets spécifiques sans avoir une vue d'ensemble plus large du monde du codage.

Chacune des étapes de cet article discute d'un "essentiel du codage" – quelque chose que je crois **être crucial de connaître au début de votre parcours de codage**.

Une dernière remarque avant de lister les étapes de la feuille de route : bien sûr, la lecture de cet article ne fera pas de vous un programmeur expert. Ce n'est pas son but. Le but de cet article est de vous faire prendre conscience que chacun de ces sujets existe, et espérons-le, de vous donner une idée de base de comment chacun fonctionne afin que vous puissiez construire dessus intelligemment à l'avenir.

## Feuille de route en 14 étapes pour les développeurs débutants

1. [Familiarisez-vous avec l'architecture des ordinateurs et les bases des données](#heading-1-familiarisez-vous-avec-larchitecture-des-ordinateurs-et-les-bases-des-donnees)

2. [Apprenez comment fonctionnent les langages de programmation](#heading-2-apprenez-comment-fonctionnent-les-langages-de-programmation)

3. [Comprenez comment fonctionne Internet](#heading-3-comprenez-comment-fonctionne-internet)

4. [Pratiquez quelques bases de la ligne de commande](#heading-4-pratiquez-quelques-bases-de-la-ligne-de-commande)

5. [Développez vos compétences en éditeur de texte avec Vim](#heading-5-developpez-vos-competences-en-editeur-de-texte-avec-vim)

6. [Apprenez un peu de HTML](#heading-6-apprenez-un-peu-de-html)

7. [Abordons un peu de CSS](#heading-7-abordons-un-peu-de-css)

8. [Commencez à programmer avec JavaScript](#heading-8-commencez-a-programmer-avec-javascript)

9. [Continuez à programmer avec Python](#heading-9-continuez-a-programmer-avec-python)

10. [Approfondissez vos connaissances avec Java](#heading-10-approfondissez-vos-connaissances-avec-java)

11. [Suivez votre code en utilisant Git](#heading-11-suivez-votre-code-en-utilisant-git)

12. [Stockez des données en utilisant des bases de données et SQL](#heading-12-stockez-des-donnees-en-utilisant-des-bases-de-donnees-et-sql)

13. [Lisez à propos des frameworks Web et MVC](#heading-13-lisez-a-propos-des-frameworks-web-et-mvc)

14. [Jouez avec les gestionnaires de paquets](#heading-14-jouez-avec-les-gestionnaires-de-paquets)

Sans plus tarder, commençons par le début !

## 1) Familiarisez-vous avec l'architecture des ordinateurs et les bases des données

L'une des choses merveilleuses à propos des langages de programmation modernes est qu'ils nous permettent de créer des applications sophistiquées sans nous soucier des détails fastidieux du matériel en arrière-plan (pour la plupart).

Cela s'appelle **l'abstraction** – la capacité de travailler avec des outils de haut niveau (dans ce cas, des langages de programmation) qui simplifient et réduisent la portée requise de notre compréhension et de nos compétences.

Cependant, cela ne signifie pas qu'il est inutile de connaître les bases du matériel sur lequel votre code s'exécute. À tout le moins, être conscient de quelques détails vous aidera à naviguer dans les conversations au travail sur l'utilisation élevée du CPU et de la mémoire.

Donc, voici un minimum de bases sur l'architecture des ordinateurs pour vous lancer :

Les parties les plus importantes de votre ordinateur se trouvent sur des **microprocesseurs** (également connus sous le nom de **circuits intégrés**).

Les microprocesseurs reposent sur un composant électrique appelé **transistor** pour fonctionner. Les transistors sont de minuscules interrupteurs électriques qui sont soit éteints (0) soit allumés (1) à un moment donné. Un seul microprocesseur peut contenir des millions ou des milliards de minuscules transistors intégrés.

La plupart des ordinateurs modernes ont un microprocesseur appelé **Unité Centrale de Traitement (CPU)**. Vous pouvez le considérer comme le cerveau de l'ordinateur. Il gère la plupart des calculs numériques et des tâches logiques que l'ordinateur effectue.

Chaque CPU a ce qu'on appelle un **jeu d'instructions**, qui est une collection de commandes binaires (zéros et uns) que le CPU comprend. Heureusement, en tant que développeurs de logiciels, nous n'avons pas vraiment besoin de nous en soucier ! C'est la puissance de l'abstraction.

Si le CPU est le centre logique du cerveau, il est utile d'avoir aussi de la mémoire pour stocker des informations temporairement ou à long terme.

Les ordinateurs ont une **mémoire vive (RAM)** en tant que "mémoire de travail" (ou mémoire à court terme) pour stocker les informations qui sont activement utilisées par les programmes en cours d'exécution.

La RAM est composée d'une collection d'**adresses mémoire**, qui peuvent être utilisées pour stocker des bits de données. Dans les anciens langages comme le C, les programmeurs ont accès à la mémoire directement en utilisant une fonctionnalité appelée **pointeurs**, mais cela est rare dans les langages plus modernes.

Enfin, nous allons aborder un composant que vous connaissez sûrement – le disque dur. Dans notre analogie du cerveau, cela représente la mémoire à long terme. Un disque dur est un dispositif interne ou externe qui stocke les données qui doivent persister même après l'arrêt de l'ordinateur.

Avant de passer à plus de détails sur les langages de programmation, passons une seconde à parler des données. Mais que voulons-nous dire exactement par le mot **données** ?

À un niveau élevé, nous pensons à des choses comme des documents texte, des images, des vidéos, des e-mails, des fichiers et des dossiers. Ce sont toutes des structures de données de haut niveau que nous créons et sauvegardons sur nos ordinateurs tous les jours.

Mais sous le capot, une puce d'ordinateur (comme une puce CPU ou RAM) n'a aucune idée de ce qu'est une "image" ou une "vidéo".

Du point de vue d'une puce, toutes ces structures sont stockées sous forme de longues séquences de uns et de zéros. Ces uns et zéros sont appelés **bits**.

Les bits sont communément stockés en ensembles de huit à la fois, connus sous le nom d'**octet**. Un octet est simplement une séquence de huit bits, comme `00000001`, `01100110`, ou `00001111`. Représenter l'information de cette manière est appelé une **représentation binaire**.

## 2) Apprenez comment fonctionnent les langages de programmation

Dans la section précédente, nous avons mentionné que la plupart des ordinateurs reposent sur un CPU, et qu'un CPU peut comprendre un ensemble spécifique d'instructions sous forme de uns et de zéros.

Par conséquent, nous pourrions théoriquement écrire du code qui dit au CPU quoi faire en enchaînant de longues séquences de uns et de zéros dans une forme que le CPU comprend. Les instructions écrites sous forme binaire comme celle-ci sont appelées **code machine**.

Cela semble horrible à utiliser, n'est-ce pas ? Eh bien, c'est probablement le cas, mais je ne le saurais pas puisque j'utilise principalement des langages de programmation de haut niveau comme JavaScript, Python et Java.

Un **langage de programmation de haut niveau** fournit un ensemble de mots-clés lisibles par l'homme, d'instructions et de règles de syntaxe qui sont beaucoup plus simples pour les gens à apprendre, déboguer et utiliser.

Les langages de programmation fournissent un moyen de combler le fossé entre la manière dont nos cerveaux humains comprennent le monde et la manière dont les cerveaux des ordinateurs (CPU) comprennent le monde.

En fin de compte, le code que nous écrivons doit être traduit en instructions binaires (code machine) que le CPU comprend.

Selon le langage que vous choisissez, nous disons que votre code est soit **compilé** soit **interprété** en code machine capable d'être exécuté par votre CPU. La plupart des langages de programmation incluent un programme appelé **compilateur** ou un **interpréteur** qui effectue cette étape de traduction.

Juste pour donner quelques exemples – JavaScript et Python sont des langages interprétés tandis que Java est un langage compilé. Qu'un langage soit compilé ou interprété (ou une combinaison des deux) a des implications pour la commodité du développeur, la gestion des erreurs, les performances et d'autres domaines, mais nous n'entrerons pas dans ces détails ici.

## 3) Comprenez comment fonctionne Internet

Quel que soit le type de programmation que vous aspirez à faire, vous rencontrerez des situations où il est utile de savoir comment les ordinateurs interagissent les uns avec les autres. Cela se produit généralement via Internet.

Internet n'est rien de plus qu'une collection mondiale d'ordinateurs connectés. En d'autres termes, c'est un réseau mondial. Chaque ordinateur du réseau accepte un ensemble de règles qui leur permettent de communiquer entre eux. Pour un ordinateur, "communiquer" signifie transférer des données.

Comme nous l'avons discuté dans la section précédente, tous les types de données – pages web, images, vidéos, e-mails, et ainsi de suite – peuvent tous être représentés par des uns et des zéros.

Par conséquent, vous pouvez penser à Internet comme un très grand ensemble d'ordinateurs qui peuvent transférer des uns et des zéros entre eux, de manière à préserver le sens de ces données. Internet n'est rien de plus qu'un medium de conversation numérique.

Si Internet est simplement une grande arène de conversation, définissons les participants à la conversation.

D'abord, une analogie : la plupart des conversations humaines nécessitent au moins deux participants. Dans la plupart des cas, une personne initie la conversation et l'autre personne répond, en supposant qu'elles sont toutes deux présentes et disponibles.

En termes d'Internet, l'ordinateur qui initie la conversation est appelé le **client**. L'ordinateur qui répond ou qui répond est appelé le **serveur**.

Par exemple, disons que vous ouvrez un navigateur web et allez sur "www.google.com". Dans ce scénario, votre navigateur web est le client. Par extension, vous pouvez aussi considérer l'ordinateur sur lequel vous travaillez comme le client.

Dans un sens plus abstrait, VOUS êtes le client parce que vous êtes celui qui initie la conversation. En tapant "www.google.com" dans la barre de recherche et en cliquant, votre navigateur demande à commencer une conversation avec l'un des ordinateurs de Google.

L'ordinateur de Google est appelé le serveur. Il répond en envoyant les données nécessaires pour afficher la page web de Google dans votre navigateur. Et voilà ! La page web de Google apparaît devant vos yeux. Tous les transferts de données Internet utilisent ce type de relation client/serveur.

## 4) Pratiquez quelques bases de la ligne de commande

La **ligne de commande** peut sembler intimidante au premier abord. Elle est souvent présentée dans les films comme un écran noir cryptique avec du texte, des nombres et des symboles incompréhensibles qui défilent. Elle est généralement associée à un pirate informatique maléfique ou à un génie de la technologie.

La vérité est qu'il ne faut pas être un génie pour utiliser ou comprendre la ligne de commande. En fait, elle nous permet d'effectuer beaucoup des mêmes tâches que nous faisons confortablement via une souris point-and-click.

La principale différence est qu'elle accepte principalement les entrées via le clavier, ce qui peut accélérer considérablement les entrées une fois que vous avez pris le coup.

Vous pouvez utiliser la ligne de commande pour naviguer dans les dossiers, lister le contenu d'un dossier, créer de nouveaux dossiers, copier et déplacer des fichiers, supprimer des fichiers, exécuter des programmes, et bien plus encore. La fenêtre dans laquelle vous pouvez taper des commandes sur la ligne de commande est appelée un **terminal**.

Faisons un court tutoriel des commandes de navigation de base qui vous donnera une idée de ce que c'est que de travailler sur la ligne de commande.

Une fois que vous avez ouvert votre terminal, une première question typique est "*Où suis-je ?*" Nous pouvons utiliser la commande `pwd` (qui signifie "Print Working Directory") pour le découvrir. Elle affiche notre emplacement actuel dans le système de fichiers, ce qui nous indique dans quel dossier nous nous trouvons actuellement.

Essayez-le vous-même :

### Comment utiliser la ligne de commande

Si vous êtes sur un Mac, ouvrez l'application Terminal, qui est essentiellement un terminal de ligne de commande Unix.

Si vous utilisez un système d'exploitation sans interface graphique (GUI), comme Linux ou Unix, vous devriez être sur la ligne de commande par défaut lorsque vous démarrez l'ordinateur. Si votre version de Linux ou Unix a une interface graphique, vous devrez ouvrir le terminal manuellement.

À l'invite, tapez `pwd` et appuyez sur &lt;ENTRÉE&gt;. La ligne de commande imprimera le chemin vers le dossier dans lequel vous vous trouvez actuellement.

Par défaut, le dossier actif lors de l'ouverture de la ligne de commande est le répertoire personnel de l'utilisateur connecté. Cela est personnalisable au cas où vous souhaitez la commodité de commencer à un autre endroit.

Pour plus de commodité, le répertoire personnel peut être référencé en utilisant le caractère tilde `~`. Nous utiliserons cela dans quelques exemples à venir.

Maintenant que nous savons dans quel dossier nous nous trouvons, nous pouvons utiliser la commande `ls` pour lister le contenu du répertoire actuel. La commande `ls` signifie "List".

Tapez `ls` et appuyez sur &lt;ENTRÉE&gt;. Le contenu (fichiers et sous-dossiers) qui réside dans le répertoire actuel est imprimé à l'écran.

Relancez la commande précédente comme ceci `ls -al` et appuyez sur &lt;ENTRÉE&gt;. Maintenant, nous obtiendrons plus de détails sur le contenu du répertoire, y compris les tailles de fichiers, les dates de modification et les permissions de fichiers.

Le tiret dans la commande précédente nous permet de définir certains indicateurs qui modifient le comportement de la commande. Dans ce cas, nous avons ajouté l'indicateur -a qui listera tout le contenu du répertoire (y compris les fichiers cachés) ainsi que l'indicateur -l qui affiche les détails supplémentaires des fichiers.

Ensuite, nous pouvons créer un nouveau dossier en utilisant la commande `mkdir`, qui signifie "Make Directory". Ci-dessous, nous créons un nouveau dossier appelé "testdir".

Tapez `mkdir testdir` et appuyez sur &lt;ENTRÉE&gt;. Ensuite, tapez `ls` et appuyez sur &lt;ENTRÉE&gt;. Vous devriez voir votre nouveau répertoire dans la liste.

Pour créer plusieurs répertoires imbriqués à la fois, utilisez l'indicateur `-p` pour créer toute une chaîne de répertoires comme ceci : `mkdir -p directory1/directory2/directory3`

La ligne de commande n'est pas très utile si nous ne pouvons rester qu'à un seul endroit, alors apprenons à naviguer dans différents répertoires du système de fichiers. Nous pouvons le faire via la commande `cd`, qui signifie "Change Directory".

Tout d'abord, tapez `cd testdir` et appuyez sur &lt;ENTRÉE&gt;. Ensuite, tapez `pwd` et appuyez sur &lt;ENTRÉE&gt;. Notez que la sortie montre maintenant que nous sommes à l'intérieur du répertoire "testdir" spécifié dans la commande cd. Nous y avons navigué !

Tapez `cd ..` et appuyez sur &lt;ENTRÉE&gt;. Le `..` indique à la ligne de commande de naviguer en arrière vers le répertoire parent.

Ensuite, tapez `pwd` et appuyez sur &lt;ENTRÉE&gt;. Notez que la sortie montre maintenant que vous êtes de retour dans le répertoire d'origine. Nous avons navigué en arrière !

Ensuite, nous allons apprendre à créer un nouveau fichier vide dans le répertoire actuel.

Tapez `touch newfile1.txt` et appuyez sur &lt;ENTRÉE&gt;. Vous pouvez utiliser la commande `ls` pour voir que le nouveau fichier a été créé dans le répertoire actuel.

Maintenant, nous allons copier ce fichier d'un dossier à un autre en utilisant la commande cp.

Tapez `cp newfile1.txt testdir` et appuyez sur &lt;ENTRÉE&gt;. Utilisez maintenant les commandes `ls` et `ls testdir` pour voir que le nouveau fichier existe toujours dans le répertoire actuel et a été copié dans le répertoire "testdir".

Nous pouvons également déplacer des fichiers au lieu de les copier en utilisant la commande `mv`.

Tapez `touch newfile2.txt` et appuyez sur &lt;ENTRÉE&gt; pour créer un nouveau fichier. Ensuite, tapez `mv newfile2.txt testdir` et appuyez sur &lt;ENTRÉE&gt; pour déplacer le fichier dans le dossier "testdir".

Utilisez les commandes `ls` et `ls testdir` pour confirmer que le fichier a été déplacé dans le dossier "testdir" (il ne devrait plus apparaître dans l'emplacement d'origine où vous l'avez créé, puisque il a été *déplacé* et non copié).

La commande `mv` peut également être utilisée pour renommer des fichiers.

Pour cela, tapez `touch newfile3.txt` et appuyez sur &lt;ENTRÉE&gt; pour créer un nouveau fichier. Ensuite, tapez `mv newfile3.txt cheese.txt` et appuyez sur &lt;ENTRÉE&gt; pour mettre à jour le nom du fichier. Utilisez `ls` pour confirmer que le fichier a été renommé.

Enfin, nous pouvons supprimer des fichiers et des dossiers en utilisant la commande `rm`.

Tapez `rm cheese.txt` et appuyez sur &lt;ENTRÉE&gt; pour supprimer le fichier. Utilisez `ls` pour confirmer que le fichier a été supprimé.

Tapez `rm -rf testdir` et appuyez sur &lt;ENTRÉE&gt; pour supprimer le répertoire "testdir" et son contenu. Utilisez `ls` pour confirmer que le répertoire a été supprimé.

Notez que nous devons utiliser les indicateurs `-rf` lors de la suppression de répertoires. Cela force la suppression du dossier et de tout son contenu.

## 5) Développez vos compétences en éditeur de texte avec Vim

À ce stade, nous avons couvert les bases de la ligne de commande et vu quelques exemples de la façon dont nous pouvons travailler avec des fichiers sans souris.

Bien que nous sachions maintenant comment créer, copier, déplacer, renommer et supprimer des fichiers à partir de la ligne de commande, nous n'avons pas encore vu comment nous éditons le contenu des fichiers texte dans le terminal.

Travailler avec des fichiers texte dans le terminal est important car le code informatique n'est rien de plus que du texte enregistré dans un ensemble organisé de fichiers.

Bien sûr, nous pourrions utiliser un éditeur de texte sophistiqué comme Microsoft Word (ou plus probablement des éditeurs de code spécialisés comme Sublime ou Atom) pour écrire et éditer notre code, mais ce n'est pas nécessaire. Le terminal est souvent l'endroit le plus pratique pour écrire et éditer du code puisque nous l'avons généralement déjà ouvert pour exécuter des commandes !

Il existe plusieurs excellents éditeurs de texte créés spécifiquement à cet effet, et je recommande [d'apprendre les bases de l'un d'eux appelé Vim](https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/).

Vim est l'un des plus anciens éditeurs de texte et c'est un joyau éprouvé par le temps. Vim signifie "***VI*** i\*\**M*\*\*proved" puisque c'est le successeur d'un outil appelé ***Vi***.

Comme mentionné, Vim est un éditeur de texte qui a été conçu pour fonctionner directement dans le terminal, donc nous n'avons pas besoin d'ouvrir une fenêtre séparée pour travailler ou d'utiliser une souris. Vim dispose d'un ensemble de commandes et de modes qui nous permettent de créer et d'éditer facilement du contenu textuel en utilisant uniquement le clavier.

Vim [a une courbe d'apprentissage](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/), mais avec un peu de pratique, les compétences que vous apprenez vous seront utiles tout au long de votre carrière de codeur.

Vim est installé par défaut sur de nombreux systèmes d'exploitation. Pour vérifier s'il est installé sur votre ordinateur, ouvrez la ligne de commande et tapez `vim -v`.

Si Vim s'ouvre dans votre terminal et affiche la version, vous êtes prêt à partir ! Sinon, vous devrez l'installer sur votre système. (Notez que vous pouvez quitter Vim en tapant `:q!` et en appuyant sur Entrée). Pour plus d'informations sur l'installation de Vim, consultez https://www.vim.org.

À mon avis, le moyen le plus rapide et le plus facile d'apprendre à utiliser Vim est d'utiliser leur tutoriel intégré, le **VimTutor**. Pour l'exécuter, assurez-vous que Vim est installé sur votre système, ouvrez la ligne de commande, tapez `vimtutor`, et appuyez sur Entrée.

C'est un si bon tutoriel qu'il n'y a aucune raison pour que je perde du temps à essayer de l'expliquer ici. Alors allez faire le VimTutor, maintenant ! À tout de suite dans la prochaine section.

Si vous avez encore de l'énergie après avoir terminé le VimTutor, consultez [ces 7 commandes Vim qui amélioreront considérablement votre productivité](https://initialcommit.com/blog/7-versatile-vim-commands) lorsque vous commencez avec Vim.

## 6) Apprenez un peu de HTML

Vous pouvez considérer le HTML – abréviation de **H**yper**T**ext **M**arkup **L**anguage – comme l'ossature d'une page web. Il détermine la structure de la page en spécifiant les éléments qui doivent être affichés et l'ordre dans lequel ils doivent être affichés.

Chaque page web que vous avez visitée dans votre navigateur a du HTML associé. Lorsque vous visitez une page web, le serveur web hébergeant la page web envoie du HTML à votre navigateur. Votre navigateur le lit ensuite et l'affiche pour vous.

La plupart des pages web contiennent un ensemble de contenu assez standard, y compris un titre, du contenu textuel, des liens vers des images, des liens de navigation, des en-têtes et des pieds de page, et plus encore. Toutes ces informations sont stockées sous forme de HTML qui définit la structure de la page.

Une chose à garder à l'esprit est que le HTML n'est pas techniquement un langage de programmation, bien qu'il soit souvent appelé "code HTML".

Comme nous le verrons plus tard, d'autres langages de programmation nous permettent d'écrire du code qui **fait des choses**, comme exécuter un ensemble d'instructions en séquence. Le HTML ne **fait** rien. Nous n'exécutons pas ou n'exécutons pas le HTML. Le HTML reste simplement dans un fichier et attend d'être envoyé à un navigateur web qui l'affichera à l'utilisateur final.

En fait, le HTML est essentiellement des données. Ce sont des données qui définissent à quoi une page web devrait ressembler, rien de plus.

Alors, comment écrit-on du HTML ? Le HTML utilise un ensemble standard de **balises** (basiquement des étiquettes) pour identifier les éléments disponibles qui composent une page web. Chaque balise est définie en utilisant des chevrons.

Par exemple, la balise **title** est définie comme `<title>Mon Titre de Page</title>` et la balise **paragraph** est définie comme `<p>Un tas de texte aléatoire.</p>`.

Chaque élément HTML est composé d'une balise d'ouverture et d'une balise de fermeture. La balise d'ouverture est simplement l'étiquette de la balise entre chevrons, comme ceci :

`<nomdelabalise>`

Cela ouvre la nouvelle balise HTML. La balise de fermeture est essentiellement la même, mais elle utilise une barre oblique après le premier chevron, pour la marquer comme une balise de fermeture :

`</nomdelabalise>`

Tout texte entre les deux balises est le contenu réel que la page affichera.

Passons en revue quelques-unes des balises les plus courantes en usage. La première est la balise `<html>`. Cela définit le début d'une page HTML. Une balise `</html>` correspondante (notez la barre oblique) définit la fin de la page HTML. Tout contenu entre ces balises fera partie de la page.

La deuxième est la balise `<head>`. Cela définit des informations supplémentaires que le navigateur utilisera pour comprendre la page. La plupart du contenu de cette balise n'est pas affiché à l'utilisateur. Une balise `</head>` correspondante définit la fin de la section HEAD.

Précédemment, nous avons vu la balise `<title>`. Elle définit le titre de la page web, que le navigateur affichera dans l'onglet du navigateur. Cette balise doit être placée à l'intérieur de la section `<head>...</head>`.

Ensuite, il y a la balise `<body>`. Tout le contenu à l'intérieur de cette balise constitue le contenu principal de la page web. Mettre ces quatre balises ensemble ressemble à ceci :

```html
<html>
    
    <head>
        <title>Mon Titre de Page</title>
    </head>
        
    <body>
        <p>Un tas de texte aléatoire.</p>
    </body>

</html>
```

Le simple extrait HTML ci-dessus représente une page web simple avec un titre et un seul paragraphe comme contenu du corps.

Cet exemple soulève un point que nous n'avons pas mentionné dans la dernière section. Les balises HTML peuvent être imbriquées les unes dans les autres. Cela signifie simplement que les balises HTML peuvent être placées à l'intérieur d'autres balises HTML.

Le HTML fournit de nombreuses autres balises pour fournir un ensemble riche de contenu aux utilisateurs web. Nous ne les couvrirons pas en détail ici, mais voici une courte liste pour référence :

* `<p>` : Un paragraphe de texte commençant sur une nouvelle ligne.

* `<h1>` : Un titre de page généralement utilisé pour les titres de page.

* `<h2>` : Un titre de section généralement utilisé pour les titres de section.

* `<hx>` : Où *x* est un nombre entre 3 et 6, pour des titres plus petits.

* `<img>` : Une image.

* `<a>` : Un lien.

* `<form>` : Un formulaire contenant des champs ou des entrées pour que l'utilisateur remplisse et soumette.

* `<input>` : Un champ d'entrée pour que les utilisateurs saisissent des informations, généralement dans un formulaire.

* `<div>` : Une division de contenu, utilisée pour regrouper plusieurs autres éléments à des fins d'espacement.

* `<span>` : Un autre élément de regroupement, mais utilisé pour envelopper des phrases de texte dans un autre élément, généralement pour appliquer un formatage spécifique à seulement une partie spécifique du contenu textuel.

## 7) Abordons un peu de CSS

Une page web sans CSS – ou **C**ascading **S**tyle **S**heets – est comme un gâteau sans glaçage. Un gâteau sans glaçage remplit sa fonction, mais il n'a pas l'air appétissant !

Le CSS nous permet d'associer des propriétés de style telles que la couleur de fond, la taille de la police, la largeur, la hauteur, et plus encore avec nos éléments HTML.

Chaque propriété de style indique au navigateur d'afficher l'effet souhaité à l'écran. Comme le HTML, le CSS n'est pas techniquement un langage de programmation. Il ne nous permet pas d'effectuer des actions, il nous permet simplement d'ajouter des styles à l'HTML de base.

Voyons comment associer des styles CSS à nos éléments HTML. Il y a trois éléments à ce puzzle :

**Le sélecteur CSS :** Utilisé pour identifier l'élément ou les éléments HTML auxquels nous voulons appliquer le style.

**Le nom de la propriété CSS :** Le nom de la propriété de style spécifique que nous voulons ajouter aux éléments HTML correspondants.

**La valeur de la propriété CSS :** La valeur de la propriété de style que nous voulons appliquer.

Voici un exemple de la façon dont ces éléments s'assemblent pour définir la couleur et la taille de la police d'un paragraphe :

```css
p {
  color: red;
  font-size: 12px;
}
```

Commençons par le début, avant les accolades. C'est là que va le sélecteur CSS. Dans ce cas, c'est la lettre **p** qui indique la balise HTML `<p>` (paragraphe). Cela signifie que les styles à l'intérieur des accolades s'appliqueront à toutes les balises `<p>` de la page web.

Passons à ce qui va à l'intérieur des accolades – les styles que nous voulons appliquer aux éléments ciblés.

Ici, nous trouvons des paires de propriétés et de valeurs CSS, séparées par un deux-points. Les propriétés (dans ce cas "color" et "font-size") sont à gauche. Les valeurs de ces propriétés (dans ce cas "red" "12px") sont à droite. Un point-virgule termine chaque paire propriété/valeur.

Vous pouvez probablement voir comment cela fonctionne. Les extraits de code CSS ci-dessus indiquent au navigateur d'utiliser des lettres rouges de taille 12px pour tout le texte placé à l'intérieur des balises `<p>`.

Alors, comment une page HTML sait-elle inclure ces styles CSS ? Voici la balise HTML `<link>`. Habituellement, les styles CSS sont créés dans des fichiers séparés (fichiers **.css**) du HTML. Cela signifie que nous avons besoin d'un moyen de les importer dans nos fichiers HTML afin que le navigateur sache que les styles existent.

L'élément `<link>` existe à cet effet. Nous incluons des éléments `<link>` dans la section `<head>` des fichiers HTML qui nous permettent de spécifier les fichiers CSS externes à importer :

```css
<head>

    <title>Mon Titre de Page</title>

    <link rel="stylesheet" type="text/css" href="/home/style.css">

</head>
```

Dans cet exemple, nous importons les styles CSS spécifiés par l'attribut **href**, dans ce cas le fichier */home/style.css*.

Dans les 3 prochaines sections, nous allons (enfin) plonger dans des langages de programmation plus techniques !

Nous allons passer en revue un aperçu général de JavaScript, Python et Java, ainsi que parcourir quelques-uns des concepts de codage essentiels communs aux 3 langages. Nous comparerons et contrastons les fonctionnalités des langages et les exemples de code afin que vous puissiez, espérons-le, obtenir une compréhension bien équilibrée des bases des trois.

## 8) Commencez à programmer avec JavaScript

Commençons par répondre à la question suivante : si nous pouvons utiliser le HTML pour construire la structure d'une page web et le CSS pour la rendre belle, pourquoi avons-nous besoin de JavaScript ?

La réponse est que techniquement, nous n'en avons pas besoin. Si nous sommes satisfaits d'un site statique qui reste là et qui est beau, nous pouvons nous contenter du HTML et du CSS.

Le mot clé ici est "statique". Si, cependant, nous voulons ajouter des fonctionnalités dynamiques à nos pages web, telles que du contenu changeant et des interactions utilisateur plus complexes, nous devons utiliser JavaScript.

### Qu'est-ce que JavaScript ?

Alors, qu'est-ce que JavaScript exactement ? JavaScript est un langage de programmation qui a été créé spécifiquement pour les sites web et Internet. Comme nous l'avons mentionné dans la section 2, la plupart des langages de programmation sont soit compilés soit interprétés, et les programmes sont généralement exécutés de manière autonome.

JavaScript est quelque peu unique à cet égard car il a été conçu pour être exécuté directement dans les navigateurs web. Il nous permet d'écrire du code représentant des ensembles d'actions qui seront exécutées sur nos pages web pour rendre nos sites beaucoup plus dynamiques.

Vous pouvez écrire du code JavaScript dans des fichiers texte nommés avec une extension `.js` ou à l'intérieur de balises `<script>` directement dans le HTML.

Pendant de nombreuses années, le code JavaScript était principalement relégué à s'exécuter à l'intérieur des navigateurs web. Mais le projet **Node.js** a changé ce paradigme en créant un environnement JavaScript autonome qui pouvait s'exécuter n'importe où.

Au lieu d'être piégé dans un navigateur (c'est-à-dire côté client), Node.js peut être installé localement sur n'importe quel ordinateur pour permettre le développement et l'exécution de code JavaScript. Vous pouvez également installer Node sur des serveurs web, ce qui vous permet d'utiliser JavaScript comme code backend pour des applications au lieu de simplement comme code frontend pour navigateur web.

Maintenant que nous avons couvert quelques bases, plongeons dans quelques bases du langage JavaScript.

### Variables et affectation en JavaScript

Les variables représentent probablement le concept le plus fondamental en programmation. Une variable est simplement un nom ou un espace réservé qui est utilisé pour référencer une valeur particulière.

Le mot **variable** implique que la valeur stockée peut changer tout au long de l'exécution du programme.

Vous pouvez utiliser des variables pour stocker des nombres, des chaînes de caractères de texte, des listes et d'autres structures de données dont nous parlerons plus en détail dans un instant.

Tous les langages de programmation utilisent des variables, mais la syntaxe varie entre les différents langages.

Les variables sont utiles car nous pouvons référencer leurs valeurs tout au long de notre code. Cela nous permet de vérifier leurs valeurs selon les besoins et d'effectuer différentes actions en fonction de la manière dont la valeur de la variable change.

En JavaScript, nous déclarons des variables en utilisant le mot-clé `let`, comme ceci : `let x;`.

Cela déclare x comme une variable que nous pouvons utiliser dans notre code. Notez que nous avons ajouté un point-virgule à la fin de la ligne. En JavaScript (et dans de nombreux autres langages), les points-virgules sont utilisés pour spécifier la fin de chaque instruction de code.

Maintenant que nous avons créé la variable *x*, nous pouvons lui assigner une valeur en utilisant le signe égal, également appelé **opérateur d'affectation** : `x = 10;`

Ici, nous avons assigné le nombre 10 à la variable nommée *x*. Maintenant, chaque fois que nous utilisons *x* dans notre code, la valeur 10 sera substituée.

La déclaration de variable et l'affectation peuvent être faites en une seule ligne comme suit :

```javascript
let x = 10;
```

### Types de données en JavaScript

Dans la dernière section, nous avons stocké une valeur entière (nombre entier) dans la variable nommée *x*. Vous pouvez également stocker des nombres décimaux, ou **nombres à virgule flottante** comme on les appelle. Par exemple, nous pourrions écrire : `let x = 6.6;`.

Les différents types de valeurs que nous pouvons stocker dans des variables sont appelés **types de données**. Jusqu'à présent, nous n'avons vu que des types de données numériques (entiers et nombres à virgule flottante), mais nous ne faisons qu'effleurer la surface. Nous pouvons également stocker des données textuelles dans des variables.

En terminologie de codage, un morceau de texte est appelé une **chaîne de caractères**. Nous pouvons stocker une valeur de chaîne dans notre variable x en l'entourant de guillemets simples ou doubles :

```javascript
let x = 'Bonjour !';

let y = "Salut toi !";
```

Le type de données suivant que nous allons discuter est le **booléen**. Un booléen ne peut contenir qu'une des deux valeurs, `true` ou `false` – et elles doivent être en minuscules. En JavaScript, true et false sont deux mots-clés utilisés spécifiquement comme valeurs pour les variables booléennes :

```javascript
let x = true;

let y = false;
```

Notez que les valeurs `true` et `false` n'apparaissent pas entre guillemets comme le font les chaînes de caractères. Si nous les entourons de guillemets, les valeurs seraient des chaînes de caractères, et non des booléens.

Nous utilisons souvent des booléens pour contrôler le flux des programmes dans des instructions conditionnelles (if/else) que nous allons apprendre ensuite.

### Instructions de contrôle de flux de programme en JavaScript

Maintenant que nous avons une compréhension des variables et des types de données JavaScript de base, jetons un coup d'œil à quelques choses que nous pouvons faire avec eux.

Les variables ne sont pas très utiles sans pouvoir dire à notre code de faire quelque chose avec elles. Nous pouvons faire faire des choses à nos variables en utilisant des **instructions**.

Les instructions sont des mots-clés spéciaux qui nous permettent d'effectuer une action dans notre code, souvent en fonction de la valeur d'une variable que nous avons définie. Les instructions nous permettent de définir le flux logique de nos programmes, ainsi que d'effectuer de nombreuses actions utiles qui dicteront le fonctionnement de nos programmes.

#### Instruction If / Else

La première instruction que nous allons discuter est l'instruction `if`. L'instruction `if` nous permet d'effectuer une action uniquement lorsqu'une condition souhaitée est vraie. Voici comment cela fonctionne :

```javascript
let x = 10;

if ( x > 5 ) {
    console.log('X est PLUS GRAND que 5 !');
} else {
    console.log('X n'est PAS PLUS GRAND que 5 !');
}
```

Nous avons défini une variable appelée *x* et lui avons donné la valeur 10. Ensuite, vient notre instruction `if`. Après le mot-clé `if`, nous avons un ensemble de parenthèses contenant la condition à évaluer, dans ce cas, `x > 5`. Nous venons de définir *x* comme étant égal à 10, donc nous savons que cette condition est vraie dans cet exemple.

Puisque la condition dans les parenthèses est vraie, le code entre les accolades sera exécuté, et nous verrons la chaîne "X est PLUS GRAND que 5 !" imprimée à l'écran. (Nous n'avons pas discuté de la signification de `console.log()`, donc pour l'instant, sachez simplement qu'elle imprime la valeur dans les parenthèses à l'écran).

Dans le même exemple, nous avons également inclus une instruction `else`. Cela nous permet d'exécuter un code spécifique dans le cas où la condition est `false`.

#### Boucles While

Le type d'instruction suivant que nous allons discuter est la **boucle while**. Les boucles nous permettent de répéter un bloc de code autant de fois que nous le souhaitons, sans copier et coller le code encore et encore.

Par exemple, supposons que nous devons imprimer une phrase à l'écran 5 fois. Nous pourrions le faire comme ceci :

```javascript
console.log('Ceci est un message très important !');
console.log('Ceci est un message très important !');
console.log('Ceci est un message très important !');
console.log('Ceci est un message très important !');
console.log('Ceci est un message très important !');
```

Cela fonctionne bien pour seulement 5 messages, mais qu'en est-il de 100, ou 1000 ? Nous avons besoin d'une meilleure façon de répéter des morceaux de code plusieurs fois, et les boucles nous permettent de le faire. En terminologie de codage, répéter un morceau de code plusieurs fois est appelé **itération.**

Cette boucle `while` suivante continuera à exécuter le bloc de code à l'intérieur tant que la condition spécifiée reste vraie :

```javascript
let x = 1;

while ( x <= 100 ) {
    
    console.log('Ceci est un message très important !');
    
    x = x + 1;
    
}
```

Dans cet exemple, nous initialisons *x* à la valeur de 1. Ensuite, nous écrivons une boucle `while`. Similaire à l'instruction `if`, nous ajoutons une condition entre parenthèses. Dans ce cas, la condition est `x <= 100`. Cette condition sera `true` tant que *x* est inférieur ou égal à 100.

Ensuite, nous spécifions le bloc de code à exécuter dans les accolades. Tout d'abord, nous imprimons notre message sur la console. Ensuite, nous incrémentons *x* de 1.

À ce stade, la boucle tente de réévaluer la condition pour voir si elle est toujours `true`. La variable *x* a maintenant une valeur de 2 puisqu'elle a été incrémentée lors de la première exécution de la boucle. La condition est toujours `true` puisque 2 est inférieur à 100.

Le code dans la boucle se répète jusqu'à ce que *x* soit incrémenté à la valeur de 101. À ce stade, *x* est supérieur à 100, donc la condition est maintenant `false`, et le code dans la boucle cesse de s'exécuter.

### Le HTML