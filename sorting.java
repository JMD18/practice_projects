package practice_projects;
import java.util.Arrays;
import java.util.Random;

class Sorting {
    public static void main(String[] args) {

        int[] arr1 = {5,8,3,7,9,2,4,1,6};
        insertionSort(arr1);
        System.out.println("Insertion : " + Arrays.toString(arr1));


        int[] arr2 = {8,3,5,9,7,2,6,1,4};
        quickSort(arr2,0,arr2.length-1);
        System.out.println("QuickSort : " + Arrays.toString(arr2));


        int[] arr3 = {2,7,4,6,9,1,3,8,5};
        mergeSort(arr3,0,arr3.length-1);
        System.out.println("MergeSort : " + Arrays.toString(arr3));

    }


    public static void insertionSort(int[] array) {
        int len = array.length;

        for(int i = 1; i < len; i++) {
            int key = array[i];
            int j = i-1;

            while(j>=0 && array[j] > key) {
                array[j+1] = array[j];
                j-=1;
            }
            array[j+1] = key;
        }

    }


    public static void quickSort(int[] array, int low, int high) {

        // int p_index = randPivot(array);
        // int p = array[p_index];

        if(low<high) { 
			int q = partition(array,low,high);
			quickSort(array,low,q-1);
			quickSort(array,q+1,high);
		}

    }

    public static int partition(int[] arr, int low, int high) {
        int x = arr[high];
		int i = low-1;

		for(int j=low; j<=(high-1);j++) {

			if(arr[j]<=x) {
				i++;
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
        
		int temp = arr[i+1];
		arr[i+1] = arr[high];
		arr[high] = temp;

		return (i+1);
    }


    public static void mergeSort(int[] arr, int low, int high) {

        if(low<high) {
            int mid = (int) Math.floor((low + high)/2);
            mergeSort(arr, low, mid);
            mergeSort(arr, mid+1, high);
            mergeArray(arr,low,mid,high);
        }

    }


    private static void mergeArray(int[] arr, int beg, int mid, int end) {

        int left_size = mid - beg + 1;
        int right_size = end - mid;
        int LeftArray[] = new int [left_size];
        int RightArray[] = new int[right_size];
        
        for(int i=0; i<left_size; ++i) {
            LeftArray[i] = arr[beg + i];
        }

        for(int j=0; j<right_size; ++j){
            RightArray[j] = arr[mid + 1+ j];
        }

        int i = 0, j = 0;
        int k = beg;
        while(i<left_size && j<right_size) {
           if(LeftArray[i] <= RightArray[j]){
                arr[k] = LeftArray[i];  
                i++;
            } else {
                arr[k] = RightArray[j];
                j++;
            }
            
            k++;
        }
        
        while(i<left_size){
            arr[k] = LeftArray[i];
            i++;
            k++;
        }

        while(j<right_size) {
            arr[k] = RightArray[j];
            j++;
            k++;
        }
    }

    


    public int randPivot(int[] array) {

        Random rn = new Random();
        int pivot = rn.nextInt(array.length-1);

        return pivot;
    }

}