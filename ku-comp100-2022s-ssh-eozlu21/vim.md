# Editors

Simplified from [the Missing Semester Lecture](https://missing.csail.mit.edu/2020/editors/).
If you want the same vim settings, copy .vmrc file under your home folder.

## Introduction
* Programming is basically typing, editing code. It is important to get efficient in this!
* This is different than regular English, e.g. writing essays. Programming is more about reading code, navigating in the code, making little changes, searches, and so on.
* You typically start with a tutorial but it takes time to get used to it, and a lot of time to get efficient, to master it.
* Which editor? It's up to you. There are graphical editors like PyCharm that might be easy to learn in the beginning. We strongly recommend learning the basics of a commandline editor such as Vim, at least, learn [how to quit Vim](https://twitter.com/iamdevloper/status/435555976687923200).
* You're not going to learn Vim in this lecture fully. Our goal is to teach you the basics. Please, practice in the lab and later, in your free time.

## Modal Editors
When programming, you're doing different types of things such as reading code, making small edits to code, writing lots of code in one go, and so on. These correspond to *modes* in Vim.

1. When you start, you're in the **normal** mode. In this mode, all the key combinations behave in a certain way.
2. Using a key combination, you can switch to another mode where meaning of key combinations change.
  For example, **insert** mode by pressing `i` in the **normal** mode. You can go back to **normal** mode, via `<ESC>` (the escape key).
3. Different modes are designed for different things:
    * **Normal:** Navigating around file, reading these, going from one file to other.
    In any mode, press **`<ESC>`** to switch to **normal** mode.
    * **Insert (`i`):** Typing text, keys go into the text.
    * **Replace (`R`):** Overwriting text.
    * **Visual -- plain (`v`), line (`V`), or block `<C-v>` (or `Ctrl-V` or `^V`):** for selecting blocks of text
    * **Command-line (`:`):** for running a command

## Basics
Enter Vim by typing `vim` on the commandline or by providing the name of the file to edit as an argument `vim main.sh`.

Try typing `x` in the **normal** mode. You will not see an "x" on the screen but it will delete a character because we are in the **normal** mode, not **insert** mode. Press `i` to go into **insert** mode and you can insert a character "x" now. How do we now which mode we are in? It shows at the bottom, `-- INSERT --` for **insert** mode or nothing for **normal** mode. Use `<ESC>` to go back to **normal** mode.

We want to avoid using mouse even to open, save, close files etc., it takes a lot of time! We can do all of these using the keyboard. This brings us to the **commandline** mode. Switch to **commandline** mode from **normal** mode by typing `:`. You can quit vim by typing `:quit` or `:q`. 

Let's change the file by going to **insert** mode, how to save this change? Go to **commandline** mode and type `:w` for writing. If you forgot what a certain command does, you can use `:help` command, for example `:help :w`. How to leave help and go back? Also, what happens if you do this: `:help w` instead of `:help :w`?

## Programming Vim
Interface to Vim is like another programming language. Once you learn different key combinations, you can combine them together to do interesting things. This way, you can write programs really fast!

### Movement
To do that, we first need to move fast: How to navigate in the file?  
* Moving cursor up (`k`), down (`j`), left (`h`), right (`l`). 
* What if want to move **w**ord by **w**ord forward (`w`) and **b**ackward (`b`)?
* What if you want t go to the **e**nd of a word (`e`)?
* What if you want to move to the beginning of a line (`0`) or end of a line (`$`) or to the first non-empty character on the line (`^`)?
* What if you want to go up (`<C-u>`) and down (`<C-d>`) fast, not line by line? 
* Or directly to the end of the file (`G`) or to the beginning of the file (`gg`)?
* Or to the **l**owest line on the screen (`L`) or the **m**iddle line (`M`), the **h**ighest line (`H`)?

## Editing
From **normal** to **insert** mode, one way is the `i` key. Another is `o` key which **o**pens a new line down where the cursor is and goes into the **insert** mode.

You can **d**elete the character on the cursor (`d`) or **d**elete the whole **w**ord (`dw`). If you delete something you didn't mean to, you can **u**ndo (`u`). Multiple undo's are allowed. You can also redo with `<C-r>`.

For example, how do you **d**elete to the **e**nd of a word? (`de`)

You can also change the end of a word in a similar way with `ce`. It deletes to the end of a word but puts you in **insert** mode so you can change it.
`c` and `d` are similar, they take motion as argument, they will either delete or change according to motion. For example, `d0` to delete to beginning of line and `cw` to change word.

If you repeat the key twice, the effect takes place on the line, for example you can use `dd` to delete the line.

You can delete a character using `x` key or replace it with another character using `r` key followed by the character you want to put in.

**Copy (`y`) - paste (`p`):** Also takes motion as an argument, `yw` to copy the word. For example, `yy` will copy the line `p` will paste it. To copy a block of things, let's talk about **visual** mode (`v`). In **visual** mode, you can move around with `h, j, k, l` to select a block of text and copy it (`y`) and then paste it (`p`). In **visual line** mode (`V`), you can select whole lines and in **visual block** mode (`<C-V>`), you can select rectangular text blocks.

## More goodies

**Case Change:** 
`~` changes the case of the character, e.g. select multiple words and flip the case.

**Counts:**
How do you do a particular thing some number of times, for example go down 4 lines? `j j j j` or better: `4j`.
Another example, go to **visual** mode and select 3 words (`3e`). Go back to **normal** mode and delete 2 words (`2dw`).

**Modifiers:**
Let's say you have some text **i**nside square brackets, you can change it quickly via `ci[`.
Or you can delete what is inside parantheses via `di(`. Change `i` to `a` to delete it all **a**round the parantheses including the parantheses (`da(`).

**Search:**
Type `/` followed by whatever you want to search for, e.g. `/range` will search for "range" and take the cursor to the first occurence of "range" in the file. Press `n` to go to the next match. You can also go to a certain line if you know the line number via `/`, e.g. `/10` will take you to line 10.

**Repeat a Command:**
Let's say you typed something and you want to repeat it down two lines, you can just do `jj.`
