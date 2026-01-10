---
title: 'Comprendre les internes de Java : Vitesse et Performance'
subtitle: ''
author: Okoye Chukwuebuka Victor
co_authors: []
series: null
date: '2023-09-24T13:44:14.000Z'
originalURL: https://freecodecamp.org/news/understanding-java-internals-speed-and-performance
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/terry-vlisidis-WsEbnsnKbUE-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: 'Comprendre les internes de Java : Vitesse et Performance'
seo_desc: 'In most conversations about programming, speed, and efficiency in Java
  are reoccurring terms as it''s a language native to these features.

  You might ask, what is Java? You may also wonder what it means for a programming
  language to be interpreted or c...'
---

Dans la plupart des conversations sur la programmation, la vitesse et l'efficacité en Java sont des termes récurrents car c'est un langage natif de ces caractéristiques.

Vous pourriez vous demander, qu'est-ce que Java ? Vous pourriez également vous interroger sur ce que signifie pour un langage de programmation d'être interprété ou compilé. Explorons ces concepts dans les sections suivantes.

## Qu'est-ce que le langage de programmation Java ?

Java est un langage de programmation indépendant de la plateforme et adopte la structure de programmation orientée objet pour construire des logiciels. Il n'est pas seulement limité au web mais aussi aux applications mobiles et de bureau.

Vous pourriez vous demander ce que signifie être indépendant de la plateforme. Cela concerne la capacité des programmes Java à fonctionner sans effort sur divers systèmes d'exploitation comme Windows, Mac et Linux.

Contrairement à des langages comme C ou C++, qui peuvent être limités à un seul système d'exploitation, l'adaptabilité de Java élimine la limitation de dépendre d'un système d'exploitation spécifique pour fonctionner.

Pour mieux comprendre Java, examinons son histoire et le but pour lequel il a été créé.

### Une brève histoire de Java

En 1991, Java a été développé par James Gosling et son équipe chez Sun Microsystems. La première version du langage, 1.0, a été publiée en 1996.

Il a été conçu pour avoir une syntaxe similaire à d'autres langages de haut niveau comme C et C++, afin que les ingénieurs de l'époque n'aient pas de problème à comprendre et à développer un programme avec Java.

Il a été développé dans l'intention de développer l'interactivité télévisuelle, mais il était trop avancé pour son époque. L'infrastructure technologique et les appareils de cette époque n'étaient pas suffisamment préparés pour tirer parti des fonctionnalités avancées de Java.

De nos jours, nous avons vu Java toujours sous les projecteurs car c'est le logiciel que la plupart des grandes entreprises technologiques adoptent en raison de sa polyvalence. Il est très demandé en tant que langage principal pour construire des applications de niveau entreprise sur différentes plateformes.

En continuant notre exploration du fonctionnement interne de Java, il y a quelques concepts clés que vous devez comprendre. Ces concepts sont de comprendre ce que signifie pour un langage de programmation d'être interprété ou compilé.

### Langages interprétés vs compilés

Nous avons souvent entendu ces termes, mais pour mieux les comprendre, imaginons un étudiant étranger entreprenant deux voyages vers différentes destinations.

Dans le premier scénario, ils arrivent à destination sans connaître la langue locale ou les coutumes, ils dépendent donc d'un interprète ou d'un traducteur pour pouvoir communiquer avec les habitants de cette région. Cela ressemble beaucoup à la façon dont un interprète dans un langage de programmation interprété traduit le code à la volée pour que l'ordinateur comprenne.

Dans le second scénario, l'étudiant a eu la prévoyance de participer à des cours pour apprendre la langue dont il aura besoin et est familier avec les coutumes de l'endroit où il se rendra. À l'arrivée, il n'a pas besoin d'un interprète pour communiquer avec les habitants de cette région. Cela est similaire au fonctionnement d'un langage compilé.

En comprenant ces deux scénarios, vous pouvez repérer les différences entre un langage interprété et un langage compilé.

Le premier traduit chaque ligne de code à la volée. C'est une traduction en temps réel, comme l'étudiant de l'exemple qui a utilisé un traducteur/interprète.

