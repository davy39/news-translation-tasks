---
title: 'Comment écrire du code infaillible en Go : un workflow pour les serveurs qui
  ne peuvent pas échouer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T00:20:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-bulletproof-code-in-go-a-workflow-for-servers-that-cant-fail-10a14a765f22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rATDejNGIZtqzLtB-LhJEQ.jpeg
tags:
- name: golang
  slug: golang
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Testing
  slug: testing
seo_title: 'Comment écrire du code infaillible en Go : un workflow pour les serveurs
  qui ne peuvent pas échouer'
seo_desc: 'By Tal Kol

  From time to time you may find yourself facing a daunting task: building a server
  that really isn’t allowed to fail, a project where the cost of error is extraordinarily
  high. What is the methodology for approaching such a task?

  Does your ...'
---

Par Tal Kol

De temps en temps, vous pouvez vous retrouver face à une tâche intimidante : construire un serveur qui n'a vraiment pas le droit d'échouer, un projet où le coût de l'erreur est extrêmement élevé. Quelle est la méthodologie pour aborder une telle tâche ?

### Votre serveur a-t-il vraiment besoin d'être infaillible ?

Avant de plonger dans ce workflow excessif, vous devriez vous demander — mon serveur a-t-il *vraiment* besoin d'être infaillible ? Il y a beaucoup de travail supplémentaire impliqué dans la préparation au pire, et ce n'est pas toujours utile.

Si le coût de l'erreur n'est pas extrêmement élevé, une approche parfaitement valable est de faire un effort raisonnable pour que les choses fonctionnent, et si votre serveur tombe en panne, il suffit de gérer le problème. Les outils de surveillance d'aujourd'hui et les workflows modernes de livraison continue nous permettent de repérer les problèmes en production rapidement et de les corriger presque immédiatement. Pour de nombreux cas, cela est suffisant.

Dans le projet sur lequel je travaille aujourd'hui, ce n'est pas le cas. Je travaille sur la mise en œuvre d'une [blockchain](https://www.orbs.com/) — une infrastructure de serveur distribuée pour exécuter du code de manière sécurisée sous consensus dans un environnement de faible confiance. L'une des applications de cette technologie est les monnaies numériques. C'est un exemple classique où le coût de l'erreur est littéralement élevé. Nous voulons naturellement que sa mise en œuvre soit aussi infaillible que possible.

Il existe d'autres cas, même lorsque l'on ne traite pas de monnaies, où un code infaillible a du sens. Le coût de la maintenance explose rapidement pour une base de code qui échoue fréquemment. Être capable d'identifier les problèmes plus tôt dans le cycle de développement, lorsque le coût de leur correction est encore faible, a de bonnes chances de rentabiliser l'investissement initial dans une méthodologie infaillible.

### Le TDD est-il la réponse magique ?

Le [Développement Piloté par les Tests](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) est souvent salué comme la solution miracle contre le code défectueux. Il s'agit d'une méthodologie de développement puriste où le nouveau code n'est pas ajouté à moins qu'il ne satisfasse un test échoué. Ce processus garantit une couverture de test de 100 pour cent et donne souvent l'illusion que votre code est testé contre tous les scénarios possibles.

Ce n'est pas le cas. Le TDD est une excellente méthodologie qui fonctionne bien pour certains, mais en soi, elle n'est toujours pas suffisante. Pire encore, le TDD instille une fausse confiance dans le code et peut rendre les développeurs paresseux lorsqu'il s'agit de considérer des cas limites paranoïaques. Je montrerai un bon exemple de cela plus tard.

### Les tests sont importants — ils sont la clé

Peu importe si vous écrivez les tests avant ou après, en utilisant une technique comme le TDD ou non. Tout ce qui compte, c'est que vous ayez des tests. Les tests sont la meilleure ligne de défense pour protéger votre code contre les pannes en production.

