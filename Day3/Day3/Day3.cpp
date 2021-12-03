#pragma once 
#include <iostream>
#include <string>
#include <vector>
#include "Header.h"
#include <fstream>
#include <streambuf>
#include <map>

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

void part1(vector<string> inputVector) {
	map<int, float> charArrayCounts;
	string finalBitGamma = ""; 
	string finalBitEpsilon = "";

	for (int y = 0; y < inputVector.size(); y++) {
		for (int x = 0; x <= inputVector[y].length()-1; x++) {
			charArrayCounts[x] = charArrayCounts[x] + ((int)inputVector[y][x] - '0');
		}
	}
	for (auto count : charArrayCounts) {
		if (count.second > (inputVector.size() - count.second)) {
			finalBitGamma += "1";
			finalBitEpsilon += "0";
		}else {
			finalBitGamma += "0";
			finalBitEpsilon += "1";
		}
	}

	cout << "Gamma: " << std::stoull(finalBitGamma, 0, 2) << endl;
	cout << "Epsilon: " << std::stoull(finalBitEpsilon, 0, 2) << endl;
	cout << "Answer: " << std::stoull(finalBitEpsilon, 0, 2) * std::stoull(finalBitGamma, 0, 2) << endl;
}



int main() {
	part1(vectorStringSplitToString(getPuzzleText("./puzzle.txt"), { '\n' }));
	system("pause");
	return 0;
}