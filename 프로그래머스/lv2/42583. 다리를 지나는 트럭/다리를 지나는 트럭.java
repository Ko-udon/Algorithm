import java.util.LinkedList;
import java.util.Queue;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int nowWeight = 0;
        int time = 0;
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < truck_weights.length; i++) {
          int truck = truck_weights[i];
          while (true) {
            //다리가 비어있다면 트럭 넣기
            if (q.isEmpty()) {
              q.add(truck);
              nowWeight += truck;
              time++;
              break;
            }
            //다리가 꽉찬 경우,
            else if (q.size() == bridge_length) {
              nowWeight -= q.poll();
            } else {
              if (nowWeight + truck <= weight) {
                q.add(truck);
                nowWeight += truck;
                time++;
                break;
              }else{
                //다리 길이는 충분하지만 무게때문에 못태우는 경우
                q.add(0);  //더미 데이터를 넣어 큐가 차게끔 하기
                time++;
              }
            }

          }

        }
        //마지막에 반복문이 끝나기 때문에
        //마지막 트럭이 다리에 탑승 + 다리 길이 만큼 시간 초과
        return time+bridge_length;
    }
}