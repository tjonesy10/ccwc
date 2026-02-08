\# ccwc



A small, cross-platform clone of the Unix `wc` command, implemented in Python as a learning project.



\## Overview



`ccwc` counts lines, words, bytes, and characters in text input.  

It mirrors the core behavior of the Unix `wc` utility and supports both file input and standard input (stdin).



This project focuses on:

\- Command-line interface design

\- File and stream handling

\- Reproducing real-world Unix tool behavior



\## Features



\- Byte count (`-c`)

\- Line count (`-l`)

\- Word count (`-w`)

\- Character count (`-m`)

\- Default mode (`-l -w -c`)

\- Reads from files or standard input



\## Requirements



\- Python 3.10 or newer

\- Windows, macOS, or Linux



\## Usage



Count bytes:

```bash

python ccwc.py -c test.txt



