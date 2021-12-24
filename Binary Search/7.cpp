#include <iostream>
using namespace std;

// Find element in a nearly sorted array (element at i an be at i-1 or i+1)

// Apply bs checking mid/mid-1/mid+1 elements. Rest is same.

int search(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;

    if (arr[mid] == key)
      return mid;

    if (arr[mid - 1] == key && mid - 1 >= start)
      return mid - 1;

    if (arr[mid + 1] == key && mid + 1 <= end)
      return mid + 1;

    else if (arr[mid] > key)
      end = mid - 2;

    else
      start = mid + 2;
  }
  return -1;
}

int main()
{
  int n = 7;
  int arr[] = {10, 3, 40, 20, 50, 80, 70};

  cout << "The index of element 40 is: " << search(arr, n, 40);
}