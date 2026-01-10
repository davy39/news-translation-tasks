---
title: Les multiples menaces pour la sécurité Serverless et comment les aborder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T09:30:21.000Z'
originalURL: https://freecodecamp.org/news/the-many-faced-threats-to-serverless-security-and-how-we-should-address-them-c0d24dc43a66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lz4OEP6QW6duz3-mxrByWg.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Les multiples menaces pour la sécurité Serverless et comment les aborder
seo_desc: 'By Yan Cui

  Threats to the security of our server­less appli­ca­tions take many forms. Some
  are old foes we have faced before. Some are new. And some have taken on new forms
  in the server­less world.

  As we adopt the server­less par­a­digm, we del­e­ga...'
---

Par Yan Cui

Les menaces pour la sécurité de nos applications serverless prennent de nombreuses formes. Certaines sont des ennemis que nous avons déjà affrontés. D'autres sont nouvelles. Et certaines ont pris de nouvelles formes dans le monde serverless.

En adoptant le paradigme serverless, nous déléguons encore plus de responsabilités opérationnelles à nos fournisseurs de cloud. Avec AWS Lambda, vous n'avez plus besoin de configurer des AMIs, de corriger le système d'exploitation ou d'installer des démons de surveillance. AWS s'occupe de tout cela pour vous.

Qu'est-ce que cela signifie pour le [Modèle de Responsabilité Partagée](https://aws.amazon.com/compliance/shared-responsibility-model/) qui a longtemps été la pierre angulaire de la sécurité dans le cloud AWS ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*6kr67q2FRqMCmJH83DSZpA.png)

### Protection contre les attaques sur le système d'exploitation

AWS prend en charge la responsabilité de maintenir le système d'exploitation hôte dans le cadre de ses compétences de base. Cela vous évite la tâche rigoureuse d'appliquer tous les derniers correctifs de sécurité. C'est quelque chose que la plupart d'entre nous ne faisons pas assez bien, car ce n'est pas notre principale préoccupation.

En faisant cela, cela nous protège des attaques contre les vulnérabilités connues du système d'exploitation et empêche des attaques telles que [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack).

En supprimant les serveurs de longue durée de l'équation, nous supprimons également les menaces posées par les serveurs compromis qui vivent dans notre environnement pendant une longue période.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yxyS9qbLUBOs_28hl5Zj6g.png)
_WannaCry s'est produit parce que le correctif de sécurité MS17-017 n'a pas été appliqué aux hôtes affectés._

Cependant, il est toujours de notre responsabilité de corriger notre application et de traiter les vulnérabilités qui existent dans notre code et nos dépendances.

### Le top 10 de l'OWASP reste aussi pertinent que jamais

![Image](https://cdn-media-1.freecodecamp.org/images/1*A-fSGp4uquJNZce9n4-lQg.png)
_À part quelques reclassifications, la liste du top 10 de l'OWASP est largement restée la même en 7 ans._

Un coup d'œil au [top 10 de l'OWASP](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) pour 2017 nous montre des menaces familières. Les attaques par injection, l'authentification compromise et le Cross-Site Scripting (XSS) occupent toujours les premières places sept ans plus tard.

#### A9 — Composants avec vulnérabilités connues

