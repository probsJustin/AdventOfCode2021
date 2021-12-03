#pragma once
#include <string>
#include <vector>


std::vector<int> vectorStringSplitToInt(std::string stringToSplit, std::string delimiter) {
	std::vector<int> returnVector;
	size_t pos = 0;
	std::string token;
	while ((pos = stringToSplit.find(delimiter)) != std::string::npos) {
		token = stringToSplit.substr(0, pos);
		returnVector.push_back(std::stoi(token));
		stringToSplit.erase(0, pos + delimiter.length());
	}
	returnVector.push_back(std::stoi(stringToSplit));	
	return returnVector;
}

std::vector<std::string> vectorStringSplitToString(std::string stringToSplit, std::string delimiter) {
	std::vector<std::string> returnVector;
	size_t pos = 0;
	std::string token;
	while ((pos = stringToSplit.find(delimiter)) != std::string::npos) {
		token = stringToSplit.substr(0, pos);
		returnVector.push_back(token);
		stringToSplit.erase(0, pos + delimiter.length());
	}
	returnVector.push_back(stringToSplit);
	return returnVector;
}
