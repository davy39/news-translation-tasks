---
title: Comment créer une bannière Twitter dynamique
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-10-11T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-dynamic-twitter-header
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Group-1--2-.png
tags:
- name: Design
  slug: design
- name: Node.js
  slug: nodejs
- name: projects
  slug: projects
- name: Twitter
  slug: twitter
seo_title: Comment créer une bannière Twitter dynamique
seo_desc: 'In mid-2021, a new Twitter design trend emerged: dynamically updated headers.
  Developers decided that static headers were boring, and dynamic Twitter headers
  were the way to go.

  Ever since then, many developers (including me) have been creating dynam...'
---

À la mi-2021, une nouvelle tendance de design sur Twitter est apparue : les bannières mises à jour dynamiquement. Les développeurs ont décidé que les bannières statiques étaient ennuyeuses, et que les bannières Twitter dynamiques étaient la voie à suivre.

Depuis lors, de nombreux développeurs (moi y compris) ont créé des bannières dynamiques sur Twitter. Mais que signifie réellement ce concept ?

L'idée est d'utiliser une bibliothèque de traitement d'images pour créer et assembler plusieurs images de manière programmatique, puis de télécharger la version finale sur Twitter.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Group-1.png align="left")

Cette idée a ouvert de nombreuses possibilités pour les utilisateurs de Twitter, car vous pouvez désormais utiliser les bannières Twitter pour mettre en avant ou promouvoir tout ce que vous souhaitez.

En fait, certains développeurs en ont fait un produit SaaS. Mais dans mon cas, je voulais simplement garder cela minimal et n'afficher que mes abonnés actuels et un message de salutation personnalisé. Voici le résultat final de ce que nous allons construire ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Web-capture_6-10-2021_84628_twitter.com.jpeg align="left")

Dans ce tutoriel, vous apprendrez à créer une bannière Twitter qui est mise à jour dynamiquement avec les photos de profil de vos abonnés actuels toutes les 60 secondes.

Alors, que devez-vous savoir pour suivre ce tutoriel ? Une connaissance de base de Node.js et de JavaScript sera extrêmement utile pour que vous puissiez tirer le meilleur parti de ce que nous apprenons ici.

# Mise en route

Pour créer notre bannière Twitter dynamique, nous allons utiliser `Nodejs` et la bibliothèque de traitement d'images `sharp`. Nous utiliserons `sharp` pour créer et fusionner les éléments de notre bannière dynamique.

Pour commencer, vous aurez besoin d'une nouvelle bannière. Pour cela, vous pouvez utiliser votre logiciel d'édition d'images préféré, mais dans mon cas, j'ai utilisé Figma.

J'ai ouvert Figma et créé une nouvelle bannière Twitter de `1500px x 500px`. Ensuite, j'ai ajouté des boîtes et du texte factices pour visualiser où j'allais placer les éléments avec `sharp` plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--3-.png align="left")

## Comment créer une application Twitter

Pour continuer, vous aurez besoin d'un compte développeur Twitter. Un compte développeur vous permet d'interagir avec l'API Twitter. Si vous n'avez pas encore de compte développeur, rendez-vous sur le [Portail des développeurs Twitter](https://developer.twitter.com/en/portal/dashboard) et créez-en un.

Pour interagir pleinement avec l'API Twitter, comme récupérer des tweets ou des abonnés, vous aurez besoin de certaines clés d'accès.

Pour obtenir ces clés d'accès, vous devrez créer une application Twitter. Connectez-vous donc à votre tableau de bord et créez une nouvelle application Twitter avec un nom unique. Une fois terminé, cliquez sur l'onglet `clés et jetons`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--11-.png align="left")

Copiez vos jetons d'accès et sauvegardez-les dans votre presse-papiers ou un fichier texte pour l'instant. Ensuite, cliquez sur `Générer des secrets`, et copiez ceux-ci également.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--15-.png align="left")

De plus, il est important que vous mettiez à jour les permissions de votre application Twitter en cliquant sur le bouton "Modifier" :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--12-.png align="left")

Une fois que vous avez cliqué sur le bouton de modification, allez-y et sélectionnez la permission de lecture et d'écriture des messages directs :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--13-.png align="left")

## Comment configurer le projet

Ouvrez votre éditeur de code, et une fois dans le répertoire de votre choix, ouvrez votre terminal. J'utilise le terminal intégré de Visual Studio Code. Allez-y et créez un nouveau répertoire :

```js
mkdir twitter-banner
```

