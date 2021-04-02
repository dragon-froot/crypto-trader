<?php
class CoinbaseExchange {
    public function __construct($key, $secret, $passphrase) {
        $this->key = $key;
        $this->secret = $secret;
        $this->passphrase = $passphrase;
    }

    public function signature($request_path='', $body='', $timestamp=false, $method='GET') {
        $body = is_array($body) ? json_encode($body) : $body;
        $timestamp = $timestamp ? $timestamp : time();

        $what = $timestamp.$method.$request_path.$body;

        return base64_encode(hash_hmac("sha256", $what, base64_decode($this->secret), true));
    }

    
}

$key = "dae17376e12d406d6f6e8ad04b0509c4";
$secret = "SMUVlOYhzwZQDAuYzcpAiOOJpPcqm0nWc+94MF/gS7ShfMBZw1HEATitGeIWvKX9ah8Fu7fnEeDYUzLJsN46iw==";
$pass = "fwl494yxb8g";
$test = new CoinBaseExchange($key, $secret, $pass);
echo $test->signature();