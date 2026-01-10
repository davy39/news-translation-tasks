---
title: Livrer un projet d'envergure dans des délais serrés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T12:58:37.000Z'
originalURL: https://freecodecamp.org/news/delivering-a-big-project-to-a-tight-deadline-4645aa62886d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: development
  slug: development
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Livrer un projet d'envergure dans des délais serrés
seo_desc: 'By Paul McGillivray

  This week we launched the first phase of a large website for a fast-growing business,
  ‘Jump In’. The company was opening another new trampoline park this week, and wanted
  the website to go live beforehand. So our deadline was fixe...'
---

Par Paul McGillivray

Cette semaine, nous avons lancé la première phase d'un site web d'envergure pour une entreprise en pleine croissance, « Jump In ». L'entreprise ouvrait un nouveau parc de trampolines cette semaine et souhaitait que le site soit en ligne avant l'ouverture. Notre échéance était donc fixe, et nous nous étions engagés à lancer un site web complet et de haute qualité à temps pour le lancement.

Avec seulement deux semaines et demie pour construire le site une fois les designs approuvés, toute l'équipe a dû, euh, « se jeter à l'eau » (jump in) et s'unir pour livrer un projet dont nous étions fiers.

C'était le premier test « à l'épreuve du feu » pour notre équipe fraîchement reconstruite ici chez Remote. Ce fut donc un excellent processus et nous avons beaucoup appris sur notre façon de travailler ensemble et sur la performance de notre nouveau workflow sous pression.

J'ai pensé qu'il serait utile de partager les points qui nous ont aidés à garder le cap et à lancer le site à temps.

### **Priorisez vos user stories**

