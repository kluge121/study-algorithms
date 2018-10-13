#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

char toUpper(char in) {
    if(in <= 'z' && in >= 'a') {
        return in - ' ';
    }
    return in;
}

int main() {
    string input;

    cin >> input;
    map<char, int> countMap;
    using pair_type = decltype(countMap)::value_type;

    // 입력을 모두 대문자로 바꾸고, Map에 저장한다.
    for(char &alphabet: input) {
        char lowerAlphabet = toUpper(alphabet);
        if(countMap[lowerAlphabet] > 0) {
            countMap[lowerAlphabet] += 1;
        } else {
            countMap[lowerAlphabet] = 1;
        }
    }

    // max값 확인
    auto max = max_element(countMap.begin(), countMap.end(),
            [] (const pair_type & p1, const pair_type & p2) {
        return p1.second < p2.second;
    });

    // max값 수 체크
    int maxCount = 0;
    for(auto it: countMap) {
        if(it.second == max->second) {
            maxCount++;
        }
    }

    if(maxCount > 1) {
        // max값이 2개 이상일 경우 물음표 출력
        cout << "?" << endl;
    } else {
        // 1개일 경우 출력
        cout << max->first << endl;
    }

    return 0;
}