

> 문제 설명
> 
> 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
> 
> 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
> 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


> 제한사항
>
> 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
> completion의 길이는 participant의 길이보다 1 작습니다.
> 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
> 참가자 중에는 동명이인이 있을 수 있습니다.

> 입출력 예
> 
> participant 	completion 	return
> 
> ["leo", "kiki", "eden"] 	["eden", "kiki"] 	"leo"
> 
> ["marina", "josipa", "nikola", "vinko", "filipa"] ["josipa", "filipa", "marina", "nikola"] "vinko"
> 
> ["mislav", "stanko", "mislav", "ana"] ["stanko", "ana", "mislav"] "mislav"

> 입출력 예 설명
> 
> 예제 #1
> "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
> 
> 예제 #2
> "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
> 
> 예제 #3
> "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

    package RetiredPerson;

    import java.util.HashMap;
    
    class Solution {
        public String solution(String[] participant, String[] completion) {
        
                HashMap<String, Integer> participantHash = new HashMap<>();
        
                String answer = "";
        
                // 입력된 참가자 명단을 하나씩 해시 맵에다가 넣어줄 것이다.
                for (String item : participant) {
                    // 이때 하나씩 원소를 넣으면서, 그 원소가 이미 해시 맵에 들어있다면
                    if (participantHash.containsKey(item)) {
                        //해당 아이템을 키로 가진 해시 맵의 value를 + 1 해준다 
                        participantHash.put(item, participantHash.get(item) + 1);
                    } else {
                        //그렇지 않으면 해당 아이템을 가진 키로 value 를 1로 새로 셋팅한다.
                        participantHash.put(item, 1);
                    }
                }
        
                // 입력된 완주한 명단을 하나씩 순회할 것이다.
                for (String item : completion) {
                    // 이때 완주명단을 하나씩 도는 중에, 참가자 해시 맵에 들어있다면
                    if (participantHash.containsKey(item)) {
                        // 해당하는 키 값을 가진 참가자 해시맵의 value를 -1 해준다.
                        participantHash.put(item, participantHash.get(item) - 1);
                    }
                }
                
                // 참가자 해시맵 키를 하나씩 순회 할 것이다. 
                for (String item : participantHash.keySet()) {
                    // 참가자 해시맵의 키를 토대로 value 를 꺼냈을 때 그 값이 0이 아니면
                    // 중복된 이름을 가진 사람이 완주하지 못한 것이다.
                    // 왜냐하면 완주한 명단을 돌면서 참가자 명단과 비교할 때 
                    // 이미 참가자 명단에 존재하는 키값이라면 +1 을 해주었기 때문에
                    // 중복된 이름을 포함하여 참가자 명단을 생성했다고 볼 수 있다.
                    if (participantHash.get(item) != 0) {
                        // 그 사람은 완주를 못한것이므로 answer에 넣는다.
                        answer = item;
                    }
                }
                return answer;
        
            }
    }

    // 다 풀고나서 느낀 점
    // 3명이 중복되면 어떻게 되는건가?
    // 3명이 중복되는 참가자명을 가지지만 그중에서 한명만 완주하면 어떻게 되는거야?

    public class Main {
        public static void main(String[] args) {
            String [] part = {"mislav", "stanko", "mislav", "ana", "mislav"};
            String [] com = {"stanko", "ana", "mislav"};

            // String [] part = {"marina", "josipa", "nikola", "vinko", "filipa"};
            // String [] com = {"josipa", "filipa", "marina", "nikola"};

            // String [] part = {"leo", "kiki", "eden"};
            //  String [] com = {"eden", "kiki"};

            Solution s = new Solution();

            System.out.println(s.solution(part, com));
        }
    }
