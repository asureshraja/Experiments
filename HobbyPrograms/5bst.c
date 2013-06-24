#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int data;
    struct node *left;
    struct node *right;

}NODE;

void addData(NODE** root,int value)
{

    if(*root==NULL)
    {

        *root = (NODE *) malloc(sizeof(NODE));

        (*root)->data=value;
        (*root)->left=NULL;
        (*root)->right=NULL;
        return;
    }
    else if(value<(*root)->data)
    addData(&(*root)->left,value);
    else
    addData(&(*root)->right,value);
    return;
}
void inorder(NODE *root)
{
if(root!=NULL)
{
inorder(root->left);
printf("%d",root->data);
inorder(root->right);
}
}
int main()
{
NODE *bst;
bst=NULL;
addData(&bst,5);
addData(&bst,6);
addData(&bst,3);
inorder(bst);
}
