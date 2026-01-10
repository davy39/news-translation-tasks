---
title: Comment planifier un travail dans PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-12T14:04:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-a-job-in-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-mat-brown-552598.jpg
tags:
- name: automation
  slug: automation
- name: database
  slug: database
- name: postgres
  slug: postgres
seo_title: Comment planifier un travail dans PostgreSQL
seo_desc: 'By Jagruti Tiwari

  Scheduling allows you to automate things so you don''t have to do them in real time.

  In this article we will see how to schedule a job in PostgreSQL. We''ll use pgAgent,
  a job scheduling agent for PostgreSQL.

  How to Install PostgreSQL...'
---

Par Jagruti Tiwari

La planification vous permet d'automatiser les choses afin de ne pas avoir à les faire en temps réel.

Dans cet article, nous verrons comment planifier un travail dans PostgreSQL. Nous utiliserons pgAgent, un agent de planification de travaux pour PostgreSQL.
# Comment installer PostgreSQL et Stack Builder
Vous pouvez installer pgAgent avec Stack Builder.

Installez PostgreSQL depuis le [site officiel](https://www.postgresql.org/download/). Cela téléchargera Stack Builder avec l'installateur.

Si vous avez déjà PostgreSQL installé, vous pourriez télécharger l'installateur et exécuter Stack Builder si vous ne l'avez pas déjà.

Stack Builder s'exécute une fois l'installation de PostgreSQL terminée. J'utilise PostgreSQL14 et pgAdmin4.

# Comment installer pgAgent

Lorsque vous exécutez Stack Builder, il ouvrira d'abord un assistant de bienvenue.

![Screenshot-2022-07-10-163841_auto_x2_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163841_auto_x2_auto_x2_colored_toned_light_ai.jpg)

Si vous avez plusieurs versions de PostgreSQL installées, vous en choisirez une pour installer pgAgent.

![Screenshot-2022-07-10-163907_auto_x2_colored_toned_light_ai_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163907_auto_x2_colored_toned_light_ai_auto_x2_colored_toned_light_ai.jpg)

Sous *Adds-ons, outils et utilitaires*, vous trouverez pgAgent. Cochez la case pour l'installer.

![Screenshot-2022-07-10-163926_auto_x2_colored_toned_light_ai--1-_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163926_auto_x2_colored_toned_light_ai--1-_auto_x2_colored_toned_light_ai.jpg)

Ensuite, il vous demandera de choisir un répertoire où vous souhaitez installer pgAgent.

![Screenshot-2022-07-10-163956](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163956.png)

Stack Builder ouvrira ensuite un assistant d'installation de pgAgent.

![Screenshot-2022-07-10-164018](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164018.png)

Ici, vous choisirez si vous souhaitez l'installer en mode mise à niveau. Si vous ne souhaitez pas modifier automatiquement les scripts lors de la mise à niveau, vous pouvez cocher la case.

![Screenshot-2022-07-10-164038](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164038.png)

Dans l'assistant *Détails d'installation de PostgreSQL*, fournissez le nom d'utilisateur et le mot de passe que vous avez saisis lors de l'installation de PostgreSQL.

![Screenshot-2022-07-10-164125](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164125.png)

Si vous entrez des détails incorrects, une erreur de connexion sera générée. Assurez-vous donc de vous souvenir de ces détails.

> **_NOTE:_** Connectez-vous à PostgreSQL avec le nom d'utilisateur et le mot de passe que vous avez fournis à cette étape pour voir les *travaux pgAgent*.

![Screenshot-2022-07-10-164233](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164233.png)

Après avoir ajouté ces détails, l'installation commence :

![Screenshot-2022-07-10-164250](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164250.png)

Cela prend quelques secondes pour se terminer.

![Screenshot-2022-07-10-164304](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164304.png)

Cliquez sur le bouton *Terminer* à la fin.

![Screenshot-2022-07-10-164320](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164320.png)

Stack Builder affichera également un assistant *Installation terminée*. Il contient des instructions pour installer et désinstaller les utilitaires.

Une fois Stack Builder installé, vous l'exécutez simplement pour installer d'autres utilitaires. Pour les désinstaller, vous devez utiliser le Panneau de configuration.

![Screenshot-2022-07-10-190229](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-190229.png)

Les *travaux pgAgent* seront visibles dans l'arborescence du navigateur sur le côté gauche du tableau de bord.

![Screenshot-2022-07-10-152307-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152307-1.png)

Ci-dessus, vous pouvez voir une vue rapprochée de l'arborescence du navigateur.
# Comment créer un travail dans pgAgent

Pour créer un nouveau travail, faites un clic droit sur le bouton *pgAgent Jobs* et cliquez sur *Créer*.

![Screenshot-2022-07-10-152329-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152329-1.png)

Vous verrez un menu, et là, cliquez simplement sur *Créer* > *Travail pgAgent*.

![Screenshot-2022-07-10-191902](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-191902.png)

La boîte de dialogue *Créer un travail pgAgent* a quatre onglets.

Le premier est l'onglet *Général*. Ici, vous entrez le nom du travail et sélectionnez une catégorie.

*Catégorie* est uniquement à des fins de catégorisation interne – cela n'affecte pas la manière dont votre travail s'exécute. Vous pouvez en sélectionner une en fonction de la fonction du travail. Comme je souhaite exporter les données vers un CSV, je choisirai la catégorie *Exportation de données*.

![Screenshot-2022-07-10-152531-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152531-1.png)

Ensuite, nous cliquons sur l'onglet *Étapes* dans la boîte de dialogue *Créer un travail pgAgent*. Dans le coin supérieur droit de la boîte, vous verrez un signe +. Cliquez dessus pour ajouter une nouvelle ligne.

![Screenshot-2022-07-10-153345-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-153345-1.png)

L'onglet *Étapes* a deux sections : *Général* et *Code*.

Dans l'onglet *Général* :

1) Ajoutez le nom de l'étape.
2) Ensuite, vous *Activez* ou *Désactivez* l'étape. Votre travail ne s'exécutera que si l'étape est activée.
3) Selon que votre travail est *local* ou *distant*, vous pouvez choisir le *Type de connexion*. Je choisirai une connexion distante.
4) Une connexion distante vous permet d'ajouter manuellement la chaîne de connexion. La syntaxe doit être comme dans [libq connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING). J'ajouterai mes détails de connexion dans le même format : ```host=localhost port=5432 dbname=postgres```
5) Dans la liste déroulante *En cas d'erreur*, vous pouvez choisir ce qui doit se passer en cas d'erreur. J'ai sélectionné pour que le travail échoue.
6) Enfin, vous pouvez commenter l'étape. Ensuite, sauvegardez les modifications.

