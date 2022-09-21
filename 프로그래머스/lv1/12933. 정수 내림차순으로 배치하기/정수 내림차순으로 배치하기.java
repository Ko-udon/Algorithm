
class Solution {
    String s="";
    public long solution(long n) {
        Solution t=new Solution();
        Long.toString(n).chars().sorted().forEach(c -> t.s = Character.valueOf((char)c) + t.s);
        return Long.parseLong(t.s);
    }
}