import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();

        Set<Character> set = new HashSet<>();

        //제외할 암호 skip 정리
        for (Character c : skip.toCharArray()) {
            set.add(c);
        }
        
        //skip을 제외한 문자 넣기
        StringBuilder sb = new StringBuilder();

        for (char i = 'a'; i <= 'z'; i++) {
            if (!set.contains(i)) {
                sb.append(i);
            }
        }
        
        //skip의 길이는 최대 10, 넉넉하게 3번 반복
        //꼭 3번이 아니여도 상관 없음
        
        String checkString = sb.toString().repeat(3);

        for (int i = 0; i < s.length(); i++) {
            char curChar = s.charAt(i);

            answer.append(checkString.charAt(checkString.indexOf(curChar) + index));
        }
        
        
        return answer.toString();
    }
}