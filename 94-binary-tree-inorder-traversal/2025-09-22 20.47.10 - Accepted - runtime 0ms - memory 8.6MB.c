/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int *a=(int*)malloc(100*sizeof(int));
    int i=0;
    void inorder(struct TreeNode* node){
        if(node==NULL) return;
        inorder(node->left);
        a[i++]=(node->val);
        inorder(node->right);
    }
    inorder(root);
    *returnSize=i;
    return a;
}