---
title: How to Automatically Generate C# Code Snippets in Visual Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-09T18:28:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-automatically-generate-code-snippets-visual-studio
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/gbi.png
tags:
- name: automation
  slug: automation
- name: C
  slug: c
- name: Productivity
  slug: productivity
- name: Snippet
  slug: snippet
- name: visual studio
  slug: visual-studio
seo_title: null
seo_desc: 'By Gilad Bar Ilan

  When you use code snippets in Visual Studio, it can make your coding process a lot
  easier and faster. But what are code snippets? And how can you use them?

  In this article, we''ll look at how you can create code snippets in C#. Just ...'
---

By Gilad Bar Ilan

When you use code snippets in Visual Studio, it can make your coding process a lot easier and faster. But what are code snippets? And how can you use them?

In this article, we'll look at how you can create code snippets in C#. Just keep in mind that snippets are available in other languages in Visual Studio as well.

If you already know what code snippets are, then you can skip down to the **“How to Auto-Generate Code Snippets”** section.

## What are Code Snippets?

If you regularly work with Visual Studio, you might already know what code snippets are. Code snippets represent a shortcut for a larger piece of code. 

As an example, open a C# project in Visual Studio and write “for” and then press the tab key twice. As you can see, instead of writing the full for loop we created a for loop just by writing “for”.

There are a lot more pre-defined code snippets you can use. For example, if you write “cw” and then press the tab key twice you’ll see an auto-completion that writes this:

```cs
Console.WriteLine();
```

You can check out the full list of the pre-defined code snippets in the docs here:

