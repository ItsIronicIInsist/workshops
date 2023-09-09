#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Disable ASLR

int main() {
	char buf[0x40];

	read(0, buf, 0x58);
}
