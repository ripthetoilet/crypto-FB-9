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

double withIntersection(string a_bigram[31][31], string txt_filtered, int lengthOfText, ofstream& f1, char str[40], string alphabet) {
	int counter[31][31] = { 0 };
	int j1, j2;
	//цикл на підрахунок біграм (так як крок і=і+1 - біграми з перетином)
	for (int i = 0; i < lengthOfText; i++) {
		j1 = alphabet.find(txt_filtered[i]);
		j2 = alphabet.find(txt_filtered[i + 1]);
		counter[j1][j2]++;
	}
	string sa_frequencyOfBi[31][31];
	double a_frequencyOfBi[31][31];
	double frequencyOfBi;
	//цикл на підрахунок частоти кожної біграми
	for (int r = 0; r < 31; ++r) {
		for (int c = 0; c < 31; ++c) {
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
	for (int r = 0; r < 31; ++r) {
		f1 << endl;
		for (int c = 0; c < 31; ++c) {
			f1 << setw(10) << sa_frequencyOfBi[r][c];
		}
	}
	f1.close();

	double entropy = 0;
	double logarifm;
	//цикл на знаходження ентропії
	for (int r = 0; r < 31; ++r) {
		for (int c = 0; c < 31; ++c) {
			logarifm = log10(a_frequencyOfBi[r][c]) / log10(2);
			//у тому випадку, коли частота біграми=0, логаріфм дорівнюватиме нескінченності
			if (logarifm == -INFINITY) {
				logarifm = 0;//запишемо через нуль для зручності(адже ми все одно будемо множити на нуль)
			}
			logarifm = a_frequencyOfBi[r][c] * logarifm;
			entropy = entropy + logarifm;
		}
	}
	entropy = entropy * (-1);
	return entropy;
}

double matrix(string a_bigram[31][31], string txt_filtered, int lengthOfText, ofstream& f1, char str[40], string alphabet) {
	int counter[31][31] = { 0 };
	int j1, j2;
	//цикл на підрахунок біграм (так як крок і=і+2 - біграми без перетину)
	for (int i = 0; i < lengthOfText; i = i + 2) {
		j1 = alphabet.find(txt_filtered[i]);
		j2 = alphabet.find(txt_filtered[i + 1]);
		counter[j1][j2]++;
	}
	string sa_frequencyOfBi[31][31];
	double a_frequencyOfBi[31][31];
	double frequencyOfBi;
	//цикл на підрахунок частоти кожної біграми
	for (int r = 0; r < 31; ++r) {
		for (int c = 0; c < 31; ++c) {
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
	for (int r = 0; r < 31; ++r) {
		f1 << endl;
		for (int c = 0; c < 31; ++c) {
			f1 << setw(10) << sa_frequencyOfBi[r][c];
		}
	}
	f1.close();

	double entropy = 0;
	double logarifm;
	//цикл на знаходження ентропії
	for (int r = 0; r < 31; ++r) {
		for (int c = 0; c < 31; ++c) {
			logarifm = log10(a_frequencyOfBi[r][c]) / log10(2);
			if (logarifm == -INFINITY) {
				logarifm = 0;
			}
			logarifm = a_frequencyOfBi[r][c] * logarifm;
			entropy = entropy + logarifm;
		}
	}
	entropy = entropy * (-1);
	return entropy;
}

double entropy(double a[31]) {
	double entropy = 0;
	double logarifm;
	for (int i = 0; i < 31; i++) {
		logarifm = log10(a[i]) / log10(2);
		logarifm = a[i] * logarifm;
		entropy = entropy + logarifm;
	}
	entropy = entropy * (-1);
	return entropy;
}

int main() {
	setlocale(LC_ALL, "Russian");
	string txt_before, txt_after;
	string txt_sorted, txt_filtered;
	ifstream f;
	ofstream f1;
	char str1[40], str2[40];
	cout << "Enter the root to .txt file: ";
	/*cin >> str1;
	txt_before = inputf(f, str1);
	txt_after = txt_before;

	//фільтрація тексту
	txt_after.erase(remove_if(txt_after.begin(), txt_after.end(), [](char c) { return !isalpha((unsigned char)c); }), txt_after.end());
	char chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (unsigned int i = 0; i < strlen(chars); ++i) {
		txt_after.erase(std::remove(txt_after.begin(), txt_after.end(), chars[i]), txt_after.end());
	}
	//верхній регістр->нижній регістр
	transform(txt_after.begin(), txt_after.end(), txt_after.begin(), tolower);

	cout << "New .txt is ready. Enter the root to it: ";
	cin >> str2;
	outputf(f1, txt_after, str2);*/
	//зчитуємо змінений файл
	cin >> str1;
	txt_filtered = inputf(f, str1);
	string alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя";
	int lengthOfText = txt_filtered.length();
	cout << "Length of new txt: " << lengthOfText << " symbols" << endl;
	string as_frequencyOfSym[31];
	int a_quantityOfSym[31];
	double a_frequencyOfSym[31];
	double frequencyOfSym;
	char symbol;
	//цикл на підрахунок усіх літер в тексті(від а до я)
	for (int i = 0; i < alphabet.length(); i++) {
		symbol = alphabet[i];
		const auto count_symbol = count(txt_filtered.cbegin(), txt_filtered.cend(), symbol);
		a_quantityOfSym[i] = count_symbol;//запис кі-сті літер у масив
	}
	//цикл на підрахунок частоти кожної літери
	for (int i = 0; i < 31; i++) {
		frequencyOfSym = (a_quantityOfSym[i] * 1.0) / lengthOfText;
		a_frequencyOfSym[i] = frequencyOfSym;//запис частоти кожної літери у масив
		as_frequencyOfSym[i] = to_string(frequencyOfSym) + " (" + alphabet[i] + ")";//запис частоти і відповідної літери у масив
	}
	string frequencyWithSym = "";
	for (int i = 0; i < 31; i++) {
		frequencyWithSym = frequencyWithSym + as_frequencyOfSym[i] + "\n";
	}
	//цикл на сортування масиву із частотами
	for (int i = 0; i < 30; ++i) {
		int bigger = i;
		for (int j = i + 1; j < 31; ++j) {
			if (a_frequencyOfSym[j] > a_frequencyOfSym[bigger]) {
				bigger = j;
			}
		}
		swap(a_frequencyOfSym[i], a_frequencyOfSym[bigger]);
	}
	string frequencySorted = "";
	for (int i = 0; i < 31; i++) {
		frequencySorted = frequencySorted + to_string(a_frequencyOfSym[i]) + "\n";
	}
	txt_sorted = frequencyWithSym + "\n" + "Sorted:" + "\n" + frequencySorted;
	/*cout << "The frequency of symbols in the new .txt has been sorted. Enter the root to it: ";
	cin >> str2;
	outputf(f1, txt_sorted, str2);*/
	cout << "Entropy(symbol frequencies): " << entropy(a_frequencyOfSym) << endl;

	const int numRows = 31;
	const int numCols = 31;
	string a_bigram[numRows][numCols];
	string bigram = "";
	char sym1;
	char sym2;
	//цикл на заповнення біграм алфавіту
	for (int r = 0; r < numRows; ++r) {
		for (int c = 0; c < numCols; ++c) {
			sym1 = alphabet[r];
			sym2 = alphabet[c];
			string bi1(1, sym1);
			string bi2(1, sym2);
			bigram = bi1 + bi2;
			a_bigram[r][c] = bigram;
		}
	}

	cout << "The frequency of bigrams(with intersection) has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies with intersection): " << withIntersection(a_bigram, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;


	cout << "The frequency of bigrams has been written. Enter the root to it: ";
	cin >> str2;
	cout << "Entropy(bigram frequencies): " << matrix(a_bigram, txt_filtered, lengthOfText, f1, str2, alphabet) << endl;
}
