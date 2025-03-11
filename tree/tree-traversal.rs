use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

// Definition of a binary tree node
#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    // Helper function to create a new node
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        }))
    }
}

// ========================
// 1. PRE-ORDER TRAVERSAL
// ========================

// Recursive pre-order traversal: Root -> Left -> Right
fn preorder_recursive(root: &Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
    if let Some(node) = root {
        let node = node.borrow();
        // Visit root first
        result.push(node.val);
        // Then traverse left subtree
        preorder_recursive(&node.left, result);
        // Finally traverse right subtree
        preorder_recursive(&node.right, result);
    }
}

// Iterative pre-order traversal using a stack
fn preorder_iterative(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut stack = Vec::new();

    // Return empty vector if tree is empty
    if root.is_none() {
        return result;
    }

    // Push the root node onto the stack
    if let Some(node) = root {
        stack.push(Rc::clone(node));
    }

    // Process nodes until stack is empty
    while !stack.is_empty() {
        // Pop the top node from the stack
        if let Some(node) = stack.pop() {
            let node_ref = node.borrow();
            // Visit the node
            result.push(node_ref.val);

            // Push right child first (so it's processed after the left child)
            if let Some(right) = &node_ref.right {
                stack.push(Rc::clone(right));
            }

            // Push left child (which will be processed before the right child)
            if let Some(left) = &node_ref.left {
                stack.push(Rc::clone(left));
            }
        }
    }

    result
}

// ========================
// 2. IN-ORDER TRAVERSAL
// ========================

// Recursive in-order traversal: Left -> Root -> Right
fn inorder_recursive(root: &Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
    if let Some(node) = root {
        let node = node.borrow();
        // First traverse left subtree
        inorder_recursive(&node.left, result);
        // Then visit root
        result.push(node.val);
        // Finally traverse right subtree
        inorder_recursive(&node.right, result);
    }
}

// Iterative in-order traversal using a stack
fn inorder_iterative(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut stack = Vec::new();
    let mut current = root.clone();

    while current.is_some() || !stack.is_empty() {
        // Reach the leftmost node of the current node
        while let Some(node) = current {
            stack.push(Rc::clone(&node));
            current = node.borrow().left.clone();
        }

        // Current is now None, backtrack to the nearest unprocessed node
        if let Some(node) = stack.pop() {
            // Visit the node
            result.push(node.borrow().val);
            // Visit right subtree
            current = node.borrow().right.clone();
        }
    }

    result
}

// ========================
// 3. POST-ORDER TRAVERSAL
// ========================

// Recursive post-order traversal: Left -> Right -> Root
fn postorder_recursive(root: &Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
    if let Some(node) = root {
        let node = node.borrow();
        // First traverse left subtree
        postorder_recursive(&node.left, result);
        // Then traverse right subtree
        postorder_recursive(&node.right, result);
        // Finally visit root
        result.push(node.val);
    }
}

// Iterative post-order traversal using two stacks
fn postorder_iterative(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut stack1 = Vec::new();
    let mut stack2 = Vec::new();

    // Return empty vector if tree is empty
    if root.is_none() {
        return result;
    }

    // Push the root node onto the first stack
    if let Some(node) = root {
        stack1.push(Rc::clone(node));
    }

    // Process nodes in stack1 and push to stack2
    while !stack1.is_empty() {
        // Pop the top node from stack1
        if let Some(node) = stack1.pop() {
            // Push this node to stack2
            stack2.push(Rc::clone(&node));
            let node_ref = node.borrow();

            // Push left child to stack1 (will be processed before right child)
            if let Some(left) = &node_ref.left {
                stack1.push(Rc::clone(left));
            }

            // Push right child to stack1
            if let Some(right) = &node_ref.right {
                stack1.push(Rc::clone(right));
            }
        }
    }

    // Pop all items from stack2 to get post-order traversal
    while let Some(node) = stack2.pop() {
        result.push(node.borrow().val);
    }

    result
}

// Alternative iterative post-order traversal using a single stack
fn postorder_iterative_single_stack(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut stack = Vec::new();
    let mut current = root.clone();
    let mut last_visited: Option<Rc<RefCell<TreeNode>>> = None;

    while current.is_some() || !stack.is_empty() {
        // Reach the leftmost node of the current node
        while let Some(node) = current {
            stack.push(Rc::clone(&node));
            current = node.borrow().left.clone();
        }

        // Get the top node without removing it yet
        if let Some(top) = stack.last().cloned() {
            // Use cloned() to avoid borrow issues
            let node_ref = top.borrow();

            // If right child exists and has not been visited yet
            if node_ref.right.is_some()
                && last_visited.as_ref().map_or(true, |last| {
                    !Rc::ptr_eq(&node_ref.right.as_ref().unwrap(), last)
                })
            {
                // Go to right subtree
                current = node_ref.right.clone();
            } else {
                // Visit the node
                result.push(node_ref.val);
                last_visited = Some(Rc::clone(&top));
                drop(node_ref); // Explicitly drop the borrow before pop
                stack.pop();
            }
        }
    }

    result
}

