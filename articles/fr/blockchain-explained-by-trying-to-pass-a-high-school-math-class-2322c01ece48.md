---
title: La blockchain expliquée en essayant de réussir un cours de maths au lycée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T04:35:30.000Z'
originalURL: https://freecodecamp.org/news/blockchain-explained-by-trying-to-pass-a-high-school-math-class-2322c01ece48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x2gUD6BhNjkF7ac4UEwg5Q.jpeg
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: learning
  slug: learning
- name: privacy
  slug: privacy
- name: 'tech '
  slug: tech
seo_title: La blockchain expliquée en essayant de réussir un cours de maths au lycée
seo_desc: 'By Kevin Kononenko

  If you have ever struggled through a high school math class, then you will be able
  to understand the principles of blockchain technology, which makes Bitcoin possible.

  Have you ever tried to learn the basics of Blockchain by readin...'
---

Par Kevin Kononenko

Si vous avez déjà eu du mal à suivre un cours de maths au lycée, alors vous serez capable de comprendre les principes de la technologie blockchain, qui rend Bitcoin possible.

Avez-vous déjà essayé d'apprendre les bases de la blockchain en lisant des articles de blog ou des wikis au hasard, ou en regardant des vidéos YouTube ?

Cela devient technique **très** rapidement. Vous êtes rapidement confronté à des concepts comme :

_Grand livre distribué_

_Hachage cryptographique_

_Signatures numériques_

Bien que vous puissiez certainement persévérer à travers la confusion initiale, vous devez comprendre une série de nouveaux concepts techniques avant de comprendre l'ensemble du système.

#### **Voici pourquoi c'est si difficile**

