#include <iostream>
#include <fstream>
#include <vector>
#include <array>
//#define mode

using namespace std;

string encrypt(string text, string key)
{
	string cipher = text;
	
	for (int i = 0; i < text.length(); i++)
	{
		int c = text[i] + key[i % key.length()];
		
		if (c < -32)
		{
			c += 32;
		}

		cipher[i] = c;
	}

	return cipher;
}

string decrypt(string cipher, string key)
{
	string text = cipher;

	for (int i = 0; i < cipher.length(); i++)
	{
		int t = cipher[i] - key[i % key.length()];

		if (t >= 0)
		{
			t -= 32;
		}

		text[i] = t;
	}

	return text;
}

vector<string> make_blocks(string text, int r)
{
	vector<string> blocks;

	for (int i = 0; i < r; i++)
	{
		string block;

		for (int j = i; j < text.length(); j += r)
		{
			block += text[j];
		}

		blocks.push_back(block);
	}

	return blocks;
}

array<int, 32> get_frequencies(string text)
{
	array<int, 32> frequencies = {};

	for (int i = 0; i < 32; i++)
	{
		frequencies[i] = 0;
	}

	for (int i = 0; i < text.length(); i++)
	{
		frequencies[text[i] + 32]++;
	}

	ofstream fout("output.txt", fstream::app);

	for (int j = 0; j < 32; j++)
	{
		fout << frequencies[j] << "\t";
	}

	fout << endl;

	fout.close();

	return frequencies;
}

char get_most(array<int, 32> frequencies)
{
	int max_id = 0;
	int max = frequencies[0];

	for (int j = 1; j < 32; j++)
	{
		if (max < frequencies[j])
		{
			max = frequencies[j];
			max_id = j;
		}
	}

	return max_id - 32;
}

void check_indexes(string cipher, int r)
{
	ofstream fout("output.txt");

	for (int i = 0; i < 32; i++)
	{
		fout << char(i - 32) << "\t";
	}

	fout << endl;

	fout.close();

	vector<string> blocks = make_blocks(cipher, r);

	float avg_index = 0;

	for (int i = 0; i < r; i++)
	{
		int n = blocks[i].length();
		
		array<int, 32> frequencies = get_frequencies(blocks[i]);

		float index = 0;

		for (int j = 0; j < 32; j++)
		{
			index += frequencies[j] * (frequencies[j] - 1);
		}

		index /= (n * (n - 1));

		//cout << "index for block " << i + 1 << " = " << index << endl;

		avg_index += index;

		//cout << "most char for block " << i + 1 << " = " << get_most(frequencies) << endl;
	}

	avg_index /= r;

	cout << "for r = " << r << "avg index = " << avg_index << endl;
}

void check_kronekera(string cipher, int r)
{
	int d = 0;

	for (int i = 0; i < cipher.length() - r; i++)
	{
		d += cipher[i] == cipher[i + r];
	}

	cout << "for r = " << r << " kroneker = " << d << endl;

	ofstream fout("output.txt");

	for (int i = 0; i < 32; i++)
	{
		fout << char(i - 32) << "\t";
	}

	fout << endl;

	fout.close();
}

void part1()
{
	ifstream fin("text.txt");

	string text = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя";
	
	fin >> text;

	fin.close();

	string keys[] = { 
		"па", //0, 2
		"твр", //1, 3
		"ънот", //2, 4
		"яэгжн", //3, 5
		"цпукснфщих", //4, 10
		"уърьбеоахзр", //5, 11
		"мябыьщуевяъд", //6, 12
		"ибчжчцтгчфяпш", //7, 13
		"эафсылазрнырзп", //8, 14
		"ьшпшьгйфлфафбощ", //9, 15
		"хшщлеширгушьзуыо", //10, 16
		"врцезжзфкжмщзмалж", //11, 17
		"сзтювмышсимцкжхуйе", //12, 18
		"имкюкабжкфлцсъдйытъ", //13, 19
		"жесвязвкщелпнасротюв" //14, 20
	};

	check_indexes(text, 1);

	for (int i = 0; i < 15; i++)
	{
		string key = keys[i];

		string cipher = encrypt(text, key);

		check_indexes(cipher, 1);
	}
}

void part2()
{
	ifstream fin("cipher.txt");

	string cipher;

	fin >> cipher;

	fin.close();

	/*for (int i = 1; i < 21; i++)
	{
		check_indexes(cipher, i);
	}*/

	/*for (int i = 1; i < 21; i++)
	{
		check_kronekera(cipher, i);
	}*/

	check_kronekera(cipher, 14);

	vector<string> blocks = make_blocks(cipher, 14);

	//o(14), a(0), e(5)

	int diff[14] = { 5, 14, 14, 5, 14, 5, 5, 14, 5, 14, 14, 14, 14, 14 };

	string key1 = "", key2 = "", key3 = "", key4 = "";

	for (int i = 0; i < 14; i++)
	{
		int most_char = get_most(get_frequencies(blocks[i]));

		key1 += char(most_char);

		key2 += char(most_char - 5 < -32 ? most_char - 5 + 32 : most_char - 5);

		key3 += char(most_char - 14 < -32 ? most_char - 14 + 32 : most_char - 14);

		most_char -= diff[i];

		if (most_char < -32)
		{
			most_char += 32;
		}

		key4 += char(most_char);
	}

	cout << "A)\t" << key1 << "\nE)\t" << key2 << "\nO)\t" << key3 << "\n*)\t" << key4 << "\n";

	string dec = decrypt(cipher, key4);

	//cout << dec;

	ofstream fout("result.txt");

	fout << dec;

	fout.close();

	/*ofstream fout("output.txt", fstream::app);

	for (int i = 0; i < dec.length(); i += 14)
	{
		fout << endl << dec.substr(i, 14);
	}

	fout.close();*/
}

int main()
{
	setlocale(LC_ALL, "RU");

#ifdef mode
	part1();
#else
	part2();
#endif

	return 0;
}