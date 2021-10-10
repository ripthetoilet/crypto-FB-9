#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>
#include <clocale>
#include <fstream>
#include <windows.h>
#include <math.h>

using namespace std;

//читання з файлу
string inputf(ifstream& f, char str[40]) {
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
void outputf(ofstream& f, string a, char str[40]) {
	f.open(str);
	if (f.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	f << a;
	f.close();
}

double withIntersection(string** a_bigram, int lengthOfArray, string txt_filtered, int lengthOfText, ofstream& f1, char str[40], string alphabet) {
	string bigram = "";
	char sym1;
	char sym2;
	//цикл на заповнення біграм алфавіту
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			sym1 = alphabet[r];
			sym2 = alphabet[c];
			string bi1(1, sym1);
			string bi2(1, sym2);
			bigram = bi1 + bi2;
			a_bigram[r][c] = bigram;
		}
	}
	int** counter = new int* [lengthOfArray];
	string** sa_frequencyOfBi = new string * [lengthOfArray];
	double** a_frequencyOfBi = new double* [lengthOfArray];
	for (int i = 0; i < lengthOfArray; i++) {
		counter[i] = new int[lengthOfArray];
		sa_frequencyOfBi[i] = new string[lengthOfArray];
		a_frequencyOfBi[i] = new double[lengthOfArray];
	}
	for (int i = 0; i < lengthOfArray; i++) {
		for (int j = 0; j < lengthOfArray; j++) {
			counter[i][j] = 0;
		}
	}

	int j1, j2;
	//цикл на підрахунок біграм (так як крок і=і+1 - біграми з перетином)
	for (int i = 0; i < lengthOfText; i++) {
		j1 = alphabet.find(txt_filtered[i]);
		j2 = alphabet.find(txt_filtered[i + 1]);
		counter[j1][j2]++;
	}
	double frequencyOfBi;
	//цикл на підрахунок частоти кожної біграми
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			frequencyOfBi = (counter[r][c] * 1.0) / (lengthOfText - 1);
			//заповнення додаткової стрінгової матриці, яку ми запишемо у файл
			sa_frequencyOfBi[r][c] = a_bigram[r][c] + ": " + to_string(frequencyOfBi) + " ";
			a_frequencyOfBi[r][c] = frequencyOfBi;
		}
	}
	//запис матриці у файл
	f1.open(str);
	if (f1.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	for (int r = 0; r < lengthOfArray; ++r) {
		f1 << endl;
		for (int c = 0; c < lengthOfArray; ++c) {
			f1 << setw(10) << sa_frequencyOfBi[r][c];
		}
	}

	f1.close();
	double entropy = 0;
	double logarifm;
	//цикл на знаходження ентропії
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			logarifm = log10(a_frequencyOfBi[r][c]) / log10(2);
			//у тому випадку, коли частота біграми=0, логаріфм дорівнюватиме нескінченності
			if (logarifm == -INFINITY) {
				logarifm = 0;//запишемо через нуль для зручності(адже ми все одно будемо множити на нуль)
			}
			logarifm = a_frequencyOfBi[r][c] * logarifm;
			entropy = entropy + logarifm;
		}
	}
	entropy = (entropy * (-1)) / 2;
	return entropy;
}

