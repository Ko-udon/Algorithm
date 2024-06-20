# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = deque([0] * bridge_length)
#     bridge_weight = 0

#     while bridge:
#         answer += 1
#         passed_truck = bridge.popleft()
#         bridge_weight -= passed_truck

#         if truck_weights:
#             if bridge_weight + truck_weights[0] <= weight:
#                 new_truck = truck_weights.pop(0)
#                 bridge.append(new_truck)
#                 bridge_weight += new_truck
#             else:
#                 bridge.append(0)

#     return answer


from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
