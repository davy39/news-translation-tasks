---
title: Comment utiliser SonarLint pour écrire un code plus propre
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2024-01-18T23:58:39.000Z'
originalURL: https://freecodecamp.org/news/use-sonarlint-to-write-cleaner-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/slint.jpg
tags:
- name: clean code
  slug: clean-code
- name: Visual Studio Code
  slug: vscode
- name: workflow
  slug: workflow
seo_title: Comment utiliser SonarLint pour écrire un code plus propre
seo_desc: 'When you''re building a coding project, the better it is, the more fun
  it''ll be to use. And the prouder you''ll be of your hard work, right?

  Also, writing quality and performant code helps your program or website work as
  expected – which should be ever...'
---

Lorsque vous construisez un projet de codage, plus il est de qualité, plus ce sera amusant à utiliser. Et plus vous serez fier de votre travail acharné, n'est-ce pas ?

De plus, écrire un code de qualité et performant aide votre programme ou site web à fonctionner comme prévu – ce qui devrait être l'objectif de chaque développeur.

[SonarLint](https://docs.sonarsource.com/sonarcloud/improving/sonarlint/) est un outil qui vous aide à vous assurer que votre code est de premier ordre. C'est comme avoir un guide amical qui vérifie votre code pour voir s'il est bien écrit et ne contient pas d'erreurs.

## Qu'est-ce que SonarLint ?

SonarLint est un outil d'analyse de code open-source qui vous aide à trouver et résoudre les problèmes de sécurité et de qualité de code dans votre code source au fur et à mesure que vous l'écrivez. Ce plugin fonctionne avec plusieurs environnements de développement intégrés (IDE), y compris des IDE bien connus comme IntelliJ IDEA, Eclipse et Visual Studio.

Le but principal de SonarLint est de vous donner un retour immédiat sur les problèmes potentiels de votre code, y compris les failles de sécurité, les bugs et d'autres pratiques recommandées pour la programmation. SonarLint analyse le code en arrière-plan pendant que vous le créez ou le modifiez dans votre IDE, vous donnant un retour instantané et exposant fréquemment les problèmes directement dans l'éditeur de code.

SonarLint est un composant de l'écosystème plus large de SonarQube.

Dans cet article, je vais vous apprendre à utiliser SonarLint pour vous aider à écrire un code de qualité.

## Pourquoi SonarLint est-il utile ?

Imaginons que la construction d'un site web est comme la construction d'une maison. Vous voulez que votre maison soit sûre et bien conçue, n'est-ce pas ? Eh bien, SonarLint est comme avoir un inspecteur minutieux qui vérifie votre travail au fur et à mesure que vous construisez, en s'assurant que tout est parfait.

Voici pourquoi SonarLint est important dans le développement web :

1. **Détecter les erreurs tôt (Qualité du code) :** Supposons que vous construisez un escalier et que vous avez accidentellement placé une marche au mauvais endroit, SonarLint est comme un ami intelligent qui vous dit immédiatement : "Hey, vous avez peut-être fait une erreur ici !" Il aide à détecter les petites erreurs dans votre code avant qu'elles ne deviennent de gros problèmes.

2. **Suivre le plan (Normes de codage) :** Lorsque vous construisez une maison, vous suivez un plan pour vous assurer que tout s'assemble correctement. En codage, il existe également des règles (comme un plan) sur la façon d'écrire un bon code. SonarLint vous aide à respecter ces règles, rendant votre code facile à lire et à utiliser.

3. **Garder la sécurité (Sécurité) :** Tout comme vous voudriez que votre maison ait de bonnes serrures sur les portes, vous voudriez que votre site web soit sécurisé. SonarLint vérifie votre code pour détecter les problèmes de sécurité potentiels, en vous assurant qu'il n'y a pas de "portes déverrouillées" qui pourraient laisser de mauvaises choses se produire.

4. **Bien travailler ensemble (Collaboration) :** Imaginez que chaque constructeur de votre équipe utilise un type d'outil différent. Ce serait le chaos ! SonarLint aide votre équipe à travailler ensemble en douceur en s'assurant que tout le monde suit les mêmes normes de codage. De cette façon, tout le monde peut comprendre et contribuer au projet facilement.

5. **Gagner du temps et des efforts (Efficacité) :** Corriger les erreurs après que toute la maison soit construite prendrait beaucoup de temps et d'efforts. SonarLint vous aide à corriger les problèmes au fur et à mesure, vous évitant de revenir en arrière et de tout refaire. C'est comme avoir un ami utile qui vous empêche de faire des erreurs dès le départ.

6. **Apprendre et s'améliorer (Éducation) :** SonarLint ne se contente pas de signaler les erreurs, mais explique également pourquoi elles pourraient poser problème. C'est comme avoir un professeur de codage qui vous aide à comprendre comment écrire un meilleur code. De cette façon, vous apprenez et devenez un meilleur développeur avec le temps.

Donc, dans le monde du développement web, SonarLint est votre compagnon de codage, et il s'assure que votre "maison" JavaScript est solide, sécurisée et bien organisée dès le départ. C'est un outil précieux dans votre flux de travail et il vous aide à créer des sites web de haute qualité que tout le monde peut apprécier.

Mais vous pouvez encore vous demander pourquoi vous avez besoin de cet outil. Vous avez déjà un débogueur installé dans votre IDE et il peut déjà suivre les erreurs dans votre environnement.

Eh bien, l'intégration de SonarLint complète votre débogueur en se concentrant sur la qualité et la sécurité du code pendant le développement.

Alors qu'un débogueur aide à trouver et corriger les problèmes d'exécution, SonarLint analyse le code en temps réel, identifie les bugs et les vulnérabilités potentielles, et fait respecter les normes de codage.

Vous pouvez également personnaliser et configurer les règles de codage en fonction des exigences spécifiques de votre projet et des normes de codage.

Cette approche proactive améliore la qualité globale du code et garantit un code plus propre et plus maintenable avant qu'il n'atteigne l'étape de débogage. Cela conduit à moins d'erreurs et à des flux de travail de développement plus fluides.

Avant d'entrer dans les détails de la configuration et de l'utilisation de SonarLint, examinons ce qui rend le code de haute qualité.

## Métriques de qualité du code

Soyez le meilleur auteur de livres de cuisine ! Lorsque vous écrivez du code, il existe des directives spécifiques que vous devez suivre.

Tout comme lorsque vous préparez une nouvelle recette ou que vous voulez suivre une recette traditionnelle, vous devez vous assurer que quiconque la lit peut la suivre, et que la recette que vous avez écrite donne un bon plat.

Dans le même sens, lorsque vous écrivez du code, il est toujours important de rendre votre code lisible afin que d'autres développeurs puissent le comprendre facilement et que votre code fonctionne comme il est censé le faire. Les métriques de qualité du code sont comme mesurer à quel point vous avez bien suivi la recette.

Voici une ventilation :

**Lisibilité (Clarté) :** Cela ressemble à s'assurer que les instructions de votre recette sont claires. Le code doit être facile à comprendre pour les autres (ou pour vous dans le futur).

**Maintenabilité (Facilité des modifications) :** Si vous deviez changer des ingrédients dans votre recette (code), il devrait être facile de changer les choses sans chaos.

**Performance (Vitesse) :** Comme vous voudriez que votre repas soit prêt rapidement, un code efficace est censé s'exécuter rapidement. Les métriques de qualité du code vérifient à quelle vitesse votre code est exécuté.

**Fiabilité (Cohérence) :** Une bonne recette a toujours le même goût. De même, un code fiable produit constamment les résultats corrects.

**Sécurité (Sécurité) :** Tout comme vérifier si les ingrédients sont sûrs à manger, les métriques de qualité du code recherchent les dangers potentiels dans votre code qui pourraient être exploités.

Ceux-ci devraient être vos objectifs lorsque vous écrivez un code de qualité. Et SonarLint peut vous aider à les accomplir.

## Comment configurer SonarLint et l'intégrer à votre IDE

Un IDE (Environnement de Développement Intégré) est une application logicielle qui aide les développeurs à écrire et déboguer du code plus efficacement. Les IDE incluent un éditeur de code et un compilateur ou un interpréteur.

Dans cet article, vous verrez comment installer SonarLint en utilisant les extensions de VS Code.

### Comment installer SonarLint avec VS Code

Tout d'abord, installez VS Code ou ouvrez l'application si vous l'avez déjà installée.

Ensuite, rendez-vous dans l'onglet Extensions de VS Code et téléchargez l'extension SonarLint.

Pour utiliser l'extension SonarLint pour JavaScript, TypeScript ou CSS, vous devez avoir une version minimale de `14.17.0` de Node.js installée sur votre système (surtout si vous voulez utiliser le [Mode Connecté](https://docs.sonarsource.com/sonarlint/vs-code/team-features/connected-mode/) avec Sonar Cloud).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonar.png align="left")

*Installer SonarLint dans VS Code*

Maintenant que vous avez installé SonarLint, l'exécution d'une analyse sur votre code devrait être facile et elle devrait commencer immédiatement après l'ouverture d'un nouveau fichier.

Cela signifie que SonarLint commencera à travailler et à détecter les erreurs dans votre code au fur et à mesure que vous les écrivez sur votre IDE. Maintenant, regardons un exemple dans la section suivante.

### Comment utiliser SonarLint dans votre IDE

Maintenant, voyons comment vous pouvez tirer le meilleur parti de SonarLint sur votre IDE. SonarLint est également un excellent enseignant, vous aidant à mieux comprendre comment écrire un code propre et vous donnant plus d'informations sur pourquoi vous avez une erreur.

Ainsi, au lieu de parcourir le web pour comprendre ce qui ne va pas avec votre code, SonarLint explique pourquoi il vous a donné une erreur.

Voici un exemple de la façon de l'utiliser.

Pour pouvoir voir l'interface sur laquelle nous allons travailler, ouvrez votre terminal dans VS Code – vous pouvez utiliser Ctrl + backtick (\`) pour cela. Je travaille actuellement sur un projet en React.js, et je n'ai pas remarqué que j'ai des noms de propriétés de bordure en double dans ma classe CSS. Heureusement, SonarLint a détecté ce problème.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint.png align="left")

*Une erreur CSS détectée par SonarLint*

Si vous cliquez sur l'ampoule, vous verrez une option pour corriger le code en désactivant la règle CSS ou en supprimant simplement la bordure supplémentaire que j'ai dans ma classe CSS dans ce cas. Il y a également une autre option pour ouvrir une règle de description afin que vous puissiez comprendre pourquoi vous obtenez cette erreur.

Ainsi, SonarLint vous donne deux options :

1. Il offre une option qui vous donne la capacité et les ressources pour comprendre pourquoi vous avez cette erreur avec le "Open description of rule".

2. Il offre une solution à l'erreur du code qu'il a trouvée.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint-another.png align="left")

