#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
	//Bool is just an int, we only set it to True or False
	//Is this put before or after the array in memory?
	bool are_we_admin = false;
	// Another array
	char array[16];
	bool are_we_really_admin = false;

	int index;
	puts("Enter the first index");
	scanf("%d", &index);

	//????
	array[index] = true;

	puts("Enter the second index");
	scanf("%d", &index);
	array[index] = true;
	
	if (are_we_admin == true) {
		if (are_we_really_admin == true) {
			puts("Congrats epic hackerzz");
		} else {
			//IGNORE - dont need to understand, just for correctness
			goto fail;
		}
	} else {
fail:
		puts("Looks like you wont be getting any super secret info :((");
		// Dont need to understand this
		printf("are_we_admin was %s, are_we_really_admin was %s.\n", 
			are_we_admin ? "true" : "false",
			are_we_really_admin ? "true" : "false");
		puts("Try setting both to true.");
	}
}