Lorsque les gens de [Snyk](https://snyk.io/) ont examiné un ensemble de données de 1792 violations de données en 2016, ils ont découvert que [**12 des 50 principales violations de données**](https://snyk.io/blog/owasp-top-10-breaches) étaient causées par des applications utilisant des composants avec des vulnérabilités connues.

De plus, [77 % des 5000 principales URL d'Alexa incluent au moins une bibliothèque vulnérable](https://snyk.io/blog/77-percent-of-sites-use-vulnerable-js-libraries). Cela est moins surprenant qu'il n'y paraît au premier abord lorsque l'on considère que certains des frameworks front-end js les plus populaires — par exemple [jQuery](https://snyk.io/vuln/npm:jquery), [Angular](https://snyk.io/vuln/npm:angular) et [React](https://snyk.io/vuln/npm:react) — avaient tous des vulnérabilités connues. Cela souligne la nécessité de mettre à jour et de corriger continuellement vos dépendances.

Contrairement aux correctifs du système d'exploitation, qui sont autonomes, fiables et faciles à appliquer, **les mises à jour de sécurité des dépendances tierces sont souvent accompagnées de modifications de fonctionnalités et d'API qui doivent être intégrées et testées**. Cela rend notre vie de développeurs difficile. C'est encore une autre chose que nous devons faire lorsque nous travaillons en heures supplémentaires pour livrer de nouvelles fonctionnalités.

Et puis il y a la question des dépendances transitoires. Si ces dépendances transitoires ont des vulnérabilités, alors vous êtes également vulnérable par le biais de vos dépendances directes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bB9XkUioCbd7TUtM8vQdVQ.png)
_[https://david-dm.org/request/request?view=tree](https://david-dm.org/request/request?view=tree" rel="noopener" target="_blank" title=")_

Trouver des vulnérabilités dans nos dépendances est un travail difficile et nécessite une vigilance constante. C'est pourquoi des services comme [Snyk](https://snyk.io/) sont si utiles. Il est même livré avec une [intégration intégrée avec Lambda](https://snyk.io/docs/aws-lambda) !

#### Attaques contre les éditeurs de NPM

![Image](https://cdn-media-1.freecodecamp.org/images/0*fyWZzYs7lD1pODKQ.gif)
_Que se passe-t-il si l'auteur/éditeur de votre dépendance tierce n'est pas celui que vous pensez ?_

L'année dernière, un chasseur de primes de sécurité [a réussi à obtenir des droits de publication directs sur **14 % des packages NPM**](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md). La liste des packages affectés comprend également des noms importants : `debug`, `request`, `react`, `co`, `express`, `moment`, `gulp`, `mongoose`, `mysql`, `bower`, `browserify`, `electron`, `jasmine`, `cheerio`, `modernizr`, `redux` et bien d'autres. Au total, ces packages représentent **20 % du nombre total de téléchargements mensuels depuis NPM**.

_Laissez cela couler un moment._

A-t-il utilisé des méthodes sophistiquées pour contourner la sécurité de NPM ?

Non, c'était une combinaison de **force brute** et l'utilisation de fuites de comptes et de crédits **connues** provenant de plusieurs sources, y compris Github. En d'autres termes, n'importe qui aurait pu faire cela avec très peu de recherche.

Il est difficile de ne pas se sentir déçu par ces auteurs de packages lorsque tant d'entre eux affichent une attitude si cavalière envers la sécurisation de l'accès à leurs comptes NPM.

> 662 utilisateurs avaient le mot de passe « 123456 », 174 — « 123 », 124 — « password ».

> 1409 utilisateurs (1 %) utilisaient leur nom d'utilisateur comme mot de passe, sous sa forme originale, sans aucune modification.

> 11 % des utilisateurs réutilisaient leurs mots de passe divulgués : 10,6 % — directement, et 0,7 % — avec des modifications mineures.

Comme je l'ai [démontré dans ma conférence sur la sécurité Serverless](https://youtu.be/jUhiPj6h_L8?t=794), vous pouvez voler des identifiants AWS temporaires en ajoutant quelques lignes de code.

Imaginez alors un scénario où un attaquant a réussi à obtenir des droits de publication sur 14 % de tous les packages NPM. Il pourrait publier une mise à jour corrective pour tous ces packages et voler des identifiants AWS à grande échelle.

Les enjeux sont élevés et c'est probablement la plus grande menace de sécurité à laquelle nous sommes confrontés dans le monde serverless. Et cela affecte également les applications s'exécutant dans EC2 ou des conteneurs.

Les problèmes et risques liés à la gestion des packages ne sont pas spécifiques à l'écosystème Node.js. J'ai passé la plupart de ma carrière à travailler avec .Net et maintenant Scala, et la gestion des packages a été un défi partout. **Nous avons besoin que les auteurs de packages fassent preuve de diligence raisonnable envers la sécurité de leurs comptes.**

#### A1 — Injection & A3 — XSS

Les injections SQL et autres formes d'attaques par injection sont toujours possibles dans le monde serverless. Tout comme les attaques par Cross-Site Scripting (XSS).

Même si vous utilisez des bases de données NoSQL, vous n'êtes peut-être pas à l'abri des attaques par injection. MongoDB, par exemple, expose un certain nombre de [vecteurs d'attaque](https://zanon.io/posts/nosql-injection-in-mongodb) via ses API de requête.

L'API plus rigide de DynamoDB rend une attaque par injection plus difficile. Mais vous êtes toujours ouvert à d'autres formes d'exploits. Par exemple, XSS et des identifiants divulgués qui accordent à l'attaquant l'accès aux tables DynamoDB.

Néanmoins, vous devez toujours assainir les entrées utilisateur, ainsi que la sortie de vos fonctions Lambda.

#### A6 — Exposition de données sensibles

Avec les serveurs, les frameworks web sont également redondants lorsque vous passez au paradigme serverless. Ces frameworks web nous ont bien servis pendant de nombreuses années. Mais ils nous ont également remis une arme chargée avec laquelle nous pouvons nous tirer une balle dans le pied.

_Troy Hunt_ a [démontré](https://skillsmatter.com/skillscasts/9954-london-dot-net-june-meetup) comment nous pouvons exposer accidentellement toutes sortes de données sensibles en laissant les options de liste de répertoires ACTIVÉES. Des fichiers web.config contenant des identifiants (à 35:28) aux fichiers de sauvegarde SQL (à 1:17:28) !

Avec _API Gateway_ et _Lambda_, les expositions accidentelles comme celle-ci sont très improbables. Parce que la liste de répertoires devient une « fonctionnalité » que vous devrez implémenter vous-même. Cela vous oblige à prendre une décision consciente sur le moment de prendre en charge la liste de répertoires, et la réponse est probablement _jamais_.

### IAM

Si vos fonctions sont compromises, la prochaine ligne de défense consiste à restreindre ce que les fonctions compromises peuvent faire.

C'est pourquoi vous devez appliquer le **Principe du Moindre Privilège** lors de la configuration des permissions Lambda.

Dans le framework [Serverless](https://serverless.com/framework/), le comportement par défaut consiste à utiliser le même rôle IAM pour toutes les fonctions du service.

Cependant, la spécification `serverless.yml` vous permet de spécifier un [rôle IAM différent par fonction](https://serverless.com/framework/docs/providers/aws/guide/iam/#custom-iam-roles-for-each-function). Mais cela implique beaucoup plus d'efforts de développement et ajoute suffisamment de friction pour que presque personne ne le fasse.

Heureusement, _Guy Lichtman_ a créé un plugin pour le framework _Serverless_ appelé [serverless-iam-role-per-function](https://github.com/functionalone/serverless-iam-roles-per-function). Ce plugin facilite grandement l'application de rôles IAM par fonction. Suivez les instructions sur la page Github et essayez-le vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T78Ys1ipg_dEFe2_K63R5A.png)
_Vous devez appliquer des politiques IAM par fonction._

#### Politique IAM non versionnée avec Lambda

Un inconvénient avec Lambda et la configuration IAM est que les politiques IAM ne sont pas versionnées avec la fonction Lambda.

Si vous avez plusieurs versions de la même fonction en utilisation active (peut-être avec différents alias), il devient problématique d'ajouter ou de supprimer des permissions :

* Ajouter des permissions à une nouvelle version permet aux anciennes versions d'avoir plus d'accès que nécessaire
* Supprimer des permissions d'une nouvelle version peut casser les anciennes versions qui ont encore besoin de ces permissions

Avant la version 1.0, c'était un problème courant avec le framework _Serverless_ car il utilisait des alias pour implémenter les étapes. Depuis la version 1.0, ce n'est plus un problème, car chaque étape est déployée en tant que fonction séparée. Par exemple :

* `service-function-dev`
* `service-function-staging`
* `service-function-prod`

Cela signifie qu'une seule version de chaque fonction est active à tout moment. Sauf lorsque vous utilisez des alias pendant un [déploiement canari](https://aws.amazon.com/blogs/compute/implementing-canary-deployments-of-aws-lambda-functions-with-alias-traffic-shifting/).

**L'isolement au niveau du compte** peut également aider à atténuer les problèmes d'ajout/suppression de permissions. Cet isolement aide également à **compartimenter les violations de sécurité**. Par exemple, une fonction compromise dans un compte non-production ne peut pas être utilisée pour accéder aux données de production.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2lyB5B4OydPapmdqbozTSQ.png)
_Nous pouvons appliquer la même idée de cloisonnement (qui a été popularisée dans le monde des microservices par le livre « Release It » de Michael Nygard) et compartimenter les violations de sécurité au niveau du compte._

#### Supprimer les fonctions inutilisées

L'un des avantages du paradigme serverless est que vous ne payez pas pour les fonctions lorsqu'elles ne sont pas utilisées.

L'inconvénient est que vous avez moins d'incitation à supprimer les fonctions inutilisées puisqu'elles ne vous coûtent rien. Cependant, ces fonctions existent toujours comme surfaces d'attaque. Elles sont également plus dangereuses que les fonctions actives car elles sont moins susceptibles d'être mises à jour et corrigées. Avec le temps, ces fonctions inutilisées peuvent devenir un foyer de vulnérabilités connues que les attaquants peuvent exploiter.

La documentation de Lambda cite également cela comme l'une des [meilleures pratiques](http://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

> Supprimez les anciennes fonctions Lambda que vous n'utilisez plus.

### L'évolution des attaques par déni de service

Avec AWS Lambda, vous êtes beaucoup plus susceptible de vous sortir d'une attaque par déni de service (DoS) en augmentant l'échelle. Cependant, l'augmentation agressive de votre architecture serverless pour combattre une attaque DoS par la force brute a une implication de coût significative.

Sans surprise, les gens ont commencé à appeler les attaques DoS contre les applications serverless des attaques **Denial of Wallet (DoW)** !

> « Mais vous pouvez simplement limiter le nombre d'invocations simultanées, non ? »

Bien sûr, et vous vous retrouvez avec un problème de DoS à la place… c'est une situation perdant-perdant.

Bien sûr, il y a [AWS Shield](https://aws.amazon.com/shield/). Pour un forfait fixe, AWS Shield Advanced vous offre une protection de paiement en cas d'attaque DoS. Mais au moment de la rédaction, cette protection ne couvre pas les coûts de Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XcX3b03mcFcmyVfENHbYPg.png)
_Pour un forfait mensuel fixe, AWS Shield Advanced offre une protection des coûts en cas d'attaque DoS, mais cette protection ne couvre pas encore Lambda._

De plus, Lambda a une **politique d'invocation au moins une fois** (at-least-once). [Selon les gens de Sungard](https://blog.sungardas.com/CTOLabs/2017/06/run-lambda-run/), cela peut entraîner jusqu'à trois invocations (réussies). Selon l'article, le taux signalé d'invocations multiples est extrêmement faible, à 0,02 %. Mais on se demande si le taux est lié à la charge et pourrait se manifester à un taux beaucoup plus élevé pendant une attaque DoS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HUDZHb1Ky4S-kQuThh1-Lg.png)
_Tiré de l'article « Run, Lambda, Run » mentionné ci-dessus._

De plus, vous devez considérer comment Lambda [réessaie les invocations échouées](http://docs.aws.amazon.com/lambda/latest/dg/retries-on-errors.html) par une [source asynchrone](http://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html). Par exemple, S3, SNS, SES et CloudWatch Events.

Officiellement, ces invocations sont réessayées deux fois avant d'être envoyées à la file d'attente des lettres mortes (DLQ) assignée, si elle est configurée. Cependant, une [analyse](https://engineering.opsgenie.com/aws-lambda-performance-series-part-2-an-analysis-on-async-lambda-fail-retry-behaviour-and-dead-b84620af406) par OpsGenie a montré que le nombre de réessais peut aller jusqu'à six avant que l'invocation ne soit envoyée à la DLQ.

Si l'attaquant DoS est capable de déclencher des invocations asynchrones échouées, il peut alors **amplifier l'impact de son attaque**.

Par exemple, si votre application permet au client de télécharger un fichier vers S3 pour traitement. L'attaquant peut alors vous attaquer par DoS en téléchargeant un grand nombre de fichiers invalides qui provoqueront des erreurs et des réessais de vos fonctions.

Tout cela s'additionne pour que le nombre réel d'invocations Lambda explose pendant une attaque DoS. Comme nous l'avons discuté précédemment, bien que votre infrastructure puisse être capable de gérer l'attaque, **votre portefeuille peut-il s'étirer dans la même mesure** ? Devriez-vous le permettre ?

### Sécurisation des données externes

![Image](https://cdn-media-1.freecodecamp.org/images/1*PlSruVB-6fWW2XyO9z-q0w.png)
_Juste une poignée des endroits où vous pourriez stocker l'état en dehors de votre fonction Lambda sans état._

En raison de la nature éphémère des fonctions Lambda, il est probable que toutes vos fonctions soient sans état. Plus que jamais, les états sont stockés dans des systèmes externes et nous devons les sécuriser à la fois **au repos** et **en transit**.

La communication avec tous les services AWS se fait via HTTPS et chaque requête est signée et authentifiée. Une poignée de services AWS offrent également un chiffrement côté serveur pour vos données au repos. Par exemple, [S3](http://amzn.to/1N3Twb8), [RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) et [Kinesis streams](http://amzn.to/2tgvFR2) viennent à l'esprit. Lambda dispose également d'une intégration intégrée avec KMS pour chiffrer les variables d'environnement.

Récemment, DynamoDB a également annoncé la [prise en charge du chiffrement au repos](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html).

La même diligence doit être appliquée lors du stockage de données sensibles dans des services/bases de données qui n'offrent pas de chiffrement intégré. En cas de violation de données, cela fournit une couche supplémentaire de protection pour les données de vos utilisateurs.

_Nous devons cela à nos utilisateurs._

Utilisez un transport sécurisé lors de la transmission de données vers et depuis les services (à la fois externes et internes). Si vous construisez des API avec API Gateway et Lambda, vous êtes obligé d'utiliser HTTPS par défaut, ce qui est une bonne chose. Cependant, les points de terminaison API Gateway sont toujours publics, vous devez prendre les précautions nécessaires pour sécuriser l'accès aux API internes.

Vous devez utiliser des [rôles IAM](http://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) pour protéger les API internes. Cela vous donne un [contrôle granulaire](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-iam-policy-examples-for-api-execution.html) sur qui peut invoquer quelles actions sur quelles ressources. L'utilisation de rôles IAM vous évite également des conversations maladroites comme celle-ci :

_« C'est le dernier jour de X, il a probablement nos clés API sur son ordinateur portable quelque part, devrions-nous faire tourner les clés API au cas où ? »_

_« Hmm.. ce serait beaucoup de travail, X est digne de confiance, il ne va rien faire. »_

_« Ok… si tu le dis… (prie secrètement que X ne perde pas son ordinateur portable ou ne développe pas une rancune tardive contre l'entreprise) »_

Heureusement, cela peut être [facilement configuré](https://serverless.com/framework/docs/providers/aws/events/apigateway#http-endpoints-with-aws_iam-authorizers) en utilisant le framework `Serverless`.

### Identifiants divulgués

![Image](https://cdn-media-1.freecodecamp.org/images/1*8wH4JqfvBQmdcQpaROJCog.png)
_Ne devenez pas un mineur de bitcoins involontaire._

Internet regorge d'histoires d'horreur de développeurs accumulant une facture AWS massive après que leurs identifiants divulgués ont été utilisés pour miner des bitcoins. Pour chaque histoire de ce type, beaucoup d'autres ont été affectées mais ont choisi de rester silencieuses. Pour la même raison, de nombreuses violations de sécurité ne sont pas divulguées publiquement car les entreprises ne veulent pas perdre la face.

Même dans mon petit cercle social, je connais deux incidents de ce type. Aucun n'a été rendu public et les deux ont entraîné des dommages d'une valeur de plus de 100 000 $. Heureusement, dans les deux cas, AWS a accepté de couvrir les coûts.

AWS analyse les dépôts Github publics pour détecter les identifiants AWS actifs et tente de vous alerter dès que possible. Mais même si vos identifiants étaient publics pendant un bref instant, ils pourraient ne pas échapper au regard vigilant des attaquants. De plus, ils existent toujours dans l'historique des commits Git, sauf si vous réécrivez également l'historique. Si vos identifiants sont tombés dans le domaine public, il est préférable de les désactiver dès que possible.

Une bonne approche pour prévenir les fuites d'identifiants AWS consiste à utiliser des hooks de pré-commit Git comme décrit dans [cet article](https://www.unixdaemon.net/cloud/preventing-aws-creds-in-git-with-pre-commit/).

D'après ce que j'entends, les attaquants sont les plus susceptibles de lancer des instances EC2 dans les régions de Sao Paulo et de Tokyo. Vous pouvez utiliser des motifs d'événements CloudWatch et Lambda pour vous alerter lorsqu'il y a des appels API EC2 dans des régions que vous n'utilisez pas. De cette façon, vous pouvez au moins réagir plus rapidement lorsque vos identifiants sont divulgués.

### Conclusions

Nous avons examiné un certain nombre de menaces pour la sécurité de nos applications serverless dans cet article. Beaucoup d'entre elles sont les mêmes menaces qui ont affligé l'industrie du logiciel depuis des années. Tous les éléments du top 10 de l'OWASP s'appliquent toujours à nous, y compris les injections SQL, NoSQL et autres formes d'attaques par injection.

Les identifiants AWS divulgués restent un problème majeur et peuvent affecter toute organisation utilisant AWS. Bien qu'il y ait quelques incidents signalés publiquement, j'ai le sentiment que le nombre réel d'incidents est beaucoup plus élevé.

Nous sommes toujours responsables de la sécurisation des données de nos utilisateurs, à la fois au repos et en transit. API Gateway est toujours accessible publiquement, nous devons donc prendre les précautions nécessaires pour sécuriser l'accès à nos API internes, de préférence avec des rôles IAM. IAM offre un contrôle granulaire sur qui peut invoquer quelles actions sur vos ressources API, et facilite la gestion de l'accès lorsque les employés arrivent et partent.

Sur une note positive, le fait qu'AWS prenne en charge la responsabilité de la sécurité du système d'exploitation hôte nous offre un certain nombre d'avantages en matière de sécurité :

* Protection contre les attaques sur le système d'exploitation, car AWS peut faire un bien meilleur travail de correction des vulnérabilités connues dans le système d'exploitation
* Les systèmes d'exploitation hôtes sont éphémères, ce qui signifie qu'il n'y a pas de serveurs compromis de longue durée

Avec API Gateway et Lambda, vous n'avez plus besoin de frameworks web pour créer une API. Sans frameworks web, il n'y a pas de moyen facile de prendre en charge la liste des répertoires. Mais c'est une bonne chose, car cela fait de la liste des répertoires une décision de conception précise. Plus d'exposition accidentelle de données sensibles par mauvaise configuration.

Les attaques DoS ont pris une nouvelle forme dans le monde serverless. Bien que vous puissiez vous sortir d'une attaque en augmentant l'échelle, cela vous coûtera toujours cher. Les coûts de Lambda encourus pendant une attaque DoS **ne sont pas** **couverts** par _AWS Shield Advanced_ au moment de la rédaction.

Pendant ce temps, de nouvelles surfaces d'attaque ont émergé avec AWS Lambda :

* Les fonctions sont souvent sur-permissionnées. Une fonction compromise peut faire plus de dégâts qu'elle ne le pourrait autrement.
* Les fonctions inutilisées sont souvent laissées pendant une longue période, car il n'y a pas de pénalité de coût. Mais les attaquants peuvent les exploiter. Elles sont également plus susceptibles de contenir des vulnérabilités connues puisqu'elles ne sont pas activement maintenues.

Par-dessus tout, la menace la plus préoccupante pour moi est les attaques contre les auteurs de packages eux-mêmes. De nombreux auteurs ne prennent pas la sécurité de leurs comptes au sérieux. Cela les met en danger ainsi que le reste de la communauté qui dépend d'eux. Il est difficile de se protéger contre de telles attaques et cela érode l'un des aspects les plus forts de tout écosystème logiciel — la communauté derrière lui.

Une fois de plus, les gens se sont avérés être le maillon le plus faible de la chaîne de sécurité.