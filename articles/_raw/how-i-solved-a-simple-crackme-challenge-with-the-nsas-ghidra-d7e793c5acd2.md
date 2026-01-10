---
title: How I solved a simple CrackMe challenge with the NSA’s Ghidra
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T15:30:50.000Z'
originalURL: https://freecodecamp.org/news/how-i-solved-a-simple-crackme-challenge-with-the-nsas-ghidra-d7e793c5acd2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9N3SURf2cF4fISICAH7tGA.png
tags:
- name: hacking
  slug: hacking
- name: General Programming
  slug: programming
- name: reverse engineering
  slug: reverse-engineering
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Denis Nuțiu

  Hello!

  I’ve been playing recently a bit with Ghidra, which is a reverse engineering tool
  that was recently open sourced by the NSA. The official website describes the tool
  as:


  A software reverse engineering (SRE) suite of tools develo...'
---

By Denis Nuțiu

Hello!

I’ve been playing recently a bit with [Ghidra](https://ghidra-sre.org/), which is a reverse engineering tool that was recently open sourced by the NSA. The official website describes the tool as:

> _A software reverse engineering (SRE) suite of tools developed by NSA’s Research Directorate in support of the Cybersecurity mission._

I’m at the beginning of my reverse engineering career, so I didn’t do anything advanced. I don’t know what features to expect from a professional tool like this, if you’re looking to read about advanced Ghidra features this is likely not the article for you.

In this article I will try to solve a simple CrackMe challenge that I’ve found on the website [root-me](https://www.root-me.org/). The challenge I’m solving is called [ELF - CrackPass](https://www.root-me.org/en/Challenges/Cracking/ELF-CrackPass). If you want to give it try by yourself, then you should consider not reading this article because it will spoil the challenge from you.

Let’s get started! I open up Ghidra and create a new Project which I call RootMe.

![Image](https://cdn-media-1.freecodecamp.org/images/t6VRANxq75gcBUE7GDwEho2IqpOJ6DC4NGt0)

Then I import the challenge file by dragging it to the project folder. I will go with the defaults.

![Image](https://cdn-media-1.freecodecamp.org/images/y2KMPmw-nfQlH9gn9ZJxP2Zqk5XZgrTD1lGF)

After being presented with some info about the binary file, I press OK, select the file, and double click it. This opens up Ghidra’s code browser utility and asks if I want to analyse the file, then I press Yes and go on with the defaults.

After we import the file, we get some information about the binary file. If we press OK and dismiss this window, and then double click the file we imported, this opens up Ghidra’s code browser utility. I select Yes when prompted to analyze the binary and go on with the defaults.

![Image](https://cdn-media-1.freecodecamp.org/images/zBOQtrTVrg3SebAl14mSBlRknf4qJrM2VBKY)

The Code Browser is quite convenient. In the left panel we get to see the disassembly view and in the right panel the decompile view.

Ghidra shows us directly the ELF header info and the entry point of the binary. After double clicking the entry point, the dissembler view jumps to the entry function.

Now we can successfully identify the main function, which I rename to main. It would be nice if the tool would attempt to automatically detect the main function and rename it accordingly.

![Image](https://cdn-media-1.freecodecamp.org/images/7Ng0waaxWM2LhOlomKpuNfPmJudV8uido7WJ)

Before analyzing the main function, I wanted to change its signature. I changed the return type to int and corrected the parameters’ type and name. This change has taken effect in the decompile view which is cool! ?

Highlighting a line in the decompile view also highlights it in the assembly view.

![Image](https://cdn-media-1.freecodecamp.org/images/2HOWsHwRO1EjjGH7Kwv4Dmvu-KVrMSkNL0yj)

Let’s explore the FUN_080485a5 function, which I’ll rename to CheckPassword.

The contents of the CheckPassword function can be found below. I’ve copied the code directly from Ghidra’s decompile view, which is a neat feature that many tools of this type lack! Being able to copy assembly and code is a nice to have feature.

```
void CheckPassword(char *param_1) {   ushort **ppuVar1;   int iVar2;   char *pcVar3;   char cVar4;   char local_108c [128];   char local_100c [4096];   cVar4 = param_1;       if (cVar4 != 0) {          ppuVar1 = __ctype_b_loc();           pcVar3 = param_1;           do {               if (((byte )(ppuVar1 + (int)cVar4) & 8) == 0) {         puts("Bad password !");                     /* WARNING: Subroutine does not return */         abort();       }       cVar4 = pcVar3[1];       pcVar3 = pcVar3 + 1;     } while (cVar4 != 0);   }   FUN_080484f4(local_100c,param_1);   FUN_0804851c(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar2 = strcmp(local_108c,local_100c);   if (iVar2 == 0) {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   else {     puts("Is not the good password !");   }   return; }
```

After taking a look at the code, I’ve come to the following conclusions. The block with the `if` checks if the user has provided a password and inspects the provided password to check if it’s a valid character or something. I’m not exactly sure what it’s checking for, but here’s what __ctype_b_loc()’s documentation says:

> _The __ctype_b_loc() function shall return a pointer into an array of characters in the current locale that contains characteristics for each character in the current character set. The array shall contain a total of 384 characters, and can be indexed with any signed or unsigned char (i.e. with an index value between 128 and 255). If the application is multi-threaded, the array shall be local to the current thread._

Anyways, that block of code is not really worth the time, because it doesn’t modify our password in any way, it just verifies it. So we can skip this kind of verification.

The next function called is FUN_080484f4. Looking at its code, we can tell that it’s just a custom memcopy implementation. Instead of copying the C code from the decompiler view, I copied the assembly code — yes, this is fun.

```
*************************************************************                     *                           FUNCTION                                               *************************************************************                     undefined  FUN_080484f4 (undefined4  param_1 , undefined4  p     undefined         AL:1           <RETURN>     undefined4        Stack[0x4]:4   param_1                                 XREF[1]:     080484f8 (R)        undefined4        Stack[0x8]:4   param_2                                 XREF[1]:     080484fb (R)                        FUN_080484f4                                    XREF[1]:     CheckPassword:080485f5 (c)    080484f4 55              PUSH       EBP 080484f5 89  e5           MOV        EBP ,ESP 080484f7 53              PUSH       EBX 080484f8 8b  5d  08       MOV        EBX ,dword ptr [EBP  + param_1 ] 080484fb 8b  4d  0c       MOV        ECX ,dword ptr [EBP  + param_2 ] 080484fe 0f  b6  11       MOVZX      EDX ,byte ptr [ECX ] 08048501 84  d2           TEST       DL,DL 08048503 74  14           JZ         LAB_08048519 08048505 b8  00  00       MOV        EAX ,0x0             00  00                         LAB_0804850a                                    XREF[1]:     08048517 (j)    0804850a 88  14  03       MOV        byte ptr [EBX  + EAX *0x1 ],DL 0804850d 0f  b6  54       MOVZX      EDX ,byte ptr [ECX  + EAX *0x1  + 0x1 ]             01  01 08048512 83  c0  01       ADD        EAX ,0x1 08048515 84  d2           TEST       DL,DL 08048517 75  f1           JNZ        LAB_0804850a                         LAB_08048519                                    XREF[1]:     08048503 (j)    08048519 5b              POP        EBX 0804851a 5d              POP        EBP 0804851b c3              RETComment: param_1 is dest, param_2 is src. 08048501 checks if src is null and if it is it returns else it initializes EAX (index, current_character) with 0. The next instructions move bytes into EBX (dest) from EDX (src).The loop stops when EDX is null.
```

And the other function FUN_0804851c generates the password from the “THEPASSWORDISEASYTOCRACK” string. Looking at the decompiled view. we can roughly see how this function works. If we didn’t have that, we would need to manually analyze every assembly instruction from the function to understand what it does.

Then, we compare the previously generated password with the password that we got from the user (the first argument, argv[1]). If it matches, the program says good job and prints it, else it prints an error message.

From this basic analysis, we can conclude that if we patch the program in various places, we can get it to spit the password without us needing to reverse any C function and write code. Patching the program means changing some of its instructions.

Let’s see what we have to patch:

At address 0x0804868c we patch the JNS instruction into a JMP. And voilà, the change is reflected in the decompiler view. The ptrace result check is bypassed.

```
{   ptrace(PTRACE_TRACEME,0,1,0);   if (argc != 2) {     puts("You must give a password for use this program !");                     /* WARNING: Subroutine does not return */     abort();   }   CheckPassword(argv[1]);   return 0;}
```

At address 0x080485b8 we patch the JZ instruction into a JMP. We bypass that password verification block we saw earlier.

```
void CheckPassword(undefined4 param_1) {   int iVar1;   char local_108c [128];   char local_100c [4096];   CustomCopy(local_100c,param_1);      GeneratePassword(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar1 = strcmp(local_108c,local_100c);   if (iVar1 == 0) {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   else {     puts("Is not the good password !");   }   return; }
```

At address 0x0804861e we patch JNZ to JZ. This inverts the if/else condition. Since we don’t know the password, we’re going to submit a random password that is not equal to the generated one, thus executing the printf on the else block.

```
void CheckPassword(undefined4 param_1) {   int iVar1;   char local_108c [128];   char local_100c [4096];   CustomCopy(local_100c,param_1);   // constructs the password from the strings and stores it in   // local_108c    GeneratePassword(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar1 = strcmp(local_108c,local_100c);   if (iVar1 == 0) { // passwords are equal     puts("Is not the good password !");   }   else {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   return; }
```

That’s all!

Now we run the program. In other tools we just save the file and it works, but in Ghidra it seems that we need to export it.

To export the program, we go to File -> Export Program (O). We change the format to binary and click OK.

![Image](https://cdn-media-1.freecodecamp.org/images/nQiTkhZ4S8BIG22V66wHKDDcovdTOugk1E3J)

I get the exported program on my desktop but it doesn’t work — I couldn’t manage to run the exported program. After trying to read it’s header with the readelf -h program, I get the following output:

```
root@DESKTOP:/mnt/c/users/denis/Desktop# readelf -h Crack.bin ELF Header:   Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00   Class:                             ELF32   Data:                              2's complement, little endian   Version:                           1 (current)   OS/ABI:                            UNIX - System V   ABI Version:                       0   Type:                              EXEC (Executable file)   Machine:                           Intel 80386   Version:                           0x1   Entry point address:               0x8048440   Start of program headers:          52 (bytes into file)   Start of section headers:          2848 (bytes into file)   Flags:                             0x0   Size of this header:               52 (bytes)   Size of program headers:           32 (bytes)   Number of program headers:         7   Size of section headers:           40 (bytes)   Number of section headers:         27   Section header string table index: 26 readelf: Error: Reading 1080 bytes extends past end of file for section headers
```

Shame. It looks like Ghidra has messed up the [file header](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#File_header)… and, right now I don’t want to manually fix headers. So I fired up another tool and applied the same patches to the file, saved it, ran it with a random argument and validated the flag.

#### Conclusions

Ghidra is a nice tool with a lot of potential. In its current state, it’s not that great but it works. I’ve also encountered a weird scrolling bug while running it on my laptop.

The alternatives would be to pay $$ for other tools of this kind, make your own tools, or work with free but not so user friendly tools.

Let’s hope that once the code is released, the community will start doing fixes and improve Ghidra.

Thanks for reading!

