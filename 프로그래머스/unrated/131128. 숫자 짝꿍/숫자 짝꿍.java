import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        StringBuilder sb = new StringBuilder();
        TreeMap<Character, Integer> mapX = new TreeMap<>(Collections.reverseOrder());
        TreeMap<Character, Integer> mapY = new TreeMap<>(Collections.reverseOrder());
         for (char s : X.toCharArray()) {
            Integer count = mapX.get(s);
            if (count == null) {
                mapX.put(s, 1);
            } else {
                mapX.put(s, count + 1);
            }

        }
        for (char s : Y.toCharArray()) {
            Integer count = mapY.get(s);
            if (count == null) {
                mapY.put(s, 1);
            } else {
                mapY.put(s, count + 1);
            }
        }
        
        for(Map.Entry<Character, Integer> e : mapX.entrySet()) {
            if (mapY.containsKey(e.getKey())) {
                while (mapY.get(e.getKey()) > 0 && mapX.get(e.getKey()) > 0) {
                    sb.append(e.getKey());
                    mapX.put(e.getKey(), mapX.get(e.getKey()) - 1);
                    mapY.put(e.getKey(), mapY.get(e.getKey()) - 1);
                }
            }
        }

        if (sb.length() == 0) {
            return "-1";
        } else if (sb.charAt(0) == '0') {
            return "0";
        }

        return sb.toString();
    
    }
    
}