class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String[] tmp1=new String[n];
        String[] tmp2=new String[n];
        
        for(int i=0;i<arr1.length;i++){
            tmp1[i]=Integer.toString(arr1[i],2);
            while(tmp1[i].length()!=n){
                tmp1[i]="0"+tmp1[i];
            }
        }
        for(int i=0;i<arr1.length;i++){
            tmp2[i]=Integer.toString(arr2[i],2);
            while(tmp2[i].length()!=n){
                tmp2[i]="0"+tmp2[i];
            }
        }
        
        
        for(int i=0;i<n;i++){
            answer[i]="";
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(tmp1[i].charAt(j)=='1'||tmp2[i].charAt(j)=='1'){
                    answer[i]+="#";
                }
                else{
                    answer[i]+=" ";
                }
            }
        }
        //System.out.println(answer[0]);
        
        return answer;
    }
}