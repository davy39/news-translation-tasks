---
title: 'La Beauté de Heroku Connect : Simplifier la Synchronisation de Base de Données'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T21:25:37.000Z'
originalURL: https://freecodecamp.org/news/the-beauty-of-heroku-connect-simplifying-database-synchronization-e57451d3b376
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EPgspRCbfWjtUtUXoGnVHg.png
tags:
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: Salesforce
  slug: salesforce
- name: technology
  slug: technology
seo_title: 'La Beauté de Heroku Connect : Simplifier la Synchronisation de Base de
  Données'
seo_desc: 'By Wilson Wang

  I’m currently a developer for Blueprint, an organization at UC Berkeley. We develop
  software pro bono for non-profits and advance technology for social good. This past
  year, my team worked on building a solution for The Dream Project. ...'
---

Par Wilson Wang

Je suis actuellement développeur pour [Blueprint](https://calblueprint.org/), une organisation à UC Berkeley. Nous développons des logiciels pro bono pour des associations et faisons progresser la technologie pour le bien social. Cette année passée, mon équipe a travaillé sur une solution pour [The Dream Project](http://www.dominicandream.org/). Le but est de fournir une meilleure éducation aux enfants en République Dominicaine.

J'écris cet article dans l'espoir de partager mon expérience d'intégration de Salesforce en utilisant Heroku Connect pour une application Ruby on Rails/React Native.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EPgspRCbfWjtUtUXoGnVHg.png)

#### Qu'est-ce que [Heroku Connect](https://www.heroku.com/connect) ?

> « Heroku Connect vous permet de créer facilement des applications Heroku qui partagent des données avec votre déploiement Salesforce. En utilisant la synchronisation bidirectionnelle entre Salesforce et Heroku Postgres, Heroku Connect unifie les données de votre base de données Postgres avec les contacts, comptes et autres objets personnalisés de la base de données Salesforce. »

Une autre façon de le dire...

Heroku Connect aide à remplacer la base de données Postgres de votre application par une base de données Salesforce. Bien sûr, comme les applications Rails se connectent nativement à Postgres, vous ne pouvez pas faire des appels et des pushes immédiats à Salesforce sans une API comme le [gem Restforce](https://github.com/restforce/restforce).

En réalité, la base de données Postgres avec laquelle notre application Rails interagira sert de déguisement pour Salesforce. C'est un intermédiaire fonctionnel. Toutes les données doivent passer par lui avant d'atteindre Salesforce, et vice versa. Heroku Connect est le pont qui combine les capacités de Force.com et Heroku sans avoir besoin d'un gem.

Vous pourriez demander... pourquoi même se donner la peine d'apprendre l'intégration de Salesforce ?

Eh bien, l'intégration de Salesforce rationalise le processus de stockage et de récupération des données. Surtout les données clients pour les entreprises.

Vous pouvez fournir à vos clients des systèmes informatiques modernisés pour une meilleure expérience utilisateur et un meilleur flux de travail. Vous accélérerez le développement d'applications. Cela crée également de meilleurs outils pour informer la gestion et les ventes sur les performances de l'entreprise.

Cela aide les entreprises à atteindre des niveaux d'opération efficaces pour les applications business-to-consumer. Cela le fait grâce à des mises à jour instantanées et précises.

#### Un Projet Exemple pour Inspiration

Pour donner un peu de contexte aux extraits de code ci-dessous dans le tutoriel, je vais expliquer au préalable le projet sur lequel je travaillais. Ce projet m'a introduit à Heroku Connect.

Auparavant, Dream enregistrait les informations des étudiants dans une base de données Salesforce. Ce n'était pas idéal pour les enseignants à utiliser. Pour faciliter leur vie, nous avons créé une application conviviale. L'application gérait la création de cours, l'inscription des étudiants et la prise de présence.

En raison de la mauvaise connexion Internet dans les campus de Dream, nous nous sommes tournés vers Heroku Connect pour une synchronisation constante des mises à jour. Il synchronisait les mises à jour du côté de la base de données Heroku Postgres et du côté de la base de données Salesforce.

Tout le code décrit dans cette démonstration est disponible dans notre [dépôt de projet](https://github.com/calblueprint/dream-rails). Vous pouvez également consulter le côté React de l'application [ici](https://github.com/calblueprint/dream-mobile).

### Bon, commençons la démonstration...

#### Aperçu

Je vais aborder cette démonstration dans l'ordre suivant :

1. Description de la Technologie
2. Installation (Heroku Postgres et Heroku Connect)
3. Mappages Heroku Connect + Notes
4. Modifications de votre application Rails locale

#### Description de la Technologie

* Force.com ([Compte Développeur Salesforce](https://developer.salesforce.com/))
* [Heroku Connect](https://www.heroku.com/connect)
* Application Rails (ma version Rails était 5.1.4)

#### Installation : Déploiement de votre application sur Rails

Après avoir configuré votre application Rails, vous souhaitez déployer votre application sur Heroku. Voici un rapide aperçu du déploiement de votre application :

1. Connectez-vous à votre compte Heroku, et vous serez redirigé vers le tableau de bord en haut à droite. Vous verrez un bouton « Nouveau » en haut à droite pour créer un nouveau projet. Saisissez le nom de votre application personnalisée et créez votre application.
2. Vous serez redirigé vers la page de déploiement de votre nouvelle application. Faites défiler vers le bas jusqu'à la section « Déployer en utilisant Heroku Git ». Suivez les instructions sur la page. (Note : après avoir ajouté la télécommande Heroku Git, vous pouvez toujours mettre à jour votre application Heroku. Vous mettez à jour en ajoutant et en validant vos modifications et enfin en faisant un git push **heroku** master.)

Très probablement, si c'est votre première fois, vous rencontrerez une erreur : « Heroku deployment failed because of sqlite3 gem error. » Cela est dû au fait que Heroku utilise Postgres au lieu de sqlite3. Pour corriger cela, consultez ce [post Stack Overflow](https://stackoverflow.com/questions/13083399/heroku-deployment-failed-because-of-sqlite3-gem-error.).

#### Heroku Postgres

Avec votre application déployée, votre page d'accueil devrait avoir l'add-on Heroku Postgres. Il s'agit de votre base de données habituelle pour les applications Heroku déployées.

![Image](https://cdn-media-1.freecodecamp.org/images/0*R9kFu8MDX4RC17HJ)
_Les add-ons comme Heroku Postgres ou Heroku Connect apparaissent dans l'onglet Aperçu ou Ressources._

Cliquez sur cet add-on pour vérifier les informations de la base de données URL dans l'onglet des paramètres. Assurez-vous d'ajouter l'URL de votre base de données Postgres à votre application Rails.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NOr58iU9H0g4xG_5)

Pour ajouter l'URL de la base de données, vous pouvez soit créer une variable d'environnement en utilisant le gem [Figaro](https://github.com/laserlemon/figaro) :

ou simplement inclure une variable URL dans votre fichier database.yml :

#### Heroku Connect

Ensuite, cliquez sur configurer les add-ons ou l'onglet des ressources, et recherchez Heroku Connect. Cliquez sur provision pour ajouter l'add-on.

![Image](https://cdn-media-1.freecodecamp.org/images/0*g85k6DdH9HyNB1vJ)

Vous serez ensuite redirigé vers l'écran ci-dessous. Notez que le nom du schéma est « salesforce » pour l'instant (n'hésitez pas à le changer également), et vous êtes prêt à continuer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WUvsdQ_IgEgV41S7Y9_hew.png)

Cliquez sur configurer la connexion. Entrez vos informations d'utilisateur Salesforce pour établir la connexion avec les détails appropriés.

Vous avez maintenant terminé la configuration ! Nous pouvons maintenant passer aux mappages.

#### Mappages

J'ai enregistré une courte vidéo de la création d'un mappage pour un objet Teacher :

La vidéo est un guide pour établir des mappages. Il y a quelques points que je souhaite expliquer davantage et qui m'ont personnellement posé problème. Après avoir lu ces clarifications, je vous recommande de regarder à nouveau la vidéo pour une meilleure compréhension.

#### 1. '__c'

Vous vous demandez peut-être pourquoi il y a tant de '__c' ajoutés à la fin de mon objet teacher et des champs teacher. Eh bien, Salesforce ajoute en réalité cela à chaque classe/champ personnalisé.

Ainsi, en revenant à mon projet Rails, le nom de la table est maintenant _Teacher__c_ au lieu de Teacher et les colonnes/champs ont changé de noms comme First_name, Last_name à _First_name__c_, _Last_name__c_. Certains champs par défaut comme _sfid_ ou _createddate_ ne sont pas personnalisés, donc ils n'ont pas besoin d'ajouter '__c'.

#### 2. Champs Personnalisés

Alors, comment créez-vous des champs personnalisés ? Eh bien, il y a en réalité une petite flèche sur le côté droit de votre écran pour que vous puissiez modifier les objets et les champs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BZ1PIjziwnyF2V3A)
_Cliquez sur afficher l'objet/les champs pour les modifier respectivement._

Après chaque modification, n'oubliez pas de vérifier si vous devez également modifier vos mappages Heroku Connect.

#### 3. Synchronisation Bidirectionnelle

![Image](https://cdn-media-1.freecodecamp.org/images/0*-CCzjvqWA4i5Aggx)

Je voulais souligner deux fonctionnalités très intéressantes de la synchronisation bidirectionnelle de Heroku Connect. La première est la fréquence de sondage, qui régule la fréquence à laquelle vous souhaitez que votre base de données Postgres se mette à jour avec les mises à jour de Salesforce. Cocher la case Accélérer le sondage rend la plupart des opérations presque instantanées.

La deuxième est la section sur la poussée des données de votre base de données Postgres pour les synchroniser avec la base de données Salesforce. Vous devez cocher la case pour que cette fonctionnalité fonctionne. Cependant, juste après, vous verrez probablement un avertissement apparaître :

![Image](https://cdn-media-1.freecodecamp.org/images/0*AxFt3ybUi7xmipGk)
_Avertissement : Les mappages en lecture-écriture nécessitent qu'un identifiant unique soit spécifié._

C'est une couche de protection pour s'assurer que vous ne créez pas accidentellement des objets en double. C'est génial si vous avez un identifiant unique (dans la vidéo, chaque enseignant a un email unique, donc j'ai fait de cela mon identifiant). Sinon, vous pouvez le sauter et avoir toujours un mappage Heroku Connect fonctionnel. Cependant, vous pourriez vouloir programmer votre application pour vérifier les enregistrements existants avant de créer un objet.

#### Modifications de votre application Rails locale

Maintenant que vous avez votre Heroku Connect bien configuré, il est temps pour un rapide ajustement local avant de pouvoir interagir avec vos données Salesforce.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qqvmsH_-kzF_NeCh)

Dans l'aperçu, vous verrez le nom de votre schéma, dans ce cas « salesforce ». Si vous aviez choisi un nom différent lors de la phase de provisionnement, ce nom apparaîtrait ici à la place.

Parce que le nom de la table de mon application Rails est toujours Teacher, je dois le changer en _Teacher__c_ pour référencer correctement les données Salesforce. Je dois changer le nom de la table au format _nom_du_schéma_._nom_de_l'objet_ ou _salesforce.teacher__c_ pour refléter les changements.

L'autre changement notable s'applique si votre modèle a des déclarations validées, comme mon modèle Teacher. Après le mot-clé validates, nous avons toujours les anciens noms de champs comme first_name sans '__c' et last_name sans '__c'. Nous devons changer ces noms soit en ajoutant '__c' aux anciens noms de champs, soit en créant des méthodes séparées :

Ensuite, créez quelques objets dans Salesforce et ouvrez votre console Rails pour récupérer ces informations. (Dans la vidéo, j'ai appelé Teacher.all pour afficher tous les objets Teacher de Salesforce dans ma console Rails.) Les informations devraient également être reflétées dans l'explorateur Heroku Connect.

### Réflexion

J'ai passé une bonne moitié de mon semestre à essayer de comprendre l'intégration de Salesforce. J'ai fait beaucoup de recherches, expérimenté différentes solutions et reçu beaucoup de soutien. En fin de compte, ce fut une expérience très éclairante de travailler avec les fonctionnalités intéressantes de Salesforce/Heroku/Rails. J'ai également appris à quel point j'ai grandi en tant que développeur et réfléchi à mes forces et faiblesses.

Habituellement, les gens implémentent les premières solutions qu'ils trouvent. Ils le font sans comprendre pourquoi c'est bien ou mal. J'ai recherché et planifié trois solutions séparées avant de découvrir Heroku Connect. À travers cela, j'ai réalisé à quel point il était important de peser les pour et les contre des différentes solutions avant de se décider, même si plus de temps est passé à rechercher plutôt qu'à implémenter.

En utilisant cette connaissance, mon équipe et moi avons construit une application pour aider les enseignants à fournir une éducation de qualité aux étudiants des écoles de la République Dominicaine qui ont une mauvaise connexion à Internet. Nous avons appris à persévérer lorsque les temps étaient difficiles parce que nous savions que malgré chaque longue session de travail, chaque correction de bug, chaque ligne de code, nous avions une mission, et chaque étape du chemin était une autre étape vers l'amélioration du monde.

Cette expérience m'a aidé à vraiment prioriser l'objectif et l'importance de faire un travail de qualité plutôt que d'utiliser immédiatement le moyen le plus rapide. Chaque solution vaut la peine d'être recherchée pour ses pour et ses contre. C'est tout une question de résilience et de ténacité.

Alors à tous les développeurs là-bas, peu importe la situation dans laquelle vous vous trouvez, ne abandonnez pas. N'ayez pas peur d'essayer de nouvelles solutions et d'échouer. Restez positif et Bon Développement !

_Wilson Wang est un junior à UC Berkeley étudiant l'informatique et la science des données. Il s'intéresse au développement de logiciels pour améliorer les relations entre les entreprises et les clients. En dehors de la technologie, Wilson est passionné par les arts martiaux, la conception architecturale et la photographie de paysage._

![Image](https://cdn-media-1.freecodecamp.org/images/1*gcqfNtbXJmAFRUZiwkBHbw.jpeg)

#### Merci d'avoir lu ! Pour en savoir plus sur Blueprint, suivez-nous sur [Facebook](http://facebook.com/CalBlueprint) et [Instagram](https://www.instagram.com/calblueprint/), et visitez notre [site web](https://calblueprint.org/) !