D'autre part, ce dernier prédigère d'abord le code pour assurer un flux fluide. Ensuite, il le "compile" ou le transforme en code machine que l'ordinateur peut comprendre et exécuter, similaire à notre étudiant préparé communiquant couramment.

Chacun de ces termes de programmation a un but similaire de permettre la communication entre les systèmes informatiques et les programmeurs.

Maintenant, alors que vous vous interrogez plus profondément sur ces termes de programmation, comprenons comment Java fonctionne.

## Comment fonctionne Java ?

Java est unique dans le sens où il est à la fois compilé et interprété.

Le flux de base est qu'il est d'abord compilé à partir du code source en ce que nous appelons le bytecode. Ensuite, il est interprété en code machine à l'aide d'un interprète nommé JVM, qui signifie Java Virtual Machine. Cette interprétation se produit au moment de l'exécution, vous pouvez donc considérer Java comme un langage interprété et aussi un langage compilé.

Maintenant, vous pourriez vous demander ce qu'est le bytecode ?

Les termes courants que nous entendons dans la compilation et l'interprétation des programmes sont principalement le code source et le code machine. Le bytecode est similaire au code machine dans le sens où il s'agit d'un code source compilé, mais il n'est pas exécutable sauf s'il est interprété par une machine virtuelle, dans ce cas, la Java Virtual Machine.

### Qu'est-ce qu'une machine virtuelle Java ?

La JVM (Java Virtual Machine) est une machine virtuelle dépendante de la plateforme qui interprète et exécute les programmes Java en bytecode et tout autre programme d'autres langages qui compile en bytecode Java.

Le bytecode Java a une qualité spéciale : il n'est pas lié à une plateforme spécifique.

Le bytecode Java, qui est similaire à un dialecte universel, peut être exécuté par une machine virtuelle Java (JVM) sur la plupart des systèmes d'exploitation que vous pouvez imaginer. Actuellement, lorsque la JVM commence son traitement, elle convertit ce bytecode en code machine qui correspond exactement au système d'exploitation sur lequel elle s'exécute.

Mais voici où cela devient intéressant : bien que le bytecode Java soit comme un caméléon qui peut s'adapter à différentes plateformes, la JVM elle-même n'est pas tout à fait aussi flexible. C'est comme avoir différentes versions d'un outil, chacune fabriquée sur mesure pour un système d'exploitation spécifique.

Ainsi, vous avez différentes versions de JVM pour correspondre à la variété de systèmes d'exploitation disponibles.

Maintenant, vous pourriez vous demander, puisque Java subit deux processus, la compilation et l'interprétation, cela le rend-il lent ? La réponse est non. Bien qu'il subisse divers traitements, il reste rapide.

Pour comprendre cela, nous devons discuter de quelques fondamentaux observés dans la JVM tels que le JIT (Just In Time Compilation), Hotspot JVM, et son unicité de mémoire/stockage.

## Comment Java atteint-il une haute vitesse ?

Il est important de noter que Java a rationalisé sa compilation pour une exécution rapide et a pris l'indépendance de plateforme d'un langage interprété.

Les langages compilés sont connus pour leur rapidité de traitement car ils convertissent le code source entièrement et non ligne par ligne, contrairement à leur homologue, les langages interprétés. Java compile en bytecode qui est plus rapide à interpréter en utilisant la JVM grâce au bytecode étant déjà très compact et optimisé.

La JVM possède plusieurs composants tels que sa capacité à manipuler la mémoire au moment de l'exécution. Grâce à la gestion automatique de la mémoire, moins de temps est consacré à l'allocation de la taille de la mémoire pour les données en utilisant son ramasse-miettes intégré.

### Comment utiliser le compilateur JIT pour obtenir une exécution plus rapide

Une autre caractéristique intéressante de la JVM, qui aide à réduire le temps passé à améliorer la vitesse de traitement du code, est le JIT, qui est un acronyme pour Just In Time.

