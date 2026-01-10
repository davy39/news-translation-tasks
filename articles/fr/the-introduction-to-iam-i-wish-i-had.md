---
title: AWS IAM – Politique, Rôles d'Accès, Ressources Expliqués, et Pourquoi Ils Sont
  Utiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-07T02:50:41.000Z'
originalURL: https://freecodecamp.org/news/the-introduction-to-iam-i-wish-i-had
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/g7In5Xr-2.jpg
tags:
- name: Cloud Services
  slug: cloud-services
- name: Cloud Solutions
  slug: cloud-solutions
- name: IAM
  slug: iam
seo_title: AWS IAM – Politique, Rôles d'Accès, Ressources Expliqués, et Pourquoi Ils
  Sont Utiles
seo_desc: 'By Periklis Gkolias

  IAM, or Identity and Access Management, is one of the most common terms you''ll
  hear in cloud-native environments.

  But what does it do? And if you''re already familiar with IAM, how long did it take
  you to fully understand it?

  I wil...'
---

Par Periklis Gkolias

IAM, ou Identity and Access Management, est l'un des termes les plus courants que vous entendrez dans les environnements cloud-native.

Mais que fait-il ? Et si vous êtes déjà familier avec IAM, combien de temps vous a-t-il fallu pour le comprendre pleinement ?

Je vais expliquer les principaux concepts derrière cette grande famille de logiciels, en gardant à l'esprit que vous êtes un ingénieur occupé.

Les principes fondamentaux décrits ici sont indépendants des fournisseurs, bien que la plupart de mon expérience soit avec l'implémentation d'AWS.

## Qu'est-ce que IAM ?
IAM est un système complexe d'entités (humains, applications, etc.) qui demandent l'accès à un système. C'est aussi un ensemble hiérarchique de règles pour accorder ou refuser l'accès demandé.

Avant d'aller plus loin, voici les principaux termes que vous rencontrerez :

- **Ressource** : Tout ce qui vaut la peine d'être protégé. Un service de stockage, une machine virtuelle, etc.
- **Politique** : Un ensemble de règles qui dictent qui peut et ne peut pas faire quelque chose sur une seule ressource ou un groupe de ressources.
- **Action** : Tout ce que quelqu'un peut faire dans l'environnement cloud. Par exemple, créer une machine virtuelle.
- **Utilisateur** : Eh bien... Un utilisateur :)
- **Groupe** : Un groupe d'utilisateurs avec les mêmes permissions appliquées.
- **Principal** : Un utilisateur ou une application demandant l'accès.
- **Rôle** : Un ensemble de pouvoirs assignés à un principal, généralement pour une durée limitée.

## Pourquoi IAM Est Utile
IAM est principalement utilisé pour l'authentification, l'autorisation, l'accès granulaire et la gouvernance.

Voyons ce que tout cela signifie :

