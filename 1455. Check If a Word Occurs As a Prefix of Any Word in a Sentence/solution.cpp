#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
    struct trienode{
        int idx;
        std::unordered_map<char,trienode*> child;
    };
    trienode *root = new trienode;

    void trieInsert(std::string& word,int index){
        trienode* curr = root;
        for(int i=0;word[i];++i){
            if(!curr->child.count(word[i])){
                curr->child[word[i]] = new trienode;
                curr->child[word[i]]->idx = index;
            }
            curr = curr->child[word[i]];
        }
    }
    int trieSearch(std::string& word){
        trienode* curr = root;
        for(int i=0;word[i];++i){
            if(!curr->child.count(word[i]))
                return -1;
            curr = curr->child[word[i]];
        }
        return curr->idx;
    }
public:
    int isPrefixOfWord(std::string sentence, std::string searchWord) {
        int n=sentence.size();
        int index=1;

        for(int i=0;i<n;++i){
            //Extract a word
            std::string word="";
            while(i<n and sentence[i]!=' '){
                word.push_back(sentence[i]);
                i++;
            }
            trieInsert(word,index);
            index++;
        }
        return trieSearch(searchWord);
    }
};