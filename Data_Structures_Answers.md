Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

  O(n), in the worst case the last available space in the buffer is empty and the function loops through n indices to put it in there.

2. What is the space complexity of your ring buffer's `append` function?

  The append function doesn't allocate any additional memory, only uses what's already been allocated, so O(1). I s'pose the space used is O(n), but since it's not part of the function I don't think that's the space complexity of the append function itself.

3. What is the runtime complexity of your ring buffer's `get` method?

  O(n) because it steps through the array to only pull out the values that aren't None.

4. What is the space complexity of your ring buffer's `get` method?

  O(n), it allocates some space for one new array which can't be longer than n.

5. What is the runtime complexity of the provided code in `names.py`?

  O(n^2), nested for loops. O(n * m), technically? :)

6. What is the space complexity of the provided code in `names.py`?

  O(n), constant space, it's not quadratic and it's not fixed no matter the input. You're allocating space for a few arrays and then just using those for operations, and that's it.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n), the python dictionary uses a hash table behind the scenes, I believe, so lookups are O(1). It will take O(n) to fill the dictionary and O(m) to lookup the names in the second array.

8. What is the space complexity of your optimized code in `names.py`?

  O(n) again, we've just added a one-time allocation of a dictionary that's n long, no problem.