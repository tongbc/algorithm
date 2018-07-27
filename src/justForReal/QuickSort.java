package justForReal;

public class QuickSort {
    public static void quickSort(int[] arr,int low,int high){
    	int temp,i,j,t;
    	if(low>high)return;
    	temp = arr[low];
    	i=low;
    	j=high;
    	while(i<j){
    		while(temp<=arr[j]&&i<j){
    			j--;
    		}
    		while(temp>=arr[i]&&i<j){
    			i++;
    		}
    		if(i<j){
    			t=arr[i];
    			arr[i] = arr[j];
    			arr[j]=t;
    		}
    	}
    	arr[low] = arr[i];
    	arr[i] = temp;
    	//�ݹ�����������
        quickSort(arr, low, j-1);
        //�ݹ�����Ұ�����
        quickSort(arr, j+1, high);
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
