#include <iostream>
using namespace std;

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
      end = mid - 1;
    }
    else
    {
      start = mid + 1;
    }
  }
  return -1;
}

int BinarySearch(int arr[], int start, int end, int key)
{
  while (start <= end)
  {
    int mid = start + (end - start) / 2;
    if (key == arr[mid])
    {
      return mid;
    }
    else if (key < arr[mid])
    {
      end = mid - 1;
    }
    else
    {
      start = mid + 1;
    }
  }
  return -1;
}

int main()
{
  int arr[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int n = sizeof(arr) / sizeof(int);

  cout << "Index of 6 is: " << BinarySearch(arr, n, 6);
}