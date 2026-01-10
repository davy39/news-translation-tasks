---
title: Comment utiliser les playbooks pour exécuter un plan de reprise après incident
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-31T01:28:09.000Z'
originalURL: https://freecodecamp.org/news/use-playbooks-for-incident-recovery
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-mateusz-dach-353644.jpg
tags:
- name: Disaster recovery
  slug: disaster-recovery
- name: workflow
  slug: workflow
seo_title: Comment utiliser les playbooks pour exécuter un plan de reprise après incident
seo_desc: 'A playbook is the official, formal written record that describes policies
  and processes that will reliably produce a working deployment of an organization''s
  resource stack. When it comes to generating predictable results, the playbook is
  the plan.

  I''...'
---

Un playbook est le document officiel et formel qui décrit les politiques et les processus permettant de produire de manière fiable un déploiement fonctionnel de la pile de ressources d'une organisation. En matière de génération de résultats prévisibles, le playbook _est_ le plan.

Je vais décrire tous les éléments clés d'un bon playbook dans un instant. Mais il est important de souligner qu'un playbook, à lui seul, est plus ou moins inutile si votre équipe n'est pas en mesure de le lire et de le convertir en résultats concrets.

Pour cela, vous devrez vous assurer que chaque membre pertinent de votre équipe est parfaitement familiarisé avec ses rôles et la manière dont il devra les remplir. Cela nécessitera de distribuer des copies du plan et de s'assurer que chacun reçoit la formation nécessaire pour performer parfaitement lorsque le moment sera venu.

Cet article provient de mon [cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/Qqo6qcDFBwU]

## Comment définir la portée du playbook

En tout cas, un bon plan commence par des définitions claires :

* Où pouvez-vous trouver des copies à jour et propres du code source ?
* Où votre environnement de production doit-il être hébergé ? Dans un cloud public comme AWS ? En local ?
* Que doit accomplir l'infrastructure ?
* Quelle est l'ampleur de votre opération : quelle échelle de ressources matérielles nécessitera-t-elle ?

Un playbook doit également définir clairement les politiques à suivre tout au long du processus de reconstruction :

* Comment les données organisationnelles doivent-elles être protégées ?
* Quelles décisions doivent être prises uniquement par les dirigeants seniors de l'entreprise ?
* Existe-t-il des restrictions sur les logiciels et solutions tierces pouvant être utilisés... ou sur les pays depuis lesquels ils peuvent être acquis ?
* Existe-t-il des composants de la pile qui _doivent_ rester locaux, ou tout peut-il être hébergé dans le cloud ?

## Comment définir les outils

Peut-être le cœur de tout playbook est la section traitant des outils logiciels et de déploiement ainsi que des procédures que vous utiliserez à chaque étape de votre flux de travail.

Cette section doit inclure le code complet des scripts gérant le déplacement des ressources du code vers le déploiement, ainsi que des liens vers tout le code logiciel utilisé, et des instructions pour l'authentification aux services que vous utiliserez.

## Comment définir les participants

Les déploiements informatiques sont effectués par des personnes. Mais quelles personnes ?

* À qui vous adressez-vous pour avoir accès à une carte de crédit afin d'acheter les ressources nécessaires ?
* Qui a accès aux bases de code clés et aux comptes en ligne dont vous aurez besoin ?
* Qui est responsable des tests et de la validation avant que le code ne soit poussé en production ?
* Que faire si cette personne n'est pas disponible ?

Chaque rôle lié au projet que vous documentez doit être défini, et la personne responsable doit être identifiée – ainsi que ses coordonnées actuelles.

Au-delà des contacts opérationnels, le playbook doit également inclure un annuaire complet des communications de l'entreprise. Si vous payez quelqu'un chaque mois, il est probable qu'il soit attendu pour remplir une fonction importante lors d'une reprise. Vous aurez donc besoin d'une source fiable pour les informations de contact – de préférence contenant plusieurs points de contact pour chaque personne.

## Comment documenter votre reprise

Les opérations de reprise peuvent être chaotiques. Mais il est néanmoins crucial que des enregistrements de journal pour chaque étape – avant, après et pendant la reprise – soient conservés. La génération et le stockage des journaux doivent donc également faire partie de votre playbook.

Même si vous n'avez pas le temps de les lire maintenant, ils seront inestimables plus tard lorsque vous tenterez de passer en revue les événements et de comprendre exactement ce qui s'est passé. L'existence de journaux et d'autres enregistrements précis et fiables peut être légalement obligatoire.

Tout examen de code et test d'application que vous incorporeriez normalement dans vos cycles de vie de déploiement doit être inclus dans votre playbook de reprise. Après tout, les bugs et les échecs ne seront pas plus amusants après une crise qu'ils ne l'étaient avant. Le code réel de tous les scripts qui alimenteraient normalement vos tests doit également être inclus ici.

## Comment maintenir votre playbook à jour

Enfin, votre playbook doit être régulièrement mis à jour pour refléter les changements apportés à votre application et à son environnement de support. Naturellement, vous souhaitez garder tous les détails à jour, y compris les changements de personnel responsables de rôles spécifiques, ainsi que leurs informations de contact correctes.

Un playbook complet créé pour une opération relativement complexe peut facilement atteindre des centaines de pages. Lorsque vous ajoutez la tâche de coordonner les actions de toutes les nombreuses personnes impliquées dans votre reprise, l'ensemble peut sembler un peu difficile à gérer. Malheureusement, vous devez simplement le faire : il n'y a vraiment pas d'alternative.

## Comment automatiser votre reprise

Eh bien, il n'y a presque pas d'alternative. Vous souvenez-vous lorsque je vous ai dit que vous deviez inclure des scripts d'opérations complets et des liens vers votre base de code dans le playbook ? Pensez-vous que notre playbook pourrait être convaincu de _s'exécuter lui-même_ ? Pourquoi pas ?

Réfléchissez-y. Des outils d'orchestration comme Ansible ou Terraform – ou des outils spécifiques au cloud comme CloudFormation d'Amazon – vous permettent de définir très précisément chaque couche de votre infrastructure dans un format qui peut être invoqué et lancé avec une seule commande.

En théorie au moins, il n'y a aucune raison pour laquelle vous ne pourriez pas construire votre playbook en tant que script réel, complet avec des commandes pour extraire des dépôts logiciels, lancer des réseaux virtuels complexes et des instances de calcul, et router des domaines DNS. Ce serait un exemple fantastique de la puissance de l'infrastructure en tant que code.

## Comment tester votre playbook

Tant que nous sommes encore sur le sujet des plans et des playbooks, je devrais ajouter une autre note très importante. Si vous allez vous donner toute la peine de rechercher et d'écrire un playbook, vous ne voulez pas découvrir au milieu d'une crise que vos plans ne fonctionnent pas réellement.

L'hypothèse sûre est que _rien_ en technologie ne fonctionnera à moins d'avoir été soigneusement et répétitivement testé à l'avance. Cela est vrai pour les playbooks de reprise, et c'est tout aussi vrai pour les sauvegardes : jusqu'à ce que vous ayez restauré avec succès une archive de sauvegarde dans un environnement réel, vous devez supposer qu'elle échouera.

Avec ce que vous avez maintenant vu sur la portée, les outils, la documentation, les mises à jour et l'automatisation des playbooks, vous êtes maintenant prêt à vous mettre au travail pour créer le vôtre. Eh bien, ne me laissez pas vous retarder !

_Cet article provient de mon [cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_