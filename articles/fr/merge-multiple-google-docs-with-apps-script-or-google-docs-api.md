---
title: Comment fusionner plusieurs Google Docs en un seul
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2024-10-29T15:49:18.798Z'
originalURL: https://freecodecamp.org/news/merge-multiple-google-docs-with-apps-script-or-google-docs-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730115525086/d5d63d7d-a5c0-4e16-868c-50901aebb248.jpeg
tags:
- name: Google Docs
  slug: google-docs
- name: APIs
  slug: apis
- name: merging
  slug: merging
seo_title: Comment fusionner plusieurs Google Docs en un seul
seo_desc: 'Merging multiple Google Docs into a single document is often essential
  for compiling reports, gathering information from various sources, or creating unified
  documents for presentations or sharing.

  By combining multiple files into one, users can keep...'
---

Fusionner plusieurs Google Docs en un seul document est souvent essentiel pour compiler des rapports, rassembler des informations provenant de diverses sources ou créer des documents unifiés pour des présentations ou des partages.

En combinant plusieurs fichiers en un seul, les utilisateurs peuvent garder les informations organisées, rationaliser la collaboration et simplifier la gestion des documents pour des projets plus importants ou des tâches récurrentes.

Mais Google Docs ne dispose pas d'une fonction intégrée pour fusionner plusieurs documents. Cela peut rendre ce processus fastidieux si vous essayez de le faire manuellement.

Bien qu'il existe des modules complémentaires disponibles pour [fusionner plusieurs Google Docs en un seul](https://workspace.google.com/marketplace/app/merge_docs_pro/61337277026), vous pouvez également créer vos propres scripts en utilisant Google Apps Script ou l'API Google Docs pour des solutions personnalisées. Cette approche vous offre une plus grande flexibilité, vous permettant de configurer une consolidation récurrente de documents et de gérer de grands volumes de fusions adaptées à vos besoins spécifiques.