- **Authentification** : L'acte de vérifier qui vous êtes.
- **Autorisation** : L'acte d'identifier si quelqu'un peut effectuer l'action qu'il demande. Cela est généralement combiné avec l'authentification, mais pas toujours.
- **Accès granulaire** : Permissions qui contrôlent chaque action pouvant se produire sur une ressource. Par exemple, un utilisateur peut avoir la permission de voir les règles de pare-feu, mais pas de les modifier. Cela est implémenté avec le [Contrôle d'Accès Basé sur les Rôles](https://en.wikipedia.org/wiki/Role-based_access_control).
- **Gouvernance** : Les actions que vous entreprenez pour savoir ce qui se passe dans votre environnement, principalement pour des raisons de budget, de conformité et de portée d'accès appropriée.

Si vous êtes une entreprise de 1 à 3 personnes, la mise en place d'une solution IAM complète est probablement excessive. Mais si votre équipe est plus grande ou si vous prévoyez de vous développer, alors vous devriez commencer à y réfléchir.

![Piliers IAM](https://www.freecodecamp.org/news/content/images/2022/04/WxyvyO4.jpg)

## Problèmes Communs Lorsque Vous N'utilisez Pas IAM
Je crois que vous pouvez voir les avantages d'une solution IAM.

Maintenant, examinons quelques problèmes courants auxquels les organisations sont confrontées en son absence.

### Il Est Difficile d'Auditer et d'Administrer l'Accès
Avez-vous entendu parler de cas où un employé avait plus d'accès qu'il n'en avait besoin ? Et en plus, personne ne le savait ?

Cela peut être évité avec une solution IAM correctement configurée.

### Configurer des Comptes pour les Nouveaux Embauchés Est un Casse-Tête
Avec une solution IAM en place, cela ne serait qu'une question de quelques clics. À savoir, configurer les utilisateurs et les ajouter aux groupes IAM que leurs équipes utilisent. C'est tout.

Mais sans une solution IAM ? Vous devriez configurer toutes les permissions pour chaque compte manuellement.

Vous pourriez avoir un utilisateur de référence à copier, mais chaque nouveau compte a-t-il besoin de toutes les permissions de l'utilisateur de référence ? Avez-vous un traitement spécial pour les comptes utilisateurs de moins de 6 mois ? L'utilisateur de référence a-t-il des permissions superutilisateur qui ne devraient pas être accidentellement assignées à un nouveau compte ?

### Le Désengagement des Personnes Est Chronophage
Ici, vous aurez des problèmes similaires au cas des nouvelles embauches ci-dessus. Mais lorsqu'un collègue part, vous devrez changer le mot de passe de tous les comptes qu'il a **potentiellement** utilisés.

Cela peut rapidement devenir compliqué, sans mentionner les effets secondaires que cela a sur les autres membres de l'équipe.

Et vous devriez faire cela pour chaque script, application et autre ressource chaque fois qu'il y a un désengagement. Que se passe-t-il si vous avez une équipe qui change 2 à 3 fois par mois ? Vous et votre équipe auriez du mal à être productifs.

### Les Choses Simples Nécessitent une Intervention Humaine
Sans une solution IAM, des tâches comme la réinitialisation d'un mot de passe ou la réactivation d'un compte verrouillé doivent être faites manuellement.

Les solutions IAM de premier ordre ont un moyen de résoudre ces problèmes rapidement sans trop de tracas.

## Bonnes Pratiques

![Bonnes pratiques](https://www.freecodecamp.org/news/content/images/2022/04/M7N8blv.jpg)

Si vous avez décidé de configurer IAM, voici quelques bonnes pratiques. Cela est loin d'être une liste complète et est basé sur mon expérience personnelle. Mais j'ai vu ces pratiques dans plus d'une équipe, donc elles devraient fonctionner pour vous aussi.

### Ne Donnez Jamais un Accès Complet... JAMAIS
Dans un scénario réel, vous ne voudriez pas que chaque utilisateur ait un accès illimité à un compte. Idéalement, personne ne devrait avoir un accès complet à quoi que ce soit (à part le propriétaire du compte).

Par exemple, si la responsabilité d'un employé est de surveiller les logs, il devrait avoir un accès en lecture seule à cet outil. Il ne devrait pas être en mesure de redémarrer un service ou de voir les informations de facturation.

### Préférez les Groupes aux Utilisateurs Multiples
Il est préférable d'utiliser des groupes plutôt que plusieurs utilisateurs lorsque vous avez le choix. Les groupes rendent l'administration exponentiellement plus facile.

Par exemple, si une nouvelle personne rejoint votre organisation en tant que développeur, elle peut être ajoutée à un groupe IAM pour les développeurs. Cette nouvelle personne héritera alors de tous les pouvoirs de ce groupe IAM.

L'alternative, créer un utilisateur pour chaque groupe (lecteur_susan, admin_susan) est considérée comme obsolète.

### Préférez les Rôles sur les Utilisateurs Existants à la Création d'un Nouvel Utilisateur
Lorsque vous en avez la possibilité, préférez assigner un rôle à un utilisateur existant plutôt que de créer un nouvel utilisateur.

Par exemple, ne créez pas un utilisateur admin et ne partagez pas le mot de passe entre 10 personnes. Créez un rôle admin et assigniez-le à quiconque en a besoin pour une durée limitée.

### Auditez les Permissions Fréquemment
Il est facile de faire des erreurs ou d'effectuer des actions malveillantes. À tout le moins, une entreprise devrait auditer les permissions régulièrement et s'assurer que seules les bonnes personnes ont le niveau minimum d'accès nécessaire pour leurs rôles.

Vous pourriez également envoyer un email à une certaine équipe lorsqu'une action suspecte se produit. Par exemple, assigner un rôle admin à un nouveau employé.

### Établissez des Limites au Préalable
Si une solution IAM le permet, ajoutez des limites à votre écosystème.

Selon la documentation d'Amazon :

> Une limite de permissions est une fonctionnalité avancée pour utiliser une politique gérée afin de définir les permissions maximales qu'une politique basée sur l'identité peut accorder à une entité IAM. La limite de permissions d'une entité lui permet d'effectuer uniquement les actions autorisées à la fois par ses politiques basées sur l'identité et ses limites de permissions.

(Je sais, je sais — J'ai promis d'être indépendant des fournisseurs 🤴)

En termes simples, vous pouvez définir les permissions « maximales » qui peuvent être assignées à quiconque.

Par exemple, un utilisateur pourra au plus voir les logs de l'outil pertinent et redémarrer un service. Si quelqu'un tente d'obtenir un rôle pour créer une nouvelle machine virtuelle, il sera refusé.

## Conclusion
Merci d'avoir lu jusqu'ici. J'espère que vous avez apprécié cette introduction à IAM.

Si vous avez des questions, n'hésitez pas à me contacter sur Twitter.