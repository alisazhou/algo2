import heapq


def get_diff(jobs):
    # want to arrange in decreasing (w - l)
    diff = []
    for w, l in jobs:
        heapq.heappush(diff, (l - w, -w))    # need to extractmax for w - l, then for w
    return diff


def get_ratio(jobs):
    ratios = []
    for w, l in jobs:
        heapq.heappush(ratios, (l/w, -w))
    return ratios


def weighted_sum_diff(jobs_diff):
    fin_time = 0
    # weighted completion time = w * finish
    weighted_total = 0
    while jobs_diff:
        job = heapq.heappop(jobs_diff)
        l_less_w, neg_w = job
        l = l_less_w - neg_w
        w = - neg_w
        fin_time += l
        weighted_total += fin_time * w
    return weighted_total


def weighted_sum_ratio(jobs_ratio):
    fin_time = 0
    weighted_total = 0
    while jobs_ratio:
        job = heapq.heappop(jobs_ratio)
        l_over_w, neg_w = job
        l = -l_over_w * neg_w
        w = -neg_w
        fin_time += l
        weighted_total += fin_time * w
    return int(weighted_total)


def overview(txt):
    with open(txt) as f:
        f.readline()
        t = f.readlines()
    jobs = []
    for line in t:
        jobs.append(tuple(int(i) for i in line.strip().split()))
    diff = get_diff(jobs)
    weighted_diff = weighted_sum_diff(diff)
    ratio = get_ratio(jobs)
    weighted_ratio = weighted_sum_ratio(ratio)
    return weighted_diff, weighted_ratio


if __name__ == "__main__":
    import sys
    txt = sys.argv[1]
    answer = overview(txt)
    print(answer)


# ANSWERS FOR TEST CASES:
# t11 - 11336 for diff, 10548 for ratio
# t112 - 23 for diff, 22 for ratio
# t113 - 145924 for diff, 138232 for ratio
