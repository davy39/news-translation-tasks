---
title: Outils d'IA que vous pouvez utiliser dans Visual Studio Code en plus de GitHub
  Copilot
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-01-22T19:56:13.000Z'
originalURL: https://freecodecamp.org/news/ai-tools-to-use-in-vs-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/ai-tool-cover-2-1.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Visual Studio Code
  slug: vscode
seo_title: Outils d'IA que vous pouvez utiliser dans Visual Studio Code en plus de
  GitHub Copilot
seo_desc: "AI tools have become quite popular recently. Developers use these tools\
  \ to help generate ideas, create simple code examples, and so on. \nIn 2023, ChatGPT\
  \ and other Large Language Models found their way into many of our toolkits. And\
  \ we can use them t..."
---

Les outils d'IA sont devenus très populaires récemment. Les développeurs utilisent ces outils pour générer des idées, créer des exemples de code simples, et ainsi de suite. 

En 2023, ChatGPT et d'autres grands modèles de langage ont trouvé leur place dans de nombreux outils. Et nous pouvons les utiliser pour être plus productifs et gagner du temps sur les tâches répétitives.

Dans cet article, vous découvrirez d'autres outils utiles en plus de GitHub Copilot.

Avant de discuter des alternatives, passons en revue ce qu'est GitHub Copilot et ce qu'il fait.

## Qu'est-ce que GitHub Copilot ?

GitHub Copilot aide les développeurs à écrire du code plus rapidement et efficacement. C'est un outil développé par GitHub et OpenAI qui utilise une IA puissante et Codex.

