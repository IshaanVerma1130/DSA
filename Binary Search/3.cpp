#include <iostream>
using namespace std;

// First and last occurence of an element

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

int main()
{
  int n = 8;
  int arr[]{1, 2, 5, 5, 5, 5, 6, 8};

  cout << "First occurence of 5: " << firstOccurence(arr, n, 5) << endl;
  cout << "Last occurence of 5: " << lastOccurence(arr, n, 5);
}
