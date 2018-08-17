package justForReal;

import org.omg.Messaging.SyncScopeHelper;

public class MinimumAbsoluteDifferenceInBST {
	class Solution {
		public int getMinimumDifference(TreeNode root) {
			int[] res = new int[] { Integer.MAX_VALUE, -1 };
			helper(root, res);
			return res[0];
		}

		private void helper(TreeNode node, int[] res) {
			if (node == null)
				return;
			helper(node.left, res);
			if (res[1] != -1) {
				res[0] = Math.min(res[0], node.val - res[1]);
			}
			res[1] = node.val;
			helper(node.right, res);
		}
	}
	
	public static void main(String[] args) {
		int[] res = new int[] { Integer.MAX_VALUE, -1 };
		System.out.println(5);
	}
	
}
