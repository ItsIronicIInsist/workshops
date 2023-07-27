#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	malloc(0x20);
	printf("Addr of win func is %p\n", win);
}
