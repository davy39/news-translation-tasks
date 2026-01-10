---
title: Que signifie "Shift Left" dans le développement logiciel ?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2024-04-15T22:25:08.000Z'
originalURL: https://freecodecamp.org/news/what-is-shift-left-in-software
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Shift-Left-.png
tags:
- name: software development
  slug: software-development
seo_title: Que signifie "Shift Left" dans le développement logiciel ?
seo_desc: "I once had a manager who, in a discussion about our project, mentioned\
  \ that we needed to try and shift our work left as much as we could. \nA few months\
  \ later in an interview, the interviewer asked me if I knew what \"shift left\"\
  \ meant.\nUnless there's ..."
---

J'ai déjà eu un manager qui, lors d'une discussion sur notre projet, a mentionné que nous devions essayer de **déplacer notre travail vers la gauche** autant que possible.

Quelques mois plus tard, lors d'un entretien, l'interviewer m'a demandé si je savais ce que signifiait "**shift left**".

Sauf s'il existe une danse logicielle secrète dont personne ne m'a parlé, je suis maintenant ici pour vous expliquer ce que signifie **shift left**.

## Que signifie "Shift Left" dans le logiciel ?

Déplacer vers la gauche est un terme technique signifiant essayer d'identifier les problèmes dès que possible dans le cycle de vie de votre projet logiciel.

Le "left" (gauche) signifie le début du projet, et c'est une phrase qui signifie simplement "essayons de détecter autant de nos problèmes, blocages et difficultés dès que possible".

## Le cycle de vie du développement logiciel

Imaginons que vous commencez un nouveau travail en tant qu'ingénieur logiciel dans une banque.

Votre cycle de vie du développement logiciel pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-110.png)
_Exemple de cycle de vie du développement logiciel_

1. Tout d'abord, les exigences sont fournies par vos chefs de produit.
2. Ensuite, l'analyse pour compléter ce travail est réalisée par vos analystes métiers.
3. Les designs sont créés pour l'apparence de l'interface utilisateur.
4. Les développeurs font leur propre planification maintenant.
5. Ensuite, les développeurs commencent le travail !
6. Pièce par pièce, la fonctionnalité est construite et les testeurs peuvent tester.
7. Le projet passe par les environnements sur son chemin vers la production. Il passe par dev. Il passe par test. Il atteint la pré-production et est publié en production.
8. Le projet entre dans une période de maintenance. Vous vérifiez les problèmes dans vos logs, vous corrigez les bugs qui surviennent.

Quelques exemples de **déplacement de notre travail vers la gauche** dans ce cycle seraient les suivants :

* Vérification des exigences par l'équipe technique pour s'assurer que tout ce qui est demandé peut être réalisé dans le délai prévu.
* Les architectes s'impliquent tôt dans la phase de planification et essaient de créer des documents techniques et de repérer les cas particuliers ou les problèmes que les développeurs pourraient rencontrer.
* Peut-être que les designers créent un prototype de base à partir des designs pour illustrer exactement ce qui est attendu.
* Lorsque les développeurs planifient, ils ont suffisamment de temps pour faire une revue approfondie. Ce n'est pas une réunion courte de 15 minutes. Ils sont censés produire des diagrammes de classe, des améliorations architecturales de code, des estimations précises, ils planifient leur suite de tests unitaires et s'assurent que la documentation pertinente est mise à jour.
* Les testeurs effectuent des tests manuels ainsi que des tests automatisés. Ils utilisent le logiciel comme le ferait un vrai utilisateur !

### Quand trouvons-nous généralement des problèmes ?

Réfléchissons aux moments où nous pourrions généralement détecter un bug dans un projet. Essayez de penser à quand vous préféreriez détecter un problème.

* À la fin du projet, lorsque tout le code a été écrit et qu'il a déjà été publié en production depuis 2 semaines
* Lorsque vous le publiez dans l'environnement de pré-production
* Par le testeur sur l'environnement de _test_
* Alors que les développeurs sont en train de coder
* Alors que les développeurs font leur planification
* Lorsque les designs sont en cours de création
* Lorsque les architectes créent leurs diagrammes architecturaux
* Alors que les chefs de produit spécifient les exigences

Le moment dans cette chronologie où vous pouvez répondre le plus facilement au problème, perdre un minimum de temps et le rectifier rapidement est **dès le début**. Et vous pouvez aider votre équipe à y parvenir en déplaçant votre travail vers la gauche.

## Il existe de nombreuses façons de détecter les erreurs

**Shift left** est une phrase, mais elle est basée sur une méthodologie entière qui nous aide à essayer de détecter les problèmes tôt pour des cycles d'itération rapides afin de livrer des logiciels.

Alors, quelles sont les autres étapes que nous pourrions essayer pour nous aider à **déplacer notre travail vers la gauche** ?

Au-delà de la simple planification, que pouvons-nous faire d'autre ?

* Vous pouvez analyser votre base de code et détecter les fautes de frappe, les erreurs courantes et les mauvaises conceptions.
* Vous pouvez introduire la vérification de type dans les parties de votre base de code que vous pensez en bénéficier.
* Vous pouvez augmenter votre couverture de tests unitaires.
* Vous pouvez augmenter votre couverture de tests d'intégration.
* Vous pouvez introduire des QA de code dans votre équipe.
* Vous pouvez introduire des logs et des alarmes métriques pour les déploiements.

Rappelez-vous simplement, plus vous avancez dans le flux de votre projet, plus il peut être difficile de se remettre d'une erreur. Détectez les problèmes dès que possible ! 
ud83d
de09

Car si votre équipe ne trouve pas le bug, vous pouvez toujours parier qu'un utilisateur le fera.

## **Conclusion**

J'espère que cela a été utile et a expliqué ce que signifie "shift left". Essayez d'incorporer cette façon de penser dans votre cycle de vie de développement et voyez ce qui se passe.

Je tweete mes articles [ici](https://twitter.com/kealanparr) si vous souhaitez en lire plus.