*Options offertes par SonarLint pour aider à corriger et comprendre ce problème*

Si vous cliquez sur la règle de description ouverte, SonarLint ouvre un autre onglet dans VS Code pour vous aider à comprendre pourquoi il a lancé cette erreur et comment vous pouvez écrire un code plus propre/meilleur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint-teacher.png align="left")

*Onglet ouvert par SonarLint dans VSCode pour aider à comprendre l'erreur*

Comme vous pouvez le voir, SonarLint est un excellent enseignant et votre meilleur compagnon alors que vous continuez à construire et à travailler sur votre IDE.

Une autre grande chose à propos de SonarLint est qu'il fonctionne avec plusieurs langages de programmation. Donc, quel que soit le langage de programmation que vous utilisez, il y a de fortes chances que SonarLint puisse le gérer.

## Conclusion

SonarLint est comme avoir un compagnon de codage qui vous aide à devenir un meilleur programmeur. Au fur et à mesure que vous écrivez du code, c'est comme avoir un enseignant à vos côtés, pointant des moyens de vous améliorer.

Imaginez avoir un ami super intelligent qui ne se contente pas de repérer les erreurs mais explique également pourquoi elles sont mauvaises et vous montre comment les corriger.

Avant que votre code n'atteigne l'étape de test, SonarLint vérifie les erreurs et s'assure que votre programme fonctionne sans problème. C'est comme avoir un super pouvoir pour détecter les problèmes tôt, vous faisant gagner du temps et des efforts.

Mais ce n'est pas tout ! SonarLint est également comme un garde de sécurité pour votre code. Il surveille les points faibles potentiels qui pourraient laisser de mauvaises choses se produire. En apprenant de SonarLint, vous pouvez écrire un meilleur code et devenir plus conscient de garder votre code sûr et sécurisé.