double matrix(string** a_bigram, int lengthOfArray, string txt_filtered, int lengthOfText, ofstream& f1, char str[40], string alphabet) {
	string bigram = "";
	char sym1;
	char sym2;
	//цикл на заповнення біграм алфавіту
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			sym1 = alphabet[r];
			sym2 = alphabet[c];
			string bi1(1, sym1);
			string bi2(1, sym2);
			bigram = bi1 + bi2;
			a_bigram[r][c] = bigram;
		}
	}
	int** counter = new int* [lengthOfArray];
	string** sa_frequencyOfBi = new string * [lengthOfArray];
	double** a_frequencyOfBi = new double* [lengthOfArray];
	for (int i = 0; i < lengthOfArray; i++) {
		counter[i] = new int[lengthOfArray];
		sa_frequencyOfBi[i] = new string[lengthOfArray];
		a_frequencyOfBi[i] = new double[lengthOfArray];
	}
	for (int i = 0; i < lengthOfArray; i++) {
		for (int j = 0; j < lengthOfArray; j++) {
			counter[i][j] = 0;
		}
	}

	int j1, j2;
	//цикл на підрахунок біграм (так як крок і=і+2 - біграми без перетину)
	for (int i = 0; i < lengthOfText; i = i + 2) {
		j1 = alphabet.find(txt_filtered[i]);
		j2 = alphabet.find(txt_filtered[i + 1]);
		counter[j1][j2]++;
	}
	double frequencyOfBi;
	//цикл на підрахунок частоти кожної біграми
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			frequencyOfBi = (counter[r][c] * 1.0) / (lengthOfText / 2);
			sa_frequencyOfBi[r][c] = a_bigram[r][c] + ": " + to_string(frequencyOfBi) + " ";
			a_frequencyOfBi[r][c] = frequencyOfBi;
		}
	}
	//запис матриці у файл
	f1.open(str);
	if (f1.fail()) {
		cout << "\n Fail to open the file";
		exit(1);
	}
	for (int r = 0; r < lengthOfArray; ++r) {
		f1 << endl;
		for (int c = 0; c < lengthOfArray; ++c) {
			f1 << setw(10) << sa_frequencyOfBi[r][c];
		}
	}
	f1.close();

	double entropy = 0;
	double logarifm;
	//цикл на знаходження ентропії
	for (int r = 0; r < lengthOfArray; ++r) {
		for (int c = 0; c < lengthOfArray; ++c) {
			logarifm = log10(a_frequencyOfBi[r][c]) / log10(2);
			if (logarifm == -INFINITY) {
				logarifm = 0;
			}
			logarifm = a_frequencyOfBi[r][c] * logarifm;
			entropy = entropy + logarifm;
		}
	}
	entropy = (entropy * (-1)) / 2;
	return entropy;
}

double entropy(double* a, int lengthOfArray) {
	double entropy = 0;
	double logarifm;
	for (int i = 0; i < lengthOfArray; i++) {
		logarifm = log10(a[i]) / log10(2);
		logarifm = a[i] * logarifm;
		entropy = entropy + logarifm;
	}
	entropy = entropy * (-1);
	return entropy;
}

string sorted_txt(int lengthOfArray, string txt_filtered, int* a_quantityOfSym, int lengthOfText, string* as_frequencyOfSym, double* a_frequencyOfSym, string alphabet) {
	double frequencyOfSym;
	char symbol;
	string frequencyWithSym = "";
	string frequencySorted = "";
	//цикл на підрахунок усіх літер в тексті(від а до я)
	for (int i = 0; i < lengthOfArray; i++) {
		symbol = alphabet[i];
		const auto count_symbol = count(txt_filtered.cbegin(), txt_filtered.cend(), symbol);
		a_quantityOfSym[i] = count_symbol;//запис кі-сті літер у масив
	}
	//цикл на підрахунок частоти кожної літери
	for (int i = 0; i < lengthOfArray; i++) {
		frequencyOfSym = (a_quantityOfSym[i] * 1.0) / lengthOfText;
		a_frequencyOfSym[i] = frequencyOfSym;//запис частоти кожної літери у масив
		as_frequencyOfSym[i] = to_string(frequencyOfSym) + " (" + alphabet[i] + ")";//запис частоти і відповідної літери у масив
	}
	for (int i = 0; i < lengthOfArray; i++) {
		frequencyWithSym = frequencyWithSym + as_frequencyOfSym[i] + "\n";
	}
	//цикл на сортування масиву із частотами
	for (int i = 0; i < lengthOfArray-1; ++i) {
		int bigger = i;
		for (int j = i + 1; j < lengthOfArray; ++j) {
			if (a_frequencyOfSym[j] > a_frequencyOfSym[bigger]) {
				bigger = j;
			}
		}
		swap(a_frequencyOfSym[i], a_frequencyOfSym[bigger]);
	}
	for (int i = 0; i < lengthOfArray; i++) {
		frequencySorted = frequencySorted + to_string(a_frequencyOfSym[i]) + "\n";
	}
	txt_filtered = frequencyWithSym + "\n" + "Sorted:" + "\n" + frequencySorted;
	return txt_filtered;
}

