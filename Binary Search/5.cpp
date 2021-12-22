#include <iostream>
using namespace std;

// Number of times an array is rotated (distinct elements)

int count(int arr[], int n)
{
  int start = 0;
  int end = n - 1;

  while (start <= end)
  {
    int mid = start + (end - start) / 2;

    if (arr[mid] <= arr[(mid + n - 1) % n] & arr[mid] <= arr[(mid + 1) % n])
    {
      return mid;
    }
    if (arr[start] <= arr[mid])
    {
      start = mid + 1;
    }
    else if (arr[mid] <= end)
    {
      end = mid - 1;
    }
  }

  return 0;
}

int main()
{
  int n = 5;
  int arr[]{7, 9, 11, 12, 15};

  cout << "Number of times array is rotated is: " << count(arr, n);
}