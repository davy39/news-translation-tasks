---
title: Apprendre à coder ? D'abord, apprenez à résoudre le problème.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T18:37:53.000Z'
originalURL: https://freecodecamp.org/news/learning-to-code-first-learn-to-solve-the-problem-128475b91301
coverImage: https://cdn-media-1.freecodecamp.org/images/1*90OqH2-MZ4cdAHmbOgStrQ.jpeg
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Apprendre à coder ? D'abord, apprenez à résoudre le problème.
seo_desc: 'By Geshan Manandhar

  Most of the tutorials you have read or watched before now usually do one thing,
  spoon-feeding.

  This is “OK” to learn a new thing, but not good when you need to solve a real task.

  A task usually involves reaching a goal by overcomi...'
---

Par Geshan Manandhar

La plupart des tutoriels que vous avez lus ou regardés jusqu'à présent font généralement une chose : ils vous mâchent le travail.

C'est "OK" pour apprendre quelque chose de nouveau, mais ce n'est pas bien lorsque vous devez résoudre une tâche réelle.

Une tâche implique généralement d'atteindre un objectif en surmontant un problème. Cet article révèle le conseil le plus important pour tous les ingénieurs logiciels débutants.

#### TL;DR

> _D'abord, résolvez le problème. Ensuite, écrivez le code. — John Johnson_

En d'autres termes, travaillez la solution sur papier en étapes. Ensuite, commencez à écrire le code pour celle-ci. Ne vous embrouillez pas dans le code et la conception logicielle d'abord.

### Alors, que se passe-t-il ?

De nombreuses fois, j'entends des débutants et des ingénieurs logiciels juniors dire : "Je pouvais suivre le tutoriel et je pensais avoir compris le concept. Mais lorsque j'ai essayé de faire quelque chose de similaire sur mon projet personnel, je n'ai pas pu le faire."

Cela se produit pour deux raisons.

Premièrement, vous avez perdu le fil de vos pensées quelque part et vous n'avez pas pu établir une chaîne.

Deuxièmement, vous étiez tellement embrouillé dans le code que le problème principal que vous essayiez de résoudre est sorti de votre champ de vision.

Ce problème se pose également pour les ingénieurs logiciels et même les ingénieurs logiciels seniors.

La bonne chose est qu'avec l'expérience, vous savez quand vous arrêter ou faire une pause. Ensuite, revenez au problème avec une approche différente et trouvez une solution plus rapidement.

Beaucoup d'entre vous peuvent se reconnaître dans cela : vous avez essayé si fort de résoudre un problème pendant des heures. Vous avez fait une pause ou dormi dessus, et lors de la session suivante, la solution était là en quelques minutes.

Ce n'est pas de la magie. C'est regarder le problème sous un autre angle.

### Illustrons avec un exemple

Vous devez effectuer une tâche — par exemple, créer un remboursement avec des paiements.

On vous donne le schéma de la base de données. Il s'agit d'une tâche backend et vous devez créer une API POST /refunds qui peut créer le remboursement et ses paiements associés. La structure de la base de données est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/0*DBOwDM4Gq6DJ00sg.png)

Un remboursement a toujours une raison, telle que "marchandises endommagées" ou "livraison tardive".

Vous pourriez discuter de la charge utile de l'API avec l'un des membres de l'équipe. Vous pourriez convenir de la charge utile JSON suivante :

#### Le scénario habituel

Ce que la plupart des ingénieurs logiciels débutants feront, c'est commencer à parcourir la base de code, s'il y en a une. Ils commenceront immédiatement à écrire du code. S'il y a une culture de test en place, peut-être qu'ils écrivent du code de test automatisé.

C'est là que la plupart des ingénieurs logiciels débutants et même certains expérimentés glissent. **N'écrivez pas de code lorsque vous n'avez pas résolu le problème.**

#### L'étape appropriée

L'étape la plus appropriée est de s'asseoir et de résoudre le problème sur papier en étapes.

Vous vous demandez donc ce que vous devez faire. Vous élaborez un plan en étapes et vous l'ajustez.

Si vous avez quelqu'un de senior dans votre équipe, vous pouvez valider vos étapes et obtenir des commentaires.

Cela réduira également le temps de révision du code. Vous avez déjà convenu de la modalité de la solution.

#### Comment faire

La tâche décrite précédemment consiste à écrire une API de création/POST où les remboursements avec paiements peuvent être créés.

Chaque remboursement peut avoir un maximum de deux paiements. L'un est de type "espèces" et l'autre est de type "crédit". Il peut également s'agir d'un remboursement avec un seul paiement, soit en espèces, soit en crédit. Voici comment j'aurais écrit les étapes suivantes sur papier :

1. Créer une méthode pour obtenir les données du contrôleur envoyées par l'utilisateur
2. Valider toutes les entrées pour les valeurs, les types de remboursement et les raisons.
3. Si toutes les validations passent, générer un numéro alphanumérique aléatoire de longueur 10 qui n'existe pas dans la table de remboursement (vérification récursive)
4. Si la validation échoue, répondre avec un message d'échec de validation approprié, décider de la structure de réponse
5. Démarrer une transaction de base de données
6. Insérer les valeurs liées au remboursement de `refund_nr`, `reason_reason`, `is_premium_customer` dans la table `refund`
7. En cas de succès d'insertion, obtenir l'id de la dernière insertion
8. Avec le refund_id, insérer les valeurs liées au paiement de fk_refund, fk_item, amount, is_cash dans la table `payment`
9. Si tout s'est bien passé, valider la transaction de base de données
10. Si un problème est survenu, annuler la transaction de base de données
11. Répondre avec un message de succès ou d'échec en fonction du succès de la transaction de base de données avec une structure appropriée
12. Relier le contrôleur et cette méthode

### Suivez le plan étape par étape, maintenant écrivez le code

Après avoir un plan étape par étape, vous pouvez commencer à écrire du code. Ensuite, vous pouvez approfondir les noms des méthodes, comment obtenir la connexion à la base de données et autres détails.

Selon le langage et le framework, vous pouvez également décider où doit se trouver le code de validation.

Vous pourriez même écrire des tests si l'entreprise et la culture le soutiennent et l'encouragent.

Lorsque votre solution est évidente dans votre esprit et que vous avez un plan d'action étape par étape sur papier, vous pouvez maintenant écrire du code.

Vous pouvez même diviser les parties de manière à ce qu'elles soient plus faciles à terminer et à relier.

Par exemple, la logique de test peut être quelque chose qui peut être écrit séparément et testé indépendamment. C'est penser à des parties indépendantes qui peuvent être reliées ensemble pour former la solution.

### Conclusion

Lorsque vous serez confronté à votre prochaine tâche, ne commencez pas à écrire du code dès le départ.

D'abord, comprenez bien le problème, puis élaborez une solution avec des étapes. Cela se fait mieux loin d'un écran, sur papier.

Ensuite, affinez votre solution et discutez-en avec quelqu'un. Lorsque vous êtes satisfait, traduisez cette solution en code. C'est un peu méthodique mais très efficace.

> Le code est toujours un moyen d'atteindre la solution, pas la solution elle-même.

Vous pouvez lire plus de mes articles de blog _sur [geshan.com.np](https://geshan.com.np/blog/2018/12/the-most-important-tip-for-beginner-software-engineers-is/)._