Puisque nous allons exécuter notre suite de tests complète *très* fréquemment — après chaque nouvelle ligne de code si possible — les tests doivent être automatisés. Aucune partie de notre confiance dans notre code ne peut résulter d'un processus de QA manuel. Les humains font des erreurs. L'attention humaine aux détails se détériore après avoir effectué la même tâche ennuyeuse cent fois de suite.

Les tests doivent être rapides. Extrêmement rapides.

Si une suite de tests prend plus de quelques secondes à s'exécuter, les développeurs risquent de devenir paresseux, poussant du code sans l'exécuter. C'est l'une des grandes choses à propos de Go — il possède l'une des chaînes d'outils les plus rapides. Il compile, reconstruit et teste en quelques secondes.

Les tests sont également des facilitateurs importants pour les projets open-source. Les blockchains, par exemple, sont presque religieusement open-source. La base de code doit être ouverte pour établir la confiance — s'exposer à l'audit et créer une atmosphère décentralisée où aucune entité gouvernante unique ne contrôle le projet.

Il est déraisonnable de s'attendre à des contributions externes massives dans un projet open-source sans une suite de tests approfondie. Les contributeurs externes ont besoin d'un moyen rapide de vérifier si leur contribution casse un comportement existant. En fait, l'ensemble de la suite de tests doit s'exécuter automatiquement sur chaque pull request et échouer automatiquement si la PR a cassé quelque chose.

Une couverture de test complète est une métrique trompeuse, mais elle est importante. Il peut sembler excessif d'atteindre 100 % de couverture, mais lorsque l'on y pense, il est déraisonnable de déployer du code en production qui n'a jamais été exécuté auparavant.

Une couverture de test complète ne signifie pas nécessairement que nous avons assez de tests et ne signifie pas que nos tests sont significatifs. Ce qui est certain, c'est que si nous n'avons pas 100 % de couverture, nous n'en avons pas assez pour nous considérer infaillibles, puisque des parties de notre code n'ont jamais été testées.

Néanmoins, il existe une chose comme trop de tests. Idéalement, chaque bug que nous rencontrons devrait casser un seul test. Si nous avons des tests redondants — différents tests qui vérifient la même chose — modifier le code existant et casser le comportement existant dans le processus entraînera trop de travail supplémentaire pour corriger les tests échoués.

### Pourquoi Go est-il un excellent choix pour un code infaillible ?

**Go est typé statiquement.** Les types fournissent un contrat entre différentes parties de code qui s'exécutent ensemble. Sans vérification de type automatique pendant la compilation, si nous voulions adhérer à nos règles de couverture strictes, nous devrions implémenter ces tests de contrat nous-mêmes. C'est le cas avec des environnements comme Node.js et JavaScript. Écrire des tests de contrat complets manuellement est beaucoup de travail supplémentaire que nous préférons éviter.

**Go est simple et dogmatique.** Go est connu pour être dépouillé de nombreuses fonctionnalités traditionnelles des langages comme l'héritage OOP classique. La complexité est le pire ennemi du code infaillible. Les problèmes ont tendance à surgir dans les coutures. Bien que le cas commun soit facile à tester, c'est le cas limite étrange auquel vous n'avez pas pensé qui finira par vous atteindre.

Le dogme est également utile dans ce sens. Il n'y a souvent qu'une seule façon de faire quelque chose en Go. Cela peut inhiber l'esprit libre de l'homme, mais lorsqu'il n'y a qu'une seule façon de faire quelque chose, il est plus difficile de se tromper sur cette seule chose.

**Go est concis mais expressif.** Le code lisible est plus facile à réviser et à auditer. Si le code est trop verbeux, son objectif principal peut être noyé par le bruit du code standard. Si le code est trop concis, il devient difficile à suivre et à comprendre.

Go trouve un bon équilibre entre les deux. Il n'y a pas beaucoup de code standard comme en Java ou C++, mais le langage est encore très explicite et verbeux dans des domaines comme la gestion des erreurs — ce qui le rend facile à vérifier que vous avez vérifié chaque route possible.

