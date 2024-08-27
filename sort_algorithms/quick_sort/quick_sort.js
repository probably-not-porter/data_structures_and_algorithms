// Quick Sort
// Javascript
// Porter L

function partition(Arr, low, high){
    var x = (low - 1);
    pivot = Arr[high];

    for (var y = low; y < high; y++){
        if (Arr[y] < pivot){
            x = x + 1;
            
            var b = Arr[x];
            Arr[x] = Arr[y];
            Arr[y] = b;
        }
    }
    var b = Arr[x+1];
    Arr[x+1] = Arr[high];
    Arr[high] = b;

    return (x + 1) 
}

function quickSort(Arr,low,high){
    console.log('quick sort');
    if (low < high){ 
        var p = partition(Arr, low, high) 
        Arr = quickSort(Arr, low, p-1) 
        Arr = quickSort(Arr, p+1, high) 
    }
    return Arr
}