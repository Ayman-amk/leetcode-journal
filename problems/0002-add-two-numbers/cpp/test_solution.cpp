#include <cassert>
#include <iostream>
#include <vector>

#include "solution.cpp"

using namespace std;

// Helper function to create a linked list from vector
ListNode* createList(const vector<int>& values) {
  if (values.empty()) return nullptr;
  ListNode* head = new ListNode(values[0]);
  ListNode* current = head;
  for (size_t i = 1; i < values.size(); ++i) {
    current->next = new ListNode(values[i]);
    current = current->next;
  }
  return head;
}

// Helper function to convert linked list to vector
vector<int> listToVector(ListNode* head) {
  vector<int> result;
  while (head) {
    result.push_back(head->val);
    head = head->next;
  }
  return result;
}

// Helper function to compare two linked lists
bool compareLists(ListNode* l1, ListNode* l2) {
  while (l1 && l2) {
    if (l1->val != l2->val) return false;
    l1 = l1->next;
    l2 = l2->next;
  }
  return l1 == nullptr && l2 == nullptr;
}

// Helper function to delete linked list
void deleteList(ListNode* head) {
  while (head) {
    ListNode* temp = head;
    head = head->next;
    delete temp;
  }
}

void test_example_1() {
  Solution solver;
  ListNode* l1 = createList({2, 4, 3});
  ListNode* l2 = createList({5, 6, 4});
  ListNode* result = solver.addTwoNumbers(l1, l2);
  ListNode* expected = createList({7, 0, 8});

  vector<int> result_vec = listToVector(result);
  vector<int> expected_vec = listToVector(expected);

  assert(compareLists(result, expected) &&
         "Test 1 failed: [2,4,3] + [5,6,4] should equal [7,0,8]");

  deleteList(l1);
  deleteList(l2);
  deleteList(result);
  deleteList(expected);
  cout << "Test 1 passed: [2,4,3] + [5,6,4] = [7,0,8]\n";
}

void test_example_2() {
  Solution solver;
  ListNode* l1 = createList({0});
  ListNode* l2 = createList({0});
  ListNode* result = solver.addTwoNumbers(l1, l2);
  ListNode* expected = createList({0});

  assert(compareLists(result, expected) &&
         "Test 2 failed: [0] + [0] should equal [0]");

  deleteList(l1);
  deleteList(l2);
  deleteList(result);
  deleteList(expected);
  cout << "Test 2 passed: [0] + [0] = [0]\n";
}

void test_example_3() {
  Solution solver;
  ListNode* l1 = createList({9, 9, 9, 9, 9, 9, 9});
  ListNode* l2 = createList({9, 9, 9, 9});
  ListNode* result = solver.addTwoNumbers(l1, l2);
  ListNode* expected = createList({8, 9, 9, 9, 0, 0, 0, 1});

  assert(compareLists(result, expected) &&
         "Test 3 failed: Large numbers with carry");

  deleteList(l1);
  deleteList(l2);
  deleteList(result);
  deleteList(expected);
  cout << "Test 3 passed: Large numbers with carry\n";
}

void test_different_lengths() {
  Solution solver;
  ListNode* l1 = createList({1, 8});
  ListNode* l2 = createList({0});
  ListNode* result = solver.addTwoNumbers(l1, l2);
  ListNode* expected = createList({1, 8});

  assert(compareLists(result, expected) &&
         "Test 4 failed: Different lengths");

  deleteList(l1);
  deleteList(l2);
  deleteList(result);
  deleteList(expected);
  cout << "Test 4 passed: Different lengths\n";
}

void test_carry_over() {
  Solution solver;
  ListNode* l1 = createList({5});
  ListNode* l2 = createList({5});
  ListNode* result = solver.addTwoNumbers(l1, l2);
  ListNode* expected = createList({0, 1});

  assert(compareLists(result, expected) &&
         "Test 5 failed: Simple carry-over");

  deleteList(l1);
  deleteList(l2);
  deleteList(result);
  deleteList(expected);
  cout << "Test 5 passed: Simple carry-over\n";
}

int main() {
  test_example_1();
  test_example_2();
  test_example_3();
  test_different_lengths();
  test_carry_over();

  cout << "All C++ tests passed for Add Two Numbers!\n";
  return 0;
}
