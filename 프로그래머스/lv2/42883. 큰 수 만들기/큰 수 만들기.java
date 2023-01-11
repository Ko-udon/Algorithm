class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder("");
        int bringLen = number.length() - k;  //문자에서 가장 큰 한개의 값을 골라도 뒤에 길이가 k보다 작으면 수를 만들수 없다. Greeedy
        
        int start = 0;
        while (start < number.length() && answer.length() < bringLen) {
          int tmp = k + answer.length() + 1;
          int max = 0;
          for (int i = start; i < tmp; i++) {
            if (max < number.charAt(i) - '0') {
              max = number.charAt(i) - '0';
              start = i + 1;
            }
          }
          answer.append(Integer.toString(max));
        }
        return answer.toString();
    }
}