Le compilateur JIT est au cœur du moteur d'exécution dans la JVM. Il observe pendant que le bytecode est interprété et exécuté, et stocke un "Hotspot". Il s'agit d'un ensemble répété de bytecode exécuté.

Au lieu de réinterpréter et d'exécuter ce même bytecode à nouveau, le compilateur JIT stocke ce bytecode fréquemment exécuté en mémoire sous forme de code machine natif pour une utilisation future.

Ce code machine mis en cache est ce qui est exécuté lorsque vous exécutez votre bytecode, ce qui entraîne un temps d'exécution plus rapide. Ce processus entier peut être appelé une compilation dynamique.

### Qu'est-ce que le ramasse-miettes et comment améliore-t-il les performances de la JVM ?

La JVM est unique dans la manière dont elle automatise la gestion de la mémoire. Cela implique l'allocation de mémoire pour les programmes qu'elle exécute.

Contrairement à C/C++, où vous écrivez un code puis calculez manuellement l'allocation de mémoire du programme, cette fonctionnalité améliore et renforce la productivité des programmeurs. Elle réduit également certaines erreurs qui peuvent résulter d'un manque de mémoire ou de fuites de mémoire.

Le ramasse-miettes aide à cela en récupérant automatiquement la mémoire occupée par des objets dans un programme qui ne sont plus utilisés. Ce faisant, il libère cette mémoire pour une utilisation future.

Vous pourriez vous demander comment cela fonctionne. Il suit les étapes décrites ci-dessous :

* Il identifie d'abord les objets inaccessibles. Ce sont des objets dans un programme qui ne sont pas utilisés. Il est strict dans cette tâche car si un objet utilisé est sélectionné et récupéré, cela fera planter notre programme car il y aura une erreur d'objet référencé. C'est un terme appelé références pendantes.
* Ensuite, il récupère la mémoire des objets inutilisés sélectionnés, ce qui libère de la mémoire pour d'autres objets futurs.
* Dans certains cas, lors de cette collecte, le ramasse-miettes compacte les objets restants en mémoire, ce qui améliore la localité de la mémoire. Cela est facultatif, car cela dépend des algorithmes de collecte des déchets utilisés.

Voici un aperçu de la manière dont le processus de ramasse-miettes fonctionne dans la machine virtuelle Java.

Selon l'algorithme de ramasse-miettes en place, il est important de noter que la collecte est déclenchée par la JVM lorsqu'elle détecte un faible espace mémoire et lance les étapes ci-dessus.

Il est également essentiel de noter que parfois une pause dans l'exécution se produira afin de libérer de l'espace mémoire.

### Optimisation du bytecode

Il existe certaines techniques supplémentaires effectuées sur le compilateur qui aident à améliorer les performances.

Le compilateur optimise le bytecode en notant les calculs similaires. Au lieu de réexécuter ces calculs, il se contente de sortir le résultat. Cela s'appelle le repliement de constantes.

Il supprime également les codes hors de portée ou les codes qui ne seront jamais exécutés. Ce faisant, il élimine les calculs inutiles.

Une autre technique utilisée par le compilateur est l'optimisation par trou d'aiguille, qui implique le remplacement des instructions de bytecode par une séquence plus efficace.

De nombreux facteurs contribuent à la performance et à la vitesse des programmes Java.

Cela va du fait qu'il est à la fois compilé et interprété, aux intrications de certains composants de son interprète (la machine virtuelle Java). Tous ces éléments jouent un rôle majeur dans l'atteinte d'une haute vitesse.

En fin de compte, pour avoir des programmes plus rapides, le programmeur doit écrire un code plus propre et organisé en utilisant de bonnes structures de données.

## Conclusion

Dans cet article, vous avez appris une brève histoire de Java et les différences entre les langages compilés et interprétés. Vous avez également appris sur certains des principaux composants de Java, tels que la machine virtuelle Java, et comment elle contribue à la performance des programmes Java.

Si vous avez aimé lire cet article, vous pouvez le partager et me suivre sur [Twitter](https://twitter.com/okoyevictorr) et [Linkedin](https://www.linkedin.com/in/okoye-chukwuebuka/).