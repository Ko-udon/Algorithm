import java.util.Arrays;

class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        int[] arr={a,b};
        int min = Arrays.stream(arr).min().getAsInt();
		int max = Arrays.stream(arr).max().getAsInt();
        while(!(min % 2 == 1 && max == min + 1)){  
            max=(max+1)/2;
            min=(min+1)/2;
            answer++;
        }
        System.out.println("Hello Java");

        return answer;
    }
}