[GitHub Copilot fonctionne avec une variété d'éditeurs de code, y compris Visual Studio Code](https://www.freecodecamp.org/news/how-to-use-github-copilot-with-visual-studio-code/), NeoVim, et JetBrains.

GitHub Copilot utilise l'apprentissage automatique. Il ne fait pas de l'autocomplétion – il suggère des extraits de code entiers pendant que vous travaillez dans votre éditeur de texte. Il peut également vous aider à déboguer et à refactoriser l'ancien code. Le but est d'améliorer l'efficacité du codage, de réduire le temps passé sur les tâches répétitives et d'augmenter la productivité.

Mais GitHub Copilot a un inconvénient : après la période d'essai, il coûte 10 $ par mois, ce que certains utilisateurs peuvent considérer comme trop élevé.

Alors maintenant, regardons quelques alternatives qui sont gratuites à utiliser.

## Synk (DeepCode)

Synk, anciennement connu sous le nom de DeepCode, est un outil qui vous aide à garder votre code sécurisé. Il fonctionne directement avec votre fichier de projet ou dépôt, ce qui le rend simple pour les équipes de [trouver et corriger les problèmes de sécurité dans leur code](https://snyk.io/platform/deepcode-ai/), dépendances, conteneurs et infrastructure.

![Page d'accueil de Synk (DeepCode)](https://www.freecodecamp.org/news/content/images/2024/01/image-44.png)
_Page d'accueil de Synk(DeepCode)_

### Cas d'utilisation

* Idéal pour les revues de sécurité en phase initiale.
* Détection et résolution efficaces des bugs.

### Fonctionnalités de Synk

* Analyse votre code tôt dans le développement pour l'aider à passer les revues de sécurité. Cela aide à éviter des corrections coûteuses plus tard dans le cycle de développement.
* Analyse les vulnérabilités et présente les résultats avec les problèmes de sécurité.
* Trouve les bugs possibles dans votre code, vous aidant à attraper et corriger les problèmes tôt.
* Suggère comment faire fonctionner votre code mieux.
* Devient plus intelligent en apprenant de différents exemples de code. Il donne de meilleures suggestions au fil du temps en utilisant des algorithmes.

### Limites de Synk

Bien que Snyk soit un outil puissant, il a quelques limites. Tout d'abord, il examine des bases de code entières, ce qui pourrait demander une puissance de calcul significative, affectant les performances.

Pour aider à atténuer ce problème, vous pouvez diviser les grandes bases de code en modules plus petits et gérables.

De plus, il pourrait y avoir une courbe d'apprentissage pour les développeurs afin de comprendre comment tirer le meilleur parti de l'outil.

Mais votre équipe peut offrir des sessions de formation ou de la documentation pour vous aider, vous et d'autres développeurs, à mieux comprendre comment utiliser Synk efficacement. Encouragez également votre équipe à fournir des ressources de support, telles que des forums ou de la documentation, pour répondre aux problèmes et questions courants.

### Prix

L'utilisation de Synk dans Visual Studio Code pour des tests de sécurité de code individuels est entièrement gratuite. Cela permet de vérifier la sécurité de votre code avant de le déployer en production. 

Pour collaborer au sein d'une équipe ou à des fins professionnelles, une mise à niveau du plan est nécessaire. Vous pouvez trouver plus d'informations sur le plan tarifaire [ici](https://snyk.io/plans/).

### Comment configurer Synk dans Visual Studio Code

Pour configurer Snyk, sélectionnez l'option "Affichage" dans votre texte pour révéler un menu déroulant.

![affichage dans l'éditeur](https://www.freecodecamp.org/news/content/images/2024/01/image-45.png)
_Sélectionnez l'option "Affichage" dans l'éditeur_

Ensuite, cliquez sur l'option "Extensions" dans ce menu déroulant, et cela vous mènera à la place de marché Visual Studio Code.

Dans la place de marché, tapez "Synk Security" et appuyez sur entrée, puis allez-y et installez-le.

![Place de marché](https://www.freecodecamp.org/news/content/images/2024/01/image-46.png)
_Place de marché_

### Comment s'authentifier dans Snyk

Après avoir installé Snyk, vous devrez vous authentifier.

Cliquez sur l'icône Synk dans votre éditeur. Cela vous mènera à la page d'authentification.

Cliquez sur le bouton pour vous authentifier et vous connecter. Une fois authentifié, retournez à votre éditeur. C'est tout !

![Authentification et connexion pour qu'il fonctionne avec votre visual studio code](https://www.freecodecamp.org/news/content/images/2024/01/authenticate-synk.gif)
_Authentification et connexion pour qu'il fonctionne avec votre visual studio code_

Après avoir terminé cette étape, vous pouvez maintenant utiliser Snyk pour examiner, comprendre et analyser votre code avant de l'envoyer en production.

### Exemple de cas d'utilisation

Pour analyser les vulnérabilités possibles dans le fichier de projet, cliquez simplement sur l'icône de synchronisation dans le panneau de gauche. Cela analysera le code et mettra en évidence les problèmes potentiels nécessitant une attention.

![exemple Synk en action](https://www.freecodecamp.org/news/content/images/2024/01/synk-example-in-action.gif)
_Exemple Synk en action_

Si vous regardez de plus près, vous verrez certaines lettres indiquant à quel point les codes écrits sont vulnérables.

* "H" signifie qu'il est vraiment élevé et doit être corrigé dès que possible.
* "M" signifie qu'il est au niveau de vulnérabilité maximum.
* "L" signifie qu'il est à un niveau de vulnérabilité faible.

Si vous cliquez sur une vulnérabilité, vous obtiendrez des suggestions sur la façon de la corriger, qui sont affichées sur le côté droit de l'éditeur.

## Swimm AI

Swimm est un [outil d'assistance au codage](https://swimm.io/) qui vous aide à comprendre des bases de code complexes et volumineuses. 

Swimm, agissant comme un guide intelligent pour les développeurs, simplifie le processus de compréhension du code complexe en fournissant des informations rapides. Il excelle également dans la correction automatique et l'augmentation des lacunes de documentation qui peuvent émerger, résultant en un environnement de développement complet et bien documenté. 

![Page d'accueil de Swimm AI](https://www.freecodecamp.org/news/content/images/2024/01/homepage-of-swimm.gif)
_Page d'accueil de Swimm AI_

### Cas d'utilisation

* Création de documents.
* Organisation du flux de travail.
* Génération automatique d'explications de fragments de code.

### Fonctionnalités de Swimm AI

* Simplifie la création de documents.
* Transforme les demandes de tirage en documents conviviaux pour un partage facile des connaissances.
* Améliore l'organisation du flux de travail avec des règles pour la visibilité des documents.
* Améliore la clarté de la communication grâce à l'amélioration guidée de la documentation, rendant les informations plus compréhensibles et accessibles.
* Analyse votre code sous plusieurs perspectives, créant des documents faciles à comprendre pour des flux de code complexes.
* Base de connaissances continuellement mise à jour, qui se synchronise automatiquement pour aligner votre documentation et les dernières modifications de code.

### Limites de Swimm AI

Comme toujours lors de l'utilisation d'outils d'IA, vous devez toujours vérifier avant de finaliser vos décisions basées sur la sortie de l'IA. 

### Prix

Lorsque Swimm est incorporé dans votre environnement de développement, il est gratuit à utiliser. Mais les grandes entreprises pourraient envisager une [mise à niveau](https://swimm.io/pricing) car les plans améliorés donnent un accès illimité aux utilisateurs. 

### **Comment configurer** Swimm AI **dans Visual Studio Code**

Visitez la place de marché de votre environnement de développement intégré (IDE), tapez "swimm," et appuyez sur Entrée. 

Ensuite, procédez à l'installation depuis la place de marché, ou vous pouvez aller sur leur [site web pour l'intégrer](https://swimm.io/integrations) dans votre IDE.

Cliquez sur l'icône VSCode pour l'initier. Ensuite, vous devrez vous connecter ou vous inscrire – cliquez sur le bouton qui apparaît. 

![Clic sur l'icône pour révéler les boutons de connexion et d'inscription](https://www.freecodecamp.org/news/content/images/2024/01/swimm-sign-in.gif)
_Clic sur l'icône_

Pour vous inscrire, suivez simplement les instructions fournies par le site web.

Puisque vous êtes authentifié, vous pouvez maintenant vous connecter et utiliser l'application.

![Direction de connexion](https://www.freecodecamp.org/news/content/images/2024/01/Login-swimm.gif)
_Direction de connexion_

Lorsque le site web externe s'ouvre, synchronisez votre environnement de développement intégré (IDE). 

![Autorisation avec votre IDE](https://www.freecodecamp.org/news/content/images/2024/01/sync-swmm.gif)
_Autorisation avec votre IDE_

Maintenant, allons-y et voyons comment cela fonctionne avec un exemple pratique.

![Exemple](https://www.freecodecamp.org/news/content/images/2024/01/Code_Jj8izaMNGF.gif)
_Exemple de Swimm AI_

## Cody AI

Cody AI est un [assistant de codage intelligent](https://sourcegraph.com/cody) qui utilise une IA avancée pour comprendre et analyser votre code. Il vous aide à coder plus rapidement et améliore également votre compréhension de la base de code. Il va au-delà des fonctions de base, identifiant des motifs et suggérant des améliorations, rendant votre expérience de codage plus efficace et perspicace.

![Page d'accueil de Cody](https://www.freecodecamp.org/news/content/images/2024/01/image-49.png)
_Page d'accueil de Cody_

### Cas d'utilisation pour Cody AI

* Faciliter la créativité dans les tâches et le brainstorming. 
* Résoudre les problèmes courants avec les outils numériques. 
* Renforcer le travail d'équipe grâce au partage rapide d'informations.

### Fonctionnalités de CodyAI

* Fournit des réponses immédiates aux demandes.
* Vous permet de télécharger divers types de données pour construire une base de connaissances personnalisée.
* Toutes les réponses de Cody ont des citations de sources adéquates.
* Peut aider à la rédaction de courriels, à la traduction de documents et à la génération de matériel marketing.
* Aide les équipes à utiliser les technologies numériques pour diagnostiquer et résoudre les problèmes.
* Sur la base des rencontres précédentes et de l'historique contextuel, il fait des suggestions et des réflexions.

### Limites de Cody AI

Comme pour tout outil, il y a des limites. Tout d'abord, la capacité de recherche de l'IA n'est pas aussi puissante. Elle analyse les requêtes des utilisateurs en utilisant les informations disponibles. En conséquence, l'IA peut donner des réponses qui manquent parfois de la profondeur ou de la spécificité souhaitée.

De plus, les robots Cody AI ne peuvent pas faire de maths ou gérer des tableaux. Cela signifie que l'IA pourrait ne pas donner de réponses précises lorsqu'elle traite des nombres ou des données complexes.

Enfin, les robots Cody AI ne peuvent pas comprendre les images, les diagrammes ou tout ce qui est visuel dans les documents. Ils n'utilisent que du texte pour formuler des réponses, donc ils ne sont pas très bons pour traiter les éléments visuels.

Pour aider à atténuer ces problèmes, assurez-vous d'être aussi clair et spécifique que possible lorsque vous formulez vos requêtes pour aider Cody à mieux comprendre vos intentions.

Vous pouvez également décomposer les questions complexes en composants plus simples pour améliorer les chances de réponses précises.

### Prix

L'installation de Cody dans votre environnement de développement intégré est gratuite pour un usage personnel. Cependant, pour les professionnels ou les entreprises souhaitant exploiter les capacités de Cody, une [mise à niveau est nécessaire](https://meetcody.ai/pricing/).

### Comment configurer Cody dans Visual Studio Code

Tout d'abord, sélectionnez l'option "Affichage" dans votre éditeur de texte pour révéler un menu déroulant comme montré ci-dessus.

Cliquez sur "Extensions", et cela vous mènera à la place de marché Visual Studio Code.

Dans la place de marché, tapez "Cody" et appuyez sur entrée, puis allez-y et installez-le.

![Installation de Cody AI](https://www.freecodecamp.org/news/content/images/2024/01/image-50.png)
_Plugin Cody_

Maintenant que l'installation est terminée, vous pouvez commencer à utiliser Cody dans votre éditeur. 

Cody fournit différentes invites de commande pour vous aider avec votre code:

* Il peut vous aider à générer de la documentation pour votre code
* Si vous contribuez à un projet open-source et trouvez la base de code confuse, Cody AI peut fournir des explications.
* Il peut vous dire dans quel langage de programmation un morceau de code est écrit.
* Vous pouvez poser des questions à Cody sans quitter votre environnement de codage.
* Cody peut apporter des modifications à votre code en fonction des instructions données.

Maintenant, je vais illustrer comment Cody peut aider à expliquer des parties de votre code avec un exemple:

![Une invite de commande de Cody AI](https://www.freecodecamp.org/news/content/images/2024/01/explain-cody-example.gif)
_Une invite de commande de Cody AI_

## Tabnine

Tabnine est un puissant assistant d'IA conçu pour les développeurs, fournissant des [complétions et suggestions de code basées sur l'IA](https://www.tabnine.com/) pour augmenter la productivité. 

Il est compatible avec une large gamme de langages de programmation et d'environnements de développement intégrés (IDE) majeurs, permettant aux développeurs de tirer parti de ses recommandations de code intelligentes de manière efficace.

![Page d'accueil de TabNine](https://www.freecodecamp.org/news/content/images/2024/01/image-52.png)
_Page d'accueil de Tabnine_

### Cas d'utilisation

* Accélérer le développement logiciel : Facilite l'écriture de code plus rapide et plus efficace.
* Assurer la cohérence du code : Maintient un style de codage cohérent parmi les différents membres de l'équipe.

### Fonctionnalités de Tabnine

* Apprend du code que vous tapez et ajuste ses suggestions pour correspondre à votre style de codage.
* Se soucie de votre vie privée. Il n'apprend que du code open-source et permissif, donc vous êtes toujours propriétaire de votre code.
* Génial pour les développeurs car il fonctionne avec de nombreux langages de programmation. C'est comme un outil pratique pour différentes choses technologiques !
* Rend le codage plus facile en donnant des suggestions intelligentes, aidant les développeurs à gagner du temps.
* Il fonctionne bien avec les éditeurs de code populaires comme Visual Studio code. Les développeurs peuvent l'utiliser dans leurs environnements de codage.

### Limites de Tabnine

Tabnine apprend de la façon dont vous codez au fil du temps, donc il pourrait prendre un peu de temps pour correspondre à votre style de codage. Il aide si vous utilisez activement l'outil et fournissez une entrée cohérente pour l'aider à apprendre votre style de codage plus rapidement.

Tabnine suggère également du code, mais il ne crée pas de sections entières. Bien que cela puisse sembler une limitation, c'est en fait ce qu'il y a de mieux pour la qualité du code. 

Enfin, il pourrait suggérer du code qui n'est pas tout à fait correct. Les développeurs devraient vérifier les suggestions pour leur exactitude. Pour aider Tabnine à suggérer un meilleur code, vous pouvez régulièrement passer en revue et accepter/rejeter les suggestions pour affiner sa compréhension de vos préférences.

Vous devriez également toujours vérifier le code suggéré pour son exactitude et son adhérence aux normes de codage avant de le finaliser.

### Prix

L'installation ne coûte rien par mois, ce qui la rend gratuite. Cependant, pour les grandes organisations, il est recommandé d'envisager une mise à niveau. Les plans mis à niveau pour les grandes organisations fournissent un accès utilisateur illimité tout en priorisant la sécurité et la vie privée.

### Comment configurer Tabnine dans Visual Studio Code

Pour commencer, sélectionnez l'option "Affichage" dans votre éditeur de texte pour révéler un menu déroulant comme montré ci-dessus.

Cliquez sur "Extensions" et cela vous mènera à la place de marché Visual Studio Code.

Dans la place de marché, tapez "Tabnine" et appuyez sur entrée, puis allez-y et installez-le.

![Extension (place de marché dans l'IDE)](https://www.freecodecamp.org/news/content/images/2024/01/use-tabnine-cover.png)
_Extension (place de marché dans l'IDE)_

Maintenant que nous l'avons installé, vous pouvez commencer à utiliser Tabnine dans votre éditeur. Voici un exemple:

![Exemple dans l'éditeur](https://www.freecodecamp.org/news/content/images/2024/01/use-tabnine-example.gif)
_Exemple dans l'éditeur_

Et voici le code:

```js
const add = (a, b) => {

  return a + b;

}

console.log(add(5,9))// sortie 14


```

## Code Whisperer

CodeWhisperer est un assistant intelligent pour le codage. Il utilise l'IA pour suggérer des morceaux de code ou des fonctions entières pendant que vous travaillez dans votre environnement de codage. Créé par [AWS](https://aws.amazon.com/codewhisperer/), il facilite le codage avec des fonctionnalités comme l'autocomplétion et la restructuration de code.

![Page d'accueil de Code Whisperer](https://www.freecodecamp.org/news/content/images/2024/01/image-56.png)
_Page d'accueil de Code Whisperer_

### Fonctionnalités de Code Whisperer

* Code Whisperer suggère du code en temps réel pendant que vous écrivez.
* S'intègre à votre environnement de développement intégré (IDE).
* Aide à améliorer la lisibilité et l'efficacité du code en aidant à améliorer et restructurer.
* Prend en charge une grande variété de langages de programmation.
* Offre une aide précieuse dans la génération et la compréhension de la documentation du code.

### Limites de Code Whisperer

CodeWhisperer pourrait avoir du mal à gérer de nouvelles tâches de codage nécessitant de la créativité.

De plus, des erreurs dans ses données/modèles de formation peuvent conduire à des suggestions de code inexactes.

Avec cela à l'esprit, vous devriez principalement utiliser CodeWhisperer comme un outil pour générer du code routinier ou répétitif, laissant les tâches plus complexes et créatives à l'expertise humaine.

Assurez-vous également de réviser et vérifier souvent les suggestions de CodeWhisperer et ne prenez pas les informations pour argent comptant.

### Comment configurer Code Whisperer dans Visual Studio Code

Tout d'abord, sélectionnez l'option "Affichage" dans votre éditeur de texte pour révéler un menu déroulant.

Cliquez sur "Extensions" et cela vous mènera à la place de marché Visual Studio Code.

Dans la place de marché, tapez "AWS Toolkit" et appuyez sur entrée, puis allez-y et installez-le.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-58.png)
_Extension(place de marché dans l'IDE)_

Maintenant que l'extension est installée, utilisons-la dans notre environnement de développement intégré (IDE).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/example-code-whisper.gif)

Voici le code:

```js
// créer une fonction de salutation
function greet(name) {
    return "Hello " + name;
}
// exporter la fonction de salutation
module.exports = greet;
```

## CodeGeex AI

CodeGeeX est un [outil utile pour le codage](https://codegeex.cn/en-US) qui crée des commentaires, suggère du code et fournit une aide par chat alimentée par l'IA. Il peut également traduire votre code dans différentes langues et fonctionne bien avec de nombreux langages de programmation et outils. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/chrome_4C9oZTEpBe.png)
_Page d'accueil de CodeGeex_

### Cas d'utilisation

* Rendre le codage plus rapide.
* Guide les nouveaux développeurs à travers de grands codes avec des commentaires et des explications automatiques.

### Fonctionnalités de CodeGeex AI

* Excellent pour terminer le code. Il aide en complétant automatiquement et en générant des lignes basées sur le code ou les commentaires existants.
* Crée des commentaires pour les méthodes et les lignes dans le code, gagnant du temps et rendant facile la compréhension du code inconnu.
* Aide à changer le code d'un langage de programmation à un autre – comme transformer Python en Java.
* Les développeurs peuvent poser des questions de codage à CodeGeeX et obtenir des réponses rapides sans rechercher sur le web.
* CodeGeeX fait plus que suggérer du code. Il peut interpréter le code sélectionné, corriger les bugs, résumer le code, et plus encore.

### Limites de CodeGeeX AI

Lorsque vous utilisez CodeGeeX, gardez à l'esprit qu'il s'agit d'un prototype de recherche, donc il pourrait ne pas toujours créer un code parfait pour chaque situation.

Il pourrait également mal comprendre certaines descriptions de langage ou extraits de code, conduisant à des erreurs possibles.

Comme toujours, assurez-vous de vérifier soigneusement le code généré pour son exactitude et son adhérence aux normes de codage.

De plus, lorsque vous fournissez des descriptions de langage ou des extraits de code, soyez aussi clair et détaillé que possible.

### Prix

CodeGeex est gratuit à installer sur Visual Studio Code, et pour une mise à niveau, cela commence à 9 $/mois.

### Comment configurer CodeGeeX AI dans Visual Studio Code

Sélectionnez l'option "Affichage" dans votre éditeur de texte pour révéler un menu déroulant.

Cliquez sur "Extensions" dans votre éditeur de texte, et cela vous mènera à la place de marché Visual Studio Code.

Dans la place de marché, tapez "CodeGeex" et appuyez sur entrée, puis procédez à son installation.

![Installer CodeGeex](https://www.freecodecamp.org/news/content/images/2024/01/image-61.png)
_Installer CodeGeex_

Après l'installation, cliquez sur l'icône, et cela vous ramènera à une page où vous pouvez vous connecter ou vous inscrire.

![Page de connexion dans CodeGeex](https://www.freecodecamp.org/news/content/images/2024/01/image-62.png)
_Page de connexion dans CodeGeex_

Une fois que vous avez terminé cette étape, vous pourrez interagir avec l'IA dans votre IDE.

Pour la déclencher, naviguez vers votre IDE, surlignez le code souhaité et faites un clic droit. Un menu déroulant apparaîtra, vous permettant de choisir la commande spécifique que vous voulez que l'IA exécute pour vous.

Voici un exemple:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/use-codegeex.gif)
_Exemple d'utilisation de CodeGeex_

Le GIF exemple a montré une chose que CodeGeex AI peut faire. 

Pour en savoir plus sur ses capacités, visitez les docs : [CodeGeeX: AI Code AutoComplete, Chat, Auto Comment](https://marketplace.visualstudio.com/items?itemName=aminer.codegeex).

Code:

```javascript
const colors = ['pink', 'blue', 'purple', 'green'];

colors.forEach(color => {
    console.log(color);
});

```

## Codeium

Codeium est un [outil gratuit et puissant](https://codeium.com/) qui rend le codage plus rapide en utilisant une IA avancée. C'est comme un super-héros pour le codage, avec un outil qui vous aide à compléter le code dans plus de 70 langages. Il est super rapide et donne des suggestions de premier ordre, rendant le codage beaucoup plus efficace. Vous pouvez utiliser Codeium comme une [extension Google Chrome](https://chromewebstore.google.com/detail/codeium-ai-code-autocompl/hobjkcpmjhlegmobgonaagepfckjkceh).

![Page d'accueil de Codeium](https://www.freecodecamp.org/news/content/images/2024/01/image-64.png)
_Page d'accueil de Codeium_

Gardez simplement à l'esprit que, en raison de sa puissance, l'utilisation de Codeium rend facile le fait de trop compter sur les suggestions générées par l'IA. Cela pourrait conduire à des erreurs dans votre code si vous n'êtes pas vigilant et ne maintenez pas vos compétences. Assurez-vous donc de toujours vérifier/exécuter votre code, d'apprendre de nouveaux sujets au besoin et de garder vos propres capacités d'écriture de code aiguisées. 

Vous pouvez [lire plus sur Codeium ici](https://ai-review.com/code-assistant/codeium/).

### Prix

L'IA est initialement gratuite à installer dans votre environnement de développement intégré (IDE) mais peut nécessiter une mise à niveau qui commence à [12 $/mois avec utilisation en équipe](https://codeium.com/pricing).

### Comment configurer Codeium dans Visual Studio Code

Pour commencer, visitez le [site web](https://codeium.com/) de Codeium et sélectionnez l'option de connexion.

![Connexion de l'utilisateur](https://www.freecodecamp.org/news/content/images/2024/01/image-66.png)
_Connexion de l'utilisateur_

En cliquant sur cela, vous serez redirigé vers la page de connexion.

![Page de connexion](https://www.freecodecamp.org/news/content/images/2024/01/image-67.png)
_Page de connexion_

Connectez-vous en utilisant soit votre email soit votre compte Google.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-68.png)
_Authentification_

Une fois que vous avez terminé la connexion, vous rencontrerez divers environnements de développement intégrés (IDE). Choisissez celui qui correspond à vos préférences – par exemple, j'utilise Visual Studio Code.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/choose-ide-codeium.gif)
_Choix de votre IDE_

Allez-y et installez-le dans votre IDE Visual Studio Code.

Après l'installation, cliquez sur l'option de connexion du compte dans Visual Studio Code pour vous authentifier avec le site web.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/use-codeium-authentication-1.gif)
_Authentification_

Une fois terminé, vous pouvez maintenant utiliser Codeium dans votre IDE.

Maintenant, voyons un exemple pratique:

![Exemple](https://www.freecodecamp.org/news/content/images/2024/01/result-from-codium.gif)
_Exemple de Codeium_

## Conclusion

L'article discute de divers outils d'IA que vous pouvez utiliser pour accélérer le développement. Certains développeurs ne pensent qu'à GitHub Copilot. Mais il existe d'autres outils d'IA avec différentes fonctionnalités qui peuvent également vous aider.

Si vous avez trouvé de la valeur dans ce tutoriel, envisagez de le partager avec d'autres développeurs qui pourraient également en bénéficier. 

Pour rester à jour avec mes derniers projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples) et [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) ou en consultant mon [BioDrop](https://www.biodrop.io/ijayhub). 

Si vous souhaitez montrer votre soutien, vous pouvez également [m'offrir un café](https://www.buymeacoffee.com/ijewriter)❤

Merci d'avoir pris le temps de lire💖