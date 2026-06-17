/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *merge=NULL,*tail=NULL;
    struct ListNode *new_node;
    while(list1!=NULL && list2!=NULL){
        new_node=(struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->next=NULL;
        if(list1->val<=list2->val){
            new_node->val=list1->val;
            list1=list1->next;
        }else{
            new_node->val=list2->val;
            list2=list2->next;
        }
        if(merge==NULL){
            merge=new_node;
            tail=merge;
        }else{
            tail->next=new_node;
            tail=tail->next;
        }        
    }
    while(list1!=NULL){
        new_node=(struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val=list1->val;
        new_node->next=NULL;
        if(merge==NULL){
            merge=new_node;
            tail=merge;
        }else{
            tail->next=new_node;
            tail=tail->next;
        }
        list1=list1->next;
    }
    while(list2!=NULL){
        new_node=(struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val=list2->val;
        new_node->next=NULL;
        if(merge==NULL){
            merge=new_node;
            tail=merge;
        }else{
            tail->next=new_node;
            tail=tail->next;
        }
        list2=list2->next;
    }
    return merge;
}