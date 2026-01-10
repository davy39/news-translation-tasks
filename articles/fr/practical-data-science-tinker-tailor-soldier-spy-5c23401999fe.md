---
title: 'Science des données pratique : bricoler, adapter, soldat, espion'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T20:39:33.000Z'
originalURL: https://freecodecamp.org/news/practical-data-science-tinker-tailor-soldier-spy-5c23401999fe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UITRP8PyvgZFeUdu.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Science des données pratique : bricoler, adapter, soldat, espion'
seo_desc: 'By Michelle Jones

  I came to data science and statistics as a failure. After finishing my master’s
  degree in psychology I applied for about 30 psychology-related jobs without success.
  I didn’t even make it to the interview stage. I then saw a job adve...'
---

Par Michelle Jones

Je suis venue à la science des données et aux statistiques en tant qu'échec. Après avoir terminé mon master en psychologie, j'ai postulé à environ 30 emplois liés à la psychologie sans succès. Je n'ai même pas atteint l'étape de l'entretien. J'ai ensuite vu une annonce pour un poste de chargé de recherche, et cela a marqué le début d'une carrière de 21 ans en tant que statisticienne appliquée dans le gouvernement. En cours de route, j'ai complété une qualification postuniversitaire en statistiques.

**Mon historique de codage**

Mon premier code était en SPSS PC version 5.0 pour ma thèse de master. En 1995, lorsque j'écrivais ma thèse, les interfaces utilisateur pour les logiciels statistiques étaient très simples. J'ai utilisé le système de menu pour créer le premier ensemble de code dont j'avais besoin. Ensuite, j'ai copié-collé ce code pour la prochaine série d'analyses sur d'autres variables, en ne changeant que les parties relatives aux noms des variables.

