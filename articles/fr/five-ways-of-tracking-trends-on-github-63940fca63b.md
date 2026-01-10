---
title: Voici 5 façons de suivre les dépôts tendance sur GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T15:12:51.000Z'
originalURL: https://freecodecamp.org/news/five-ways-of-tracking-trends-on-github-63940fca63b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Wk2sOsVhjtblFT0VM6iRaw.png
tags:
- name: Design
  slug: design
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Voici 5 façons de suivre les dépôts tendance sur GitHub
seo_desc: 'By Vitaliy Potapov

  GitHub trending is a constantly updated list of repositories that provide a view
  of the open-source projects which the community is most excited about.

  Trending repositories are displayed based on the number of times they’ve been s...'
---

Par Vitaliy Potapov

[GitHub trending](https://github.com/trending) est une liste constamment mise à jour de dépôts qui offrent un aperçu des projets open-source qui passionnent le plus la communauté.

Les dépôts tendance sont affichés en fonction du nombre de fois où ils ont été étoilés par les utilisateurs chaque jour, semaine ou mois. Vous pouvez les filtrer en fonction d'un langage de programmation spécifique pour voir ce qui se passe dans votre domaine d'intérêt.

Suivre cette page vous tiendra également informé des projets les plus "chauds" dont tout le monde parle. J'ai essayé cinq méthodes différentes pour suivre les tendances sur GitHub et j'ai établi quelques comparaisons et contrastes comme mis en évidence ci-dessous.

#### 1. Newsletter GitHub Explore

Il s'agit de la newsletter officielle de GitHub. Vous pouvez [vous y abonner ici](https://github.com/explore#newsletter). Les emails sont envoyés quotidiennement, hebdomadairement ou mensuellement, selon votre préférence. L'email contient les 5 dépôts tendance principaux parmi tous les langages de programmation pour la période sélectionnée :

![Image](https://cdn-media-1.freecodecamp.org/images/rTRRKgydWhUpWPGeh28MgOQp92s8P4umTMFp)
_Newsletter GitHub Explore_

La newsletter contient également des recommandations personnalisées. Par exemple, elle peut contenir une liste de projets étoilés par des personnes que vous suivez sur GitHub.

**Avantages :**

* Newsletter officielle
* Envoi quotidien, hebdomadaire ou mensuel
* Recommandations personnalisées

**Inconvénients :**

* Vous ne pouvez pas vous abonner à un langage de programmation particulier
* Seuls les 5 dépôts principaux sont dans la liste, bien qu'il y en ait 25 sur la page GitHub trending

#### 2. Notifications GitHub

Le système de notifications GitHub est un moyen natif et pratique de suivre l'activité sur GitHub. Pour de nombreux développeurs, il fait partie de leur processus de travail quotidien. Vous pouvez recevoir des notifications sur les nouveaux commentaires, les pull requests, les mentions et toute autre activité à laquelle vous pourriez être impliqué.

![Image](https://cdn-media-1.freecodecamp.org/images/E1c6i7bh3G4LUKbxGHbuFh-hRqqiVpcUCGPc)
_Cloche de notification web GitHub, issue de [la documentation officielle](https://help.github.com/articles/accessing-your-notifications/" rel="noopener" target="_blank" title=")_

[GitHub-trending-repos](https://github.com/vitalets/github-trending-repos) est un dépôt spécial qui utilise les notifications GitHub pour vous envoyer des mises à jour sur les tendances. Chaque issue dans ce dépôt est liée à un langage de programmation particulier. Sur une base quotidienne et hebdomadaire, le bot vérifie la page des dépôts tendance et laisse un commentaire. Vous pouvez vous abonner à une issue et recevoir des mises à jour sur l'interface web GitHub ou par email.

![Image](https://cdn-media-1.freecodecamp.org/images/mlQrzM0MhtXcsqHLL5z9-3pHEWAkSyj-JsVl)
_Notification web GitHub avec les nouvelles tendances_

![Image](https://cdn-media-1.freecodecamp.org/images/8l5mrOSoxEhkvEBb76EUbPAIjMCb0k4JNGHc)
_Exemple de commentaire du bot_

**Avantages :**

* Vous pouvez vous abonner aux tendances d'un langage de programmation particulier
* Vous pouvez recevoir des notifications soit sur l'interface web GitHub, soit par email
* Vous pouvez choisir entre des mises à jour quotidiennes et hebdomadaires

**Inconvénients :**

* Tous les langages de programmation ne sont pas encore disponibles pour l'abonnement

#### 3. Bot Twitter

Toutes les 30 minutes, le bot [@TrendingGithub](https://twitter.com/TrendingGithub) tweete sur un dépôt ou un développeur tendance actuel :

![Image](https://cdn-media-1.freecodecamp.org/images/QIEvPrCVCagHnnBwVX6YW51CvbVG1DLzJYMP)
_Exemple de tweet de @TrendigGithub_

Les followers peuvent facilement suivre le pouls des tendances GitHub. Les dépôts sont sélectionnés parmi tous les langages de programmation. En interne, le projet mémorise les éléments tweetés pendant 30 jours pour éviter la duplication de contenu.

**Avantages :**

* Twitter est un canal pratique pour recevoir des nouvelles
* Vous pouvez suivre les développeurs tendance également

**Inconvénients :**

* Impossible de s'abonner à un langage de programmation particulier
* Recevoir des mises à jour toutes les 30 minutes peut être gênant

Le code source du projet est [disponible sur GitHub](https://github.com/andygrunwald/TrendingGithub).

#### 4. Newsletter Changelog Nightly

[Changelog Nightly](https://changelog.com/nightly) est une newsletter automatisée envoyée chaque nuit à 22h, heure centrale des États-Unis (CT). Elle collecte les dépôts tendance parmi tous les langages de programmation et les divise en trois groupes :

1. _Premières fois_ - dépôts tendance non précédemment envoyés par email
2. _Top nouveaux_ - dépôts tendance open-source tout au long de la journée
3. _Répétitions_ - dépôts tendance qui sont déjà apparus dans la newsletter auparavant

![Image](https://cdn-media-1.freecodecamp.org/images/9bbKYAzBv642UbMlGbIc1oWyY2QP66UxYRr2)
_Email Changelog Nightly_

Il s'agit d'un sous-projet de [Changelog](https://changelog.com/) - une entreprise de médias numériques offrant beaucoup d'autres choses intéressantes pour les développeurs : 7 podcasts techniques, des nouvelles, un email modéré hebdomadaire et des discussions communautaires dans Slack.

**Avantages :**

* Les éléments sont séparés en groupes significatifs : premières fois, créés aujourd'hui et répétitions

**Inconvénients :**

* La seule option de planification disponible est l'envoi quotidien d'emails
* Impossible de filtrer par un langage de programmation particulier

Il est intéressant de noter que Changelog Nightly est alimenté par [GitHub Archive](https://www.githubarchive.org/) - une base de données enregistrant toute l'activité publique sur GitHub. Vous pouvez accéder aux données avec n'importe quel client HTTP et faire votre propre analyse.

#### 5. Navigation manuelle dans le dépôt mis à jour quotidiennement

Envisagez cette méthode si vous n'avez besoin d'aucune notification. Chaque jour, un script dans le dépôt [github-trending](https://github.com/josephyzhou/github-trending) extrait les projets tendance et les enregistre sous forme de fichiers markdown. Vous pouvez parcourir manuellement ces fichiers et découvrir ce qui était tendance à une date particulière.

![Image](https://cdn-media-1.freecodecamp.org/images/LBkOehionUFg4AyZ3nFkBCi6eSUmYk5lgRz9)
_Fichiers markdown quotidiens avec les dépôts tendance_

Le contenu de chaque fichier couvre 7 langages de programmation : Swift, Objective-C, Go, JavaScript, Ruby, Rust et Python.

![Image](https://cdn-media-1.freecodecamp.org/images/ZGIwNNGke5UHpWGCahTio-uInYhxKYzb1I3t)
_Projets tendance pour Swift le 26 novembre 2017_

**Avantages :**

* Vous pouvez accéder à l'historique complet des tendances
* Vous n'êtes pas dérangé par les notifications

**Inconvénients :**

* Seuls 7 langages sont supportés
* Seules les tendances quotidiennes, pas de mises à jour hebdomadaires ou mensuelles
* Aucune information sur les étoiles acquises
* Vous devez parcourir manuellement

### Conclusion

Chaque méthode a ses propres avantages et inconvénients. Vous pouvez toutes les essayer et sélectionner celle qui vous convient le mieux.

Je crois que suivre les nouveaux projets GitHub est une partie importante du monde open-source. Cela a un effet gagnant-gagnant :

1. En tant que développeur, vous pouvez améliorer votre propre productivité en utilisant des approches et des outils modernes.
2. En tant qu'auteur de projet, vous pouvez recevoir des retours de la communauté et de l'inspiration pour le développement futur.

Merci d'avoir lu ! Vous êtes les bienvenus pour partager comment vous découvrez les tendances sur GitHub.