---
title: Ingénierie suffisamment bonne pour démarrer une entreprise Internet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-02T18:28:06.000Z'
originalURL: https://freecodecamp.org/news/good-enough-engineering-to-start-an-internet-company
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/0_LwPXGTcWzWROtCb2-1.jpeg
tags:
- name: engineering
  slug: engineering
- name: startup
  slug: startup
seo_title: Ingénierie suffisamment bonne pour démarrer une entreprise Internet
seo_desc: 'By Wenbin Fang

  I gave a guest lecture in an undergraduate software engineering class (CSCE431)
  at Texas A&M University in March 2019. Now I’ve turned this lecture into a blog
  post here, and hopefully some people on the Internet will find this useful....'
---

Par Wenbin Fang

J'ai donné une conférence invitée dans une classe de génie logiciel de premier cycle ([CSCE431](https://parasol.tamu.edu/~jeff/course/431/syllabus.html)) à l'[Université Texas A&M](https://www.tamu.edu/) en mars 2019. Maintenant, j'ai transformé cette conférence en un article de blog ici, et j'espère que certaines personnes sur Internet trouveront cela utile.

Si vous arrivez d'une recherche Google, voici quelques contextes :

Je dirige une petite entreprise Internet — Listen Notes, Inc. — avec un seul employé à temps plein (moi), en date du 2 août 2019. Nous avons construit un site web de moteur de recherche de podcasts [ListenNotes.com](https://www.listennotes.com/) et une [API de podcast](https://www.listennotes.com/api/).

---

Je vais partager avec vous mon expérience sur le démarrage d'une entreprise Internet. Construire un produit Internet n'est pas comme construire un iPhone ou une pyramide. Votre produit n'a pas besoin d'être parfait au début. Si vous construisez quelque chose d'utile, d'autres personnes vous diront quoi faire ensuite. Et vous découvrirez ce qui suit. Généralement, vous devriez être à l'aise avec l'incertitude, si vous voulez démarrer votre propre entreprise.

La première version de Facebook a été lancée début février 2004, ce qui représentait à peine quatre semaines de travail pour un étudiant de premier cycle. C'était un produit suffisamment bon avec une ingénierie suffisamment bonne. Aujourd'hui, tout diplômé en informatique devrait être capable de construire la première version de Facebook en un week-end, en utilisant un framework de programmation web moderne (par exemple, Rails, Django...).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_eUI1qz9hToUB2j8J.jpeg align="left")

Des entreprises comme Google, Snapchat, Spotify, Amazon, Twitter et d'autres sont toutes de grandes entreprises Internet de notre génération.

Cependant, je ne peux pas vous dire comment devenir une entreprise aussi réussie qu'elles. Je n'en suis pas encore là. Ces entreprises sont si réussies et si grandes. Par exemple, Google compte 100 000 employés, en mars 2019. Mais il y a eu un moment dans l'histoire où Google n'avait que deux employés. Vous devez commencer quelque part ou nulle part. Je peux parler de la façon de commencer.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_I4_WGAoGLblwwqyS.jpeg align="left")

Espérons qu'après cette leçon, vous trouverez que démarrer une entreprise Internet n'est pas difficile du tout. Et vous apprendrez quelques outils et services que vous pourrez utiliser dans vos futurs projets.

Vous m'entendrez dire « il y a un outil » beaucoup. C'est ce que je veux dire par « ingénierie suffisamment bonne ». Nous sommes en 2019. Il est peu probable que vous soyez la première personne à rencontrer un problème fondamentalement nouveau. Il doit y avoir des outils et des services qui peuvent vous aider à résoudre des problèmes — souvent, gratuitement !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_ViBYy46VqNACtgNA.jpeg align="left")

Avant d'aller plus loin, laissez-moi vous donner une brève introduction de Listen Notes.

Listen Notes est un site web de moteur de recherche de podcasts. Vous tapez un mot-clé et vous recherchez tous les podcasts d'Internet. C'est aussi simple que Google :) Mais simple ne signifie pas facile. Nous avons également construit beaucoup d'outils sur le moteur de recherche de base pour aider les gens à découvrir et à profiter des podcasts.

