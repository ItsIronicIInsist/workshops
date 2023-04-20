#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>



unsigned long get_int();
void generate_passphrase(char * buf, int nbytes);
void win();
void get_input(char * user_input, unsigned long user_len);

int main(void) {
	char passphrase[0x40];
	char user_input[0x40];
	char locked = 1;

	unsigned long user_len;
	int passphrase_len = 0x40;


	generate_passphrase(passphrase, 0x40);

	while (locked) {
		puts("How many bytes will be entered?");
		user_len = get_int();

		if (user_len < (int)passphrase_len) {
			printf("Enter your input: ");
			get_input(user_input, user_len);

			user_input[user_len - 1] = 0;
		}

		if (memcmp(user_input, passphrase, 0x40) == 0) {
			locked = 0;
		}
	}

	win();
}

unsigned long get_int() {
	char buf[0x16];
	fgets(buf, 16, stdin);
	buf[strcspn(buf, "\0")] = 0;

	return atol(buf);
}

void generate_passphrase(char * buf, int nbytes) {
	FILE * f = fopen("/dev/urandom", "r");

	fread(buf, 1, nbytes, f);

	fclose(f);
}

void win() {
	system("/bin/sh");
}

void get_input(char * user_input, unsigned long user_len) {
	for (int i = 0 ; i < user_len ; i++) {
		int c = getchar();
		if (c == '\n') break;

		user_input[i] = c;
	}
}
