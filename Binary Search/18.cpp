#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

// Allocation of pages to a number of students

// Given an array of number of pages of 'n' books

// Distribute then into 'm' students such that:
// 1. Every student gets atleast one book
// 2. The books should be distributed to the students in a continuous order
// 3. All books must be distributed

// Minimize the maximum number of pages a student reads

bool isValid(int arr[], int n, int students, int limit) // Check if our proposed limit can be satisfied or not
{
  int stud = 1;
  int sum = 0;

  for (int i = 0; i < n; i++)
  {
    sum += arr[i];
    if (sum > limit) // If the sum goes above limit
    {                // Increase required number of students by 1
      stud++;
      sum = arr[i];
    }

    if (stud > students) // If required number of students becomes greater than possible students return false
      return false;
  }

  return true;
}

int allocate(int arr[], int n, int students)
{
  if (n < students)
    return -1;

  sort(arr, arr + n);
  int start, end = 0, res = -1;

  start = *max_element(arr, arr + n);  // Set start as the highest number of pages
  end = accumulate(arr, arr + n, end); // Set end as the sum of all pages

  while (start <= end)
  {
    int mid = start + (end - start) / 2; // Propose a limit i.e. mid

    if (isValid(arr, n, students, mid)) // Check if mid can satisfy the value
    {                                   // If it can then store possible value in res and set new end to left of mid
      res = mid;
      end = mid - 1;
    }
    else // Otherwise search to the right of mid
      start = mid + 1;
  }

  return res;
}

int main()
{
  int n = 4;
  int arr[]{12, 34, 67, 90};
  int students = 2;

  cout << allocate(arr, n, students);
}