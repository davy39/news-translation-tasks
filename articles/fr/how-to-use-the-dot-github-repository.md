---
title: Comment utiliser le dépôt .github
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-14T18:01:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-dot-github-repository
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Thumbnail.png
tags:
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment utiliser le dépôt .github
seo_desc: 'By Anish De

  GitHub has many special repositories. For instance, you can create a repository
  that matches your username, add a README file to it, and all the information in
  that file will be visible on your GitHub profile.

  You might already be familia...'
---

Par Anish De

GitHub possède de nombreux dépôts spéciaux. Par exemple, vous pouvez créer un dépôt qui correspond à votre nom d'utilisateur, y ajouter un fichier README, et toutes les informations de ce fichier seront visibles sur votre profil GitHub.

Vous êtes peut-être déjà familier avec le répertoire `.github` que vous trouverez dans de nombreux dépôts. Le répertoire `.github` contient des workflows, des modèles de problèmes, des modèles de pull request, des informations de financement et d'autres fichiers spécifiques à ce projet.

Mais un autre dépôt spécial que vous pouvez créer est le dépôt `.github`. Il sert de solution de repli pour tous vos dépôts qui n'ont pas de répertoire `.github` avec des modèles de problèmes et d'autres fichiers de santé communautaire.

Par exemple, supposons que j'ai un dépôt nommé `.github` avec des modèles de problèmes génériques pour les rapports de bugs et les demandes de fonctionnalités. Et supposons que je crée un autre dépôt appelé `new-project`, mais que je n'y ajoute pas de répertoire `.github` avec des modèles de problèmes.

Alors, si quelqu'un va dans le dépôt `new-project` et ouvre un problème, il lui sera présenté une option pour choisir parmi les modèles génériques déjà dans le répertoire `.github`.

De même, si j'ajoute un code de conduite à mon dépôt `.github`, il sera affiché dans tous mes dépôts qui n'en ont pas explicitement un.

Notez simplement que les fichiers à l'intérieur du répertoire `.github` d'un dépôt seront choisis plutôt que ceux du dépôt `.github`. Par exemple, si mon dépôt `new-project` a un répertoire `.github` avec un modèle de demande de fonctionnalité à l'intérieur, celui-ci sera utilisé au lieu du modèle de demande de fonctionnalité générique du dépôt `.github`.

Voyons comment ce dépôt spécial fonctionne en action.

## Comment utiliser .github sur les comptes GitHub personnels

Créer ce dépôt spécial est aussi simple que de créer n'importe quel autre dépôt sur GitHub. Alors, allez-y et ouvrez GitHub dans votre navigateur web et créez le dépôt comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Xo__mfEdt.png)
_Création d'un dépôt .github sur mon compte GitHub personnel_

