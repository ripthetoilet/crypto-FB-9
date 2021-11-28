#include <string>
#include <fstream>
#include <streambuf>
#include<iostream>
#include<cmath>
#include <vector>
#include <locale>
#include <string>
#include <algorithm>
#include <conio.h>
#include <windows.h>
#include <string.h>
#include <stdlib.h>
#include <memory>
#include <map>
#include <unordered_map>
#include <iterator>
#include <regex>
#include <sstream>
#include <cmath>
#include <list>
#include <iomanip>
#include "AllBigrams.h"
using namespace std;
int gModule = 961;
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
map< char, int> Alphabet_Rus = { {'а', 0 },
                                {'б', 1 },
                                {'в', 2 },
                                {'г', 3 },
                                {'д', 4 },
                                {'е', 5 },
                                {'ж', 6 },
                                {'з', 7 },
                                {'и', 8 },
                                {'й', 9 },
                                {'к', 10},
                                {'л', 11},
                                {'м', 12},
                                {'н', 13},
                                {'о', 14},
                                {'п', 15},
                                {'р', 16},
                                {'с', 17},
                                {'т', 18},
                                {'у', 19},
                                {'ф', 20},
                                {'х', 21},
                                {'ц', 22},
                                {'ч', 23},
                                {'ш', 24},
                                {'щ', 25},
                                {'ы', 26},
                                {'ь', 27},
                                {'э', 28},
                                {'ю', 29},
                                {'я', 30} };
