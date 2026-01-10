---
title: Méthodes Agile et Méthodologie pour Débutants – Développement Logiciel Agile
  et Exemples de Gestion de Projet Agile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T22:34:44.000Z'
originalURL: https://freecodecamp.org/news/agile-methods-and-methodology-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98cc740569d1a4ca1c1c.jpg
tags:
- name: agile
  slug: agile
- name: agile development
  slug: agile-development
- name: software development
  slug: software-development
seo_title: Méthodes Agile et Méthodologie pour Débutants – Développement Logiciel
  Agile et Exemples de Gestion de Projet Agile
seo_desc: "By Adam Naor\nAgile is a methodology for approaching software development.\
  \ It consists of different frameworks such as SCRUM or Kanban that help development\
  \ teams continuously build, test, and gather feedback on their product. \nAgile\
  \ consists of four ..."
---

Par Adam Naor

Agile est une méthodologie pour aborder le développement logiciel. Elle se compose de différents frameworks tels que SCRUM ou Kanban qui aident les équipes de développement à construire, tester et recueillir continuellement des feedbacks sur leur produit. 

Agile repose sur quatre principes fondamentaux :

1. Les individus et les interactions plutôt que les processus et les outils
2. Un logiciel fonctionnel plutôt qu'une documentation exhaustive
3. La collaboration avec le client plutôt que la négociation contractuelle
4. Répondre au changement plutôt que suivre un plan

Je reviendrai sur ces principes plus tard et les expliquerai plus en détail. Pour ce faire, il est important de faire un pas en arrière et de comprendre les pratiques de développement logiciel précédemment utilisées.

## Méthode en Cascade (Waterfall)

Le développement en cascade est une approche très linéaire pour construire un produit. Il laisse peu ou pas de place pour les feedbacks ou les itérations jusqu'à ce que le produit soit complètement construit et testé. 

Voici comment cela fonctionne : les équipes passent des semaines (et parfois des mois) à rédiger des documents de spécifications produits. 

Avant qu'une seule ligne de code ne soit écrite, les chefs de produit, les analystes et les designers rassemblent un document massif qui décrit les exigences du produit dans les moindres détails. 

Pour le moins, c'est un processus long et laborieux dans lequel, inévitablement, certaines choses sont oubliées. 

Voici une simple expérience de pensée. Pensez à Google Search ou à un outil de recherche d'emails clients.

Essayez maintenant d'imaginer le document de spécifications pour ces produits. 

Sans aucun doute, des choses importantes seront oubliées. On ne peut tout simplement pas concevoir les cas d'utilisation, l'échelle ou la portée de l'évolution de ces produits au fil du temps.

Si vous avez construit un produit - en tant que développeur solo ou membre d'une équipe - vous pouvez probablement vous identifier à cette affirmation. 

Lorsque tout est convenu, les spécifications sont transmises à l'équipe d'ingénierie qui construit alors le produit selon les spécifications, en utilisant des données qualitatives et quantitatives.

Lorsque tout est codé, les tests commencent. 

Si c'est un produit complexe, les tests et la correction des bugs peuvent prendre des semaines ou des mois, car l'ensemble du produit doit subir un examen rigoureux. Lorsque les testeurs et les chefs de produit valident les exigences de test, le produit est prêt à être déployé en production. 

Il y a plusieurs inconvénients au développement en cascade, en voici quelques-uns.

### Manque de mécanismes de feedback intégrés

Que se passe-t-il si l'équipe de développement suit les spécifications à la lettre et qu'il s'avère que voir le produit prendre vie n'est pas aussi convaincant que ce que l'équipe produit avait imaginé ? Ou pire encore, que se passe-t-il s'il y avait une erreur dans le document de spécifications ? 

Avec le développement en cascade, vous ne connaîtrez pas les réponses à ces questions avant que le produit ne soit déjà construit. 

Le développement de produits peut entraîner des coûts fixes élevés. Si le produit ne fonctionne pas, ces coûts peuvent devenir des coûts irrécupérables. 

Les coûts irrécupérables sont l'ennemi du constructeur, car un coût irrécupérable est un coût qui a déjà été engagé et ne peut pas être récupéré.

### Et si la feuille de route change ?

Cela arrive tout le temps. Cela arrive sur l'ordinateur que vous utilisez pour lire cet article, cela arrive dans votre entreprise, et cela arrive dans les entreprises technologiques, grandes et petites.

Que se passe-t-il si la feuille de route change et que l'équipe doit se concentrer sur autre chose ? Avec la méthode en cascade, vous vous retrouvez avec un produit inutilisable. Pensez : rigidité.

Encore une fois, si vous ne pouvez pas transformer vos coûts fixes en quelque chose de flexible, vous vous retrouverez avec une grosse facture et peu de résultats à montrer. 

