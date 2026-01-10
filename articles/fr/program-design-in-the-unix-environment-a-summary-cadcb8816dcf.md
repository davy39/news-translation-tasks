---
title: 'Conception de programmes dans l''environnement Unix : un résumé d''article
  académique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-28T20:29:12.000Z'
originalURL: https://freecodecamp.org/news/program-design-in-the-unix-environment-a-summary-cadcb8816dcf
coverImage: https://cdn-media-1.freecodecamp.org/images/0*O-H_d2lDRBmnCgFG.jpg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: summary
  slug: summary
- name: 'tech '
  slug: tech
- name: unix
  slug: unix
seo_title: 'Conception de programmes dans l''environnement Unix : un résumé d''article
  académique'
seo_desc: 'By Shubheksha Jalan

  Today, let’s take a look at “Program Design in the Unix Environment” published in
  1983 by Pike and Kernighan.

  The paper opens by listing why Unix has been successful, and then comments on the
  Unix philosophy and its benefits. It d...'
---

Par Shubheksha Jalan

Aujourd'hui, examinons « [Program Design in the Unix Environment](http://harmful.cat-v.org/cat-v/unix_prog_design.pdf) » publié en 1983 par Pike et Kernighan.

L'article commence par énumérer les raisons du succès d'Unix, puis commente la [philosophie Unix](https://en.wikipedia.org/wiki/Unix_philosophy) et ses avantages. Il le fait en examinant des exemples où les programmes se sont éloignés de la philosophie Unix et en discutant des compromis résultants.

Les raisons du succès d'Unix :

1. Portabilité : le noyau et les applications étaient écrits en C, ils pouvaient donc être transférés d'un système à l'autre sans être réécrits dans le langage d'assemblage spécifique à ce système.
2. Le même système d'exploitation fonctionnait sur différents matériels, les utilisateurs étaient donc déjà familiers et n'avaient pas à réapprendre lors de la sortie de nouveaux matériels.
3. Les fournisseurs pouvaient livrer le même logiciel avec chaque machine malgré les changements de matériel.
4. Le système n'était pas trop grand et était facile à modifier puisque tout était écrit en C.
5. Il fournissait une nouvelle philosophie basée sur l'utilisation d'outils polyvalents. Ils faisaient une chose bien et pouvaient être combinés pour accomplir une tâche particulière, au lieu de créer des outils monolithiques géants qui ne servaient qu'un seul but.

L'article soutient que l'utilisation et la conception des outils sont étroitement liées, et la manière dont ils s'emboîtent est le sujet principal de cet essai.

L'article plonge ensuite dans `cat` (l'utilitaire en ligne de commande Unix pour concaténer et imprimer des fichiers). Il copie son entrée vers sa sortie. L'entrée est généralement une séquence d'un ou plusieurs fichiers ou l'entrée standard. La sortie est un fichier ou la sortie standard.

Le but principal de `cat` était d'agir comme un utilitaire pour concaténer des fichiers. Il peut être combiné avec l'opérateur pipe (`|`) pour améliorer et étendre davantage son utilité par la redirection de sortie.

D'autres systèmes, en revanche, tentent de regrouper un ensemble de fonctionnalités liées dans une seule commande, ce qui va à l'encontre de la philosophie Unix. Cela crée également un verrouillage de fonctionnalités qui pourraient être utiles à d'autres programmes.

Avantages de l'approche Unix :

1. Le shell et les programmes qu'il peut invoquer fournissent un accès uniforme aux fonctionnalités du système. Exemple : les arguments de nom de fichier sont développés par le shell de manière similaire pour chaque commande. Grâce aux pipes, nous n'avons pas besoin que chaque commande traite le pré- et post-traitement de l'entrée.
2. La croissance est facile lorsque les fonctions sont bien séparées.

Exemple : l'opérateur `(backtic)` a été ajouté pour convertir la sortie d'un programme en entrée d'un autre sans nécessiter de modifications dans d'autres programmes, car il est interprété par le shell. Tous les programmes que le shell invoque acquièrent automatiquement cette fonctionnalité. Si chaque programme nécessitant cette fonctionnalité l'interprétait, il serait très difficile d'imposer l'uniformité et de mener des expérimentations supplémentaires, car chaque nouvelle idée affecterait tous les programmes souhaitant l'utiliser.

