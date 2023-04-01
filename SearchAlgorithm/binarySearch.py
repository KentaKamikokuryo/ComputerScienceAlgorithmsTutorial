# name space
class BinarySearch:

    @staticmethod
    def iterative_implementation(l, value):

        start = 0
        end = len(l) - 1

        # searched space is l[start, ..., end]
        while start <= end:

            mid = (start + end) // 2

            # "value" is found in the "l"
            if l[mid] == value:

                return True, mid

            elif l[mid] < value:

                start = mid + 1

            else:

                end = mid - 1

        # "value" is not found in the "l"
        return False, -1

    @staticmethod
    def recursive_implementation(l, start, end, value):

        if start > end:

            return False, -1

        mid = (start + end) // 2

        if value == l[mid]:
            return True, mid

        elif value < l[mid]:
            return BinarySearch.recursive_implementation(l, start, mid - 1, value)

        else:
            return BinarySearch.recursive_implementation(l, mid + 1, end, value)


if __name__ == "__main__":

    nums = [2, 5, 6, 8, 9, 10]
    target = 5

    boolean, index = BinarySearch.iterative_implementation(nums, target)

    if boolean:
        print("Element is found at index: {}".format(index))
    else:
        print("Element is not found.")

