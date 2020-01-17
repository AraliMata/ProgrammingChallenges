class Solution {
public:
    int fib(int N) {
        int prev = 0;
        int curr = 0;
        int last = 1;

        for (int i = 0; i < N; i++){

            prev = curr;
            curr = last;
            last = prev + curr;

        }

        return curr;
    }
};