Bitcoin (et la blockchain) sont basés sur un paradigme distribué et décentralisé. Nous sommes habitués à des autorités centralisées et dignes de confiance, comme les banques, les prestataires de soins de santé et les entreprises (oui, nous faisons même confiance à la plupart d'entre elles).

Chacune de ces institutions a des systèmes compliqués en place pour maintenir une haute qualité. Afin de maintenir ces mêmes normes pour des produits vitaux _sans_ l'autorité centralisée... nous avons besoin de nouvelles règles compliquées pour garder les systèmes décentralisés en fonctionnement également.

Alors, dans cet article, je vais créer un nouveau lycée appelé "Lycée Distribué" qui fonctionne selon les principes de la blockchain. Nous allons créer une nouvelle façon de noter les devoirs de la classe de maths en utilisant un système distribué. Les élèves pourront maintenir le système de notation par eux-mêmes, sans l'implication des enseignants.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Rj_2EXsXSvtjIL8x.)

**Une dernière note :** Bien que Bitcoin soit probablement l'application la plus populaire de la technologie blockchain en 2018, de nombreuses autres industries commenceront probablement à adopter la blockchain au cours des cinq prochaines années.

Cette explication s'appliquera principalement à Bitcoin, mais elle s'appliquera également à d'autres types de blockchains. Par exemple, les prestataires de soins de santé pourraient utiliser une blockchain pour stocker de manière sécurisée les historiques médicaux individuels.

Si vous cherchez une explication plus technique, cette [vidéo animée de 20 minutes sur YouTube](https://www.youtube.com/watch?v=Lx9zgZCMqXE) sur Bitcoin est probablement ma préférée.

### La manière centralisée de gérer un lycée

Imaginez que vous êtes en première année de lycée et que vous suivez le cours d'algèbre pour tous les élèves de 9e année. Pour réussir le cours, vous devez obtenir une note suffisante aux devoirs, aux quiz et aux tests. Il y a 30 élèves au total dans votre classe.

Tout cela est géré par une seule autorité centralisée : l'enseignant. Cette personne va noter tous vos devoirs, vous remettre vos bulletins chaque trimestre et s'assurer que personne ne triche aux tests (ce qui ruinerait l'intégrité de la classe).

![Image](https://cdn-media-1.freecodecamp.org/images/0*UaeN6iaCD0UUJ6-t.)

Bien que ce soit le système auquel nous sommes tous habitués, il présente en réalité certains défauts inhérents.

1. **Cela peut être inefficace :** lorsque vous donnez 30 tests à un enseignant en même temps, il peut parfois mettre une semaine à vous les rendre — parce que cela prend une éternité pour noter 30 tests !
2. **Parfois, c'est risqué :** parfois, un enseignant peut perdre le test d'un élève. Ou les tests papier peuvent être ruinés par des inondations ou d'autres catastrophes naturelles. Ces choses arrivent. Et les enseignants gèrent tellement de devoirs qu'il y aura probablement des erreurs en cours de route.
3. **Corruptible :** Avez-vous déjà été le perturbateur de la classe ? Lorsque l'enseignant s'assoit pour noter votre test, il peut jeter un coup d'œil au nom en haut du test et devenir instantanément partial en notant le test. Parfois, c'est difficile à éviter (la nature humaine et tout ça).
4. **Coûteux :** Tout ce temps passé à noter les tests est du temps qui pourrait être utilisé pour faire d'autres choses, plus productives. C'est aussi probablement la partie du travail que l'enseignant préfère le moins. Il est probablement devenu enseignant pour aider les élèves à apprendre, pas pour passer tout son temps "libre" à noter des tests. Au lieu de cela, les dollars des contribuables de vos parents sont utilisés pour une activité qui pourrait être grandement améliorée.

Vous pouvez voir des problèmes similaires avec d'autres systèmes centralisés. Par exemple, bien que nous fassions confiance aux banques avec notre argent durement gagné, l'industrie bancaire a aidé à causer la [crise financière de 2008](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%932008) par des pratiques risquées qui ont nécessité un sauvetage massif financé par les contribuables.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-Jp5sc1d8PL_JreA.)

Bien que nous fassions confiance aux médecins, [l'erreur médicale est la troisième cause de décès aux États-Unis](https://www.usnews.com/news/articles/2016-05-03/medical-errors-are-third-leading-cause-of-death-in-the-us), derrière les maladies cardiaques et le cancer. Nombre de ces erreurs pourraient être causées par l'inaccessibilité de données médicales importantes pour les médecins.

Alors, retour au cours de maths au lycée. Vous vous demandez probablement... comment allons-nous résoudre tous ces problèmes en supprimant l'influence de l'enseignant, la personne avec le plus d'expertise dans ce système ? Comment pourrions-nous empêcher que cela ne devienne une anarchie ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*BmLmZP9UAVLDbv49.gif)

C'est là que le concept de blockchain intervient. Avant de me lancer dans la manière spécifique dont nous allons utiliser la blockchain pour créer une nouvelle façon de gérer le Lycée Distribué, vous devez savoir que chaque blockchain a des règles spécifiques qui sont instituées par son créateur.

Dans l'exemple de Bitcoin, ce serait "[Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto)" qui a écrit le livre blanc original et créé les règles (algorithmes) qui permettent son fonctionnement sans intervention humaine.

Dans notre exemple d'école, nous allons avoir un principal exceptionnellement visionnaire qui a changé les règles.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4p657mzLzJjE13V-.)

### Créer une blockchain pour le lycée distribué

Alors qu'un enseignant note les tests et gère les notes en privé, une blockchain rend toutes les transactions publiques. Ainsi, la blockchain ne dépend d'aucune autorité centrale autre que la personne qui l'a créée.

Si vous ne l'avez pas encore deviné, cela signifie que dans le Lycée Distribué, nous allons commencer par faire en sorte que les élèves de 9e année notent les tests les uns des autres !

Disons que c'est le jour du test, et que la période de cours dure une heure. Les élèves empilent soigneusement leurs tests sur le bureau de l'enseignant lorsqu'ils ont terminé.

Mais, au lieu de prendre tous les tests à la maison pour les noter, l'enseignant mélange le tout dans un grand tas et demande à chaque élève de prendre un test au hasard et de le noter avec une clé de correction.

Cela est connu comme une **transaction**. C'est l'unité fondamentale qui constitue une blockchain. Disons qu'un élève, Andy, a donné à un autre élève, Alice, une note de 84. Dans ce cas, Andy est l'**expéditeur** et Alice est le **destinataire**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*t2VhNUww6r7ioUsE.)

En termes de Bitcoin, cela ne serait pas aléatoire : vous savez où vous envoyez de l'argent !

![Image](https://cdn-media-1.freecodecamp.org/images/0*QRWwpy7J6et9kjFV.)

Jusqu'à présent, nous avons résolu les problèmes de vitesse et de coût. Les enseignants n'ont plus besoin de passer du temps à noter, et chaque élève peut noter un autre test assez rapidement. Mais il y a un énorme potentiel de fraude. Cela ressemble beaucoup à de l'anarchie. Il faut un réseau de personnes responsables qui maintiendront tous les participants honnêtes.

C'est là que les politiques du principal entrent en jeu. Le principal contrôle la seule chose qui intéresse tout le monde : le système de notation. Au Lycée Distribué, le principal décide de permettre aux élèves de terminale (12e année) de gérer ce système de blockchain en échange d'une récompense.

Si un élève de terminale révise 20 de ces tests notés en 1 jour, il peut participer à une compétition pour obtenir **10 points ajoutés à l'un de ses propres tests**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1SnDo-1Zf1wigpvx.)

Cet ensemble de 20 transactions est connu comme un **bloc**, et nous montrerons éventuellement comment tous les blocs fonctionnent ensemble pour former une **blockchain**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AKHGsWEryV33QBrV.)

Alors pourquoi seuls les élèves de terminale peuvent-ils faire cela ? Et pourquoi doit-ce être une compétition ?

Il doit s'agir d'élèves de terminale, car le principal a besoin de participants capables de gérer la charge de travail de notation des tests chaque jour (s'ils le souhaitent). Si le système ralentit, alors personne n'aurait ses tests validés et enregistrés, ce qui serait un échec complet.

Et il doit s'agir d'une compétition afin que le système de points ne soit pas complètement dévalué. Imaginez si chaque élève de terminale révisait ses 20 tests et recevait 10 points sur son propre test ? L'inflation des notes serait galopante, de la même manière que l'inflation monétaire augmente lorsque le gouvernement imprime plus d'argent. Il doit y avoir une compétition pour un nombre limité de points. Je partagerai les termes de la compétition plus tard.

Le principal ne force aucun élève de terminale à participer, mais il y a une forte incitation pour eux à le faire.

Dans Bitcoin, chaque bloc a une limite de 1 mégaoctet (Mo) de données. Fin 2017, la transaction moyenne comprenait environ 500 octets de données, donc un bloc contenait généralement environ 2000 transactions ([source](https://arstechnica.com/tech-policy/2017/12/bitcoin-fees-are-skyrocketing/)).

![Image](https://cdn-media-1.freecodecamp.org/images/0*S2XeukezziEmbTz-.)

### Une introduction au grand livre distribué

Maintenant, nous savons comment un test est noté (une transaction) et les incitations en place pour que les élèves de terminale maintiennent le système avec intégrité : ils obtiennent plus de points en révisant et en validant plus de tests. Mais il nous manque encore toute l'infrastructure distribuée pour savoir comment ce travail est réellement accompli.

Disons que 10 élèves de terminale ont accepté l'offre du principal. Ils veulent faire partie de cette compétition pour gagner plus de points sur leurs propres tests. Un autre groupe de 10 élèves de terminale décide de se porter volontaire pour aider à maintenir le système, mais sans participer à la compétition. Cela fait simplement partie du soutien au système distribué, et de l'esprit du mouvement vers une notation open-source.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2aTv7QNJDk-Z1VVC.)

Chacun de ces élèves de terminale est un [**nœud complet**](https://bitcoin.org/en/full-node) dans le réseau. Ils communiquent en temps réel sur les nouvelles transactions et les blocs.

Les 10 élèves de terminale qui ont décidé de participer à la compétition sont appelés **mineurs**. Ils construisent des blocs avec des transactions disponibles dans le **mempool**, le réservoir de transactions non confirmées.

Lorsque qu'un élève, comme Andy, termine de noter un test, l'élève diffuse une **transaction non validée** au réseau d'élèves de terminale. Chaque nœud complet la partage avec tout le monde, comme une rumeur. Elle devient partie du mempool.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oRwV9z9DSPTj0oeH.)

Chaque nœud doit **valider** la transaction en premier. En d'autres termes, ils déterminent si elle était possible ou non. Dans cet exemple, la validation pourrait signifier confirmer que le correcteur a effectivement noté le test correctement en entrant toutes les réponses finales dans votre calculatrice. Nous aborderons l'autre partie de la validation dans un peu.

Après validation, chaque mineur a l'opportunité de construire son propre bloc à partir de 20 tests, ou transactions.

Mais attendez ! Les jours de test, 30 nouvelles transactions devraient être ajoutées au réseau, puisque il y a 30 élèves dans la classe. Comment les mineurs choisissent-ils les transactions à ajouter à leur bloc ?

La réponse est une **frais de transaction**. Chaque **expéditeur** doit attacher un frais de transaction à sa transaction pour compenser les mineurs pour leur travail. Donc, les mineurs choisissent généralement de mettre toutes les transactions avec les frais les plus élevés dans leurs blocs immédiatement. Puisque cela fonctionne sur l'offre et la demande, ils peuvent inclure les transactions avec des frais plus bas les jours où il y a moins de tests à valider.

Dans notre exemple d'école, ce frais de transaction pourrait être un point en moins sur le test de l'expéditeur à donner au mineur. Cela ne serait pas prélevé sur le test d'Alice (le destinataire). Dans Bitcoin, ce serait une petite fraction d'un Bitcoin, comme 0,000003 BTC. L'expéditeur paie le frais puisque c'est la manière la plus facile de gérer la logistique.

![Image](https://cdn-media-1.freecodecamp.org/images/0*G4LLKTQ0ZbDOUa2z.)

À ce stade, chaque mineur a son bloc de 20 transactions validées qu'il aimerait ajouter à la blockchain. Maintenant, il est temps pour la compétition de voir lequel des 10 mineurs verra son bloc accepté et recevra les points du principal.

![Image](https://cdn-media-1.freecodecamp.org/images/0*llDVmllWBaTLR4U3.)

Une dernière chose. Vous commencez à voir la quantité de _redondance_, ou de travail répété. Chaque bloc proposé aura de nombreuses transactions (tests) en commun. C'est une mesure de sécurité nécessaire pour faire fonctionner un système distribué. Si tous les nœuds valident les transactions séparément, cela rend beaucoup plus difficile la tricherie du système.

### La course pour la preuve de travail

Imaginez qu'après tout ce travail pour créer un bloc de 20 transactions, le principal partage ensuite un problème de maths de niveau terminale avec chaque mineur. La personne qui résout le problème en premier reçoit tous les points et voit son bloc confirmé.

Cela signifierait que "les riches deviennent plus riches", et cela fausserait les incitations pour l'ensemble du système.

Chaque jour, les meilleurs élèves en maths auraient une excellente chance de gagner la compétition, et le reste des élèves de terminale aurait peu ou pas de chance. Bientôt, la plupart des mineurs/élèves de terminale cesseraient de participer puisqu'ils ne recevraient jamais de points.

Alors, à la place, notre principal va organiser une chasse au trésor dans l'école chaque soir. Importamment, la chasse au trésor n'a **rien** à voir avec la capacité en maths d'un mineur. Cela encourage tout le monde à continuer à miner.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qr4WFhLdSP25-2cA.)

Le principal va cacher un trophée quelque part dans l'école. Les élèves doivent courir partout jusqu'à ce qu'ils le trouvent, puis crier pour que le reste des élèves de l'école puissent confirmer qu'ils l'ont trouvé et rentrer chez eux. Puisque ce principal a quelques capacités de prescience magique, il cache le trophée dans un endroit parfait pour qu'il prenne environ une heure à trouver chaque nuit.

![Image](https://cdn-media-1.freecodecamp.org/images/0*KInaCht6IDVdOhgP.)

Cela semble-t-il arbitraire ? En d'autres termes, cela semble-t-il sorti de nulle part ?

Eh bien, cela doit être sans rapport avec la validation des tests afin de pouvoir égaliser les chances. Cela est connu sous le nom de "[preuve de travail](https://en.bitcoin.it/wiki/Proof_of_work)" dans Bitcoin. Il s'agit d'un algorithme qui est difficile à résoudre, mais facile pour les autres nœuds à confirmer une fois qu'il est résolu. Chaque mineur de Bitcoin doit deviner des nombres jusqu'à ce qu'il choisisse le bon qui résout l'énigme. Dans Bitcoin, un nouveau bloc est confirmé toutes les 10 minutes, en moyenne.

Gardez à l'esprit que les mineurs de Bitcoin sont en réalité des ordinateurs massifs qui ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*-l7_x9hWb_TnXykS.)
_[Crédit image](https://medium.com/@lopp/the-future-of-bitcoin-mining-ac9c3dc39c60" rel="noopener" target="_blank" title=")._

L'algorithme devient également progressivement plus difficile avec le temps à mesure que plus de mineurs rejoignent le réseau. S'il y a plus de mineurs, cela signifie qu'il y aura plus de devinettes, donc le défi doit devenir plus difficile si Bitcoin veut continuer à confirmer un bloc toutes les 10 minutes.

Cet exemple démontre comment Bitcoin (et notre exemple d'école) forcent chaque mineur à rivaliser contre le reste du réseau. Une fois qu'un mineur résout l'énigme, il partage sa réponse avec le reste du réseau, qui peut être rapidement confirmée. Après que les nœuds atteignent un **consensus**, ou que plus de 50% s'accordent sur le fait que le bloc est **confirmé**, il peut être ajouté à la blockchain.

Cela a motivé certains mineurs à former des **guildes**. Dans notre exemple d'école, cela signifie que quelques élèves s'accorderaient pour partager les points une fois que l'un d'eux a trouvé le trophée. Cela augmente simplement la probabilité que le premier à trouver le trophée soit un membre de leur équipe.

Dans Bitcoin, la puissance de calcul totale qui travaille à résoudre cette "énigme de preuve de travail" est appelée le [**taux de hachage**](https://bitcoin.org/en/vocabulary#hash-rate). Les plus grandes guildes de Bitcoin contrôlent environ 10% du taux de hachage, ce qui donne encore aux autres mineurs une bonne chance de résoudre l'énigme. Si une guilde contenait 50% du taux de hachage, il y aurait moins d'incitation pour les autres à continuer à miner.

Une fois qu'un bloc est confirmé, le mineur reçoit le prix (10 points sur un test) et tous les frais de transaction des transactions confirmées. Les transactions qui n'ont pas fait partie du bloc retournent alors au **mempool** pour être incluses dans un bloc futur.

### Construire une blockchain

Jusqu'à présent, nous avons couvert la plupart des étapes qui permettent d'ajouter un bloc supplémentaire à la blockchain. Mais nous n'avons pas encore abordé le but de la construction d'une blockchain elle-même.

Une blockchain a une structure simple à trois niveaux. Une série de transactions constitue un bloc. Et une série de blocs constitue une blockchain.

Bien que vous puissiez certainement diviser une blockchain en morceaux basés sur le timing, généralement, chaque nœud individuel (élève de terminale) maintiendra l'historique complet de la blockchain, ou le **grand livre**.

Dans notre exemple de lycée, nous regardons une classe de 9e année. Donc, l'historique complet de la classe pourrait être toutes les notes de tous les élèves de la classe entière, de la maternelle jusqu'à aujourd'hui. Puisque nous ajoutons des blocs à un intervalle d'un jour, et qu'il y a environ 180 jours dans l'année scolaire, cela signifierait que la blockchain contient environ 1700 blocs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YdtjX9-71kre2aca.)

Chaque bloc a un identifiant unique, qui, grâce à une "[fonction de hachage](https://www.coindesk.com/information/how-do-bitcoin-transactions-work/)", dépend de l'identifiant de bloc du bloc précédent. C'est ce qui sécurise la blockchain : il n'y a pas de substitution de bloc, ou de réécriture de l'histoire, car cela changerait l'identifiant de bloc de chaque bloc suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IDnKIxaCaRxsE8RU.)

Puisque notre exemple d'éducation utilise des intervalles d'un jour, vous pourriez penser, "Oh, il devrait être facile de créer un identifiant unique pour chaque bloc, puisque chaque date n'apparaît qu'une seule fois !"

Mais cela introduirait une vulnérabilité de sécurité. Si un mineur était capable d'introduire un nouveau bloc quelque part au milieu de la chaîne, cela ne casserait pas le motif ! Le mineur déviant pourrait facilement répliquer l'identifiant de bloc, et aucun des blocs suivants ne changerait leur valeur, puisque les dates suivent un motif fiable qui peut être facilement répliqué.

Voici un [générateur de hachage avec lequel vous pouvez jouer](http://www.miraclesalad.com/webtools/sha256.php). Je souhaite qu'il y ait une merveilleuse analogie que je pourrais vous donner pour l'ordre des blocs, mais malheureusement, c'est le but de la fonction de hachage. Elle rend très, très difficile l'imitation et le remplacement des blocs (impossible, autant que nous le sachions). Donc, je vais ajouter quelques chaînes aléatoires pour montrer ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*c9DDWVUYJU9Gf_lL.)

Nous allons couvrir la confidentialité dans la section suivante, car pour l'instant, il semble que chaque élève de terminale puisse voir l'historique complet des notes de chaque élève de 9e année. Ce n'est pas ce que nous voulons !

Mais, d'un autre côté, le grand livre distribué permet à chaque élève de terminale de garantir la validité des tests notés lorsqu'ils circulent dans le réseau.

Ce système de classement est **relatif**, plutôt qu'absolu. L'ordre des blocs compte beaucoup plus que les moments où ils ont été ajoutés à la chaîne. Les horodatages, comme nous l'avons discuté ci-dessus, sont trop faciles à copier et à imiter.

Donnons un exemple de ce que l'on appelle une **attaque de double dépense**. Disons qu'un de vos camarades de classe passe un test de maths un lundi et sait qu'elle a mal réussi. Un de vos camarades de classe note cette version du test et la diffuse ensuite aux nœuds, comme d'habitude.

Votre camarade de classe qui a mal réussi étudie comme un fou cette nuit-là, puis se présente le lendemain pour passer le même test avec une autre classe. Peut-être que l'enseignant ne l'a pas remarquée là la veille — donc elle peut convaincre l'enseignant qu'elle n'était pas présente le jour précédent. Rappelez-vous, l'enseignant n'a aucun rôle dans la notation des tests, donc l'enseignant ne peut pas rapidement se référer aux examens du jour précédent. L'élève est autorisé à passer le test à nouveau et le soumet avec le reste de la classe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PEQrhnTmZhPyNDwZ.)

Voici les dernières options pour les blocs de la blockchain, avec la tentative d'Alice de remplacer sa note précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YEn6fQq_eZvWuSyl.)

Oh, au fait, Alice devra maintenant devenir un mineur sur le réseau et participer à la chasse au trésor. Elle est maintenant le 11e mineur sur ce réseau.

La règle est que "la chaîne la plus longue gagne". Cela signifie que le jour 11, le reste du réseau peut travailler à l'ajout d'un nouveau bloc avec le dernier ensemble de transactions. Mais Alice travaillera à "**bifurquer**" la chaîne et à ajouter un nouvel ensemble de transactions pour le jour 10 avec 19 transactions en commun, et sa nouvelle note de test en remplacement de l'ancienne note de test.

La bifurcation signifie qu'elle tente de construire une nouvelle chaîne la plus longue, par opposition à la chaîne que le reste du réseau suppose être la plus longue.

Si elle peut gagner la chasse au trésor ce jour-là, puis revenir le lendemain et gagner à nouveau, elle aurait la chaîne la plus longue.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ssSrX9xeV-rGw8D7.)

Cela fait partie de la valeur du système de "preuve de travail". Puisqu'Alice est l'un des 11 mineurs du réseau, elle a environ 1% de chances de résoudre deux blocs de suite. Il y a 99% de chances qu'elle fasse tout ce travail pour ne rien obtenir. Pas une grande incitation.

C'est aussi pourquoi les identifiants de bloc et les identifiants de bloc précédents sont un meilleur schéma d'étiquetage qu'une date spécifique. Si Alice gagne la course le jour où elle passe secrètement le test une deuxième fois, tous les nouveaux tests de ce jour seront toujours stockés dans la blockchain. Ils devront simplement attendre un jour de plus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_P5KrKwCU2FuXkYG.)

### Introduction aux clés publiques et privées

Jusqu'à présent, nous avons couvert tous les mécanismes qui permettront aux élèves du Lycée Distribué de gérer leurs propres notes. Il nous manque encore une chose majeure : la confidentialité !

Pour l'instant, les notes de chaque élève sont exposées pour toujours sur la blockchain. Si cela était une monnaie, il serait facile de savoir combien d'argent chaque personne possède. Ce n'est pas ce que nous voulons.

En même temps, la transparence est un excellent moyen de tenir les individus responsables des notations injustes et d'autres pratiques frauduleuses.

C'est pourquoi Bitcoin utilise un système cryptographique avec des **clés publiques et privées**. Au lycée, vous êtes probablement habitué aux casiers qui bordent presque tous les couloirs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lWOuvJJs7uvVxzK4.)

Eh bien, dans Bitcoin, il y a un nombre (essentiellement) illimité de combinaisons de clés privées-publiques. Donc, à la place, imaginez que les murs de ce lycée sont bordés des petites boîtes aux lettres que vous voyez dans un immeuble d'appartements.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SaCRqoGbn9LGrNZw.)

Et elles couvrent tous les murs de cette école entière. Et, puisque il y a un nombre total illimité de casiers, chaque élève de l'école peut posséder un nombre illimité de casiers. En termes mathématiques :

_Illimité/30 élèves = Illimité_

Avez-vous vu [Harry Potter et l'Ordre du Phénix](https://en.wikipedia.org/wiki/Harry_Potter_and_the_Order_of_the_Phoenix_(film)) ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*lhLjy4ByrTRhb22J.)

C'est comme les scènes de la "[Salle des Prophéties](http://harrypotter.wikia.com/wiki/Hall_of_Prophecy)" — apparemment sans limite.

Mais peu importe...

Pour simplifier, supposons que chaque élève reçoit 1 boîte aux lettres pour chaque année scolaire (de la 9e à la 12e) pendant laquelle ils ont passé des tests. Si un élève est en 9e année, cela signifie qu'il utilise son casier de 9e année.

Revenons à notre transaction, où Andy note le test d'Alice.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pz1ZwzVBr9c_TYNt.)

Nos **nœuds complets**, les merveilleux élèves de terminale, doivent d'abord évaluer si Andy est qualifié pour noter les tests de maths de 9e année. Andy doit se prouver.

Voici un problème : si Andy annonce joyeusement au réseau qu'il a noté le devoir d'Alice, il risque de l'exposer. Et si elle a eu une note d'échec ? Elle ne veut pas que le monde entier le sache, pour toujours !

Donc, il doit diffuser en gardant les deux anonymes. Il peut glisser un mot au hasard à l'un des nœuds... tout comme la plupart des rumeurs dans les films de lycée des années 1980 commencent !

![Image](https://cdn-media-1.freecodecamp.org/images/0*t4cxM7jDV10lZAZQ.gif)

Ensuite, le nœud complet partagerait cette rumeur avec le reste du réseau.

C'est là que nos **clés publiques** entrent en jeu. Lorsque Andy glisse un mot sur son test noté au réseau, il dit en réalité :

* Mon adresse de boîte aux lettres actuelle est 126900trl.
* Afin de prouver que j'étais là le jour du test, voici la clé de correction que l'enseignant m'a donnée pour noter ce test spécifique (**signature numérique**).
* De plus, afin de prouver que je suis bien un élève de 9e année en classe d'algèbre, voici les notes de l'examen final de la classe de maths chaque année de la 1re à la 8e année, et la clé de correction pour chacun de ces tests (**chaîne de transactions**).
* Je vais livrer le test à la boîte aux lettres 856734pok

![Image](https://cdn-media-1.freecodecamp.org/images/0*EgJPXleu1fqn6T4N.)

Cela répond à deux questions clés :

1. L'expéditeur est-il la personne qu'il/elle prétend être ?
2. L'expéditeur est-il qualifié pour être l'expéditeur (noter le test) ?

Pour répondre à la première question, Bitcoin utilise une **signature numérique**. La signature numérique est unique à chaque transaction et est formée avec un hachage de l'identifiant de transaction et de la clé privée. Dans ce cas, c'est un peu comme la clé du test : vous ne pouvez la posséder que si vous étiez là le jour spécifique du test et que l'enseignant vous l'a donnée.

Pour la deuxième question, rappelez-vous que dans Bitcoin, il n'y a pas de concept de "compte" ou de "solde de compte". Si c'était le cas, Andy pourrait simplement partager un numéro d'identification qui prouve qu'il est qualifié.

Afin de prouver que cette clé publique particulière (la clé publique d'Andy) a l'approbation suffisante, il doit partager un historique de tests que chaque nœud complet peut valider. De cette manière, tout le monde peut valider qu'il a terminé la 1re à la 8e année. Andy doit également fournir la clé de correction pour chacun de ces tests pour prouver qu'il était dans la salle à ce moment-là. Cela s'appelle la **chaîne de transactions**. Je ne la couvrirai pas ici, mais c'est une partie importante de la validation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_CQr2_5Bm1-pJBYh.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*TuGPI64sSgjzdV5O.)
_[Crédit image](https://www.cryptocompare.com/wallets/guides/how-do-digital-signatures-in-bitcoin-work/" rel="noopener" target="_blank" title=")._

Après que la transaction d'Andy soit **validée** puis incluse dans un bloc qui a été **confirmé**, il peut aller déposer le test dans la boîte aux lettres d'Alice sans connaissance publique.

Comme vous l'avez remarqué dans la transaction ci-dessus, Andy a dû accéder aux tests des 8 dernières années ! Ce système de casiers ne permet à Andy d'accéder qu'à ses tests.

Andy a un ensemble de 8 **clés privées**. Chaque fois qu'il commençait une nouvelle année, il ouvrait un autre casier et mettait ses notes de cette année dans le casier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3PLQPo9mhRE477b0.)

Les autres peuvent glisser ses derniers résultats de test dans son casier, mais seul lui peut ensuite récupérer les résultats.

Les logiciels Bitcoin comme [Coinbase](http://coinbase.com/) vous permettent de créer de nombreuses combinaisons de clés publiques/privées dans votre portefeuille. Cela améliore la sécurité. Vous ne voulez jamais donner vos clés privées, qui sont le seul moyen d'accéder aux Bitcoins qui vous ont été transférés. Contrairement à une banque traditionnelle, il n'y a personne vers qui se tourner si vous oubliez ou perdez une clé privée. Le Bitcoin sera bloqué.

### Réflexions finales

Pour résumer, nous avons :

* Tests (Transactions)
* Clés de correction (Signatures numériques)
* Élèves de 9e année (expéditeurs et destinataires)
* Élèves de 12e année (nœuds complets)
* Principal (créateur de la blockchain)
* Boîtes aux lettres illimitées (clés publiques/privées)
* Pas d'enseignants notant les tests (autorité centralisée)
* Pas de bulletins (Comptes/soldes de comptes)

Une grande partie de ce système tourne autour du concept d'être "sans confiance", comme vous l'avez probablement vu par les vérifications et les équilibres minutieux et les structures d'incitation. Dans le manuel traditionnel pour administrer la banque ou l'éducation publique, la confiance dans une autorité centrale joue un rôle énorme. Afin de redonner ce contrôle aux individus, il doit y avoir une énorme quantité de redondance de la part des nœuds pour prévenir la fraude, ainsi que des protocoles de sécurité minutieux pour empêcher les pirates d'infiltrer le système.

Mais ce système distribué pourrait révolutionner la manière dont de nombreuses industries gèrent leurs données et pourrait aider à prévenir les accidents industriels, les fautes professionnelles médicales et les ruines financières.

Si vous ne l'avez pas encore remarqué, il y a une énorme quantité de travail dupliqué à travers tous les nœuds complets. Entre la validation et la confirmation des transactions, ainsi que la devinette des réponses à la "preuve de travail" aussi rapidement que possible, le système consomme beaucoup d'énergie. [Selon une estimation](https://arstechnica.com/tech-policy/2017/12/bitcoins-insane-energy-consumption-explained/), le réseau Bitcoin consomme autant d'énergie que le pays du Danemark ! Mais cela est également nécessaire pour former un consensus et maintenir l'intégrité de l'exploitation minière.

### Obtenez plus d'explications visuelles

Avez-vous apprécié ce tutoriel ? Applaudissez-le, laissez un commentaire ou inscrivez-vous ici pour obtenir mes dernières explications techniques :