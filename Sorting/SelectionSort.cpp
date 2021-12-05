#include <iostream>
using namespace std;

// Pick the smallest element from the list and replace the first index of the array with the element
// Continue doing this for all other elements
// The last element would already be in the sorted position

void SelectionSort(int arr[], int n)
{
  for (int i = 0; i < n - 1; i++) // We go from i = 0 to n-2
  {
    int minIndex = i;
    for (int j = i + 1; j < n; j++) // Pick smallest element from j = i to n-1
    {
      if (arr[minIndex] > arr[j])
      {
        minIndex = j;
      }
    }
    int temp = arr[i];
    arr[i] = arr[minIndex];
    arr[minIndex] = temp;
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
  SelectionSort(arr, n);
  printArr(arr, n);
}