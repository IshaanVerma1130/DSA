#include <iostream>
using namespace std;

// Iterate over the array and pick every element starting from the second.
// Store that element in a variable and make that position a hole
// Iterate back from that element and push every bigger element one step forward in the array making that element's position the current hole
// Replace the hole with the element stored before

void InsertionSort(int arr[], int n)
{
  for (int i = 1; i < n; i++) // We go from i = 1 to n-1
  {
    int value = arr[i];                       // Store current element in a variable
    int hole = i;                             // Make current position the hole
    while (hole > 0 && arr[hole - 1] > value) // Iterate back from the hole
    {
      arr[hole] = arr[hole - 1];
      hole--;
    }
    arr[hole] = value;
  }
}

void printArr(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main()
{
  int n = 6;
  int arr[]{2, 7, 4, 1, 5, 3};
  InsertionSort(arr, n);
  printArr(arr, n);
}