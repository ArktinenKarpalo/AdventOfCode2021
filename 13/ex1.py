import sys
dots, folds = sys.stdin.read().strip().split("\n\n")
dots = list(map(lambda x: list(map(int, x.split(","))), dots.split("\n")))
folds = folds.split("\n")

for fold in folds:
    along, x = fold.split(" ")[-1].split("=")
    x = int(x)
    if along == "y":
        dots = list(map(lambda x: [x[1], x[0]], dots))

    dots = list(map(lambda y: [y[0] if y[0] < x else x-(y[0]-x), y[1]], dots))
    if along == "y":
        dots = list(map(lambda x: [x[1], x[0]], dots))
    break
print(len(set(map(lambda x: (x[0], x[1]), dots))))
