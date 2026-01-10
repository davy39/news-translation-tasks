---
title: Comment rédiger une documentation QA qui fonctionnera réellement
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2024-06-17T18:29:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-qa-documentation-that-will-actually-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/How-to-Write-QA-Documentation-That-Will-Actually-Work.jpg
tags:
- name: documentation
  slug: documentation
- name: Quality Assurance
  slug: quality-assurance
seo_title: Comment rédiger une documentation QA qui fonctionnera réellement
seo_desc: "Imagine developing a complex software product without taking any action\
  \ to protect against errors. Human error and unexpected code combinations can cause\
  \ a wide range of defects. This is where quality assurance (QA) documentation comes\
  \ in. \nUsually, ..."
---

Imaginez développer un produit logiciel complexe sans prendre aucune mesure pour se protéger contre les erreurs. L'erreur humaine et les combinaisons de code inattendues peuvent provoquer une large gamme de défauts. C'est là que la documentation d'assurance qualité (QA) intervient. 

Généralement, un testeur QA crée un rapport après avoir découvert un bug. L'étape suivante est qu'ils envoient un rapport au gestionnaire de bugs. Basiquement, un gestionnaire de bugs est un développeur qui corrige un bug selon le rapport détaillé. Le gestionnaire de bugs assure un processus QA propre et efficace et facilite une conversation claire entre les correcteurs et les testeurs. 

Mais vous vous demandez peut-être – pourquoi avons-nous besoin de documentation QA ?

Les tests QA sont essentiels dans les produits IT aujourd'hui. Les délais serrés, les compétences uniques au sein de l'organisation et la demande de développer des produits soulignent la nécessité d'une méthodologie structurée. La documentation QA guide les testeurs à travers des niveaux de clarté et une couverture globale. 

J'ai écrit cet article pour faciliter un peu votre vie. Alors le voici, votre guide ultime sur la façon d'écrire une documentation QA logicielle qui fonctionnera.

### Voici ce que nous allons couvrir :

