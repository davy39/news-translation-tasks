---
title: Comment automatiser le processus de publication de vos articles de blog avec
  TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-06T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/automating-my-blog-posts-publishing-process-with-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/cover.jpg
tags:
- name: Developer Tools
  slug: developer-tools
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: TypeScript
  slug: typescript
seo_title: Comment automatiser le processus de publication de vos articles de blog
  avec TypeScript
seo_desc: 'By TK

  Since I''m trying to build a writing habit, well, I''m writing more and more. Even
  though I use publishing blogs like Medium, dev.to, and Hashnode, I like to post
  my content on my own blog as well.

  As I wanted to build a simple website, this blog...'
---

Par TK

Comme j'essaie de prendre l'habitude d'écrire, j'écris de plus en plus. Même si j'utilise des plateformes de publication comme [Medium](https://medium.com/@leandrotk_), [dev.to](https://dev.to/teekay), et [Hashnode](https://hashnode.com/@teekay), j'aime aussi publier mon contenu sur [mon propre blog](http://leandrotk.github.io/tk).

Comme je voulais construire un site web simple, ce blog est essentiellement composé de HTML et de CSS avec très peu de JavaScript. Mais le fait est que j'avais besoin d'améliorer le processus de publication.

Alors, comment cela fonctionne-t-il maintenant ?

Je gère la roadmap du blog sur Notion. Cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/blog-roadmap.png)

C'est un simple tableau de type Kanban. J'aime ce tableau parce qu'il me permet d'avoir une représentation physique (ou numérique ?) de toutes mes idées. Je l'utilise également pour construire un brouillon, le peaufiner et l'améliorer de plus en plus, puis le publier sur le blog.

J'écris donc mes articles de blog en utilisant Notion. Une fois terminé, je copie le texte de Notion et je le colle dans un outil en ligne pour transformer le Markdown en HTML. Ensuite, je peux utiliser ce HTML pour créer l'article réel.

Mais ce n'est que le corps, le contenu de la page. Je dois toujours créer l'intégralité du HTML avec le contenu du head, du body et du footer.

Ce processus est fastidieux et ennuyeux. Mais bonne nouvelle, il peut être automatisé. Et cet article traite justement de cette automatisation. Je veux vous montrer les coulisses de ce nouvel outil que j'ai créé et ce que j'ai appris au cours de ce processus.

## Fonctionnalités

Mon idée principale était d'avoir un article HTML complet prêt à être publié. Comme je l'ai mentionné précédemment, les sections `<head>` et `<footer>` ne changent pas beaucoup. Je pouvais donc les utiliser comme un "template".

Avec ce template, j'ai des données qui peuvent changer pour chaque article que j'écris et publie. Ces données sont des variables dans le template avec cette représentation `{{ variableName }}`. Un exemple :

```html
<h1>{{ title }}</h1>

```

Maintenant, je peux utiliser le template et remplacer les variables par des données réelles – des informations spécifiques pour chaque article.

La deuxième partie est le corps, l'article réel. Dans le template, il est représenté par `{{ article }}`. Cette variable sera remplacée par le HTML généré à partir du Markdown de Notion.

Lorsque nous copions et collons des notes depuis Notion, nous obtenons une sorte de style Markdown. Ce projet transformera ce Markdown en HTML et l'utilisera comme variable `article` dans le template.

Pour créer le template idéal, j'ai examiné toutes les variables que je devais créer :

* `title`
* `description`
* `date`
* `tags`
* `imageAlt`
* `imageCover`
* `photographerUrl`
* `photographerName`
* `article`
* `keywords`

Avec ces variables, j'ai créé le [template](https://github.com/leandrotk/publisher/blob/master/examples/template.html).

Pour transmettre certaines de ces informations pour construire le HTML, j'ai créé un fichier `json` comme configuration de l'article : `article.config.json`. J'y ai quelque chose comme ceci :

