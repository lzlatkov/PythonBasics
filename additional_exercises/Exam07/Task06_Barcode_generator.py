low_limit = int(input())
up_limit = int(input())

low_limit_4 = low_limit % 10
up_limit_4 = up_limit % 10

low_limit = low_limit // 10
up_limit = up_limit // 10

low_limit_3 = low_limit % 10
up_limit_3 = up_limit % 10

low_limit = low_limit // 10
up_limit = up_limit // 10

low_limit_2 = low_limit % 10
up_limit_2 = up_limit % 10

low_limit_1 = low_limit // 10
up_limit_1 = up_limit // 10

for i in range(low_limit_1, up_limit_1 + 1):
    for j in range(low_limit_2, up_limit_2 + 1):
        for k in range(low_limit_3, up_limit_3 + 1):
            for l in range(low_limit_4, up_limit_4 + 1):
                if i % 2 > 0 and j % 2 > 0 and k % 2 > 0 and l % 2 > 0:
                    print(f"{i}{j}{k}{l}", end=" ")
