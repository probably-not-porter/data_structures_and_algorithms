// Insertion Sort
// Javascript
// Porter L

function insertionSort(Arr){
    console.log('insertion sort');
    for (var x = 0; x < Arr.length; x++){
        var key = Arr[x];
        var y = x - 1;
        while (y >= 0 && key < Arr[y]){
            Arr[y + 1] = Arr[y];
            y = y - 1;
        }
        Arr[y + 1] = key;
    }
    return Arr
}