int main() {
	setlocale(LC_ALL, "Russian");
	string txt_before, txt_after;
	string txt_sorted, txt_filtered;
	ifstream f;
	ofstream f1;
	char str1[40], str2[40];
	/*cout << "Enter the root to .txt file: ";
	cin >> str1;
	txt_before = inputf(f, str1);
	txt_after = txt_before;

	//фільтрація тексту(щоб залишилися пробіли)
	for (int i = 0; i < txt_after.length(); i++) {
		//cout << a[i] << endl;
		if (txt_after[i] == ' ') {
			txt_after.replace(i, 1, "q");
		}
	}
	txt_after.erase(remove_if(txt_after.begin(), txt_after.end(), [](char c) { return !isalpha((unsigned char)c); }), txt_after.end());
	for (int i = 0; i < txt_after.length(); i++) {
		//cout << a[i] << endl;
		if (txt_after[i] == 'q') {
			txt_after.replace(i, 1, " ");
		}
	}
	char chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (unsigned int i = 0; i < strlen(chars); ++i) {
		txt_after.erase(remove(txt_after.begin(), txt_after.end(), chars[i]), txt_after.end());
	}
	for (int i = txt_after.size() - 1; i >= 0; i--) {
		if (txt_after[i] == ' ' && txt_after[i] == txt_after[i - 1]) {
			txt_after.erase(txt_after.begin() + i);
		}
	}
	transform(txt_after.begin(), txt_after.end(), txt_after.begin(), tolower);*/

	//фільтрація тексту(без пробілів)
	/*txt_after.erase(remove_if(txt_after.begin(), txt_after.end(), [](char c) { return !isalpha((unsigned char)c); }), txt_after.end());
	char chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (unsigned int i = 0; i < strlen(chars); ++i) {
		txt_after.erase(std::remove(txt_after.begin(), txt_after.end(), chars[i]), txt_after.end());
	}
	//верхній регістр->нижній регістр
	transform(txt_after.begin(), txt_after.end(), txt_after.begin(), tolower);

	cout << "New .txt is ready. Enter the root to it: ";
	cin >> str2;
	outputf(f1, txt_after, str2);*/

	string alphabet;
	int lengthOfText;
	int lengthOfArray;
	//зчитуємо змінений файл
	cout << "Enter the name of filtered txt(without spaces): ";
	cin >> str1;
	txt_filtered = inputf(f, str1);
	alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя";
	lengthOfArray = alphabet.length();
	lengthOfText = txt_filtered.length();
	cout << "Length of new txt: " << lengthOfText << " symbols" << endl;
	string* as_frequencyOfSym = new string[lengthOfArray];
	int* a_quantityOfSym = new int[lengthOfArray];
	double* a_frequencyOfSym = new double[lengthOfArray];
	txt_sorted = sorted_txt(lengthOfArray, txt_filtered, a_quantityOfSym, lengthOfText, as_frequencyOfSym, a_frequencyOfSym, alphabet);
	cout << "The frequency of symbols in the new .txt has been sorted. Enter the root to it: ";
	cin >> str2;
	outputf(f1, txt_sorted, str2);
	cout << "Entropy(symbol frequencies): " << entropy(a_frequencyOfSym, lengthOfArray) << endl;

	string** a_bigram = new string*[lengthOfArray];
	for (int i = 0; i < lengthOfArray; i++) {
		a_bigram[i] = new string[lengthOfArray];
	}
	cout << "The frequency of bigrams(with intersection) has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies with intersection): " << withIntersection(a_bigram, lengthOfArray, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;

	cout << "The frequency of bigrams has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies): " << matrix(a_bigram, lengthOfArray, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;

	cout << "Enter the name of filtered txt(with spaces): ";
	cin >> str1;
	txt_filtered = inputf(f, str1);
	alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя ";
	lengthOfArray = alphabet.length();
	lengthOfText = txt_filtered.length();
	cout << "Length of new txt: " << lengthOfText << " symbols" << endl;
	string* as_frequencyOfSym2 = new string[lengthOfArray];
	int* a_quantityOfSym2 = new int[lengthOfArray];
	double* a_frequencyOfSym2 = new double[lengthOfArray];
	txt_sorted = sorted_txt(lengthOfArray, txt_filtered, a_quantityOfSym2, lengthOfText, as_frequencyOfSym2, a_frequencyOfSym2, alphabet);
	cout << "The frequency of symbols in the new .txt has been sorted. Enter the root to it: ";
	cin >> str2;
	outputf(f1, txt_sorted, str2);
	cout << "Entropy(symbol frequencies): " << entropy(a_frequencyOfSym2, lengthOfArray) << endl;

	string** a_bigram2 = new string * [lengthOfArray];
	for (int i = 0; i < lengthOfArray; i++) {
		a_bigram2[i] = new string[lengthOfArray];
	}
	cout << "The frequency of bigrams(with intersection) has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies with intersection): " << withIntersection(a_bigram2, lengthOfArray, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;

	cout << "The frequency of bigrams has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies): " << matrix(a_bigram2, lengthOfArray, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;
}
