---
title: 'Minecraft Forge : Comment télécharger, installer et utiliser Forge'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-10T22:59:00.000Z'
originalURL: https://freecodecamp.org/news/minecraft-forge-how-to-download-install-and-use-forge
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dfd740569d1a4ca3ac2.jpg
tags:
- name: gaming
  slug: gaming
- name: minecraft
  slug: minecraft
- name: toothbrush
  slug: toothbrush
seo_title: 'Minecraft Forge : Comment télécharger, installer et utiliser Forge'
seo_desc: 'If you are reading this article you probably already know Minecraft. We
  use Forge to manipulate the game Minecraft to make it do what we want. This could
  be anything, ranging from new cool creatures to entire new systems in the game.

  Forge is a moddi...'
---

Si vous lisez cet article, vous connaissez probablement déjà Minecraft. Nous utilisons Forge pour manipuler le jeu Minecraft afin de lui faire faire ce que nous voulons. Cela peut être n'importe quoi, allant de nouvelles créatures cool à des systèmes entièrement nouveaux dans le jeu.

Forge est une API de modding. Minecraft Forge (ou Forge en abrégé) est une couche entre notre code et Minecraft lui-même.

Nous ne pouvons pas demander directement à Minecraft d'ajouter des objets et de faire des choses spéciales et cool. C'est pourquoi nous avons besoin d'une API (interface de programmation d'applications) pour gérer notre logique et faire en sorte que Minecraft la reconnaisse.

## **Ça a l'air cool ! Comment puis-je commencer ?**

* Vous aurez besoin du JDK (Java development kit) qui est un ensemble de bibliothèques, d'outils et de l'environnement d'exécution pour créer des programmes Java et les exécuter.
* Un compte Minecraft qui peut être acheté sur leur site officiel. ([https://minecraft.net/en-us/store/](https://minecraft.net/en-us/store/))
* Un IDE (Eclipse ou IntelliJ sont recommandés pour le développement Minecraft)

Après avoir installé/acquis ces logiciels, téléchargez la version de Forge souhaitée sur [https://files.minecraftforge.net/](https://files.minecraftforge.net/).

**Astuce** : Survolez le bouton d'information et appuyez sur téléchargement direct pour éviter un virus Adfly !

Une fois que vous avez téléchargé ce ZIP, vous pourrez le décompresser. Faites-le et utilisez la commande cd (cmd/command) dans le répertoire contenant tous les fichiers Forge. Exécutez `gradlew setupDecompWorkspace`.

Ensuite, choisissez votre IDE (environnement de développement intégré).

* Eclipse ? `gradlew eclipse`.
* IntelliJ ? Importez le fichier build.gradle dans votre configuration IntelliJ.

## **D'accord, et maintenant ? Comment ajouter de nouveaux objets fantaisistes ? (Configuration de base du mod)**

Patience. Il y a beaucoup plus à faire. Vous devrez bien sûr texturer un objet, ajouter du code et bien plus encore ! Dans cet article, nous ne regarderons que quelques exemples de code simple que j'utilise également pour mes propres mods. Le voici !

`@Mod.EventBusSubscriber @Mod(modid = Version.MOD_ID, name = Version.MOD_NAME, version = Version.VERSION) public class TheMod {

```text
public static ModMetadata metadata;

public static File baseDir;
public static Configuration config;

@SidedProxy(clientSide="com.ciphry.client.ClientProxy", serverSide="com.ciphry.common.CommonProxy")
public static CommonProxy proxy;

@Mod.EventHandler
public void preInit(FMLPreInitializationEvent event) {
    proxy.preInit(event);

    baseDir = new File(event.getModConfigurationDirectory(), MOD_ID);
    config = new Configuration(event.getSuggestedConfigurationFile());

    if (!baseDir.exists())
        baseDir.mkdir();
}

@Mod.EventHandler
public void init(FMLInitializationEvent event) {
    proxy.init(event);

}

@Mod.EventHandler
public void postInit(FMLPostInitializationEvent event) {
    proxy.postInit(event);
}
```

Utilisez ce code comme vous le souhaitez. Assurez-vous simplement de modifier, par exemple, les chaînes de proxy et plus encore. Cela devrait vous donner un aperçu de base de ce à quoi ressemble une classe de mod de base.