[https://www.listennotes.com/](https://www.listennotes.com/)

Faisons un pas en arrière pour parler des podcasts. Un podcast est un type de format de média. Certaines personnes l'appellent « radio à la demande ». Nous consommons des tonnes de contenu médiatique chaque jour. Nous regardons des vidéos YouTube, regardons la télévision, lisons des livres, écoutons de la musique et écoutons des podcasts. Nous consommons du contenu médiatique parce que nous voulons obtenir des informations, acquérir des connaissances et être divertis. Aujourd'hui, vous pouvez littéralement apprendre n'importe quel sujet en écoutant des podcasts. Vous pouvez écouter des podcasts pendant que vos yeux et vos mains sont occupés (par exemple, conduire, faire de l'exercice, marcher, faire le ménage...).

Début 2017, je me suis rendu compte que je consommais plus d'informations à partir de podcasts que d'autres formats de médias (par exemple, la télévision, les livres...). J'avais besoin d'un moteur de recherche de podcasts que je pouvais utiliser pour rechercher et trouver des épisodes individuels à écouter en rafale. En rétrospective, un moteur de recherche de podcasts devrait être une chose très simple à exister. Mais je n'ai pas pu en trouver un bon. J'ai donc passé moins d'une semaine à construire un prototype de Listen Notes, le moteur de recherche de podcasts né de mes propres souhaits et nécessités.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_pXGHwh1sY_r0Hdk0.png align="left")

*Toute première version de Listen Notes. Crédits :* [*Lifehacker*](https://lifehacker.com/the-best-podcast-search-engine-1818560337)

J'ai lancé le prototype et je l'ai beaucoup utilisé moi-même. Mais je n'ai pas touché au code pendant environ neuf mois, jusqu'à ce que je décide de travailler dessus à temps plein après avoir quitté ma première startup ratée. C'était en septembre 2017. Un an et demi plus tard, je m'amuse toujours à travailler sur Listen Notes :)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_3s9fAs-S58WF7YpI.jpeg align="left")

Avez-vous besoin de savoir où trouver un bureau ? Oui, il y a un service pour cela. J'utilise [WeWork](https://refer.wework.com/i/WenbinFang). J'ai un petit bureau à l'intérieur de [WeWork](https://refer.wework.com/i/WenbinFang) à San Francisco. Le bureau n'est pas bon marché, mais je pense que c'est un bon investissement pour la productivité.

Je peux choisir de dépenser de l'argent pour être 200 % plus productif moi-même, ou dépenser de l'argent pour embaucher un employé de plus. Je peux choisir d'économiser de l'argent et de perdre plus de temps, ou d'économiser du temps et de gagner plus d'argent. Si vous étiez moi, quel serait votre choix ?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_nw-ySjF-T_--JiT2.jpeg align="left")

En démarrant une entreprise Internet, nous devons avoir une entreprise formelle, une entité légale. Il y a un service pour cela.

J'ai utilisé [Stripe Atlas](https://atlas.stripe.com/invite/wxg9m9er) pour incorporer Listen Notes, Inc. J'ai payé 500 $, et j'ai obtenu une C Corp du Delaware en 10 jours. Stripe Atlas offre certains avantages, par exemple, 5 000 $ de crédits AWS (Amazon Web Services). Mais pour maintenir l'entreprise, je dois payer ~2 000 $/an pour les taxes, la comptabilité et autres. Cela vous donne une idée de base du coût minimum de gestion d'une entreprise.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_l-l4WwCXLziPLLHm.jpeg align="left")

Parce que nous sommes une entreprise maintenant, nous devons traiter certaines questions juridiques. Il y a un service pour cela.

