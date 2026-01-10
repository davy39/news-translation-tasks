---
title: Comment automatiser les revues de code sur Github
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T22:22:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-code-reviews-on-github-41be46250712
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i_C4bry8eP6mlT3OqVo45A.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: code
  slug: code
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: Comment automatiser les revues de code sur Github
seo_desc: 'By Mukesh Thawani

  Creating pull requests and reviewing them are two of the most common tasks in a
  developer’s daily schedule. Most projects have common guidelines which developers
  need to follow while creating and reviewing the pull requests.

  Now, it...'
---

Par Mukesh Thawani

La création de pull requests et leur révision sont deux des tâches les plus courantes dans l'emploi du temps quotidien d'un développeur. La plupart des projets ont des directives communes que les développeurs doivent suivre lors de la création et de la révision des pull requests.

Maintenant, il est difficile pour les développeurs de se souvenir de chaque directive lors de la création d'une pull request. Il est encore plus difficile pour les réviseurs de s'assurer que chaque ligne de code est conforme aux directives établies.

Nous avons été confrontés au même problème avec nos projets et l'avons résolu en automatisant la majeure partie du travail manuel répétitif. Cela a grandement facilité la vie de nos développeurs et réviseurs. Ils ont passé plus de temps à améliorer la qualité du code et moins à des tâches courantes.

Dans cet article, je vais décrire exactement comment nous l'avons fait, quels aspects du processus nous avons automatisés et les outils que nous avons utilisés pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/Kxybxb-zIXEpPgFUVpgyt5xnrnPhjVk-YG14)
_Plus de 200 millions de pull requests créées sur Github. Source : Octoverse_

### Automatiser les problèmes de style

Nous ne voulons pas que nos réviseurs demandent aux contributeurs d'ajouter le numéro et la description du ticket Jira correspondant chaque fois qu'ils créent une pull request. Au lieu de cela, nous avons déployé un bot qui effectue toutes les vérifications régulières. Cela aide les contributeurs à suivre les directives du projet.

Oui, un bot peut vérifier si la description est présente ou non en vérifiant le corps de la pull request. Il peut commenter une pull request si la description est manquante.

