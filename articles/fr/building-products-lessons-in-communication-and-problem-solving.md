---
title: Ce que j'ai appris en construisant des produits – Leçons de communication et
  de résolution de problèmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T15:46:49.000Z'
originalURL: https://freecodecamp.org/news/building-products-lessons-in-communication-and-problem-solving
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/learning_to_build_products_header.png
tags:
- name: communication
  slug: communication
- name: Problem Solving
  slug: problem-solving
- name: product development
  slug: product-development
- name: Productivity
  slug: productivity
seo_title: Ce que j'ai appris en construisant des produits – Leçons de communication
  et de résolution de problèmes
seo_desc: "By Zaid Humayun\nI spent a year learning how to build products. Rather,\
  \ I spent that year learning just how hard it is to build good products. \nIt's\
  \ been a roller coaster ride so far and I want to share my learnings.\nI'm going\
  \ to highlight the most im..."
---

Par Zaid Humayun

J'ai passé un an à apprendre à construire des produits. Ou plutôt, j'ai passé cette année à apprendre à quel point il est difficile de construire de bons produits. 

Cela a été une montée en roller coaster jusqu'à présent et je veux partager mes apprentissages.

Je vais mettre en lumière les leçons les plus importantes que j'ai apprises en cours de route.


## À quoi s'attendre de cet article

Avant de commencer, je tiens à préciser que cet article de blog n'est pas aussi technique que la plupart des choses que vous lirez sur freeCodeCamp. 

Bien qu'explorer la technologie soit précieux, je crois qu'il est tout aussi bénéfique pour les programmeurs de regarder l'aspect commercial des choses. Cela est en partie parce que ce n'est pas quelque chose à quoi la plupart des programmeurs prêtent attention.

À mesure que la programmation devient de plus en plus populaire et commodifiée, il deviendra plus précieux pour les programmeurs de comprendre exactement comment ils ajoutent de la valeur à une entreprise.

Répondre au **pourquoi** de la résolution de problèmes est l'aspect commercial le plus crucial lors de la construction de solutions technologiques.


## Un peu de contexte

Je travaille dans une entreprise de fabrication de vêtements basée à Bangalore, en Inde. Oui, vous avez bien lu. Je travaille dans la technologie au sein d'une entreprise de fabrication de vêtements à Bangalore, en Inde.

Ce n'est pas le travail le plus glamour, mais il offre beaucoup d'opportunités pour expérimenter.

L'industrie du vêtement est l'une des industries les plus désorganisées en Inde. Pour les personnes travaillant dans le monde de la technologie, il est un peu difficile de saisir à quel point elle est désorganisée. 

Lorsque les personnes dans la technologie pensent à un problème, elles pensent à parcourir de grands ensembles de données pour en tirer des informations qui pourraient se transformer en fonctionnalités plus efficaces. 

Mais, que faites-vous lorsque les données sont encore écrites au crayon sur papier ? Comment accédez-vous même à ces informations ? 

Parfois, on a l'impression que le reste du monde a avancé à toute vitesse, laissant certaines industries loin derrière. Et souvent, on a l'impression que la roue de l'invention revient en tournant à nouveau.

## Comment les choses fonctionnent dans l'entreprise

Avant de pouvoir présenter les problèmes, je dois expliquer comment fonctionne une unité de fabrication de vêtements. 

Voici un aperçu extrêmement simplifié de la chaîne d'approvisionnement dans la fabrication de vêtements

