#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>

using namespace std;

//читання з файлу
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
//запис у файл
void outputf(ofstream& f, string a, string str) {
	f.open(str);
	if (f.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	f << a;
	f.close();
}
string  RUS(const string& DOS_string) {
	char* p_buf = new char[DOS_string.length() + 1];
	OemToCharA(DOS_string.c_str(), p_buf);
	string  res(p_buf);
	delete[] p_buf;
	return res;
}

int main() {
	setlocale(LC_ALL, "Russian");
	ifstream f;
	ofstream f1;
	string file_name, txt_before, txt_after;
	cout << "Enter the root to .txt file: ";
	cin >> file_name;
	txt_before = inputf(f, file_name);
	//cout << txt << endl;
	txt_after = txt_before;
	string key;
	string alphabet;
	int lengthOfText, lengthOfKey;
	lengthOfText = txt_before.length();
	int* OT = new int[lengthOfText];
	int* key_mas = new int[lengthOfText];
	int* CT = new int[lengthOfText];
	alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
	int lengthOfAlphabet = alphabet.length();
	int j, j1;
	int j2;
	while (true) {
		j2 = 0;
		cout << "Enter the key word: ";
		cin >> key;
		key = RUS(key);
		lengthOfKey = key.length();
		for (int i = 0; i < lengthOfText; i++) {
			j = alphabet.find(txt_before[i]);
			OT[i] = j;
		}
		/*for (int i = 0; i < lengthOfText; i++) {
			cout << OT[i] << "\t";
		}*/
		for (int i = 0; i < lengthOfText; i++, j2++) {
			if (j2 == lengthOfKey) {
				j2 = -1;
				i--;
			}
			else {
				j1 = alphabet.find(key[j2]);
				key_mas[i] = j1;
			}
		}
		/*cout << endl;
		for (int i = 0; i < lengthOfText; i++) {
			cout << key_mas[i] << "\t";
		}*/
		for (int i = 0; i < lengthOfText; i++) {
			CT[i] = (OT[i] + key_mas[i]) % lengthOfAlphabet;
		}
		/*cout << endl;
		for (int i = 0; i < lengthOfText; i++) {
			cout << CT[i] << "\t";
		}*/
		for (int i = 0; i < lengthOfText; i++) {
			txt_after[i] = alphabet[CT[i]];
		}
		cout << endl;
		cout << "New .txt is ready. Enter the root to it: ";
		cin >> file_name;
		outputf(f1, txt_after, file_name);
	}
}
