---
title: 'Comment créer des applications low-code réussies : la puissance du transfert
  de connaissances au sein des équipes de développement'
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2024-09-04T15:19:15.982Z'
originalURL: https://freecodecamp.org/news/low-code-knowledge-transfer
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724883531478/4fa7979a-e61a-4268-94dc-a48dfcf17b4b.jpeg
tags:
- name: Low Code
  slug: low-code
- name: teamwork
  slug: teamwork
- name: Collaboration
  slug: collaboration
- name: best practices
  slug: best-practices
seo_title: 'Comment créer des applications low-code réussies : la puissance du transfert
  de connaissances au sein des équipes de développement'
seo_desc: Low-code models, such as Microsoft's Power Platform, make it simple for
  anyone to start creating applications. The barriers to entry are relatively low,
  as users need only a work or school email to get started. Developers can also quickly
  release new...
---

Les modèles low-code, tels que la Power Platform de Microsoft, permettent à n'importe qui de commencer à créer des applications en toute simplicité. Les barrières à l'entrée sont relativement faibles, car les utilisateurs n'ont besoin que d'une adresse e-mail professionnelle ou scolaire pour débuter. Les développeurs peuvent également déployer rapidement de nouvelles applications.

Mais à mesure que cela se produit, des questions surgissent : qui assure le support de ces applications ? Et qui effectuera les mises à jour en cas de demande de fonctionnalité ou de bug ?

De nombreuses applications low-code sont souvent créées par un seul développeur, ce qui mène intrinsèquement à un point de défaillance unique (single point of failure).

Et ne vous laissez pas tromper par la simplicité annoncée du low-code en pensant que n'importe qui peut modifier l'application, corriger les problèmes et ajouter de nouvelles fonctionnalités. Le low-code peut toujours contenir de la complexité, et des solutions complexes peuvent rapidement devenir un problème pour les organisations et les équipes qui exploitent des dizaines, voire des centaines, d'autres dépendances low-code ou non.

Cela ne signifie pas que les organisations doivent restreindre strictement qui peut créer ces applications. Cela contredirait l'objectif même du low-code. C'est un modèle qui permet aux parties prenantes elles-mêmes de prototyper rapidement des idées et de développer des solutions à faible coût pour des problèmes qui, dans le développement traditionnel, pourraient coûter des millions de dollars.

Dans ce monde du low-code, les organisations comme les développeurs ont besoin d'un plan. Les développeurs, spécifiquement, devraient avoir un plan pour transférer les connaissances de leurs produits, qu'ils travaillent en équipe ou de manière indépendante.

## Comment simplifier la complexité

Notre équipe, relativement petite, a créé de nombreuses solutions low-code, en s'appuyant principalement sur la suite de produits Microsoft. Certaines de ces solutions sont de simples applications Canevas low-code, tandis que d'autres contiennent des centaines de dépendances qui n'ont rien de low-code.

Nous avons appris, parfois à nos dépens, l'importance de garantir la maintenabilité dans notre développement. Cela signifie supporter les applications que nous construisons et permettre aux membres actuels et futurs de l'équipe de les supporter à leur tour.

Au départ, nous avons été attirés par la promesse de pouvoir créer des produits résolvant les problèmes rapidement. Avant même de nous en rendre compte, nous avions notre propre problème : comment supporter cet éventail de produits, en veillant à ce que nous ne soyons pas les seuls à pouvoir le faire, mais que les nouveaux membres de l'équipe le puissent aussi ?

### Ralentir pour accélérer

Cela peut sembler contraire au paradigme du low-code, mais faire des pauses fréquentes pour considérer les impacts à long terme de vos décisions est essentiel pour garantir que les outils que vous construisez aujourd'hui pourront être supportés demain.

Cela ne signifie pas revenir aux rythmes du développement logiciel traditionnel, mais vous ne devriez pas considérer la création de produits low-code comme une course vers la ligne d'arrivée.

### Pair Programming

L'intégration de pratiques de développement logiciel traditionnelles peut grandement bénéficier au mouvement low-code. Même si vos applications impliquent peu ou pas de code conventionnel, des concepts comme le Pair Programming peuvent être appliqués efficacement lors de la création de produits low-code.

Prenez, par exemple, le processus de création d'une Power App. Traditionnellement, une seule personne pouvait modifier une application à la fois. Bien que cette limitation ait changé — plusieurs personnes peuvent désormais modifier une application simultanément — la définition d'un processus collaboratif reste cruciale.

Notre équipe emploie souvent une approche avec un « conducteur » (driver) principal, où un membre dirige le développement tandis qu'un autre observe, fournissant des commentaires et des suggestions en temps réel.

Cette méthode maintient l'engagement de chacun et aide à atténuer les effets de la vision étroite sur le produit. Et cette approche collaborative est particulièrement précieuse pour les aspects les plus complexes de l'application.

