#include <iostream>
#include <vector>
using namespace std;

// First negative integer in every windwo of size k

int solve(int arr[], int n, int k)
{
  int i = 0;
  int j = 0;
  vector<int> vec;

  while (j < n)
  {
    if (arr[j] < 0)
      vec.push_back(arr[j]);

    if (j - i + 1 == k)
    {
      if (vec.size() == 0)
        cout << "0 ";

      else
      {
        cout << vec.front() << " ";

        if (arr[i] == vec.front())
          vec.erase(vec.begin());
      }

      i++;
      j++;
    }

    else if (j - i + 1 < k)
    {
      j++;
    }
  }
}

int main()
{
  int n = 8;
  int arr[]{12, -1, -7, 8, -15, 30, 16, 28};
  int k = 3;

  solve(arr, n, k);
}