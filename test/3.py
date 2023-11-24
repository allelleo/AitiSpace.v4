volume: list[int] = [

]
for i in range(10):
    volume.append(int(input()))

mean: int = sum(volume) / len(volume)
steps = 0


def spill(free: int):
    for i in range(len(volume)):
        if volume[i] > mean:
            add = mean - volume[i]
            if not add < free:
                free -= add
                volume[i] = volume[i] + add
            else:
                volume[i] = volume[i] + free
                break


for i in range(len(volume)):
    if volume[i] > mean:
        steps += 1
        free: int = volume[i] - mean
        spill(free)
print(steps)