Pour les tâches plus simples, nous travaillons souvent en parallèle tout en restant étroitement connectés via Teams ou Zoom, prêts à nous coordonner pour garantir que chaque composant différent fait partie d'un tout cohérent.

### Revues d'application/de code

Low-code ne signifie pas « no code ». Il est difficile de créer des applications robustes uniquement par glisser-déposer. Même un outil comme Power Apps possède son propre langage appelé Power FX.

Prévoyez du temps chaque semaine pour parcourir ou réviser les applications des autres afin de vous familiariser avec leurs créations. Cherchez les points d'amélioration et soyez prêt à accepter des commentaires sur vos propres créations.

Si vous utilisez du code traditionnel dans votre projet, une partie de cela peut être accomplie avec des PR (Pull Requests). Pour les implémentations purement low-code, tenez un document des modifications et instaurez un processus de validation pour garantir que les autres membres de l'équipe ont accès aux nouveaux changements.

Par exemple, imaginez l'ajout d'un nouvel écran à une application Canevas, permettant aux utilisateurs de mettre à jour leurs paramètres personnels. Ce changement devrait être documenté comme non révisé jusqu'à ce qu'au moins un autre membre de l'équipe l'ait examiné et validé.

### Impliquer les autres membres de l'équipe

Si vous faites partie d'une équipe, chaque produit devrait impliquer au moins deux personnes pour éviter les points de défaillance uniques. Assurez-vous que chaque produit a un développeur (ou propriétaire de produit) principal et secondaire. Pour les plus grandes équipes, permettez à ce rôle secondaire de tourner, garantissant que chaque membre est plus intimement impliqué dans les produits de l'équipe.

Une façon d'impliquer les autres et de les mettre à niveau consiste à faire ajouter de nouvelles fonctionnalités ou corriger des bugs dans les produits existants par d'autres membres de l'équipe, sous la direction du développeur principal. Ce transfert de connaissances aidera à cultiver un sentiment d'appartenance vis-à-vis des divers produits que votre équipe supporte, menant à un engagement et une motivation accrus.

De plus, comme la charge de travail est répartie plus uniformément au sein de l'équipe, les goulots d'étranglement sont réduits, ce qui permet une gestion plus expéditive de la correction des bugs et de l'amélioration des produits.

## Quand une approche pratique n'est pas possible...

Une grande partie de ce que je décris ci-dessus est une tentative d'impliquer les autres dans les projets. Plus nous manipulons ces outils, mieux nous les comprendrons.

Inévitablement, cependant, lorsque cette expérience pratique n'est pas possible, il est essentiel d'avoir des pratiques capables d'atténuer les effets du développement isolé — c'est-à-dire un développement réalisé par une seule ou quelques personnes seulement.

Les deux choses les plus importantes que nous puissions faire sont de créer et maintenir une documentation complète sur nos produits et d'utiliser des pratiques standard autant que possible. Parlons d'abord de la documentation.

### Documenter, documenter, documenter

Comme vous l'avez probablement constaté, le mouvement low-code permet de créer des applications rapidement. Plus il y a d'applications, moins nous avons de points de contact avec les plus anciennes. Bien que ces points de contact soient essentiels au processus de transfert de connaissances, compter uniquement sur eux ne suffit pas.

Que vous soyez en équipe ou développeur solo, la création d'une documentation décrivant chaque aspect de vos produits est cruciale. Pour les petits projets, il peut s'agir d'un simple document texte. Pour les projets plus importants, vous pourriez utiliser un site SharePoint. Bien sûr, à mesure que les produits deviennent encore plus complexes, les diverses dépendances auront probablement leur propre documentation (par exemple, des dépôts Git).

Voici un exemple de la manière dont vous pourriez documenter un produit que vous construisez :

Disons que vous avez une application qui permet aux utilisateurs de réserver une salle de conférence pour des réunions. Cette application se compose d'une interface utilisateur (telle qu'une application Canevas) et d'un code personnalisé qui crée un rappel de suivi pour la personne ayant réservé la réunion un jour avant. Ce rappel pourrait envoyer un e-mail pour rappeler la réunion à l'utilisateur et, si la réunion n'a plus lieu, l'encourager à annuler la réservation. Enfin, ce produit pourrait également comporter un élément de rapport, où les administrateurs peuvent voir l'utilisation des salles de conférence au fil du temps pour mieux comprendre la demande.

Voici comment vous pourriez documenter ce projet :

1. Établissez une source unique de vérité pour ce projet, comme une page SharePoint.
    
2. Cette page décrit brièvement le projet, les propriétaires du produit et les développeurs principaux.
    
3. La page décrirait également brièvement les composants de ce projet (application Canevas, code personnalisé et tableau de bord de rapport).
    
