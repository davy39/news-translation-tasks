---
title: Comment rédiger une bonne description de Pull Request – Et pourquoi c'est important
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T22:01:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-pull-request-description
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wp3082255.jpg
tags:
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Testing
  slug: testing
- name: version control
  slug: version-control
seo_title: Comment rédiger une bonne description de Pull Request – Et pourquoi c'est
  important
seo_desc: "By Sajal Sharma\nWriting a good Pull Request description is one of the\
  \ most tedious jobs a developer has to do. And it can feel counter-productive at\
  \ times. \nBut developing this skill goes a long way and really helps your stakeholders\
  \ and your organiz..."
---

Par Sajal Sharma

Rédiger une bonne description de Pull Request est l'une des tâches les plus fastidieuses qu'un développeur doit accomplir. Et cela peut parfois sembler contre-productif. 

Mais développer cette compétence est très utile et aide vraiment vos parties prenantes et votre organisation à long terme. 

Il est donc toujours préférable de prendre ces 10 minutes supplémentaires aujourd'hui plutôt que de devoir se casser la tête dans 6 mois pour expliquer pourquoi vous avez fait ce que vous avez fait.

L'article suivant explique les différentes parties d'une description de Pull Request, et pourquoi vous devriez les inclure.

## Qu'est-ce qu'une description de PR ?

Une description de pull request décrit ce qui constitue la Pull Request et quelles modifications vous avez apportées au code.

Elle explique ce que vous avez fait, y compris les modifications de code, les modifications de configuration, les migrations incluses, les nouvelles API introduites, les modifications apportées aux anciennes API, les nouveaux workers/crons introduits dans le système, les modifications de copie, et ainsi de suite. Vous comprenez l'idée.

Vous devriez inclure cette section car elle donne un aperçu aux différentes parties prenantes de ce que la PR fait. 

Pour une personne non technique, la description devrait expliquer quel sera l'impact sur le système lorsque ces modifications de code seront déployées en production. 

Cela aidera également le relecteur à comprendre ce qu'il devra examiner (une sorte de prologue/bande-annonce). 

Et enfin, cela aide les équipes QA/SDET à comprendre la portée de la PR également. 

Ainsi, le "quoi" de la PR devrait donner un aperçu de ce qui constitue les modifications dans la PR.

## La section "Pourquoi"

Cette section explique pourquoi les modifications décrites ci-dessus ont été effectuées.

Parfois, un développeur pense qu'il est acceptable d'écrire "Exigence métier/produit" dans la description. C'est bien, mais cela va à l'encontre du but de cette section. 

S'il existe une meilleure explication quant à la raison pour laquelle les modifications ont été suggérées, il est toujours bon de joindre un lien de référence vers un document contenant ces informations. Une bonne section "Pourquoi" devrait expliquer la raison derrière les modifications.

Vous devriez inclure cette section car elle donne une explication sur pourquoi vous avez suggéré vos modifications. Cela peut ne pas sembler raisonnable d'inclure cette section à court terme, mais elle joue un rôle vital à mesure que le produit mûrit et s'étend sur plusieurs années. 

Les développeurs et les équipes produit viennent et partent, mais le code reste. Et lorsqu'un nouveau développeur travaille sur un morceau de code et y trouve une incohérence, il peut creuser plus profondément et retrouver la pull request de 2 ans auparavant qui a apporté ces modifications. 

Un bon "pourquoi" leur donne l'explication et les hypothèses faites à cette époque.

**Le CTO de GoJek** a un jour expliqué qu'ils ne remettent pas en question leur code hérité et ne se demandent pas pourquoi il semble y avoir une fonctionnalité absurde dans le produit. 

Ils retournent simplement vérifier la documentation. 

Les hypothèses et les circonstances peuvent avoir changé, et donc le code évolue. Ce qui semble assez absurde aujourd'hui aurait pu être pertinent il y a 2 ans. Il est donc préférable d'expliquer aujourd'hui pourquoi vous apportez une modification particulière.

## Portée des tests

Cette section devrait comprendre une liste de scénarios sur lesquels vous devez vous concentrer lors du test de cette PR particulière. (Cela inclut les flux, les API, les crons, les workers, et ainsi de suite.)

Une bonne portée de test donne de la visibilité à l'équipe QA/SDET sur les scénarios et les flux qu'ils doivent tester.

Cela peut également vous aider pendant que vous écrivez cette section. Je suis tombé sur des problèmes moi-même, ce qui m'a incité à revenir à la phase de développement et à les tester à nouveau. 

