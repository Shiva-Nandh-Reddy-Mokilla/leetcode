class Solution {
    public String reverseVowels(String s) {
        int left=0;
        int right=s.length()-1;
        Set<Character> vowels= Set.of('a','A','e','E','i','I','o','O','u','U');
        char[] check= s.toCharArray();
        while(left<right){
            if(!vowels.contains(check[left])){
                left++;
            }
            else if(!vowels.contains(check[right])){
                right--;
            }
            else{
                char temp=check[left];
                check[left]=check[right];
                check[right]=temp;
                left++;
                right--;
            }
        }

        return new String(check);





            }
        }

        
    
