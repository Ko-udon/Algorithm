class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];        
        
        for(int i=0; i<targets.length; i++) {
        	for(int j=0; j<targets[i].length(); j++) {
        		int idx = 101;
        		for(int k=0; k<keymap.length; k++) {
        			int index = keymap[k].indexOf(targets[i].charAt(j));
                    //해당하는 문자가 없으면 -1을 반환하므로
        			if(index != -1) {
        				if(idx > index) {
        					idx = index;
        				}
        			}
        		}
        		if(idx == 101) {
        			answer[i] = -1;
        			break;
        		}
        		else {
        			answer[i] += idx+1;
        		}        		        		
        	}
        }
        
        return answer;
    }
}