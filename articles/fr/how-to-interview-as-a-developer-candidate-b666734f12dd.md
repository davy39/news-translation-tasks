---
title: Guide du développeur pour les entretiens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-31T17:24:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-interview-as-a-developer-candidate-b666734f12dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CTlZ73vo9IM0Crz_NhSL3Q.png
tags:
- name: careers
  slug: careers
- name: Interviewing
  slug: interviewing
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Guide du développeur pour les entretiens
seo_desc: 'By Dave Smith

  Alternate title: How to interview a company

  Have you ever been in a job interview, and the interviewer looks across the table
  and says, “do you have any questions?”, and you just stare back and say, “umm, I
  don’t think so”. If this has ...'
---

Par Dave Smith

#### Titre alternatif : Comment interviewer une entreprise

Vous est-il déjà arrivé d'être en entretien d'embauche, et que l'interviewer vous regarde de l'autre côté de la table et dise : « Avez-vous des questions ? », et que vous le regardiez en retour et disiez : « Euh, je ne pense pas. » Si cela vous est arrivé, il y a de fortes chances que vous ayez adopté une vision assez unilatérale de l'expérience de l'entretien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CTlZ73vo9IM0Crz_NhSL3Q.png)

En tant que candidat, vous êtes naturellement concentré sur un objectif : obtenir l'offre d'emploi. Mais n'oubliez pas que les entretiens d'embauche ne sont pas à sens unique. Vous devriez être tout aussi concentré sur **l'interview de l'entreprise** qu'ils le sont sur l'interview de vous.

Mais que devriez-vous leur demander ?

De nombreux développeurs en quête d'emploi m'ont posé cette question. Au cours des 15 dernières années, j'ai travaillé pour 7 entreprises (en comptant 2 stages et un passage de 6 mois dans une startup), et j'ai passé des entretiens dans une douzaine d'autres. J'ai finalement décidé de noter toutes les questions que je pose lors de ces entretiens dans l'espoir que d'autres les trouvent utiles.

> Note : Nous abordons ce sujet et bien d'autres dans notre podcast hebdomadaire de conseils pour développeurs [Soft Skills Engineering](https://softskills.audio/). Abonnez-vous !

