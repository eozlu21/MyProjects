# The Shell

## Why the shell?

We want to teach you how to make the most of the tools you know, show you new tools to add to your toolbox, and hopefully instill in you some excitement for exploring (and perhaps building) more tools on your own. 

## What is the shell?

1. **Terminal**: Old-school textual interface to your computer. Think of it as a device through which one interacts with a computer, typically with a keyboard and display. Available almost on all platforms.

  **Why?** to run programs, give them input, and check their output.

2. **Console**: Physical terminal directly connected to a machine. On Linux, the console appears as several terminals (ttys numbered), and you can switch between them.

  **Command line**: An interface where the user types a command (which is expressed as a sequence of characters — typically a command name followed by some parameters) and presses the Return key to execute that command.

3. **Shell**: Command line interpreter to run programs.
There are many different unix shells. Ubuntu's default shell is [Bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)) (like most other Linux distributions). Popular alternatives include [zsh](http://en.wikipedia.org/wiki/Zsh) (which emphasizes power and customizability) and [fish](http://en.wikipedia.org/wiki/Friendly_interactive_shell) (which emphasizes simplicity).

We will be using the most common **Bourne Again SHell** or "**bash**" in short, to access it:
* Open the terminal on your computer (you can install it if not available).
or 
* Go to Shell tab on repl.it and type `$SHELL` to get a user's shell.

If you want to learn more about this: [a great post] (https://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line).

## What do we see?

*The prompt*: The main textual interface to the shell. It tells you the following things:

* The name of the user
* The name of the machine
* *current working directory*, meaning where you currently are, is `~` (short for "home"). 
* The `$` sign means you are not the root user

## The first commands

Let's type a command for the shell to interpret:

`date`

executes the `date` program to print the current date and time. 

Back to the prompt, let's execute another command, this time with arguments:

`echo hello`

executes the program `echo` with the argument `hello`. 
The `echo` program simply prints out its arguments.  

The command and the arguments are separated by whitespace. Shell parses them and then runs the program indicated by the first word, using each following word as an argument. 

To use space in the argument, e.g. `hello world`, 
* you can quote the argument with `'` or `"`:
`"hello world"` or `'hello world'`
or 
* escape the space character with `\`: (`hello\ world`).

## Where to find commands?

How does the shell know how to find the `date` or `echo` programs? Like python, the shell is a programming environment. This means that it has variables, conditionals, loops, and functions (next lectures!). 

Your commands are interpreted by the shell as programs. When you type something other than its programming keywords, it looks up for it in an environment variable called `$PATH`.  

`$PATH` is a list of directories for the shell to search for programs for your command. To see these directories, you can type:

`echo $PATH`

To find which directory the program `echo` is in, type:

`which echo`

This means, when you type `echo $PATH`, what is executed actually is the following:

`/bin/echo $PATH`

## Navigating the shell

* A **path** on the shell is a delimited list of directories; separated by `/` on Linux and macOS and `\` on Windows. 

* On Linux and macOS, the path / is the **root** of the file system, under which all directories and files lie, whereas on Windows there is one root for each disk partition (e.g., `C:\`). 

* If a path starts with `/`, it is called an *absolute path*. Any other path is a *relative path*. 

* Relative paths are relative to the current working directory.

* Use the `pwd` command to see the current working directory.

* Use `cd` to change to another directory specified by the following argument.

`cd /home`

*  In a path, `.` refers to the current directory, and `..` to its parent directory.

`cd ..`
  
`pwd`

`../../bin/echo hello`


* When we run a program, it will operate in the current directory unless we tell it otherwise. For example, it will usually search for files there, and create new files there if it needs to.

* To see the list of files, directories in a given directory, we use the `ls` command. Without any arguments, `ls` will print the contents of the current directory:

  `ls`

  `cd ..`

  `ls`

* Most commands accept flags and options (flags with values) that start with `-` to modify their behavior. Usually, running a program with the `-h` or `--help` flag will print some help text that tells you what flags and options are available. For example, type the following to learn about the flags and options for `ls`:

`ls --help`

* Or you can find them online. GNU provides links to its [manuals](http://www.gnu.org/manual/manual.html) including the core [GNU utilities](http://www.gnu.org/software/coreutils/manual/coreutils.html), which covers many commands introduced within this lesson.

  **GNU:** An extensive collection of free software, which can be used as an operating system or can be used in parts with other operating systems. The use of the completed GNU tools led to the family of operating systems popularly known as Linux.

## Permissions

Type `ls -l` for detailed information:

* `d` stands for directory.

* There are three groups of three characters `rwx` for `(r)ead`, `(w)rite`, `e(x)ecute` permissions, respectively:
  * The	first three characters are permissions for *the owner of the file* (fguney)
  * The second three, *the owning group* (staff)
  * The last three, *everyone else*
* `-` means no permission for the corresponding field. 


* To enter a directory, one needs execute permissions (`x`) permission on the directory and its parents. Similarly:
  * to list its contents, read (`r`) permissions,
  * to modify its contents, write (`w`) permissions. 

* For example, all the files in `/bin` have the `x` permission set for "everyone else", which means anyone can execute them.


* Other useful commands:
  * `mv` to rename/move a file
  * `cp` to copy a file
  * `mkdir` to make a new directory

## Connecting programs

There are two primary *streams* for programs: **input** and **output** streams. 
  * to read input => read from the input stream,
  * to display something => print to the output stream. 

* Input and output are by default, your terminal. We use the keyboard for input and the screen for output.

* We can rewire these streams using angle bracket signs:
  for input stream : `< file`
  for output stream: `> file`
  
  `echo hello > hello.txt`
  
  `cat hello.txt`
  
  `cat < hello.txt`
  
  `cat < hello.txt > hello2.txt`
  
  `cat hello2.txt`

* You can use `>>` to append to a file
	
`echo appended\ hello >> hello.txt`

* **Pipe** `|` operator to *chain* programs such that the output of one is the input of another:

`ls -l / | tail -n1`



