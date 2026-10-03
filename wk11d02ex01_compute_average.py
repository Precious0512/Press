"""
Filename: wk11d02ex01_compute_average.py
Description: Python version of the Flowgorithm computeAverage(numbers) flowchart.
             The function intentionally keeps the flowchart's behavior,
             including its known flaw: it stops at the first zero.
Author: Precious Arellano
Date: 2026

GitHub repository: <paste your PROGCON Week 11 repository URL here>

TEST SUMMARY (hand-traced; confirm against your Flowgorithm runs)
-----------------------------------------------------------------
Array              Flowchart output   True average   Verdict
[22, 9, 0, 17]     15.5               12.0           INCORRECT
[22, 0, 49, 8]     22.0               19.75          INCORRECT
[35, 13, 22, 0]    23.333...          17.5           INCORRECT
[10, 5, -4, 27]    9.5                9.5            CORRECT

REFLECTION
----------
- Zeros: the first zero hits the ELSE branch, so the zero is never added
  and the function stops reading the array.
- Early return: the function returns total / count at that moment. Every
  element after the zero is ignored, so the average covers only part of
  the list.
- Updates: total and count are updated together, but only when num != 0.
  The result is wrong whenever a zero appears and there are non-zero values
  after it (arrays 1 and 2) or when the zero itself should have counted
  in the denominator (array 3).
- Array 4 has no zero, so the loop finishes and the final return is correct.
"""


def computeAverage(numbers):
    """
    Compute the average of the first four values in a list.

    Parameters:
        numbers (list): A list of numbers (at least 4 items).

    Returns:
        float: total / count at the first zero, or after the loop ends.

    Known limitations:
        - Stops at the first zero (early return), so later values are ignored.
        - The zero itself is never counted, which gives the wrong average.
        - Raises ZeroDivisionError if the first value is 0 (count is still 0).
        - The loop is hardcoded to 4 items, matching the flowchart (0 to 3).
    """
    total = 0
    count = 0

    # Loop over indices 0 to 3, matching the flowchart's "i = 0 to 3"
    for i in range(4):
        num = numbers[i]

        # Decision: is the current value a zero?
        if num != 0:
            # Non-zero value: update total and count together
            total = total + num
            count = count + 1
        else:
            # Early return: a zero ends the function immediately.
            # This is the flaw: remaining values are skipped.
            return total / count

    # Final return: reached only when no zero was found
    return total / count


if __name__ == "__main__":
    tests = [
        ([22, 9, 0, 17], 12.0),
        ([22, 0, 49, 8], 19.75),
        ([35, 13, 22, 0], 17.5),
        ([10, 5, -4, 27], 9.5),
    ]
    for data, true_avg in tests:
        result = computeAverage(data)
        verdict = "CORRECT" if abs(result - true_avg) < 1e-9 else "INCORRECT"
        print(f"{data}: output={result}, true={true_avg} -> {verdict}")
