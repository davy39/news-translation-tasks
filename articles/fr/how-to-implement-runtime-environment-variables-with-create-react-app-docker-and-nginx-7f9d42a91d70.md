---
title: Comment implémenter des variables d'environnement d'exécution avec create-react-app,
  Docker et Nginx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T22:57:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70
coverImage: https://cdn-media-1.freecodecamp.org/images/0*auL6Qm-oQV0NC_pU.png
tags:
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment implémenter des variables d'environnement d'exécution avec create-react-app,
  Docker et Nginx
seo_desc: 'By Krunoslav Banovac

  There are many ways to configure your React application. Let’s use an approach which
  respects Twelve-Factor App methodology. This means it enforces reconfiguration during
  runtime. Therefore no build per environment would be requi...'
---

Par Krunoslav Banovac

Il existe de nombreuses façons de configurer votre application React. Utilisons une approche qui respecte la [**méthodologie Twelve-Factor App**](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology). Cela signifie qu'elle impose une reconfiguration pendant l'exécution. Par conséquent, aucune compilation par environnement ne serait nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/0*auL6Qm-oQV0NC_pU.png)

### ? Que voulons-nous accomplir ?

Nous voulons pouvoir exécuter notre application React en tant que conteneur Docker qui est construit une seule fois. Elle s'exécute partout en étant configurable **pendant l'exécution**. Le résultat devrait être un conteneur léger et performant qui sert notre application React en tant que contenu statique, ce que nous réalisons en utilisant Nginx Alpine. Notre application devrait permettre la configuration dans le fichier docker-compose comme suit :

```yml
version: "3.2"
services:
  my-react-app:
    image: my-react-app
    ports:
      - "3000:80"
    environment:
      - "API_URL=https://production.example.com"
```

