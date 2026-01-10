---
title: Vous voulez comprendre Pretty Good Privacy ? Simulez-le.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T14:09:28.000Z'
originalURL: https://freecodecamp.org/news/understanding-pgp-by-simulating-it-79248891325f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AasVs894VEy5lON0kgvfMA.jpeg
tags:
- name: coding
  slug: coding
- name: encryption
  slug: encryption
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Vous voulez comprendre Pretty Good Privacy ? Simulez-le.
seo_desc: 'By Tejaas Solanki

  As the name suggests, Pretty Good Privacy (or PGP) is an encryption program that
  actually provides pretty good privacy. The “pretty good” bit is meant to be a bit
  of an ironic understatement. It has been one of the dominant forms of...'
---

Par Tejaas Solanki

Comme son nom l'indique, Pretty Good Privacy (ou PGP) est un programme de chiffrement qui offre une confidentialité assez bonne. Le terme "pretty good" est une litote ironique. Il a été l'une des formes dominantes de chiffrement de bout en bout pour les communications par e-mail après son développement par Phil Zimmermann en 1991. Il est devenu de plus en plus populaire après son utilisation par le lanceur d'alerte Edward Snowden.

PGP offre deux éléments essentiels pour une communication sécurisée :

1. **Confidentialité** : Assurée par l'utilisation du chiffrement symétrique par blocs, de la compression avec l'algorithme ZIP et de la compatibilité e-mail avec le schéma d'encodage radix64
2. **Authentification** : Assurée par l'utilisation de signatures numériques

Sans plus attendre, examinons le fonctionnement de PGP.

#### Comment cela fonctionne

