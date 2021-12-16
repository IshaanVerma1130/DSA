#include <iostream>
using namespace std;

int partition(int arr[], int start, int end)
{
  int pivot = arr[end];
  int partitionIndex = start;

  for (int i = start; i < end; i++)
  {
    if (arr[i] <= pivot)
    {
      swap(arr[i], arr[partitionIndex]);
      partitionIndex++;
    }
  }
  swap(arr[partitionIndex], arr[end]);
  return partitionIndex;
}

void QuickSort(int arr[], int start, int end)
{
  if (start < end)
  {
    int partitionIndex = partition(arr, start, end);
    QuickSort(arr, start, partitionIndex - 1);
    QuickSort(arr, partitionIndex + 1, end);
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
  QuickSort(arr, 0, n - 1);
  printArr(arr, n);
}