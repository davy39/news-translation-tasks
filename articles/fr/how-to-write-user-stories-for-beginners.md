---
title: 'Comment rédiger des User Stories pour débutants : Agile en pratique'
subtitle: ''
author: Ben
co_authors: []
series: null
date: '2024-12-16T19:38:16.101Z'
originalURL: https://freecodecamp.org/news/how-to-write-user-stories-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734447615195/2b7c6025-bce2-447e-a685-19f785dcd402.png
tags:
- name: agile
  slug: agile
- name: agile development
  slug: agile-development
- name: user stories
  slug: user-stories
seo_title: 'Comment rédiger des User Stories pour débutants : Agile en pratique'
seo_desc: 'In this tutorial, you’ll learn about an important part of the Agile approach
  to software development: user stories.

  I’ll take you through what user stories are, common pitfalls that I’ve seen with
  creating user stories, and the frameworks that exist ...'
---

Dans ce tutoriel, vous apprendrez une partie importante de l'approche Agile pour le développement logiciel : les user stories.

Je vais vous expliquer ce que sont les user stories, les pièges courants que j'ai observés lors de leur création, et les frameworks qui existent pour valider si votre user story est "bonne".

### Voici ce que nous allons couvrir :

* [Les débuts de l'Agile](#les-debuts-de-lagile)
    
* [Qu'est-ce que l'Agile ?](#quest-ce-que-lagile)
    
* [Qu'est-ce qu'une User Story ?](#quest-ce-quune-user-story)
    
    * [Structure d'une User Story](#structure-dune-user-story)
        
    * [Exemple de User Stories](#exemple-de-user-stories)
        
* [Comment créer de bonnes User Stories](#comment-creer-de-bonnes-user-stories)
    
* [Pièges courants dans la création de User Stories](#pieges-courants-dans-la-creation-de-user-stories)
    
    * [Se concentrer sur les aspects techniques](#se-concentrer-sur-les-aspects-techniques)
        
    * [Collaboration des parties prenantes](#collaboration-des-parties-prenantes)
        
    * [User Stories vagues](#user-stories-vagues)
        
* [Comment commencer avec les User Stories](#comment-commencer-avec-les-user-stories)
    
* [Conclusion](#conclusion)
    

## Les débuts de l'Agile

Il est probable que vous ayez déjà entendu parler du développement Agile et des User Stories. Mais si ce n'est pas le cas, faisons un bref rappel historique :

Les User Stories font partie d'un concept plus large appelé méthodologies Agile.

Les méthodologies Agile existent depuis 2001, lorsque 17 ingénieurs logiciels respectés se sont réunis dans une station de ski de l'Utah et ont créé le désormais célèbre [Manifeste Agile](https://agilemanifesto.org/).

Si des noms comme Robert Martin, Martin Fowler et Kent Beck ne vous disent rien, une fois que vous aurez terminé cet article, allez les chercher. Ils possèdent une richesse de connaissances et ont offert au monde du logiciel une manière plus fluide de livrer des projets, appelée Agile.

## Qu'est-ce que l'Agile ?

Agile est davantage une manière de penser qu'une méthode prescrite. Des méthodes prescrites existent, comme Scrum et Kanban, mais Agile est un concept.

Agile promeut la collaboration, les retours rapides et la livraison fréquente de valeur à l'utilisateur.

La manière de penser Agile encourage la flexibilité dans la planification des projets, ce qui contraste fortement avec son concurrent de l'époque, la planification de projet en cascade (Waterfall), qui était très rigide sur ce qui était livré et quand.

Les méthodologies Agile promeuvent la réalisation de "juste assez" de recherche au début pour lancer le projet, puis l'apprentissage, l'itération et la modification de la conception et des livrables selon les besoins tout au long du projet jusqu'à la livraison du code final. Cette approche "changer et apprendre en cours de route" est appelée "planification adaptative".

Agile promeut la livraison rapide et fréquente de quelque chose de valeur, généralement sous la forme de la livraison de code en production à la fin de chaque "sprint" de deux semaines. Cela est très différent de la planification traditionnelle en cascade, qui nécessitait souvent des mois de développement avant qu'un changement visible par l'utilisateur puisse être livré en production.

Un autre aspect clé de l'Agile est l'accent qu'il met sur la collaboration étroite et fréquente des parties prenantes. Le produit, la QA, l'ingénierie et les ventes ont tous une grande contribution et un retour constant sur le projet tout au long du cycle de vie du projet.

Maintenant que vous en savez un peu plus sur le fonctionnement de l'Agile, plongeons plus profondément dans la manière dont nous validons la valeur pour l'utilisateur.

Entrez dans l'univers des User Stories.

![Photo par Mikhail Nilov : https://www.pexels.com/photo/a-hand-pointing-the-sticky-note-on-the-wall-6592358/](https://cdn.hashnode.com/res/hashnode/image/upload/v1733997119683/6002c66a-b11c-4607-a37f-36480a970099.jpeg align="center")

## Qu'est-ce qu'une User Story ?

Une user story est un moyen en anglais simple de connecter l'ingénieur à l'objectif final du logiciel.

Elle est conçue de sorte qu'une personne non technique puisse la lire et comprendre ce qui est livré, et qu'un ingénieur puisse la regarder et voir la valeur et comment valider que vous avez livré cette valeur.

### Structure d'une User Story

> En tant que [type d'utilisateur], lorsque je [effectue une action], [résultat attendu]

À sa base, c'est tout.

Vous mettez l'accent sur l'utilisateur final et la "valeur" que vous allez livrer.

Examinons les entrées :

* **Type d'utilisateur** : Il n'existe pas d'utilisateur "taille unique". Vous avez des "utilisateurs administrateurs", des "utilisateurs connectés", des "utilisateurs avec la permission X" ou des "utilisateurs dans le rôle Y". Cela précise qui effectue l'action.
    
* **Effectuer une action** : Que fait l'utilisateur ? Clique-t-il sur le bouton "connexion" ? Supprime-t-il un enregistrement ? Soumet-il un formulaire ?
    
* **Résultat attendu** : Une fois que votre utilisateur a effectué l'action, que devrait-il se passer ? S'il a cliqué sur "connexion" avec l'adresse e-mail et le mot de passe corrects, où devrait-il être dirigé ? S'il a cliqué sur "connexion" avec une adresse e-mail et un mot de passe incorrects, que devrait-il se passer ?
    

### Exemple de User Stories

Examinons des exemples de user stories pour une page de connexion.

Rien de mieux que des exemples.

Mettons la scène. Vous avez une page de connexion avec une zone de texte pour une adresse e-mail et une zone de texte pour un mot de passe. Vous avez un bouton de soumission. C'est tout.

Quelles sont les différentes permutations qui peuvent se produire sur cette page du point de vue de l'utilisateur ?

> En tant qu'utilisateur connecté, lorsque la page se charge, je suis redirigé vers la page d'accueil connectée

Si je suis déjà connecté, je ne veux pas avoir à ressaisir mes informations, redirigez-moi simplement vers la page d'accueil connectée.

> En tant qu'utilisateur non connecté, lorsque je saisis l'adresse e-mail correcte mais le mot de passe incorrect et que je clique sur Connexion, un message d'erreur apparaît

Je suis un utilisateur qui n'est pas déjà connecté et j'ai saisi des informations incorrectes. Je ne devrais pas être connecté.

> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail et un mot de passe incorrects et que je clique sur connexion, un message d'erreur apparaît.

Encore une fois. Je ne suis pas un utilisateur connecté. J'ai saisi des informations incorrectes, je ne devrais pas être connecté.

> En tant qu'utilisateur non connecté, lorsque je saisis l'adresse e-mail et le mot de passe corrects et que je clique sur connexion, je suis redirigé vers la page d'accueil connectée.

Cette fois, je ne suis pas déjà connecté, je saisis les informations correctes et je clique sur connexion. Je suis connecté au système.

Pouvez-vous voir comment toutes ces histoires sont centrées sur l'utilisateur ?

Vous avez peut-être remarqué que certains des "comportements attendus" ci-dessus ne sont pas entièrement définis. Nous aborderons cela plus tard dans les critères d'acceptation.

![Photo par cottonbro studio : https://www.pexels.com/photo/manager-considering-project-strategy-by-the-task-board-6804077/](https://cdn.hashnode.com/res/hashnode/image/upload/v1733997173211/1946f2a3-eee3-497e-960b-a6aeac9bd48d.jpeg align="center")

## Comment créer de bonnes User Stories

Il existe un bon modèle appelé le modèle INVEST qui montre très simplement comment savoir si vos user stories sont bonnes.

**Modèle INVEST** :

* **I**ndépendant : Peut être développé séparément.
    
* **N**égociable : Ouvert à la discussion et au changement.
    
* **V**alable : Livre de la valeur à l'utilisateur.
    
* **E**stimable : Peut être estimé en termes d'effort.
    
* **S**mall : Tient dans un sprint.
    
* **T**estable : A des critères d'acceptation clairs.
    

Appliquons ce modèle INVEST à l'un des exemples de user stories ci-dessus :

> En tant qu'utilisateur non connecté, lorsque je saisis l'adresse e-mail et le mot de passe corrects et que je clique sur connexion, je suis redirigé vers la page d'accueil connectée.

*(Je vais faire quelques hypothèses ici, car il s'agit d'une base de code théorique et d'un projet théorique)*

Cette histoire est-elle **Indépendante** ? Je dirais oui. C'est une petite histoire qui implique seulement quelques composants qui existent probablement déjà. Si la base de données n'a pas encore été créée pour le projet, cela nous donnerait une dépendance. Cela ne serait plus indépendant.

Est-elle **Négociable** ? Eh bien, oui. Cette histoire pourrait facilement être modifiée pour rediriger vers la page de profil de l'utilisateur plutôt que vers sa page d'accueil.

Cette histoire est définitivement **valable**. Une fois implémentée, l'utilisateur peut se connecter. Si l'histoire était :

> En tant qu'utilisateur non connecté, lorsque je saisis l'adresse e-mail et le mot de passe corrects et que je clique sur connexion, rien ne se passe

Cela ne serait pas valable. L'utilisateur n'en tirerait aucun bénéfice.

L'histoire est-elle **estimable** ? Encore une fois, nous devons faire quelques hypothèses dans ce scénario inventé, mais j'espère certainement que cela serait facilement estimable. C'est une histoire concise, impliquant peu de composants, dans un domaine que tout le monde connaît et avec des critères d'acceptation clairs.

L'histoire est certainement **petite**. Il y a peu d'ambiguïté dans ce qui doit être fait, il n'y a qu'un seul chemin utilisateur et des résultats clairs. Regardons une histoire qui serait trop grande :

> En tant qu'utilisateur non connecté, la page de connexion devrait fonctionner comme prévu.

Comme discuté plus haut dans cet article, il y a de nombreuses façons dont la page de connexion peut et devrait fonctionner. "Devrait fonctionner comme prévu" semble couvrir toutes ces permutations. Cela serait trop grand pour être efficacement dimensionné en tant qu'histoire, et probablement trop grand pour être complété en un seul sprint.

L'histoire est définitivement **Testable**. Il y a des actions utilisateur claires à entreprendre qui ont un résultat clair. Cette user story peut être couverte par des tests unitaires, des tests d'intégration et des tests manuels.

Il semble que nous ayons créé une bonne user story !

Si vous utilisez la structure que j'ai définie ci-dessus, et que l'histoire répond aux critères du modèle INVEST, c'est probablement une bonne histoire.

## Pièges courants dans la création de User Stories

J'ai vu des user stories mal tournées dans le passé où les gens ont manqué quelques aspects cruciaux de la user story :

### Se concentrer sur les aspects techniques

Comme le montrent mes exemples ci-dessus, la user story est non technique.

Il ne devrait y avoir aucune référence à un nom de service, un nom de base de données, ou une validation basée sur quelque chose que l'utilisateur ne peut pas voir.

Dès que votre histoire n'est plus compréhensible par l'utilisateur final, vous avez fait une erreur.

Concentrez-vous sur ce que l'utilisateur va faire et sur ce que l'utilisateur va voir.

Examinons un exemple d'histoire axée sur la technique :

> En tant qu'utilisateur non connecté, lorsque je clique sur le lien de mot de passe oublié avec une adresse e-mail correcte, un enregistrement est logged dans une table de base de données indiquant que le lien de réinitialisation du mot de passe a été envoyé.

Cette histoire ne peut pas être vérifiée par un utilisateur et les utilisateurs non techniques peuvent ne pas comprendre ce que cela signifie.

Corrigeons cela :

> En tant qu'utilisateur non connecté, lorsque je clique sur le lien de mot de passe oublié avec une adresse e-mail correcte, un e-mail est envoyé à l'adresse e-mail fournie avec un lien de réinitialisation du mot de passe oublié

Les utilisateurs non techniques peuvent comprendre cela et cela met l'accent sur l'utilisateur, pas sur le produit.

### Collaboration des parties prenantes

Agile est collaboratif.

Les user stories nécessitent l'apport du produit, des BA, de la QA, des ingénieurs et, surtout, des utilisateurs.

C'est ainsi que vous vous assurerez de livrer ce que l'utilisateur veut. Plus on est de fous, plus on rit.

Si, par exemple, seule une équipe d'ingénierie créait des user stories, elles pourraient ressembler à ceci :

> En tant qu'utilisateur connecté, lorsque la page se charge, je suis redirigé vers la page d'accueil connectée
> 
> En tant qu'utilisateur non connecté, lorsque je saisis l'adresse e-mail correcte mais le mot de passe incorrect et que je clique sur Connexion, un message d'erreur apparaît
> 
> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail et un mot de passe incorrects et que je clique sur connexion, un message d'erreur apparaît.

Et c'est bien. Mais maintenant, impliquons la QA, qui vient d'une perspective différente car ils ont des expériences différentes avec le logiciel :

> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail correcte en hébreu et un mot de passe correct, je suis redirigé vers la page d'accueil
> 
> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail et un mot de passe corrects et que je clique plusieurs fois sur connexion, je suis redirigé vers la page d'accueil

Super. Nous obtenons maintenant un ensemble plus complet de user stories qui couvrent plus de situations. Mais que se passe-t-il si nous impliquons le produit ?

> En tant qu'utilisateur non connecté, lorsque la page se charge, mon gestionnaire de mots de passe devrait pré-charger mon nom d'utilisateur et mon mot de passe, lorsque je clique sur connexion, je suis redirigé vers la page d'accueil

L'équipe produit connaît les utilisateurs. Ils savent que les gens utilisent vraiment des gestionnaires de mots de passe. Nous devons nous assurer que lorsque l'utilisateur ne tape rien (car le texte est chargé par le gestionnaire de mots de passe), la connexion fonctionne toujours correctement.

### User Stories vagues

L'idée derrière une bonne user story est que tout le monde, quelle que soit son expertise, peut la comprendre.

Si vous avez écrit une User Story qui peut être interprétée de 10 manières différentes par 10 personnes différentes, vous avez un peu dévié.

J'ai mentionné ci-dessus que je parlerais des critères d'acceptation, et c'est le moment de le faire.

Re-examinons la User Story suivante :

> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail et un mot de passe incorrects et que je clique sur connexion, un message d'erreur apparaît.

Il y a du flou là-dedans.

Quel message devrait apparaître ? Lorsque la page se recharge après une tentative de connexion invalide, la zone de texte du nom d'utilisateur doit-elle être réinitialisée à vide ou pré-remplie avec la valeur précédemment saisie ? Que signifie "adresse e-mail incorrecte" ? Une adresse e-mail qui n'a jamais été vue auparavant, ou une adresse e-mail qui n'est pas valide pour le moment (abonnements non payés, abonnements annulés, etc.)

Comme vous pouvez le voir, les détails comptent.

Cette User Story est un exemple simple assez artificiel et j'ai réussi à trouver beaucoup de questions à ce sujet.

Résolvons le problème :

> En tant qu'utilisateur non connecté, lorsque je saisis une adresse e-mail qui n'est pas enregistrée dans le système, lorsque je clique sur connexion, un message d'erreur apparaît

Cela a supprimé les questions autour de l'action de l'utilisateur mais n'a pas résolu le problème du message d'erreur attendu.

Entrez les critères d'acceptation.

Dans la user story, vous devez avoir un ensemble de critères d'acceptation qui définissent si l'implémentation de la user story est conforme aux attentes.

Des choses comme :

* Message d'erreur : "Adresse e-mail ou mot de passe invalide"
    
* Les zones de texte de l'adresse e-mail et du mot de passe sont réinitialisées à vide lors du rechargement
    
* L'utilisateur ne peut pas accéder aux pages où une connexion est requise
    
* Un "mot de passe oublié" est suggéré à l'utilisateur.
    

Les critères d'acceptation indiquent ce qui est attendu de l'implémentation.

## Comment commencer avec les User Stories

Commencez petit.

Vous ne serez pas parfait pour affiner et créer des user stories dès le début.

Créer des user stories est autant un art qu'une science. La pratique rend parfait.

La création de User Stories doit être faite en groupe. Souvent, cela se fait avec l'approche des "3 Amigos", où vous aurez un ingénieur, une personne produit et une QA qui se réunissent et réfléchissent aux différentes permutations que vous devez supporter.

Une fois que vous avez livré votre projet, faites une rétrospective. Jetez un regard en arrière et voyez quels sont les manques dans vos user stories. Il y aura des bugs que les utilisateurs trouveront, que la QA et les tests d'acceptation trouveront, et ceux-ci sont dus soit à des manques dans vos user stories, soit à des manques dans vos tests. Dans tous les cas, vous devriez en tirer des leçons pour la prochaine fois.

## Conclusion

Agile est collaboratif. Scrum est collaboratif. Créer des User Stories est collaboratif. N'oubliez pas cela.

Plus vous avez de personnes issues de différents domaines d'expertise qui réfléchissent à la création de user stories, plus vous avez de chances de couvrir l'ensemble complet des workflows.

L'utilisateur est au centre. Si vous incluez jamais une terminologie que votre utilisateur ne comprend pas, repensez la user story.

Vous ne serez pas parfait dès le début, mais plus vous ferez cela, plus vous deviendrez rapide et efficace. Prenez cela de quelqu'un qui fait cela depuis plus de 10 ans. La différence de vitesse et de qualité de ma création de User Stories aujourd'hui par rapport à il y a 10 ans est un monde à part.

*Dans son temps libre, Ben écrit son blog tech* [*Just Another Tech Lead*](https://justanothertechlead.com/) *et gère un site créant des calculateurs en ligne gratuits pour toujours sur* [*CalculatorLord.com*](https://calculatorlord.com/)*.*