Vous pouvez utiliser [Clerky](https://www.clerky.com/) pour générer des documents juridiques ou utiliser [UpCounsel](https://www.upcounsel.com/rf/CvryzEze) pour obtenir un avocat. J'ai utilisé les deux services. Ils ne sont pas parfaits, mais ils valent l'argent. Vous ne pouvez pas vous attendre à obtenir des services de niveau Ritz-Carlton avec un prix McDonald's, n'est-ce pas ? Si vous voulez être heureux, vous feriez mieux de fixer le bon niveau d'attente.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_0bVKZbAgNClaVQ85.jpeg align="left")

Pour commencer, vous avez juste besoin d'un nom de domaine suffisamment bon — un domaine .com à 10 $/an. Vous pouvez toujours acheter un excellent nom de domaine plus tard.

Par exemple, Dropbox a utilisé getdropbox.com pendant plus de 2 ans avant d'acheter dropbox.com pour 300 000 $. Comment ai-je découvert ce genre d'anecdote ? J'écoute des podcasts ! Il y avait [une interview en podcast de Drew Houston](https://www.listennotes.com/clips/334-drew-houston-the-billionaire-founder-of-RUThbQcPekK/) (cofondateur et PDG de Dropbox), où il parlait de la façon dont ils ont sécurisé le nom de domaine dropbox.com.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_ADgueIJbGpwHov-7.jpeg align="left")

Après avoir obtenu un nom de domaine, assurez-vous de créer également un ensemble de comptes d'entreprise sur les sites de réseaux sociaux tels que Twitter, Facebook, Instagram et (peut-être) Snapchat.

Et la plupart des entreprises utilisent simplement [G Suite](https://gsuite.google.com/) pour leur email d'entreprise, qui est essentiellement Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_aJpa4rgV5Hj12KNg.jpeg align="left")

Les entreprises Internet construisent des services en ligne. La plupart des logiciels aujourd'hui sont des services en ligne. Si vous ne pouvez pas accéder à Internet, vous ne pouvez pas utiliser la plupart des applications sur votre téléphone.

Les services en ligne suivent généralement le modèle client/serveur. Le logiciel côté client envoie des requêtes au côté serveur et obtient des réponses pour rendre l'interface utilisateur ou pour effectuer certaines tâches.

Tous les sites web sont des services en ligne, évidemment. Nous utilisons des navigateurs web pour accéder aux sites web. Dans une certaine mesure, les applications mobiles sont des navigateurs spécialisés.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_afLXTGIgvm3BU7Hj.jpeg align="left")

Côté serveur, nous exécutons des serveurs. Vous avez juste besoin de serveurs suffisamment bons pour commencer. Par « serveurs », j'entends VPS (Virtual Private Servers), qui fournissent essentiellement un accès root à une adresse IP. Une fois que vous vous connectez en ssh à une adresse IP (un VPS), vous pouvez faire ce que vous voulez, par exemple, installer des logiciels et y mettre votre code. Et vous êtes maintenant ouvert aux affaires.

Pour les VPS, je recommande d'utiliser quelque chose de simple au début, par exemple, [DigitalOcean](https://m.do.co/c/2288c0b7e091) ou [AWS Lightsail](https://aws.amazon.com/lightsail/). Chez Listen Notes, nous avons utilisé [DigitalOcean](https://m.do.co/c/2288c0b7e091) pendant environ un an parce que c'est bon marché et facile à configurer, puis nous sommes passés à AWS EC2 lorsque notre site web a eu plus de trafic et que nous avions besoin de plus de flexibilité et d'une configuration « production ».

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_LxybEVeLPU7uck2_.jpeg align="left")

Une telle architecture backend est assez courante pour exécuter un service en ligne.

Le côté client (par exemple, les navigateurs) envoie des requêtes. L'équilibreur de charge distribue les requêtes uniformément aux serveurs web. Nous exécutons généralement beaucoup de serveurs web, où le code côté serveur est en cours d'exécution (par exemple, Rails, Django...). Nous avons besoin d'un datastore pour stocker nos données. Les serveurs web interagissent avec le datastore pour lire et écrire des données.

Du côté gauche, c'est le traitement synchrone. Voici une requête, et le serveur web la traite et retourne une réponse immédiatement. C'est synchrone.

Nous avons également besoin de traitement asynchrone pour gérer les tâches non urgentes, longues ou intensives en calcul. Nous ne voulons pas consommer des ressources de calcul pour de telles tâches sur le serveur web. Nous externalisons donc généralement de telles tâches pour que les workers les traitent. Les serveurs web placent des messages dans la file d'attente des messages, et les workers prennent les messages pour traiter les tâches.

Par exemple, nous générons ce type d'image pour les résultats de recherche sur Listen Notes ([Exemple](https://lnns.co/uzSXWqJbg9Y)) :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_G6ulti1avYqc2hqd.png align="left")

