#include <iostream>
#include <limits.h>
using namespace std;

// Max sum sub-array of size k

int solve(int arr[], int n, int k)
{
  int i = 0, j = 0;
  int sum = 0;
  int maxSum = INT_MIN;

  while (j < n)
  {
    sum += arr[j];

    if (j - i + 1 == k)
    {
      maxSum = max(maxSum, sum);
      sum -= arr[i];
      i++;
      j++;
    }

    else if (j - i + 1 < k)
    {
      j++;
    }
  }

  return maxSum;
}

int main()
{
  int n = 7;
  int arr[]{2, 5, 1, 8, 2, 9, 10};
  int k = 3;

  cout << solve(arr, n, k);
}