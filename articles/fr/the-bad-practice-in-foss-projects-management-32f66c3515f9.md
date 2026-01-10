---
title: Ne limitez pas le potentiel de votre projet open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-21T21:01:02.000Z'
originalURL: https://freecodecamp.org/news/the-bad-practice-in-foss-projects-management-32f66c3515f9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xyb4yDofTG6gYGzA0mvU9w.jpeg
tags:
- name: Free Software
  slug: free-software
- name: open source
  slug: open-source
- name: openstack
  slug: openstack
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Ne limitez pas le potentiel de votre projet open source
seo_desc: 'By Julien Danjou

  During the OpenStack summit a few weeks ago, I had the chance to talk to some people
  about my experience on running open source projects. It turns out that after hanging
  out in communities and contributing to many projects for years,...'
---

Par Julien Danjou

Lors du sommet OpenStack il y a quelques semaines, j'ai eu l'occasion de parler à certaines personnes de mon expérience dans la gestion de projets open source. Il s'avère qu'après avoir traîné dans des communautés et contribué à de nombreux projets pendant des années, je peux peut-être fournir un certain recul et un regard externe à beaucoup de ceux qui sont nouveaux dans ce domaine.

Il existe de nombreuses ressources expliquant comment gérer un projet open source. Aujourd'hui, je souhaite aborder un angle différent et souligner ce que vous ne devriez pas faire _socialement_ dans vos projets. Cette liste provient de divers projets open source que j'ai rencontrés ces dernières années. Explorons ces mauvaises pratiques et illustrons-les avec des exemples.

#### Ne percevez pas les nouveaux contributeurs comme une nuisance

Lorsque les développeurs de logiciels et les mainteneurs sont occupés, il y a une chose dont ils n'ont pas besoin : plus de travail. Pour beaucoup de gens, la réaction instinctive à une contribution externe est : zut, plus de travail. Et en fait, c'est le cas.

Ainsi, certains mainteneurs tendent à éviter ce surplus de travail. Ils déclarent explicitement qu'ils ne veulent pas de contributions, ou ils font sentir aux contributeurs, de manière passive-agressive, qu'ils ne sont pas les bienvenus. Cela peut prendre de nombreuses formes différentes, de les ignorer à être désagréable. Cela permet au mainteneur du projet d'éviter de coacher les nouveaux contributeurs sur la manière dont ils peuvent contribuer de manière productive au projet.

C'est l'une des plus grosses erreurs que vous puissiez faire dans l'open source. Si les gens vous envoient plus de travail, vous devriez faire tout ce qui est nécessaire pour les faire sentir les bienvenus, afin qu'ils continuent à travailler avec vous. Très vite, ils pourraient devenir les personnes qui font le travail que vous faites, au lieu de vous. Pensez simplement : retraite !

