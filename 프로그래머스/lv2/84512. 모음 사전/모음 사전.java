class Solution {
    public int solution(String word) {
        String words="AEIOU";
        int[] x={781,156,31,6,1};
        int index,result= word.length();
        for(int i=0;i<word.length();i++){
          index=words.indexOf(word.charAt(i));
          result+=x[i]*index;
        }
        System.out.println(result);
        return result;
    }
}