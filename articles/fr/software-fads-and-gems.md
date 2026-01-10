---
title: 'Comment regarder en arrière peut nous aider à avancer : une rétrospective
  sur les pépites et les modes du logiciel'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-30T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/software-fads-and-gems
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/hidden-gem.jpg
tags:
- name: asyncio
  slug: asyncio
- name: Bitcoin
  slug: bitcoin
- name: formats
  slug: formats
- name: NoSQL
  slug: nosql
- name: Python
  slug: python
seo_title: 'Comment regarder en arrière peut nous aider à avancer : une rétrospective
  sur les pépites et les modes du logiciel'
seo_desc: 'By Pakal de Bonchamp

  Maybe one of the most important qualities of a developer is the ability to pick
  the right tool for the right job, without hopping onto bandwagons or reinventing
  the wheel. This might require a bit of technology analysis, but even...'
---

Par Pakal de Bonchamp

Peut-être l'une des qualités les plus importantes d'un développeur est la capacité à choisir le bon outil pour le bon travail, sans sauter sur des modes ou [réinventer la roue](https://en.wikipedia.org/wiki/Not_invented_here). Cela peut nécessiter un peu d'analyse technologique, mais surtout, une touche de pensée critique.

Voici un examen de quelques tendances exagérées et de quelques aspects sous-estimés, dans différents domaines du merveilleux monde de l'informatique : **les bases de données, l'asynchronicité, la cryptomonnaie et les formats de données**. Je ne toucherai pas au sujet des services web REST, sur lequel j'ai déjà [ranté longuement](https://www.freecodecamp.org/news/rest-is-the-new-soap-97ff6c09896d/).

_Comme d'habitude, vos retours sont les bienvenus si des erreurs factuelles se sont glissées dans cet article (pas entièrement impartial)._

## Bases de données : NoSQL et ZODB

Peu de moments, dans l'histoire de l'informatique, ont été aussi ironiquement éclairés que l'arrivée des bases de données No-SQL, vers 2009. Une vague déferlante a frappé les rives du développement backend et de l'administration système : les bases de données SQL étaient trop rigides, trop lentes, trop difficiles à répliquer.

Ainsi, les nouveaux projets les ont massivement abandonnées au profit de magasins clé-valeur comme Redis, de bases de données orientées documents comme MongoDB/CouchDB, ou de bases de données orientées graphe comme Neo4j. Et nous devons reconnaître une chose : ces nouvelles bases de données brillaient dans les benchmarks ; elles brillaient autant que... n'importe quelle base de données SQL abandonnant toutes ses [contraintes ACID](https://www.geeksforgeeks.org/acid-properties-in-dbms/) et la flexibilité de son langage de requête.

Mais l'horizon était sombre pour de nombreux programmeurs. Ils ont appris, à leurs dépens, que la persistance des données n'était pas une préoccupation mineure. Et qu'ils devaient, par exemple, activer explicitement les "Write Concerns" dans MongoDB, pour s'assurer que les données ne se perdent pas avant d'atteindre le disque.

Ils ont appris que la "cohérence éventuelle" était un joli mot pour "incohérence temporaire", ouvrant la porte à des bugs silencieux, désagréables et difficiles à reproduire en production. Et que les transactions - et leur verrouillage implicite - étaient des fonctionnalités précieuses, et que les imiter à la main, avec des drapeaux maladroits fourrés dans des documents, était tout sauf facile et robuste.

Et ils ont appris que les schémas de données, et l'intégrité référentielle, étaient plus que bienvenus pour empêcher les bases de données de devenir des tas d'objets incohérents. Et que le manque de capacités d'indexation avancées (sur plusieurs clés, sur des champs de documents profonds) dans les magasins clé-valeur pouvait devenir assez embarrassant.

Ainsi, les gens ont commencé à réinventer les fonctionnalités SQL sur le dessus des bases de données NoSQL, en imitant les schémas de données, les clés étrangères, l'agrégation avancée, dans des bibliothèques "ORM" spécifiques au langage (mongoengine, mongoid, mongomapper...). Dans ce contexte, cet acronyme "Object-Relational Mapper" aurait dû, à lui seul, être un indice que quelque chose avait dérapé.

Il y avait quelque chose de surréaliste à voir des bases de données NoSQL, qui étaient conçues pour des cas d'utilisation spécifiques (données hautement répliquées ou hétérogènes, [collections de taille limitée](https://docs.mongodb.com/manual/core/capped-collections/) ou [TTLs](https://docs.mongodb.com/manual/tutorial/expire-data/), systèmes pub/sub...), être utilisées simplement pour stocker un tas d'objets de même forme dans une seule instance de serveur.

Une base de données SQL standard aurait parfaitement fait le travail, et offert beaucoup plus d'options et de plugins (différents moteurs de stockage, scripts Percona toolkit, IDEs comme HeidiSql ou Mysql Workbench, processus de migration de schéma de base de données intégrés dans les frameworks web...). Même si cela signifiait fourrer des données non structurées supplémentaires dans un champ Text sérialisé (ou, de nos jours, des [champs Json dédiés de PostgreSQL](https://www.postgresql.org/docs/current/datatype-json.html)).

Avec le temps, les bases de données NoSQL elles-mêmes se sont beaucoup améliorées, entre autres en empruntant des fonctionnalités au monde SQL. Mais réinventer SQL n'est pas une tâche facile. Les bases de données relationnelles traitent de l'analyse du langage de requête, des jeux de caractères et des collations, de l'agrégation et de la conversion des données, des transactions et des niveaux d'isolation, des vues et des caches de requêtes, des déclencheurs, des procédures embarquées, des [SIG](http://wiki.gis.com/wiki/index.php/Geographic_information_system), des permissions fines, de la réplication et du clustering... des fonctionnalités complexes et sensibles, pilotées par des centaines de paramètres répartis sur plusieurs niveaux (par base de données, par table, par connexion).

Ainsi, malgré leurs grands progrès (transactions multi-documents, meilleure agrégation de données, fonctions JavaScript stockées, stockage pluggable, contrôle d'accès basé sur les rôles dans MongoDB), les bases de données NoSQL ont encore du mal à rivaliser avec les principales bases de données SQL, purement en termes de fonctionnalités.

Heureusement, la plupart des projets n'ont besoin que d'un petit sous-ensemble de ces fonctionnalités de base de données SQL : quelques validations de schéma, quelques index corrects, et les affaires peuvent démarrer ; donc pour les équipes manquant d'expertise SQL, la simplicité relative de nombreuses bases de données NoSQL peut effectivement être, pour être honnête, un facteur pertinent.

La vague semble s'être estompée depuis, et les projets semblent plus enclins à combiner différentes bases de données selon les besoins réels. Ils séparent ainsi les comptes utilisateurs, les files d'attente de tâches et les caches similaires, les données de journalisation et de statistiques... chacun dans le stockage le plus pertinent.

Toutes ces bases de données NoSQL citées, et leurs innombrables alternatives, brillent dans leurs cas d'utilisation prévus. Mais j'aimerais mentionner une pépite trop peu connue et trop peu utilisée de l'écosystème Python. Avez-vous déjà voulu persister vos données d'une manière vraiment, vraiment facile ? Alors je vous oriente vers le [ZODB](http://www.zodb.org/en/latest/). Vous l'ouvrez comme un dictionnaire, vous y poussez les données que vous voulez, vous validez la transaction, et vous êtes prêt à partir.

*Exemple d'une instance locale simple de ZODB :*

```python
from ZODB import FileStorage, DB
import transaction

storage = FileStorage.FileStorage('mydatabase.fs')
root = DB(storage).open().root()
print("ROOT:", root)
root['employees'] = ['Mary', 'Jo', 'Bob']
transaction.commit()
```

Les graphes de données sont gérés avec grâce (pas d'erreur de récursion), les objets sont chargés de manière paresseuse à l'accès, des types spéciaux d'"arbre de seaux" sont fournis pour parcourir d'énormes quantités de données tout en gardant la mémoire basse, et plusieurs backends de stockage existent, y compris [relstorage](https://relstorage.readthedocs.io/en/latest/install.html) qui exploite la puissance des bases de données SQL. Parfait, n'est-ce pas ?

D'accord, je mens, il y a quelques pièges. Il n'y a pas de système d'indexation intégré (il faut utiliser Zcatalog ou similaire à la place). L'utilisation de types "persistants" dédiés est fortement conseillée, pour détecter et persister automatiquement les mutations des objets. L'outil global est assez limité par rapport aux bases de données grand public. Et le modèle de concourance basé sur le "verrouillage optimiste" peut vous forcer, sous charge lourde, à réessayer une opération plusieurs fois jusqu'à ce qu'elle parvienne à être appliquée.

L'extrême intégration avec le langage Python a un inconvénient supplémentaire : si vous introduisez des changements cassants dans votre modèle de données, votre base de données pourrait ne plus se charger, vous devez donc gérer les migrations de schéma avec soin.

Mais le contexte est tout : ZODB n'est pas destiné à la persistance des données à long terme et interopérables, mais au stockage sans effort d'objets Python (possiblement très hétérogènes). Il peut rendre les scripts de longue durée capables de reprendre après une interruption, il peut stocker les données des joueurs de sessions de jeu en ligne... si vous voulez vraiment stocker des articles de blog ou des comptes personnels dans ZODB, vous feriez mieux de vous limiter aux types natifs de Python, et d'implémenter vos propres vérifications de cohérence. Mais quoi qu'il arrive, n'utilisez pas un [shelf stdlib](https://docs.python.org/3.7/library/shelve.html) très limité, si vous pouvez avoir un ZODB pratique sous la main pour stocker vos données en cours de travail.

## Asynchronicité : Asyncio, Trio et Green Threads

Il y a eu un défi immémorial entre les modèles de programmation synchrones et asynchrones, dans tous les programmes liés aux E/S. Les noyaux ont fourni des modes asynchrones pour les opérations de disque, avec plus ou moins de succès (E/S non bloquantes _overlapped_ sur Windows, API _io_submit_() limitée sur Linux...).

Le code de mise en réseau a rendu le problème encore plus aigu, avec le besoin d'un grand nombre de connexions à long terme, chacune ne réalisant que des opérations CPU mineures.

Certains langages, comme Erlang, ont confronté cela en étant asynchrones dès le départ, et en laissant différentes tâches communiquer par passage de messages (a.k.a [Modèle d'Acteur](https://en.wikipedia.org/wiki/Actor_model)).

Dans d'autres langages, plusieurs modèles de conception ont émergé pour s'attaquer au problème :

* callbacks
* syntaxe async/await
* threads légers

Les callbacks étaient auparavant la solution majeure dans les frameworks grand public. Par exemple dans jQuery ou Twisted, le développeur fournissait des callables comme arguments ou comme méthodes d'instance, et ceux-ci étaient appelés à la complétion/annulation des E/S, dans un modèle appelé [Inversion de Contrôle](https://en.wikipedia.org/wiki/Inversion_of_control). Cela fonctionne, c'est sûr, mais cela rend les flux de programme assez difficiles à prédire et à déboguer, d'où le terme "soupe de callbacks" souvent utilisé dans ce contexte.

Ces dernières années, la syntaxe [async/await](https://docs.python.org/3/library/asyncio-task.html) est devenue très tendance, surtout dans le monde Python. Mais il y a un problème : comme l'Inversion de Contrôle, c'est une toute nouvelle façon de programmer, presque un nouveau langage. La vaste quantité de packages actuellement disponibles, composés de modules, de classes et de méthodes, ne fonctionne tout simplement PAS avec async/await.

Toute E/S, toute opération coûteuse, cachée au fond d'une sous-dependence, pourrait ruiner votre journée. Nous regardons donc actuellement des milliers de grands modules être réimplémentés joyeusement, avec un tout nouveau monde de bugs et de fonctionnalités manquantes.

Est-ce que tout cela en vaut la peine ? Les développeurs Python ont massivement sauté dans le train du package [asyncio](https://docs.python.org/3/library/asyncio.html), qui est devenu partie intégrante de la stdlib. Mais cette technologie a des problèmes effrayants, comme la difficulté de la contre-pression des sockets, la gestion fragile des exceptions et de ctrl-C, l'annulation non sécurisée des tâches (fuite), et la courbe d'apprentissage abrupte d'une API pleine de pièges et de concepts redondants. D'autres frameworks comme Trio/Curio, semblaient [beaucoup plus prudents sur ces sujets](https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/).

Si nous devons recoder des tonnes de bibliothèques existantes, pourquoi baser les nouvelles versions sur un moteur que certains développeurs ont - non sans arguments - appelé un [dépotoir de mauvais design](https://veriny.tf/asyncio-a-dumpster-fire-of-bad-design/) ? Mais l'[effet de réseau](https://en.wikipedia.org/wiki/Network_effect) est énorme dans de tels cas, et les frameworks alternatifs basés sur async/await auront du mal à défier la norme.

Et qu'en est-il du troisième modèle cité ci-dessus, les threads légers ? Bien avant cette tendance async/await, les développeurs Python ont pensé : nous avons déjà un code métier synchrone parfaitement bien, alors changeons la façon dont il est exécuté, pas la façon dont il est écrit. Ainsi sont apparus les threads légers, ou "greenlets". Ils fonctionnent comme un tas de petites tâches planifiées sur le dessus de quelques threads natifs, des tâches qui cèdent le contrôle les unes aux autres uniquement lorsqu'elles bloquent sur des E/S ou le font explicitement ; et avec une bien meilleure performance que les threads natifs, en termes d'utilisation de la mémoire et de délai de commutation.

En fin de compte, ce système peut rapidement booster n'importe quelle base de code existante pour qu'elle supporte des milliers de tâches concurrentes à long terme. Et ce n'est pas une expérience folle isolée : les threads légers Python ont été utilisés à l'origine dans le jeu Eve Online (via Stackless Python), et ont depuis été portés avec succès vers CPython (Gevent, Eventlet...) et PyPy. Et ils ont en fait [existé depuis longtemps](https://en.wikipedia.org/wiki/Green_threads) dans de nombreux langages de programmation, sous différents noms (processus légers, threads légers, fibres...).

Les inconvénients de ce système ?

* Les bibliothèques doivent bien jouer avec les threads légers, en cédant le contrôle au lieu de bloquer sur les E/S, et en lançant des threads légers au lieu de threads natifs. En Python, les bibliothèques principales (socket, time.sleep(), threading) sont rendues compatibles avec les threads légers via le monkey-patching ; mais les extensions compilées doivent être particulièrement vérifiées, car elles peuvent contourner ces correctifs et bloquer sur leurs propres appels système.
* Aucune lourde computation, ou autre tâche chronophage, ne doit être effectuée, sinon toutes les autres tâches sont impactées par le délai. Pour de tels besoins, déléguez simplement le travail à un pool de [threads natifs](http://www.gevent.org/api/gevent.threadpool.html) (ou une file d'attente de travailleurs de type [celery](http://www.celeryproject.org/)).

Comme nous le voyons, ces inconvénients sont similaires à ceux de async/await, sauf que vous n'avez presque pas à toucher le code original, synchrone. Un "sauf" qui peut signifier des mois ou des années de travail évités ; votre CTO et CEO devraient être hautement satisfaits de cela.

Maintenant, vous entendrez parfois des rationalisations étranges de la part de personnes qui ont abandonné les threads légers au profit d'une réimplémentation complète async/await. Quelque chose dans le genre de "_Explicite est mieux qu'implicite, et tous ces awaits me montrent exactement où mon code pourrait changer de contexte, alors que les threads légers pourraient changer discrètement si une fonction tierce effectue une sorte d'E/S ou de changement explicite_".

Mais le problème est...

PREMIÈREMENT, pourquoi avez-vous besoin de savoir à quels points exactement le programme passera à une autre tâche ? Pendant toutes ces années, avec les threads natifs (préemptifs), un changement pouvait se produire n'importe où, n'importe quand, même au milieu d'un simple incrément.

Mais nous avons appris à gérer cette menace invisible correctement, en protégeant les sections critiques avec des verrous et d'autres primitives de synchronisation (Recursive Locks, Event, Condition, Semaphore...), en gardant un ordre approprié lors de l'imbrication des verrous, et en utilisant des structures de données thread-safe (Queues et similaires) qui gèrent la concourance pour nous.

Les threads légers sont un terrain d'entente entre les threads préemptifs (implicites) et async/await (explicites), mais toutes ces technologies feraient mieux de s'en tenir à la bonne vieille méthode de protection des opérations concurrentes.

Les verrous peuvent être dangereux s'ils sont mal utilisés (surtout puisque la plupart des implémentations bloquent, au lieu de détecter les interblocages et de les signaler comme des exceptions), mais ils sont bon marché et robustes. Quel est l'intérêt d'essayer de faire de la concourance sans verrou, en vérifiant la position de chaque appel potentiellement déclencheur de changement, lorsque vous pourriez avoir à ajouter une nouvelle opération (même une simple sortie de journalisation) au milieu de votre séquence sans verrou soigneusement élaborée, et ainsi ruiner sa sécurité ?

*Ce code naïf montre comment un appel récemment ajouté à log_counter_value() brise un code asynchrone autrement sûr.*

```python

async def increment_counter(counter):
     current = counter.current_value
     await log_counter_value(current)  # Un changement de contexte indésirable se produit ici
     counter.current_value = current + 1
```

DEUXIÈMEMENT, devez-vous vraiment gérer la synchronisation ? Dans le monde du web en particulier, où les requêtes HTTP ne sont pas censées interagir, nous voulons du parallélisme, pas de la concourance. Les données persistantes (et les transactions) sont censées être gérées par des bases de données et des caches externes, pas dans le tas de mémoire du processus.

Ainsi, les bonnes pratiques habituelles de thread-safety (utilisation d'une initialisation thread-safe du processus via des verrous, des structures en lecture seule pour les données globales, et des données en lecture-écriture uniquement locales aux frames de pile) suffisent à rendre l'ensemble du système "thread/greenlet/asynctask safe".

Si un jour vous devez implémenter des algorithmes hautement concurrents à l'intérieur d'un processus, vous choisirez le meilleur outil pour cela, mais pas besoin de construire des usines de marteaux si tout ce que vous avez à faire est d'enfoncer un clou.

## Argent : Bitcoins et alternatives

Réfléchissons un moment. Quels sont les plus grands défis de notre 21ème siècle ? Le changement climatique ? L'évasion fiscale ? La légitimité du pouvoir de l'État ? Ainsi, des esprits candides pourraient penser que la sobriété énergétique, la traçabilité financière, et des organisations (vraiment) démocratiques, seraient des objectifs à poursuivre.

Mais un groupe de hackers intelligents a décidé que les monnaies actuelles étaient un problème majeur, et a inventé les Bitcoins : un système "preuve de travail" dévorant de l'énergie, une anonymat facile des détenteurs d'argent, et une gouvernance floue (pour le moins).

Avec une telle adéquation entre les besoins et la demande, il n'est pas surprenant que les Bitcoins soient devenus ce qu'ils sont : un produit de (presque) pure spéculation, encensé par les [ransomwares](https://cointelegraph.com/news/research-suggests-russian-based-hackers-behind-ryuk-ransomwares-25-million-gains) et diverses mafias, minés en masse par des usines de cartes graphiques, avec un appétit particulièrement élevé pour [être volés](https://cryptosec.info/exchange-hacks/) (ou perdus).

Cette monnaie, et ses frères et sœurs rapidement émergés, ont une histoire déjà pleine de moments déconcertants, avec des divisions de chaîne accidentelles, des [soft forks](https://en.bitcoin.it/wiki/Softfork) bloqués pour des [raisons politiques](https://en.bitcoin.it/wiki/Segregated_Witness), des [hard forks](https://en.wikipedia.org/wiki/List_of_bitcoin_forks) décidés de manière assez arbitraire par diverses personnes (ou forcés par des [cyberattaques](https://news.bitcoin.com/verge-is-forced-to-fork-after-suffering-a-51-attack/)), et des batailles sans fin entre différentes monnaies, ou différentes versions de la même monnaie (Bitcoin Core, Cash, Gold, SV...). Les algorithmes (cryptographie, consensus, code de transaction...) étaient encensés comme les fondations d'un système à toute épreuve et autogéré, mais certains acteurs ont dû [pirater leurs propres utilisateurs](https://www.coindesk.com/crypto-developer-komodo-hacks-wallet-users-to-foil-13-million-hack) pour les protéger du vol, tandis que même les "smart contracts" tant glorifiés ont montré des failles de sécurité effrayantes, et [pas autant de cas d'utilisation](https://www.coindesk.com/three-smart-contract-misconceptions) que certains l'espéraient.

Soyons clairs : la blockchain, un grand livre public basé sur les arbres de Merkle, est loin d'être une mauvaise idée. Mais lorsque les décisions ne sont pas basées sur les besoins de la société et la prudence concernant les bugs, mais sur l'idéologie et la cupidité, le résultat peut être prédit. Et le déclin de l'engouement est proportionnel aux espoirs indûment investis.

Quel est le "meilleur" équivalent du Bitcoin, de l'Ethereum, et autres ? De nombreuses cryptomonnaies alternatives existent, avec des formes d'autorisation plus légères, avec différents algorithmes crypto, avec différents paramètres de confidentialité, avec différents taux d'adoption aussi... Mais si vous me demandez, ce dont nous avons vraiment besoin, c'est "**d'une monnaie facilement traçable pour les finances de l'État et des ONG**" ; un grand livre public conçu de sorte que tout citoyen puisse facilement auditer comment l'argent public est utilisé, du moment où il est collecté via les impôts et les dons, au moment où il retourne dans les circuits privés en payant des biens ou des salaires d'employés. _Est-ce que quelque chose comme cela existe déjà, quelqu'un ? Je n'ai pas réussi à le trouver..._

On pourrait également mentionner les monnaies _locales_ non cryptographiques (ex. la "[Gonette](https://translate.google.com/translate?sl=fr&tl=en&u=http%3A%2F%2Fwww.lagonette.org%2F)" à Lyon, France), maintenues à parité avec les monnaies nationales, qui ont l'avantage de favoriser les entreprises locales et ainsi de réduire les dommages collatéraux du commerce international.

## Formats de données : Texte et Binaire

Un passant spirituel a un jour défini XML comme "_la lisibilité des données binaires avec l'efficacité du texte_". En effet, les parseurs XML tendent à être lents et à encombrer la mémoire (en mode DOM), comparés aux chargeurs de données binaires ; et éditer des configurations et des documents XML à la main n'est pas la meilleure expérience utilisateur que l'on puisse avoir.

Nous comprenons facilement pourquoi XML, en tant que métalangage permettant de créer de nouvelles balises et propriétés pour toutes sortes d'usages, doit être si verbeux. Mais pourquoi un tel enthousiasme pour les formats basés sur du texte, lorsque le but est de transmettre des informations entre serveurs en utilisant des types de données bien définis ?

L'analyse des charges utiles HTTP en une représentation interne, puis l'analyse, par exemple, de son corps JSON, finit par ajouter un surcoût significatif aux requêtes de services web. Pour quel gain ? Les formats binaires comme [Bson](http://bsonspec.org/) rendraient la sérialisation/désérialisation beaucoup plus performante ; et des formats textuels sémantiquement équivalents pourraient être utilisés pour le débogage (auto-convertis par les outils de développement des navigateurs web, Wireshark, CURL et similaires), et pour la création manuelle de charges utiles de test.

Certes, la gestion de ces représentations duales des mêmes données ajouterait un peu de complexité au système, mais à une époque où les startups aiment exposer des services web à des milliers de clients simultanés, le gain de performance peut être réel, avec un effort pas si important.

## Conclusion

Quelle est la morale de tout cela ? Toujours la même, "_utilisez le bon outil pour le bon travail, et méfiez-vous des modes irrationnelles_". Cela peut prendre beaucoup de lecture avant d'avoir une profondeur de vue suffisante, sur un sujet spécifique, pour prendre des décisions éclairées ; mais cet investissement se rentabilise rapidement.

Deviner à quel point un framework sera soutenu à long terme, ou quel protocole/format gagnera une guerre de standardisation, est un problème différent, mais au moins nous pouvons avoir nos opinions fermement fondées, lorsqu'il s'agit d'aspects purement techniques, et cela, c'est de l'or.