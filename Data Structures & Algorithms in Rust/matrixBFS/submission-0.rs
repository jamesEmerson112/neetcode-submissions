// Wavefront Planner
// (NeetCode calls this "Matrix Breadth-First Search", Medium)
//
// A warehouse robot's occupancy grid is given as a binary matrix. 0 is a free
// cell the robot can drive through, 1 is an obstacle the lidar has flagged - a
// pallet, a shelf leg, another robot parked in the aisle. The robot sits at its
// dock in the top-left cell and has to reach the pick station in the
// bottom-right cell.
//
// Return the length of the shortest route from the dock to the pick station
// that passes only through free cells. The robot moves one cell at a time,
// vertically or horizontally. The length of a route is the number of moves,
// so a dock that is already the pick station is 0 moves away. If the station
// cannot be reached at all, return -1.
//
// Example:
//   grid = [[0, 0, 0, 0],
//           [1, 1, 0, 0],
//           [0, 0, 0, 1],
//           [0, 1, 0, 0]]
//   answer = 6
//
// This is the wavefront planner from mobile robotics. The DFS problem next
// door counted every route for a resilience audit done in advance; this one
// finds the single fastest route, which is the thing the robot actually
// drives. Breadth-first search expands the grid in rings of equal distance
// from the dock, so the first ring that touches the pick station is the
// shortest path by construction. Each ring is one frame of the wavefront.
//
// Rust note: the queue is a `VecDeque` from `std::collections`, with
// `push_back` to enqueue and `pop_front` to dequeue. Process one ring at a
// time by reading `queue.len()` before draining that many cells, and count a
// move each time a ring finishes without reaching the station.

use std::collections::{HashSet, VecDeque};

pub struct Solution;

impl Solution {
    #[allow(unused_variables)] // remove once implemented
    pub fn shortest_path(&self, grid: Vec<Vec<i32>>) -> i32 {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn grid(rows: &[&[i32]]) -> Vec<Vec<i32>> {
        rows.iter().map(|row| row.to_vec()).collect()
    }

    #[test]
    fn aisle_with_a_six_move_route() {
        let g = grid(&[
            &[0, 0, 0, 0],
            &[1, 1, 0, 0],
            &[0, 0, 0, 1],
            &[0, 1, 0, 0],
        ]);
        assert_eq!(Solution.shortest_path(g), 6);
    }

    #[test]
    fn dock_is_already_the_pick_station() {
        // start and end are the same cell, which is zero moves
        assert_eq!(Solution.shortest_path(grid(&[&[0]])), 0);
    }

    #[test]
    fn dock_is_blocked() {
        let g = grid(&[&[1, 0], &[0, 0]]);
        assert_eq!(Solution.shortest_path(g), -1);
    }

    #[test]
    fn pick_station_is_blocked() {
        let g = grid(&[&[0, 0], &[0, 1]]);
        assert_eq!(Solution.shortest_path(g), -1);
    }

    #[test]
    fn tiny_open_floor() {
        // across then down, or down then across, both two moves
        let g = grid(&[&[0, 0], &[0, 0]]);
        assert_eq!(Solution.shortest_path(g), 2);
    }

    #[test]
    fn shelving_seals_the_middle_aisle() {
        // the blocked row splits the floor in two
        let g = grid(&[&[0, 0, 0], &[1, 1, 1], &[0, 0, 0]]);
        assert_eq!(Solution.shortest_path(g), -1);
    }

    #[test]
    fn forced_detour_is_longer_than_the_straight_line() {
        // Manhattan distance is 6 but the shelving forces the robot to snake:
        // right along the top, down the right side, back along row 2, down
        // the left side, then right along the bottom. That is 10 moves. A
        // greedy "always head toward the station" approach gets this wrong.
        let g = grid(&[
            &[0, 0, 0],
            &[1, 1, 0],
            &[0, 0, 0],
            &[0, 1, 1],
            &[0, 0, 0],
        ]);
        assert_eq!(Solution.shortest_path(g), 10);
    }
}
