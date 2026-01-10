---
title: Qu'est-ce que la RAM ? Comment accéder à la RAM de votre ordinateur et lire
  son contenu
subtitle: ''
author: Gursimar Singh
co_authors: []
series: null
date: '2023-04-24T19:31:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-access-and-read-ram-contents
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/ram-article.png
tags:
- name: Computer Science
  slug: computer-science
- name: hardware
  slug: hardware
seo_title: Qu'est-ce que la RAM ? Comment accéder à la RAM de votre ordinateur et
  lire son contenu
seo_desc: "This article is a comprehensive guide on how to read the contents of your\
  \ computer's RAM. \nRandom Access Memory (RAM) is a crucial component of any computer\
  \ system, and it is responsible for temporarily storing data that is required by\
  \ the system to ..."
---

Cet article est un guide complet sur la façon de lire le contenu de la RAM de votre ordinateur. 

La mémoire vive (RAM) est un composant crucial de tout système informatique, responsable du stockage temporaire des données nécessaires au système pour exécuter ses fonctions. Mais le contenu de la RAM peut être assez volatile et est généralement perdu lorsque le système est éteint.

Une façon de préserver le contenu de la RAM est d'effectuer un vidage de la RAM, qui est un processus de copie du contenu de la RAM sur un périphérique de stockage, tel qu'un disque dur. Vous pouvez analyser le vidage de la RAM, et les données qu'il contient peuvent fournir des informations précieuses sur l'état du système au moment où le vidage a été effectué.

Dans cet article, je vais vous guider à travers le processus de lecture du contenu de la RAM, ainsi qu'expliquer ce qu'est un vidage de RAM et comment il peut être utile pour analyser un système informatique. Je vais également vous fournir des instructions étape par étape sur la façon d'effectuer un vidage de RAM et comment analyser les données résultantes.

## Pourquoi lire les données de la RAM ?

Lire des données depuis le disque est quelque chose que vous pourriez être habitué à faire. Mais pouvons-nous également lire des données directement depuis la RAM, où les informations les plus essentielles sont stockées ?

En tant que développeurs, nous pouvons investiguer la complexité spatiale et approfondir la RAM pour comprendre ce qui se passe.

Accéder et lire le contenu de la RAM peut être utile dans une variété de scénarios. Un cas d'utilisation courant est le dépannage et le diagnostic de problèmes avec un système informatique. En examinant le contenu de la RAM, vous pouvez obtenir des informations sur l'état du système à un moment particulier.

Par exemple, si votre ordinateur plante soudainement, examiner le contenu de la RAM peut vous aider à identifier la cause du plantage.

Un autre cas d'utilisation est l'analyse forensique. Lors de l'investigation d'un système informatique pour des preuves de mauvaise conduite, examiner le contenu de la RAM peut fournir des informations précieuses sur les activités qui étaient en cours sur le système.

Par exemple, un professionnel de la sécurité peut utiliser l'analyse de la RAM pour déterminer si un processus particulier était en cours d'exécution sur le système ou pour identifier des fichiers qui ont été récemment accessibles.

De plus, accéder et lire le contenu de la RAM peut également être utile pour les développeurs de logiciels et les chercheurs. En analysant les données stockées dans la RAM, les développeurs peuvent obtenir des informations sur les performances de leur logiciel et identifier des problèmes potentiels ou des goulots d'étranglement. Les chercheurs peuvent également utiliser l'analyse de la RAM pour étudier le comportement des logiciels malveillants ou pour développer de nouveaux outils et techniques de sécurité.

Dans l'ensemble, accéder et lire le contenu de la RAM peut être utile pour le dépannage, l'analyse forensique, le développement de logiciels et la recherche. Cela fournit un moyen précieux d'obtenir des informations sur le fonctionnement interne d'un système informatique et peut aider à identifier des problèmes et des menaces de sécurité potentielles.

Avant d'aller plus loin dans les détails, prenons un bref aperçu de la nomenclature. Cela peut être une connaissance commune, mais vous devrez comprendre la terminologie au fur et à mesure que vous parcourez ce guide, donc cela vaut la peine de faire une révision.

## Qu'est-ce que la RAM ?

Il existe un périphérique matériel physique appelé RAM (qui signifie Random Access Memory) : la mémoire physique, un CPU, un disque dur et d'autres composants physiques.

Par-dessus cela, nous avons le système d'exploitation. Le système d'exploitation est toujours en conversation avec la pièce de matériel connue sous le nom de "kernel" – et c'est l'un des aspects les plus critiques de ce logiciel.

Si nous considérons les choses du point de vue de l'utilisateur, nous nous connectons initialement au système d'exploitation afin de pouvoir effectuer nos tâches, dont la majorité inclut l'exécution d'applications.

### Qu'est-ce que le Kernel ?

