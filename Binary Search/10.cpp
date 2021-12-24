#include <iostream>
using namespace std;

// Next letter in a sorted array of alphabets

char search(char arr[], int n, char key)
{
  int start = 0;
  int end = n - 1;
  int res = '\0';

  while (start <= end)
  {
    int mid = start + (end - start) / 2;

    if (arr[mid] == key)
      start = mid + 1;

    if (arr[mid] > key)
    {
      res = arr[mid];
      end = mid - 1;
    }

    else
      start = mid + 1;
  }
  return res;
}

int main()
{
  int n = 5;
  char arr[]{'a', 'b', 'd', 'g', 'h'};

  cout << "Alphabet next in order to 'g' is: " << search(arr, n, 'g');
}