#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void create_admin();
void print_menu();
int get_int();

struct user {
	int id;
};

unsigned char next_id = 0;

int main(void) {
	int user_choice;
	struct user u;
	char cmd[0x40];

	create_admin();
	
	while (true) {
		print_menu();
		user_choice = get_int();

		switch (user_choice) {
			case 1:
				u.id = next_id++;
				printf("id is %d\n", u.id);
				break;
				
			case 2:
				fgets(cmd, 0x40, stdin);

				if (u.id == 0) {
					system(cmd);
				} else {
					printf("%s", cmd);
				}
				break;

			default:
				continue;
		}
	}
}

void create_admin() {
	next_id++;
}

void print_menu() {
	puts("1. Create user");
	puts("2. Evaluate command");
	printf("> ");
}

int get_int() {
	char buf[0x4];
	fgets(buf, 4, stdin);
	buf[strcspn(buf, "\0")] = 0;

	return atoi(buf);
}