Un kernel est une portion fondamentale d'un système d'exploitation qui accepte les instructions de l'utilisateur avec l'aide du programme que nous exécutons en arrière-plan. Cela peut se produire indépendamment du programme que nous exécutons en arrière-plan.

Tout ce qui doit être calculé est géré par l'unité centrale de traitement (CPU), mais quoi que nous fassions et comment que nous gérions les services fournis par le CPU, les données, les instructions, le code et le programme doivent tous passer par la mémoire vive (RAM).

Cela implique que les résultats de tout ce que nous faisons avec les données à un moment donné seront disponibles au sommet de la mémoire. Si vous êtes un programmeur et que vous construisez une sorte de structure de données, cela indique que toutes les données vivront au sommet de la RAM.

Nous pouvons aller directement à la RAM et voir comment les structures de données ont été créées et comment elles s'alignent, et nous pouvons voir comment la complexité spatiale fonctionne là-bas.

Par exemple, si nous discutons de n'importe quel navigateur web, comme Chrome, il peut y avoir eu des failles de sécurité générées dans une application. Donc la méthode la plus efficace est de naviguer vers la RAM et d'investiguer comment les données ont fonctionné.

Disons que vous ouvrez n'importe quel site web sécurisé dans Chrome (ou n'importe quel navigateur), comme gmail.com. Toutes les informations que vous entrez dans Gmail, y compris votre nom d'utilisateur et votre mot de passe, sont envoyées sur internet à un serveur géré par Google. Ces données ont été entièrement cryptées, et il sera difficile, sinon impossible, de craquer le mot de passe.

Mais afin d'entrer votre mot de passe, vous utilisez probablement un ordinateur avec un clavier attaché. Après cela, certains programmes crypteront les données et les enverront sur internet. Cela signifie qu'initialement, vos données étaient présentes dans la RAM.

Tout d'abord, le mot de passe est une donnée standard, et le mot de passe va et atterrit au sommet de la RAM. Ensuite, certains programmes crypteront les données et les enverront sur internet. Si vous pouvez accéder à la RAM, vous pouvez l'examiner pour déterminer si votre mot de passe a été crypté ou non. Et ce processus est assez simple.

Regardons un exemple pour voir comment cela fonctionne. Nous allons prétendre que "a" est une variable et "9" est la donnée. Lorsque nous exécutons le programme, cette donnée se charge sur la RAM. Lorsque le programme se termine, les données de la RAM auront disparu, bien que personne ne l'ait encore prouvé. Mais c'est le cas, et nous pouvons le prouver avec une petite investigation.

Alors, comment pouvons-nous vérifier si cette donnée est toujours présente dans la RAM après que l'application a fini de s'exécuter si elle a été chargée tout en haut de la mémoire ?

Eh bien, la RAM sera bientôt effacée de ces contenus. Un "vidage de RAM" est le processus de capture de toute la RAM. Cela démontre la forme réelle dans laquelle l'ensemble de données complet est rendu accessible et chargé sur la RAM pour la première fois. Et vous apprendrez comment capturer ou extraire les données de la mémoire ensuite.

Afin d'accomplir cela, vous aurez besoin d'une forme de logiciel. Par conséquent, l'objectif de ce programme est de voyager plus loin dans la mémoire. Il ira dans la mémoire et récupérera toutes les données stockées dans la mémoire avant de continuer.

### Qu'est-ce que LiME ?

L'extracteur de mémoire Linux, parfois appelé LiME, est un logiciel puissant. C'est ce que vous utilisez pour extraire la mémoire de Linux. Ce logiciel est également connu sous le nom de driver, également appelé module. Cela est dû au fait que la RAM est un périphérique, ce qui complique encore les choses.

Nous avons besoin d'une forme de driver pour accéder au périphérique afin que nous puissions essayer de lire son contenu. LiME est un exemple de driver, et si vous êtes familier avec Linux, vous savez peut-être que pour faire fonctionner un driver, vous devez charger ce driver avec l'assistance du kernel.

Dans le contexte de Linux, un driver est également appelé un module. Donc LiME est un module du kernel Linux. Nous avons accès à ce qui est connu comme un module chargeable du kernel, ce qui nous permet d'installer le module sur le système d'exploitation.

Nous avons couvert suffisamment de contexte. Maintenant, regardons comment nous pouvons extraire le contenu de la RAM. Nous allons passer par le processus étape par étape de manière pratique.

## **Installation** et **Configurations**

