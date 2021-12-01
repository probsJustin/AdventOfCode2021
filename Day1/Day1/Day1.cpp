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

std::vector<int> vectorStringSplitToInt(string stringToSplit, string delimiter) {
	std::vector<int> returnVector; 
	size_t pos = 0;
	std::string token;
	while ((pos = stringToSplit.find(delimiter)) != std::string::npos) {
		token = stringToSplit.substr(0, pos);
		returnVector.push_back(std::stoi(token));
		stringToSplit.erase(0, pos + delimiter.length());
	}
	return returnVector; 
}

string part1(vector<int> inputVector) {
	int quantity = 0;
	for (int x = 0; x <= inputVector.size() - 1; x++) {
		if (x != 0) {
			if (inputVector[x - 1] < inputVector[x]) {
				quantity++;
			}
		}
	}
	cout << quantity << endl;
	return "done";
}

string part2(vector<int> inputVector) {
	vector<int> setOfSumsForSlidingWindow; 
	for (int x = 0; x <= inputVector.size() -1 ; x++) {
		if (x > 0 && x <= inputVector.size()-2) {
			setOfSumsForSlidingWindow.push_back(inputVector[x - 1] + inputVector[x] + inputVector[x + 1]);
		}
	}
	part1(setOfSumsForSlidingWindow);
	return "done";
}



int main() {
	part1(vectorStringSplitToInt(getPuzzleText("./puzzle.txt"), { '\n' }));
	part2(vectorStringSplitToInt(getPuzzleText("./puzzle.txt"), { '\n' }));
	system("pause");
	return 0;
}