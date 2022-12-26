import java.util.HashSet;
import java.util.Arrays;
import java.util.Set;
class Solution {
    public int solution(int[] elements) {
        int[] newElements=new int[elements.length*2];
    for(int i=0;i<newElements.length;i++){
      newElements[i]=i<elements.length?elements[i]:elements[i-elements.length];
    }


    Set<Integer> list=new HashSet<>();
    for(int i=1;i<=elements.length;i++){
      for(int j=0;j<elements.length;j++){
          list.add(Arrays.stream(newElements,j,j+i).sum());
      }
    }


    return list.size();
    }
}