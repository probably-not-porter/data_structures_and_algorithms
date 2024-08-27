<?php
// Quick Sort
// PHP
// Porter L

function partition($Arr, $low, $high){
    $i = $low - 1;
    $pivot = $Arr[$high];

    for ($j = $low; $j < $high; $j++){
        if ($Arr < $pivot){
            $i++;
            $b = $Arr[$i];
            $Arr[$i] = $Arr[$j];
            $Arr[$j] = $Arr[$i];
        }
    }
    $b = $Arr[$i + 1];
    $Arr[$i + 1] = $Arr[$high];
    $Arr[$high] = $Arr[$i + 1];

    return ($i + 1);
}

function quickSort($Arr, $low, $high){
    if ($low < $high){
        $p = partition($Arr, $low, $high);
        quickSort($Arr, $low, $p - 1);
        quickSort($Arr, $p+1, $high);
    }
    return $Arr;
}

// Example
$test_array = array(2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3);
echo "Original Array : ";
echo implode(', ',$test_array );
echo "\nSorted Array : ";
echo implode(', ',quickSort($test_array, 0, count($test_array)));
echo "\n";

?>