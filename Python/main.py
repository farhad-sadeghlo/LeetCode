# from Q13roman_to_integer import roman_to_integer
# from Q242valid_anagram import validAnagram
# from Q916Word_Subsets import wordSubsets
# from Q858Mirror_Reflection import mirror_reflection
# from Anagram_List import anagram_list
# from hundred_liked_questions_Two_Sum import twoSum
# from contains_duplicate import duplicates
# from Add_Two_Numbers_Singly_Linked_List import ListNode
# from Q1672_Richest_Customer_Wealth import Solution
# from Q1480Running_Sum_of_1d_Array import Solution
# from Q1342Number_of_Steps_to_Reduce_a_Number_to_Zero import Solution
# from Q412_Fizz_Buzz import Solution
# from Q876_Middle_of_the_Linked_List import Solution
# from Q876_Middle_of_the_Linked_List import ListNode
# from Q383_RansomNote import Solution
# from Q21Merge_Two_Sorted_Lists import MergeTwoLinkedLists
from Linked_List import LinkedList
from Q21Merge_Two_Sorted_Lists import MergeTwoSortedLists
from copy import deepcopy

if __name__ == '__main__':
    # roman_to_integer(input('please type in your roman number: ')).romanToInt()
    # validAnagram().anagram()
    # wordSubsets(input('please type in list of your words: '), input('please type in list of your chars: ')).subsets()
    # mirror_reflection(input('please type in p: '), input('please type in q: ')).reflection()
    # anagram_list(input('please type in your list of words: ')).anagram_list()
    # twoSum(input('please type in your list of numbers: '), input('please type in your summation target to be matched from the list: ')).twoSum()
    # duplicates(input('please type in your list of numbers: ')).containsDuplicate()
    # ListNode().addTwoNumbers()
    # print(Solution().maximumWealth(input('please type in your list of accounts: '))
    # print(Solution().runningSum(input('please type in your list of numbers: ')))
    # print(Solution().numberOfSteps(input('please type in your number: ')))
    # print(Solution().fizzBuzz(input('please type in your number: ')))
    ############################################################
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # print(Solution().middleNode(node1))
    ############################################################
    # print(Solution().canConstruct(input('please type in your ransomNote: '), input('please type in your magazine: ')))
    ############################################################
    # LinkedList
    ll = LinkedList()
    # lst = input('Please type in your list: ')
    for val in sorted([2, 9, 1, 3, -2, 10, 99]):
        ll.append(val)
    l1 = deepcopy(ll)
    print('This is your first linkedlist')
    l1.print_list()

    ll.reverse()
    print('This is the reversed first linkedlist')
    ll.print_list()

    ll = LinkedList()
    for val in sorted([5, 1, 4, 2, 125]):
        ll.append(val)
    l2 = deepcopy(ll)
    print('This is your second linkedlist')
    l2.print_list()


    # print('This is a deepcopy of l1')
    # l1.print_list()
    # print('This is a deepcopy of l2')
    # l2.print_list()
    ll = LinkedList()
    l3 = MergeTwoSortedLists(l1=l1.head, l2=l2.head).merge_two_list()
    ll.head = l3
    print('This is the merged linked list')
    ll.print_list()

    # print(MergeTwoLinkedLists(node1, node2).print_list())
    # print(MergeTwoLinkedLists(input('please type in your first linked list: '), input('please type in your second linked list: ')).merge_two_sorted_linked_lists())