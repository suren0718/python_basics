import heapq

def min_days_to_produce_heap(machines, target):
    heap = []

    # machines = [(units, maint_days)]
    for idx, (units, maint_days) in enumerate(machines):
        cycle_len = 1 + maint_days   # 1 day for production + maint_days
        heapq.heappush(heap, (1, idx, units, cycle_len))  # first production on day 1
        print(heap)
    produced = 0
    last_day = 0

    while produced < target:
        day, idx, units, cycle_len = heapq.heappop(heap)
        produced += units
        last_day = day

        # machine will be ready again after full cycle
        heapq.heappush(heap, (day + cycle_len, idx, units, cycle_len))

    return last_day


# Example usage:
machines = [
    (10, 2),   # produces 10 units in 1 day, then 2 days maintenance
    (5, 1)     # produces 5 units in 1 day, then 1 day maintenance
]
target = 50
print(min_days_to_produce_heap(machines, target))  # minimal days
