#include <stdio.h>
#include <stdlib.h>

// gcc -o vuln vuln.c -no-pie -fno-stack-canary -z execstack
// Also disable ASLR

int main() {
	char buf[0x40];

	gets(buf);
}
