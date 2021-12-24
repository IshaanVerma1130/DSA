#include <iostream>
using namespace std;

// Find element in infinite sorted array

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

int search(int arr[], int key)
{
  int start = 0;
  int end = 1;

  while (arr[end] < key)
  {
    start = end;
    end *= 2;
  }

  return BinarySearch(arr, start, end, key);
}

int main()
{
}