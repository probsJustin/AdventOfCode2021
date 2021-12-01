#pragma once 
#include <iostream>
#include <string>
#include <vector>
#include "Header.h"
#include <fstream>
#include <streambuf>

using namespace std;

string getPuzzleText(string fileLocation) {
	std::ifstream t(fileLocation);
	std::string str;

	t.seekg(0, std::ios::end);
	str.reserve(t.tellg());
	t.seekg(0, std::ios::beg);

	str.assign((std::istreambuf_iterator<char>(t)),
		std::istreambuf_iterator<char>());

	return str; 
}



int main() {

	system("pause");
	return 0;
}