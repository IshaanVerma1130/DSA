#include <iostream>
using namespace std;

// Find ceil of element in sorted array

int ceil(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;
  int res = -1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;

    if (arr[mid] == key)
      return arr[mid];

    if (arr[mid] < key)
      start = mid + 1;

    else
    {
      res = arr[mid];
      end = mid - 1;
    }
  }
  return res;
}

int main()
{
  int n = 11;
  int arr[] = {1, 2, 3, 4, 6, 7, 8, 10, 10, 12, 19};

  cout << "Ceil of 5 is: " << ceil(arr, n, 5);
}