from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0

    while bridge:
        answer += 1
        passed_truck = bridge.popleft()
        bridge_weight -= passed_truck

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                bridge_weight += new_truck
            else:
                bridge.append(0)

    return answer