#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

string inputf(ifstream& f, string str) {
	string a;
	f.open(str);
	if (f.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	string extra = "";
	while (getline(f, a)) {
		extra += a;
	}
	f >> extra;
	f.close();
	return extra;
}
void outputf(ofstream& f, string a, string str) {
	f.open(str);
	if (f.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	f << a;
	f.close();
}
void f_quantityOfSym(int* quantityOfSym, int lengthOfAlphabet, string alphabet, string txt) {
	char symbol;
	for (int i = 0; i < lengthOfAlphabet; i++) {
		symbol = alphabet[i];
		const auto count_symbol = count(txt.cbegin(), txt.cend(), symbol);
		//cout << alphabet[i] << ": " << count_symbol << endl;
		quantityOfSym[i] = count_symbol;//запис кі-сті літер у масив
	}
}
double f_index_OT(int lengthOfText, int* quantityOfSym, int lengthOfAlphabet, double index_OT) {
	double extra;
	extra = 1.0 / (lengthOfText * (lengthOfText - 1));
	for (int i = 0; i < lengthOfAlphabet; i++) {
		index_OT = index_OT + (quantityOfSym[i] * (quantityOfSym[i] - 1));
	}
	index_OT = index_OT * extra;
	return index_OT;
}
int max_quantityOfSym(int* quantityOfSym, int lengthOfAlphabet) {
	int maximum = 0;
	for (int i = 0; i < lengthOfAlphabet; i++) {
		maximum = max(maximum, quantityOfSym[i]);
	}
	//cout << "Max: " << maximum << endl;
	for (int i = 0; i < lengthOfAlphabet; i++) {
		if (quantityOfSym[i] == maximum) {
			return i;
		}
	}
}
string find_key(vector<int> max_sym, int letter_place, int lengthOfKey, int lengthOfAlphabet, string alphabet, string key) {
	key = "";
	int placeOfKey = 0;
	for (int i = 0; i < lengthOfKey; i++) {
		//cout << max_sym[i] << " - " << alphabet[max_sym[i]] << endl;
		placeOfKey = (max_sym[i] - letter_place);
		if (placeOfKey < 0) {
			placeOfKey = lengthOfAlphabet + placeOfKey;
		}
		placeOfKey = placeOfKey % lengthOfAlphabet;
		//cout << "keyPlace: " << placeOfKey << endl;
		//cout << alphabet[placeOfKey] << endl;
		key = key + alphabet[placeOfKey];
	}
	//cout << "Key: " << key << endl;
	return key;
}

int main() {
	setlocale(LC_ALL, "Russian");
	ifstream f;
	ofstream f1;
	string file_name, txt_before, txt_after;
	cout << "Enter the root to .txt file: ";
	cin >> file_name;
	txt_before = inputf(f, file_name);
	string alphabet, key_block;
	alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
	int lengthOfAlphabet = alphabet.length();
	int lengthOfText, lengthOfKey;
	lengthOfText = txt_before.length();

	//знаходження довжини ключа
	/*while (true) {
		cout << "Enter the length of r: ";
		cin >> lengthOfKey;
		string* block = new string[lengthOfKey];
		int extra;
		//cout << txt_before << endl;
		for (int rows = 0; rows < lengthOfKey; rows++) {
			key = "";
			extra = rows;
			while (rows < lengthOfText) {
				key = key + txt_before[rows];
				rows = rows + lengthOfKey;
			}
			rows = extra;
			block[rows] = key;
		}
		cout << endl;
		int* quantityOfSym = new int[lengthOfAlphabet];
		double index_OT = 0;
		for (int i = 0; i < lengthOfKey; i++) {
			//cout << block[i] << endl;
			f_quantityOfSym(quantityOfSym, lengthOfAlphabet, alphabet, block[i]);
			index_OT = f_index_OT(block[i].length(), quantityOfSym, lengthOfAlphabet, index_OT);
			cout << "Index of Open Text: " << index_OT << endl;
		}
		delete[] block;
	}*/

	//теоретичне значення I
	/*double math_hope = 0;
	double freq;
	for (int i = 0; i < 31; i++) {
		cin >> freq;
		//cout << freq << endl;
		math_hope = math_hope + (freq * freq);
		//cout << math_hope << endl;
	}
	cout << endl;
	cout << math_hope << endl;*/

	cout << "Enter the length of r: ";
	cin >> lengthOfKey;
	string* block = new string[lengthOfKey];
	int extra;
	//cout << txt_before << endl;
	for (int rows = 0; rows < lengthOfKey; rows++) {
		key_block = "";
		extra = rows;
		while (rows < lengthOfText) {
			key_block = key_block + txt_before[rows];
			rows = rows + lengthOfKey;
		}
		rows = extra;
		block[rows] = key_block;
	}
	cout << endl;
	int* quantityOfSym = new int[lengthOfAlphabet];
	double index_OT = 0;
	vector<int> max_sym;
	string key;
	for (int i = 0; i < lengthOfKey; i++) {
		//cout << block[i] << endl;
		f_quantityOfSym(quantityOfSym, lengthOfAlphabet, alphabet, block[i]);
		max_sym.push_back(max_quantityOfSym(quantityOfSym, lengthOfAlphabet));
		//index_OT = f_index_OT(block[i].length(), quantityOfSym, lengthOfAlphabet, index_OT);
		//cout << "Index of Open Text: " << index_OT << endl;
	}
	/*for (int i = 0; i < lengthOfKey; i++) {
		cout << "Symbol: " << alphabet[max_sym[i]] << endl;
	}*/
	for (int i = 0; i < lengthOfAlphabet; i++) {
		key = find_key(max_sym, i, lengthOfKey, lengthOfAlphabet, alphabet, key);
		cout << "Key[" << alphabet[i] << "]: " << key << endl;
	}
	key = "войнамагаэндшпиль";
	txt_after = txt_before;
	int place_of_key = 0;
	int extra_k;
	//cout << txt_before << endl;
	for (int rows = 0; rows < lengthOfKey; rows++) {
		extra_k = rows;
		while (rows < lengthOfText) {
			//cout << alphabet.find(txt_before[rows]) << endl;
			//cout << alphabet.find(key[extra_k]) << endl;
			place_of_key = (alphabet.find(txt_before[rows]) - alphabet.find(key[extra_k]));
			//cout << place_of_key << endl;
			if (place_of_key < 0) {
				place_of_key = lengthOfAlphabet + place_of_key;
			}
			place_of_key = (place_of_key % lengthOfAlphabet);
			//cout << "%: " << place_of_key << endl;
			//cout << alphabet[place_of_key] << endl;
			txt_after[rows] = alphabet[place_of_key];
			rows = rows + lengthOfKey;
		}
		rows = extra_k;
	}
	cout << endl;
	//cout << txt_before << endl;
	cout << txt_after << endl;
	cout << endl;
	cout << "New .txt is ready. Enter the root to it: ";
	cin >> file_name;
	outputf(f1, txt_after, file_name);
}