**Go a des chemins clairs d'erreur et de récupération.** Traiter les erreurs en temps d'exécution avec grâce est une pierre angulaire pour un code infaillible. Go a une convention stricte de la manière dont les erreurs sont retournées et propagées. Les environnements comme Node.js — où plusieurs types de flux de contrôle comme les callbacks, les promesses et l'async sont mélangés ensemble — résultent souvent en des fuites comme des [rejets de promesses non gérés](http://thecodebarbarian.com/unhandled-promise-rejections-in-node.js.html). Récupérer de ces erreurs est presque [impossible](https://shapeshed.com/uncaught-exceptions-in-node/).

**Go a une bibliothèque standard extensive.** Les dépendances ajoutent des risques, surtout lorsqu'elles proviennent de sources qui ne sont pas nécessairement bien maintenues. Lorsque vous déployez votre serveur, vous déployez toutes vos dépendances avec lui. Vous êtes responsable de leurs dysfonctionnements également. Les environnements débordant de dépendances fragmentées, comme Node.js, sont plus difficiles à maintenir infaillibles.

Cela est également risqué d'un point de vue sécurité, car vous êtes aussi vulnérable que votre [dépendance la plus faible](https://thenewstack.io/npm-password-resets-show-developers-need-better-security-practices/). La bibliothèque standard extensive de Go est bien maintenue et réduit la dépendance aux dépendances externes.

**La vitesse de développement reste rapide.** Le principal attrait des environnements comme Node.js est un cycle de développement extrêmement rapide. Le code prend simplement moins de temps à écrire et vous devenez plus productif.

Go préserve ces avantages assez bien. La chaîne d'outils de construction est assez rapide pour rendre les retours immédiats. Le temps de compilation est négligeable, et le code semble s'exécuter comme s'il était interprété. Le langage a assez d'abstractions comme le garbage collection pour concentrer les efforts d'ingénierie sur les fonctionnalités principales.

### Jouons avec un exemple fonctionnel

Maintenant, les introductions étant terminées, il est temps de plonger dans du code. Nous avons besoin d'un exemple suffisamment simple pour que nous puissions nous concentrer sur la méthodologie, mais suffisamment compliqué pour avoir du contenu. Je trouve qu'il est plus facile de prendre quelque chose de mon quotidien, alors construisons un serveur qui traite des transactions similaires à des monnaies. Les utilisateurs pourront vérifier le solde d'un compte. Les utilisateurs pourront également transférer des fonds d'un compte à un autre.

Nous garderons les choses très simples. Notre système n'aura qu'un seul serveur. Nous ne allons pas non plus traiter de l'authentification des utilisateurs ou de la cryptographie. Ce sont des fonctionnalités produit, alors que nous voulons nous concentrer sur la construction de la fondation logicielle infaillible.

### Décomposer la complexité en parties gérables

La complexité est le pire ennemi du code infaillible. L'une des meilleures façons de traiter la complexité est de *diviser et conquérir* — diviser le problème en problèmes plus petits et résoudre chacun séparément. Comment diviser ? Nous suivrons le principe de [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns). Chaque partie doit traiter une seule préoccupation.

Cela va de pair avec l'architecture populaire des [microservices](https://www.martinfowler.com/articles/microservices.html). Notre serveur sera composé de services. Chaque service aura une responsabilité claire et une interface bien définie pour la communication avec les autres services.

Une fois que nous avons structuré notre serveur de cette manière, nous serons libres de décider comment chaque service s'exécute. Nous pouvons exécuter tous les services ensemble dans le même processus, faire de chaque service son propre serveur séparé et communiquer via RPC, ou diviser les services pour qu'ils s'exécutent sur différentes machines.

Puisque nous commençons tout juste, nous garderons les choses simples — tous les services partageront le même processus et communiqueront directement en tant que bibliothèques. Nous pourrons changer cette décision facilement à l'avenir.

