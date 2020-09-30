// Bucket Sort
// Javascript
// Porter L

function bucketSort(Arr){
    console.log('bucket sort');
    var max_value = Math.max(...Arr);
    var size = max_value / Arr.length;
    var buckets_list = [];

    for (x = 0; x < Arr.length; x++){
        buckets_list.push([]);
    }

    for (y = 0; y < Arr.length; y++){
        var z = Math.floor(Arr[y] / size);
        if (z != Arr.length){
            buckets_list[z].push(Arr[y]);
        }
        else{
            buckets_list[Arr.length - 1].push(Arr[y]);
        }
    }

    for (z = 0; z < Arr.length; z++){
        insertionSort(buckets_list[z]);
    }

    var Arr_out = [];
    for (x = 0; x < Arr.length; x++){
        Arr_out = Arr_out.concat(...buckets_list[x]);
    }
    return Arr_out
}