Ensuite, vous devez vous déplacer dans ce nouveau répertoire, alors exécutez :

```js
cd twitter-banner
```

Une fois dans ce répertoire, créons notre projet Node.js en exécutant cette commande :

```js
npm init -y
```

Pour l'instant, vous avez un projet Node.js vide, alors installons toutes les dépendances dont nous aurons besoin.

Toujours dans le répertoire du projet et dans votre terminal, exécutez ce qui suit :

```js
npm i dotenv axios sharp twitter-api-client
```

Nous utiliserons `dotenv` pour lire nos variables d'environnement. `axios` nous permet de télécharger des images distantes. Le `twitter-api-client` est ce que nous utiliserons pour établir et communiquer avec Twitter. Et enfin, `sharp` est une bibliothèque de traitement d'images que nous utiliserons dans ce tutoriel pour créer notre bannière dynamique.

Avant de pouvoir continuer, vous devrez créer un fichier `.env` et ajouter vos clés d'accès et secrets que vous avez copiés de Twitter précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--10-.png align="left")

Créez un fichier `index.js` avec le code suivant :

```js
// étape 1
const dotenv = require("dotenv");
dotenv.config();
const { TwitterClient } = require("twitter-api-client");
const axios = require("axios");
const sharp = require("sharp");

// étape 2
const twitterClient = new TwitterClient({
  apiKey: process.env.API_KEY,
  apiSecret: process.env.API_SECRET,
  accessToken: process.env.ACCESS_TOKEN,
  accessTokenSecret: process.env.ACCESS_SECRET,
});

// étape 3
async function get_followers() {
  const followers = await twitterClient.accountsAndUsers.followersList({
    count: 3,
  });

  console.log(followers);
}

// appeler la fonction
get_followers()
```

Dans ce code, nous importons nos dépendances installées et les stockons dans des variables, par exemple `sharp = require("sharp")`.

Dans la deuxième étape, nous nous sommes connectés à Twitter.

Enfin, nous avons créé une fonction `get_followers()`. En utilisant notre `twitter-api-client`, nous avons récupéré nos abonnés, et en utilisant le paramètre `count`, nous avons limité la récupération à seulement `3` abonnés.

💡 Voici un conseil : Si vous vivez dans un pays où Twitter n'est pas actuellement disponible (comme c'est mon cas), vous [pouvez vouloir installer un VPN](https://www.freecodecamp.org/news/securing-your-network-connections-using-openvpn/) sur votre système.

Ouvrez maintenant votre fichier `package.json` et ajoutez un script de démarrage `"start": "node index.js"` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--8-.png align="left")

Exécutez maintenant `npm start`, et si tout fonctionne bien, vous devriez voir vos 3 abonnés affichés sur la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--9-.png align="left")

## Comment récupérer les abonnés depuis Twitter

Pour commencer, nous allons récupérer nos abonnés récents depuis Twitter, ce que nous avons déjà fait dans la dernière section. Modifiez simplement votre fichier `index.js` avec le code suivant :

```js
...
async function get_followers() {
  const followers = await twitterClient.accountsAndUsers.followersList({
    screen_name: process.env.TWITTER_HANDLE,
    count: 3,
  });

  const image_data = [];
  let count = 0;

  const get_followers_img = new Promise((resolve, reject) => {
    followers.users.forEach((follower, index, arr) => {
      process_image(
        follower.profile_image_url_https,
        `${follower.screen_name}.png`
      ).then(() => {
        const follower_avatar = {
          input: `${follower.screen_name}.png`,
          top: 380,
          left: parseInt(`${1050 + 120 * index}`),
        };
        image_data.push(follower_avatar);
        count++;
        if (count === arr.length) resolve();
      });

    });
  });


Analysons un peu ce code : nous avons d'abord créé une fonction `get_followers()`. À l'intérieur de la fonction, nous avons récupéré nos abonnés récents et les avons sauvegardés dans la variable `followers`. Ensuite, nous avons créé une nouvelle `Promise` appelée `get_followers_img` et pour chacun des abonnés, nous avons appelé une fonction `process_img()` :

```js
process_image(
        follower.profile_image_url_https,
        `${follower.screen_name}-${index}.png`
      )