Donc, la seule chose dont nous avons besoin est le driver LiME. Voici le lien pour télécharger ce module particulier : [https://github.com/gursimarsm/LiME](https://github.com/gursimarsm/LiME).

Maintenant, démarrez votre système Linux (j'utilise RedHat Enterprise Linux). Vous pouvez utiliser la commande **`free -h`** pour vérifier la quantité de mémoire RAM utilisée, disponible et d'autres détails. Le mien ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-186.png)
_Sortie de l'exécution de la commande `free -m`_

Pour accéder à la RAM, nous avons besoin d'un logiciel où le kernel peut charger des modules supplémentaires. Dans notre cas, le nom du module est LiME. Donc, les logiciels que nous installons sont appelés "**kernel-devel**" et "**kernel-headers**". Ces deux logiciels sont ceux dont nous avons besoin pour installer afin d'effectuer nos actions ultérieures, c'est-à-dire utiliser le module LiME.

Si vous souhaitez installer le logiciel, vous devez avoir "yum" configuré. Pour contexte, **yum** est une commande que vous pouvez utiliser pour installer le logiciel dans le système d'exploitation RedHat Linux. Je vais démontrer comment le configurer dans l'annexe pour référence.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-187.png)
_Installation_

Maintenant que vous avez installé ce logiciel, vous avez besoin d'un autre logiciel car vous devez télécharger certains drivers depuis GitHub. Donc, maintenant vous devez installer Git si vous ne l'avez pas déjà. Vous pouvez le faire en utilisant la commande **`yum install git`**. Vous devez également configurer votre compte pour pouvoir travailler avec.

```bash
# git config --global user.name "Votre Nom" 

# git config --global user.email "vous@example.com"  
```

J'ai partagé le dépôt ci-dessus. C'est un module de kernel chargeable (LKM). Il vous permet d'acquérir toute la mémoire de votre système d'exploitation Linux ou de tout type de système d'exploitation (y compris les appareils Android car Android est également basé sur Linux).

Vous pouvez télécharger le module en utilisant la commande `**# g**it clone**** [**https://github.com/gursimar**sm**/LiME**](https://github.com/gursimarsm/LiME)`.

Après avoir téléchargé cela, vous devez vous déplacer dans le répertoire du logiciel. Vous y trouverez plusieurs dossiers. Mais, pour exécuter le code principal, vous devez vous déplacer dans le répertoire "src".

Dans ce répertoire, vous trouverez plusieurs programmes basés sur le langage C. Donc, afin d'utiliser les fichiers, vous devrez les compiler. Pour cela, vous pouvez utiliser la commande **`make`**. Installez cela comme suit :

```bash
# yum install make 

# yum install gcc       
```

Dans le répertoire /LiME/src/, exécutez la commande **`make`** pour compiler tout le code.

Si vous rencontrez une erreur, cela peut être dû au fait que nous utilisons la dernière version de LiME, et elle vient avec une nouvelle fonctionnalité appelée orc metadata generate. Pour implémenter cette fonctionnalité, vous devez installer une chose supplémentaire qui fait partie de LiME appelée **`elfutils-libelf-devel`**. Vous pouvez le faire en utilisant yum comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-188.png)
_Comment installer **`elfutils-libelf-devel`**_

Après cela, si nous exécutons maintenant la commande `make`, elle demandera au compilateur GCC de compiler tout le code. Après la compilation, elle créera un fichier objet final appelé le fichier objet du kernel, et c'est le module final dans LiME.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-189.png)
_Sortie_

Vous pouvez trouver ce fichier dans le même répertoire en utilisant la commande **`ls`**. 

## **Comment utiliser le module**

Avec ce module, le kernel a maintenant la capacité de capturer ou de lire toute la RAM. Par défaut, nous ne pouvons pas lire toute la RAM en une seule fois, mais maintenant grâce au module LiME, nous pouvons.

Pour en savoir plus sur le module LiME, vous pouvez utiliser la commande **`modinfo`**. Tapez `modinfo` avec `lime`. Cela vous montrera plus de détails comme où le fichier est disponible, et il affiche également tous les modules ou drivers qui viennent avec certains paramètres supplémentaires. Chaque paramètre a certains avantages.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-190.png)
_modinfo_

Ici, nous allons utiliser deux paramètres qui sont très importants : `path` et `format`.

`path` signifie que lorsque nous lisons toute la RAM, nous devons stocker les données de la RAM dans un fichier. Donc, pour spécifier le fichier de destination que nous souhaitons créer, nous devons donner cette information particulière ici.

Le paramètre suivant, `format`, spécifie le format dans lequel nous voulons lire les données de la RAM. Donc, dans ce cas, nous voulons lire le format de la RAM tel quel. Les données stockées dans la RAM sont principalement en binaire, et nous voulons lire toutes les données dans ce format binaire uniquement et les capturer dans leur forme brute.

Donc, le format sera brut et stocké dans le fichier où que nous donnions le chemin.

Enfin, il est temps de lire les données de la RAM. Donc, passons à la commande principale qui nous aidera à commencer à lire toute la RAM.

### Démonstration

Tapez votre mot de passe pour votre compte Gmail dans Chrome pour cette démonstration. Cela vous aidera à apprendre comment capturer les données de la RAM et également si votre mot de passe est crypté.

