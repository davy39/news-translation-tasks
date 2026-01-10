---
title: Comment utiliser fnm – Fast Node Manager
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-06-09T15:30:55.000Z'
originalURL: https://freecodecamp.org/news/fnm-fast-node-manager
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/rocket-fnm.jpg
tags:
- name: node
  slug: node
seo_title: Comment utiliser fnm – Fast Node Manager
seo_desc: "If you've been working with Node for a while, you will most likely discover\
  \ that your projects – or one you're working on – are written for an older version\
  \ of Node. That means they won't work as expected with the latest version. \nIn\
  \ that case, a Nod..."
---

Si vous travaillez avec Node depuis un certain temps, il est probable que vous découvrirez que vos projets – ou celui sur lequel vous travaillez – sont écrits pour une version plus ancienne de Node. Cela signifie qu'ils ne fonctionneront pas comme prévu avec la dernière version. 

Dans ce cas, un gestionnaire de versions de Node peut vous aider à gagner un temps précieux en installant et en basculant entre différentes versions de Node. 

Aujourd'hui, je vais vous présenter `fnm` (Fast Node Manager), un gestionnaire de versions de Node, écrit en Rust avec simplicité et rapidité à l'esprit. `fnm` offre également une compatibilité multiplateforme.

  <h2 id="toc-heading" style="border-bottom: 2px solid cornflowerblue; margin-bottom: 0px; font-weight: normal;">Table des matières</h2>
  <ul style="padding-left: 0px; padding-block: 0.5rem; list-style-type: none; margin: 0px;">
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>
      <a href="#installation-pour-systeme-linux-et-shell-zsh">Installation pour système Linux et shell <code>zsh</code></a>
      <ul style="padding-left: 1.3em; list-style-type: none;">
        <li><span style="margin-right:.6rem;color:#66a62e;font-weight:700">1.1</span><a href="#configuration-du-shell">Configuration du shell</a></li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.2</span>
          <a href="#comment-installer-le-script-de-completion">Comment installer le script de complétion</a>
        </li>
      </ul>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>
      <a href="#utilisation-courante-de-fnm">Utilisation courante de <code>fnm</code>
      </a>
      <ul style="padding-left: 1.3em; list-style-type: none;">
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.1</span>
          <a href="#comment-lister-toutes-les-versions-distantes-de-node">Comment lister toutes les versions distantes de Node</a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.2</span>
          <a href="#comment-installer-plusieurs-versions-de-node">Comment installer plusieurs versions de Node</a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.3</span>
          <a href="#comment-definir-des-alias-pour-une-version-de-node">Comment définir des alias pour une version de Node</a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.4</span>
          <a href="#comment-utiliser-une-version-particuliere-de-node">Comment utiliser une version particulière de Node</a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.5</span>
          <a href="#comment-attacher-une-version-de-node-a-un-projet">Comment attacher une version de Node à un projet</a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.6</span>
          <a href="#comment-desinstaller-une-version-de-node">Comment désinstaller une version de Node</a>
        </li>
      </ul>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>
        <a href="#comment-supprimer-fnm">Comment supprimer <code>fnm</code></a>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>
      <a href="#resume">Résumé</a>
    </li>
  </ul>

<h2 id="installation-pour-systeme-linux-et-shell-zsh"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>Installation pour système Linux et shell zsh
<a href="#installation-pour-systeme-linux-et-shell-zsh" aria-label="Anchor link for: &quot;Installation pour système Linux et shell zsh
&quot;" style="text-decoration: none;">§</a></h2>

Ici, je ne couvrirai que l'installation de `fnm` pour les systèmes Linux et le shell `zsh`. Voir la [documentation](https://github.com/Schniz/fnm) pour les instructions d'installation sur d'autres plateformes et shells.

Assurez-vous d'abord que `curl` est installé sur votre système. Ensuite, exécutez la commande suivante pour installer `fnm` :

```zsh
curl -fsSL https://fnm.vercel.app/install | bash -s -- --skip-shell
```

Cela installera `fnm` dans votre répertoire `$HOME/.fnm/`.

La **mise à jour** de `fnm` est la même que de **l'installer à nouveau** avec la commande ci-dessus.

<h3 id="configuration-du-shell">
  <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.1</span>Configuration du shell <a href="#configuration-du-shell" aria-label="Anchor link for: &quot;Configuration du shell
&quot;" style="text-decoration: none;">§</a>
</h3>

Il y a une étape importante supplémentaire. Ajoutez simplement ce qui suit à votre fichier `.zshrc` :

```zsh
# fnm
export PATH=/home/$USER/.fnm:$PATH
eval "$(fnm env --use-on-cd --version-file-strategy=recursive)"
```

<h3 id="comment-installer-le-script-de-completion"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.2</span>Comment installer le script de complétion
<a href="#comment-installer-le-script-de-completion" aria-label="Anchor link for: &quot;Comment installer le script de complétion
&quot;" style="text-decoration: none;">§</a></h3>

