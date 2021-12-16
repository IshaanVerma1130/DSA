#include <iostream>
using namespace std;

// Agnostic Sorted array

int BinarySearch(int arr[], int n, int key)
{
  if (arr[0] < arr[n - 1])
  {
    int start = 0;
    int end = n - 1;

    while (start <= end)
    {
      int mid = start + (end - start) / 2;
      if (arr[mid] == key)
      {
        return mid;
      }
      else if (arr[mid] < key)
      {
        start = mid + 1;
      }
      else
      {
        end = mid - 1;
      }
    }
  }
  else
  {
    int start = 0;
    int end = n - 1;

    while (start <= end)
    {
      int mid = start + (end - start) / 2;
      if (arr[mid] == key)
      {
        return mid;
      }
      else if (arr[mid] < key)
      {
        end = mid - 1;
      }
      else
      {
        start = mid + 1;
      }
    }
  }
}

int main()
{
  int arr[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int n = sizeof(arr) / sizeof(int);

  cout << "Index of 6 is: " << BinarySearch(arr, n, 6);
}