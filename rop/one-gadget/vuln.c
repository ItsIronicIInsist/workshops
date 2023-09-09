#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Disable ASLR

int main() {
	char buf[0x40];

	gets(buf);
}