Pour tous nos projets, nous utilisons le classique backlog de User Stories avec un tableau Kanban pour la gestion de nos tâches. Étant une société de développement .NET, nous avons inévitablement fini par utiliser Visual Studio Team Services, que nous avons trouvé intuitif, simple et puissant. Par le passé, nous avons travaillé avec [TargetProcess](https://www.targetprocess.com/), [ActiveCollab](https://activecollab.com/), et plus récemment [Jira](https://www.atlassian.com/software/jira), avant de passer à [VSTS](https://www.visualstudio.com/team-services/).

Nous nous assurons que notre backlog de User Stories est toujours classé par ordre de priorité. Nos cœurs étant joyeusement engagés envers le Manifeste Agile, ces priorités sont les priorités métier de notre client, et non nos priorités de développement.

Cela signifie que, même si nous pourrions vraiment avoir envie de construire toute la couche métier (business layer) pour l'ensemble du projet dès le départ pour nous faciliter la tâche plus tard, la couche métier en soi n'offre aucune valeur à notre client — il ne veut pas d'une couche métier, il veut que ses clients cliquent sur un bouton « Réserver maintenant » qui fonctionne, ou qu'ils remplissent un formulaire « Contactez-nous » qui envoie les données à l'API de Constant Contact.

Nous nommons et priorisons donc nos tâches en conséquence, avec l'exigence métier la plus pressante en haut, et la couche métier est naturellement construite « au besoin ».

Nous tirons trois avantages évidents de cette méthode :

1. Nous ne nous retrouvons pas à construire une architecture pour des fonctionnalités qui ne seront jamais réalisées ou jamais utilisées.
2. Si le client doit remplacer une fonctionnalité du backlog par une autre soudainement plus urgente, nous n'avons pas perdu de temps de développement à préparer cette fonctionnalité.
3. Si, pour une raison quelconque, le client doit lancer le projet plus tôt, ou s'il manque d'argent et ne peut pas continuer le développement (bien que cela ne nous soit jamais arrivé), le projet aura déjà été construit avec les fonctionnalités les plus importantes, et celles laissées de côté seront celles qui importent le moins.

C'est une façon de travailler rassurante et efficace.

### **Créez une checklist préalable**

Dans le feu de l'action, à quelques heures de l'échéance, il peut être facile d'oublier les petites choses qui restent pourtant essentielles au lancement d'un projet.

Établir une checklist dès le début du projet peut vous aider à rester concentré dans le feu de la bataille, et peut également vous donner des indications sur ce que vous pourriez faire tôt, avant que la pression ne monte. Des éléments relativement mineurs et petits en termes de développement peuvent causer de gros problèmes plus tard s'ils sont oubliés ; des choses comme le code de suivi Google Analytics et les redirections 301 des pages de l'ancien site vers leurs nouveaux remplaçants.

Nous avons créé des tâches de user story pour chaque élément et les avons placées au bas du backlog, de sorte qu'une fois toutes les fonctionnalités principales téléchargées et testées, nous savions que ces tâches devaient également être effectuées avant le lancement.

Il existe d'excellentes checklists web disponibles en ligne qui pourraient vous aider à réfléchir à ce que vous devez inclure.

[http://frontendchecklist.io](http://frontendchecklist.io/) est un projet open source créé par David Dias qui est incroyablement complet et très populaire sur GitHub en ce moment, avec de nombreuses contributions de la communauté. La [checklist Humaan Website](https://humaan.com/checklist/) est à la fois esthétique et complète, tout comme [webdevchecklist.com](http://webdevchecklist.com/)

Tom Houdmont a écrit un [article très détaillé et utile sur box UK](https://www.boxuk.com/insight/blog-posts/the-ultimate-website-launch-checklist) concernant les points à ne pas oublier. Et si vous voulez aller plus loin, l'excellent Smashing Magazine propose une liste de pas moins de [45 checklists pour sites web](https://www.smashingmagazine.com/2009/06/45-incredibly-useful-web-design-checklists-and-questionnaires/) couvrant toutes les spécialités du web.

### **Obtenez les informations importantes dès le départ**

Maintenant que nous avons notre checklist de fin de phase, nous savons ce que nous devrons savoir avant le lancement. Il est vraiment utile d'obtenir immédiatement toute information ou ressource manquante, afin de ne pas oublier de la demander dans le feu de l'action plus tard.

Croyez-moi, rien n'est plus décourageant que de se donner corps et âme pour respecter l'échéance d'un projet, pour se rendre compte à la toute dernière minute que vous n'avez pas reçu de copie du certificat SSL pour le nouveau site, et que vous devrez attendre des heures pour qu'un nouveau soit traité parce que le responsable informatique du client n'a pas de copie de la clé privée.

Identifiants DNS, ID Google Analytics, certificat SSL, et tout autre document, image ou ressource dont vous pourriez avoir besoin pendant le développement du projet — tout ce que vous pouvez obtenir dès le départ pourrait vous faire gagner des heures plus tard, quand cela comptera vraiment.

### **Ne laissez pas la dérive du périmètre détruire vos délais**

Lorsque le client commence à voir le projet se développer, de nouvelles idées non prévues initialement peuvent arriver en masse. Des suggestions pour une nouvelle façon d'afficher les données aux fonctionnalités et sections entières qui avaient été oubliées ou omises du cahier des charges, il peut être tentant de voir la nouvelle fonctionnalité « indispensable » et de tout arrêter pour l'ajouter au projet. C'est très bien, mais rappelons-nous d'abord l'essentiel.

Il y a un vieil adage dans le monde du développement logiciel : « Qualité, Budget ou Temps : choisissez-en deux ». Nous n'aimons pas cela. Nous ne voulons jamais faire de compromis sur la qualité, dépasser le budget ou manquer une échéance. Nous ajoutons donc un quatrième élément : le Périmètre (Scope).

Ainsi, nous maintenons notre qualité, nous respectons le budget et nous tenons nos délais, mais ce qui est livré à cette échéance fait continuellement l'objet de discussions et de réflexions.

Ainsi, lorsqu'un client demande une nouvelle fonctionnalité — en plein milieu du développement — qui prendra par exemple une demi-journée à construire, nous répondons : « certainement — quelle fonctionnalité souhaiteriez-vous retirer de cette version pour faire place à cette nouvelle fonctionnalité ? »

La discussion qui en résultera garantira que le client se concentre sur ses priorités et l'aidera à déterminer si cette nouvelle idée mérite d'être incluse dans la version actuelle ou si elle doit être reportée à une phase ultérieure. En gardant le contrôle du périmètre, nous protégeons les autres valeurs (et nos soirées). Ce qui m'amène logiquement au point suivant :

### **Maintenez un haut niveau de qualité**

De nouvelles fonctionnalités sont construites et mises en ligne rapidement à l'approche de l'échéance, et nous pouvons facilement oublier de tester aussi minutieusement que d'habitude. Et le contrôle qualité des feuilles de style et des interactions peut tout aussi facilement être compromis.

Je préfère de loin passer ce temps supplémentaire quand je suis dans le code d'une fonctionnalité pour m'assurer que je vais la livrer correctement — avec l'aspect voulu, le fonctionnement attendu, les feuilles de style correctes et une validation appropriée sur les formulaires, etc.

Je ne dis pas que nous devrions sur-développer et écrire du code inutile, mais il est beaucoup plus agréable de prendre le temps de bien faire les choses que de devoir y revenir à la demande du client alors que je suis beaucoup plus proche de l'échéance. C'est stressant, et je n'ai pas besoin de ce genre de négativité dans ma vie, merci.

Restez « lean », gardez vos patterns sous contrôle, écrivez vos tests et faites votre QA. Dès la première fois, pas au moment du lancement — ou pire, après le lancement !

### **Ne perdez pas vos processus sous la pression**

Dans la lignée de ce que je viens de dire, en plus de garder votre code propre, il est important de maintenir votre processus de gestion de projet en place lorsque vous êtes sous pression, surtout si vous travaillez en équipe.

Je suis passé par là — je manque de temps, et au lieu d'ajouter mes user stories au backlog VSTS, j'écris une petite checklist dans Notepad++ ou [Todoist](https://todoist.com/) (mon nouvel outil de productivité préféré). Avant que je m'en rende compte, aucun membre de l'équipe ne sait sur quelles tâches je travaille, personne ne sait quelles tâches ont été accomplies, et un autre membre de l'équipe de développement travaille sur quelque chose que j'ai déjà corrigé.

Respectez le processus — il y a une raison pour laquelle il est en place, sinon vous finirez par ralentir en essayant d'aller plus vite.

Il existe un livre fantastique à ce sujet intitulé « [Work Clean: The Life-Changing Power of Mise-En-Place to Organize Your Life](https://www.amazon.co.uk/Work-Clean-Life-Changing-Mise-En-Place-Organize/dp/0241200334) » de Dan Charnas. Dans ce livre, Charnas parle de « ralentir pour accélérer » — prendre le temps de s'assurer que tout est préparé et que les processus sont en place vous aide en fait à atteindre une vitesse de productivité beaucoup plus élevée lorsque vous êtes dans le flux (flow). Essayez, et jetez aussi un œil au livre ; je l'ai adoré.

### **Soyez au clair sur votre définition de « fini »**

Les user stories sont, par définition, généralement courtes et concises. Nous veillons à ce que notre gestion de projet d'inspiration agile ne se transforme pas en un simple cycle en cascade (waterfall) en discutant de chaque story au moment où elle doit être réalisée, au lieu de la spécifier en détail des semaines à l'avance.

L'inconvénient est qu'un développeur qui n'a pas été impliqué dans le processus de définition du périmètre et des spécifications n'aura pas tout l'historique d'une user story lorsqu'il la choisira en haut de la liste. Si tout le monde est concentré sur ses propres stories à l'approche de l'échéance, le développeur pourrait être tenté de simplement se lancer dans la tâche.

Dans de nombreux cas, une user story simple et concise sera facile à interpréter. Mais dans d'autres cas, le développeur pourrait se retrouver à s'égarer, travaillant sur des tâches qui n'ont tout simplement pas besoin d'être terminées pour l'échéance.

Il y a quelques mesures que nous pouvons prendre pour essayer d'éviter ce scénario :

En prenant à cœur le concept de « ralentir pour accélérer » dont je viens de parler, le développeur doit toujours discuter de la story avec le product manager s'il y a le moindre besoin de clarification.

En tant que développeurs, il peut être très facile pour nous de penser « oh c'est bon, je gère » et de simplement continuer. Mais en se rappelant que le client fait partie de l'équipe, prendre le téléphone et revoir la story avec lui peut s'avérer très éclairant la plupart du temps.

À tout le moins, une courte conversation avec la personne qui a écrit le ticket permettra de s'assurer que tout le monde est sur la même longueur d'onde.

La personne qui écrit la user story au départ devrait inclure une « définition de fini » (definition of done). Cela peut simplement être une liste de choses qui se produiront une fois la story terminée. Par exemple :

* L'utilisateur clique sur le bouton « rapports » et une liste de rapports s'affiche.
* La liste contient le nom, la description, le type de fichier et un bouton « télécharger » pour chaque rapport.
* Cliquer sur « télécharger » enregistre le rapport sur l'appareil de l'utilisateur.
* Des jetons d'accès (access tokens) doivent être utilisés lors de la récupération des téléchargements pour maintenir la sécurité des documents.

Voilà donc les principaux points qui nous ont sauvés ou qui nous ont ralentis, selon le moment où les leçons ont été apprises au cours de ce projet particulier. J'espère vraiment que vous trouverez certains de ces points utiles lorsque vous travaillerez avec des délais serrés, ou même simplement sur votre prochain projet logiciel ou web.

Nous avons encore quelques phases à réaliser, mais tant nous, chez Remote, que nos clients, Jump In, sommes ravis du site jusqu'à présent. Allez le voir sur [www.gojumpin.com](http://www.gojumpin.com/).

Publié à l'origine sur [remote.online](http://remote.online/journal/delivering-a-big-project-to-a-tight-deadline).