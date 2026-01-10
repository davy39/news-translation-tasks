---
title: 'Comment commencer votre parcours Open Source : Un guide pour débutants pour
  contribuer'
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-10-03T15:01:31.501Z'
originalURL: https://freecodecamp.org/news/how-to-start-your-open-source-journey-beginners-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727909892455/221e81fb-d41d-463a-a1fa-d5ef2d316eaf.png
tags:
- name: Open Source
  slug: opensource
- name: GitHub
  slug: github
- name: Git
  slug: git
- name: open source
  slug: open-source
- name: opensource
  slug: opensource-inactive
seo_title: 'Comment commencer votre parcours Open Source : Un guide pour débutants
  pour contribuer'
seo_desc: 'Open source software has become the backbone of modern technology, powering
  everything from small startups to giant corporations.

  Contributing to open source projects is not just a way to give back to the community
  – it''s also an excellent opportunit...'
---

Les logiciels open source sont devenus la colonne vertébrale de la technologie moderne, alimentant tout, des petites startups aux grandes entreprises.

Contribuer à des projets open source n'est pas seulement un moyen de rendre à la communauté – c'est aussi une excellente opportunité d'améliorer vos compétences, de construire votre portfolio et de vous connecter avec des développeurs partageant les mêmes idées du monde entier.

Mais pour de nombreux débutants, la perspective de contribuer à l'open source peut être intimidante. Les barrières courantes incluent ne pas savoir par où commencer, la peur de faire des erreurs ou se sentir intimidé par des bases de code complexes.

Ce guide vise à briser ces barrières et à vous fournir un chemin clair pour faire votre première contribution open source.

### Ce que nous allons couvrir :