Pour vérifier ces deux choses, passez à l'invite de commande et vérifiez si les données sont toujours sur la RAM. Vous devrez charger un module particulier en utilisant la commande **`insmod`**. Cela vous aidera à insérer le module.

Copiez le chemin complet du module et collez-le avec la commande `insmod`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-191.png)
_commande `insmod`_

Ce module sera chargé avec l'aide du kernel. Le module commencera à capturer toutes les données de la RAM et les stockera dans un fichier, par exemple, myram.data

Il chargera également le vidage complet de la mémoire ou le vidage de la RAM dans ce fichier et dans le format que nous voulons capturer. Donc, le format sera le format brut.

Nous utiliserons ces deux paramètres (ne vous inquiétez pas pour cela pour l'instant). Nous avons besoin de seulement deux paramètres pour effectuer, et maintenant dès que nous exécutons cette commande, toutes les données que nous avons seront capturées et stockées dans ce fichier particulier. Cette commande prend généralement quelques secondes, selon la vitesse du CPU et la quantité de données que nous avons dans la RAM.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-192.png)
_Commande_

### Comment lire les données

Maintenant, nous avons ce fichier myram.data et toutes les données de la RAM sont stockées dans ce fichier. Parce que nous avons capturé ces données au format brut, les données seront en binaire. Si nous essayons de lire ces données directement depuis ce fichier, en tant qu'êtres humains, nous ne pouvons pas les lire même si nous essayons avec les premières lignes en utilisant la commande head pour lire certaines des 10 premières lignes.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-193.png)
_Sortie_

Donc, nous pouvons utiliser la commande "cat", qui lira toutes les données. Mais, encore une fois, la même chose va se produire – elle lira toutes les données, mais les données seront affichées au format binaire. Ensuite, nous devons utiliser la fonction pipe avec cette commande et la combiner avec une autre nouvelle commande appelée `strings` :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-194.png)
_Commande_

String est une commande qui convertira les données en texte régulier dans un format lisible par l'homme.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-195.png)
_Sortie_

La liste continuera et continuera. Vous pouvez l'interrompre en utilisant **Ctl+C**.

Pour l'instant, cela ne signifiera pas grand-chose de voir et de lire toutes les données. Nous savons que certaines données présentes dans la RAM sont le mot de passe appelé mywebpasswordgmail. Donc, juste pour confirmer que ces données sont disponibles sur la RAM, nous pouvons utiliser un autre pipe avec la commande `grep`. La commande grep nous aide à trier les données.

```bash
cat /myram.data | strings | grep mywebpasswordgmail 
```

Maintenant, nous recherchons cette chaîne dans toutes les données. Elle convertira les données en texte régulier, et partout où cette chaîne particulière apparaît, grep attrapera cette ligne et nous permettra de commencer à rechercher, puis nous montrera ces données.

Donc, comme vous pouvez le voir dans cet exemple simple, tout ce que vous tapez sur votre clavier peut également aller dans la RAM – même si c'est votre mot de passe ou un site sécurisé que vous surfez, vos données sont là sur la RAM. Peu importe quel programme vous exécutez. Si vous tapez en utilisant le clavier, tout sera chargé sur la RAM et pourra être extrait. Cela s'appelle le vidage de mémoire.

LiME nous fournit de nombreuses autres capacités puissantes. Pour l'instant, nous capturons les données directement depuis le système où nous effectuons les actions. Mais nous pouvons également exécuter LiME sur le système et il peut capturer les données en temps réel et envoyer les données sur le réseau à un autre ordinateur.

Que signifie cela ? Pensez-y de cette manière : par exemple, quelqu'un ouvre un site web et tape quelque chose en temps réel. Ce message entier est transmis en temps réel à un autre ordinateur.

Nous ne parlons pas de keyloggers, nous parlons simplement de la RAM. Tout ce qui se passe lorsque n'importe quel programme est en cours d'exécution, la base de données stocke certaines données. Les programmes lisent les données depuis d'autres parties du disque dur. Et tout ce qui se passe sur la RAM peut être capturé en temps réel par le système et envoyé sur le réseau à d'autres ordinateurs.

# Conclusion

Nous sommes enfin arrivés à la fin de cet article. J'espère que vous l'avez apprécié et que vous avez appris quelque chose de nouveau.

Je suis toujours ouvert aux suggestions et aux discussions sur [LinkedIn](https://www.linkedin.com/in/gursimarsm). Envoyez-moi des messages directs.

Si vous avez apprécié mon écriture et souhaitez me motiver, envisagez de laisser des étoiles sur [GitHub](https://github.com/gursimarsm) et de m'endosser pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/gursimarsm).

Jusqu'au prochain, restez en sécurité et continuez à apprendre.