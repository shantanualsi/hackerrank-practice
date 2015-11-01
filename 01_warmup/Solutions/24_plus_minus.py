if __name__ == '__main__':
    num_zeros = 0
    num_negatives = 0
    num_positives = 0
    array_length = float(raw_input())
    array_input = map(int, raw_input().split(" "))
    for entry in array_input:
        if entry is 0:
            num_zeros += 1
        elif entry < 1:
            num_negatives += 1
        else:
            num_positives += 1
    print "%.3f\n%.3f\n%.3f" % (num_positives/array_length,
            num_negatives/array_length, num_zeros/array_length)
