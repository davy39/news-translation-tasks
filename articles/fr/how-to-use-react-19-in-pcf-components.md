---
title: Comment utiliser React 19 dans les composants PCF de Power Apps
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-05-23T13:22:04.987Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-19-in-pcf-components
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747861011004/173ecdcd-7bca-4c4f-967b-47616bd79a06.png
tags:
- name: powerapps
  slug: powerapps
- name: pcf
  slug: pcf
- name: React
  slug: reactjs
seo_title: Comment utiliser React 19 dans les composants PCF de Power Apps
seo_desc: 'The Power Apps Component Framework – PCF for short – lets you create complex
  custom components using traditional web development tools like HTML, CSS, and JavaScript.

  When creating a new PCF project, you can choose from two types of controls: standar...'
---

Le Power Apps Component Framework  PCF en abrégé  vous permet de créer des composants personnalisés complexes en utilisant des outils traditionnels de développement web comme HTML, CSS et JavaScript.

Lors de la création d'un nouveau projet PCF, vous pouvez choisir entre deux types de contrôles : les **contrôles standard** et les **contrôles virtuels React**. Pour les composants non triviaux, React est souvent un bon choix car il abstrait une grande partie de la manipulation lourde du DOM. Cependant, lorsque vous utilisez React avec PCF, vous êtes actuellement limité à React 16 dans les applications Canvas et React 17 dans les applications Model-Driven.

Cela ne signifie pas que vous *ne pouvez pas* utiliser une version plus récente  mais cela signifie renoncer au support de la virtualisation. Pour de nombreux composants PCF, ce compromis est généralement acceptable.

Dans cet article, je vais vous montrer comment intégrer la dernière version de React (v19) avec votre composant PCF. Nous installerons les dépendances nécessaires et configurerons le composant pour tirer pleinement parti de la dernière version de React.

### Cet article suppose que vous :

* Comprenez comment utiliser le PAC CLI pour créer des projets PCF.

* Êtes à l'aise avec l'utilisation de la ligne de commande et d'un éditeur de code (par exemple, VS Code)

* Connaissez les bases de React

* Avez une certaine expérience avec le développement PCF

Note : Vous n'avez pas besoin d'accès à un environnement Power Platform sauf si vous souhaitez déployer le composant. Le harnais de test intégré sera suffisant pour suivre cet article.

### Dans ce tutoriel, vous allez :

