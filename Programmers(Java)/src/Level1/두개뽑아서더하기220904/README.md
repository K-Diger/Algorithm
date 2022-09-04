# 두 개 뽑아서 더하기

# 문제 설명

정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 

배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항

    numbers의 길이는 2 이상 100 이하입니다.
    numbers의 모든 수는 0 이상 100 이하입니다.

# 입출력 예

|numbers |	result|
|---|---|
|[2,1,3,4,1] |	[2,3,4,5,6,7]|
|[5,0,2,7] |	[2,5,7,9,12]|

# 입출력 예 설명

## 입출력 예 #1

    2 = 1 + 1 입니다. (1이 numbers에 두 개 있습니다.)
    3 = 2 + 1 입니다.
    4 = 1 + 3 입니다.
    5 = 1 + 4 = 2 + 3 입니다.
    6 = 2 + 4 입니다.
    7 = 3 + 4 입니다.
    따라서 [2,3,4,5,6,7] 을 return 해야 합니다.

## 입출력 예 #2

    2 = 0 + 2 입니다.
    5 = 5 + 0 입니다.
    7 = 0 + 7 = 5 + 2 입니다.
    9 = 2 + 7 입니다.
    12 = 5 + 7 입니다.
    따라서 [2,5,7,9,12] 를 return 해야 합니다.

---

# 풀이 - 코드

    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    
    public class Main {
    
        public static int[] solution(int[] numbers) {
            Map<Integer, Integer> tempHashMapForCombination = new HashMap<>();
            int numbersLength = numbers.length;
    
            for (int i = 0; i < numbersLength - 1; i++) {
                for (int j = i + 1; j < numbersLength; j++) {
                    tempHashMapForCombination.put(numbers[i] + numbers[j], 0);
                }
            }
    
            return tempHashMapForCombination.keySet().stream()
                    .sorted()
                    .mapToInt(i -> i)
                    .toArray();
        }
    
        public static void main(String[] args) {
            System.out.println(Arrays.toString(solution(new int[]{2, 1, 3, 4, 1})));
        }
    }

# 풀이 - 상세

    Map<Integer, Integer> tempHashMapForCombination = new HashMap<>();

입력받은 배열의 원소의 합의 조합을 담을 HashMap을 만든다.

HashMap은 중복된 Key 가 있으면 그에 따른 Value 처리를 따로 할 뿐 Key 자체는 늘어나지 않기 때문에 이 자료구조를 썼다.

<br>
        
    int numbersLength = numbers.length;

    for (int i = 0; i < numbersLength - 1; i++) {
        for (int j = i + 1; j < numbersLength; j++) {
            tempHashMapForCombination.put(numbers[i] + numbers[j], 0);
        }
    }

입력받은 배열의 길이를 담아둔 후

배열의 길이만큼 버블정렬 느낌으로(i, j 로 일일히 탐색) 각각 탐색하여 원소의 조합을 만들어준다.

이때, 중복된 Key가 나오더라도, 그 Value 값은 손대지 않는다.

<br>

    return tempHashMapForCombination.keySet().stream()
            .sorted()
            .mapToInt(i -> i)
            .toArray();

위와 같이 반환을 해주는데

KeySet -> Array 로 변환하는 Stream 구문이다.

또한 중간연산에 정렬까지 해줘야 정답으로 인정될 수 있다.