---
title: L'assurance qualité est brisée. Voici comment nous pouvons la rendre aussi
  agile que tout le reste.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-22T18:24:58.000Z'
originalURL: https://freecodecamp.org/news/quality-assurance-is-broken-heres-how-we-can-make-it-as-agile-as-everything-else-64bd19d5e426
coverImage: https://cdn-media-1.freecodecamp.org/images/0*13Pw6ew6bhXzg5wp.
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: L'assurance qualité est brisée. Voici comment nous pouvons la rendre aussi
  agile que tout le reste.
seo_desc: 'By Derwin

  Process is the key to great software.

  In general, the industry has made leaps and bounds in software development processes.
  But testing processes still remain archaic.

  Test engineers are forced to manually crunch through tests and bugs at t...'
---

Par Derwin

Le processus est la clé d'un excellent logiciel.

En général, l'industrie a fait des bonds en avant dans les processus de développement logiciel. Mais les processus de test restent encore archaïques.

Les ingénieurs de test sont obligés de traiter manuellement les tests et les bugs à la fin de chaque cycle de développement.

Le résultat ? Une tonne de temps et d'énergie gaspillés tout au long du processus.

Le développement agile est radicalement différent de la méthode en cascade, qui est une méthodologie de développement logiciel plus ancienne et plus rigide.

Notre équipe pratique l'agile. Mais en tant que leader d'une équipe d'ingénieurs de test, j'ai remarqué que notre processus d'assurance qualité est beaucoup plus similaire à la méthode en cascade.

### Le QA en cascade

Nous commençons les tests à la fin du processus de développement. Cela laisse les ingénieurs de test à court de temps. On pourrait dire que les tests QA dans l'agile sont une version compressée de la méthode en cascade.

Bien qu'il y ait moins de tests par session dans l'agile que dans la méthode en cascade, le processus pourrait être beaucoup plus efficace. Pour commencer, lorsque les tests sont regroupés à la fin, ils sont souvent très urgents et sensibles au temps. Cela force les ingénieurs de test à optimiser pour la vitesse, ce qui signifie généralement tester les produits manuellement.

Évidemment, les tests manuels fonctionnent. Mais il y a tant d'aspects de ces tests qui pourraient être automatisés si les ingénieurs de test avaient plus de temps pour écrire des scripts qui testent le logiciel.

Le coût temporel des tests manuels s'accumule dans les semaines suivantes, car le QA teste manuellement les nouvelles versions du même logiciel. Au lieu de cela, ils auraient pu construire des scripts automatisés pour tester davantage le logiciel, ce qui libérerait les ingénieurs de test et fournirait un retour plus rapide pour les ingénieurs logiciels.

Chez Flipp, nous avons essayé de tester le logiciel de manière manuelle, à l'ancienne. Mais nous avons rencontré nos propres inconforts et défis.

Par exemple, tout retard dans le système ou la sortie de la fonctionnalité aurait un impact sur l'équipe QA la semaine suivante. Ces types de retards s'accumulaient, au point où l'équipe d'ingénierie logicielle serait extrêmement en avance sur le QA, et le QA essayerait désespérément de rattraper son retard.

Une solution courante au problème de l'équipe de développement prenant trop d'avance sur l'équipe de test est d'organiser un "bug bash". Ainsi, l'équipe de développement peut tous tester les bugs pour aider l'équipe QA à rattraper son retard avant la fin du sprint.

Nous avons mis en place une solution encore plus simple : **les équipes de développement incluent les ingénieurs de test dès le début.**

Ainsi, les ingénieurs de test peuvent identifier des scénarios et écrire des scripts pour tester le nouveau code de l'équipe de développement. Alors que les développeurs construisent le logiciel réel, les ingénieurs de test peuvent construire les scripts pour tester ce logiciel, qui peuvent être utilisés encore et encore chaque semaine. Plus important encore, cela permet collectivement d'économiser beaucoup de temps, d'attention et d'énergie dans les tests ultérieurs.

Chez Flipp, notre équipe QA pose beaucoup de questions de précision et d'aspects de conception de testabilité dès le début, afin de ne pas avoir à passer par le cycle de QA pour découvrir qu'il y a des bugs dans le système. Nous le questionnons dès le départ. Voici quelques exemples standards de nos questions de précision :

* « Quelle charge prévoyons-nous ? »
* « Quels types de balises analytiques utilisons-nous pour mesurer le succès du projet ? »
* « Comment allons-nous le rendre testable pour pouvoir le déployer facilement ? »

