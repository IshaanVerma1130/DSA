#include <iostream>
using namespace std;

int peak(int arr[], int n)
{
  int start = 0;
  int end = n - 1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;

    if (mid > 0 && mid < n - 1)
    {
      if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
        return mid;
      else if (arr[mid] < arr[mid - 1])
        end = mid - 1;
      else
        start = mid + 1;
    }

    if (mid == 0)
      return arr[0] > arr[1] ? 0 : 1;

    if (mid == n - 1)
      return arr[n - 1] > arr[n - 2] ? n - 1 : n - 2;
  }

  return -1;
}

int BinarySearchAsc(int arr[], int start, int end, int key)
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

int BinarySearchDesc(int arr[], int start, int end, int key)
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
      start = mid + 1;
    }
    else
    {
      end = mid - 1;
    }
  }
  return -1;
}

int search(int arr[], int n, int key)
{
  int index = peak(arr, n);
  int bsLeft = BinarySearchAsc(arr, 0, index - 1, key);
  int bsRight = BinarySearchDesc(arr, index, n - 1, key);

  if (bsRight == -1 && bsLeft == -1)
    return -1;
  if (bsRight != -1 && bsLeft == -1)
    return bsRight;
  if (bsRight == -1 && bsLeft != -1)
    return bsLeft;
}

int main()
{
  int n = 7;
  int arr[]{-3, 9, 8, 20, 17, 5, 1};

  cout << "Index of 20 in Bitonic array is: " << search(arr, n, 9);
}