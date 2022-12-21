import java.util.Arrays;
import java.util.Collections;
import java.util.List;
class Solution {
    public String[] solution(String[] files) {
        String[] answer = {};
        Arrays.sort(files,(o1,o2)->{
            String head1=o1.split("[0-9]")[0].toLowerCase();
            String head2=o2.split("[0-9]")[0].toLowerCase();

            if(head1.compareTo(head2)==0){
                String numTail1=o1.substring(head1.length());
                String numTail2=o2.substring(head2.length());
                return Integer.parseInt(calNumber(numTail1))-Integer.parseInt(calNumber(numTail2));
            }else{
                return head1.compareTo(head2);
            }
        });

        // List<String> list= Arrays.stream(files).toList();
        // System.out.println(list);

        return files;
    }
    private static String calNumber(String numTail){
        StringBuilder sb = new StringBuilder();
        for (char c : numTail.toCharArray()) {
            if (Character.isDigit(c) && sb.length() <= 5) {
                sb.append(c);
            } else {
                return sb.toString();
            }
        }
        return sb.toString();

    }
}