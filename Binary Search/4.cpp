#include <iostream>
using namespace std;

// Count of element in an array

int firstOccurence(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;
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

int lastOccurence(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;
  int res = -1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;
    if (arr[mid] == key)
    {
      res = mid;
      start = mid + 1;
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

int count(int arr[], int n, int key)
{
  int first = firstOccurence(arr, n, key);
  int last = lastOccurence(arr, n, key);

  if (first != -1 && last != -1)
    return last - first + 1;
  else
    return 0;
}

int main()
{
  int n = 8;
  int arr[]{1, 2, 5, 5, 5, 5, 5, 6, 8};

  cout << "Count of 5 is: " << count(arr, n, 5);
}