![supply_chain_basic-1](https://www.freecodecamp.org/news/content/images/2021/02/supply_chain_basic-1.png)

Assez simple, n'est-ce pas ? C'est vraiment le cas ! Et comme dans toute autre industrie, le diable est dans les détails.

Plongeons un peu plus profondément. Pour faire court, examinons simplement la relation entre le moulin à textile et le fabricant de vêtements. 

Tout commence par une commande passée par l'acheteur auprès du fabricant de vêtements. L'acheteur indiquera au fabricant de vêtements qu'il nécessite un type spécifique de tissu pour ses vêtements. Cela s'appelle un style de tissu.

Maintenant, lorsque nous parlons du style de tissu, cela peut signifier beaucoup de choses différentes. Voici quelques-unes des variables qui composent le style du tissu.

![parts_of_style-1](https://www.freecodecamp.org/news/content/images/2021/02/parts_of_style-1.png)

Pour l'instant, pour garder les choses simples, concentrons-nous simplement sur la couleur du tissu.

Le fabricant de vêtements passera ensuite une commande de tissu auprès du moulin à textile. Une fois que le moulin à textile est prêt à expédier le tissu, la complexité commence.

Le problème est une question d'échelle. Lorsque vous avez plus de 30 fournisseurs de tissu, répartis dans tout un pays, il est difficile de suivre les expéditions de tissu que vous recevez.

## Comment nous pouvons définir le problème

Voici les problèmes clés :

* Suivre quand vous recevez l'expédition de tissu
* Suivre la quantité de tissu que vous avez reçue
* Suivre de quel fournisseur vous avez reçu le tissu
* Suivre à quel endroit vous avez reçu le tissu
* Si le tissu passe les contrôles d'inspection de qualité
* Si le tissu passe les tests de laboratoire indiqués par l'acheteur

Notre problème va se concentrer uniquement sur les trois points suivants :

* Quand avons-nous reçu une expédition de tissu d'un fournisseur ?
* Quelle quantité de tissu avons-nous reçue dans une expédition spécifique ?
* À quel endroit avons-nous reçu le tissu ?

La solution la plus évidente est les feuilles Excel. 

>*Leçon #1 : Dans les grandes organisations, Excel fonctionne comme une base de données distribuée.*

Excel fonctionne bien, pendant un certain temps, puis devient rapidement difficile à maintenir.

Pourquoi ? Commençons une entreprise hypothétique de fabrication de vêtements pour répondre à cette question.

### Phase 1

![simple_excel_sheet_fabric](https://www.freecodecamp.org/news/content/images/2021/02/simple_excel_sheet_fabric.png)

D'accord, nous venons de commencer et nous avons 2 fournisseurs, 3 usines et un siège social. C'est plutôt bien pour un début !

Disons aussi que nous avons 1 acheteur. Avoir un seul acheteur signifie que le nombre de différents styles de tissu que nous devons gérer est faible.

Au fur et à mesure que chaque usine reçoit du tissu, elles informent le siège social par e-mail de la quantité de tissu et du style de tissu qu'elles ont reçus. Ensuite, le siège social met ces données dans une feuille Excel.

Chaque usine reçoit du tissu une fois par jour, donc cela signifie que le siège social recevra 3 e-mails par jour. Pas trop mal ! 

Même si un fournisseur retarde une expédition, il est relativement facile de suivre car il n'y a que 2 fournisseurs.

### Phase 2

Les choses se passent bien, l'entreprise grandit et vous décidez de vous développer. Vous créez 5 usines supplémentaires. 

Vous augmentez également le nombre d'acheteurs avec lesquels vous travaillez, ce qui à son tour augmente le nombre de styles de tissu.

Vous voulez également augmenter votre chiffre d'affaires, donc 3 des usines reçoivent du tissu deux fois par jour : une fois le matin, une fois le soir.

![complicated_excel_sheet_fabric](https://www.freecodecamp.org/news/content/images/2021/02/complicated_excel_sheet_fabric.png)

Les choses viennent de devenir un peu plus réelles. 

Vous remarquerez que le visage de chaque fournisseur est maintenant invisible. Ce n'est pas une coïncidence. Oui, je l'ai fait pour gagner de la place, mais je l'ai aussi fait pour illustrer comment, à mesure que l'échelle augmente, vos relations personnelles avec les partenaires commerciaux passent au second plan. 

Il est tout simplement impossible de maintenir le même type de relation personnelle que vous aviez avec 2 fournisseurs, avec 6 fournisseurs et 8 usines en plus !

Vous pourriez vous demander pourquoi le point ci-dessus est pertinent. C'est parce que cela mène à la leçon suivante.

>Leçon #2 : Les relations commerciales sont construites presque entièrement sur la confiance, surtout en l'absence de technologie.

Examinons la leçon ci-dessus un peu. C'est important parce que le but de la plupart des systèmes technologiques est d'éliminer le besoin de confiance. Bien sûr, ce n'est pas entièrement possible.

>Avant de continuer, il y a une chose rapide que je dois mentionner. Lorsque les fournisseurs fournissent du tissu aux unités de fabrication, ils le fournissent généralement sous la forme d'un rouleau de tissu.

Construisons un scénario avec vous en tant que fabricant de vêtements. Vous avez un fournisseur qui vous fournit des rouleaux de tissu. 

Une fois, vous recevez 10 rouleaux de tissu et, sur la base d'un tuyau anonyme, vous décidez de mesurer la longueur de chaque rouleau de tissu par rapport à ce que le fournisseur vous dit qu'il est.

![trust_relationship](https://www.freecodecamp.org/news/content/images/2021/02/trust_relationship.png)

L'infographie ci-dessus vous montre à quoi cela ressemblerait. 

À votre grand dam, vous découvrez que le fournisseur vous trompe et que vous manquez de 36 m de tissu. Dans une industrie à faible marge comme la fabrication de vêtements, cela compte pour beaucoup.

De plus, cela n'était que pour 10 rouleaux de tissu. À mesure que votre entreprise grandit, vous allez commander plus de rouleaux de tissu à un fournisseur. Imaginez que vous aviez 100 rouleaux de tissu à passer au lieu de 10. 

Vérifier manuellement chaque rouleau de tissu n'est pas une opération qui peut être mise à l'échelle, et à mesure que vos opérations se développent, la confiance devient plus importante.

Maintenant, revenons à nos problèmes d'échelle. Nous avons un total de 6 fournisseurs, 8 usines et plus d'acheteurs – et donc plus de styles de tissu.

Avec 5 usines recevant du tissu une fois par jour et 3 usines recevant du tissu deux fois par jour, le siège social recevra `5*1 + 3*2 = 11 emails` par jour.

Les choses sont devenues plus difficiles non seulement parce que le siège social reçoit plus d'e-mails, mais aussi parce que les styles de tissu qu'ils reçoivent ont également augmenté. Cela ajoute au nombre de lignes dans une feuille Excel. 

Maintenant, lorsqu'un fournisseur retarde une expédition, les choses deviennent beaucoup plus difficiles à suivre parce que les usines reçoivent 11 expéditions par jour de 6 fournisseurs différents.

Mais, même maintenant, Excel n'est pas une mauvaise option du tout. Cependant, le département du tissu est sous une grande pression pour suivre la charge de travail, donc le siège social fait ce que toute bonne organisation ferait et ajoute quelques employés de plus. 

Ajouter deux employés était-ce une mauvaise idée ? Toutes les réponses sont subjectives.

Un technologue dirait : "Pourquoi ajouter deux employés de plus ? Vous devez simplifier le processus en ajoutant de l'automatisation !"

Un PDG répondrait : "Pourquoi ? Le coût de l'automatisation n'en vaut pas la peine. Il est plus simple d'ajouter deux employés et de garder notre processus le même."

>Leçon #3 : Tout ne vaut pas la peine d'être automatisé. C'est la leçon la plus difficile à accepter pour moi.

> [XKCD pertinent](https://xkcd.com/1205/)

### Phase 3

Le temps passe et les affaires continuent de prospérer. En tant que PDG capitaliste, vous voulez augmenter à nouveau l'échelle de l'entreprise !

Cette fois, vous augmentez le nombre d'usines à 14. Vous ajoutez également plus d'acheteurs au portefeuille, ce qui augmente le nombre de styles de tissu avec lesquels les usines doivent travailler. 6 usines reçoivent du tissu deux fois par jour et les 8 restantes reçoivent du tissu une fois par jour.

Vous travaillez également avec 20 fournisseurs maintenant en raison de tous les différents styles de tissu dont vous avez besoin.

![really_complicated_excel_sheet_fabric](https://www.freecodecamp.org/news/content/images/2021/02/really_complicated_excel_sheet_fabric.png)

Je n'ai pas pris la peine de nommer l'un des fournisseurs ou des usines dans l'image ci-dessus car cela serait trop d'effort. 

Mais, encore une fois, c'est pour illustrer que la relation personnelle que vous auriez pu avoir avec chacun des gestionnaires des usines se détériore. Vous ne pouvez tout simplement pas maintenir chacune de ces relations au même degré.

Maintenant, le siège social recevra `8*1 + 6*2 = 20` e-mails par jour ! Chaque e-mail contient également plus de données car nous avons augmenté le nombre de styles avec lesquels nous travaillons.

Maintenir une feuille Excel centrale manuelle devient de plus en plus difficile. Ajouter simplement plus d'employés à la tâche ne sera pas nécessairement utile car vous pourriez vous retrouver avec plusieurs copies d'une feuille Excel centralisée au siège social.

## Comment résoudre le problème

Maintenant, il existe plusieurs façons de résoudre ce problème. 

L'une pourrait être de demander à chacune des usines de maintenir leur propre feuille Excel quotidienne et de l'envoyer en pièce jointe par e-mail au siège social.

Cependant, cela implique à nouveau que quelqu'un copie et colle les données de chaque usine dans une feuille Excel centralisée. Rien de mal à cela, mais il existe probablement une solution plus efficace.

Une autre solution potentielle serait de demander à chacune des unités de maintenir une feuille Google individuelle et d'exécuter un script en utilisant [Google App Script](https://developers.google.com/apps-script) chaque jour comme un [cron job](https://en.wikipedia.org/wiki/Cron) et de récupérer les données.

![google_sheet_cron_job](https://www.freecodecamp.org/news/content/images/2021/02/google_sheet_cron_job.png)

Cependant, si vous voulez plus de données comme la longueur de chaque rouleau, vous n'avez pas de chance. Il n'y a aucun moyen de demander aux personnes travaillant dans les usines de saisir manuellement la longueur de chaque rouleau de tissu chaque jour. Parce que, comme nous l'avons dit plus tôt, vous pourriez potentiellement recevoir 150 rouleaux de tissu par jour.

### Notre solution

La solution que nous avons finalement choisie, dans mon entreprise, n'est pas surprenante : nous avons décidé d'utiliser des codes-barres.

Nous plaçons un code-barres sur chaque rouleau de tissu. Le code-barres correspond à la longueur d'un rouleau, au style de tissu et à l'acheteur pour lequel il est destiné.

Nous avons construit une petite application Android qui permet aux utilisateurs de scanner des codes-barres avec l'appareil photo de l'appareil, et à chaque scan, elle appelle une API indiquant que ce code-barres spécifique a été scanné à un endroit spécifique (localisé via GPS).

Scanner un rouleau de tissu nous permet de localiser le rouleau via GPS et la date et l'heure.

En additionnant tous les rouleaux de tissu scannés à un endroit, nous pouvons connaître la longueur totale de tissu reçue par une usine.

Le meilleur de tout, cela réduit la charge de travail pour les usines elles-mêmes. Leur seul travail maintenant est de scanner les rouleaux de tissu. Scanner un rouleau de tissu prend ~3 secondes, donc scanner 100 rouleaux de tissu prend ~5 minutes.

Voici un schéma de base de ce que nous avons construit : 

![fabtrak_architecture_deployment](https://www.freecodecamp.org/news/content/images/2021/02/fabtrak_architecture_deployment.png)

* Une application basée sur le web qui est utilisée pour générer les codes-barres
* Une application Android qui est utilisée pour scanner les codes-barres
* Une API avec laquelle communiquent à la fois l'application web et l'application Android. L'API communique à son tour avec la base de données MySQL.

L'ensemble est hébergé sur AWS et l'application Android est hébergée sur le Google Play Store.

La solution semble assez simple, mais elle ne l'est pas.

### Ce que nous avons appris en résolvant le problème

>Leçon #4 : Construire des choses pour les gens est difficile car il y a souvent un décalage entre les personnes qui construisent la chose et les personnes pour lesquelles la chose est construite.

Ce décalage est la raison pour laquelle c'est une excellente idée de construire un produit qui comble un besoin que vous avez longtemps souhaité voir exister.

L'une des premières erreurs que nous avons commises avec l'application Android était de donner trop d'options à nos utilisateurs
![initial_fabscan_sketch](https://www.freecodecamp.org/news/content/images/2021/02/initial_fabscan_sketch.png)

Le croquis ci-dessus montre à quoi ressemblait une version très précoce de notre application. Cliquer sur chacun de ces boutons vous emmenait à l'écran de la caméra. Cependant, chacun d'eux faisait un appel API différent et renvoyait donc un résultat différent. 

La raison d'inclure le bouton Entrer était que, si le code-barres devait être rayé et ne pouvait pas être capté par la caméra du téléphone, l'utilisateur pouvait alors entrer le code-barres à la place et cela compterait comme un scan.

Voici à quoi ressemble l'un de nos numéros de code-barres : `k29_%!s5qG`. Il n'y a aucune chance que quelqu'un s'assoie et entre cette séquence de caractères. 

La raison d'être du bouton Lire était que si quelqu'un voulait identifier de quel type de tissu était un rouleau spécifique, il pouvait scanner le code-barres en mode Lecture et cela renvoyait des informations sur ce rouleau de code-barres.

Les usines avaient déjà leur propre méthode de stockage des informations sur le rouleau, cependant. Elles les écrivaient simplement au crayon sur papier et les collaient sur une étiquette attachée au rouleau. 

Est-ce le système le plus avancé technologiquement ? Pas du tout ! Mais, est-ce que cela fonctionne ? Absolument ! Et nous aurions dû respecter le fait qu'elles avaient déjà leur propre façon de faire la même opération.

Le résultat final est que presque personne ne se donne la peine de cliquer sur l'un ou l'autre des boutons Lire ou Entrer.

Lors de la construction de choses, gardez les choses au strict minimum. Il n'y a aucune raison d'ajouter des fonctionnalités supplémentaires sauf si absolument nécessaire.

La deuxième erreur que nous avons commise était de ne pas connaître notre public.

Lorsque nous avons eu l'idée de construire une application web pour que les gens l'utilisent pour générer des codes-barres, cela semblait être une évidence.

Nous avons cependant rencontré un problème amusant.

Lorsque nous avons expliqué aux personnes travaillant dans les usines qu'elles devaient entrer l'adresse dans la barre d'adresse, nous avons obtenu des regards vides en réponse.

Vous voyez, avec le milieu privilégié dont la plupart d'entre nous viennent, nous avons tendance à oublier qu'il y a une grande majorité de la population qui ne sait pas comment interagir avec un navigateur web. Pourquoi ? Ils n'en ont jamais eu besoin. Ils interagissent avec Internet principalement via des applications pour smartphones.

Cela peut sembler un peu exagéré, mais j'ai vu les preuves de mes propres yeux. Ce n'est pas pour suggérer que les personnes qui ne savent pas utiliser un navigateur sont moins intelligentes, loin de là. Cela signifie simplement que nous devons communiquer les choses différemment.

Maintenant, ce sujet de communication m'amène à la dernière leçon que j'ai apprise. Probablement la leçon la plus dure et définitivement la plus perspicace.

> Leçon #5 : Tous les problèmes dans une organisation sont des problèmes de communication.

Revenez sur ce que nous avons couvert dans cet article. 

Le premier problème que nous avons découvert était celui des e-mails. Lorsque l'organisation est petite, moins d'e-mails sont échangés. À mesure qu'une organisation se développe, le nombre d'e-mails augmente et il devient plus difficile de suivre. Problème de communication.

Le deuxième problème que nous avons découvert était celui de la confiance entre le fournisseur et le fabricant. Le fournisseur a communiqué de fausses informations au fabricant. Le fabricant a dû passer un temps précieux à corriger ces fausses informations. Problème de communication.

Le troisième problème que nous avons découvert était comment expliquer aux personnes qui n'ont jamais utilisé un navigateur web, comment naviguer vers une page spécifique. Problème de communication.

Je sais que cela ressemble un peu à du pigeonnage où j'essaie de forcer chaque problème à être un problème de communication, mais au cœur de la plupart des problèmes se trouve juste cela : une mauvaise communication.

## Conclusion

J'ai passé sous silence les aspects plus techniques de la solution que nous avons construite. Cependant, je pense que ce n'est pas la partie intéressante. Ce qui est intéressant, c'est la manière dont nous avons tenté de résoudre les problèmes. 

Si vous pensez que les problèmes sur lesquels je travaille sont intéressants, jetez un coup d'œil à nos [offres d'emploi](https://www.id-flo.com/careers).

Si vous ne trouvez pas de rôle qui vous convient dans les offres, veuillez m'envoyer un e-mail à zaid@indian-designs.com.