%[https://docs.microsoft.com/en-us/visualstudio/ide/visual-csharp-code-snippets?view=vs-2019]

## How to Create Custom Code Snippets

Now that you understand what a code snippet is, we can now go over how to create one.

To create your first code snippet, create a “.snippet” file. I called my file “MySnippet.snippet”, but you can call it whatever you want.

After the creation of the code snippet file, open the file in Visual Studio and add the following piece of code into the file.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title></Title>    
            <Author></Author>
            <Description></Description>
            <Shortcut></Shortcut> 
        </Header>
        <Snippet>
            <Code Language="">
                <![CDATA[]]>
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
```

In the example above, we use the basic structure of a code snippet file. Now, we’ll edit it and create a code snippet that will convert “cr” to `Console.ReadLine()`.

#### Title Tag

The title tag contains the title of the snippet (not the shortcut name). In this example we’ll call the title “ReadLineSnippet”.

#### Author Tag

In the Author tag, you can insert your name/company to get credit for the snippet creation.

#### Description Tag

In the description tag, insert a short description of what the snippet does exactly.

#### Shortcut Tag

The name in the shortcut tag is the name that calls the larger piece of code. For example:

```cs
cw -> Console.WriteLine();
```

The “cw” is specified as the name in the shortcut tag.

#### Language

Because we're working with C# we should specify that in the language:

```cs
<Code Language = "CSharp">
```

#### <![CDATA[]]>

The <![CDATA[]]> holds the value of our snippet. In our example, inside the squared brackets we’ll insert `Console.ReadLine()` like this:

```cs
<![CDATA[Console.ReadLine();]]>
```

### Additional Code Snippet Options

#### Defining Variables:

We can also define variables and give them a default value. By defining a variable we can use it multiple times in the snippet, and we give the user the option to change all the occurrences of the default value at once.

For example, if our snippet creates the following code:

```cs
arr -> 
Object[] arr = new Object[100];
for(int i = 0; i < arr.Length; i++)
{   
	arr[i] = default(Object);
}
```

And we define “Object” as a variable, we can replace all its occurrences. All we need to do is to write in the first occurrence a different name – for example “int” – and then tab twice and it will turn all occurrences of “Object” to “int”.

If we had defined `arr` as a variable too, we could move from one variable to another by pressing tab (when you create the snippet the first variable will be selected in red/cyan color – you can move to the other by pressing tab).

### How to define a variable

```xml
<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>init array.</Title>    
            <Author>Gilad Bar-Ilan</Author>
            <Description>creates and initializes an array.</Description>
            <Shortcut>myArr</Shortcut> 
        </Header>
        <Snippet>
            <Code Language="CSharp">
                <![CDATA[$typeName$[] $varName$ = new $typeName$[100];
                for(int $i$ = 0; $i$ < $varName$.Length; $i$++)
                {
                  $varName$[$i$] = default($typeName$);
                }]]>
            </Code>
            <Declarations>      
                <Literal>      
                    <ID>varName</ID>      
                    <ToolTip>variable name.</ToolTip>         
                    <Default>arr</Default>        
                </Literal>
                <Literal>      
                    <ID>typeName</ID>      
                    <ToolTip>type name.</ToolTip>         
                    <Default>Object</Default>        
                </Literal>
                 <Literal>      
                    <ID>i</ID>      
                    <ToolTip>iterator name.</ToolTip>         
                    <Default>i</Default>        
                </Literal>
             </Declarations> 	
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
```

As you can see in the example above, each variable we use needs to be inside the `<Literal>` tag under the `<Declarations>` tag.

* `<ID>`  — How we call the variable in the `<![CDATA[]]>`
* `<ToolTip>` — A short description of the variable.
* `<Default>`  — The default value of the variable.

**NOTE** — When you use a variable in the `<![CDATA[]]>` you should write it in the following structure: `$<here you put the variable name>$`.

### How to add the code snippet to your project

After we’ve created our code snippet file, we want to use it in our projects. To do so we should put the file inside the custom snippet folder of Visual Studio. This will automatically add the code snippet to our project.

If you want to find the folder path:

* Open a C# project.
* Go to Tools -> Code Snippets Manager
* Copy the path you see in the head of the box opened where it says “Location”.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-200.png)

After you’ve got the path, simply add the file into the path.

**NOTE —** Your “My Code Snippets” folder may be located in a different place on your computer, so don't rely on the path in the picture.

## How to Auto-Generate Code Snippets

Now we can now go over what it means to auto-generate code snippets.

We know that adding “.snippet” files into the “My Code Snippets” folder adds the snippets automatically into our project. So now we can use that behaviour to create code that will automatically create snippet files and add them to our project.

### What kind of code snippets do we want?

In this project, we are going to create a snippet for objects with a default constructor where the shortcut name will be the type name. For example:

```cs
Random + tab twice -> Random random = new Random();
```

The idea of the project is to read the namespaces we use in our project and make a custom snippet for each object that follows the conditions. 

We want to add the snippets for the types of every namespace we use. This means that even if we specify a namespace in the ‘using’ but don’t use any of its objects, we’ll still include a code snippet for its members (those who follow the condition).

In addition to the namespaces, we are also going to create a snippet for our defined types.

#### Things we need to take care of:

* Remove the no longer needed types’ code snippets (if we removed types we’ve created or removed namespaces from the project).
* Update the code snippets every time the user runs the program (we don’t update in the background).
* Add new snippets for new namespaces we use / types we create.
* Make a structure for the types’ code snippet.

### How to get all of our defined objects

If we want to get the full list of the user-defined types there are two ways to do so.

The first way – which is not as good as the second – is by using Regular Expressions. By using regular expressions, we can go over each file in our project and match for a default constructor in a class/declaration of a struct (because structs always have a default constructor).

#### Problems with the Regex technique

If the user separates the files we can check before using the regex if the file was modified. By doing that we can avoid repeating files that haven’t been modified.

But minor changes in the file will cause us to read the file again even if there is no difference in the objects. It'll also result in unorganized files that have a lot of code in a single file which can cause us to read the file over and over. (If the whole code is in a single file or just a few we won’t be able to avoid reading unchanged parts from the code.)

#### The Second Technique — Reflection

Instead of using Regex we can use reflection and get the classes we created by reading the metadata instead of reading each file as a text.

```cs

        /// <summary>
        /// Returns a list of all the types we created.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetCustomTypes()
        {
            StackTrace myStackTrace = new StackTrace();

            //contains the name of the namesapce of the project
            //using stackframe we get's the first calling method (main - the bottom of the stack) and then we check the namespace of the type where the method is located.
            //in our case main is located under 'Program' then we check what is the namespace of Program.
            string namespace_ = myStackTrace.GetFrame(myStackTrace.FrameCount - 1).GetMethod().DeclaringType.Namespace;

            Assembly assembly = Assembly.GetExecutingAssembly();
            
            //holds all the custom types.
            //assembly.GetTypes() => returns all the types.
            //then we remove all the types which is not related to our namesapce.
            //then we remove all the compiler created types.
            //then we remove all the types which doesn't have a default constructor.
            var types = assembly.GetTypes().Where(x => x.Namespace == namespace_).Where(x => !x.Name.Contains("<>c"))
                        .Where(x => x.GetConstructors().Any(x => x.GetParameters().Length == 0));
            return types.ToList();
        }

```

### How to get the libraries’ objects

We'll run into a lot of problems in this part of the project. Let's look at what might go wrong.

#### Problem 1

If we read the assemblies we use in our project using Reflection we won’t have the option to get the types from libraries we defined in the ‘using’ but that we don’t actually use. For example:

```cs
using System.Linq;
using System.IO;
public static void Main()
{  
	int[] arr = Enumerable.Range(0,100).ToArray(); //Linq's functionallity
}
```

In the example above ,we only use Linq functionality, which means that if we are going to read the used assemblies in the project we won’t see System.IO even though we want it to be shown.

#### Problem 2

Another possible problem happens even when we do use the library. This is because a namespace can have multiple assemblies and due to efficiency the compiler won’t call all the assemblies when it doesn’t need to. So even if we use the library it doesn't mean we’ll have all the assemblies.

#### How can we solve the problem?

This problem is complicated because we cannot change the way the compiler works. So if we want to solve the problem we’ll have to be creative.

Our solution won't be very efficient, but we don’t have a lot of options for how to solve this.

#### We can use an algorithm

* We get all the namespaces we use in all of our “.cs” files in the project.
* Then we iterate over all the System DLL files and we check if the types there relate to one of the namespaces we use in the project.
* We add to this list also our defined types, as well as references we added to the project, if the reference is defined in the ‘using’ we add his types even if we don‘t use his types in the program itself.
* After we do that we check if the type has a default constructor.

The code for solving the problem is quite complicated, so let’s go over it.

```cs
using System;
using System.Reflection;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace Reader
{
    public class TypeReader
    {
        public static List<Type> GetAllTypes()
        {
            #region GetSystemLibrary Files
            string systemDllPath = typeof(string).Assembly.Location; //gets the dll of the string type.
            systemDllPath = Path.GetDirectoryName(systemDllPath);
            string[] systemLibraries = Directory.GetFiles(systemDllPath); //the list of the system libraies dlls.  
            #endregion

            #region Namespaces in project files.
            string[] namespaces_ = Directory.GetFiles(GetSourceCodePath())
                                      .Where(x => x.EndsWith(".cs")).ToArray();
            namespaces_ = GetNamespaces(namespaces_).ToArray();//we remove the semi colon
            #endregion

            #region Check the system libraries.
            List<Type> types = systemLibraries.Where(x => x.EndsWith(".dll")).Select(x =>
            {
                Assembly asm = null;
                try
                {
                    asm = Assembly.LoadFile(x);

                }
                catch
                {
                    asm = null;
                }

                return asm;
            }).SelectMany(x => x != null ? x.GetTypes() : new Type[] { })
                        .Where(x => x != null && !x.Name.Contains("<>c")).Where(x => namespaces_.Contains(x.Namespace))
                        .Where(x => x.IsPublic && (x.IsClass || x.IsValueType)).ToList();
            #endregion

            #region add assemblies we use in our program.
            types.AddRange(AppDomain.CurrentDomain.GetAssemblies()
                           .SelectMany(x => x.GetTypes().Where(x => !x.Name.Contains("<>c")).Where(x => namespaces_.Contains(x.Namespace)))
                           .Where(x => x.IsPublic && (x.IsClass || x.IsValueType)));
            #endregion

            #region add custom types we created.
            types.AddRange(GetCustomTypes()); //adds our custom created snippets
            #endregion

            #region add types belongs to refrences we didn't use in our project.
            types.AddRange(GetUnUsedRefrenecedTypes(namespaces_)); //adds the refrenced libraries we specify but don't use.
            #endregion

            #region filter types.
            types = types.Where(x => x.IsValueType || x.GetConstructors().Any(x => x.GetParameters().Length == 0)).ToList();
            #endregion

            #region remove duplicated type names.
            types = types.GroupBy(x => x.FullName).Select(x => x.First()).ToList();
            #endregion

            return types;
        }

        //Returns the assembly of the main function.
        public static string GetMainAssemblyLocation()
        {
            StackTrace main = new StackTrace();
            string path = main.GetFrame(main.FrameCount - 1).GetMethod().DeclaringType.Assembly.Location;
            return Path.GetDirectoryName(path);
        }

        public static string GetSourceCodePath()
        {
            string projectPath = GetMainAssemblyLocation();

            try
            {
                while (!Directory.GetFiles(projectPath).Any(x => x.EndsWith(".cs")))
                {
                    projectPath = projectPath.Remove(projectPath.LastIndexOf("\\"));
                }
            }
            catch
            {
                throw new SourceCodeNotFoundException();
            }

            return projectPath;
        }

        public static List<string> GetNamespaces(string[] files)
        {
            List<string> namespaces = new List<string>();

            foreach (string file_ in files)
            {
                StreamReader fileStream = new StreamReader(file_);
                Regex matchUsing = new Regex(@"using([ ]|\t|\n)+\S+;");
                string[] fileNamespaces = matchUsing.Matches(fileStream.ReadToEnd()).Select(x => x.Value)
                                          .Select(x => x.Remove(x.IndexOf("using"), "using".Length).Trim()).ToArray();
                namespaces.AddRange(fileNamespaces);

                fileStream.Close();
            }

            return namespaces.Select(x => x.Remove(x.Length - 1, 1)).Distinct().ToList();
        }

        /// <summary>
        /// This is used in case we have a custom refrenced library (could be a dll we created)
        /// and we specify that in the using, however, we don't use his assemblies.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetUnUsedRefrenecedTypes(string[] namespaces_)
        {
            string sourceCode = GetMainAssemblyLocation();
            List<Type> otherTypes = new List<Type>();

            string[] fileNames = Directory.GetFiles(Path.GetDirectoryName(sourceCode));

            if (fileNames.Any(x => x.EndsWith(".dll")))
            {
                fileNames = fileNames.Where(x => x.EndsWith(".dll")).ToArray();

                foreach (var file in fileNames)
                {
                    Assembly asm;

                    try
                    {
                        asm = Assembly.LoadFile(file);
                    }
                    catch
                    {
                        continue;
                    }

                    otherTypes.AddRange(asm.GetTypes().Where(x => !x.Name.Contains("<>c"))
                                        .Where(x => x.IsPublic && (x.IsClass || x.IsValueType))
                                        .Where(x => namespaces_.Contains(x.Namespace)).GroupBy(x => x.Name)
                                        .Select(x => x.First()));
                }
            }

            return otherTypes;
        }

        /// <summary>
        /// Returns a list of all the types we created.
        /// </summary>
        /// <returns></returns>
        public static List<Type> GetCustomTypes()
        {
            StackTrace myStackTrace = new StackTrace();
            Type mainType = myStackTrace.GetFrame(myStackTrace.FrameCount - 1).GetMethod().DeclaringType;

            //contains the name of the namesapce of the project
            //using stackframe we get's the first calling method (main - the bottom of the stack) and then we check the namespace of the type where the method is located.
            //in our case main is located under 'Program' then we check what is the namespace of Program.
            string namespace_ = mainType.Namespace;
            Assembly assembly = mainType.Assembly;

            //holds all the custom types.
            //assembly.GetTypes() => returns all the types.
            //then we remove all the types which is not related to our namesapce.
            //then we remove all the compiler created types.
            //then we remove all the types which doesn't have a default constructor.
            var types = assembly.GetTypes().Where(x => x.Namespace == namespace_).Where(x => !x.Name.Contains("<>c")); ;
            return types.ToList();
        }
    }

    internal class SourceCodeNotFoundException : Exception
    {
        public override string Message => "Could not load the '.cs' files, please make sure\n" +
                                    "your files located in the default place / you have a valid project type.";
    }
}

```

#### **Important Note:**

```cs
//If I mention in the explanation the words "main function" I mean:

public static void Main()
{   
	TypeReader.GetAllTypes();
}
//Which means that the main function does not located in the 
//TypeReader class it's the main function who calls the class.
```

### GetSystemLibrary Files Region

In these lines, we get all the library files of “System”.

* We check where the assembly of one of the system DLLs is located (in our case where the assembly of ‘string’ is).
* Then we remove the file name from the path so we’ll have only the directory.
* Then we take only the library files from the directory (“.dll”).

We do so because all of the System libraries files are located in the same directory.

### Namespaces in the project files Region

In these lines, we get all the namespaces we use in all of our project files.

#### Custom methods we use in these lines

**GetSourceCodePath —** This function returns the path of our source code. First, we get the path of the main function’s dll. By assuming that the user works with the default way of sorting directories in Visual Studio, we ‘remove’ directories from our path until we reach a directory with .cs files.

**GetMainAssemblyLocation** — We use StackTrace to get the assembly location of the main function. An example for 'Removing' is  
C:\Users\File1\File2 -> C:\Users\File1

If we can’t find any directory we throw **SourceCodeNotFoundException**.

**GetNamespaces —** The method returns all the namespaces within the files we entered. It iterates over each file and reads all the namespaces we are using in each one of them using Regex.

For each namespace we’ll get `using <Something>;` then we’ll remove all of the extra characters and we only keep the `<Something>`.

#### In GetAllTypes

* We read all the files from our source code directory
* We only keep the files with an extension of “.cs”
* We get the namespaces of the files.

### Check the system libraries Region

In these lines, we check the system libraries. These lines fix both problems we mentioned before.

* We get all the files in the system DLL's directory and we only keep those that represent a dll (with an extension of “.dll”).
* We try to load each one of these files.
* If we can load the file then we get the types in the assembly.
* We remove all the compiler created types “<>c”.
* We only keep the types related to one of the namespaces in our project.
* Then we only keep the public types and those that are class or struct.

#### Why do we do it like this?

The problems we mentioned before were caused because we tried to check what the program **actually** uses in runtime. But the compiler makes optimizations, and that’s why we cannot really reach the cases mentioned in the problems.

So for solving this problem, we need to get creative and check the namespaces we use in our project files. Then we load the assemblies, and at the end check that each type if its namespace is one of the namespaces we use in our project.

### add assemblies we use in our program Region

In these lines, we add the assemblies we use in our program.

For each one of the assemblies, we make the same check for the type it contains.

* If the type is public
* If it’s struct or class
* If it’s not a compiler-created type.
* If it’s related to one of the namespaces we use in our project.

### add custom types we created Region

In this line, we add all of the custom types we’ve created.

**GetCustomTypes —** The function uses StackTrace for getting the namespace and the assembly of the main function.

After we have the assembly we get the types that related to the main’s namespace.

### add types belongs to references we didn't use in our program Region

In this line, we add the types that belong to references we didn’t use in the program and that were specified in the ‘using’ (just like we did for the system types, but this time we do that for the references we added manually, not ‘System’).

**GetUnUsedReferencedTypes** 

* We go over the source code directory (the manually added references located there).
* We try to load the ‘.dll’ files and add all the types that pass the conditions we did in previous checks in main.

### filter types Region

In this line, we only keep value types and classes that have a default constructor (if they are value types they have a default constructor for sure).

### remove duplicated type names Region

We remove duplicated types by name.

## How to Build the Snippets

We've gotten through the hard part, so now it’s time to build the snippets!

```cs
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using Reader;

namespace SnippetGenerator2
{
    public class CodeSnippetGenerator
    {
        public string SnippetLocation;

        public CodeSnippetGenerator(string snippetLocation)
        {
            this.SnippetLocation = snippetLocation.EndsWith("\\") ? snippetLocation : snippetLocation + "\\";
        }

        public void UpdateSnippets()
        {
            List<Type> allTypes = TypeReader.GetAllTypes();
            Func<Type, string> makeFileName = x => SnippetLocation + x.Name + "-" + x.Namespace + ".snippet";

            DirectoryInfo myCodeSnippets = new DirectoryInfo(SnippetLocation);
            string[] snippetFileNames = allTypes.Select(x => makeFileName(x)).ToArray();
            string[] previous = myCodeSnippets.GetFiles().Where(x => x.Name.EndsWith(".snippet")).Select(x => x.Name).ToArray();

            //we only keep the files that no longer exsisted.
            previous = previous.Where(x => !snippetFileNames.Contains(x)).ToArray();
            previous.ToList().ForEach(x =>
            {
                try
                {
                    File.Delete(SnippetLocation + x);
                }
                catch { }
            });//we remove the files we don't need.

            allTypes.ForEach(x => 
            {
                if (!Directory.GetFiles(SnippetLocation).Contains(makeFileName(x)))
                    CreateSnippet(x);
            }
            ); //we create snippets for the types.
        }

        public List<string> RemoveAllCodeSnippets()
        {
            string[] files = Directory.GetFiles(SnippetLocation).ToArray();
            List<string> notDeleted = new List<string>();
   

            files.ToList().ForEach(x =>
            {
                StreamReader snippetFile = new StreamReader(x);

                if (snippetFile.ReadToEnd().Contains("<Author>AUTO-GENERATOR</Author>"))
                {
                    snippetFile.Close();

                    try
                    {
                        File.Delete(x);
                    }
                    catch
                    {
                        notDeleted.Add(x);
                    }
                }
            });

            int i = 0;
            while(i < notDeleted.Count)
            {
                i++;
                try
                {
                    File.Delete(notDeleted[i]);
                }
                catch
                {
                    continue;
                }
                notDeleted.Remove(notDeleted[i]);
            }

            return notDeleted;
        }


        /// <summary>
        /// Creates a snippet.
        /// </summary>
        /// <param name="type">The type to make the default create for.</param>
        /// <param name="description">The description of the snippet.</param>
        internal void CreateSnippet(Type type,
                                       string description = "DefaultDescription")
        {

            string snippet_structure = $@"<?xml version=""1.0"" encoding=""utf-8""?>
  <CodeSnippets xmlns = """">  
     <CodeSnippet Format = ""1.0.0"">   
         <Header>    
            <Title>{type.Name}-{type.Namespace}</Title>    
            <Author>AUTO-GENERATOR</Author>
            <Description> {description}</Description>
            <Shortcut> {type.Name} </Shortcut>   
         </Header>   
         <Snippet>  
           <Code Language = ""CSharp"">    
                 <![CDATA[{type.Name} $obj$ = new {type.Name}();]]>     
             </Code>     
             <Declarations>      
                <Literal>      
                    <ID>obj</ID>      
                    <ToolTip>variable name.</ToolTip>         
                       <Default>{type.Name.ToLower()}</Default>        
                   </Literal>       
                </Declarations>         
             </Snippet>        
           </CodeSnippet>
         </CodeSnippets>";

            //write the snippet into the snippets directory.
            File.WriteAllText(SnippetLocation + type.Name + "-" + type.Namespace + ".snippet", snippet_structure);
        }
    }
}

```

Let's talk about this code:

* “Reader” is the namespace of the class we’ve built before.
* TypeReader is the name of the class we’ve built before.
* The file names of the Snippets will be written as `<TypeName>-<NamespaceName>.snippet`

#### The Constructor

* The constructor accepts the path for the “My Code Snippets” directory from the user.

#### The CreateSnippet method

The “CreateSnippet” method creates a snippet with a common structure.

* Title — The `<typeName>-<namespace>`
* Author — AUTO-GENERATOR, we call all of them by the same name so we’ll know what snippets were created by the CodeSnippetGenerator and what were created by the user.
* We create a structure of:

```cs
TypeName typename(in small letters) = new TypeName();
```

* We set the “shortcut” to be the type name also.

#### The RemoveAllSnippets method

The RemoveAllSnippets method removes all the snippets **that the CodeSnippetGenerator** created. 

We know if files were created by the code snippet generator by checking if the Author tag contains “AUTO-GENERATOR”. 

We try again to delete files that were not deleted the first time. If we can’t delete them at the second time we return a list of the file names that we couldn't delete.

#### The UpdateSnippets method

The UpdateSnippets method updates the snippets each run. On each run:

* We read the names of the types we use in our main program (not in the CodeSnippetGenerator class).
* We read the names of the .snippet files we have from the previous run.
* We make an array of filenames for each one of our types from our current run.
* We see what snippet files we no longer need by comparing what names of snippet files we had in our previous run that don't exist in the filenames of the current run.
* We remove these files.
* Then we create a “.snippet” file for each type that doesn’t already have one.

## How to Use the Snippet Auto-Generator Program

If you want to use the program, simply open a C# project and at the beginning of the main function write:

```cs
var csg = new CodeSnippetGenerator("path of 'My Code Snippets'>);
csg.UpdateSnippets(); //to create & update the snippets in 
project.csg.RemoveAllSnippets(); //to remove the created snippets.
```

Congratulations! You’ve now created your own CodeSnippetGenerator.

I hope these come in handy and save you time when you're writing your code. Thanks for reading :)


