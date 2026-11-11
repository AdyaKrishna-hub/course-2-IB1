import pytest, searching_sort

@pytest.mark.parametrize('list_in, expected', 
    [([5, 6, 1]),] # typical
    # [1000, 999,..., 1]
    [(list(range(1000, 0, -1)), list(range(1, 1001)))],
    ([], []), # empty
    ([0]), # single element
    (['hi','bye', 'hello']), # already sorted
    ([1, 2, 1, 2], [1, 1, 2, 2]), # duplicates
    [0, -10, 100])

def test_searching_sort(list_in, expected): # test function
    searching_sort.seq_search(list_in) # note: sorts in-place
    assert list_in == expected # match against expected