L'installation du script de complétion est **optionnelle**. Si vous vous demandez quel est le rôle de cette étape, voici ce qu'elle fait : elle tente de compléter automatiquement la commande partielle que vous tapez concernant fnm lorsque vous appuyez sur la touche TAB. Par exemple, si vous tapez `fnm ls-` et appuyez sur la touche TAB, il complétera automatiquement à `fnm ls-remote`.

`fnm` est livré avec tous les codes de complétion pour différents shells avec son binaire. Vous devrez coller ce code dans un fichier nommé `_fnm` dans un répertoire spécifié dans la variable d'environnement `FPATH` :

```zsh
fnm completions --shell zsh > <un_repertoire_fpath>/_fnm
```

Voir la sortie de `echo $FPATH` pour obtenir tous les répertoires possibles et remplacer `<un_repertoire_fpath>` par un répertoire réel. Il est recommandé d'utiliser un chemin local utilisateur. Si aucun chemin de ce type n'existe, vous pouvez en définir un dans votre `.zshrc` en ajoutant cette ligne :

```zsh
fpath=(/home/$USER/votre/chemin/prefere/ici $fpath)
```

<h2 id="utilisation-courante-de-fnm"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>Utilisation courante de <code>fnm</code>
<a href="#utilisation-courante-de-fnm" aria-label="Anchor link for: &quot;Utilisation courante de fnm
&quot;" style="text-decoration: none;">§</a></h2>

<h3 id="comment-lister-toutes-les-versions-distantes-de-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.1</span>Comment lister toutes les versions distantes de Node
<a href="#comment-lister-toutes-les-versions-distantes-de-node" aria-label="Anchor link for: &quot;Comment lister toutes les versions distantes de Node
&quot;" style="text-decoration: none;">§</a></h3>

Pour voir toutes les différentes versions de Node que vous pouvez installer, exécutez :

```zsh
fnm ls-remote
```

Cela imprimera toutes les versions comme ci-dessous :

```
.
.
.
v16.15.0 (Gallium)
v16.15.1 (Gallium)
v17.0.0
v17.0.1
v17.1.0
v17.2.0
v17.3.0
v17.3.1
v17.4.0
v17.5.0
v17.6.0
v17.7.0
v17.7.1
v17.7.2
v17.8.0
v17.9.0
v17.9.1
v18.0.0
v18.1.0
v18.2.0
v18.3.0
```

<h3 id="comment-installer-plusieurs-versions-de-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.2</span>Comment installer plusieurs versions de Node
<a href="#comment-installer-plusieurs-versions-de-node" aria-label="Anchor link for: &quot;Comment installer plusieurs versions de Node
&quot;" style="text-decoration: none;">§</a></h3>

Installons Node de la version `v18.3.0` :

```zsh
fnm install v18.3.0
```

Pour installer Node de la dernière version LTS, vous pouvez utiliser l'option `--lts`. Exécutez donc la commande suivante pour l'installer également :

```
fnm install --lts
```

`fnm` supporte également la correspondance partielle de version. `fnm` devine la dernière version disponible à partir de votre entrée partielle. Par exemple, si vous faites simplement :

```
fnm install 17
```

Cela installera Node de la version `v17.9.1`, qui est la dernière version disponible commençant par `17`. Expérimentez donc avec la commande ci-dessus.

Vérifions votre version de Node en entrant `node --version` dans votre terminal. Notez que la première installée est utilisée par défaut.

Avant de voir comment commencer à utiliser une version installée différente de Node, voyons comment vous pouvez définir un alias (nom) pour une version afin de pouvoir vous y référer facilement.

<h3 id="comment-definir-des-alias-pour-une-version-de-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.3</span>Comment définir des alias pour une version de Node
<a href="#comment-definir-des-alias-pour-une-version-de-node" aria-label="Anchor link for: &quot;Comment définir des alias pour une version de Node
&quot;" style="text-decoration: none;">§</a></h3>

Par défaut, la première version de Node que vous installez en utilisant `fnm` reçoit l'alias `default`.

La syntaxe pour définir un alias pour une version est :

```
fnm alias <version> <nom>
```

Si vous souhaitez définir l'alias `default`, il existe un raccourci :

```
fnm default <version>
```

Vous pouvez également définir plusieurs alias pour une version.

La syntaxe pour supprimer un alias est :

```
fnm unalias <nom>
```

<h3 id="comment-utiliser-une-version-particuliere-de-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.4</span>Comment utiliser une version particulière de Node
<a href="#comment-utiliser-une-version-particuliere-de-node" aria-label="Anchor link for: &quot;Comment utiliser une version particulière de Node
&quot;" style="text-decoration: none;">§</a></h3>

Vous pouvez utiliser une version particulière de Node en utilisant la sous-commande `use` :

```zsh
fnm use 16

```

Pour vérifier la version actuelle de Node, exécutez simplement :

```
fnm current

```

Pour lister toutes les versions de Node que vous avez installées avec `fnm`, exécutez :

```
fnm ls

```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/fnm-ls-1.png)

Notez que vous pouvez contourner `fnm` et utiliser l'installation système de Node sur votre système (si elle existe) en utilisant `system` :

```zsh
fnm use system
```

