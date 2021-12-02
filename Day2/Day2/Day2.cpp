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
	vector<string> parsedPuzzle = inputVector;
	vector<vector<string>> fullParsedPuzzle;

	map<string, int> position; 
	position["forward"] = 0; 
	position["up"] = 0; 
	position["down"] = 0; 

	for (int i = 0; i < parsedPuzzle.size(); i++) {
		fullParsedPuzzle.push_back(vectorStringSplitToString(parsedPuzzle[i], { ' ' }));
	}

	for (int x = 0; x <= fullParsedPuzzle.size() - 2; x++) {
		for (int y = 0; y <= fullParsedPuzzle[x].size() - 2; y = y + 2) {
				position[fullParsedPuzzle[x][y]] = position[fullParsedPuzzle[x][y]] + stoi(fullParsedPuzzle[x][y + 1]);
		}
	}

	cout << "Part1 Answer:"  << (position["down"] - position["up"]) * position["forward"] << endl;
}

void part2(vector<string> inputVector) {

	map<string, int> position;
	position["aim"] = 0;
	position["depth"] = 0;
	position["horizontal"] = 0;

	vector<string> parsedPuzzle = inputVector;
	vector<vector<string>> fullParsedPuzzle;
	for (int i = 0; i < parsedPuzzle.size(); i++) {
		fullParsedPuzzle.push_back(vectorStringSplitToString(parsedPuzzle[i], { ' ' }));
	}

	for (int x = 0; x <= fullParsedPuzzle.size() - 2; x++) {
		for (int y = 0; y <= fullParsedPuzzle[x].size() - 2; y = y + 2) {
			switch (fullParsedPuzzle[x][y][0]) {
				case 'u': {
					position["aim"] = position["aim"] - stoi(fullParsedPuzzle[x][y + 1]);
					break;
				}
				case 'd': {
					position["aim"] = position["aim"] + stoi(fullParsedPuzzle[x][y + 1]);
					break;
				}
				case 'f': {
					position["horizontal"] = position["horizontal"] + stoi(fullParsedPuzzle[x][y + 1]);
					position["depth"] = position["depth"] + (position["aim"] * stoi(fullParsedPuzzle[x][y + 1]));
					break;
				}
			}

		}
	}
	cout << "Part2 Answer:" << position["horizontal"] * position["depth"] << endl;

}

int main() {
	part1(vectorStringSplitToString(getPuzzleText("./puzzle.txt"), { '\n' }));
	part2(vectorStringSplitToString(getPuzzleText("./puzzle.txt"), { '\n' }));

	system("pause");
	return 0;
}