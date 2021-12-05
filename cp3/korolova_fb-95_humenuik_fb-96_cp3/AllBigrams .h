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

using namespace std;

//создания начального map
void StartMap(map<int, int>* pKey);
//расположение елементов в порядке спадания и запись в ключ
void ArrangeNumbersInAscendingOrder(map<int, int>* pConstKey, map<int, int>* pKey);
//расположение елементов в порядке спадания и запись в ключ
void ArrangeNumbersInDescendingOrder(map<int, int>* pConstKey, map<int, int>* pKey);
//выводит ключи
void OutKey(map<int, int> pKey);
//запись в мап с определенного елемента до конца
void WriteTo(map<int, int>::iterator pIterator, map<int, int>* pMap, map<int, int>* pNSymphols);
//перезапись ключа в порядке спадания
void ReWriting(map<int, int>::iterator pKeyForGame, map<int, int>* pKey, map<int, int>* pNSymphols);
//перезапись ключа в порядке возрастания
void ReWriting_Max(map<int, int>::iterator pKeyForGame, map<int, int>* pKey, map<int, int>* pNSymphols);
//поиск по значению в мапе
void MapFindValue(int pValue, map<int, int> pMap, int* pLocation);
//проверка на использываный елементи поиск минимального
void UsedMinElements(map<int, int> pUsedNumbers, map<int, int> pNSymphols, int* pMinElement);
//проверка на использываный елемент и поиск максимального
void UsedMaxElements(map<int, int> pUsedNumbers, map<int, int> pNSymphols, int* pMaxElement);
//Перезаписаь в map lNSymphols  
void WriteToNumberSympholsMap(map<int, int>::iterator pKeyForGame, map<int, int>::iterator pIteratorForMinElement, map<int, int>* pKey, int lMinElement, map<int, int>* pNSymphols);
//делаем ключ во втором случае 
void ChangerMap(map<int, int>* pUsedNumbers1Element, map<int, int>* pUsedNumbers2Element, map<int, int>* pUsedNumbers3Element, map<int, int>* pKey, map<int, int>::iterator pIteratorForCheckMap, int* pCounterFor1Element, int* pCounterFor2Element, int* pCounterFor3Element);
//получение всех ключей что у нас эсть возможны
void GettingKeys(map<int, map<int, int>>* pAllKeys);