class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;

        String[] skillArr= skill.split("");
        for(int i=0;i<skill_trees.length;i++) {
            String tmp=skill_trees[i];
            for(int j=0;j<tmp.length();j++){
                String s=Character.toString(tmp.charAt(j));
                if(!skill.contains(s)) tmp=tmp.replace(s,"0");
            }
            tmp=tmp.replace("0","");  //이유는 모르겟는데 E가 자꾸 안지워짐,,
            //System.out.println(tmp);
            if(skill.indexOf(tmp)==0){
                answer++;
            }

        }

        return answer;
    }
}