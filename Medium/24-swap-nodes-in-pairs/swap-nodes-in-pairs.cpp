/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* temp= head;
        if (temp == nullptr or temp->next == nullptr){
            return head;
        }

        ListNode* newhead = temp->next;
        ListNode* next_node = temp->next;
        ListNode* new_pair = next_node->next;
        next_node->next = temp;
        temp->next = new_pair;

        while(temp->next!=nullptr and temp->next->next !=nullptr){
            next_node = new_pair->next;
            temp->next = next_node;
            new_pair->next = next_node->next;
            next_node->next = new_pair;
            temp=new_pair;
            new_pair = new_pair->next;
        }
        
        return newhead;

    }
};