* [Établir un plan de test et un rapport de progression des tests](#heading-etablir-un-plan-de-test-et-un-rapport-de-progression-des-tests)
* [Créer des cas de test](#heading-creer-des-cas-de-test)
* [Rapports de défauts](#heading-rapports-de-defauts)
* [Conseils utiles pour la rédaction de rapports de défauts](#heading-conseils-utiles-pour-la-redaction-de-rapports-de-defauts)
* [Soumettre un rapport de défaut](#heading-soumettre-un-rapport-de-defaut)
* [Conclusion](#heading-conclusion)

## Établir un plan de test et un rapport de progression des tests

Développer un excellent logiciel nécessite une approche approfondie et documentée des tests. Tout commence dans la phase de développement avec un plan de vérification complet servant de modèle pour l'ensemble du processus QA. Il décrit les exigences générales, définit la route suivie, identifie les actifs nécessaires et établit un calendrier simple pour atteindre les objectifs.

### Élaborer une feuille de route avant de commencer

Avant de commencer à mettre en œuvre votre plan de test, prenez le temps de réfléchir à la situation générale. Posez-vous la question :

_Quel problème ce logiciel résout-il ?_ Dès que vous comprenez le but principal du logiciel, vous serez en mesure de gérer le processus de vérification et d'identifier les fonctionnalités qui sont les plus importantes pour vos objectifs. 

Je vous promets que une fois que vous verrez que vous pouvez faire cela, vous prioriserez rapidement vos efforts. Ils sont principalement basés sur l'importance de la fonctionnalité et son impact sur l'utilisateur.

### Créer un plan

Le plan de test est la partie centrale de la technique QA. Le plan de test doit contenir les éléments clés suivants :

* **Test imaginaire** : Identifiez clairement l'impact attendu de la méthode de paiement. Confirmera-t-il que la fonctionnalité principale fonctionne sans problème, ou vous alertera-t-il sur les lacunes de capacité ?
* **Méthode de test** : Décrivez comment le test sera effectué. Ferez-vous des tests ciblés, des tests inutiles, ou un mélange des deux ?
* **Allocation des ressources** : Identifiez l'équipement et la technologie nécessaires pour effectuer un contrôle complet. Quel cadre de contrôle utiliserez-vous ? Des configurations matérielles ou logicielles spécifiques sont-elles requises pour un contrôle approprié ?
* **Calendrier et dates restantes** : Établissez un calendrier réaliste pour l'essai. Fixez des dates limites claires pour garder le projet sur la bonne voie.

### Comprendre le 'pourquoi' et le 'comment'

Une feuille de route bien développée garantira que les problèmes clés sont abordés tout au long de l'approche d'amélioration :

* **Exigences d'acceptation** : Des critères de réussite/échec clairs doivent être définis pour tous les cas de contrôle. Ainsi, les critères permettent au client de comprendre que le produit est de haute qualité et prêt pour l'utilisateur final.
* **Gestion des ressources** : Identifiez les actifs nécessaires pour les tests. Cela inclut les machines préférées, les copies de logiciels sous diverses formes, l'expertise requise, et plus encore.
* **Dynamique d'équipe** : Assurez-vous que des rôles et des tâches simples sont définis au sein de l'équipe de test. Qui est responsable de cas de test particuliers ? Qui documente les bugs et qui parle aux développeurs ?
* **Gestion du temps** : Je conseille de fixer des temps de vérification réalistes, en tenant compte des délais du projet et de la disponibilité de l'aide utile.

Le rapport de progression des tests est une autre partie de la documentation QA, similaire au plan de test, mais avec des données supplémentaires sur la progression actuelle. Ce document vous permet, à vous et à votre équipe de développement, de surveiller la progression du projet et d'identifier tout problème organisationnel.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/test-plan-and-progress-report-1.png)
_Un plan de test et un rapport de progression_

## Créer des cas de test

Considérez chaque cas de test comme une recette détaillée pour trouver des défauts potentiels dans la fonctionnalité d'un programme logiciel. En suivant ces "recettes" et en évaluant les résultats attendus et réels, les défauts peuvent être identifiés et traités avec précision avant qu'une action préventive ne soit prise. 

Chaque cas de test agit comme une unité indépendante, décrivant les étapes nécessaires pour évaluer un élément particulier d'un programme logiciel. 

Voici une ventilation des éléments clés qui constituent un cas de test bien défini. Voici mon guide étape par étape pour créer des cas de test :

* **ID** : Il s'agit d'un champ d'identifiant pour aider à distinguer les cas de test et à les suivre facilement.
* **Priorité** : Cela indique la gravité du cas de test en fonction de la fonctionnalité du programme et de son impact sur la performance globale normale de l'application logicielle connue.
* **Exigences de test** : Il s'agit des exigences pour tester le logiciel avec succès, cela peut inclure des documents de référence également.
* **Module logiciel** : Cela montre la fonctionnalité en cours de test. Il fait également référence au document de spécifications des exigences logicielles (SRS) expliquant en détail la fonctionnalité du logiciel.
* **Contexte de test** : Cela détaille le plan de test pour clarifier comment les tests quotidiens seront effectués. Il identifie également les données de test requises pour une étude de cas réussie et inclut des informations statistiques uniques et importantes.
* **Sortie attendue** : Cela décrit la sortie attendue à afficher si le test est réussi.
* **Sortie réelle** : Cela indique le résultat réel en cas d'échec et montre au développeur les erreurs dans le module d'application du programme logiciel.
* **Commentaire** : Il s'agit d'une section facultative où le testeur peut donner une description des observations ou ajouter des enregistrements supplémentaires.

Tous les QA incluent généralement les éléments ci-dessus, mais peuvent également être conçus spécifiquement pour la tâche sélectionnée par le groupe QA. De plus, chaque cas de contrôle suit un cycle de vie qui définit les phases de création, de test (réussite, échec), d'achèvement, et ainsi de suite. 

Dans la section suivante, nous examinerons un autre élément important de la documentation QA : le rapport de défaut.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/test-cases.png)
_Cas de test_

## Rapports de défauts

La déclaration de défauts est un élément important de la documentation QA. Le suivi des problèmes est la déclaration détaillée des problèmes soudains qui surviennent dans un produit logiciel. La documentation minutieuse de ces problèmes pose les bases d'un produit final complexe et sans bug. 

Cela semble simple, n'est-ce pas ? Oui, mais seulement jusqu'à ce que vous commenciez à documenter.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/bug-task.png)
_Un rapport de défaut_

Le rapport de bug se compose des sections suivantes : Identifiant, Résumé, Description, Étapes pour reproduire, Reproductibilité, Gravité, Priorité, Environnement et Pièces jointes.

* **Identifiant** : Chaque problème de programme logiciel se voit attribuer un identifiant complètement unique qui agit comme une plaque signalétique personnalisée. Cela rend la documentation QA moins compliquée à naviguer et permet une communication verbale entre l'installateur, le testeur et le chef de projet (PM).
* **Résumé** : C'est l'occasion de fournir des réponses brèves et informatives à trois questions de base : Quel était le problème ? Où le problème est-il apparu ? Dans quelles conditions spécifiques le problème est-il apparu ?
* **Explication** : Examinez le journal des échecs plus en détail. Résumez l'action identifiée (le résultat terminé) et vérifiez-la par rapport à l'action prévue (le résultat final prédit). Inclure un lien vers les exigences de l'application du programme logiciel peut servir d'élément de référence utile.
* **Méthode de reproduction** (STR) : Cette phase doit être considérée comme une recette étape par étape pour reproduire le défaut. Elle doit être stricte et couvrir toutes les étapes qui ont causé le problème. Sauter des étapes critiques peut rendre difficile la reproduction du problème et causer des retards.
* **Reproductibilité** : Dans cette section, vous clarifiez si le bug apparaît chaque fois que vous suivez le STR. Vous devez utiliser des nombres pour montrer les chances approximatives, par exemple, 7 fois sur 10.
* **Gravité** : Ici, vous expliquez combien de mal le bug peut apporter au projet. Essentiellement, il s'agit d'une mesure de la gravité de la perturbation technique qu'un bug causera à l'ensemble du projet. N'oubliez pas que les problèmes connus pour être mineurs peuvent croître et vous causer des problèmes extrêmes dans tout le logiciel.
* **Priorité** : Chaque journal d'erreurs attribue une priorité de problème qui indique son urgence. Les priorités courantes sont des lettres (A : priorité la plus élevée, Z : priorité la plus élevée), des nombres (1 : priorité la plus élevée, 9 : priorité la plus élevée), ou des termes descriptifs (élevée, moyenne, basse).
* **Environnement** : Spécifiez le modèle de gadget ou de navigateur dans lequel le bug est apparu. Cela vous aidera à mettre le problème en contexte et à réduire une cause valide.
* **Pièces jointes** : Si possible, enrichissez la documentation avec des captures d'écran, des enregistrements d'écran, des documents de journal de la console, et autres. Cela aidera à fournir une documentation visuelle de l'erreur.

Ma structure fournit des informations détaillées, afin que vous puissiez donner aux développeurs les moyens de diagnostiquer, de traiter et d'éliminer efficacement tout bug logiciel. De cette manière, cela conduit à des produits plus conviviaux et plus robustes. 

Maintenant, dans la section suivante, nous verrons quelques conseils utiles que vous pouvez utiliser pour la rédaction de rapports de défauts.

### Conseils utiles pour la rédaction de rapports de défauts

1. Écrivez un résumé suffisant. Peu importe qu'il soit long ou court. Ce qui compte, c'est qu'il soit clair.
2. Jetez un coup d'œil au résumé et à la description. Ont-ils l'air à peu près identiques ? Vous avez dû oublier de décrire les résultats attendus et réels dans la description et d'ajouter le lien vers les exigences.
3. Capturez le problème à l'aide d'une capture d'écran. Cela peut vous faire gagner beaucoup de temps, à vous et à l'équipe de développement. Parfois, un simple coup d'œil à l'image suffit pour comprendre la situation.
4. Avant de signaler le problème, essayez de le reproduire au moins 3 fois pour être sûr qu'il existe.
5. Signalez le problème dès que possible et informez votre chef de projet ou propriétaire de produit si le problème est majeur.
6. Vérifiez les erreurs de grammaire dans votre documentation QA pour ne pas être pris en défaut par la police de la grammaire.
7. Aussi comique que cela puisse paraître, assurez-vous que le problème n'est pas une fonctionnalité – relisez la documentation !
8. Ne manquez aucune information importante dans vos Étapes pour reproduire.

## Soumettre un rapport de défaut

L'élément final et l'un des plus importants de la documentation QA est le rapport de défaut. Vous comprenez qu'il couvre l'ensemble du cycle de vie d'un problème, de sa découverte initiale à sa fermeture finale. 

Examinons maintenant les domaines clés de ce processus :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/defect-report-lifecycle.jpg)
_un cycle de vie de rapport de défaut_

Nous allons passer en revue le mode de vie du rapport de défaut pièce par pièce :

### Signalement du problème :

Cette aventure commence par la compilation minutieuse et la soumission d'un rapport sur l'ensemble du programme. Cela sert de feuille de route pour les développeurs et fournit une évaluation claire du problème.

### Triage et tâches :

Le gestionnaire de tâches ou le responsable technique joue le rôle de gardien à ce stade. Ils comparent soigneusement les fichiers. Si le fichier contient suffisamment d'éléments pour travailler, il est attribué au développeur et réparé. Cependant, si le fichier manque d'éléments essentiels, il peut être rejeté pour une amélioration supplémentaire.

### Correction de bugs :

Le développeur attribué prend l'initiative et travaille diligemment pour éliminer le bug ennuyeux.

### Vérification et achèvement :

Une fois que le développeur affirme avoir résolu le problème, c'est à votre tour en tant que QA. Vérifiez soigneusement la correction en retestant la fonctionnalité en question. Si tout fonctionne comme il se doit, vous avez terminé. 

La documentation est arrivée à une fin heureuse. Idéalement, cela se produira dans un délai raisonnable d'une à deux semaines.

### Redémarrage et continuation :

Mais ce n'est pas toujours aussi simple. Si l'on sait que des bugs sont encore commises dans le système de validation, il n'y a pas lieu de désespérer ! 

Rouvrez la documentation des bugs et envoyez-la aux développeurs pour une attention supplémentaire. Parfois, le processus de correction des bugs est répétitif et nécessite de la patience. Mais en étant prudent et efficace, vous pouvez garantir que tous les rapports de bugs atteindront finalement leur destination finale, résultant en un produit logiciel plus poli et plus fiable.

## Conclusion

L'assurance qualité est un processus que vous ne pouvez tout simplement pas éviter. Chaque avion, avant le départ, subit une vérification technique. S'il y a un problème, l'avion est cloué au sol jusqu'à ce que le problème soit résolu. Il en va de même pour tout logiciel. 

Mais la documentation QA n'est pas toujours "écrite et ignorée". À un moment donné du cycle de vie du développement logiciel, la documentation QA doit être continuellement mise à jour et améliorée à mesure que les exigences changent, que de nouvelles fonctionnalités sont introduites et que des retours sont reçus de la mise en œuvre et de l'utilisation en production.

Il existe également un nombre croissant de styles qui utilisent l'intelligence artificielle et l'apprentissage automatique pour automatiser partiellement la création de la documentation QA. 

Par exemple, le traitement du langage naturel (NLP) est utilisé pour analyser les documents d'exigences et générer des exemples de contrôle de brouillon. Les bots de test peuvent utiliser le NLP pour interpréter et exécuter de manière routinière des cas de test dirigés. L'évaluation prédictive peut également être utilisée pour identifier les zones les plus dangereuses d'un programme logiciel qui nécessitent un contrôle plus détaillé.

Bien que ces stratégies soient encore nouvelles et pas assez matures pour remplacer les testeurs humains, elles peuvent aider à la croissance et augmenter l'exploration manuelle, surtout pour les constructions grandes et complexes. En faisant de la documentation QA un passe-temps collaboratif et continu, votre équipe peut livrer un meilleur logiciel plus rapidement et avec moins de défauts.

### Avez-vous besoin d'améliorer la qualité de votre logiciel ?

Mon entreprise KeenEthics fournit des services solides de [développement et d'assurance qualité](https://coventit.com/services/custom-software-development). Au cas où vous auriez besoin d'une estimation pour un projet similaire, n'hésitez pas à [nous contacter](https://coventit.com/contact-us).

Si vous avez apprécié l'article, vous devriez continuer avec [Comment l'externalisation IT économise des coûts pour votre entreprise](https://coventit.com/blog/How-IT-Outsourcing-Saves-Costs) et [Éviter les pièges de l'externalisation IT : Conseils pour minimiser les risques](https://coventit.com/blog/risks-of-it-outsourcing).