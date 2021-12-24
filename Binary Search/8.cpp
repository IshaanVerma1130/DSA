#include <iostream>
using namespace std;

// Find floor of element in sorted array

int floor(int arr[], int n, int key)
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
    {
      res = arr[mid];
      start = mid + 1;
    }

    else
      end = mid - 1;
  }
  return res;
}

int main()
{
  int n = 7;
  int arr[] = {1, 2, 8, 10, 10, 12, 19};

  cout << "Floor of 5 is: " << floor(arr, n, 5);
}