```json
{
  "title": "React Hooks, Context API, and Pokemons",
  "description": "Understanding how hooks and the context api work",
  "date": "2020-04-21",
  "tags": [
    "javascript",
    "react"
  ],
  "imageAlt": "The Ash from Pokemon",
  "photographerUrl": "<https://www.instagram.com/kazuh.illust>",
  "photographerName": "kazuh.yasiro",
  "articleFile": "article.md",
  "keywords": "javascript,react"
}

```

La première étape était que le projet sache comment ouvrir et lire le template et la configuration de l'article. J'utilise ces données pour remplir le template.

Le template d'abord :

```typescript
const templateContent: string = await getTemplateContent();

```

Nous devons donc essentiellement implémenter la fonction `getTemplateContent`.

```typescript
import fs, { promises } from 'fs';
import { resolve } from 'path';

const { readFile } = promises;

const getTemplateContent = async (): Promise<string> => {
  const contentTemplatePath = resolve(__dirname, '../examples/template.html');
  return await readFile(contentTemplatePath, 'utf8');
};

```

Le `resolve` avec `__dirname` obtiendra le chemin absolu vers le répertoire du fichier source en cours d'exécution. Ensuite, il va vers le fichier `examples/template.html`. Le `readFile` lira de manière asynchrone et renverra le contenu du chemin du template.

Maintenant que nous avons le contenu du template, nous devons faire la même chose pour la configuration de l'article.

```typescript
const getArticleConfig = async (): Promise<ArticleConfig> => {
  const articleConfigPath = resolve(__dirname, '../examples/article.config.json');
  const articleConfigContent = await readFile(articleConfigPath, 'utf8');
  return JSON.parse(articleConfigContent);
};

```

Deux choses différentes se produisent ici :

* Comme `article.config.json` est au format JSON, nous devons transformer cette chaîne JSON en un objet JavaScript après avoir lu le fichier.
* Le retour du contenu de la configuration de l'article sera un `ArticleConfig` tel que je l'ai défini dans le type de retour de la fonction. Construisons-le.

```typescript
type ArticleConfig = {
  title: string;
  description: string;
  date: string;
  tags: string[];
  imageCover: string;
  imageAlt: string;
  photographerUrl: string;
  photographerName: string;
  articleFile: string;
  keywords: string;
};

```

Lorsque nous récupérons ce contenu, nous utilisons également ce nouveau type.

```typescript
const articleConfig: ArticleConfig = await getArticleConfig();

```

Maintenant, nous pouvons utiliser la méthode `replace` pour remplir les données de configuration dans le contenu du template. Juste pour illustrer l'idée, cela ressemblerait à ceci :

```typescript
templateContent.replace('title', articleConfig.title)

```

Mais certaines variables apparaissent plus d'une fois dans le template. Les Regex à la rescousse. Avec ceci :

```typescript
new RegExp('\\{\\{(?:\\\\s+)?(title)(?:\\\\s+)?\\}\\}', 'g');

```

... j'obtiens toutes les chaînes qui correspondent à `{{ title }}`. Je peux donc construire une fonction qui reçoit un paramètre à trouver et l'utilise à la place du titre.

```typescript
const getPattern = (find: string): RegExp =>
  new RegExp('\\{\\{(?:\\\\s+)?(' + find + ')(?:\\\\s+)?\\}\\}', 'g');

```

Maintenant, nous pouvons remplacer toutes les correspondances. Un exemple pour la variable title :

```typescript
templateContent.replace(getPattern('title'), articleConfig.title)

```

Mais nous ne voulons pas remplacer seulement la variable title, mais toutes les variables de la configuration de l'article. Remplaçons tout !