Une portée de test bien rédigée aide les développeurs à tester la PR plus efficacement et donne une image complète de la PR à la personne qui la teste.

## Document(s) pertinent(s)

Cette section inclut tout document pertinent qui doit être joint à la description de la PR.

Cela peut inclure des documents d'exigences produit, des diagrammes architecturaux, des diagrammes de système de base de données, des modèles de conception utilisés, des diagrammes de classe, de la documentation de bibliothèques externes, et ainsi de suite.

Cette section aide à expliquer les hypothèses et les références que vous avez faites lors du travail sur cette demande de fonctionnalité. Et elle joue un rôle majeur à long terme. 

Lorsque quelqu'un revient et voit pourquoi une telle modification a été suggérée, la section des documents pertinents le dirigera vers la documentation spécifique afin qu'il puisse comprendre clairement le problème. Ou cela peut le diriger vers les détails techniques de l'implémentation du scénario au moment du développement.

## PR(s) dépendante(s) (le cas échéant)

Il arrive que certaines fonctionnalités s'étendent sur plusieurs dépôts GitHub et qu'il soit important de les publier dans un certain ordre. 

Par exemple, vous devrez peut-être déployer un dépôt avant un autre, ou vous devrez peut-être les déployer côte à côte.

Quoi qu'il en soit, cette section explique tout code dépendant sur lequel cette PR repose.

Vous devriez inclure cette section car elle aide vraiment le déployeur à comprendre l'ordre de déploiement. Si le code d'un autre dépôt doit être déployé en premier, alors le déployeur contactera la personne responsable du déploiement de l'autre dépôt pour s'assurer que leur déploiement se fasse en premier. Globalement, cela aide à simplifier le processus de déploiement.

## Modifications de configuration (le cas échéant)

Cette section devrait inclure toutes les modifications de configuration qui doivent être ajoutées aux secrets avant que la PR ne soit déployée en production.

Il arrivera que le déployeur fusionne 10 à 20 PR à la fois et il devient difficile pour lui de suivre toutes les modifications de configuration. 

Pour cette raison, il est toujours préférable de les inclure dans la section des modifications de configuration. (Ne mettez pas les clés secrètes là, incluez simplement les noms des clés et comment obtenir les secrets.)

## Tags/Étiquettes

Ceux-ci sont très importants dans une description de pull request et transmettent beaucoup de sens lorsque l'équipe grandit. 

Voici quelques tags que j'utilise, mais vous pouvez ajouter différents tags selon vos besoins.

* **Dev Complété** - Lorsque le développement est terminé du côté du développeur.
* **Auto-revu** - Lorsque le ou les développeurs de la Pull Request ont revu la Pull Request de leur côté et peuvent maintenant la donner à leurs pairs pour une relecture.
* **Auto-testé** - Lorsque le ou les développeurs de la Pull Request ont testé les modifications eux-mêmes selon la description qu'ils ont donnée dans la section Portée des tests.
* **Modifications de configuration** - Ce tag indique qu'il y a des modifications de configuration à effectuer avant de déployer la PR en production. (Cela inclut les clés secrètes qui doivent être mises dans le système.)
* **Contient des migrations** - Cela indique que la PR contient une migration. Si c'est une migration longue, cela devrait être spécifié au préalable.
* **Prêt pour la publication** - Cela indique au déployeur que la PR est prête pour le déploiement et sera prise en charge par le déployeur dans le prochain cycle de déploiement.
* **Relecture par les pairs** - Lorsque le pair a revu la PR et que les modifications suggérées sont faites par le ou les développeurs. Cela est mis en place par le pair qui a revu la PR.
* **Testé par la QA** - Cela indique que la QA/SDET a testé la PR et qu'elle est prête à être déployée en production.

## Conclusion

Dans cet article, nous avons passé en revue les différentes parties d'une description de PR. La plupart des PR que vous créez n'auront pas besoin de toutes ces sections et tags, mais vous devriez essayer d'en inclure autant que possible. 

Rédiger cette description peut ne pas sembler productif au moment où vous créez une PR, mais cela peut définitivement s'avérer utile à l'avenir.

Une dernière remarque : Ce qui précède représente mes opinions et peut différer de votre perspective. Mais j'ai développé cette stratégie au fil des ans, et elle contient les contributions et l'expérience de nombreuses personnes avec lesquelles j'ai travaillé dans l'industrie. Vous pouvez donc vous sentir en confiance en sachant qu'elle a été testée en conditions réelles à un haut degré.