import java.util.*;
 
class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        ArrayList<Integer> db[][][][] = new ArrayList[3][2][2][2];
        HashMap<String,Integer> dict = new HashMap<>();
        dict.put("cpp", 0); dict.put("java", 1); dict.put("python", 2);
        dict.put("backend", 0); dict.put("frontend", 1);
        dict.put("junior", 0); dict.put("senior", 1);
        dict.put("chicken", 0); dict.put("pizza", 1);
        for(int i=0; i<3; i++){
            for(int j=0; j<2; j++){
                for(int k=0; k<2; k++){
                    for(int l=0; l<2; l++){
                        db[i][j][k][l] = new ArrayList<Integer>();
                    }
                }
            }
        }
        
        for(int i=0; i<info.length; i++){
            String temp[] = info[i].split(" ");
            db[dict.get(temp[0])][dict.get(temp[1])][dict.get(temp[2])][dict.get(temp[3])].add(Integer.parseInt(temp[4]));
        }
        for(int i=0; i<3; i++){
            for(int j=0; j<2; j++){
                for(int k=0; k<2; k++){
                    for(int l=0; l<2; l++){
                        Collections.sort(db[i][j][k][l]);
                    }
                }
            }
        }
        
        for(int idx=0; idx<query.length ; idx++){
            String temp[] = query[idx].split(" and ");
            String temp2[] = temp[3].split(" ");
            
            int is,ie,js,je,ks,ke,ls,le;
            if(temp[0].equals("-")){
                is=0; ie=2;
            }else{
                is = ie = dict.get(temp[0]);
            }
            
            if(temp[1].equals("-")){
                js=0; je=1;
            }else{
                js = je = dict.get(temp[1]);
            }
            
            if(temp[2].equals("-")){
                ks=0; ke=1;
            }else{
                ks = ke = dict.get(temp[2]);
            }
            
            if(temp2[0].equals("-")){
                ls=0; le=1;
            }else{
                ls=le=dict.get(temp2[0]);
            }
            
            int cnt = 0;
            for(int i=is; i<=ie; i++){
                for(int j=js; j<=je; j++){
                    for(int k=ks; k<=ke; k++){
                        for(int l=ls; l<=le; l++){
                            cnt += binarySearch(db[i][j][k][l], Integer.parseInt(temp2[1]));
                        }
                    }
                }
            }
            
            answer[idx] = cnt;
            
        }
                                
        return answer;
    }
    
    public static int binarySearch(ArrayList<Integer> db, int score){
        int left = 0;
        int right = db.size();
        int mid;
        
        while(left<right){
            mid = (left+right)/2;
            
            if(db.get(mid) >= score){
                right = mid;
            }else{
                left = mid+1;
            }
        }
        
        return db.size()-right;
        
    }
}