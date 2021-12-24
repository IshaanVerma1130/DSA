#include <iostream>
using namespace std;

// Find element in rotated sorted array (distinct elements) (from right to left)

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

int count(int arr[], int n)
{
  int start = 0;
  int end = n - 1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;
    int prev = (mid + n - 1) % n;
    int next = (mid + 1) % n;

    if (arr[start] <= arr[end])
      return start;

    if (arr[mid] < arr[prev] && arr[mid] < arr[next])
    {
      return mid;
    }

    if (arr[start] < arr[mid])
    {
      start = mid + 1;
    }

    else if (arr[mid] < arr[end])
    {
      end = mid - 1;
    }
  }
  return 0;
}

int search(int arr[], int n, int key)
{
  int index = count(arr, n);
  int bsLeft = BinarySearch(arr, 0, index - 1, key);
  int bsRight = BinarySearch(arr, index, n - 1, key);

  if (bsRight == -1 & bsLeft == -1)
    return -1;
  if (bsRight != -1 & bsLeft == -1)
    return bsRight;
  if (bsRight == -1 & bsLeft != -1)
    return bsLeft;
}

int main()
{
  int n = 7;
  int arr[]{4, 5, 6, 7, 0, 1, 2};

  cout << "Index of 0 is: " << search(arr, n, 0);
}