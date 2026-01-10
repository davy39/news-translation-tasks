---
title: Comment utiliser Rust + WebAssembly pour effectuer du Machine Learning et de
  la Visualisation de Données sans serveur dans le Cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T16:26:16.000Z'
originalURL: https://freecodecamp.org/news/rust-webassembly-serverless-tencent-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/origin_img_6f483a12-6885-4499-b35b-2e23c949ef8g.PNG
tags:
- name: Machine Learning
  slug: machine-learning
- name: Rust
  slug: rust
- name: WebAssembly
  slug: webassembly
seo_title: Comment utiliser Rust + WebAssembly pour effectuer du Machine Learning
  et de la Visualisation de Données sans serveur dans le Cloud
seo_desc: 'The Tencent Serverless Cloud Function Custom Runtime allows developers
  to write serverless functions in any programming language.

  In this article, we make the case for serverless functions in Rust and WebAssembly,
  and demonstrate their use in machine...'
---

Le Tencent Serverless Cloud Function Custom Runtime permet aux développeurs d'écrire des fonctions sans serveur dans n'importe quel langage de programmation.

Dans cet article, nous faisons le cas des fonctions sans serveur en Rust et WebAssembly, et démontrons leur utilisation dans le machine learning et la visualisation.

Vous apprendrez comment créer une fonction simple pour le machine learning et déployer un site web sans serveur autour de celle-ci, gratuitement (sauf si un million de personnes l'utilisent !).

## D'abord, qu'est-ce que Tencent ?

Tencent est la plus grande entreprise Internet en dehors des États-Unis avec plus d'un milliard d'utilisateurs actifs quotidiens. Son bras de cloud computing, [Tencent Cloud](https://cloud.tencent.com/?lang=en), est classé parmi les cinq premiers fournisseurs de cloud dans le monde par part de marché.

Si vous souhaitez atteindre le marché mondial avec vos services cloud, Tencent Cloud devrait être en haut de votre liste.

Tencent Cloud est également un innovateur de premier plan dans le domaine du computing sans serveur avec des offres solides allant des runtimes FaaS (Function as a Service), des déclencheurs, des connecteurs et des outils de développement.

Les [Tencent Serverless Cloud Functions (SCF)](https://intl.cloud.tencent.com/document/product/583) supportent déjà 10+ langages de programmation et frameworks de runtime. Mais le SCF Custom Runtime récemment publié a fait un pas de plus. Le SCF peut désormais supporter des fonctions écrites dans n'importe quel langage de programmation.

Dans cet article, je vais couvrir comment exécuter des fonctions WebAssembly, écrites en Rust, dans le SCF.

### Ce que nous allons couvrir dans cet article

Nous allons d'abord passer en revue les concepts de base. Ensuite, nous allons examiner un exemple complet mais simple de hello world pour déployer votre première fonction sans serveur WebAssembly.

Enfin, nous allons faire quelque chose d'utile avec un exemple de machine learning as a service (MLaaS) qui prend des données et retourne le modèle ajusté et la visualisation au format SVG.

[Voici l'application finale](https://www.secondstate.io/demo/2020-tencentcloud.html) que vous allez créer à la fin de ce tutoriel. Elle est complètement "serverless" et entraîne des coûts lorsque les gens l'utilisent.

L'interface HTML et JavaScript peut être hébergée sur n'importe quel ordinateur, y compris votre ordinateur portable, et la [fonction backend](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca) pour effectuer le machine learning et le dessin SVG est sur Tencent Cloud Serverless.

## Pourquoi WebAssembly et Rust

Les fonctions sans serveur traditionnelles sont basées sur des frameworks lourds. Les développeurs doivent écrire des fonctions dans des frameworks d'application spécifiques, tels que JavaScript dans Node.js ou Python Boto, etc.

Le Tencent Cloud SCF Custom Runtime brise ce moule et permet aux développeurs d'écrire des fonctions sans serveur dans n'importe quel langage.

Pour démontrer ce point, il fournit des exemples pour une [fonction basée sur un script Bash](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-shellDemo), une [fonction TypeScript basée sur Deno](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-denoDemo), et une [fonction binaire native basée sur Rust](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-rustDemo). Cela nous permet de créer et de déployer des fonctions sans serveur basées sur WebAssembly sur Tencent Cloud.

Pourquoi voulons-nous faire cela ? Voici [quelques raisons](https://www.secondstate.io/articles/why-webassembly-server/).

* WebAssembly est conçu pour la performance. [Les fonctions WebAssembly pourraient être 10x plus rapides](https://www.secondstate.io/articles/performance-rust-wasm/) que des programmes comparables écrits en JavaScript ou Python.

* Les fonctions WebAssembly sont portables. Bien qu'il soit possible d'exécuter des binaires natifs sur SCF Custom Runtime, ces binaires doivent être compilés pour l'environnement exact du système d'exploitation pour Custom Runtime. Il s'agit actuellement de CentOS 7.6 sur des CPU X86, et pourrait changer plus tard. Les fonctions WebAssembly sont portables et très faciles à déployer et à gérer comme nous allons le voir.

* Les fonctions WebAssembly sont sûres. Il est connu que même avec Docker, les applications binaires natives pourraient violer le conteneur. Puisque votre application dépend probablement de nombreuses bibliothèques tierces, le risque de code malveillant dans vos dépendances est réel. WebAssembly, avec son [modèle de sécurité basé sur les capacités](https://www.secondstate.io/articles/wasi-access-system-resources/), offre une meilleure protection d'exécution pour votre code.

* Bien que WebAssembly soit agnostique aux langages de programmation, Rust, AssemblyScript (un sous-ensemble de TypeScript), C/C++, et Go sont parmi les meilleurs langages pour écrire des fonctions WebAssembly. En particulier, Rust est un langage de programmation populaire et en forte croissance avec une communauté passionnée. Il nous permet d'écrire des fonctions hautement efficaces, tout en étant sûres en mémoire.

Enfin, programmer et déployer des fonctions WebAssembly sur Tencent Cloud est en fait assez facile. Vous pouvez le faire en une heure. Commençons.

## Prérequis

Tout d'abord, inscrivez-vous pour un [compte Tencent Cloud](https://cloud.tencent.com/?lang=en). Pour la plupart des projets de développement et personnels, vous pouvez probablement rester dans son [niveau gratuit](https://intl.cloud.tencent.com/document/product/583/12282) de service.

Ensuite, sur votre ordinateur de développement local ou conteneur Docker, assurez-vous d'avoir Rust et l'outil [ssvmup](https://www.secondstate.io/articles/ssvmup/) installés. La chaîne d'outils ssvmup compile et optimise les programmes Rust en bytecode WebAssembly.

Utilisez simplement les commandes suivantes pour installer les deux. Ou vous pouvez vous référer à [ce guide](https://www.secondstate.io/articles/ssvmup/).

```bash
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
$ source $HOME/.cargo/env
... ...
$ curl https://raw.githubusercontent.com/second-state/ssvmup/master/installer/init.sh -sSf | sh
```

La fonction WebAssembly est exécutée dans la [Second State VM](https://www.secondstate.io/ssvm/) — une [VM WebAssembly haute performance](https://www.secondstate.io/articles/ssvm-performance/) optimisée pour les cas d'utilisation et applications côté serveur.

## Bonjour, le monde

Pour commencer avec votre première fonction Rust et WebAssembly sur Tencent Cloud, nous vous encourageons à cloner ou [forker ce dépôt de modèle](https://github.com/second-state/ssvm-tencent-starter) sur Github et à l'utiliser comme base pour votre propre application.

La fonction Rust dans [main.rs](https://github.com/second-state/ssvm-tencent-starter/blob/master/src/main.rs) est la fonction sans serveur que nous allons déployer sur SCF. Comme vous pouvez le voir à partir de son code source, elle lit l'entrée de la fonction à partir de `STDIN`, puis utilise la macro `println!` pour envoyer les résultats à `STDOUT`.

```rust
use std::io::{self, Read};
use serde::Deserialize;

fn main() {    
    let mut buffer = String::new();    
    io::stdin().read_to_string(&mut buffer).expect("Erreur de lecture depuis STDIN");    
    let obj: FaasInput = serde_json::from_str(&buffer).unwrap();    
    let key1 = &(obj.key1);    
    let key2 = &(obj.key2);    
    println!("Bonjour ! {}, {}", key1, key2);
}

#[derive(Deserialize, Debug)]
struct FaasInput {    
    key1: String,    
    key2: String
}
```

La fonction Rust `main()` utilise la bibliothèque `serde` pour analyser une chaîne JSON à partir de `STDIN`.

Le JSON ressemble à ce qui suit. La raison pour laquelle nous écrivons la fonction de cette manière est que c'est le modèle JSON hello world intégré que SCF utilise pour tester les fonctions déployées.

```json
{  
    "key1": "valeur de test 1",  
    "key2": "valeur de test 2"
}
```

La fonction extrait les valeurs `key1` et `key2` et génère le message de bonjour suivant vers `STDOUT`.

```text
Bonjour ! valeur de test 1, valeur de test 2
```

Mais, comment une requête web à cette fonction est-elle traduite en `STDIN` ? Et comment la réponse de la fonction dans `STDOUT` est-elle traduite en une réponse HTTP ?

Cela est fait par l'infrastructure SCF Custom Runtime et le programme [bootstrap](https://github.com/second-state/ssvm-tencent-starter/blob/master/cloud/bootstrap) dans notre modèle.

Comme vous pouvez le voir, le programme [bootstrap](https://github.com/second-state/ssvm-tencent-starter/blob/master/cloud/bootstrap) est simplement un programme shell bash qui interroge continuellement le SCF pour les requêtes entrantes. Il traduit la requête entrante en `STDIN` et appelle la fonction WebAssembly via le SSVM. Il prend ensuite la sortie `STDOUT` et la renvoie dans SCF en tant que réponse de la fonction.

Vous n'avez pas besoin de modifier le programme bootstrap si vous utilisez notre modèle.

Maintenant, vous pouvez compiler la fonction Rust en bytecode WebAssembly avec ssvmup, puis créer un fichier zip pour le déploiement sur le Tencent Cloud SCF Custom Runtime.

```bash
$ ssvmup build
```

[Suivez les instructions et les captures d'écran](https://github.com/second-state/ssvm-tencent-starter/blob/master/README.md) pour déployer et tester le fichier `hello.zip` ci-dessus. Vous avez maintenant déployé avec succès une fonction sans serveur WebAssembly !

Ensuite, créons un service web utile à partir d'une fonction Rust.

## Machine Learning as a Service

Pour cet exemple, nous avons choisi une tâche de machine learning intensivement calculatoire pour démontrer la performance d'une fonction Rust WebAssembly.

La fonction sans serveur prend une chaîne d'entrée de nombres délimités par des virgules qui représentent un ensemble de points sur un plan 2-D. Le format des données d'entrée est `x1,y1,x2,y2,...`.

La fonction analyse les données et calcule deux vecteurs propres qui indiquent les directions de la plus grande variance dans les données.

Les vecteurs propres donnent aux scientifiques des données des indices sur les facteurs sous-jacents qui entraînent la variance dans les données. Cela s'appelle l'analyse en composantes principales (PCA).

Notre fonction crée un graphique SVG avec les points de données d'entrée ainsi que les vecteurs propres tracés sur celui-ci. Elle génère le graphique SVG en texte XML.

Pour commencer avec cet exemple, vous devriez [cloner ou forker ce dépôt](https://github.com/second-state/wasm-learning). Le projet se trouve dans le dossier [tencentcloud/ssvm/pca](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca). Vous pouvez également copier le contenu du [Cargo.toml](https://github.com/second-state/wasm-learning/blob/master/tencentcloud/ssvm/pca/Cargo.toml) et du [src/](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca/src) dans votre modèle hello world.

Si vous faites cela, assurez-vous de modifier le [Cargo.toml](https://github.com/second-state/wasm-learning/blob/master/tencentcloud/ssvm/pca/Cargo.toml) pour pointer vers le dossier correct du code source pour notre bibliothèque Rust de machine learning.

Je ne vais pas entrer dans les détails du code source Rust pour PCA ou la génération SVG dans ce tutoriel car ils impliquent une quantité importante de code de calcul. Si vous êtes intéressé, vous pouvez consulter plus de ressources à la fin de cet article.

Vous pouvez [suivre le même processus](https://github.com/second-state/ssvm-tencent-starter/blob/master/README.md) que dans l'exemple hello world. Utilisez ssvmup pour créer un package `pca.zip` et le déployer sur Tencent Cloud SCF Custom Runtime.

Ensuite, nous voulons associer la fonction déployée à une passerelle API web afin qu'elle puisse être invoquée à partir d'une requête web HTTP ou HTTPS. Faites cela à partir de l'onglet Gestion des déclencheurs dans la console web pour SCF. [Voir les instructions et les captures d'écran ici](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca#create-a-web-service).

La console API transforme une requête HTTP en une entrée JSON pour la fonction sans serveur. Par exemple, voici une requête HTTP POST à l'URL de la passerelle API. Nous mettons les points de données délimités par des virgules du fichier `iris.csv` dans le corps de la requête POST.

```bash
$ curl -d @iris.csv -X POST https://service-m9pxktbc-1302315972.hk.apigw.tencentcs.com/release/PCASVG
```

La passerelle API transmet le JSON suivant à l'entrée STDIN de la fonction Rust. Le corps de la requête POST est maintenant l'attribut body dans le JSON.

```json
{
  "body": "3.5,0.2,3,0.2,...",
  "headerParameters": {},
  "headers": {
    "accept": "/",
    "content-length": "11",
    "content-type": "application/x-www-form-urlencoded",
    "host": "service-aj0plx8u-1302315972.hk.apigw.tencentcs.com",
    "user-agent": "curl/7.54.0",
    "x-anonymous-consumer": "true",
    "x-api-requestid": "e3123014742e7dd79f0652968bf1f62e",
    "x-b3-traceid": "e3123014742e7dd79f0652968bf1f62e",
    "x-qualifier": "$DEFAULT"
  },
  "httpMethod": "POST",
  "path": "/my_hk",
  "pathParameters": {},
  "queryString": {},
  "queryStringParameters": {},
  "requestContext": {
    "httpMethod": "ANY",
    "identity": {},
    "path": "/my_hk",
    "serviceId": "service-aj0plx8u",
    "sourceIp": "136.49.211.114",
    "stage": "release"
  }
}
```

La fonction Rust analyse les données dans le corps, effectue PCA, et génère le graphique SVG. Elle imprime le contenu SVG vers STDOUT, qui est récupéré par la passerelle API et renvoyé en tant que réponse HTTP.

> Pour utiliser cette URL de passerelle API dans les requêtes AJAX, vous devez également configurer la passerelle Tencent Cloud pour accepter les requêtes web CORS. [Consultez ce guide](https://www.secondstate.io/articles/tencentcloud-api-gateway-cors/) sur la façon de le faire.

L'exemple HTML JavaScript ci-dessous montre comment utiliser cette fonction sans serveur dans une page web.

Il prend les données CSV du champ `textarea` avec l'ID `csv_data`, fait une requête AJAX HTTP POST à la fonction sans serveur, puis place la valeur de retour, qui est un graphique SVG, dans un élément HTML avec l'ID `svg_img`. [Voir la démonstration en direct ici](https://www.secondstate.io/demo/2020-tencentcloud.html).

```javascript
$.ajax({
  method: "POST",
  url: "https://service-m9pxktbc-1302315972.hk.apigw.tencentcs.com/release/PCASVG",
  data: $('#csv_data').val(),
  dataType: "text"
}).done(function(data) {
  $('#svg_img').html(data);
})
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/tencentcloud_pca_webapp.png align="left")

*L'application web sans serveur en action.*

## Prochaines étapes

Le Tencent SCF Custom Runtime est un environnement sans serveur très puissant. Il fournit un environnement Linux générique pour toute fonction d'application que vous souhaitez écrire, ainsi que des interfaces web standard pour interagir avec l'entrée et la sortie de la fonction. Cela vaut définitivement la peine d'essayer.

Comme discuté dans l'article, nous croyons que Rust et WebAssembly offrent une [pile haute performance, sûre, portable et future-proof](https://www.secondstate.io/articles/why-webassembly-server/) pour les fonctions sans serveur. Rust et WebAssembly avec SCF Custom Runtime, c'est l'avenir !

## Ressources

* En savoir plus sur [pourquoi utiliser WebAssembly côté serveur](https://www.secondstate.io/articles/why-webassembly-server/)

* En savoir plus sur [Tencent Serverless Cloud Functions](https://intl.cloud.tencent.com/document/product/583)

* [En savoir plus sur les algorithmes de machine learning](https://www.freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today/)

* [Commencer avec Rust](https://www.rust-lang.org/learn/get-started)

* [Algorithmes de machine learning en Rust et WebAssembly](https://github.com/second-state/wasm-learning/tree/master/nodejs/algos)

* [Commencer avec les fonctions Rust dans Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/)

* En savoir plus sur la [Second State WebAssembly VM](https://www.secondstate.io/ssvm/)

[Abonnez-vous à notre newsletter](https://webassemblytoday.substack.com/) et restez en contact. Bon codage !