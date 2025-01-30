class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
       ArrayList<Boolean> list=new ArrayList<>();
       int maximum=0;
       for(int candy:candies){
        maximum=Math.max(maximum,candy);
       } 
       for(int candy:candies){
        list.add(candy+extraCandies>=maximum);
       }
       return list;
    }
}