/**
 * # 퀵소트
 *
 * 시간복잡도
 * 최선: Ω(n log(n))
 * 평균: Θ(n log(n))
 * 최악: O(n^2)
 *
 * 공간복잡도
 * 최악: O(log(n))
 */

#include <iostream>

using namespace std;


int partition(int *arr, int low, int high) {
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;

    while (true) {
        do { i++; } while (arr[i] < pivot);
        do { j--; } while (arr[j] > pivot);
        if (i >= j) {
            return j;
        }

        swap(arr[i], arr[j]);
    }
}

void quickSort(int *arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot);
        quickSort(arr, pivot + 1, high);
    }
}

int main() {
    int arr[10] = {3, 6, 1, 8, 4, 10, 7, 2, 5, 9};

    size_t arrSize = sizeof(arr) / sizeof(int);

    quickSort(arr, 0, (int) arrSize - 1);

    for (const auto &num: arr) {
        cout << num << " ";
    }

    return 0;
}