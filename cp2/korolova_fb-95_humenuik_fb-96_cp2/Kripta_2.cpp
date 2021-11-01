#include <string>
#include <fstream>
#include <streambuf>
#include <iostream>
#include <vector>
#include <locale>
#include <string>
#include <algorithm>
#include<conio.h>
#include <stdio.h>
#include<windows.h>
#include <string.h>
#include<stdlib.h>
#include <memory>
#include <map>
#include <unordered_map>
#include <iterator>
#include <regex>
#include <sstream>
#include <math.h>
#include <iomanip>

using namespace std;
//////////////////////////////////////////////////////////////////////////////////////////////////////////
int SizeAlphabet = 32;
std::string massiv;    
int pCounterForDeciphertext = 1;
map< int, string > FrequencyOfLettersOfTheRussianLanguage = { { 1,"о" },
                                                            { 2,"е"},
                                                            { 3,"а"},
                                                            { 4,"и"},
                                                            { 5,"н"},
                                                            { 6,"т"},
                                                            { 7,"с"},
                                                            { 8,"р"},
                                                            { 9,"в"},
                                                            {10,"л"},
                                                            {11,"к"},
                                                            {12,"м"},
                                                            {13,"д"},
                                                            {14,"п"},
                                                            {15,"у"},
                                                            {16,"я"},
                                                            {17,"ы"},
                                                            {18,"ь"},
                                                            {19,"г"},
                                                            {20,"з"},
                                                            {21,"б"},
                                                            {22,"ч"},
                                                            {23,"й"},
                                                            {24,"х"},
                                                            {25,"ж"},
                                                            {26,"ш"},
                                                            {27,"ю"},
                                                            {28,"ц"},
                                                            {29,"щ"},
                                                            {30,"э"},
                                                            {31,"ф"},
                                                            {32,"ъ"} };
map< string, int> Alphabet_Rus = { {"а", 0 },
                                {"б", 1 },
                                {"в", 2 },
                                {"г", 3 },
                                {"д", 4 },
                                {"е", 5 },
                                {"ж", 6 },
                                {"з", 7 },
                                {"и", 8 },
                                {"й", 9 },
                                {"к", 10},
                                {"л", 11},
                                {"м", 12},
                                {"н", 13},
                                {"о", 14},
                                {"п", 15},
                                {"р", 16},
                                {"с", 17},
                                {"т", 18},
                                {"у", 19},
                                {"ф", 20},
                                {"х", 21},
                                {"ц", 22},
                                {"ч", 23},
                                {"ш", 24},
                                {"щ", 25},
                                {"ъ", 26},
                                {"ы", 27},
                                {"ь", 28},
                                {"э", 29},
                                {"ю", 30},
                                {"я", 31} };
map< int, string> Alphabet_Rus_2 = { {0 , "а" },
                                { 1, "б"},
                                { 2, "в"},
                                { 3, "г"},
                                { 4, "д"},
                                { 5, "е"},
                                { 6, "ж"},
                                { 7, "з"},
                                { 8, "и"},
                                { 9, "й"},
                                {10, "к"},
                                {11, "л"},
                                {12, "м"},
                                {13, "н"},
                                {14, "о"},
                                {15, "п"},
                                {16, "р"},
                                {17, "с"},
                                {18, "т"},
                                {19, "у"},
                                {20, "ф"},
                                {21, "х"},
                                {22, "ц"},
                                {23, "ч"},
                                {24, "ш"},
                                {25, "щ"},
                                {26, "ъ"},
                                {27, "ы"},
                                {28, "ь"},
                                {29, "э"},
                                {30, "ю"},
                                {31, "я"} };