Voici les avantages que nous avons remarqués en mettant en place cette solution, et pourquoi nous pensons que chaque entreprise doit repenser la manière dont elle teste la qualité.

### **_Retour plus rapide que l'agile_**

![Image](https://cdn-media-1.freecodecamp.org/images/29ySTNEC89U1NhUDTTwpeVsIHPnch4o1fwbR)

En général, la durée du cycle de sprint varie d'un projet à l'autre. Mais par exemple, disons que chaque sprint dure cinq jours.

Lors des trois premiers jours, les ingénieurs logiciels passeront par le système de ticketing — construisant des fonctionnalités et complétant des tickets. Une fois terminés, ils passent leur version au QA. Les ingénieurs de test du QA ont les derniers jours pour examiner ces tickets.

Ce serait un cycle de sprint typique à la fois en agile et en cascade : Planifier, développer, coder et tester.

J'ai mentionné cela plus tôt, mais je veux vraiment insister sur ce point :

Au lieu de laisser les tests à la fin, nous devrions implémenter les tests dès le début (pendant la phase de "planification") et commencer à poser des questions. En tant qu'ingénieurs de test, nous devrions déterminer comment tester et quels systèmes nous devons construire pour pouvoir le tester dès le départ.

Traditionnellement, les ingénieurs logiciels enverraient une version aux ingénieurs de test, qui effectueraient ensuite manuellement un test et la renverraient aux ingénieurs logiciels s'il y avait des problèmes ou des bugs avec le code. Il y aurait un décalage de 1 à 2 jours car le QA pourrait travailler sur des tickets précédents. Les ingénieurs logiciels devraient attendre que ce ticket soit terminé. Donc, si les tests QA sont effectués manuellement :

1. Les ingénieurs de test préparent le temps pour effectuer les tests
2. Les ingénieurs logiciels perdent du temps et de l'énergie à changer de contexte entre différents tickets
3. Les ingénieurs de test passent du temps à effectuer les tests

Assez encombrant, n'est-ce pas ? Regardons comment un test automatisé pourrait fonctionner :

Un ingénieur de test construit un script où chaque fois que quelqu'un apporte une modification et la déploie sur les serveurs, le test garantit qu'il n'y aura pas d'erreurs 500 ou d'erreurs JavaScript. Si le test trouve l'une de ces erreurs, la version a échoué ce test, et les ingénieurs logiciels seront avertis en quelques minutes. Personne n'a à attendre 2 à 3 jours, cela se fait automatiquement. Ce retour extrêmement rapide permet à l'équipe logicielle de se déplacer beaucoup plus rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/C0CzSGxUDLrjKLzL56kWt5XrwI8W48zXH9yY)

Le retour rapide se traduit par des économies significatives, en particulier pour les erreurs simples et évidentes. Il minimise également le changement de contexte, un coût souvent négligé.

Considérez l'esprit des ingénieurs logiciels lorsqu'ils doivent revenir à la version qu'un ingénieur de test vient de renvoyer. « Quelle était cette fonctionnalité à nouveau ? Quel était ce bug ? Comment le corriger ? »

Ici, en cinq minutes, ils sauront que la phase de test est terminée et si elle nécessite plus de travail.

Naturellement, à mesure que le logiciel devient plus complexe, les tests aussi.

### **_Minimiser les urgences_**

Parce que le QA considère les situations dès le début du processus de développement logiciel — et n'attend pas jusqu'à la fin pour tester manuellement les scénarios et les situations — ils auront plus de temps pour prédire les urgences ou considérer une gamme plus large de circonstances.

C'est aussi proche de zéro urgence que possible pour les ingénieurs logiciels et de test. Évidemment, des erreurs imprévues surviennent encore. Mais maintenant, l'équipe a une meilleure idée de la manière de collecter et de comprendre les données, et de l'impact d'un bug sur les utilisateurs.

Par exemple, disons que les utilisateurs signalent une erreur avec le curseur de réduction dans l'application Flipp. L'ingénieur de test aura considéré les balises analytiques nécessaires pour vérifier rapidement la portée et la signification du bug. Grâce à ces mesures, ils pourraient examiner les données et informer l'équipe : « Cela n'impacte que 1 % de nos utilisateurs. » Ils peuvent déterminer que ce qui semblait être une urgence ne l'est pas vraiment.

Une équipe QA standard est inflexible et ne permettra à aucun bug de passer. Ici, il y a une tolérance pour permettre aux petits bugs de passer — afin que les ingénieurs de test puissent se concentrer sur des bugs de plus haute priorité et de plus grande portée. Ils peuvent évaluer plus précisément le risque des bugs et ce qui passe. Si l'impact est minimal, alors les ingénieurs de test peuvent le signaler et faire en sorte que les ingénieurs logiciels le corrigent dans le prochain sprint.