Tout le travail dédié, les délais stressants et les nuits tardives ne mèneront pas aux résultats que vous souhaitiez au début du projet.

### Le produit prend la poussière jusqu'à ce qu'il soit enfin livré

Au lieu de livrer des améliorations incrémentielles en production sur une période de temps, la méthodologie en cascade attend de livrer l'ensemble du produit jusqu'à la toute fin.

Bien que ce soit une approche raisonnable pour construire une voiture, ce n'est pas une bonne approche pour le logiciel.

Le logiciel, contrairement aux voitures, est flexible dans les entrées de conception.

Les gens ne peuvent pas utiliser des voitures à moitié produites. Mais nous utilisons des logiciels à moitié construits tout le temps. 

## Entrez dans l'Agile

Agile aide à résoudre ces problèmes en permettant aux équipes de développement de produits de construire continuellement des fonctionnalités qui ajoutent de la valeur. Il permet également aux équipes de recevoir régulièrement des feedbacks sur leur travail et d'apporter des modifications si nécessaire. 

Avec l'emploi des méthodes Agile, les équipes livrent de manière constante et prévisible de petits morceaux de code en production à un rythme rapide.

Une fois qu'ils ont terminé toute sorte de fonctionnalité qui ajoutera de la valeur, ils la testent et la publient dans le monde. C'est une approche itérative de la construction technologique. 

Au lieu de prendre des mois pour construire un produit final et effectuer un test de bout en bout, le développement Agile permet aux équipes de construire continuellement de plus petites parties du produit final et de les ajouter à la production au fil du temps. 

Cela signifie que les tests vont plus vite puisque vous ne testez que la compatibilité du dernier morceau de code. Cela signifie également que les utilisateurs et les parties prenantes sont plus satisfaits car ils peuvent voir et utiliser les dernières améliorations du produit de manière continue. 

Considérez les deux approches avec un exemple concret de rénovation d'une cuisine. Supposons qu'il faudra six mois pour faire le travail de rénovation correctement. 

La méthode en cascade suggérerait que l'entrepreneur et son équipe reconstruisent entièrement la cuisine, puis révèlent toute la cuisine au client après les six mois. 

Bien que le travail soit fait dans le même laps de temps, le propriétaire est laissé dans l'ignorance. Des questions simples comme "comment cela avance-t-il" restent largement sans réponse. Pire encore, les propriétaires ne peuvent utiliser aucune partie de la cuisine jusqu'à la toute fin.

Avec Agile, l'entrepreneur déterminerait plutôt ce que son équipe pourrait accomplir toutes les quelques semaines, puis permettrait à son client de le voir et de l'utiliser pendant qu'ils rénovent le reste. 

Peut-être peuvent-ils remplacer les armoires le premier mois, les plans de travail le deuxième mois, et d'ici le troisième mois, ils installent un nouveau réfrigérateur et une nouvelle cuisinière. Pas un mauvais résultat pour les deux parties !

Dans la deuxième approche, le propriétaire bénéficie de l'utilisation de parties de la cuisine avant que tout ne soit terminé. Au lieu que la nouvelle cuisinière ne reste là à prendre la poussière, elle est réellement utilisée dès qu'elle peut l'être. 

Et peut-être que le propriétaire de la cuisine veut échanger une armoire contre une étagère ?  

L'entrepreneur peut maintenant au moins planifier ce changement avant la fin des six mois et informer le propriétaire de la manière dont cela affectera le calendrier du projet. 

Apparemment, les deux parties peuvent travailler ensemble et communiquer de manière transparente pour garantir que les bons résultats et le bon travail soient accomplis.

Ce sont quelques-uns des nombreux avantages de l'Agile. Les deux parties en sortent gagnantes. 

Essayez de tirer cette leçon vers l'avant alors que vous apprenez de nouvelles compétences de développement sur freeCodeCamp et appliquez vos compétences sur des projets.

## Considérons quelques autres exemples dans le monde du logiciel

En revisitant les quatre principes de l'Agile, nous pouvons maintenant commencer à trouver des exemples de l'application de l'Agile dans les mondes réel et numérique.

J'espère que vous pouvez maintenant voir comment ces principes sont une attaque directe contre le processus en cascade. 

### Principe #1 : Les individus et les interactions plutôt que les processus et les outils

Avoir un processus solide et un ensemble d'outils est très important dans l'Agile. Cependant, valoriser les individus et les interactions plutôt que les outils permet de créer plus de valeur et de production. 

Les membres individuels de l'équipe peuvent innover. 

Au lieu de forcer les gens à se conformer à des idéations et des spécifications strictes, vous pouvez leur donner plus de latitude pour expérimenter.

Faire passer les individus avant les outils inclut l'expérimentation de nouveaux flux de travail. Un exemple pertinent pour l'innovation dans le développement logiciel Agile est le codec, un programme informatique qui encode ou décode un flux de données numériques ou des signaux. 

