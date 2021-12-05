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
/////////////////////////////////////////////////////////////////////////////////////////
void RetrievingInformationFromAFile(std::vector<char>* pText, string pPath)
{
    std::ifstream inBigramka(pPath);
    std::vector<char> lText{
        std::istreambuf_iterator<char>(inBigramka),
        std::istreambuf_iterator<char>() };
    *pText = lText;
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
//Получения с Веторов чара просто массив чаров
char* VectorCharToChar(string pPath, int* lSizeText)
{
    ////////////////////////////////////// Локальные переменные
    std::vector<char> lText;
    //////////////////////////////////////
    RetrievingInformationFromAFile(&lText, pPath);//считываем файлы по пути который у нас эсть
    lText.erase(std::remove_if(lText.begin(), lText.end(), &DeleteExtraLetters), lText.end());//удаляем лишние символы
    char* lTextInChar = new char[lText.size()];
    *lSizeText = lText.size();
    //////////////////////////////////////
    ConvertVectorToChar(lText, lTextInChar);//превращаем вектор чаров в массив чаров
    return lTextInChar;
}
///////////////////////////////////////////////////////////////////////////////////////////
//выводим часто встречаемые биграмки
void PrintoutBigramki(map < string, int>* pMaxBigramki)
{
    for (auto lMaxBigramki : *pMaxBigramki)
    {
        cout << lMaxBigramki.first << "\t:" << lMaxBigramki.second << "\t" << endl;
    }
}
//Поиск всех биграмок в тексте
void FindBigramka(map < string, int>* pAllBigrams, char* pTextInChar, int  lSizeText, int* lQuontityBigrams)
{
    int kabachok = 0;
    map < string, int> ::iterator it_1, it_2;
    for (int h = 0; h <= lSizeText; h = h + 2)//for each char in string/////
    {
        if (h <= lSizeText - 1)
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
    map < string, int> lAllBigrams;
    int  lSizeText = 0;
    //////////////////////////////////////
    char* lTextInChar = VectorCharToChar(pPath, &lSizeText);
    int lQuontityBigrams = 0;
    FindBigramka(&lAllBigrams, lTextInChar, lSizeText, &lQuontityBigrams);

    Max5Bigrams(lAllBigrams, pMaxBigramki, lQuontityBigrams);
    cout << "Вывод для проверки!" << endl;
    for (auto lMaxBigramki : *pMaxBigramki)
    {
        cout << lMaxBigramki.first << "\t:" << lMaxBigramki.second << "\t" << endl;
    }
    cout << endl;   return;
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
        return;
    }
    map<int, int> result;
    map<int, int> :: iterator lResultIterator;
    result.insert(make_pair(0, 0));
    result.insert(make_pair(1, 1));

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
        lA = lReversFirstValue * pSecondValue;
        if (lA < 0)
        {
            double lIDK = -lA / gModule;
            lA = lA + (lIDK + 1) * gModule;
        }
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
//Функция проверки правильности числа
int Proverka(int lValue)
{
    if (lValue < 0)
    {
        double lIDK = -lValue / gModule;
        return lValue + (lIDK + 1) * gModule;
    }
    else if (lValue > gModule)
    {
        double lIDK = lValue / gModule;
        return lValue - lIDK * gModule;
    }
    else { return lValue; }
}
//Функция подсчета буквы а и б
void AandB(map < int, string> ::iterator pDecipherBigram1, map < int, string> ::iterator pDecipherBigram2, map < map< int, int>, string> ::iterator pCipherBigram1, map < map< int, int>, string> ::iterator pCipherBigram2, double* a, double* b)
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
    
    int lB = 0,lA = 0;
    map <int, int> lAllA;
    LinearEquation(x1- x2, y1- y2, gModule,&lAllA);
    if (lAllA.size() == 1)
    {
        lB = y1 - lAllA.begin()->second * x1;
        *b = Proverka(lB);
        lA = lAllA.begin()->second;
        *a = Proverka(lA);
        return;
    }
}
//поиск по значению в мапе и вствка нужного значения
void MapFindValue(map < int, int> ::iterator pIterator, map<string, int> pMap, map < map< int, int>, string>* pMapIn)
{
    map < string, int> ::iterator lMapIterator;
    map< int, int> lMapForValue;
    lMapForValue.insert(make_pair(pIterator->first, pIterator->second));
    for (lMapIterator = pMap.begin(); lMapIterator != pMap.end(); lMapIterator = next(lMapIterator))
    {
        if (lMapIterator->second == pIterator->second)
        {
            pMapIn->insert(make_pair(lMapForValue, lMapIterator->first)); ;
            break;
        }
    }
}
//Считаем буквы а и б для нашей дешифровку афинного шифра
void AllAandB(map < string, int>pMaxBigramkiForDeciphertext, map < string, int> pMaxBigramkiForCiphertext, map<int, map<int, int>> pAllKeys, map<int, map<double, double>>* pAllKeysAandB)
{
    map < map< int, int>, string> lMBFCTITRO;//pMax bigramki for cipher text in the right order
    map < map< int, int>, string> ::iterator lMBFCTITROIterator;
    map < int, string> ::iterator lMBFDTConstIterator;// 1 2 3 4 5 
    map < int, int> ::iterator lAllKeysIterator;
    map < int, string>  lMBFDTConst;// 1 2 3 4 5 

    for (int lCounter = 1; lCounter <= 5; lCounter++)
    {
        MapFindValueStringInt(lCounter, pMaxBigramkiForDeciphertext, &lMBFDTConst);
    }
    int lCounter = 1;
    map<double, double> lValueForAAndB;
    for (auto lAllKeys : pAllKeys)
    {
        lAllKeysIterator = lAllKeys.second.begin();
        for (lAllKeysIterator; lAllKeysIterator != lAllKeys.second.end(); lAllKeysIterator = next(lAllKeysIterator))
        {
            MapFindValue(lAllKeysIterator, pMaxBigramkiForCiphertext, &lMBFCTITRO);
        }
        double a = 0, b = 0;
        lMBFCTITROIterator = lMBFCTITRO.begin();
        lMBFDTConstIterator = lMBFDTConst.begin();
        map<double, double> lValueForAAndBTemporary;

        for (lMBFCTITROIterator; lMBFCTITROIterator != prev(lMBFCTITRO.end()); lMBFCTITROIterator = next(lMBFCTITROIterator))
        {
            AandB(lMBFDTConstIterator, next(lMBFDTConstIterator), lMBFCTITROIterator, next(lMBFCTITROIterator), &a, &b);
            if ((a != 0 && b != 0) && (lValueForAAndB.find(a) == lValueForAAndB.end()))
            {
                lValueForAAndB.insert(make_pair(a, b));
                lValueForAAndBTemporary.insert(make_pair(a, b));
                pAllKeysAandB->insert(make_pair(lCounter, lValueForAAndBTemporary));
                lCounter++; lValueForAAndBTemporary.clear();
            }
            a = 0, b = 0;
            lMBFDTConstIterator = next(lMBFDTConstIterator);
        }
        cout << lAllKeys.first<<endl;
        lMBFCTITRO.clear();
    }
}
string FindingLetterByNumber(int n)
{
    if (n < 26) 
    { 
        int lValue = n - 32;
        if (lValue < 0) { lValue = 32 + lValue; }
        return Alphabet_Rus_2.find(lValue)->second;
    }
    else 
    {
        int lValue = n + 1 - 32;
        if (lValue < 0) { lValue = 32 + lValue; }
        return Alphabet_Rus_2.find(lValue)->second;
    }
}
string GettingBigram(int n)
{
    return FindingLetterByNumber(n / 31) + FindingLetterByNumber(n % 31);
}
string DecipheringBigramka(string BigramkaString, double pA, double pB)
{
    char* lDBigram = &BigramkaString[0];
    string DecipherBigramkaString = "";
    int y1 = 0, lReversFirstValue=0;
    BigramkaToValue(lDBigram, &y1);

    ReverseNumber(pA, gModule, &lReversFirstValue);
    
    int lXProverka = (y1 - pB) * lReversFirstValue, lX = 0;
    lX = Proverka(lXProverka);
    DecipherBigramkaString = DecipherBigramkaString + GettingBigram(lX);
    return DecipherBigramkaString;
}
//Дешифровка всех текстов
string DecipheringText(char* lTextInChar, int lSizeText, map<double, double> lMapWithKey)
{
    string DecipheringNeededText = "";
    for (int h = 0; h <= lSizeText; h = h + 2)//for each char in string/////
    {
        if (h <= lSizeText - 1)
        {
            char BigramkaChar[3] = { lTextInChar[h],lTextInChar[h + 1],0 };
            std::string BigramkaString(BigramkaChar);
            map<double, double>   ::iterator lIteratorWithKey = lMapWithKey.begin();
            DecipheringNeededText = DecipheringNeededText + DecipheringBigramka(BigramkaString, lIteratorWithKey->first, lIteratorWithKey->second);
        }
    }
    return DecipheringNeededText;
}
//удаление текстов с плохими биграмами
void DeletingBannedBigrams(map < int, map < string, int>>* pAllBigramsForAllTextes, map < int, string>* pAllTexts, int lQuontityBigram)
{
    map < int, string> BannedBigrams {  { 0, "аь" },
                                        { 1, "уь" },
                                        { 2, "оь" },
                                        { 3, "еь" },
                                        { 4, "иь" },
                                        { 5, "ыь" },
                                        { 6, "эь" },
                                        { 7, "юь" },
                                        { 8, "яь" },
                                        { 9, "йь" },
                                        {10, "кь" },
                                        {11, "хь" },
                                        {12, "ць" },
                                        {13, "ьа" },
                                        {14, "ьй" },
                                        {15, "ьу" },
                                        {16, "ьы" },
                                        {17, "ьл" },
                                        {18, "ьь" },
                                        {19, "йй" },
                                        {20, "шш" },
                                        {21, "щщ" },
                                        {22, "ыы" },
                                        {23, "ээ" } };
    map < int, map < string, int>>::iterator lIterator;
    int lValue = 0;
    for (lIterator = pAllBigramsForAllTextes->begin(); lIterator != pAllBigramsForAllTextes->end(); lIterator = next(lIterator))
    {
        map < string, int> lMap = lIterator->second;
        map < string, int> ::iterator lMapIterator = lMap.begin();
        map < int, string>::iterator BannedBigramsIterator = BannedBigrams.begin();
        for (BannedBigramsIterator = BannedBigrams.begin(); BannedBigramsIterator != BannedBigrams.end(); BannedBigramsIterator=next(BannedBigramsIterator))
        {
            lValue = lIterator->first;
            if ((lMap.find(BannedBigramsIterator->second) != lMap.end()) && (lMap.find(BannedBigramsIterator->second)->second > lQuontityBigram/100))
            {
                pAllTexts->erase(lIterator->first);
                break;
            }
        }
    }
}
double ConformityIndexTexs(string pTextInChar,int pSizeText)
{
    map< string, int> ArrayLetters;
    map< string, int> ::iterator it_1;
    double lMatchIndex = 0; int pSizeAlphabet = 1;
    for (int h = 0; h <= pSizeText; h++)//поиск того сколько раз встречается каждая буква
    {
        if (h <= pSizeText - 1)
        {
            char BigramkaChar[2] = { pTextInChar[h],0 };
            std::string BigramkaString(BigramkaChar);

            it_1 = ArrayLetters.find(BigramkaString);
            if (it_1 == ArrayLetters.end())
            {
                ArrayLetters.insert(make_pair(BigramkaString, 1));
            }
            else if (it_1 != ArrayLetters.end()){it_1->second++;}
        }
    }
    //////////////////////////////////////////////////////////////////////////////////////////////////////////Рахуємо индекс
    for (auto& pArrayLetters : ArrayLetters)  //for each unique char in map
    {
        lMatchIndex = lMatchIndex + ((pArrayLetters.second) * (pArrayLetters.second - 1.0)) / (pSizeText * (pSizeText - 1));
        if (pSizeAlphabet == 31){return  lMatchIndex;}
        pSizeAlphabet++;
    }
}
//Проверка индекс
bool CheckerIndex(double pIndex)
{
    if (pIndex > 0.05 && pIndex < 0.06) { return 1; }
    if (pIndex > 0.06) { return 0; }
}
//Дешифровка текста по о и б и канеш по самому тексту
string FindingText(map<int, map<double, double>> lAllKeysAandB, string pPath)
{
    ////////////////////////////////////// Локальные переменные
    map < int, string> lAllTexts;
    map < string, int> lAllBigrams;
    map < int, map < string, int>> lAllBigramsForAllTextes;
    map<int, map<double, double>> ::iterator lKeyIterator;
    lKeyIterator = lAllKeysAandB.begin();
    int lSizeText = 0;
    //////////////////////////////////////
    char* lTextInChar = VectorCharToChar(pPath,&lSizeText);
    cout << "Количество символов " << (lSizeText - 1) << endl;
    string DecipheringNeededText = "";

    for (lKeyIterator = lAllKeysAandB.begin(); lKeyIterator != lAllKeysAandB.end(); lKeyIterator = next(lKeyIterator))
    {
        map<double, double> lMapWithKey = lKeyIterator->second;
        int lReversFirstValue = 0;
        ReverseNumber(lMapWithKey.begin()->first, gModule, &lReversFirstValue);
        if (lReversFirstValue == 0) {  }
        else 
        {
            DecipheringNeededText = DecipheringText(lTextInChar, lSizeText, lMapWithKey);
            lAllTexts.insert(make_pair(lKeyIterator->first, DecipheringNeededText));
            DecipheringNeededText.clear();
        }
    }
    int lQuontityBigram = 0;
    for (auto pAllTexts : lAllTexts)
    {
        int lQuontityBigrams = 0;
        char* DecipheringNeededTextInChar = &pAllTexts.second[0];
        int lSizeDecipherText = strlen(DecipheringNeededTextInChar);
        FindBigramka(&lAllBigrams, DecipheringNeededTextInChar, lSizeDecipherText, &lQuontityBigrams);
        lAllBigramsForAllTextes.insert(make_pair(pAllTexts.first, lAllBigrams));
        lQuontityBigram = lQuontityBigrams;
        lQuontityBigrams = 0; lAllBigrams.clear();
    }
    DeletingBannedBigrams(&lAllBigramsForAllTextes,&lAllTexts, lQuontityBigram);
    for (auto pAllTexts : lAllTexts)
    {
        double lIndex = ConformityIndexTexs(pAllTexts.second, lSizeText);
        bool lValue = CheckerIndex(lIndex);
        if (lValue == 1) 
        { 
            map<double, double> lMap = lAllKeysAandB.find(pAllTexts.first)->second;
            cout << lIndex << endl<< lMap.begin()->first << "\t" << lMap.begin()->second << endl << pAllTexts.second << endl;
        return pAllTexts.second; 
        }
    }
    cout << endl;
}
//получение по формуле
void LAKFJLAJF(string *SearchedText)
{
    string lPath = "ШТ.txt";
    map<int, map<double, double>> lAllKeysAandB;
    map<int, map<int, int>> lAllKeys;
    map< string, int> MaxBigramkiForDeciphertext{   { "то"  , 1},
                                                    { "ен"  , 2},
                                                    { "но"  , 3},
                                                    { "на"  , 4},
                                                    { "ст"  , 5} };
    map< string, int> MaxBigramkiForCiphertext  {   { "йа"  , 1},
                                                    { "юа"  , 2},
                                                    { "чш"  , 3},
                                                    { "юд"  , 4},
                                                    { "рщ"  , 5} };

    GettingKeys(&lAllKeys);//получаем все варинаты чисел с 1 2 3 4 5 до 5 4 3 2 1
    AllAandB(MaxBigramkiForDeciphertext, MaxBigramkiForCiphertext, lAllKeys, &lAllKeysAandB);
    *SearchedText = FindingText(lAllKeysAandB, lPath);
    cout << endl;
}
int main()
{
    setlocale(LC_ALL, "ru");
    system("color 0A");
    SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
    SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывод
    string lText = "";
    LAKFJLAJF(&lText);

    system("pause");
    return 0;
}