//////////////////////////////////////////////////////////////////////////////////////////////////////////
bool DeleteExtraLetters(char c)
{
    switch (c)
    {
    case 'а':
    case 'б':
    case 'в':
    case 'г':
    case 'д':
    case 'е':
    case 'ж':
    case 'з':
    case 'и':
    case 'й':
    case 'к':
    case 'л':
    case 'м':
    case 'н':
    case 'о':
    case 'п':
    case 'р':
    case 'с':
    case 'т':
    case 'у':
    case 'ф':
    case 'х':
    case 'ц':
    case 'ч':
    case 'ш':
    case 'щ':
    case 'ъ':
    case 'ы':
    case 'ь':
    case 'э':
    case 'ю':
    case 'я':
        return false;
    default:
        return true;
    }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
void VigenèreCipher()
{
    std::ifstream lReadFile("Удаление лишних символов в файле без пробелов.txt");
    std::vector<char> Text{
        std::istreambuf_iterator<char>(lReadFile),
        std::istreambuf_iterator<char>() };
    ///KEY 
    int j = 0;
    string lKey;
    cout << "Input your fucking key: " << endl;
    cin >> lKey;
    ///KEY 
    char* lTextCypher = new char[Text.size()];
    for (int a = 0; a < Text.size(); a++)
    {
        lTextCypher[a] = Text[a];
    }
    int a = Text.size();
    ////////////////////////////////////////////////////////////////////////////
    map < string, int> ::iterator it_1, it_2, it_3, it_4;

    ////////////////////////////////////////////////////////////////////////////
    cout << "Количество символов " << (Text.size() - 1) << endl;
    cout << "Размер ключа " << lKey.size() << endl;

    std::ofstream ofs("Шифрована кіска.txt");
    std::streambuf* our_buffer = std::cout.rdbuf(ofs.rdbuf());
    ////////////////////////////////////////////////////////////////////////////
    for (int h = 0; h <= Text.size() - 1; h++)//for each char in string/////
    {
        char lCypherText[2] = { lTextCypher[h],0 };
        std::string lCypherTextString(lCypherText);

        it_1 = Alphabet_Rus.find(lCypherTextString);

        if (it_1 != Alphabet_Rus.end() && j <= lKey.size() - 1)
        {
            if (j < lKey.size() - 1)
            {
                char lKeyElement[2] = { lKey[j], 0 };
                std::string lKeyElementString(lKeyElement);
                it_2 = Alphabet_Rus.find(lKeyElementString);
                int lNumberCypher = (it_1->second + it_2->second) % 32;
                ////////////////////////////////////////////////////////////////////////////
                for (auto X : Alphabet_Rus)
                {
                    if (X.second == lNumberCypher)
                    {
                        j = j + 1;
                        cout << X.first;
                    }
                }
            }
            ////////////////////////////////////////////////////////////////////////////
            else if (j == lKey.size() - 1)
            {
                char lKeyElement[2] = { lKey[j], 0 };
                std::string lKeyElementString(lKeyElement);
                it_2 = Alphabet_Rus.find(lKeyElementString);
                int lNumberCypher = (it_1->second + it_2->second) % 32;
                ////////////////////////////////////////////////////////////////////////////
                for (auto X : Alphabet_Rus)
                {
                    if (X.second == lNumberCypher)
                    {
                        cout << X.first;
                    }
                }
                ////////////////////////////////////////////////////////////////////////////
                j = 0;
            }
        }
        else if (it_1 == Alphabet_Rus.end())
        {
            cout << "Letters error. This symbol don't letter:" << lCypherText << endl;
        };
        if (h == Text.size() - 1)
        {
            break;
        }
    }
    ////////////////////////////////////////////////////////////////////////////
    std::cout.rdbuf(our_buffer);
    ofs.close();
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
void Decoder()
{
    std::ifstream lReadFileDecoder("Шифрована кіска.txt");
    std::vector<char> TextDecoder{
        std::istreambuf_iterator<char>(lReadFileDecoder),
        std::istreambuf_iterator<char>() };

    int j = 0;
    string lKey;
    cout << "Input your fucking key: " << endl;
    cin >> lKey;
    ///KEY
    char* lTextDecypher = new char[TextDecoder.size()];
    for (int a = 0; a < TextDecoder.size(); a++)
    {
        lTextDecypher[a] = TextDecoder[a];
    }
    int a = TextDecoder.size();
    ////////////////////////////////////////////////////////////////////////////
    map < string, int> ::iterator it_1, it_2, it_3, it_4;
    ////////////////////////////////////////////////////////////////////////////
    cout << "Количество символов " << (TextDecoder.size() - 1) << endl;
    cout << "Размер ключа " << lKey.size() << endl;

    for (int pQuontity = 0; pQuontity < lKey.size(); pQuontity++)
    {
        char lFirstKeyElement[2] = { lKey[pQuontity], 0 };
        it_3 = Alphabet_Rus.find(lFirstKeyElement);
        if (pQuontity == 0 || it_3->second > it_4->second)
        {
            it_4 = it_3;
            cout << " Найбільший елемент має номер:" << it_4->second << endl;
        }
        else if (it_3->second <= it_4->second)
        {
        }
    }
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////
    for (int h = 0; h <= TextDecoder.size() - 1; h++)//for each char in string/////
    {
        char lDecypherText[2] = { lTextDecypher[h],0 };
        std::string lDecypherTextString(lDecypherText);

        it_1 = Alphabet_Rus.find(lDecypherTextString);

        if (it_1 != Alphabet_Rus.end() && j <= lKey.size() - 1)
        {
            if (j < lKey.size() - 1)
            {
                char lKeyElement[2] = { lKey[j], 0 };
                std::string lKeyElementString(lKeyElement);
                it_2 = Alphabet_Rus.find(lKeyElementString);
                int lNumberDecypher = (it_1->second - it_2->second) % 32;
                if (lNumberDecypher < -(it_4->second))
                {
                    lNumberDecypher = (it_1->second + it_2->second) % 32;
                }
                else if (lNumberDecypher >= -(it_4->second) && lNumberDecypher < 0)
                {
                    lNumberDecypher = 32 + lNumberDecypher;
                }
                else if (lNumberDecypher >= 0)
                {
                }
                ////////////////////////////////////////////////////////////////////////////
                for (auto X : Alphabet_Rus)
                {
                    if (X.second == lNumberDecypher)
                    {
                        j = j + 1;
                        cout << X.first;
                    }
                }
            }
            ////////////////////////////////////////////////////////////////////////////
            else if (j == lKey.size() - 1)
            {
                char lKeyElement[2] = { lKey[j], 0 };
                std::string lKeyElementString(lKeyElement);
                it_2 = Alphabet_Rus.find(lKeyElementString);
                int lNumberDecypher = (it_1->second - it_2->second) % 32;
                if (lNumberDecypher < -(it_4->second))
                {
                    lNumberDecypher = (it_1->second + it_2->second) % 32;
                }
                else if (lNumberDecypher >= -(it_4->second) && lNumberDecypher < 0)
                {
                    lNumberDecypher = 32 + lNumberDecypher;
                }
                else if (lNumberDecypher >= 0)
                {
                }
                ////////////////////////////////////////////////////////////////////////////
                for (auto X : Alphabet_Rus)
                {
                    if (X.second == lNumberDecypher)
                    {
                        cout << X.first;
                    }
                }
                ////////////////////////////////////////////////////////////////////////////
                j = 0;
            }
        }
        else if (it_1 == Alphabet_Rus.end())
        {
            cout << lDecypherText << endl;
        };
        if (h == TextDecoder.size() - 1)
        {
            break;
        }
    }
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
void DecipherTextWithoutKey(map < int, string> pResultForCiphertext)
{
    map < int, string> DecipherText;
    string lDecipherText = "";
    string pPartForCiphertext;
    int lStepForMass = 1;
    int lSize = 0;
    int pSizeForChiprotext = 0;
    int pCounterDecipcher = 1;
    while (lSize <= massiv.size())//записиваем части текста под размер нашего ключа
    {
        for (auto& lResultForCiphertext : pResultForCiphertext)//функцыя, которая делает дешифротекст
        {
            pPartForCiphertext = lResultForCiphertext.second;
            if (pCounterDecipcher < massiv.size())
            {
                lDecipherText = lDecipherText + pPartForCiphertext[pSizeForChiprotext];
            }
            else if (pCounterDecipcher == massiv.size())
            {
                lDecipherText = lDecipherText + pPartForCiphertext[pSizeForChiprotext];
                DecipherText.insert(make_pair(pCounterForDeciphertext, lDecipherText));
                cout << "Номер текста " << pCounterForDeciphertext << endl << lDecipherText << endl;
                pCounterForDeciphertext++;
                lDecipherText.clear();
                pCounterDecipcher = 1;
            }
            pCounterDecipcher++;
            lSize++;
        }
        pSizeForChiprotext++;
    }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
void BuckvoSchet(string pPath)
{
    /////////////////////////////////////////////////////////////////////////////////////////
    string pPathOut = "Шифрований кабачок без лишніх символів ебта.txt";
    std::ifstream in(pPath);
    std::vector<char> array{
        std::istreambuf_iterator<char>(in),
        std::istreambuf_iterator<char>() };
    /////////////////////////////////////////////////////////////////////////////////////////
    for (char c : array) {
        massiv.push_back(c);
    }

    cout << "Перед удалением " << endl << massiv << endl;
    /////////////////////////////////////////////////////////////////////////////////////////
    massiv.erase(std::remove_if(massiv.begin(), massiv.end(), &DeleteExtraLetters), massiv.end());
    cout << "После удаления " << endl << massiv << endl;
    /////////////////////////////////////////////////////////////////////////////////////////    
    map< string, int> ArrayLetters;
    map< int, double> ArrayLettersSum;
    map< string, int> ::iterator ArrayLettersEnd;
    map< string, int> ::iterator it_1, it_2, it_3;
    map< int, double> ::iterator lIteratorKey_1, lIteratorKey_2;
    int countbich = 0;
    int pArrayLettersEnd;
    double lMatchIndex = 0;
    double lGeneralMatchIndex = 0;
    int pCounter = 1;
    int lStep = 1;
    int lSize = 40;
    int lSizeKey = 0;
    double lFirstKeyElement_2 = 0.0;
    int lQuontity = 0;
    int pQuontity = 2;
    //////////////////////////////////////
    //I am assuming that buffer has some data
    char* c = new char[massiv.size()];

    for (int a = 0; a < massiv.size(); a++)
    {
        c[a] = massiv[a];
    }
    int a = massiv.size();
    //////////////////////////////////////
    int lSizeMassive = massiv.size() - 1;
    cout << "Количество символов " << lSizeMassive << endl;
    //////////////////////////////////////////////////////////////////////////////////////////////////////////Рахуємо як часто зустрічаються букви у всьому тексті 
    for (int h = 0; h <= massiv.size(); h++)//for each char in string/////
    {
        if (h <= massiv.size() - 1)
        {
            char BigramkaChar[2] = { c[h],0 };
            std::string BigramkaString(BigramkaChar);

            it_1 = ArrayLetters.find(BigramkaString);
            if (it_1 == ArrayLetters.end())
            {
                ArrayLetters.insert(make_pair(BigramkaString, 1));
            }
            else if (it_1 != ArrayLetters.end())
            {
                it_1->second++;
            }
        }
        else if (h == massiv.size())
        {
            cout << "Конец массива...." << endl;
        }
    }
    //////////////////////////////////////////////////////////////////////////////////////////////////////////Рахуємо индекс
    int pSizeAlphabet = 1;
    for (auto& pArrayLetters : ArrayLetters)  //for each unique char in map
    {
        lMatchIndex = lMatchIndex + ((pArrayLetters.second) * (pArrayLetters.second - 1.0)) / (lSizeMassive * (lSizeMassive - 1));
        if (pSizeAlphabet == SizeAlphabet)
        {
            cout << 0 << "\t" << lMatchIndex << "\t" << endl;
            ArrayLettersSum.insert(make_pair(0, lMatchIndex));
        }
        pSizeAlphabet++;
    }
    ArrayLetters.clear();
    int lStepForMass = 1;//Крок для массиву 
    std::string lBigramkaString = "";

    map< int, string> lDividedArray; // Массив у який записуємо наш массив поділений на кількісь розміру ключа

    map< int, string>::iterator lIteratorKey1, lIteratorKey2;
    map< int, double> AvarageIndexMap;
    map< int, char> TheMostCommonElementsInText; // Массив у який записуємо елементи які більше всього зустрічалися в частинах тексту
    pSizeAlphabet = 1;
    //////////////////////////////////////////////////////////////////////////////////////////////////////////Записуємо значення у массив після поділу
    std::ofstream ofs("Індекси відповідності.txt");
    std::streambuf* our_buffer = std::cout.rdbuf(ofs.rdbuf());
    for (int lStepForKey = 2; lStepForKey <= 30; lStepForKey++)//
    {
        lStepForMass = 1;
        if ((lStepForKey - 1) > 1)
        {
            lGeneralMatchIndex = lGeneralMatchIndex / (lStepForKey - 1);
            //cout << (lStepForKey - 1) << "\t" << lGeneralMatchIndex << "\t" << "Средний" << endl;
            AvarageIndexMap.insert(make_pair((lStepForKey - 1), lGeneralMatchIndex));
            lGeneralMatchIndex = 0;
        }
        //cout << "Предпологаемый размер ключа " << lStepForKey << endl;
        for (int pCounterMass2 = lStepForMass - 1; pCounterMass2 <= massiv.size(); pCounterMass2 = pCounterMass2 + lStepForKey)//for each char in string/////
        {
            if (lStepForMass < lStepForKey)
            {
                if (pCounterMass2 < massiv.size())
                {
                    char BigramkaChar[2] = { c[pCounterMass2],0 };
                    std::string BigramkaString(BigramkaChar);
                    it_1 = ArrayLetters.find(BigramkaString);
                    if (it_1 == ArrayLetters.end())
                    {
                        ArrayLetters.insert(make_pair(BigramkaString, 1));
                    }
                    else if (it_1 != ArrayLetters.end())
                    {
                        it_1->second++;
                    }
                    lBigramkaString = lBigramkaString + BigramkaString;
                    lMatchIndex = 0;
                    if ((pCounterMass2 + lStepForKey) > massiv.size())
                    {
                        //cout << lBigramkaString << endl;
                        /*PartOfText.MyClass.NumberDividing;*/
                        lSizeMassive = lBigramkaString.size();
                        //cout << "Конец массива...." << endl;
                        lBigramkaString.clear();
                        pCounterMass2 = lStepForMass - lStepForKey;
                        pArrayLettersEnd = ArrayLetters.size();
                        for (auto& pArrayLetters : ArrayLetters)  //for each unique char in map
                        {
                            lMatchIndex = lMatchIndex + ((pArrayLetters.second) * (pArrayLetters.second - 1.0));
                            if (pSizeAlphabet == pArrayLettersEnd)
                            {
                                lMatchIndex = lMatchIndex / (lSizeMassive * (lSizeMassive - 1.0));
                                lGeneralMatchIndex = lGeneralMatchIndex + lMatchIndex;
                                cout << lStepForKey << "\t" << lMatchIndex << "\t" << endl;
                                ArrayLettersSum.insert(make_pair(lStepForKey, lMatchIndex));
                            }
                            pSizeAlphabet++;
                        }
                        ArrayLetters.clear();
                        lStepForMass++;
                        pSizeAlphabet = 1;
                    }
                }
                else if (pCounterMass2 == massiv.size())
                {
                    lMatchIndex = 0;
                    if ((pCounterMass2 + lStepForKey) > massiv.size())
                    {
                        //cout << lBigramkaString << endl;
                        //cout << "Конец массива...." << endl;
                        lSizeMassive = lBigramkaString.size();
                        lBigramkaString.clear();
                        pCounterMass2 = lStepForMass - lStepForKey;
                        pArrayLettersEnd = ArrayLetters.size();
                        for (auto& pArrayLetters : ArrayLetters)  //for each unique char in map
                        {
                            lMatchIndex = lMatchIndex + ((pArrayLetters.second) * (pArrayLetters.second - 1.0));
                            if (pSizeAlphabet == pArrayLettersEnd)
                            {
                                lMatchIndex = lMatchIndex / (lSizeMassive * (lSizeMassive - 1.0));
                                lGeneralMatchIndex = lGeneralMatchIndex + lMatchIndex;
                                cout << lStepForKey << "\t" << lMatchIndex << "\t" << endl;
                                ArrayLettersSum.insert(make_pair(lStepForKey, lMatchIndex));
                            }
                            pSizeAlphabet++;
                        }
                        ArrayLetters.clear();
                        lStepForMass++;
                        pSizeAlphabet = 1;
                    }
                }
            }
            else if (lStepForMass == lStepForKey)
            {
                lMatchIndex = 0;
                if (pCounterMass2 <= massiv.size())
                {
                    char BigramkaChar[2] = { c[pCounterMass2],0 };
                    std::string BigramkaString(BigramkaChar);
                    it_1 = ArrayLetters.find(BigramkaString);
                    if (it_1 == ArrayLetters.end())
                    {
                        ArrayLetters.insert(make_pair(BigramkaString, 1));
                    }
                    else if (it_1 != ArrayLetters.end())
                    {
                        it_1->second++;
                    }
                    lBigramkaString = lBigramkaString + BigramkaString;
                    if ((pCounterMass2 + lStepForKey) > massiv.size())
                    {
                        //cout << lBigramkaString << endl;
                        //cout << "Конец массива...." << endl;
                        lSizeMassive = lBigramkaString.size();
                        lBigramkaString.clear();
                        pCounterMass2 = lStepForMass - lStepForKey;
                        pArrayLettersEnd = ArrayLetters.size();
                        for (auto& pArrayLetters : ArrayLetters)  //for each unique char in map
                        {
                            lMatchIndex = lMatchIndex + ((pArrayLetters.second) * (pArrayLetters.second - 1.0));
                            if (pSizeAlphabet == pArrayLettersEnd)
                            {
                                lMatchIndex = lMatchIndex / (lSizeMassive * (lSizeMassive - 1.0));
                                lGeneralMatchIndex = lGeneralMatchIndex + lMatchIndex;
                                cout << lStepForKey << "\t" << lMatchIndex << "\t" << endl;
                                ArrayLettersSum.insert(make_pair(lStepForKey, lMatchIndex));
                            }
                            pSizeAlphabet++;
                        }
                        ArrayLetters.clear();
                        lStepForMass++;
                        pSizeAlphabet = 1;
                    }
                }
            }
        }
        if (lStepForKey == 10)
        {
            lGeneralMatchIndex = lGeneralMatchIndex / (lStepForKey);
            //cout << lStepForKey << "\t" << lGeneralMatchIndex << "\t" << "Средний" << endl;
            AvarageIndexMap.insert(make_pair((lStepForKey), lGeneralMatchIndex));
            lGeneralMatchIndex = 0;
        }
    }
    for (auto& pAvarageIndexMap : AvarageIndexMap)
    {
        cout << pAvarageIndexMap.first << "\t" << pAvarageIndexMap.second << "\t" << "Средний" << endl;
    }
    std::cout.rdbuf(our_buffer);
    ofs.close();
    //////////////////////////////////////////////////////////////////////////////////////////////////////////Шукаємо максимальний індекс і визначаємо розмір ключа
    for (auto& pAvarageIndexMap : AvarageIndexMap)  //for each unique char in map
    {
        double lFirstKeyElement_1 = pAvarageIndexMap.second;
        if ((round(lFirstKeyElement_1 * 100) / 100) > (round(lFirstKeyElement_2 * 100) / 100))
        {
            lFirstKeyElement_2 = lFirstKeyElement_1;
            lQuontity = pQuontity;
            if (pQuontity == AvarageIndexMap.size() + 1)
            {
                cout << "\nНайбільший індекс співпадінь: " << lFirstKeyElement_2 << ". А отже розмір ключа у нас: " << lQuontity << endl;
                lSizeKey = lQuontity;
            }
        }
        else if (lFirstKeyElement_2 == 0)
        {
            lFirstKeyElement_2 = lFirstKeyElement_1;
        }
        else if ((round(lFirstKeyElement_1 * 100) / 100) <= (round(lFirstKeyElement_2 * 100) / 100))
        {
            if (pQuontity == AvarageIndexMap.size() + 1)
            {
                cout << "\nНайбільший індекс співпадінь: " << lFirstKeyElement_2 << ". А отже розмір ключа у нас: " << lQuontity << endl;
                lSizeKey = lQuontity;
            }
        }
        pQuontity++;
    }
    cout << "//////////////////////////////////////////////////////////////////////////////////////////////////////////" << endl;
    int lPartOfTheText = 1;
    lStepForMass = 1;
    for (int pCounterMass2 = lStepForMass - 1; pCounterMass2 <= massiv.size(); pCounterMass2 = pCounterMass2 + lSizeKey)//записиваем части текста под размер нашего ключа
    {
        if (lStepForMass < lSizeKey)
        {
            if (pCounterMass2 < massiv.size())
            {
                char BigramkaChar[2] = { c[pCounterMass2],0 };
                std::string BigramkaString(BigramkaChar);
                it_1 = ArrayLetters.find(BigramkaString);
                if (it_1 == ArrayLetters.end())
                {
                    ArrayLetters.insert(make_pair(BigramkaString, 1));
                }
                else if (it_1 != ArrayLetters.end())
                {
                    it_1->second++;
                }
                lBigramkaString = lBigramkaString + BigramkaString;
                lMatchIndex = 0;
                if ((pCounterMass2 + lSizeKey) > massiv.size())
                {
                    lDividedArray.insert(make_pair(lPartOfTheText, lBigramkaString));
                    cout << "Пара под номером " << lPartOfTheText << " создана" << endl;
                    lBigramkaString.clear();
                    pCounterMass2 = lStepForMass - lSizeKey;
                    lStepForMass++;
                    pSizeAlphabet = 1;
                    lPartOfTheText++;
                }
            }
            else if (pCounterMass2 == massiv.size())
            {
                lMatchIndex = 0;
                if ((pCounterMass2 + lSizeKey) > massiv.size())
                {
                    lDividedArray.insert(make_pair(lPartOfTheText, lBigramkaString));
                    cout << "Пара под номером " << lPartOfTheText << " создана" << endl;
                    lBigramkaString.clear();
                    pCounterMass2 = lStepForMass - lSizeKey;
                    lStepForMass++;
                    pSizeAlphabet = 1;
                    lPartOfTheText++;
                }
            }
        }
        else if (lStepForMass == lSizeKey)
        {
            lMatchIndex = 0;
            if (pCounterMass2 <= massiv.size())
            {
                char BigramkaChar[2] = { c[pCounterMass2],0 };
                std::string BigramkaString(BigramkaChar);
                it_1 = ArrayLetters.find(BigramkaString);
                if (it_1 == ArrayLetters.end())
                {
                    ArrayLetters.insert(make_pair(BigramkaString, 1));
                }
                else if (it_1 != ArrayLetters.end())
                {
                    it_1->second++;
                }
                lBigramkaString = lBigramkaString + BigramkaString;
                if ((pCounterMass2 + lSizeKey) > massiv.size())
                {

                    lDividedArray.insert(make_pair(lPartOfTheText, lBigramkaString));
                    cout << "Пара под номером " << lPartOfTheText << " создана" << endl;
                    lBigramkaString.clear();
                    pCounterMass2 = lStepForMass - lSizeKey;
                    lStepForMass++;
                    pSizeAlphabet = 1;
                    lPartOfTheText++;
                }
            }
        }
    }
    cout << "//////////////////////////////////////////////////////////////////////////////////////////////////////////" << endl;
    map < string, int> ::iterator IteratorForFind;
    map < string, int> ::iterator lCipherLetter;
    map < string, int> ::iterator IteratorForFindMostFrequencyLetterInAlphabet;
    map < string, int> ::iterator LetterOfKey;
    map < int, string> ::iterator IteratorForFindMostFrequencyLetter;
    map < int, string> ::iterator DecipherLettr;
    map < int, string> ::iterator IteratorForKey;
    map < int, string> ::iterator LetterForFindForKey;
    map < int, string> ::iterator IteratorResultForCiphertext;
    map < int, string> DecipherText;
    map < int, string> MostPopularLetterInPart;
    map < int, string> MaxElementForPart;
    map < int, string> MapForKey;
    map < int, string> ResultForCiphertext;
    int NumberDecipher;
    int lNumberLetter = 1;
    int pCounterForDeciphertext = 1;
    int NumberElementForPart = 1;
    string DecipherPartOfText;
    pSizeAlphabet = 1;
    int pCounterDecipcher = 1;
    int pSizeForChiprotext = 0;
    bool lBoolValue = 1;
    std::ofstream ofs_1("Вивід.txt");
    std::streambuf* our_buffer_1 = std::cout.rdbuf(ofs_1.rdbuf());
    cout << "Cчитаем какой у нас максимльный встреча буква" << endl;
    for (auto pDividedArray : lDividedArray)
    {
        ArrayLetters.clear();
        string ElementOfArray = pDividedArray.second;
        IteratorForFindMostFrequencyLetter = FrequencyOfLettersOfTheRussianLanguage.find(lNumberLetter);
        IteratorForFindMostFrequencyLetterInAlphabet = Alphabet_Rus.find(IteratorForFindMostFrequencyLetter->second);
        for (int NumberOfString = 0; NumberOfString <= ElementOfArray.length(); NumberOfString++)
        {
            if (NumberOfString <= ElementOfArray.length() - 1)// считаем сколько раз буква встречается
            {
                char BigramkaChar[2] = { ElementOfArray[NumberOfString],0 };
                std::string BigramkaString(BigramkaChar);

                it_1 = ArrayLetters.find(BigramkaString);
                if (it_1 == ArrayLetters.end())
                {
                    ArrayLetters.insert(make_pair(BigramkaString, 1));
                }
                else if (it_1 != ArrayLetters.end())
                {
                    it_1->second++;
                }
            }
            else if (NumberOfString == ElementOfArray.length())
            {
            }
        }
        int MaxElement = 0;
        pSizeAlphabet = 1;
        string MaxElementString = "";
        pArrayLettersEnd = ArrayLetters.size();
        for (auto& pArrayLetters : ArrayLetters)  //считаем какой у нас максимльный встреча буква
        {

            if (pArrayLetters.second > MaxElement)
            {
                MaxElement = pArrayLetters.second;
                MaxElementString = pArrayLetters.first;
                if (pSizeAlphabet == pArrayLettersEnd)
                {
                    it_1=Alphabet_Rus.find(MaxElementString);
                    cout << MaxElementString << "\t" << MaxElement << "\t" << it_1->second << endl;
                    MaxElementForPart.insert(make_pair(NumberElementForPart, MaxElementString));
                    NumberElementForPart++;
                }
            }
            else if (pSizeAlphabet == pArrayLettersEnd)
            {
                cout << MaxElementString << "\t" << MaxElement << "\t" << endl;
                MaxElementForPart.insert(make_pair(NumberElementForPart, MaxElementString));
                NumberElementForPart++;
            }
            pSizeAlphabet++;
        }
        ArrayLetters.clear();
    }
    int kabachok = 0; int lNumberKey = 0; int pCounterForKey = 0;
    string ElementOfArrayCharr;

    cout << "//////////////////////////////////////////////////////////////////////////////////////////////////////////" << endl;
    cout << "Ключик под номером " << pCounterForKey << " после дешифроки" << endl;

        IteratorForFindMostFrequencyLetterInAlphabet = Alphabet_Rus.find(FrequencyOfLettersOfTheRussianLanguage[1]);
        int lLetterNumber = IteratorForFindMostFrequencyLetterInAlphabet->second;
        lNumberLetter = 1;
        for (auto pDividedArray : lDividedArray)
        {
            pCounterForKey++;
            string ElementOfArray = pDividedArray.second;
            if (lBoolValue)
            {
                for (auto& pMaxElementForPart : MaxElementForPart)  //считаем итый елемент k
                {
                    kabachok++;
                    if (pMaxElementForPart.first == kabachok)
                    {
                        ElementOfArrayCharr = pMaxElementForPart.second;
                        IteratorForFind = Alphabet_Rus.find(ElementOfArrayCharr);
                        lNumberKey = (IteratorForFind->second - lLetterNumber) % 32;
                        if (lNumberKey < 0)
                        {
                            lNumberKey = 32 + lNumberKey;
                        }
                        else if ( lNumberKey > 0)
                        {
                        }
                        LetterForFindForKey = Alphabet_Rus_2.find(lNumberKey);
                        cout << kabachok << "\t" << lNumberKey << "\t" << LetterForFindForKey->second << "\t" << endl;
                        MapForKey.insert(make_pair(kabachok, LetterForFindForKey->second));
                    }
                }
                lBoolValue = 0;
            }
            kabachok = 0;
            LetterForFindForKey = MapForKey.find(lNumberLetter);
            LetterOfKey = Alphabet_Rus.find(LetterForFindForKey->second);
            for (int NumberOfString = 0; NumberOfString <= ElementOfArray.length() - 1; NumberOfString++)//шифровка куска текста
            {
                char pElement[2] = { ElementOfArray[NumberOfString],0 };
                std::string pElementString(pElement);
                lCipherLetter = Alphabet_Rus.find(pElementString);
                if (lCipherLetter != Alphabet_Rus.end() && NumberOfString <= ElementOfArray.length() - 1)
                {
                    if (NumberOfString < ElementOfArray.length() - 1)
                    {
                        int lNumberDecypher = (lCipherLetter->second - LetterOfKey->second) % 32;
                        if (lNumberDecypher < 0)
                        {
                            lNumberDecypher = 32 + lNumberDecypher;
                        }
                        else if (lNumberDecypher >= 0)
                        {
                        }
                        ////////////////////////////////////////////////////////////////////////////
                        DecipherLettr = Alphabet_Rus_2.find(lNumberDecypher);
                        DecipherPartOfText = DecipherPartOfText + DecipherLettr->second;
                    }
                    ////////////////////////////////////////////////////////////////////////////
                    else if (NumberOfString == ElementOfArray.length() - 1)
                    {
                        int lNumberDecypher = (lCipherLetter->second - LetterOfKey->second) % 32;
                        if (lNumberDecypher < 0)
                        {
                            lNumberDecypher = 32 + lNumberDecypher;
                        }
                        else if (lNumberDecypher >= 0)
                        {
                        }
                        ////////////////////////////////////////////////////////////////////////////
                        DecipherLettr = Alphabet_Rus_2.find(lNumberDecypher);
                        DecipherPartOfText = DecipherPartOfText + DecipherLettr->second;
                        //cout << "Номер кусочка " << pDividedArray.first << ", символ яким шифруємо:" << LetterOfKey->first << "!" << endl << DecipherPartOfText << endl;
                        ResultForCiphertext.insert(make_pair(LetterForFindForKey->first, DecipherPartOfText));
                        lNumberLetter++;
                        DecipherPartOfText.clear();
                        ////////////////////////////////////////////////////////////////////////////
                    }
                }
                else if (IteratorForFind == Alphabet_Rus.end())
                {
                    cout << "Данный символ не найден в алфавите" << ElementOfArrayCharr << endl;
                }
            }

            ////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////
        }
        //посмотреть как меняется индекс соответсвия с ростом ключа сделать первые шаги
        cout << "//////////////////////////////////////////////////////////////////////////////////////////////////////////" << endl;
        DecipherTextWithoutKey(ResultForCiphertext);
        MapForKey.clear();
        ResultForCiphertext.clear();
        ResultForCiphertext.clear();
        lBoolValue = 1;
        std::cout.rdbuf(our_buffer_1);
        ofs_1.close();
    _getch();
    return;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
void DecoderSelection()
{
    string lPath = "Шифрований кабачок.txt";
    std::ifstream lReadFileDecoder(lPath);
    std::vector<char> TextDecoder{
        std::istreambuf_iterator<char>(lReadFileDecoder),
        std::istreambuf_iterator<char>() };

    ///KEY 
    char* lTextDecypher = new char[TextDecoder.size()];
    for (int a = 0; a < TextDecoder.size(); a++)
    {
        lTextDecypher[a] = TextDecoder[a];
    }
    int a = TextDecoder.size();
    ////////////////////////////////////////////////////////////////////////////
    map < string, int> ::iterator it_1, it_2, it_3, it_4;
    ////////////////////////////////////////////////////////////////////////////
    BuckvoSchet(lPath);
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
int main()
{
    setlocale(LC_ALL, "ru");
    SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
    SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывод

    int counter = 1, chosen_option = counter;
    std::vector<std::string> Options;
    std::vector<std::string> Options_2;
    setlocale(LC_ALL, "Ukrainian");
    Options.push_back("          	                                                        \n");
    Options.push_back("-----------------------------------------------------------------\n");
    Options.push_back("|                               Menu                             |\n");
    Options.push_back("-----------------------------------------------------------------\n");
    Options.push_back("| 1 - Шифрование текста шифром Вижинера                          |\n");
    Options.push_back("| 2 - Декодирывание текста шифром Вижинера                       |\n");
    Options.push_back("| 3 - Дешифровка без ключа                                       |\n");
    Options.push_back("| 4 -                                                            |\n");
    Options.push_back("-----------------------------------------------------------------\n");
    Options.push_back("|                              Вихід                             |\n");
    Options.push_back("-----------------------------------------------------------------\n");
    while (chosen_option != 9)
    {
        HANDLE hd = GetStdHandle(STD_OUTPUT_HANDLE);
        COORD cd;
        cd.X = 0;
        cd.Y = 0;
        SetConsoleCursorPosition(hd, cd);

        for (size_t i = 0; i < Options.size(); ++i)
        {
            if ((i + 1) == counter) std::cout << "> " << Options[i] << std::endl;
            else                    std::cout << Options[i] << std::endl;
        }
        char pressed = _getch();

        if (pressed == 'w' && counter != 0)
            counter--;
        if (pressed == 'w' && counter == 0)
            counter = Options.size();
        if (pressed == 's' && counter != Options.size())
            counter++;
        if (pressed == 's' && counter == Options.size())
            counter = 0;

        if (pressed == '\r' || pressed == '\n')
        {
            chosen_option = counter;

            HANDLE hd = GetStdHandle(STD_OUTPUT_HANDLE);
            COORD cd;
            cd.X = 0;
            cd.Y = 0;
            SetConsoleCursorPosition(hd, cd);
            switch (chosen_option)
            {
            case 5:
                system("pause");
                system("cls");
                cout << "\n";
                cout << "1 - Шифрование текста шифром Вижинера\n";
                VigenèreCipher();
                system("pause");
                system("cls");
                cout << "\n";
                break;
            case 6:
                system("pause");
                system("cls");
                cout << "\n";
                cout << "2 - Декодирывание текста шифром Вижинера\n";
                Decoder();
                cout << "\n";
                system("pause");
                system("cls");
                cout << "\n";
                break;
            case 7:
                system("pause");
                system("cls");
                cout << "\n";
                cout << "3 - Частота букв\n";
                DecoderSelection();
                cout << "\n";
                system("pause");
                system("cls");
                cout << "\n";
                break;
            case 8:
                system("pause");
                system("cls");
                cout << "\n";
                cout << "4 - Частота букв\n";

                system("pause");
                system("cls");
                cout << "\n";
                break;
            case 10:
                system("pause");
                system("cls");
                cout << "\n";
                cout << "Вихiд... ";
                system("pause");
                system("cls");
                cout << "\n";
                return 0;
                break;
            }
            _getch();
        }
    }
    _getch();
}