Cependant, dans les versions futures de `cat`, de nombreuses nouvelles options ont été introduites (comme l'impression des numéros de ligne et des caractères non imprimables).

Les auteurs soutiennent que, au lieu d'ajouter ces options à `cat` lui-même, soit des programmes existants auraient dû être utilisés, soit de nouveaux programmes auraient dû être créés. Par exemple, la fonctionnalité de numérotation des lignes aurait pu être fournie en utilisant `pr`. Cependant, il n'y avait aucun programme permettant d'imprimer des caractères non imprimables, ce qui justifiait la création d'un nouveau.

> Une telle modification confond ce que `cat` est censé faire — concaténer des fichiers — avec ce qu'il fait dans un cas spécial courant — afficher un fichier sur le terminal. Un programme UNIX devrait faire une chose bien, et laisser les tâches sans rapport à d'autres programmes. Le travail de `cat` est de collecter les données dans les fichiers. Les programmes qui collectent des données ne devraient pas changer les données ; `cat` ne devrait donc pas transformer son entrée.

Chaque fois que nous divisons quelque chose en plusieurs programmes, nous sacrifions une certaine efficacité. Mais puisque `cat` est généralement utilisé sans aucune option, il est logique que les cas les plus courants soient les plus efficaces.

> Les programmes séparés ne sont pas toujours meilleurs que des options plus larges ; ce qui est mieux dépend du problème. Chaque fois que l'on a besoin d'un moyen pour effectuer une nouvelle fonction, on est confronté au choix d'ajouter une nouvelle option ou d'écrire un nouveau programme (en supposant qu'aucun des outils programmables ne fera le travail de manière pratique). Le principe directeur pour faire ce choix devrait être que chaque programme fait une chose. Les options sont ajoutées de manière appropriée à un programme qui a déjà la bonne fonctionnalité. Si un tel programme n'existe pas, alors un nouveau programme est nécessaire. Dans ce cas, les critères habituels de conception de programmes doivent être utilisés : le programme doit être aussi général que possible, son comportement par défaut doit correspondre à l'utilisation la plus courante, et il doit coopérer avec d'autres programmes.

Considérons un autre problème : gérer les lignes de terminal rapides. Comment gérer la sortie de `cat` qui défile hors du haut de l'écran ?

Il y a deux approches :

1. Informez chaque commande des propriétés du terminal pour qu'elle fasse la bonne chose.
2. Écrivez une commande qui gère uniquement les terminaux sans modifier d'autres programmes.

Considérons des exemples des deux approches : `lsc` et `ls` qui imprime la liste des fichiers dans un répertoire.

`lsc` varie sa sortie en fonction de l'entrée. Il affiche la liste de manière colonnaire à travers l'écran pour que la sortie s'adapte si elle est dirigée vers le terminal. `ls` affiche tout dans une seule colonne.

> En conservant la sortie en une seule colonne vers les fichiers ou les pipes, `lsc` assure la compatibilité avec des programmes comme `grep` ou `wc` qui s'attendent à ce que les choses soient imprimées une par ligne. Cet ajustement ad-hoc du format de sortie en fonction de la destination n'est pas seulement désagréable, il est unique — aucune commande UNIX standard n'a cette propriété.

Les auteurs soutiennent que la fonctionnalité de colonisation est utile en général et ne devrait pas être enfermée uniquement dans `lsc`, la rendant inaccessible aux autres programmes. Ils prônent un programme différent dont le travail principal est la colonisation.

> Un raisonnement similaire suggère une solution pour le problème général des données qui défilent hors des écrans (colonisés ou non) : un programme séparé pour prendre n'importe quelle entrée et l'imprimer écran par écran. De tels programmes sont désormais largement disponibles, sous des noms comme pg et more. Cette solution n'affecte aucun autre programme, mais peut être utilisée avec tous. Comme d'habitude, une fois que la fonctionnalité de base est correcte, le programme peut être amélioré avec des options...

Sur la base de l'exemple précédent, les auteurs parlent également de différents cas où certaines fonctionnalités sont enfermées dans un programme spécifique (comme l'historique des entrées dans le terminal) qui seraient mieux placées comme un service central. Tous les programmes interactifs pourraient en bénéficier.

Ils concluent en expliquant que l'augmentation des commandes existantes avec des fonctionnalités/options n'est pas souhaitable dans Unix, cela va à l'encontre de sa philosophie de base : faire en sorte qu'un programme fasse une chose bien. Plusieurs de ces programmes peuvent être composés pour accomplir une tâche plus complexe.

> La clé de la résolution de problèmes sur le système UNIX est d'identifier les bonnes opérations primitives et de les placer au bon endroit. Les programmes UNIX tendent à résoudre des problèmes généraux plutôt que des cas particuliers. Dans un sens très large, les programmes sont orthogonaux, couvrant l'espace des tâches à accomplir (bien qu'avec une certaine quantité de chevauchement pour des raisons d'histoire, de commodité ou d'efficacité). Les fonctions sont placées là où elles feront le plus de bien : il ne devrait pas y avoir de paginateur dans chaque programme qui produit une sortie, pas plus qu'il ne devrait y avoir de correspondance de motifs de noms de fichiers dans chaque programme qui utilise des noms de fichiers.

> Une chose que UNIX n'a pas besoin, c'est de plus de fonctionnalités. Il est réussi en partie parce qu'il a un petit nombre de bonnes idées qui fonctionnent bien ensemble. Ajouter simplement des fonctionnalités ne rend pas les choses plus faciles pour les utilisateurs — cela rend simplement le manuel plus épais. La bonne solution au bon endroit est toujours plus efficace que le bricolage aléatoire.