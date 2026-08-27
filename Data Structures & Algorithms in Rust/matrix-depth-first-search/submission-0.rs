// Evacuation Route Count
// (NeetCode calls this "Matrix Depth-First Search", Medium)
//
// A ward floor plan is given as a binary matrix. 0 is a corridor square a gurney
// can pass through, 1 is blocked — fire, smoke, a collapsed ceiling, a sealed
// contamination door. A code has been called. The patient is in the top-left
// square and the ambulance bay is the bottom-right square.
//
// Return the number of distinct routes from the patient to the ambulance bay
// that pass only through clear squares. A gurney moves one square at a time,
// vertically or horizontally, and nobody wheels it back through a square they
// have already come through, so a single route may not visit a square twice.
//
// The count is the redundancy margin. Twelve routes means one more blocked
// corridor is an inconvenience. One route means that corridor is a fatal
// dependency. Zero means the patient cannot be moved at all and the plan
// becomes shelter in place.
//
// Example:
//   floor_plan = [[0, 0, 0, 0],
//                 [1, 1, 0, 0],
//                 [0, 0, 0, 1],
//                 [0, 1, 0, 0]]
//   answer = 2
//
// This is a preparedness question, not something anyone runs during the code.
// In the moment you want breadth-first search for the single fastest way out.
// Enumerating every route is exponential, and it is what a safety audit does in
// advance when the question is whether the floor plan is resilient at all.
//
// Rust note: the Python version of this nests a `dfs` closure that mutates a
// `visited` grid from the enclosing scope. That does not work here — a closure
// cannot borrow `visited` mutably and also call itself. Use a free function (or
// an associated fn) that takes `visited: &mut Vec<Vec<bool>>` as a parameter.

pub struct Solution;

impl Solution {
    #[allow(unused_variables)] // remove once implemented
    pub fn count_paths(&self, floor_plan: Vec<Vec<i32>>) -> i32 {
        todo!("backtracking DFS: step onto a square, recurse on the 4 neighbours, step back off")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn floor_plan(rows: &[&[i32]]) -> Vec<Vec<i32>> {
        rows.iter().map(|row| row.to_vec()).collect()
    }

    #[test]
    fn ward_with_two_routes() {
        let plan = floor_plan(&[
            &[0, 0, 0, 0],
            &[1, 1, 0, 0],
            &[0, 0, 0, 1],
            &[0, 1, 0, 0],
        ]);
        assert_eq!(Solution.count_paths(plan), 2);
    }

    #[test]
    fn patient_is_already_at_the_bay() {
        // start and end are the same square, which counts as one route
        assert_eq!(Solution.count_paths(floor_plan(&[&[0]])), 1);
    }

    #[test]
    fn patients_room_is_cut_off() {
        let plan = floor_plan(&[&[1, 0], &[0, 0]]);
        assert_eq!(Solution.count_paths(plan), 0);
    }

    #[test]
    fn ambulance_bay_is_cut_off() {
        let plan = floor_plan(&[&[0, 0], &[0, 1]]);
        assert_eq!(Solution.count_paths(plan), 0);
    }

    #[test]
    fn tiny_open_ward() {
        // across then down, or down then across
        let plan = floor_plan(&[&[0, 0], &[0, 0]]);
        assert_eq!(Solution.count_paths(plan), 2);
    }

    #[test]
    fn open_ward_with_no_blockages() {
        // 12 self-avoiding routes across a clear 3x3 floor; this catches a
        // solution that only ever moves right and down, which would miss the
        // routes that double back around an obstacle
        let plan = floor_plan(&[&[0, 0, 0], &[0, 0, 0], &[0, 0, 0]]);
        assert_eq!(Solution.count_paths(plan), 12);
    }

    #[test]
    fn fire_seals_the_middle_corridor() {
        // the blocked row splits the floor in two, stranding the patient
        let plan = floor_plan(&[&[0, 0, 0], &[1, 1, 1], &[0, 0, 0]]);
        assert_eq!(Solution.count_paths(plan), 0);
    }
}
