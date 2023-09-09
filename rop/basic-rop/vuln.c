#include <stdio.h>
#include <stdlib.h>

// disable ASLR

int main() {
	char buf[0x40];

	gets(buf);
}
