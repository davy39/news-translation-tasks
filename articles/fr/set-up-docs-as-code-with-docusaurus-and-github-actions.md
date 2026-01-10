---
title: Comment configurer la documentation en tant que code avec Docusaurus et GitHub
  Actions
subtitle: ''
author: EZINNE ANNE EMILIA
co_authors: []
series: null
date: '2025-02-05T17:26:30.659Z'
originalURL: https://freecodecamp.org/news/set-up-docs-as-code-with-docusaurus-and-github-actions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738248926082/9a2a6855-00d4-4e25-a8bd-c1d645f21de5.png
tags:
- name: documentation
  slug: documentation
- name: docs-as-code
  slug: docs-as-code
- name: docusaurus
  slug: docusaurus
- name: GitHub
  slug: github
- name: github-actions
  slug: github-actions-1
seo_title: Comment configurer la documentation en tant que code avec Docusaurus et
  GitHub Actions
seo_desc: For technical writers, keeping documentation up to date manually can be
  really frustrating. Issues like outdated guides, broken links, and missing updates
  are a pain, and they can make writers less productive. These issues can also make
  it harder for...
---

Pour les rédacteurs techniques, maintenir la documentation à jour manuellement peut être vraiment frustrant. Des problèmes comme des guides obsolètes, des liens brisés et des mises à jour manquantes sont une source de frustration et peuvent réduire la productivité des rédacteurs. Ces problèmes peuvent également rendre plus difficile pour les utilisateurs d'utiliser efficacement les docs et d'obtenir des informations correctes.

La documentation en tant que code, ou docs as code, est une approche de gestion de la documentation qui traite les docs comme un codebase. Elle permet de versionner, de mettre à jour automatiquement et de réviser vos docs comme vous le feriez dans un codebase. Docs as code aide à s'assurer que vos docs sont à jour et que les utilisateurs peuvent accéder à des informations précises.

Ce tutoriel vous montrera comment :

* Créer un site web de documentation en utilisant Docusaurus.

* Suivre les changements avec Git et GitHub.

* Construire et déployer sur une plateforme d'hébergement.

* Configurer un workflow pour effectuer des révisions grammaticales en utilisant GitHub Actions avant de fusionner vos changements.

## Prérequis

Ce tutoriel est adapté aux débutants, mais il y a quelques outils dont vous aurez besoin pour suivre :

