def hanoi(n, start, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {start} to {target}")
    else:
        # Move n-1 disks to auxiliary rod
        hanoi(n-1, start, target, auxiliary)
        # Move largest disk to target rod
        print(f"Move disk {n} from {start} to {target}")
        # Move n-1 disks from auxiliary rod to target rod
        hanoi(n-1, auxiliary, start, target)


hanoi(3, 'A', 'B', 'C')
