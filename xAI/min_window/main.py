import math

def min_window_frequency_match(s, t):
    target = {}
    for num in t:
        target[num] = target.get(num, 0) + 1

    min_len = math.inf
    result = []

    print("Target frequencies:", target)

    for i in range(len(s)):
        aux = []
        window_count = {}
        found = False

        for j in range(i, len(s)):
            aux.append(s[j])
            window_count[s[j]] = window_count.get(s[j], 0) + 1

            # Check if window matches target frequencies
            is_valid = True
            for key in target:
                if window_count.get(key, 0) < target[key]:
                    is_valid = False
                    break

            if is_valid:
                if len(aux) < min_len:
                    result = aux[:]
                    min_len = len(aux)
                found = True
                break  # No need to expand this window further

        print(f"Window [{i}]: {aux} → Match? {'Yes' if found else 'No'}")

    return result

print(min_window_frequency_match([1, 2, 2, 3, 1, 2, 4], [1,4]))