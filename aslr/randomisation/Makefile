
randomised: leakPtr.o
	gcc -o randomised leakPtr.c

nonRandomised: leakPtr.o
	clang -o nonRandomised leakPtr.c -fno-pie

all:
	make randomised
	make nonRandomised
