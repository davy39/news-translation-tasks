---
title: Comment extraire des pages d'un PDF et les rendre avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-14T11:19:00.000Z'
originalURL: https://freecodecamp.org/news/extract-pdf-pages-render-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/pdf-extract.png
tags:
- name: JavaScript
  slug: javascript
- name: pdf
  slug: pdf
seo_title: Comment extraire des pages d'un PDF et les rendre avec JavaScript
seo_desc: "By Hrishikesh Pathak\nPDF stands for portable document format. PDFs were\
  \ designed by Adobe in the 90s for Windows. They are self-contained documents with\
  \ support for nearly all major operating systems. \nBut sometimes you'll need to\
  \ modify a PDF to sui..."
---

Par Hrishikesh Pathak

PDF signifie format de document portable. Les PDF ont été conçus par Adobe dans les années 90 pour Windows. Ce sont des documents autonomes avec support pour presque tous les systèmes d'exploitation majeurs. 

Mais parfois, vous devrez modifier un PDF pour répondre à vos besoins et pas seulement le visualiser. Malheureusement, les logiciels disponibles pour les PDF sont souvent insuffisants pour vos exigences spécialisées.

Mais vous êtes un programmeur, n'est-ce pas ? Pourquoi ne pas créer un logiciel qui aide le PDF à fonctionner comme vous le souhaitez ? Eh bien, c'est l'inspiration pour cet article.

Dans cet article, nous explorerons toutes les bibliothèques PDF populaires en JavaScript. Pourquoi JavaScript ? Parce qu'il dispose de certains packages PDF assez décents, et les gens l'aiment. Surtout moi-même.

## Le projet de visionneuse PDF que vous allez construire dans ce tutoriel

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Pdf_Modification_--.png)
_Une capture d'écran de la visionneuse PDF que vous allez construire_