4. Enfin, vous incluriez une documentation sur tous les aspects faciles à ignorer ou les implémentations de projet non standard (nous reviendrons sur la standardisation plus tard).
    

La page SharePoint gère la vue d'ensemble de haut niveau du projet et vous oriente dans la bonne direction. Concernant les composants individuels, l'application Canevas inclura des commentaires et des notes dans l'historique des versions, et votre code personnalisé s'appuiera sur Git et inclura souvent un fichier Readme détaillé.

La documentation peut être un défi, mais elle est critique. Bien que la documentation doive être complète, elle doit compléter les techniques de transfert de connaissances pratiques décrites ci-dessus.

### Standardiser autant que possible

Qu'il s'agisse de low-code ou de développement traditionnel, il est important d'avoir des pratiques standard. C'est encore plus important lorsqu'on parle de low-code en raison de la vitesse à laquelle les choses peuvent être développées et potentiellement devenir incontrôlables.

De la planification du projet à la conception, du développement et des tests à la formation croisée des membres de l'équipe, prenez le temps de créer des pratiques standard pour chaque phase.

La standardisation ne doit pas être considérée comme un moyen d'éliminer le besoin de formation croisée et de documentation, mais plutôt comme un moyen de compléter ces étapes et de réduire le temps nécessaire dans ces domaines.

Si vous pouvez aborder un problème de la même manière à chaque fois, vous pouvez consacrer du temps à discuter de ces parties non standard et faciles à oublier de ce que vous construisez.

Voici quelques questions pour vous aider à démarrer :

1. Quelles sont les grandes étapes requises pour chaque application ? Qui sera impliqué dans ces étapes ?
    
2. Quels outils utiliserez-vous ? (par exemple, Power Apps, Appian, Pega)
    
3. Pouvez-vous supporter le développement traditionnel ? Si oui, à quoi cela ressemblera-t-il ?
    
4. Quelle est votre approche philosophique du développement ? Par exemple, devez-vous concevoir d'abord l'interface utilisateur ou la logique métier ? Quelle base de données utiliserez-vous ? (par exemple, SharePoint ou Dataverse)
    
5. Quelles conventions utiliserez-vous dans votre code ? (par exemple, conventions de nommage pour les écrans et les variables)
    
6. À quoi ressemble ce processus de transfert de connaissances ou de formation croisée ? Avez-vous des moments dédiés chaque semaine pour examiner le travail des autres ?
    

Bien sûr, cette liste n'est pas exhaustive. Plus vous apprendrez, plus vous réaliserez ce qui doit être discuté. Commencez par créer une procédure opérationnelle normalisée (SOP) et soyez prêt à la modifier tôt et souvent.

## Et si je suis un développeur solo ?

Si vous êtes un développeur solo, il peut être facile de penser que les recommandations ci-dessus ne s'appliquent pas. Mais rien n'est plus faux. Créer et maintenir un Framework de transfert de connaissances est encore plus critique en tant que développeur solo. Bien que le co-développement et le Pair Programming ne soient pas directement applicables, les concepts le sont.

Par exemple, prenez le temps de rencontrer d'autres développeurs et de demander des commentaires. Au minimum, ce sera un excellent moyen de rencontrer d'autres personnes faisant la même chose. Et, bien sûr, avec l'IA qui occupe le devant de la scène dans la programmation, vous pouvez toujours tirer parti de l'IA pour vous aider à apprendre de nouvelles techniques et à optimiser ce que vous construisez.

Enfin, la documentation et les pratiques standard sont tout aussi nécessaires pour le développeur individuel. D'une part, si vous travaillez un jour avec d'autres, vous aurez une référence pour votre travail. D'autre part, ces éléments agiront comme un rappel externe de la manière dont vous avez l'intention de résoudre les problèmes liés au développement à l'avenir.

## Conclusion

Bien que les plateformes low-code offrent une rapidité et une flexibilité incroyables, elles peuvent également introduire des défis en matière de maintenance. Un développement rapide, s'il n'est pas géré avec soin, peut mener à des problèmes qui compromettent le succès à long terme de vos applications.

Mais en ralentissant intentionnellement et en établissant un plan clair pour le transfert de connaissances, vous pouvez sauvegarder l'avenir de vos produits critiques. Cette approche garantit que les applications restent supportées et durables, aujourd'hui et pour les années à venir.

Restez curieux.

*N'oubliez pas de consulter toutes les autres excellentes ressources de freeCodeCamp. Et pour voir d'autres contenus de ma part, rendez-vous sur* [*scriptedbytes.com*](http://scriptedbytes.com)[*,*](http://scriptedbytes.com/) *ou consultez ma* [*chaîne YouTube @Scripted Bytes*](https://www.youtube.com/@ScriptedBytes)*.*