```typescript
const buildArticle = (templateContent: string) => ({
  with: (articleConfig: ArticleAttributes) =>
    templateContent
      .replace(getPattern('title'), articleConfig.title)
      .replace(getPattern('description'), articleConfig.description)
      .replace(getPattern('date'), articleConfig.date)
      .replace(getPattern('tags'), articleConfig.articleTags)
      .replace(getPattern('imageCover'), articleConfig.imageCover)
      .replace(getPattern('imageAlt'), articleConfig.imageAlt)
      .replace(getPattern('photographerUrl'), articleConfig.photographerUrl)
      .replace(getPattern('photographerName'), articleConfig.photographerName)
      .replace(getPattern('article'), articleConfig.articleBody)
      .replace(getPattern('keywords'), articleConfig.keywords)
});

```

Maintenant je remplace tout ! Nous l'utilisons comme ceci :

```typescript
const article: string = buildArticle(templateContent).with(articleConfig);

```

Mais il nous manque deux parties ici :

* `tags`
* `article`

Dans le fichier JSON de configuration, `tags` est une liste. Donc, pour la liste :

```json
['javascript', 'react'];

```

Le HTML final serait :

```html
<a class="tag-link" href="../../../tags/javascript.html">javascript</a>
<a class="tag-link" href="../../../tags/react.html">react</a>

```

J'ai donc créé un autre template : `tag_template.html` avec la variable `{{ tag }}`. Nous avons juste besoin de mapper la liste `tags` et de créer chaque template de balise HTML.

```typescript
const getArticleTags = async ({ tags }: { tags: string[] }): Promise<string> => {
  const tagTemplatePath = resolve(__dirname, '../examples/tag_template.html');
  const tagContent = await readFile(tagTemplatePath, 'utf8');
  return tags.map(buildTag(tagContent)).join('');
};

```

Ici, nous :

* récupérons le chemin du template de tag
* récupérons le contenu du template de tag
* parcourons les `tags` et construisons le HTML final du tag basé sur le template

`buildTag` est une fonction qui renvoie une autre fonction.

```typescript
const buildTag = (tagContent: string) => (tag: string): string =>
  tagContent.replace(getPattern('tag'), tag);

```

Elle reçoit `tagContent` - c'est le contenu du template de tag - et renvoie une fonction qui reçoit un tag et construit le HTML final du tag. Et maintenant, nous l'appelons pour obtenir les tags de l'article.

```typescript
const articleTags: string = await getArticleTags(articleConfig);

```

À propos de l'article maintenant. Cela ressemble à ceci :

```typescript
const getArticleBody = async ({ articleFile }: { articleFile: string }): Promise<string> => {
  const articleMarkdownPath = resolve(__dirname, `../examples/${articleFile}`);
  const articleMarkdown = await readFile(articleMarkdownPath, 'utf8');
  return fromMarkdownToHTML(articleMarkdown);
};

```

Elle reçoit `articleFile`, nous essayons d'obtenir le chemin, de lire le fichier et de récupérer le contenu Markdown. Ensuite, nous passons ce contenu à la fonction `fromMarkdownToHTML` pour transformer le Markdown en HTML.

Pour cette partie, j'utilise une bibliothèque externe appelée `showdown`. Elle gère tous les cas particuliers pour transformer le Markdown en HTML.

```typescript
import showdown from 'showdown';

const fromMarkdownToHTML = (articleMarkdown: string): string => {
  const converter = new showdown.Converter()
  return converter.makeHtml(articleMarkdown);
};

```

Et maintenant j'ai les tags et le HTML de l'article :

```typescript
const templateContent: string = await getTemplateContent();
const articleConfig: ArticleConfig = await getArticleConfig();
const articleTags: string = await getArticleTags(articleConfig);
const articleBody: string = await getArticleBody(articleConfig);

const article: string = buildArticle(templateContent).with({
  ...articleConfig,
  articleTags,
  articleBody
});

```

J'ai oublié une chose de plus ! Auparavant, je m'attendais à devoir toujours ajouter le chemin de l'image de couverture dans le fichier de configuration de l'article. Quelque chose comme ceci :

```typescript
{
  "imageCover": "an-image.png",
}

```

Mais nous pourrions supposer que le nom de l'image sera `cover`. Le défi était l'extension. Cela peut être `.png`, `.jpg`, `.jpeg` ou `.gif`.

