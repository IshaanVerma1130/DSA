#include <iostream>
using namespace std;

// Peak element

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

int main()
{
  int n = 4;
  int arr[]{5, 10, 20, 15};

  cout << "Peak element is: " << peak(arr, n);
}