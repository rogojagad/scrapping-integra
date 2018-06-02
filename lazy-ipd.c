#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv){
	// run the spec
	char command[50];
	
	strcpy(command, "python auto-ipd/v2-auto-ipd.py");
	
	system(command);
}