* [VSCode IDE (ou un autre IDE de votre choix)](https://code.visualstudio.com/download).

* [Node.js et npm installés.](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

* [Un compte GitHub.](https://github.com/)

* [Une connaissance raisonnable de l'utilisation de Git et GitHub.](https://www.freecodecamp.org/news/gitting-things-done-book/)

## Pourquoi les rédacteurs techniques utilisent-ils Docs as Code ?

Avant de plonger dans le vif du sujet, parlons rapidement de ce qu'est "docs as code" et pourquoi c'est important. En 2015, deux rédacteurs techniques chez Google ont eu l'idée de faciliter la contribution des développeurs à la documentation et de mieux organiser leurs documents d'entreprise. Il y avait des moments où ils devaient écrire sur une application sur laquelle ils travaillaient, mais les choses étaient vraiment désorganisées. Ils ont donc mis au point ce processus. Depuis, de nombreuses entreprises ont adopté cette approche.

Docs as code est maintenant une approche populaire de gestion de la documentation, et elle est soutenue par de nombreux outils conçus pour traiter la documentation comme du code. Tom Johnson explique ce concept plus en détail dans [son article sur docs as code](https://idratherbewriting.com/learnapidoc/pubapis_docs_as_code.html).

La documentation traditionnelle repose sur des documents Word et des PDF, où les changements sont suivis manuellement ou via l'historique des révisions du document. Les rédacteurs doivent mettre à jour et publier le contenu manuellement, sans moyen d'automatiser les tâches routinières.

En revanche, docs as code emprunte des principes et des outils au développement logiciel pour rendre la documentation plus structurée, versionnée et automatisée. La documentation est stockée dans un contrôle de version (comme Git), écrite dans des langages de balisage légers, et mise à jour en même temps que le code.

Cette approche garantit que la documentation évolue en même temps que le logiciel, maintient une haute qualité et permet une collaboration efficace, tout comme l'écriture de code.

### Outils que nous utiliserons dans ce tutoriel

Passons en revue les principaux outils que nous utiliserons pour ce tutoriel :

1. Docusaurus est un outil créé par Facebook pour créer des sites web de documentation. Il supporte le markdown et le mdx. Il supporte également le versionnage et les thèmes personnalisés, ce qui le rend facile à utiliser pour créer des docs conviviaux et professionnels.

2. Vale est un vérificateur de style et de grammaire personnalisable pour les rédacteurs. Il garantit une langue, un ton et un style cohérents dans les documents techniques. Il existe d'autres bons linters que vous pourriez utiliser pour la révision, mais c'est ce que nous utiliserons ici.

3. GitHub Actions : Un outil CI/CD pour automatiser les workflows directement dans GitHub. Il aide à tester, construire et déployer le code avec facilité.

## Étape 1 : Installer Docusaurus

Ouvrez votre terminal de ligne de commande et entrez ce qui suit :

```javascript
npx create-docusaurus@latest docs-as-code-tutorial classic
```

`docs-as-code-tutorial` est le nom que j'utilise pour le site. Vous pouvez le remplacer par un autre nom de site si vous le souhaitez. Sélectionnez JavaScript comme langage que vous souhaitez utiliser. Cela commencerà à créer un nouveau site Docusaurus. Après avoir exécuté le code, vous verrez le dossier `docs-as-code-tutorial` dans votre espace de travail VSCode. Naviguez vers le dossier.

Ensuite, démarrez le serveur de développement pour que vous puissiez voir vos docs.

```javascript
cd docs-as-code-tutorial
npm start
```

Avec cela, le site commencera à fonctionner à l'adresse `localhost:3000`.

Lorsque vous consultez le site, vous verrez du contenu pré-généré. Donc, dans l'étape suivante, vous devrez créer un dépôt et lier le dossier local à votre dépôt distant.

![la page d'accueil de docusaurus](https://cdn.hashnode.com/res/hashnode/image/upload/v1737868185569/0cf96b6c-770a-4965-b017-1fe54796c673.png align="center")

## Étape 2 : Créer un dépôt

Maintenant, vous devez créer un dépôt pour `docs-as-code-tutorial`. Allez donc sur votre compte GitHub et créez un nouveau dépôt.

Après avoir créé le dépôt, vous devrez lier le dépôt au dossier dans votre espace de travail VSCode.

Ouvrez un nouveau terminal et exécutez ces commandes :

```javascript
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/myname/docs-as-code-tutorial.git
git push -u origin main
```

Avec cela, vous avez lié le dépôt, et Git commencera à suivre vos changements.

## Étape 3 : Personnaliser vos docs dans le fichier `docusaurus.config`

Avant de commencer à personnaliser, créez une branche où vous pourrez apporter vos modifications avant de les pousser vers la branche principale.

```powershell
git checkout -b "new_branch"
```

Le fichier `docusaurus.config.js` est l'endroit où vous pouvez apporter la plupart des modifications à votre site. Changez la propriété `title` en `Docs as code`.

```javascript
const config = {
  title: 'Docs as code',
  tagline: 'Documentation as code',
//rest of your code
   navbar: {
        title: 'Docs as code',
//rest of your code
  }
}
```

Cela s'affichera comme le nouveau titre lorsque vous prévisualiserez les docs. Ce n'est qu'une illustration pour montrer comment fonctionne Docusaurus. Vous pouvez personnaliser davantage le site selon votre style souhaité, mais nous n'entrerons pas dans plus de détails ici (car le but principal de ce tutoriel est de montrer comment configurer vos docs en tant que code).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737869529640/c4dab104-9f8b-4dad-a3a5-250d15d4552d.png align="center")

Après avoir apporté les modifications, le site devrait avoir un aspect légèrement différent.

Vous pouvez pousser les modifications maintenant.

```powershell
git commit -am "first commit"
git push --set-upstream origin new_branch
```

## Étape 4 : Modifier vos docs

Pour ce tutoriel, j'apporterai des modifications dans la section `docs`. Allez dans `intro.md` et remplacez le texte markdown par ce texte :

```markdown
# Comment configurer docs-as-code

La documentation-as-code est un excellent moyen de pousser les changements apportés dans votre machine locale vers votre site de docs en direct. Pour y parvenir, vous avez besoin d'un IDE, d'un générateur de site statique, d'un dépôt Git, d'un CI/CD pour configurer les workflows et d'une plateforme d'hébergement. 

## Pourquoi les rédacteurs techniques utilisent-ils docs-as-code ?

La documentation-as-code est un excellent moyen de pousser les changements apportés dans votre machine locale vers votre site de docs en direct. Pour y parvenir, vous avez besoin d'un IDE, d'un générateur de site statique, d'un dépôt Git, d'un CI/CD pour configurer les workflows et d'une plateforme d'hébergement. 
```

Après avoir apporté les modifications, prévisualisez vos docs.

![intro.md affichant le texte](https://cdn.hashnode.com/res/hashnode/image/upload/v1737870301247/dba83233-a11c-4ec0-aeaf-b11e525ca090.png align="center")

## Étape 5 : Ajouter la fonctionnalité de linting

Ajoutez le linter Vale à vos docs pour réviser les erreurs. Pour cela, installez le CLI Vale avec l'une de ces commandes.

* Exécutez `choco install vale` pour Windows

* `brew install vale` pour MacOs, ou

* `snap install vale` pour Linux

### **Comment configurer Vale**

Comme je l'ai mentionné précédemment, Vale est un outil de vérification de style et de grammaire personnalisable. Cela signifie que vous pouvez le configurer pour réviser vos docs exactement comme vous le souhaitez.

Vale utilise le guide de style Vale lors de l'exécution des révisions pour repérer les erreurs et faire des suggestions. Mais vous pouvez ajouter le guide de style de votre entreprise ou tout autre guide de style si vous le préférez. Il existe des guides de style publics que vous pouvez utiliser comme le guide de style Google, le guide de style Microsoft, etc. Pour ce tutoriel, nous utiliserons le guide de style Microsoft.

Si vous ne l'avez pas déjà, vous devrez [obtenir le guide de style Microsoft](https://github.com/errata-ai/Microsoft/releases/download/v0.7.0/Microsoft.zip), le télécharger et le décompresser. Créez un dossier styles et déplacez le dossier Microsoft dans le dossier styles.

Cela devrait être votre chemin de fichier :

```javascript
- docs-as-code-tutorial
  //other folders
  - styles
    - Microsoft
  //other folders
```

Dans vos docs, créez un fichier `.vale.ini` et ajoutez-le à votre racine.

Ajoutez ce code dans le fichier :

```plaintext
StylesPath = styles

MinAlertLevel = suggestion

[*.md]

BasedOnStyles = Vale, Microsoft
```

Comprenons ce qui se passe ici :

* Le `StylesPath` est défini sur le dossier styles où vous avez ajouté le guide de style Microsoft que vous avez téléchargé. Le MinAlertLevel définit les alertes Vale sur `suggestion` - cela signifie que Vale mettra en évidence les suggestions, les avertissements et les erreurs trouvés dans vos docs. Si le MinAlertLevel est défini sur les erreurs, alors Vale mettra en évidence uniquement les erreurs. Si défini sur les avertissements, alors il mettra en évidence les avertissements et les erreurs (et ainsi de suite).

* `[*.md]` indique à Vale de parcourir uniquement les fichiers `.md`.

* `BasedOnStyles` indique quel guide de style vous utilisez pour le linting. Dans ce cas, il s'agit du guide de style Microsoft et du guide de style Vale. Donc, lorsque le linter est en cours d'exécution, il mettra en évidence les suggestions, les avertissements et les erreurs en utilisant les guides de style spécifiés.

Pour tester vos docs, exécutez `vale intro.md` (en supposant que vous avez toujours le fichier `intro.md`).

Cela devrait être le résultat :

```plaintext
[1;32m✓[0m 0 errors, 0 warnings and 0 suggestions in stdin.
```

## Étape 6 : Construire le site

Pour cela, exécutez `npm run build`. Après cela, vous pouvez prévisualiser la construction avec `npm run serve`.

## Étape 7 : Déployer le site

Il existe différentes plateformes d'hébergement où vous pouvez héberger votre site en direct. Ce tutoriel couvre deux options d'hébergement : GitHub Pages et Netlify.

### **Déployer avec GitHub Pages**

Pour déployer sur GitHub Pages, vous devrez définir le nom de votre dépôt et le nom d'utilisateur/organisation GitHub dans le fichier `docusaurus.config.js`.

```javascript
// Set the production url of your site here

  url: 'https://ezinneanne.github.io/',

  // Set the /<baseUrl>/ pathname under which your site is served

  // For GitHub pages deployment, it is often '/<projectName>/'

  baseUrl: '/docs-as-code-tutorial/',

  // GitHub pages deployment config.

  // If you aren't using GitHub pages, you don't need these.

  organizationName: 'ezinneanne', // Usually your GitHub org/user name.

  projectName: 'docs-as-code-tutorial', // Usually your repo name.
```

Vous pouvez déployer le site sur GitHub Pages de la manière suivante :

* En utilisant le terminal Powershell avec cette commande :

    `cmd /C 'set "GIT_USER=<GITHUB_USERNAME>" && yarn deploy'`

* En utilisant le terminal de ligne de commande Windows avec cette commande :

    `cmd /C "set "GIT_USER=<GITHUB_USERNAME>" && yarn deploy"`

* En utilisant Bash avec cette commande :  
    `GIT_USER=<GITHUB_USERNAME> yarn deploy`

Assurez-vous simplement de remplacer `<GITHUB_USERNAME>` par votre nom d'utilisateur sur GitHub.

Voilà ! Le site est déployé à l'adresse [https://ezinneanne.github.io/docs-as-code-tutorial/](https://ezinneanne.github.io/docs-as-code-tutorial/).

![la page d'accueil docs-as-code déployée sur GitHub Pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1737918709225/3eb12747-4a13-4c17-a7ad-ab6ee84b64ff.png align="center")

### **Déployer avec Netlify**

Pour déployer sur Netlify, vous n'avez besoin que de l'URL de production et de l'URL de base :

```javascript
// Set the production url of your site here

  url: 'https://docs-as-code-tutorial.netlify.app',

  baseUrl: '/',
```

1. Allez sur votre [compte Netlify](https://www.netlify.com/) et liez votre dépôt.

2. Cliquez sur `Add new site`.

3. Cliquez sur `import an existing project`.

4. Connectez-vous à votre compte GitHub et sélectionnez le dépôt `docs-as-code-tutorial`.

5. Donnez un nom à votre site, il doit être le même que l'URL dans votre `docusaurus.config.js`.

6. Ajoutez le répertoire de publication qui est `build` et la commande de construction qui est `npm run build`. Ensuite, Netlify déployera sur votre branche par défaut `main`, sauf si vous spécifiez autrement.

7. Enfin, déployez !

Vous devriez voir le site fonctionner à l'adresse [https://docs-as-code-tutorial.netlify.app/](https://docs-as-code-tutorial.netlify.app/).

Pour d'autres options de déploiement, [vous pouvez](https://docs-as-code-tutorial.netlify.app/) [consulter la documentation de Docusaurus](https://docusaurus.io/docs/deployment).

## Étape 8 : Configurer un workflow de documentation en utilisant GitHub Actions

Maintenant, nous allons configurer un workflow pour la documentation. Dans GitHub, lorsque vous déployez sur GitHub Pages, il configure un workflow par défaut pour vous à `pages-build-deployments`.

Netlify automatise également les déploiements mais ne crée pas de fichier de workflow dans votre dépôt. Au lieu de cela, il gère le processus via sa plateforme, en surveillant votre dépôt pour les changements et en exécutant des constructions basées sur vos paramètres. Dans ce tutoriel, nous allons configurer un workflow avec GitHub Actions qui automatise l'exécution des vérifications de linting de Vale à travers les docs.

Créez un répertoire `.github/workflows` et ajoutez un fichier `vale-linter.yml` dans celui-ci.

Ajoutez ce code dans le fichier :

```yaml
name: Vale Lint Checker

# Trigger the workflow on specific events.
on:
  push: # Run on every push to the main branch.
    branches:
      - main
  pull_request: # Run on pull requests targeting any branch.
    branches:
      - '*'
  workflow_dispatch: # Allow manual triggering from the Actions tab.

jobs:
  prose:
    runs-on: ubuntu-latest
    steps:
      # Step 1: Check out the repository code.
      - name: Checkout Code
        uses: actions/checkout@v3 

      # Step 2: Set up Node.js
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16 # Use Node.js 16 or higher

      # Step 3: Run Vale lint checks.
      - name: Vale Lint
        uses: errata-ai/vale-action@reviewdog
        with:
          files: .
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Après avoir apporté ces modifications, exécutez les commandes suivantes :

```powershell
git add .
git commit -m "changes"
```

Enfin, poussez vers le dépôt avec `git push`.

Allez dans l'onglet `Actions` de votre dépôt. Vous devriez voir le workflow en cours d'exécution :

![La page du dépôt GitHub avec un focus sur l'onglet Actions montrant le workflow vale](https://cdn.hashnode.com/res/hashnode/image/upload/v1737521586319/3d554246-f8e6-4885-bac5-2cead1b3dd56.png align="center")

Cliquez sur le bouton `changes` et cliquez sur le job `prose`.

![Un bref aperçu de la sortie de linting de Vale dans l'exécution du job prose](https://cdn.hashnode.com/res/hashnode/image/upload/v1737970927236/632e2753-5d2e-474b-a05e-74a9affa634d.png align="center")

Maintenant, vous devriez voir toutes les lignes dans vos fichiers `.md` mises en évidence par Vale.

Avec cela, vos docs sont configurés pour fonctionner comme un codebase ! Vous pouvez apporter des modifications, et lorsque vous poussez, révisez et fusionnez, cela se synchronisera automatiquement.

Gardez à l'esprit que cela est pour Netlify. Pour GitHub Pages, vous devrez configurer un workflow pour le déploiement automatique.

## Résumé

Dans ce tutoriel, vous avez appris comment configurer la documentation en tant que code en utilisant Docusaurus. Vous avez également vu comment déployer votre documentation sur un site en direct, et automatiser le workflow de linting avec Vale et GitHub Actions.

[Il existe d'autres workflows](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow) que vous pouvez configurer pour faciliter la charge de travail dans la gestion de votre site de documentation. N'oubliez pas que le point principal est d'organiser et de structurer vos docs tout en automatisant les pratiques de documentation régulières à l'aide d'outils de développement logiciel. Cela vous permet de vous concentrer sur la chose la plus importante, qui est de créer du contenu de qualité pour vos lecteurs.