import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i =0; i<players.length; i++){
            map.put(players[i],i);
        }
        //백준허브 테스트
        
        for(int i =0; i<callings.length; i++){
            int pos = map.get(callings[i]);
            String player = players[pos - 1];
            players[pos-1] = callings[i];
            players[pos] = player;
            
            map.replace(player, map.get(player) + 1);
            map.replace(callings[i], map.get(callings[i]) - 1);
        }
        
        //System.out.print(map);
        
        
        
        return players;
    }
    
    
}