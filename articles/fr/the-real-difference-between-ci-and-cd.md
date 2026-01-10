---
title: La vraie différence entre l'Intégration Continue et le Déploiement Continu
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-01T21:37:46.000Z'
originalURL: https://freecodecamp.org/news/the-real-difference-between-ci-and-cd
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/continuous-integration-and-delivery.png
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
seo_title: La vraie différence entre l'Intégration Continue et le Déploiement Continu
seo_desc: "By Jean-Paul Delimat\nThere is plenty of content out there describing what\
  \ Continuous Integration, Continuous Delivery, and Continuous Deployment are. But\
  \ what purposes do these processes serve in the first place? \nIt is crucial to\
  \ understand the prob..."
---

Par Jean-Paul Delimat

Il existe de nombreux contenus décrivant ce que sont l'Intégration Continue, la Livraison Continue et le Déploiement Continu. Mais à quoi servent ces processus en premier lieu ?

Il est crucial de comprendre les problèmes que résolvent l'IC et le DC pour les utiliser correctement. Cela permettra à votre équipe d'améliorer votre processus et d'éviter de gaspiller des efforts à poursuivre des métriques fantaisistes qui n'apportent aucune valeur à votre processus.

## L'Intégration Continue est un problème d'équipe

Si vous travaillez en équipe, il est probable que plusieurs développeurs travaillent sur le même dépôt. Il y a une branche principale dans le dépôt qui contient la dernière version du code. Les développeurs travaillent sur différentes choses dans différentes branches. Une fois qu'une personne a terminé sa modification, elle la pousse ou la fusionne dans la branche principale. Finalement, toute l'équipe tirera cette modification.

Le scénario que nous voulons éviter est qu'un commit défectueux arrive dans la branche principale. Défectueux signifie que le code ne compile pas ou que l'application ne démarre pas ou est inutilisable. Pourquoi ? Non pas parce que l'application est cassée ou parce que tous les tests doivent toujours être verts. Ce n'est pas un problème, vous pouvez décider de ne pas déployer cette version et attendre une correction.

Le problème est que toute votre équipe est bloquée. Tous les développeurs qui ont tiré le commit défectueux passeront 5 minutes à se demander pourquoi cela ne fonctionne pas. Plusieurs essaieront probablement de trouver le commit défectueux. Certains essaieront de corriger le problème par eux-mêmes en parallèle de l'auteur du code défectueux.

C'est une perte de temps pour votre équipe. Le pire, c'est que les incidents répétés alimentent une méfiance envers la branche principale et encouragent les développeurs à travailler séparément.

> L'Intégration Continue consiste à empêcher la branche principale de se casser afin que votre équipe ne soit pas bloquée. C'est tout. Ce n'est **pas** une question d'avoir tous vos tests verts tout le temps et la branche principale déployable en production à chaque commit.

Le processus d'Intégration Continue est indépendant de tout outil. Vous pourriez vérifier manuellement que la fusion de votre branche et de la branche principale fonctionne localement, puis seulement pousser la fusion dans le dépôt. Mais ce serait très inefficace. C'est pourquoi l'Intégration Continue est mise en œuvre à l'aide de vérifications automatisées.

Les vérifications garantissent que, au minimum :

