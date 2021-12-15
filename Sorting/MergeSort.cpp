#include <iostream>
using namespace std;

void Merge(int child1[], int lenChild1, int child2[], int lenChild2, int parent[], int lenParent)
{
  int i, j, k;
  i = j = k = 0;

  while (i < lenChild1 && j < lenChild2)
  {
    if (child1[i] <= child2[j])
    {
      parent[k] = child1[i];
      i++;
    }
    else
    {
      parent[k] = child2[j];
      j++;
    }
    k++;
  }
  while (i < lenChild1)
  {
    parent[k] = child1[i];
    i++;
    k++;
  }
  while (j < lenChild2)
  {
    parent[k] = child2[j];
    j++;
    k++;
  }
}

void MergeSort(int arr[], int n)
{
  if (n < 2)
    return;
  int mid = n / 2;

  int child1[mid];
  int child2[n - mid];

  for (int i = 0; i < mid; i++)
  {
    child1[i] = arr[i];
  }

  for (int i = mid; i < n; i++)
  {
    child2[i - mid] = arr[i];
  }

  MergeSort(child1, mid);
  MergeSort(child2, n - mid);
  Merge(child1, mid, child2, n - mid, arr, n);
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
  MergeSort(arr, n);
  printArr(arr, n);
}