* [Créer un projet PCF](#heading-creer-un-projet-pcf)

* [Installer les dépendances React](#heading-installer-les-dependances-react)

* [Créer un bouton non-React](#heading-creer-un-bouton-non-react)

* [Créer un bouton React](#heading-creer-un-bouton-react)

* [Ajouter le bouton React au composant PCF](#heading-ajouter-le-bouton-react-au-composant-pcf)

* [Rendre le bouton React lorsque le composant PCF est mis à jour](#heading-rendre-le-bouton-react-lorsque-le-composant-pcf-est-mis-a-jour)

## Créer un projet PCF

Pour créer un projet PCF, vous utiliserez le **PAC CLI**. Si vous ne l'avez pas encore installé, suivez les instructions [ici](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction?tabs=windows).

À partir du répertoire de votre choix, créez un nouveau dossier pour ce projet, puis ouvrez votre terminal et exécutez :

```bash
pac pcf init -ns SampleNameSpace -n SampleComponent --template field
```

Une fois terminé, exécutez :

```bash
npm install
```

Cela installe les dépendances du projet par défaut.

Alors, pourquoi n'avons-nous pas utilisé le drapeau `--framework` pour spécifier React lors de la création du projet ? Parce que ce drapeau configure un contrôle virtuel React, qui ne supporte que React 16/17. Au lieu de cela, nous créons un contrôle standard et installons React nous-mêmes.

## Installer les dépendances React

Pour utiliser React 19, vous aurez besoin de quatre dépendances :

* `react`

* `react-dom`

* `@types/react`

* `@types/react-dom`

Ces deux dernières fournissent les typages TypeScript pour React. Installez les dépendances ci-dessus avec :

```bash
npm install -D react react-dom @types/react @types/react-dom
```

Vous pouvez vérifier l'installation en regardant le fichier `package.json` dans le projet.

![Le fichier package.json montrant les dépendances react installées.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747410603816/a7eeeb60-dcbe-49c9-9913-6319cd246333.png align="center")

Bien que ce ne soit pas nécessaire pour ce que nous allons faire, afin d'utiliser certaines des nouvelles fonctionnalités de React, vous devrez peut-être ajuster les `compilerOptions` dans le fichier `tsconfig.json` pour inclure la ligne suivante :

```json
"jsx": "react-jsx"
```

Voici à quoi devrait ressembler le fichier `tsconfig.json` avec la ligne `jsx` ajoutée :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1747410782472/524ac9a6-3898-4427-8bab-090fe0a3f718.png align="center")

## Créer un bouton non-React

Vérifions que tout fonctionne avant d'introduire React.

À partir de la ligne de commande, exécutez :

```bash
npm run start:watch
```

Cela peut prendre un moment. Cela ouvrira un navigateur montrant votre harnais de test PCF. Vous verrez probablement un écran vide. C'est normal  nous n'avons encore rien rendu.

Ouvrez `index.ts` dans le dossier `SampleComponent`. Ce fichier contient une classe qui implémente l'interface de contrôle standard PCF. Créons un bouton basique non-React.

Mettez à jour la méthode `init` dans le fichier `index.ts` comme ceci :

```typescript
public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
): void {
    // Un bouton basique avec du JS vanilla et le DOM
    const btn = document.createElement('button');
    btn.textContent = 'Cliquez-moi !';
    container.appendChild(btn);

    // Un écouteur d'événement simple pour les clics sur le bouton
    btn.addEventListener('click', () => {
        alert('Bouton cliqué !');
    });
}

```

Maintenant, retournez à votre harnais de test. Vous devriez voir un bouton. Cliquer dessus devrait afficher une alerte.

![Harnais de test PCF avec bouton cliquable.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747411524929/36d26f79-1d48-403c-9005-56655a16ed04.png align="center")

![Harnais de test PCF avec alerte affichée après que le bouton a été cliqué.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747411544199/85aab788-1a02-439c-8597-d74d6fa3a39c.png align="center")

## Créer un bouton React

Ensuite, remplaçons notre code DOM simple par React.

Supprimez le code du bouton de `init()`, laissant la méthode `init` vide.

Ensuite, créez un nouveau fichier : `Button.tsx`. À l'intérieur de `Button.tsx`, ajoutez le code ci-dessous. Ce composant acceptera une prop label et émettra un événement `onClick`. Assurez-vous d'exporter la fonction.

```typescript
export default function Button(props: { label: string; onClick: () => void }) {
    return <button onClick={props.onClick}>{props.label}</button>;
}
```

## Ajouter le bouton React au composant PCF

Dans `index.ts`, mettez à jour le fichier pour :

1. Importer `createRoot` depuis `react-dom/client`

2. Importer le composant `Button`

3. Rendre le composant `Button`

Voici l'exemple minimal :

```typescript
import { createRoot } from 'react-dom/client'; // importer la méthode createRoot
import Button from './Button'; // importer le composant button.tsx que nous venons de créer

export class SampleComponent
    implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
    constructor() {
        // Vide
    }
    public init(
        context: ComponentFramework.Context<IInputs>,
        notifyOutputChanged: () => void,
        state: ComponentFramework.Dictionary,
        container: HTMLDivElement
    ): void {
        // Ajoutez le code ci-dessous pour créer une racine React qui nous permet de rendre notre composant de bouton.
        const root = createRoot(container);
        root.render(
            Button({ label: 'Bouton React', onClick: () => alert('Bouton React cliqué !') })
        );
    }
    // Autres méthodes ici...
}
```

Vous devriez maintenant voir « Bouton React » dans le navigateur. Cliquer dessus déclenchera l'alerte.

![Harnais de test PCF avec le bouton React](https://cdn.hashnode.com/res/hashnode/image/upload/v1747412200377/ef496e75-de8f-4abe-8371-25dd295ee057.png align="center")

![Harnais de test PCF avec alerte affichée après que le bouton React a été cliqué.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747412239139/d4c73764-667f-445c-9366-aa270e456d13.png align="center")

## Rendre le bouton React lorsque le composant PCF est mis à jour

De nombreux composants PCF reçoivent des valeurs d'entrée dynamiques. Si les entrées changent, nous voulons que le composant React se re-render. C'est là que `updateView()` intervient. `updateView()` est déclenché lorsque le sac de propriétés PCF change.

Déplaçons la logique de rendu de `init()` vers `updateView()`.

Tout d'abord, importez `Root` depuis `react-dom/client`, et initialisez `root` en tant que propriété de la classe.

```typescript
import { createRoot, Root } from 'react-dom/client'; // ajoutez Root comme une importation

export class SampleComponent implements ComponentFramework.StandardControl<IInputs, IOutputs> {
    root: Root; // initialisez la propriété root sur la classe SampleComponent
    constructor() {
        // Vide
    }
    // autres méthodes ici...
}
```

Ensuite, modifiez `init()` pour définir `this.root` sur la racine créée par la méthode `createRoot` de React. Déplacez la logique de rendu de la méthode `init` vers `updateView()`, en remplaçant `root` par `this.root`.

```typescript
public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
    ): void {
        this.root = createRoot(container); // attribuez la racine que React crée à this.root
    }

public updateView(context: ComponentFramework.Context<IInputs>): void {
    // rendre le composant de bouton React, en référençant this.root
    this.root.render(
        Button({ label: 'Bouton React', onClick: () => alert('Bouton cliqué !') })
    );
}
```

Avec la configuration ci-dessus, React va maintenant re-rendre votre bouton lorsque le sac de propriétés d'un composant PCF change.

## Conclusion

Vous avez maintenant créé un composant PCF qui utilise la dernière version de React ! En installant et en configurant React manuellement, vous évitez les limitations de version des contrôles React intégrés de Microsoft  déverrouillant la puissance des fonctionnalités modernes de React.

Bien que cette configuration ne supporte pas la virtualisation, pour de nombreux composants, c'est un compromis équitable pour des outils modernes et une maintenabilité.

Si vous construisez des composants PCF au-delà de la simple manipulation du DOM, React peut être un moyen puissant d'améliorer votre flux de développement et la flexibilité de l'UI.

***Avez-vous aimé cet article ?*** J'écris régulièrement sur le low-code, les modèles de développement et les sujets technologiques pratiques sur [scriptedbytes.com](https://www.scriptedbytes.com/)