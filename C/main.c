#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

// Return 1 if there's alphabetic characters in string, else return 0.
int hasAlpha(char * string){
	char ch = string[0];
	int i = 0;
	while (ch != '\0') {
		if(isalpha(ch))
			return 1;
		ch = string[++i];
	}
	return 0;
}

// Return 1 if there's a space in string, else return 0.
int hasSpace(char * string) {
	char ch = string[0];
	int i = 0;
	while (ch != '\0') {
		if(isspace(ch))
			return 1;
		ch = string[++i];
	}
	return 0;
}

/* Return 1 is addr is a valid IP address, return 0 otherwise */
int is_valid_ip(const char * addr) {
	char * token;
	char * duplicate = malloc(strlen(addr) * sizeof(char));
	strcpy(duplicate, addr);
	int scount = 0;
	token = strtok(duplicate, ".");
	while(token != NULL) {
		if(atoi(token) >= 0 && atoi(token) <= 255 && (token[0] != '0' || strlen(token) == 1) && !hasAlpha(token) && !hasSpace(token))
			scount++;
		token = strtok(NULL,".");
	}
	free(duplicate);
	if(scount == 4)
		return 1;
	else
		return 0;
}

int main() {
	printf("%d\n", is_valid_ip("192.168.0.1"));
}