J'ai donc construit une fonction pour obtenir la bonne extension d'image. L'idée est de chercher l'image dans le dossier. Si elle existe, renvoyer l'extension.

J'ai commencé par la partie "existence".

```typescript
fs.existsSync(`${folder}/${fileName}.${extension}`);

```

Ici, j'utilise la fonction `existsSync` pour trouver le fichier. S'il existe dans le dossier, elle renvoie true. Sinon, false.

J'ai ajouté ce code dans une fonction :

```typescript
const existsFile = (folder: string, fileName: string) => (extension: string): boolean =>
  fs.existsSync(`${folder}/${fileName}.${extension}`);

```

Pourquoi ai-je procédé ainsi ?

En utilisant cette fonction, je dois passer le `folder`, le `fileName` et l' `extension`. Le `folder` et le `fileName` sont toujours les mêmes. La différence est l' `extension`.

Je pouvais donc construire une fonction en utilisant le currying. De cette façon, je peux construire différentes fonctions pour les mêmes `folder` et `fileName`. Comme ceci :

```typescript
const hasFileWithExtension = existsFile(examplesFolder, imageName);

hasFileWithExtension('jpeg'); // vrai ou faux
hasFileWithExtension('jpg'); // vrai ou faux
hasFileWithExtension('png'); // vrai ou faux
hasFileWithExtension('gif'); // vrai ou faux

```

La fonction complète ressemblerait à ceci :

```typescript
const getImageExtension = (): string => {
  const examplesFolder: string = resolve(__dirname, `../examples`);
  const imageName: string = 'cover';
  const hasFileWithExtension = existsFile(examplesFolder, imageName);

  if (hasFileWithExtension('jpeg')) {
    return 'jpeg';
  }

  if (hasFileWithExtension('jpg')) {
    return 'jpg';
  }

  if (hasFileWithExtension('png')) {
    return 'png';
  }

  return 'gif';
};

```

Mais je n'aimais pas cette chaîne de caractères codée en dur pour représenter l'extension de l'image. Les `enum` sont vraiment géniaux !

```typescript
enum ImageExtension {
  JPEG = 'jpeg',
  JPG = 'jpg',
  PNG = 'png',
  GIF = 'gif'
};

```

Et la fonction utilisant maintenant notre nouvel enum `ImageExtension` :

```typescript
const getImageExtension = (): string => {
  const examplesFolder: string = resolve(__dirname, `../examples`);
  const imageName: string = 'cover';
  const hasFileWithExtension = existsFile(examplesFolder, imageName);

  if (hasFileWithExtension(ImageExtension.JPEG)) {
    return ImageExtension.JPEG;
  }

  if (hasFileWithExtension(ImageExtension.JPG)) {
    return ImageExtension.JPG;
  }

  if (hasFileWithExtension(ImageExtension.PNG)) {
    return ImageExtension.PNG;
  }

  return ImageExtension.GIF;
};

```

Maintenant j'ai toutes les données pour remplir le template. Super !

Comme le HTML est prêt, je veux créer le fichier HTML réel avec ces données. J'ai essentiellement besoin d'obtenir le bon chemin, le HTML, et d'utiliser la fonction `writeFile` pour créer ce fichier.

Pour obtenir le chemin, je devais comprendre la structure de mon blog. Il organise les dossiers par année, par mois, par titre, et le fichier est nommé `index.html`.

Un exemple serait :

```bash
2020/04/publisher-a-tooling-to-blog-post-publishing/index.html

```

Au début, j'ai pensé à ajouter ces données au fichier de configuration de l'article. Ainsi, chaque fois, je devrais mettre à jour cet attribut pour obtenir le bon chemin.

Mais une autre idée intéressante était de déduire le chemin à partir de certaines données que nous avons déjà dans le fichier de configuration de l'article. Nous avons la `date` (ex: `"2020-04-21"`) et le `title` (ex: `"Publisher: tooling to automate blog post publishing"`).

