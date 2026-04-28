def print_rods(rods):
    print("\nCurrent State:")
    for name in rods:
        print(f"{name}: {rods[name]}")
    print("-" * 30)


def tower_of_hanoi(n, source, auxiliary, destination, rods):
    if n == 0:
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary, rods)

    disk = rods[source].pop()
    rods[destination].append(disk)

    print(f"[Move] Disk {disk}: {source} ➝ {destination}")
    print_rods(rods)

    tower_of_hanoi(n - 1, auxiliary, source, destination, rods)


print("Welcome 👩‍💻 Let's visualize Tower of Hanoi!\n")

n = int(input("Enter number of disks: "))

rods = {
    "Start": list(range(n, 0, -1)),
    "Helper": [],
    "Goal": []
}

print_rods(rods)

tower_of_hanoi(n, "Start", "Helper", "Goal", rods)

print("\nCompleted!")