<h3 id="comment-attacher-une-version-de-node-a-un-projet"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.5</span>Comment attacher une version de Node à un projet
<a href="#comment-attacher-une-version-de-node-a-un-projet" aria-label="Anchor link for: &quot;Comment attacher une version de Node à un projet
&quot;" style="text-decoration: none;">§</a></h3>

Vous pouvez créer un fichier [`.node-version`](https://github.com/shadowspawn/node-version-usage) à la racine de votre projet et y écrire simplement la version souhaitée de Node pour ce projet afin d'attacher une version de Node à celui-ci :

```zsh
echo 'v18.3.0' > .node-version

```

`fnm` respecte ce fichier. Donc, si vous êtes dans ce répertoire, vous pouvez simplement utiliser `fnm install` ou `fnm use` pour installer ou utiliser cette version.

`fnm` respecte également le fichier `.nvmrc` (il est similaire au fichier `.node-version` mais provient de `nvm`). Donc, si vous avez utilisé `nvm` auparavant, vous aurez une transition en douceur vers `fnm`.

`fnm` peut utiliser ces fichiers de configuration pour détecter la version de Node et même commencer à l'utiliser automatiquement lors de l'utilisation de `cd`, ce qui est vraiment pratique dans la plupart des cas. J'ai donc déjà activé ces fonctionnalités dans la configuration du shell en ajoutant les indicateurs suivants à la commande `fnm env` :

* **`--use-on-cd`** : Cet indicateur indique à `fnm` que lorsque vous utilisez `cd` pour entrer dans un répertoire racine de projet, il doit automatiquement utiliser la version de Node spécifiée dans `.node-version` (ou `.nvmrc`). Cool, n'est-ce pas ?
* **`--version-file-strategy=recursive`** : Cet indicateur et sa valeur `recursive` indiquent essentiellement à `fnm` d'utiliser la version de Node spécifiée dans `.node-version` (ou `.nvmrc`) même lorsque vous êtes dans un répertoire imbriqué et utilisez la sous-commande `use` ou `install` sans version. Il indique également à `fnm` d'utiliser la version de Node aliasée à `default` lorsque vous êtes en dehors de tout répertoire de projet de ce type et utilisez la sous-commande `use` sans version. L'utilisation de cet indicateur avec `--use-on-cd` vous permet d'avoir la magie d'utiliser ou d'installer automatiquement la version pertinente de Node (comme décrit ici) lorsque vous entrez et sortez profondément de ces répertoires de projet.

Si ces fonctionnalités interfèrent avec votre flux de travail, vous pouvez supprimer ces indicateurs à tout moment dans votre configuration de shell pour les désactiver.

<h3 id="comment-desinstaller-une-version-de-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.6</span>Comment désinstaller une version de Node
<a href="#comment-desinstaller-une-version-de-node" aria-label="Anchor link for: &quot;Comment désinstaller une version de Node
&quot;" style="text-decoration: none;">§</a></h3>

Désinstaller une version de Node est très similaire à son installation. Vous devez simplement utiliser la sous-commande `uninstall` au lieu de `install`. C'est tout.

<h2 id="comment-supprimer-fnm"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>Comment supprimer <code>fnm</code>
<a href="#comment-supprimer-fnm" aria-label="Anchor link for: &quot;Comment supprimer fnm
&quot;" style="text-decoration: none;">§</a></h2>

Supprimer `fnm` est aussi simple que de supprimer le répertoire `.fnm` de votre `home` et de supprimer sa configuration spécifique que vous avez ajoutée dans votre fichier de configuration de shell. N'oubliez pas de supprimer également le script de complétion.

<h2 id="resume"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>Résumé
<a href="#resume" aria-label="Anchor link for: &quot;Résumé
&quot;" style="text-decoration: none;">§</a></h2>

Voici un résumé de toutes les commandes que nous avons discutées dans cet article :

```zsh
# Lister toutes les versions distantes
fnm ls-remote

# Lister toutes les versions installées
fnm ls

# Installation
fnm install <version>

# Désinstallation
fnm uninstall <version>

# Installer la dernière version LTS de Node
fnm install --lts

# Définir un alias
fnm alias <version> <nom>

# Raccourci pour définir 'default' comme alias
fnm default <version>

# Supprimer un alias
fnm unalias <nom>

# Utiliser une version particulière de Node
fnm use <version>

# Afficher la version de Node actuellement utilisée
fnm current

```

De plus, si vous avez besoin d'aide rapide, `fnm` dispose d'une aide intégrée que vous pouvez obtenir à tout moment directement depuis votre terminal comme suit :

* Aide pour la commande `fnm` : `fnm --help`
* Aide pour toute sous-commande : `fnm <sous-commande> --help`

Si vous aimez `fnm`, n'oubliez pas de lui donner une étoile sur [GitHub](https://github.com/Schniz/fnm). Je pense qu'il mérite plus d'étoiles qu'il n'en a actuellement.

Merci d'avoir lu ! Si vous le souhaitez, vous pouvez consulter mon [site web](https://www.ashutoshbiswas.dev/) et me suivre sur [Twitter](https://twitter.com/ashutoshbw) et [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/).

Bon codage 😄