Alors, quels services devrions-nous avoir ? Notre serveur est un peu trop simple pour être divisé, mais pour démontrer ce principe, nous le ferons quand même. Nous devons répondre aux requêtes HTTP des clients pour vérifier les soldes et effectuer des transactions. Un service peut traiter l'interface HTTP client — nous l'appellerons _PublicApi_. Un autre service possédera l'état — le grand livre de tous les soldes — nous l'appellerons donc _StateStorage_. Le troisième service reliera les deux et implémentera notre logique métier du « contrat » pour changer les soldes. Puisque les blockchains permettent généralement à ces contrats d'être déployés par les développeurs d'applications, le troisième service sera chargé de les exécuter — nous l'appellerons _VirtualMachine_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M0eFouGRL_3r5DVB9ZfjOA.png)

Nous placerons le code des services dans notre projet sous `/services/publicapi`, `/services/virtualmachine` et `/services/statestorage`.

### Définir clairement les limites des services

Lors de l'implémentation des services, nous voudrons pouvoir travailler sur chacun séparément. Possiblement même assigner différents services à différents développeurs. Puisque les services dépendent les uns des autres et que nous allons paralléliser le travail sur leur implémentation, nous devrons commencer par définir des interfaces claires entre eux. En utilisant cette interface, nous pourrons tester un service individuellement et simuler tout le reste.

Comment pouvons-nous définir l'interface ? Une option est de la documenter, mais la documentation tend à devenir obsolète et désynchronisée avec le code. Nous pourrions utiliser les déclarations d'_interface_ de Go. Cela a du sens, mais il est préférable de définir l'interface de manière agnostique au langage. Notre serveur n'est pas limité à Go uniquement. Nous pourrions décider plus tard de réimplémenter l'un des services dans un autre langage plus approprié à ses exigences.

