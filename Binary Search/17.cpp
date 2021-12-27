#include <iostream>
#include <vector>
using namespace std;

// Binary Search in 2D array

struct Index
{
  int i = -1;
  int j = -1;
};

Index search(vector<vector<int>> arr, int n, int m, int key)
{
  Index index;
  int i = 0;
  int j = m - 1;

  while (i < n && j >= 0)
  {
    if (arr[i][j] == key)
    {
      index.i = i;
      index.j = j;
      return index;
    }

    else if (arr[i][j] > key)
    {
      j--;
    }

    else
    {
      i++;
    }
  }

  return index;
}

void printIndex(Index index, int key)
{
  if (index.i != -1 && index.j != -1)
    cout << "Found " << key << " at index: " << index.i << ", " << index.j;

  else
    cout << "Element not found";
}

int main()
{
  int n = 4;
  int m = 4;
  vector<vector<int>> mat = {{10, 20, 30, 40},
                             {15, 25, 35, 45},
                             {27, 29, 37, 48},
                             {32, 33, 39, 50}};
  int key = 0;

  printIndex(search(mat, n, m, key), key);
}