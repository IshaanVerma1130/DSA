#include <iostream>
using namespace std;

// Find min absolute difference with a given element in a sorted array

// Another trick:
// If element is not present in the array
// High points to floor element
// Low points to ceil element

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

int min(int a, int b)
{
  return a < b ? a : b;
}

int minDiff(int arr[], int n, int key)
{
  int floorVal = floor(arr, n, key);
  int ceilVal = ceil(arr, n, key);

  return min(ceilVal - key, key - floorVal);
}

int main()
{
  int n = 3;
  int arr[]{4, 6, 10};

  cout << "Min diff with 7 is: " << minDiff(arr, n, 7);
}