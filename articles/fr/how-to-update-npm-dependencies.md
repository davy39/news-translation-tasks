---
title: Comment mettre à jour les dépendances NPM
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-07-05T22:55:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-npm-dependencies
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/deps.png
tags:
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: npm
  slug: npm
seo_title: Comment mettre à jour les dépendances NPM
seo_desc: 'The Node Package Manager (npm) provides various features to help you install
  and maintain your project''s dependencies.

  Dependencies can become outdated over time due to bug fixes, new features, and other
  updates. The more project dependencies you hav...'
---

Le Node Package Manager (npm) fournit diverses fonctionnalités pour vous aider à installer et maintenir les dépendances de votre projet.

Les dépendances peuvent devenir obsolètes avec le temps en raison des corrections de bugs, des nouvelles fonctionnalités et d'autres mises à jour. Plus vous avez de dépendances de projet, plus il est difficile de suivre ces mises à jour. 

Les packages obsolètes peuvent poser une menace pour la sécurité et avoir des effets négatifs sur les performances. Les packages à jour préviennent les vulnérabilités. Cela signifie que les vérifications et mises à jour périodiques des dépendances sont importantes.

## Comment maintenir les dépendances à jour

Maintenant, vous pourriez passer par chaque package individuel dans package.json un par un pour changer la version et exécuter `npm install <package>@latest` pour obtenir la dernière version. Mais ce n'est pas la méthode la plus efficace. 

Imaginez si vous aviez 20 packages ou plus qui pourraient utiliser une mise à jour de version. Au lieu de cela, vous devriez développer un flux de travail pour vérifier périodiquement les nouvelles versions avant que le nombre de dépendances obsolètes ne croisse et que cela devienne de plus en plus difficile à mettre à niveau.

Voici un flux de travail qui m'aide à rester à jour : d'abord, découvrir quels packages doivent être mis à jour et à quel point les versions sont en retard. Ensuite, choisir de mettre à jour les packages individuellement ou ensemble en lot. Toujours tester les mises à jour pour s'assurer qu'il n'y a pas eu de changements cassants.

Je préfère effectuer les mises à jour de versions majeures individuellement. Avec les mises à jour majeures, vous êtes susceptible de rencontrer des changements cassants. Il est beaucoup plus facile d'annuler ou d'adresser les changements de code en relation avec un package comparé à plusieurs.

Dans cet article, je vais passer en revue les méthodes pour inspecter et mettre à niveau les dépendances en détail.

## Comment utiliser la commande `npm outdated`

```
npm outdated
```

Cette commande vérifie chaque dépendance installée et compare la version actuelle avec la dernière version dans le [registre npm](https://www.npmjs.com/). Elle est imprimée sous forme de tableau décrivant les versions disponibles.

Elle est intégrée à npm, donc aucun package supplémentaire n'est requis pour le téléchargement. `npm outdated` est un bon point de départ pour avoir un aperçu du nombre de mises à jour de dépendances requises.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-03-at-1.14.41-PM.png)

* Current est la version actuelle installée.
* Wanted est la version maximale du package selon la plage [semver](https://docs.npmjs.com/misc/semver).
* Latest est la version du package marquée comme dernière dans le registre npm.

Avec cette méthode, pour installer les mises à jour pour chaque package, vous devez simplement exécuter :

```
npm update
```

Gardez à l'esprit qu'avec `npm update`, il ne mettra jamais à jour vers une version majeure avec des changements cassants. Il met à jour les dépendances dans package.json et package-lock.json. Il utilisera la version "wanted". 

Pour obtenir la version "latest", ajoutez `@latest` aux installations individuelles, par exemple `npm install react@latest`. 

## Comment utiliser `npm-check-updates`

Pour une expérience de mise à niveau avancée et personnalisable, je recommande [`npm-check-updates`](https://www.npmjs.com/package/npm-check-updates). Ce package peut faire tout ce que `npm outdated` et `npm upgrade` peuvent faire avec quelques options de personnalisation supplémentaires. Il nécessite cependant une installation de package.

Pour commencer, installez le package [`npm-check-updates`](https://www.npmjs.com/package/npm-check-updates) globalement :

```
npm install -g npm-check-updates
```

Ensuite, exécutez `ncu` pour afficher les packages à mettre à niveau. Similaire à `npm outdated`, il n'appliquera aucun changement.

```
ncu
Checking package.json
[====================] 12/12 100%

 @testing-library/user-event    ^13.5.0  →  ^14.2.1
 @types/jest                    ^27.5.2  →  ^28.1.4
 @types/node                  ^16.11.42  →  ^18.0.1

Run ncu -u to upgrade package.json
```

Pour mettre à niveau les dépendances, vous devez simplement exécuter :

```
ncu --upgrade

// ou 
ncu -u
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/screenshot.png)
_Ressource : [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)_

* Rouge = majeur
* Cyan = mineur
* Vert = patch

Cela met à jour les dépendances uniquement dans le fichier package.json et sélectionnera la dernière version même si elle inclut un changement cassant. Avec cette méthode, `npm install` n'est pas exécuté automatiquement, alors assurez-vous de l'exécuter ensuite pour mettre à jour package-lock.json.

Pour choisir votre type de version préféré, exécutez `ncu --target [patch, minor, latest, newest, greatest]`. 

### Comment utiliser le mode interactif avec `npm-check-updates`

```
ncu --interactive

// ou 
ncu -i
```

Le mode interactif vous permet de sélectionner des packages spécifiques à mettre à jour. Par défaut, tous les packages sont sélectionnés. 

Naviguez vers le bas à travers chaque package et utilisez la barre d'espace pour désélectionner, et entrez lorsque vous êtes prêt à mettre à niveau tous les packages sélectionnés. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/175337598-cdbb2c46-64f8-44f5-b54e-4ad74d7b52b4.png)
_Ressource : [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)_

Il existe plusieurs façons d'améliorer l'expérience interactive de `npm-check-updates`. 

```ncu
ncu --interactive --format group
```

Cette commande regroupe et organise les packages en versions majeures, mineures et patch.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/175336533-539261e4-5cf1-458f-9fbb-a7be2b477ebb--1-.png)
_Ressource : [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)_

`npm-check-updates` fournit d'autres outils utiles tels que le [mode doctor](https://github.com/raineorshine/npm-check-updates#doctor-mode) qui installe les mises à jour et exécute des tests pour vérifier les changements cassants. 

Je vous suggère vivement de consulter la [documentation](https://github.com/raineorshine/npm-check-updates) pour en savoir plus sur tout ce que ce package a à offrir. Le projet est bien maintenu avec un taux de téléchargement hebdomadaire en hausse d'environ ~[294,467](https://www.npmjs.com/package/npm-check-updates) au moment de la rédaction de cet article.

## Résumé

Prendre l'habitude de mettre régulièrement à jour vos dépendances aidera à la sécurité et aux performances de vos applications. 

Les outils `npm outdated` et `npm-check-updates` sont tous deux utiles pour vérifier les packages qui pourraient utiliser une mise à jour de version. 

Je suggère d'essayer ces deux méthodes pour voir laquelle offre une meilleure expérience développeur.

J'espère que ces méthodes vous aideront dans le processus de mise à jour !