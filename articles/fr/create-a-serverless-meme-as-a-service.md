---
title: Comment créer un Meme-as-a-Service sans serveur
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2021-02-25T15:54:07.000Z'
originalURL: https://freecodecamp.org/news/create-a-serverless-meme-as-a-service
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/meme1.png
tags: []
seo_title: Comment créer un Meme-as-a-Service sans serveur
seo_desc: 'The “meme economy” is apparently the next big thing. It is a natural extension
  of the Internet’s “attention economy”. Among many others, even Elon Musk is doing
  it. By some estimate, the meme economy is already worth $250 million USD.


  The meme econo...'
---

L'économie des memes est apparemment la prochaine grande tendance. C'est une extension naturelle de l'économie de l'attention d'Internet. Parmi [beaucoup d'autres](https://www.bloomberg.com/press-releases/2021-02-23/sino-global-shipping-partners-up-with-cybermiles-blockchain-to-explore-non-fungible-token-business), même [Elon Musk s'y met](https://www.axios.com/meme-economy-tesla-elon-musk-c1e9c225-d8e2-4953-a591-0a29dacf2d4a.html). Selon certaines estimations, l'économie des memes vaut déjà [250 millions de dollars USD](https://news.bitcoin.com/blockchain-backed-nft-market-value-grew-299-in-2020/).

> L'économie des memes est là où la FOMO rencontre la YOLO. — Felix Salmon d'AXIOS

Cependant, créer un meme prend du temps. Que diriez-vous d'une application web qui permet à n'importe qui de personnaliser un meme et d'en générer un nouveau ? [C'est un meme-as-a-service (MaaS) !](https://sls-website-ap-hongkong-hmtn9c-1302315972.cos-website.ap-hongkong.myqcloud.com/)

## Pourquoi sans serveur ?

En tant que développeur, il n'est probablement pas difficile de créer une application web qui ajoute des légendes textuelles aux images. Cependant, un meme-as-a-service a des exigences supplémentaires.

* La tâche de traitement d'image est souvent intensive en calcul et nécessite des performances élevées.

* Le service de meme peut être très peu utilisé ou il pourrait exploser en popularité. En d'autres termes, il doit être scalable et le développeur ne paie que pour l'utilisation réelle.

Il existe des solutions aux problèmes ci-dessus. Tout d'abord, nous utiliserons un langage de programmation moderne haute performance pour écrire la fonction de manipulation d'image et de texte. Nous utiliserons Rust à cette fin, qui offre des performances natives mais avec une sécurité mémoire.

Ensuite, nous pouvons mieux répondre à l'exigence de scalabilité avec une fonction sans serveur dans un cloud public. Une fonction sans serveur est gratuite lorsqu'elle n'est pas utilisée et peut rapidement passer à l'échelle pour des millions d'utilisateurs.

Bien qu'il soit possible d'exécuter un programme natif compilé à partir de Rust en tant que fonction sans serveur, une meilleure façon est d'exécuter le programme Rust dans une VM WebAssembly en tant que fonction sans serveur.

La VM WebAssembly agit comme une couche de compatibilité et un bac à sable de sécurité entre l'application native et l'environnement hôte sans serveur. Elle permet au programme Rust d'être plus portable car la VM WebAssembly est préconfigurée pour s'exécuter dans une variété de systèmes d'exploitation et d'images de conteneurs requis par les environnements d'exécution sans serveur de cloud public.

De plus, WebAssembly facilite l'accès sécurisé des programmes Rust aux bibliothèques logicielles écrites en C/C++. Un exemple est d'[accéder aux bibliothèques Tensorflow dans les systèmes d'exploitation hérités depuis Rust](https://www.secondstate.io/articles/wasi-tensorflow/).

## Démarrage rapide

Dans ce tutoriel, nous utiliserons [un projet de modèle sur GitHub](https://github.com/second-state/tencent-meme-scf) pour déployer notre Rust meme-as-a-service sur Tencent Cloud. Le modèle est basé sur le framework Serverless open source.

Le programme Rust compile et s'exécute sur la VM Second State (SSVM), qui est une VM WebAssembly optimisée pour s'exécuter dans des environnements d'hébergement basés sur le cloud.

> Bien que nous utilisions Tencent Cloud dans cet exemple, le Serverless Framework est agnostique à tous les principaux clouds publics. Vous pouvez facilement déployer sur AWS ou Azure avec des modifications mineures.

Tout d'abord, vous devrez [installer le Serverless Framework](https://www.serverless.com/framework/docs/getting-started/) et créer un compte gratuit sur [Tencent Cloud](https://cloud.tencent.com/). Ensuite, forkez ou clonez le [dépôt GitHub du modèle](https://github.com/second-state/tencent-meme-scf) et accédez à son répertoire.

```bash
$ git clone https://github.com/second-state/tencent-meme-scf
$ cd tencent-meme-scf
```

Vous pouvez maintenant utiliser le Serverless Framework pour déployer la fonction cloud, une passerelle API pour le service de fonction, et une page HTML statique qui utilise le service de fonction. Il est configuré pour se déployer sur Tencent Cloud dans le fichier `.env`.

Suivez simplement les instructions à l'écran pour vous connecter à Tencent Cloud et déployer.

```bash
$ sls deploy
... ...
  website:       https://sls-website-ap-hongkong-kfdilz-1302315972.cos-website.ap-hongkong.myqcloud.com
  vendorMessage: null

63s ‹ tencent-meme-scf › "deploy" ran for 3 apps successfully.
```

Chargez l'URL du `website` dans un navigateur pour voir votre [meme-as-a-service en action](https://sls-website-ap-hongkong-hmtn9c-1302315972.cos-website.ap-hongkong.myqcloud.com/) ! Il vous permet de personnaliser le texte, la position et la taille de chaque légende / filigrane sur l'image du meme.

## Comment fonctionne l'application

L'architecture globale de l'application est une application JAMStack typique. La logique backend pour le traitement d'image est déployée en tant que fonction sans serveur, et est disponible via une API.

L'interface utilisateur frontend est une page web statique HTML et JavaScript. Le frontend interagit avec l'API backend via des appels JavaScript Ajax.

La fonction sans serveur backend pour ajouter des légendes (ou filigranes) à l'image de fond du meme est écrite en Rust dans le fichier [main.rs](https://github.com/second-state/tencent-meme-scf/blob/main/src/main.rs). Il lit d'abord le fichier de police pour le texte du filigrane et le fichier d'image de fond.

Il lit ensuite l'entrée de l'application utilisateur qui spécifie le texte, la position et la taille de chaque filigrane. L'entrée est sous la forme de texte JSON, et elle est analysée en un tableau de structures Rust à l'aide de la bibliothèque `serde_json`.

La fonction `_watermark()` ajoute chaque filigrane à l'image. La fonction sortie l'image finale et l'encode en base64. La passerelle API de l'environnement d'exécution sans serveur retourne l'image encodée en base64 à l'appel JavaScript pour être affichée sur la page web.

```rust
const FONT_FILE : &[u8] = include_bytes!("PingFang-Bold.ttf") as &[u8];
const TEMPLATE_BUF : &[u8] = include_bytes!("bg.png") as &[u8];

fn main() {
  let mut buffer = String::new();
  io::stdin().read_to_string(&mut buffer).expect("Error reading from STDIN");
  let obj: FaasInput = serde_json::from_str(&buffer).unwrap();

  let mut img = image::load_from_memory(TEMPLATE_BUF).unwrap();

  let memes: Vec<Watermark> = serde_json::from_str(&(obj.body)).unwrap();
  for m in memes {
    _watermark(m, &mut img);
  }

  let mut buf = vec![];
  img.write_to(&mut buf, image::ImageOutputFormat::Png).unwrap();
  println!("{}", base64::encode_config(buf, base64::STANDARD));
}
```

La fonction `_watermark()` ajoute un texte de filigrane à l'image. Elle utilise les bibliothèques standard de traitement d'image Rust (connues sous le nom de crates) pour manipuler l'image du meme.

```rust
fn _watermark(w: Watermark, img: &mut image::DynamicImage) {
  let font_size = w.font_size;

  let font = Vec::from(FONT_FILE);
  let font = Font::try_from_vec(font).unwrap();

  let scale = Scale {
    x: font_size,
    y: font_size,
  };
  drawing::draw_text_mut(img, image::Rgba([0u8, 0u8, 0u8, 255u8]), w.left, w.top, scale, &font, &w.text);
}
```

Le JavaScript frontend prend le texte d'entrée de l'utilisateur, la position et la taille de la police à partir du formulaire HTML, soumet les données d'entrée en JSON à la fonction cloud, puis affiche l'image base64 retournée.

```javascript
var memes = [];
memes[0] = {};
memes[0].text = $('#top-says').val();
memes[0].left = parseInt($('#top-left').val());
memes[0].top = parseInt($('#top-top').val());
memes[0].font_size = parseInt($('#top-font').val());
... ...

$.ajax({
  url: window.env.API_URL,
  type: "post",
  data : JSON.stringify(memes),
  dataType: "text",
  success: function (data) {
    const img_url = "data:image/png;base64," + data;
    $('#wm_img').prop('src', img_url);
  },
  error: function(jqXHR, exception){
    console.log("Error Status: " + jqXHR.statusText);
  }
});
```

## Créez votre propre meme-as-a-service

Avec le modèle de code source, vous pouvez créer votre propre meme-as-a-service. Vous pouvez changer l'image de fond du meme, et changer l'interface utilisateur pour ajouter des filigranes textuels.

Pour ce faire, assurez-vous d'abord d'avoir installé le compilateur [Rust](https://www.rust-lang.org/tools/install) et les outils de construction [ssvmup](https://www.secondstate.io/articles/ssvmup/).

Apportez des modifications au code Rust et au document HTML. Compilez la fonction Rust en WebAssembly, et copiez le résultat dans le dossier `scf/`.

```bash
$ ssvmup build --enable-aot
$ cp pkg/scf.so scf/
```

Exécutez la commande du framework serverless pour déployer l'application.

```bash
$ sls deploy
... ...
  website:       https://sls-website-ap-hongkong-kfdilz-1302315972.cos-website.ap-hongkong.myqcloud.com
  vendorMessage: null

63s ‹ tencent-meme-scf › "deploy" ran for 3 apps successfully.
```

## Qu'est-ce qui suit

Maintenant que vous avez créé et publié votre propre meme-as-a-service, félicitations !

Il y a beaucoup plus que vous pouvez faire avec l'application JAMStack et les fonctions sans serveur. Par exemple, vous pouvez créer des fonctions sans serveur pour l'inférence Tensorflow afin d'incorporer une reconnaissance et un traitement d'image avancés à votre application.