_Nous devrions pouvoir configurer notre application React en utilisant le drapeau `-e` (variables d'environnement) lors de l'utilisation de la commande `Docker run`._

> _À première vue, cette approche peut sembler apporter un bénéfice trop faible pour le travail supplémentaire qu'elle nécessite pour la configuration initiale. Mais une fois la configuration terminée, les configurations spécifiques à l'environnement et le déploiement seront beaucoup plus faciles à gérer. Donc pour ceux qui ciblent des environnements dynamiques ou utilisent des systèmes d'orchestration, cette approche est définitivement quelque chose à considérer._

### ? Le problème

Tout d'abord, il doit être clair qu'il n'existe pas de variables d'environnement dans l'environnement du navigateur. Quelle que soit la solution que nous utilisons de nos jours, ce n'est rien de plus qu'une fausse abstraction.

Mais alors, vous pourriez demander, qu'en est-il des fichiers `.env` et des variables d'environnement préférées `REACT_APP` qui viennent [directement de la documentation](https://facebook.github.io/create-react-app/docs/adding-custom-environment-variables) ? Même dans le code source, celles-ci sont utilisées comme `process.env` tout comme nous utilisons les variables d'environnement dans Node.js.

En réalité, l'objet `process` n'existe pas dans l'environnement du navigateur, il est spécifique à Node. CRA par défaut ne fait pas de rendu côté serveur. Il ne peut pas injecter de variables d'environnement pendant le service de contenu (comme [Next.js](https://github.com/zeit/next.js) le fait). **Pendant la transpilation**, le processus Webpack remplace toutes les occurrences de `process.env` par une valeur de chaîne qui a été donnée. Cela signifie **qu'il ne peut être configuré que pendant le temps de construction**.

#### ? Solution

Le moment spécifique où il est encore possible d'injecter des variables d'environnement se produit lorsque nous démarrons notre conteneur. Ensuite, nous pouvons lire les variables d'environnement depuis l'intérieur du conteneur. Nous pouvons les écrire dans un fichier qui peut être servi via Nginx (qui sert également notre application React). Elles sont importées dans notre application en utilisant la balise `<script>` à l'intérieur de la section `<head>` de `index.html`. À ce moment-là, nous exécutons un script bash qui crée un fichier JavaScript avec les variables d'environnement assignées en tant que propriétés de l'objet global `window`. Injectées pour être globalement disponibles dans notre application à la manière du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mqvCYhYLV_KN3VzY.png)
_Vous trouverez un lien vers le dépôt GitHub à la fin de l'article._

### ? Guide étape par étape

Commençons par un projet `create-react-app` simple et créons un fichier `.env` avec notre première variable d'environnement que nous voulons exposer.

```sh
# Générer une application React
create-react-app cra-runtime-environment-variables
cd cra-runtime-environment-variables

# Créer des variables d'environnement par défaut que nous voulons utiliser
touch .env
echo "API_URL=https//default.dev.api.com" >> .env
```

Ensuite, écrivons un petit script bash qui lira le fichier `.env` et extraira les variables d'environnement qui seront écrites dans le fichier. Si vous définissez une variable d'environnement à l'intérieur du conteneur, sa valeur sera utilisée, sinon, elle reviendra à la valeur par défaut du fichier .env. Il créera un fichier JavaScript qui place les valeurs des variables d'environnement en tant qu'objet qui est assigné en tant que propriété de l'objet `window`.

```sh
#!/bin/bash

# Recreate config file
rm -rf ./env-config.js
touch ./env-config.js

# Add assignment 
echo "window._env_ = {" >> ./env-config.js

# Read each line in .env file
# Each line represents key=value pairs
while read -r line || [[ -n "$line" ]];
do
  # Split env variables by character `=`
  if printf '%s\n' "$line" | grep -q -e '='; then
    varname=$(printf '%s\n' "$line" | sed -e 's/=.*//')
    varvalue=$(printf '%s\n' "$line" | sed -e 's/^[^=]*=//')
  fi

  # Read value of current variable if exists as Environment variable
  value=$(printf '%s\n' "${!varname}")
  # Otherwise use value from .env file
  [[ -z $value ]] && value=${varvalue}
  
  # Append configuration property to JS file
  echo "  $varname: \"$value\"," >> ./env-config.js
done < .env

echo "}" >> ./env-config.js
```

Nous devons ajouter la ligne suivante à l'élément `<head>` à l'intérieur de `index.html` qui importe ensuite le fichier créé par notre script bash.

```html
<script src="%PUBLIC_URL%/env-config.js"></script>
```

Affichons notre variable d'environnement dans l'application :

```jsx
<p>API_URL: {window._env_.API_URL}</p>
```

#### ? Développement

Pendant le développement, si nous ne voulons pas utiliser Docker, nous pouvons exécuter le script bash via le runner `npm script` en modifiant `package.json` :

```json
  "scripts": {
    "dev": "chmod +x ./env.sh && ./env.sh && cp env-config.js ./public/ && react-scripts start",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "build": "react-scripts build'"
  },
```

Et si nous exécutons `yarn dev`, nous devrions voir une sortie comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e4ugnbph1YnN3uVbH2QNZA.png)
_Utilisation de la valeur par défaut API_URL du fichier .env_

Il existe deux façons de reconfigurer les variables d'environnement dans l'environnement de développement. Soit changer la valeur par défaut à l'intérieur du fichier `.env`, soit remplacer les valeurs par défaut en exécutant la commande `yarn dev` avec des variables d'environnement préfixées :

```sh
API_URL=https://my.new.dev.api.com yarn dev
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*MHnRJn_JkV33mmK6Yh1raw.png)
_Utilisation de la valeur API_URL qui a été passée via CLI_

Enfin, modifions `.gitignore` pour exclure les configurations d'environnement du code source :

```
# Temporary env files
/public/env-config.js
env-config.js
```

Pour l'environnement de développement, c'est tout ! Nous sommes à mi-chemin. Nous n'avons pas fait une grande différence à ce stade par rapport à ce que CRA offrait par défaut pour l'environnement de développement. Le vrai potentiel de cette approche brille en production.

#### ? Production

Maintenant, nous allons créer une configuration minimale de Nginx afin de pouvoir construire une image optimisée qui sert l'application prête pour la production.

```sh
# Create directory for Nginx configuration
mkdir -p conf/conf.d
touch conf/conf.d/default.conf conf/conf.d/gzip.conf
```

Le fichier de configuration principal devrait ressembler à ceci :

```
server {
  listen 80;
  location / {
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
    expires -1; # Set it to different value depending on your standard requirements
  }
  error_page   500 502 503 504  /50x.html;
  location = /50x.html {
    root   /usr/share/nginx/html;
  }
}
```

Il est également utile d'activer la compression gzip afin que nos actifs soient plus légers pendant la transition réseau :

```
gzip on;
gzip_http_version  1.0;
gzip_comp_level    5; # 1-9
gzip_min_length    256;
gzip_proxied       any;
gzip_vary          on;

# MIME-types
gzip_types
  application/atom+xml
  application/javascript
  application/json
  application/rss+xml
  application/vnd.ms-fontobject
  application/x-font-ttf
  application/x-web-app-manifest+json
  application/xhtml+xml
  application/xml
  font/opentype
  image/svg+xml
  image/x-icon
  text/css
  text/plain
  text/x-component;
```

Maintenant que notre configuration Nginx est prête, nous pouvons enfin créer les fichiers Dockerfile et docker-compose :

```sh
touch Dockerfile docker-compose.yml
```

Initialement, nous utilisons l'image `node:alpine` pour créer une version de production optimisée de notre application. Ensuite, nous construisons une image d'exécution sur la base de `nginx:alpine`.

```dockerfile
# => Build container
FROM node:alpine as builder
WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn
COPY . .
RUN yarn build

# => Run container
FROM nginx:1.15.2-alpine

# Nginx config
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

# Static build
COPY --from=builder /app/build /usr/share/nginx/html/

# Default port exposure
EXPOSE 80

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]
```

Notre conteneur est maintenant prêt. Nous pouvons faire toutes les choses standard avec lui. Nous pouvons construire un conteneur, l'exécuter avec des configurations en ligne et le pousser vers un dépôt fourni par des services tels que [Dockerhub](https://hub.docker.com/).

```sh
docker build . -t kunokdev/cra-runtime-environment-variables
docker run -p 3000:80 -e API_URL=https://staging.api.com -t kunokdev/cra-runtime-environment-variables
docker push -t kunokdev/cra-runtime-environment-variables
```

La commande `docker run` ci-dessus devrait produire une application comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kK7Ss5ODlukXgsLNuYh0Lg.png)
_Utilisation de API_URL qui a été fourni via le drapeau de variable d'environnement à la commande docker run_

Enfin, créons notre fichier docker-compose. Vous aurez généralement différents fichiers docker-compose selon l'environnement et vous utiliserez le drapeau `-f` pour sélectionner le fichier à utiliser.

```yml
version: "3.2"
services:
  cra-runtime-environment-variables:
    image: kunokdev/cra-runtime-environment-variables
    ports:
      - "5000:80"
    environment:
      - "API_URL=production.example.com"
```

Et si nous faisons `docker-compose up`, nous devrions voir une sortie comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7TBDwzS_otshjMhQqvycmg.png)
_Utilisation de API_URL qui a été fourni via la propriété d'environnement docker-compose_

Super ! Nous avons maintenant atteint notre objectif. Nous pouvons reconfigurer notre application facilement dans les environnements de développement et de production de manière très pratique. Nous pouvons maintenant enfin construire une seule fois et exécuter partout !

**Si vous êtes bloqué ou avez des idées supplémentaires, accédez au [code source sur GitHub](https://github.com/kunokdev/cra-runtime-environment-variables).**

#### ? Prochaines étapes

L'implémentation actuelle du script shell imprimera toutes les variables incluses dans le fichier .env. La plupart du temps, nous ne voulons pas exposer toutes ces variables. Vous pourriez implémenter des filtres pour les variables que vous ne voulez pas exposer en utilisant des préfixes ou une technique similaire.

#### ? Solutions alternatives

Comme indiqué ci-dessus, la configuration au moment de la construction satisfera la plupart des cas d'utilisation. Vous pouvez vous appuyer sur l'approche par défaut en utilisant un fichier .env par environnement et construire un conteneur pour chaque environnement et injecter des valeurs via les variables d'environnement fournies par Webpack de CRA.

Vous pourriez également jeter un œil à ce [problème du dépôt GitHub de CRA](https://github.com/facebook/create-react-app/issues/2353) qui couvre ce problème. À l'heure actuelle, il devrait y avoir plus de publications et de problèmes qui couvrent ce sujet. Chacun offre une solution similaire à celle ci-dessus. C'est à vous de décider comment vous allez implémenter les détails spécifiques. Vous pourriez utiliser Node.js pour servir votre application, ce qui signifie que vous pouvez également remplacer le script shell par un script Node.js. Notez que Nginx est plus pratique pour servir du contenu statique.

_Si vous avez des questions ou souhaitez offrir des commentaires ; n'hésitez pas à ouvrir un problème sur [GitHub](https://github.com/kunokdev/cra-runtime-environment-variables). Optionnellement, suivez-moi pour d'autres publications liées aux technologies web._