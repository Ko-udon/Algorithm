import java.util.Stack;
class Solution {
    public String solution(String p) {

    String answer;

    // 1. 올바른 괄호 문자열이라면, 바로 문자열을 반환한다.
    if (check(p)) {
      return p;
    }
    // 2. 나머지 균현잡힌 괄호 문자열 => 올바른 괄호 문자열 변환 메소드 호출 및 answer에 저장.
    answer = split(p);

    return answer;
  }

  public static String split(String w) {

    // 1. 입력된 문자열 w를 u와 v로 나누어 저장하는 StringBuilder클래스 객체.
    StringBuilder u = new StringBuilder();
    StringBuilder v = new StringBuilder();

    // 2. 빈 문자열인 경우, 빈 문자열을 반환.
    if (w.length() == 0) {
      return "";
    }

    u.append(w.substring(0, getString(w) + 1));
    v.append(w.substring(getString(w) + 1));

    //u가 올바른 괄호 문자열일 경우
    if (check(u.toString())) {
      u.append(split(v.toString()));
      //올바른 괄호가 아닌 경우
    } else {
      StringBuilder str = new StringBuilder();
      str.append("(");
      str.append(split(v.toString()));
      str.append(")");
      str.append(turn(u.toString()));
      return str.toString();
    }

    return u.toString();
  }

  public static String turn(String p) {
    String tmp = "";
    for (int i = 1; i < p.length() - 1; i++) {
      if (p.charAt(i) == '(') {
        tmp += ")";
      } else {
        tmp += "(";
      }
    }
    return tmp;
  }

  public static boolean check(String p) {
    boolean is = true;
    Stack<Character> stack = new Stack<Character>();

    for (int i = 0; i < p.length(); i++) {
      if (p.charAt(i) == '(')  // 현재 (가 들어갈 자리면 스택에 넣는다.
      {
        stack.push('(');
      } else {
        if (stack.isEmpty()) // 현재 )가 들어갈 자리인데 스택이 비어있을경우 -> false
        {
          return false;
        } else {
          stack.pop();    // 현재 )가 들어갈 상태에서 스택에 괄호('(')가 있는경우 -> pop
        }
      }
    }
    is = (stack.isEmpty()) ? true : false;
    return is;
  }

  public static int getString(String p) {
    int cnt = 0;
    int tmp = 0;
    String u = "";
    if (p.charAt(tmp) == '(') {
      cnt++;
    } else {
      cnt--;
    }

    while (cnt != 0) {
      tmp++;
      if (p.charAt(tmp) == '(') {
        cnt++;
      } else {
        cnt--;
      }
    }
    return tmp;
  }
}