![Image](https://cdn-media-1.freecodecamp.org/images/g8klZsrmqlbBjDEAGQPpzpfl6WiNVNO2estK)
_Heureusement, ce n'était pas des cartes perforées. [Crédit image](https://en.wikipedia.org/wiki/Fortran#/media/File:FortranCardPROJ039.agr.jpg" rel="noopener" target="_blank" title=")._

Travailler directement avec le code m'a permis de comprendre comment le code fonctionnait : commandes, options de commande et marqueurs de fin de ligne. Cela m'a fait réfléchir sérieusement aux options que je voulais dans l'analyse parce que je les tapais. C'est ainsi que j'ai été initiée au codage. C'était aussi plus rapide que d'utiliser le système de menu.

À peu près à la même époque, j'ai eu une introduction en douceur à SAS, version 6, pour aider un professeur avec son analyse de données. Le code avait été écrit, et je ne faisais que le modifier pour mettre à jour l'analyse. Cette version de SAS n'avait qu'un éditeur de programme, et j'ai lu de nombreux guides utilisateur SAS en version papier. Ce fut mon introduction au codage sans système de menu, et j'ai fait beaucoup d'erreurs au début. Ma compétence spéciale était de ne pas fermer les guillemets pour les chaînes de caractères.

De là, j'ai passé les 21 années suivantes à utiliser des logiciels statistiques dans divers rôles au sein du gouvernement. J'ai utilisé SPSS, SAS, R et Stata. J'ai appris VBA, que j'ai principalement utilisé pour Excel, et aussi pour Access. Pour mon doctorat, qui est mon objectif actuel, j'utilise R, VBA, Java et Latex.

**Bricoler**

Le rôle principal d'un scientifique des données est de bricoler. Environ 90 % de mon temps a été consacré à la transformation des données dans un format adapté à l'analyse. Parfois, cela peut être une tâche simple mais chronophage, par exemple, faire correspondre des données entre plusieurs extraits de data warehouse parce qu'une quatrième forme normale n'est pas utile pour l'analyse des données. Parfois, les transformations peuvent être simples et rapides. Un exemple est le changement de données du format large au format long, ou vice versa, en raison des hypothèses de structure de données dans le logiciel.

Un bricolage plus compliqué inclut le recodage de données détaillées dans un format moins détaillé utile à l'analyse. Par exemple, il existe de nombreuses façons différentes dont les gens répondent aux options de réponse "Autre" dans les enquêtes, mais toutes doivent être codées pour l'analyse.

![Image](https://cdn-media-1.freecodecamp.org/images/De8REfoHLkzHG7MMwwtj9dyBs-xOc75An1O0)
_Parfois, il est important de comparer des pommes et des oranges, et parfois nous voulons simplement en savoir plus sur les fruits. [Crédit image](https://www.flickr.com/photos/microassist/7268711202" rel="noopener" target="_blank" title=")._

**Adapter**

La plus grande influence sur la façon dont vous coderez dans une organisation est la culture. La culture contrôle quel logiciel est utilisé, quel logiciel peut être introduit et comment votre code interagira avec les autres membres du personnel. Parfois, vos collègues voudront des rapports. Parfois, vos collègues sont des experts en la matière et vous aideront à recoder. Parfois, vous devez produire une solution de codage pour que vos collègues l'utilisent. Vous pouvez être l'un des nombreux membres du personnel qui utilise un logiciel pour effectuer des analyses.

Vous devez adapter vos solutions pour répondre à ces besoins. L'analyse des données pour les rapports est votre tâche standard de scientifique des données et peut être effectuée avec n'importe quel logiciel statistique. Vous êtes la seule personne à utiliser le logiciel, et les complications de codage ne sont visibles que par vous. Votre restriction est le logiciel disponible à utiliser.

Travailler avec des collègues pour adapter les données est également facile à faire. Un exemple est le recodage des réponses ouvertes en catégories agrégées pour l'analyse. J'ai tendance à utiliser Excel pour cela, car la plupart des organisations disposent de ce logiciel et tous les membres du personnel peuvent y accéder, mais tout logiciel capable de gérer des lignes de données est utile. Après avoir discuté du problème et de la solution avec les collègues, je place les données dans une seule colonne dans Excel, avec une ligne de titre, et je les transmets.

Parfois, le besoin d'adapter les données n'est pas évident jusqu'à ce qu'une première analyse soit effectuée. Une variable peut être collectée en utilisant un nombre relativement faible de sous-catégories. Par exemple, l'état de la relation, et vous trouvez que les résultats pour une sous-catégorie seront dans la marge d'erreur. Vous pouvez souhaiter recoder vos données de sorte que cette sous-catégorie soit fusionnée avec une autre sous-catégorie logique. Cette nouvelle sous-catégorie combinée sera renommée en quelque chose de plus approprié, reflétant le nouveau contenu.

Adapter le code pour que les collègues l'utilisent peut être facile. Si vos collègues utilisent le même logiciel statistique, fournir du code pour ce logiciel avec des commentaires et des instructions peut être tout ce qui est requis. Fréquemment, le personnel n'a pas de logiciel statistique et nécessite simplement une solution dans un logiciel qu'il utilise. Ce logiciel est susceptible d'être Excel. Votre tâche peut aller de la vérification des formules à la fourniture d'une macro VBA dans un classeur Excel avec macros activées.

**Soldat**

La plupart des membres du personnel ne comprennent pas ce que vous faites. Ils voient ce que vous produisez, mais ils n'ont aucune connaissance et aucun intérêt pour la façon dont vous le faites. Comme je l'ai dit plus tôt, environ 90 % de votre rôle consiste en un travail de base, car les données arrivent rarement dans un format adapté à l'analyse. Si c'est le cas, un autre scientifique des données a fait le travail de base pour vous.

Un autre travail de base consiste à essayer de faire fonctionner le code et, peut-être, à mettre en œuvre une solution différente. Par exemple, j'ai une fois fait l'erreur d'essayer d'utiliser une boucle for-next dans R sur quelques millions d'enregistrements. C'était avant que je ne découvre que R utilise la vectorisation, ce qui a rendu la solution une ligne de code.

![Image](https://cdn-media-1.freecodecamp.org/images/AYhLKyuSxS27hish2bD4UhlqPhYg-wEF7b3C)
_La fée des données qui fait tout le travail difficile pour moi. [Crédit image](https://pixabay.com/en/angel-feathers-female-magic-wand-1298818/" rel="noopener" target="_blank" title=")._

**Espion**

Assurez-vous de savoir ce que votre collègue client veut avant de commencer quoi que ce soit, surtout quelque chose qui prendra beaucoup de temps. Les gens peuvent être non spécifiques, par exemple, en disant simplement qu'ils ont besoin d'un rapport.

Vous utilisez les astuces d'un espion. Comment le rapport sera-t-il utilisé ? Ont-ils besoin d'analyses détaillées ou simplement de haut niveau ? Par exemple, analysez-vous par sexe et âge séparément, mais pas par sexe et âge combinés ? Les gens veulent-ils une ventilation des données ? Utilisez un tableau. Les gens veulent-ils une image générale ? Utilisez un graphique. Si le rapport est long, sur quoi chaque chapitre doit-il se concentrer ? Quelles analyses sont les mieux adaptées au rapport ? Quels types de conclusions le collègue veut-il mettre en avant ?

**Conseils**

Enregistrez les ensembles de données intermédiaires, ne les écrasez pas. Si je lis à partir d'un autre type de fichier, par exemple, .csv, j'enregistre toujours le nouvel ensemble de données importé. Je fais mes manipulations de données sur cet ensemble de données mais j'enregistre dans un ensemble de données différent. De cette façon, lorsque les manipulations se passent mal (et elles le feront), vous n'avez pas besoin de réimporter les données depuis le début. Si quelque chose est étrange dans les résultats de l'analyse, par exemple, il y a une catégorie qui est vide, vous pouvez voir si le problème vient des données originales ou de quelque chose que vous avez fait.

N'oubliez pas de commenter votre code et de coder pour la clarté et pas toujours pour l'efficacité. Plusieurs fois, j'ai dû revenir à un code écrit 6 mois, 1 an, 2 ans auparavant et comprendre ce que j'avais fait et pourquoi je l'avais fait de cette manière.

Lorsque je traite de nombreuses lignes de code, j'utilise des blocs de commentaires pour sectionner le code. Cela est utile lorsque vous devez exécuter uniquement une partie du code à nouveau et que vous essayez de trouver le code que vous devez réexécuter.

Lorsque je travaille avec de grandes quantités de code utilisées pour écrire des chapitres dans un rapport, je sépare les analyses de chaque chapitre dans différents fichiers de code. Chaque fichier de code porte le numéro de chapitre pertinent dans le nom de fichier.

Supposez que personne ne révisera votre travail. Avant l'analyse, vérifiez les données pour vous assurer qu'elles sont raisonnables. J'utilise des tableaux de fréquence pour cela. Ce sont un moyen rapide de voir s'il y a des catégories inattendues ou des catégories qui contiennent trop peu de données pour être rapportées avec précision.

**Enfin**

En tant que scientifique des données, vous êtes l'expert en logiciel. Vous pouvez conseiller sur le logiciel à utiliser, en fonction des besoins et des fonds de l'organisation. Vous devrez peut-être effectuer, ou aider à, la formation formelle du personnel. Vous êtes susceptible d'être la personne appelée et contactée par e-mail lorsque les gens ont des problèmes avec le logiciel. Vous aurez beaucoup d'interactions avec le département ICT.

**Quelques exemples de mon travail**

Chapitre quatre de [ce rapport](http://www.police.govt.nz/about-us/publication/pursuits-the-case-for-change) sur les poursuites policières. J'ai utilisé SAS.

Document de travail sur [l'écart de rémunération entre les sexes](http://www.ssc.govt.nz/wp15) dans la fonction publique néo-zélandaise, l'une de mes publications les plus citées. Les données ont été analysées à l'aide de SPSS.

Mon seul article [publié](http://onlinelibrary.wiley.com/doi/10.1111/nbu.12075/abstract) (derrière un paywall), et cela a utilisé les données d'autres personnes. J'ai seulement utilisé Excel.

Un article publié (non derrière un paywall) où je me suis [amusée avec des graphiques](https://www.sciencedirect.com/science/article/pii/S0273230016302276?via%3Dihub#fig1), ceux-ci ont été réalisés en R. Je les ai esquissés sur papier avant de les coder.

Cette [étude et rapport](http://www.foodstandards.gov.au/publications/Pages/consumerlabelsurvey2015.aspx) a pris plus de 2 ans. La plupart de l'analyse a été réalisée dans Stata, complétée par R pour les analyses d'arbres de décision. Les graphiques ont été produits dans Excel, en utilisant les résultats de Stata.