Mon objectif est que ce soit un document vivant. Si vous avez des suggestions, faites-le moi savoir via [Twitter](https://twitter.com/djsmith42), et je les incorporerai pour que tout le monde en profite.

### Qui allez-vous rencontrer ?

Lors d'un entretien, vous aurez généralement l'occasion de rencontrer trois types de personnes. Selon la taille de l'entreprise, il peut s'agir d'une seule personne ou de plusieurs :

* Ingénieurs logiciels
* Responsables techniques (lead technique, manager intermédiaire, directeur)
* Direction de l'entreprise (VP, CTO, CEO, manager de département)

J'ai des questions différentes pour chaque type de personne, que je vais lister ci-dessous. Notez que je répète parfois la même question à plusieurs personnes pour voir comment leurs réponses se comparent.

Cet article est assez long et est plus destiné à servir de référence que de lecture continue. Si je devais passer un entretien aujourd'hui, je l'emporterais avec moi et m'y référerais (discrètement) pendant mon entretien.

La plupart de ces questions n'ont pas de réponse « correcte » ou « incorrecte ». Elles sont conçues pour vous aider à en apprendre davantage sur l'entreprise, sa culture, ses processus et son organisation. Elles servent également de points de départ pour la conversation, ce qui peut être très utile pendant un entretien lorsque votre cerveau a décidé de faire une pause.

Par courtoisie, je dis généralement aux interviewers au début de l'entretien que j'aimerais avoir un peu de temps pour poser des questions. Cela les aidera à planifier en conséquence. Habituellement, ils me laissent poser des questions à la fin de l'entretien, alors soyez attentif à l'emploi du temps des interviewers et faites-les savoir de vos intentions tôt dans le processus. Après chaque question, faites une pause pour demander s'il est possible pour vous de continuer à poser des questions, et combien de temps les interviewers ont.

### Questions pour les ingénieurs logiciels

#### 1. Comment savez-vous sur quoi travailler chaque jour ?

Le but de cette question est d'identifier des dysfonctionnements. Je veux obtenir des réponses de 2 ou 3 ingénieurs. Si la direction de l'entreprise dit qu'ils suivent un certain processus, mais que les ingénieurs ne parlent pas de ce processus, c'est un signe de dysfonctionnement. Si vous obtenez des réponses différentes de la part de différents ingénieurs, c'est un autre signe de dysfonctionnement.

Dans une équipe de haute qualité, j'obtiens des réponses cohérentes à cette question. Chaque développeur connaît le processus, et le processus est suffisamment léger pour soutenir les ingénieurs plutôt que de les opprimer.

Exemple de bonne réponse (il y en a beaucoup d'autres) : « Nous faisons des sprints de N semaines où chaque ingénieur s'engage sur un ensemble de fonctionnalités et de corrections de bugs à livrer. Chaque jour, nous faisons un point sur l'avancement de nos engagements. Nous avons un excellent chef de produit qui interface avec les clients pour nous aider à prioriser les fonctionnalités et les corrections de bugs. »

Exemple de mauvaise réponse (il y en a beaucoup d'autres) : « Je viens au bureau et je vois quels feux il faut éteindre. La plupart du temps, je suis interrompu par une urgence. »

Remarquez que je ne mentionne pas « Scrum » ou toute autre méthodologie spécifique. Je m'intéresse beaucoup moins aux étiquettes que l'entreprise utilise pour son processus d'ingénierie qu'au processus quotidien réel de « comment les choses se font ».

#### 2. Quel système de contrôle de révision utilisez-vous ?

De bons outils sont un indicateur fort d'une bonne équipe. Si une équipe utilise un système de contrôle de révision ancien, ils utilisent probablement un tas d'autres outils obsolètes. De plus, ils ne valorisent probablement pas les gains d'efficacité qui peuvent être réalisés en investissant dans de bons outils.

Une bonne question de suivi est de demander sur les flux de travail. Utilisez-vous des branches ? Préférez-vous le rebase ou le merge (termes git) ? Ces questions vous diront à quel point ils sont experts avec leurs outils choisis, ce qui vous en dira long sur leur niveau de compétence, ce qui à son tour vous dira à quoi vous attendre si vous prenez le poste. Par exemple, serez-vous le « expert git local » ou apprendrez-vous d'un véritable Linus Torvalds ?

Cette question peut lancer une discussion sur les outils en général, ce qui vous donnera souvent de bons aperçus.

#### 3. Qu'aimez-vous dans le fait de travailler ici ?

Réponse forte : Je tire beaucoup de satisfaction du travail que je fais.  
Réponse forte : Nous nous amusons beaucoup au travail.  
Réponse forte : J'adore travailler avec des collègues vraiment intelligents et sympathiques.  
Réponse forte : La direction respecte l'ingénierie.

Plus il y a de bonnes réponses, mieux c'est. Je n'ai pas besoin d'obtenir toutes les réponses ci-dessus pour donner une bonne note à l'entreprise. Gardez à l'esprit que certaines personnes ne sont pas naturellement « expansives », donc vous ne recevrez peut-être pas de réponses exceptionnelles ici, et cela peut être tout à fait normal.

Mais si j'entends les types de réponses suivantes, et très peu de la liste des bonnes réponses, je m'inquiète :

Réponse faible : Cela paie les factures.  
Réponse faible : Je n'ai pas à travailler très dur.  
Réponse faible : Il n'y a pas beaucoup de pression pour livrer.  
Réponse faible : Cela n'a pas d'importance si je fais de grosses erreurs.  
Réponse faible : (silence)

Ne pensez pas que j'invente ces réponses. Je les ai réellement entendues lors de vrais entretiens.

Je ne considère pas automatiquement une entreprise comme mauvaise si j'entends ces réponses faibles, mais si ce sont les seules réponses, je cherche généralement ailleurs.

#### 4. Écrivez-vous des tests unitaires ?

Soyez prudent lorsque vous tirez des conclusions sur une équipe d'ingénierie en fonction de leurs pratiques de tests unitaires. Si une équipe est enthousiaste lorsque je demande à propos des tests unitaires, c'est généralement un bon signe. Bien que d'un autre côté, s'ils ne peuvent pas expliquer **pourquoi** ils font des tests unitaires, ou les inconvénients des tests unitaires, cela peut être un indicateur de dogmatisme aveugle. S'ils fournissent de mauvaises excuses pour ne pas écrire de tests, surtout des excuses comme « nous n'avons pas le temps », c'est un mauvais signe pour moi.

Si les ingénieurs me disent qu'ils écrivent des tests unitaires, et qu'ils sont capables de me donner des métriques sur leurs tests, comme le temps qu'ils prennent pour s'exécuter, le nombre de tests qu'ils ont, et leur couverture de code, cela m'attire beaucoup. Cela me dit qu'ils ont de bons outils, et qu'ils savent comment les utiliser. D'un autre côté, s'ils croient que 100 % de couverture de code garantit une base de code sans bugs, je suis méfiant.

Je veux savoir à l'avance si je vais travailler sur une grande base de code ancienne et non testée dans cette entreprise. Cela m'aidera à gérer mes propres attentes et à décider si c'est quelque chose que je veux faire.

Questions de suivi :

* Préférez-vous les tests unitaires ou les tests d'intégration ?
* Avez-vous des tests d'acceptation ?
* Quel(s) framework(s) de test utilisez-vous ? L'aimez-vous ?
* Combien de temps prennent vos tests unitaires pour s'exécuter ?

#### 5. Avez-vous une intégration continue ?

Les meilleures équipes de développement logiciel que je connais utilisent des outils comme Jenkins, Travis et Buildbot. Si l'équipe n'a pas d'intégration continue, j'essaie de voir s'ils sont familiers avec le concept. S'ils ne le sont pas, c'est un mauvais signe selon mon expérience. Avoir un système d'intégration continue signifie que l'équipe croit probablement en l'automatisation, ce qui est généralement un très bon signe selon mon expérience.

Pour certaines équipes, cela mène naturellement à une discussion sur la [livraison continue](http://www.amazon.com/Continuous-Delivery-Deployment-Automation-Signature/dp/0321601912), qui est un concept différent mais lié à l'intégration continue. Si c'est un poste de développeur web, je m'attends à ce que l'équipe ait au moins **entendu** parler de la livraison continue, et les bonnes équipes tendent à la mettre en place, au moins en partie.

Questions de suivi :

* Lorsque l'intégration continue signale une erreur, combien de temps votre équipe met-elle à la corriger ?
* Qu'aimez-vous/détestez-vous dans votre système d'intégration continue ?
* Combien de temps prennent vos exécutions d'intégration continue ? Les rendez-vous plus rapides ?

#### 6. Que mesurez-vous ?

Il s'agit d'une question ouverte destinée à découvrir si l'équipe a mis des efforts à mesurer son logiciel. Pour les équipes de développement web, les réponses tendent à se concentrer sur des métriques de performance comme les temps de réponse du serveur, le débit des requêtes, le nombre d'utilisateurs, la réactivité côté client, etc. Mais la discussion peut aborder des sujets comme le nombre d'utilisateurs parlant différentes langues, la répartition des navigateurs, les taux de succès/échec du cache, et bien d'autres sujets. Si l'équipe n'a pas pris le temps de mesurer, cela peut indiquer qu'ils n'utilisent pas de données réelles pour informer leurs décisions. Ils peuvent être des optimiseurs prématurés. Je valorise une équipe qui utilise des données réelles et mesurées pour prendre des décisions, surtout en matière de performance, mais cela s'applique à tant d'autres choses.

Si l'interviewer connaît les réponses à beaucoup de ces questions, c'est un bon signe que l'équipe est de haute qualité. S'ils n'ont aucune idée de pourquoi ils devraient même se soucier de ces mesures, cela pourrait être un indicateur négatif.

Encore une fois, la règle sur le dogmatisme s'applique ici. Si l'équipe semble s'être accrochée à une métrique qui ne fournit pas nécessairement des informations précieuses et exploitables, et qu'ils ne peuvent pas vous l'expliquer de manière satisfaisante, cela peut être un signe d'avertissement.

Questions de suivi :

* Quelles sont vos métriques de produit les plus importantes ?
* Quels systèmes de mesure utilisez-vous ? (par exemple, [MixPanel](https://mixpanel.com/), [statsd](https://github.com/etsy/statsd), etc.)

#### 7. Comment trouvez-vous et corrigez-vous les bugs ?

Une équipe solide a généralement des testeurs dédiés, et les développeurs de l'équipe se concentrent sur la qualité. Une équipe vraiment solide a une impressionnante automatisation des tests. Certaines équipes sont trop petites pour avoir des testeurs dédiés ou une automatisation des tests, mais cela ne signifie pas nécessairement qu'elles sont une mauvaise équipe. Lorsque je pose cette question, j'essaie de comprendre leur processus. Leurs cheveux sont-ils toujours en feu ? Ont-ils un processus sain pour trouver et prioriser les bugs ? Compte-t-il sur les utilisateurs pour trouver les bugs ?

Questions de suivi :

* Comment priorisez-vous les bugs ?
* Quel système de suivi des bugs utilisez-vous ? (et ce que vous détestez à ce sujet)
* Utilisez-vous Excel pour suivre les bugs ? ([nooo!](http://www.nooooooooooooooo.com/))
* Combien de bugs avez-vous dans votre système de suivi des bugs ?
* Combien de temps prennent vos bugs à corriger (min/max/typique) ?

#### 8. Quels outils de collaboration utilisez-vous ?

Selon mon expérience, les équipes très performantes utilisent de nombreux outils de collaboration. Elles utilisent souvent des services de chat (Slack, IRC, HipChat, Jabber), des services de revue de code (Gerrit, GitHub, GitLab, Review Board), et bien sûr, le vénérable mais vieillissant Email. Je cherche des indicateurs que chaque développeur sait ce que font les autres développeurs. Je ne cherche pas des niveaux de détail insensés, mais plutôt une conscience générale. De plus, j'aime voir des intégrations avec des outils de collaboration. L'exemple le plus simple est un email automatique envoyé chaque fois qu'il y a une erreur de build automatisée. Un autre exemple pour les équipes de développement web est les services de journalisation des erreurs automatisées qui notifient la salle de chat de l'équipe lorsque des erreurs graves se produisent, ou lorsque des métriques clés franchissent un certain seuil.

#### 9. Quels frameworks utilisez-vous ?

Mes préférences personnelles en matière de frameworks sont doubles :

1. J'aime les trucs modernes.
2. J'aime les trucs nouveaux pour moi.

Donc, si une équipe développe une application de bureau [AIX](https://en.wikipedia.org/wiki/IBM_AIX) en [Motif](https://en.wikipedia.org/wiki/Widget_toolkit), je ne suis probablement pas intéressé. Mais peut-être que vous l'êtes. C'est un sujet profondément personnel, et vous devriez l'aborder avec une solide compréhension de vos propres préférences.

Quelles que soient vos préférences en matière de frameworks, il est important de comprendre **pourquoi** l'équipe a choisi ses framework(s). Sont-ils guidés par la hype ? Changent-ils de frameworks comme de sous-vêtements ? Leur base de code est-elle jonchée d'éclats d'obus dus au changement de framework du mois ? Sont-ils bloqués sur une version ancienne ?

Sur le sujet du **pourquoi**, j'aime comprendre combien de latitude les développeurs ont dans le choix des technologies. Est-ce que la direction impose le choix des technologies ? La direction se fie-t-elle aux développeurs ? Pour aller au fond de ces questions, je demande généralement : « Comment en êtes-vous venus à utiliser le framework X dans votre projet ? ». Si les développeurs ne connaissent pas la réponse, cela peut être un mauvais signe, ou cela peut signifier qu'ils sont simplement assez nouveaux dans l'entreprise pour ne pas avoir été présents lors de la décision.

J'aime voir les équipes contribuer aux projets open source qu'elles utilisent. Cela me dit qu'elles sont non seulement capables d'**utiliser** le code open source, mais qu'elles sont suffisamment compétentes pour y contribuer également. Ce sont les types de développeurs avec lesquels j'aime travailler. Si l'entreprise est prête à les payer pour le faire, c'est encore mieux. Cela me dit que l'entreprise comprend ce que signifie être un citoyen de l'open source.

Si l'équipe réinvente la roue plutôt que d'utiliser des outils facilement disponibles pour les aider à construire leur produit, je m'inquiète. Il y a des exceptions à cette règle. Par exemple, lorsque Facebook [travaillait sur leur propre framework](https://facebook.github.io/react/blog/2013/06/05/why-react.html), je ne leur en aurais pas tenu rigueur (ou peut-être que si).

#### 10. Quand pouvons-nous faire du pair programming ?

Si vous voulez avoir une image vraiment claire de ce que c'est que de travailler avec cette équipe, alors essayez de travailler réellement avec eux. Je ne l'ai jamais personnellement fait, mais j'ai un ami qui l'a fait (une histoire probable, n'est-ce pas). Je pense que c'est une idée fantastique. Si vous voulez apprendre presque tout sur l'équipe, allez travailler avec eux pendant une demi-journée. Cela peut nécessiter que vous signiez un accord de confidentialité. Si l'équipe est même prête à considérer cette idée, je pense que c'est un très bon signe.

Vous devrez probablement organiser cela avec quelqu'un de la direction, donc cette question est plus conçue pour obtenir une réaction des développeurs. Ils peuvent être tellement horrifiés par l'idée que cela ne vaut pas la peine d'en parler à la direction.

#### 11. Quand est votre prochaine échéance ?

(contribué par [Evan Farrer](https://twitter.com/evanfarrer))

Cette question est conçue pour vous en dire plus sur le processus de développement que l'entreprise suit réellement. Cette question, à elle seule, n'est pas très informative, mais lorsque vous ajoutez ces questions, les choses deviennent beaucoup plus intéressantes :

* Qui a fixé cette échéance ?
* Avez-vous respecté votre dernière échéance ? Si non, pourquoi ?

Les équipes de haute qualité s'accordent sur les échéances et s'y engagent ensemble. Les échéances qui sont imposées arbitrairement peuvent être un signe de dysfonctionnement, ou au moins que les ingénieurs n'ont pas leur mot à dire lors de la détermination du calendrier.

#### 12. Combien de temps faut-il pour configurer un nouvel environnement de développement ?

(Contribué par [Evan Farrer](https://twitter.com/evanfarrer))

Cette question permet d'évaluer les efforts que l'entreprise a mis dans l'expérience des développeurs. Faut-il des heures, des jours ou des semaines pour que les nouveaux développeurs aient leur ordinateur configuré et prêt à commencer à coder ? Est-ce automatisé ou manuel ? Cela vous indiquera à quel point l'équipe est compétente dans les « activités de support » qui ne sont pas directement liées à l'écriture de logiciels, mais qui aident à les soutenir. L'équipe prend-elle cela au sérieux ?

Certaines entreprises se targuent d'avoir un processus de configuration de développement si rapide que les nouveaux développeurs peuvent mettre du code en production dès le premier jour. Cela montre que l'entreprise prend très au sérieux la fourniture d'une expérience sans friction pour les développeurs.

### Questions pour les responsables techniques

#### 1. Quand avez-vous écrit du code pour la dernière fois ?

J'aime les managers ayant un solide bagage technique. Sans offense pour mes amis MBA, mais j'ai trouvé que les managers que j'apprécie vraiment sont ceux qui ont fait ce que je fais.

#### 2. Comment êtes-vous devenu manager ?

J'aime les managers qui ont choisi de devenir manager parce qu'ils aiment vraiment cela et ont un talent pour cela, plutôt que d'y avoir été forcés. J'aime aussi lorsque les managers semblent se concentrer sur le service à leur équipe. Mes managers préférés sont ceux qui se concentrent sur l'amélioration de la vie de leur équipe, plutôt que sur la « gestion vers le haut ». Ils se voient comme un aide et un protecteur pour leur équipe. Ils ont une attitude de service, et ils considèrent que leur travail le plus important est de rendre la vie professionnelle de leurs membres d'équipe meilleure.

#### 3. Comment vos ingénieurs savent-ils sur quoi travailler chaque jour ?

Puisque je pose la même question aux ingénieurs, j'aime comparer la réponse du manager pour voir si elles correspondent. Si elles ne correspondent pas, cela peut signifier qu'il y a un dysfonctionnement. Le pire type de dysfonctionnement est le dysfonctionnement non reconnu. Je crois que c'est le travail du manager d'identifier ce type de disparité et de le corriger.

#### 4. Quel est le plus grand défi de votre équipe en ce moment ?

Ils répondent généralement qu'il s'agit d'un manque de personnel. Comme il s'agit d'une réponse courante et évidente (ils recrutent après tout), j'aime demander quel est leur deuxième plus grand défi. Je cherche des signaux d'alarme comme des retards de planning, des problèmes de qualité de produit et des drames interpersonnels. Vous reconnaîtrez les signaux d'alarme lorsque vous les verrez. Chaque équipe a des problèmes, donc les réponses que vous obtiendrez dépendront de plusieurs facteurs :

* La conscience des problèmes par le manager
* La volonté du manager d'être honnête avec vous
* La gravité des problèmes au sein de l'équipe

#### 5. Comment mesurez-vous la performance individuelle ?

Un manager compétent aura une bonne technique pour le faire. Les meilleurs managers recueilleront soigneusement les commentaires de toute l'équipe lors de l'évaluation de la performance d'un membre individuel de l'équipe. Un mauvais manager prendra une décision basée sur ses propres observations, sans consulter l'équipe.

#### 6. Faites-vous des évaluations de performance formelles ?

J'aime travailler pour des managers qui valorisent le fait de donner des commentaires et d'aider leurs membres d'équipe à s'améliorer. Les évaluations de performance peuvent être des expériences douloureuses ou positives. D'après mes propres observations, je pense que la plupart des gens les considèrent comme douloureuses. Un manager vraiment excellent saura cela et aura pris des mesures pour rendre les évaluations de performance excellentes d'une manière ou d'une autre qui vous impressionne et vous donne envie de travailler pour eux.

Questions de suivi :

* Pouvez-vous me parler d'une fois où vous avez aidé quelqu'un à améliorer ses performances ?
* Comment coachez-vous les gens pendant ces évaluations ?

#### 7. Faites-vous des augmentations de salaire annuelles ?

J'aime savoir que ma rémunération sera ajustée pour correspondre à ma contribution à l'entreprise, et que nous y jetterons un coup d'œil officiel au moins une fois par an. Pour les entreprises où cela s'applique, j'aime demander à propos des actions. Allez-vous me donner des options d'achat d'actions ? Allez-vous me donner plus d'options d'achat d'actions chaque année ?

Certains ingénieurs sont mal à l'aise de poser des questions financières comme celle-ci. Ne le soyez pas. Les ingénieurs passent généralement un très petit pourcentage de leur temps à réfléchir à ces sujets, mais les managers ont ces conversations **tout le temps**. Ces questions ne devraient pas mettre un manager mal à l'aise :

* Comment budgétisez-vous les augmentations ?
* Quel était le pourcentage médian de l'augmentation de l'année dernière dans votre équipe ?
* Quelle augmentation de salaire pourrais-je espérer dans un an ? Meilleur cas, pire cas ?

Je ne pose pas ces questions comme un contrat signé dans le sang ou une garantie d'augmentations futures. Au lieu de cela, je veux comprendre comment l'entreprise fonctionne. Devrai-je faire des efforts pour demander des augmentations, ou y a-t-il déjà un processus standard en place ?

#### 8. Puis-je obtenir des documents à emporter décrivant les avantages de l'entreprise ?

(Contribué par [Evan Farrer](https://twitter.com/evanfarrer))

Je suppose que la plupart des gens savent déjà demander cela, mais cela vaut la peine d'être mentionné pour l'exhaustivité. La plupart des entreprises sont prêtes à vous donner un tas de papier, ou un site web, qui décrit les avantages de l'entreprise. C'est important à savoir, car c'est souvent une partie assez importante de votre rémunération. Cela peut ne s'appliquer qu'aux États-Unis. Je ne suis pas certain de la manière dont les incitations à l'assurance médicale fournies par l'entreprise fonctionnent dans d'autres pays.

#### 9. Classez-vous les employés les uns contre les autres ?

(Contribué par [Matt Ryan](https://twitter.com/mattvryan))

Certaines entreprises déterminent les augmentations et les bonus (je n'invente pas cela) en classant chaque employé dans une grande liste triée, du meilleur au pire, puis en forçant un certain pourcentage d'employés dans des sous-listes « bons », « moyens » et « mauvais ».

Je n'ai jamais rencontré un ingénieur qui aime cela. Cela est particulièrement courant parmi les grandes entreprises. Cela peut influencer la manière dont vous interagissez avec vos pairs, car vous savez qu'un jour vous devrez rivaliser avec eux pour de l'argent.

Lorsque je rencontre cela, cela ne signifie pas immédiatement que l'entreprise est un endroit terrible pour travailler. Il y a souvent de petites poches d'excellence volant sous le radar dans des entreprises comme celle-ci. Demandez aux interviewers ce qu'ils pensent du système. Certains managers seront assez francs sur leur aversion pour le système, et certains vous diront même des stratégies qu'ils utilisent pour « manipuler » le système au bénéfice de leur équipe. Si vous trouvez ce type de manager, vous pourrez peut-être ignorer le système de classement.

Gardez à l'esprit, également, que tout le monde ne déteste pas ce système. Juste parce que je n'ai pas rencontré quelqu'un qui l'aime ne signifie pas qu'ils n'existent pas.

Questions de suivi :

* Pensez-vous vraiment que X % de vos employés sont « mauvais » ? Que dit cela de votre processus de recrutement ? (c'est une question audacieuse — avancez prudemment)
* Appliquez-vous une sorte de courbe pour déterminer les meilleurs performeurs ?
* Quelles métriques utilisez-vous pour classer les employés ?
* Comment savez-vous que ces métriques sont collectées avec précision ?
* Comment savez-vous que ces métriques identifient réellement les meilleurs performeurs ?

Pour plus d'informations, voici [une bonne analyse de cela par Matt Ryan](http://www.mvryan.org/2012/07/stack-ranking-at-microsoft/).

#### 10. Faites-vous des rétrospectives d'équipe régulières ?

(Contribué par [Aric Parkinson](https://medium.com/@aric.parkinson))

Si oui, à quoi ressemblent-elles ? À quelle fréquence recevez-vous des commentaires des membres de votre équipe ? Quand était la dernière fois que vous avez changé quelque chose dans la manière dont vous gérez votre équipe en fonction des commentaires reçus ?

Ces questions vous donneront une idée de la réactivité que vous pouvez attendre de la gestion, et si l'équipe contribue beaucoup aux commentaires pour la gestion.

Si les rétrospectives ne se font pas, il est difficile pour une équipe d'identifier les problèmes, et encore moins de changer de cap pour les corriger. Et si un manager n'a pas l'impression de recevoir des commentaires sur la manière dont l'équipe pourrait mieux fonctionner, alors ils sont probablement soit sourds aux problèmes de l'équipe, soit ils créent une atmosphère où les gens ne se sentent pas en sécurité pour parler des problèmes.

### Questions pour la direction

Je n'ai pas toujours l'occasion de parler avec la direction senior de l'entreprise, surtout pour les grandes entreprises, mais lorsque je le fais, je le prends comme une opportunité d'évaluer la viabilité financière de l'entreprise. Je ne suis pas vraiment qualifié pour le faire, mais il y a certains problèmes évidents que je peux parfois découvrir lors d'un entretien. De plus, j'aime savoir à quoi ressemble la culture de haut en bas, car cette information peut me dire comment l'entreprise valorise ses ingénieurs, positivement et négativement.

#### 1. Comment êtes-vous financé ?

J'essaie de comprendre l'argent derrière l'entreprise. Si elles sont financées par du capital-risque, du private equity, des actions publiques, ou auto-financées via des revenus, je veux le savoir. Souvent, je peux le découvrir avant l'entretien assez facilement, mais la direction de l'entreprise ajoutera souvent des informations que je ne peux pas trouver via Google ou [CrunchBase](http://crunchbase.com/).

#### 2. Êtes-vous rentable ?

Si vous êtes rentable, c'est génial ! Si vous n'êtes pas rentable, quel est votre plan pour le devenir ? Certaines startups ont un plan pour cela, tandis que d'autres cherchent une sortie via une acquisition ou une introduction en bourse.

Sujets de suivi :

* Revenus historiques des derniers trimestres/années. Est-ce qu'ils sont en hausse ?
* Risques pour la rentabilité comme la concurrence, les dépenses surprises et les manques à gagner surprises.
* Durée de vie : Combien de temps l'entreprise pourrait-elle fonctionner avant de lever plus de capital.

#### 3. Quel est votre avis sur l'externalisation ?

Je veux savoir si le poste pour lequel je postule est susceptible d'être externalisé à l'avenir, ou si le poste pourrait se transformer en une position de gestion d'ingénieurs externalisés.

Je ne parle pas seulement d'externalisation offshore ici. Cela inclut également les contractuels.

#### 4. Parlez-moi de la culture de l'entreprise.

Il s'agit d'une autre question que j'utilise pour concilier la perspective des ingénieurs avec celle de la direction. Je cherche des divergences comme signe de dysfonctionnement. Si la direction et l'ingénierie sont sur la même longueur d'onde, cela indique une bonne communication de haut en bas. Je veux savoir si la direction senior est déconnectée des employés sur le terrain. Je veux aussi voir si la direction a une vision solide qui est bien communiquée. Mes entreprises préférées pour lesquelles travailler ont une vision forte et partagée.

Certaines entreprises [prennent la culture très au sérieux](http://www.slideshare.net/reed2001/culture-1798664), et cela peut être une bonne chose. Au moins, vous serez clair sur ce que l'entreprise valorise. Pour d'autres entreprises, vous devrez le découvrir à travers des nuances implicites, parfois non dites. La culture peut être très importante. Y a-t-il des luttes politiques internes ? La professionnalisme est-il valorisé ? L'honnêteté est-elle valorisée ? Les heures supplémentaires sont-elles valorisées ?

#### 5. Quelle assurance avez-vous que cette entreprise sera un succès ?

Avec cette question, je cherche des preuves réelles, et non pas seulement du battage marketing. Si la direction senior me donne des chiffres réels, comme le chiffre d'affaires, la taille du marché et la capitalisation, c'est un bon signe. De plus, si je peux vérifier ces informations à partir d'autres sources, c'est un signe encore meilleur. D'un autre côté, les chiffres peuvent indiquer quelque chose de très mauvais, comme une durée de vie d'un mois sans financement à l'horizon.

#### 6. Parlez-moi de votre structure de reporting.

Pour moi, la meilleure réponse à cette question est une réponse simple. Si la personne peut dessiner un organigramme simple qui explique la structure de reporting, je suis satisfait. Ma préférence personnelle est de travailler pour des petites entreprises agiles avec un minimum de frais organisationnels et de communication. Votre préférence peut différer, et c'est bien. Peu importe votre préférence, cette question est conçue pour vous donner les informations dont vous avez besoin pour prendre une décision éclairée sur l'entreprise.

### Conclusion

Les entretiens sont bidirectionnels. Assurez-vous de tirer tout ce dont vous avez besoin de l'expérience pour prendre une décision éclairée si vous avez la chance d'obtenir une offre. Bonne chance !