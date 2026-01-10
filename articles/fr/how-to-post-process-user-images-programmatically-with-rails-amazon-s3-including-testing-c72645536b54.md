---
title: Comment post-traiter les images des utilisateurs de manière programmatique
  avec Rails & Amazon S3 (y compris les tests)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T17:12:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-post-process-user-images-programmatically-with-rails-amazon-s3-including-testing-c72645536b54
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v1Pr428uI0vmh25_cDl-eQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Comment post-traiter les images des utilisateurs de manière programmatique
  avec Rails & Amazon S3 (y compris les tests)
seo_desc: 'By Amber Wilkie

  The problem

  In our platforms, we allow our users to upload their own images for profile pictures.
  This results, as you might imagine, in a wide variety of image sizing, quality and
  formats. We display these images in various ways thro...'
---

Par Amber Wilkie

### Le problème

Dans nos plateformes, nous permettons à nos utilisateurs de télécharger leurs propres images pour les photos de profil. Cela entraîne, comme vous pouvez l'imaginer, une grande variété de tailles, de qualités et de formats d'images. Nous affichons ces images de diverses manières dans nos plateformes.

Pour la plupart, nous pouvons éviter les problèmes de taille en définissant manuellement la taille sur la balise image. Mais dans un endroit très important — les emails — certains serveurs ignorent notre style et affichent ces images en taille réelle : énormes.

Nous avons besoin d'un moyen de reformater les images des utilisateurs de manière programmatique. De plus, puisque nous allons manipuler les images de toute façon, nous aimerions les faire pivoter automatiquement, ajuster les niveaux et les couleurs, et généralement les rendre aussi belles et aussi cohérentes que possible.

### Considérations

* Nos images sont stockées avec le stockage cloud S3 d'Amazon. Heureusement, Amazon offre une API relativement facile à utiliser pour interagir avec leurs services.
* Parce que nos images sont sur S3, j'ai pensé qu'il serait excellent d'avoir ce service en tant que fonction Lambda, déclenchée lorsqu'un utilisateur télécharge une photo. Malheureusement, je n'ai pas réussi, pour la vie de moi, à faire apparaître quoi que ce soit dans la console CloudWatch (où les logs devraient apparaître). Après avoir buté contre ce mur pendant une journée, j'ai décidé de le ramener en interne.
* Nous hébergeons sur Heroku, qui offre un planificateur gratuit et simple pour exécuter des tâches. Il n'est pas critique pour nous d'avoir ces images converties immédiatement après le téléchargement. Nous pouvons planifier un travail qui récupère tout ce qui est nouveau dans les 10 dernières minutes, et le convertir.

### Le Worker

Ce dont nous avons besoin maintenant, c'est d'un worker que nous pouvons appeler aussi fréquemment que Heroku nous le permet (10 minutes est l'intervalle le plus court).

#### Rassembler les bons utilisateurs

Tout d'abord, nous allons rassembler tous les utilisateurs qui ont des images à convertir. Nous avons stocké les images des utilisateurs dans un motif spécifique dans notre bucket S3 qui inclut un dossier `files`. Nous pouvons simplement rechercher les utilisateurs dont les photos de profil correspondent à l'expression régulière dans `files` :

```
User.where(profilePictureUrl: { '$regex': %r(\/files\/) })
```

Votre expérience peut varier ici, en termes de recherche : nous utilisons une base de données Mongo.

Bien sûr, nous utiliserons un motif différent pour les images traitées. Cela ne récupérera que ceux qui ont téléchargé de nouvelles images depuis la dernière exécution de la tâche. Nous allons boucler à travers chacun de ces utilisateurs et effectuer les actions suivantes.

#### Configuration d'un fichier temporaire

Nous aurons besoin d'un endroit pour stocker les données d'image que nous allons manipuler. Nous pouvons le faire avec un dossier `tmp`. Nous utiliserons cela comme un lieu de stockage pour l'image que nous voulons télécharger vers le nouvel emplacement S3. Nous la nommerons comme nous aimerions que notre image finale soit nommée. Nous voulions simplifier et standardiser les images dans notre système, donc nous utilisons l'identifiant unique de l'utilisateur comme nom de l'image :

```
@temp_file_location = "./tmp/#{user.id}.png"
```

#### Obtenir l'image brute et la sauvegarder localement

Maintenant, nous allons parler à notre bucket S3 et obtenir l'image brute, gigante et non formatée de l'utilisateur :

```
key = URI.parse(user.profilePictureUrl).path.gsub(%r(\A\/), '')
s3 = Aws::S3::Client.new
response = s3.get_object(bucket: ENV['AWS_BUCKET'], key: key)
```

Le code `key` prend la chaîne d'URL que nous avons enregistrée comme `profilePictureUrl` de l'utilisateur et supprime tout ce qui n'est pas le chemin final vers l'image.

Par exemple, `http://images.someimages.com/whatever/12345/image.png` retournerait `whatever/12345/image.png` à partir de ce code. C'est exactement ce que S3 veut de nous pour trouver l'image dans notre bucket. Voici le gem pratique `aws-sdk` qui travaille pour nous avec `get_object`.

Maintenant, nous pouvons appeler `response.body.read` pour obtenir un blob d'une image (blob est le bon mot, bien que ce soit au-dessus de mon niveau de salaire pour vraiment comprendre comment les images sont envoyées d'avant en arrière sur le web). Nous pouvons écrire ce blob localement dans notre dossier tmp :

