import heapq
from typing import List, Tuple

def min_merge_cost_with_plan(lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Повертає:
      total_cost — мінімальна можлива сума витрат,
      plan — список кроків у вигляді (a, b, a_plus_b) у тому порядку, як з'єднували.
    Алгоритм: завжди беремо дві найкоротші довжини (мін-купа).
    """
    if not lengths or len(lengths) == 1:
        return 0, []

    heap = list(lengths)
    heapq.heapify(heap)

    total_cost = 0
    plan = []

    while len(heap) > 1:
        a = heapq.heappop(heap)  # найменший
        b = heapq.heappop(heap)  # другий найменший
        s = a + b
        total_cost += s
        plan.append((a, b, s))
        heapq.heappush(heap, s)

    return total_cost, plan


# Приклад:
if __name__ == "__main__":
    lengths = [4, 6, 8, 12]
    cost, plan = min_merge_cost_with_plan(lengths)
    print("Порядок об'єднання:")
    for a, b, s in plan:
        print(f"{a} + {b} = {s}")
    print("Мінімальна сума витрат:", cost)