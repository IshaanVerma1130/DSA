#include <iostream>
using namespace std;

// Number of times an array is rotated (distinct elements) (from right to left)

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

int main()
{
  int n = 7;
  int arr[]{4, 5, 6, 7, 0, 1, 2};

  cout << "Number of times array is rotated is: " << count(arr, n);
}