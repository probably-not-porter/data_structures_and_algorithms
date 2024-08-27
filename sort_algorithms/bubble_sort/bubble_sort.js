// Bubble Sort
// Javascript
// Porter L

function bubbleSort(Arr){
    console.log('bubble sort');
    var length = Arr.length;
    for (x = 0; x < length-1; x++){
        for (y = 0; y < length-x-1; y++){
            if (Arr[y] > Arr[y+1]){
                var b = Arr[y];
                Arr[y] = Arr[y+1];
                Arr[y+1] = b;
            }
        }
    }
    return Arr
}