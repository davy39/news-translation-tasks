---
title: Comment fusionner des fichiers Word en utilisant NodeJS
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2024-10-15T16:22:56.003Z'
originalURL: https://freecodecamp.org/news/how-to-merge-word-files-using-nodejs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728997884597/9eb261f8-b299-4f43-bd0d-e2122b2c0c7b.png
tags:
- name: Node.js
  slug: nodejs
seo_title: Comment fusionner des fichiers Word en utilisant NodeJS
seo_desc: 'Merging Word files is essential for applications like document automation,
  where multiple reports, proposals, or forms need to be consolidated into a single
  document.

  Content management systems also rely on this functionality to combine documents
  for...'
---

La fusion de fichiers Word est essentielle pour des applications comme l'automatisation de documents, où plusieurs rapports, propositions ou formulaires doivent être consolidés en un seul document.

Les systèmes de gestion de contenu s'appuient également sur cette fonctionnalité pour combiner des documents en vue d'une édition collaborative ou d'un archivage.

[Node.js](https://nodejs.org/en) est un bon choix pour de telles tâches car il prend en charge à la fois les opérations côté serveur et côté client, permettant une gestion efficace des documents dans divers environnements.

Dans ce tutoriel, j'expliquerai comment [fusionner des documents Word](https://www.mergedocs.pro/merge-word-documents) en utilisant des [applications web développées en Node.js](https://www.freecodecamp.org/news/how-to-build-an-event-app-with-node-js/).

## Prérequis

1. **Node.js** et **npm** – Assurez-vous que les deux sont installés pour gérer les dépendances.

2. **Bibliothèques** – Les bibliothèques suivantes sont requises :

   * `docx-merger` pour la fusion côté serveur de fichiers Word.

   * `mammoth` pour convertir `.docx` en HTML, utile pour la fusion côté client.

   * `html-docx-js` (ou une bibliothèque similaire) pour convertir HTML en `.docx`.

## Méthode 1 : Fusion côté serveur avec `docx-merger`

[`docx-merger`](https://www.npmjs.com/package/docx-merger) est une bibliothèque spécialisée [Node.js](https://www.freecodecamp.org/news/node-js-basics/) conçue pour fusionner plusieurs fichiers `.docx` en combinant directement leur contenu, y compris le texte, les tableaux et autres éléments courants, en un seul document cohésif. Elle est particulièrement utile lorsque vous devez conserver la structure et la mise en forme originales des documents fusionnés.

Voici comment fonctionne docx-merger et pourquoi il est efficace pour la fusion côté serveur :

* **Fusion directe des éléments** `.docx` : `docx-merger` lit la structure XML sous-jacente de chaque fichier `.docx` et les combine au niveau du document. Cela préserve la mise en page, les styles, les en-têtes, les pieds de page et même les structures complexes comme les tableaux et les images, de sorte que la sortie conserve l'apparence des fichiers originaux.

* **Options de fusion configurables** : La bibliothèque offre une flexibilité dans la fusion. Vous pouvez spécifier si vous souhaitez combiner des documents entiers ou fusionner sélectivement des sections spécifiques. Cela est particulièrement utile pour les cas d'utilisation où seules certaines parties des documents doivent être fusionnées, comme l'ajout de résumés, l'ajout de pages de titre ou la combinaison de sections provenant de plusieurs rapports.

* **Gestion des objets intégrés** : `docx-merger` prend en charge les éléments intégrés tels que les images, les formes et autres médias. Lors de la fusion, il conserve ces objets, garantissant que les éléments visuels ne sont pas perdus ou déformés dans la sortie. Cela est crucial pour les rapports, les présentations et autres documents où les graphiques jouent un rôle significatif.

* **API simplifiée pour l'intégration** : L'API de `docx-merger` est simple, ce qui facilite son incorporation dans les applications Node.js. Vous initialisez la bibliothèque avec les documents que vous souhaitez fusionner, configurez les options de fusion, puis générez le résultat sous forme de fichier `.docx`. Cette facilité d'utilisation permet d'ajouter facilement la fusion de documents aux workflows existants, que ce soit en tant que script autonome ou dans le cadre d'un pipeline de traitement de documents plus large.

En utilisant `docx-merger`, vous pouvez fusionner efficacement de grands volumes de documents en toute confiance que leur mise en forme et leur contenu d'origine seront préservés, ce qui en fait un choix idéal pour le traitement de documents côté serveur en Node.js.

### **Installation de** `docx-merger`

Pour commencer, installez `docx-merger` via npm :

```javascript
npm install docx-merger
```

Cette bibliothèque ne nécessite aucune configuration supplémentaire au-delà de l'installation. Une fois installée, vous pouvez l'importer et initialiser une nouvelle instance pour commencer à fusionner des fichiers.

Elle fonctionne en lisant chaque fichier `.docx` sous forme de buffer, puis en les combinant en un seul fichier de sortie.

### **Fusion de fichiers avec** `docx-merger`

Suivez les étapes ci-dessous pour fusionner des fichiers docx en utilisant `docx-merge` :

1. Tout d'abord, importez `fs` pour gérer la lecture des fichiers et `docx-merger` pour la fusion.

2. Initialisez `docx-merger` avec un objet de configuration vide et un tableau de buffers de fichiers à fusionner.

3. Utilisez la méthode `.save()` pour fusionner et [enregistrer le fichier résultant sous forme de buffer](https://www.freecodecamp.org/news/how-to-read-and-write-files-with-nodejs/), puis écrivez-le sur le disque en utilisant `fs.writeFileSync()`.

**Exemple :**

```javascript
const fs = require('fs');

const DocxMerger = require('docx-merger');

const files = [fs.readFileSync('file1.docx'), fs.readFileSync('file2.docx')];

const docxMerger = new DocxMerger({}, files);

docxMerger.save('nodebuffer', (data) => {

 fs.writeFileSync('merged.docx', data);

});
```

Cet exemple lit `file1.docx` et `file2.docx` sous forme de buffers, les fusionne et enregistre le document fusionné sous le nom `merged.docx`.

### **Cas d'utilisation pour la fusion côté serveur :**

La fusion côté serveur avec `docx-merger` est idéale pour les scénarios nécessitant un traitement en grand volume ou une automatisation. Par exemple :

1. **Traitement de documents par lots** : Automatisation de la fusion de factures, de rapports ou d'enregistrements pour de grands ensembles de données.

2. **Workflows de documents automatisés** : Consolidation de différentes sections d'un document provenant de diverses sources pour des workflows comme la génération de rapports ou l'archivage.

3. **Services backend** : Exécution dans des environnements serveur où l'utilisateur interagit indirectement, comme la fusion de documents via une API ou une tâche backend planifiée.

## Méthode 2 : Fusion côté client avec `mammoth` et conversion HTML

[`mammoth`](https://www.npmjs.com/package/mammoth) est une bibliothèque Node.js qui [convertit les fichiers Word en HTML](https://www.docstomarkdown.pro/convert-word-to-html/), ce qui la rend idéale pour les applications côté client nécessitant une manipulation de documents en temps réel. Cette approche est particulièrement utile pour les scénarios où les utilisateurs doivent éditer ou combiner des documents directement dans le navigateur avant de les exporter.

Voici ce qui fait de `mammoth` un outil puissant pour la gestion de documents côté client :

* **Fidélité élevée** – Conversion de `.docx` en HTML : `mammoth` traduit le contenu `.docx` en HTML propre et sémantique, préservant les formats essentiels comme les titres, les paragraphes et les listes. Cela garantit que les documents convertis conservent leur structure d'origine et sont faciles à manipuler dans un environnement web.

* **Gestion des images intégrées avec Base64** – Lorsque `mammoth` rencontre des images intégrées dans un fichier `.docx`, il les encode en Base64 et les inclut dans des balises `<img>` dans le HTML de sortie. Cela permet aux images d'être affichées, fusionnées ou manipulées de manière transparente avec le texte, rendant le document final plus cohésif et visuellement précis lors de la ré-exportation en `.docx`.

* **Édition dynamique de documents** – Parce que `mammoth` génère du HTML, il est facile d'ajouter ou d'ajuster le contenu des documents côté client en utilisant JavaScript ou des frameworks côté client. Les utilisateurs peuvent combiner plusieurs extraits HTML provenant de différents fichiers `.docx`, réorganiser des sections ou même injecter du nouveau contenu dynamiquement, ce qui est précieux pour les applications nécessitant une personnalisation de contenu en temps réel.

* **Conversion en retour en** `.docx` avec `html-docx-js` – Après avoir créé ou édité un document en HTML, vous pouvez le convertir en format `.docx` en utilisant des bibliothèques comme `html-docx-js`. Cette bibliothèque prend le contenu HTML fusionné et génère un fichier `.docx` téléchargeable, ce qui facilite le retour du document final à l'utilisateur dans le format d'origine.

L'utilisation de `mammoth` pour la fusion côté client offre une manière flexible et interactive de gérer le contenu des documents dans le navigateur, avec des fonctionnalités qui prennent en charge à la fois le texte et les images. Combiné avec `html-docx-js` ou un outil similaire, vous pouvez créer des applications puissantes qui permettent aux utilisateurs de personnaliser et de fusionner des documents à la volée, puis d'exporter leur travail sous forme de fichiers `.docx`.

### **Conversion de** `.docx` **en HTML avec** `mammoth`

Tout d'abord, installez `mammoth` :

```javascript
npm install mammoth
```

Après l'installation, `mammoth` peut être utilisé pour convertir des fichiers `.docx` en HTML, ce qui permet une fusion facile du contenu des documents, y compris les images, en manipulant la sortie HTML.

**Exemple de code pour convertir des fichiers** `.docx` **en HTML :**

```javascript
import mammoth from 'mammoth';

import fs from 'fs';

async function convertDocxToHtml(filePath) {

 const result = await mammoth.convertToHtml({ path: filePath });

 return result.value;

}

async function mergeHtmlFiles() {

 const html1 = await convertDocxToHtml('file1.docx');

 const html2 = await convertDocxToHtml('file2.docx');

 const mergedHtml = html1 + html2;

 return mergedHtml;

}

const mergedHtmlContent = await mergeHtmlFiles();
```

Dans cet exemple, `convertDocxToHtml` lit un fichier `.docx` et le convertit en format HTML. `mammoth` convertit automatiquement les images du document en URLs de données encodées en Base64, afin qu'elles puissent être fusionnées et affichées avec le texte.

### **Fusion de HTML avec images et conversion en retour en** `.docx`

Une fois le contenu HTML fusionné, y compris les images encodées en Base64, vous pouvez utiliser [`html-docx-js`](https://www.npmjs.com/package/html-docx-js) pour le convertir en format `.docx`. Ce processus garantit que le texte et les images sont préservés dans la sortie finale.

**Installer** `html-docx-js`

```javascript
npm install html-docx-js
```

Ensuite, utilisez la bibliothèque pour envelopper le HTML fusionné et le convertir en `.docx` :

```javascript
import htmlDocx from 'html-docx-js';

import fs from 'fs';

const wrappedHtmlContent = <html><body>${mergedHtmlContent}</body></html>;

const docxBuffer = htmlDocx.asBlob(wrappedHtmlContent);

fs.writeFileSync('merged_with_images.docx', docxBuffer);
```

Dans ce code, le contenu HTML fusionné, qui contient du texte et des images, est enveloppé dans une structure HTML de base, puis passé à `htmlDocx.asBlob()`. Cette fonction génère un buffer `.docx`, conservant à la fois le texte et les images, qui est ensuite enregistré sous forme de fichier `.docx` sur le disque.

### **Cas d'utilisation pour la gestion des images dans la fusion côté client :**

La fusion côté client avec `mammoth` et `html-docx-js` est utile pour :

1. **Édition de documents en temps réel** : Applications interactives où les utilisateurs peuvent télécharger, fusionner et télécharger des fichiers `.docx` directement dans le navigateur, avec des images intégrées.

2. **Plateformes collaboratives** : Outils pour la création collaborative de documents, où les utilisateurs doivent fusionner des fichiers `.docx` et conserver les images intactes.

3. **Générateurs de documents personnalisés** : Applications générant des documents avec du texte et des images provenant de plusieurs fichiers `.docx`, comme des rapports personnalisés, en veillant à ce que tous les éléments soient conservés dans la sortie finale.

Cette méthode offre une solution complète pour la fusion de documents côté client, permettant une gestion flexible du contenu riche dans divers cas d'utilisation.

## Gestion des erreurs et bonnes pratiques

La fusion de fichiers Word peut présenter plusieurs défis, notamment en matière de mise en forme et de gestion des erreurs. Voici les problèmes clés, ainsi que des conseils pour la [gestion des erreurs](https://www.freecodecamp.org/news/effective-error-handling-in-react-applications/) :

### **Problèmes courants et gestion des erreurs**

1. **Incohérences de mise en page** : La conversion HTML peut entraîner des différences de mise en forme inattendues lors de la reconversion en `.docx`.

2. **Différences de style** : Les styles personnalisés dans `.docx` peuvent ne pas se traduire correctement en HTML, entraînant des écarts de police et de marges. Validez toujours que chaque fichier est correctement converti et appliquez une feuille de style cohérente pour minimiser les incohérences.

3. **Mise en forme des images** : Les images encodées en Base64 peuvent ne pas s'afficher correctement dans le `.docx` final, similaire aux défis de la [fusion de fichiers PDF](https://www.mergedocs.pro/merge-pdf-files). Assurez-vous que toutes les images sont correctement formatées avant la fusion et vérifiez les problèmes lors de la conversion.

### **Bonnes pratiques**

1. **Mise en forme cohérente** : Normalisez les styles entre les documents en utilisant une feuille de style prédéfinie pour minimiser les incohérences.

2. **Intégrité des données** : Validez que chaque fichier est lu et converti correctement en vérifiant la sortie de chaque conversion.

3. **Vérifications de l'encodage et du format** : Confirmez que tous les fichiers sont au format `.docx` attendu et que les images Base64 sont correctement formatées pour garantir des conversions réussies.

## **Conclusion**

Les deux méthodes de fusion de fichiers Word avec Node.js – en utilisant `docx-merger` pour la fusion côté serveur et `mammoth` avec la conversion HTML pour la fusion côté client – offrent une flexibilité pour divers cas d'utilisation :

**Fusion côté serveur (docx-merger) :**

* Idéale pour le traitement par lots et les workflows automatisés.

* Adaptée à la fusion de documents en grand volume sans interaction utilisateur.

* Fonctionne efficacement avec des frameworks comme Express.js et NestJS, permettant une intégration transparente dans les services backend pour le traitement de plusieurs fichiers.

**Fusion côté client (mammoth et conversion HTML) :**

* Meilleure pour les applications interactives en temps réel où les utilisateurs manipulent directement les documents.

* Prend en charge l'édition dynamique et la combinaison de documents dans le navigateur.

* Fonctionne bien avec des frameworks comme Astro.js, React ou Vue.js, facilitant une intégration fluide dans les applications web modernes.

Pour étendre cette fonctionnalité, envisagez les étapes suivantes :

* Intégrez ces méthodes dans une application ou un service web plus large où les utilisateurs peuvent télécharger et fusionner des documents directement.

* Optimisez les performances pour les environnements à forte utilisation en explorant :

   * La mise en cache des fichiers pour réduire le traitement redondant.

   * L'optimisation du processus de conversion pour la vitesse et l'efficacité.

   * L'équilibrage de charge pour les implémentations côté serveur afin de gérer plusieurs requêtes.

En suivant les bonnes pratiques et en assurant une gestion robuste des erreurs, vous pouvez créer une solution fiable et évolutive pour la fusion de fichiers `.docx` avec Node.js.