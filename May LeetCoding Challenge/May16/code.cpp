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
    ListNode* oddEvenList(ListNode* head) {
        if(head ==  NULL){
            return head;
        }
        int counter = 1;
        ListNode* endptr =  head;
        
        //reaching the end for reference .
        
        while(endptr->next != NULL){
            endptr = endptr->next;
            counter =  counter+1;
        }
        
        if(counter == 2 || counter == 1){
            return head;
        }
            
        
        ListNode* privousNode = NULL; 
        ListNode* currentptr =  head;
        
        
        for(int i =1 ; i <= counter;i++){
            if(i%2 == 0){
                //appending the next node to previous node.
                ListNode* next =   currentptr->next;
                privousNode->next = next;
                endptr->next =  currentptr;
                currentptr->next = NULL;
                endptr =  currentptr;
                currentptr = next;
                
                // privousNode = currentptr;
                // currentptr = currentptr->next;
                    
                // printing the values
               //  ListNode* printptr =  head;
               //  while (printptr != NULL){
               //      cout<<printptr->val;
               //      printptr=printptr->next;
               //  }
               // cout<<endl;
            }else{
                privousNode = currentptr;
                currentptr = currentptr->next;
               
            }
       
        }
        
        return head;
        
        
        
    }

};