1. [Comprendre l'Open Source](#heading-comprendre-open-source)

2. [Comment se préparer pour votre première contribution](#heading-comment-se-preparer-pour-votre-premiere-contribution)

3. [Comment trouver le bon projet Open Source](#heading-comment-trouver-le-bon-projet-open-source)

4. [Comprendre les directives du projet](#heading-comprendre-les-directives-du-projet)

5. [Comment faire votre première contribution](#heading-comment-faire-votre-premiere-contribution)

6. [Bonnes pratiques pour la contribution Open Source](#heading-bonnes-pratiques-pour-la-contribution-open-source)

7. [Outils pratiques pour commencer](#heading-outils-pratiques-pour-commencer)

8. [Poursuivre votre parcours Open Source](#heading-poursuivre-votre-parcours-open-source)

9. [Conclusion](#heading-conclusion)

## Comprendre l'Open Source

### Qu'est-ce que l'open source ?

L'open source fait référence à des logiciels dont le code source est librement disponible pour que chacun puisse le consulter, le modifier et le distribuer. Cette approche collaborative du développement de logiciels a conduit à la création de nombreux outils et plateformes puissants que nous utilisons quotidiennement, tels que Linux, WordPress et TensorFlow.

### Avantages de la contribution à des projets open source

Contribuer à des projets open source offre de nombreux avantages pour les développeurs. C'est un excellent moyen d'améliorer vos compétences, en vous exposant à divers styles de codage et aux meilleures pratiques. Vos contributions peuvent également vous aider à construire un portfolio solide, fournissant une preuve tangible de vos capacités aux employeurs potentiels.

La communauté open source offre des opportunités de réseautage précieuses, vous connectant avec des développeurs du monde entier et pouvant conduire à des opportunités d'emploi ou à des mentorats. En contribuant, vous rendez également à la communauté, aidant à améliorer les outils sur lesquels vous et d'autres comptent quotidiennement.

Enfin, vous gagnez des informations sur la gestion de projet, apprenant comment les projets logiciels à grande échelle sont coordonnés et maintenus. Ces avantages améliorent collectivement vos compétences techniques, vos perspectives de carrière et votre compréhension de l'écosystème de développement logiciel.

## Comment se préparer pour votre première contribution

### Configurer votre environnement de développement

1. Choisissez un éditeur de code ou un IDE (Environnement de Développement Intégré) avec lequel vous êtes à l'aise. Les options populaires incluent Visual Studio Code, Sublime Text ou les IDE de JetBrains.

2. Installez Git sur votre ordinateur. Git est le système de contrôle de version le plus largement utilisé dans les projets open source.

### Apprendre les bases du contrôle de version (Git) :

Comprendre Git est crucial pour contribuer à l'open source. Voici quelques concepts clés pour commencer :

* Dépôt : Un dossier de projet contenant tous les fichiers et l'historique des versions.

* Clone : Créer une copie locale d'un dépôt sur votre machine.

* Branche : Une ligne de développement séparée pour de nouvelles fonctionnalités ou des corrections de bugs.

* Commit : Enregistrer les modifications dans votre dépôt local.

* Push : Télécharger vos modifications locales vers le dépôt distant.

* Pull Request : Proposer vos modifications pour qu'elles soient fusionnées dans le projet principal.

Prenez le temps de pratiquer ces concepts sur un projet personnel avant de vous lancer dans des contributions open source.

## Comment trouver le bon projet Open Source

### Identifier vos compétences et intérêts :

Commencez par lister vos compétences (langages de programmation, frameworks, design, documentation) et domaines d'intérêt. Cela vous aidera à trouver des projets qui correspondent à vos capacités et passions.

### Explorer les ressources pour trouver des projets :

Bien que nous présenterons quelques outils spécifiques plus tard dans ce guide, voici quelques plateformes générales que vous pouvez explorer pour trouver des projets open source :

1. La section "Explore" de GitHub

2. CodeTriage

3. Up For Grabs

4. First Timers Only

5. Le dépôt de votre logiciel préféré (recherchez les étiquettes "good first issue")

Rappelez-vous, la clé est de trouver un projet qui vous intéresse vraiment, car cela vous motivera tout au long du processus de contribution.

## Comprendre les directives du projet

Avant de commencer à contribuer à un projet open source, il est crucial de comprendre les directives du projet. Ces directives se trouvent généralement dans des fichiers comme [CONTRIBUTING.md](http://CONTRIBUTING.md), CODE\_OF\_[CONDUCT.md](http://CONDUCT.md), ou dans le fichier README du projet.

### Lire les directives de contribution

Le fichier [CONTRIBUTING.md](http://CONTRIBUTING.md) est votre feuille de route pour devenir un contributeur précieux. Il contient généralement des informations sur :

* Comment configurer le projet localement

* Le processus de soumission des contributions

* Les normes de codage et les guides de style

* Comment signaler des bugs ou suggérer de nouvelles fonctionnalités

* Les canaux de communication pour le projet

Par exemple, la bibliothèque open source populaire React a un fichier [CONTRIBUTING.md](https://github.com/facebook/react/blob/main/CONTRIBUTING.md) complet. Il inclut des sections sur :

* Code de conduite

* Flux de travail de développement

* Bugs

* Proposer un changement

* Envoyer une Pull Request

### Familiarisez-vous avec la structure du projet et les normes de codage

Prenez le temps de comprendre l'architecture du projet et l'organisation des fichiers. Cela peut impliquer :

1. Explorer la structure des répertoires

2. Lire la documentation sur l'architecture du projet

3. Examiner le code existant pour comprendre le style de codage

De nombreux projets utilisent des outils automatisés pour faire respecter les normes de codage. Par exemple, un projet JavaScript peut utiliser ESLint pour le linting du code. Vous pourriez voir un fichier de configuration comme .eslintrc.js à la racine du projet :

```javascript
module.exports = {
  "extends": "airbnb",
  "rules": {
    "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
    "no-console": "off"
  }
};
```

Cette configuration vous indique que le projet suit le guide de style JavaScript d'Airbnb avec quelques modifications personnalisées.

## Comment faire votre première contribution

Passons en revue le processus de réalisation de votre première contribution, en utilisant un exemple concret.

### Choisir un problème

Supposons que vous avez trouvé un problème dans le dépôt d'un éditeur markdown populaire. Le problème est étiqueté "good first issue" et décrit un bug où l'aperçu ne se met pas à jour lorsque l'utilisateur tape un backtick (`).

### Communiquer avec les mainteneurs du projet

Avant de commencer le travail, vous commentez le problème :

```plaintext
Bonjour ! Je suis nouveau dans l'open source et j'aimerais travailler sur ce problème. 
Est-il toujours disponible ? Je pense l'aborder en modifiant 
le listener d'événements pour le composant de l'éditeur. Cela semble être une bonne approche ?
```

Un mainteneur répond, vous accueillant et confirmant votre approche.

### Créer un fork et travailler sur votre solution

1. Forker le dépôt vers votre compte GitHub.

2. Cloner votre fork localement :

```plaintext
git clone https://github.com/votreutilisateur/markdown-editor.git
```

3. Créer une nouvelle branche :

```plaintext
git checkout -b fix-backtick-preview
```

4. Faire vos modifications. Par exemple, vous pourriez modifier le composant de l'éditeur :

```javascript
class Editor extends React.Component {
  handleChange = (event) => {
    const { value } = event.target;
    this.props.onChange(value);
    
    // Forcer la mise à jour de l'aperçu sur le backtick
    if (value.endsWith('`')) {
      this.props.forceUpdatePreview();
    }
  }

  render() {
    // ... reste du composant
  }
}
```

5. Commiter vos modifications :

```plaintext
git add .
git commit -m "Fix: Mettre à jour l'aperçu sur l'entrée de backtick"
```

6. Pousser vers votre fork :

```plaintext
git push origin fix-backtick-preview
```

### Soumettre une Pull Request

1. Allez dans le dépôt original sur GitHub.

2. Cliquez sur "New pull request" et sélectionnez votre branche.

3. Remplissez le modèle de pull request :

```markdown
## Description
Cette PR corrige le problème où l'aperçu ne se met pas à jour lorsqu'un backtick est tapé.

## Modifications
- Modifié le composant Editor pour forcer une mise à jour lorsqu'un backtick est entré

## Tests
1. Ouvrir l'éditeur
2. Taper du texte suivi d'un backtick
3. Vérifier que l'aperçu se met à jour immédiatement

Corrige #123
```

4. Soumettez la pull request et attendez les retours.

## Bonnes pratiques pour la contribution Open Source

### Écrire des messages de commit clairs

De bons messages de commit sont cruciaux pour la maintenabilité du projet. Suivez ces directives :

* Utilisez l'impératif dans la ligne de sujet

* Limitez la ligne de sujet à 50 caractères

* Capitalisez la ligne de sujet

* Ne terminez pas la ligne de sujet par un point

* Séparez le sujet du corps par une ligne vide

* Limitez le corps à 72 caractères

* Utilisez le corps pour expliquer quoi et pourquoi vs. comment

Exemple d'un bon message de commit :

```plaintext
Corriger la condition de course dans le pool de connexions

- Ajouter un verrou mutex lors de l'accès à la ressource partagée
- Implémenter un mécanisme de réessai pour les connexions échouées

Ce changement empêche plusieurs threads d'accéder au pool de connexions
simultanément, ce qui causait des plantages occasionnels dans des
scénarios de charge élevée. Le mécanisme de réessai améliore la résilience
aux problèmes réseau temporaires.
```

### Documenter vos modifications

Une documentation claire est aussi importante qu'un bon code. Voici quelques bonnes pratiques :

1. Mettre à jour les fichiers README pertinents

2. Ajouter des commentaires en ligne pour la logique complexe

3. Mettre à jour ou créer de la documentation API pour les nouvelles fonctionnalités

Par exemple, si vous avez ajouté une nouvelle fonction à une bibliothèque Python :

```python
def validate_email(email: str) -> bool:
    """
    Valider une adresse email.

    Args:
        email (str): L'adresse email à valider.

    Returns:
        bool: True si l'email est valide, False sinon.

    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    # Détails de l'implémentation...
```

### Répondre aux retours

Lorsque vous recevez des retours sur votre pull request :

1. Répondez rapidement et poliment

2. Traitez tous les commentaires, même si c'est juste pour les reconnaître

3. Si vous n'êtes pas d'accord avec une suggestion, expliquez votre raisonnement avec respect

4. Faites les modifications demandées et mettez à jour votre pull request

Par exemple :

Relecteur : "Pourriez-vous ajouter un test unitaire pour la nouvelle fonction validate\_email ?"

Vous : "Absolument, c'est une excellente suggestion. J'ajouterai une suite de tests complète pour divers formats d'email et cas limites. Je pousserai les modifications sous peu."

## Outils pratiques pour commencer

### Git Begin : Votre porte d'entrée vers les contributions Open Source

Pour vous aider à faire vos premiers pas dans l'open source, j'ai développé Git Begin, une application web gratuite conçue pour rendre la recherche de votre première opportunité de contribution aussi facile que possible.

#### Comment fonctionne Git Begin :

1. Visitez [Git Begin](https://gitbegin.theenthusiast.dev)

2. Sélectionnez votre langage de programmation ou framework préféré parmi les options proposées.

3. Parcourez une liste soigneusement sélectionnée de problèmes étiquetés comme "good first issue" ou "beginner-friendly" à travers divers projets open source.

4. Chaque problème est présenté avec des informations clés telles que le nom du projet, la description du problème et les compétences requises.

5. Lorsque vous trouvez un problème qui vous intéresse, cliquez dessus pour être redirigé vers le problème original sur GitHub.

Git Begin élimine le processus accablant de recherche à travers d'innombrables dépôts. Il vous présente des opportunités ciblées et adaptées aux débutants qui correspondent à vos compétences et intérêts, rendant plus facile que jamais le début de votre parcours open source.

### Un projet réel pour les premiers contributeurs

En plus de Git Begin, je suis ravi de vous présenter un autre projet gratuit et open-source conçu spécifiquement pour les débutants afin de pratiquer leurs compétences et de faire des contributions significatives :

* Projet : Job Scraper

* Description : Un outil pour extraire des offres d'emploi de plusieurs pages de carrière d'entreprises

* Dépôt : [https://github.com/The-Enthusiast-404/career-craft-scrapper](https://github.com/The-Enthusiast-404/career-craft-scrapper)

#### À propos du projet :

Ce projet Job Scraper est un composant crucial d'une plateforme plus large et ambitieuse que j'aide à développer et qui révolutionnera le processus de recherche d'emploi. Cette plateforme gratuite vise à être une ressource complète pour les chercheurs d'emploi, offrant une gamme d'outils pour rationaliser leur recherche d'emploi et leur processus de candidature.

Le Job Scraper lui-même agrège les offres d'emploi de diverses pages de carrière d'entreprises, formant la base de notre plateforme. Mais ce n'est qu'un début. Notre vision s'étend à la création d'un écosystème complet qui inclura :

1. Un système centralisé de candidature à des emplois, permettant aux utilisateurs de postuler à plusieurs postes dans différentes entreprises de manière transparente.

2. Des outils de création de CV alimentés par l'IA pour aider les chercheurs d'emploi à rédiger des CV convaincants adaptés à leurs rôles cibles.

3. Un simulateur d'entretien innovant alimenté par l'IA, capable de simuler des entretiens pour des rôles et des piles technologiques spécifiques, aidant les candidats à se préparer plus efficacement.

En contribuant au projet Job Scraper, vous ne gagnez pas seulement une expérience précieuse en web scraping et en traitement de données, mais vous participez également à la construction d'une plateforme qui fera une réelle différence dans les carrières des gens.

C'est une opportunité de travailler sur un projet avec des applications pratiques immédiates tout en contribuant à une vision plus large de rendre la recherche d'emploi plus accessible et efficace pour tous.

En tant que contributeur open source, vous aurez l'occasion de travailler sur divers aspects de ce système, de l'amélioration des algorithmes de scraping à l'aide potentielle au développement de certaines des fonctionnalités alimentées par l'IA à l'avenir.

Ce projet offre un mélange unique d'expérience de codage pratique et de la satisfaction de travailler sur un outil qui aura un impact direct sur les chercheurs d'emploi du monde entier.

#### Opportunités de contribution actuelles :

Il existe un certain nombre de "good first issues" disponibles, tous axés sur des tâches de web scraping. Ceux-ci peuvent inclure :

* Ajouter la prise en charge de l'extraction d'offres d'emploi depuis une nouvelle page de carrière d'entreprise

* Améliorer le processus de nettoyage des données pour un site d'emploi spécifique

* Renforcer la résilience du scraper contre les changements dans la structure d'un site web

Chaque problème est soigneusement documenté pour aider les nouveaux venus à comprendre la tâche et son contexte dans le cadre du projet plus large.

#### Premières étapes dans l'Open Source

Le projet Job Scraper est devenu un point d'entrée accueillant pour de nombreux développeurs faisant leurs premières contributions open source. À ce jour, nous avons eu plusieurs contributeurs qui ont choisi le dépôt pour leur première pull request, la plupart d'entre eux étant des étudiants désireux de gagner une expérience réelle.

Ces nouveaux venus dans l'open source ont ajouté avec succès de nouvelles fonctionnalités de scraping, amélioré les algorithmes existants et amélioré nos capacités de traitement de données.

Leurs réalisations démontrent que notre dépôt est un point de départ idéal pour toute personne souhaitant commencer son parcours open source, en particulier les étudiants souhaitant appliquer leurs compétences à un projet pratique.

#### Comment s'impliquer :

1. Visitez le dépôt : [https://github.com/The-Enthusiast-404/career-craft-scrapper](https://github.com/The-Enthusiast-404/career-craft-scrapper)

2. Lisez le README et les fichiers [CONTRIBUTING.md](http://CONTRIBUTING.md) pour comprendre le projet et les directives de contribution

3. Parcourez les problèmes ouverts étiquetés "good first issue"

4. Commentez un problème sur lequel vous aimeriez travailler, et je vous guiderai à travers les prochaines étapes

Rappelez-vous, Git Begin et le projet Job Scraper sont des ressources entièrement gratuites. Nous nous engageons à fournir un environnement de soutien pour que les développeurs apprennent et grandissent dans leur parcours open source.

## Poursuivre votre parcours Open Source

### Construire sur votre première contribution :

Après avoir fait votre première contribution, prenez le temps de réfléchir à ce que vous avez appris. Considérez :

* Quels aspects du processus avez-vous trouvé difficiles ?

* Quelles nouvelles compétences ou connaissances avez-vous acquises ?

* Comment pouvez-vous appliquer cette expérience à de futures contributions ?

Utilisez ces informations pour guider vos prochaines étapes dans l'open source.

### Devenir un contributeur régulier :

Pour devenir un contributeur régulier :

1. Configurez les notifications du projet pour rester informé des nouveaux problèmes et discussions.

2. Participez aux discussions du projet, offrez des informations ou posez des questions.

3. Prenez en charge des problèmes de plus en plus complexes à mesure que vous vous familiarisez avec le projet.

4. Aidez les nouveaux venus en répondant à leurs questions ou en examinant leurs pull requests.

5. Envisagez de contribuer à la documentation ou d'écrire des tests, qui sont souvent négligés mais sont des aspects cruciaux des projets open source.

### Explorer de nouveaux projets :

À mesure que vous gagnez en confiance, n'hésitez pas à explorer de nouveaux projets :

1. Recherchez des projets dans différents domaines pour élargir vos compétences.

2. Envisagez de contribuer à des outils ou bibliothèques que vous utilisez dans votre travail quotidien.

3. Explorez des projets de différentes tailles - des petites utilités aux grands frameworks.

Rappelez-vous, chaque projet offre des opportunités d'apprentissage et des défis uniques.

## Conclusion

Contribuer à l'open source peut être une expérience incroyablement enrichissante. Cela vous permet d'améliorer vos compétences en codage, de collaborer avec des développeurs du monde entier et de faire un impact significatif sur des projets utilisés par des millions de personnes.

Rappelez-vous, tout le monde commence quelque part. N'ayez pas peur de faire des erreurs – elles font partie du processus d'apprentissage. La communauté open source est généralement accueillante et soutenante envers les nouveaux venus.

Nous espérons que ce guide, ainsi que des outils comme Git Begin et notre projet Job Scraper, vous aideront à faire vos premiers pas dans le monde de la contribution open source. Bon codage, et nous avons hâte de voir vos contributions !

#### Ressources :

* Git Begin : [https://gitbegin.theenthusiast.dev](https://gitbegin.theenthusiast.dev)

* Projet Job Scraper : [https://github.com/The-Enthusiast-404/career-craft-scrapper](https://github.com/The-Enthusiast-404/career-craft-scrapper)

* Documentation Git : [https://git-scm.com/doc](https://git-scm.com/doc)

* Guides GitHub : [https://guides.github.com/](https://guides.github.com/)

* Guide Open Source : [https://opensource.guide/](https://opensource.guide/)