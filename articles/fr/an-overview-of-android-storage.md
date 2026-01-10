---
title: Aperçu du stockage Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-08-25T16:05:00.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-android-storage
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0aa740569d1a4ca4a11.jpg
tags:
- name: Android
  slug: android
- name: coding
  slug: coding
- name: development
  slug: development
- name: storage
  slug: storage
- name: 'tech '
  slug: tech
seo_title: Aperçu du stockage Android
seo_desc: Storage is this thing we are all aware of, but always take for granted.
  Not long ago, every leap in storage capacity was incremental and appeared to be
  impossible. Nowadays, we don’t give a second thought when contemplating how much
  of it our devices...
---

Le stockage est cette chose dont nous sommes tous conscients, mais que nous tenons toujours pour acquise. Il n'y a pas si longtemps, chaque avancée en matière de capacité de stockage était incrémentielle et semblait impossible. Aujourd'hui, nous ne nous posons même plus la question de savoir combien nos appareils en ont (et nous nous soucions peu des différences).

Un point plus important serait d'examiner l'évolution de ce qui est stocké en mémoire. Avant les smartphones, nous sauvegardions une photo occasionnelle ou deux, quelques jeux et une tonne de messages texte. Mais maintenant, n'importe quel téléphone standard aura un mélange d'applications, de documents, de photos, de vidéos, de fichiers musicaux, et plus encore. Découvrons comment nous pouvons utiliser l'espace de stockage d'un appareil pour nos applications.

Ce que nous allons couvrir dans cet article est :

1. Les différents types de stockage sur les téléphones Android
2. Les différences entre les types de stockage
3. Comment utiliser le stockage dans votre application

Chaque application a accès à deux types de stockage différents : **_interne_** et **_externe_**. Il existe des différences majeures entre ces deux types de stockage, et les connaître vous aidera lors de la conception de votre prochaine application.

Avant de commencer, une chose doit être dite à propos du stockage et du cache. Le stockage est destiné aux choses que vous souhaitez sauvegarder de manière persistante, tandis que le cache est là pour sauvegarder des choses temporairement.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-227.png)
_Photo par [Unsplash](https://unsplash.com/@erdaest?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Erda Estremera</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Stockage interne

Lorsque chaque application est exécutée sur le système d'exploitation, elle dispose de son propre stockage interne. Ce stockage est privé et réservé uniquement à l'utilisation de l'application. Cela signifie que d'autres applications ne peuvent pas y accéder, ni l'utilisateur. Une autre chose à garder à l'esprit lors de l'utilisation du stockage interne est sa disponibilité. Contrairement au stockage externe, le stockage interne est toujours disponible pour votre application.

L'utilisation de ce stockage présente cependant des inconvénients. Si l'utilisateur supprime l'application, toutes les données stockées dans le stockage interne de votre application sont également supprimées. Imaginez ce qui se passerait si vous installiez un jeu sur votre téléphone et que, quelque temps plus tard, vous décidiez de le supprimer. Vous aimeriez que votre progression dans le jeu soit sauvegardée, au cas où vous réinstalleriez le jeu.

Alors, comment sauvegarder un fichier dans le stockage interne ?

```java
public void saveFileInternalStorage() {
   
        String FILENAME = "hello_world_file";
        String inputToFile = "Hello From Internal Storage!";
   
        try {
            FileOutputStream fileOutputStream = openFileOutput(FILENAME, Context.MODE_PRIVATE);
            fileOutputStream.write(inputToFile.getBytes());
            fileOutputStream.close();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has been saved successfully",
                    Toast.LENGTH_SHORT).show();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has not been saved successfully due to an exception " + e.getLocalizedMessage(),
                    Toast.LENGTH_SHORT).show();
        } catch (IOException e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has not been saved successfully due to an exception " + e.getLocalizedMessage(),
                    Toast.LENGTH_SHORT).show();
        }
 }
```

Comme vous pouvez le voir dans l'exemple de code, nous sauvegardons un fichier appelé **_hello_world_file_** qui contient le texte **_Hello From Internal Storage!_**. J'ai créé deux clauses catch juste pour démontrer les exceptions qui peuvent survenir lors de la tentative de faire cela, mais vous pouvez les minimiser à une seule clause catch avec l'objet Exception général.

Faites attention que la méthode **_openFileOutput_** ouvrira le fichier s'il existe déjà, mais sinon, elle le créera. Le deuxième paramètre de cette méthode est le mode de fichier. Ce paramètre désigne la portée du fichier et l'accès à celui-ci. La valeur par défaut est MODE_PRIVATE, qui rend le fichier accessible uniquement à votre application.

Les deux autres valeurs pour ce paramètre sont MODE_WORLD_READABLE et MODE_WORLD_WRITEABLE, mais elles ont été obsolètes depuis l'API 17. Le partage de fichiers privés avec d'autres applications utilise une logique différente que vous pouvez lire plus en détail [ici](https://developer.android.com/training/secure-file-sharing). Enfin, lors de l'écriture dans le fichier, nous convertissons notre chaîne en octets et nous nous assurons de fermer le fichier à la fin.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-228.png)
_Photo par [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Spiske</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Stockage externe

Contrairement à ce que le nom implique, il s'agit d'un stockage défini par le fait qu'il n'est pas toujours accessible. Cela peut signifier qu'il peut s'agir d'une carte SD externe (stockage externe secondaire), mais il peut également s'agir d'un stockage trouvé sur l'appareil (stockage externe principal).

Pour illustrer ce fait, le stockage externe est un stockage auquel vous pouvez accéder lorsque vous connectez votre appareil à un ordinateur via un câble USB. Comme vous l'avez peut-être deviné, tout ce qui est stocké dans ce type de stockage est accessible à d'autres applications sur votre appareil, mais sera conservé si vous désinstallez l'application.

Avant de pouvoir démontrer comment sauvegarder des fichiers dans le stockage externe, nous devons faire deux choses :

1. Vérifier qu'il y a suffisamment d'espace pour sauvegarder le fichier
2. Demander la permission pendant l'exécution

Pour vérifier qu'il y a suffisamment d'espace de stockage, les lignes de code suivantes sont nécessaires :

```java
//Vérifier si vous pouvez lire/écrire dans le stockage externe
public boolean isExternalStorageWritable() {
    String state = Environment.getExternalStorageState();
    if (Environment.MEDIA_MOUNTED.equals(state)) {
        return true;
    }
    return false;
}
```

Pour obtenir l'accès au stockage externe, nous devons ajouter la permission suivante à notre AndroidManifest.xml :

```java
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

De plus, depuis l'API 23, les permissions dangereuses ne sont pas autorisées pendant l'installation, mais pendant l'exécution. L'écriture dans le stockage externe est classée comme telle, donc nous devons ajouter une logique pour permettre à l'utilisateur de décider s'il accorde ou non la permission à l'application.

```java
public void saveFileExternalStorage(View view) {
        if (isExternalStorageWritable()) {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) ==
                PackageManager.PERMISSION_GRANTED) {
                    writeFileToExternalStorage();
                } else{
                    ActivityCompat.requestPermissions(this,
                            new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 0);
                }
            }
        }

        @Override
        public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
            switch (requestCode) {
                case 0:
                {
                    writeFileToExternalStorage();
                    break;
                }
            }
        }
