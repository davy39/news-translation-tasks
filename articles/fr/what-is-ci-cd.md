---
title: Qu'est-ce que le CI/CD ? Apprenez l'intégration continue/déploiement continu
  en construisant un projet
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-04-07T19:31:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-ci-cd
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/jj-ying-4XvAZN8_WHo-unsplash.jpg
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
seo_title: Qu'est-ce que le CI/CD ? Apprenez l'intégration continue/déploiement continu
  en construisant un projet
seo_desc: 'Hi everyone! In this article you''re going to learn about CI/CD (continuous
  integration and continuous deployment).

  We''re going to review what this practice is about, how it compares to the previous
  approach in the software development industry, and f...'
---

Bonjour à tous ! Dans cet article, vous allez apprendre le CI/CD (intégration continue et déploiement continu).

Nous allons passer en revue ce que cette pratique implique, comment elle se compare à l'approche précédente dans l'industrie du développement logiciel, et enfin voir un exemple pratique de la manière dont nous pouvons l'implémenter dans nos projets.

C'est parti !

# Table des matières

* [Intro](#heading-intro)
    
* [Comment fonctionne le CI/CD](#heading-comment-fonctionne-le-cicd)
    
* [Les principaux avantages du CI/CD](#heading-les-principaux-avantages-du-cicd)
    
* [Outils pour le CI/CD](#heading-outils-pour-le-cicd)
    
* [Comment configurer un pipeline CI/CD avec GitHub Actions](#heading-comment-configurer-un-pipeline-cicd-avec-github-actions)
    
    * [Initialisation du projet](#heading-initialisation-du-projet)
        
    * [Qu'est-ce que GitHub Actions et comment fonctionne-t-il ?](#heading-quest-ce-que-github-actions-et-comment-fonctionne-t-il)
        
    * [Configuration de notre workflow](#heading-configuration-de-notre-workflow)
        
    * [La magie](#heading-la-magie)
        
* [Conclusion](#heading-conclusion)
    

# Intro

L'intégration continue et la livraison continue (CI/CD) est une approche de développement logiciel qui vise à améliorer la vitesse, l'efficacité et la fiabilité de la livraison de logiciels. Cette approche implique une intégration fréquente du code, des tests automatisés et un déploiement continu des modifications logicielles en production.

Avant l'adoption du CI/CD dans l'industrie du développement logiciel, l'approche courante était un modèle traditionnel, **en cascade**, de développement logiciel.

Dans cette approche, les développeurs travaillaient en silos, chaque étape du cycle de vie du développement logiciel étant complétée en séquence. Le processus impliquait généralement la collecte des exigences, la conception du logiciel, le codage, les tests et le déploiement.

**Les inconvénients de cette approche traditionnelle incluent :**

1. **Cycles de publication lents :** Puisque chaque étape du cycle de vie du développement logiciel était complétée en séquence, le cycle de publication était lent, ce qui rendait difficile une réponse rapide aux besoins changeants des clients.
    
2. **Taux d'échec élevés :** Les projets logiciels étaient sujettes à des échecs en raison d'un manque de tests automatisés, ce qui signifiait que les développeurs devaient compter sur des tests manuels, entraînant des erreurs et des bugs dans le code.
    
3. **Collaboration limitée :** L'approche traditionnelle ne favorisait pas la collaboration entre les développeurs, les testeurs et les autres parties prenantes, ce qui rendait difficile l'identification et la correction des problèmes.
    
4. **Coût élevé :** La nature manuelle du développement logiciel signifiait qu'il était coûteux, avec des coûts élevés associés aux tests, au débogage et à la correction des erreurs.
    
5. **Agilité limitée :** Puisque l'approche traditionnelle était linéaire, il n'était pas possible d'apporter des modifications au logiciel rapidement ou de répondre aux besoins des clients en temps réel.
    

Le CI/CD est apparu comme une solution à ces inconvénients, en introduisant une approche plus agile et collaborative du développement logiciel. Le CI/CD permet aux équipes de travailler ensemble, d'intégrer leurs modifications de code fréquemment et d'automatiser le processus de test et de déploiement.

# Comment fonctionne le CI/CD

Le CI/CD est un processus automatisé qui implique une intégration fréquente du code, des tests automatisés et un déploiement continu des modifications logicielles en production.

Expliquons chaque étape un peu plus en détail :

### Intégration du code

La première étape du pipeline CI/CD est l'intégration du code. Dans cette étape, les développeurs soumettent leurs modifications de code à un dépôt distant (comme [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/) ou [BitBucket](https://bitbucket.org/product/)), où le code est intégré à la base de code principale.

Cette étape vise à garantir que les modifications de code sont compatibles avec le reste de la base de code et ne cassent pas la build.

### Tests automatisés

Une fois le code intégré, l'étape suivante est celle des tests automatisés. Les tests automatisés impliquent l'exécution d'une suite de tests pour garantir que les modifications de code sont fonctionnelles, répondent aux normes de qualité attendues et sont exemptes de défauts.

Cette étape permet d'identifier les problèmes tôt dans le processus de développement, permettant aux développeurs de les corriger rapidement et efficacement.

Si vous n'êtes pas familier avec le sujet des tests, vous pouvez vous référer [à cet article que j'ai écrit il y a quelque temps](https://www.freecodecamp.org/news/test-a-react-app-with-jest-testing-library-and-cypress/).

### Déploiement continu

Après que les modifications de code aient passé l'étape des tests automatisés, l'étape suivante est le déploiement continu. Dans cette étape, les modifications de code sont automatiquement déployées dans un environnement de pré-production pour des tests supplémentaires.

Cette étape vise à garantir que le logiciel est continuellement mis à jour avec les dernières modifications de code, livrant de nouvelles fonctionnalités aux utilisateurs rapidement et efficacement.

### Déploiement en production

L'étape finale du pipeline CI/CD est le déploiement en production. Dans cette étape, les modifications logicielles sont publiées pour les utilisateurs finaux. Cette étape implique la surveillance de l'environnement de production, garantissant que le logiciel fonctionne sans problème, et l'identification et la correction de tout problème qui survient.

Les quatre étapes d'un pipeline CI/CD fonctionnent ensemble pour garantir que les modifications logicielles sont testées, intégrées et déployées en production automatiquement. Cette automatisation aide à réduire les erreurs, à augmenter l'efficacité et à améliorer la qualité globale du logiciel.

En adoptant un pipeline CI/CD, les équipes de développement peuvent atteindre des cycles de publication plus rapides, réduire le risque de défauts logiciels et améliorer l'expérience utilisateur.

Gardez à l'esprit que les étapes du pipeline peuvent varier en fonction du projet ou de l'entreprise spécifique dont nous parlons. Cela signifie que certaines équipes peuvent ou non utiliser des tests automatisés, certaines équipes peuvent ou non avoir un environnement de "pré-production", et ainsi de suite.

Les parties clés qui constituent la pratique CI/CD sont l'intégration et le déploiement. Cela signifie que le code doit être continuellement intégré dans un dépôt distant, et que ce code doit être continuellement déployé dans un environnement donné après chaque intégration.

# Les principaux avantages du CI/CD

Les principaux avantages du CI/CD incluent :

1. **Cycles de publication plus rapides :** En automatisant le processus de test et de déploiement, le CI/CD permet aux équipes de publier des logiciels plus fréquemment, répondant rapidement aux besoins des clients.
    
2. **Qualité améliorée :** Les tests automatisés garantissent que les modifications logicielles n'introduisent pas de nouveaux bugs ou problèmes, améliorant la qualité globale du logiciel.
    
3. **Collaboration accrue :** L'intégration et les tests fréquents du code nécessitent que les développeurs travaillent en étroite collaboration, conduisant à une meilleure collaboration et communication.
    
4. **Risque réduit :** Le déploiement continu permet aux développeurs d'identifier et de corriger rapidement les problèmes, réduisant le risque de pannes majeures et de temps d'arrêt.
    
5. **Économique :** Le CI/CD réduit la quantité de travail manuel nécessaire pour déployer les modifications logicielles, économisant du temps et réduisant les coûts.
    

En résumé, le CI/CD est apparu comme une solution aux limitations de l'approche traditionnelle et linéaire du développement logiciel. En introduisant une approche plus agile et collaborative du développement logiciel, le CI/CD permet aux équipes de travailler ensemble, de publier des logiciels plus fréquemment et de répondre rapidement aux besoins des clients.

# Outils pour le CI/CD

Il existe plusieurs outils disponibles pour implémenter des pipelines CI/CD dans le développement logiciel. Chaque outil a ses propres caractéristiques, avantages et inconvénients. Voici quelques-uns des outils les plus couramment utilisés dans les pipelines CI/CD aujourd'hui :

### Jenkins

[Jenkins](https://www.jenkins.io/) est un serveur d'automatisation open-source largement utilisé dans les pipelines CI/CD. Il est hautement personnalisable et prend en charge une large gamme de plugins, ce qui le rend adapté à divers environnements de développement. Voici quelques-unes de ses principales caractéristiques :

**Avantages :**

* Hautement personnalisable avec une large gamme de plugins
    
* Prend en charge l'intégration avec divers outils et technologies
    
* Fournit des rapports et des analyses détaillés
    

**Inconvénients :**

* Nécessite une certaine expertise technique pour la configuration et la maintenance
    
* Peut être gourmand en ressources, surtout pour les grands projets
    
* Manque d'un tableau de bord centralisé pour gérer plusieurs projets
    

Si vous souhaitez en savoir plus sur Jenkins, [voici un cours complet pour vous](https://www.freecodecamp.org/news/learn-jenkins-by-building-a-ci-cd-pipeline/).

### Travis CI

[Travis CI](https://www.travis-ci.com/) est une plateforme CI/CD basée sur le cloud qui fournit des tests et un déploiement automatisés pour les projets logiciels. Il prend en charge plusieurs langages de programmation et frameworks, ce qui le rend adapté à divers environnements de développement. Voici quelques-unes de ses principales caractéristiques :

**Avantages :**

* Facile à configurer et à utiliser
    
* Basé sur le cloud, donc pas besoin de configurer et de maintenir une infrastructure
    
* Prend en charge une large gamme de langages de programmation et de frameworks
    
* Fournit des rapports et des analyses détaillés
    

**Inconvénients :**

* Options de personnalisation limitées
    
* Non adapté aux grands projets avec des exigences complexes
    
* Prise en charge limitée pour les installations sur site
    

Voici un tutoriel utile sur [comment automatiser le déploiement sur GitHub Pages avec Travis CI](https://www.freecodecamp.org/news/learn-how-to-automate-deployment-on-github-pages-with-travis-ci/).

### GitHub Actions

[GitHub Actions](https://github.com/features/actions) est un outil CI/CD puissant qui permet aux développeurs d'automatiser les workflows, d'exécuter des tests et de déployer du code directement depuis leurs dépôts GitHub.

**Avantages :**

* Intégré avec GitHub
    
* Facile à utiliser
    
* Fournit un large écosystème et une bonne documentation
    

**Inconvénients :**

* Minutes de build limitées
    
* Syntaxe YAML complexe
    

Commentaire à part : Je mentionne GitHub Actions ici parce que c'est un outil populaire – mais gardez à l'esprit que d'autres fournisseurs de dépôts en ligne comme GitLab et BitBucket offrent également des options très similaires à GitHub Actions.

### Fonctionnalités CI/CD intégrées par les hébergeurs

Les hébergeurs populaires tels que [Vercel](https://vercel.com/) ou [Netlify](https://www.netlify.com/) disposent de fonctionnalités CI/CD intégrées qui vous permettent de lier un dépôt en ligne à un site donné et de déployer sur ce site après qu'un événement donné se produise dans ce dépôt.

**Avantages :**

* Très simple à configurer et à utiliser
    

**Inconvénients :**

* Options de personnalisation limitées
    

Chacun de ces outils a ses propres caractéristiques, avantages et inconvénients. Le choix de l'outil dépendra des exigences spécifiques de votre projet, de l'expertise technique de votre équipe et de votre budget.

Voici un tutoriel sur [comment déployer une application front-end avec Netlify](https://www.freecodecamp.org/news/how-to-deploy-your-front-end-app/). Et dans ce tutoriel, vous apprendrez [comment utiliser Vercel pour déployer une application Next.js](https://www.freecodecamp.org/news/how-to-build-a-jamstack-site-with-next-js-and-vercel-jamstack-handbook/).

# Comment configurer un pipeline CI/CD avec GitHub Actions

Super, maintenant que nous avons une idée claire de ce qu'est le CI/CD, voyons comment nous pouvons implémenter un exemple simple avec un projet réel en utilisant [GitHub Actions](https://github.com/features/actions).

## Initialisation du projet

Nous allons commencer avec une application React très basique construite avec [Vite](https://www.freecodecamp.org/news/how-to-build-a-react-app-different-ways/#what-is-vite). Vous pouvez le faire en exécutant `yarn create vite` dans votre console.

Nous allons nous concentrer sur le pipeline CI/CD ici, donc il n'y aura pas de complexité dans le code de l'application lui-même. Mais juste pour avoir une idée, le composant `app.jsx` aura ce code :

```javascript
import './App.css';

function App() {

	return (
		<div className='App'>
			<h1>Vite + Reactooooo</h1>
		</div>
	);
}

export default App;
```

Et ensuite, nous aurons un fichier de test qui vérifiera que ce texte est rendu :

```javascript
import { describe, expect, it } from 'vitest';
import { render, screen } from './utils/test-utils/test-utils.jsx';

import App from 'src/App.jsx';

describe('App', async () => {
	it('should render while authenticating', () => {
		render(<App />);

		expect(screen.getByText('Vite + Reactooooo')).toBeInTheDocument();
	});
});
```

Ce test s'exécutera chaque fois que nous exécuterons la commande `yarn test`.

L'étape suivante devrait être de pousser notre code vers un dépôt GitHub. Ensuite, parlons un peu plus de ce que sont GitHub Actions et comment ils fonctionnent.

## Qu'est-ce que GitHub Actions et comment fonctionne-t-il ?

GitHub Actions est un service CI/CD (Intégration Continue/Déploiement Continu) fourni par GitHub. Il permet aux développeurs d'automatiser les workflows en définissant des scripts personnalisés, connus sous le nom d'"actions", qui peuvent être déclenchés par des événements tels que des pushs vers un dépôt, des pull requests ou des issues.

Les actions sont définies dans un fichier YAML, également connu sous le nom de "workflow", qui spécifie les étapes nécessaires pour accomplir une tâche. Les workflows GitHub Actions peuvent s'exécuter sur des environnements Linux, Windows et macOS et prennent en charge une large gamme de langages de programmation et de frameworks.

Lorsque qu'un événement déclenche un workflow GitHub Actions, le service crée un nouvel environnement, installe les dépendances et exécute les étapes définies dans l'ordre spécifié. Cela peut inclure des tâches telles que la construction, les tests, l'emballage et le déploiement du code.

GitHub Actions fournit également plusieurs actions intégrées qui peuvent être utilisées pour simplifier les tâches courantes, telles que la récupération du code, la construction et les tests des applications, la publication des versions et le déploiement sur des fournisseurs de cloud populaires comme AWS, Azure et Google Cloud.

Les workflows GitHub Actions peuvent être exécutés selon un calendrier, manuellement ou automatiquement lorsqu'un événement spécifique se produit, comme l'ouverture d'une pull request ou le push d'un nouveau commit vers une branche.

## Configuration de notre workflow

Super, donc comme nous l'avons vu, GitHub Actions est une fonctionnalité qui nous permet de définir des workflows pour nos projets. Ces workflows ne sont rien d'autre qu'une série de tâches ou d'étapes qui s'exécuteront sur le cloud de GitHub après un événement donné que nous déclarons.

La manière dont GitHub lit et exécute ces workflows est en lisant automatiquement les fichiers dans le répertoire `.github/workflows` à la racine de notre projet. Ces fichiers de workflow doivent avoir l'extension `.yaml` et utiliser la syntaxe [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml).

Pour créer un nouveau workflow, nous devons simplement créer un nouveau fichier YAML dans ce répertoire. Nous appellerons le nôtre `prod.yaml` puisque nous l'utiliserons pour déployer la branche de production de notre projet.

Gardez à l'esprit qu'un seul projet peut avoir de nombreux workflows différents qui exécutent différentes tâches à différentes occasions. Par exemple, nous pourrions avoir un workflow pour les branches de développement et de pré-production également, car ces environnements pourraient nécessiter différentes tâches à exécuter et se déployeront probablement sur différents sites.

Après avoir créé ce fichier, ajoutons le code suivant :

```yaml
# Nom de notre workflow
name: Production deploy

# Déclencher le workflow sur push vers la branche main
on:
  push:
    branches:
      - main

# Liste des jobs
# Un "job" est un ensemble d'étapes qui sont exécutées sur le même runner
jobs:
  # Nom du job
  test-and-deploy-to-netlify:
    # Système d'exploitation à utiliser
    runs-on: ubuntu-latest

    # Liste des étapes qui composent le job
    steps:
    # Récupère votre dépôt sous $GITHUB_WORKSPACE, afin que votre job puisse y accéder
    - name: Checkout code
      uses: actions/checkout@v2

    # Configuration de l'environnement Node.js
    - name: Use Node.js 16.x
      uses: actions/setup-node@v2
      with:
        node-version: '16.x'

    # Installation des dépendances
    - name: Install dependencies
      run: yarn install

    # Exécution des tests
    - name: Run tests
      run: yarn test

    # Déploiement sur Netlify
    - name: Netlify Deploy
      uses: jsmrcaga/action-netlify-deploy@v2.0.0
      with:
        # Jeton d'authentification à utiliser avec Netlify
        NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
        # Votre identifiant de site Netlify
        NETLIFY_SITE_ID:  ${{ secrets.NETLIFY_SITE_ID }}
        # Répertoire où les fichiers construits sont stockés
        build_directory: './dist'
        # Commande pour installer les dépendances
        install_command: yarn install
        # Commande pour construire le site web statique
        build_command: yarn build
```

Donc, notre workflow a les tâches suivantes déclarées :

1. Étape "Checkout code" qui récupère le dernier commit sur la branche actuelle.
    
2. Étape "Use Node.js 16.x" qui configure l'environnement Node.js à la version 16.x.
    
3. Étape "Install dependencies" qui installe les dépendances du projet en utilisant le gestionnaire de paquets Yarn.
    
4. Étape "Run tests" qui exécute les tests du projet en utilisant le gestionnaire de paquets Yarn.
    
5. Étape "Netlify Deploy" qui déploie le projet sur Netlify en utilisant l'action jsmrcaga/action-netlify-deploy. Cette étape utilise les secrets de jeton d'authentification et d'identifiant de site Netlify stockés dans les secrets du dépôt GitHub. Le répertoire de build, la commande d'installation et la commande de build sont également spécifiés.
    

Vous avez probablement remarqué que les première et dernière étapes ont le mot-clé `uses`. Ce mot-clé vous permet d'utiliser des actions ou des workflows développés par d'autres utilisateurs de GitHub, et c'est l'une des meilleures fonctionnalités de GitHub Actions.

Ce qui est génial, c'est qu'en utilisant ces actions tierces, nous pouvons exécuter des tâches complexes telles que le déploiement sur un hébergeur externe ou la construction d'une infrastructure cloud complexe sans avoir besoin d'écrire chaque ligne de code nécessaire.

Comme ces tâches tendent à être répétitives et fréquemment exécutées dans de nombreux projets, nous pouvons simplement utiliser un workflow développé par un compte d'entreprise officiel (comme Azure ou AWS par exemple) ou un développeur open-source indépendant. Pensez à cela comme utiliser une bibliothèque tierce. C'est la même idée mais appliquée aux workflows CI/CD. Très pratique.

Une autre chose importante à mentionner ici est que dans les workflows GitHub Actions, les tâches s'exécutent **séquentiellement**, l'une après l'autre. Et si une tâche donnée échoue ou génère une erreur, **la suivante ne s'exécutera pas**. Cela est important car si nous avons un problème lors de l'installation de nos dépendances ou si un test échoue, nous ne voulons pas que ce code soit déployé.

Avant de pouvoir pousser ce code et voir comment la magie fonctionne, nous devons d'abord créer un site sur Netlify et obtenir le **NETLIFY\_AUTH\_TOKEN** et le **NETLIFY\_SITE\_ID**. C'est assez simple même si vous n'avez pas d'expérience préalable avec Netlify, alors essayez et cherchez un peu sur Google si vous ne trouvez pas. ;)

Une fois que vous avez ces deux jetons, vous devez les déclarer comme secrets de dépôt dans votre dépôt GitHub. Vous pouvez le faire à partir de l'onglet "settings" :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-32.png align="left")

*Configurez les deux jetons secrets Netlify dans votre dépôt*

Avec cela en place, notre fichier `prod.yaml` pourra maintenant lire ces deux jetons et exécuter l'action de déploiement Netlify.

## La magie

Maintenant que nous avons tout en place, poussons notre code et voyons comment cela se passe.

Après avoir poussé, si nous allons à l'onglet "actions" de notre dépôt, à gauche nous verrons une liste de tous les workflows que nous avons dans notre dépôt. Et à droite nous verrons une liste de chaque exécution du workflow sélectionné. Puisque notre workflow s'exécute après chaque push, nous devrions voir une nouvelle exécution chaque fois que nous poussons.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-33.png align="left")

*Une exécution de workflow*

Lorsque l'exécution a une lumière jaune à gauche, cela signifie qu'elle est encore en cours d'exécution (exécution des tâches). Si elle a une lumière verte, cela signifie qu'elle a terminé son exécution avec succès et si la lumière est rouge, vous savez que quelque chose a mal tourné, haha...

Après avoir cliqué sur l'exécution, nous pouvons voir une liste des jobs du workflow (nous n'en avions qu'un seul).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-34.png align="left")

*Les jobs du workflow*

Et après avoir cliqué sur le job, nous pouvons voir une liste des tâches du job.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-35.png align="left")

*Les tâches du job*

Chaque tâche est extensible et à l'intérieur nous pouvons voir les logs correspondant à l'exécution de cette tâche. C'est assez utile pour le débogage. ;)

Maintenant, si nous allons sur notre site Netlify précédemment configuré, nous devrions voir notre application en cours d'exécution !

Et maintenant que nous avons notre pipeline CI/CD en place, nous pouvons déployer notre application après chaque push vers la branche principale, tout cela sans lever le petit doigt. =D

# **Conclusion**

Le CI/CD est une approche de développement logiciel qui offre plusieurs avantages aux équipes de développement logiciel, notamment un temps de mise sur le marché plus rapide, une qualité améliorée, une collaboration accrue, un risque réduit et une rentabilité.

En automatisant le pipeline de livraison de logiciels, les équipes peuvent rapidement déployer de nouvelles fonctionnalités et des corrections de bugs, tout en réduisant le risque de pannes majeures et de temps d'arrêt.

Avec la disponibilité de plusieurs outils CI/CD, il est devenu plus facile pour les équipes de mettre en œuvre cette approche et d'améliorer leur processus de livraison de logiciels.

Eh bien, tout le monde, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/03/giphy-1.gif align="left")