Dans ce tutoriel, j'expliquerai comment fusionner plusieurs Google Docs en un seul document en utilisant [Apps Script](https://developers.google.com/apps-script) ou l'[API Google Docs](https://developers.google.com/docs/api/reference/rest).

## Comment fusionner des Google Docs en utilisant Google Apps Script

Utiliser Google Apps Script pour fusionner plusieurs Google Docs est une méthode simple pour automatiser la fusion de documents directement dans Google Workspace.

Cette approche devrait bien fonctionner pour vous si vous avez besoin d'une solution simple qui ne nécessite pas de configurations complexes ou d'API externes. Vous pouvez exécuter Apps Script dans Google Drive, ce qui le rend facile à configurer et à exécuter directement depuis le navigateur.

Voici un guide étape par étape sur la façon d'utiliser Google Apps Script pour fusionner des documents.

### **Étape 1 : Ouvrir Google Apps Script**

Dans Google Drive, cliquez sur **Nouveau** > **Google Apps Script** pour créer un nouveau script.

Ensuite, nommez le projet quelque chose de pertinent, comme "Fusionneur de documents".

### **Étape 2 : Écrire le code Apps Script**

Copiez et collez le code suivant dans l'éditeur Apps Script. Ce script créera un nouveau Google Doc et ajoutera le contenu de chaque document spécifié.

```javascript
function mergeGoogleDocs(docIds) {
  const mergedDoc = DocumentApp.create("Document Fusionné"); // Crée un nouveau document
  const body = mergedDoc.getBody();

  docIds.forEach(id => {
    const doc = DocumentApp.openById(id);
    const docBody = doc.getBody();
    
    // Ajoute le contenu de chaque document au document fusionné
    for (let i = 0; i < docBody.getNumChildren(); i++) {
      const element = docBody.getChild(i).copy(); // Copie chaque élément pour préserver la mise en forme
      body.appendParagraph(element.getText());
    }
    body.appendPageBreak(); // Ajoute un saut de page après chaque document
  });

  Logger.log("URL du Document Fusionné : " + mergedDoc.getUrl());
}

function runMerge() {
  const docIds = [
    'DOCUMENT_ID_1', 
    'DOCUMENT_ID_2', 
    'DOCUMENT_ID_3'
  ]; // Remplacez par les IDs réels de vos documents
  
  mergeGoogleDocs(docIds);
}
```

**Explication du Code :**

* **Création du Document Fusionné** : `DocumentApp.create("Document Fusionné")` crée un nouveau Google Doc nommé "Document Fusionné", qui servira de destination pour tout le contenu.
    
* **Récupération et Copie du Contenu** : `DocumentApp.openById(id)` ouvre chaque document dans `docIds`, puis récupère son contenu. Le script copie chaque élément, en préservant sa mise en forme d'origine, et l'ajoute au nouveau document.
    
* **Ajout de Sauts de Page** : `body.appendPageBreak()` ajoute un saut de page après chaque document, aidant à maintenir une séparation claire entre les sections fusionnées.
    
* **Journalisation de l'URL du Document Fusionné** : L'URL finale du document fusionné est journalisée, vous permettant d'y accéder directement depuis la console Apps Script.
    

### **Étape 3 : Exécuter le Script**

Tout d'abord, vous voudrez enregistrer le script et autoriser les permissions requises.

Ensuite, dans l'éditeur Apps Script, sélectionnez `runMerge()` comme fonction à exécuter. Entrez un tableau d'IDs de documents que vous souhaitez fusionner, comme `['DOCUMENT_ID_1', 'DOCUMENT_ID_2', 'DOCUMENT_ID_3']`.

Enfin, exécutez le script, et il créera un document fusionné dans votre Google Drive. L'URL s'affichera dans le journal de la console.

### **Comment Personnaliser le Script**

**Ordre des Documents** : La séquence dans laquelle les documents sont fusionnés est contrôlée par l'ordre des `docIds` dans le tableau. Organisez ces IDs de documents pour définir l'ordre exact que vous souhaitez dans le document final.

Cette approche est utile pour structurer des documents tels que des rapports, des livres ou des présentations, en veillant à ce que les chapitres ou sections apparaissent dans le flux prévu.

**Ajout de Mise en Forme Personnalisée** : Le script peut être personnalisé pour ajouter une mise en forme spécifique à chaque section du document fusionné. Vous pouvez insérer des en-têtes ou des pieds de page pour distinguer chaque document, inclure des sauts de page ou configurer un style cohérent pour les polices, les tailles et les couleurs.

Par exemple, vous pouvez ajouter des en-têtes de manière programmatique au début de chaque nouveau document dans la fusion, aidant à créer une structure cohésive.

**Gestion d'Éléments Spécifiques** : Apps Script prend en charge une personnalisation détaillée pour fusionner uniquement certains types de contenu, comme du texte, des images ou des tableaux, tout en ignorant les autres. Vous pouvez ajuster le script pour filtrer les éléments par type ou pour prioriser des formats spécifiques.

Par exemple, pour créer un document visuellement attrayant, vous pourriez choisir de fusionner uniquement du texte et des images tout en excluant les tableaux ou les éléments non pris en charge. Cette approche fournit un document final plus soigné en se concentrant sur les types de contenu dont vous avez le plus besoin.

### **Quand Utiliser Google Apps Script pour la Fusion**

Google Apps Script est idéal si vous voulez une solution simple, intégrée à Google Drive, sans avoir besoin de configurer un accès à une API externe. Il est particulièrement utile pour des fusions rapides ou des projets individuels au sein de Google Workspace, et il offre suffisamment de flexibilité pour gérer la plupart des formats et structures de documents standard.

Pour des exigences plus complexes, telles que la fusion à travers d'autres plateformes ou l'intégration avec des outils externes, envisagez d'utiliser l'API Google Docs expliquée dans la section suivante.

## Comment Fusionner des Google Docs en Utilisant l'API Google Docs

Combiner des Google Docs en utilisant l'API Google Docs vous permet de combiner programmatiquement le contenu de plusieurs documents en un seul fichier unifié. Cela est idéal pour automatiser des fusions répétitives ou créer des documents personnalisés à la demande.

Cette approche est puissante pour les utilisateurs qui ont besoin d'un contrôle précis sur le contenu, la mise en forme et la disposition des documents, ce qui la rend adaptée à des flux de travail plus importants ou à des intégrations au sein d'autres applications.

Voici un guide détaillé, étape par étape, sur la façon d'utiliser l'API Google Docs pour fusionner plusieurs Google Docs en un seul.

### **Étape 1 : Activer l'API Google Docs**

Tout d'abord, allez dans la [Console Google Cloud](https://console.cloud.google.com/). Créez un nouveau projet ou sélectionnez un projet existant.

Dans la Bibliothèque d'API, recherchez "Google Docs API" et activez-la pour votre projet.

Ensuite, créez des identifiants OAuth 2.0 en allant dans **APIs & Services** > **Identifiants**. Choisissez **Créer des identifiants** > **ID client OAuth** et configurez cela pour une Application Web si vous prévoyez de l'intégrer dans des services Web.

### **Étape 2 : Installer la Bibliothèque Client** `googleapis`

Dans un environnement Node.js, vous aurez besoin du package `googleapis` pour interagir avec l'API Google Docs. Installez-le en exécutant :

```bash
npm install googleapis
```

### **Étape 3 : Écrire le Script pour Fusionner les Google Docs**

Le script suivant utilise l'API Google Docs pour créer un nouveau document, récupérer le contenu de chaque document source, puis ajouter ce contenu au nouveau document.

```javascript
const { google } = require('googleapis');
const docs = google.docs('v1');

async function mergeGoogleDocs(auth, docIds) {
  // Étape 3a : Créer un nouveau document qui servira de document fusionné
  const newDoc = await docs.documents.create({
    auth,
    requestBody: { title: 'Document Fusionné' },
  });
  const newDocId = newDoc.data.documentId;

  // Étape 3b : Parcourir chaque ID de document, récupérer le contenu et l'ajouter au nouveau document
  for (const docId of docIds) {
    // Récupérer le contenu du corps du document
    const doc = await docs.documents.get({
      auth,
      documentId: docId,
    });

    // Préparer chaque élément de contenu comme une requête pour le nouveau document
    const requests = doc.data.body.content.map((element) => ({
      insertText: {
        text: element.paragraph?.elements?.[0]?.textRun?.content || '',
        location: { index: 1 }, // Ajouter au début du document, décalage à chaque insertion
      },
    }));

    // Envoyer une requête de mise à jour par lot pour insérer tous les éléments dans le nouveau document
    await docs.documents.batchUpdate({
      auth,
      documentId: newDocId,
      requestBody: { requests },
    });
  }

  console.log(`URL du Document Fusionné : https://docs.google.com/document/d/${newDocId}`);
}
```

**Explication du Code :**

1. **Création du Document Fusionné** : `docs.documents.create()` crée un nouveau Google Doc intitulé "Document Fusionné". Cet ID de document (`newDocId`) servira de destination où le contenu de chaque document sera ajouté.
    
2. **Récupération du Contenu** : La méthode `docs.documents.get()` récupère le contenu de chaque document en fonction de son ID. Cela récupère tous les éléments du corps du document, tels que les paragraphes, les images et autres éléments pris en charge.
    
3. **Préparation des Requêtes d'Insertion** : La fonction `map()` convertit chaque élément de document en une requête `insertText`. Chaque requête spécifie le texte et l'emplacement dans le nouveau document où il doit être ajouté.
    
4. **Ajout de Texte en Séquence** : La méthode `batchUpdate` prend un ensemble de requêtes et les applique séquentiellement au nouveau document. Ici, l'index de localisation commence à 1 (le début du document) et se décale à chaque nouvelle insertion pour éviter l'écrasement.
    

### **Étape 4 : Exécuter le Script**

Maintenant, vous initialiserez la variable `auth` avec des [identifiants OAuth 2.0](https://developers.google.com/identity/protocols/oauth2), qui authentifient l'accès à l'API Docs.

Ensuite, vous devrez appeler la fonction `mergeGoogleDocs`, en passant l'objet `auth` et un tableau d'IDs de documents.

Une fois le script exécuté, il générera une URL pour le document fusionné, auquel vous pourrez accéder directement dans Google Docs.

### **Personnalisation et Options Supplémentaires**

* **Ordre d'Insertion** : Contrôlez l'ordre dans lequel le contenu des documents est ajouté en organisant les IDs de documents dans `docIds`.
    
* **Mise en Forme** : L'API Google Docs peut prendre en charge une mise en forme supplémentaire, telle que du texte en gras ou en italique, en modifiant les requêtes d'insertion. Cela peut être réalisé avec des requêtes avancées en utilisant la méthode d'API `updateTextStyle`.
    
* **Types d'Éléments** : Le script gère actuellement uniquement les paragraphes de texte. Pour fusionner d'autres éléments comme des images ou des tableaux, étendez le script pour prendre en charge plus de types d'éléments en utilisant des vérifications conditionnelles sur la structure `element`.
    

### **Quand Utiliser l'API Google Docs pour la Fusion**

L'API Google Docs est idéale si vous avez besoin d'un contrôle précis sur la structure des documents, la mise en forme spécifique des éléments et l'automatisation à grande échelle pour la fusion.

Cette approche est particulièrement utile lorsque vous gérez des exigences de mise en forme complexes, telles que des en-têtes personnalisés, des listes ou des tableaux, et permet une intégration transparente avec des applications externes ou des flux de travail en dehors de Google Workspace.

Si vous avez des besoins de fusion à haut volume ou si vous cherchez à incorporer la fusion dans des processus automatisés plus larges, l'API Google Docs offre une flexibilité et des options de personnalisation avancées au-delà de ce que Google Apps Script peut offrir.

## Conclusion

En conclusion, la fusion de Google Docs est cruciale pour organiser et rationaliser la gestion des documents. Bien que Google Docs manque d'une fonction intégrée pour cela, vous pouvez exploiter Google Apps Script pour une automatisation simple ou l'API Google Docs pour une fusion plus avancée et à grande échelle.

Pour ceux qui recherchent une solution conviviale sans avoir besoin de coder, [**Merge Docs Pro**](https://www.mergedocs.pro/) offre une interface intuitive pour combiner plusieurs Google Docs en un seul document. Il simplifie la consolidation des documents, améliore la collaboration et fait gagner du temps, ce qui en fait un excellent choix si vous cherchez à rationaliser votre flux de travail au sein de Google Workspace.