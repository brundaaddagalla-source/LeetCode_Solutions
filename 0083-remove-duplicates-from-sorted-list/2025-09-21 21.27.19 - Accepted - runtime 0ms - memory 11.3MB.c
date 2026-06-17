/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head==NULL) return NULL;
    struct ListNode *preptr=head, *ptr=head->next;
    while(ptr!=NULL){
        if(preptr->val==ptr->val){
            preptr->next=ptr->next;
            free(ptr);
            ptr=preptr->next;
        }
        else{
            preptr=preptr->next;
            ptr=ptr->next;
        }
    }
    return head;
}