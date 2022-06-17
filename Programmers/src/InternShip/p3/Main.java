package InternShip.p3;

import java.util.Arrays;

class Solution {
    public int[] solution(int n, String[] plans, String[] clients) {
        int[] answer = new int[clients.length];

        String[] clientData = new String[clients.length];
        String[] plansData = new String[plans.length];


        String[] clientService = new String[clients.length];
        String[] plansService = new String[plans.length];



        for (int i = 0; i < clientData.length; i++) {
            int index = clients[i].indexOf(" ");

            clientData[i] = clients[i].substring(0, index);

        }

        for (int i = 0; i < clientService.length; i++) {
            int index = clients[i].indexOf(" ");

            clientService[i] = clients[i].substring(index+1);

        }

        for (int i = 0; i < plansData.length; i++) {
            int index = plans[i].indexOf(" ");

            plansData[i] = plans[i].substring(0, index);

        }

        for (int i = 0; i < plansService.length; i++) {
            int index = plans[i].indexOf(" ");

            plansService[i] = plans[i].substring(index+1);

        }

        for (int i = 0; i < plansService.length-1; i++) {
            plansService[i+1] += " " + plansService[i];

        }

        for (int i = 0; i < clientData.length; i++) {
            for (int j = 0; j < plansData.length; j++) {
                if (Integer.parseInt(plansData[j]) > Integer.parseInt(clientData[i])) {
                    if (plansService[j].contains(clientService[i])) {
                        answer[i] = j;
                    }
                }

            }

        }

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {

        Solution s = new Solution();

        int n = 5;

        String[] plans = {"100 1 3", "500 4", "2000 5"};
        String[] clients = {"300 3 5", "1500 1", "100 1 3", "50 1 2"};

        s.solution(n, plans, clients);
    }
}
