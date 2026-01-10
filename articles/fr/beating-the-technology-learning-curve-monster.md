---
title: Comment vaincre le monstre de la courbe d'apprentissage technologique
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-17T13:16:00.000Z'
originalURL: https://freecodecamp.org/news/beating-the-technology-learning-curve-monster
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca164740569d1a4ca4e59.jpg
tags:
- name: learning
  slug: learning
- name: technology
  slug: technology
seo_title: Comment vaincre le monstre de la courbe d'apprentissage technologique
seo_desc: Doing what I do for a living, which these days mostly involves creating
  technology books and courseware, I’m constantly learning new technologies. In a
  way, my new tech adventures are not much different than the ones most IT pros face,
  except that mi...
---

Faire ce que je fais pour gagner ma vie, ce qui ces jours-ci implique principalement la [création de livres et de supports de cours sur la technologie](https://bootstrap-it.com/), j'apprends constamment de nouvelles technologies. En un sens, mes aventures technologiques ne sont pas très différentes de celles auxquelles sont confrontés la plupart des professionnels de l'informatique, sauf que les miennes arrivent probablement plus souvent.

Parce qu'il y a tant de choses qui dépendent de ma compréhension de la nouvelle plateforme ou du nouveau processus — et tant d'autres plateformes et processus plus récents qui attendent mon attention une fois que j'ai terminé avec celui-ci — mon objectif principal est d'entrer et de sortir le plus rapidement possible.

Essayer d'organiser les couches de complexité et les métaphores de conception inhérentes à une technologie tout en luttant pour déterminer si elle fera exactement ce que je veux peut parfois être carrément intimidant. Sans un bon plan d'attaque, je suis dans l'impasse.

Avant de partager quelques-uns des outils que j'ai utilisés avec succès dans mon propre apprentissage, il vaut la peine de discuter d'une technologie (relativement) nouvelle dans le monde réel.

Il y a quelque temps, la société de surveillance de la gestion des opérations ScienceLogic a [mené une enquête](https://www.sciencelogic.com/company/news/releases/28-percent-information-technology-pros-fear-cloud-adoption) auprès de plus de mille professionnels de l'entreprise et de l'informatique, cherchant à connaître leurs opinions sur l'adoption du cloud. Bien qu'il soit clair que de plus en plus de la charge de travail informatique est transférée vers les fournisseurs de cloud (avec Amazon Web Services en tête de file selon toutes les métriques), il existe une préoccupation profonde et généralisée quant à l'impact que ce changement pourrait avoir.

31 % des répondants ont estimé qu'ils manquaient des compétences pour diriger en toute confiance un déploiement cloud, 50 % ont affirmé qu'ils manquaient des outils pour gérer correctement l'infrastructure dans le cloud, et 28 % craignaient que le passage au cloud ne mette en danger leurs emplois actuels.

Ça vous dit quelque chose ? Plus le changement est rapide et perturbateur, plus nous nous inquiétons tous de la manière — ou si — nous allons suivre. Et si vous pensez que Joe, le professionnel de l'informatique, passe des nuits blanches à se demander comment il va tout comprendre, montrez un peu de sympathie pour son manager qui est responsable de faire entrer tout un département dans le cloud.

AWS est particulièrement dans mes pensées en ce moment parce que mon livre Wiley/Sybex « [AWS Certified Cloud Practitioner Study Guide](https://www.amazon.com/gp/product/1119490707/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1119490707&linkCode=as2&tag=projemun-20&linkId=c407a50c1752a2bc7d9ff3ea66ac8cdc) » vient de sortir. AWS était une technologie avec laquelle j'ai d'abord eu du mal à comprendre il y a plus d'une décennie lorsque j'avais besoin de construire mon propre système de webconférence public (en utilisant BigBlueButton). Ce fut un long voyage entre ce premier serveur EC2 et le niveau de confort et l'expérience approfondie que j'ai atteints avant de tenter d'écrire le livre, mais les choses que j'ai faites correctement — et incorrectement — en faisant ces premiers pas ont grandement contribué à façonner la manière dont j'enseigne maintenant les sujets informatiques.

## Séquentiel vs scan-and-run

La manière dont vous allez apprendre une compétence dépend en partie de ce que vous prévoyez apprendre. Si vous cherchez une introduction qui vous mènera de zéro à fonctionnel sur un environnement full-stack et multi-niveaux comme AWS, alors vous pourriez être plus en sécurité en allant de manière séquentielle. Commencer par le début peut vous aider à éviter de manquer des détails critiques — comme le fonctionnement de la facturation ou de la sécurité sur AWS. Croyez-moi : si vous n'aimez pas l'idée de frais de service mensuels à quatre chiffres ou d'une infrastructure compromise, alors vous ne voulez pas sauter les bases de la facturation et de la sécurité.

Mais si c'est un logiciel autonome (comme une [technologie de virtualisation](https://www.freecodecamp.org/news/linux-server-virtualization-the-basics/) ou un nouvel IDE) que vous pouvez tester en toute sécurité quelques fois dans votre propre réseau avant de le déployer réellement, alors plus rapide est mieux. Pour ce type de projet, je lance souvent un conteneur Linux propre en utilisant LXC (que je trouve bien préférable à Docker pour explorer de nouveaux logiciels) ou, lorsque l'application avec laquelle je travaille nécessite un accès au noyau de l'hôte (comme SELinux), une [machine virtuelle Linux sur Virtual Box](https://www.freecodecamp.org/news/how-to-create-a-virtual-it-workspace-16927c0f3535/?source=rss----336d898217ee---4).

Par « scan-and-run », j'entends soigneusement élaborer une chaîne de recherche sur DuckDuckGo.com (ou l'un de ces autres moteurs de recherche dont les noms m'échappent pour l'instant), rapidement extraire les informations que vous voulez des résultats, et les essayer sur votre serveur virtuel jetable. Ça n'a pas fonctionné ? Félicitations. Vous venez d'apprendre quelque chose que vous ne saviez pas encore.

Assurez-vous simplement de bien documenter à la fois vos échecs et vos succès afin de ne pas avoir à tourner en rond dans le même parc encore et encore.

## La ligne de commande

Étant donné le choix, je préfère généralement travailler à partir de la ligne de commande Bash plutôt que des consoles GUI. Ce n'est pas parce que je suis un snob de la ligne de commande (bien que je le sois), mais je trouve que la nature non ambiguë et traçable d'une CLI fonctionne bien avec les expériences itératives. En langage clair, cela signifie qu'il est plus facile de retracer mes étapes pour déterminer exactement ce qui a fonctionné et ce qui n'a pas fonctionné. Et n'oubliez pas que les messages d'erreur Bash peuvent facilement être recyclés en recherches internet fantastiques.

Un autre avantage de la CLI : les motifs prévisibles d'un environnement shell bien conçu peuvent rendre encore plus facile l'anticipation des fonctionnalités qu'une GUI web bien conçue. Permettez-moi d'illustrer cela en utilisant la CLI AWS. Une fois installée et correctement configurée, même l'exécution de `aws` sans aucun argument vous donnera quelque chose d'utile. Remarquez comment la sortie vous guide pour ajouter `help` à toute commande partiellement complétée pour retourner une assistance contextuelle.

> *$ aws*  
> *usage: aws \[options\] \[ \] \[parameters\]*  
> *To see help text, you can run:*

> *aws help*  
> *aws help*  
> *aws help*  
> *aws: error: too few arguments*

Il est vrai qu'il y a beaucoup d'aide disponible via la GUI : toutes les pages de la console AWS ont des liens vers des ressources de documentation étendues. Mais ce serait la documentation AWS qui, bien que bien écrite et soigneusement maintenue, est généralement très, très verbeuse et parfois un peu confuse. Les documents CLI en ligne sont beaucoup plus ciblés et vous font entrer et sortir plus rapidement.

Le simple fait d'être familier avec la manière d'accéder à ce type d'informations peut vous rendre beaucoup plus rapide et plus efficace... même pendant les premières étapes de l'apprentissage. Et la structure de base est disponible bien au-delà d'AWS.

![Image](https://cdn-media-1.freecodecamp.org/images/0*l7aSgokWBmg6e6E7.jpg align="left")

*Manning's* [*Learn Amazon Web Services in a Month of Lunches*](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&a_bid=1c1b5e27)

D'un autre côté, comme je l'ai écrit dans mon livre "Learn AWS in a Month of Lunches", je pense que la console navigateur AWS est en fait un meilleur endroit pour commencer à comprendre le fonctionnement du cloud d'Amazon. C'est parce que la structure de haut niveau joue un rôle si important dans la compréhension de la manière dont les dizaines et dizaines de services AWS fonctionnent ensemble, et le site web fait un si bon travail de visualisation. Mais peut-être que c'est juste moi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pxkXha80CKi8vXaff7KxIA.png align="left")

*Documentation officielle AWS — complète avec des illustrations utiles*

## Faites-le vous-même

Plus que toute autre chose, votre apprentissage sera le plus efficace si vous retroussez vos manches et essayez par vous-même. Non seulement vous devriez dupliquer les exemples de documentation, mais aussi changer les paramètres pour voir ce qui se casse. Ensuite, planifiez et exécutez vos propres projets basés sur les technologies que vous apprenez. Appliquer vos connaissances au monde réel est crucial.