def build_heap(data):
    def sift_down(data, i, swaps):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < len(data) and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < len(data) and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(data, min_index, swaps)

    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)

    return swaps


def main():
    input_type = input("I or F: ").strip().upper()

    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == 'F':
        file_name = input("File: ").strip()
        file_path = f'tests/{file_name}'
        
        with open(file_path, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        print("Invalid input type.")
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
