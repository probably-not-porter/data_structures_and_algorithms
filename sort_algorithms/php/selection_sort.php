<?php
// Selection Sort
// PHP
// Porter L

function selection_sort($Arr)
{
    for ($x = 0;$x < count($Arr);$x++){
        $min_index = $x;
        for ($y = $x + 1; $y < count($Arr); $y++){
            if ($Arr[$min_index] > $Arr[$y]){
                $min_index = $y;
            }
        }
        $b = $Arr[$x];
        $Arr[$x] = $Arr[$min_index];
        $Arr[$min_index] = $b; 
    }
    return $Arr;
}

// Example
$test_array = array(2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3);
echo "Original Array : ";
echo implode(', ',$test_array );
echo "\nSorted Array : ";
echo implode(', ',selection_Sort($test_array));
echo "\n";

?>