Après avoir créé le dépôt, vous pouvez commencer à y ajouter des fichiers. Le premier fichier que je vais ajouter est un formulaire de rapport de bug. Je ne vais pas entrer dans les détails de la création d'un formulaire de problème dans cet article, mais vous pouvez consulter un [article précédent que j'ai écrit sur les formulaires de problèmes GitHub](https://blog.anishde.dev/creating-a-bug-report-form-in-github).

`.github/ISSUE_TEMPLATE/bug_report.yml` 

```yml
name: 🐛 Rapport de Bug
description: Déposer un rapport de bug ici
title: "[BUG]: "
labels: ["bug"]
assignees: ["AnishDe12020"]
body:
  - type: markdown
    attributes:
      value: |
        Merci d'avoir pris le temps de remplir ce rapport de bug 🤗
        Assurez-vous qu'il n'y a pas de problèmes ouverts/fermés pour ce sujet 😃
        
  - type: textarea
    id: bug-description
    attributes:
      label: Description du bug
      description: Donnez-nous une brève description de ce qui s'est passé et de ce qui aurait dû se passer
    validations:
      required: true
      
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Étapes pour reproduire
      description: Étapes pour reproduire le comportement.
      placeholder: |
        1. Allez à '...'
        2. Cliquez sur '...'
        3. Faites défiler jusqu'à '...'
        4. Voir l'erreur
    validations:
      required: true
  - type: textarea
    id: additional-information
    attributes:
      label: Informations supplémentaires
      description: |
        Fournissez toute information supplémentaire telle que des logs, des captures d'écran, des scénarios dans lesquels le bug se produit afin de faciliter la résolution du problème.

```

Je vais également créer un formulaire de demande de fonctionnalité.

`.github/ISSUE_TEMPLATE/feature_request.yml` 

```yml
name: ✨ Demande de Fonctionnalité
description: Demander une nouvelle fonctionnalité ou amélioration
labels: ["enhancement"]
title: "[FEAT]: "
body:
  - type: markdown
    attributes:
      value: |
        Veuillez vous assurer que cette demande de fonctionnalité n'a pas déjà été soumise par quelqu'un en consultant les autres problèmes ouverts/fermés
  
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Donnez-nous une brève description de la fonctionnalité ou de l'amélioration que vous aimeriez
    validations:
      required: true
      
  - type: textarea
    id: additional-information
    attributes:
      label: Informations supplémentaires
      description: Donnez-nous quelques informations supplémentaires sur la demande de fonctionnalité comme des solutions proposées, des liens, des captures d'écran, etc.

```

Je vais également ajouter un modèle de pull request.

`.github/pull_request_template.md`

```md
<!-- 
Merci d'avoir créé cette pull request 🤗

Veuillez vous assurer que la pull request est limitée à un type (docs, fonctionnalité, etc.) et gardez-la aussi petite que possible. Vous pouvez ouvrir plusieurs prs au lieu d'en ouvrir une énorme.
-->

<!-- Si cette pull request ferme un problème, veuillez mentionner le numéro du problème ci-dessous -->
Closes # <!-- Numéro du problème ici -->

## 📝 Description
<!-- Ajoutez une brève description de la pr -->

<!-- Vous pouvez également choisir d'ajouter une liste de changements et s'ils ont été complétés ou non en utilisant la syntaxe de liste de tâches markdown
- [ ] Non complété
- [x] Complété
-->

## ✅ Vérifications
<!-- Assurez-vous que votre pr passe les vérifications CI et vérifiez les champs suivants si nécessaire - -->
- [ ] Ma pull request adhère au style de code de ce projet
- [ ] Mon code nécessite des changements dans la documentation
- [ ] J'ai mis à jour la documentation comme requis
- [ ] Tous les tests ont passé

## ℹ️ Informations supplémentaires
<!-- Toute information supplémentaire comme des changements majeurs, des dépendances ajoutées, des captures d'écran, des comparaisons entre le nouveau et l'ancien comportement, etc. -->

```

Le dernier fichier que je vais ajouter est un code de conduite – mais celui-ci sera à la racine du dépôt. Malgré cela, cela fonctionnera comme prévu (les fichiers de code de conduite sont généralement conservés à la racine du dépôt). Notez que j'utilise la convention [Contributor Covenant](https://www.contributor-covenant.org/).

`CODE_OF_CONDUCT.md` 

```md

# Code de conduite de Contributor Covenant

## Notre engagement

En tant que membres, contributeurs et leaders, nous nous engageons à faire en sorte que la participation à notre
communauté soit une expérience sans harcèlement pour tout le monde, indépendamment de l'âge, de la taille du corps,
d'un handicap visible ou invisible, de l'ethnicité, des caractéristiques sexuelles, de l'identité et de l'expression de genre,
du niveau d'expérience, de l'éducation, du statut socio-économique, de la nationalité, de l'apparence personnelle,
de la race, de la caste, de la couleur, de la religion, ou de l'identité et de l'orientation sexuelle.

Nous nous engageons à agir et à interagir de manière à contribuer à une communauté ouverte, accueillante,
diverse, inclusive et saine.

## Nos normes

Des exemples de comportement qui contribuent à un environnement positif pour notre
communauté incluent :

* Faire preuve d'empathie et de gentillesse envers les autres
* Être respectueux des opinions, points de vue et expériences différents
* Donner et accepter gracieusement des commentaires constructifs
* Accepter la responsabilité et s'excuser auprès de ceux affectés par nos erreurs,
  et apprendre de l'expérience
* Se concentrer sur ce qui est meilleur non seulement pour nous en tant qu'individus, mais pour l'ensemble
  de la communauté

Des exemples de comportement inacceptable incluent :

* L'utilisation de langage ou d'images sexualisés, et l'attention ou les avances sexuelles
  de quelque nature que ce soit
* Le trolling, les commentaires insultants ou dérogatoires, et les attaques personnelles ou politiques
* Le harcèlement public ou privé
* La publication d'informations privées d'autrui, telles qu'une adresse physique ou électronique,
  sans leur permission explicite
* Tout autre comportement qui pourrait raisonnablement être considéré comme inapproprié dans un
  cadre professionnel

## Responsabilités d'application

Les leaders de la communauté sont responsables de clarifier et de faire respecter nos normes de
comportement acceptable et prendront des mesures correctives appropriées et équitables en
réponse à tout comportement qu'ils jugent inapproprié, menaçant, offensant,
ou nuisible.

Les leaders de la communauté ont le droit et la responsabilité de supprimer, modifier ou rejeter
les commentaires, commits, code, modifications de wiki, problèmes et autres contributions qui
ne sont pas alignés avec ce Code de Conduite, et communiqueront les raisons des décisions de modération
lorsque cela est approprié.

## Portée

Ce Code de Conduite s'applique dans tous les espaces communautaires, et s'applique également lorsqu'
un individu représente officiellement la communauté dans des espaces publics.
Des exemples de représentation de notre communauté incluent l'utilisation d'une adresse e-mail officielle,
la publication via un compte de réseau social officiel, ou l'action en tant que représentant désigné
lors d'un événement en ligne ou hors ligne.

## Application

Les cas de comportement abusif, de harcèlement ou autrement inacceptable peuvent être
signalés aux leaders de la communauté responsables de l'application à
[INSERT CONTACT METHOD].
Toutes les plaintes seront examinées et enquêtées rapidement et équitablement.

Tous les leaders de la communauté sont tenus de respecter la vie privée et la sécurité du
signalant de tout incident.

## Lignes directrices pour l'application

Les leaders de la communauté suivront ces Lignes directrices d'impact communautaire pour déterminer
les conséquences de toute action qu'ils jugent en violation de ce Code de Conduite :

### 1. Correction

**Impact communautaire** : Utilisation de langage inapproprié ou autre comportement jugé
non professionnel ou indésirable dans la communauté.

**Conséquence** : Un avertissement écrit privé des leaders de la communauté, fournissant
de la clarté sur la nature de la violation et une explication de pourquoi le
comportement était inapproprié. Une excuse publique peut être demandée.

### 2. Avertissement

**Impact communautaire** : Une violation par un incident unique ou une série d'
actions.

**Conséquence** : Un avertissement avec des conséquences pour un comportement continu. Aucune
interaction avec les personnes impliquées, y compris une interaction non sollicitée avec
ceux qui appliquent le Code de Conduite, pendant une période de temps spécifiée. Cela
inclut l'évitement des interactions dans les espaces communautaires ainsi que les canaux externes
comme les réseaux sociaux. La violation de ces termes peut conduire à une interdiction temporaire ou permanente.

### 3. Interdiction temporaire

**Impact communautaire** : Une violation grave des normes communautaires, incluant
un comportement inapproprié soutenu.

**Conséquence** : Une interdiction temporaire de toute sorte d'interaction ou de communication publique
avec la communauté pendant une période de temps spécifiée. Aucune interaction publique ou
privée avec les personnes impliquées, y compris une interaction non sollicitée avec
ceux qui appliquent le Code de Conduite, n'est autorisée pendant cette période.
La violation de ces termes peut conduire à une interdiction permanente.

### 4. Interdiction permanente

**Impact communautaire** : Démontrer un schéma de violation des normes communautaires, incluant
un comportement inapproprié soutenu, le harcèlement d'un
individu, ou l'agression ou le dénigrement de classes d'individus.

**Conséquence** : Une interdiction permanente de toute sorte d'interaction publique au sein de la
communauté.

## Attribution

Ce Code de Conduite est adapté de [Contributor Covenant][homepage],
version 2.1, disponible à
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Les Lignes directrices d'impact communautaire ont été inspirées par
[L'échelle d'application du code de conduite de Mozilla][Mozilla CoC].

Pour des réponses aux questions courantes sur ce code de conduite, voir la FAQ à
[https://www.contributor-covenant.org/faq][FAQ]. Des traductions sont disponibles à
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

Nous pouvons ajouter plus de fichiers comme des informations de financement, des guides de contribution, et bien plus. Pour plus d'informations, vous pouvez consulter la [documentation GitHub concernant les fichiers de santé communautaire](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

### Le dépôt `.github` en action

Mon [dépôt de blogs](https://github.com/AnishDe12020/blog) n'a aucun modèle de problème, code de conduite, ou autre fichier à part les fichiers markdown de mes blogs et un README. C'est donc le meilleur dépôt pour tester si cette fonctionnalité fonctionne ou non.

Je peux déjà voir le code de conduite apparaître ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/4Dk1gl1ZS.png)

Si j'essaie de créer un problème, je suis présenté avec les modèles également :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/5fqH-4IYX.png)

Cela fonctionnera également lors de la création d'une pull request.

## Comment utiliser le dépôt .github pour une organisation/compte public

Le dépôt `.github` sur un compte d'organisation fonctionne exactement comme le dépôt `.github` sur un compte GitHub personnel – sauf qu'il y a une différence.

Les organisations peuvent également avoir des README de profil qui apparaissent sur la page de l'organisation sur GitHub. Ce README réside dans le répertoire `profile` du dépôt `.github` de l'organisation. Pour démontrer cela, je vais rapidement créer une organisation de démonstration.

Lors de la création du dépôt `.github` pour une organisation, vous devriez obtenir ce message :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/s2QEAhtHG-1.png)

De plus, lors de l'ajout du README de profil à `profile/README.md`, vous devriez obtenir ce message :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/vf0IEmbTH-1.png)
_Création d'un README d'organisation GitHub_

Maintenant, je vais ajouter du contenu à ce fichier README et le commiter. Lorsque je visite la page d'accueil de l'organisation, voici ce que nous devrions voir :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/svqbJ3PfG.png)
_Voir le contenu du README du profil de l'organisation GitHub sur la page de l'organisation_

## Conclusion

J'espère que vous savez maintenant ce que fait le dépôt `.github`. Vous devriez également savoir comment configurer des fichiers de santé communautaire par défaut pour vos dépôts et un README de profil pour votre organisation.

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/AnishDe12020) et passez une bonne journée 😃

### Ressources

* [Documentation GitHub sur les fichiers de santé communautaire](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
* [Mon dépôt `.github`](https://github.com/AnishDe12020/.github)
* [Le dépôt `.github` de mon organisation de test](https://github.com/AnishDe12020-test/.github)
* [Contributor Covenant](https://www.contributor-covenant.org/)
* [Article sur la prise en main des formulaires de problèmes GitHub](https://blog.anishde.dev/creating-a-bug-report-form-in-github)

Je travaille actuellement sur un projet appelé DevKit qui est une PWA qui abritera des outils de développement dans une seule application et fournira des moyens pour accomplir votre travail rapidement. N'hésitez pas à le consulter sur [https://www.devkit.one/](https://www.devkit.one/).