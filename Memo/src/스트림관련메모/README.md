# 스트림 관련 메모

---

# Collection(HashMap KeySet) 순회하며 해당 값 정렬 및 row int array 로 변환

    tempHashMapForCombination.keySet().stream()
        .sorted()
        .mapToInt(i -> i)
        .toArray();