Ce type de tâche de génération d'image est assez intensive en calcul et n'est pas urgent. Nous l'externalisons donc pour que les workers la traitent, au lieu de la gérer sur les serveurs web.

Enfin, il doit y avoir un Scheduler pour les travaux planifiés basés sur le temps. De nombreuses entreprises utilisent simplement des cron jobs sur Linux et passent à autre chose lorsqu'elles deviennent plus grandes (par exemple, [J'ai construit un système Scheduler pour mon ancien employeur Nextdoor il y a quelques années pour remplacer les cron jobs](https://engblog.nextdoor.com/we-don-t-run-cron-jobs-at-nextdoor-6f7f9cc62040)). Pour Listen Notes, nous avons beaucoup de travaux planifiés basés sur le temps, par exemple, envoyer des [Listen Alerts](https://www.listennotes.com/alerts/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_N2yqsvWuyxZtT6CC.jpeg align="left")

Nous utilisons Nginx comme un simple équilibreur de charge. Le code backend est principalement en Python/Django. Nous utilisons différents datastores pour différents usages. Nous utilisons Postgres pour le datastore principal, qui est notre seule source de vérité. Nous sommes un moteur de recherche, donc nous utilisons Elasticsearch. Nous utilisons Redis pour beaucoup de choses, mais surtout pour le cache et l'implémentation de certaines fonctionnalités « rapides » comme [Listen Real-Time](https://www.listennotes.com/realtime/).

Pour le traitement asynchrone, nous utilisons [Celery](http://www.celeryproject.org/), [Celery Beat](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html), et [RabbitMQ](https://www.rabbitmq.com/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_C2dVWNEIv_f_pQHA.jpeg align="left")

Nous devons maintenir les processus côté serveur en fonctionnement 24/7. Nous ferions mieux d'utiliser un gestionnaire de processus pour redémarrer automatiquement les processus s'ils plantent. Nous utilisons beaucoup [Supervisor](http://supervisord.org/) chez Listen Notes.

Deux recommandations ici :

* Apprenez les piles technologiques de vraies entreprises sur [stackshare.io](https://stackshare.io/stacks/trending)

* Écoutez [Software Engineering Daily](https://www.listennotes.com/podcasts/software-engineering-daily-software-Gw1zYJbjPF-/). Ils interviewent des ingénieurs de vraies entreprises, donc vous pouvez apprendre comment les entreprises font de l'ingénierie.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_EeishiFBoh3ISQWh.jpeg align="left")

En tant qu'utilisateurs finaux, nous recevons des tonnes de notifications des services en ligne via email, SMS et notifications push. Lorsqu'un chauffeur Uber approche, nous recevons des notifications push. Lorsque nous faisons des achats sur Amazon, nous recevons des notifications par email (généralement avec des reçus). Lorsque nos comptes bancaires rencontrent des problèmes, nous recevons des notifications SMS.

Inversons la situation. Lorsque nous construisons des services en ligne, comment envoyons-nous des notifications aux utilisateurs ? Il y a un service ou une API pour chaque canal de notification, par exemple, [SendGrid](https://sendgrid.com/) ou [Amazon SES](https://aws.amazon.com/ses/) pour les emails, [Twilio](https://www.twilio.com/) pour les SMS...

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_SrGLHpymGagenKzF.jpeg align="left")

Ensuite, nous avons besoin de certains types de déclencheurs pour initier les notifications.

Un type de déclencheur provient des actions de l'utilisateur. Par exemple, un utilisateur peut inviter des personnes à contribuer à la même playlist sur [Listen Later](http://listennotes.com/listen). Lorsqu'il ou elle clique sur le bouton d'invitation, cela déclenche une notification par email qui est envoyée au contributeur potentiel. Le serveur web place donc un message dans la file d'attente des messages, et l'un des workers prend le message et envoie l'email d'invitation plus tard.

Un autre type de déclencheur provient des planifications basées sur le temps, par exemple, envoyer des emails à ces 500 personnes à 7 heures du matin tous les matins.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_Kvjr0cWa0iTIZnyH.jpeg align="left")

Chacun des blocs dans le diagramme d'architecture représente un processus ou plusieurs processus sur les systèmes d'exploitation. Nous pouvons exécuter ces processus sur un serveur ou plusieurs serveurs.

Nous créons généralement une provision de plusieurs ensembles de serveurs pour différents publics et à différentes fins.

Chaque ensemble de serveurs s'exécute dans un environnement séparé.

Les serveurs dans l'environnement de production servent le trafic en direct. Le public est composé d'utilisateurs réels.

Les serveurs dans l'environnement de staging sont principalement pour les tests. Le public est composé d'employés de l'entreprise. Nous avons besoin de l'environnement de staging pour tester manuellement les fonctionnalités du produit avant de publier le tout en production.

Et nous avons besoin d'un environnement de développement à des fins de développement, qui est généralement utilisé par un seul développeur.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_eiriAOpM2vrtUpSJ.jpeg align="left")

Pour Listen Notes, nous utilisons [Vagrant](https://www.vagrantup.com/) et [VirtualBox](https://www.virtualbox.org/) pour configurer une machine virtuelle. Et nous exécutons tout à l'intérieur de cette machine virtuelle.

Puisque le code backend de Listen Notes est principalement écrit en Python/Django, j'utilise PyCharm pour écrire du code. Je sais, ce n'est pas [VS Code](https://code.visualstudio.com/) ou un autre éditeur de texte cool que les autres utilisent. Mais je suis 1000 fois plus productif en utilisant PyCharm qu'en utilisant d'autres éditeurs de texte — bien que j'ai été un utilisateur de Vim pendant 5 ans et un utilisateur d'Emacs pendant 6 autres années :) C'est comme certaines personnes aiment la nourriture épicée, tandis que d'autres non. Nous ne pouvons pas blâmer les gens qui n'aiment pas la nourriture épicée, n'est-ce pas ? Ne vous impliquez pas dans la guerre religieuse des IDE, des langages, des technologies... FAIRE AVANCER LES CHOSES est plus important.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_En1rYW0gxYbkH0FA.jpeg align="left")

En termes d'ingénierie front-end, je n'ai pas grand-chose à partager ici. Listen Notes n'a qu'un site web. Nous n'avons pas d'applications natives (sauf pour [une application expérimentale Just Listen](https://www.listennotes.com/labs/)).

Pour le front-end web, j'utilise Reactjs conventionnel et [Bootstrap](https://getbootstrap.com/). Assez standard de nos jours.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_NWGlzjmYMHId1cl-.jpeg align="left")

Si vous commencez tout juste vos projets, je vous suggérerais de vous concentrer sur une seule plateforme d'abord. Ne devenez pas multiplateforme trop tôt. Nous avons généralement des ressources très limitées au tout début. Regardez Instagram : lorsqu'ils étaient une entreprise indépendante, ils n'avaient qu'une application iOS initialement. Et ils ont été rachetés pour 1 milliard de dollars.

Si vous construisez un site web, assurez-vous de le rendre réactif dès le premier jour. Vous pouvez facilement utiliser les outils de développement des navigateurs modernes pour tester différentes tailles d'écran (par exemple, [sur Chrome](https://developers.google.com/web/tools/chrome-devtools/device-mode/)).

Vous voulez également tester sur plusieurs systèmes d'exploitation et navigateurs. Il y a un service pour cela : utilisez [BrowserStack](https://www.browserstack.com/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_tIQlkg6S1V_gTR3S.jpeg align="left")

Si vous avez plus d'un serveur, vous feriez mieux de NE PAS installer de logiciels et faire la configuration manuellement. L'infrastructure en tant que code est une pratique courante dans les entreprises Internet de nos jours. Basiquement, nous codifions la spécification des serveurs et automatisons la configuration des serveurs.

Pour Listen Notes, nous utilisons [Ansible](https://docs.ansible.com/ansible/latest/index.html). Nous devons écrire un ensemble de fichiers de configuration yml pour spécifier quel logiciel installer et où mettre les fichiers de configuration. Lorsque nous exécutons ansible-playbook en ligne de commande, il configurera automatiquement plusieurs serveurs pour nous.

De nos jours, les serveurs sont élastiques ou même éphémères, avec des configurations à la demande pour répondre à la charge de travail nécessaire. Les serveurs viennent et partent. Vous pouvez exécuter plus de serveurs pendant la journée, lorsqu'il y a plus de trafic ; et exécuter moins de serveurs la nuit, lorsqu'il y a moins de trafic. L'infrastructure en tant que code rend ce type de chose facile.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_-sbGXk-jXJ2PNmuB.jpeg align="left")

Les entreprises Internet déploient du code assez fréquemment de nos jours, au moins une fois par semaine ou même plusieurs fois par jour. Certaines entreprises font du déploiement continu, en livrant du code dès qu'il y a un nouveau commit git.

Pour Listen Notes, j'ai un script rapide pour déployer du code, où je peux spécifier l'environnement de déploiement, le type de serveur et le SHA du commit git comme paramètres. Je peux donc appuyer sur un bouton et déployer une version spécifique du code (par exemple, HEAD, ou n'importe quel commit git) sur des serveurs spécifiques (par exemple, web, API, worker...) dans un environnement spécifique (par exemple, production, staging...).

Nous déployons du nouveau code, mais nous ne publions pas nécessairement de nouvelles fonctionnalités. De nos jours, nous faisons des [feature toggles](https://martinfowler.com/articles/feature-toggles.html) dans le code, qui sont essentiellement des instructions if-else. Nous pouvons cacher le nouveau code derrière une instruction if, et nous utilisons la variable de feature toggle pour contrôler l'exécution ou non du nouveau code. Nous stockons généralement la variable de feature toggle dans un type de datastore, par exemple, Redis. Nous pouvons faire très sophistiqué ici. Nous pouvons activer la nouvelle fonctionnalité pour 10 % des utilisateurs d'abord, puis 20 %, puis 50 %, puis 100 %.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_DtYd8dMFgOhu0yB2.jpeg align="left")

Les services en ligne doivent être disponibles 24/7. Il est donc important d'avoir des outils pour la surveillance et les alertes.

Il y a un service pour cela !

De nombreuses entreprises utilisent [Datadog](https://www.datadoghq.com/). Nous utilisons Datadog chez Listen Notes également. Nous pouvons facilement construire des graphiques de surveillance pour fournir une grande visibilité des serveurs et des applications. Nous pouvons également configurer des alertes lorsque certaines métriques sont anormales (par exemple, supérieures à un certain seuil).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_MN8jF4VJZncXH3jS.jpeg align="left")

Si vous voulez apprendre les meilleures pratiques pour construire et exploiter des services en ligne, lisez [The Twelve-Factor App](https://12factor.net/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_3c2lMu1346EFUJWr.jpeg align="left")

En ce qui concerne les outils internes, je vois cette image d'iceberg. Les outils internes sont un gros morceau de code comme un iceberg se cachant sous l'eau, invisible pour les étrangers.

Si vous n'avez jamais exploité un service en ligne populaire auparavant, vous ne serez pas conscient que vous devez construire beaucoup d'outils à utiliser en interne (par vous-même, par vos employés).

Différentes entreprises construisent différents outils internes pour divers usages. Jusqu'à présent, j'ai construit certains outils internes pour aider au développement (par exemple, prévisualiser les notifications par email sans réellement envoyer les emails), pour fournir une vue de Dieu (par exemple, voir les requêtes de recherche, extraire rapidement des infos pour un utilisateur particulier...), et pour lutter contre les mauvais acteurs (par exemple, modération de contenu, détection de spam...).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_1i-QbtebgVN1Lqxe.jpeg align="left")

Donc, à ce stade, nous savons comment démarrer une entreprise avec 500 $ et nous savons comment construire un service en ligne avec une ingénierie suffisamment bonne.

Profit !

Oh, attendez...

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_ws52_8ACRqslINf7.jpeg align="left")

Comment les gens trouvent-ils ce que vous avez construit ? Comment gagnez-vous de l'argent ?

[Le PDG de Pinterest dit que la clé du succès était le marketing, pas l'ingénierie.](https://www.cbsnews.com/news/pinterest-ceo-says-key-to-success-was-marketing-not-engineering/) Eh bien, c'est tellement vrai.

L'ingénierie est déterministe. Le marketing et les affaires sont non déterministes. Si vous voulez construire un service en ligne, vous pouvez le construire. Mais nous vivons dans un monde bruyant maintenant. Des tonnes de choses se disputent notre attention. Le marketing est super difficile.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_bDYZs0OyffawGACf.jpeg align="left")

Je ne suis pas un expert en marketing. Je cherche toujours comment faire un meilleur marketing moi-même...

Il existe plusieurs canaux que vous pouvez utiliser pour diffuser vos messages. Essayez-les tous. Trouvez le plus efficace. Doublez sur celui-ci. Une recommandation ici : [Les 19 canaux que vous pouvez utiliser pour obtenir de la traction](https://medium.com/@yegg/the-19-channels-you-can-use-to-get-traction-93c762d19339)

Si vous voulez faire du SEO, vous pouvez trouver de bons tutoriels sur Internet. Mais généralement, vous voulez rendre votre site web aussi rapide que possible. Google préfère les sites web rapides de nos jours.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_U6_Pa-7K1NiY2yhE.jpeg align="left")

Le meilleur document SEO est [de Google](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) lui-même.

Et si vous êtes curieux du trafic d'un site web, utilisez simplement [l'extension chrome de SimilarWeb](https://chrome.google.com/webstore/detail/similarweb-traffic-rank-w/hoklmmgfnpapgjgcpechhaamimifchmp?utm_source=chrome-ntp-icon). Le nombre n'est pas 100 % précis, mais devrait être du même ordre de grandeur :)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_luegMv5EuB6OA3_U.jpeg align="left")

Une entreprise Internet gagne de l'argent en vendant des vues aux annonceurs ou en vendant des biens/services directement aux utilisateurs.

Chez Listen Notes, nous faisons les deux. Nous diffusons des publicités avec une combinaison de [Carbon Ads](https://www.carbonads.net/) et de ventes directes (gérées via [Google Ad Manager](https://admanager.google.com/home/)). Nous vendons également une API aux développeurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_-GXgPMkqZ1WJnvn9.jpeg align="left")

Vous pourriez me demander pourquoi je n'utilise pas les technologies XYZ. Eh bien, je suis une personne pratique. Le but est de faire avancer les choses, et non de faire de la technologie pour le plaisir de faire de la technologie.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_PQhWAP2aaAXa9USS.jpeg align="left")

En particulier, je préfère les technologies ennuyeuses, qui existent généralement depuis de nombreuses années, voire des décennies. Consultez [cet article de blog sur la pile technologique de Listen Notes](https://broadcast.listennotes.com/the-boring-technology-behind-listen-notes-56697c2e347b).

L'ingénierie logicielle de nos jours est principalement pilotée par Google et StackOverflow :) Si vous avez besoin d'aide, vous pouvez trouver plus d'informations sur les anciennes technologies matures à partir de Google et StackOverflow — mais comme beaucoup de choses dans nos vies, ce n'est pas toujours vrai.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_2EC6RMZx08CthnRL.jpeg align="left")

Je dois vous dire une mauvaise nouvelle : il est impossible pour vous de venir avec une idée de startup 100 % originale de nos jours. Si vous pensez que votre idée est unique et originale, il est plus probable que vous ne lisiez pas assez de livres ou n'écoutiez pas assez de podcasts :)

Lorsque j'ai mentionné « il y a un outil/service pour cela », c'est une startup en soi. Vous pouvez emprunter leurs idées et construire une meilleure version. Ou vous pouvez aborder des problèmes similaires sous un angle différent.

Oh, et voici une vidéo sur la technologie de Facebook en 2005 : [https://www.youtube.com/watch?v=xFFs9UgOAlE](https://www.youtube.com/watch?v=xFFs9UgOAlE)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_cD-AyO5meslYf6y2.jpeg align="left")

D'accord. Vous pouvez démarrer une entreprise AUJOURD'HUI !

*Quatre-vingts pour cent du succès, c'est de se présenter*

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_WEQS02kCfZ-YsXHl.jpeg align="left")

Vous pouvez trouver le deck ici : [http://bit.ly/good-enough-tech](http://bit.ly/good-enough-tech)

Et vous pouvez toujours me parler de manière asynchrone par email :)

---

Si vous aimez les podcasts, essayez [Listen Notes](https://www.listennotes.com/).

Si vous voulez construire une application de podcast, essayez [Listen API](https://www.listennotes.com/api/).