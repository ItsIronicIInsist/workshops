#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int get_int();

//To avoid interfering with stack corruption
char name_len;
unsigned int i = 0;
int c;

int main() {
	char name[0x40];
	name_len = get_int();

	if (name_len > 0x40) {
		puts("Nice try, but no.");
	} else {
		for (i = 0 ; i < name_len ; i++) {
			c = getchar();
			if (c == '\n') break;

			name[i] = c;
		}
	}
}

int get_int() {
	char buf[0x4];
	fgets(buf, 4, stdin);
	buf[strcspn(buf, "\0")] = 0;

	return atoi(buf);
}