Voici une [démo en direct de ce que vous allez construire](https://hrishiksh.github.io/modify-pdf-fcc/) pendant ce tutoriel.

1. Tout d'abord, nous explorerons quelques packages PDF populaires pour le travail lié aux PDF en JavaScript. Ensuite, nous les comparerons et trouverons le meilleur package qui répond à nos exigences.
2. Ensuite, nous chargerons un PDF existant et en extrairons quelques pages. Les pages extraites formeront un nouveau document PDF.
3. Puis nous rendrons le nouveau PDF (que nous avons créé à l'étape 2) dans le navigateur.
4. Enfin, nous téléchargerons le nouveau PDF pour une utilisation ultérieure.

Donc, ce sont toutes les étapes que nous allons suivre ici. J'espère que vous êtes excité de voir les résultats. Plongeons-nous.

## Bibliothèques PDF pour JavaScript

J'ai découvert deux principaux types de bibliothèques PDF en JavaScript. L'une est pour le rendu des PDF et l'autre pour la manipulation (ou modification) des PDF. J'ai trouvé un tas de bibliothèques PDF après avoir cherché pendant une heure ou deux, et voici mes meilleurs choix.

Tous les packages listés ici sont gratuits et open-source. Vous pouvez trouver tous ces packages dans le registre npm.

### [pdfjs](https://mozilla.github.io/pdf.js)

Ce package est fait par Mozilla, la société derrière le navigateur web Firefox. pdfjs est une plateforme basée sur les standards web pour analyser et rendre les PDF. 
Lorsque vous visualisez un PDF dans Firefox, le visionneur PDF est fait avec ce package pdfjs.

La force principale de ce package est le rendu des PDF sur une page web. Les autres fonctionnalités de modification des PDF sont très limitées avec ce package. Si vous voulez créer un visionneur PDF personnalisé pour votre site, probablement ce package est celui que vous recherchez.

pdfjs a une API très simple. Ils ont beaucoup de tutoriels pour commencer avec la bibliothèque. Si vous n'êtes pas suffisamment convaincu, jouez avec cette bibliothèque pendant un certain temps et vous allez sûrement tomber amoureux.

### [pdf-lib](https://pdf-lib.js.org/)

Contrairement au package pdfjs précédent, pdf-lib est principalement utilisé pour la création et la manipulation de PDF. Vous pouvez générer un nouveau document PDF dynamiquement avec ce package selon vos besoins.

Ce package a un support robuste pour modifier un document existant. Vous pouvez faire beaucoup de modifications de PDF avec cette bibliothèque. Par exemple, vous pouvez faire la division et la fusion de PDF, et vous pouvez extraire une page, annoter un document PDF, ajouter un plan, et bien d'autres choses que vous pouvez imaginer.

Il n'a que JavaScript comme dépendance. Donc, il peut fonctionner sur n'importe quel appareil qui a un runtime JavaScript. Le navigateur, Nodejs, Deno, et React Native sont bien supportés. Si vous pouvez installer JavaScript sur un appareil, alors cette bibliothèque fonctionnera sûrement.

Le principal inconvénient de pdf-lib est qu'il n'a pas un fort support de rendu. Si vous voulez faire une belle UI pour la visualisation de PDF avec cette bibliothèque, alors pdf-lib n'est pas le bon choix pour vous. Dans ce scénario, vous devriez utiliser pdfjs à la place.

### [pdfjs](https://github.com/rkusa/pdfjs) #2

Si vous pensez que je me répète, alors ce n'est pas le cas. Il s'agit d'une bibliothèque JavaScript pour créer des documents PDF. Elle a une API très simple à utiliser.

La bibliothèque pdfjs précédente que nous avons discutée a un très bon support de rendu dans l'UI mais elle manque de fonctionnalités de création et de modification de PDF.

Mais cette bibliothèque est construite en pensant à la création de PDF. Elle a une API très simple et est adaptée aux débutants. Vous pouvez la comparer avec le package pdf-lib.

Le principal inconvénient de cette bibliothèque pdfjs est que le support pour la modification de documents existants est encore en phase bêta. Cela ne fonctionne pas tout le temps et est encore en cours de développement. 

Si votre objectif principal est la modification de PDF (par exemple, l'extraction de pages, la fusion, la division, l'annotation, etc.), alors cette bibliothèque pourrait ne pas fonctionner pour vous.

Si les contributeurs peuvent faire fonctionner la fonctionnalité de modification, alors ce pourrait être le meilleur package PDF pour JavaScript.

### [js-pdf](https://parall.ax/products/jspdf)

Contrairement à tous les packages PDF listés ci-dessus, cette bibliothèque est une véritable bête. Vous pouvez faire n'importe quel travail lié aux PDF avec cette bibliothèque. C'est comme une bibliothèque polyvalente. Si vous voulez des fonctionnalités sophistiquées liées aux PDF, alors cette bibliothèque peut le faire.

Mais il existe de meilleurs packages en JavaScript qui sont très bons pour des tâches individuelles. Par exemple, pdfjs est un meilleur moteur de rendu PDF que js-pdf, et pdf-lib a un meilleur support de modification que js-pdf.

Ici, je ne parle pas de la performance réelle ou d'autres types de métriques, je parle de l'expérience du développeur. Je trouve que son API n'est pas très intuitive. Pour un débutant, cela peut être écrasant au premier abord. C'est mon opinion, cependant, et ce que j'ai expérimenté lorsque je l'ai utilisé.

La génération de PDF est la principale force de cette bibliothèque. Vous pouvez générer n'importe quel type de PDF avec le design que vous avez. Ce package fera tout le travail difficile pour vous. Si vous êtes expérimenté, alors ce pourrait être le meilleur choix pour vous.

### [react-pdf](https://react-pdf.org/) 

Comme son nom l'indique, cette bibliothèque est spécialisée dans les écosystèmes React. L'utilisation est très React-ish. Vous pouvez facilement créer un document avec sa syntaxe de type JSX.

Vous pouvez créer et afficher un document PDF avec des composants React simples. Mais les fonctionnalités sont très limitées. Cette bibliothèque est principalement pour la génération de PDF.

Si votre objectif est d'afficher un PDF à l'utilisateur, alors vous pouvez utiliser ce package. En tant qu'amoureux de React, vous allez adorer cette bibliothèque. Consultez leur terrain de jeu et passez un peu de temps avec ce package. De cette façon, vous saurez si vous avez besoin de cette bibliothèque ou non.

## Pourquoi nous allons utiliser pdf-lib dans ce tutoriel

Parmi toutes ces bibliothèques PDF mentionnées ci-dessus, j'utiliserai pdf-lib pour cet article. Comme nous allons diviser et fusionner des pages PDF et aussi les rendre dans le navigateur, pdf-lib semble être le meilleur choix pour ce contexte.

De plus, pdf-lib a une API assez simple à utiliser et toutes ces API sont bien documentées. Si vous utilisez TypeScript, vous pouvez également obtenir l'inférence de type, ce qui est très utile.

Last but not least, leurs exemples sont très bons. Vous pouvez être opérationnel en quelques minutes. Donc j'aime cette bibliothèque pour mes cas d'utilisation.

## Comment lire un fichier PDF local en JavaScript

Avant de faire des opérations sur notre document PDF, nous devons obtenir le document de l'utilisateur. La lecture de n'importe quel fichier dans le navigateur peut être gérée par l'API web `FileReader`.

Tout d'abord, nous allons créer un bouton d'entrée de fichier et ensuite traiter le fichier téléchargé en utilisant l'API web `FileReader`.

```html
<input type="file" id="file-selector" accept=".pdf" onChange={onFileSelected} />
```

Comme l'API Filereader fonctionne avec des callbacks, je trouve async/await beaucoup plus propre et plus facile à utiliser. Donc, faisons une fonction helper pour modifier les callbacks de Filereader en async/await.

```js
function readFileAsync(file) {
    return new Promise((resolve, reject) => {
      let reader = new FileReader();
      reader.onload = () => {
        resolve(reader.result);
      };
      reader.onerror = reject;
      reader.readAsArrayBuffer(file);
    });
  }
```

Maintenant, lorsqu'un utilisateur télécharge un fichier en utilisant l'entrée de fichier précédente, nous écoutons l'événement d'entrée de fichier et ensuite nous lisons le fichier en utilisant cette fonction `readFileAsync`.

L'implémentation de cette logique ressemble à ceci en code :

```js
const onFileSelected = async (e) => {
    const fileList = e.target.files;
    if (fileList?.length > 0) {
      const pdfArrayBuffer = await readFileAsync(fileList[0]);
    }
  };
```

## Comment extraire des pages PDF

Jusqu'à présent, notre PDF est téléchargé et converti en `ArrayBuffer` JavaScript. Comme nous extrayons une plage de pages du PDF, nous voulons un tableau avec ces numéros de page du PDF.

Générer un tableau de nombres naturels n'est pas difficile en JavaScript. Donc nous faisons une fonction nommée `range()` pour générer tous les index que nous voulons. 

Nous devons fournir le numéro de page de début et le numéro de page de fin, puis cette fonction `range()` peut générer un tableau avec les numéros de page appropriés.

```js
function range(start, end) {
	let length = end - start + 1;
	return Array.from({ length }, (_, i) => start + i - 1);
}

```

Ici, nous ajoutons -1 à la fin. Connaissez-vous la raison ? Oui – en programmation, les index commencent à 0, pas à 1. Donc nous devons déduire -1 de chaque numéro de page pour obtenir le comportement que nous voulons.

Maintenant, commençons la partie principale de cet article : l'extraction. Avant de faire tout le travail, importez la bibliothèque pdf-lib.

```js
import { PDFDocument } from "pdf-lib";

```

Tout d'abord, nous chargeons le `ArrayBuffer` PDF que nous avons obtenu de la fonction `onFileSelected` précédente. Ensuite, nous chargeons le `ArrayBuffer` dans la fonction `PDFDocument.load(arraybuffer)`. C'est notre PDF fourni par l'utilisateur. Pour plus de commodité, nous l'appellerons `pdfSrcDoc`.

Maintenant, nous allons créer un nouveau PDF. Toutes les pages PDF extraites du document fourni par l'utilisateur sont fusionnées dans le nouveau document. Nous utilisons la fonction `PDFDocument.create()` pour cela. Pour faciliter l'utilisation, nous l'appelons `pdfNewDoc`.

Après cela, nous copions nos pages souhaitées de `pdfSrcDoc` dans `pdfNewDoc` en utilisant la fonction `copyPages()`. Ensuite, nous ajouterons la page copiée à `pdfNewDoc`.

Pour enregistrer les modifications, exécutez `pdfNewDoc.save()`. Créons une fonction appelée `extractPdfPage()` pour réutiliser la logique. Le code à l'intérieur de la fonction ressemblera à ceci :

```js
async function extractPdfPage(arrayBuff) {
    const pdfSrcDoc = await PDFDocument.load(arrayBuff);
    const pdfNewDoc = await PDFDocument.create();
    const pages = await pdfNewDoc.copyPages(pdfSrcDoc,range(2,3));
    pages.forEach(page=>pdfNewDoc.addPage(page));
    const newpdf= await pdfNewDoc.save();
    return newpdf;
  }
```

Nous retournons un `Uint8Array` de la fonction `extractPdfPage()`.

## Comment rendre le PDF dans le navigateur

Jusqu'à présent, nous avons un `Uint8Array` d'un PDF modifié. Pour le rendre dans votre navigateur, nous devons le convertir en Blob.

Ensuite, nous allons créer une URL à partir de celui-ci et le rendre dans un iframe.

Vous pouvez également créer votre propre visionneur PDF en utilisant la bibliothèque pdfjs comme je l'ai mentionné ci-dessus. Mais si vous n'avez pas besoin d'une telle personnalisation, le visionneur PDF par défaut du navigateur est suffisant pour cet usage.

```js
function renderPdf(uint8array) {
    const tempblob = new Blob([uint8array], {
      type: "application/pdf",
    });
    const docUrl = URL.createObjectURL(tempblob);
    setPdfFileData(docUrl);
  }
```

Maintenant, vous pouvez facilement rendre cette docUrl retournée par la fonction `renderPdf()` dans un `iframe`. 

## Exemple de code complet

J'utilise Next.js pour ce tutoriel. Si vous utilisez un autre framework ou JavaScript vanilla, les résultats seront similaires. Voici tout le code pour ce projet :

```js
import { useState } from "react";
import { PDFDocument } from "pdf-lib";

export default function Home() {
  const [pdfFileData, setPdfFileData] = useState();

  function readFileAsync(file) {
    return new Promise((resolve, reject) => {
      let reader = new FileReader();
      reader.onload = () => {
        resolve(reader.result);
      };
      reader.onerror = reject;
      reader.readAsArrayBuffer(file);
    });
  }

  function renderPdf(uint8array) {
    const tempblob = new Blob([uint8array], {
      type: "application/pdf",
    });
    const docUrl = URL.createObjectURL(tempblob);
    setPdfFileData(docUrl);
  }

  function range(start, end) {
    let length = end - start + 1;
    return Array.from({ length }, (_, i) => start + i - 1);
  }

  async function extractPdfPage(arrayBuff) {
    const pdfSrcDoc = await PDFDocument.load(arrayBuff);
    const pdfNewDoc = await PDFDocument.create();
    const pages = await pdfNewDoc.copyPages(pdfSrcDoc, range(2, 3));
    pages.forEach((page) => pdfNewDoc.addPage(page));
    const newpdf = await pdfNewDoc.save();
    return newpdf;
  }

  // Exécuter lorsque l'utilisateur sélectionne un fichier
  const onFileSelected = async (e) => {
    const fileList = e.target.files;
    if (fileList?.length > 0) {
      const pdfArrayBuffer = await readFileAsync(fileList[0]);
      const newPdfDoc = await extractPdfPage(pdfArrayBuffer);
      renderPdf(newPdfDoc);
    }
  };

  return (
    <>
      <h1>Bonjour le monde</h1>
      <input
        type="file"
        id="file-selector"
        accept=".pdf"
        onChange={onFileSelected}
      />
      <iframe
        style={{ display: "block", width: "100vw", height: "90vh" }}
        title="PdfFrame"
        src={pdfFileData}
        frameborder="0"
        type="application/pdf"
      ></iframe>
    </>
  );
}

```

Vous pouvez maintenant enregistrer le PDF résultant en utilisant le bouton de téléchargement sur le visionneur PDF.

## Où aller à partir d'ici

Dans cet article, je n'ai fait qu'effleurer la surface. Si vous voulez travailler avec des PDF et en faire quelque chose, alors pdf-lib est une bibliothèque très puissante à cet effet.

Vous pouvez fusionner deux PDF en un seul, vous pouvez faire pivoter des pages, ou supprimer certaines pages d'un PDF. Ce ne sont que quelques exemples – les possibilités sont infinies.

Si vous voulez déployer votre application Next.js sur Cloudflare Pages, [c'est l'article](https://hrishikeshpathak.com/blog/deploy-nextjs-cloudflare-pages) que vous devriez consulter.

Faites quelque chose avec cela. Faites des choses créatives et montrez-les moi sur [Twitter](https://twitter.com/hrishikshpathak).

## Conclusion

Si vous avez lu jusqu'ici, je vous suis très reconnaissant. Cela donne l'impression que je crée du contenu que quelqu'un d'une autre partie du monde lira. Partagez-le avec vos amis codeurs.

Voulez-vous ajouter un plan à votre document PDF ? Je sais que c'est une tâche très difficile à réaliser. J'ai traversé beaucoup de difficultés pour ajouter cette fonctionnalité dans un document PDF en utilisant JavaScript. Êtes-vous intéressé ? C'est une histoire pour l'avenir.

Passez une bonne journée.