# About

This is code from the following article, which describes the Heartbleed vulnerability
in detail and shows how to create a demonstration.

https://fixme

# How to Run

You'll need a Linux computer with Docker installed.

```
$ git clone https://github.com/jknudsen-synopsys/heartbleed-box
$ cd heartbleed-box
$ ./build.sh
$ ./run.sh
```

Then open a new terminal window or tab.

```
$ ./simulate-post.sh username password
$ python3 exploit.py
```