# 컬렉션 관련 메모

---

# 컬렉션의 최대 최소

# 1.1 컬렉션(HashMap) Key, Value 최댓값 구하기

### Collections.max()

    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    
    // HashMap Key, Value 최댓값 구하기
    // Level 1. 폰켓몬 에서 사용됨
    public class HashMapKeyAndValueMin {
    
        public static void main(String[] args) {
    
            Map<Integer, Integer> pairInformation = new HashMap<Integer, Integer>();
    
            // HashMap Key 최댓값
            int maxKey = Collections.max(pairInformation.keySet());
    
            // HashMap Value 최댓값
            int maxValue = Collections.max(pairInformation.values());
        }
    }

# 1.2 컬렉션(HashMap) Key, Value 최소값 구하기

### Collections.min()

    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    
    // HashMap Key, Value 최솟값 구하기
    // Level 1. 폰켓몬 에서 사용됨
    public class HashMapKeyAndValueMin {
    
        public static void main(String[] args) {
    
            Map<Integer, Integer> pairInformation = new HashMap<Integer, Integer>();
    
            // HashMap Key 최솟값
            Integer minKey = Collections.min(pairInformation.keySet());
    
            // HashMap Value 최솟값
            Integer minValue = Collections.min(pairInformation.values());
        }
    }

---
