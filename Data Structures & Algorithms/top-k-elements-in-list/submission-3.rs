impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut count = HashMap::new();
        let mut freq = vec![vec![]; nums.len() + 1];

        for &num in &nums {
            *count.entry(num).or_insert(0usize) += 1;
        }
        for (&num, &cnt) in &count {
            freq[cnt].push(num);
        }

        let mut res = Vec::new();
        for i in (1..freq.len()).rev() {
            for &num in &freq[i] {
                res.push(num);
                if res.len() == k {
                    return res;
                }
            }
        }
        res
    }
}