// ========================
// 4. LEVEL-ORDER TRAVERSAL
// ========================

// Recursive level-order traversal (BFS)
fn levelorder_recursive(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    let mut result = Vec::new();

    fn height(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                let left_height = height(&node.left);
                let right_height = height(&node.right);
                1 + std::cmp::max(left_height, right_height)
            }
        }
    }

    fn get_level(root: &Option<Rc<RefCell<TreeNode>>>, level: i32, curr_level: &mut Vec<i32>) {
        if let Some(node) = root {
            let node = node.borrow();
            if level == 1 {
                curr_level.push(node.val);
            } else if level > 1 {
                get_level(&node.left, level - 1, curr_level);
                get_level(&node.right, level - 1, curr_level);
            }
        }
    }

    let h = height(root);
    for i in 1..=h {
        let mut curr_level = Vec::new();
        get_level(root, i, &mut curr_level);
        result.push(curr_level);
    }

    result
}

// Iterative level-order traversal using a queue
fn levelorder_iterative(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    let mut result: Vec<Vec<i32>> = Vec::new();

    // Return empty vector if tree is empty
    if root.is_none() {
        return result;
    }

    let mut queue = VecDeque::new();
    if let Some(node) = root {
        queue.push_back(Rc::clone(node));
    }

    while !queue.is_empty() {
        let level_size = queue.len();
        let mut current_level = Vec::new();

        // Process all nodes at current level
        for _ in 0..level_size {
            if let Some(node) = queue.pop_front() {
                let node_ref = node.borrow();

                // Visit the node
                current_level.push(node_ref.val);

                // Add left child to queue if exists
                if let Some(left) = &node_ref.left {
                    queue.push_back(Rc::clone(left));
                }

                // Add right child to queue if exists
                if let Some(right) = &node_ref.right {
                    queue.push_back(Rc::clone(right));
                }
            }
        }

        result.push(current_level);
    }

    result
}

// Function to demonstrate all traversals
fn demonstrate_traversals() {
    // Create a sample binary tree:
    //      1
    //     / \
    //    2   3
    //   / \   \
    //  4   5   6
    let root = TreeNode::new(1);
    let left = TreeNode::new(2);
    let right = TreeNode::new(3);
    let left_left = TreeNode::new(4);
    let left_right = TreeNode::new(5);
    let right_right = TreeNode::new(6);

    // Connect nodes
    root.borrow_mut().left = Some(Rc::clone(&left));
    root.borrow_mut().right = Some(Rc::clone(&right));
    left.borrow_mut().left = Some(Rc::clone(&left_left));
    left.borrow_mut().right = Some(Rc::clone(&left_right));
    right.borrow_mut().right = Some(Rc::clone(&right_right));

    // Test all traversals
    let root_option = Some(Rc::clone(&root));

    // 1. Pre-order traversal
    let mut preorder_result = Vec::new();
    preorder_recursive(&root_option, &mut preorder_result);
    println!("Pre-order (recursive): {:?}", preorder_result);
    println!(
        "Pre-order (iterative): {:?}",
        preorder_iterative(&root_option)
    );

    // 2. In-order traversal
    let mut inorder_result = Vec::new();
    inorder_recursive(&root_option, &mut inorder_result);
    println!("In-order (recursive): {:?}", inorder_result);
    println!(
        "In-order (iterative): {:?}",
        inorder_iterative(&root_option)
    );

    // 3. Post-order traversal
    let mut postorder_result = Vec::new();
    postorder_recursive(&root_option, &mut postorder_result);
    println!("Post-order (recursive): {:?}", postorder_result);
    println!(
        "Post-order (iterative, two stacks): {:?}",
        postorder_iterative(&root_option)
    );
    println!(
        "Post-order (iterative, single stack): {:?}",
        postorder_iterative_single_stack(&root_option)
    );

    // 4. Level-order traversal
    println!(
        "Level-order (recursive): {:?}",
        levelorder_recursive(&root_option)
    );
    println!(
        "Level-order (iterative): {:?}",
        levelorder_iterative(&root_option)
    );
}

fn main() {
    demonstrate_traversals();
}
