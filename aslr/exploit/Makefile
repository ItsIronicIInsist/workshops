
randomised: exploit.o
	gcc -o randomised exploit.c

nonRandomised: exploit.o
	clang -o nonRandomised exploit.c -fno-pie

all:
	make randomised
	make nonRandomised