Le codec H266/VVC utilise environ la moitié des données pour diffuser des vidéos 4K. Et il est reconnu comme la solution de codage la plus efficace pour le futur streaming en temps réel 4K et même 4K VR. 

Comment cette découverte a-t-elle été faite ? Elle a été faite par des personnes utilisant l'Agile pour résoudre des problèmes de compression vidéo.

Plus précisément, elle a été faite parce que les individus ont été libres de construire, tester, expérimenter et innover sur une période de temps. On ne leur a pas dit de construire la cuisine à partir de zéro et de revenir dans six mois.

Ils ont fait de petits pas dans la bonne direction. Ce résultat est instructif.

Voici un deuxième exemple : lorsque Lastpass a été acquis par LogMeIn, LogMeIn s'intéressait autant à la technologie qu'à la culture de conception que Lastpass avait mise en place pour construire des produits. 

Quel type de culture était-ce ? Une qui priorisait l'Agile.

L'Agile ne permet pas seulement de mettre des produits sur le marché plus rapidement, mais il crée également des résultats créatifs et synergiques qui sont précieux.

Créer de la valeur est intégré dans la culture de l'Agile.

### Principe #2 : Un logiciel fonctionnel plutôt qu'une documentation exhaustive

Cela devrait être évident maintenant. Au lieu de spécifications et de planifications verbeuses, écrivez simplement quelques lignes de code qui fonctionnent. 

Testez-le. Obtenez des feedbacks dessus. Livrez-le.

Ensuite, faites-le à nouveau. 

Répétez.

Un exemple hautement pertinent de ce processus de répétition se trouve dans Forms on Fire. 

Ils ont créé un logiciel pour faciliter la collecte de données mobiles. Ils n'ont pas écrit toute leur entreprise avant de lancer ; ils ont écrit quelques lignes de code, l'ont testé et l'ont livré. 

Alors qu'ils prenaient de l'élan, ils ont accéléré leurs tests et leurs étapes itératives.

Et ils ont répété ce qui fonctionnait et jeté ce qui ne fonctionnait pas. Les résultats parlent d'eux-mêmes.

### Principe #3 : La collaboration avec le client plutôt que la négociation contractuelle

L'Agile promeut une boucle de feedback rapide pour obtenir les retours des clients et des parties prenantes. 

Qu'y a-t-il de mieux que de travailler en arrière à partir de ce que veulent les vrais utilisateurs et clients ?

J'ai un mentor en affaires qui a conseillé qu'au lieu de sur-analyser ce que veulent les clients à travers une planification sans fin, gardez cela simple. "Mitigez les distractions", a-t-il dit. 

J'ai écrit sur le principe KISS dans [freeCodeCamp](https://www.freecodecamp.org/news/keep-it-simple-stupid-how-to-use-the-kiss-principle-in-design/) et ce conseil est certainement vrai dans l'Agile : construisez quelque chose de petit et voyez si vos clients l'aiment.

Si c'est le cas, continuez. 

### Principe #4 : Répondre au changement plutôt que suivre un plan

Les boucles de feedback rapides engendrent des changements et des ajustements rapides. C'est ce qui rend l'Agile si formidable pour les équipes de développement. 

C'est pourquoi vous devriez l'adopter.

Les feuilles de route changent toujours, c'est une constante connue. En utilisant les méthodologies Agile, les équipes peuvent répondre au changement en écoutant les feedbacks des clients et en apportant les ajustements nécessaires.

Il arrive que répondre au changement signifie ajuster votre produit ou changer votre façon de penser sur les utilisateurs ou la concurrence. 

Un exemple classique que les étudiants en Agile peuvent examiner dans le domaine du e-commerce est la vente sur Amazon. Comment ajustez-vous rapidement votre stratégie face à la concurrence ? Une façon est de construire des communautés fermées ou d'essayer différentes stratégies de lancement de produits. 

Déployer des solutions tactiques et malléables est conseillé.

Il y a un merveilleux proverbe : "Nous ne pouvons pas changer la direction du vent. Nous pouvons seulement ajuster nos voiles."

Quand je pense à l'Agile, je pense à ce dicton. 

L'Agile, c'est apprendre, l'Agile, c'est enseigner. L'Agile, c'est la flexibilité.

Vous pouvez pratiquer l'Agile dans votre travail quotidien ou suivre des cours en ligne pour vous développer davantage.

Certaines personnes sont assez intelligentes pour prédire ce que leur client veut. Elles savent dans quelle direction le vent souffle. 

Mais pour nous, simples mortels, l'Agile est une méthodologie pour naviguer autour de nos déficiences dans la compréhension de ce que veulent les clients. 

C'est le système qui nous permet d'ajuster constamment nos voiles.