```

Notre méthode **_writeFileToExternalStorage_** ressemble à ceci :

```java
public void writeFileToExternalStorage() {
            String root = Environment.getExternalStorageDirectory().toString();
            File myDir = new File(root + "/saved_files");
            if (!myDir.exists()) {
                myDir.mkdirs();
            }
            try {
                File file = new File(myDir, "myfile.txt");
                FileOutputStream out = new FileOutputStream(file);
                out.write(inputToFile.getBytes());
                out.close();
                Toast.makeText(getApplicationContext(),
                        "File myfile.txt" + " has been saved successfully to external storage",
                        Toast.LENGTH_SHORT).show();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
```

Si vous souhaitez voir un exemple de tout le code présenté ici, vous pouvez vous rendre sur ce [dépôt GitHub](https://github.com/TomerPacific/MediumArticles/tree/master/AndroidStorage).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-229.png)
_Photo par [Unsplash](https://unsplash.com/@steve_j?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Steve Johnson</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Bon à savoir

Ci-dessus, il s'agissait de deux exemples simples de la façon de travailler avec les différents types de stockage pour votre application. Puisque nous traitons d'une ressource gérée par le système, nous devons également être conscients des comportements qui y sont associés.

Par défaut, votre application sera installée dans le stockage interne (**_voir l'explication internalOnly_**), mais à partir du niveau d'API 8, vous pouvez ajouter un attribut, **_installLocation_**, à votre manifeste qui permet à votre application d'être installée dans le stockage externe. Une raison de le faire est si votre application est très grande et que vous préféreriez que l'utilisateur l'installe sur le stockage externe de l'appareil, car il y a plus d'espace là-bas.

Il existe trois valeurs pour cet attribut :

* **_auto_** - signifie que vous n'avez pas de préférence spécifique quant à l'endroit où l'application sera installée. L'application essaiera d'être installée dans le stockage interne, mais si celui-ci est plein, elle l'installera dans le stockage externe
* **_internalOnly_** - l'application ne sera installée que dans le stockage interne, et si l'espace est insuffisant, elle ne sera pas installée
* **_preferExternal_** - signifie que vous souhaitez que votre application soit installée dans le stockage externe, mais si l'espace est insuffisant, elle sera installée en interne

Pour les options auto et preferExternal, l'utilisateur a la possibilité de déplacer l'application du stockage externe vers le stockage interne, et vice versa.

Gardez à l'esprit que lorsqu'un utilisateur connecte son appareil à un ordinateur et active le partage de données ou démonte une carte SD, toutes les applications exécutées à partir du stockage externe sont détruites. Si votre application utilise l'une des fonctionnalités suivantes, vous ne devez pas l'installer dans le stockage externe :

> _Différents services (en particulier le service d'alarme), les moteurs de méthode d'entrée, les fonds d'écran animés, les widgets d'application, les gestionnaires de comptes, les adaptateurs de synchronisation, les administrateurs d'appareils et les récepteurs de diffusion écoutant l'achèvement du démarrage._