![Image](https://cdn-media-1.freecodecamp.org/images/h7n4CPzzBvjkUfIT30AQ48qJ0ksUOCYrv-La)
_Applozic Bot commentant les pull requests._

Nous pouvons également ajouter un [modèle de pull request](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/) pour obtenir certaines des informations liées à la pull request. Mais cette approche augmente la friction nécessaire à la création d'une pull request. Lorsque nous ajoutons des règles, nous devons nous assurer que l'expérience d'un nouveau développeur sera aussi fluide que possible. En même temps, nous devons maintenir la qualité du code.

Maintenant, examinons les étapes nécessaires à la création d'un tel bot.

### 'Danger' à la rescousse

> [_Danger_](http://danger.systems/) _s'exécute pendant votre processus CI et donne aux équipes la possibilité d'automatiser les tâches courantes de révision de code. Cela fournit une autre étape logique dans votre build, à travers laquelle Danger peut aider à vérifier vos tâches répétitives dans la révision quotidienne du code._

> _Vous pouvez utiliser Danger pour codifier les normes de votre équipe. Laissant aux humains le soin de réfléchir à des problèmes plus difficiles. Il le fait en laissant des messages à l'intérieur de vos PR en fonction des règles que vous créez avec le langage de script Ruby. Au fil du temps, à mesure que les règles sont respectées, le message est modifié pour refléter l'état actuel de la révision du code._

> _Danger est utilisé dans tous types de projets : gems ruby, applications python, projets Xcode, blogs, sites web et modules npm._

Il vous fournira une abstraction au-dessus de l'API de Github pour obtenir des détails liés à une pull request et effectuer les vérifications nécessaires. Il a été créé et est maintenu par Orta et de nombreux autres contributeurs formidables. Après l'installation, vous devez créer un fichier nommé Dangerfile qui contiendra toutes les règles. Ce fichier doit être présent à la racine de votre projet.

Après avoir ajouté ce fichier, vous êtes prêt avec les règles. Maintenant, vous devez exécuter Danger chaque fois que quelqu'un crée une pull request.

### L'ajouter à votre workflow CI

Nous utilisons Bitrise dans nos projets de SDK mobile. C'est un service d'intégration continue et de livraison continue pour les applications mobiles. Si vous utilisez un service CI différent, vous pouvez consulter ce [guide](https://danger.systems/guides/getting_started.html#continuous-integration) sur la façon d'intégrer Danger avec ce service. Il y a un article de blog détaillé sur l'intégration de Danger avec Bitrise. Je vais le résumer en cinq points :

* Installez bundler, créez un Gemfile et ajoutez le gem Danger au Gemfile.
* Créez un Dangerfile pour votre projet.
* Créez un utilisateur bot sur Github et un jeton d'accès personnel pour le bot.
* Ajoutez ensuite le jeton généré sur Bitrise.
* Ajoutez une étape de script dans le workflow du projet. C'est tout ! 🎉

### Règles que nous pouvons automatiser

L'une des façons d'identifier les règles que nous pouvons automatiser est d'examiner la réponse de l'API de pull request de Github. En comparant la réponse de l'API avec notre liste de contrôle ou nos directives de pull request, nous pouvons nous faire une idée des possibilités qui existent. Voici à quoi ressemble la réponse :

![Image](https://cdn-media-1.freecodecamp.org/images/svTngozizNzNJo2tIyJDAFWyppgAL-dLHRgW)
_Réponse de l'API de pull request de Github_

* Elle retourne presque toutes les informations que vous voyez sur la page web de pull request de GitHub comme le titre, la description, l'assigné, les réviseurs, les labels, etc.
* Il y a une autre API pour récupérer la liste des fichiers modifiés. Pour chaque fichier, elle retournera le nom du fichier, le nombre d'ajouts au fichier, le nombre de suppressions dans le fichier.
* Nous n'avons pas besoin d'utiliser ces API car nous allons utiliser Danger qui nous donne un moyen facile d'interagir avec ces données.

![Image](https://cdn-media-1.freecodecamp.org/images/3eWH5zzgFStXBVRrFH0wGwaf7BcdDO4M3gOV)
_Réponse de l'API de liste des fichiers de pull request de Github_

### Liste des règles que nous avons automatisées

Lorsque nous avons ajouté Danger à notre dépôt, nous avons examiné nos exigences et certains des autres projets qui utilisaient Danger. Voici **certaines des vérifications** que nous avons dans nos projets.

* **Avertir si c'est une grosse PR** : Nous avons tendance à faire l'erreur de pousser beaucoup de changements dans une seule PR. La révision de telles PR est une tâche difficile. Nous avons ajouté un avertissement qui apparaît lorsque le nombre de lignes mises à jour dans une PR est supérieur à 500.
* **Encourager les descriptions de pull request** : Parfois, les développeurs pensent que la description n'est pas nécessaire ou nous oublions de l'ajouter. Même si vous avez mentionné le numéro du problème, une brève description aide toujours et donne un contexte à la pull request. Pour voir si la description est vide ou non, nous pouvons vérifier la longueur du corps :

![Image](https://cdn-media-1.freecodecamp.org/images/cIc1nvWw2LtsPkplGfFyTYfVHIHbo3knjsL1)

* **Vérifier si les tests sont manquants** : Nous savons tous que les tests sont importants et pourtant nous avons tendance à sauter cette étape. Chaque fois que nous apportons une modification au code source, nous devons ajouter des tests si possible. Maintenant, il avertit s'il y a des changements dans le code source et que le dossier de tests n'est pas modifié, ce qui signifie que de nouveaux tests sont manquants.
* **Mettre à jour le Changelog** : Ajouté une nouvelle fonctionnalité ou corrigé un bug — mettez à jour le Changelog avec les détails. Nous avons rendu obligatoire l'ajout d'une entrée de Changelog si le changement est non trivial. Si le Changelog n'est pas mis à jour et que la pull request n'est pas marquée comme triviale, alors notre CI échoue la build. Maintenant, nous n'avons pas à suivre si le Changelog a été mis à jour.
* **Encourager le rebase plutôt que les commits de fusion** : À mesure que le projet grandit, il est toujours recommandé d'éviter les commits de « fusion » afin que le projet ait un historique propre. Nous préférons utiliser le rebase au lieu de fusionner différentes branches. Nous pouvons ajouter une vérification pour les messages de ce format : « Merge branch 'master' » pour éviter les commits de fusion.

![Image](https://cdn-media-1.freecodecamp.org/images/LHJv16-BauUBZd5Xt0QybFyE9aNkABawaXUu)

### Où aller ensuite

Pour référence, vous pouvez consulter le [Dangerfile d'ApplozicSwift](https://github.com/AppLozic/ApplozicSwift/blob/master/Dangerfile) ou dans certains des autres projets open source populaires comme [React Native](https://github.com/facebook/react-native/blob/master/bots/dangerfile.js) ou [CocoaPods](https://github.com/CocoaPods/CocoaPods/blob/master/Dangerfile). J'ai découvert en écrivant cet article de blog que des projets comme React Native et React utilisaient également danger. Cela nous montre comment ce processus d'automatisation de ces vérifications est devenu une partie du workflow commun des pull requests.

_Vous avez aimé l'histoire ? Cliquez sur ce bouton d'applaudissements et suivez-moi sur [Medium](https://medium.com/@MukeshThawani). Merci pour la lecture ! Cet article a été initialement publié sur le [blog de Kommunicate](https://www.kommunicate.io/blog/automate-code-reviews-on-github-using-a-chatbot/).