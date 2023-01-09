import java.util.HashSet;
import java.util.Iterator;
class Solution {
    HashSet<Integer> numberSet = new HashSet<>();

  public boolean isPrime(int num) {
    if(num == 1 || num == 0) {
      // 1과 0은 소수에서 제외되니 false처리
      return false;
    }

    //⭐⭐ 소수를 찾을때는 아리스토테네스의 체의 limit을 계산한다.
    // 소수인지 확인하려고 하는 값의 제곱근을 구한다. => Math.sqrt(number)
    int limit = (int) Math.sqrt(num);

    // 에라토스테네스의 체에 따라 limit까지만 배수 여부를 확인한다.
    for(int i=2; i<=limit; i++) {
      if(num % i == 0) {
        return false;
      }
    }

    return true;
  }
  public void recursive(String t,String others){
    if(!t.equals("")){
      numberSet.add(Integer.parseInt(t));
    }

    for(int i=0;i<others.length();i++){
      if(!t.equals("")){
        numberSet.add(Integer.valueOf(t));
      }
      recursive(t+others.charAt(i),others.substring(0, i) + others.substring(i+1));
    }

  }

  public int solution(String numbers) {
    int answer = 0;
    recursive("",numbers);
    Iterator<Integer> it= numberSet.iterator();
    while (it.hasNext()){
      if(isPrime(it.next())){
        answer++;
      }
    }
    return answer;
  }
}