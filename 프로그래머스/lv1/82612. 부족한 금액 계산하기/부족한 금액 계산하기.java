class Solution {
    public long Price(int price, int count){
        int n=1;
        long totalPrice=0;
        while(n<count+1){
            totalPrice+=price*n;
            n++;
        }
        return totalPrice;
    }
    public long solution(int price, int money, int count) {
        long answer = -1;
        answer=(money>Price(price,count))?0:Price(price,count)-money;

        return answer;
    }
}