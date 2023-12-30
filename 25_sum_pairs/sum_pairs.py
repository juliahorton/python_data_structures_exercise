def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    sum_to_goal = []

    for x in range(len(nums)):
        for y in nums[x:]:
            if nums[x] + y == goal:
                sum_to_goal.append([nums[x],y])

    if len(sum_to_goal) == 0:
        return ()
    
    min_idx = nums.index(sum_to_goal[0][-1])

    for idx in range(len(sum_to_goal)):
        if nums.index(sum_to_goal[idx][-1]) < min_idx:
            min_idx = nums.index(sum_to_goal[idx][-1])

    for pair in sum_to_goal:
        if nums.index(pair[-1]) == min_idx:
            return tuple(pair)