### **_Réinventer la culture de votre équipe logicielle_**

En fin de compte, l'intégration des ingénieurs de test dans le processus de développement logiciel est un symptôme d'un changement culturel plus large. Les perspectives des ingénieurs de test seront désormais prises en compte plus tôt dans le processus.

Côté ingénierie de test, les ingénieurs de test doivent être plus curieux pour voir comment ils peuvent améliorer le système et sa qualité.

Le changement concernerait tout le monde — propriétaires de produits, scrum masters, ingénieurs de test et ingénieurs logiciels — acceptant ces questions plus tôt et les prenant en compte.

Cela unifiera l'équipe et créera une meilleure compréhension de ce à quoi ressemble le succès d'une fonctionnalité.

Typiquement, les responsables d'ingénierie et les propriétaires de produits prennent _x_ jours pour mener quelque chose à terme. Mais leur définition de « terminé » est différente de celle du QA. Leur définition de « terminé » est l'envoi du logiciel au QA. En revanche, la définition de « terminé » du QA est lorsque le logiciel est prêt à être publié pour les utilisateurs.

### Un compte rendu détaillé de la manière dont nous faisons le QA chez Flipp

En conclusion, je vais vous donner un exemple spécifique de ce à quoi cela pourrait ressembler lorsque votre équipe logicielle construit et teste une fonctionnalité. Passons en revue les différentes étapes d'un sprint de deux semaines, et quel devrait être le rôle, les objectifs et les priorités de l'ingénieur de test dans chacune d'elles.

Notez que chez Flipp, nous appelons nos ingénieurs de test « ingénieurs logiciels en test ». Pour plus de clarté, nous les avons appelés ingénieurs de test dans cet article, mais ce changement de terminologie dans notre organisation reflète à quel point le QA est vraiment intégré à l'équipe d'ingénierie logicielle.

#### Étape 1 : Concept

Cette étape a lieu le premier jour, lorsque la fonctionnalité n'est encore qu'une idée. L'équipe n'a pas beaucoup de clarté sur la fonctionnalité (environ 10 %). Ils en savent un peu, mais ne savent pas exactement comment elle sera construite.

Le travail le plus important de l'ingénieur de test à cette étape est de comprendre parfaitement, et potentiellement aider à définir, ce que signifie le succès pour le propriétaire du produit. Certaines entreprises appellent ces définitions les « critères d'acceptation ».

Dans tous les cas, je préfère utiliser la question directrice : « Qu'est-ce que gagner ? »

Trouver la réponse — et les métriques clés correspondantes — sera le principal objectif de toute l'équipe lors de l'étape de concept.

#### Étape 2 : Maquettes et designs

Cette étape a également lieu tôt dans le sprint (généralement le premier jour), lorsque la fonctionnalité a été définie un peu plus clairement (environ 30 %). La compréhension de la fonctionnalité par l'ingénieur de test changera la manière dont il la teste, et la compréhension du comportement utilisateur souhaité informera le flux de test.

Le propriétaire du produit pourrait définir la victoire comme le fait que l'utilisateur effectue une certaine action. Si c'est le cas, l'ingénieur de test doit aider à déterminer comment amener l'utilisateur là. Alors que l'équipe commence à préparer des maquettes, certains flux ou concepts pourraient ne pas avoir de sens. C'est le travail de l'ingénieur de test et de l'équipe de signaler les maquettes qui ne suivent pas le flux utilisateur ou qui ne mènent pas à la victoire.

