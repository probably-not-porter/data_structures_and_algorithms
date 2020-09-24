// Quick Sort
// Javascript
// Porter L

function partition(Arr, low, high){
    var i = (low - 1);
    pivot = Arr[high];

    for (var j = low; j < high; j++){
        if (Arr[j] < pivot){
            i = i + 1;
            
            var b = Arr[i];
            Arr[i] = Arr[j];
            Arr[j] = b;
        }
    }
    var b = Arr[i+1];
    Arr[i+1] = Arr[high];
    Arr[high] = b;

    return (i + 1) 
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