À partir de la date, je peux obtenir l'année et le mois. À partir du titre, je peux générer le dossier de l'article. Le fichier `index.html` est toujours constant.

La chaîne ressemblerait à ceci :

```typescript
`${year}/${month}/${slugifiedTitle}`

```

Pour la date, c'est très simple. Je peux diviser par `-` et déstructurer :

```typescript
const [year, month]: string[] = date.split('-');

```

Pour le `slugifiedTitle`, j'ai construit une fonction :

```typescript
const slugify = (title: string): string =>
  title
    .trim()
    .toLowerCase()
    .replace(/[^\\w\\s]/gi, '')
    .replace(/[\\s]/g, '-');

```

Elle supprime les espaces au début et à la fin de la chaîne. Puis met la chaîne en minuscules. Ensuite, elle supprime tous les caractères spéciaux (ne garde que les caractères de mots et les espaces). Et enfin, elle remplace tous les espaces par un `-`.

La fonction complète ressemble à ceci :

```typescript
const buildNewArticleFolderPath = ({ title, date }: { title: string, date: string }): string => {
  const [year, month]: string[] = date.split('-');
  const slugifiedTitle: string = slugify(title);

  return resolve(__dirname, `../../${year}/${month}/${slugifiedTitle}`);
};

```

Cette fonction tente d'obtenir le dossier de l'article. Elle ne génère pas le nouveau fichier. C'est pourquoi je n'ai pas ajouté `/index.html` à la fin de la chaîne finale.

Pourquoi ai-je fait cela ? Parce qu'avant d'écrire le nouveau fichier, nous devons toujours créer le dossier. J'ai utilisé `mkdir` avec ce chemin de dossier pour le créer.

```typescript
const newArticleFolderPath: string = buildNewArticleFolderPath(articleConfig);
await mkdir(newArticleFolderPath, { recursive: true });

```

Et maintenant, je pouvais utiliser le dossier pour y créer le nouveau fichier d'article.

```typescript
const newArticlePath: string = `${newArticleFolderPath}/index.html`;
await writeFile(newArticlePath, article);

```

Une chose qui nous manque ici : comme j'ai ajouté l'image de couverture dans le dossier de configuration de l'article, je devais la copier et la coller au bon endroit.

Pour l'exemple `2020/04/publisher-a-tooling-to-blog-post-publishing/index.html`, l'image de couverture serait dans le dossier assets :

```bash
2020/04/publisher-a-tooling-to-blog-post-publishing/assets/cover.png

```

Pour ce faire, j'ai besoin de deux choses :

* créer un nouveau dossier `assets` avec `mkdir`
* copier le fichier image et le coller dans le nouveau dossier avec `copyFile`

Pour créer le nouveau dossier, j'ai juste besoin du chemin du dossier. Pour copier et coller le fichier image, j'ai besoin du chemin actuel de l'image et du chemin de l'image de l'article.

Pour le dossier, comme j'ai le `newArticleFolderPath`, j'ai juste besoin de concaténer ce chemin au dossier assets.

```typescript
const assetsFolder: string = `${newArticleFolderPath}/assets`;

```

Pour le chemin actuel de l'image, j'ai le `imageCoverFileName` avec la bonne extension. J'ai juste besoin d'obtenir le chemin de l'image de couverture :

```typescript
const imageCoverExamplePath: string = resolve(__dirname, `../examples/${imageCoverFileName}`);

```

Pour obtenir le futur chemin de l'image, je dois concaténer le chemin de l'image de couverture et le nom du fichier image :

```typescript
const imageCoverPath: string = `${assetsFolder}/${imageCoverFileName}`;

```

Avec toutes ces données, je peux créer le nouveau dossier :

```typescript
await mkdir(assetsFolder, { recursive: true });

```

Et copier-coller le fichier de l'image de couverture :

```typescript
await copyFile(imageCoverExamplePath, imageCoverPath);

```

Alors que j'implémentais cette partie sur les chemins (`paths`), j'ai vu que je pouvais tous les regrouper dans une fonction `buildPaths`.