L'ingénieur de test n'agit pas nécessairement en tant que responsable de l'assurance qualité ici, mais contribue toujours en tant que membre de l'équipe. Il doit aider à identifier différents profils d'utilisateurs et différentes manières dont l'application sera utilisée (c'est-à-dire, personas). La chose la plus importante pour l'ingénieur de test dans cette phase est encore une question de compréhension : saisir la fonctionnalité dans son ensemble plutôt que les éléments individuels des tickets.

#### Étape 3 : Tickets

Les tickets logiciels constituent la majeure partie du sprint. Cela pourrait potentiellement avoir lieu du jour 1 au jour 10. Les tickets rendent la fonctionnalité beaucoup plus claire (à environ 60 %).

Alors que les ingénieurs logiciels travaillent sur la fonctionnalité et résolvent les tickets, les ingénieurs de test construisent de petits tests pour s'assurer que la fonctionnalité sera construite correctement. Les tickets rendent la fonctionnalité plus concrète. À mesure que la fonctionnalité devient plus certaine, les méthodes de test deviennent plus claires. L'ingénieur de test devrait également construire des pipelines pour permettre un retour plus rapide.

C'est beaucoup d'informations, donc je recommande que l'ingénieur de test commence par construire littéralement un test qui s'exécuterait après chaque commit ou toute modification. Je recommande de construire d'abord le scénario du chemin heureux, puis de passer aux tests plus détaillés.

Lorsque l'ingénieur de test aborde ces autres tests plus détaillés, il devrait également identifier d'autres chemins : Que se passe-t-il si l'utilisateur fait pivoter l'écran ? Que se passe-t-il s'ils annulent ? Que se passe-t-il s'ils ont une combinaison de fonctionnalités étrange ? Qu'en est-il des pannes critiques potentielles de la fonctionnalité (par exemple, s'assurer que la page se charge et éviter l'erreur redoutée 500, ou s'assurer que l'action sur la page web est enregistrée avec précision dans la base de données).

Certains de ces autres chemins seront fréquents, d'autres seront moins courants. L'ingénieur de test devrait prioriser ceux qu'il devrait tester. Je recommande d'évaluer en fonction de ces deux critères :

Quel est l'impact sur le chiffre d'affaires ou les métriques commerciales clés ? L'ingénieur de test devrait faciliter la tâche des utilisateurs pour qu'ils atteignent leur objectif. Par exemple, chez Flipp, nous voulons rendre cela aussi facile que possible pour les utilisateurs d'accéder à leur prospectus souhaité. Tout obstacle nuit à la qualité.

Cela affecte-t-il la rétention ? L'ingénieur de test doit s'assurer que l'application ne plante pas, ou que les utilisateurs ne quittent pas pour une raison non prévue. Ils devraient également envisager des moyens de ramener les utilisateurs ou de les encourager à rouvrir l'application.

La chose la plus importante pour les ingénieurs de test est qu'ils priorisent ce qui est trouvé, en fonction de leur définition de la victoire. Ils doivent également identifier les risques dans toute la fonctionnalité en fonction de l'utilisation, de l'impact et de la probabilité que ce scénario se produise. Combien de personnes le ticket influencera-t-il ? À quel point le problème est-il profond ? Si l'application échoue, sera-t-il difficile de récupérer ?

#### Étape 4 : Assurance qualité et test

L'assurance qualité et les tests ont lieu des jours 5 à 10 (jusqu'à la publication). La fonctionnalité devrait être claire à 90-100 % à ce stade.

À mesure que les tickets sont résolus, les ingénieurs de test devraient examiner leur stratégie, qu'ils ont développée dans les étapes précédentes, et commencer à exécuter leur plan. Ils travailleront avec les ingénieurs logiciels pour obtenir plus de clarté ou pour résoudre les bugs.

La chose la plus importante ici est que les ingénieurs de test s'assurent que les fonctionnalités liées à la victoire sont claires. Les éléments "agréables à avoir" ou "devraient faire" ne seront pas corrigés sauf s'il y a du temps supplémentaire.

#### Étape 5 : Publication/déploiement

La publication a lieu le dernier jour (hypothétique jour 10). Le travail de l'ingénieur de test doit garantir que la publication se déroule sans encombre. Avant la publication, ils devraient tester la fonctionnalité sur une réplique du système de production. Nous avons une liste de contrôle post-publication spécifique que nous utilisons pour garder les choses cohérentes. Je ne vous ennuyerai pas avec les détails.

Alors que la fonctionnalité est lancée, les ingénieurs de test devraient surveiller de près les données pour voir si elles sont dans un état sain et examiner les journaux de plantage. Nous sommes humains, donc nous manquons parfois des choses même après les tests. Il pourrait y avoir des événements que même les ingénieurs de test les plus prudents n'anticipent pas.

Une assurance qualité plus intelligente commence par la prise en compte des tests dès le début du processus de développement logiciel. Cela signifie intégrer les ingénieurs de test avec les ingénieurs logiciels dès le début du cycle de test et prendre en compte les scénarios et les possibilités dès le départ. Cela rendra le processus de développement plus intelligent et, surtout, conduira à un meilleur logiciel.

_Je suis Derwin, le directeur de l'ingénierie de test chez [Flipp](https://flipp.com/). J'ai publié une version partielle de cela sur [le blog Flipp](http://eng.flipp.com/). Si vous êtes intéressé à réinventer la manière dont les gens achètent des choses, consultez nos [offres d'emploi actuelles](https://corp.flipp.com/jobs)._