Vient ensuite la section *Code* dans l'onglet *Étapes*.
![Screenshot-2022-07-10-155158-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-155158-1.png)

Comme je souhaite exporter les données d'une vue, j'appellerai la vue et lui demanderai d'exporter le fichier. Le code sera :
```COPY (select * from acc_view) TO E'C:\\test-data\\try.csv';```

Je sauvegarderai les modifications après avoir ajouté le code.

![Screenshot-2022-07-10-153614-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-153614-1.png)

Nous sommes maintenant prêts à planifier un travail. Dans l'onglet *Planifications*, nous ajoutons la *date et heure de début* et la *date et heure de fin* pour que le travail commence et se termine.

![Screenshot-2022-07-10-163332-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163332-1.png)

*SQL* est le dernier onglet. Il montre le code généré par l'interface graphique. Si vous souhaitez planifier un travail de manière dynamique, vous devrez exécuter le code de procédure affiché ici.

# Comment voir les travaux créés dans pgAgent

Une fois qu'un nouveau travail est créé, il sera affiché sous *pgAgent jobs* dans l'arborescence du navigateur.

![Screenshot-2022-07-10-163417-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163417-1.png)

Ses *planifications* et *étapes* seront affichées lorsque vous développez le travail.

![Screenshot-2022-07-10-163540-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163540-1.png)

Pour voir si le travail a été exécuté (s'il a échoué ou réussi), vous sélectionnez le travail par son nom et cliquez sur l'onglet *Statistiques* dans le tableau de bord. Ici, vous pouvez voir le nombre de fois où le travail a été exécuté, l'heure de début et de fin, son statut et son identifiant. *s* signifie succès et *f* signifie échec dans la colonne *Statut*.

![Screenshot-2022-07-10-163639-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163639-1.png)

Pour déboguer pourquoi un travail a échoué, vous pouvez simplement cliquer sur le nom de l'étape sous *Étapes* dans l'arborescence du navigateur et cliquer sur *Statistiques* dans le tableau de bord. Dans la colonne *Sortie*, vous pouvez voir pourquoi le travail a échoué.

Dans mon cas, il n'a pas pu accéder au répertoire auquel je tentais de copier les données. Une fois que j'ai changé le chemin, mon travail a été exécuté avec succès (notez la première ligne).

# Comment modifier les travaux dans pgAgent
Pour modifier un travail dans pgAgent, vous sélectionnez le travail et cliquez sur l'onglet *Propriétés* dans le tableau de bord.

![Screenshot-2022-07-10-201542](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-201542.png)

Cliquez sur l'icône du crayon dans le coin supérieur gauche, cela ouvrira un assistant où vous pourrez modifier tous les détails.
# Conclusion
Il n'est pas toujours faisable de créer des planificateurs dans votre code, mais lorsque c'est une option, cela peut être vraiment utile.

La planification de travaux couplée à l'exportation de données au format CSV est une fonctionnalité puissante de PostgreSQL. J'essaierai d'expliquer comment créer un travail de manière dynamique dans le prochain tutoriel. Bon apprentissage.