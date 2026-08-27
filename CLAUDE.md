# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **mirror**, not a project. It is populated automatically by the NeetCode.io GitHub Sync
integration: solutions are written in the browser editor on neetcode.io, and every submission is
pushed here as a new file. There is no build system, no dependency manifest, no test suite, no
linter config, and no CI.

The practical consequence is that editing a file here does not change anything on NeetCode. The
authoritative copy of a solution lives upstream; this repo is the record of what was submitted.
Treat existing files as an append-only history of attempts rather than source to be maintained.

## Layout and file naming

```
<topic folder>/<problem-slug>/submission-N.py
```

`Data Structures & Algorithms/` is the only topic folder with content — 43 Python files across 38
problem folders. `Data Structures & Algorithms in Rust/` exists at the repo root but is empty and
untracked (git does not store empty directories).

**`N` is NeetCode's index into the submission history for that problem, not a local counter.** Gaps
are normal and expected: `valid-word-abbreviation/` contains only `submission-9.py`, and
`minimum-remove-to-make-valid-parentheses/` contains `submission-4`, `-5`, and `-6`. Never renumber,
backfill, or consolidate these. A new attempt at a problem becomes a new numbered file; it does not
overwrite an older one. When several submissions exist for one problem, the highest number is the
most recent attempt.

## The two kinds of file

**Problem solutions** define `class Solution` with a single method whose name and signature are
fixed by the NeetCode judge (`twoSum`, `numIslands`, `rightSideView`). Recursive problems add a
helper method on the same class rather than a nested function — see `mergeSort/submission-0.py`,
which splits into `mergeSortHelper` and `merge`. Many files retain the commented-out type definition
block that NeetCode prefills in the editor (`# Definition for a binary tree node.` followed by a
commented `class TreeNode`, or the equivalent `Pair` block for the sorting problems). That block is
part of the submitted text; leave it in place.

**Data structure implementations** live in the camelCase folders — `dynamicArray`, `hashTable`,
`heap`, `queue`, `singlyLinkedList`, `binarySearchTree`, `graph`, `unionFind`. These define a named
class (`DynamicArray`, `MinHeap`, `Deque`, `UnionFind`) whose full method set is a contract set by
the NeetCode problem, so method names cannot be changed even when they are non-Pythonic
(`getSize`, `isSameComponent`, `pushback`). Where a helper node type is needed, it is defined as a
plain `class Node` above the main class in the same file, since the judge supplies only one file.

## Files do not run standalone

Most files use `List`, `Optional`, `deque`, `defaultdict`, `Counter`, and `heapq` **without importing
them** — the NeetCode judge injects those names into the execution environment. Running
`python "Data Structures & Algorithms/two-integer-sum/submission-0.py"` fails with
`NameError: name 'List' is not defined`. Only three files carry explicit imports
(`binary-tree-right-side-view/submission-1.py`, `binary-tree-vertical-order-traversal/submission-0.py`,
`count-servers-that-communicate/submission-1.py`), and `kth-largest-element-in-an-array/submission-1.py`
imports `heapq` inside the method body.

Syntax checking works and is the only repo-wide check available:

```bash
# Check one file
python -m py_compile "Data Structures & Algorithms/two-integer-sum/submission-0.py"

# Check everything
find "Data Structures & Algorithms" -name "*.py" -exec python -m py_compile {} +
```

To actually exercise a solution, write a throwaway driver outside the repo that supplies the missing
imports and any judge-provided type (`TreeNode`, `Pair`), then imports or execs the submission file.
Do not add imports, drivers, `if __name__ == "__main__"` blocks, or test files into the submission
files themselves — that would diverge them from what was submitted upstream.

## Commit conventions

The integration writes `Add: <problem-slug> - submission-N` for individual syncs and
`Bulk sync: <count> submissions` for batch pushes. Match the `Add:` form when committing a solution
by hand so the history stays uniform.

## Style

The code is deliberately unpolished: first-person reasoning comments left inline ("since it needs a
pivot, I should create a helper as well"), occasional leftover `print` debugging, and snake_case
locals mixed with the camelCase the judge imposes on method names. Each file is a point-in-time
record of one attempt. Do not normalize formatting, strip comments, or refactor across files. If a
solution needs improving, that belongs in a new submission, not an edit to an old one.
