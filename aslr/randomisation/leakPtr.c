#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	printf("Addr of win func is %p\n", win);
}
