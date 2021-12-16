#include <iostream>
using namespace std;

// Reverse sorted array

int BinarySearch(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;
    if (key == arr[mid])
    {
      return mid;
    }
    else if (key < arr[mid])
    {
      start = mid + 1;
    }
    else
    {
      end = mid - 1;
    }
  }
  return -1;
}

int main()
{
  int arr[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int n = sizeof(arr) / sizeof(int);

  cout << "Index of 6 is: " << BinarySearch(arr, n, 6);
}