```

La fonction prend deux paramètres : l'URL de l'image de l'abonné et le nom de l'image (pour lequel nous avons utilisé le nom d'écran de l'abonné `${follower.screen_name}.png`).

Une autre chose que je voulais souligner est `follower_img_data`. Souvenez-vous quand j'ai dit que nous allions créer et ajouter plusieurs images ensemble ? Pour faire cela dans `sharp`, vous avez besoin de trois propriétés :

1. input : Le chemin vers le fichier

2. top : Position verticale de l'image

3. left : Position horizontale

Nous poussons chacun des `follower_img_data` dans notre tableau `image_data` :

```js
image_data.push(follower_img_data);
```

Enfin, nous vérifions si tous les processus sont terminés et ensuite nous résolvons :

```js
...
count++;
if (count === arr.length) resolve();
```

## Comment traiter les images

Dans l'étape précédente, nous avons appelé une fonction `process_img()` que nous n'avons pas encore créée. Dans cette étape, nous allons créer cette fonction.

Dans votre `index.js`, créez la fonction avec le code suivant :

```js
...
async function process_image(url, image_path) {
  await axios({
    url,
    responseType: "arraybuffer",
  }).then(
    (response) =>
      new Promise((resolve, reject) => {
        const rounded_corners = new Buffer.from(
          '<svg><rect x="0" y="0" width="100" height="100" rx="50" ry="50"/></svg>'
        );
        resolve(
          sharp(response.data)
            .resize(100, 100)
            .composite([
              {
                input: rounded_corners,
                blend: "dest-in",
              },
            ])
            .png()
            .toFile(image_path)
        );
      })
  );
}
```

`sharp` ne supporte pas l'utilisation d'images distantes (images non stockées sur votre système de fichiers), donc nous allons utiliser `axios` pour télécharger les images distantes depuis Twitter. Ensuite, lorsque nos promesses sont résolues, nous utiliserons `sharp` pour redimensionner et sauvegarder les images en Buffer dans notre système de fichiers en utilisant `toFile(image_path)`.

> Remarque : Buffer ici fait référence au stockage en mémoire utilisé pour stocker temporairement des données (et dans notre cas, des images). Vous pouvez utiliser ces données comme si elles étaient dans votre système de fichiers.

Vous remarquerez également que nous avons créé une variable `rounded_corners` dans laquelle nous avons dessiné un rectangle avec svg :

```js
const rounded_corners = new Buffer.from(
    '<svg>
        <rect x="0" y="0" width="100" height="100" rx="50" ry="50"/>
    </svg>
');
```

Pour que notre rectangle créé imite une image arrondie, il doit :

* avoir la même taille que notre image redimensionnée `100`

* avoir son rayon vertical et horizontal égal à la moitié de la taille de notre image redimensionnée `50`

## Comment créer le texte

Tout doit être une image – même le texte. Pour créer du texte avec `sharp`, nous devons le créer sous forme d'images SVG et le sauvegarder dans le stockage Buffer. Maintenant, dans votre fichier `index.js`, créez une fonction appelée `create_text()` :

```js
...
async function create_text(width, height, text) {
  try {
    const svg_img = `
    <svg width="${width}" height="${height}">
    <style>
    .text {
      font-size: 64px;
      fill: #000;
      font-weight: 700;
    }
    </style>
    <text x="0%" y="0%" text-anchor="middle" class="text">${text}</text>
    </svg>
    `;
    const svg_img_buffer = Buffer.from(svg_img);
    return svg_img_buffer;
  } catch (error) {
    console.log(error);
  }
}
```

La fonction `create_text()` prend trois paramètres :

1. width : largeur de l'image

2. height : hauteur de l'image

3. text : texte réel que vous voulez écrire, par exemple Hello World

## Comment dessiner la bannière Twitter

Jusqu'à présent, tout va bien ! Nous avons créé et traité plusieurs images, et maintenant vient la partie amusante : ajouter ces images ensemble pour créer une nouvelle image.

Pour commencer, retournez à votre fonction `get_followers()` et ajoutez ceci à la fin :

```js
  get_followers_img.then(() => {
     draw_image(image_data);
  });
```

Maintenant, créons la fonction `draw_image` que nous venons d'appeler. Créez une nouvelle fonction `draw_image` dans votre fichier `index.js` comme ceci :

```js
...
async function draw_image(image_data) {
  try {
    const hour = new Date().getHours();
    const welcomeTypes = ["Bonjour", "Bon après-midi", "Bonsoir"];
    let welcomeText = "";

    if (hour < 12) welcomeText = welcomeTypes[0];
    else if (hour < 18) welcomeText = welcomeTypes[1];
    else welcomeText = welcomeTypes[2];

    const svg_greeting = await create_text(500, 100, welcomeText);

    image_data.push({
      input: svg_greeting,
      top: 52,
      left: 220,
    });

    await sharp("twitter-banner.png")
      .composite(image_data)
      .toFile("new-twitter-banner.png");

    // téléverser la bannière sur twitter
    upload_banner(image_data);
  } catch (error) {
    console.log(error);
  }
}
```

La première chose que nous avons faite dans ce code a été de créer un texte de salutation en fonction de l'heure de la journée. Ensuite, en utilisant la fonction `create_text()` que nous avons créée précédemment, nous avons créé et sauvegardé la salutation sous forme d'image SVG en buffer :

```js
const svg_greeting = await create_text(500, 100, welcomeText);
```

L'étape suivante a été d'ajouter notre nouvelle image en buffer à notre tableau de données d'images :

```js
    image_data.push({
      input: svg_greeting,
      top: 52,
      left: 220,
    });
```

Notez que j'ai obtenu les valeurs top et left à partir du design Figma (ne les inventez pas !).

Ensuite, nous avons combiné nos multiples images en une seule en utilisant `.composite(image_data)` et l'avons sauvegardée dans un nouveau fichier appelé `new-twitter-banner.png`.

```js
    await sharp("twitter-banner.png")
      .composite(image_data)
      .toFile("new-twitter-banner.png");
```

Enfin, une fois que nous avons réussi à créer notre nouvelle image, nous appelons une fonction `upload_banner()`. Comme son nom l'indique, elle nous permet de téléverser notre nouvelle bannière Twitter sur Twitter.

## Comment téléverser la bannière sur Twitter

Pour téléverser notre nouvelle bannière sur Twitter, nous devons d'abord lire l'image depuis notre système de fichiers. Nous devons donc requérir un nouveau module. Ne vous inquiétez pas – nous n'allons pas l'installer, il est fourni avec NodeJs.

En haut de `index.js`, où nous avons requis d'autres modules, ajoutez ce qui suit :

```js
// autres modules
const fs = require("fs");
```

Ensuite, en bas de votre fichier `index.js`, créez une fonction `upload_banner()` avec le code suivant :

```js
async function upload_banner(files) {
  try {
    const base64 = await fs.readFileSync("new-twitter-banner.png", {
      encoding: "base64",
    });
    await twitterClient.accountsAndUsers
      .accountUpdateProfileBanner({
        banner: base64,
      })
      .then(() => {
        console.log("Téléversement sur Twitter terminé");
        delete_files(files);
      });
  } catch (error) {
    console.log(error);
  }
}
```

Remarquez que nous avons appelé une autre fonction `delete_files()` une fois l'image téléversée sur Twitter. Cela est dû au fait que nous ne voulons pas que notre serveur soit rempli d'images de nos nouveaux abonnés, donc après chaque téléversement réussi, nous supprimons les images :

```js
...
async function delete_files(files) {
  try {
    files.forEach((file) => {
      if (file.input.includes('.png')) {
        fs.unlinkSync(file.input);
        console.log("Fichier supprimé");
      }
    });
  } catch (err) {
    console.error(err);
  }
}
```

La fonction ci-dessus vérifie notre `image_data` (maintenant appelée files) et pour chaque `input`, elle vérifie si l'input inclut `.png`. Elle fait cela parce que certaines de nos images (texte SVG) sont des buffers et ne sont pas sauvegardées sur notre système de fichiers. Tentative de suppression de cela entraînerait une erreur.

Enfin, nous voulons exécuter la fonction `get_followers()` toutes les 60 secondes car c'est là que tout commence :

```js
...
get_followers();
setInterval(() => {
  get_followers();
}, 60000);
```

Et c'est tout ! Si vous êtes intéressé, le code complet est sur Github :

%[https://github.com/iamspruce/twitter-banner]

## Conclusion

Si vous êtes arrivé jusqu'ici, félicitations ! Vous devriez maintenant voir votre bannière Twitter dynamique. Et selon l'heure de la journée, vous devriez voir un message de salutation – dans mon cas, c'est le matin ici alors que j'écris ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Web-capture_2-10-2021_105540_twitter.com.jpeg align="left")

Le reste dépend maintenant de votre créativité. Si vous avez créé quelque chose de merveilleux avec ceci, n'hésitez pas à tweeter à ce sujet et à me taguer [@sprucekhalifa](https://twitter.com/sprucekhalifa). Et n'oubliez pas de cliquer sur le bouton suivre.

Alors je vous dis "Allez dans le monde et soyez créatif". Oh, et bon codage !