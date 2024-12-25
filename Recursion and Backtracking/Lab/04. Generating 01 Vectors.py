rows = int(input())
vector = [0] * rows

def print_vector(idx, vector):

    if idx == len(vector):
        print("".join(list(map(str, vector))))

        return 1

    for i in range(2):
        vector[idx] = i

        print_vector(idx + 1, vector)



print_vector(0, vector)