* L'application doit se construire et démarrer
* Les fonctionnalités les plus critiques doivent être fonctionnelles à tout moment (parcours d'inscription/connexion de l'utilisateur et fonctionnalités clés de l'entreprise)
* Les couches communes de l'application sur lesquelles tous les développeurs s'appuient doivent être stables. Cela signifie des tests unitaires sur ces parties.

En pratique, cela signifie que vous devez utiliser n'importe quel framework de tests unitaires qui fonctionne pour vous et sécuriser les couches communes de l'application. Parfois, ce n'est pas beaucoup de code et cela peut être fait assez rapidement. Vous devez également ajouter un "test de fumée" vérifiant que le code compile et que l'application démarre. Cela est particulièrement important dans les technologies avec des injections de dépendances complexes comme Java Spring ou .NET core. Dans les grands projets, il est si facile de mal configurer vos dépendances que vérifier que l'application démarre toujours est une nécessité.

> Si vous avez des centaines ou des milliers de tests, vous n'avez pas besoin de tous les exécuter pour chaque fusion. Cela prendra beaucoup de temps et la plupart des tests vérifient probablement des fonctionnalités "non bloquantes pour l'équipe".

Nous verrons dans les prochaines sections comment le processus de Livraison Continue tirera parti de ces nombreux tests.

### Ce n'est pas une question d'outils

Les outils et les vérifications automatisées sont très bien. Mais si vos développeurs ne fusionnent que des branches géantes sur lesquelles ils travaillent pendant des semaines, ils ne vous aideront pas. L'équipe passera beaucoup de temps à fusionner les branches et à corriger les incompatibilités de code qui finiront par survenir. C'est autant une perte de temps que d'être bloqué par un commit défectueux.

> L'Intégration Continue ne concerne pas les outils. Il s'agit de travailler par petites portions et d'intégrer votre nouveau code à la branche principale et de tirer fréquemment.

Fréquemment signifie au moins quotidiennement. Divisez la tâche sur laquelle vous travaillez en tâches plus petites. Fusionnez votre code très souvent et tirez très souvent. De cette façon, personne ne travaille séparément pendant plus d'un jour ou deux et les problèmes n'ont pas le temps de devenir des boules de neige.

Une grande tâche n'a pas besoin d'être entièrement dans une seule branche. Elle ne devrait jamais l'être. Les techniques pour fusionner le travail en cours dans la branche principale sont appelées "branching by abstraction" et "feature toggles". Voir l'article de blog [Comment commencer avec l'Intégration Continue](https://fire.ci/blog/how-to-get-started-with-continuous-integration/) pour plus de détails.

### Points clés pour une bonne construction CI

C'est très simple. **Gardez-la courte. 3-7 minutes devraient être le maximum.** Ce n'est pas une question de CPU et de ressources. Il s'agit de la productivité des développeurs. La première règle de la productivité est la concentration. Faites une chose, terminez-la, puis passez à la suivante.

Le changement de contexte est coûteux. Les études montrent qu'il faut ~23 minutes pour se reconcentrer profondément sur quelque chose lorsque vous êtes perturbé.

Imaginez que vous poussez votre branche pour la fusionner. Vous commencez une autre tâche. Vous passez 15-20 minutes à vous y mettre. La minute après être dans la zone, vous recevez une notification "build failed" de votre construction CI de 20 minutes pour la tâche précédente. Vous revenez pour la corriger. Vous la poussez à nouveau. Vous avez facilement perdu plus de 20 minutes à aller et venir.

> Multipliez 20 minutes une ou deux fois par jour par le nombre de développeurs dans votre équipe... C'est beaucoup de temps précieux gaspillé.

Maintenant, imaginez si le retour venait dans les 3 minutes. Vous n'auriez probablement pas commencé la nouvelle tâche du tout. Vous auriez relu votre code une fois de plus ou révisé une PR en attendant. La notification d'échec arriverait et vous la corrigeriez. Ensuite, vous pourriez passer à la tâche suivante. C'est le genre de concentration que votre processus devrait permettre.

Garder votre construction CI courte en fait un compromis. Les tests qui prennent plus de temps ou qui apportent peu de valeur dans le contexte de l'IC doivent être déplacés vers l'étape de DC. Et oui, les échecs là-bas doivent également être corrigés. Mais comme ils n'empêchent personne de faire son travail, vous pouvez prendre les corrections comme une "prochaine tâche" lorsque vous terminez ce que vous faites. Éteignez simplement les notifications pendant que vous travaillez et vérifiez de temps en temps. Gardez le changement de contexte au minimum.

## La Livraison Continue et le Déploiement Continu sont des problèmes d'ingénierie

Commençons par les définitions pour clarifier cela.

**La Livraison Continue** consiste à pouvoir déployer n'importe quelle version de votre code à tout moment. En pratique, cela signifie la dernière ou l'avant-dernière version de votre code. Vous ne déployez pas automatiquement, généralement parce que vous n'avez pas à le faire ou êtes limité par le cycle de vie de votre projet. Mais dès que quelqu'un en a envie, un déploiement peut être effectué en un minimum de temps. Cette personne peut être l'équipe de test/QA qui souhaite tester des choses sur un environnement de staging ou de pré-production. Ou il peut effectivement être temps de déployer le code en production.

L'idée de la Livraison Continue est de préparer des artefacts aussi proches que possible de ce que vous voulez exécuter dans votre environnement. Ceux-ci peuvent être des fichiers .jar ou .war si vous travaillez avec Java, ou des exécutables si vous travaillez avec .NET. Ceux-ci peuvent également être des dossiers de code JS transpilé ou même des conteneurs Docker, tout ce qui rend le déploiement plus court (c'est-à-dire que vous avez pré-construit autant que possible à l'avance).

En préparant des artefacts, je ne veux pas dire transformer le code en artefacts. Cela prend généralement quelques scripts et minutes d'exécution. Préparer signifie :

> Exécutez tous les tests que vous pouvez pour vous assurer que, une fois déployé, le code fonctionnera réellement. Exécutez des tests unitaires, des tests d'intégration, des tests de bout en bout, et même des tests de performance si vous pouvez automatiser cela.

De cette façon, vous pouvez filtrer quelles versions de votre branche principale sont réellement prêtes pour la production et lesquelles ne le sont pas. La suite de tests idéale :

* Garantit que les fonctionnalités clés de l'application fonctionnent. Idéalement, toutes les fonctionnalités
* Garantit qu'aucun problème de performance critique n'a été introduit afin que, lorsque votre nouvelle version atteint vos nombreux utilisateurs, elle ait une chance de durer
* Effectue un essai à sec de toute mise à jour de base de données dont votre code a besoin pour éviter les surprises

Elle n'a pas besoin d'être très rapide. 30 minutes ou 1 heure est acceptable.

**Le Déploiement Continu** est l'étape suivante. Vous déployez la version la plus à jour et prête pour la production de votre code dans un environnement. Idéalement en production si vous faites suffisamment confiance à votre suite de tests DC.

Notez que, selon le contexte, cela n'est pas toujours possible ou ne vaut pas l'effort. La Livraison Continue est souvent suffisante pour être productive, surtout si vous travaillez dans un réseau fermé et avez des environnements limités dans lesquels vous pouvez déployer. Il peut également être que le cycle de publication de votre logiciel empêche les déploiements non planifiés.

La Livraison Continue et le Déploiement Continu (appelons-les DC à partir de maintenant) ne sont pas des problèmes d'équipe. Ils consistent à trouver le bon équilibre entre le temps d'exécution, les efforts de maintenance et la pertinence de votre suite de tests pour pouvoir dire "Cette version fonctionne comme elle le devrait."

Et c'est un équilibre. Si vos tests durent 30 heures, c'est un problème. Voir [cet article épique](https://news.ycombinator.com/item?id=18442941) sur ce à quoi ressemble la suite de tests de la base de données Oracle. Mais si vous passez tellement de temps à maintenir vos tests à jour avec le dernier code que cela entrave la progression de l'équipe, ce n'est pas bon non plus. De plus, si votre suite de tests ne garantit presque rien... elle est essentiellement inutile.

Dans un monde idéal, nous voulons un ensemble d'artefacts déployables par commit dans la branche principale. Vous pouvez voir que nous avons un problème de scalabilité verticale : plus nous passons rapidement du code aux artefacts, plus nous sommes prêts à déployer la version la plus récente du code.

## Quelle est la grande différence ?

L'Intégration Continue est un problème de scalabilité horizontale. Vous voulez que les développeurs fusionnent leur code souvent afin que les vérifications doivent être rapides. Idéalement en quelques minutes pour éviter que les développeurs ne changent de contexte tout le temps avec des retours hautement asynchrones des constructions CI.

Plus vous avez de développeurs, plus vous avez besoin de puissance de calcul pour exécuter des vérifications simples (construction et test) sur toutes les branches actives.

> **Une bonne construction CI :**

> Garantit qu'aucun code qui casse les choses de base et empêche les autres membres de l'équipe de travailler n'est introduit dans la branche principale, et

> Est suffisamment rapide pour fournir un retour aux développeurs en quelques minutes afin d'éviter le changement de contexte entre les tâches.

La Livraison Continue et le Déploiement Continu sont des problèmes de scalabilité verticale. Vous avez une opération plutôt complexe à effectuer.

> **Une bonne construction CD :**

> Garantit que le plus grand nombre de fonctionnalités possible fonctionnent correctement.

> Plus c'est rapide, mieux c'est, mais ce n'est pas une question de vitesse. Une construction de 30-60 minutes est acceptable.

Une idée fausse courante est de voir le CD comme un problème de scalabilité horizontale comme le CI : plus vous pouvez passer rapidement du code aux artefacts, plus vous pouvez traiter de commits, et plus vous pouvez vous rapprocher du scénario idéal.

Mais nous n'en avons pas besoin. Produire des artefacts pour chaque commit et aussi rapidement que possible est généralement excessif. Vous pouvez très bien aborder le CD sur une base de meilleur effort : avoir une seule construction CD qui sélectionnera simplement le dernier commit à vérifier une fois qu'une construction donnée est terminée.

Ne vous trompez pas sur le CD. C'est vraiment difficile. Atteindre une confiance suffisante dans les tests pour dire que votre logiciel est prêt à être déployé automatiquement fonctionne généralement sur des applications à faible surface comme les API ou les interfaces utilisateur simples. Il est très difficile à réaliser sur une interface utilisateur complexe ou un grand système monolithique.

## Conclusion

Les outils et les principes utilisés pour exécuter l'IC et le DC sont souvent très similaires. Les objectifs sont cependant très différents.

L'Intégration Continue est un compromis entre la vitesse de la boucle de retour aux développeurs et la pertinence des vérifications que vous effectuez (construction et test). Aucun code qui entraverait la progression de l'équipe ne devrait arriver dans la branche principale.

La Livraison Continue ou le Déploiement Continu consiste à exécuter des vérifications aussi approfondies que possible pour détecter les problèmes dans votre code. L'exhaustivité des vérifications est le facteur le plus important. Elle est généralement mesurée en termes de couverture de code ou de couverture fonctionnelle de vos tests. Détecter les erreurs tôt empêche le code défectueux d'être déployé dans un environnement et économise le temps précieux de votre équipe de test.

Concevez vos constructions CI et CD pour atteindre ces objectifs et gardez votre équipe productive. Aucun workflow n'est parfait. Des problèmes surgiront de temps en temps. Utilisez-les comme des leçons apprises pour renforcer votre workflow chaque fois qu'ils se produisent.

Publié le 27 nov. 2019 sur le [Blog Fire CI](https://fire.ci/blog/).