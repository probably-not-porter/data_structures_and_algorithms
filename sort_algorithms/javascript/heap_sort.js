// Heap Sort
// Javascript
// Porter L

function heapify(Arr, x, y){
    let largest = y;
    let left = 2 * y + 1;
    let right = 2 * y + 2;

    if (left < x && Arr[y] < Arr[left]){
        largest = left;
    }

    if (right < x && Arr[largest] < Arr[right]){
        largest = right
    }

    if (largest != y){
        let tmp = Arr[y];
        Arr[y] = Arr[largest];
        Arr[largest] = tmp

        heapify(Arr, x, largest);
    }

    return Arr
}

function heapSort(Arr){
    let x = Arr.length;

    for (let y = Math.floor(x / 2) - 1; y > -1; y--){
        heapify(Arr, x, y);
    }

    for (let y = x-1; y > 0; y--){
        let tmp = Arr[y];
        Arr[y] = Arr[0];
        Arr[0] = tmp

        heapify(Arr, y, 0)
    }

    return Arr
}