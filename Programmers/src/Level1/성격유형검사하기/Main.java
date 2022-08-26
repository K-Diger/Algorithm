package Level1.성격유형검사하기;

// ["AN", "CF", "MJ", "RT", "NA"] 	[5, 3, 2, 7, 5] 	"TCMA"
// ["TR", "RT", "TR"] 	[7, 1, 3] 	"RCJA"

// RT CF JM AN


// 1, 7 : 3점
// 2, 6 : 2점
// 3, 5 : 1점
// 4 : 0점

class Solution {

    static int R, T, C, F, J, M, A, N = 0;

    public String solution(String[] survey, int[] choices) {
        String answer = "";

        int choiceLen = choices.length;

        for (String item : survey) {
            for (int i = 0; i < choiceLen; i++) {

                String leftSurvey = item.substring(0, 1);
                String rightSurvey = String.valueOf(item.charAt(1));

                System.out.println("R = " + R + ", T = " + T + ", C = " + C + ", F = " + F + ", J = " + J + ", M = " + M + ", A = " + A + ", N = " + N);

                System.out.println("leftSurvey = " + leftSurvey);
                System.out.println("rightSurvey = " + rightSurvey);

                // 첫 번째 문자 비교 if 문
                if (leftSurvey.equals("R")) {
                    R += choices[i];
                }
                else if (leftSurvey.equals("T")) {
                    T += choices[i];
                }
                else if (leftSurvey.equals("C")) {
                    C += choices[i];
                }
                else if (leftSurvey.equals("F")) {
                    F += choices[i];
                }
                else if (leftSurvey.equals("J")) {
                    J += choices[i];
                }
                else if (leftSurvey.equals("M")) {
                    M += choices[i];
                }
                else if (leftSurvey.equals("A")) {
                    A += choices[i];
                }
                else if (leftSurvey.equals("N")) {
                    N += choices[i];
                }

                // 두 번째 문자 비교 if 문
                if (rightSurvey.equals("R")) {
                    R += choices[i];
                    break;
                }
                else if (rightSurvey.equals("T")) {
                    T += choices[i];
                    break;
                }
                else if (rightSurvey.equals("C")) {
                    C += choices[i];
                    break;
                }
                else if (rightSurvey.equals("F")) {
                    F += choices[i];
                    break;
                }
                else if (rightSurvey.equals("J")) {
                    J += choices[i];
                    break;
                }
                else if (rightSurvey.equals("M")) {
                    M += choices[i];
                    break;
                }
                else if (rightSurvey.equals("A")) {
                    A += choices[i];
                    break;
                }
                else if (rightSurvey.equals("N")) {
                    N += choices[i];
                    break;
                }
            }

        }

        System.out.println(R + ", " + T + ", " + C + ", " + F + ", " + J + ", " + M + ", " + A + ", " + N);

        return answer;
    }

    public static void main(String[] args) {

        String[] survey = {"AN", "CF", "MJ", "RT", "NA"};
        int[] choices = {5, 3, 2, 7, 5};

        Solution s = new Solution();

        s.solution(survey, choices);
    }
}