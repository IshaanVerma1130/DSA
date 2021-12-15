#include <iostream>
using namespace std;

// Iterate over the array multiple times and swap the current element with the next if it is greater

// Improved Bubble Sort:-
// 1. Added flag to stop algo if array is already sorted
// 2. Doesnot iterate to the last element in every iteration as the algo sorts from the end using (k)

void BubbleSort(int arr[], int n)
{
  for (int k = 0; k < n - 1; k++) // We go from k = 0 to n-1
  {
    bool flag = false;
    for (int i = 0; i < n - k - 1; i++) // We go from i = 0 to n-k-1 (As the elements from n-1 till (n-1)-k are already sorted)
    {
      if (arr[i] > arr[i + 1]) // If we find elements to swap set flag to true
      {
        int temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        flag = true;
      }
    }
    if (!flag)
    {
      break;
    }
  }
}

void printArr(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main()
{
  int n = 6;
  int arr[]{2, 7, 4, 1, 5, 3};
  BubbleSort(arr, n);
  printArr(arr, n);
}