Je vais expliquer le concept de PGP du point de vue de l'implémentation dans le contexte d'Alice (l'expéditeur) et de Bob (le destinataire). Nous utiliserons les algorithmes suivants :

1. RSA comme algorithme de chiffrement asymétrique
2. SHA-512 comme algorithme de hachage
3. DES comme algorithme de chiffrement symétrique et
4. ZIP pour la compression

Vous pouvez utiliser d'autres algorithmes également. (Je sais que DES est trop ancien pour être utilisé, mais le but ici est de comprendre le concept de PGP.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*TJrbLs2vV9PfyTKKYt_leg.jpeg)
_**Le processus PGP**_

Alice et Bob génèrent tous deux leur paire de clés (clés publiques et privées) en utilisant l'algorithme RSA. Les clés publiques d'Alice et de Bob doivent être connues l'une de l'autre.

**Côté d'Alice / Expéditeur :**

1. Alice écrit un message M, qu'elle souhaite envoyer à Bob.
2. M est fourni en entrée à l'algorithme SHA-512 pour obtenir le hachage binaire de 512 bits (représenté sous forme de chaîne hexadécimale de 128 bits).
3. Ce hachage est signé numériquement en utilisant l'algorithme RSA, c'est-à-dire que le hachage est chiffré par les clés privées d'Alice. Les entrées de RSA sont les clés privées d'Alice et le hachage. La sortie de RSA est le hachage signé numériquement ou le hachage chiffré EH.
4. Maintenant, M et EH sont concaténés ensemble. (Concaténés au sens où ils sont placés dans un tableau de chaînes).
5. M et EH (qui sont dans un tableau de chaînes) servent d'entrée à l'algorithme de compression ZIP pour obtenir le M compressé et le EH compressé, à nouveau dans un tableau de chaînes.
6. La sortie de l'étape précédente est maintenant chiffrée en utilisant l'algorithme de chiffrement symétrique DES. Pour cela, nous allons d'abord générer la SecretKey pour DES. Cette clé et la sortie de l'étape 5 serviront d'entrée à l'algorithme de chiffrement DES qui nous fournira une sortie chiffrée (à nouveau dans un tableau de chaînes).
7. Dernier point mais non des moindres, puisque M est chiffré en utilisant SecretKey, celle-ci doit également être envoyée à Bob. Nous allons chiffrer la SecretKey de l'algorithme DES avec la clé publique de Bob. Nous allons utiliser RSA pour cela et les entrées seront la clé publique de Bob et SecretKey.
8. Les sorties des étapes 6 et 7 sont maintenant concaténées et envoyées comme message final à Bob.

Le message entier est envoyé sous forme de tableau de chaînes (`String finalmessage[]`) qui contient les éléments suivants aux indices :

0 : Message compressé M qui est chiffré avec la SecretKey

1 : Hachage signé numériquement EH qui est ensuite compressé et chiffré avec la SecretKey

2 : Sortie de l'étape 7

**Côté de Bob / Destinataire :**

1. Bob va d'abord déchiffrer la SecretKey de DES avec ses clés privées. Les entrées de l'algorithme RSA pour cela seront les clés privées de Bob et `finalmessage[2]`. La sortie de RSA donnera à Bob la SecretKey.
2. Cette SecretKey servira maintenant d'une des entrées à l'algorithme de déchiffrement DES pour le déchiffrement de `finalmessage[0]` et `finalmessage[1]`. Ces deux éléments serviront également d'entrées à l'algorithme de déchiffrement DES. La sortie de cette étape sera la `version déchiffrée` de `finalmessage[0]` et `finalmessage[1]`.
3. Les sorties de l'étape précédente doivent être fournies en entrée à l'algorithme ZIP pour la décompression.
4. À partir de la sortie de l'étape précédente, nous obtiendrons le hachage signé numériquement et le message original M. Nous vérifierons si le hachage a été signé par Alice. Pour cela, nous calculerons le hachage du message original M en utilisant SHA-512 (`calculated_hash`). Nous déchiffrerons également le hachage signé numériquement avec les clés publiques d'Alice en utilisant RSA. (Entrées de RSA : hachage signé numériquement et clés publiques d'Alice et sortie de RSA : `decrypted_hash`).
5. Comparez `decrypted_hash` et `calculated_hash`. S'ils s'avèrent être les mêmes, alors l'authentification est réussie, ce qui signifie que le message a bien été envoyé par Alice.

Ce qui suit est la simulation de PGP réalisée de la manière la plus simple en utilisant Java.

```java
import java.util.*;
import java.math.*;
import javax.crypto.Cipher;
import java.security.*;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;
import javax.crypto.spec.*;

public class PGP{

static Cipher ecipher, dcipher;//Nécéssaire pour DES

public static void main(String args[]) throws Exception{

	//Génération des clés de l'expéditeur
	KeyPair senderkeyPair = buildKeyPair();
	PublicKey senderpubKey = senderkeyPair.getPublic();
	PrivateKey senderprivateKey = senderkeyPair.getPrivate();
	//Génération des clés du destinataire
	KeyPair receiverkeyPair = buildKeyPair();
	PublicKey receiverpubKey = receiverkeyPair.getPublic();
	PrivateKey receiverprivateKey = receiverkeyPair.getPrivate();

	//Envoi des clés publiques et privées pour le choix de la signature numérique ou du chiffrement asymétrique normal
	String messagetoreceiver[] = senderside(senderpubKey, senderprivateKey, receiverpubKey, receiverprivateKey);
	receiverside(messagetoreceiver, senderpubKey, senderprivateKey, receiverpubKey, receiverprivateKey);						
}


public static void receiverside(String messagetoreceiver[], PublicKey senderpubKey, PrivateKey senderprivateKey, PublicKey receiverpubKey, PrivateKey receiverprivateKey) throws Exception {
	
	//Le destinataire reçoit le message messagetoreceiver[] avec messagetoreceiver[2] comme clé secrète chiffrée avec la clé publique du destinataire
	//Le destinataire déchiffre le messagetoreceiver[2] avec sa clé privée
	String receiverencodedsecretkey = decrypt(receiverpubKey, receiverprivateKey, messagetoreceiver[2], 1);
	//La clé après déchiffrement est sous forme encodée en base64
	byte[] decodedKey = Base64.getDecoder().decode(receiverencodedsecretkey);
	SecretKey originalKey = new SecretKeySpec(decodedKey, 0, decodedKey.length, "DES");
	System.out.println("\nCôté Destinataire : SecretKey DES du Destinataire après Déchiffrement avec sa Clé Privée=\n"+originalKey.toString());
	
	//Déchiffrer le reste du message dans messagetoreceiver avec SecretKey originalKey
	String receiverdecryptedmessage[] = new String[messagetoreceiver.length-1];
	System.out.println("\nCôté Destinataire : Message après Déchiffrement avec SecretKey=");
	for (int i=0;i<messagetoreceiver.length-1;i++) {
		messagetoreceiver[i] = decryptDES(messagetoreceiver[i], originalKey);
		System.out.println(messagetoreceiver[i]);
	}
	
	//Décompresser ce message maintenant, c'est-à-dire décompresser messagetoreceiver
	String unzipstring[] = new String[receiverdecryptedmessage.length];
	System.out.println("\nCôté Destinataire : Message Décompressé=");
	for (int i=0;i<unzipstring.length;i++) {
		unzipstring[i] = decompress(messagetoreceiver[i]);
		System.out.println(unzipstring[i]);
	}
	
	//Le message a été reçu et est dans unzipstring mais vérifiez la signature numérique de l'expéditeur, c'est-à-dire vérifiez le hachage avec senderpubkey
	//Donc déchiffrement du hachage chiffré dans unzipstring avec la clé publique de l'expéditeur
	String receivedhash = decrypt(senderpubKey, senderprivateKey, unzipstring[1], 0);                                 
	System.out.println("\nCôté Destinataire : Hachage Reçu=\n"+receivedhash);
	//Calcul du SHA512 côté destinataire du message
	String calculatedhash = sha512(unzipstring[0]);
	System.out.println("\nCôté Destinataire : Hachage Calculé par le Destinataire=\n"+calculatedhash);
	if (receivedhash.equalsIgnoreCase(calculatedhash)) {
		System.out.println("\nHachage Reçu = Hachage Calculé\nAinsi, la Confidentialité et l'Authentification sont toutes deux atteintes\nSimulation PGP Réussie\n");
	}

}


public static String[] senderside(PublicKey senderpubKey, PrivateKey senderprivateKey, PublicKey receiverpubKey, PrivateKey receiverprivateKey) throws Exception {
	
	//Entrée de l'utilisateur
	System.out.print("\nSimulation PGP:\nCôté Expéditeur : Message d'entrée=\n");
	Scanner sc = new Scanner(System.in);
	String rawinput;
	rawinput = sc.nextLine();
	
	//Génération du hachage SHA-512 du message original
	String hashout = sha512(rawinput);	
	System.out.println("\nCôté Expéditeur : Hachage du Message=\n"+hashout);
	
	//Chiffrer le hachage du message avec les clés privées de l'expéditeur -> Signature Numérique
	String encryptedprivhash = encrypt(senderpubKey, senderprivateKey, hashout, 0);
	System.out.println("\nCôté Expéditeur : Hachage Chiffré avec la Clé Privée de l'Expéditeur (Signature Numérique)=\n"+ encryptedprivhash);     

	//Concaténer le message original et le hachage chiffré
	String beforezipstring[] = {rawinput, encryptedprivhash};
	System.out.println("\nCôté Expéditeur : Message avant Compression=\n"+beforezipstring[0]+beforezipstring[1]);
	
	//Appliquer zip à beforezipbytes[][]
	String afterzipstring[] = new String[beforezipstring.length];
	System.out.println("\nCôté Expéditeur : Message après Compression=");
	for (int i=0;i<beforezipstring.length;i++) {
		afterzipstring[i] = compress(beforezipstring[i]);
		System.out.println(afterzipstring[i]);
	}

	//Chiffrer zipstring avec DES
	SecretKey key = KeyGenerator.getInstance("DES").generateKey();
	System.out.println("\nCôté Expéditeur : SecretKey DES=\n"+key.toString());
	String afterzipstringDES[] = new String[afterzipstring.length+1];
	System.out.println("\nCôté Expéditeur : Message Compressé Chiffré avec SecretKey=");
	for (int i=0;i<afterzipstring.length;i++) {
		afterzipstringDES[i] = encryptDES(afterzipstring[i], key);
		System.out.println(afterzipstringDES[i]);
	}

	//Chiffrer la clé DES avec la Clé Publique du Destinataire en utilisant RSA
	String encodedKey = Base64.getEncoder().encodeToString(key.getEncoded());
	//SecretKey est encodée en base64 puisque le chiffrement direct de la chaîne donne la clé au format chaîne lors du déchiffrement qui ne peut pas être convertie au format SecretKey
	String keyencryptedwithreceiverpub = encrypt(receiverpubKey, receiverprivateKey, encodedKey, 1);
	System.out.println("\nCôté Expéditeur : SecretKey DES Chiffrée avec la Clé Publique du Destinataire=\n"+keyencryptedwithreceiverpub);
	
	//Déchiffrer la clé DES avec la Clé Privée du Destinataire en utilisant RSA
	afterzipstringDES[2]=keyencryptedwithreceiverpub;
	String messagetoreceiver[] = afterzipstringDES;
	System.out.println("\nMessage Final au Destinataire=");
	for (int i=0;i<messagetoreceiver.length;i++) {
		System.out.println(messagetoreceiver[i]);
	}
	return messagetoreceiver;
}


public static String encryptDES(String str, SecretKey key) throws Exception {
	ecipher = Cipher.getInstance("DES");
	ecipher.init(Cipher.ENCRYPT_MODE, key);
	// Encoder la chaîne en bytes en utilisant utf-8
	byte[] utf8 = str.getBytes("UTF8");
	// Chiffrer
	byte[] enc = ecipher.doFinal(utf8);
	// Encoder les bytes en base64 pour obtenir une chaîne
	return new sun.misc.BASE64Encoder().encode(enc);
}


public static String decryptDES(String st, SecretKey key) throws Exception {
	dcipher = Cipher.getInstance("DES");
	dcipher.init(Cipher.DECRYPT_MODE, key);
	// Décoder base64 pour obtenir les bytes
	byte[] dec = new sun.misc.BASE64Decoder().decodeBuffer(st);
	byte[] utf8 = dcipher.doFinal(dec);
	// Décoder en utilisant utf-8
	return new String(utf8, "UTF8");
}


public static String decompress(String st) throws IOException {
	byte[] compressed = new sun.misc.BASE64Decoder().decodeBuffer(st);
	ByteArrayInputStream bis = new ByteArrayInputStream(compressed);
	GZIPInputStream gis = new GZIPInputStream(bis);
	BufferedReader br = new BufferedReader(new InputStreamReader(gis, "UTF-8"));
	StringBuilder sb = new StringBuilder();
	String line;
	while((line = br.readLine()) != null) {
		sb.append(line);
	}
	br.close();
	gis.close();
	bis.close();
	return sb.toString();
}


public static String compress(String data) throws IOException {
	ByteArrayOutputStream bos = new ByteArrayOutputStream(data.length());
	GZIPOutputStream gzip = new GZIPOutputStream(bos);
	gzip.write(data.getBytes());
	gzip.close();
	byte[] compressed = bos.toByteArray();
	bos.close();
	return new sun.misc.BASE64Encoder().encode(compressed);
}


//Prend n'importe quelle chaîne en entrée et calcule le hachage sha 512 bits. La sortie est une chaîne hex de 128 bits
public static String sha512(String rawinput){
	String hashout = "";
	try{
		MessageDigest digest = MessageDigest.getInstance("SHA-512");
		digest.reset();
		digest.update(rawinput.getBytes("utf8"));
		hashout = String.format("%040x", new BigInteger(1, digest.digest()));
	}
	catch(Exception E){
		System.out.println("Exception de Hachage");
	}
	return hashout;
}


public static KeyPair buildKeyPair() throws NoSuchAlgorithmException {
	final int keySize = 2048;
	KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
	keyPairGenerator.initialize(keySize);      
	return keyPairGenerator.genKeyPair();
}


//n: 0->encryptwithprivatekey 1->encryptwithpublickey
public static String encrypt(PublicKey publicKey, PrivateKey privateKey, String message, int ch) throws Exception {
	Cipher cipher = Cipher.getInstance("RSA");
	if (ch == 0) {
		cipher.init(Cipher.ENCRYPT_MODE, privateKey);  
		byte[] utf8 = cipher.doFinal(message.getBytes("UTF-8"));
		return new sun.misc.BASE64Encoder().encode(utf8);
	}
	else {
		cipher.init(Cipher.ENCRYPT_MODE, publicKey);  
		byte[] utf8 = cipher.doFinal(message.getBytes("UTF-8"));
		return new sun.misc.BASE64Encoder().encode(utf8);
		}
	}


//n: 0->decryptwithpublickey 1->decryptwithprivatekey
public static String decrypt(PublicKey publicKey,PrivateKey privateKey, String st, int ch) throws Exception {
	Cipher cipher = Cipher.getInstance("RSA");
	byte[] encrypted = new sun.misc.BASE64Decoder().decodeBuffer(st);
	if (ch == 0) {
		cipher.init(Cipher.DECRYPT_MODE, publicKey);
		byte[] utf8 = cipher.doFinal(encrypted);
		return new String(utf8, "UTF8");
	}
	else {
		cipher.init(Cipher.DECRYPT_MODE, privateKey);
		byte[] utf8 = cipher.doFinal(encrypted);
		return new String(utf8, "UTF8");
		}
	}
}
```

Nous avons utilisé le schéma d'encodage base64 qui est similaire au radix64 utilisé dans PGP.

**Remarque :**

1. Nous encodons en base64 les chaînes après chiffrement et compression afin d'obtenir une forme de texte lisible.
2. Pour le déchiffrement et la décompression, nous envoyons les entrées décodées en base64 comme entrées réelles aux algorithmes de déchiffrement et de décompression.
3. La clé a été encodée et décodée en base64 puisque j'ai utilisé Java pour la simulation de PGP, qui nécessite une forme encodée côté destinataire afin qu'elle puisse être convertie en type de données SecretKey pour le processus de déchiffrement.

Veuillez suivre, applaudir et partager. Commentez pour toute erreur, amélioration ou suggestion. Vous pouvez même me suivre sur [Twitter](https://twitter.com/tejaas_solanki?lang=en).