package justForReal;

public class ReverseNode {
	public Node reverse(Node node) {
		Node pre = null;
//		Node now = node;
		while(node != null){
			Node now = node;
			node = now.next;
			now.next = pre;
			pre = now;
		}
		node = pre;
		return node;
	}
	
	public Node DgReverse(Node node){
		if(node==null||node.next==null){
			return node;
		}
		Node newHead = DgReverse(node);
		node.next.next = node;
		node.next = null;
		return newHead;
	}
}