```
File.open(@temp_file_location, 'wb') { |file| file.write(response.body.read) }
```

Si nous nous arrêtons ici, vous verrez que vous pouvez réellement ouvrir ce fichier dans votre dossier temporaire (avec le nom que vous avez défini ci-dessus — dans notre cas `<user>`.png ).

#### Traiter l'image

Maintenant que nous avons téléchargé l'image depuis Amazon, nous pouvons faire ce que nous voulons avec ! ImageMagick est un outil incroyable disponible gratuitement pour tout le monde.

Nous avons utilisé une version simplifiée pour Rails appelée [MiniMagick](https://github.com/minimagick/minimagick). Ce gem dispose également d'une excellente API qui rend les choses très faciles. Nous n'avons même pas besoin de faire quoi que ce soit de spécial pour récupérer l'image. Le `@temp_file_location` que nous avons utilisé précédemment pour sauvegarder l'image fonctionnera parfaitement pour attirer l'attention de MiniMagick :

```
image = MiniMagick::Image.new(@temp_file_location)
```

Voici les paramètres pour nos photos, mais il y a _des tonnes_ d'options à explorer :

```ruby
image.combine_options do |img|
  img.resize '300x300>'
  img.auto_orient
  img.auto_level
  img.auto_gamma
  img.sharpen '0x3'
  image.format 'png'
end
```

`combine_options` est un moyen pratique de faire un tas de choses à une image en un seul bloc. Lorsque cela se termine, l'image est sauvegardée à nouveau là où elle était avant. (Le formatage de l'image ne peut pas être fait avec l'`img` de `combine_options`.) Maintenant, ce fichier image dans notre dossier temporaire est tout post-traité !

#### Télécharger vers S3 et sauvegarder comme nouvelle photo de profil de l'utilisateur

Maintenant, tout ce que nous avons à faire est de configurer une autre connexion à S3 et de faire le téléchargement :

```ruby
Aws.config.update(
  region: ENV['AWS_REGION'],
  credentials: Aws::Credentials.new(ENV['AWS_ACCESS_KEY_ID'], ENV['AWS_SECRET_ACCESS_KEY']))

s3 = Aws::S3::Resource.new
name = File.basename(@temp_file_location)
bucket = ENV['AWS_BUCKET'] + '-output'
obj = s3.bucket(bucket).object(name)
obj.upload_file(@temp_file_location, acl: 'public-read')
```

Par convention avec Lambda, les tâches automatiques enverront vers un nouveau bucket avec le nom de l'ancien bucket plus « -output » ajouté, donc je suis resté avec cela. Toutes les images formatées des utilisateurs seront déposées dans ce bucket. Puisque nous nommons les images par (unique) identifiants d'utilisateurs, nous sommes sûrs de ne jamais écraser la photo d'un utilisateur avec celle d'un autre.

Nous créons un nouvel objet avec le nom du nouveau fichier, dans le bucket de notre choix, puis nous `upload_file`. Il doit être `public-read` si nous voulons qu'il soit visible sans beaucoup de tracas pour nos clients (vous pouvez choisir une option de sécurité différente).

Si cette dernière ligne retourne true (ce qui sera le cas si le téléchargement se passe bien), nous pouvons mettre à jour notre enregistrement utilisateur :

```
new_url = "https://s3.amazonaws.com/#{ENV['AWS_BUCKET']}-output/#{File.basename(@temp_file_location)}"
user.update(profilePictureUrl: new_url)
```

Et c'est tout ! Si nous exécutons ce worker, nous allons auto-formater et redimensionner toutes les images des utilisateurs dans le système. Toutes les images originales seront en place dans leur ancien motif (et au cas où quelque chose irait mal), et tous les liens des utilisateurs pointeront vers leurs nouvelles images formatées.

### Tests

Nous ne pourrions pas ajouter une nouvelle fonctionnalité à une application Rails sans tester, n'est-ce pas ? Absolument. Voici à quoi ressemblent nos tests pour cela :

```ruby
RSpec.describe Scripts::StandardizeImages, type: :service do
  let!(:user) { User.make!(:student, profilePictureUrl: 'https://s3.amazonaws.com/files/some_picture.jpg') }

  before do
    stub_request(:get, 'https://s3.amazonaws.com/files/some_picture.jpg')
      .with(
        headers: {
          'Accept' => '*/*',
          'Accept-Encoding' => 'gzip;q=1.0,deflate;q=0.6,identity;q=0.3',
          'Host' => 's3.amazonaws.com',
          'User-Agent' => 'Ruby'
        }
      )
      .to_return(status: 200, body: '', headers: {})
    allow_any_instance_of(MiniMagick::Image).to receive(:combine_options).and_return(true)
    allow_any_instance_of(Aws::S3::Object).to receive(:upload_file).and_return(true)
  end

  describe '.call' do
    it 'trouve tous les utilisateurs avec des photos de profil non mises à jour, télécharge, reformate et télécharge la nouvelle photo' do
      Scripts::StandardizeImages.call

      expect(user.reload.profilePictureUrl)
        .to eq "https://s3.amazonaws.com/#{ENV['AWS_BUCKET']}-output/#{user.to_param}.png"
    end
  end
end
```

Si vous regardez d'abord le test lui-même, vous verrez que nous testons que l'URL de la nouvelle photo de profil de notre utilisateur a été sauvegardée correctement. Le reste, nous nous en soucions moins, puisque nous ne voulons pas que notre test télécharge quoi que ce soit, et nous ne voulons probablement pas passer du temps à ce que notre test manipule des images.

Mais bien sûr, le code va essayer de parler à Amazon et de lancer MiniMagick. Au lieu de cela, nous pouvons simuler ces appels. Juste au cas où ce serait nouveau pour vous, je vais passer en revue cette partie.

#### Simulation des appels

Si vous ne simulez pas les appels dans vos tests, vous devriez probablement commencer à le faire immédiatement. Tout ce qui est requis est le gem Webmock. Vous le requérez dans votre `rails_helper` et c'est à peu près tout.

Lorsque votre test essaie de faire un appel à une source externe, vous obtiendrez un message comme celui-ci (j'ai caché les clés privées et autres avec des …) :

```ruby
WebMock::NetConnectNotAllowedError:
       Les connexions HTTP réelles sont désactivées. Requête non enregistrée : GET https://...
Vous pouvez simuler cette requête avec le snippet suivant :
stub_request(:get, "https://...").
         with(
           headers: {
          'Accept'=>'*/*',
          'Accept-Encoding'=>'',
          'Authorization'=>...}).
         to_return(status: 200, body: "", headers: {})
```

Il suffit de copier le morceau `stub_request` et vous êtes bien parti pour la simulation. Vous devrez peut-être retourner quelque chose dans ce `body`, selon ce que vous faites avec l'appel à l'API externe.

J'ai trouvé difficile de faire en sorte que cette réponse simulée retourne quelque chose que mon code verrait comme une image, donc j'ai simplement simulé la fonction `MiniMagick` également. Cela fonctionne bien car nous ne voyons pas la sortie dans ce test de toute façon. Vous devrez tester manuellement que l'image obtient le bon formatage.

Alternativement, vous pouvez utiliser `Aws.config[:s3] = { stub_responses: true }` dans votre initialiseur de test ou éventuellement sur votre `rails_helper` pour simuler toutes les requêtes S3.

#### Une dernière note : Travis CI

Selon les options que vous décidez d'appliquer à votre image, vous pouvez constater que la version d'ImageMagick de Travis n'est pas la même que la vôtre. J'ai essayé beaucoup de choses pour faire en sorte que Travis utilise le même ImageMagick que moi. En fin de compte, je simule l'appel `MiniMagick`, donc c'est un point discutable. Mais attention : si vous ne simulez pas cette fonction, vous pouvez constater que votre CI échoue parce qu'il ne reconnaît pas une option plus récente (comme `intensity`).

Merci d'avoir lu !