Lets do it...
<?php 

function HTTPPost($url, array $params) {
    $query = http_build_query($params);
    $ch    = curl_init();
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $query);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

$params = array();
$params['merchant_id'] = '<type your merchant_id>';
$params['access_key'] = '<type your access_key>';
$params['contract_number'] = '<type your contract_number>';
$params['return_url'] = 'http://101e98f8.ngrok.io/return_url';
$params['cancel_url'] = 'http://101e98f8.ngrok.io/cancel_url';
$params['notification_url'] = 'http://101e98f8.ngrok.io/notification_url';
$params['amount'] = 100;
$params['reference'] = 'my_reference'; 

$response = HTTPPost('http://101e98f8.ngrok.io/do_web_payment', $params);
$result = json_decode($response, true);

echo '<pre>';
var_dump($response);
echo '</pre>';

echo '<pre>';
var_dump($result);
echo '</pre>';

echo $result['result'];

echo $result['result']['code'];