map< int, string> Alphabet_Rus_2{ {0 , "а" },
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
//поиск по значению в мапе и вствка нужного значения
void MapFindValueStringInt(int pValue, map<string, int> pMap, map < int, string>* pMapIn)
{
    map < string, int> ::iterator lMapIterator;
    for (lMapIterator = pMap.begin(); lMapIterator != pMap.end(); lMapIterator = next(lMapIterator))
    {
        if (lMapIterator->second == pValue)
        {
            pMapIn->insert(make_pair(lMapIterator->second, lMapIterator->first)); ;
            break;
        }
    }
}
//полечаем текст с файла и записываем в vector<char>
void RetrievingInformationFromAFile(std::vector<char>* pText, string pPath)
{
    std::ifstream inBigramka(pPath);
    std::vector<char> lText{
        std::istreambuf_iterator<char>(inBigramka),
        std::istreambuf_iterator<char>() };
    *pText = lText;
}
//выводим часто встречаемые биграмки
void PrintoutBigramki(map < string, int>* pMaxBigramki)
{
    for (auto lMaxBigramki : *pMaxBigramki)
    {
        cout << lMaxBigramki.first << "\t:" << lMaxBigramki.second << "\t" << endl;
    }
}
//переводим текст в массив char
void ConvertVectorToChar(std::vector<char> pText, char* pCharElement)
{
    for (int a = 0; a < pText.size(); a++)
    {
        pCharElement[a] = pText[a];
    }
    int a = pText.size();
    pCharElement[a] = '\0';
}
//Поиск всех биграмок в тексте
void FindBigramka(map < string, int>* pAllBigrams, char* pTextInChar, std::vector<char> pText, int* lQuontityBigrams)
{
    int kabachok = 0;
    int lSize = 0;
    map < string, int> ::iterator it_1, it_2;
    lSize = pText.size();
    for (int h = 0; h <= lSize; h = h + 2)//for each char in string/////
    {
        if (h <= lSize - 1)
        {
            char BigramkaChar[3] = { pTextInChar[h],pTextInChar[h + 1],0 };
            std::string BigramkaString(BigramkaChar);

            it_2 = it_1 = pAllBigrams->find(BigramkaString);
            if (it_2 == pAllBigrams->end())
            {
                pAllBigrams->insert(make_pair(BigramkaString, 1));
                (*lQuontityBigrams)++;
            }
            else if (it_2 != pAllBigrams->end())
            {
                it_2->second++;
                (*lQuontityBigrams)++;
            }
        }
        else if (h == pText.size())
        {
            cout << "Конец массива...." << endl;
            kabachok = h;
        }
    }
}
//поиск 5 самых встречаемых биграмок в текстах
void Max5Bigrams(map < string, int> pAllBigrams, map < string, int>* pMaxBigramki, int pQuontityBigrams)
{
    for (int i = 1; i <= 5; i++)
    {
        auto x = std::max_element(pAllBigrams.begin(), pAllBigrams.end(), [](const pair<string, int>& p1, const pair<string, int>& p2) {return p1.second < p2.second; });
        cout << x->first << " : " << x->second << endl;
        pMaxBigramki->insert(make_pair(x->first, i));
        pAllBigrams.erase(x->first);
    }
}
//поиск самых встречаемых биграмок
void MostUsed(string pPath, map < string, int>* pMaxBigramki)
{
    ////////////////////////////////////// Локальные переменные
    std::vector<char> lText;
    map < string, int> lAllBigrams;
    map < string, int> ::iterator lAllBigramsIterator;
    //////////////////////////////////////
    RetrievingInformationFromAFile(&lText, pPath);
    lText.erase(std::remove_if(lText.begin(), lText.end(), &DeleteExtraLetters), lText.end());//удаляем лишние символы
    char* lTextInChar = new char[lText.size() + 1];
    //////////////////////////////////////
    ConvertVectorToChar(lText, lTextInChar);
    //cout << "Наш текст\n" << lTextInChar << endl;
    //////////////////////////////////////
    cout << "Количество символов " << (lText.size() - 1) << endl;
    int lQuontityBigrams = 0;
    FindBigramka(&lAllBigrams, lTextInChar, lText, &lQuontityBigrams);
    lAllBigramsIterator = lAllBigrams.find("юд");
    lAllBigramsIterator = lAllBigrams.find("рщ");

    Max5Bigrams(lAllBigrams, pMaxBigramki, lQuontityBigrams);
    cout << "Вывод для проверки!" << endl;
    for (auto lMaxBigramki : *pMaxBigramki)
    {
        cout << lMaxBigramki.first << "\t:" << lMaxBigramki.second << "\t" << endl;
    }
    cout << endl;
    lText.clear();
    return;
}
//Превращение биграмки в число
void BigramkaToValue(char *lDecipherBigram1, int* pIntValue)
{
    *pIntValue = Alphabet_Rus.find(lDecipherBigram1[0])->second * 31 + Alphabet_Rus.find(lDecipherBigram1[1])->second;
}
void gcd(int pfirstValue, int pMod, map<map<int, int>, int> *pResultForGcd)
{
    map <int, int> lValuesOfGcd;
    int lCounter = 1;
    while (pfirstValue > 0 && pMod > 0)
    {
        if (pfirstValue > pMod)
        {
            lValuesOfGcd.insert(make_pair(lCounter,pfirstValue / pMod));

            pfirstValue %= pMod;
        }

        else
        {
            lValuesOfGcd.insert(make_pair(lCounter, pMod / pfirstValue));
            pMod %= pfirstValue;
        }
        lCounter++;
    }
    pResultForGcd->insert(make_pair(lValuesOfGcd, pMod + pfirstValue));
}
void ReverseNumber(int pValue, int pMod, int* pReversFirstValue)
{
    map<map<int, int>, int> lResultForGcd;
    //map<int, int> ::iterator lIterator233;
    map<map<int, int>, int> ::iterator asdsf;
    if (pValue<0)
    {
        double lIDK = -pValue/ gModule;
        pValue = pValue + (lIDK+1)*gModule;

    }
    gcd(pValue, pMod, &lResultForGcd);

    if (lResultForGcd.begin()->second != 1)
    {
        cout << "Gcd not equal to 1" << endl;
    }
    map<int, int> result;
    map<int, int> :: iterator lResultIterator;
    result.insert(make_pair(0, 0));
    result.insert(make_pair(1, 1));
    asdsf = lResultForGcd.begin();
    int lValue = gModule;
    int lCounter = 2;
    for (int begin = 0; begin < lResultForGcd.begin()->first.size(); begin++)
    {
        int lChecker1 = lResultForGcd.begin()->first.find(begin+1)->second;
        int lChecker2 = result.find(begin + 1)->second;
        int lChecker3 = result.find(begin)->second;
        int lChecker4 = (lValue - lChecker1) * lChecker2;
        int lChecker5 = lChecker4 + lChecker3;
        int lChecker6 = lChecker5%961;

        result.insert(make_pair(lCounter,(((lValue - lResultForGcd.begin()->first.find(begin+1)->second) * result.find(begin+1)->second) + result.find(begin)->second) % 961));
        lCounter++;
    }
    lResultIterator = prev(prev(result.end()));
    *pReversFirstValue= lResultIterator->second;
}
void LinearEquation(int pFirstValue, int pSecondValue, int pMod, map <int, int>*pAllA)
{
    map<map<int,int>,int> lResultForGcd;
    gcd(pFirstValue, pMod, &lResultForGcd);

    if (lResultForGcd.begin()->second == 1)
    {
        int lReversFirstValue = 0; int lA = 0;
        ReverseNumber(pFirstValue, pMod,&lReversFirstValue);
        ReverseNumber(lReversFirstValue* pSecondValue, pMod, &lA);
        pAllA->insert(make_pair(1, lA));

        return;
    }
    if (pSecondValue % lResultForGcd.begin()->second > 0){return ;}
    int lValue = lResultForGcd.begin()->second, lX0 = 0;

    ReverseNumber((pFirstValue / lValue) *(pSecondValue / lValue), pMod / lValue, &lX0);

    map<int, int> lRresult;
    map<int, int> ::iterator lResultIterator;
    int lCounter = 2;
    for (int begin = 0; begin < lResultForGcd.begin()->first.size(); begin++)
    {
        lRresult.insert(make_pair(lX0 + begin* pMod, pMod));
        lCounter++;
    }
    *pAllA = lRresult;
}
//Функция подсчета буквы а и б
void AandB(map < int, string> ::iterator pDecipherBigram1, map < int, string> ::iterator pDecipherBigram2, map < int, string> ::iterator pCipherBigram1, map < int, string> ::iterator pCipherBigram2, double* a, double* b)
{
    double Module = 961;
    char* lDecipherBigram1 = &pDecipherBigram1->second[0];
    char* lDecipherBigram2 = &pDecipherBigram2->second[0];
    char* lCipherBigram1 = &pCipherBigram1->second[0];
    char* lCipherBigram2 = &pCipherBigram2->second[0];
    char alkjla = pDecipherBigram1->second[0];
    int x1 = 0, x2 = 0, y1 = 0, y2 = 0;
    BigramkaToValue(lDecipherBigram1, &x1);
    BigramkaToValue(lDecipherBigram2, &x2);
    BigramkaToValue(lCipherBigram1, &y1);
    BigramkaToValue(lCipherBigram2, &y2);
    
    int lA = 0, lB = 0;
    map <int, int> lAllA;
    LinearEquation(x1- x2, y1- y2, gModule,&lAllA);
    if (lAllA.size() == 1)
    {
        *b = y1 - lAllA.begin()->second * x1;
        *a = lAllA.begin()->second;
        return;
    }
}
//Считаем буквы а и б для нашей дешифровку афинного шифра
void AllAandB(map < string, int>pMaxBigramkiForDeciphertext, map < string, int> pMaxBigramkiForCiphertext, map<int, map<int, int>> pAllKeys, map<double, double>* pAllKeysAandB)
{
    map < int, string> lMBFCTITRO;//pMax bigramki for cipher text in the right order
    map < int, string> ::iterator lMBFCTITROIterator;
    map < int, string> ::iterator lMBFDTConstIterator;// 1 2 3 4 5 
    map < int, int> ::iterator lAllKeysIterator;
    map < int, string>  lMBFDTConst;// 1 2 3 4 5 

    for (int lCounter = 1; lCounter <= 5; lCounter++)
    {
        MapFindValueStringInt(lCounter, pMaxBigramkiForDeciphertext, &lMBFDTConst);
    }
    for (auto lAllKeys : pAllKeys)
    {
        lAllKeysIterator = lAllKeys.second.begin();
        for (lAllKeysIterator; lAllKeysIterator != lAllKeys.second.end(); lAllKeysIterator = next(lAllKeysIterator))
        {
            MapFindValueStringInt(lAllKeysIterator->second, pMaxBigramkiForCiphertext, &lMBFCTITRO);
        }
        double a = 0, b = 0;
        lMBFCTITROIterator = lMBFCTITRO.begin();
        lMBFDTConstIterator = lMBFDTConst.begin();
        for (lMBFCTITROIterator; lMBFCTITROIterator != lMBFCTITRO.end(); lMBFCTITROIterator = next(lMBFCTITROIterator))
        {
            AandB(lMBFDTConstIterator, next(lMBFDTConstIterator), lMBFCTITROIterator, next(lMBFCTITROIterator), &a, &b);
            pAllKeysAandB->insert(make_pair(a, b));
            a = 0, b = 0;
            lMBFDTConstIterator = next(lMBFDTConstIterator);
        }
    }
}
//Дешифровка текста по о и б и канеш по самому тексту
void DecipheringText(map<double, double> lAllKeysAandB, string pPath)
{
    ////////////////////////////////////// Локальные переменные
    std::vector<char> lText;
    map < string, int> lAllBigrams;
    //////////////////////////////////////
    RetrievingInformationFromAFile(&lText, pPath);
    lText.erase(std::remove_if(lText.begin(), lText.end(), &DeleteExtraLetters), lText.end());//удаляем лишние символы
    char* lTextInChar = new char[lText.size()];
    //////////////////////////////////////
    ConvertVectorToChar(lText, lTextInChar);
    cout << "Количество символов " << (lText.size() - 1) << endl;
}
//получение по формуле
void LAKFJLAJF()
{
    map < string, int> MaxBigramkiForCiphertext;
    map < string, int> MaxBigramkiForDeciphertext;
    map<double, double> lAllKeysAandB;
    map<int, map<int, int>> lAllKeys;
    string lPathForCiphertext = "ШТ.txt";
    string lPathForDeciphertext = "ВТ.txt";

    MostUsed(lPathForCiphertext, &MaxBigramkiForCiphertext);
    MostUsed(lPathForDeciphertext, &MaxBigramkiForDeciphertext);

    GettingKeys(&lAllKeys);
    AllAandB(MaxBigramkiForDeciphertext, MaxBigramkiForCiphertext, lAllKeys, &lAllKeysAandB);
}
int main()
{
    setlocale(LC_ALL, "ru");
    system("color 0A");
    SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
    SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывод
    LAKFJLAJF();

    system("pause");
    return 0;
}