```typescript
const buildPaths = (newArticleFolderPath: string): ArticlePaths => {
  const imageExtension: string = getImageExtension();
  const imageCoverFileName: string = `cover.${imageExtension}`;
  const newArticlePath: string = `${newArticleFolderPath}/index.html`;
  const imageCoverExamplePath: string = resolve(__dirname, `../examples/${imageCoverFileName}`);
  const assetsFolder: string = `${newArticleFolderPath}/assets`;
  const imageCoverPath: string = `${assetsFolder}/${imageCoverFileName}`;

  return {
    newArticlePath,
    imageCoverExamplePath,
    imageCoverPath,
    assetsFolder,
    imageCoverFileName
  };
};

```

J'ai également créé le type `ArticlePaths` :

```typescript
type ArticlePaths = {
  newArticlePath: string;
  imageCoverExamplePath: string;
  imageCoverPath: string;
  assetsFolder: string;
  imageCoverFileName: string;
};

```

Et je pouvais utiliser la fonction pour obtenir toutes les données de chemin dont j'avais besoin :

```typescript
const {
  newArticlePath,
  imageCoverExamplePath,
  imageCoverPath,
  assetsFolder,
  imageCoverFileName
}: ArticlePaths = buildPaths(newArticleFolderPath);

```

La dernière partie de l'algorithme maintenant ! Je voulais valider rapidement l'article créé. Et si je pouvais ouvrir l'article créé dans un onglet de navigateur ? Ce serait génial !

C'est ce que j'ai fait :

```typescript
await open(newArticlePath);

```

Ici, j'utilise la bibliothèque `open` pour simuler la commande d'ouverture du terminal.

Et voilà !

## Ce que j'ai appris

Ce projet a été très amusant ! J'ai appris des choses intéressantes au cours de ce processus. Je veux les lister ici :

* Comme je suis en train d'[apprendre TypeScript](https://leandrotk.github.io/tk/2020/04/typescript-learnings/index.html), je voulais valider rapidement le code que j'écrivais. J'ai donc configuré `nodemon` pour compiler et exécuter le code à chaque sauvegarde de fichier. C'est génial de rendre le processus de développement si dynamique.
* J'ai essayé d'utiliser les nouvelles `promises` de `fs` de Node : `readFile`, `mkdir`, `writeFile`, et `copyFile`. C'est au niveau `Stability: 2`.
* J'ai fait beaucoup de [currying](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html) pour certaines fonctions afin de les rendre réutilisables.
* Les Enums et les [Types](https://leandrotk.github.io/tk/2020/04/typescript-learnings-002-type-system/index.html) sont de bons moyens de rendre l'état cohérent en TypeScript, mais aussi de fournir une bonne représentation et documentation de toutes les données du projet. Les [contrats de données](https://leandrotk.github.io/tk/2020/04/thinking-in-data-contracts/index.html) sont une chose vraiment sympa.
* L'état d'esprit orienté outillage. C'est l'une des choses que j'aime vraiment dans la programmation. Construire des outils pour automatiser les tâches répétitives et faciliter la vie.

J'espère que cette lecture vous a plu ! Continuez à apprendre et à coder !

Cet article a été initialement publié [sur mon blog](https://leandrotk.github.io/tk/2020/04/publisher-a-tooling-to-automate-the-process-to-publish-my-blog-posts/index.html).

Mon [Twitter](https://twitter.com/leandrotk_) et mon [GitHub](https://github.com/leandrotk/).

## Ressources

* [Outil Publisher : code source](https://github.com/leandrotk/publisher)
* [Penser en contrats de données](https://leandrotk.github.io/tk/2020/04/thinking-in-data-contracts/index.html)
* [Apprentissages TypeScript](https://leandrotk.github.io/tk/2020/04/typescript-learnings/index.html)
* [Closures, Currying et Abstractions Cool](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html)
* [Apprendre React en construisant une application](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)