Prenons l'exemple de mon ami Gordon, qui a commencé en tant que contributeur à Ceilometer en 2013. Il faisait de grandes revues de code, mais en fait, il me donnait plus de travail en détectant des bugs dans mes patches et en m'envoyant des patches que je devais revoir. Au lieu d'être un tyran pour qu'il arrête de me faire retravailler mon code et revoir ses patches, [j'ai demandé que nous lui fassions encore plus confiance en l'ajoutant en tant que relecteur principal](http://lists.openstack.org/pipermail/openstack-dev/2013-May/008975.html).

Si les contributeurs ne sont pas capables de faire leur première contribution, ils ne feront certainement pas une seconde. Ils n'en feront aucune. Et le projet pourrait très bien avoir perdu ses futurs mainteneurs.

#### Ne limitez pas vos contributeurs à des tâches ingrates

Lorsque de nouveaux contributeurs arrivent et veulent contribuer à un projet particulier, ils apportent avec eux une grande variété de motivations. Certains d'entre eux sont des utilisateurs, mais d'autres sont simplement des personnes qui cherchent à voir à quoi ressemble la contribution à un projet open source. Ils veulent l'excitation de redonner à un écosystème qu'ils utilisent.

La réponse habituelle des mainteneurs est de pousser les gens à faire des tâches ingrates. Cela signifie faire des travaux qui n'ont aucun intérêt, peu de valeur, et probablement aucun impact direct sur le projet.

Certaines personnes n'ont en fait pas d'objection à faire des tâches ingrates, mais d'autres en ont. Certaines personnes les aimeront dès que vous leur donnerez quelque chose — n'importe quoi — à faire et une reconnaissance pour leurs efforts. Mais d'autres se sentiront offensés que vous leur ayez demandé de faire un travail à faible impact. Soyez conscient de cela, et assurez-vous de faire un high-five aux personnes qui font vos tâches ingrates. C'est la seule façon de les garder autour de vous.

![Image](https://cdn-media-1.freecodecamp.org/images/PtYAzAz-LaY1ESGGJJLPw4TeyRqe8ccXFDtM)

#### N'oubliez pas de louer même les petites contributions

Lorsque la première pull request qu'un nouveau contributeur envoie est juste une correction de faute de frappe, certains développeurs se sentiront agacés à l'idée de perdre un temps précieux à vérifier une contribution si petite. Et personne ne se soucie de l'anglais approximatif dans leur documentation de toute façon, n'est-ce pas ?

Mes premières contributions à [home-assistant](https://github.com/home-assistant/home-assistant/commit/36cb12cd157b22bdc1fa28b700ca0fb751cca7a4) et [Postmodern](https://github.com/marijnh/Postmodern/commit/ec537f72393e1032853b78e0b7b4d0ff98632a02) consistaient à corriger des fautes de frappe dans leur documentation.

J'ai contribué à [Org-mode](http://orgmode.org/) pendant quelques années. [Mon premier patch pour orgmode](http://repo.or.cz/org-mode.git/commit/a153f5a31dffbc6b78a8c5d8d027961abe585a38) concernait la correction d'une docstring. Ensuite, j'ai envoyé 56 patches, corrigeant des bugs et ajoutant des fonctionnalités avancées. J'ai également écrit quelques modules externes. À ce jour, je suis toujours #16 sur la liste des principaux contributeurs d'Org-mode, qui compte 390 contributeurs. Ainsi, j'ai fini par être bien plus qu'un petit contributeur à leur projet. Je suis assez sûr qu'en rétrospective, leur communauté était heureuse de ne pas avoir rejeté ma correction de documentation comme une perte de leur temps.

#### Ne fixez pas la barre trop haut pour les nouveaux venus

![Image](https://cdn-media-1.freecodecamp.org/images/9zgly5UpeD17kYmC8wK7DsPnEA2TQ0aNfqZr)

Lorsque de nouveaux contributeurs arrivent, leurs connaissances sur le projet, son contexte et les technologies peuvent varier largement. L'une des erreurs que les mainteneurs de projets font souvent est de demander aux contributeurs d'effectuer une série de tâches compliquées avant de pouvoir contribuer. Cela peut avoir pour effet de faire fuir de nombreux contributeurs qui sont relativement timides ou introvertis. Ils peuvent simplement disparaître, se sentant trop stupides pour aider.

Avant de faire tout commentaire, vous ne devriez faire aucune supposition sur leurs connaissances. Vous devez également être très délicat lorsque vous évaluez les compétences des contributeurs, car certaines personnes pourraient se sentir vexées si vous les sous-estimez trop.

Une fois que leur niveau de compétence a été correctement évalué (quelques échanges devraient suffire), vous devez mentorat votre contributeur au bon degré afin qu'il puisse s'épanouir. Cela prend du temps et de l'expérience pour maîtriser cela, et vous risquez probablement d'en perdre certains en cours de route, mais c'est un chemin que chaque mainteneur doit prendre.

Le mentorat est un aspect très important de l'accueil des nouveaux contributeurs à votre projet, quel qu'il soit. Le mentorat s'applique également bien en dehors du logiciel libre.

#### Ne faites pas faire de sacrifices aux gens pour qu'ils vous aident

![Image](https://cdn-media-1.freecodecamp.org/images/lc02j3EgHpqE5-Cv7MFB5DyCZGf83DA7ChBN)

C'est un aspect qui varie beaucoup en fonction du projet et du contexte, mais c'est vraiment important. En tant que projet de logiciel libre, où la plupart des gens contribueront de leur propre bonne volonté et parfois sur leur temps libre, vous ne devez pas leur demander de faire de grands sacrifices. Cela ne fonctionnera pas.

L'une des pires choses que vous puissiez faire est de demander aux contributeurs de voler 5 000 kilomètres pour se rencontrer en personne et discuter du projet. Cela place les contributeurs dans une position inéquitable, en fonction de leur capacité à quitter leur famille pendant une semaine, à prendre un avion/bateau/voiture/train, à louer un hôtel, etc. Ce n'est pas bien, et vous devriez faire tout ce qui est en votre pouvoir pour éviter d'_exiger_ des contributeurs qu'ils fassent cela afin de participer au projet et de se sentir inclus dans sa communauté.

Ne vous méprenez pas. Je ne dis pas que les activités sociales devraient être interdites. Tout au contraire. Évitez simplement d'exclure des personnes lorsque vous discutez de tout projet.

Le même principe s'applique à toute autre forme de discussion qui rend la participation de tous compliquée : réunions IRC (il est difficile pour certaines personnes de bloquer une heure, surtout en fonction du fuseau horaire dans lequel elles vivent), visioconférence (surtout en utilisant des logiciels non libres), etc.

Tout ce qui demande aux gens d'interagir avec le projet de manière synchrone pendant une période de temps leur imposera des contraintes qui peuvent les mettre mal à l'aise.

Le meilleur moyen est encore l'e-mail et ses dérivés asynchrones (comme les systèmes de suivi de bugs) qui permettent aux gens de travailler à leur propre rythme sur leur propre temps.

#### N'oubliez pas que vous avez un Code de Conduite — écrit ou implicite

Les codes de conduite semblent être un sujet à la mode (et un sujet délicat), alors que de plus en plus de communautés s'ouvrent à un public plus large qu'auparavant — ce qui est formidable.

En fait, toutes les communautés ont un code de conduite, qu'il soit écrit avec de l'encre noire, ou porté dans l'esprit de chacun de manière inconsciente.

Maintenant, en fonction de la taille de votre communauté et de la manière dont vous vous sentez à l'aise pour l'appliquer, vous pouvez vouloir l'écrire dans un document, comme [Debian l'a fait](https://www.debian.org/code_of_conduct).

Avoir un code de conduite ne transforme pas magiquement toute la communauté de votre projet en une bande de nounours qui suivent ses directives. Mais cela fournit un artefact intéressant auquel vous pouvez vous référer lorsque cela est nécessaire. Vous pouvez le lancer à certaines personnes, pour indiquer que leur comportement n'est pas le bienvenu dans le projet, et d'une certaine manière, faciliter leur exclusion potentielle — même si personne ne veut généralement aller aussi loin, et c'est rarement aussi utile.

Je ne pense pas qu'il soit obligatoire d'avoir un tel document pour les petits projets. Mais vous devez garder à l'esprit que le code de conduite implicite sera dérivé de _votre_ propre comportement. La manière dont vos leader(s) communiquent avec les autres déterminera l'ambiance sociale de l'ensemble du projet. Ne sous-estimez pas cela.

Lorsque nous avons commencé le projet [Ceilometer](http://launchpad.net/ceilometer), nous avons implicitement suivi le [Code de Conduite d'OpenStack](https://www.openstack.org/legal/community-code-of-conduct/) avant même qu'il n'existe, et nous avons probablement fixé la barre un peu plus haut. En étant gentils, accueillants et ouverts d'esprit, nous avons atteint un score de diversité décent, avec jusqu'à 25 % de notre équipe principale étant des femmes — bien au-dessus du ratio actuel dans OpenStack et la plupart des projets open source !

![Image](https://cdn-media-1.freecodecamp.org/images/haNLTaYddoJRNdL9Uq4j0SnEzOcojkL5gNuO)

#### Ne faites pas sentir aux non-anglophones qu'ils sont des étrangers

Il est assez important d'être conscient que la grande majorité des projets de logiciels libres utilisent l'anglais comme langue commune de communication. Cela a beaucoup de sens : c'est une langue couramment parlée, et elle semble bien faire le travail.

Mais une grande proportion des hackers ne sont pas des locuteurs natifs de l'anglais. Beaucoup ne sont pas capables de parler anglais couramment. Cela signifie que le rythme auquel ils peuvent avoir une conversation peut être lent, ce qui peut frustrer les locuteurs natifs de l'anglais.

La principale démonstration de ce phénomène peut être observée lors d'événements sociaux (par exemple, des conférences) où les gens débattent. Il peut être très difficile pour les gens d'expliquer leurs pensées en anglais et de communiquer correctement à un rythme décent, rendant la conversation et la transmission des idées lentes.

La pire chose que l'on puisse voir dans ce contexte est un locuteur natif de l'anglais coupant la parole aux gens et les ignorant, simplement parce qu'ils parlent trop lentement. Je comprends que cela peut être frustrant, mais le problème ici n'est pas le non-locuteur natif de l'anglais — c'est que le médium utilisé ne place pas vos collègues codeurs sur un terrain de jeu égal que la conversation asynchrone le ferait.

Dans une moindre mesure, le même principe s'applique aux réunions IRC, qui sont relativement synchrones. Les médias complètement asynchrones n'ont pas ce défaut, et c'est pourquoi ils devraient également être préférés.

#### Pas de vision, pas de délégation

L'une des tragédies les plus courantes dans le monde de l'open source est de voir un mainteneur lutter avec la croissance de son projet tandis que d'autres contributeurs tentent sans succès de l'aider.

En effet, lorsqu'un afflux de nouveaux contributeurs commence à demander de nouvelles fonctionnalités, des retours ou des directions, certains mainteneurs s'étouffent et ne savent pas comment répondre. Cela finit par frustrer les contributeurs, qui peuvent donc simplement disparaître.

Il est important d'avoir une vision pour votre projet et de la communiquer. Faites savoir clairement à vos contributeurs ce que vous voulez et ne voulez pas dans votre projet. Transmettre cela de manière claire (et non agressive, s'il vous plaît) est un bon moyen de réduire les frictions entre les contributeurs. Ils sauront très vite s'ils veulent rejoindre votre navire ou non, et à quoi s'attendre. Alors soyez un bon capitaine.

S'ils choisissent de travailler avec vous et de contribuer, vous devriez commencer à leur faire confiance dès que possible, et déléguer certaines de vos responsabilités. Cela peut être n'importe quelle tâche que vous faisiez vous-même : revoir des patches ciblant un sous-système, corriger des bugs, ou écrire des docs.

Laissez les gens posséder une partie entière du projet, afin qu'ils se sentent responsables et s'en soucient autant que vous. Faire le contraire — être un maniaque du contrôle — est votre meilleur moyen de rester seul avec votre logiciel open source. Et aucun projet ne va croître et devenir réussi de cette manière.

En 2009, lorsque Uli Schlachter a envoyé [son premier patch à awesome](http://article.gmane.org/gmane.comp.window-managers.awesome.devel/1746/match=uli+schlachter), cela représentait plus de travail pour moi. Je devais revoir ce patch, et j'étais déjà assez occupé à concevoir les nouvelles versions d'awesome et à faire mon travail de jour ! Le travail d'Uli n'était pas parfait, et j'ai dû le corriger moi-même. Plus de travail. Et qu'ai-je fait ? Quelques minutes plus tard, je [lui ai répondu](http://article.gmane.org/gmane.comp.window-managers.awesome.devel/1747/match=uli+schlachter) avec un plan clair de ce qu'il devait faire, et ce que je pensais de son travail.

En réponse, Uli a envoyé des patches et amélioré le projet. Savez-vous ce qu'Uli fait aujourd'hui ? Il gère le projet du gestionnaire de fenêtres awesome, et ce depuis 2010 au lieu de moi. J'ai réussi à transmettre ma vision, à la déléguer, et puis à prendre ma retraite !

#### Soyez prudent pour reconnaître tous les types de contributions

Les gens contribuent de différentes manières, et ce n'est pas toujours avec du code. Il y a beaucoup de tâches entourant les projets de logiciels libres : documentation, tri des bugs, support utilisateur, design de l'expérience utilisateur, communication, traduction…

Par exemple, il a fallu un certain temps à [Debian](http://debian.org/) pour reconnaître qu'ils devraient accorder à leurs traducteurs le statut de Développeur Debian. [OpenStack](http://openstack.org/) travaille dans la même direction en essayant de [reconnaître les contributions non techniques](https://wiki.openstack.org/wiki/NonATCRecognition).

Dès que votre projet commence à attribuer des badges à certaines personnes et à créer différentes classes de membres dans la communauté, vous devez être très prudent pour ne pas oublier personne. C'est la route la plus facile pour perdre des contributeurs en cours de route.

![Image](https://cdn-media-1.freecodecamp.org/images/apEMscaPcDbRHgxm2XT8b0hOpQAeAKSRcynN)

#### N'oubliez pas d'être reconnaissant

Cette liste entière a été inspirée par de nombreuses années de hacking open source et de contributions à des logiciels libres. Faites-moi savoir dans la section des commentaires si vous avez quelque chose qui vous a empêché de contribuer à des projets open source. Merci pour la lecture !

> Article original à [https://julien.danjou.info/blog/2016/foss-projects-management-bad-practice](https://julien.danjou.info/blog/2016/foss-projects-management-bad-practice)