Une approche consiste à utiliser [protobuf](https://developers.google.com/protocol-buffers/) — une syntaxe simple et agnostique au langage de Google pour définir des messages et des points de terminaison de service.

Commençons par _StateStorage_. Nous structurerons l'état comme un magasin clé-valeur :

Bien que _PublicApi_ soit accessible via HTTP client, il est toujours une bonne pratique de lui donner une interface claire de la même manière :

Cela nécessitera de définir les structures de données _Transaction_ et _Address_ :

Nous placerons les définitions `.proto` des services dans notre projet sous `/types/services` et les structures de données générales sous `/types/protocol`. Une fois les définitions prêtes, elles peuvent être [compilées](https://developers.google.com/protocol-buffers/docs/reference/go-generated) en code Go. L'avantage de cette approche est que le code qui ne respecte pas le contrat ne se compilera tout simplement pas. Les méthodes alternatives nous obligeraient à écrire des tests de contrat explicitement.

Les définitions complètes, les fichiers Go générés et les instructions de compilation sont disponibles [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/types). Félicitations à [Square Engineering](https://www.freecodecamp.org/news/how-to-write-bulletproof-code-in-go-a-workflow-for-servers-that-cant-fail-10a14a765f22/undefined) pour avoir créé [goprotowrap](https://github.com/square/goprotowrap).

Notez que nous n'intégrons pas encore de couche de transport RPC, et les appels entre services seront actuellement des appels de bibliothèque réguliers. Lorsque nous serons prêts à diviser les services en différents serveurs, nous pourrons ajouter une couche de transport comme [gRPC](https://grpc.io/docs/tutorials/basic/go.html).

### Les types de tests dans notre projet

Puisque les tests sont la clé du code infaillible, discutons d'abord des types de tests que nous allons écrire :

#### **Tests unitaires**

C'est la base de la [pyramide de test](https://blog.primehammer.com/test-pyramid/). Nous testerons chaque unité en isolation. Qu'est-ce qu'une unité ? En Go, nous pouvons définir une unité comme étant chaque fichier dans un package. Si nous avons `/services/publicapi/handlers.go`, nous placerons son test unitaire dans le même package sous `/services/publicapi/handlers_test.go`.

Il est préférable de placer les tests unitaires dans le même package que le code testé afin que les tests aient accès aux variables et fonctions non exportées.

#### **Tests de service / d'intégration / de composant**

Le type suivant de tests a plusieurs noms qui font tous référence à la même chose — prendre plusieurs unités et les tester ensemble. C'est un niveau au-dessus de la pyramide. Dans notre cas, nous nous concentrerons sur un service entier. Ces tests définissent les spécifications pour un service. Pour le service _StateStorage_ par exemple, nous les placerons dans `/services/statestorage/spec`.

Il est préférable de placer ces tests dans un package différent de celui du code testé pour imposer l'accès uniquement via les interfaces exportées.

#### **Tests de bout en bout**

C'est le sommet de la pyramide de test, où nous testons notre système entier avec tous les services combinés. Ces tests définissent les spécifications de bout en bout pour le système, nous les placerons donc dans notre projet sous `/e2e/spec`.

Ces tests doivent également être placés dans un package différent de celui du code testé pour imposer l'accès uniquement via les interfaces exportées.

Quels tests devons-nous écrire en premier ? Devons-nous commencer par la base et remonter ? Ou aller de haut en bas ? Les deux approches sont valides. L'avantage de l'approche de haut en bas est pour la construction des spécifications. Il est généralement plus facile de raisonner sur les spécifications pour l'ensemble du système en premier. Même si nous divisons notre système en services de la mauvaise manière, la spécification du système resterait la même. Cela nous aiderait également à comprendre cela.

L'inconvénient de commencer par le haut est que nos tests de bout en bout seront les derniers à réussir (uniquement après que l'ensemble du système ait été implémenté). Cela signifie qu'ils resteront en échec pendant longtemps.

### Tests de bout en bout

Avant d'écrire des tests, nous devons considérer si nous allons tout écrire à partir de zéro ou utiliser un framework. Compter sur des frameworks pour les dépendances de développement est moins dangereux que de compter sur des frameworks pour le code de production. Dans notre cas, puisque la bibliothèque standard de Go n'a pas un bon support pour le [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) et que ce format est excellent pour définir des spécifications, nous opterons pour un framework.

Il existe de nombreux excellents candidats comme [GoConvey](https://github.com/smartystreets/goconvey) et [Ginkgo](https://github.com/onsi/ginkgo). Ma préférence personnelle est [Ginkgo](http://onsi.github.io/ginkgo/) avec [Gomega](http://onsi.github.io/gomega/) (noms terribles, mais que pouvez-vous faire) qui utilisent une syntaxe comme `Describe()` et `It()`.

À quoi ressemble un test ? Vérification du solde de l'utilisateur :

Puisque notre serveur fournit une interface HTTP publique au monde, nous accédons à cette API web en utilisant [http.Get](https://golang.org/pkg/net/http/). Et pour effectuer une transaction ?

Le test est très descriptif et peut même remplacer la documentation. Comme vous pouvez le voir ci-dessus, nous permettons aux comptes d'atteindre un solde négatif. C'est un choix de produit. Si cela n'était pas autorisé, le test refléterait cela.

Le fichier de test complet est disponible [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/e2e/spec).

### Tests d'intégration de service / de composant

Maintenant que nous avons terminé avec les tests de bout en bout, nous descendons la pyramide et implémentons les tests de service. Cela est fait pour chaque service séparément. Choisissons un service qui a une dépendance à un autre service, car ce cas est plus intéressant.

Nous commencerons par _VirtualMachine_. L'interface protobuf pour ce service est disponible [ici](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/types/services/virtualmachine.proto). Parce que _VirtualMachine_ repose sur le service _StateStorage_ et fait des appels à celui-ci, nous allons devoir [simuler](https://en.wikipedia.org/wiki/Mock_object) _StateStorage_ afin de tester _VirtualMachine_ en isolation. L'objet simulé nous permettra de contrôler les réponses de _StateStorage_ pendant le test.

Comment pouvons-nous implémenter des objets simulés en Go ? Nous pouvons simplement créer une implémentation de stub basique, mais l'utilisation d'une bibliothèque de simulation nous fournira également des assertions utiles pendant le test. Ma préférence est [go-mock](https://github.com/maraino/go-mock).

Nous placerons la simulation pour _StateStorage_ dans `/services/statestorage/mock.go`. Il est préférable de placer les simulations dans le même package que le code simulé pour fournir l'accès aux variables et fonctions non exportées. La simulation est pour l'instant principalement du code standard, mais à mesure que nos services deviennent plus compliqués, nous pourrions nous retrouver à ajouter une certaine logique ici. Voici la simulation :

Si vous attribuez différents services à différents développeurs, il est logique d'implémenter d'abord les simulations et de les partager entre l'équipe.

Revenons à l'écriture de notre test de service pour _VirtualMachine_. Quel scénario devons-nous tester exactement ici ? Il est préférable de suivre l'[interface](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/types/services/virtualmachine.proto) pour le service et concevoir des tests pour chaque point de terminaison. Nous implémenterons le test pour le point de terminaison `CallContract()` avec l'argument _method_ de `"GetBalance"` en premier :

Remarquez que le service que nous testons, _VirtualMachine_, reçoit un pointeur vers sa dépendance _StateStorage_ dans sa méthode `Start()` via une simple injection de dépendance. C'est là que nous passons l'instance simulée. Remarquez également à la ligne 23 où nous instruisons la simulation sur la manière de répondre lorsqu'elle est accédée. Lorsque sa méthode `ReadKey` est appelée, elle doit retourner la valeur `100`. Nous vérifions ensuite qu'elle a bien été appelée exactement une fois à la ligne 28.

Ces tests deviennent les spécifications pour le service. La suite complète pour le service _VirtualMachine_ est disponible [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/spec). Les suites pour les autres services sont disponibles [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/statestorage/spec) et [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/publicapi/spec).

### Implémentons enfin une unité

L'implémentation du contrat pour la _méthode_ `"GetBalance"` est un peu trop simple, alors passons à l'implémentation légèrement plus compliquée pour la _méthode_ `"Transfer"`. Le contrat de transfert doit lire les soldes de l'expéditeur et du destinataire, calculer leurs nouveaux soldes et les réécrire dans l'état. Le test d'intégration de service pour celui-ci est très similaire à celui que nous venons d'implémenter :

Nous allons enfin nous mettre au travail et créer une unité appelée `processor.go` qui contient l'implémentation réelle du contrat. Voici ce que donne notre implémentation initiale :

Cela satisfait le test d'intégration de service, mais le test d'intégration ne contient qu'un scénario de cas commun. Qu'en est-il des cas limites et des échecs potentiels ? Comme vous pouvez le voir, l'un des appels que nous faisons à _StateStorage_ peut échouer. Si nous visons une couverture à 100 %, nous devons vérifier tous ces cas. Un test unitaire serait un excellent endroit pour le faire.

Puisque nous allons devoir exécuter la fonction plusieurs fois avec différentes entrées et paramètres de simulation pour atteindre tous les flux, un [test piloté par tableau](https://github.com/golang/go/wiki/TableDrivenTests) rendrait ce processus un peu plus efficace. La convention en Go est d'éviter les frameworks sophistiqués dans les tests unitaires. Nous pouvons abandonner [Ginkgo](http://onsi.github.io/ginkgo), mais nous devrions probablement garder [Gomega](http://onsi.github.io/gomega/) pour que nos comparateurs ressemblent à nos tests précédents. Voici le test :

Si vous êtes déconcerté par le symbole "Ω", ne vous inquiétez pas, il s'agit simplement d'un nom de variable régulier (contenant un pointeur vers [Gomega](http://onsi.github.io/gomega/)). Vous êtes libre de le renommer en ce que vous voulez.

Pour gagner du temps, nous n'avons pas montré la méthodologie stricte du TDD où une nouvelle ligne de code ne serait écrite que pour résoudre un test échoué. En utilisant cette méthodologie, le test unitaire et l'implémentation pour `processTransfer()` seraient implémentés sur plusieurs itérations.

La suite complète de tests unitaires dans le service _VirtualMachine_ est disponible [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine). Les tests unitaires pour les autres services sont disponibles [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/statestorage) et [ici](https://github.com/orbs-network/go-scaffold/tree/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/publicapi).

Nous avons atteint 100 % de couverture, nos tests de bout en bout réussissent, nos tests d'intégration de service réussissent et nos tests unitaires réussissent. Le code remplit ses exigences à la lettre et est minutieusement testé.

Cela signifie-t-il que tout fonctionne ? Malheureusement non. Nous avons encore plusieurs bugs désagréables qui se cachent en pleine vue dans notre implémentation simple.

### L'importance des tests de stress

Tous nos tests jusqu'à présent ont testé une seule requête traitée à la fois. Qu'en est-il des problèmes de synchronisation ? Chaque requête HTTP en Go est traitée dans sa propre _goroutine_. Puisque ces goroutines s'exécutent simultanément, potentiellement sur différents threads du système d'exploitation sur différents cœurs de CPU, nous sommes confrontés à des problèmes de synchronisation. Ce sont des bugs très désagréables qui ne sont pas faciles à traquer.

L'une des approches pour trouver les problèmes de synchronisation consiste à stresser le système avec de nombreuses requêtes en parallèle et à s'assurer que tout fonctionne encore. Cela devrait être un test de bout en bout car nous voulons tester les problèmes de synchronisation dans l'ensemble de notre système avec tous les services. Nous placerons les tests de stress dans notre projet sous `/e2e/stress`.

Voici à quoi ressemble un test de stress :

Remarquez que le test de stress inclut des données aléatoires. Il est recommandé d'utiliser une graine constante (voir ligne 39) pour rendre le test déterministe. Exécuter un scénario différent à chaque fois que nous exécutons nos tests n'est pas une bonne idée. La fragilité des tests qui réussissent parfois et échouent parfois réduit la confiance des développeurs dans la suite.

La partie délicate des tests de stress sur HTTP est que la plupart des machines ont du mal à simuler des milliers d'utilisateurs simultanés et à ouvrir des milliers de connexions TCP simultanées (vous verrez des échecs étranges comme "descripteurs de fichiers maximum" ou "connexion réinitialisée par le pair"). Le code ci-dessus tente de gérer cela avec grâce en limitant les connexions simultanées à des lots de 200 et en utilisant les paramètres de _Transport_ de _IdleConnection_ pour recycler les sessions TCP entre les lots. Si ce test est instable sur votre machine, essayez de réduire la taille du lot à 100.

Oh non… le test échoue :

Que se passe-t-il ici ? _StateStorage_ est implémenté comme une simple carte en mémoire. Il semble que nous essayons d'écrire dans cette carte en parallèle à partir de différents threads. Il peut sembler au premier abord que nous devrions simplement remplacer la carte régulière par la carte thread-safe `[sync.map](https://golang.org/pkg/sync/#Map)` mais notre problème est un peu plus profond.

Jetez un coup d'œil à l'implémentation de `[processTransfer()](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/processor.go)`. Elle lit deux fois à partir de l'état puis écrit deux fois. L'ensemble des lectures et des écritures n'est pas une transaction atomique, donc si un autre thread modifie l'état après qu'un thread a lu à partir de celui-ci, nous allons avoir une corruption des données. La solution est de s'assurer qu'une seule instance de `processTransfer()` peut s'exécuter simultanément — vous pouvez le voir [ici](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/processor.go#L6).

Essayons d'exécuter à nouveau le test de stress. Oh non, un autre échec !

Celui-ci nécessite un peu plus de débogage pour comprendre. Il semble que cela se produise lorsqu'un utilisateur essaie de transférer un montant à lui-même (le même utilisateur est à la fois l'expéditeur et le destinataire). En regardant l'implémentation, il est facile de voir [pourquoi cela se produit](https://github.com/orbs-network/go-scaffold/blob/716806bd41641278b060612387a752944c5e7445/services/virtualmachine/processor.go#L18).

Celui-ci est un peu troublant. Nous avons suivi un workflow de type TDD et nous avons encore rencontré un bug de logique métier difficile. Comment cela peut-il être ? Notre code n'est-il pas testé contre tous les scénarios avec une couverture de 100 % ? Eh bien… ce bug est le résultat d'une exigence de produit défectueuse, et non d'une implémentation défectueuse. Les exigences pour `processTransfer()` auraient dû clairement indiquer que si un utilisateur transfère un montant à lui-même, rien ne se passe.

Lorsque nous découvrons un bug de logique métier, nous devons toujours le reproduire d'abord dans nos tests unitaires. Il est très facile d'[ajouter ce cas](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/processor_test.go#L26) à notre test piloté par tableau précédent. La correction est également simple — vous pouvez la voir [ici](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/processor.go#L12).

### Sommes-nous enfin libres ?

Après avoir ajouté les tests de stress et nous être assurés que tout passe, notre système fonctionne-t-il enfin comme prévu ? Est-il enfin infaillible ?

Malheureusement non.

Nous avons encore quelques bugs désagréables que même le test de stress n'a pas découverts. Notre fonction "simple" `processTransfer()` est toujours à risque. Considérez ce qui se passe si nous atteignons jamais [cette ligne](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/services/virtualmachine/processor.go#L25). La première écriture dans l'état a réussi mais la seconde échoue. Nous sommes sur le point de retourner une erreur, mais nous avons déjà corrompu notre état en y écrivant des données à moitié cuites. Si nous allons retourner une erreur, nous devrons annuler la première écriture.

Cela est un peu plus compliqué à corriger. La meilleure solution est probablement de changer [notre interface](https://github.com/orbs-network/go-scaffold/blob/f1cd4f35d697a6946b2e45616f4817dc4007bb0f/types/services/statestorage.proto#L6) entièrement. Au lieu d'avoir un point de terminaison dans _StateStorage_ nommé `WriteKey` que nous appelons deux fois, nous devrions probablement le renommer en `WriteKeys` — un point de terminaison que nous appellerons *une fois* pour écrire les deux clés ensemble dans une seule transaction.

Il y a une leçon plus grande ici : une suite de tests méthodique n'est pas suffisante. Traiter les bugs complexes nécessite une pensée critique et une créativité paranoïaque de la part des développeurs. Il est recommandé de faire examiner votre code par quelqu'un d'autre et de réaliser des revues de code dans votre équipe. Encore mieux, l'open source de votre code et l'encouragement de la communauté à l'auditer est l'une des meilleures façons de rendre votre code plus infaillible.

Tout le code de cet article est disponible sur Github en tant que dépôt d'exemple unique. Vous êtes les bienvenus pour utiliser ce projet comme kit de démarrage pour votre prochain serveur. Vous êtes également les bienvenus pour examiner le dépôt et découvrir plus de bugs et le rendre plus infaillible. Soyez créativement paranoïaque !

[**orbs-network/go-scaffold**](https://github.com/orbs-network/go-scaffold)
[_go-scaffold - Projet de démarrage en Go pour un serveur basé sur des microservices avec des tests approfondis_github.com](https://github.com/orbs-network/go-scaffold)

**_Tal est un fondateur chez Orbs.com — une infrastructure de blockchain publique pour des applications grand public à grande échelle avec des millions d'utilisateurs. Pour en savoir plus et lire les livres blancs d'Orbs [cliquez ici](https://orbs.com/white-papers). [Suivez sur [Telegram](https://t.me/orbs_network), [Twitter](https://twitter.com/orbs_network), [Reddit](https://www.reddit.com/r/ORBS_Network/)]_**

**_Note : si vous êtes intéressé par la blockchain — venez contribuer ! Orbs est un projet entièrement open source où chacun peut participer._**