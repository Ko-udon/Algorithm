class Solution {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        var answer: String = "Yes"
        var index1 = 0
        var index2 = 0
        for(each in goal) when {
            index1 < cards1.size && each == cards1[index1] -> index1++
            index2 < cards2.size && each == cards2[index2] -> index2++
            else -> return "No"
        }
        return answer
    }
}