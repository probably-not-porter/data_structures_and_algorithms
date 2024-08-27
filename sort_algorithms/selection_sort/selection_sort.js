// Selection Sort
// Javascript
// Porter L

function selectionSort(Arr){
    console.log('selection sort');
    for (x = 0; x < Arr.length; x++){
        var min_index = x;
        for (y = x+1; y < Arr.length; y++){
            if (Arr[min_index] > Arr[y]){
                min_index = y;
            }
        }
        var b = Arr[x];
        Arr[x] = Arr[min_index];
        Arr[min_index] = b;
    }
    return Arr
}