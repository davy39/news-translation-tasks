---
title: Guide GSoC 2023 – Comment se préparer au Google Summer of Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-16T17:04:36.000Z'
originalURL: https://freecodecamp.org/news/google-summer-of-code-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-prateek-katyal-2763246.jpg
tags:
- name: gsoc
  slug: gsoc
- name: open source
  slug: open-source
seo_title: Guide GSoC 2023 – Comment se préparer au Google Summer of Code
seo_desc: "By Abhisman Sarkar\nGoogle Summer of Code is an open source program that\
  \ is managed by Google's Open Source team. \nThey invite developers to spend their\
  \ summer contributing to the source code for various different organisations taking\
  \ part in the prog..."
---

Par Abhisman Sarkar

[Google Summer of Code](https://summerofcode.withgoogle.com/) est un programme open source géré par l'équipe Open Source de Google.

Ils invitent les développeurs à passer leur été à contribuer au code source de diverses organisations participant au programme.

De nombreuses organisations listent leurs idées de projets pour que les participants puissent y faire leur choix. L'année dernière, lors de la [saison 2022](https://summerofcode.withgoogle.com/archive/2022/organizations), pas moins de 202 organisations différentes ont participé au programme, et celui-ci s'est achevé avec environ 1 166 projets menés à bien.

Pensez à la quantité phénoménale de code qui a été écrite et à quel point les organisations open source et les utilisateurs en général en ont bénéficié. Vous pouvez en savoir plus sur la saison dernière [ici](https://opensource.googleblog.com/2022/12/gsoc-2022-its-wrap.html).

J'ai fait partie de ces contributeurs, en écrivant du code pour le projet [TUF](https://theupdateframework.io/). Mon travail consistait à introduire la rétrocompatibilité dans le client Python de TUF afin que le téléchargement de métadonnées respectant différentes versions de TUF puisse être facilement géré.

J'écris ce tutoriel pour vous faire découvrir le GSoC et vous expliquer comment augmenter vos chances d'être sélectionné dans le programme. Je passerai également en revue la manière dont cela vous bénéficiera, tant du point de vue de l'apprentissage que de la carrière. J'espère que cela vous inspirera suffisamment pour contribuer à l'open source et postuler au GSoC, même si vous ne l'avez jamais fait auparavant.

# Chronologie du GSoC

Le GSoC suit une chronologie similaire chaque année. Vous pouvez trouver la page de la session 2023 [ici](https://developers.google.com/open-source/gsoc/timeline).

La page explique à peu près tout ce que vous devez savoir, et vous y trouverez les dates précises de chaque annonce. Néanmoins, je vais partager mes conseils sur la manière de se préparer à chaque étape du voyage et les meilleures mesures à prendre en cours de route.

Les trois premières annonces sont spécifiques aux organisations (orgs). Cela signifie que vous n'avez pas à vous en soucier, car il s'agit des dates auxquelles les organisations doivent postuler pour que leurs projets soient inclus dans le programme GSoC.

## Publication de la liste des organisations de mentorat acceptées :

Une fois les organisations annoncées, commencez à parcourir la liste et jetez un œil aux idées de projets qui vous semblent intéressantes.

Ne ciblez pas trop d'organisations. Essayez de viser un maximum de 2 ou 3 idées de projets au sein de la même organisation. Cela vous permet de concentrer vos efforts sur la participation à cette organisation, ce qui augmente réellement vos chances d'être sélectionné.

Cibler trop d'organisations divise vos efforts et peut avoir pour conséquence que vous ne soyez pas admis dans le programme.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-137.png)
_Page de recherche d'organisations_

Filtrez les organisations en saisissant votre langage de programmation préféré, le nom de l'organisation ou le sujet dans la barre de recherche. Une fois que vous aurez ouvert la page d'une organisation, vous pourrez trouver les technologies et les sujets mentionnés. Jetons un coup d'œil à la page de la CNCF :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-161.png)
_Page GSoC de la CNCF_

Ici, vous pouvez voir toutes les différentes technologies et thématiques. Ne vous découragez pas si vous ne connaissez pas tous les outils, car ces listes concernent l'ensemble des idées de projets mentionnées sous l'organisation (il y a donc de fortes chances que votre projet particulier ne les nécessite pas tous). De plus, comme le programme est une expérience d'apprentissage, vous apprendrez ces sujets par vous-même.

Cliquez ensuite sur **Ideas List**, et vous serez dirigé vers une page présentant toutes les différentes idées de projets de cette organisation. C'est là que vous pourrez lire la description de chaque projet et examiner la pile technologique pour chacun d'eux.

Vous pourriez trouver l'étiquette **Difficulty** sous votre projet, mais ne vous découragez pas si un projet que vous trouvez intéressant est marqué comme difficile. Vous pouvez toujours apprendre sur le tas et mettre en œuvre ce que vous apprenez. Il est probable que vous deviez travailler un peu plus dur, mais ce n'est pas grave.

Sous l'idée du projet, vous trouverez également le dépôt amont (upstream) et/ou la page des tickets (issues) en amont. Consultez-les et commencez à lire la documentation du dépôt et toutes les autres informations.

Maintenant, vous vous demandez peut-être : où aller si vous avez des questions ? Retournez sur la page de l'organisation sur le site du GSoC et vous y trouverez des liens vers la liste de diffusion de l'organisation, le canal Slack public et Twitter, parmi divers autres liens.

Si vous ne trouvez pas ces informations ici, allez sur la page du dépôt et vous trouverez probablement les liens vers les canaux de communication dans le fichier Readme.

Après avoir rejoint le canal public, présentez-vous et exprimez votre enthousiasme à l'idée de contribuer au projet.

Lorsque vous posez des questions, voici quelques points à garder à l'esprit. Tout d'abord, assurez-vous de faire vos propres recherches en cherchant votre question en ligne, puis posez-la en disant : « Bonjour, j'ai ce problème. J'ai fait telle recherche à ce sujet et j'ai trouvé telle réponse, bien que je pense qu'elle puisse être incorrecte. J'apprécierais que quelqu'un puisse m'aider, merci. »

Formuler votre question ainsi montre aux autres que vous avez réfléchi à votre problème, que vous avez essayé de chercher en ligne et que vous n'avez pas simplement abandonné sans réfléchir. Les gens seront alors plus enclins à vous aider.

Bien souvent, si votre question est assez courante, vous trouverez la réponse réelle en ligne. De plus, avec la prolifération des outils d'IA, il y a de fortes chances que vous trouviez ce dont vous avez besoin. Si ce n'est pas le cas, allez-y et posez votre question.

De plus, essayez toujours de **ne pas** envoyer de messages personnels à quelqu'un. Posez vos questions dans les canaux publics. De cette façon, de nombreuses personnes voient votre problème et les chances de recevoir de l'aide augmentent. Envoyer un message personnel ne garantit pas toujours une réponse, car la personne est probablement occupée par son propre travail. Le fait de poser une question sans personne d'autre pour y répondre ajoute à cette charge de travail.

## Début de la période de candidature pour les contributeurs GSoC :

En tant que contributeur, vous devrez formuler une proposition pour votre idée de projet spécifique avant une date limite.

Pour la session 2023, les propositions des contributeurs commencent à être acceptées à partir du 20 mars jusqu'à la date limite du 4 avril. Commencez à travailler sur vos propositions à l'avance et n'attendez pas la date limite de soumission.

Voici quelques conseils de ma part :

### Commencez le processus de révision tôt

Il est tout à fait acceptable de demander à votre mentor de réviser votre premier brouillon de proposition, mais essayez de commencer le processus de révision le plus tôt possible. Mettez en œuvre les suggestions de votre mentor, puis demandez à nouveau des révisions.

Ce faisant, soyez respectueux de leur temps. Ils peuvent ne pas être toujours disponibles ; dans ce cas, essayez d'obtenir des commentaires d'autres mainteneurs travaillant sur le projet.

Gardez toujours à l'esprit que les mainteneurs sont des personnes qui ont une vie professionnelle et privée séparée et qu'ils travaillent sur le projet pendant leur temps libre.

### Créez un calendrier

Une bonne proposition est un aspect important du processus de sélection. [Cette page](https://google.github.io/gsocguides/student/writing-a-proposal#submit-a-proposal-early) contient de bonnes informations concernant les sous-thèmes que vous devriez mentionner.

Assurez-vous de formuler un calendrier approprié (section Deliverable), car cela montre au mentor et aux mainteneurs que vous avez réellement réfléchi au projet et à la manière dont vous comptez le résoudre. Les dates réelles auxquelles vous mettriez en œuvre quelque chose n'ont pas vraiment d'importance ; il s'agit davantage de la façon dont vous avez envisagé la résolution du projet.

Personnellement, la création d'un calendrier a eu un impact majeur sur mon processus de sélection, car ma mentore a mentionné à plusieurs reprises qu'elle aimait la façon dont j'avais pensé à la mise en œuvre du projet.

Cela montre vraiment que vous avez suffisamment réfléchi au problème pour proposer une approche pour le résoudre.

### Contribuez au dépôt du projet

Contribuez et travaillez sur des tickets (issues) dans le dépôt du projet. Il n'est pas nécessaire qu'il s'agisse de changements majeurs, mais assurez-vous qu'ils ne soient pas uniquement triviaux (comme corriger la grammaire, supprimer des fichiers, etc.).

À mesure que vous commencez à contribuer, commencez par des problèmes faciles et montez en puissance au fur et à mesure que vous maîtrisez le projet. Si vous débutez dans tout cela, comprenez que la première étape est généralement la plus difficile et que les suivantes sont comparativement moins ardues.

Lors de la formulation de votre proposition, n'oubliez pas de mentionner ces contributions antérieures, car elles rendent votre proposition beaucoup plus percutante. Elles montrent également à votre mentor que vous êtes quelqu'un qui a déjà contribué au projet.

### Parlez de votre expérience passée

Incluez un passage sur vos expériences professionnelles passées et vos réalisations (section Biographical Information). Mentionnez des travaux pour lesquels vous avez des preuves, car cela ajoute de la valeur à votre proposition. Incluez toute expérience passée en open source, en hackathon ou en création d'applications.

Essayez de classer ces expériences par ordre de pertinence par rapport au projet et n'encombrez pas trop cette section si vous en avez trop. Limitez-vous à un maximum de 8 à 10.

En plus de tous ces points, je vous suggère de parcourir la page mentionnée ci-dessus et d'étudier les points restants pour avoir une bonne idée de ce que vous devriez mentionner dans votre proposition.

Une fois que vous avez fini de formuler une proposition, créez votre propre compte GSoC et allez sur votre page de contributeur. Vous y trouverez le lien pour sélectionner le projet sur lequel vous travaillerez et le lien pour soumettre la proposition.

En résumé, concentrez-vous sur 3 points clés lors de votre candidature :

1. Avoir de bonnes contributions de code dans le dépôt du projet.
2. Avoir une proposition de haute qualité et bien révisée.
3. Être actif dans la communauté en échangeant avec d'autres contributeurs et participants.

Quelques changements ont été mis en œuvre lors de la saison 2022 et sont là pour rester. Il s'agit de :

* **Flexibilité du calendrier du projet.** Vous pouvez prendre entre 10 et 22 semaines pour terminer votre projet. Prolongez votre délai si vous estimez que la période de 12 semaines n'est pas suffisante, mais assurez-vous d'en communiquer avec votre mentor.

* **Choix de l'engagement temporel.** Vous aurez le choix entre un projet de durée moyenne ou longue.

* **Ouvert à tous.** Le GSoC était un programme réservé aux étudiants jusqu'à sa saison 2021. Mais depuis la saison 2022, le programme a commencé à accepter tout le monde, étudiant ou non. Quiconque souhaite intégrer ce programme peut se lancer.

La date limite de dépôt des candidatures pour la saison 2023 est le 4 avril, et vous recevrez une réponse le 4 mai.

Je sais, un mois semble long et vous serez probablement anxieux à l'approche de la date des résultats. Je l'étais aussi. Si vous êtes sélectionné, félicitations pour votre travail acharné.

Mais si vous ne l'êtes pas, ne soyez pas déçu, car vous aurez probablement appris énormément sur l'open source tout au long du processus. Et vous pouvez maintenant travailler à soumettre votre candidature pour d'autres programmes de mentorat open source. [Cette page](https://github.com/deepanshu1422/List-Of-Open-Source-Internships-Programs) contient d'excellentes informations sur tous les autres programmes.

## Pourquoi vous devriez faire le GSoC

Jusqu'à présent, nous avons parlé de la chronologie et de la préparation de votre proposition. Parlons maintenant du pourquoi.

Pourquoi devriez-vous vous intéresser à ce programme et à l'open source en général ? Commençons par parler de l'open source.

### Pourquoi l'open source ?

Travailler sur des **logiciels Open Source** est un excellent moyen d'aider la communauté au sens large en contribuant à des projets utilisés par des millions de personnes à travers le monde. Le travail que vous fournissez aide à améliorer des logiciels qui sont des éléments importants de nombreux systèmes à grande échelle.

De plus, le fait que presque tous les logiciels open source soient gratuits permet à chacun de les utiliser dans sa vie quotidienne, qu'il s'agisse de grandes organisations ou d'un utilisateur ordinaire. Consacrer du temps de votre vie bien remplie à travailler sur l'OSS est donc un exploit formidable et louable.

Tout cela semble génial, mais **comment le fait de contribuer à l'open source vous aide-t-il à subvenir à vos besoins ?** Travailler sur l'open source vous permet d'acquérir une expérience de niveau industriel. Vous apprendrez ce que c'est que de travailler réellement sur de grands projets.

Étant moi-même contributeur, j'ai eu le plaisir d'en apprendre énormément sur la manière de travailler concrètement sur des changements. De nombreux facteurs entrent en jeu, tels que le téléchargement du code source, l'ajout de modifications au code, l'exécution de tests, le test manuel des modifications en créant un binaire, le push des modifications, et ainsi de suite. Tant de choses à apprendre.

Étant moi-même étudiant à l'université, je n'ai pas eu à attendre un emploi pour découvrir l'industrie. Tout ce que j'avais à faire était de travailler dur et de contribuer à des projets open source.

Voici quelques extraits du [10ème rapport annuel sur les emplois Open Source](https://www.linuxfoundation.org/research/the-10th-annual-open-source-jobs-report) de la Linux Foundation qui pourraient vous inspirer :

> Selon 93 % des responsables du recrutement interrogés, les talents en open source sont de plus en plus difficiles à trouver. En conséquence, les entreprises se tournent désormais vers la formation de leur personnel aux nouveaux outils d'automatisation du cloud, d'orchestration et de productivité des développeurs pour combler cet écart autant que possible.

> La grande majorité des employeurs (93 %) signalent des difficultés à trouver suffisamment de talents possédant des compétences en open source. Cette tendance n'est pas près de disparaître, avec près de la moitié (46 %) des employeurs prévoyant d'augmenter leurs recrutements en open source au cours des six prochains mois, et 73 % des professionnels de l'open source affirmant qu'il serait facile de trouver un nouveau poste s'ils décidaient de changer.

Le rapport poursuit en expliquant comment les entreprises sont prêtes à offrir une rémunération plus élevée aux professionnels de l'open source et comment les incitations financières font une différence beaucoup plus grande. Je vous recommande de lire et de télécharger le rapport pour obtenir une description beaucoup plus détaillée.

En résumé, l'open source est un excellent moyen pour vous d'apprendre et d'acquérir des connaissances concrètes, tout en vous fournissant des compétences qui vous aideront à vous démarquer sur ce marché du travail compétitif.

### Comment le GSoC aide-t-il ?

Nous avons parlé des avantages de l'open source et de la manière dont il vous aide à acquérir de nombreuses compétences réelles. La question se pose alors : quel rôle joue le GSoC là-dedans ?

Travailler sur un dépôt et contribuer au code est formidable, mais cela peut sembler vraiment intimidant. Dans le cadre d'un programme de mentorat comme le GSoC, vous travaillez sur une idée de projet avec l'aide d'un guide qui est un mentor expérimenté. Il vous aidera tout au long du processus. Sur une période de 3 mois ou plus, cela booste réellement vos compétences et fait de vous un bien meilleur développeur qu'auparavant.

Vous développerez de nombreuses nouvelles compétences tout en apprenant à coder en équipe. Votre contribution au code aide également le projet à se développer, car vous travaillerez à la mise en œuvre de diverses fonctionnalités importantes. Cela profite à la fois au projet et à la communauté open source en général.

Lorsque je participais au GSoC, j'ai beaucoup appris sur la collaboration, les bonnes pratiques de code, l'utilisation de Git et énormément sur les tests. J'ai pu comprendre les pratiques asynchrones (async) et comment communiquer mes avancées à mon équipe, même si nous étions dans des fuseaux horaires différents.

J'étais responsable du code que je soumettais et de la livraison du travail que l'on attendait de moi. Je pense que cela m'a vraiment aidé à grandir en tant que personne et à devenir un meilleur développeur.

J'ai également pu apprendre énormément sur ce que c'était réellement de travailler sur un projet concret et acquérir une telle expérience de niveau industriel auprès de professionnels aussi talentueux. C'est devenu une expérience que je chérirai toujours.

Grâce à ce programme, vous découvrez le monde de l'open source et rencontrez des développeurs formidables qui font un effort supplémentaire pour que les logiciels open source restent gratuits et accessibles à tous. Vous êtes introduit dans une merveilleuse communauté de développeurs passionnés et partageant les mêmes idées, qui sont extrêmement accueillants et prêts à aider d'autres développeurs en herbe.

Vous recevez également une allocation pendant que vous travaillez à l'écriture de code pour ces organisations, ce qui, je pense, est aussi un excellent point positif. Tout cela fait de la contribution à l'Open Source via le GSoC une expérience d'apprentissage incroyable que chaque développeur devrait, selon moi, pouvoir apprécier.

### Merci de m'avoir lu !

C'est tout pour le moment ! Si vous avez décidé de postuler au GSoC, bonne chance. J'espère que vous apprécierez le processus, que vous apprendrez beaucoup et que vous vous amuserez à contribuer à l'open source.