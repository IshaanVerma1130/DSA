#include <iostream>
using namespace std;

// Index of first '1' in infinite binary sorted array

int firstOccurence(int arr[], int start, int end, int key)
{
  int res = -1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;
    if (arr[mid] == key)
    {
      res = mid;
      end = mid - 1;
    }
    else if (arr[mid] > key)
    {
      end = mid - 1;
    }
    else
    {
      start = mid + 1;
    }
  }

  return res;
}

int search(int arr[])
{
  int start = 0;
  int end = 1;

  while (arr[end] < 1)
  {
    start = end;
    end *= 2;
  }

  return firstOccurence(arr, start, end, 1);
}

int main()
{
}