<?php
header("Content-Type: application/json; charset=utf-8");
$T=$_GET["arg"]??null;

if (!$T) {
    echo json_encode(["hianyzik"],JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    return;
}

$array=[
    "x" => $x, 
    "y" => $y,
];

$json = json_encode($array, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
echo $json;
?>
