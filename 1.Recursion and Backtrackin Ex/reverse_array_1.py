def reverse(idx, n):
    if idx == len(elements) // 2:
        return
    swap_idx = len(elements) -1 - idx
    elements[idx],elements[swap_idx] = elements[swap_idx],elements[idx]
    reverse(idx+1,elements)


elements = input().split()
reverse(0, elements)
print(' '.join(elements))

# iterative

for left_idx in range(len(elements)//2):
    right_idx = len(elements) - 1 - left_idx
    elements[left_idx],elements[right_idx]=elements[right_idx],elements[left_idx]

print(' '.join(elements))